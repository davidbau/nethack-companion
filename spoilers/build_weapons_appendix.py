#!/usr/bin/env python3
"""Parse objects.h + weapon.c and emit the Weapons Appendix markdown."""
import re
from pathlib import Path

OBJ = Path('/Users/davidbau/git/mazesofmenace/teleport/maud/nethack-c/upstream/include/objects.h').read_text()
WEAP = Path('/Users/davidbau/git/mazesofmenace/teleport/maud/nethack-c/upstream/src/weapon.c').read_text()

# Extra damage from dmgval in weapon.c
SDAM_PLUS = {  # vs small target
    'IRON_CHAIN', 'CROSSBOW_BOLT', 'MACE', 'SILVER_MACE', 'WAR_HAMMER',
    'FLAIL', 'SPETUM', 'TRIDENT',
}
SDAM_D4 = {
    'BATTLE_AXE', 'BARDICHE', 'BILL_GUISARME', 'GUISARME', 'LUCERN_HAMMER',
    'MORNING_STAR', 'RANSEUR', 'BROADSWORD', 'ELVEN_BROADSWORD', 'RUNESWORD',
    'VOULGE',
}
LDAM_PLUS = {
    'IRON_CHAIN', 'CROSSBOW_BOLT', 'MORNING_STAR', 'PARTISAN', 'RUNESWORD',
    'ELVEN_BROADSWORD', 'BROADSWORD',
}
LDAM_D4 = {'FLAIL', 'RANSEUR', 'VOULGE'}
LDAM_D6 = {'HALBERD', 'SPETUM'}
LDAM_2D4 = {'BATTLE_AXE', 'BARDICHE', 'TRIDENT'}
LDAM_2D6 = {'TSURUGI', 'DWARVISH_MATTOCK', 'TWO_HANDED_SWORD'}

SKILL_NAMES = {
    'P_DAGGER': 'Dagger', 'P_KNIFE': 'Knife', 'P_AXE': 'Axe',
    'P_PICK_AXE': 'Pick-axe', 'P_SHORT_SWORD': 'Short sword',
    'P_BROAD_SWORD': 'Broadsword', 'P_LONG_SWORD': 'Long sword',
    'P_TWO_HANDED_SWORD': 'Two-handed sword', 'P_SABER': 'Saber',
    'P_CLUB': 'Club', 'P_MACE': 'Mace', 'P_MORNING_STAR': 'Morning star',
    'P_FLAIL': 'Flail', 'P_HAMMER': 'Hammer',
    'P_QUARTERSTAFF': 'Quarterstaff', 'P_POLEARMS': 'Polearms',
    'P_SPEAR': 'Spear', 'P_TRIDENT': 'Trident', 'P_LANCE': 'Lance',
    'P_BOW': 'Bow', 'P_SLING': 'Sling', 'P_CROSSBOW': 'Crossbow',
    'P_DART': 'Dart', 'P_SHURIKEN': 'Shuriken',
    'P_BOOMERANG': 'Boomerang', 'P_WHIP': 'Whip',
    'P_UNICORN_HORN': 'Unicorn horn',
}

# Parse WEAPON(...) entries
def parse_macro(text, name):
    pattern = re.compile(
        rf'{name}\("([^"]+)",\s*(?:"([^"]+)"|NoDes)\s*,\s*([^)]+?)\)',
        re.DOTALL)
    out = []
    for m in pattern.finditer(text):
        wname = m.group(1)
        desc = m.group(2) or ''
        args = m.group(3)
        args = re.sub(r'\s+', ' ', args).strip()
        args = re.sub(r'/\*.*?\*/', '', args)  # remove inline comments
        # Split by comma, but careful — sub field might have `|`
        parts = [p.strip() for p in args.split(',')]
        out.append((wname, desc, parts))
    return out

weapons = parse_macro(OBJ, 'WEAPON')
projectiles = parse_macro(OBJ, 'PROJECTILE')
bows = parse_macro(OBJ, 'BOW')

# WEAPON signature: name, desc, kn, mg, bi, prob, wt, cost, sdam, ldam, hitbon, typ, sub, metal, color, sn
def parse_weapon(name, parts):
    fields = {
        'kn': parts[0], 'mg': parts[1], 'bi': parts[2],
        'prob': parts[3], 'wt': parts[4], 'cost': parts[5],
        'sdam': parts[6], 'ldam': parts[7], 'hitbon': parts[8],
        'typ': parts[9], 'sub': parts[10], 'metal': parts[11],
        'color': parts[12] if len(parts) > 12 else '', 'sn': parts[13] if len(parts) > 13 else '',
    }
    return fields

def parse_projectile(name, parts):
    # PROJECTILE: kn, prob, wt, cost, sdam, ldam, hitbon, metal, sub, color, sn
    return {
        'kn': parts[0], 'prob': parts[1], 'wt': parts[2], 'cost': parts[3],
        'sdam': parts[4], 'ldam': parts[5], 'hitbon': parts[6],
        'metal': parts[7], 'sub': parts[8], 'color': parts[9],
        'sn': parts[10] if len(parts) > 10 else '',
        'bi': '0',
    }

def parse_bow(name, parts):
    # BOW: kn, prob, wt, cost, hitbon, metal, sub, color, sn
    return {
        'kn': parts[0], 'prob': parts[1], 'wt': parts[2], 'cost': parts[3],
        'hitbon': parts[4], 'metal': parts[5], 'sub': parts[6],
        'color': parts[7], 'sn': parts[8] if len(parts) > 8 else '',
        'sdam': '2', 'ldam': '2',
        'bi': '0',  # bows are one-handed
    }

# Build (name, fields, weapon-type) tuples
all_weapons = []
for n, d, parts in weapons:
    all_weapons.append((n, d, parse_weapon(n, parts), 'WEAPON'))
for n, d, parts in projectiles:
    all_weapons.append((n, d, parse_projectile(n, parts), 'PROJECTILE'))
for n, d, parts in bows:
    all_weapons.append((n, d, parse_bow(n, parts), 'BOW'))

# Helper: format damage with extra
def fmt_damage(sn, sdam, ldam, hitbon, kind):
    if kind == 'BOW':
        return '—'  # bows themselves do 1d2 / 1d2; their projectiles do real dmg
    sdam = int(sdam)
    ldam = int(ldam)
    s_str = f'1d{sdam}' if sdam > 1 else '1'
    l_str = f'1d{ldam}' if ldam > 1 else '1'
    if sn in SDAM_PLUS: s_str += '+1'
    elif sn in SDAM_D4: s_str += '+1d4'
    if sn in LDAM_PLUS: l_str += '+1'
    elif sn in LDAM_D4: l_str += '+1d4'
    elif sn in LDAM_D6: l_str += '+1d6'
    elif sn in LDAM_2D4: l_str += '+2d4'
    elif sn in LDAM_2D6: l_str += '+2d6'
    return f'{s_str} / {l_str}'

def fmt_skill(sub):
    sub = sub.strip().lstrip('-')
    return SKILL_NAMES.get(sub, sub)

def fmt_material(metal):
    return {
        'IRON': 'iron', 'WOOD': 'wood', 'METAL': 'metal', 'SILVER': 'silver',
        'COPPER': 'copper', 'GOLD': 'gold', 'GLASS': 'glass', 'BONE': 'bone',
        'LEATHER': 'leather', 'CLOTH': 'cloth', 'PLASTIC': 'plastic',
        'MINERAL': 'stone',
    }.get(metal.strip(), metal.strip().lower())

# Group by skill class
groups = {}
for name, desc, f, kind in all_weapons:
    skill = fmt_skill(f.get('sub', ''))
    groups.setdefault(skill, []).append((name, desc, f, kind))

# Order
SKILL_ORDER = [
    'Dagger', 'Knife', 'Short sword', 'Saber', 'Broadsword',
    'Long sword', 'Two-handed sword', 'Axe', 'Pick-axe',
    'Club', 'Mace', 'Morning star', 'Flail', 'Hammer',
    'Quarterstaff', 'Polearms', 'Spear', 'Trident', 'Lance',
    'Whip', 'Bow', 'Crossbow', 'Sling', 'Dart', 'Shuriken',
    'Boomerang',
]

# Notes — one-line annotation for interesting rows
NOTES = {
    'long sword': "Dip at experience level 5+ in a fountain for a 1-in-30 chance at Excalibur (1-in-6 for Knights).",
    'two-handed sword': "Two-handed (no shield). Vorpal Blade is the artifact form.",
    'mace': "The Priest's first sacrifice gift, Demonbane, is a +d4/+0 silver mace.",
    'silver mace': "Bonus damage to demons, undead, and shape-changers.",
    'silver dagger': "Silver damage to demons. Common Rogue/Ranger off-hand.",
    'silver saber': "Werebane is the artifact form — silver damage to weres and demons.",
    'silver arrow': "Silver damage to demons and weres.",
    'silver spear': "Silver damage to demons and weres.",
    'long sword': "Dip in a fountain at XL5+ for Excalibur (1-in-30; 1-in-6 for Lawful Knights).",
    'dagger': "Stackable; Rogues multishot up to three in a single throw.",
    'battle-axe': "Two-handed; +1d4 small, +2d4 large.",
    'elven dagger': "Stackable. Sting is the artifact form.",
    'orcish dagger': "Stackable.",
    'short sword': "The Rogue's starter.",
    'katana': "+1 to-hit baked in. Snickersnee is the artifact form.",
    'lance': "Devastating from horseback (jousting bonus); useless on foot.",
    'tsurugi': "Two-handed. The Tsurugi of Muramasa is the artifact form.",
    'club': "What a Caveman starts with — basic but free of curses early.",
    'quarterstaff': "Two-handed but light; the Wizard's starting weapon.",
    'aklys': "Returns when thrown if Strength is high enough.",
    'boomerang': "Returns when thrown. Always.",
    'bullwhip': "The Archeologist's starter; can disarm a monster.",
    'crysknife': "Polymorphs back to a worm tooth when dropped; keep it equipped or buried.",
    'athame': "Used for engraving wards — Elbereth on the floor lasts longer engraved with an athame.",
    'sling': "Trains sling skill from any rock you pick up.",
    'crossbow': "Bolts pierce — and crossbows fire one shot per turn at most.",
    'yumi': "The Samurai's bow.",
    'unicorn horn': "Doubles as a cure-everything tool when applied (unicorn horn use, not weapon).",
    'pick-axe': "Doubles as a digging tool; an Archeologist's quiet superpower.",
    'dwarvish mattock': "Two-handed. Digs through walls; cannot two-weapon.",
    'morning star': "+1d4 small, +1 large — punches above its weight for a one-hander.",
    'trident': "+1 small, +2d4 large — the giant-killer; one-handed.",
    'war hammer': "Mjollnir is the artifact form (Neutral Valkyrie sacrifice gift).",
    'broadsword': "+d4 small, +1 large. Stormbringer is the chaotic-aligned artifact form.",
    'partisan': "Polearm; reach (attacks 2 squares away).",
    'halberd': "Polearm; +1d6 large.",
    'bardiche': "Polearm; +1d4 small, +2d4 large.",
    'glaive': "Polearm; reach.",
    'ranseur': "Polearm; +1d4 small, +1d4 large.",
    'spetum': "Polearm; +1 small, +1d6 large.",
    'voulge': "Polearm; +1d4 small, +1d4 large.",
    'guisarme': "Polearm; +1d4 small.",
    'bill-guisarme': "Polearm; +1d4 small.",
    'fauchard': "Polearm; reach.",
    'lucern hammer': "Polearm; +1d4 small.",
    'bec de corbin': "Polearm; reach.",
    'flail': "+1d4 large; one-handed.",
    'rubber hose': "Joke weapon (1d4 / 1d3). Damages even Shades, who are immune to most.",
}

# Pre-clean for lookup (lowercase name → note)
def get_note(name):
    return NOTES.get(name.lower(), '')

# Generate markdown
out = []
out.append('### Weapons')
out.append('')
out.append("Damage is shown as **vs small / vs large**, the dice rolled before "
           "enchantment and excluding silver/material bonuses. **Wt** is unit weight; "
           "**Cost** is the unenchanted shop base price in zorkmids. **Hit** is the "
           "to-hit bonus baked into the weapon itself (most are 0). Two-handed "
           "weapons that prevent shield use and two-weapon combat are flagged in "
           "the notes. Weapons are grouped by their skill class so you can see your "
           "options within each skill tree at a glance.")
out.append('')

# Section-level prose (printed BEFORE the table) for groups where the
# whole class deserves a heading paragraph. Keeps the notes column from
# carrying the same "polearm; reach" boilerplate on every row.
SECTION_PROSE = {
    'Polearms': (
        "All polearms are two-handed and have a reach of two squares "
        "(`#apply` the weapon to strike a target one tile away from "
        "you, with one empty intervening square). They can't be used "
        "in melee against an adjacent monster — the haft gets in the "
        "way — which means you switch weapons or use the polearm's "
        "reach attack, not both. Notes below describe each entry's "
        "extra damage; the reach mechanic is identical across the "
        "class."
    ),
}

# Drop per-row "Polearm; …" boilerplate; just keep the extra-damage
# part since reach is now in the section prose.
POLEARM_NOTE_STRIP = {
    'partisan': "Reach.",
    'halberd': "+1d6 large.",
    'bardiche': "+1d4 small, +2d4 large.",
    'glaive': "Reach.",
    'ranseur': "+1d4 small, +1d4 large.",
    'spetum': "+1 small, +1d6 large.",
    'voulge': "+1d4 small, +1d4 large.",
    'guisarme': "+1d4 small.",
    'bill-guisarme': "+1d4 small.",
    'fauchard': "Reach.",
    'lucern hammer': "+1d4 small.",
    'bec de corbin': "Reach.",
}
for name, replacement in POLEARM_NOTE_STRIP.items():
    NOTES[name] = replacement

for skill in SKILL_ORDER:
    if skill not in groups:
        continue
    items = groups[skill]
    out.append(f'#### {skill}')
    out.append('')
    if skill in SECTION_PROSE:
        out.append(SECTION_PROSE[skill])
        out.append('')
    out.append('<div class="dense-table">')
    out.append('')
    # Lopsided dash widths in the separator tell pandoc to give the
    # Notes column a much wider rendered column than the numeric ones.
    out.append('| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |')
    out.append('|--------|--------------|----|------|-----|----------|--------------------------------------------------------------------|')
    for name, desc, f, kind in items:
        sn = f.get('sn', '').strip()
        dmg = fmt_damage(sn, f['sdam'], f['ldam'], f.get('hitbon', '0'), kind)
        wt = f['wt']
        cost = f['cost']
        hit = f.get('hitbon', '0')
        hit_str = f'+{hit}' if int(hit) > 0 else '—'
        mat = fmt_material(f.get('metal', ''))
        note = get_note(name)
        out.append(f'| {name} | {dmg} | {wt} | {cost} | {hit_str} | {mat} | {note} |')
    out.append('')
    out.append('</div>')
    out.append('')

print('\n'.join(out))
