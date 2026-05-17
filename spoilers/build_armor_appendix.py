#!/usr/bin/env python3
"""Parse objects.h and emit the Armor Appendix markdown."""
import re
from pathlib import Path

OBJ = Path('/Users/davidbau/git/mazesofmenace/teleport/maud/nethack-c/upstream/include/objects.h').read_text()
# Strip deferred / disabled entries (#if 0 ... #endif blocks)
OBJ = re.sub(r'#if 0[\s\S]*?#endif', '', OBJ)

POWER_NAMES = {
    '0': '',
    'CLAIRVOYANT': 'Clairvoyance.',
    'WARNING': 'Warning.',
    'TELEPAT': 'Telepathy.',
    'STEALTH': 'Stealth.',
    'POISON_RES': 'Poison resistance.',
    'PROTECTION': '',  # cloak of protection — MC column already shows the 3
    'INVIS': 'Invisibility.',
    'ANTIMAGIC': 'Magic resistance.',
    'DISPLACED': 'Displacement.',
    'DRAIN_RES': 'Drain resistance.',
    'SHOCK_RES': 'Shock resistance.',
    'REFLECTING': 'Reflection.',
    'FUMBLING': 'Causes frequent fumbling.',
    'FAST': '+1 speed.',
    'WWALKING': 'Water walking.',
    'JUMPING': '`#apply` to leap.',
    'LEVITATION': 'Levitation (cannot be removed while in the air).',
    'FIRE_RES': 'Fire resistance.',
    'COLD_RES': 'Cold resistance.',
    'SLEEP_RES': 'Sleep resistance.',
    'DISINT_RES': 'Disintegration resistance.',
    'ACID_RES': 'Acid resistance.',
}

MATERIAL_NAMES = {
    'IRON': 'iron', 'WOOD': 'wood', 'METAL': 'metal',
    'SILVER': 'silver', 'COPPER': 'copper', 'GLASS': 'glass',
    'CLOTH': 'cloth', 'LEATHER': 'leather', 'MITHRIL': 'mithril',
    'DRAGON_HIDE': 'dragonhide', 'BONE': 'bone',
    'PLASTIC': 'plastic',
}

def parse_macro(name, sig_field_names):
    """sig_field_names: list of field names in macro signature order, excluding name/desc."""
    pattern = re.compile(
        rf'{name}\("([^"]+)",\s*(?:"([^"]+)"|NoDes)\s*,\s*([^)]+?)\)',
        re.DOTALL)
    out = []
    for m in pattern.finditer(OBJ):
        wname = m.group(1)
        desc = m.group(2) or ''
        args = m.group(3)
        args = re.sub(r'\s+', ' ', args)
        args = re.sub(r'/\*.*?\*/', '', args)
        parts = [p.strip() for p in args.split(',')]
        d = dict(zip(sig_field_names, parts))
        out.append((wname, desc, d))
    return out

# ARMOR(name, desc, kn, mgc, blk, power, prob, delay, wt, cost, ac, can, sub, metal, c, sn)
ARMOR_SIG = ['kn', 'mgc', 'blk', 'power', 'prob', 'delay', 'wt', 'cost',
             'ac', 'can', 'sub', 'metal', 'color', 'sn']
HELM_SIG  = ['kn', 'mgc',        'power', 'prob', 'delay', 'wt', 'cost',
             'ac', 'can',        'metal', 'color', 'sn']
CLOAK_SIG = HELM_SIG
GLOVES_SIG = HELM_SIG
BOOTS_SIG  = HELM_SIG
# SHIELD(name, desc, kn, mgc, blk, pow, prob, delay, wt, cost, ac, can, metal, c, sn)
SHIELD_SIG = ['kn', 'mgc', 'blk', 'power', 'prob', 'delay', 'wt', 'cost',
              'ac', 'can',        'metal', 'color', 'sn']
# DRGN_ARMR(name, mgc, power, cost, ac, color, snam) — no desc field
DRGN_SIG = ['mgc', 'power', 'cost', 'ac', 'color', 'sn']

def parse_drgn_armr():
    out = []
    pattern = re.compile(r'DRGN_ARMR\("([^"]+)",\s*([^)]+?)\)', re.DOTALL)
    for m in pattern.finditer(OBJ):
        wname = m.group(1)
        args = m.group(2)
        args = re.sub(r'\s+', ' ', args)
        args = re.sub(r'/\*.*?\*/', '', args)
        parts = [p.strip() for p in args.split(',')]
        d = dict(zip(DRGN_SIG, parts))
        out.append((wname, '', d))
    return out

all_armor = []
for n, d, f in parse_macro('ARMOR', ARMOR_SIG):
    f['blk'] = f.get('blk', '0')
    all_armor.append((n, d, f))
for n, d, f in parse_macro('HELM', HELM_SIG):
    f['sub'] = 'ARM_HELM'; f['blk'] = '0'
    all_armor.append((n, d, f))
for n, d, f in parse_macro('CLOAK', CLOAK_SIG):
    f['sub'] = 'ARM_CLOAK'; f['blk'] = '0'
    all_armor.append((n, d, f))
for n, d, f in parse_macro('GLOVES', GLOVES_SIG):
    f['sub'] = 'ARM_GLOVES'; f['blk'] = '0'
    all_armor.append((n, d, f))
for n, d, f in parse_macro('BOOTS', BOOTS_SIG):
    f['sub'] = 'ARM_BOOTS'; f['blk'] = '0'
    all_armor.append((n, d, f))
for n, d, f in parse_macro('SHIELD', SHIELD_SIG):
    f['sub'] = 'ARM_SHIELD'
    all_armor.append((n, d, f))
for n, d, f in parse_drgn_armr():
    f['sub'] = 'ARM_SUIT'  # scale mail
    if 'scales' in n and 'mail' not in n:
        f['sub'] = 'ARM_SCALES'
    f['kn'] = '1'
    f['blk'] = '1'
    f['delay'] = '5'
    f['wt'] = '40'
    f['can'] = '0'
    f['metal'] = 'DRAGON_HIDE'
    all_armor.append((n, d, f))

# Subgroups
SLOTS = {
    'ARM_SHIRT': 'Shirts',
    'ARM_SUIT': 'Body armor (suits)',
    'ARM_SCALES': 'Dragon scales',
    'ARM_CLOAK': 'Cloaks',
    'ARM_HELM': 'Helmets',
    'ARM_GLOVES': 'Gloves',
    'ARM_BOOTS': 'Boots',
    'ARM_SHIELD': 'Shields',
}
SLOT_ORDER = ['ARM_SUIT', 'ARM_SCALES', 'ARM_SHIRT', 'ARM_CLOAK',
              'ARM_HELM', 'ARM_GLOVES', 'ARM_BOOTS', 'ARM_SHIELD']

groups = {}
for n, d, f in all_armor:
    sub = f.get('sub', 'ARM_SUIT')
    groups.setdefault(sub, []).append((n, d, f))

# Discipline: only annotate when the note adds something the columns
# don't already say. Most leather-jacket / orcish-X / 'a slightly
# different stat' rows stay blank. The reader is in the appendix
# already; they can read the numbers.
NOTES = {
    'plate mail': "Spellcasting penalty.",
    'crystal plate mail': "Never rusts. Spellcasting penalty.",
    'dwarvish mithril-coat': "Light enough for spellcasting. Wizard mid-game goal.",
    'elven mithril-coat': "Light, expensive, no casting penalty.",
    'chain mail': "Dwarves drop these.",
    'studded leather armor': "No spellcasting penalty.",
    'gray dragon scale mail': "Endgame body-armor goal.",
    'silver dragon scale mail': "",
    'gold dragon scale mail': "Emits light.",
    'yellow dragon scale mail': "Rare.",
    'gray dragon scales': "Make-into upgrade to scale mail.",
    'Hawaiian shirt': "Tourist starter. Worn under body armor.",
    'T-shirt': "Worn under body armor.",
    'mummy wrapping': "Blocks invisibility while worn.",
    'oilskin cloak': "Resists grab attacks.",
    'robe': "+1 spellcasting effectiveness.",
    'alchemy smock': "Fantastic early-game safety.",
    'cloak of protection': "Best non-magical defensive cloak.",
    'cloak of magic resistance': "Lightest source of magic resistance.",
    'cornuthaum': "Wizards only; blocks other clairvoyance for non-Wizards.",
    'dunce cap': "Int/Wis → 6. Always cursed on generation.",
    'fedora': "Tourist starter; Eye of the Aethiopica base.",
    'helm of brilliance': "+d4 Int/Wis when blessed and enchanted.",
    'helm of opposite alignment': "Flips alignment. Catastrophic if cursed.",
    'helm of telepathy': "Telepathy while blind.",
    'gauntlets of fumbling': "Avoid.",
    'gauntlets of power': "Sets Strength to 25.",
    'gauntlets of dexterity': "+d3 Dex per enchantment.",
    'water walking boots': "Critical for the Castle drawbridge.",
    'jumping boots': "`#apply` to leap.",
    'fumble boots': "Avoid.",
    'levitation boots': "Can't remove while levitating. Trap item.",
    'large shield': "Blocks two-handed weapons.",
    'shield of reflection': "Saves the body-armor slot.",
}

out = []
out.append('### Armor Tables')
out.append('')
out.append("**AC** is the armor-class bonus the piece provides (higher number = "
           "more protection; this is the amount subtracted from your displayed AC). "
           "**MC** is the magic-cancellation level (1-3) — higher MC reduces the "
           "chance of magic attacks landing. **Wt** is weight; **Cost** is shop "
           "base price. The **Notes** column folds in the intrinsic property "
           "granted while the piece is worn, alongside any tactical caveats. "
           "Armor is grouped by slot. Dragon scale mail is listed separately "
           "because of its sheer importance to the endgame.")
out.append('')

for slot in SLOT_ORDER:
    if slot not in groups:
        continue
    items = groups[slot]
    out.append(f'#### {SLOTS[slot]}')
    out.append('')
    out.append('<div class="dense-table">')
    out.append('')
    out.append('| Armor | AC | MC | Wt | Cost | Material | Notes |')
    out.append('|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|')
    for name, desc, f in items:
        ac = 10 - int(f.get('ac', '10'))
        mc = int(f.get('can', '0'))
        mc_str = str(mc) if mc > 0 else '—'
        power_raw = f.get('power', '0').strip()
        power_str = POWER_NAMES.get(power_raw, '')
        wt = f.get('wt', '?')
        cost = f.get('cost', '?')
        mat = MATERIAL_NAMES.get(f.get('metal', ''), f.get('metal', '').lower())
        extra_note = NOTES.get(name, '')
        # Fold Power text into Notes, joining with a single space.
        note = ' '.join(s for s in (power_str, extra_note) if s)
        out.append(f'| {name} | +{ac} | {mc_str} | {wt} | {cost} | {mat} | {note} |')
    out.append('')
    out.append('</div>')
    out.append('')

print('\n'.join(out))
