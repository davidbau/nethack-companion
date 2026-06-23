#!/usr/bin/env python3
"""Derive a per-symbol corpse/eating classification from the NetHack 5.0 source.

Reads include/monsters.h, applies the eat-safety predicates from
include/mondata.h and src/eat.c, and prints a per-symbol summary: the modal
("general") verdict for each ASCII class, plus the monsters that deviate from
it (the rows that must be broken out).

Source of truth only; no hand-entered monster data.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "nethack-c" / "upstream"
MONSTERS_H = ROOT / "include" / "monsters.h"

# cpostfx() specials (src/eat.c:1129+): PM bareword -> short effect note.
# These are the deviations that aren't derivable from flags alone.
CPOSTFX = {
    "WRAITH": "gain a level",
    "HUMAN_WERERAT": "lycanthropy",
    "HUMAN_WEREJACKAL": "lycanthropy",
    "HUMAN_WEREWOLF": "lycanthropy",
    "NURSE": "full heal",
    "STALKER": "invisibility + see invisible",
    "YELLOW_LIGHT": "stun",
    "GIANT_BAT": "stun",
    "BAT": "stun",
    "GIANT_MIMIC": "stick in place (mimic gold)",
    "LARGE_MIMIC": "stick in place (mimic gold)",
    "SMALL_MIMIC": "stick in place (mimic gold)",
    "QUANTUM_MECHANIC": "toggles Speed",
    "LIZARD": "cures stoning; never rots",
    "LICHEN": "never rots",
    "CHAMELEON": "random polymorph",
    "DOPPELGANGER": "random polymorph",
    "GENETIC_ENGINEER": "random polymorph",
    "MIND_FLAYER": "+Int, telepathy",
    "MASTER_MIND_FLAYER": "+Int, telepathy",
    "GREEN_SLIME": "turn to slime (death)",
    "DEATH": "no effect (Rider)",
    "FAMINE": "no effect (Rider)",
    "PESTILENCE": "no effect (Rider)",
    "DISENCHANTER": "strips a random intrinsic",
    "TENGU": "teleportitis + teleport control",
    "NEWT": "may restore a little Pw",
    "DISPLACER_BEAST": "displacement (temporary)",
    "VIOLET_FUNGUS": "hallucination",
}

# MR_* conveyed-resistance bit -> intrinsic label (intrinsic_possible, eat.c:903)
MR_INTRINSIC = {
    "MR_FIRE": "fire res",
    "MR_COLD": "cold res",
    "MR_SLEEP": "sleep res",
    "MR_DISINT": "disint res",
    "MR_ELEC": "shock res",
    "MR_POISON": "poison res",
    "MR_ACID": "acid res*",   # temporary
    "MR_STONE": "stone res*", # temporary
}

def split_top(args):
    """Split a comma-separated arg string at top-level (paren-aware)."""
    out, depth, cur = [], 0, ""
    for ch in args:
        if ch == "(":
            depth += 1; cur += ch
        elif ch == ")":
            depth -= 1; cur += ch
        elif ch == "," and depth == 0:
            out.append(cur.strip()); cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out

def grab_mon_blocks(text):
    """Yield the argument string inside each MON( ... ) invocation."""
    i = 0
    while True:
        m = re.search(r"\bMON\s*\(", text[i:])
        if not m:
            return
        start = i + m.end()
        depth, j = 1, start
        while depth:
            if text[j] == "(":
                depth += 1
            elif text[j] == ")":
                depth -= 1
            j += 1
        yield text[start:j-1]
        i = j

def parse():
    text = MONSTERS_H.read_text()
    # strip // and /* */ comments so they don't confuse the parser
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"//[^\n]*", "", text)
    mons = []
    for block in grab_mon_blocks(text):
        a = split_top(block)
        if len(a) < 14:
            continue
        nam = a[0]
        mname = re.search(r'NAM\("([^"]*)"\)', nam) or re.search(r'"([^"]*)"', nam)
        name = mname.group(1) if mname else nam
        sym = a[1]
        siz = split_top(re.search(r"SIZ\((.*)\)", a[5]).group(1)) if a[5].startswith("SIZ") else ["0","0"]
        cwt, cnutrit = siz[0], siz[1]
        mconveys = a[7]
        flg1 = a[8]
        flg2 = a[9]
        geno = a[3]
        pm = a[13]
        mons.append(dict(name=name, sym=sym, cwt=cwt, cnutrit=cnutrit,
                         mconveys=mconveys, flg1=flg1, flg2=flg2, geno=geno, pm=pm))
    return mons

def verdict(m):
    """Return (risk, benefit) short strings for one monster."""
    f, conv, pm = m["flg1"], m["mconveys"], m["pm"]
    # Puddings & oozes are G_NOCORPSE but leave edible globs; everything else
    # with G_NOCORPSE truly leaves nothing.
    if "G_NOCORPSE" in m["geno"] and m["sym"] != "S_PUDDING":
        return ("NO CORPSE", "")
    risks, benefits = [], []
    if pm in ("COCKATRICE", "CHICKATRICE", "MEDUSA"):
        risks.append("PETRIFY (death)")
    if "M1_POIS" in f:
        risks.append("poisonous")
    if "M1_ACID" in f:
        risks.append("acidic")
    if "M2_GIANT" in m["flg2"]:
        benefits.append("+Str")
    if pm in CPOSTFX:
        note = CPOSTFX[pm]
        (risks if ("death" in note or "lycanthropy" in note or "stun" in note
                   or "stick" in note or "slime" in note or "polymorph" in note
                   or "toggles" in note or "strips" in note
                   or "hallucination" in note) else benefits).append(note)
    for bit, lab in MR_INTRINSIC.items():
        if bit in conv:
            benefits.append(lab)
    if pm in ("FLOATING_EYE",):
        benefits.append("telepathy")
    return (", ".join(risks), ", ".join(benefits))

# S_* (sans prefix) -> (glyph, friendly name), matching the book's Bestiary.
SYM = {
    "ANGEL": ("A", "Angels & celestials"), "ANT": ("a", "Ants & insects"),
    "BAT": ("B", "Bats & birds"), "BLOB": ("b", "Blobs"),
    "CENTAUR": ("C", "Centaurs"), "COCKATRICE": ("c", "Cockatrices"),
    "DEMON": ("&", "Major demons"), "DOG": ("d", "Dogs & canines"),
    "DRAGON": ("D", "Dragons"), "EEL": (";", "Eels & sea monsters"),
    "ELEMENTAL": ("E", "Elementals"), "EYE": ("e", "Eyes & spheres"),
    "FELINE": ("f", "Cats"), "FUNGUS": ("F", "Fungi & molds"),
    "GHOST": (" ", "Ghosts & shades"), "GIANT": ("H", "Giants & titans"),
    "GNOME": ("G", "Gnomes"), "GOLEM": ("'", "Golems"),
    "GREMLIN": ("g", "Gremlins & gargoyles"), "HUMAN": ("@", "Humans & elves"),
    "HUMANOID": ("h", "Dwarves & humanoids"), "IMP": ("i", "Imps & minor demons"),
    "JABBERWOCK": ("J", "Jabberwocks"), "JELLY": ("j", "Jellies"),
    "KOBOLD": ("k", "Kobolds"), "KOP": ("K", "Keystone Kops"),
    "LEPRECHAUN": ("l", "Leprechauns"), "LICH": ("L", "Liches"),
    "LIGHT": ("y", "Lights"), "LIZARD": (":", "Lizards"),
    "MIMIC": ("m", "Mimics"), "MUMMY": ("M", "Mummies"),
    "NAGA": ("N", "Nagas"), "NYMPH": ("n", "Nymphs"),
    "OGRE": ("O", "Ogres"), "ORC": ("o", "Orcs"),
    "PIERCER": ("p", "Piercers"), "PUDDING": ("P", "Puddings & oozes"),
    "QUADRUPED": ("q", "Quadrupeds"), "QUANTMECH": ("Q", "Quantum mechanics"),
    "RODENT": ("r", "Rodents"), "RUSTMONST": ("R", "Rust monsters & disenchanters"),
    "SNAKE": ("S", "Snakes"), "SPIDER": ("s", "Arachnids & centipedes"),
    "TRAPPER": ("t", "Trappers & lurkers"), "TROLL": ("T", "Trolls"),
    "UMBER": ("U", "Umber hulks"), "UNICORN": ("u", "Unicorns & horses"),
    "VAMPIRE": ("V", "Vampires"), "VORTEX": ("v", "Vortices"),
    "WORM": ("w", "Worms"), "WRAITH": ("W", "Wraiths"),
    "XAN": ("x", "Xans & fantastic insects"), "XORN": ("X", "Xorns"),
    "YETI": ("Y", "Apelike creatures"), "ZOMBIE": ("Z", "Zombies"),
    "ZRUTY": ("z", "Zruties"),
}

def gen_text(sig):
    r, b = sig
    if r == "NO CORPSE":
        return "No corpse — nothing to eat."
    if "PETRIFY" in r:
        return "**Never eat — petrifies (death).**"
    if r and b:
        return f"{r.capitalize()}; eat for {b}."
    if r:
        return f"{r.capitalize()}."
    if b:
        return f"Eat for {b}."
    return "Plain food."

def emit_md():
    mons = parse()
    bysym = {}
    for m in mons:
        key = m["sym"].replace("S_", "")
        if key not in SYM:
            continue
        bysym.setdefault(key, []).append(m)
    print("| Sym | Class | Eating verdict |")
    print("|----|-------|----------------|")
    for key in sorted(bysym, key=lambda k: SYM[k][1].lower()):
        glyph, name = SYM[key]
        rows = bysym[key]
        sigs = {}
        for m in rows:
            sigs.setdefault(verdict(m), []).append(m["name"])
        modal = max(sigs, key=lambda s: len(sigs[s]))
        verdict_txt = gen_text(modal)
        devs = []
        for sig, names in sigs.items():
            if sig == modal:
                continue
            nm = ", ".join(f"*{n}*" for n in names)
            devs.append(f"{nm} {gen_text(sig).rstrip('.').lower()}")
        if devs:
            verdict_txt += " " + "; ".join(devs) + "."
        g = "` `" if glyph == " " else f"`{glyph}`"
        print(f"| {g} | {name} | {verdict_txt} |")

def main():
    if "--md" in sys.argv:
        emit_md()
        return
    mons = parse()
    bysym = {}
    for m in mons:
        bysym.setdefault(m["sym"], []).append(m)
    for sym in sorted(bysym):
        rows = bysym[sym]
        sigs = {}
        for m in rows:
            r, b = verdict(m)
            sig = (r, b)
            sigs.setdefault(sig, []).append(m["name"])
        print(f"\n=== {sym}  ({len(rows)} monsters) ===")
        # modal signature = the general verdict
        modal = max(sigs, key=lambda s: len(sigs[s]))
        for sig, names in sorted(sigs.items(), key=lambda kv: -len(kv[1])):
            tag = "GENERAL" if sig == modal else "deviant"
            r, b = sig
            desc = " | ".join(x for x in (("risk: "+r) if r else "", ("eat: "+b) if b else "") if x) or "plain food"
            print(f"  [{tag}] {desc}")
            print(f"        {', '.join(names)}")

if __name__ == "__main__":
    main()
