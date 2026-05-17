#!/usr/bin/env python3
"""Parse monsters.h and emit the Bestiary Appendix markdown."""
import re
from pathlib import Path

TEXT = Path('/Users/davidbau/git/mazesofmenace/teleport/maud/nethack-c/upstream/include/monsters.h').read_text()
# Strip preprocessor noise
TEXT = re.sub(r'#if 0[\s\S]*?#endif', '', TEXT)

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
    'AT_WEAP': 'weapon', 'AT_MAGC': 'spell',
}
AD_NAMES = {
    'AD_PHYS': '', 'AD_MAGM': 'magic', 'AD_FIRE': 'fire',
    'AD_COLD': 'cold', 'AD_SLEE': 'sleep', 'AD_DISN': 'disint',
    'AD_ELEC': 'shock', 'AD_DRST': 'poison', 'AD_ACID': 'acid',
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

# Key flags from M1/M2/M3 we'll surface in a notes column
KEY_FLAGS = {
    'M1_FLY': 'flies',
    'M1_SWIM': 'swims',
    'M1_AMPHIBIOUS': 'amphibious',
    'M1_AMORPHOUS': 'amorphous',
    'M1_TUNNEL': 'tunnels',
    'M1_CONCEAL': 'hides',
    'M1_HIDE': 'hides',
    'M1_REGEN': 'regen',
    'M1_SEE_INVIS': 'sees-invis',
    'M1_TPORT': 'teleports',
    'M1_TPORT_CNTRL': 'tport-cntrl',
    'M1_POIS': 'poisonous-corpse',
    'M2_STALK': 'stalks',
    'M2_NASTY': 'nasty',
    'M2_STRONG': 'strong',
    'M2_PEACEFUL': 'peaceful',
    'M2_DOMESTIC': 'domestic',
    'M2_SHAPESHIFTER': 'shifter',
    'M3_INFRAVISION': 'infravis',
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

def fmt_attack(at, ad, n, d):
    at_name = AT_NAMES.get(at, at)
    ad_name = AD_NAMES.get(ad, ad)
    n = int(n); d = int(d)
    if n == 0 and d == 0:
        dmg = ''
    elif n == 0:
        dmg = f'0d{d}'
    else:
        dmg = f'{n}d{d}'
    parts = [at_name]
    if dmg:
        parts.append(dmg)
    if ad_name:
        parts.append(ad_name)
    return ' '.join(parts)

def fmt_attacks(atks):
    seen = []
    for at, ad, n, d in atks:
        if at == 'NO_ATTK':
            continue
        s = fmt_attack(at, ad, n, d)
        if s:
            seen.append(s)
    return ' · '.join(seen) if seen else '—'

def fmt_flags(mon):
    out = []
    for f, label in KEY_FLAGS.items():
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
    'floating eye': "Passive gaze paralyses if you melee in daylight. Use ranged or close eyes first.",
    'medusa': "Gaze petrifies. Use a mirror; she petrifies herself on her own reflection.",
    'mind flayer': "Tentacle attacks drain Int; if Int hits 3 you die. Wear an alignment-matching helmet or kill from range.",
    'master mind flayer': "Five tentacles per turn. Catastrophic without telepathy + free action.",
    'leprechaun': "Steals gold and teleports away. Carry no gold near them.",
    'nymph': "Steals an item and teleports. Block her path or kill from range.",
    'shopkeeper': "Don't anger one. They're stronger than they look and have eternal grudges.",
    'priest': "Temple defenders. Convert their altars or sacrifice on them.",
    'high priest': "Endgame altar guardian. Don't fight one head-on.",
    'Cerberus': "Three-headed hellhound. Reflection + fire resistance only.",
    'orc-captain': "Hits hard. Drops decent loot.",
    'master lich': "Casts double-trouble. Disperse or kill from afar.",
    'arch-lich': "End-game tier. Casts death rays. Magic resistance mandatory.",
    'mummy lord': "Curses your equipment on touch. Bring uncursing on hand.",
    'red dragon': "Cone of fire. Get fire resistance before you meet one.",
    'blue dragon': "Cone of lightning. Shock resistance.",
    'gray dragon': "Anti-magic breath. Magic resistance helps; reflection doesn't.",
    'black dragon': "Disintegration breath. Disint resistance OR reflection.",
    'silver dragon': "Cold breath plus reflection scales — your reflection target.",
    'green dragon': "Poison breath; poison resistance is enough.",
    'white dragon': "Cone of cold. Cold resistance.",
    'yellow dragon': "Acid breath; rare.",
    'orange dragon': "Sleep ray. Sleep resistance trivialises.",
    'gold dragon': "Fire breath. Drops gold-colored scales (light source).",
    'baby red dragon': "Same breath type as the adult; less HP. Still bad without fire res.",
    'baby blue dragon': "Lightning breath, ditto.",
    'storm giant': "Throws boulders for big damage. Carries shock attacks.",
    'fire giant': "Throws boulders. Surprisingly poor offensively if you have fire res.",
    'frost giant': "Throws boulders. Has cold attacks.",
    'titan': "Tough humanoid with magic missiles. Casts spells.",
    'rust monster': "Touch rusts iron. Strip armor before engaging or use silver.",
    'disenchanter': "Touch removes enchantment. Devastating to your +5 long sword.",
    'umber hulk': "Confusion gaze. Hard to navigate around. Hits hard too.",
    'minotaur': "Two claws plus a butt. Heavy hitter; usually guards a vault.",
    'foocubus': "Succubus/Incubus. Steals XP and items if you accept advances.",
    'invisible stalker': "Permanent invisibility + see-invis. Plays mind games.",
    'jabberwock': "Powerful but slow. Free XP if you're set up.",
    'Death': "Rider of the Apocalypse. Vanquish three to ascend.",
    'Pestilence': "Rider; spreads disease.",
    'Famine': "Rider; drains nutrition to starvation.",
    'Wizard of Yendor': "Rodney himself. The final test before the Plane of Earth.",
    'Vlad the Impaler': "Vampire boss in Vlad's Tower. Has the Candelabrum.",
    'High Priest': "Each major temple has one. Tougher than priests.",
    'Croesus': "Vault guardian on Fort Ludios. Drops a wand of wishing wish-share.",
    'mail daemon': "Delivers in-game mail. Don't attack one — they don't fight back.",
    'pony': "Knight's starting steed.",
    'kitten': "Common Valkyrie/Wizard/Tourist starting pet.",
    'little dog': "Common Archeologist/Caveman/Samurai starting pet.",
    'pony': "Knight's starting steed.",
    'guardian naga': "Friendly to the Healer. Hostile otherwise.",
    'Master of Thieves': "Rogue quest nemesis.",
    'Cyclops': "Caveman quest nemesis. Throws boulders.",
    'Lord Surtur': "Valkyrie quest nemesis. Has Mjollnir if you don't.",
    'Lord Carnarvon': "Archeologist quest leader.",
    'Hippocrates': "Healer quest leader.",
    'Ashikaga Takauji': "Samurai quest nemesis.",
    'King Arthur': "Knight quest leader. Holds Excalibur if you didn't get it.",
    'Grand Master': "Monk quest leader.",
    'Arch Priest': "Priest quest leader.",
    'Orion': "Ranger quest leader. Bow user.",
    'Master Assassin': "Rogue quest nemesis backup.",
    'Twoflower': "Tourist quest leader.",
    'Norn': "Valkyrie quest leader.",
    'Neferet the Green': "Wizard quest leader.",
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
out.append('### Bestiary')
out.append('')
out.append("Every monster you might meet. Grouped by ASCII symbol so you can flip "
           "to the right page mid-game. **Lvl** is the base monster level. **Spd** "
           "is movement rate (12 is normal player speed). **AC** is armor class "
           "(lower is better). **MR%** is the percentage chance the monster resists "
           "your spells and magic attacks. **Attacks** lists each attack's mode, "
           "damage dice, and side effect; multiple attacks separated by `·` are "
           "made per turn. **Notes** folds in the most tactically-relevant trait "
           "flags (flies, sees-invis, regenerates, poisonous-corpse, etc.) "
           "alongside specific heads-ups for monsters that deserve one.")
out.append('')

for sym in SYM_ORDER:
    items = groups.get(sym)
    if not items:
        continue
    ch, label = SYM_TO_CHAR[sym]
    out.append(f'#### {label} `{ch}`')
    out.append('')
    out.append('| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |')
    out.append('|------|-------|-----|-----|----|-----|---------|--------------------------------------------------------------------|')
    for name, mon in items:
        clr = color_str(mon['color'])
        atks = fmt_attacks(mon['atks'])
        flags = fmt_flags(mon)
        extra = NOTES.get(name, '')
        # Fold flag string and heads-up note into a single Notes cell.
        # Flag string ends without punctuation; add a period and space
        # before the prose note when both are present.
        if flags and extra:
            note = f'{flags}. {extra}'
        elif flags:
            note = f'{flags}.'
        else:
            note = extra
        out.append(f'| {name} | {clr} | {mon["lvl"]} | {mon["mov"]} | {mon["ac"]} | '
                   f'{mon["mr_pct"]} | {atks} | {note} |')
    out.append('')

print('\n'.join(out))
