#!/usr/bin/env python3
"""Parse monsters.h and emit raw Bestiary Appendix markdown.

The appendix in companion.md has hand-reviewed tactical prose and notes.  This
extractor is useful for checking its source-derived rows, but its output is not
a drop-in replacement for the curated appendix.
"""
import re
from pathlib import Path

UPSTREAM = Path(__file__).resolve().parent.parent / 'nethack-c' / 'upstream'
if not (UPSTREAM / 'include' / 'monsters.h').exists():
    raise SystemExit(
        f"NetHack source not found at {UPSTREAM}. Run ./setup.sh "
        "to initialize the submodule.")
TEXT = (UPSTREAM / 'include' / 'monsters.h').read_text()
# Strip preprocessor noise
TEXT = re.sub(r'#if 0[\s\S]*?#endif', '', TEXT)
TEXT = re.sub(r'#ifdef CHARON[\s\S]*?#endif', '', TEXT)

# --- Glyph + symbol mapping ----------------------------------------
SYM_TO_CHAR = {
    'S_ANT': ('a', "Ants and insects"),
    'S_BLOB': ('b', "Blobs"),
    'S_COCKATRICE': ('c', "Cockatrices"),
    'S_DOG': ('d', "Dogs and canines"),
    'S_EYE': ('e', "Eyes and spheres"),
    'S_FELINE': ('f', "Felines"),
    'S_GREMLIN': ('g', "Gremlins"),
    'S_HUMANOID': ('h', "Humanoids"),
    'S_IMP': ('i', "Imps and minor demons"),
    'S_JELLY': ('j', "Jellies"),
    'S_KOBOLD': ('k', "Kobolds"),
    'S_LEPRECHAUN': ('l', "Leprechauns"),
    'S_MIMIC': ('m', "Mimics"),
    'S_NYMPH': ('n', "Nymphs"),
    'S_ORC': ('o', "Orcs"),
    'S_PIERCER': ('p', "Piercers"),
    'S_QUADRUPED': ('q', "Quadrupeds"),
    'S_RODENT': ('r', "Rodents"),
    'S_SPIDER': ('s', "Arachnids and centipedes"),
    'S_TRAPPER': ('t', "Trappers and lurkers"),
    'S_UNICORN': ('u', "Unicorns and horses"),
    'S_VORTEX': ('v', "Vortices"),
    'S_WORM': ('w', "Worms"),
    'S_XAN': ('x', "Xans and fantastic insects"),
    'S_LIGHT': ('y', "Lights"),
    'S_ZRUTY': ('z', "Zruties"),
    'S_ANGEL': ('A', "Angelic beings"),
    'S_BAT': ('B', "Bats and birds"),
    'S_CENTAUR': ('C', "Centaurs"),
    'S_DRAGON': ('D', "Dragons"),
    'S_ELEMENTAL': ('E', "Elementals"),
    'S_FUNGUS': ('F', "Fungi and molds"),
    'S_GNOME': ('G', "Gnomes"),
    'S_GIANT': ('H', "Giant humanoids"),
    'S_invisible': ('I', "Invisible monsters"),
    'S_JABBERWOCK': ('J', "Jabberwocks"),
    'S_KOP': ('K', "Keystone Kops"),
    'S_LICH': ('L', "Liches"),
    'S_MUMMY': ('M', "Mummies"),
    'S_NAGA': ('N', "Nagas"),
    'S_OGRE': ('O', "Ogres"),
    'S_PUDDING': ('P', "Puddings and oozes"),
    'S_QUANTMECH': ('Q', "Quantum mechanics"),
    'S_RUSTMONST': ('R', "Rust monsters and disenchanters"),
    'S_SNAKE': ('S', "Snakes"),
    'S_TROLL': ('T', "Trolls"),
    'S_UMBER': ('U', "Umber hulks"),
    'S_VAMPIRE': ('V', "Vampires"),
    'S_WRAITH': ('W', "Wraiths"),
    'S_XORN': ('X', "Xorns"),
    'S_YETI': ('Y', "Apelike creatures"),
    'S_ZOMBIE': ('Z', "Zombies"),
    'S_HUMAN': ('@', "Humans and elves"),
    'S_GHOST': (' ', "Ghosts"),
    'S_GOLEM': ("'", "Golems"),
    'S_DEMON': ('&', "Major demons"),
    'S_EEL': (';', "Sea monsters"),
    'S_LIZARD': (':', "Lizards"),
    'S_WORM_TAIL': ('~', "Long-worm tails"),
    'S_MIMIC_DEF': (']', "Mimic objects"),
}

# Symbol order: lowercase a-z, then uppercase A-Z, then specials
SYM_ORDER = [
    'S_ANT', 'S_BLOB', 'S_COCKATRICE', 'S_DOG', 'S_EYE', 'S_FELINE',
    'S_GREMLIN', 'S_HUMANOID', 'S_IMP', 'S_JELLY', 'S_KOBOLD',
    'S_LEPRECHAUN', 'S_MIMIC', 'S_NYMPH', 'S_ORC', 'S_PIERCER',
    'S_QUADRUPED', 'S_RODENT', 'S_SPIDER', 'S_TRAPPER', 'S_UNICORN',
    'S_VORTEX', 'S_WORM', 'S_XAN', 'S_LIGHT', 'S_ZRUTY',
    'S_ANGEL', 'S_BAT', 'S_CENTAUR', 'S_DRAGON', 'S_ELEMENTAL',
    'S_FUNGUS', 'S_GNOME', 'S_GIANT', 'S_invisible', 'S_JABBERWOCK',
    'S_KOP', 'S_LICH', 'S_MUMMY', 'S_NAGA', 'S_OGRE', 'S_PUDDING',
    'S_QUANTMECH', 'S_RUSTMONST', 'S_SNAKE', 'S_TROLL', 'S_UMBER',
    'S_VAMPIRE', 'S_WRAITH', 'S_XORN', 'S_YETI', 'S_ZOMBIE',
    'S_HUMAN', 'S_DEMON', 'S_GOLEM', 'S_EEL', 'S_LIZARD',
]

# --- Attack type / damage type names ---
AT_NAMES = {
    'AT_NONE': 'passive', 'AT_CLAW': 'claw', 'AT_BITE': 'bite',
    'AT_KICK': 'kick', 'AT_BUTT': 'butt', 'AT_TUCH': 'touch',
    'AT_STNG': 'sting', 'AT_HUGS': 'hug', 'AT_SPIT': 'spit',
    'AT_ENGL': 'engulf', 'AT_BREA': 'breath', 'AT_EXPL': 'explode',
    'AT_BOOM': 'death-burst', 'AT_GAZE': 'gaze', 'AT_TENT': 'tentacle',
    'AT_WEAP': 'weapon', 'AT_MAGC': 'cast',
}
AD_NAMES = {
    'AD_PHYS': '', 'AD_MAGM': 'magic', 'AD_FIRE': 'fire',
    'AD_COLD': 'cold', 'AD_SLEE': 'sleep', 'AD_DISN': 'disint',
    'AD_ELEC': 'shock', 'AD_DRST': 'drain-Str', 'AD_ACID': 'acid',
    'AD_BLND': 'blind', 'AD_STUN': 'stun', 'AD_SLOW': 'slow',
    'AD_PLYS': 'paralyse', 'AD_DRLI': 'drain-XL', 'AD_DREN': 'drain-Pw',
    'AD_LEGS': 'leg-wound', 'AD_STON': 'petrify',
    'AD_STCK': 'sticky', 'AD_SGLD': 'steal-gold',
    'AD_SITM': 'steal-item', 'AD_SEDU': 'seduce',
    'AD_TLPT': 'teleport', 'AD_RUST': 'rust', 'AD_CONF': 'confuse',
    'AD_DGST': 'digest', 'AD_HEAL': 'heal', 'AD_WRAP': 'wrap',
    'AD_WERE': 'lyc', 'AD_DRDX': 'drain-Dx',
    'AD_DRCO': 'drain-Co', 'AD_DRIN': 'drain-Int',
    'AD_DISE': 'disease', 'AD_DCAY': 'decay',
    'AD_SSEX': 'seduce', 'AD_HALU': 'hallu',
    'AD_DETH': 'death', 'AD_PEST': 'pestilence',
    'AD_FAMN': 'famine', 'AD_SLIM': 'slime',
    'AD_ENCH': 'disenchant', 'AD_CORR': 'corrode',
    'AD_POLY': 'polymorph', 'AD_CLRC': 'cleric',
    'AD_SPEL': 'spell', 'AD_RBRE': 'rnd-breath',
    'AD_SAMU': 'steal-amulet', 'AD_CURS': 'curse',
}

# Resistance bits (MR_*)
MR_FLAGS = {
    'MR_FIRE': 'fire-res',
    'MR_COLD': 'cold-res',
    'MR_SLEEP': 'sleep-res',
    'MR_DISINT': 'disint-res',
    'MR_ELEC': 'shock-res',
    'MR_POISON': 'pois-res',
    'MR_ACID': 'acid-res',
    'MR_STONE': 'ston-res',
}

# Key flags from M1/M2/M3 we'll surface. Discipline: only flags that
# change the player's combat or movement strategy. Flags that just
# affect XP bookkeeping (M2_NASTY), flavor sizing (M2_STRONG), or
# visibility-in-dark detection (M3_INFRAVISION) are omitted.
KEY_FLAGS = {
    'M1_FLY': 'flies',
    'M1_SWIM': 'swims',
    'M1_AMPHIBIOUS': 'amphibious',
    'M1_AMORPHOUS': 'amorphous',
    'M1_TUNNEL': 'tunnels',
    'M1_CONCEAL': 'hides',
    'M1_HIDE': 'hides',
    'M1_REGEN': 'regenerates',
    'M1_SEE_INVIS': 'sees-invis',
    'M1_TPORT': 'teleports',
    'M1_TPORT_CNTRL': 'teleport-control',
    'M1_POIS': 'poisonous-corpse',
    'M1_MINDLESS': 'mindless',
    'M2_UNDEAD': 'undead',
    'M2_DEMON': 'demonic',
    'M2_STALK': 'follows stairs',
    'M2_PEACEFUL': 'starts peaceful',
    'M2_DOMESTIC': 'tameable',
    'M2_SHAPESHIFTER': 'shapeshifter',
}

# Verb/predicate form for class-intro prose. Indexed by the short
# label used in KEY_FLAGS / MR_FLAGS values.
PROSE_FORM = {
    'flies': 'fly',
    'swims': 'swim',
    'amphibious': 'are amphibious',
    'amorphous': 'are amorphous',
    'tunnels': 'tunnel through walls',
    'hides': 'hide',
    'regenerates': 'regenerate',
    'sees-invis': 'see invisible',
    'teleports': 'teleport',
    'teleport-control': 'control where they teleport',
    'poisonous-corpse': 'have poisonous corpses',
    'mindless': 'are mindless',
    'undead': 'are undead',
    'demonic': 'are demons',
    'follows stairs': 'follow you up and down stairs',
    'starts peaceful': 'start peaceful',
    'tameable': 'are tameable by feeding',
    'shapeshifter': 'shapeshift',
    'fire-res': 'are fire-resistant',
    'cold-res': 'are cold-resistant',
    'sleep-res': 'are sleep-resistant',
    'disint-res': 'are disintegration-resistant',
    'shock-res': 'are shock-resistant',
    'pois-res': 'are poison-resistant',
    'acid-res': 'are acid-resistant',
    'ston-res': 'are petrification-resistant',
}

CLR_TO_NAME = {
    'CLR_BLACK': 'black', 'CLR_RED': 'red', 'CLR_GREEN': 'green',
    'CLR_BROWN': 'brown', 'CLR_BLUE': 'blue', 'CLR_MAGENTA': 'magenta',
    'CLR_CYAN': 'cyan', 'CLR_GRAY': 'gray', 'CLR_WHITE': 'white',
    'CLR_ORANGE': 'orange', 'CLR_BRIGHT_GREEN': 'bright-green',
    'CLR_YELLOW': 'yellow', 'CLR_BRIGHT_BLUE': 'bright-blue',
    'CLR_BRIGHT_MAGENTA': 'bright-magenta',
    'CLR_BRIGHT_CYAN': 'bright-cyan',
    'NO_COLOR': '—',
    'HI_DOMESTIC': 'white', 'HI_LORD': 'magenta', 'HI_GOLD': 'yellow',
    'HI_LEATHER': 'brown', 'HI_CLOTH': 'magenta', 'HI_SILVER': 'gray',
    'HI_COPPER': 'orange', 'HI_PAPER': 'white', 'HI_METAL': 'cyan',
    'HI_MINERAL': 'gray', 'HI_GLASS': 'cyan', 'HI_WOOD': 'brown',
    'DRAGON_SILVER': 'gray',
    'HI_ZAP': 'bright-blue', 'HI_NOIR': 'black',
}

# --- Parse monsters ---
# Each MON entry begins with `MON(NAM("name"), S_xxx,` ... and is multi-line
MON_RE = re.compile(
    r'MON\(NAMS?\(\s*"([^"]+)"(?:,\s*(?:"[^"]*"|\(const char \*\) 0)\s*,'
    r'\s*(?:"[^"]*"|\(const char \*\) 0))?\s*\),\s*(S_\w+),'
    r'([\s\S]*?)(?=\n\s+MON\(|\n\s*/\*|\n\s*\}\s*;)',
    re.MULTILINE)

ATTK_RE = re.compile(r'ATTK\(\s*(\w+),\s*(\w+),\s*(\d+),\s*(\d+)\s*\)')

def parse_mon(body):
    """Parse the tail of a MON() block after the symbol."""
    # LVL(lvl, mov, ac, mr, aln)
    lvl_m = re.search(r'LVL\(\s*(-?\d+),\s*(-?\d+),\s*(-?\d+),\s*(-?\d+),\s*(-?\d+)\s*\)', body)
    if not lvl_m:
        return None
    lvl, mov, ac, mr_pct, aln = (int(x) for x in lvl_m.groups())
    # G_* flags appear after LVL(...) inside parentheses
    gen_m = re.search(r'\),\s*\(?([^()]*G_\w+[^()]*)\)?,', body)
    gen = gen_m.group(1).strip() if gen_m else ''
    # Attacks
    atks = ATTK_RE.findall(body)
    # SIZ(wt, nut, snd, siz)
    siz_m = re.search(r'SIZ\(\s*(\d+),\s*(\d+),\s*(\w+),\s*(\w+)\s*\)', body)
    wt, nut, snd, siz = (siz_m.groups() if siz_m else ('?','?','?','?'))
    # Two resistance fields (mr1, mr2) come after SIZ
    after_siz = body[siz_m.end():] if siz_m else body
    # The first two comma-separated terms after SIZ are mr1 and mr2
    mr_match = re.match(r'\s*,\s*([^,]+?)\s*,\s*([^,]+?)\s*,', after_siz)
    mr1 = mr_match.group(1).strip() if mr_match else '0'
    mr2 = mr_match.group(2).strip() if mr_match else '0'
    # M1/M2/M3 flags — pull out all M[123]_* tokens that appear in the body
    m1_flags = set(re.findall(r'\bM1_\w+', body))
    m2_flags = set(re.findall(r'\bM2_\w+', body))
    m3_flags = set(re.findall(r'\bM3_\w+', body))
    # Difficulty (the comma-separated integer near the end)
    # Look for ',\s*(\d+),\s*(CLR|HI|NO|DRAGON)' style
    diff_m = re.search(r',\s*(\d+),\s*(CLR_\w+|HI_\w+|NO_COLOR|DRAGON_\w+),', body)
    diff = int(diff_m.group(1)) if diff_m else 0
    color = diff_m.group(2) if diff_m else 'NO_COLOR'
    return {
        'lvl': lvl, 'mov': mov, 'ac': ac, 'mr_pct': mr_pct, 'aln': aln,
        'gen': gen, 'atks': atks, 'wt': wt, 'nut': nut, 'siz': siz,
        'mr1': mr1, 'mr2': mr2,
        'm1': m1_flags, 'm2': m2_flags, 'm3': m3_flags,
        'diff': diff, 'color': color,
    }

def fmt_attack(at, ad, n, d, lvl):
    at_name = AT_NAMES.get(at, at)
    ad_name = AD_NAMES.get(ad, ad)
    n = int(n); d = int(d)
    if n == 0 and d == 0:
        dmg = ''
    elif n == 0:
        # Passive 0dN attacks use (monster level + 1)dN in combat.
        dmg = f'{lvl + 1}d{d}' if at == 'AT_NONE' else f'0d{d}'
    else:
        dmg = f'{n}d{d}'
    parts = [at_name]
    if dmg:
        parts.append(dmg)
    if ad_name:
        parts.append(ad_name)
    return ' '.join(parts)

def fmt_attacks(atks, lvl):
    seen = []
    for at, ad, n, d in atks:
        if at == 'NO_ATTK':
            continue
        s = fmt_attack(at, ad, n, d, lvl)
        if s:
            seen.append(s)
    if not seen:
        return '—'
    # A monster definition can repeat the same attack several times.
    # Preserve that information without making the reader parse five
    # identical phrases in a row.
    collapsed = []
    for attack in seen:
        if collapsed and collapsed[-1][0] == attack:
            collapsed[-1][1] += 1
        else:
            collapsed.append([attack, 1])
    return ' · '.join(
        f'{attack} ×{count}' if count > 1 else attack
        for attack, count in collapsed
    )

def fmt_flags(mon):
    out = []
    for f, label in KEY_FLAGS.items():
        if f == 'M1_POIS' and (
                'G_NOCORPSE' in mon['gen'] or 'M2_WERE' in mon['m2']):
            continue
        if f in mon['m1'] or f in mon['m2'] or f in mon['m3']:
            out.append(label)
    # Resistances (mr1)
    mr1_text = mon['mr1']
    for token, label in MR_FLAGS.items():
        if token in mr1_text:
            out.append(label)
    return ', '.join(out)

def color_str(color):
    return CLR_TO_NAME.get(color, color.lower())

# Notes — a one-line annotation only for monsters that earn one.
NOTES = {
    'jackal': "The first thing that ever killed you.",
    'killer bee': "Stings carry poison; a pack can wipe out an unprepared early hero.",
    'soldier ant': "Poison sting. The most lethal `a` you'll meet in the early dungeon.",
    'gelatinous cube': "Slow but paralyses on touch. Don't melee without free-action.",
    'acid blob': "Passive acid damage — punching one corrodes your gloves.",
    'cockatrice': "Touch petrifies. Always carry a lizard corpse.",
    'chickatrice': "A small cockatrice. Same petrify rules apply.",
    'floating eye': "Passive gaze paralyses on melee if you and the eye can see each other. Use ranged, or wear a blindfold or towel.",
    'medusa': "Gaze petrifies. Use a mirror; she petrifies herself on her own reflection.",
    'mind flayer': "Tentacles drain Int; once it reaches 3, the next tentacle that lands kills. Any helmet blocks 7/8 of tentacles.",
    'master mind flayer': "Five tentacles per turn. Any helmet blocks 7/8 of them.",
    'leprechaun': "Steals gold and teleports away. Carry no gold near them.",
    'nymph': "Steals an item and teleports. Block her path or kill from range.",
    'shopkeeper': "Don't anger one. They're stronger than they look and have eternal grudges.",
    'priest': "Temple defenders. Convert their altars or sacrifice on them.",
    'high priest': "Endgame altar guardian. Don't fight one head-on.",
    'Cerberus': "Three-headed hellhound. Reflection + fire resistance only.",
    'orc-captain': "Hits hard. Drops decent loot.",
    'master lich': "Casts wizard spells. Kill from afar.",
    'arch-lich': "End-game tier. Casts death rays. Magic resistance mandatory.",
    'red dragon': "Cone of fire. Get fire resistance before you meet one.",
    'blue dragon': "Cone of lightning. Shock resistance.",
    'gray dragon': "Anti-magic breath. Magic resistance helps; reflection doesn't.",
    'black dragon': "Disintegration breath. Disint resistance OR reflection.",
    'silver dragon': "Cold breath plus reflection scales — your reflection target.",
    'green dragon': "Poison breath; poison resistance is enough.",
    'white dragon': "Cone of cold. Cold resistance.",
    'yellow dragon': "Acid breath.",
    'orange dragon': "Sleep ray. Sleep resistance trivialises.",
    'gold dragon': "Fire breath. Drops gold-colored scales (light source).",
    'baby red dragon': "Same breath type as the adult; less HP. Still bad without fire res.",
    'baby blue dragon': "Lightning breath, ditto.",
    'storm giant': "Throws boulders for big damage. Carries shock attacks.",
    'fire giant': "Throws boulders.",
    'frost giant': "Throws boulders. Has cold attacks.",
    'titan': "Tough humanoid with magic missiles. Casts spells.",
    'rust monster': "Touch rusts iron. Strip armor before engaging or use silver.",
    'disenchanter': "Touch removes enchantment. Devastating to your +5 long sword.",
    'umber hulk': "Confusion gaze. Hard to navigate around. Hits hard too.",
    'minotaur': "Two claws plus a butt. Heavy hitter; usually guards a vault.",
    'foocubus': "Succubus/Incubus. Steals XP and items if you accept advances.",
    'invisible stalker': "Permanent invisibility + see-invis. Plays mind games.",
    'jabberwock': "Four 2d10 attacks; baseline speed, so retreat early if you cannot take the exchange.",
    'Death': "Rider of the Apocalypse. Vanquish three to ascend.",
    'Pestilence': "Rider; spreads disease.",
    'Famine': "Rider; drains nutrition to starvation.",
    'Wizard of Yendor': "Rodney himself. The final test before the Plane of Earth.",
    'Vlad the Impaler': "Vampire boss in Vlad's Tower. Has the Candelabrum.",
    'High Priest': "Each major temple has one. Tougher than priests.",
    'Croesus': "Vault guardian in Fort Ludios. Hoards gold, gems, and magic items.",
    'mail daemon': "Appears only to deliver in-game mail, then leaves.",
    'pony': "Knight's starting steed.",
    'kitten': "Common starting pet; guaranteed for Wizards.",
    'little dog': "Guaranteed Cave Dweller, Ranger, and Samurai starting pet.",
    'pony': "Knight's starting steed.",
    'guardian naga': "Lawful characters may find one peaceful.",
    'Master of Thieves': "Rogue quest leader; also Tourist quest nemesis.",
    'Cyclops': "Healer quest nemesis. Throws boulders.",
    'Lord Surtur': "Valkyrie quest nemesis.",
    'Lord Carnarvon': "Archeologist quest leader.",
    'Pelias': "Barbarian quest leader.",
    'Shaman Karnov': "Cave Dweller quest leader.",
    'Hippocrates': "Healer quest leader.",
    'Ashikaga Takauji': "Samurai quest nemesis.",
    'King Arthur': "Knight quest leader. Holds Excalibur if you didn't get it.",
    'Grand Master': "Monk quest leader.",
    'Arch Priest': "Priest quest leader.",
    'Orion': "Ranger quest leader. Bow user.",
    'Master Assassin': "Rogue quest nemesis.",
    'Lord Sato': "Samurai quest leader.",
    'Twoflower': "Tourist quest leader.",
    'Norn': "Valkyrie quest leader.",
    'Neferet the Green': "Wizard quest leader.",
    'Thoth Amon': "Barbarian quest nemesis.",
    'Master Kaen': "Monk quest nemesis.",
    'Dark One': "Wizard quest nemesis.",
}

# Build groups
groups = {}
for m in MON_RE.finditer(TEXT):
    name = m.group(1)
    sym = m.group(2)
    body = m.group(3)
    if not name:
        continue
    mon = parse_mon(body)
    if not mon:
        continue
    groups.setdefault(sym, []).append((name, mon))

# Compose markdown
out = []
out.append('### Bestiary Tables')
out.append('')
out.append("Every monster you might meet, grouped by map symbol. **Lvl** is the "
           "base monster level. **Spd** "
           "is movement rate (12 is normal player speed). **AC** is armor class "
           "(lower is better). **MR** is the percentage chance the monster resists "
           "your spells and magic attacks. **Attacks** lists each attack's mode, "
           "dice, and side effect; for a status attack, the dice can measure duration "
           "rather than HP damage. Attacks separated by `·` can all occur in "
           "one turn. **Notes** lists traits that change the fight, such as flight, "
           "seeing invisible, regeneration, or a poisonous corpse.")
out.append('')

def mon_labels(mon):
    """Return the set of short labels (KEY_FLAGS + MR_FLAGS) that
    apply to this monster."""
    labels = set()
    for flag, label in KEY_FLAGS.items():
        # Human-form werecreatures change form instead of leaving the
        # poisonous corpse suggested by their M1 flags.
        if flag == 'M1_POIS' and (
                'G_NOCORPSE' in mon['gen'] or 'M2_WERE' in mon['m2']):
            continue
        if flag in mon['m1'] or flag in mon['m2'] or flag in mon['m3']:
            labels.add(label)
    for token, label in MR_FLAGS.items():
        if token in mon['mr1']:
            labels.add(label)
    return labels

def class_trait_summary(items):
    """Compute which traits are (a) universal across the class and
    (b) shared by all-but-one member. Returns:
      universal: set of labels
      almost:    list of (label, exception_name) for traits that ALL
                 except one member possess (only meaningful for classes
                 with >= 4 members; we don't want 'all except a' for a
                 2-member class)
    """
    if len(items) < 2:
        return set(), []
    label_members = {}
    all_names = {n for n, _ in items}
    for name, mon in items:
        for label in mon_labels(mon):
            label_members.setdefault(label, set()).add(name)
    universal = set()
    almost = []
    for label, members in label_members.items():
        missing = all_names - members
        if not missing:
            universal.add(label)
        elif len(missing) == 1 and len(items) >= 4:
            almost.append((label, next(iter(missing))))
    return universal, almost

def join_with_and(strs):
    if not strs:
        return ''
    if len(strs) == 1:
        return strs[0]
    if len(strs) == 2:
        return f'{strs[0]} and {strs[1]}'
    return ', '.join(strs[:-1]) + f', and {strs[-1]}'

def class_intro(label_word, items):
    universal, almost = class_trait_summary(items)
    if not universal and not almost:
        return ''
    # Deterministic ordering — flag dict insertion order, then MR dict.
    order = list(KEY_FLAGS.values()) + list(MR_FLAGS.values())
    def order_key(label_or_pair):
        lbl = label_or_pair[0] if isinstance(label_or_pair, tuple) else label_or_pair
        return order.index(lbl) if lbl in order else 999
    sentences = []
    if universal:
        ordered_u = sorted(universal, key=order_key)
        # Group consecutive "are X" predicates into a single "are X, Y, Z"
        # clause so we don't get "are mindless, are sleep-resistant, are
        # poison-resistant" with three are's.
        prose_parts = []
        i = 0
        while i < len(ordered_u):
            lbl = ordered_u[i]
            form = PROSE_FORM.get(lbl, lbl)
            if form.startswith('are '):
                # Collect a run of "are X" predicates and merge.
                adjectives = [form[len('are '):]]
                j = i + 1
                while j < len(ordered_u):
                    next_form = PROSE_FORM.get(ordered_u[j], ordered_u[j])
                    if not next_form.startswith('are '):
                        break
                    adjectives.append(next_form[len('are '):])
                    j += 1
                prose_parts.append('are ' + join_with_and(adjectives))
                i = j
            else:
                prose_parts.append(form)
                i += 1
        sentences.append(f'All {label_word} {join_with_and(prose_parts)}.')
    for label, exception in sorted(almost, key=order_key):
        verb = PROSE_FORM.get(label, label)
        sentences.append(f'All except *{exception}* also {verb}.')
    return ' '.join(sentences)

def fmt_flags_excluding(mon, exclude_labels):
    """Per-row flag string, with hoisted labels removed."""
    return ', '.join(sorted(mon_labels(mon) - exclude_labels,
                            key=lambda l: list(KEY_FLAGS.values()).index(l)
                            if l in KEY_FLAGS.values()
                            else 100 + list(MR_FLAGS.values()).index(l)
                            if l in MR_FLAGS.values() else 999))

# One-sentence (occasionally two-sentence) strategic prose per class.
# Should answer "what should I know about fighting this letter that the
# row data doesn't tell me?" — keep links and concrete tactical advice;
# skip flavor descriptions of what the monster looks like.
CLASS_PROSE = {
    'S_ANT': (
        "Insects, often in groups. The soldier ant is the early game's "
        "infamous killer: its bite and poisoned sting can drop a "
        "low-level hero in two rounds. Killer bees swarm; the queen "
        "bee in a beehive room is tough on her own."
    ),
    'S_BLOB': (
        "Slow, mindless, immune to a lot. Don't melee an acid blob "
        "with bare hands or a metal weapon you care about: the passive "
        "acid corrodes both. Gelatinous cubes paralyse on touch."
    ),
    'S_COCKATRICE': (
        "Medieval bestiary creature: a chicken with a serpent's tail "
        "whose touch turns flesh to stone. Carry a lizard corpse, "
        "fight gloved, and never wield a cockatrice corpse bare-handed. See "
        "[Petrification](#petrification-stoning)."
    ),
    'S_DOG': (
        "Wild canines hunt in packs. Domestic ones can be tamed by "
        "feeding (see [Making Friends](#making-friends)). Werejackals "
        "and werewolves can give lycanthropy."
    ),
    'S_EYE': (
        "The floating eye's passive paralysis gaze is the single most "
        "famous newbie killer in the game: never melee one without "
        "free action, blindness, or a ranged attack."
    ),
    'S_FELINE': (
        "Wild felines are fast and hostile; a tiger or displacer "
        "beast can turn an ordinary corridor into a bad fight. "
        "Several smaller cats can be starting pets."
    ),
    'S_GREMLIN': (
        "Touch in water (or just at night) can steal an intrinsic. Kill "
        "them on dry land, ideally during daylight."
    ),
    'S_HUMANOID': (
        "Dwarves carry better-than-average loot (weapons, armor, and "
        "pick-axes), but that same equipment makes them dangerous to "
        "an unarmored explorer."
    ),
    'S_IMP': (
        "Annoying minor demons. Imps insult you; quasits drain "
        "Dexterity; homunculi can put you to sleep."
    ),
    'S_JELLY': (
        "Stationary or near-stationary. The blue jelly's passive cold "
        "and the spotted jelly's passive acid bite even when you hit them."
    ),
    'S_KOBOLD': (
        "Weak early-game fodder. All are poisonous to eat — leave the "
        "corpses unless you have poison resistance."
    ),
    'S_LEPRECHAUN': (
        "Steals gold and teleports away. The fix is to carry no gold "
        "near them, or to kill from range. The corpse drops the gold back."
    ),
    'S_MIMIC': (
        "Disguised as items, walls, or fountains. Common in shops and "
        "zoos. The giveaway is the wrong object on the wrong square."
    ),
    'S_NYMPH': (
        "Steals one item and teleports away. The cure is to engage from "
        "range, block her path with pets, or wear an amulet of life "
        "saving and steal the item back from her corpse later."
    ),
    'S_ORC': (
        "Pack hunters with mediocre loot but real numbers. The Mines "
        "are full of them; bring a chokepoint."
    ),
    'S_PIERCER': (
        "Clings to the ceiling and drops on you when you walk under. "
        "A hard helmet blocks the 4d6 blow; good AC can dodge it."
    ),
    'S_QUADRUPED': (
        "Mixed bag. Rothes are early-game wreckers (three attacks per "
        "turn). Mumakil are slow but extremely sturdy."
    ),
    'S_RODENT': (
        "Mostly nuisance fodder. Giant rats are common in the early "
        "dungeon; their corpses are safe food."
    ),
    'S_SPIDER': (
        "Includes scorpions and centipedes. Giant spider and scorpion "
        "corpses are poisonous; cave spider and centipede corpses are safe."
    ),
    'S_TRAPPER': (
        "Stationary engulfers that look like a piece of dungeon. "
        "Stepping into one starts a swallow attack you can't easily "
        "escape. Search next to a suspicious square; farlook cannot "
        "display a hidden lurker."
    ),
    'S_UNICORN': (
        "White, gray, and black correspond to Lawful, Neutral, and "
        "Chaotic. Killing a co-aligned unicorn costs 5 Luck; killing a "
        "cross-aligned one does not change Luck. Any thrown gem pacifies "
        "a hostile unicorn, while real gems can also change Luck."
    ),
    'S_VORTEX': (
        "Engulfing elemental clouds. Only the fog cloud is slow; the "
        "others move at speed 20–22. Their attacks blind, freeze, shock, "
        "or burn, and the energy vortex also drains Pw."
    ),
    'S_WORM': (
        "Long worms become a maze of tail segments as they grow. "
        "Purple worms swallow you whole and digest. Don't get cornered."
    ),
    'S_XAN': (
        "Grid bugs are trivial; xans, the bigger relatives, sting your "
        "legs and slow you down."
    ),
    'S_LIGHT': (
        "Yellow light explodes when it attacks, causing 10d20 turns of "
        "blindness unless you resist blindness. Black light causes "
        "10d12 turns of hallucination. See "
        "[Light Bursts](#light-bursts)."
    ),
    'S_ZRUTY': (
        "A zruty is a nasty mid-game brute with two claws and a heavy "
        "bite, but worth good experience if you can take the flurry. "
        "The name comes from the hairy wild man of Slavic folklore."
    ),
    'S_ANGEL': (
        "Powerful late-game spellcasters with weapons. Astral-Plane "
        "Angels guard each High Priest — see "
        "[The Ascension Run](#the-ascension-run)."
    ),
    'S_BAT': (
        "Erratic flyers, mostly nuisance. A vampire bat's poisoned "
        "bite drains Strength; poison resistance blocks it."
    ),
    'S_CENTAUR': (
        "Mounted archers with strong physical attacks. They wield "
        "bows and shoot at range."
    ),
    'S_DRAGON': (
        "Each color breathes its element type. Reflection bounces the "
        "ranged breath back. Adults are sources of dragon scale mail; "
        "babies bite but do not breathe. See "
        "[Dragon Scale Mail](#armor-tables)."
    ),
    'S_ELEMENTAL': (
        "Air elementals engulf and batter you; fire elementals burn; "
        "water elementals make one heavy physical attack; earth is slow but tough."
    ),
    'S_FUNGUS': (
        "Stationary. Lichen corpses never rot — keep one in your "
        "pack as iron rations. Violet and yellow molds bite back on "
        "melee with elemental passive damage."
    ),
    'S_GNOME': (
        "Gnomish PCs find most Mines residents peaceful. A gnome lord "
        "hits harder than its ordinary kin, and a gnomish wizard attacks "
        "only with spells."
    ),
    'S_GIANT': (
        "Boulder throwers. Fire, frost, and storm giants deal their "
        "named element and their corpses can grant the matching "
        "resistance; titans cast spells. A true giant corpse also "
        "raises Strength."
    ),
    'S_invisible': (
        "Single species — the invisible stalker. Permanent invis "
        "plus see-invis itself. Get see-invisible or telepathy."
    ),
    'S_JABBERWOCK': (
        "The monster from Lewis Carroll's *Jabberwocky* (\"O frabjous "
        "day! Callooh! Callay!\"). It moves at player baseline speed and "
        "makes four 2d10 attacks, so decide early whether you can stand "
        "and trade blows. Vorpal Blade beheads it automatically."
    ),
    'S_KOP': (
        "Police force triggered by stealing from shops or hurting "
        "shopkeepers. Paying what you owe dismisses every Kop; otherwise "
        "escape rather than grinding through a force that can respawn."
    ),
    'S_LICH': (
        "Skeletal spellcasters. Higher tiers cast wizard spells; master "
        "and arch-liches demand magic resistance, and an arch-lich can "
        "cast touch of death."
    ),
    'S_MUMMY': (
        "Mindless undead with physical claw attacks. A wand or spell "
        "of undead turning deals 1d8 and makes them flee. On death, a "
        "mummy leaves the already-old corpse of its base race."
    ),
    'S_NAGA': (
        "Long serpentine bodies with ranged attacks. Black naga corpses "
        "can grant poison resistance; their acid and stoning resistance is temporary."
    ),
    'S_OGRE': (
        "Big melee brutes. They carry a club and sometimes a battle-axe, "
        "but no armor."
    ),
    'S_PUDDING': (
        "Splits when you hit them. Brown puddings corrode armor on "
        "touch; black puddings corrode both armor and weapons. Fire-"
        "kill them so they don't split, or pick a chokepoint."
    ),
    'S_QUANTMECH': (
        "Touch teleports you randomly. The annoyance is the lost "
        "position more than the damage, but a random teleport into a "
        "dangerous room can still kill you."
    ),
    'S_RUSTMONST': (
        "Rust monsters rust iron equipment on touch; disenchanters "
        "remove the enchantment off your +5 long sword. Strip iron "
        "armor / switch to silver or non-iron weapons before engaging."
    ),
    'S_SNAKE': (
        "Mostly poisonous. The pit viper and cobra are the "
        "dangerous ones; garter snakes are fodder."
    ),
    'S_TROLL': (
        "Regenerates from corpses. Eat the corpse, kill it with "
        "Trollsbane, or stone it so no corpse remains."
    ),
    'S_UMBER': (
        "Confusion gaze. Blindness defeats it; free action does not. "
        "The confusion stacks and wrecks navigation."
    ),
    'S_VAMPIRE': (
        "Drains XL on bite. Shapeshifts to bat or cloud. Vlad the "
        "Impaler is the vampire boss in his Tower. Ordinary vampires "
        "and vampire lords leave an old human corpse; Vlad leaves none."
    ),
    'S_WRAITH': (
        "Drains XL on touch. A fresh plain wraith corpse grants an "
        "experience level when eaten; barrow wights and Nazgul leave "
        "no corpse."
    ),
    'S_XORN': (
        "D&D's three-armed, three-eyed creatures from the Elemental "
        "Plane of Earth. They phase through walls and eat metal objects "
        "from the floor; their attacks are purely physical."
    ),
    'S_YETI': (
        "Apes and great apes mostly; sasquatches are fast. Carnivore "
        "corpses are safe food."
    ),
    'S_ZOMBIE': (
        "Slow undead, easy to kite. A wand or spell of undead turning "
        "deals 1d8 and makes them flee. Race-based zombies leave an "
        "already-old corpse of that race; ghouls and skeletons leave none."
    ),
    'S_HUMAN': (
        "Never make assumptions from an `@` alone. It can be a peaceful "
        "shopkeeper, priest, watchman, or quest leader; or Medusa, a role "
        "nemesis, Croesus, or the Wizard of Yendor. Check the name first."
    ),
    'S_DEMON': (
        "Major demons. Most can gate in reinforcements (a single "
        "barbed devil in your face can become five). Silver weapons "
        "and Demonbane do extra damage. Geryon, Dispater, Baalzebub, "
        "and Asmodeus may accept a bribe."
    ),
    'S_GOLEM': (
        "Iron, stone, and clay golems are dangerous; wood and leather "
        "golems are early-game fodder. A rare gold golem is a walking "
        "treasure pile."
    ),
    'S_EEL': (
        "Lives in water. Wraps around you and drags you under to "
        "drown. Don't fight one from a water square without magical "
        "breathing or escape."
    ),
    'S_LIZARD': (
        "Mostly harmless. **Lizard corpses cure petrification and "
        "never rot.** Carry one for cockatrices. Medusa's gaze kills "
        "immediately, so a lizard cannot save you from it."
    ),
}

for sym in SYM_ORDER:
    items = groups.get(sym)
    if not items:
        continue
    ch, label = SYM_TO_CHAR[sym]
    out.append(f'#### {label} `{ch}`')
    out.append('')
    # Strategic prose intro: one or two sentences about what to know
    # tactically and (where relevant) a snippet of trivia about the
    # class's origin. Curated, not generated.
    if sym in CLASS_PROSE:
        out.append(CLASS_PROSE[sym])
        out.append('')
    # Per-class hoisting: pull out flags/resistances shared by every (or
    # all-but-one) member, mention them in a one-line intro, and strip
    # them from the per-row flag column. The hoisted traits become
    # narrative; the row column carries only what's distinctive.
    intro = class_intro(label.lower(), items)
    if intro:
        out.append(intro)
        out.append('')
    # Compute the SAME exclusion set the intro used, so per-row flag
    # strings drop the hoisted labels.
    universal, almost = class_trait_summary(items)
    hoisted = universal | {label for label, _ in almost}
    out.append('::: dense-table')
    out.append('')
    out.append('| Name | Color | Lvl | Spd | AC | MR | Attacks | Notes |')
    out.append('|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|')
    for name, mon in items:
        clr = color_str(mon['color'])
        atks = fmt_attacks(mon['atks'], mon['lvl'])
        flag_excl = hoisted
        flags = fmt_flags_excluding(mon, flag_excl)
        extra = NOTES.get(name, '')
        parts = []
        if flags:
            parts.append(flags + '.')
        if extra:
            parts.append(extra)
        note = ' '.join(parts)
        out.append(f'| {name} | {clr} | {mon["lvl"]} | {mon["mov"]} | {mon["ac"]} | '
                   f'{mon["mr_pct"]} | {atks} | {note} |')
    out.append('')
    out.append(':::')
    out.append('')

print('\n'.join(out))
