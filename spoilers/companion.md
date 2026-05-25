# A Traveler's Companion to the <span class="nobr">Mazes of Menace</span>

```{=html}
<p style="text-align: center; font-style: italic; margin: 1.5em 0;">Do not read this guide aloud. The dungeon is listening.</p>
```

```{=latex}
For more than forty years the NetHack community has grown Jay
Fenlason's ``first-semester programming project'' into the most
unforgivingly intricate and emblematic roguelike, and a thriving
culture of fun and community beyond the game itself. We hope this
companion helps bring the joy of NetHack to a new generation of
players.
```

---

## Before You Read Further

You are holding (or more likely scrolling through) a guide to the
Mazes of Menace, the vast and ever-shifting dungeon complex that sits
beneath a place the locals just call "the dungeon entrance." What lies
below is one of the oldest and most treacherous adventure destinations
in existence: dozens of levels of corridors, vaults, and special
chambers, stretching from the relatively tame upper mines all the way
down to the molten depths of Gehennom and beyond.

People have been descending into these depths for more than four decades.
Most of them died. The ones who made it back brought stories, and some
of those stories eventually got written down. You're reading the latest
edition of that accumulated lore.

**A word of caution.** This guide will change how you experience
the Mazes. Once you know that a floating eye can paralyze you with
a glance, you can never un-know it. Some adventurers prefer the
thrill of discovery over the comfort of preparation. If that's
you, close this guide now and go learn things the hard way. There
is real joy in that.

**Looking for the manual instead?** If you're just looking for game
commands, item lists, and mechanics without spoilers, you want the
**[Guide to the Mazes of Menace](../guidebook/)** instead. That's the
reference manual that comes with the game. This document is a
*strategic* guide. It assumes you already know how to play and want
to know how to *survive*.

But if you have perished under the deadly gaze of just one too
many floating eyes, or if you are tired of the gods abandoning
you to starve with no food rations on level four, read on. We
will do our best to keep you alive.

<aside class="download-box">
<strong>Prefer to read offline?</strong> Print the <a href="book.pdf">book-format PDF</a> (A5 trim, <a href="cover.pdf">cover</a>).
</aside>

---

## Table of Contents

**Part One: Before You Set Out**

1. [Choosing Your Expedition](#choosing-your-expedition) — Roles, races, and alignments
2. [What to Pack](#what-to-pack) — Starting equipment and early priorities
3. [Your First Descent](#your-first-descent) — Surviving the early dungeon

**Part Two: Dungeon Sights**

4. [The Lay of the Land](#the-lay-of-the-land) — Rooms, corridors, and dungeon features (with map)
5. [Field Guide to Dungeon Fauna](#field-guide-to-dungeon-fauna) — Monster classes at a glance
6. [Points of Interest](#points-of-interest) — Fountains, altars, thrones, and sinks
7. [Branches and Landmarks](#branches-and-landmarks) — The Mines, Sokoban, and beyond
8. [Traps and Hazards](#traps-and-hazards) — What the dungeon has in store for you
9. [Feelings and Sounds](#feelings-and-sounds) — Cryptic messages the dungeon uses to tell you what just happened

**Part Three: Survival**

10. [The Art of Combat](#the-art-of-combat) — Hit probability, damage, and tactics
11. [Things That Will Kill You](#things-that-will-kill-you) — Top-ten killers, common deaths, mimics, dragons
12. [Ways to Die Instantly](#ways-to-die-instantly) — Instadeaths and how to recognize them
13. [Divine Relations](#divine-relations) — Prayer, sacrifice, and altars
14. [Making Friends](#making-friends) — Pets, taming, and peaceful coexistence

**Part Four: Gear and Provisions**

15. [A Practical Identification Strategy](#a-practical-identification-strategy) — Figuring out what you've found (with flowchart)
16. [Provisions and Dining](#provisions-and-dining) — Food, nutrition, and dining
17. [The Apothecary](#the-apothecary) — Potions and their many uses
18. [The Scroll Rack](#the-scroll-rack) — Scrolls, their effects, and confused reading
19. [Wands and Staves](#wands-and-staves) — Magical implements
20. [Rings and Amulets](#rings-and-amulets) — Jewelry, for better or worse
21. [Tools of the Trade](#tools-of-the-trade) — From pickaxes to magic lamps
22. [The Armory](#the-armory) — Weapons, armor, and hitting things
23. [Curses and How to Break Them](#curses-and-how-to-break-them) — Spotting them, undoing them, surviving them

**Part Five: Mastery**

24. [Spellcasting](#spellcasting) — Magic for the studious adventurer
25. [Luck and Fortune](#luck-and-fortune) — The hidden numbers that shape your fate
26. [Enhancing Skills](#enhancing-skills) — Mastering specific styles of combat and magic
27. [Wishes and Wishing](#wishes-and-wishing) — Getting what you want
28. [Artifacts](#artifacts) — Legendary equipment and how to obtain it

**Part Six: The Deep Dungeon**

29. [The Castle](#the-castle) — The gateway to Gehennom
30. [Gehennom](#gehennom) — A travel advisory
31. [The Ascension Kit](#the-ascension-kit) — Gear for the long climb
32. [The Ascension Run](#the-ascension-run) — Getting back out alive
33. [The Elemental Planes](#the-elemental-planes) — The final gauntlet

**Appendices**

34. [Advanced Controls](#advanced-controls) — Command counts, prefixes, and efficiency techniques
35. [Customization](#options-worth-knowing-about) — rcfile options worth knowing
36. [Sokoban Solutions](#sokoban-solutions) — All eight level variants, solved
37. [Voluntary Challenges](#voluntary-challenges) — Conducts and self-imposed restrictions
38. [Shopping and Shopkeeper Pricing](#shopping-and-shopkeeper-pricing) — Commerce in the dungeon
39. [Weapons Tables](#weapons-tables)
40. [Armor Tables](#armor-tables)
41. [Spell Tables](#spell-tables)
42. [Bestiary Tables](#bestiary-tables)
43. [What Changed Since Last Time](#what-changed-since-last-time) — What's new in 5.0 vs 3.6.x, and what to do about it
44. [Acknowledgements](#acknowledgements) — Standing on the shoulders of giants


## Part One: Before You Set Out

<!-- audit
2026-05-22 community-strategy additions citation index:
- This audit-pass folded a curated batch of community strategies
  into the book. Each addition is cross-cited with its source URL
  in the planning document `strategy-audit.md` (sibling file in
  this repo). The primary sources drawn on were the NetHackWiki
  (https://nethackwiki.com/wiki/), its Fandom mirror
  (https://nethack.fandom.com/wiki/), David Damerell's ID and
  prayer spoilers at chiark.greenend.org.uk, and Kate Nepveu's
  Steelypips RGRN archive at https://www.steelypips.org/nethack/.
- See strategy-audit.md for the per-addition citation entries.
-->

### Choosing Your Expedition
<!-- audit
2026-05-21:
- Archeologist starts with touchstone (u_init.c:50) and knows_object(TOUCHSTONE) so the tool itself is identified (u_init.c:660-662); does NOT have knows_class(GEM_CLASS) — gems are NOT pre-identified; touchstone identifies gems by rubbing per apply.c:2678-2707 (Ken Arnold)
- Healer starts with wand of sleep, 4 potions of healing, 4 potions of extra healing, and 3 blessed spellbooks (healing, extra healing, stone-to-flesh) (u_init.c:81-90); the spellbooks are always blessed so reading them always succeeds
- Tourist starts with 4 scrolls of magic mapping, 2 potions of extra healing, 21-40 +2 darts, Hawaiian shirt, expensive camera, credit card, and 10 random food items (u_init.c:150-159)
2026-05-18:
- Knight starts with +1 long sword and +1 lance (u_init.c:91-92)
- Cave Dweller gains Fast at XL 7 (attrib.c:37)
- Knight gains Fast at XL 7 (attrib.c:45)
- Healer starts with poison resistance at XL 1 (attrib.c:41)
- Ranger gains Searching XL 1, Stealth XL 7, See Invisible XL 15 (attrib.c:63-66)
- Elf gains sleep resistance at XL 4 (attrib.c:95)
- Cave Dweller starts with sling + flint stones (u_init.c:68-71)
- Ranger starts with +2 cloak of displacement (u_init.c:128)
- Wizard starts with cloak of MR + wand + rings + potions + scrolls + books + marker (u_init.c:167-176)
- Knight has intrinsic jumping from XL 1 (u_init.c:691)
- amethyst converts booze (not sickness) to fruit juice (potion.c:2161-2163)
- unicorn horn converts sickness to fruit juice (potion.c:2151-2154)
- Mjollnir is the Valkyrie sacrifice gift; needs a co-aligned altar (artilist.h:109)
- Knight code penalizes attacks on fleeing or helpless monsters (uhitm.c:336-339); peaceful kill is Samurai's giri
- all 13 role alignment/race availabilities (role.c)
- race stat caps (Str/Int/Wis/Dex/Con/Cha): Human {STR18(100),18,18,18,18,18} (role.c:597-598); Elf {18,20,20,18,16,18} (role.c:617-618); Dwarf {STR18(100),16,16,20,20,16} (role.c:637-638); Gnome {STR18(50),19,18,18,18,18} (role.c:657-658); Orc {STR18(50),16,16,18,18,16} (role.c:677-678)
- race stat FLOORS are uniformly {3,3,3,3,3,3} for every race (role.c:597, 617, 637, 657, 677)
- race intrinsic tables (attrib.c:91-105): hum_abil=none; dwa_abil=Infravision@XL1; elf_abil=Infravision@XL1+Sleep_resistance@XL4; gno_abil=Infravision@XL1; orc_abil=Infravision+Poison_resistance both@XL1
- initial roll distributes 75 points starting from role attrbase, clipped by race ATTRMAX, floor ATTRMIN=3 (attrib.c:723-737, init_attr_role_redist at 699-718); initial values typically land well below the race cap
- strategy aligned with NetHackWiki Valkyrie, Excalibur: Valkyrie is widely cited as the easiest beginner role; Knight 1-in-6 Excalibur dip at XL 5+ confirmed (https://nethackwiki.com/wiki/Valkyrie, https://nethackwiki.com/wiki/Excalibur)
-->

The first decision you'll make, before you even set foot on the
stairs, is who you are. In the Mazes, this means three things: your
**role**, your **race**, and your **alignment**. Together, these
determine your starting equipment, your natural abilities, which gods
hear your prayers, and which artifacts you can safely handle.

Don't agonize over this choice too much on your first few trips. You
will die regardless, and each death teaches something. But if you'd
like a recommendation for a first expedition, read on.

#### The Roles

There are thirteen roles available to adventurers. Each comes with
different starting equipment, different intrinsic abilities gained at
various experience levels, and a different quest to complete in the
mid-game.

**Archeologist.** You start with a bullwhip, a pickaxe, a tinning
kit, and a touchstone. The pickaxe is the kit's workhorse: it
lets you dig through walls and create your own escape routes from
the very first level. The tinning kit lets you preserve corpses
for later, and the touchstone is your gem-identification edge:
rub a gem on it and the game tells you whether it's the real
thing or worthless glass. Useful for unicorn negotiation and shop
pricing. Archeologists are capable and flexible, though a bit
fragile in early combat. *Alignment: Lawful or Neutral.*

**Barbarian.** You start strong. Literally. A two-handed sword and
good starting strength mean you can hack through early monsters with
ease. The downside is that two-handed weapons prevent you from using a
shield, and Barbarians are not known for their finesse. You do get
poison resistance from the start, which saves you from several common
early deaths. A straightforward role for players who like straightforward
solutions. *Alignment: Neutral or Chaotic.*

**Cave Dweller.** You start primitive but tough, with a club, a
sling, and a pile of flint stones for it. You gain speed by
mid-game and your hit dice are generous. The Cave Dweller's
simplicity is a virtue: fewer tools, fewer things to manage.
*Alignment: Lawful or Neutral.*

**Healer.** You begin with a stethoscope, four potions of healing
and four of extra healing, a **wand of sleep**, three **blessed
spellbooks** (healing, extra healing, stone-to-flesh, all
guaranteed to read), and poison resistance. The stethoscope lets
you check a monster's hit points and your own internal state; the
wand of sleep makes Healers a stronger early-game combatant than
the medical kit suggests. You're also **immune to sickness**, so
unknown potions of sickness become a free quaff-test (dip a
unicorn horn into them to convert to fruit juice).
*Alignment: Neutral.*

**Knight.** You start mounted on a saddled pony, with a +1 long sword
and a +1 lance among your gear. The pony is a decent combatant early
on and the basis of your unique trick: jousting from horseback with
the lance is devastating when it connects, though the lance is largely
useless on foot. As a Lawful character with a starting long sword, you
also have the best odds in the game at **Excalibur**. Dip your long sword
in a fountain at experience level 5+ and Knights get a 1-in-6 chance
per dip, far better than the 1-in-30 every other Lawful role faces.
Knights follow a code of conduct that imposes alignment penalties
for attacking fleeing or helpless monsters, so pick your fights
carefully. Knights also have intrinsic jumping, which lets you
reposition without spending an attack. *Alignment: Lawful.*

**Monk.** You fight best with bare hands and start with no weapon
at all. Monks gain martial arts abilities as they level, eventually
becoming formidable unarmed combatants. You start with sleep
resistance and see invisible, and you should avoid eating meat if
you want to maintain your spiritual discipline. **Mind what you
wear:** body armor costs −20 to-hit, a shield disables your
martial-arts hit bonus, and metallic helmets, gloves, or boots
each add a casting penalty. The starting robe is a cloak (not
body armor) and adds a 20-point spellcasting bonus, larger than
the Wizard's own. Keep wearing it. One of the more unusual roles,
rewarding for experienced players. *Alignment: Any.*

**Priest.** You start with a mace, four potions of holy water, and
the ability to intuitively sense whether items are blessed, cursed,
or uncursed, so you know on sight whether that cloak you just found
is safe to wear. Competent fighters with access to clerical spells.
Your first sacrifice gift is guaranteed: Demonbane (now a silver
mace), which aligns with your weapon skill — sacrifice early and
often. Keep at least one holy water in reserve: dipping plain water
into it makes more, indefinitely. *Alignment: Any (matches your god).*

**Ranger.** You start with a bow, a generous supply of arrows, a
dagger, and a **+2 cloak of displacement** — one of the strongest
defensive starts in the game. You're unmatched as an early-game
ranged threat. Rangers gain Searching at XL 1, Stealth at XL 7,
and See Invisible at XL 15. Your elven racial option grants sleep
resistance at XL 4. Hoard the +2 stack of arrows; they break at
roughly 25% per hit while +0s break around 67%. Mulch the cheap
stack on the level-1 newts. *Alignment: Neutral or Chaotic.*

**Rogue.** NetHack's thief class: lockpicking and stealthy
assassinations. You start with a short sword, six daggers for
throwing, leather armor, a lock pick, a sack, and a potion of
sickness (toss it at an enemy, or save it to coat any darts,
shuriken, or arrows you find — only missiles can be poisoned).
Your lock pick makes every locked door, chest, and box openable from
turn one. You get stealth from the beginning, which lets you walk up
to sleeping enemies without waking them, and your backstab ability
deals extra damage (+1 to +your level) when you hit a monster that's
fleeing or helpless. Throw daggers rather than stab with them:
Rogues get a multishot bonus on thrown daggers, and the backstab
modifier applies to throws against fleeing targets too. Stealth
and range are the role. *Alignment: Chaotic.*

**Samurai.** You start with a katana, which is one of the better
one-handed weapons in the game, plus a wakizashi backup and a yumi
bow with arrows. Samurai get speed early and have a strong martial
kit overall. The katana's damage output carries you through the
early game with ease. The wakizashi is community-classified
dead weight: drop it and find a long sword for the off-hand
instead, since long sword shares katana skill for two-weapon.
*Alignment: Lawful.*

**Tourist.** You start with a Hawaiian shirt, a credit card, an
expensive camera, a truly absurd number of +2 darts, two potions
of extra healing, and four scrolls of magic mapping. Tourists
have weak combat and a fragile early game (this is the hardest of
the standard roles), but the mapping scrolls take the edge off
exploration and the darts train ranged skills fast. Most runs
lean on a **camera-flash blinding** of whatever's closest,
follow-up darts from range, and the pet to finish. A good role
for players who have ascended before and want a real challenge.
*Alignment: Neutral.*

**Valkyrie.** The standard recommendation for a first serious
attempt. You start with a spear, a small shield, and cold
resistance; strong combat stats and good starting equipment do
the rest. **Mjollnir** (+d5/+d24 war hammer that returns when
thrown at Strength 25) drops as your sacrifice gift regardless
of alignment, and is what you'll wield by the late game.
*Alignment: Lawful or Neutral. Female only.*

**Wizard.** You start with a quarterstaff, a **cloak of magic
resistance** (an endgame-quality item from turn one), a wand, two
rings, three potions, three scrolls, the force-bolt spell plus a
random spellbook, and a high-enchantment magic marker. Physical
combat is terrible, so spells are the answer: fragile early,
overwhelming late. Advancing a spell-school skill (new in 5.0)
also identifies spellbooks of that school by appearance, so you
get free book-ID just by casting (see
[Spellcasting](#spellcasting)). Two warnings — Wizards start with
*zero* food rations and a kitten that won't share lunch, and force
bolt shatters potions on the ground and breaks any mirror a nymph
is carrying. Keep the quarterstaff wielded while you cast: any
quarterstaff lowers spell-failure rate, a small free bonus on top
of the cloak. *Alignment: Neutral or Chaotic.*

#### The Races

Your race affects your starting and maximum attributes, and which
intrinsics you get. All stats range from 3 and higher; the table
below shows the maximum each race can reach for each attribute.

| Race  | Str    | Int | Wis | Dex | Con | Cha | Intrinsics                     |
|-------|--------|-----|-----|-----|-----|-----|--------------------------------|
| Human | 18/100 | 18  | 18  | 18  | 18  | 18  | —                              |
| Elf   | 18     | 20  | 20  | 18  | 16  | 18  | Infravision; sleep res at XL 4 |
| Dwarf | 18/100 | 16  | 16  | 20  | 20  | 16  | Infravision                    |
| Gnome | 18/50  | 19  | 18  | 18  | 18  | 18  | Infravision                    |
| Orc   | 18/50  | 16  | 16  | 18  | 18  | 16  | Infravision, poison res        |

**Human.** No infravision, no poison resistance, no special
talents. On the bright side, every role is open to you and
nobody in the dungeon singles you out for being one.
Perfectly serviceable.

**Dwarf.** Sturdy fighters with the best Dex and Con caps and
matching human Strength. Infravision (the ability to see
warm-blooded creatures in the dark) from level 1. Available
for: Archeologist, Cave Dweller, Valkyrie.

**Elf.** Infravision plus sleep resistance at XL 4. Fragile compared
to humans but with the best Int and Wis caps. Elf Priests and
Wizards get a free musical instrument. Available for: Priest,
Ranger, Wizard.

**Gnome.** Small but resourceful; slightly higher Int cap than a
human. Available for: Archeologist, Cave Dweller, Healer, Ranger,
Wizard.

**Orc.** Poison resistance from level 1 is genuinely useful. Lower
stat caps overall, and humans, elves, and dwarves are race-hostile
to orcs (shopkeepers, priests, watchmen included); other orcs aren't
automatically peaceful either. Available for: Barbarian, Ranger,
Rogue, Wizard.

#### Alignment

Your alignment (Lawful, Neutral, or Chaotic) determines which gods
you worship, which artifacts you can safely use, and how certain
actions affect your standing. It's tempting to think of these as
"good," "balanced," and "evil," but it's more nuanced than that.

The key thing to understand about alignment is that it's a number.
Every action that matches your alignment's expectations increases it;
actions that violate your alignment's code decrease it. Your alignment
record affects your relationship with your god, which in turn affects
whether prayer will save you or smite you.

**Lawful** characters should avoid attacking peaceful creatures and
should never murder. Sacrifice frequently at co-aligned altars.
Lawful has the advantage of access to Excalibur, a top-tier melee
weapon obtainable as early as experience level 5.

**Neutral** characters have the most flexibility. You can get away
with more than a Lawful character, but your god still frowns on
truly chaotic behavior. Neutral has access to some excellent quest
artifacts.

**Chaotic** characters can kill with relative impunity but should
avoid pious behavior that doesn't match their dark patron's
expectations. Chaotic is often paired with Rogue for thematic
consistency.

For your first game: **Lawful or Neutral Valkyrie, Human or Dwarf.** Strong
combat, cold resistance, and Mjollnir waiting at the first
co-aligned altar you can sacrifice on. It's the closest thing to
an easy mode the Mazes offer, which is to say it's still very
hard.

---

<!-- audit
2026-05-18:
- tripe rations are dog food for typical PCs (eat.c:2138-2145)
- orcs and carnivores enjoy tripe (eat.c:2132-2136)
- altar BUC flash is amber/black and sets bknown (do.c:363-389)
- pets avoid cursed items (dogmove.c:535-536, 1065-1067)
- touchstone identifies gems (apply.c:2658-2696)
- floating-eye paralysis fires on melee against the eye (uhitm.c:5853, 6022)
- Burdened status label (botl.c:12)
- food ration weight and nutrition (objects.h:1110)
- strategy aligned with NetHackWiki Curse-testing, Altar: altar amber/black flash and pet step-avoidance are confirmed canonical curse-testing techniques (https://nethackwiki.com/wiki/Curse-testing, https://nethackwiki.com/wiki/Altar)
-->
### What to Pack

Your starting kit is fixed by your role and suited to its strengths,
but you'll want to improve on it. In the early game, keep an eye out
for these items as you descend. They'll shore up most roles'
weaknesses.

#### The Early Shopping List

**A source of nutrition.** You will get hungry. It happens faster
than you think. But your main food source isn't going to be the
rations in your pack. Unless you're playing a vegetarian role,
**most of your food in the early dungeon is the corpses of the
things you kill.** Eat fresh kills as you go, and rations become
emergency backup rather than the main course. Grab every food
ration you see, sure, but two or three is plenty to carry; you
don't need to hoard. Tripe rations are for your pet, not for you.

**A way to identify things.** In the early game, your primary
identification tools are altars (drop items to see if they flash
blessed/cursed), your pet (it won't step on cursed items), and
experimentation. A scroll of identify is valuable, but you might not
find one for a while. A touchstone (a gray stone that identifies gems)
is helpful but not urgent.

**Armor improvements.** Whatever you're wearing, you can probably do
better. Look for cloaks, helmets, gloves, and boots to fill empty
equipment slots. Even basic items like a helmet or pair of gloves
provide armor class benefits and can protect against specific attacks.

**A ranged attack.** Daggers, darts, or a bow with arrows. Fighting
from range is almost always safer than melee, and some monsters (like
floating eyes) should never be fought in melee.

**Supply chests.** Some of the large boxes and chests you find on
the levels above the Oracle are special supply chests. They are
usually locked but stocked with useful magical items: healing or
gain-energy potions, enchant-weapon or enchant-armor scrolls,
sometimes a wand of digging or a low-level spellbook. About
two-thirds of the early levels have one. Picking or `#force`ing them
open is almost always worth the time.

**Restraint.** New adventurers pick up everything they find. Veterans
pick up everything they need. The difference is about forty pounds
and the ability to outrun a gnome lord. If your status line reads
"Burdened," you're carrying more than you can use. You are also
moving slow enough for some monsters to land two hits per one of
yours. When your pile of stuff gets too heavy, drop the non-essentials.
Careful about what you leave for monsters, though. Remember that
monsters can pick up what you drop, and they can loot containers.
You can drop stuff a level up; monsters don't carry stashes between
levels.

---

### Your First Descent
<!-- audit
2026-05-21:
- poison-resistance corpse list for Rule 6, all with MR_POISON in both mresists and mconveys: killer bee (monsters.h:100), cave spider (monsters.h:944), yellow mold (monsters.h:1636); black pudding glob also conveys MR_POISON via mconveys (monsters.h:2118)
- puddings carry G_NOCORPSE (monsters.h:2114) so there is no CORPSE object, but on death they drop a GLOB_OF_BLACK_PUDDING / GLOB_OF_BROWN_PUDDING / etc. food item (mon.c:715-734 mksobj_at)
- eating a glob takes the same intrinsic path as eating a corpse: `piece->otyp == CORPSE || piece->globby` both trigger cpostfx(corpsenm) which calls givit() for each conveyed property (eat.c:562, 2040, 2984)
- kicking a sink can summon a black pudding: 4/5 outcomes are klunk, otherwise 1/3 chance of black pudding (dokick.c:1201-1238) — the canonical beginner trick to roll cold+shock+poison resistance globs
- magic resistance and reflection have no intrinsic source for players in 5.0; both come only from extrinsics: GDSM (do_wear.c:806-883), amulet of reflection, cloak of MR, silver shield, silver/gray DSM
2026-05-18:
- stair-falling damage is 1-3 HP via rnd(3) (do.c:1780-1795)
- floating-eye paralysis (mhitu.c:2536-2557)
- pets step around their owner (dogmove.c:535)
- lizard and lichen corpses never rot (eat.c:58-61)
- killer bees: speed 18, G_LGROUP, M1_POIS sting AT_STNG/AD_DRST 1d3 (monsters.h:96-102)
- supply chests appear above Oracle: at most one per level (placed in a random fillable room); 2/3 chance per level; 2/3 chest vs 1/3 large box; 5/6 locked (mklev.c:1010-1119)
- prayer cooldown averages ~1000 turns: rnz(300)/rnz(350) scaled by rne(4) (pray.c:780, 1356, 1819)
- corpse safe within 30 turns; tainted past ~175 turns (eat.c:1887, 1939)
- strategy aligned with NetHackWiki Stoning, Prayer, Magic resistance: lizard corpse as petrification cure, prayer-when-in-Trouble cooldown, and MR/reflection/poison-resistance "big three" are canonical advice (https://nethackwiki.com/wiki/Stoning, https://nethackwiki.com/wiki/Prayer, https://nethackwiki.com/wiki/Magic_resistance)
-->

You step down the stairs. The air is cool and damp. A corridor
stretches before you, branching into darkness. Your pet trots
beside you.

Welcome to the dungeon.

The first few levels of the Mazes are designed to ease you in, which
is a relative term. Monsters are weaker, but you are too. Your gear is
minimal, your hit points are low, and you don't yet have the
resistances that make the mid-game survivable. Levels one through
five are where the most characters die, not because the threats
are the greatest, but because you have the fewest resources to
deal with them.

#### The Golden Rules of Early Survival

**Rule 1: Don't fight what you can't beat.** This sounds obvious, but
it's the single most violated principle in the Mazes. If a monster is
too tough for you, walk away. Use corridors as chokepoints. Funnel
enemies so you fight them one at a time. If you stumble into a room
full of monsters, step back into the corridor and force them to come
to you in single file.

```
  Bad: fighting in the open       Good: corridor chokepoint

  ┌─────·──────┐                  ┌─────·──────┐
  │·Z··Z·······│                  │·Z···Z······│
  │··Z·@·Z·Z···│                  │··Z··Z······│
  │····Z·······│                  │·Z··········+##@
  │··Z·········│                  │··Z·········│
  └────────────┘                  └────────────┘

  You're surrounded.              They come to you one at a time.
```

**Rule 2: Don't eat things you don't understand.** Monster corpses
can grant powerful intrinsics, or they can poison you, give you food
poisoning, or worse. Until you know what a corpse does, leave it on
the ground. (Kobold `k` meat, for example, is poisonous and confers
nothing.) The exceptions: you can always safely eat food rations,
lembas wafers, cram rations, and fruits. Lichen corpses are safe and
never rot. Lizard corpses are safe, never rot, and cure
petrification — keep one in *open* inventory, not buried in a bag:
if a cockatrice touches you, you have two turns to chew. Newt
corpses are safe, and they sometimes restore 1–3 Pw, which is the
first sustainable mana source a spellcaster will see.

**Rule 3: Your pet is your friend.** Your starting pet is more useful
than it appears. It will fight alongside you, pick up items (which
tells you they're not cursed, since pets avoid cursed items on the ground),
and can even be trained to steal from shops. Keep it fed by dropping
tripe rations or corpses near it. A healthy, well-fed pet is one of
your best early assets.

**Rule 4: Learn to pray.** If you are about to die (hit points
critically low, starving, turning to stone) you
can pray to your god for help. In the early game, with decent
alignment, prayer will almost certainly save you. But you can only
pray about once every thousand turns or so, and praying at the
wrong time (when your god is angry, when you're in Gehennom, or
when you've prayed too recently) can make things much worse. Think
of prayer as an emergency button with a cooldown. Don't waste it
on minor problems (see [Divine Relations](#divine-relations) for
the full mechanics). If you've blundered into a peaceful and your
alignment tanks, you can grind it back by killing the always-hostile
classes (fungi `F`, fluids and oozes, insects); a clean ledger is
worth the detour.

**Rule 5: Explore thoroughly but move purposefully.** Every turn you
spend in the dungeon costs nutrition. If you stand around for hundreds
of turns, you'll starve. But rushing past rooms means missing
items you need. The sweet spot is to explore each level fairly
completely (check rooms, open doors, look for hidden passages) but
don't grind. When you've found what the level has to offer, move on.

**Rule 6: Build your defenses.** In the first half of the game,
your real goal isn't accumulating treasure. It's acquiring the
resistances and protections that will help you survive the late
game. The three most important are **magic resistance**,
**reflection**, and **poison resistance**. Poison
resistance can be acquired as an *intrinsic* by eating the right
corpse, like a killer bee, a cave spider, a yellow mold, or a
[black pudding](#a-note-on-puddings) kicked from a sink.
Magic resistance and reflection come from special gear: scale
mail made from the hide of a slain dragon (gray for MR, silver
for reflection), a special cloak (of MR) or amulet (of
reflection), a polished silver shield (reflection too), or a
one-of-a-kind artifact bestowed by your
god, won on the Quest, or granted as a wish. Your adventure will be
shaped by the protective items you obtain.

#### Dungeon Hazards (and How to Survive Them)

Here's a short list of common early deaths and how to prevent them:

**Starvation.** Eat when you're Hungry (the status message), not
when you're Weak or Fainting. If you're Fainting, pray immediately.
Pick up every food ration you find.

**Floating eyes.** They're the `e` on the map. Small, blue, and
seemingly harmless. If you hit one in melee, you'll be paralyzed, and
every monster in the vicinity will take free shots at your frozen body.
Use ranged attacks, or just walk around them. They are very slow.

**Rotted corpses.** If you eat a corpse that's been on the ground too
long, you'll get food poisoning, which is lethal without treatment.
Eat corpses fresh — within about 30 turns of the kill for a guaranteed-safe meal. Past that, the rot roll turns random; past ~175 turns an uncursed corpse is certainly tainted.
If you do get food poisoning, pray immediately.

**Falling down stairs while overburdened.** If you're carrying too
much, taking the stairs can make you tumble for 1–3 HP. Annoying
rather than dangerous, unless you're carrying a cockatrice corpse:
the tumble counts as touching it, and stairs become the most
literal instadeath in the game.

**Caught in the open by a pack.** Jackals are the single most common
cause of death on the public server. They bite for 1d2, but packs
of four to seven spawn on the upper levels and surround you in
open rooms. Killer bees, foxes, soldier ants, dwarves, and gnomes
all kill in this same shape. Retreat to a doorway or corridor at
the first sign of more than two attackers; they can only approach
single-file there.

**Pushing too quickly into the Mines.** The problem isn't depth,
it's getting there too early. The deeper Mines below Minetown are
crowded with armored dwarves and gnome rulers, second only to
jackals as a public-server killer. If your gear and experience
level aren't ready for armored melee fighters in packs, head back
up to the main Dungeons of Doom branch and come back to the Mines
later.

#### Supply Containers

New in NetHack 5.0: somebody has been leaving care packages.

Every level above the Oracle has a 2/3 chance of hosting a "supply
chest": usually a chest (sometimes a large box), usually locked,
seeded with at least one survivability item. The contents pool:
potion of healing (about a 50% chance per chest, sometimes a pair),
or otherwise potion of extra healing / speed / gain energy, scroll
of enchant weapon, enchant armor, confuse monster, or scare monster,
wand of digging, or spellbook of healing. There's also a 2/3 chance
of an extra random item, biased toward low-level spellbooks. The
Mines branch level gets a different gift: a guaranteed food ration,
cram ration, or lembas wafer.

These look like ordinary containers, no special marking. On your
first ten levels, check every chest and large box you find. A
locked one will yield to a credit card, a key, a wand of opening,
or you can `#force` the issue with a weapon you don't mind
breaking. An orcish dagger off the first orc you kill is
a perfect tool (pet-test it first: could be cursed). The contents aren't guaranteed
to change your run, but finding a stack of healing potions on level
4 before you've learned the hard way how much you need them is the
dungeon's act of goodwill.

---

## Part Two: Dungeon Sights

```{=latex}
\vspace*{0.6in}
```

### The Lay of the Land
<!-- audit
2026-05-21:
- branch staircases render with the S_brupstair / S_brdnstair symbols in CLR_YELLOW (defsym.h:124-125)
- the brupstair / brdnstair glyph is only selected after known_branch_stairs is true: the stair leads to a different dungeon AND the hero has traversed it (stairs.c:180-183, display.c:2347-2354)
2026-05-18:
- DoD is 25-29 levels (rn1(5,25) = rn2(5)+25) (dungeon.lua:10-11, hack.h:1535)
- Gnomish Mines branch DL 2-4 (dungeon.lua:15-19)
- Oracle DL 5-9 (dungeon.lua:60-66)
- Sokoban entry is one level above the Oracle, going up (dungeon.lua:20-25)
- 4 Sokoban levels with 2 fixed variants each (dat/soko*.lua)
- Big Room 40% chance, DL 10-12 (dungeon.lua:66-73)
- Quest portal DL 11-16 (dungeon.lua:26-31; chainlevel oracle base=6 range=2)
- Rogue Level DL 15-18 (dungeon.lua:52-58)
- Fort Ludios portal placed at any DL 11 up to just above Medusa, 1/3 per qualifying level (mklev.c:2647-2651)
- Medusa DL ~21-25 (dungeon.lua:74-80)
- Castle at bottom of DoD, DL ~27 (dungeon.lua:81-83)
- Mine's End: 3 variants, all guarantee a not-cursed luckstone (minend-1.lua:77, minend-2.lua:116, minend-3.lua:67)
- 7 Minetown variants; 1-in-7 is Orcish Town (minetn-1.lua, dungeon.lua:179-184)
- 5.0 sink glyph is white `{`, shared with bright-blue fountain (defsym.h:133, fixes5-0-0.txt:827)
- Travel/farlook matches on displayed symbol; `#` no longer cycles to sinks (getpos.c:1046-1062)
- Trap room places 1 randomly chosen trap type from 8 (themerms.lua:101-114)
- Teleportation hub places 2-4 fixed-destination teleporters (themerms.lua:264-279)
- Fake Delphi is a geometric joke: empty room within an Oracle-shaped room, no monsters (themerms.lua:291-305)
- Light source room places exactly one lit oil lamp (themerms.lua:204-210)
- Massacre places 5-25 role corpses only — no wraith (themerms.lua:172-189)
- Mausoleum places one waiting M/V/L/Z monster or one @ corpse (themerms.lua:419-443)
-->

The Mazes are procedurally generated. No two visits are quite the
same. But the dungeon follows patterns, and understanding those
patterns is the first step toward navigating them effectively.

#### The Big Picture

When Jay Fenlason wrote the original *Hack* in 1982, every level
in the dungeon looked the same: rooms, corridors, a staircase down
to more of the same. More than forty years of community
development later, the Dungeons of Doom you first descend into are
only one neighborhood of a much larger world. If you survive long
enough, your adventure will lead you through towns, towers, and
castles; swamps and islands and fortresses; an underworld of
molten halls and four elemental planes that climb back to a temple
where angels and demons do battle around the altars to the gods.
Each landmark has its own architecture, its own inhabitants, and
its own rewards. Every game is different, but the dungeon has a
story to tell: an arc through a familiar cast of landmarks, each
tougher and stranger than the last.

The dungeon is a branching tree with a main trunk that descends
through three main phases. Off the trunk are several optional side
branches that you will want to explore along the way. The exact
depths and layouts vary from game to game, but the diagram that
follows shows the typical shape. Knowing where you are in this
tree helps you know what's coming.

The **Dungeons of Doom** form the upper half, roughly levels 1
through 27. Side branches lead to the **Gnomish Mines** (where
you can find a *[luckstone](#luck-and-fortune)* and
*[shops](#shopping-and-shopkeeper-pricing)*), **Sokoban** (a
*[puzzle](#sokoban)* with a prize at the top), your
[Quest dungeon](#the-quest), and sometimes **Fort Ludios** (a vault
full of gold). The trunk ends at **The Castle**, the gateway to
Gehennom.

**Gehennom** is the lower half: maze levels and demon lords,
with the **Amulet of Yendor** at the bottom in Moloch's Sanctum.
Once you have it, you climb back up through the **Elemental
Planes** to the **Astral Plane**, where your god awaits your
offering.

<!-- DMAP-BEGIN -->
<div><figure style="margin: 1.5em 0; text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 611" role="img" aria-label="Dungeons of Doom map" style="display:block;margin:0 auto;max-width:760px;width:100%;height:auto;font-family:'EB Garamond','Garamond','Georgia',serif;font-feature-settings:'liga' 0, 'dlig' 0;"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker></defs><line x1="380" y1="55" x2="380" y2="611" stroke="#B5651D" stroke-width="2.5" fill="none"/><rect x="40" y="0" width="680" height="39" rx="4" fill="#B5651D"/><text x="380" y="26" font-size="22" font-weight="600" fill="#fff" text-anchor="middle" letter-spacing="0.08em">DUNGEONS OF DOOM</text><line x1="150" y1="140" x2="150" y2="246" stroke="#5B8E3A" stroke-width="2" fill="none"/><line x1="630" y1="166" x2="630" y2="194" stroke="#B58A1A" stroke-width="2" fill="none"/><line x1="630" y1="305" x2="630" y2="343" stroke="#3B6FA0" stroke-width="2" fill="none"/><rect x="290" y="55" width="180" height="40" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="72" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">The Dungeon Entrance</text><text x="380" y="89" font-size="12" font-style="italic" fill="#555" text-anchor="middle">up-stair to exit</text><rect x="60" y="108" width="180" height="32" rx="6" fill="#E8F4DC" stroke="#5B8E3A" stroke-width="1.5"/><text x="150" y="129" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Gnomish Mines</text><rect x="60" y="168" width="180" height="40" rx="6" fill="#E8F4DC" stroke="#5B8E3A" stroke-width="1.5"/><text x="150" y="185" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Minetown</text><text x="150" y="202" font-size="12" font-style="italic" fill="#555" text-anchor="middle">shops, temple</text><rect x="60" y="246" width="180" height="40" rx="6" fill="#E8F4DC" stroke="#5B8E3A" stroke-width="1.5"/><text x="150" y="263" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Mine's End</text><text x="150" y="280" font-size="12" font-style="italic" fill="#555" text-anchor="middle">luckstone</text><rect x="290" y="163" width="180" height="40" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="180" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">The Oracle</text><text x="380" y="197" font-size="12" font-style="italic" fill="#555" text-anchor="middle">paid hints</text><rect x="540" y="126" width="180" height="40" rx="6" fill="#FFF4CC" stroke="#B58A1A" stroke-width="1.5"/><text x="630" y="143" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Sokoban prize</text><text x="630" y="160" font-size="12" font-style="italic" fill="#555" text-anchor="middle">bag of holding/amulet of reflection</text><rect x="540" y="194" width="180" height="32" rx="6" fill="#FFF4CC" stroke="#B58A1A" stroke-width="1.5"/><text x="630" y="215" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Sokoban entry</text><rect x="290" y="269" width="180" height="32" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="290" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle"><tspan>Q</tspan>uest portal</text><rect x="540" y="265" width="180" height="40" rx="6" fill="#DDE9F5" stroke="#3B6FA0" stroke-width="1.5"/><text x="630" y="282" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle"><tspan>Q</tspan>uest entry</text><text x="630" y="299" font-size="12" font-style="italic" fill="#555" text-anchor="middle">your role's dungeon</text><rect x="540" y="343" width="180" height="40" rx="6" fill="#DDE9F5" stroke="#3B6FA0" stroke-width="1.5"/><text x="630" y="360" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle"><tspan>Q</tspan>uest goal</text><text x="630" y="377" font-size="12" font-style="italic" fill="#555" text-anchor="middle">★ Bell of Opening, role artifact</text><rect x="290" y="329" width="180" height="32" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="350" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Big Room (40%)</text><rect x="290" y="389" width="180" height="32" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="410" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Rogue Level</text><rect x="60" y="420" width="180" height="40" rx="6" fill="#FFD966" stroke="#B5891A" stroke-width="1.5"/><text x="150" y="437" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Fort Ludios</text><text x="150" y="454" font-size="12" font-style="italic" fill="#555" text-anchor="middle">vault of gold</text><rect x="290" y="479" width="180" height="32" rx="6" fill="#B8D4F0" stroke="#2E5C8E" stroke-width="1.5"/><text x="380" y="500" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Medusa's Island</text><rect x="230" y="539" width="300" height="58" rx="8" fill="#FFFFFF" stroke="#B5891A" stroke-width="2.5"/><text x="380" y="565" font-size="17" font-weight="600" fill="#1f2933" text-anchor="middle">THE CASTLE</text><text x="380" y="582" font-size="14" font-style="italic" fill="#7A5A0A" text-anchor="middle">wand of wishing</text><line x1="380" y1="124" x2="240" y2="124" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><line x1="380" y1="210" x2="540" y2="210" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><line x1="470" y1="285" x2="540" y2="285" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><line x1="380" y1="440" x2="240" y2="440" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><text x="275" y="120" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">down</text><text x="500" y="206" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">up</text><text x="505" y="281" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">portal</text><text x="275" y="436" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">portal</text><circle cx="380" cy="124" r="4" fill="#B5651D"/><circle cx="380" cy="210" r="4" fill="#B5651D"/><circle cx="380" cy="440" r="4" fill="#B5651D"/><circle cx="380" cy="104.0" r="4" fill="#B5651D"/><circle cx="380" cy="114.0" r="4" fill="#B5651D"/><circle cx="150" cy="149.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="159.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="217.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="227.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="237.0" r="4" fill="#5B8E3A"/><circle cx="380" cy="134.0" r="4" fill="#B5651D"/><circle cx="380" cy="144.0" r="4" fill="#B5651D"/><circle cx="380" cy="154.0" r="4" fill="#B5651D"/><circle cx="630" cy="175.0" r="4" fill="#B58A1A"/><circle cx="630" cy="185.0" r="4" fill="#B58A1A"/><circle cx="380" cy="220.0" r="4" fill="#B5651D"/><circle cx="380" cy="230.0" r="4" fill="#B5651D"/><circle cx="380" cy="240.0" r="4" fill="#B5651D"/><circle cx="380" cy="250.0" r="4" fill="#B5651D"/><circle cx="380" cy="260.0" r="4" fill="#B5651D"/><circle cx="630" cy="314.0" r="4" fill="#3B6FA0"/><circle cx="630" cy="324.0" r="4" fill="#3B6FA0"/><circle cx="630" cy="334.0" r="4" fill="#3B6FA0"/><circle cx="380" cy="310.0" r="4" fill="#B5651D"/><circle cx="380" cy="320.0" r="4" fill="#B5651D"/><circle cx="380" cy="370.0" r="4" fill="#B5651D"/><circle cx="380" cy="380.0" r="4" fill="#B5651D"/><circle cx="380" cy="430.0" r="4" fill="#B5651D"/><circle cx="380" cy="450.0" r="4" fill="#B5651D"/><circle cx="380" cy="460.0" r="4" fill="#B5651D"/><circle cx="380" cy="470.0" r="4" fill="#B5651D"/><circle cx="380" cy="520.0" r="4" fill="#B5651D"/><circle cx="380" cy="530.0" r="4" fill="#B5651D"/></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 681" role="img" aria-label="Gehennom map" style="display:block;margin:0 auto;max-width:760px;width:100%;height:auto;font-family:'EB Garamond','Garamond','Georgia',serif;font-feature-settings:'liga' 0, 'dlig' 0;"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker></defs><line x1="380" y1="0" x2="380" y2="39" stroke="#B5651D" stroke-width="2.5" fill="none"/><line x1="380" y1="0" x2="380" y2="625" stroke="#A14A3F" stroke-width="2.5" fill="none"/><rect x="40" y="0" width="680" height="39" rx="4" fill="#A14A3F"/><text x="380" y="26" font-size="22" font-weight="600" fill="#fff" text-anchor="middle" letter-spacing="0.08em">GEHENNOM</text><line x1="150" y1="288" x2="150" y2="306" stroke="#6B4E96" stroke-width="2" fill="none"/><rect x="290" y="53" width="180" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="70" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Valley of the Dead</text><text x="380" y="87" font-size="12" font-style="italic" fill="#555" text-anchor="middle">Gehennom's entrance</text><rect x="290" y="141" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="162" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Asmodeus's Lair</text><rect x="290" y="191" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="212" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Juiblex's Swamp</text><rect x="290" y="251" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="272" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Baalzebub's Lair</text><rect x="60" y="248" width="180" height="40" rx="6" fill="#E3D8F0" stroke="#6B4E96" stroke-width="1.5"/><text x="150" y="265" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Vlad the Impaler</text><text x="150" y="282" font-size="12" font-style="italic" fill="#555" text-anchor="middle">★ Candelabrum</text><rect x="60" y="306" width="180" height="32" rx="6" fill="#E3D8F0" stroke="#6B4E96" stroke-width="1.5"/><text x="150" y="327" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Vlad's Tower</text><rect x="290" y="351" width="180" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="368" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Orcus Town</text><text x="380" y="385" font-size="12" font-style="italic" fill="#555" text-anchor="middle">Wand of Orcus · magic lamp/marker</text><rect x="290" y="419" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="440" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Wizard's Tower</text><rect x="290" y="469" width="180" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="486" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Wizard of Yendor</text><text x="380" y="503" font-size="12" font-style="italic" fill="#555" text-anchor="middle">★ Book of the Dead</text><rect x="230" y="567" width="300" height="58" rx="8" fill="#2D2D2D" stroke="#FFC857" stroke-width="2.5"/><text x="380" y="593" font-size="17" font-weight="600" fill="#FFC857" text-anchor="middle">Moloch's Sanctum</text><text x="380" y="610" font-size="14" font-style="italic" fill="#FFE680" text-anchor="middle">the Amulet of Yendor</text><line x1="380" y1="322" x2="240" y2="322" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><text x="275" y="318" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">up</text><circle cx="380" cy="322" r="4" fill="#A14A3F"/><circle cx="380" cy="102.0" r="4" fill="#A14A3F"/><circle cx="380" cy="112.0" r="4" fill="#A14A3F"/><circle cx="380" cy="122.0" r="4" fill="#A14A3F"/><circle cx="380" cy="132.0" r="4" fill="#A14A3F"/><circle cx="380" cy="182.0" r="4" fill="#A14A3F"/><circle cx="380" cy="232.0" r="4" fill="#A14A3F"/><circle cx="380" cy="242.0" r="4" fill="#A14A3F"/><circle cx="380" cy="292.0" r="4" fill="#A14A3F"/><circle cx="380" cy="302.0" r="4" fill="#A14A3F"/><circle cx="380" cy="312.0" r="4" fill="#A14A3F"/><circle cx="150" cy="297.0" r="4" fill="#6B4E96"/><circle cx="380" cy="332.0" r="4" fill="#A14A3F"/><circle cx="380" cy="342.0" r="4" fill="#A14A3F"/><circle cx="380" cy="400.0" r="4" fill="#A14A3F"/><circle cx="380" cy="410.0" r="4" fill="#A14A3F"/><circle cx="380" cy="460.0" r="4" fill="#A14A3F"/><circle cx="380" cy="518.0" r="4" fill="#A14A3F"/><circle cx="380" cy="528.0" r="4" fill="#A14A3F"/><circle cx="380" cy="538.0" r="4" fill="#A14A3F"/><circle cx="380" cy="548.0" r="4" fill="#A14A3F"/><circle cx="380" cy="558.0" r="4" fill="#A14A3F"/><line x1="380" y1="631" x2="380" y2="681" stroke="#5B8E3A" stroke-width="2.5" stroke-dasharray="7,5" fill="none"/><text x="400" y="661" font-size="15" font-weight="600" font-style="italic" fill="#5B8E3A">now go <tspan style="font-weight:800;font-size:17px">ALL</tspan> the way back up...</text></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 299" role="img" aria-label="Elemental Planes and Ascension" style="display:block;margin:0 auto;max-width:760px;width:100%;height:auto;font-family:'EB Garamond','Garamond','Georgia',serif;font-feature-settings:'liga' 0, 'dlig' 0;"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker></defs><rect x="40" y="0" width="680" height="39" rx="4" fill="#5D3C8E"/><text x="380" y="26" font-size="22" font-weight="600" fill="#fff" text-anchor="middle" letter-spacing="0.08em">THE ELEMENTAL PLANES</text><rect x="68" y="89" width="120" height="40" rx="6" fill="#E8DDC8" stroke="#8B6F47" stroke-width="1.5"/><text x="128" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Earth</text><rect x="236" y="89" width="120" height="40" rx="6" fill="#E0F4FA" stroke="#3B9FA8" stroke-width="1.5"/><text x="296" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Air</text><rect x="404" y="89" width="120" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="464" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Fire</text><rect x="572" y="89" width="120" height="40" rx="6" fill="#DDE9F5" stroke="#3B6FA0" stroke-width="1.5"/><text x="632" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Water</text><rect x="260" y="179" width="240" height="42" rx="6" fill="#D8C6F0" stroke="#5D3C8E" stroke-width="1.5"/><text x="380" y="197" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Astral Plane</text><text x="380" y="213" font-size="12" font-style="italic" fill="#555" text-anchor="middle">three altars · pick yours</text><rect x="230" y="239" width="300" height="50" rx="10" fill="#FFE680" stroke="#B5891A" stroke-width="2.5"/><text x="380" y="262" font-size="18" font-weight="700" fill="#7A5A0A" text-anchor="middle" letter-spacing="0.1em">ASCENSION</text><text x="380" y="281" font-size="11" font-style="italic" fill="#7A5A0A" text-anchor="middle">offer the Amulet at your altar</text><path d="M 380 39 C 380 53 128 53 128 67 L 128 89" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><line x1="188" y1="109" x2="236" y2="109" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><text x="212" y="105" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">portals</text><line x1="356" y1="109" x2="404" y2="109" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><line x1="524" y1="109" x2="572" y2="109" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><path d="M 632 129 C 632 143 380 143 380 157 L 380 179" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><line x1="380" y1="221" x2="380" y2="239" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/></svg><figcaption style="font-style: italic; color: #5a5a5a; font-size: 0.9em; margin-top: 0.5em;">Branches extend left and right of the main trunk. Pearls (small colored dots) indicate the approximate number of intervening dungeon levels. ★ marks the three Invocation items (Bell of Opening, Candelabrum, Book of the Dead) needed to enter Moloch's Sanctum and claim the Amulet.</figcaption></figure></div>
<!-- DMAP-END -->

Simple enough on paper. Surviving it is another matter.

#### The Map Symbols

Everything in the dungeon is represented by a symbol on the screen.
Learning to read these symbols quickly is important:

| Symbol   | Meaning                       |
| -------- | ----------------------------- |
| `.`      | Floor (room)                  |
| `#`      | Corridor                      |
| `-`  `│` | Wall (horizontal, vertical)   |
| `+`      | Closed door (or spellbook)    |
| `<`      | Stairs up                     |
| `>`      | Stairs down                   |
| `{`      | Fountain (bright blue) or sink (white) |
| `_`      | Altar                         |
| `\`      | Throne                        |
| `^`      | Trap (once revealed)          |
| `@`      | You (or a human-type monster) |

Letters represent monsters: `d` for dogs, `D` for dragons, `Z` for
zombies. Colors help distinguish within a class: a red `D` is a red
dragon, while a gray `D` is a gray dragon (see
[Field Guide to Dungeon Fauna](#field-guide-to-dungeon-fauna)).

**Color memo: branch staircases turn yellow.** Staircases that
lead into a sub-branch (Mines, Sokoban, the Quest, and so on)
display in yellow once you've used them. Ordinary main-trunk
stairs stay default-colored, so on a level with several stairs
the yellow one is your way back into the branch.

Item symbols are punctuation marks:

| Symbol | Item Class         |
| ------ | ------------------ |
| `)`    | Weapons            |
| `[`    | Armor              |
| `%`    | Food (comestibles) |
| `!`    | Potions            |
| `?`    | Scrolls            |
| `/`    | Wands              |
| `=`    | Rings              |
| `"`    | Amulets            |
| `(`    | Tools              |
| `+`    | Spellbooks         |
| `*`    | Gems and stones    |
| `$`    | Gold (zorkmids, abbreviated **zm**) |

#### Room Types

Most rooms in the dungeon are ordinary, empty or with a few items
and monsters scattered about. But some rooms are special:

```
   A shop:                 A zoo:                 A throne room:
   ┌───────┐               ┌────────┐             ┌────────┐
   │··[·?!·│               │Z··Z$Z··│             │··Z·Z·Z·│
   │···@···│               │$Z···$Z·│             │·Z·\··Z·│
   │!··)·/·│               │·Z$Z··Z$│             │··Z·Z···│
   └──+────┘               └───+────┘             └───+────┘
      #                        #                      #
   @ = shopkeeper          Z = sleeping           \ = throne
   Items for sale.         $ = gold piles         Monsters guard.
```

**Shops.** Identified by the shopkeeper standing in the doorway (or
inside). Shops sell items of a particular type: general
stores, armor shops, weapon shops, scroll shops, potion shops, and
more. Items on the shop floor belong to the shopkeeper; pick one up
and you'll be quoted a price. You can sell items too. Shopkeepers are
extremely powerful in combat, so don't steal unless you have a plan.

**Temples.** A room with an altar and a priest or priestess tending
it. The altar's alignment matters: if it matches yours, you can
sacrifice here for good effects. If it doesn't, the resident priest
won't be friendly about your attempts. The priest will also accept
gold donations in exchange for clairvoyance or a permanent AC bonus
— see [Donating to Priests](#donating-to-priests).

**Throne rooms.** A room with a [*throne* (`\`)](#thrones) and
usually surrounded by monsters. Sitting on the throne has random
effects, sometimes wonderful, sometimes terrible.

**Zoos.** A room packed with sleeping monsters and gold. They wake
**not** when you enter, but from the noise of you fighting the
first few. Fight from the doorway so they wake one or two at a
time, not all at once.

**Barracks.** A room full of soldiers. They're organized and armed,
but they're also carrying good equipment. Worth clearing if you can
handle the fight.

**Beehives.** A room full of killer bees and royal jelly. The bees
are dangerous in numbers, but royal jelly is excellent food.

**Themed Rooms.** You'll occasionally walk into rooms that are
not from the list above but interesting in other ways. These are
**Themed Rooms**, a new feature of 5.0, and there are dozens of
them. Some have unusual *shapes*, and some have unusual
*contents*. Interesting ones to look out for:

- **Light source rooms.** They reliably contain a lit oil
  lamp. Free torch.
- **Buried treasure.** A burned engraving somewhere on the floor
  reads *"Dig 3 east 2 south"* (or wherever) and points to a buried
  chest plus 3–12 random items. A pick-axe earns its weight here.
- **Massacre.** Floor strewn with adventurer-role corpses (rogue,
  ranger, valkyrie, etc.). Useful for sacrifice and for eating
  the safe ones for intrinsics if you know the role.
- **Mausoleum.** A small interior chamber with one waiting
  monster (mummy, vampire, lich, or zombie) or a human corpse.
  Open the door carefully.
- **Spider nest, buried zombies, trap room, teleportation hub.**
  These are traps in everything but name. Spider nest and buried
  zombies scale with level difficulty, so what looks innocuous
  on Dlvl 4 is rough on Dlvl 18. Trap rooms can be anything
  from arrow traps to anti-magic to land mines; recognize the
  pattern, retreat, prepare, return.
- **Light-and-frame rooms (pillars, room-in-a-room, blocked
  center).** Tactically excellent for setting up [Elbereth](#elbereth)
  squares or anchoring a polearm fight.

Themed rooms are mixed in with ordinary rooms; you can have
several on a single level. They make the early dungeon less
predictable in a friendly way: more terrain types to fight in,
more item discovery, and the occasional educational ambush.

---

### Field Guide to Dungeon Fauna
<!-- audit
2026-05-18:
- xan: AT_STNG AD_LEGS (sting cripples legs); xan is class `x`, not the engulfer `t` (S_TRAPPER) (monsters.h:1157-1159)
- leprechaun attack is AT_CLAW AD_SGLD (gold-steal claw), not a bite (monsters.h:660)
- long worms grow tail segments on a movement-driven wgrowtime timer, not per hit (worm.c:218-237)
- pudding split admits IRON|METAL weapons only (uhitm.c:1616-1618)
- there are no dragonhide weapons in 5.0; DRAGON_HIDE material is body-armor-only
- silver and wooden weapons are the actual pudding non-splitters (uhitm.c:1616-1620 admits IRON|METAL only)
- all other class-symbol mappings (defsym.h) and per-monster stats verified clean
- rothe ('q'-class fame): three attacks per turn (claw + two bites), the only Q-class monster lacking M2_STRONG, and the canonical early-q threat per NetHackWiki (https://nethackwiki.com/wiki/Rothe, https://nethackwiki.com/wiki/Quadruped)
-->


The Mazes are home to hundreds of monster species, organized into
classes denoted by letters. Lowercase letters are generally smaller
or less dangerous; uppercase letters are larger or more threatening.
Color further distinguishes individual species within a class.

Here is a quick field guide to what each letter means, roughly ordered
by how early you might encounter them. For the full level / speed /
AC / attack details on every monster, see the
[Bestiary Tables](#bestiary-tables) appendix.

#### Common Early Encounters

| Sym    | Class                  | Notes                                                                      |
| ------ | ---------------------- | -------------------------------------------------------------------------- |
| [`a`](#ants-and-insects-a)    | [Ants](#ants-and-insects-a)      | Soldier ants are a frequent early-game killer: speed 18, two attacks per turn (bite + strength-draining sting), and they travel in packs. A wandering soldier-ant group on Dlvl 4 can end a careless run. Killer bees, giant ants, fire ants are all the same shape of problem. |
| [`b`](#blobs-b)    | [Blobs](#blobs-b)     | Acidic or gelatinous. Acid blobs have no active attack — they only splash 1d8 acid back when *you* hit *them*, and the splash can corrode your weapon. Kill at range. Eat for [resistances](#useful-corpse-effects). |
| [`B`](#bats-and-birds-b)    | [Bats](#bats-and-birds-b)      | The `B` class is **deceptively dangerous because of speed**. Bats and giant bats clock in at speed 22 — nearly twice the player's base 12, so they get roughly two bites per one of your swings. Giant bats bite for 1d6 each; the math catches up fast. Vampire bats are still in the bat class but their second bite drains Strength (not levels). |
| [`d`](#dogs-and-canines-d)    | [Dogs and other canines](#dogs-and-canines-d) | The `d` class covers your starting pet (little dog, kitten via cat-class) **and** the most numerous early-game predators. **Jackals** are the single most common cause of death on the public server — they only bite for 1d2, but they spawn in packs and there are a *lot* of them on the upper levels. Foxes bite for 1d3 and are faster (speed 15) but spawn alone. Coyotes, dingos, wolves get progressively worse. Tame `d` (your pet, larger dogs you've fed up) help fight everything else. |
| [`e`](#eyes-and-spheres-e)    | [Eyes](#eyes-and-spheres-e)      | **Floating eyes paralyze on melee hit.** Never hit an `e` in melee. Use ranged attacks. (And eat them for telepathy.) Spheres (flaming/freezing/shocking) explode in a 3×3 area; also kill them at range. |
| [`f`](#felines-f)    | [Cats](#felines-f)      | Like dogs, often starting pets. Felines can be tamed with tripe.                        |
| [`G`](#gnomes-g)    | [Gnomes](#gnomes-g)    | The standard inhabitants of the Gnomish Mines. Individually weak, but the Mines have a lot of them — and **plain gnomes, gnome lords, and (later) gnome rulers are all in the top fifteen causes of death** on the public server, because mid-game players treat the Mines as a milk run and walk into a four-on-one with full-strength enemies. If you're a gnome yourself, most of them are peaceful. |
| [`h`](#humanoids-h)    | [Humanoids](#humanoids-h) | Dwarves, bugbears, mind flayers. Wide range of difficulty. **Dwarves in particular are dangerously underrated**: they hit harder than they look, they're armored, and they're the second most common cause of death on the public server because of how many you meet in the Mines. Don't trade blows with one in melee until your AC is solid. |
| [`i`](#imps-and-minor-demons-i)    | [Imps](#imps-and-minor-demons-i)      | Minor pests. Weak claw, regeneration, and a stream of insults — annoying but not dangerous. |
| [`j`](#jellies-j)    | [Jellies](#jellies-j)   | Spotted and ochre jellies. Passive acid damage on melee.                                |
| [`k`](#kobolds-k)    | [Kobolds](#kobolds-k)   | Weak individually but sometimes carry poisoned weapons.                                 |
| [`o`](#orcs-o)    | [Orcs](#orcs-o)      | Numerous and modest in strength one-on-one; dangerous in packs. Hill orcs and Mordor orcs are the common upper-dungeon variants. |
| [`r`](#rodents-r)    | [Rodents](#rodents-r)   | Rats and rock moles. Rock moles eat metal items, so protect your gear.                  |
| [`s`](#arachnids-and-centipedes-s)    | [Spiders](#arachnids-and-centipedes-s)   | Cave spiders are weak (eat them for poison resistance). Giant spiders poison.            |
| [`x`](#xans-and-fantastic-insects-x)    | [Grid bugs](#xans-and-fantastic-insects-x) | The weakest monster in the game; they can't even move diagonally. But they don't leave corpses. The `x` class also covers the much-later **xan**, whose sting cripples your legs (slow movement until it heals). |
| [`:`](#lizards)    | [Lizards](#lizards)   | Newts, geckos, and iguanas are individually weak — usually not too dangerous if you're paying attention. The class matters mostly for the corpses: **lizard corpses cure [petrification](#petrification-stoning)** (always carry one for cockatrice/Medusa insurance), and newt corpses may restore 1–3 mana. |

#### Mid-Dungeon Threats

| Sym    | Class             | Notes                                                                                                |
| ------ | ----------------- | ---------------------------------------------------------------------------------------------------- |
| [`A`](#angelic-beings-a)    | [Angels](#angelic-beings-a)            | Powerful, usually aligned. Don't fight your own.                                                     |
| [`C`](#centaurs-c)    | [Centaurs](#centaurs-c)          | Fast (speed 18-20). Half spawn with a bow or crossbow, but they'll still close into melee for weapon and kick attacks. Mountain centaurs hit hardest: 1d10 weapon plus *two* 1d6 kicks per turn. |
| [`E`](#elementals-e)    | [Elementals](#elementals-e)        | Hard to kill. Air elementals [engulf](#engulfment); earth elementals phase through walls. |
| [`f`](#felines-f)    | [Displacer beast](#felines-f)   | Cat-class, but vicious: AC −10, three-attack melee, and a 50% chance on each player melee to swap places with you instead. Eat the corpse for temporary intrinsic Displacement. |
| [`F`](#fungi-and-molds-f)    | [Fungi](#fungi-and-molds-f)             | Yellow mold, green mold, shriekers. Shriekers summon other monsters.                                 |
| [`g`](#gremlins-g)    | [Gremlins / gargoyles](#gremlins-g)   | Heavy claws plus a special trick. Gremlins **strip a random intrinsic on hit at night** and **multiply when wet** (don't kick one into a fountain). Gargoyles are slow but armored (AC −4) with three-attack salvos; winged gargoyles fly. |
| [`G`](#gnomes-g)    | [Gnome lords/kings](#gnomes-g) | Tougher gnomes. Still fairly manageable.                                                             |
| [`'`](#golems)    | [Golems](#golems)            | Built things. Iron golems hit hard and resist nearly everything; clay, stone, and wood golems are softer. Glass golems leave gems on death. |
| [`H`](#giant-humanoids-h)    | [Giants](#giant-humanoids-h)            | Strong melee, throw boulders. Giants carry gems.                                                     |
| [`J`](#jabberwocks-j)    | [Jabberwock](#jabberwocks-j)        | Rare, but if you see one you're in for a fight. Four 2d10 attacks per turn (two bites and two claws) at normal speed. |
| [`K`](#keystone-kops-k)    | [Keystone Kops](#keystone-kops-k)     | The shopkeeper-summoned constabulary. They appear when you steal, refuse to pay, or anger a shopkeeper. Individually weak but they swarm, and they jeer at you. |
| [`l`](#leprechauns-l)    | [Leprechauns](#leprechauns-l)       | Steal your gold and teleport away. A single claw can grab up to *all* of your purse. Hide gold in a sack, drop it elsewhere, or fight at range. |
| [`L`](#liches-l)    | [Liches](#liches-l)            | Spellcasters. Arch-liches are among the most dangerous monsters in the game.                         |
| [`m`](#mimics-m)    | [Mimics](#mimics-m)            | Disguised as items, walls, doors, fountains, altars, or boulders. See [A note on mimics](#a-note-on-mimics). |
| [`M`](#mummies-m)    | [Mummies](#mummies-m)           | Aggressive undead with physical claw attacks. Their corpses are dangerous to eat (age you). Mummy wrappings worn as a cloak block invisibility. That is usually a downside, but very useful if you've gone invisible and you need a shopkeeper to interact with you. |
| [`n`](#nymphs-n)    | [Nymphs](#nymphs-n)            | [Steal items from your inventory, then teleport away](#a-note-on-nymphs). Fight from range. |
| [`N`](#nagas-n)    | [Nagas](#nagas-n)             | Large serpent-bodied creatures. Red nagas breathe fire, black nagas spit acid, golden nagas cast spells, guardian nagas spit Str-drain poison and have a paralyzing bite. Tough; speeds 12–16. |
| [`O`](#ogres-o)    | [Ogres](#ogres-o)             | Strong melee fighters. Ogre lords and kings are tougher.                                             |
| [`p`](#piercers-p)    | [Piercers](#piercers-p)          | Disguise as stalactites; drop from the ceiling onto whatever walks below. The fall does serious damage. Hard to spot in advance. |
| [`P`](#puddings-and-oozes-p)    | [Puddings](#puddings-and-oozes-p)          | [Black and brown puddings split when hit in melee with an iron or metal weapon](#a-note-on-puddings) (scalpel and tsurugi count). Good to eat for [intrinsics](#useful-corpse-effects). |
| [`q`](#quadrupeds-q)    | [Quadrupeds](#quadrupeds-q)        | Multi-attack mid-game bruisers. The **rothe** is the famous one (three attacks per turn at sluggish speed 9, dangerous in packs); mumakil are solo two-attack bruisers (4d12 butt + 2d6 bite).                              |
| [`R`](#rust-monsters-and-disenchanters-r)    | [Rust monster / disenchanter](#rust-monsters-and-disenchanters-r) | Rust monsters corrode worn iron armor when they hit you, and your wielded iron weapon when you hit them. Use non-iron alternatives (mithril, silver, dragonhide) or take iron gear off before the fight; iron items in your inventory aren't touched. **Disenchanters** drain enchantment on hit; see [Enchantment Drain](#enchantment-drain). |
| [`S`](#snakes-s)    | [Snakes](#snakes-s)            | Cobras and pit vipers poison. Water moccasins come from fountains.                                   |
| [`t`](#trappers-and-lurkers-t)    | [Trappers / lurkers above](#trappers-and-lurkers-t) | Hide in plain sight on floor or ceiling and [engulf you](#engulfment) when you walk under/onto them. |
| [`T`](#trolls-t)    | [Trolls](#trolls-t)            | [Regenerate. They come back from the dead unless you eat or tin the corpse](#a-note-on-trolls). |
| [`u`](#unicorns-and-horses-u)    | [Horses / unicorns](#unicorns-and-horses-u) | Horses are usually mountable, mostly peaceful in the wild. Unicorns are color-coded by alignment: same-aligned spawn peaceful, cross-aligned hostile. The gem-throwing negotiation playbook is in [Luck and Fortune](#luck-and-fortune). |
| [`U`](#umber-hulks-u)    | [Umber hulk](#umber-hulks-u)        | Confuses on sight. Avoid looking at them directly.                                                   |
| [`v`](#vortices-v)    | [Vortices](#vortices-v)          | [Engulfing](#engulfment) wisps. Air, fire, ice, and steam vortices each apply their element to whatever they engulf. Kill at range. |
| [`w`](#worms-w)    | [Worms](#worms-w)             | Long worms grow tail segments as they move and can be a corridor in themselves. |
| [`W`](#wraiths-w)    | [Wraiths](#wraiths-w)           | [Drain levels on hit](#level-drain). But [their corpses grant a level](#a-note-on-wraiths), so eat them fresh. |
| [`y`](#lights-y)    | [Yellow/black lights](#lights-y) | Explode adjacent. Yellow blinds you; black hallucinates you. Black lights are invisible without *see invisible*. Kill at range. |
| [`Y`](#apelike-creatures-y)    | [Yetis](#apelike-creatures-y)             | Tough melee combatants. Corpses may grant cold resistance.                                           |
| [`z`](#zruties-z)    | [Zruty](#zruties-z)             | Three-attack mid-game brute. Uncommon but a fair fight if you've geared up.                          |
| [`Z`](#zombies-z)    | [Zombies](#zombies-z)           | Slow, numerous, come in many varieties. Zombie corpses are old and will rot.                         |

#### Things You Don't Want to Meet

| Sym    | Class            | Notes                                                                                                    |
| ------ | ---------------- | -------------------------------------------------------------------------------------------------------- |
| [`c`](#cockatrices-c)    | [Cockatrices](#cockatrices-c)      | **Touch = [instant petrification](#petrification-stoning).** Never hit one barehanded. Wield their corpse with gloves as a weapon. |
| [`D`](#dragons-d)    | [Dragons](#dragons-d)          | [Each color has its own breath weapon, resistance, and scale mail property](#a-note-on-dragons). See note below. |
| [`h`](#humanoids-h)    | [Mind flayers](#humanoids-h)     | [Drain intelligence on hit](#brainlessness). **If Int hits your racial minimum (3 for humans), you die.** A helmet blocks 7/8 tentacles. Kill from range. |
| [`V`](#vampires-v)    | [Vampires](#vampires-v)         | [Drain levels](#level-drain). Vampire lords fly and are fast. |
| [`w`](#worms-w)    | [Purple worms](#worms-w)     | The big worm: [swallows you whole on a hit, then digests](#engulfment). Cut your way out from inside. |
| [`X`](#xorns-x)    | [Xorn](#xorns-x)             | Phases through walls and floors. Three claws and a bite per turn; hard to ambush and hard to escape from. |
| [`;`](#sea-monsters)    | [Sea monsters](#sea-monsters)     | [Drowning is an instadeath](#drowning). Don't fight in water without a plan. |
| [`&`](#major-demons)    | [Demons](#major-demons)           | Major demons (Orcus, Demogorgon, Asmodeus) are boss-level threats.                                       |
| [`@`](#humans-and-elves)    | [Humans (hostile)](#humans-and-elves) | Includes the Wizard of Yendor, the most persistent nuisance in the game.                          |
| [`Q`](#quantum-mechanics-q)    | [Quantum mechanics / genetic engineers](#quantum-mechanics-q) | Quantum mechanics teleport their target on a hit; genetic engineers (new in 5.0) polymorph their target. |

#### Special Symbols

A few map glyphs aren't monsters in the conventional sense, but you'll see them and need to know what they mean.

| Sym    | What it is               | Notes                                                                                                |
| ------ | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| `I`    | Invisible monster marker | The game remembers the last spot you sensed something you couldn't see. The `I` stays there until you bump it or step on the square; the monster has usually moved. |
| `~`    | Long worm tail segment   | Part of a long worm's body. Hitting the tail damages the worm and shortens the chain; hitting the head (the `w`) is full melee. |
| `]`    | Strange object           | **Always a [mimic](#a-note-on-mimics).** No ordinary item ever displays as `]` (compare `[`, armor — `]` is its mirror). |
| `⎕` <br>(space) | Ghost            | Ghosts left from bones files. The glyph is a literal space, which paints over the floor underneath: in a room, a ghost shows as a one-square *gap* in the floor where a `.` should be. Walk into the gap to identify it. |

---

### Points of Interest
<!-- audit
2026-05-22 fountains fact-check:
- magic-fountain placement: mklev.c:2297 mkfountain() rolls !rn2(7) — 1/7 of *randomly placed* fountains; predefined fountains via lua des.feature("fountain",x,y) call lspo_feature (sp_lev.c:4904) which sets FOUNTAIN typ + looted/warned only, never blessedftn — so Minetown, Mine's End, Oracle, Big Room (bigrm-4), Castle, Juiblex's swamp are never magic
- magic-fountain gate: mgkftn && u.uluck >= 0 && fate >= 10 (fountain.c:254); fires on 21/30 quaffs at Luck ≥ 0; "Wow! This makes you feel great!" at fountain.c:257; AMAX restore loop fountain.c:259-263; +1 attr 264-272; flag consumed at fountain.c:275
- sink-kicked fountain blessedftn=0 explicit (do.c:421)
- dipfountain has no blessedftn check; dryup() at fountain.c:232 clears it — dipping a magic fountain can waste the charge if the fountain dries
- curse-some-items (case 24, "This water's no good!"): iterates gi.invent only (fountain.c:312-320), so container contents (bag interior) are safe
- poisonous water (case 21, "The water is contaminated!"): poison_strdmg if no Poison_resistance else losehp(rnd(4),"unrefrigerated sip of juice") (fountain.c:300-307)
- scare-monsters (case 29, "bad breath"): iterates fmon entire-level, monflee each (fountain.c:367-381)
- water demon 1 in 30 (case 23); wish gate rnd(100) > 80 + level_difficulty() (fountain.c:78); level_difficulty in DoD == depth(&u.uz) (dungeon.c:2027); at DL ≥ 20, threshold 100, rnd(100) never > 100, so 0% wish
- Elbereth scares water demons in DoD: onscary excludes only Rodney/lawful-minions/Angels/Riders (monmove.c:243-271); Elbereth disabled in Gehennom/Planes (Inhell || In_endgame, monmove.c:295-302); musical instruments use the auditory_scare=(x=0,y=0) path which BYPASSES the Inhell/In_endgame check (works in Gehennom)
- Wizard random starting items: u_init.c:167-178 has 3 random scrolls (may roll SCR_TAMING) and 1 random spellbook (may roll SPE_CHARM_MONSTER); Wizards do NOT roll random tools so cannot start with magic harp / tooled horn / leather drum
- strategy refs:
  + https://nethackwiki.com/wiki/Fountain — general mechanics; never-magic-fountain list
  + https://nethackwiki.com/wiki/Talk:Water_demon — "double-Elbereth" survival strategy (~97.95% survivable per wiki claim)
  + https://nethackwiki.com/wiki/Fountain_quaffing — early-game wish-fishing strategy, risk discussion
  + http://www.chiark.greenend.org.uk/~damerell/games/magicfountain.txt — Damerell statistical defense; drop items on the fountain tile to avoid make-pool curse; sack interior protected
  + https://www.steelypips.org/nethack/331/foun-331.html — Steelypips fountain spoiler

2026-05-18:
- Fountain quaff: 7 case branches in rnd(30) (fountain.c:286-387)
- Water demon spawn rate: 1 in 30 quaffs (fountain.c:247, 314)
- Shallow wish odds: water demon × rnd(100) > 80 + level_difficulty() ≈ 1/150 (fountain.c:78, 247)
- Wish odds drop to zero past DL 20 (fountain.c:78 level_difficulty term)
- Excalibur dip: lawful + XL ≥ 5 + long sword + quan=1, 1/6 Knight or 1/30 other (fountain.c:404-405)
- Non-lawful Excalibur dip curses the sword and consumes the fountain (fountain.c:411-424)
- Fountain dip cases 17-20 UNCURSE the dipped item (NOT bless) (fountain.c:464-475)
- Altar BUC flash: amber=blessed, black=cursed, no flash=uncursed (do.c:379-389)
- Altar conversion via cross-race sacrifice can flip the altar (pray.c:1717-1736)
- Throne trigger: rnd(6) > 4 = 1 in 3 chance of any effect (sit.c:45)
- Throne effect chosen from rnd(13) outcomes (sit.c:46, 68-209)
- Throne wish (case 6) requires u.uluck + rn2(5) ≥ 0, i.e. non-negative Luck (sit.c:106-110)
- Throne ID: identify_pack(rn2(5)) — 4/5 chance of 1-4 items, 1/5 chance of entire pack (sit.c:198, invent.c:2721)
- Throne can vanish "in a puff of logic" on rn2(3), even when nothing happens (sit.c:224-233)
- Vlad's throne: cases 1-4 grant wish + destroy throne; 5-13 are negatives (sit.c:241-353)
- Kicking sink: 4/5 klunk, else 1/3 black pudding, 1/3 amorous demon, 1/3 ring backup (dokick.c:1201-1238)
- Each kick outcome gated by S_LPUDDING / S_LDWASHER / S_LRING (once per sink) (dokick.c:1209-1232)
- Dip potion of polymorph: sink → fountain/throne/altar/grave (do.c:404-454)
- Grave case may fail and print "The sink vanishes." (engrave.c:1691-1693)
- Dip POT_OBJECT_DETECTION: "You sense a ring lost down the drain" while S_LRING unset (fountain.c:771-776)
- Dip POT_LEVITATION: drops a ring once per sink (fountain.c:767-770, 804-826)
- Dip POT_ACID: "The drain seems less clogged" (fountain.c:755-766)
- Drop ring in sink: searching + slow-digestion are returned to inventory; all others consumed (do.c:507-516)
- Ring of hunger vanishes ALL items on the sink square (do.c:556-570)
- Ring of teleportation moves the sink to a fresh ROOM tile (do.c:575-580)
- Rotten food in fountains is slime molds, not fruit (objnam.c:414-427)
- VAULT_GUARD_TIME = 30 turns (hack.h:69) before the guard appears; "Croesus", "Kroisos", "Creosote" all dismiss the guard if Croesus is still alive (vault.c:513-543); lying with a Lawful character loses one alignment (vault.c:507-511)
-->

Not everything interesting in the dungeon is trying to kill you.
Scattered throughout the levels are fixtures that reward the
curious, and occasionally punish them. Learning what to do (and what
*not* to do) with each of these is a rite of passage.

#### Fountains `{`

Ah, fountains. That gentle bubbling sound has lured more adventurers
to their doom than any trap, with the promise of a cool refreshing
drink.

If you don't have [bad luck](#gaining-and-losing-luck), about one in
seven is a **magic fountain** that is indistinguishable from a
regular fountain until you take a drink.
Quaffing from a magic one says, *Wow! This makes you feel great!*,
restores all your attributes to their maximum values, and raises a
random attribute by one, consuming the magic charge; afterwards the
fountain behaves like any other. (Pre-placed fountains like those
in Minetown or the Oracle, or sink-kicked fountains, are never
magic. Also: dipping gets no benefits from magic charge but could
consume it.)

**Quaffing from an ordinary fountain** is a dangerous slot machine
with dozens of random effects including:

| Outcome           | Effect                                                |
| ----------------- | ----------------------------------------------------- |
| Water demon       | A water demon appears, hostile                        |
| Water nymph       | A water nymph appears and tries to steal an item      |
| Water moccasins   | A swarm of snakes appears                             |
| Curse some items  | "This water's no good!" — items in your main inventory may be cursed (items inside a bag are safe) |
| Poisonous water   | "The water is contaminated!" — Str damage (poison resistance blocks the worst) |
| See invisible     | You gain the ability to see invisible creatures       |
| Detect monsters   | Brief view of every monster on the level              |
| Self-knowledge    | A brief enlightenment readout of your own state       |
| Scare monsters    | Bad breath — every monster on the level panics        |
| Nothing           | "The water is cool and refreshing" or "tasteless"     |

Most of the time, nothing happens. A demon appears about 1/30; on
shallow levels it may grant you a wish instead of attacking,
working out to roughly 1 wish per 150 quaffs, dropping to zero
chance past Dlvl 20. If you want to take the risk, it is a good idea
to put your items in a bag to protect them from cursing and engrave
[Elbereth](#elbereth) on a couple squares to protect against demons. Wizards'
random starting items can include a scroll of taming or charm-monster
spellbook, and any character with a protective instrument (tooled
horn, leather drum, magic harp) can scare or charm a demon — making
the gamble safer.

**Dipping in a fountain** is a different gamble, and one that Lawful
characters should know by heart. If you're at least experience level
5, dipping a long sword may transform it into Excalibur, one of the
finest weapons in the dungeon. Knights get a generous 1/6 chance per
dip; everyone else gets a meager 1/30. Otherwise, dipping can rust
your gear, summon hostile water creatures, or occasionally
uncurse the dipped item.

The conventional wisdom: if you're a lawful Knight carrying a long
sword, dip in every fountain you see until Excalibur appears. Other
lawful characters should try too, but pack patience. If you're not lawful, don't dip.

#### Altars `_`

If fountains are slot machines, altars are the single most useful
piece of furniture in the dungeon. Treat every altar like the
treasure it is.

**Dropping items on an altar** reveals their BUC status instantly:
- **Amber flash** → blessed
- **Black flash** → cursed
- No flash → uncursed

This is free, unlimited, and works on everything. In the early game,
your first altar becomes your testing laboratory: haul every
suspicious piece of gear there before putting it on. Many promising
ascensions have been saved by the simple discipline of altar-testing
before wearing. (Drop the whole pile at once; you'll see one flash
per item.)

**Sacrificing monster corpses on an altar** deepens your relationship
with your god. The corpse must be fresh (stale sacrifices are an
insult) and the bigger the monster, the more your god is impressed.
Sacrifice enough and your deity may reward you with an artifact
weapon aligned to your cause. Don't sacrifice your starting pet —
the alignment penalty is steep and the residual aggravate-monster
intrinsic sticks around for the rest of the run. See
[Divine Relations](#divine-relations) for the full theology.

**Converting an altar** to your alignment is possible by sacrificing
ordinary monster corpses on a cross-aligned altar. Each attempt has
a chance of flipping the altar to your god, a chance of doing
nothing, and a chance of backfiring (the wrong god notices and
punishes you, or worse, *you* get converted). It's a real gamble,
but worth it when the dungeon gives you an altar to the wrong god
and you need a co-aligned one for sacrifice and holy water. See
[Altars and Alignment](#altars-and-alignment) for the gotchas
(same-race sacrifice, unicorns).

#### Thrones `\`

Sitting on a throne is the purest gamble in NetHack. The list of
possible outcomes reads like a wish list shuffled with a hit list:

- A wish (if your luck is positive)
- Genocide of a monster class
- Free identification of one to four items in your pack — or, one time in five, your entire inventory
- A stat boost or a stat drain
- An electric shock
- Full healing
- A crowd of hostile monsters, summoned for your amusement
- Confusion
- A curse on one of your items
- Magic mapping of the level
- See invisible
- All your gold, vanished

About one time in three, something happens, but you won't know which
column of the ledger it's going to hit. Sit on a throne when you're
strong enough to survive the worst row of that table; the wish
branch only fires above Luck 7, so grab the luckstone first if
that's what you're after. Even when nothing happens, the throne
may vanish in a puff of logic, so you might get several tries or
none at all. (Vlad's throne in the Tower is special: it never
vanishes without granting a wish first.) Kicking a throne is a
different gamble: at positive Luck it dislodges 201–500 gold and
Luck+1 gems (max 6), which doubles as a free Luck-meter if you've
lost track.
<!-- Throne mechanics: src/sit.c throne_sit_effect(), rnd(6)>4 for 1/3
     activation, rnd(13) for effect, !rn2(3) for vanishing.
     Vlad's throne: special_throne_effect(), cases 1-4 grant wish and
     destroy throne, cases 5-13 are negative but throne survives. -->

#### Sinks `{`

Sinks are the dungeon's most underrated identification tool.

**Kicking a sink** can shake loose a ring (useful!), summon a
[black pudding](#a-note-on-puddings) (terrifying, but its glob is a
[triple-resistance snack](#useful-corpse-effects)), summon an
*amorous demon* posing
as "the dish washer" (the same incubus/succubus as [a seduction
encounter](#seduction) — careful!), or just stub your toe. Each
non-stub outcome fires at most once per sink. Worth a kick in the
early game if you can handle what comes out.

**Pouring potions down a sink** (by dipping) produces telltale
effects — a clever way to narrow down potion identities without
risking a sip. Five potions print unique sink-only messages:

| Sink message                                                 | Potion             |
| ------------------------------------------------------------ | ------------------ |
| *"The sink transforms into a fountain/throne/altar/grave!"* (or *"The sink vanishes."*) | polymorph                     |
| *"Muddy waste pops up from the drain..."* (first time per sink also drops a ring) | levitation |
| *"It leaves an oily film on the basin."*                     | oil                |
| *"The drain seems less clogged."* (blind: *"a sucking sound"*)| acid               |
| *"You sense a ring lost down the drain."* (once per sink)    | object detection   |

For most other potions, the sink instead prints *"A wisp of vapor
rises up..."* and then applies the same vapor effect as breathing a
broken potion: the side effect normally identifies the potion
(sleeping makes you yawn, hallucination starts hallucinating,
blindness blinds briefly, healing nudges HP, and so on). Wasted on
water, fruit juice, gain level, gain energy, and monster detection:
those all just print *"nothing seems to happen."*

**Quaffing from a sink** rolls one of 20 random effects. Mostly
nothing useful (mild flavor messages, summoned sewer rat, vomit,
scalding water), but three outcomes are worth the occasional risk:
~5% chance to gain an experience level outright, ~5% chance to find a
ring at your feet (once per sink), and ~5% chance to drink a random
unidentified potion. Worth a quaff or two from any sink you
encounter, but keep HP and an escape plan in reserve: it could summon
a water elemental, or it could polymorph you.

**Dropping a ring down a sink** produces a message unique to the ring
type — the most reliable non-magical way to identify rings. **Most
rings are consumed**, but two come back after IDing themselves for
free. Reserve a virgin sink for this: a sink that's already been
kicked, quaffed, or poly'd may have moved, vanished, or angered
nearby monsters by the time you've found rings to test.

| Message                                              | Ring                  | Ring kept? |
|------------------------------------------------------|-----------------------|------------|
| *"You thought your ring got lost in the sink, but there it is!"* | searching | **yes**    |
| *"The ring is regurgitated!"*                        | slow digestion        | **yes**    |
| *"The sink quivers upward for a moment."*            | levitation            | no         |
| *"You smell rotten slime molds."* (or your custom fruit)              | poison resistance     | no         |
| *"Several flies buzz angrily around the sink."*     | aggravate monster     | no         |
| *"Static electricity surrounds the sink."*           | shock resistance      | no         |
| *"You hear loud noises coming from the drain."*      | conflict              | no         |
| *"The water flow seems fixed."*                      | sustain ability       | no         |
| *"The water flow seems stronger/weaker now."*        | gain strength         | no         |
| *"The water flow seems greater/lesser now."*         | gain constitution     | no         |
| *"The water flow hits/misses the drain."*            | increase accuracy     | no         |
| *"The water's force seems greater/smaller now."*     | increase damage       | no         |
| *"Suddenly, [items] vanish from the sink!"*<br>any other items on the sink square vanish too | hunger                | no |
| *"The sink momentarily vanishes."*<br>sink moves to a new spot         | teleportation         | no |
| *"The sink transforms into a fountain/throne/altar/grave!"*<br>(or rarely *"The sink vanishes."* if grave generation fails) | polymorph             | no |

#### Vaults

A vault is a tiny walled-off 2×2 room not connected to the rest of
the level. Each one holds a pile of gold. You'll usually find one by
digging through stone or by teleporting in. The engraving *"ad
aerarium"* on a level marks one nearby (see
[Engravings](#engravings)) — though a scroll of gold detection
(or object detection) will spotlight the gold pile through the
walls, and magic mapping reveals the closet directly.

After about thirty turns inside, a guard appears at the doorway and
asks *"Who are you?"* The trick: answer *Croesus* (also accepted as
*Kroisos* or *Creosote*). The guard takes that as the name of the
vault's owner and politely leaves, gold untouched. If you give your
real name, the guard escorts you out the long way and the gold goes
with him. If you're Lawful, lying costs you one alignment.

If Croesus himself is dead (you killed him at Fort Ludios), claiming
his name angers the guard. Use the real-name route then.

---

### Branches and Landmarks

A practical tour of the branches and landmarks, in roughly the order you'll visit them.

**Sokoban or Mines first?** The Mines entrance shows up first
(Dlvl 2 to 4), but the *strategic* suggestion for most beginners
is Sokoban. It's a controlled puzzle crawl with mostly trivial
monsters, and the prize at the top (reflection or a bag of
holding) materially helps the Mines run afterward. Slashing
through the Mines early is exciting and fun, but if you want to
play the strategic game, skip them until you've solved Sokoban
and then return to the Mines when you are stronger and better
equipped.

#### The Gnomish Mines
<!-- audit
2026-05-18:
- Mines branch DL 2-4 (dungeon.lua:15-19; base=2 range=3)
- 7 Minetown variants (dungeon.lua:179-184); 1/7 picks Orcish Town (minetn-1.lua)
- gnomish PC lovemask MH_DWARF|MH_GNOME → gnomes and dwarves peaceful (role.c:654)
- Orcish Town: unaligned altar, no shops, no priest, iron-bar terrain (minetn-1.lua:18, 52, 79-88)
- Orcish Town scatters 7+ candles since Izchak's shop is absent (minetn-1.lua:98-105)
- candle shop present in minetn-2..7 (Izchak); absent only in minetn-1 (minetn-{2..7}.lua)
- all 3 Mine's End layouts place a not-cursed luckstone (minend-1.lua:77, minend-2.lua:116, minend-3.lua:67)
- minend-1 also places a mimic appear_as="obj:luckstone" — BUC-test before grabbing (minend-1.lua:59)
- Minetown watchmen are peaceful=1 in non-orcish variants (minetn-2.lua:149)
- strategy aligned with NetHackWiki Gnomish Mines, Minetown, Mines' End, Standard strategy: Minetown described as the prime price-ID/BUC-test/priest-donation stop; guaranteed luckstone at Mine's End is canonical; Standard strategy recommends Sokoban-before-Mines as the default branch ordering for the reflection/BoH prize before tackling the Mines pack fights (https://nethackwiki.com/wiki/Gnomish_Mines, https://nethackwiki.com/wiki/Minetown, https://nethackwiki.com/wiki/Mines%27_End, https://nethackwiki.com/wiki/Standard_strategy)
-->


The entrance appears somewhere around dungeon levels 2 through 4, as
a downward staircase. You'll know you're in the Mines because the
walls become rough stone and the corridors get irregular, as
pictured below.

```
               ··└       ·······?└┘·└─┐
                ··└      ·G···········│
                ···      ┐·····*······└
                 ··└┐    │··`········
            ┌──┐ ┐··│┌─┐┌┘········
          ┌─┘··└┐│··└┘·└┘······┌
         ┌┘·····│┌─·`·······<·┌
         │······└┘·····)······└┐
     └───┘····┌┐····)··········└─┘  └┐
┐·············││·`········@··········│
└─┐······─┐·──┴┼─┐···················└
  └──┐·   │····└─┘···┌┐h··············└
     └┐   └──┐·······│└─┐···┌┐·········│
             └──┐····└  └───┘ ─┐·│····┌┘
```

The Mines are populated primarily by gnomes, dwarves, and the
occasional dwarf lord. If you're playing a gnomish character, most
of them will be peaceful, which makes the Mines a relatively
comfortable detour. Everyone else will need to fight through a
steady stream of hostile gnomes and dwarves.

The Mines also have a notorious surprise guest: a mind flayer can
spawn on any random Mines level outside Minetown and Mine's End.
*"You sense a faint wave of psychic energy"* on an unexplored Mines
level is the warning. A mind flayer drains Intelligence on every
successful tentacle hit. In the early game you may not have the helmet
protection or ranged attack power you'll need to fight one safely. Retreat to prep, or
skip the branch.

**Minetown** appears a few levels into the Mines. Usually it's a small
settlement with shops and a temple, and it's worth visiting early.
The shops let you sell unwanted items for gold and buy useful gear.
The temple has an altar (check the alignment) and a resident priest.
If the altar matches your alignment, you've found a safe place to
identify items by dropping them on it. The Minetown priest can also
grant permanent AC reductions. Donate at least the amount the
priest names and you gain a point of intrinsic protection (a
permanent −1 to your AC). The asked amount scales with your
experience level, so early visits give you the cheapest points (see
[Donating to Priests](#donating-to-priests)).

Candles spawn often enough that you'll usually have enough by
endgame, but you do need to source seven for the Candelabrum of
Invocation later. **Izchak's lighting store** in Minetown is the
clean answer: buy seven there. If the shop is absent (Orcish Town
layout), seven are scattered on that level instead. Wax candles
burn longer than tallow but either works, and mixing types is fine.

One in seven times, however, Minetown generates as **Orcish Town**:
an overrun settlement with no shops, no priest, and iron bars blocking
the entrances. There's still an unaligned altar, but you won't get
any shopping done. If you were counting on Minetown for early commerce,
this is a rude surprise.

Watch out for the Minetown watch. The guards are
peaceful unless you steal from a shop or attack a peaceful creature.
If you anger them, they'll call for reinforcements.

**Mine's End** is the bottom of the Mines. All three Mine's End
variants contain a guaranteed (not-cursed) luckstone, so you'll
get one wherever you arrive. A luckstone in your open inventory
prevents your luck from timing out toward zero, which affects
everything from combat to fountain wishes. Grab it and carry it
for the rest of the game. (One layout variant also seeds a [**fake
luckstone mimic**](#a-note-on-mimics) disguised as a luckstone —
BUC-test what you pick up before relying on it.)

#### Sokoban

The entrance staircase appears somewhere around dungeon levels 6
through 10 (one level below the Oracle), and it goes up. Sokoban is a set of
four puzzle levels where you push boulders onto holes or into place
to open a path. Teleport doesn't work here, and you can't dig down
off the entrance level (its floor is reinforced).

The puzzles are fixed (two variants per level, randomly chosen).
<!-- audit
2026-05-19:
- in Sokoban, pit traps suck you in regardless of flying/levitation (trap.c:1850 gates on !Sokoban; trap.c:3014-3023 "Air currents pull you down")
- Sokoban walls are W_NONDIGGABLE on every soko level (non_diggable in each soko*.lua); dig_check fails (dig.c:228-230)
2026-05-18:
- entrance DL 6-10: Oracle base 5 range 5 + Sokoban one level up (dungeon.lua:21-24, 60-66)
- 4 levels × 2 fixed variants (dat/soko*.lua)
- noteleport on every Sokoban level (soko1-1.lua:7 and matching line in each soko*.lua)
- hardfloor only on the entrance; blocks dig-down off entrance (soko4-1.lua:38, soko4-2.lua:7)
- sokoban_guilt = change_luck(-1) + u.uconduct.sokocheat++ (trap.c:7039-7054)
- guilt triggers: squeeze past boulder (hack.c:299, 307, 398, 403)
- guilt triggers: dismount onto boulder (steed.c:767)
- guilt triggers: polymorph boulder (zap.c:1710-1711), fracture by striking (zap.c:5555-5556)
- guilt triggers: scroll of earth (read.c:1951)
- bare-hand force-fight on boulder is harmless (hack.c:2287, 2318-2321)
- pick-axe/mattock force-fight digs the boulder (hack.c:2269-2275)
- levitation also blocks pushing boulders: "not enough leverage" (hack.c:415-425)
- prize: 75/25 weighted bag of holding vs amulet of reflection (soko1-1.lua:103-107, soko1-2.lua:105-109)
- cursed scroll of scare monster placed under the prize as bait (soko1-1.lua:111, soko1-2.lua:113)
- conduct only reported once the branch is entered (insight.c:2215-2228)
- strategy aligned with NetHackWiki Sokoban, Amulet of reflection: prize/cheat-luck-penalty mechanics and the "solve honestly for the prize" advice match (https://nethackwiki.com/wiki/Sokoban, https://nethackwiki.com/wiki/Amulet_of_reflection)
- pushing a boulder exercises Strength via exercise(A_STR, TRUE) (hack.c boulder push handler); Stressed encumbrance exercises Str too but applies HP cost via near_capacity checks (attrib.c, eat.c:3197+)
-->

Each level has exactly one correct solution. If you push a boulder
into a corner where it blocks your progress there is no way to
start over. You're left with a few ways to cheat, which might or
might not help: **squeeze past** the boulder (drop your stuff to
fit), **dig the boulder** with a wielded pick-axe or mattock, or
**fracture it** with a wand of striking or a scroll of earth (or
polymorph the boulder into something else). Each of these costs a
point of Luck and breaks the Sokoban conduct. The walls themselves
are non-diggable on every Sokoban level, and pit traps are inescapable
— even flying or levitation won't carry you over an open pit, the
air currents pull you down anyway. **Teleport doesn't work here:**
the level forbids it.

The prize at the top is either a **bag of holding** or an **amulet
of reflection**, both extremely valuable; the
[Sokoban Solutions appendix](#sokoban-solutions) documents the
per-variant 75/25 weighting. A cursed scroll of scare monster is
placed under the prize as bait. A bag of holding lets you carry far
more inventory at reduced weight. An amulet of reflection bounces
ray attacks back at their casters. Either one is worth the detour.

One important rule: the Sokoban levels penalize you for "cheating."
Breaking or polymorphing boulders, reading scrolls of earth, or
squeezing past boulders costs you a point of luck each time. Solve
each level honestly if you can. The luck penalty isn't a sentence,
though: it clears the moment you legitimately finish the level
above it, and the prize is still available regardless of
infractions. One desperate boulder-smash won't ruin the run.

**Strength training side effect.** Every legitimate boulder-push
exercises Strength. Sokoban is the safest place to grind Str up
since the puzzles require dozens of pushes without putting you in
combat. Don't try to train Str by walking around Stressed in the
rest of the dungeon: the HP penalty isn't worth what you'd gain.

For complete solutions to all eight level variants, see
[Sokoban Solutions](#sokoban-solutions) in the appendices.

<!-- audit
2026-05-18:
- Oracle DL 5-9 (dungeon.lua:60-66, dungeon.c:405-411)
- 4 fountains in the delphi sub-room (oracle.lua:19-22)
- 8 centaur statues flank the Oracle (oracle.lua:9-16)
- minor consultation costs 50 zm (rumors.c:699)
- major consultation costs 500 + 50 × u.ulevel (rumors.c:699)
- minor consults ALWAYS pull from the true-rumor pool (rumors.c:747, 151-156)
- Sokoban branch goes up from the Oracle level (dungeon.lua:20-25)
- Oracle is M2_PEACEFUL with AT_NONE; she never attacks (monsters.h:2738-2745)
- strategy aligned with NetHackWiki Oracle (level), List of major consultations: paying for a major consultation is a recognized wisdom-and-intel investment (https://nethackwiki.com/wiki/Oracle_(level), https://nethackwiki.com/wiki/List_of_major_consultations)
-->
#### The Oracle

Somewhere in the mid-levels of the Dungeons of Doom (around levels
5 through 9), you'll find a special room containing the Oracle of
Delphi, flanked by centaur statues and four fountains.

The Oracle offers two services:

- **Minor consultations** are cheap (50 zorkmids) and produce
  fortune-cookie-style messages, drawn from the same true-rumor
  pool, mostly atmospheric, occasionally useful.
- **Major consultations** are expensive (500 + 50 × experience
  level) but pay back the gold in useful intel: hints about
  monsters, items, and game mechanics.

The Oracle is peaceful and never attacks. Her room is a safe place
to rest for a moment, though the fountains are subject to the usual
fountain risks.

#### The Quest
<!-- audit
2026-05-18:
- quest portal Dlvl 11-16: Oracle DL 5-9 + base=6 range=2 chained off Oracle (dungeon.lua:62-64, 27-31)
- XL 14 required to descend (quest.h:45 MIN_QUEST_LEVEL, quest.c:149)
- friendly word with leader on first quest level (quest.c:97 Is_qstart → on_start)
- alignment-record refusal at MIN_QUEST_ALIGN below threshold (quest.c:164)
- 3 artifacts grant carried MR via CARY(AD_MAGM): Orb of Detection, Magic Mirror, PYEC (artilist.h:221, 257, 293)
- 3 artifacts grant wielded/worn MR via DFNS(AD_MAGM): Sceptre of Might, Eyes of Overworld, Eye of Aethiopica (artilist.h:234, 262, 305)
- nemesis gets Bell of Opening as starting inventory; drops on kill (makemon.c:1378-1379)
- quest artifact is placed under nemesis at level generation, NOT carried (Val-goal.lua:49,76; Wiz-goal.lua:73,96; etc.)
- return portal lives on Is_qstart (first quest level) only (quest.c:97, 191-204)
- "nemesis carries an amulet of life saving" is wiki-belief, not source-guaranteed; M2_COLLECT means they may pick one up (https://nethackwiki.com/wiki/Nemesis)
- strategy aligned with NetHackWiki Quest, Bell of Opening, Quest artifact: XL 14 + 20 alignment record gate, nemesis guards both artifact and Bell, return-portal only on the first quest level (https://nethackwiki.com/wiki/Quest, https://nethackwiki.com/wiki/Bell_of_Opening, https://nethackwiki.com/wiki/Quest_artifact)
-->

Around dungeon levels 11 through 16, a magic portal drops you onto
your Quest.

You'll know when you've reached the right level. The first time you
arrive there, a faint telepathic call from your quest leader breaks
through:

> *You receive a faint telepathic message .... Your help is urgently
> needed .... Look for a ...ic transporter. You couldn't quite make
> out that last message.*

You are now looking for a magic portal, which renders as a bright
magenta `^` once you discover it. Like any trap, it stays hidden
until you step on it (which also triggers it) or search the square.

To embark on your Quest, you will need experience level 14 and a
friendly word with your quest leader on the first floor before
they will let you descend. If you are prepared and worthy, your
leader will send you to retrieve your role's quest artifact from
a quest nemesis.

Mid-game XP is slow to earn, so the path to XL 14 usually
includes eating a few [wraith corpses](#a-note-on-wraiths) (one
experience level each), or a blessed potion of gain level.
(Wraith corpses don't drop on graveyard levels, though! A good
strategy is to lead a wraith out of the Valley of the Dead before
killing it.)

Each role has a unique Quest with unique maps, a unique nemesis,
and a unique artifact reward. The Valkyrie hunts Lord Surtur for
the Orb of Fate. A Samurai's path ends in a duel with Ashikaga
Takauji over the Tsurugi of Muramasa. The Wizard descends into
the Dark One's stronghold for the Eye of the Aethiopica. The
[Artifacts](#artifacts) chapter has the full per-role list.

Quest artifacts are powerful. Each grants a unique mix of carried
or worn intrinsics: protection, luck, ESP, warning, reflection, or
stealth depending on role. A few grant magic resistance just by
being carried; a few others block magic attacks only when wielded
or worn. The [Artifacts](#artifacts) chapter has the per-role list. Getting your
quest artifact is a pivotal moment. The late game starts here.

**Two prizes wait on the nemesis's square.** The **Bell of Opening**
rides in the nemesis's pack and falls when you kill them (one of the
three invocation items you'll need for Gehennom). Your role's quest
artifact has been sitting under their feet the whole time, placed
when the level was generated. Pick both up. The Quest is the only
place in the game you can get them.

Most nemeses carry an amulet of life saving, so expect to kill them
twice. The portal back to the main dungeon is on the first Quest
level only. If you descend underprepared and have to turn back, you
may have a long climb home.

If your alignment record is too low, your quest leader will refuse
to send you. A history of attacking peacefuls is the usual cause. Keep your hands
clean.

#### The Rogue Level
<!-- audit
2026-05-18:
- Rogue Level appears DL 15-18 per base=15 range=4 (dungeon.lua:54-58)
- welcome message "older, more primitive world" (do.c:1913)
- uppercase-only monsters via Is_rogue_level (makemon.c:1672)
- symbol swaps: armor `]`, amulet `,`, food `:`, gold same as gems (drawing.c:73-79)
- doors forced D_NODOOR — no closed doors (mklev.c:647-648)
- no fountains/sinks/altars/shops/graves via skip_nonrogue (mklev.c:988-989)
- rogueprobs item pool: weapon/armor/food/potion/scroll/wand/ring only — no spellbooks/tools/amulets/gems/coins (mkobj.c:58-64)
- tile mode disabled in Qt, X11, win32, curses ports (win/X11/winmap.c:1009, win/Qt/qt_map.cpp:145, 228)
- engraving has no rogue-level guard — Elbereth works as usual (engrave.c)
-->


Somewhere in the middle dungeon you'll cross a one-level
historical district.
*"You enter what seems to be an older, more primitive world."*
The neighborhood is preserved as it was when **Rogue** was the
only dungeon-crawl anyone had heard of, and a few details give
the era away:

- All the wildlife is in capital letters: lowercase species
  hadn't been invented yet.
- Armor displays as `]`, food as `:`, amulets as `,`, and gold
  shares a symbol with gems (in Rogue they were the same thing).
- Doors don't close. Hinges came later.
- Tile mode switches off in favor of plain ASCII characters.
- No fountains, sinks, altars, shopkeepers, or priests — and
  no spellbooks, tools, or amulets in the natural item pool, all
  post-Rogue inventions.

Modern mechanics still work; you can engrave [Elbereth](#elbereth) here even
though that was a Hack-era addition. A small anachronism.

#### Fort Ludios
<!-- audit
2026-05-19:
- portal placed Dlvl 11 up to just above Medusa, 1/3 chance per qualifying level (mklev.c:2647-2651)
- portal always inside a sealed vault (mklev.c:1322-1331 calls mk_knox_portal from add_room VAULT)
2026-05-18:
- level is non-diggable: des.non_diggable over full level (knox.lua:35)
- noteleport flag blocks intra-level teleport AND scroll of plain teleport — only LEVEL teleport escapes (teleport.c:854, 1502, knox.lua:9)
- garrison: 16 soldiers + 1 lieutenant (knox.lua:126-142)
- 4 D-class dragons in storerooms (knox.lua:146-149); 4 giant eels in moat (knox.lua:151-154); 1 stone giant (knox.lua:144)
- 4 corner-tower gem caches: diamond, emerald, ruby, amethyst (knox.lua:156-167)
- treasury is 15×4=60 tiles; each holds 600+rnd(0,300) gold and 1/3 of them are trapped (knox.lua:57-69)
- treasury gold totals 36k-54k (60 × 600 = min, 60 × 900 = max)
- Croesus is L20 / 4d10 weapon / MS_GUARD (monsters.h:2861-2863)
- Croesus is NOT M3_COVETOUS — his only mflags3 is M3_INFRAVISIBLE (monsters.h:2865-2868)
- only Wizard of Yendor has M3_COVETOUS; Vlad has M3_WANTSCAND; Riders use their own logic
- alarm sounds on arrival and every revisit until Croesus dies (do.c:1893-1904)
- alarm wakes existing soldiers; it doesn't spawn new ones
- soldiers carry K_RATION / C_RATION (makemon.c:694-700)
- strategy aligned with NetHackWiki Fort Ludios, Croesus: bag-of-holding-for-gold and shoot-Croesus-across-the-moat are canonical (https://nethackwiki.com/wiki/Fort_Ludios, https://nethackwiki.com/wiki/Croesus)
-->

Fort Ludios is optional and easy to miss entirely. It appears as a
magic portal anywhere from Dlvl 11 down to just above Medusa,
always inside a sealed vault, so you'll need to dig in. The portal
leads to a fortified military compound: sixteen soldiers and a
lieutenant, with more drifting out of the barracks once the alarm
trips. Four guard dragons. A stone giant. Four giant eels
patrolling the moat. And **Croesus** on the throne, the vault
guardian himself. The level is non-diggable. The level prevents
teleportation, so once you're inside the only way out is back
through the portal or a scroll of *level* teleportation
(a plain scroll of teleportation won't work here). Croesus
hits hard in melee, so shoot or zap him from across the moat
rather than walking up.

The real prize is the gold. A 60-square treasury holds 36k to 54k
gold, with land mines and spiked pits on roughly a third of the
tiles. Gem caches in each corner tower (diamonds, emeralds, rubies,
amethysts), plus the occasional chest in the barracks. Soldiers
carry rations and serviceable weapons. The alarm only quiets once
Croesus is dead. Fort Ludios is a good place to visit for gold,
identification scrolls, or shop stock, but it's not essential for
victory.

If you can't find the portal, don't worry about it. Fort Ludios is
a bonus, not a requirement.

#### Medusa's Island
<!-- audit
2026-05-19:
- Perseus loot is per-layout — not uniform: shield 75% in medusa-1/3/4 but 25% in medusa-2 (medusa-2.lua:58-63)
- boots are 25% in medusa-1/3/4 but 75% in medusa-2 — swapped with the shield
2026-05-18:
- Medusa DL 20-29: base=-5 range=4 from DoD bottom 25-29 (dungeon.lua:75-81)
- four layouts (medusa-1.lua through medusa-4.lua); all use des.stair("down") — no ladder
- scimitar blessed +2 at 50% and sack at 50% are constant across all four layouts (medusa-1.lua:70, 73)
- shield is cursed in every layout (medusa-1.lua:64 and matching lines in others)
- gaze reflection stones Medusa via ureflects → killed(mtmp) (mhitu.c:1721-1745)
- stone resistance also blocks the gaze (mhitu.c:1747-1748) — rarely attainable pre-Medusa
- eel grab drown uses eel's tile, not yours: is_pool(magr->mx, magr->my) (uhitm.c:3389-3401)
- levitation/water-walking on adjacent dry land does NOT save you once grabbed
- medusa-2 has six electric eels (not giant eels), AD_ELEC bite (medusa-2.lua:99-104, monsters.h:3239-3247)
- kraken only on medusa-4 (medusa-4.lua:122)
- strategy aligned with NetHackWiki Medusa, Reflection, Perseus: reflection/blindfold against the gaze, levitation/water-walking to cross, Perseus statue as a backup reflection source (https://nethackwiki.com/wiki/Medusa, https://nethackwiki.com/wiki/Reflection, https://nethackwiki.com/wiki/Perseus)
-->

Medusa's level sits near the bottom of the Dungeons of Doom, around
level 25. You'll know it by the large body of water and the
statues scattered around (those used to be adventurers).

The level has three challenges stacked together:

1. **Crossing the water.** The island is surrounded by water.
   You'll need levitation, water walking boots, or some creative
   approach (freezing water with a wand of cold, building a boulder
   bridge, polymorphing into a flying creature). Don't wade in
   without preparation, because:

2. **Giant eels** (electric eels on one layout). The water is home
   to giant eels that can grab and drown you on a successful hit,
   reaching into adjacent dry tiles too. See the eel-survival rules
   below.

3. **Medusa herself.** Her gaze turns you to stone. You need
   either **reflection** (a shield of reflection or amulet of
   reflection bounces the gaze back, stoning her instead) or
   **blindness** (you can't meet her gaze if you can't see). A
   mirror also works if you apply it at her. Reflection is the
   cleanest solution. If you got the amulet of reflection from
   Sokoban, you're already prepared.

There is a downward staircase on the island itself
that leads toward the Castle. The level has four possible layouts
(two added in 3.6), so don't rely on memorizing a
single map.

**The Perseus statue.** One of the statues on the island is named
**Perseus** — the mythological hero who killed Medusa with a
mirrored shield. `#loot` him for a (cursed) **shield of reflection**
(75% in three of the four layouts; 25% in the fourth), a blessed +2
**scimitar** (50%), **levitation boots** (25% in three layouts; 75%
in the fourth — the same layout that's stingy with the shield), and
a **sack** to put them in (50%). The shield is cursed, so plan to
uncurse it before swapping it in. The other statues on the level are
intentionally empty.

> *Arien Malec collected crossing strategies from RGRN posters
> back in the early 2000s, with input from Pat Rankin, Geoduck,
> Topi Linkala, and others. This is a condensed version of his guide.*

**Surviving Medusa's gaze.** You need one of the following before
entering her level:

- **Reflection** (amulet, shield, or silver dragon scale mail).
  Her gaze bounces back and stones her instead. This is the
  cleanest solution and the one most players use.
- **Blindfold or towel.** Wear it before entering line of sight.
  You'll need telepathy or monster detection to navigate while
  blind. Works perfectly but makes the level harder to explore.
- **A mirror.** Apply it at Medusa to reflect her gaze at close
  range. More dangerous than passive reflection since you need to
  be adjacent.
- **One-shot kill.** If you have a wand of death, the spell finger
  of death, or a cockatrice corpse, you can kill Medusa before she
  gets a turn. Combine with speed or stealth for reliability. (A
  wielded cockatrice corpse, with gloves, is the cheapest of these
  options and bypasses the reflection requirement entirely.)
  Whatever you do, **don't eat her corpse**: she's the Gorgon, and
  the cadaver instantly petrifies whoever sits down for dinner.

**Crossing the water.** The island is surrounded by deep water.
Your options, from safest to most desperate:

- **Levitation** (ring, boots, potion, or spell). The easiest way
  to cross. Eels can still grab you from adjacent water (see
  [Drowning](#drowning) in [Ways to Die Instantly](#ways-to-die-instantly)).
- **Water walking boots.** You walk on the surface. Eels can still
  grab you in adjacent water.
- **Wand of cold.** Zap the water to freeze a path of ice. Ice
  is safe to walk on. This is reliable and only costs a few
  charges.
- **Scroll of earth.** Creates boulders that fall into the water,
  making a boulder bridge. Slow but works if you have nothing else.
- **Polymorph** into a flying or swimming creature. Risky if you
  lack polymorph control.
- **Jumping boots or the knight's jump.** Can leap across narrow
  water gaps, but requires careful positioning.

**Surviving the eels.** The water contains giant eels (and on
one of the four layout variants, a kraken) that can grab and drown
you. Critical rules:

- An **oilskin cloak** or **greased armor** makes the eel slip off
  on the grab attempt. Greasing wears off, so it's not fully
  reliable; oilskin doesn't.
- **Magical breathing** (amulet or polymorph) prevents the drown
  even after being grabbed.
- **Kill eels at range** whenever possible. Wands, spells, and
  thrown weapons all work. Don't melee eels in the water.
- Levitation and water walking do NOT protect against being grabbed
  by an eel in adjacent water. The drown check uses the *eel's*
  tile, not yours. Only oilskin/grease, magical breathing, or
  killing the eel first are reliable.

#### The Castle {#castle-overview}
<!-- audit
2026-05-18:
- Castle is the last DoD level: base=-1 (dungeon.lua:7-12, 82-85)
- fortified structure surrounded by a moat with a drawbridge (castle.lua:25-41)
- defenders: soldiers in barracks, dragons in storerooms, court of high-letter monsters in throne room (castle.lua:54, 60, 180, 185, 195-221)
- wand of wishing in a locked chest in one of the four corner towers (castle.lua:48-52, 142-149)
- Gehennom branches off the Castle; the stairs do not return (dungeon.lua:39-43)
-->

The Castle is the last level of the Dungeons of Doom proper, a
stone fortress surrounded by a moat with a drawbridge as its only
entrance. Inside waits an army of defenders: soldiers in the
barracks, dragons guarding the storerooms, and a court of
high-letter monsters in the throne room. Hidden in a chest in
one of the four corner towers is the **wand of wishing**.

The Castle is the last step of the dungeon proper and the gateway
to [Gehennom](#gehennom). For how to open the drawbridge and what
to do once you're inside, see [The Castle](#the-castle) in Part
Six.

---

### Traps and Hazards

Traps are invisible until you step on one, detect it with a search
(`s` command), or reveal it by other means. Once discovered, they
show up as `^` on your map, small consolation after you've already
fallen in a pit. Each search of an adjacent square has an independent
chance of revealing a trap, but the chance is well under 100%, so
search repeatedly in suspicious areas. Your pet, being closer to the
ground and warier by nature, will hesitate to step on traps it
knows about; watch its movement for clues.

Here are the traps you'll encounter, roughly grouped by how much
you'll regret finding them:

#### Nuisance Traps
<!-- audit
2026-05-18:
- arrow trap empty-click is 1/15 once `trap->once && trap->tseen` (trap.c:1199, 1228)
- dart trap 1/6 chance the dart is poisoned (trap.c:1273)
- squeaky board skipped by Levitation OR Flying unless forcetrap (trap.c:1419)
- squeaky board wakes monsters: wake_nearby for player, wake_nearto range 40 for monster (trap.c:1436, 1473)
- rust trap default branch (40% via cases 3,4 of rn2(5)) douses lamplit items then cloak else suit else shirt (trap.c:1610, 1632-1643)
- rust trap cases 0/1/2 hit helm, then left-arm chain (shield→weapon→gloves), then right-arm (weapon→gloves) (trap.c:1611-1627)
- missed arrows and darts land via place_object + stackobj — can be farmed (trap.c:1217-1220, 1288-1291)
- mounted player: steed absorbs the hit 50% of the time (trap.c:1211, 1276)
-->

| Trap            | Effect                                              |
| --------------- | --------------------------------------------------- |
| Arrow trap      | Fires an arrow at you (modest damage)               |
| Dart trap       | Fires a dart, may be poisoned                       |
| Squeaky board   | Makes noise, wakes nearby monsters                  |
| Rust trap       | Splashes water: rusts iron worn armor, soaks cloak/suit/shirt, douses lit lamps |

Annoying but rarely lethal. The silver lining: arrow and dart traps
produce free ammunition. Veterans sometimes trigger them deliberately
to stock up.

#### Movement Traps
<!-- audit
2026-05-18:
- trapdoor cascade: dlevel++ per loop iteration, `if (rn2(4)) break` = 25%/level chance to keep falling (trap.c:442-453)
- holes use the same hole_destination cascade as trapdoors (trap.c:519-522, 442-453)
- pit base damage 1d6 (trap.c:1950, rnd(adj_pit ? 3 : 6))
- spiked pit base damage 1d10 with 1/6 chance of poison (trap.c:1925, 1938-1945)
- Levitation OR Flying skip pit/hole/trapdoor, gated `!Sokoban && ...` (trap.c:633-639, 1850)
- in Sokoban the skip is disabled — pits suck you in regardless
-->


| Trap             | Effect                                                     |
| ---------------- | ---------------------------------------------------------- |
| Pit              | You fall in, take minor damage, can climb out              |
| Spiked pit       | Like a pit, but with spikes (more damage, possible poison) |
| Trapdoor         | Drops you down a dungeon shaft — usually one level, but with a 25%-per-level chance to keep falling, so you can land several deeper |
| Teleport trap    | Teleports you randomly on the level                        |
| Level teleporter | Teleports you to a random dungeon level                    |
| Hole             | Like a trapdoor, but you can see it                        |
| Magic portal     | Transports to a different branch (branch entrances)        |

Trapdoors and level teleporters are the most disruptive: one wrong
step and you're separated from your pet, your stash, and your
carefully explored map. But with teleport control (from an item or
intrinsic), teleport traps become free transportation. **Levitation
or flying** both make you immune to pits, holes, and trapdoors
entirely — except in Sokoban, where the puzzle levels disable the
skip and you fall in regardless.

#### Dangerous Traps
<!-- audit
2026-05-20:
- random polymorph timer is rn1(500, 500) = 500-999 turns (polyself.c:813); decremented each turn until 0
- nohands or verysmall form on polymorph triggers break_armor() which dropx() drops worn gear to the floor (polyself.c:1248-1351)
2026-05-18:
- anti-magic implosion damage QUARTERED (not halved) for pass-walls: `dmgval2 = (dmgval2 + 3) / 4` (trap.c:2371-2372)
- max 4d4 raw damage caps at 4 after quartering (16+3)/4 = 4
- anti-magic damage composition: base 1d4 + 1d4 per half_physical/half_spell + 1d4 for wielding Magicbane + 1d4 for carrying first non-quest AD_MAGM artifact (trap.c:2351-2369; loop breaks on first match)
- cancellation on any magical trap detonates `20 + d(3,6)` at the square then removes trap (zap.c:3611-3621)
- ANTI_MAGIC counts as is_magical_trap (trap.h:121)
- polymorph trap is blocked entirely by Antimagic OR Unchanging (trap.c:2486-2489) — PolyControl only directs the change
- sleep gas: Sleep_resistance skips the fall_asleep branch in trapeffect_slp_gas_trap (trap.c:1570)
- iron footwear: blocks bear-trap leg damage (trap.c:1517-1518), blocks spiked-pit spikes (trap.c:1901-1903), blocks polymorph trap (trap.c:2478-2483)
- iron footwear absorbs an anti-magic drain by losing 1 enchantment, but only if spe>0 (trap.c:2328-2343)
- strategy aligned with NetHackWiki Fire trap, Anti-magic field, Polymorph trap: fire trap destroys scrolls/potions/spellbooks, MR makes anti-magic trap deal extra damage, MR/Unchanging block polymorph traps (https://nethackwiki.com/wiki/Fire_trap, https://nethackwiki.com/wiki/Anti-magic_field, https://nethackwiki.com/wiki/Polymorph_trap)
-->


| Trap              | Effect                                               |
| ----------------- | ---------------------------------------------------- |
| Land mine         | Explosion, heavy damage, items can be destroyed      |
| Bear trap         | Holds you in place until you escape                  |
| Sleeping gas trap | Puts you to sleep (helpless for several turns)       |
| Fire trap         | Burns you, destroys scrolls and potions in inventory |
| Magic trap        | Random magical effects (some good, some very bad)    |
| Anti-magic field  | Drains magical energy; hits harder if you carry magic resistance |
| Polymorph trap    | Polymorphs you into a random creature                |
| Rolling boulder   | Triggers a boulder rolling along a fixed track; takes you out if your square is in its path |

Fire traps are the sleeper threat. The fire itself hurts, but
the real catastrophe is your inventory: scrolls burn, potions
shatter, and that stack of twenty scrolls of identify you've been
hoarding is suddenly ash. Fire resistance saves your skin but
*not* your belongings. Items inside a *sack* or *oilskin sack*
survive the trap; the sack itself absorbs the burn. Gehennom is
fire-trap country, so keep your consumables bagged.

Polymorph traps are a double-edged sword. With polymorph control,
they're a free polymorphing booth. Without it, you become something
random, possibly a newt that can't use any of its equipment.
**Magic resistance and the Unchanging intrinsic both block the
polymorph entirely.** Tcontrol is the only way to *use* the trap;
MR or Unchanging let you walk through it untouched.

If you do get caught and polymorphed into a handless form, your
gear drops to the floor on the spot. Don't panic and don't move:
random polymorphs wear off in a few hundred turns, and your kit
is at the square you're standing on. Defend the square if you
can, pray if a monster has you in a corner, and pick everything
up the moment you change back. (If you happen to be carrying a
wand of polymorph or know the spell, zapping or casting it on
yourself lets you reroll the form, but only if your current form
can use a wand or cast.)

Sleeping gas is murder in monster-rich areas. You can't fight, you
can't run, you can't even wake up on purpose. Monsters line up
to hit you like it's a buffet. Sleep resistance (elven blood, the
right ring) sidesteps it.

Magic traps roll one of about a dozen random effects. The
bad outcomes are summoning hostile monsters, cursing one of
your items, aggravating monsters, blindness, sleep, stun,
vomiting, and an earthquake that pops pits open in the
surrounding squares. The good outcomes are an HP restore, a
mana refill, a Charisma boost, a magic-mapping flash, and a
room-lighting flash. Patient players sometimes camp a known
magic trap until their Charisma climbs (about +1.4 average per
zap), shop prices and all.

Bear traps clamp on for several turns. Try to step *diagonally*
off the square; the diagonal escape is about five times faster
than orthogonal. A wand of opening or spell of knock frees you on
the spot.

If you have magic resistance and you *want* to enter a teleport
trap (for vault access, say), MR blocks the trip — unless you
press `Ctrl+T` first, which forces a voluntary trap-use that
bypasses the resistance.

**Anti-magic fields hit harder if you're magic-resistant.**
Counterintuitive enough to mislead returning players. The trap
drains spell energy, and having *magic resistance* also triggers
an "anti-magic implosion" that costs you HP. The damage is
d4 base, plus another d4 if you have half-physical or
half-spell damage, plus d4 for wielding Magicbane, plus
d4 for carrying any one magic-resistance artifact (only one
counts — the check breaks on first match). At worst that's 4d4
damage, quartered (rounded up) if you can pass through walls. The
defense is finding the trap first (search) and stepping around it.
A wand of cancellation aimed at a magical trap *does* remove the
trap, but it triggers a 20 + 3d6 damage blast at the trap's square
in the process — not a silent defuse.

Iron footwear (iron shoes or kicking boots) absorbs a
surprising amount of trap punishment in 5.0: no leg damage from a
bear trap, no spikes from a spiked pit, no polymorph from a
polymorph trap (your shoes shift instead), and a positively-
enchanted pair eats an anti-magic field's drain by losing one
enchantment instead. Useful protection to have on if you haven't
found anything better yet.

#### Searching and Detection
<!-- audit
2026-05-18:
- dosearch0 search mechanics at detect.c:2016-2093
- rnl applies a Luck bias (good Luck → 0, bad Luck → x-1) (rnd.c:112-128)
- SDOOR/SCORR roll is rnl(7 - fund); fund capped at +5 (detect.c:2026-2032, 2042-2054)
- trap-detection roll is rnl(8) with NO fund bonus (detect.c:2079) — Excalibur+lenses don't speed trap-finding
- Excalibur is the only SPFX_SEARCH artifact (artilist.h:85-86)
- wand of secret door detection is NODIR; findit reveals SDOOR/SCORR/traps/trapped chests/trapped doors/hidden mimics/hiders (detect.c:1639-1718, zap.c:2552-2558)
- wand area is a circle of radius BOLT_LIM=8 (vision.c:27-45 circle_data, hack.h:49) gated by couldsee() line of sight (vision.c:2144)
- Flying/Levitation skip most floor traps but NOT magic/teleport/anti-magic (trap.c:1061-1082 floor_trigger list omits MAGIC_TRAP/TELEP_TRAP/ANTI_MAGIC; trap.c:3026 check_in_air bypass gated by floor_trigger)
-->

The best defense against traps is finding them before they find you:

- **Search (`s`)** repeatedly. Each search has an independent chance
  to reveal each adjacent trap, and Luck improves the odds. (The
  artifact/lenses search bonus only speeds up secret-door and
  secret-corridor discovery, not trap finding.)
- **Wand of secret door detection** reveals everything hidden in a
  roughly circular area around you (radius about eight, blocked by
  line of sight): secret doors, secret corridors, traps, trapped
  chests, and concealed monsters. It's not directional.
- **Crystal ball** can reveal traps across the entire level
- **Pets** avoid known traps, so watch their pathfinding for clues
- **Flying and levitation** make you immune to most floor traps
  (you'll still trigger magic, teleport, and anti-magic traps)
- **A scroll of gold detection read while confused** turns the
  gold-reveal into a *trap* reveal — every magical trap on the
  level lights up at once. Confused gold detection is the cheapest
  pre-Gehennom trap survey.

A good time to search is when the dungeon has already hinted that
something is wrong: a stray corpse in the middle of an otherwise
empty room, a scatter of arrows or darts on the floor, a square
your pet refuses to cross, or a themed room whose gimmick is
hidden hazards.

#### Finding Secret Doors
<!-- audit
2026-05-19:
- ring of searching auto-calls dosearch0(1) each turn unless level is noautosearch (allmain.c:342-344)
- Excalibur enchantment feeds `fund = uwep->spe` only if SPFX_SEARCH (detect.c:2026-2027, artilist.h:85-86)
- lenses add +2 to fund if worn and not Blind (detect.c:2029-2030)
- fund is capped at +5 — a +5 Excalibur alone hits the cap; lenses only help if enchantment is <+3 (detect.c:2031-2032)
- per-square reveal roll is rnl(7 - fund) for SDOOR/SCORR (detect.c:2042-2054)
- blessed scroll of magic mapping converts every SDOOR to a visible door (read.c:2121-2130)
- +0 Excalibur contributes nothing because fund = spe = 0
-->

The Dungeons of Doom were designed by architects who believed that
every room should have one emergency exit that requires ten minutes
of tapping on walls to locate. Secret doors and corridors are the
game's passive-aggressive way of saying "you haven't explored
*thoroughly* enough."

**When to search for secrets:**

- **Dead ends** that feel too convenient. If a corridor just stops,
  and you haven't found what you came for, there's probably a door
  in the surrounding walls
- **Suspiciously empty rooms** with no obvious exit. The exit exists;
  it's just been cunningly disguised as a wall
- **After exhausting all visible options.** When you've explored
  everything reachable and still haven't found the downstairs, it's
  time to stop wandering and start wall-tapping

**The systematic approach:**

Type `20s` to search twenty times in one spot. For new characters
with average Luck, you need 15-22 searches to reliably reveal a
secret. Searching once and moving on is essentially announcing your
intention to remain lost.

Move three squares along the wall and repeat. Each search reaches
one square in every direction, so a stride of three gives complete
wall coverage with no gaps and no wasted re-searching. The pattern
looks tedious on paper because it *is* tedious, but tedium is
cheaper than being trapped on Dlvl 1 forever.

**Items that help:**

- **Ring of searching** auto-searches every turn while it's worn
- **Excalibur** (or any artifact with the searching aura), wielded, adds its enchantment to your search bonus (a freshly-dipped +0 Excalibur adds nothing)
- **Lenses** worn (and you not blind) add +2 to the search bonus — but the total bonus from Excalibur + lenses caps at +5, so lenses only help if Excalibur's enchantment is below +3
- **Wand of secret door detection** instantly reveals nearby secrets in a radius
- **Blessed scroll of magic mapping** shows every secret door on the level (only the blessed version)

**The wisdom of patience:**

Secret doors are NetHack's way of teaching you that brute force
doesn't solve every problem. Sometimes you need brute force applied
methodically to every wall section in sequence. The downstairs you
seek is behind one of these walls. Finding it is a matter of
systematic elimination. The only mistake is giving up after three
searches and declaring the level "impossible."

<!-- audit
2026-05-18:
- uncursed athame is excluded from dulling_wep — instant Elbereth, no enchantment cost (engrave.c:1306-1307)
- cursed athame dulls like any blade
- default engrave rate is 10 (one occupation tick for an 8-char word); rate=1 only on dulling_wep / RING_CLASS / GEM_CLASS (engrave.c:1320-1325)
- edged weapon dulls about 1 enchantment per 2 chars (engrave.c:1357-1365 + comment); 8-char Elbereth costs ~−4 enchantment from spe=0
- DUST/BLOOD surface-garble is 1/25 and bypassed by BURN/ENGRAVE (engrave.c:1223)
- impairment scrambles (Blind 1/11, Confused 1/7, Stunned 1/4, Hallucination 1/2) apply to ALL engraving types (engrave.c:1224-1225)
- strict-match Elbereth: full engr_txt must equal "Elbereth" exactly (engrave.c:256)
- BURN engravings erode only on ice or magical fire @ 50% (engrave.c:278)
- DUST monster-step erosion is 1 char per monster move (monmove.c:734, engrave.c:271-289)
- "ad aerarium" engraving marks BOTH TELEP_TRAP and LEVEL_TELEP niches (mklev.c:733, 809-811, 823)
- vault is a 2×2 room placed by create_room then filled + makevtele() (mklev.c:53, 1320-1333)
-->
#### Engravings

You can write on the dungeon floor with the engrave command (`E`).
Engravings serve a few practical purposes: writing **Elbereth**
(covered next), running the engrave-test on an unidentified wand
(covered in the wand chapter), or just leaving a note for whoever
finds your bones file. The mechanics described here apply to *any*
engraving, not just Elbereth.

**Methods, speed, and durability.** The tool you write with
determines how quickly you can finish, how hard the engraving is
to erase, and whether your stylus suffers wear.

| Method                    | Speed         | Durability     | Notes                             |
| ------------------------- | ------------- | -------------- | --------------------------------- |
| Finger (dust)             | Instant       | Fragile        | Smudges when monsters step on it  |
| Uncursed athame           | Instant       | Semi-permanent | Doesn't dull (cursed athame does) |
| Other edged weapon        | Several turns | Semi-permanent | Interruptible; dulls (~1 enchantment per 2 chars — "Elbereth" costs ~−4) |
| Hard gem or diamond       | Several turns | Semi-permanent | Interruptible                     |
| Wand of digging           | Instant       | Semi-permanent | Good middle ground                |
| Wand of fire or lightning | Instant       | Permanent      | Burns the word into the floor     |

The three durability tiers correspond to how the text resists
ordinary erosion:

- **Fragile** (dust) — a monster stepping on the square smudges
  one character. In dust, an Elbereth lasts as long as the floor
  stays clear.
- **Semi-permanent** (scratched into the floor) — monster traffic
  doesn't smudge it. Random erosion can occasionally chip a
  character under unusual conditions, but in practice the
  engraving lasts indefinitely.
- **Permanent** (burned in) — the engraving doesn't erode at all
  under normal conditions; only ice tiles or magical attacks can
  damage it.

**Engraving is an interruptible occupation.** Anything written by
hand at multi-turn speed (non-athame edged weapon, gem) takes one
turn per letter. If you're interrupted mid-word — by an attack, a
monster wandering into view, or anything else that breaks an
occupation — you get a partial engraving that does nothing useful.
Instant methods (any wand, finger-in-dust, or an uncursed athame)
finish in a single occupation action.

**Impairment and errors.** If you are blind, confused, stunned, or
hallucinating, you have a chance of misspelling each letter, and
this scrambling applies to *every* engraving method, including
burns from a wand of fire. (Only the dust/blood surface-garble
roll is skipped for harder methods.) A misspelled message has no
special power; this matters most for Elbereth.

**Overwriting and combining.** Appending to an existing engraving
is possible, but for named-word magic like Elbereth the engraving
must read *exactly* that word and nothing else, so the appended
text usually destroys the ward. To refresh, overwrite the square
or pick a fresh one.

**Two engravings worth recognizing.** Most engravings you find are
random flavor (graffiti, "elbereth" left by someone else, etc.),
but two specific messages are *trap markers* placed by the
dungeon: *"ad aerarium"* (Latin: *to the treasury*) is engraved
near a secret closet containing either a **vault teleporter**
(a one-shot trap that drops you into Croesus's 2×2 gold vault on
the same level — pick up the gold, then escape ahead of the vault
guard) or a **level teleporter** (sends you to a random dungeon
level, often unwelcome without teleport control); *"Vlad was
here"* marks a secret closet containing a **trap door**. Both are easy to miss in the message log, and
worth investigating when you see them — but be ready for what's
on the other side.

#### Elbereth
<!-- audit
2026-05-19:
- while levitating, finger and weapon engraving refused (engrave.c:1003-1006)
- but wand engraving falls through after "gesture toward floor"; ptext=TRUE wands (fire, lightning, cold, digging) still complete the engraving (engrave.c:1007-1011, 1099-1104, 1186-1189)
- v2 "no actual writing happens" claim was wrong for BURN wands — corrected
2026-05-18:
- hypocrite alignment hit: adjalign((u.ualign.record > 5) ? -5 : -rnd(5)) — flat −5 only with healthy alignment, else rnd(5) avg −3 (mon.c:4280)
- defile rule: del_engr_at fires unconditionally — burned Elbereth wiped too (mon.c:4267-4285)
- strict-match Elbereth: full engr_txt must equal "Elbereth" (engrave.c:256)
- Elbereth dead in Gehennom and the endgame planes (monmove.c:302, In_hell || In_endgame)
- onscary lives at monmove.c:241 (not teleport.c as old comment claimed)
- ignored by S_HUMAN + unique_corpstat (quest nemeses, named monsters) (monmove.c:259-261)
- ignored by Riders, Angels, lawful minions, Wizard of Yendor (monmove.c:251-253)
- ignored by minotaur (monmove.c:301)
- blind and peaceful monsters pass through (monmove.c:299-300)
- cornered ALLOW_SSM step-through (mon.c:2278-2282)
- strategy aligned with NetHackWiki Elbereth, Engraving: exact-spelling rule, defile-and-hypocrite penalty, ward dead in Gehennom/endgame, burn-with-wand-of-fire for permanence (https://nethackwiki.com/wiki/Elbereth, https://nethackwiki.com/wiki/Engraving)
2026-05-23:
- defile rule fires for any attack with via_attack=TRUE: melee (uhitm.c:1293,1302,1403,6398), thrown weapons via dothrow.c:1965,2230,2282 → wakeup(mon, TRUE) → setmangry(mtmp, TRUE) (mon.c:4350-4355), and wand zaps via zap.c:4948,5495
- "kill at range from Elbereth" is therefore a 4.x-era piece of advice; in 5.0 it defiles too
- Rogue "Elbereth in the doorway, daggers from beyond" cannot work in 5.0: throwing from Elbereth defiles it; standing off Elbereth means Elbereth doesn't protect anything (monmove.c:295-302 requires u_at(x,y))
-->


##### Where the word comes from

*Elbereth* is Sindarin for "Star-Queen," one of the Elvish names
of **Varda Elentári**, highest of the Valar in J.R.R. Tolkien's
*Silmarillion* — the one who set the stars in the sky. In *The
Lord of the Rings* the Elves invoke her name for protection
against evil: Frodo cries *"O Elbereth! Gilthoniel!"* on
Weathertop and the Witch-king recoils, and Sam invokes her in
Shelob's lair to make the Phial of Galadriel burn brighter.
NetHack lifts the conceit directly: writing Varda's name on the
dungeon floor is an appeal to a higher power for safe ground.

> *The mechanics below are inspired by Kate Nepveu's Elbereth FAQ.
> Kate also maintained steelypips.org, the long-running archive
> that preserved decades of community spoilers.*

##### The ward

Writing the word **Elbereth** on the floor creates a protective
ward. Most monsters will not melee-attack you while you stand on an
Elbereth square; they mill around, frustrated, instead. The ward
applies whether you wrote it or found it already engraved, and the
underlying engraving method (dust, scratched, burned) doesn't
affect the strength of the protection — only how long the engraving
will survive.

##### Rules of the ward

- **It only works while you stand on it.** Step off and the
  protection ends. Stepping back on resumes it.
- **It must be the exact word.** "Elbereth," nothing more, nothing
  less. Misspellings (from impairment) and combined text don't
  count.
- **Some monsters ignore it.** Anything represented by `@`
  (humans, elves, player-like creatures), the Riders on the Astral
  Plane, Angels, minotaurs, unique/named monsters (quest nemeses,
  Vlad, the Wizard), shopkeepers, guards, and any blind monster
  will all walk right through. So will cornered monsters with no
  retreat path: a creature with nowhere to flee will fight rather
  than stand helplessly. As a rough principle, anything intelligent
  enough to recognize the misuse, anything that can't perceive the
  inscription, and anything with nothing to lose disregards the ward.
- **Elbereth doesn't work in Gehennom, on the Elemental Planes, or
  on the Astral Plane.** Below the Castle, you're on your own.

##### The defile rule (important)

If you attack a monster while standing on Elbereth — melee, thrown
weapon, or wand zap — and that monster *would* have feared the
ward (or is peaceful), the engraving is **deleted instantly, in
full, regardless of how it was made.** Even a burned-permanent
Elbereth disappears in one swing.
You take an **alignment hit** ("You feel like a hypocrite") and see
the message *"The engraving beneath you fades."* The hit is a flat
−5 if your alignment record is comfortably positive (above +5);
otherwise it's a random −1 to −5.

The durability table doesn't show this: "permanent" and
"semi-permanent" describe resistance to *passive* wear (monster
footsteps, erosion). Your own hostile action wipes the word
regardless of tier. So Elbereth is strictly **defensive**.
Use it to heal, drink a potion, read a scroll, swap gear, regroup.
Any attack from on top — melee, thrown, or zapped — defiles it, so
step off when you mean to fight back.

##### Practical use

In an emergency, write Elbereth in the dust with your finger: free,
instant, and good enough to buy a turn or two. Most monsters will
back off and let you act. Once the immediate danger passes, you can
either step off the dust ward to keep it for next time (it survives
until a monster steps on the square), or upgrade to something more
durable.

For a permanent safe spot, useful for stashing items, resting at a
fixed retreat point, or anchoring a corridor fight — burn the word
with a wand of fire or lightning. One turn, no interruption risk,
no impairment penalty, no wear. A semi-permanent engraving (athame,
weapon, gem, wand of digging) is the middle ground: durable, but
the slow methods can be interrupted mid-word.

While levitating, you can't engrave with your finger or your
weapon: the game refuses both. A wand of fire, lightning, cold,
or digging still works from above. You'll see "you gesture toward
the floor below you" first, but the burn lands anyway. The old
finger-in-dust trick from earlier editions is gone, but torching
Elbereth into the floor from a wand of fire while floating still
works.

A **scroll of scare monster** dropped on the floor acts like
Elbereth on its square, doesn't erode, and works while you're not
standing on it. The catch: it disappears one read after you pick
it up, so leave it where you want the safe spot. The Castle wand
chest is parked on top of a cursed one for exactly this reason.

<!-- audit
2026-05-18:
- passes_bars uses verysmall() = msize < MZ_SMALL = TINY only (mondata.c:552-563)
- grid bug / bat / sewer rat are MZ_TINY (monsters.h:889, 1149, 1269); kitten and little dog are MZ_SMALL and stay out
- acid (ray/breath/spit) corrodes bars unconditionally (zap.c:5347-5369)
- lightning shares the acid branch but is gated `rn2(10) break` — melts on roughly 1 zap in 10 (zap.c:5349)
- striking and force bolt have NO IRONBARS handler — they pass through harmlessly
- rock moles eat bars via the metallivorous arm (hack.c:769-784)
- xorns and earth elementals pass walls and so pass bars
- bars sit on a room-wall tile (mklev.c:783); niche payload one square further into stone
- scroll of teleportation placed in niche only when `!noteleport` on the level (mklev.c:790-792)
-->
#### Iron Bars

Iron bars look like a barrier but aren't solid: light passes through,
you can see what's on the other side, and **tiny** creatures (grid
bugs, bats, rats) can squeeze between — kittens and little dogs are
already too big. What they resist is almost everything the player
can throw at them: pick-axes bounce off ("Clang!"), wands of digging
fizzle, weapons swing through harmlessly, and kicking just hurts
your foot. Wands and spells of *striking* and *force bolt* pass
through the bars without effect. The bars corrode for an acid ray,
acid breath or spit (if you are polymorphed into a yellow dragon or
black naga), and a **wand of lightning** can melt them too — though
only about one zap in ten actually dissolves the bars.

The practical early-game answer is to **dig around** them. Iron bars
sit in a niche cut into a room wall, so digging diagonally past the
bars (or breaking through the wall to the stone behind and then back
into the niche) reaches the contents without touching the bars. Mid-game,
polymorph into something that breathes acid or lightning, passes
walls (xorn, earth elemental), is **tiny** enough to slip between,
or eats metal (rock mole). Starting pets won't fit, but a polymorphed
pet can.

What's typically behind them: a scroll of teleportation (unless the
level is non-teleport, in which case the niche skips it), occasionally
a random item or a previous adventurer's corpse. The scroll is a joke: you'd
need one already to read it from outside the bars.

---

### Feelings and Sounds
<!-- audit
2026-05-18:
- vault sounds: "counting gold" means vault with gold; "searching" means empty vault (sounds.c:253-262)
- "Wow! ...great!" needs blessed restore-ability with zero unfixable troubles (potion.c:658-661)
- same string also fires from a blessed magic fountain (fountain.c:257)
- non-boot stealth gear gives "move very quietly"; boots give "walk very quietly" (do_wear.c:123-129)
- lycanthropy cure is quaffing holy water, not dipping (potion.c:728-737)
- quantum corpse toggles HFast on or off: "seem faster" or "seem slower" by current state (eat.c:1227-1235)
- dosounds() is silenced by Deaf, !flags.acoustics, u.uswallow, or Underwater (sounds.c:208-209)
- bugle reveille at muse.c:843-846 is gated only by !Deaf (not by dosounds)
- sad-feeling at mon.c:3100-3101 is NOT gated by Deaf — it's a feeling, not a sound
- oracle "strange wind" (sounds.c:190); shop "cursing shoplifters" (sounds.c:322)
- fountain "bubbling water" or "water falling on coins" (sounds.c:214-218)
-->

Much of the most important information in NetHack comes to you as
cryptic feelings and sounds. They sound like atmosphere, but most
of them are specific signals. If you don't know what they mean,
you'll miss the cues entirely. They are worth memorizing.

(Caveat: being **deaf**, **swallowed**, or **underwater** silences
the ambient-sound channel completely — Permadeaf conducts in
particular lose every level-flavor cue. The feeling-from-corpse
messages still come through.)

| Message                                          | What it means                                                            |
|--------------------------------------------------|--------------------------------------------------------------------------|
| *"You have a sad feeling for a moment, then it passes."* | Your pet just died offscreen.                                        |
| *"You hear someone counting gold coins."* | Vault on this level, with gold still in it.                                                       |
| *"You hear the footsteps of a guard on patrol."*<br>*"You hear someone searching."* | Vault on this level (the "searching" message means the vault is already empty).    |
| *"You hear a strange wind."*           | Oracle on this level.                                                                  |
| *"You hear someone cursing shoplifters."* | Shop on this level.                                                                 |
| *"You hear bubbling water."*<br>*"You hear water falling on coins."* | Fountain on this level.                                          |
| *"You hear a bugle playing reveille!"* | A soldier just woke nearby soldiers; expect a fight.                                   |
| *"You hear a slurping sound."*         | A gelatinous cube just ate items off the floor on this level.                          |
| *"You hear a crunching sound."*        | A rust monster, rock mole, or other metallivore just ate something metallic.           |
| *"You hear a wolf howling at the moon."* (or jackal) | A werecreature is somewhere on this level.                               |
| *"You hear crashing rock."*            | A tunneler (dwarf, gnome miner, rock mole, umber hulk) just dug through stone.         |
| *"You hear a chugging sound."*         | A monster just drank a potion (usually healing themselves).                            |
| *"You hear a nearby zap."*             | A monster just zapped a wand at something offscreen.                                   |
| *"You feel healthy."*                  | Intrinsic poison resistance from a corpse.                                             |
| *"You feel a momentary chill."*        | Intrinsic fire resistance from a corpse.                                               |
| *"You feel full of hot air."*          | Intrinsic cold resistance from a corpse.                                               |
| *"Your health currently feels amplified!"* | Intrinsic shock resistance from a corpse.                                          |
| *"You feel wide awake."*               | Intrinsic sleep resistance from a corpse.                                              |
| *"You feel very firm."*                | Intrinsic disintegration resistance from a corpse.                                     |
| *"You feel a strange mental acuity."*  | Intrinsic telepathy from a corpse.                                                     |
| *"You seem faster."*                   | Intrinsic speed from a quantum mechanic corpse. (If you already had speed, you instead "seem slower" — quantum corpses toggle.) |
| *"You feel a mild buzz."*              | Eye of newt corpse restored 1–3 mana.                                                  |
| *"You sense a lack of food nearby."*   | Scroll of food detection, no food on level.                                            |
| *"You feel materially poor."*          | Scroll of gold detection, no gold on level.                                            |
| *"You feel like someone is helping you."* | Scroll of remove curse; worn/wielded cursed items uncursed.                         |
| *"You move very quietly."*             | Ring of stealth or elven cloak. (Elven boots give *"You walk very quietly"* instead.)  |
| *"Wow! This makes you feel great!"*    | Blessed potion of restore ability with no remaining troubles — *or* a blessed magic fountain hit. |
| *"You feel feverish."*                 | Lycanthropy infection from a were-monster. `q`uaff holy water, eat wolfsbane, or `#pray`. |
| *"You are slowing down."*              | You're turning to stone. Immediately eat a lizard corpse, drink acid, or pray.         |
| *"You are turning into slime."*        | Green-slime contagion. Burn it off (read a fire scroll, cast fireball on yourself, or self-zap a wand of fire), or `#pray`. |
| *"You feel deathly sick."*             | Terminal illness (Pestilence, Demogorgon). Quaff extra healing, eat eucalyptus, or pray. |

---

## Part Three: Survival

### The Art of Combat
<!-- audit
2026-05-20:
- waking a sleeping monster via attack invokes wakeup() (uhitm.c:250, 305, 1403, 1926, 5213, 5590, 5694, 5764, 5774); if the struck monster was sleeping AND not MS_SILENT AND not helpless, growl() fires (mon.c:4353-4356 wakeup)
- growl() calls wake_nearto(mtmp->mx, mtmp->my, mtmp->data->mlevel * 18) (sounds.c:421) — radius approx sqrt(mlevel * 18) in tiles
- Knight caitiff penalty: -1 alignment for attacking helpless or fleeing non-undead monsters when Lawful (uhitm.c:336-341)
- Samurai dishonor penalty: -1 alignment for attacking peacefuls (uhitm.c:342-345)
- Samurai poisoned-weapon penalty: -sgn(u.ualign.type) alignment (uhitm.c:1521)
- Quest entrance requires alignment record >= MIN_QUEST_ALIGN = 20 AND ulevel >= MIN_QUEST_LEVEL = 14 (quest.h:43-45)
2026-05-18:
- to-hit factors: XL, Str, Dex, Luck, enchantment, AC (find_roll_to_hit)
- abon includes both Strength AND Dexterity; Dex 25 yields +11 (weapon.c:950-988)
- dbon has a Strength cap: max +6 at STR 18/100 or higher (weapon.c:993-1015)
- two-handed weapons get a 3/2 Strength-bonus multiplier (weapon.c bhitval two-handed branch)
- conflict requires mutual sight and a Cha-vs-Lvl resist roll: resist_chance = min(19, Cha - m_lev + XL) (mondata.c:1607-1612)
- two-weapon and shield are mutually exclusive
- Expert two-weapon: Rogue and Samurai only (u_init.c skill tables)
- Rangers cannot two-weapon at all (no P_TWO_WEAPON_COMBAT entry) (u_init.c:440-466 Skill_Ran table)
- two-weapon penalty is a flat table: -9/-7/-5/-3 to-hit, -3/-1/0/+1 damage
- Luck to-hit contribution is sgn(Luck)·((|Luck|+2)/3), capping at ±5 (uhitm.c:377); Luck itself ranges ±10, ±13 with luckstone
- monsters use m_move (phase 3) then mattacku/castmu (phase 4) on the same turn (monmove.c:911, 943-944, 971)
- no "free extra step" change exists; that earlier claim was fabricated
- strategy aligned with NetHackWiki Corridor, Movement tactics, Twoweapon: corridor chokepoint as the single biggest tactical principle, two-weapon penalty tied to skill rank (https://nethackwiki.com/wiki/Corridor, https://nethackwiki.com/wiki/Movement_tactics, https://nethackwiki.com/wiki/Twoweapon)
-->

The most important combat technique in the Mazes is knowing when
*not* to fight. The second most important is making sure you hit
really, really hard when you do.

#### To-Hit Calculation

Every swing of your weapon is a d20 roll, modified by everything
the game can think of to make your life interesting:

- Your experience level (the game's way of saying "you've seen things")
- Your weapon's enchantment (a +7 Excalibur hits *noticeably* better)
- Your Luck (the universe literally takes sides; the to-hit contribution caps around ±5 even though Luck itself ranges further)
- Your Strength and Dexterity bonuses (muscles plus agility, both matter)
- The monster's AC (the lower their AC, the harder they are to tag)

You need to roll at or above (10 + defender's AC - your modifiers).
Since some late-game monsters have AC of -10 or worse, this formula
can feel like trying to hit smoke. Enchant your weapon. Keep your
luck up. And maybe don't try to punch an arch-lich.

#### Damage

Base damage depends on your weapon and whether the target is small
or large. (Most weapons are optimized for one or the other, because
apparently dungeon physics care about monster volume.) Added to base:

- Weapon enchantment (+1 per point)
- Strength bonus (up to +6 for STR 18/xx, or more)
- Weapon skill bonus (depends on skill level)
- Special bonuses (silver damage, artifact bonuses, etc.)
- In 5.0, **two-handed weapons** get a 50% bonus to the strength
  damage component, a deliberate payoff for giving up your shield

This narrows the gap between two-handed builds and dual-wielding
considerably. A Barbarian with a two-handed sword and respectable
Strength is not just accepting the trade-off of foregoing a
shield: they're dealing measurably more damage per swing than a
comparable one-handed build. If you've been avoiding
two-handed weapons because the math didn't add up, run those numbers
again.

#### AC and Defense

Your AC determines how likely monsters are to hit *you*. The journey
from "I die to gnomes" to "nothing can touch me" looks like this:

| Stage         | Typical AC | Protection level        |
| ------------- | ---------- | ----------------------- |
| Starting out  | 8 to 10    | Wearing a good attitude |
| Early dungeon | 2 to 5     | Basic armor equipped    |
| Mid-game      | -5 to 0    | Enchanted armor + cloak |
| Endgame       | -20 to -10 | Walking tank            |

At AC -20, almost nothing hits you with physical attacks. Feel
free to laugh at ogres. But many late-game threats use special
attacks (breath weapons, spells, gaze attacks) that ignore AC
entirely. You can be wearing impenetrable armor and a disenchanter
will still ruin your day. AC is necessary but not sufficient.

#### Two-Weapon Combat
<!-- audit
2026-05-19:
- Rogue and Samurai are the only roles reaching Expert in P_TWO_WEAPON_COMBAT (u_init.c skill tables).
- Valkyrie and Knight cap at Skilled (u_init.c skill tables).
- Barbarian caps at Basic (u_init.c skill tables).
- Ranger has NO P_TWO_WEAPON_COMBAT entry: cannot two-weapon at all (u_init.c:440-466 Skill_Ran table).
- Penalty structure is a flat negative replacement per skill tier: to-hit -9/-7/-5/-3, damage -3/-1/0/+1.
- Penalties are not a "split" between the two weapons. (weapon.c:1576-1600 hit-bonus and 1676-1695 dam-bonus apply the same flat penalty per-strike — no halving)
-->

Some roles can fight with a weapon in each hand, which looks
impressive and gives more attacks per turn. The catch: each strike
takes a flat to-hit and damage penalty determined by your
two-weapon skill (−9/−7/−5/−3 to hit, −3/−1/0/+1 damage from
Unskilled through Expert), and the loadout must be melee on both
sides — no shield, no launcher (bow, crossbow, sling), no ammo
(arrows, bolts), no projectiles (darts, shuriken). Only
**Rogue** and **Samurai** can reach Expert; Valkyrie and Knight
cap at Skilled; everyone else lower or none. Rangers don't have
the skill at all. If you're not sure, just use one really good
weapon. In 5.0, two-handed weapons gained a 3/2 strength damage
bonus, making them a good alternative.

#### Fighting Smart

The dungeon rewards cowardice, cunning, and property damage. Here
are the time-tested tactics that keep adventurers breathing:

- **Use corridors.** Monsters can only approach one at a time in a
  corridor — the single most important tactical principle in the
  Mazes. Never fight a mob in an open room if you can retreat to a
  chokepoint and fight them in single file. It turns a suicide
  mission into a turkey shoot.
- **Fight at range.** Wands, thrown weapons, and spells let you
  soften up monsters before they reach you. This is especially
  important against monsters with dangerous melee attacks. A fire
  ant is scary in melee. A fire ant that you've already zapped
  three times is just a warm corpse.
- **Know when to run.** The Mazes have no medals for bravery, only
  for survival. If a fight is going badly, use a scroll of
  teleportation, a wand of teleportation, or just run. Dead
  adventurers don't get second chances (unless wearing an amulet
  of life saving).
- **Use conflict.** A ring of conflict makes monsters fight each
  other. Walk into a room full of enemies, put on the ring, and
  watch from the doorway as they destroy each other. Two 5.0
  caveats: a monster has to *see* you for conflict to affect it
  (so blind or out-of-sight monsters keep their wits), and the
  chance scales with your **Charisma**: high Cha makes it
  noticeably more reliable, low Cha makes it flaky.
- **Elbereth for emergencies.** Write it, stand on it, recover.
  The monsters will mill around you looking confused and angry,
  which is exactly how you want them. Step off Elbereth before
  resuming the fight: any attack from on top — melee, thrown, or
  zapped — defiles the engraving and costs you alignment ("you
  feel like a hypocrite"). Elbereth is a rest stop, not a
  firing position.
- **Ranged attackers retreat.** Monsters with ranged attacks
  (archers, spellcasters, anything that can hurt you from a distance)
  now actively back away when you close to melee range. Walking toward
  a centaur archer to neutralize its bow no longer works; it will
  simply back up and keep shooting. The tactical implications: use
  corners and narrow passages to cut off their retreat, bring ranged
  options of your own, or use a wand of teleportation to skip past the
  dance. This change also means monster spellcasters are more dangerous
  than they used to be: they'll maintain the range they need to cast
  while you struggle to close.
- **Cornered scared monsters fight.** Elbereth still works, and the
  engrave-and-regenerate tactic still works, but only when the monster
  has somewhere to go. A frightened monster that has nowhere to flee
  will now turn and fight rather than stand helplessly while you
  recover. If you've carved [Elbereth](#elbereth) in a corridor and then backed a
  monster into a dead end, be ready for it to make a decision about
  that arrangement. Keep an exit behind the monster, or expect contact.
- **The first swing wakes the room.** Sleeping monsters stay asleep
  while you walk past them, but a hit on one wakes everything around
  it: the struck monster growls, and the growl wakes any other
  sleeping monster within roughly seven squares for a level-3 gnome,
  more for larger creatures. A packed room becomes a simultaneous
  brawl on swing two. Pull the pack one at a time by *backing away*
  into a corridor first (so they wake strung out in a line) or write
  [Elbereth](#elbereth) and let them come.
- **Watch your alignment around peacefuls.** Knights and Samurai
  take a special alignment hit for attacking the helpless, fleeing,
  or peaceful (a caitiff penalty for Knights, a giri-breaking
  penalty for Samurai). The Quest entrance check requires alignment
  record at least 20 *and* experience level at least 14. A handful
  of careless peaceful kills can lock a Knight or Samurai out of
  the Quest for the rest of the run.
- **Doors and diagonals.** You can't move diagonally through a
  door: approach and leave orthogonally. **Closing a door**
  (`c` + direction) blocks pets and any monster lacking the
  intelligence or hands to open it; handy when you want to slip
  away from your pet, or when you need a turn or two of quiet.

---

### Things That Will Kill You
<!-- audit
2026-05-20:
- mines residents are class G (gnomes, S_GNOME) and h (humanoids incl. dwarves, S_HUMANOID); g is gremlins/gargoyles (defsym.h:295, 301, 303, 333)
- gnomish wizard has AT_MAGC AD_SPEL — random spellcaster, can cast sleep (monsters.h:1695-1701)
- homunculus AT_BITE AD_SLEE 1d3 (monsters.h:551-558)
- soldier ant speed 18, AT_BITE 2d4 + AT_STNG AD_DRST 3d4 (monsters.h:103-110)
- water demon: S_DEMON class &, level 8, NOCORPSE NOGEN (monsters.h:2911-2919)
- rope golem AT_HUGS 6d1 grapple (monsters.h:2523-2529)
- iron golem level 18, speed 6, AT_WEAP 4d10 + AT_BREA AD_DRST 4d6 (poison gas, drains Strength), MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON (monsters.h:2586-2594); slow but heavy hitter, not a speedster
- bats and giant bats speed 22; raven and vampire bat speed 20 with two attacks each (monsters.h:1269-1294)
- steam/fire vortices speed 22; queen bee speed 24 (rare); air elemental speed 36 (monsters.h vortices, queen bee, air elemental rows)
- water demon wish: rnd(100) > (80 + level_difficulty()) — 20% chance at depth 0, drops to 0% past level_difficulty 20 (fountain.c:78)
- clay golem AT_CLAW AD_PHYS 3d10 single (monsters.h:2562-2569)
- stone golem AT_CLAW AD_PHYS 3d8 single (monsters.h:2570-2577)
- golems are class ' (apostrophe), not P (defsym.h:359)
2026-05-19:
- Very_fast = (HFast & ~INTRINSIC) || EFast (youprop.h:377)
- Blue DSM sets EFast |= W_ARM (do_wear.c:822); speed boots set EFast |= W_ARMF
- either alone reaches Very Fast; wearing both doesn't go faster
2026-05-18:
- mount slip damage 10-14 HP via rn1(5, 10) (steed.c:354)
- water demon spawn rate is 1 in 30 quaffs at fountain.c:247, 314
- bones items 80% cursed via rn2(5) gate (bones.c:290)
- all 9 DSM extrinsic properties verified at do_wear.c:806-883
- gold DSM permanent light radius 4/3/2 blessed/uncursed/cursed (light.c:881-911)
- gold DSM is the only body-slot light source (artifact.c:2264-2275)
- confused genocide hits your role: u.umonster ← gu.urole.mnum (read.c:2839, u_init.c:991)
- mumakil attack solo, not in packs; AT_BUTT 4d12 + AT_BITE 2d6 (monsters.h:838-845)
- shimmering DSM does not exist in 5.0 (#if 0 DEFERRED in objects.h:509-511, 536-538)
- strategy aligned with NetHackWiki Bones, Yet Another Stupid Death, Sleep, Golem: bones loot 80% cursed and dangerous, early-game pacing matters more than depth, sleep resistance recommended before Mines, iron golem and rope golem are the dangerous golems for the player (https://nethackwiki.com/wiki/Bones, https://nethackwiki.com/wiki/Yet_Another_Stupid_Death, https://nethackwiki.com/wiki/Sleep, https://nethackwiki.com/wiki/Golem)
-->

Only about **0.4% of games end in ascension.** The other 99.6%
are deaths. NetHack ends in death by default; survival is the
exception.

**The early dungeon is deadly.** The top ten killers are,
in order: jackals, dwarves, soldier ants, gnome lords, sewer rats,
giant bats, [small mimics](#a-note-on-mimics), gnomes, foxes, water moccasins. Every
one of them lives on the upper dungeon levels. None are
intrinsically dangerous to a prepared character. They get you
because you haven't built HP, AC, or resistances yet and they
outnumber you. The strategic takeaway: the early game has been the
deadliest stretch of NetHack since 1987. Don't push to descend;
spend the turns clearing levels, finding altars, and getting BUC
information.

**On pacing.** A rough rule of thumb: your experience level should
be at least somewhere near the dungeon level you're standing on.
Going down stairs at experience level 4 onto Dungeon level 12 is
how you meet things you can't outrun and can't outfight. The
dungeon doesn't wait — every step deeper raises the monster
difficulty roll, and a fragile character with 30 HP isn't going
to soak even a single bad encounter. There's no prize for getting
to Sokoban quickly. Clear, identify, level up, then descend.

**On bones.** "Bones" levels are levels saved from another
adventurer's death and replayed in your game. The game flags them
("This place looks familiar..." or a recognized layout, plus a
grave marker in the dungeon overview) but doesn't otherwise warn
you. They are dangerous in two ways. First, items on a bones level
generate cursed about 80% of the time, so don't put on anything
you find there without altar-testing or pet-testing. Second, and
much less well known: bones-level *monsters* can be far above the
level's normal difficulty. The previous adventurer may have died
with a master mind flayer adjacent, or a summoned demon nearby, or
in monster form. Those creatures stick around. Treat any
above-depth monster on a bones level as evidence to retreat, not
to engage. If your character isn't ready for the monster, leave
the level and come back when you are.

#### Common Combat Deaths

Beyond the top ten, certain enemy categories kill more
beginners than their depth or appearance would suggest.
The shape of the threat is usually pack tactics, surprising
speed, or one catastrophic special attack.

**The Gnomish Mines is a choice, not a routine stop.** Mines
residents are `G`, gnomes, and `h`, the humanoid class that
includes dwarves.
Plain gnomes, gnome lords, dwarves, and gnomish wizards all
sit in the top fifteen causes of death on the public server,
because the Mines funnel four or five armed opponents into
a single room and beginners walk in at XL 3 expecting an
extra branch. Dwarves hit harder than they look and come
armored. Gnomish wizards (a `G` with spell attacks) can cast
sleep at you among other things, and a sleeping adventurer in
a Mines room is a dead one. Take the branch when you have HP, a real weapon,
and sleep resistance. A positive AC at XL 5 is not enough.

**Sleep without resistance is a near-instadeath.** A homunculus
(`i`) bite, a gnomish wizard's sleep spell, or later an orange dragon
or Nazgul breath puts you to sleep for several turns. If you
are alone in a corridor it costs you a couple of rounds. If
you are surrounded by anything else, the surrounding monsters
chew through your HP while you cannot move. Sleep resistance
comes from any elf, elven mummy, or giant corpse, and from
several roles' starting kits (Wizard's cloak of MR, Ranger's
elven cloak). Eat for it before descending into the Mines or
the lower Quest.

**Bats and other speedsters** (`B`). Bats and giant bats clock in
at speed 22, nearly twice your starting 12. They get two attacks
for every one of yours, and a 1d4 bite at double rate chews
through low HP fast. Ravens and vampire bats are speed 20 with
two attacks each (and the vampire bat's second bite drains
Strength). The defense is positioning, not HP totals: fight from
a doorway so they cannot kite around you, or kill them at range.
Centaurs (speed 18 to 20) and vortices raise the same problem
later on.

**Ants and other pack travelers** (`a`). Soldier ants are
speed 18 with two attacks (bite plus a Strength-draining
sting) and travel in groups. A wandering soldier-ant pack
on Dlvl 4 can end a careless run. Killer bees, giant ants,
and fire ants are the same shape of problem. Treat any
chittering or buzzing on an unexplored level as a reason
to back up and find a chokepoint before the pack closes.

**Quadrupeds** (`q`). Rothes are three-attack pack hunters
at sluggish speed 9: a single one is easy to outrun, but
three in a room is several real fights stacked together.
Mumakil are solo two-attack bruisers (4d12 butt plus 2d6
bite) that hit harder than anything else in the upper
dungeon. Both wander mid-level rooms.

**Golems** (`'`). Golems are class `'` (apostrophe), not
`P` (which is puddings). Most are slow but several hit
disproportionately hard. The rope golem grapples on a hugs
attack and pins you in place for adjacent friends to chew on.
Clay and stone golems deliver 3d10 and 3d8 in a single claw.
The iron golem is the endgame model: level 18, 4d10 weapon
plus a 4d6 poison-gas breath that drains Strength, and resistant
to fire, cold, electricity, sleep, and poison. Most golems
leave no corpse, so they cannot be eaten for intrinsics. Kill
them quickly and at range when you can.

**Water demons from fountains** (`&`). Quaffing a fountain
summons a water demon roughly 1 quaff in 30. Water demons
are major demons (class `&`, level 8) who attack first and
grant a wish only if you survive. Wish odds also drop with
depth, so casual quaffing pays worse the deeper you go.
Don't quaff from fountains until you have magic resistance,
reflection, or a clear path of retreat.

**Floating eyes** (`e`). Hit one in melee and you're paralyzed for
~70 turns; whatever passes by during the nap kills you. Kill at
range, then eat the corpse for telepathy.

**Minotaurs** (`H`, in the Castle and maze levels of Gehennom).
Three attacks averaging ~38 damage per turn — the hardest hitter
short of the Riders themselves. A wand of sleep, a thrown potion
of paralysis (with free action), or just digging down before they
reach you are the standard answers.

**Major demons gate in more major demons.** Every melee hit from
a major demon has roughly a 1-in-13 chance of summoning another.
A single bad fight in Gehennom can cascade into an arena.

#### Deadly Mistakes

Routine mistakes kill more adventurers than exotic instadeaths.
The list below is sorted roughly by frequency on the public
server.

**Eating mistakes.** Rotted corpse, [poisonous corpse](#deadly-poison), and
[choking](#choking) each rank in the top forty causes of death. Don't
eat old corpses. Don't eat while Satiated. Don't finish a
heavy corpse if you're already approaching Satiated. Pray
immediately if you ate something you shouldn't have.

**Reading unidentified scrolls in a shop.** A confused or
cursed scroll of teleportation level-teles you out of the
shop with the unpaid merchandise still in your pack, turning
the shopkeeper hostile when you return. A scroll of fire
destroys shop goods you are liable for. Save the price-ID
session for outside.

**Mount slips and riding accidents.** More heroes die slipping
off saddled ponies than die to mind flayers. Getting on a
steed rolls against your experience level plus the steed's
tameness; on a failure you take 10 to 14 HP. Don't mount
while Confused, Fumbling, or Glib, don't mount with a cursed
or greased saddle, and don't mount a barely-tame pony at
experience level 2.

**Pet kills.** Kittens, little dogs, housecats, and ponies
all appear on the death list, almost always because the
player put on a ring of conflict and forgot to take it off.
Remove the ring before walking back to your pet.

**Boiling and shattering potions.** Hot ground in Gehennom
shatters any potion you drop on the floor, and the shrapnel
is deadly. Keep potions in a bag once you descend below the
Castle. Bagging your potion and scroll stash earlier is also
wise: a yellow dragon's lightning bolt shatters every loose
potion in your pack, and a fire trap incinerates loose
scrolls.

**Killed by your own wand.** Self-zapped attack wands, rays
ricocheting off a wall in a narrow corridor and back into
your face. Engrave-test wands before pointing them at
yourself.

**Killed by a grid bug.** The weakest monster in the game
kills more than 11,000 adventurers per year. They get the
last hit on someone who walked away from a real fight at
2 HP, or someone who decided to read a scroll on the turn
one was adjacent. Don't read scrolls under threat.

**Killed by kicking.** Kicking sinks summons a [black pudding](#a-note-on-puddings),
a foocubus, or worse. Kicking doors can break your toe.
Kicking locked chests can electrocute you, and electric
shock is a top-100 cause of death on its own. Stop kicking
things.

**Wrath of a god.** You prayed when your god wasn't willing.
See [Divine Relations](#divine-relations) for the prayer
cooldown and what counts as "trouble" worth a prayer.

**Scroll of genocide while confused.** Confused genocide
removes your role's own species from the world (Valkyrie,
Wizard, Samurai). You become the genocide. Don't read
scrolls under confusion unless you already know what they
are.

**Scroll of earth on yourself.** Buried under a pile of
boulders you summoned on your own head.

The median death is a preventable swarm of jackals on Dlvl 3.

#### A note on dragons

Dragons deserve a full briefing. Each color has its own breath
weapon, resistance, scale mail property, and degree of desire to
kill you specifically. The summary:

**Gray** dragon scale mail grants magic resistance, the most important
defensive property in the game, full stop. Gray dragons are the ones
you most want to kill for their skin, and also the ones most likely
to make you regret trying.

**Silver** dragon scale mail grants reflection. The second pillar of
not dying to wands.

**Black** dragons disintegrate everything you're wearing along with
you, including your magic resistance. Carry reflection or eat enough
black dragons to grow disintegration resistance before going where
they live. Their scale mail grants disintegration resistance plus
drain resistance, a rare extrinsic source of the latter.

**Yellow** dragon scale mail is an underrated pick. Listed power is
acid resistance, but it also grants **stoning resistance** — the
same outright immunity acid blob corpses give. If you find a yellow
dragon and don't already have stone-res, killing it is worth the
trip. Yellow dragons are rare, though.

**Orange** dragon scale mail grants sleep resistance *and* free
action (the ring's effect), bundled into one slot.

**White** dragon scale mail grants cold resistance *and* slow
digestion — a useful nutritional save on long descents.

**Red** dragon scale mail grants fire resistance *and* infravision,
the same effect as a ring of infravision or being elven.

**Green** dragon scale mail grants poison resistance *and* sickness
resistance — a pair of niche defenses in one slot.

**Blue** dragon scale mail grants shock resistance *and* intrinsic
**speed** — same tier as speed boots. (Wearing both at once doesn't
make you faster; either alone reaches Very Fast.) One of the most
powerful body slots in the game.

**Gold** dragons are new in 5.0 and breathe fire. Their scale mail
has no resistance power but is permanently lit (radius 4 blessed, 3
uncursed, 2 cursed) — the only body-slot light source in the game,
and it lets you abandon torches and oil. It also confers
hallucination resistance.

All scale mails are dragonhide, body-slot, +9 AC worn (the best in
the body slot), and resist disenchantment naturally. The choice of
which color to chase is usually whichever dragon's territory you
can reach safely; about one in three adult-dragon kills drops a
set of scales, which you can wear directly or convert to scale
mail by reading a non-cursed scroll of enchant armor while
wearing them.

#### A note on mimics

You will frequently meet mimics in **shops**, with more as you get
deeper. An average shop has one or two mimics sitting in the
aisles, masquerading as items. They're slow (speed 3) but their
claws hit hard. Small mimics rank in the top ten causes of death.

**The visual tell.** A mimic appearing as a generic "strange
object" renders on the map as `]` — a mirror of `[`, the armor
class. No real item ever displays as `]`. A `]` on a shop floor
or anywhere else is always a mimic.

**Other contextual disguises** (rare in practice but worth
knowing): a mimic in a temple may appear as an extra altar, in a
Delphi room as a second fountain, in a maze as a lone boulder. So
"a single piece of furniture that shouldn't be there" is
suspicious.

**How to uncover one safely.** Search the adjacent square (`s`)
reveals concealed mimics like it reveals traps. Throw a cheap item
at the suspected square; the mimic uncloaks and the item lands
harmlessly. A stethoscope applied to the square also uncloaks.
Telepathy, ESP, astral vision, and a wand of secret door detection
see through the disguise and show the mimic as `m`. Your pet won't
step onto a mimic.

**Sticking.** Large and giant mimics glue you in place on a
successful claw hit: you can't move, you can't go down stairs, you
can't escape down a hole. Magic cancellation (cloak of protection,
amulet of guarding, etc.) reduces the sticking chance — one more
reason to secure MC before browsing mid-game shops.

**Eating the corpse** turns you into a pile of gold (or, while
hallucinating, an orange) for 20 / 40 / 50 turns depending on
size. Anything that tries to pick "you" up snaps the spell.

#### A note on nymphs

The `n` class (wood, water, mountain) doesn't want to kill you.
She wants your inventory. Each successful claw hit lifts a random
item from your pack, and the nymph then **teleports away**,
sometimes within the level, sometimes off it entirely. Your bag
of holding, your amulet of reflection, a freshly-wished cloak of
magic resistance: gone, often to a level you'll never revisit.
No NetHack horror story is more universal than "a nymph walked
off the level with my bag of holding."

**The second claw is seduction.** Nymphs get two attacks per
turn, and the seduction half drains experience levels if the
nymph is the opposite gender of your character. A successful
seduction can also strip a ring or amulet you're wearing. A
single bump can rob you, drop your XL, and snatch the cloak off
your shoulders, all in one round.

**Defenses.** Kill at range (darts, force bolt, a wand of
anything). [Engrave **Elbereth**](#elbereth): nymphs respect it. Or drop your
most irreplaceable items on the floor before approaching.
Whatever's not in your pack can't be stolen.

**Already robbed?** A satiated nymph stays in the dungeon
somewhere, often a nearby level, and her corpse drops what she
stole. If you have time, search the floors above and below;
sometimes you get the bag of holding back.

**Never engage a nymph while carrying the Amulet of Yendor**
during the Ascension Run. Losing the Amulet to a teleporting
thief means a return trip to Moloch's Sanctum, which is usually
where ascension runs go to die.

#### A note on puddings

Puddings are the dungeon's signature self-multiplying monsters,
and their leftover globs are also among the best food you can
find. The class lives in the mid-dungeon and Gehennom.
**Brown and black puddings split when you hit them with an iron
or metal weapon**: one becomes two, two becomes four, and your
long-sword grinding session turns into a swarm. **Black pudding
additionally corrodes your wielded weapon** on its passive
return-hit, so each round of splitting is also a step toward
your blade rusting away. The community consensus: a beginner
discovers puddings the same way every time — by feeding them
their best weapon and watching the population graph go up.

**Defenses.** Melee with a **silver or wooden weapon** (silver
dagger, elven dagger, athame, club, quarterstaff). These don't
trigger the split. Mithril also bypasses the check. Wands of
cold and fire kill puddings outright with no split, and most
spells work too.

**Gray ooze** doesn't split, but it rusts armor on a hit; don't
engage in your starting iron suit if you can avoid it.

**Eat the globs.** A pudding leaves a **glob** rather than a
corpse, and the globs are some of the best food in the game.
(That's *instead* of a corpse, not in addition to one: the old
3.4-era "pudding farm for endless altar fodder" trick doesn't
work in 5.0. The reward from a split pudding is more globs, not
more sacrifice meat.)
They're slow to spoil (about 500 turns of edibility, twice a
normal corpse) and packed with resistances. A brown-pudding glob
grants **cold, shock, and poison resistance** over repeated
eats; a gray-ooze glob grants **fire, cold, and poison
resistance**; a black-pudding glob also grants **cold, shock,
and poison resistance**. Brown pudding and gray ooze are
*vegetarian*-safe; black pudding is not. Globs of the same color
stack and shrink together, so a pile of brown-pudding globs is a
re-rollable chance at the resistance you don't yet have. The
strategic flip-side of the splitting trap: if you can kill one
pudding cleanly (silver weapon, cold/fire wand, spell), the
splitting becomes a *feature* — every divided pudding is one
more glob to eat. The full intrinsic table is in
[Useful Corpse Effects](#useful-corpse-effects).

#### A note on trolls

The `T` class doesn't stay dead. After you kill a troll, its
corpse sits on the floor for a few hidden turns and then stands
back up — at full HP, fresh and angry. A pile of corpses after a
five-troll fight is a *timer*, not a kill count: walk away for
twenty turns and the same five trolls are coming back. The
veteran's lament — *"I beat the trolls, I got cocky, the trolls
beat me"* — is the most repeated story on the public boards.

**Stopping the revival.** Eat the corpse (trolls are safe to
eat for everyone but vegetarians). Tin it with a tin opener.
Apply a magic whistle to summon a pet who'll eat it. Zap a wand
of teleportation at the corpse to send it off-level. Destroy it
with a wand of striking. In Gehennom, the lava under your feet
is the simplest solution — kick the corpse onto a lava square
and walk on.

**Trolls drop their gear when they die.** If they revive, they
re-collect what they were carrying, so a revive-and-recollect
cycle leaves piles of mixed troll-gear and dead-troll bodies on
the same square. Pick up the gear before they wake up; the loot
is yours either way.

**Class members.** Plain troll, ice troll, rock troll, water
troll, and the late-game Olog-hai. All revive; the corpse
behaves the same way regardless of variant. The Olog-hai is the
one to fear — a three-attack hitter at level 13, and "fighting
the same Olog-hai twice in twenty turns" is one of those
experiences that turns a careless run into a careful one.

#### A note on wraiths

The `W` class has a touch attack that **drains an experience
level** — one of the few permanent character setbacks in the
game. You lose stat points, hit points, mana, and the most
recent skill slot. There is no easy undo, and the wraith can
land the touch again if you let it. The standard advice on the
public boards: fear the wraith on first sight, plan the kill
from across the room.

**But the corpse is one of the most valuable consumables in the
game.** Eating a fresh wraith corpse grants you a level — the
inverse operation. So the recipe: kill the wraith carefully
(the touch is melee-range only, so engage at distance or from
inside a corridor where you control the spacing), then eat the
corpse the moment it drops. Wraith corpses spoil quickly, so
hesitation costs you the trade.

**Farming wraiths.** Mid-to-late-game players actively
hunt wraiths in the upper Quest and throughout Gehennom for free
XP. A *cursed* scroll of genocide naming "wraith" reverse-
genocides four to six fresh wraiths at your feet — a ready-made
banquet, if you can drop each one in the turn it arrives. The
classic setup is to stand on stairs (so you can escape if it
goes wrong), drop a stack of cursed scrolls, and graze. Some
ascending heroes credit a wraith binge for the experience levels
that carried them through Gehennom.

#### A note on Seduction {#seduction}
<!-- audit
2026-05-18:
- could_seduce at mhitu.c:1980 requires opposite-sex genagr/gendef; same-sex foocubus just claws
- demon's succubus/incubus form is randomly assigned at generation, not based on player gender (makemon.c:1278-1279 `mtmp->female = femaleok ? rn2(2) : 0`; mhitu.c:1988-1989 doseduce reads Mgender(mon) not player)
- stripped items go to inventory, not dropped on the floor (mhitu.c:2351 calls remove_worn_item which just unequips into inventory, steal.c:213)
- level-drain outcome is fatal at XL 1 — do not farm a foocubus at low level (exper.c:232-238 losexp at u.ulevel==1 with non-null drainer calls done(DIED))
-->

The **amorous demon** (`&`, gray) appears as a **succubus** to
male heroes and an **incubus** to female ones. A same-sex foocubus
just claws at you and never starts the seduction. The encounter is
a Cha+Int gamble: five bad outcomes vs. five good ones, plus a
payment phase. Handled badly it can drain a level, an attribute,
and 6–15 HP; handled well it grants a level, an attribute, full
HP, and extra max Pw.

**Mechanics.** The demon must be adjacent and not on cooldown. It
strips off your worn armor one piece at a time (cloak, suit,
boots, gloves, shield, helm, shirt). The items are unequipped to
your inventory, not taken or dropped on the floor; the only thing
the strip costs you is the slot for the rest of the encounter.
You get a yes/no prompt before each piece comes off with
probability Cha/20 (so Cha 18 prompts about 9 times in 10; Cha 10
about half the time). **If you're still wearing a body armor or
cloak when the strip ends, the encounter ends right there** and the
demon walks away. A hard-to-remove suit is the simplest defense.

If you do get to the act, the outcome rolls against your combined
Cha+Int (capped at 32). At the cap the bad-outcome chance is about
6%; at Cha+Int = 20 it's about 40%; at 10 it's nearly 70%. Check
your stats before you accept.

| Bad outcome (low Cha+Int)         | Good outcome (high Cha+Int) |
|-----------------------------------|------------------------------|
| Energy drained (Pw → 0, −1d10 max)| +1d5 max Pw, refilled        |
| −1 Constitution                   | +1 Constitution              |
| −1 Wisdom                         | +1 Wisdom                    |
| Lose 1 XP level (drain res blocks)| Gain 1 XP level              |
| 6–15 HP damage                    | HP restored to max           |

The demon then charges 500+ zorkmids (high Cha can refuse; peaceful
demons charge 1/5). Being asleep or otherwise unresponsive defers
the attempt entirely.

**Strategic note.** At high Cha+Int the encounter is net-positive,
and the armor-removal step strips *cursed* worn pieces too — an
amorous demon can be the cheapest curse-removal in the dungeon.
Some players keep one alive to farm XP and attributes. Don't try
this at experience level 1, though: the level-drain outcome is
fatal.

#### A note on Light Bursts {#light-bursts}
<!-- audit
2026-05-18:
- yellow light: AT_EXPL/AD_BLND, monster level 3 (monsters.h:1169-1191, mhitu.c:1623-1650)
- black light: AT_EXPL/AD_HALU, monster level 5; perminvis (makemon.c:1317-1320)
- both die in their own explosion
- telepathy does NOT reveal black lights (M1_MINDLESS at monsters.h:1188-1189); only warning does
- warning detects only at adjacent range — exactly when they explode, so it helps less than it looks
- plain potion of healing cures blindness only when blessed (potion.c:1994-2004); extra/full always do
-->

**Yellow lights** (`y`, level 3) and **black lights** (`y`, level 5)
attack by exploding the moment you're adjacent. Yellow lights blind
you for **10d20 turns** (up to 200 — a *blessed* potion of healing
or any extra/full healing cures, or apply a unicorn horn); black
lights hallucinate you for **10d12 turns** (a unicorn horn cures it,
or wait it out). Both lights die in the explosion, so the encounter
resolves immediately, but the after-effect is long enough to be the
real threat. Black lights are invisible; *see invisible* reveals them, but
because they die in the same turn they attack, you'll only "see"
them just before they vanish.

**Defenses:** Kill them at range with wands, thrown daggers, breath
weapons — anything that doesn't bring you adjacent. *Warning*
detects them through invisibility, but *telepathy* does not (they're
mindless). If you do get blinded, a unicorn horn cures it.

---

### Ways to Die Instantly

Some things in the Mazes kill you outright. Not by whittling down
your hit points, not by wearing you down over time, but by ending
your life in a single move with no second chance. These are called
instadeaths, and learning to recognize the situations that produce
them is the difference between a promising run and a one-line
epitaph.

> *The catalog of instadeaths below is inspired by Trevor Powell's
> Instadeath Spoiler, which drew on Dylan O'Donnell's RGRN files.
> Trevor defined an instadeath as "a single move death which does
> not involve the player's hit points dropping to zero," and that
> taxonomy has been the standard reference ever since.*

#### Attack Wands and the Warning Shot
<!-- audit
2026-05-18:
- mwandexp gates the first-zap warning miss (muse.c:1830-1860)
- buzz_force_miss is the dispatch path for the warning shot (muse.c:1815, 1834)
- 6 beam wands trigger the warning: death, sleep, fire, cold, lightning, magic missile (muse.c:1842-1847)
- the visible warning shot identifies the wand to the player
- late-game zones spawn monsters with mwandexp=TRUE — no warning shot (makemon.c:1290-1293)
- late-game zones: Stronghold, Knox, Quest, Gehennom, Vlad's Tower, endgame
-->

Being hit by a powerful wand can mean instant death. A wand of
death or finger of death kills an unprotected character outright,
and ray wands of cold, fire, lightning, or magic missile can roll
lethal damage too. But the first time any given monster zaps a
beam wand (death, sleep, fire, cold, lightning, magic missile)
at you, the shot misses. If you can see the monster, the wand
identifies itself in the same moment, so now you know what was
just aimed at you and you have a turn to do something about it
before the next zap connects.

#### Choking
<!-- audit
2026-05-18:
- eat-while-satiated death via done(CHOKING) (eat.c:248, 286); warning string at eat.c:3314
- "Continue eating?" prompt only with paranoid_confirmation:eating (default off)
- death only fires at u.uhunger >= 2000 with 1/20 escape; Breathless never choke (eat.c:258-266)
- amulet of strangulation generates 90% cursed (mkobj.c:1063); beginner can't just take it off
- escape: pray, or uncurse via holy water or remove curse
- strangulation is a timer death via done_timeout(DIED, STRANGLED), not an attack — MR has nothing to block (timeout.c:890-894)
-->

If you push past Satiated and keep eating, you can choke and die.
The game prints "You're having a hard time getting all of it down"
as a warning; if you have eating-confirmations turned on it'll also
prompt you. Past a hard nutrition threshold the choke check fires
and, unless you're Breathless or pass a 1-in-20 escape, kills you
instantly.

**The other path to choking is the amulet of strangulation.** Worn,
it puts a short countdown on your throat and kills you when it runs
out. The amulet generates cursed 90% of the time, so you usually
can't just take it off: pray, or uncurse it with holy water or
remove curse. Magic resistance doesn't help — strangulation isn't
an attack, it's a timer death. Polymorphing into a Breathless form
*does* save you.

**Defense:** Don't eat above Satiated. Be paranoid about unidentified
amulets.

#### Starvation

This isn't technically instant, but it feels like it. If your
nutrition drops to zero, you faint. If you don't eat something while
fainted, you die. In the early game before you've established a food
supply, starvation is a real threat.

**Defenses:** Eat corpses promptly. Pray when your god is willing
and you are Weak or Fainting (prayer cures hunger). Carry food
rations, tripe rations, or lembas wafers. Don't let nutrition
management slide.

**Famine**, one of the three Riders in the endgame, will kill you
quickly through starvation by draining 40–80 nutrition per
hit, without any extrinsic that blocks it. At the end of the
game, be sure to enter the Astral Plane Satiated and carry a
stack of food rations through the fight, or you will be Faint
soon after Famine hits.

#### Deadly Poison
<!-- audit
2026-05-19:
- AD_DRST extra-damage roll is ~1/240 per qualifying hit: rn2(8) × rn2(30) (uhitm.c:3154, attrib.c:362)
- poison death is purely `u.uhp <= loss`, no carrycap term (attrib.c:366) — burden is irrelevant
- poison resistance grants full immunity (attrib.c:338-343)
- Famine corpse is instantly fatal (eat.c:831-838)
-->

A handful of monsters (pit vipers, killer bees, cobras, some
spiders) have a poison-damage branch that can deliver 10 to 34
extra HP of damage on top of the normal hit. At full HP you
usually survive; at low HP it can outright kill you. The "extra-damage" roll fires about 1 in 240 per
qualifying hit. Eating any Rider corpse (Death, Pestilence, *or*
Famine) is genuinely instantly fatal regardless of HP.

**Defenses:** Poison resistance makes you immune. Most characters
can get this early by eating enough appropriate corpses. It's one
of the first intrinsics worth acquiring.

#### Brainlessness
<!-- audit
2026-05-18:
- mind flayer 3 tentacles, master 5 tentacles; AD_DRIN + AT_WEAP 1d8 (monsters.h:523-535)
- INT loss rnd(2) per hit; up to 10 lost per turn from a master (uhitm.c:3263)
- brainlessness death; lifesaving still dies (eat.c:698-715)
- 1-in-5 chance of losespells per hit (uhitm.c:3264)
- losespells zeroes rn2(n+1) random spells; re-study restores them (spell.c:1759-1827)
- 5.0 AD_DRIN no longer wipes maps or item IDs — only spells (uhitm.c:3263-3271: only adjattrib INT, losespells, drain_weapon_skill — no forget_map/forget_objects calls)
- polymorphed into a mindflayer, brain-eating restores Int (eat.c:679-688)
- any helmet blocks 7/8 tentacle drains via `uarmh && rn2(8)` (uhitm.c:3235)
- greasing adds an extra slip-roll on top of the helmet check (uhitm.c:3232 → u_slip_free at mhitu.c:1047-1064)
- blessed potion of restore ability restores all lost attributes (potion.c:646-691)
- blessed potion of full healing does NOT restore stats (potion.c:1144-1162)
- prayer fixes drained attributes via TROUBLE_POISONED (pray.c:270-272, 547-552)
- unicorn horn no longer restores attributes in 5.0 (apply.c:2306-2327)
- strategy aligned with NetHackWiki Mind flayer, Helm: any helmet blocks 7/8 tentacles, greasing stacks slip-roll, range-kill is safest (https://nethackwiki.com/wiki/Mind_flayer, https://nethackwiki.com/wiki/Helm)
-->

Mind flayers drain Intelligence with their tentacle attacks. If
your Intelligence drops to your racial minimum (3 for humans), the
next drain kills you: "brainlessness." A regular mind flayer has
three tentacle attacks per turn; the **master mind flayer** has
*five*, plus a heavier weapon strike. A single unprepared turn
next to a master mind flayer can drop your Int by up to ten.
Each hit also has a 1-in-5 chance to trigger **spell amnesia**: a
random number of your memorized spells (zero to all of them) drop
to zero retention; re-study from spellbooks to restore. (Before
5.0 amnesia used to wipe maps and identification also, but no
longer.)

**Defenses:** **Wear any helmet.** Even a plain orcish helm blocks
seven of every eight tentacle drains. Greasing the helmet stacks an
additional slip-off roll on top, so a greased helmet is the gold
standard. Better yet, kill them at range (wands, spells) so the
question doesn't arise. One counterintuitive detail: a mind
flayer's *mind blast* only fires if you have telepathy. If you're
wearing an amulet of ESP and you can spare the turn, take it off
before the fight. To recover drained Intelligence you need a
*potion of restore ability* (uncursed restores one stat; blessed
restores all), the spell of restore ability, or prayer when you're
in good standing. In 5.0 the unicorn horn no longer restores lost
attributes, so don't rely on it. Stockpile at least one restore
ability before pushing into mind flayer territory.

#### Engulfment

Two monsters hide in plain sight until you walk into them. The
**lurker above** (`t`, gray, level 10) hides on the ceiling and
drops onto whoever passes underneath; the **trapper** (`t`,
green, level 12) hides on the floor and engulfs whoever steps
onto it. Both look like ordinary terrain until they trigger.
Engulfment wraps and crushes rather than digesting, but you still
take damage every turn until you cut your way out, with limited
movement options while inside.

Other engulfers don't hide; they just swallow you in melee.
Dragons and purple worms can swallow whole creatures up to their
size. Dragons tend to be polite about it (you escape after one or
two turns); purple worms are the bigger danger, and the dread
**fog cloud** and **air elemental** count as engulfers too even
though they don't digest.

**Defenses:** Searching reveals hidden monsters. *Telepathy*
shows them through the deception. Wearing a *ring of warning* or
a *helm of caution* tips you off before you step.

**Getting out.** Once engulfed, attack the host repeatedly;
weapons still work from inside. If you have a wand of digging,
zap it (no direction needed): it almost always expels you
immediately, leaving the engulfer at 1 HP. A wand of opening or
the knock spell forces the engulfer to release you on the spot
without killing it, useful if a *tame* purple worm has swallowed
you in conflict.
Ranged spells and rays will tear into the host from the inside.

#### Drowning
<!-- audit
2026-05-18:
- drown check uses monster's tile (uhitm.c:3389-3390)
- Swimming, Amphibious, or Breathless all defeat the drown (youprop.h:264-277)
- pool-entry check at hack.c:3272; Flying also skips entry, Levitation is the canonical defense
- emergency_disrobe is gated on Stressed+ (trap.c:4897-4941)
- krakens placed only on medusa-4 in the Dungeon (medusa-4.lua:122); other placements are Quest/fakewiz/wizard1
- "swamp rooms" comment refers to eels, not krakens (mkroom.c:557-565)
- encumbrance does NOT gate the grab-drown path: being Burdened won't save you once grabbed
- strategy aligned with NetHackWiki Drowning, Giant eel, Amulet of magical breathing: range-kill sea monsters, magical breathing/Swimming/Amphibious as the only true grab-drown defenses (https://nethackwiki.com/wiki/Drowning, https://nethackwiki.com/wiki/Giant_eel, https://nethackwiki.com/wiki/Amulet_of_magical_breathing)
-->

Giant eels, electric eels, and krakens can grab you with their
wrap attack. Once they have you, each of the monster's turns you
can drown — the check uses the *monster's* tile (always water for
an eel or kraken), not yours, so you can drown even while standing
on adjacent dry land. Only *Swimming*, *magical breathing*, or
*amphibious form* prevent the drown; encumbrance doesn't matter
here. (Encumbrance only matters if you *fall* into water and need
to crawl out — stressed or worse forces emergency disrobe.) You'll
meet eels and krakens at Medusa's level, in moats around the
Castle, in swamp rooms, and on the Water Plane.

**Defenses:** An amulet (or spell) of *magical breathing* gives
you Breathless and ends the grab-drown threat. Levitation keeps
you above pools so you can't walk into them, but **does not save
you from an eel's grab** once it lands. Kill sea monsters at range
whenever possible — their grab attack requires adjacency.

#### Petrification (Stoning)
<!-- audit
2026-05-18:
- stoning timer starts at 5 (uhitm.c:3937)
- ticks 5→1 with five distinct messages (timeout.c:128-148)
- at counter 3 "limbs have turned to stone" sets nomul(-3) paralysis (timeout.c:163-165)
- two more messages fire after paralysis before done(STONING) at counter 0
- acid-blob corpse grants TIMED HStone_resistance += d(3,6), not permanent (eat.c:932-934, 1089-1094)
- Unchanging does not interrupt stoning: only blocks poly (polyself.c:1381-1384)
- poly_when_stoned auto-cure requires already being a non-stone golem (mondata.c:80-85)
- plain wand of polymorph cannot target the poly_when_stoned outcome
- stepping on a cockatrice corpse without Fumbling is safe
- Fumbling can trip the hero onto the corpse for instapetrify (timeout.c:1256-1261)
- strategy aligned with NetHackWiki Stoning, Cockatrice, Lizard: gloves around cockatrice corpses, lizard/acid corpse to interrupt the countdown, weaponized corpse for offense (https://nethackwiki.com/wiki/Stoning, https://nethackwiki.com/wiki/Cockatrice, https://nethackwiki.com/wiki/Lizard)
- eating any acidic corpse cures in-progress stoning (eat.c:860-861, fix_petrification at eat.c:867-877)
2026-05-23:
- cockatrice hiss (AD_STON) fires on 1/3 of landed melee hits (uhitm.c:4215)
- stoning roll within is `!rn2(10) || flags.moonphase == NEW_MOON` (uhitm.c:4245)
- 5.0 explicitly removed the lizard-corpse new-moon override (uhitm.c:4231-4243 source comment)
- net per-hit stoning rate: ~1/30 baseline, ~1/3 on new moon
- citation: source comment names the design change; NetHackWiki Cockatrice page still documents pre-5.0 lizard mitigation (https://nethackwiki.com/wiki/Cockatrice)
-->


Petrification is the dungeon's most notorious way to instantly
kill you, and the reason every experienced player carries a lizard
corpse. Touching a
cockatrice without gloves, eating a cockatrice corpse, catching
Medusa's gaze, or **kicking** a cockatrice corpse barefoot will
turn you to stone. *Stepping* on the corpse is safe so long as
you don't have Fumbling (Fumbling can trip you over the corpse for
instant death). The process is sometimes immediate; otherwise a
five-turn countdown announces itself with *"You are slowing down,"*
*"Your limbs are stiffening,"* *"Your limbs have turned to stone"*
(at which point you are **paralyzed** and can no longer act),
*"You have turned to stone,"* and *"You are a statue"* (death).

**Defenses ahead of time:** wear gloves around cockatrice corpses,
use reflection against Medusa, and pile up *timed* stoning
resistance from acid blob corpses (each one grants d(3,6) turns of
HStone resistance: useful but not permanent). For something
permanent, wear yellow dragon scale mail.

**Peril in the new moon.** A cockatrice's hiss has a small chance
to start stoning on any landed melee hit (roughly 1 in 30). On
the real-world night of a new moon, that jumps to about 1 in 3.
Hunt the nest on another night.

**Defenses while it's happening:** eat a lizard corpse (this is
why you carry one), eat an acidic corpse, drink a potion of acid,
pray, or cast stone-to-flesh on yourself. Keep the lizard in your
**main inventory**, not in a bag: pulling it out of a bag takes a
turn you can't spare against a two-turn timer. Note: act *before*
the "Your limbs have turned to stone" message — after that
you're paralyzed for three turns and the final messages kill you. Amulet
of Unchanging does **not** interrupt stoning. If you happen to be
polymorphed into a non-stone golem, wearing it during the countdown
is actively harmful — it blocks the stone-golem auto-poly that
would otherwise save you on death.

Out of lizards? Any acidic corpse will do: acid blob, jellies,
yellow dragon, black naga, and yes, green slime works (but green
slime starts a *different* countdown that turns you to slime; only
reach for it as a last resort). Quaffing a potion of acid has the
same curative effect.

**The other side of the coin:** a wielded cockatrice corpse (with
gloves on) is one of the game's most devastating weapons —
anything you hit that lacks stoning resistance turns to stone. The
classic offense, known to veterans as the "rubber chicken,"
handles demon lords, Medusa, and even a Rider on a good day. The
failure modes you must guard against are falling into a pit, hole,
or trapdoor while carrying it, and losing the gloves. Thrown
cockatrice eggs work the same way and have the same hazard if a
monster throws one at you.

#### Disintegration
<!-- audit
2026-05-18:
- only player-facing AD_DISN is black dragon breath (monsters.h:1520, ZT_BREATH(ZT_DEATH) at zap.c:4464-4493)
- beholder is the only other AD_DISN monster and is #if 0-gated (monsters.h:367-371)
- black dragons have MR_DISINT in attack and defense slots (monsters.h:1523)
- reflected beam does 0 damage to them via resists_disint (zap.c:4318)
- worn-armor priority on disint hit: shield first (zap.c:4476-4479), then body armor + cloak (zap.c:4480-4486)
- amulet of life saving rescues you (end.c catches DIED) but breath still destroys cloak/shirt (zap.c:4487-4492)
- an ordinary shield eats one breath; shields of reflection don't have a failure mode (zap.c:4476-4479)
- Antimagic check is on the death-ray branch only; the AD_DISN breath branch checks Disint_resistance only (zap.c:4464-4497)
-->

A black dragon's breath is the only monster, spell, or wand that
disintegrates you. (A deeply angered god can also call down a
wide-angle disintegration beam as a follow-up to lightning;
reflection won't block that one. Only disintegration resistance
will. Stay on speaking terms with your god.)

**Defenses:** Disintegration resistance (from eating a black dragon
corpse or wearing black dragon scale mail) gives full immunity.
**Reflection** bounces the breath back, protecting you — but black
dragons are themselves disintegration-resistant, so the bounce
won't kill them. Magic resistance does **not** help.

**Without disintegration resistance**, the game tries to save your
worn armor before disintegrating you: the breath destroys your
**shield** first if you have one, then your **body armor**; only
if neither is worn do you die outright (with your cloak and shirt
destroyed in the process). So an ordinary shield at least eats one
breath for you before being lost. An amulet of life saving still
rescues you from the fatal case, though you lose any armor it took.

#### Level Drain
<!-- audit
2026-05-18:
- vampire bats deal AD_DRST (drain Strength), NOT AD_DRLI — pois-res blocks (monsters.h:1291-1297)
- shield of drain resistance is new in 5.0 (objects.h:656-658)
- eating wraith corpse adds a level via pluslvl (eat.c:1141)
- drained-level HP/Pw math uses u.uhpinc / u.ueninc (exper.c:251-273)
- wraith corpse weightless and untinnable because cnutrit==0
- sysopt.seduce defaults to 1 (sys.c:100)
- foocubus bite is AD_SSEX; AD_SSEX→AD_DRLI substitution only fires when SEDUCE disabled (mhitu.c:327-334)
- blessed potion of restore ability restores ALL lost levels (potion.c:687-691)
- uncursed/plain restore ability returns one level per quaff
- strategy aligned with NetHackWiki Drain resistance, Wraith, Excalibur: Excalibur/Stormbringer/Staff of Aesculapius for drain resistance, eat wraith corpse to regain a level (https://nethackwiki.com/wiki/Drain_resistance, https://nethackwiki.com/wiki/Wraith, https://nethackwiki.com/wiki/Excalibur)
-->

A recurring theme in the bestiary: certain monsters reduce your
experience level on a hit, taking the HP and power gains that came
with each lost level. Wraiths, barrow wights, Nazgul, vampires,
vampire leaders, and Vlad himself all carry level-drain attacks.
Stormbringer in an enemy's hand does the same. Drained levels do
not come back on their own. You re-earn them by killing more
monsters, by drinking a potion of restore ability (a blessed one
restores all lost levels at once), or by eating a wraith corpse.

(Don't confuse drain-life with *Strength* drain: a vampire bat's
poisoned bite drains Str, not levels. Stat drain is a separate
problem and [Enchantment Drain](#enchantment-drain) covers its cousin.)

**Defenses:** *Drain resistance* makes you immune. The classic
sources are wielding Excalibur (Lawful), Stormbringer (Chaotic),
or the Staff of Aesculapius (Healer's quest artifact). New in 5.0:
wearing **black dragon scale mail** (disintegration resistance
plus drain resistance, both in one slot) or a **shield of drain
resistance** (random shop find, no other property).

Eating a fresh wraith corpse restores one experience level and is
one of the better reasons to keep one fresh; wraith corpses are
weightless and can't be tinned (no nutrition), so eat them as soon
as the fight ends.

#### Enchantment Drain
<!-- audit
2026-05-18:
- disenchanter generates only in Gehennom (G_HELL: monsters.h:2156, makemon.c:1935, 1998)
- active claw targets armor via some_armor (do_wear.c:2629, uhitm.c:3619)
- target order: cloak → body armor → shirt → 1/4 chance for helm/gloves/boots/shield (do_wear.c:2634-2652)
- if naked, rn2(5) picks ring/amulet/blindfold; never targets a wielded weapon (uhitm.c:3621-3640 mhitm_ad_ench cases 0-4 enumerate uright/uleft/uamul/ublindf only)
- active hit prints "Your X seems less effective" (uhitm.c:3641)
- weapon drain is passive-only: fires when you melee the disenchanter (mhitu.c:2508-2515)
- passive drain is silent
- obj_resists: 10% chance for ordinary, 90% for artifact (zap.c:1392-1394)
- Invocation items and Rider corpses always resist (zap.c:1462-1467)
- MC negates the active attack (uhitm.c:3613) but NOT the passive counter
- eating a disenchanter corpse strips a random intrinsic (eat.c:1270-1275)
- strategy aligned with NetHackWiki Disenchanter, Magic cancellation: MC armor blocks the active claw but not the passive counter; range-kill is the cleanest plan, and the corpse is not safe to eat (https://nethackwiki.com/wiki/Disenchanter, https://nethackwiki.com/wiki/Magic_cancellation)
-->

**Disenchanters** (`R`, blue) appear only in Gehennom. Their
claw is the silent ascension-killer it's reputed to be, but the
mechanic is more constrained than common lore suggests.

Their **active** claw picks one of your worn armor pieces (cloak
first, then suit, then shirt, then helm, gloves, boots, or shield
by weighted chance) and shaves 1 off its enchantment. If you have no armor at
all, it can instead chew a ring, amulet, or blindfold. **It can't
reach your wielded weapon** with the active attack. The game does
print "Your *thing* seems less effective" each time, so you'll
know when it lands.

Your weapon only takes enchantment damage as a **passive** counter
when you hit them in melee. Three or four melee strikes will take
a +7 sword to +3; that passive drain is silent. Range-killing
sidesteps both attacks at once.

**Defenses.** **Magic-cancellation armor** at MC3 mostly blocks
their armor drain, but doesn't stop melee from draining your
weapon. Don't melee them even with MC3 armor. Rings of conflict and pets
reliably redirect them to other targets. Artifacts resist drain
9 times in 10; ordinary items only 1 in 10. **Don't eat the
corpse**: it strips a random intrinsic.

<!-- audit
2026-05-18:
- lurker above is ceiling-hider, M1_HIDE+M1_FLY; trapper is floor-hider, M1_HIDE (monsters.h:973-998)
- both use AT_ENGL with AD_WRAP+AD_PHYS, NOT AD_DGST (5.0 retcon away from digestion)
- damage handler at mhitu.c:1437-1453
- search reveals; both have no M1_MINDLESS so telepathy and warning work too
- warnreveal triggers when mlev/4 ≥ warning level (detect.c:2107-2120)
- weapons still hit normally while swallowed: mhit guaranteed when u.uswallow (uhitm.c:781, 805)
- wand of digging while swallowed: zap_dig reduces engulfer HP to 1 and calls expels (dig.c:1568-1582); whirly engulfers ignored
- wand of opening / knock spell at engulfer or at self: release_hold expels you (zap.c:382-391, 575-609, 2929-2947)
- ranged buzz wands "rip into" the engulfer from inside (zap.c:4802-4820)
-->
#### The Touch of Death
<!-- audit
2026-05-18:
- self-zap WAN_DEATH or SPE_FINGER_OF_DEATH skips the Antimagic check (zap.c:2885-2902)
- only the ray-bolt path checks Antimagic (zap.c:4497-4502)
- self-zap escape requires being nonliving (undead/manes/golems/S_VORTEX) or is_demon (mondata.h:219-220)
- Rider Death rn2(20): 17-19 = full touch (15%), 5-16 = permdrain=1 (60%), 0-4 = miss (25%) (uhitm.c:3858-3882)
- 8d6 + 50 + half-damage permdrain only on rolls 17-19
- MR on the 17-19 branch falls through to the smaller permdrain rather than being harmless
- the smaller permdrain on rolls 5-16 is NOT reduced by MR (mcastu.c:326-337)
- strategy aligned with NetHackWiki Touch of death, Wand of death, Death resistance: MR blocks incoming death rays but not self-zap; nonliving/demon polyform is the self-zap fallback (https://nethackwiki.com/wiki/Touch_of_death, https://nethackwiki.com/wiki/Wand_of_death, https://nethackwiki.com/wiki/Death_resistance)
-->

Some monsters, most notably Death (one of the Riders on the Astral
Plane), can kill you with a single touch. The Finger of Death spell
and the wand of death work similarly. **Do not zap a wand of death
or finger of death at Death the Rider** — Death absorbs the
attack and gains max HP. Magic missile is the recommended answer
against all three Riders.

**Death the Rider's touch** rolls 1d20 each hit. Rolls 17-19 trigger
the full **8d6 + 50** instakill attempt and permadrain half the
damage from your max HP — magic resistance fully blocks this
high-damage branch. Rolls 5-16 (the most common 60%) deliver a
smaller life-drain that MR does **not** block. Rolls 0-4 miss
entirely. A high-level character with many hit points can survive
the high-damage hit; the permadrain still hurts.

**The wand of death and Finger of Death spell** are gated by magic
resistance only when the death ray *hits you from outside*. If you
misfire and self-zap, MR doesn't save you — only being **nonliving**
(polymorphed into a vampire, lich, skeleton, etc.) or a demon will.
This is one of the rare cases where being polymorphed into something
dead is the safer state. The same nonliving/demon immunity also
protects against incoming death rays.

An amulet of life saving will revive you once if the touch or zap
kills you outright.

<!-- audit
2026-05-18:
- hunger thresholds: Satiated >1000, Not Hungry >150, Hungry >50, Weak >0, Fainting ≤0 (eat.c:3369-3372)
- faint path (eat.c:3410-3432)
- STARVED death at u.uhunger < -(100 + 10*Con) (eat.c:3437-3447)
- initial u.uhunger = 900 (eat.c:129)
- TROUBLE_STARVING covers Weak through STARVED (pray.c:216-217)
- strategy aligned with NetHackWiki Hunger, Prayer: praying when Weak/Fainting is a canonical TROUBLE_STARVING fix (https://nethackwiki.com/wiki/Hunger, https://nethackwiki.com/wiki/Prayer)
-->
#### Genocide
<!-- audit
2026-05-18:
- confused-uncursed scroll of genocide self-genocides your role's species (read.c:1737)
- PLAYER+REALLY branch in do_genocide kills you with killer = "genocidal confusion" (read.c:2838-2972)
- mndx = u.umonster = gu.urole.mnum (read.c:2839, u_init.c:991) — role species (PM_VALKYRIE etc.), not race
-->

Reading an uncursed scroll of genocide while confused can genocide
your own species. Don't do this.

#### Saving Yourself from Imminent Death {#delayed-deaths}
<!-- audit
2026-05-19:
- sliming timer is 10, not 9: make_slimed(10L,...) (uhitm.c:3199, eat.c:854, polyself.c:456, uhitm.c:3570)
- the "9-turn" impression came from the t/2 message cadence (timeout.c:391)
- cancellation prevents new infections (uhitm.c:3556-3560) but does NOT clear a running Slimed timer
- polymorph cure requires flaming() or PM_GREEN_SLIME (polyself.c:842)
- vomiting cures only SICK_VOMITABLE; Pestilence's SICK_NONVOMITABLE is unaffected (eat.c:3745-3746)
- rotted-corpse food poisoning is gated by Sick_resistance, NOT poison resistance (eat.c:1904-1914)
- Fire_resistance survives lava damage but still gets trapped: lava_effects sets utrap TT_LAVA on the fire-res branch (trap.c:6964-6968)
-->

Not every fatal threat kills instantly. Several give you a few
turns to react.

**Sliming.** Being hit by a green slime (or eating its glob, or
being digested by one as a polyform) starts a ~10-turn
transformation into a green slime yourself — dead. **Cures:** burn
the slime off with fire (a wand of fire zapped at yourself, a
scroll of fire read at self, a fire trap, a red dragon's breath);
polymorph into a flame-bodied or slime-immune form; or cast the
spell of *cure sickness*. An **amulet of unchanging** blocks the
contagion entirely and even aborts a transformation already
underway. Cancelling the green slime in melee prevents new
infections but does nothing to a timer already running. Prayer
would cure it, but green slime lives in Gehennom where prayer
fails, so don't plan on it. Fire is the most reliable cure.

**Illness (food poisoning).** Eating a rotten corpse or certain
attacks (giant ant, etc.) gives you food poisoning, which kills in
10–19 turns ("You feel deathly sick."). **Cures:** a unicorn horn
(apply it), pray, eat a eucalyptus leaf, or vomit (by being
satiated and eating more). Vomiting from other causes also cures
food poisoning. Poison resistance does NOT protect against food
poisoning — that's *sickness resistance*, a separate intrinsic.

**Pestilence's terminal illness** is the harder cousin: vomiting
won't clear it, and the timer is Constitution-dependent (~20+Con
turns). The cures that *do* work: unicorn horn, prayer, eucalyptus
leaf.

**Sinking in lava.** Falling into lava without levitation or fire
resistance gives you a few turns to escape before you sink and die.
Your inventory is also at risk. **Cures:** prayer, levitation
(put on levitation boots or a ring), teleport, or just step out if
you can. Fire resistance prevents the damage but doesn't prevent
sinking. Lava immersion also destroys most of your inventory.

**Drowning (being held).** When grabbed by an eel or kraken in
water, you have a few turns to escape before drowning. The drown
check uses the eel's tile, so levitation, water walking, and
encumbrance status are irrelevant once the grab lands. **Cures:**
magical breathing (amulet or spell), kill or teleport the eel
before it pulls you under, or avoid water entirely. See
[Drowning](#drowning) in [Ways to Die Instantly](#ways-to-die-instantly) for the full picture.

**Strangulation.** Wearing a cursed amulet of strangulation slowly
kills you over a few turns. **Cure:** remove the amulet (requires
uncursing it first, since cursed amulets can't be removed: use a
scroll of remove curse, holy water, or prayer).

---

### Divine Relations
<!-- audit
2026-05-18:
- TROUBLE_PUNISHED = -1 is a MINOR trouble, not major (pray.c:91)
- major troubles: stinking cloud (TROUBLE_REGION), collapsing, stuck-in-wall, cursed levitation boots, unusable hands, cursed blindfold (pray.c:218-243)
- minor afflictions: blind=-5, stunned=-9, confused=-10, hallucination=-11 (pray.c:95, 99-101)
- crowning adds rnz(1000) * kick on top of the ordinary rnz(350) prayer wait (pray.c:1356-1361)
- crowning does NOT lock alignment — the one-way conversion gate is ualignbase[CURRENT]==ualignbase[ORIGINAL] (pray.c:1638)
- same-race blood always converts lawful or neutral altars to CHAOTIC, never to co-aligned (pray.c:1717-1720)
- on a chaotic altar, same-race blood summons a demon (pray.c:1723-1739)
- strategy aligned with NetHackWiki Prayer, Sacrifice, Protection racket, Crowning: prayer-as-emergency rules, sacrifice-fresh-corpses, protection-AC stacks across donations, crowning penalty (https://nethackwiki.com/wiki/Prayer, https://nethackwiki.com/wiki/Sacrifice, https://nethackwiki.com/wiki/Protection_racket, https://nethackwiki.com/wiki/Crowning)
-->


Your relationship with your god is one of the most important
mechanics in the game. A happy god answers prayers, forgives
transgressions, and occasionally sends gift artifacts. An angry god
smites you.

#### Prayer

Praying (`#pray`) calls on your god for help. When conditions are
right, prayer is the single most powerful emergency tool in the
game. When conditions are wrong, it can kill you.

> *The mechanics below are inspired by Matthew Lahut's Praying
> Spoiler, the long-running RGRN reference for the prayer system.*

**What prayer fixes (in priority order).** Your god addresses your
problems in a specific order, fixing the most urgent first:

1. Petrification in progress (stoning)
2. Sliming in progress
3. Strangulation
4. Sinking in lava
5. Illness (food poisoning, sickness)
6. Severe hunger (Weak or Fainting)
7. Standing in a stinking cloud
8. Critically low HP (≤5, or below a fraction of maxHP that scales with your experience level: 1/5 at XL 1–5, 1/6 at 6–13, 1/7 at 14–21, 1/8 at 22–29, 1/9 at XL 30+)
9. Lycanthropy
10. Stuck in a wall, collapsing under load, cursed levitation boots, unusable hands (cursed glove + cursed wielded weapon), cursed blindfold

After resolving the major troubles above, your god may also grant
additional blessings: clearing minor afflictions (plain hunger,
blindness, confusion, stunning, hallucination, ordinary punishment
with iron ball and chain), improving your alignment, or even
gifting intrinsics like telepathy or speed.

**The requirements for a safe prayer.** All of the following must
be true:

- Your **alignment** must be non-negative. Killing peacefuls,
  robbing shops, and other misdeeds reduce alignment. Sacrifice
  and virtuous behavior raise it.
- Your **luck** must be non-negative. Luck is affected by many
  things (see [Luck and Fortune](#luck-and-fortune)).
- Your god must not be **angry**. God anger is separate from
  alignment and accumulates from specific offenses (breaking
  conduct with your god, desecrating altars).
- The **prayer timeout** must have expired. After a successful
  prayer, you must wait before praying again. The timeout averages
  around 450 turns but can range from under 200 to over 700 due to
  the random formula used. In a genuine emergency (HP critical,
  starving), there is some forgiveness if your timeout is close to
  expiring.
- You must not be **polymorphed** into a demon or undead while
  worshipping a non-chaotic god.
- You must not be in **Gehennom** (unless you worship Moloch, which
  no standard role does). Your god cannot hear you there. This is
  one of the things that makes Gehennom so dangerous.
- If you're on an altar, it should be **co-aligned**. Praying on a
  cross-aligned altar directs your prayer to the wrong god.

**When prayer goes wrong.** If any requirement is unmet, your god
responds with punishment instead of help: loss of alignment, loss of
luck, increased timeout, cursing of worn items, or summoning of
hostile minions. Severe transgressions (praying to a very angry god)
can trigger lightning or disintegration, both potentially fatal.

**Practical guidance.** Pray when you're about to die and have no
other option. Starvation, stoning, illness, and critically low HP
are all valid emergencies. Don't waste prayers on minor
inconveniences. Before you pray, make a mental check: is my
alignment positive? Have enough turns passed? Am I on a co-aligned
altar or no altar at all? If you can't answer yes to these, find
another solution.

**Prayer timeout tracking.** The game doesn't show your timeout
directly, but you can estimate it. Count roughly 500 turns from
your last prayer (more if it went badly). In the early game, when
turns are slow and you're fighting one creature at a time, 500
turns pass quickly. In the late game, when you might take 100
actions per level, it takes longer to feel.

#### Sacrifice

Sacrifice is a trade: a corpse you could eat, given up to your god
in exchange for divine help. Drop a fresh corpse on an altar that
matches your alignment (`#offer`) and your god takes notice. Over
time that notice pays out as artifact weapons, holy water, restored
alignment, and eventually a crown.

The rules:

- The corpse must be fresh — killed within the last **50 turns**.
  A corpse older than that has zero sacrifice value (the gods
  simply ignore it).
- Bigger monsters are more valuable sacrifices, and your god
  expects more impressive offerings as you advance. If the altar
  gives back *"You have a feeling of inadequacy,"* the corpse fell
  short of what your god was hoping for this time.
- The altar must match your alignment, or you're praying to someone
  else's god (which has its own consequences).
- Same-race sacrifice is forbidden and severely punished. On a
  lawful or neutral altar it turns the altar chaotic (not co-aligned —
  only chaotic heroes benefit); on a chaotic altar it summons a demon.

With enough sacrifice credit, your god may gift you an artifact
weapon. The first gift comes after relatively modest sacrifice;
subsequent gifts require substantially more. The per-attempt
chance is roughly 1 in (10 + 2·*n*), where *n* is the number of
gifts you've already received, so the first roll is 1-in-10 and
the second drops to about 1-in-14. Don't be surprised if you get one artifact and then
nothing more for thousands of turns.

The first gift is biased toward your role's signature artifact
(Magicbane for Wizards, Demonbane for Priests, Mjollnir for
Valkyries, and so on), so sacrifice early — it locks in the
role-bias gift before the random pool dilutes it. Gift artifacts are
always aligned to your god and always match a weapon skill you can
use.

There is a minimum. In 5.0, not every corpse you drop on
the altar moves you toward the next artifact gift. The gods have
opinions about what constitutes a worthy offering, and a kobold doesn't
make the cut. Fresh corpses of appropriately challenging monsters are
what advances your standing.

#### Donating to Priests

A peaceful priest in their own temple accepts donations. `#chat` to
them and a prompt appears: *How much will you offer (suggested: X or
Y)?* The two numbers are the priest's suggested thresholds for
the two reward tiers.

**What you get:**

- **Clairvoyance** — a few hundred turns of automatic short-range
  map awareness (you "see" the immediate area around you every few
  turns without moving). Granted if you offer in the lower tier.
- **Protection** — an intrinsic AC bonus that *stacks* across
  visits. Granted if you offer in the upper tier. Your **first**
  donation grants 2–4 points; subsequent donations add 1 each up
  to 9; past 9, the chance to get another point drops to 1-in-N.
  The bonus persists for life, unlike clairvoyance.

**The cost.** Pay enough and the benefit is yours. The priest's
prompt always shows you the exact ask, which scales with your
experience level and how much gold you're carrying:

- **Clairvoyance:** a randomized 150–250 zorkmids × experience
  level as the base ask
- **Protection:** twice that — 300–500 zorkmids × experience level

If you walk in carrying far more gold than the baseline, the
priest scales the ask up to match, roughly a third of your purse
for clairvoyance, two-thirds for protection. A rich hero who hands
over only the baseline amount will be politely thanked but not
blessed. The prompt always tells you the exact figure, so trust
it over any rule of thumb.

**The cheapskate penalty.** If you offer noticeably less than
what's expected while clearly able to afford more, the priest
calls you a Cheapskate and will hold a grudge: the next time you
chat with that same priest, the cost will be higher. The
penalty stacks if you keep doing it, and it sticks for the rest of
the game. Other priests in other temples aren't affected. Refusing
to donate anything at all also costs you alignment with your god.

**Practical guidance:**

- **Donate early, donate often.** Protection stacks, so 500 zm at
  XL 1 buys the same AC reduction as 15000 zm at XL 30. Visiting
  the Minetown temple every time you climb back up from the Mines
  is a classic stacking ritual.
- **Count gold before chatting.** The priest's roll is sensitive to
  what's in your inventory; drop excess gold on the floor outside
  the temple before asking, then pick it back up.
- **Cross-aligned priests still accept donations** and still grant
  the AC and clairvoyance. You miss the alignment bonus and you
  can't sacrifice on their altar, but the AC ramp still works.
- **Walk away rather than lowball.** Once the cheapskate flag is
  set on a priest, it doesn't come off. If the suggested amount is
  more than you want to part with, decline the prompt entirely
  rather than offering a token sum.

<!-- Donation mechanics: src/priest.c priest_talk(), 5.0 line 638:
     rn1(101, 150 + cheapskate * 40) × u.ulevelpeak. Tier thresholds
     at suggested × quan, 2 × suggested × quan, 3 × suggested × quan,
     where quan = max(1, money / (3 × suggested × XL)). -->

#### Altars and Alignment

To convert a cross-aligned altar, sacrifice ordinary fresh
corpses on it. Each attempt either flips the altar to your god
(success), costs you Luck (failure), or, if your god is already
angry, converts *you* to the altar's alignment instead. Better
odds at higher experience level. Worth the risk when you need a
co-aligned altar for sacrifice gifts, holy water, or BUC testing.

Two complications worth knowing. A *successful* conversion can
still summon a pair of hostile minions from the displaced god,
arriving just as you exhale; have an exit plan in case the
"victory" comes with company. And if you try this with a
*negative* alignment record, the result inverts: instead of the
altar flipping to your god, your god disowns you and you become a
follower of the altar's god permanently.

Two things to **never** sacrifice on any altar:

- **A same-race corpse** (humans for most roles; also elves if
  you're elven). Punished on every altar; on a Chaotic one it
  summons a demon.
- **A unicorn whose alignment matches the altar.** Counts as an
  insult to that god.

#### Crowning

If your alignment record reaches 20 *and* your Luck reaches 10,
your god may crown you on a successful prayer. Crowning grants:

- A special title (e.g., "Hand of Elbereth" for lawful characters).
- An artifact weapon appropriate to your alignment, if one is
  available that you can use. A Lawful crowning transforms whatever
  long sword you happen to be wielding into Excalibur in place, so
  having a +7 long sword in hand at the moment of crowning gives
  you a +7 Excalibur.
- Intrinsic fire resistance, cold resistance, shock resistance,
  sleep resistance, poison resistance, and see invisible.
- Permanent skill-unrestriction on your alignment's sword slot, and
  permanent knowledge of your role's special spell.
- A class-specific bonus: Wizards get the *finger of death* spell;
  Monks get *restore ability*.

The catch is that crowning **adds about ~1000 turns of prayer
timeout** on top of the usual post-prayer wait, turning prayer into
an unreliable emergency tool. If you're sacrificing to fish for an
artifact gift, watch your piousness so you don't trigger a crowning
by accident. Applying a stethoscope to yourself reports it in
words, and *piously* is the highest band — the one in which the
next sacrifice could crown you.

---

### Making Friends
<!-- audit
2026-05-21:
- Titan stats: LVL(16, 18, -3, 70, 9); attacks AT_WEAP 2d8 + AT_MAGC AD_SPEL; M1_FLY, M2_ROCKTHROW, M2_MAGIC; difficulty 20 (monsters.h:1777-1785)
- Balrog stats: LVL(16, 5, -2, 75, -14); AT_WEAP 8d4 + AT_WEAP 4d6; M1_FLY; MR_FIRE|MR_POISON; difficulty 20 (monsters.h:3043-3051) — speed 5 is the limiter
- Archon stats: LVL(19, 16, -6, 80, 15); AT_WEAP 2d4 × 2 + AT_GAZE AD_BLND 2d6 + AT_CLAW 1d8 + AT_MAGC AD_SPEL 4d6; MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON; M1_FLY|M1_SEE_INVIS|M1_REGEN; M2_NOPOLY (monsters.h:1254-1265)
- polyok() rejects M2_NOPOLY: #define polyok(ptr) (((ptr)->mflags2 & M2_NOPOLY) == 0L) (mondata.h:93) — Archons cannot be a polymorph result
2026-05-18:
- "sad feeling for a moment" fires when an offscreen pet dies (mon.c:952, 3101, 3495)
- leaving a pet behind alive produces no message; loyalty decays at 1 per 150 moves apart (dog.c:689-697)
- pet curse-avoidance has a starvation exception (dogmove.c:535-538)
- tameness loss sources: hunger past threshold, long separation, player-dealt damage via abuse_dog (uhitm.c:1593-1595)
- scroll of taming radius: bd = confused ? 5 : 1, area (2*bd+1)² (read.c:1689) — 3×3 normal, 11×11 confused
- confused charm-monster spell fails outright (spell.c:1372) — the 11×11 trick is scroll-only
- strategy aligned with NetHackWiki Pet, Tameness, Scroll of taming: keep your pet fed for tameness, pet-shoplift trick, confused-scroll-of-taming 11×11 area effect (https://nethackwiki.com/wiki/Pet, https://nethackwiki.com/wiki/Tameness, https://nethackwiki.com/wiki/Scroll_of_taming)
- apport: edog->apport initialized to A_CHA (dog.c:60), grows as the pet eats food you drop near you, drives pickup/return behavior (dogmove.c:316-422); enables pet-shoplifting in practice
- magic whistle teleports pets toward the hero on every apply (apply.c whistle handler)
- gray dragon resists magic damage via resists_magm (mondata.c:215-225 includes AD_MAGM and PM_BABY_GRAY_DRAGON); magic-resistant targets cannot be polymorphed
- long worm's lengthening tail occupies a chain of map tiles (worm.c:27-100); the head moves but segments stay until they shrink
-->

The Mazes of Menace are dark, hostile, and full of things that want
to eat you. Under those circumstances, a loyal companion is worth
more than a bag of gold. Fortunately, the dungeon provides.

#### Starting Pets

Most roles begin with a faithful pet: a little dog or a kitten,
depending on your role. This small creature is more useful than it
looks. It follows you between levels (if adjacent when you take
stairs), fights alongside you, picks up items, and eats food it
finds on the floor. Think of it as a self-propelled, self-feeding
trap detector with teeth.

A pet that eats well and fights often will grow. A little dog
becomes a dog, then a large dog. A kitten becomes a housecat, then
a large cat. A grown large dog or large cat is a genuine combat
asset, capable of taking on mid-dungeon threats that would give
you trouble.

One more thing: your pet usually avoids cursed items when there's
an uncursed alternative, which makes it a *probabilistic*
curse-detector. Drop items on the ground and watch what your pet
walks past versus what it walks around. If it has no choice, it
will still cross the cursed square, but consistent avoidance
across many turns is a strong tell. Even when it does step onto
a cursed pile (chasing food, or pulled by a magic whistle), the
game prints *"[pet] moves reluctantly onto …"*. That message is a
giveaway.

#### Feeding and Loyalty

Pets have an invisible tameness score that decreases when they go
hungry past the threshold, when you leave them behind on another
level for too many turns, or when *you* hit them. (Combat damage
from other monsters doesn't reduce tameness.) When tameness hits
zero, the pet either goes untame-but-peaceful or turns fully
hostile. Feeding is the antidote:

- **Dogs and cats** love tripe rations and most meat
- **Horses** prefer apples, carrots, and other vegetarian fare

Tripe rations are ideal for dogs and cats. You'll find them
scattered through the dungeon. Always pick them up, even though
they're revolting food for humans. Your pet will adore you for it.

#### Taming New Creatures

If your starting pet perishes (or you want an army), several
methods of taming exist:

- **Throwing food** at a suitable creature: meat for dogs and cats,
  produce for horses
- **Scroll of taming** or **spell of charm monster** both route
  through the same handler and tame all eligible creatures within
  a 3×3 radius. Reading the scroll while confused widens that to
  11×11 (but you can't cast the spell while confused).
- **Magic trap effects** occasionally produce taming

Taming isn't limited to small animals: with a scroll of taming or
the charm monster spell, you can recruit a purple worm to swallow
your enemies whole (its growing tail will sprawl across the room
and get in the way of your shots), a dragon to breathe fire at
them, a titan to crush them underfoot. The exclusion list is substantial, though:
no humans (priests, shopkeepers, watchmen, soldiers, kings), no
covetous monsters (the Wizard, liches, masters), no demons (unless
you are one), no vault guards, quest leaders, nor minions can be
tamed. Unique monsters (Medusa, etc.) also resist.

#### What Pets Do for You

A well-fed pet earns its keep in several ways:

- **Combat muscle.** A strong pet clears rooms and softens up
  dangerous monsters before you engage
- **Curse detection.** The old drop-and-watch trick, described
  above: free, reliable, and available from turn one
- **Shoplifting.** If your pet picks up an item inside a shop and
  carries it out the door, the shopkeeper blames the animal, not
  you. This takes patience (the pet must wander onto the item,
  then wander back out) but it's the cheapest way to acquire a
  wand of wishing from a shop
- **Sacrifice fodder.** Monsters your pet kills leave corpses
  you can sacrifice on altars, exactly as if you'd killed them
  yourself

**Training apport (fetching).** Hand-feeding your pet builds a
score called apport. A pet with high apport will pick up nearby
items and bring them to you. This is what makes pet-shoplifting
practical: once your pet returns dropped items reliably, you can
drop something at the shop counter, walk out, and trust the pet
to follow with the goods. Pair it with a magic whistle (below) to
yank a loaded pet to your side from anywhere on the level.

**Upgrading your pet.** Three moves matter most.

- A **magic whistle** teleports every tame creature on the level
  to a spot next to you each time you blow it. Distance doesn't
  matter; trapped pets get freed in the process.
- Tame a **warhorse** early (throw apples or carrots) and you have
  a fast, hard-hitting mount before mid-game.
- Late in the run, **polymorph your pet** into a stronger form.
  **Titan** is a popular target: level 16, speed 18, flies,
  throws boulders, and casts spells. Faster than anything else
  this strong, so it keeps up with a speed-boosted hero, and the
  spell-cast attack threatens at range. Balrog hits harder but
  is speed 5, slow enough that anything that runs gets away.
  Gray dragon is an alternative when you specifically want the
  magic-resistance intrinsic and a body that won't accidentally
  re-polymorph.
- If you can tame an **Archon** directly (via a scroll of taming
  on a hostile, magic-whistle recall of one you tamed earlier, or
  a conflict-ring accident), do it. Archons are the consensus
  ultimate pet: level 19, speed 16, AC −6, magic
  resistance, sees invisible, flies, regenerates, and a multi-
  attack that includes a blinding gaze and a spell-cast. You
  cannot polymorph a pet into an Archon: you must encounter one
  and tame it.

#### Keeping Your Pet Alive

Pets die from the same things you do: traps, poison, powerful
monsters, drowning in water. Keep an eye on your companion's
health (`;` to farlook) and don't lead it into fights it can't
win. A dead pet is not just a loss of utility; it's a cold feeling
in the pit of your stomach.

If you change levels and your pet isn't adjacent, it won't follow.
Your pet is still alive on the previous level. Its loyalty is
ticking down, though, so go back for it before it forgets you
were friends.
A **magic whistle** is the recommended fix: applying one warps every
pet on your level to a square next to you, even on no-teleport
floors. **Sokoban** also doesn't let pet loyalty decay — leaving
a pet there while you do the Quest or the Mines is the dungeon's
safest kennel.

If you see *"You have a sad feeling for a moment"* — that's
different. That message means a pet of yours just died
offscreen on another level, usually one you left behind that
got into a fight it couldn't win.

Current editions have added two things that veteran pet-owners should know.

First: your pet eats for a reason beyond loyalty. The same corpse
mechanics that grant you resistances apply to pets as well. A pet that
dines on the right monsters will gain resistances: fire resistance, cold
resistance, whatever the dungeon's terrible buffet was offering. A
well-fed pet is also a better-armored one. This is not something you can
reliably engineer, but it's a reason to let your pet eat rather than
scooping up every corpse yourself.

Second: pets can now be revived. If your companion falls in battle,
stand on its corpse at a co-aligned altar and pray. The gods, in
their occasional mercy, may return it to you. This is a last-resort
miracle, not a renewable strategy: your prayer timeout, your
alignment, and a certain amount of luck all factor in. A pet
you've carried since the early game is worth a detour to the
nearest temple before you write it off.

---

## Part Four: Gear and Provisions

### A Practical Identification Strategy

Here is the central puzzle of the Mazes, and the thing that kills
more promising expeditions than any monster: you will find dozens of
items, and you won't know what most of them are.

Every game, the dungeon shuffles the deck. Potions, scrolls, wands,
rings, amulets, and spellbooks are all given randomized appearances.
The "milky potion" in this game might be healing; in your next game
it might be paralysis. The only things that stay consistent between
games are the item classes themselves (a `!` is always a potion, a
`?` is always a scroll) and the prices, which turn out to be the
single most powerful identification tool you have.

<!-- FLOWCHART-BEGIN -->
::: web-only

<div><figure style="margin: 1.5em 0; text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 736" role="img" aria-label="The identification flowchart" style="max-width: 760px; width: 100%; height: auto; font-family: 'EB Garamond', 'Garamond', 'Georgia', serif;"><title>The Identification Flowchart</title><defs><marker id="arrowhead" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker><style>.start{fill:#E8F4FD;stroke:#3B6FA0;stroke-width:2}.decision{fill:#FFF4E6;stroke:#B5651D;stroke-width:2}.action{fill:#F0F9E8;stroke:#5B8E3A;stroke-width:2}.final{fill:#FCE8E6;stroke:#A14A3F;stroke-width:2}.label{font-size:18px;fill:#1f2933;text-anchor:middle}.startlbl{font-size:19px;font-weight:600;fill:#1f2933;text-anchor:middle}.branch{font-size:16px;font-style:italic;fill:#5a5a5a}.edge{fill:none;stroke:#5a5a5a;stroke-width:1.5}</style></defs><rect class="start" x="40" y="20" width="320" height="50" rx="25" ry="25"/><text class="startlbl" x="200" y="51">Found an item</text><path class="edge" d="M 200 70 L 200 100" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="100" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="133">Can you reach an altar?</text><path class="edge" d="M 360 128 L 430 128" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="121" text-anchor="middle">yes</text><rect class="action" x="430" y="100" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="133">Drop it. Check BUC.</text><text class="branch" x="210" y="172">no</text><path class="edge" d="M 200 156 L 200 190" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="190" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="223">Is your pet nearby?</text><path class="edge" d="M 360 218 L 430 218" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="211" text-anchor="middle">yes</text><rect class="action" x="430" y="184" width="290" height="62" rx="8" ry="8"/><text class="label" x="575" y="210">Drop it. Pet avoids it?</text><text class="label" x="575" y="232" style="font-size: 16px;"><tspan style="font-style: italic; fill:#5a5a5a;">yes</tspan>: it's cursed; <tspan style="font-style: italic; fill:#5a5a5a;">no</tspan>: it's safe</text><text class="branch" x="210" y="262">no</text><path class="edge" d="M 200 246 L 200 290" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="290" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="323">Can you reach a shop?</text><path class="edge" d="M 360 318 L 430 318" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="311" text-anchor="middle">yes</text><rect class="action" x="430" y="290" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="323">Check price.</text><text class="branch" x="210" y="362">no</text><path class="edge" d="M 200 346 L 200 380" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="380" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="413">Is it a wand?</text><path class="edge" d="M 360 408 L 430 408" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="401" text-anchor="middle">yes</text><rect class="action" x="430" y="380" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="413">Engrave-test it.</text><text class="branch" x="210" y="452">no</text><path class="edge" d="M 200 436 L 200 470" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="470" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="503">Spare ring or potion with a sink?</text><path class="edge" d="M 360 498 L 430 498" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="491" text-anchor="middle">yes</text><rect class="action" x="430" y="470" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="503">Drop ring or dip potion.</text><text class="branch" x="210" y="542">no</text><path class="edge" d="M 200 526 L 200 560" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="560" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="593">Is it safe to use-test?</text><path class="edge" d="M 360 588 L 430 588" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="581" text-anchor="middle">yes</text><rect class="action" x="430" y="560" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="593">Try it carefully.</text><text class="branch" x="210" y="632">no</text><path class="edge" d="M 200 616 L 200 660" marker-end="url(#arrowhead)"/><rect class="final" x="40" y="660" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="693">Read a scroll of identify.</text></svg><figcaption style="font-style: italic; color: #5a5a5a; font-size: 0.9em; margin-top: 0.5em;">The identification flowchart: cheapest method first, scroll of identify last.</figcaption></figure></div>

:::
<!-- FLOWCHART-END -->

#### Blessed, Uncursed, Cursed (BUC)
<!-- audit
2026-05-18:
- altar flash on drop: amber blessed, black cursed, no flash uncursed (do.c:379-388)
- pet steps around cursed items (dogmove.c:535-538); starvation exception
- cursed gain-level rockets you through the ceiling (potion.c:1083-1109)
- cursed or confused scroll of teleportation is a LEVEL teleport (read.c:2015-2025)
- holy water made by praying on a co-aligned altar with potions of water (pray.c:2336-2339)
- Priest senses BUC naturally (invent.c:2763, 3545)
- blessed scroll of identify: at least 2 items, plus 1-in-5 chance for the whole pack (read.c:2086-2092)
- cursed scroll of identify IDs only itself on first cursed read (read.c:2074-2081)
- strategy aligned with NetHackWiki Identification, Curse-testing, BUC: altar > pet > shop-price > engrave/sink > use-test > scroll-of-identify ordering matches canonical advice (https://nethackwiki.com/wiki/Identification, https://nethackwiki.com/wiki/Curse-testing, https://nethackwiki.com/wiki/BUC)
-->

Before you can worry about *what* an item is, you need to know
*what condition* it's in. Every item in the Mazes is blessed, uncursed,
or cursed (BUC for short), and the difference matters far more than
you'd think. The gods have opinions about your equipment, and those
opinions have consequences:

- A **blessed** scroll of identify reveals at least 2 items in your
  pack (more with positive Luck), and one time in five reveals the
  whole pack. An *uncursed* scroll IDs one or two items; a *cursed*
  scroll IDs only the scroll itself the first time you read one of
  that type, and one item per subsequent cursed read.
- A **cursed** piece of armor bonds to your skin like it has
  abandonment issues. You cannot remove it until you lift the curse.
- A **cursed** potion of gain level interprets "gain a level" in the
  most literal architectural sense: you rocket through the ceiling
  to the floor above, instead of gaining an experience level.

Blessed items are helpful beyond their description, uncursed
items work as advertised, and cursed items find creative ways to
ruin your day. A blessed luckstone passively
improves your luck; a cursed one drags it down. A cursed scroll of
teleportation sends you to a random *level* instead of teleporting
within the current one. You get the idea.

You don't see BUC status by default (Priests are the exception: they
sense it naturally, which tells you something about clerical
paranoia). But there are several reliable ways to check:

**Altar testing.** Drop an item on an altar:

  - An amber flash means blessed.
  - A black flash means cursed.
  - No flash means uncursed.

This is free, fast, and unlimited. If you find an altar early,
use it heavily.

**Pet testing.** Your pet won't step on cursed items. If you drop
something and your dog walks around it, it's cursed. If the dog walks
over it (or picks it up), it's safe. Not as precise as an altar, but
works anywhere. Two ways the test can lie: a hungry pet will march
straight over a cursed pile if there's food in the same stack, and
items that *autocurse on wear* (helm of opposite alignment,
gauntlets of fumbling, dunce cap, levitation boots) read as
uncursed on both pet and altar tests, then curse themselves the
instant you put them on.

**Holy water.** Dipping an item in blessed water (holy water) will
uncurse a cursed item or bless an uncursed one. Dipping in cursed
water (unholy water) curses an uncursed item or unblesses a
blessed one. You make holy water by praying on a co-aligned altar
while carrying potions of water; it's precious in the early game,
so save it for items you've already identified.

**Scroll of identify.** A blessed scroll identifies at least 2
items in your pack, more with positive Luck, with a 1-in-5 chance
to ID the whole pack outright. An uncursed scroll IDs one or two
items per read. A cursed scroll IDs only itself the first time you
read one of that type, then one item per cursed read after. Pick
every unidentified item into your inventory before reading a
blessed scroll: the jackpot reads everything in your pack.

#### The Price Is Right
<!-- audit
2026-05-18:
- buy/sell multipliers and Cha bands match shk.c get_cost/set_cost
- sell offer is 1/2 base (shk.c:3160); 3/8 on unID items from an unfamiliar shopkeeper (shk.c:3173-3174)
- Tourist surcharge (+33%) applies with dunce cap, Tourist below XL 15, or visible Hawaiian shirt — non-stacking
- ~1/4 of unID items carry a fixed 4/3 buy surcharge per item
- ~1/4 of shopkeepers are "unfamiliar" with unID; they offer 3/4 sell, fixed per shop
- angry-shop +33% surcharge sticks: pacify_shk(FALSE) at shk.c:2663 does NOT clear it
- only pacify_shk(TRUE) clears (shk.c:302, 793 — bones-load and new-customer transitions)
- the JS price widget mirrors get_cost/set_cost exactly
- AMULET macro hard-codes base price 150 for every magic amulet; FAKE_AMULET_OF_YENDOR is base 0 (objects.h:831-834, 865-869)
-->

Shopkeepers are, without exaggeration, your most important
identification tool. Every unidentified item has a fixed base price
that depends on what it actually is. When you pick up an item in a
shop, the shopkeeper quotes you a price derived from that base price,
modified by your Charisma and the shopkeeper's markup.

Two ways to get a quote without committing to the buy: **throw**
the item into the shop from outside (you forfeit ownership but the
shopkeeper still quotes the buy price as they pick it up), or
**`#chat`** with the shopkeeper while standing on the item to hear
the same quote. The chat trick is the polite way to price-ID a
heavy item, or to price-test under teleportitis.

A note on the markup: three things give you "sucker" sell prices
(1/3 base instead of 1/2). Wearing a *dunce cap*, being a *Tourist
under XL 15*, or letting a *T-shirt or Hawaiian shirt show* (no
body armor and no cloak) all flip the divisor. Cover the shirt
before you sell, and don't browse in your cone hat. Charisma
doesn't touch sell prices at all; the Charisma bands in the table
above only move *buy* prices.

> *Shopkeeper pricing was first documented in detail by Gregory
> Bond's Shopping Spoiler, HTML-formatted by Kate Nepveu and
> hosted on steelypips.org. David Damerell's Object Identification
> Spoiler expanded the price-based identification techniques. The
> mechanics below draw from both.*

The key insight: items in the same category that share a base price
are in the same **price group**. If you know the price, you can
narrow down the possibilities enormously, sometimes to just two or
three candidates.

Pick up an item and note the quoted price. With average Charisma
(11-15), buy price equals base and sell is half base. Low Charisma
pushes buy up (×2 at Cha ≤ 5); high Charisma pulls it down (×½ at
Cha ≥ 19). Sell prices don't change with Charisma, but if
shopkeepers see you as a **mark**, then you can only sell at a
third of base, and you'll have to pay 4/3 to buy. Three visible
cues count you as a mark: wearing a **dunce cap**, playing a
**Tourist** below XL 15, or wearing a **Hawaiian shirt visibly**
(no body armor or cloak over it). The rest of this guide refers to
them collectively as *Tourist*. You don't need to memorize the
formulas; what matters is grouping by price tier.

Two further wrinkles affect unidentified items. About a quarter of
unID'd items carry an extra 4/3 buy surcharge, fixed per item, so a
given scroll's surcharge status is consistent across shops. And
about a quarter of shopkeepers are "unfamiliar" with unID'd
merchandise and offer only 3/4 of normal on sell, fixed per
shopkeeper, so once you've tested one unID item you know the rule
for all unID sales at that shop. Either wrinkle can shift a quoted
price into an adjacent tier, so when in doubt check the surrounding
tiers too.

**Angry.** A shopkeeper you've previously angered (fired a wand from a doorway,
attacked them, picked up an unpaid item while broke) and then made
amends (paid the bill, fled and let them calm down) becomes peaceful
again but keeps a permanent +33% buy surcharge on every item. Paying
the bill clears the bill but not the surcharge; that flag sticks for
the rest of your visits to that shopkeeper. Sell prices are
unaffected.

The price tables for each item class follow. These are your
field reference for shopping trips.

::: print-only

```{=latex}
\clearpage
\thispagestyle{plain}
\vspace*{\fill}
\begin{center}
\includegraphics[width=0.92\linewidth]{cover/build/flowchart.pdf}\\[0.6em]
{\itshape\footnotesize The identification flowchart: cheapest method first, scroll of identify last.}
\end{center}
\vspace*{\fill}
\clearpage
```

##### Quoted-price conversion

Each row shows the price you'd transact for the listed base prices.

**Buy rows** are the Charisma bands (the price you'd be *quoted*
to buy). A bare band (like *11–15*) is the baseline; *11–15^T^*
is Cha 11–15 with one ×4/3 surcharge applied; *11–15^T2^* is two
surcharges stacked. Surcharges come from three sources: a Tourist
markup (low-XL Tourist, dunce cap, or visible undershirt), an
angry shopkeeper, or the random unidentified-item surcharge that
fires on about 1 item in 4 (deterministic per object — two of the
same appearance disagreeing is the giveaway).

**Sell rows** at the bottom show what an unangry shopkeeper
*offers* for a sale. Sell prices ignore Charisma. *S* is the
baseline ½ of base. *S^T^* is the same sucker condition (dunce
cap, low-XL Tourist, visible undershirt) — on the sell side it
cuts your offer to ⅓ instead of ½. *S^P^* is a pennypinching
shopkeeper (1 in 4) who shaves ¼ off unidentified items;
unlike the buy-side unid surcharge, this is per-shopkeeper, not
per-item — the same pennypinching shop applies it to every
unidentified item you bring in. *S^TP^* stacks both.

| Charisma / Markups               |   Mult |  20 |  50 |  60 |  80 | 100 | 150 | 175 | 200 | 300 |  500 |
|----------------------------------|:-------|----:|----:|----:|----:|----:|----:|----:|----:|----:|-----:|
| 6–7^T2^                          |  ×2.67 |  53 | 133 | 160 | 213 | 267 | 400 | 467 | 533 | 800 | 1333 |
| 8–10^T2^                         |  ×2.37 |  47 | 119 | 142 | 190 | 237 | 356 | 415 | 474 | 711 | 1185 |
| 6–7^T^                           |  ×2.0  |  40 | 100 | 120 | 160 | 200 | 300 | 350 | 400 | 600 | 1000 |
| 8–10^T^, 11–15^T2^               |  ×1.78 |  36 |  89 | 107 | 142 | 178 | 267 | 311 | 356 | 533 |  889 |
| 6–7                              |  ×1.5  |  30 |  75 |  90 | 120 | 150 | 225 | 263 | 300 | 450 |  750 |
| 8–10, 11–15^T^, 16–17^T2^        |  ×1.33 |  27 |  67 |  80 | 107 | 133 | 200 | 233 | 267 | 400 |  667 |
| 18^T2^                           |  ×1.19 |  24 |  59 |  71 |  95 | 119 | 178 | 207 | 237 | 356 |  593 |
| 11–15, 16–17^T^                  |  ×1.00 |  20 |  50 |  60 |  80 | 100 | 150 | 175 | 200 | 300 |  500 |
| 18^T^, 19+^T2^                   |  ×0.89 |  18 |  44 |  53 |  71 |  89 | 133 | 156 | 178 | 267 |  444 |
| 16–17                            |  ×0.75 |  15 |  38 |  45 |  60 |  75 | 113 | 131 | 150 | 225 |  375 |
| 18, 19+^T^                       |  ×0.67 |  13 |  33 |  40 |  53 |  67 | 100 | 117 | 133 | 200 |  333 |
| 19+, S                           |  ×0.5  |  10 |  25 |  30 |  40 |  50 |  75 |  88 | 100 | 150 |  250 |
| S^P^                             |  ×0.375 |   8 |  19 |  23 |  30 |  38 |  56 |  66 |  75 | 113 |  188 |
| S^T^                             |  ×0.333 |   7 |  17 |  20 |  27 |  33 |  50 |  58 |  67 | 100 |  167 |
| S^TP^                            |  ×0.25 |   5 |  13 |  15 |  20 |  25 |  38 |  44 |  50 |  75 |  125 |

:::

##### Scroll Prices

| Price | Scrolls                                                                                                           |
| ----- | ----------------------------------------------------------------------------------------------------------------- |
|    20 | identify                                                                                                          |
|    50 | light                                                                                                             |
|    60 | blank paper, enchant weapon                                                                                       |
|    80 | enchant armor, remove curse                                                                                       |
|   100 | confuse monster, destroy armor, fire, food detection, gold detection, magic mapping, scare monster, teleportation |
|   200 | amnesia, create monster, earth, taming                                                                            |
|   300 | charging, genocide, punishment, stinking cloud                                                                    |

<div class="price-id-toolbar"></div>

The $100 group is crowded, which makes scroll price-ID less precise
than other categories. But you can still narrow things down. If a
scroll is in the $20 group, it's identify. Period. That's one of the
most useful scrolls in the game and you just found it for free.

```{=latex}
\needspace{6\baselineskip}
```

A closet tip: a *single* unidentified scroll alone in a
one-square closet, behind a door or in a niche, is almost always
scroll of teleportation. The dungeon generator hides it there as
the level's teleport-trap clue. If you find that closet, you've
probably found a free $100 ID.

##### Spellbook Prices

Spellbooks price at 100 × the spell's level, which makes reading
risk easy to gauge: a $700 book is level 7 and will probably
explode in the hands of anyone who isn't a careful Wizard.

<div class="price-id-toolbar"></div>

| Price | Level | Spellbooks                                                                                                                  |
| ----- | ----- | --------------------------------------------------------------------------------------------------------------------------- |
|   100 | 1     | confuse monster, detect monsters, flame sphere, force bolt, freeze sphere, healing, jumping, knock, light, protection      |
|   200 | 2     | chain lightning, create monster, cure blindness, detect food, drain life, magic missile, slow monster, wizard lock          |
|   300 | 3     | cause fear, clairvoyance, cure sickness, detect unseen, extra healing, haste self, identify, remove curse, sleep, stone to flesh |
|   400 | 4     | cone of cold, detect treasure, fireball, invisibility, levitation, restore ability                                          |
|   500 | 5     | charm monster, dig, magic mapping                                                                                           |
|   600 | 6     | create familiar, polymorph, teleport away, turn undead                                                                      |
|   700 | 7     | cancellation, finger of death                                                                                               |

<div class="price-id-toolbar"></div>

##### Potion Prices

| Price | Potions                                                                     |
| ----- | --------------------------------------------------------------------------- |
|    20 | healing                                                                     |
|    50 | booze, fruit juice, see invisible, sickness                                 |
|   100 | confusion, extra healing, hallucination, restore ability, sleeping, water   |
|   150 | blindness, gain energy, invisibility, monster detection, object detection   |
|   200 | enlightenment, full healing, levitation, polymorph, speed                   |
|   250 | acid, oil                                                                   |
|   300 | gain ability, gain level, paralysis                                         |

<div class="price-id-toolbar"></div>

Healing sits alone at $20, uniquely identifiable from the price tag.
Water is always the "clear" potion, so if you see "clear potion" you
know what it is without even checking the price. The $50 group is
tricky because sickness and see invisible are in there together (one
very good, one very bad). The $200 group is packed with excellent
potions.

##### Ring Prices

| Price | Rings                                                                                                                                                                      |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   100 | adornment, hunger, protection, protection from shape changers, stealth, sustain ability, warning                                                                           |
|   150 | aggravate monster, cold resistance, gain constitution, gain strength, increase accuracy, increase damage, invisibility, poison resistance, see invisible, shock resistance |
|   200 | fire resistance, free action, levitation, regeneration, searching, slow digestion, teleportation                                                                           |
|   300 | conflict, polymorph, polymorph control, teleport control                                                                                                                   |

<div class="price-id-toolbar"></div>

The $300 group is extremely informative: only four rings live there,
and three of them (conflict, polymorph control, teleport control) are
among the most powerful in the game.

##### Wand Prices

| Price | Wands                                                                                                                                                          |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   100 | light, nothing                                                                                                                                                 |
|   150 | digging, enlightenment, locking, magic missile, make invisible, opening, probing, secret door detection, slow monster, speed monster, stasis, striking, undead turning |
|   175 | cold, fire, lightning, sleep                                                                                                                                   |
|   200 | cancellation, create monster, polymorph, teleportation                                                                                                         |
|   500 | death, wishing                                                                                                                                                 |

<div class="price-id-toolbar"></div>

If a wand costs $500, you are having a very good day.

##### Amulet Prices

All amulets have a base price of $150 except the cheap Amulet of
Yendor imitations ($0). Price won't ID them; you'll need other methods.

<script>
document.addEventListener('DOMContentLoaded', function() {
  var toolbars = document.querySelectorAll('.price-id-toolbar');
  if (!toolbars.length) return;
  var CHA_BUY = {
    'lt5':    [2, 1],
    '6to7':   [3, 2],
    '8to10':  [4, 3],
    '11to15': [1, 1],
    '16to17': [3, 4],
    '18':     [2, 3],
    'ge19':   [1, 2]
  };
  var state = {cha: '11to15', sell: false, touristy: false, angry: false};

  // Populate each toolbar with the same compact button set.
  // Cha bracket on the left, then independent toggles: Sell, Tourist, Dunce.
  var btnHTML =
    '<span class="price-id-label">Cha</span>' +
    '<button data-group="cha" data-val="lt5">≤5</button>' +
    '<button data-group="cha" data-val="6to7">6-7</button>' +
    '<button data-group="cha" data-val="8to10">8-10</button>' +
    '<button data-group="cha" data-val="11to15">11-15</button>' +
    '<button data-group="cha" data-val="16to17">16-17</button>' +
    '<button data-group="cha" data-val="18">18</button>' +
    '<button data-group="cha" data-val="ge19">≥19</button>' +
    '<span class="price-id-sep">·</span>' +
    '<button data-group="toggle" data-val="sell">Sell</button>' +
    '<button data-group="toggle" data-val="touristy">Tourist</button>' +
    '<button data-group="toggle" data-val="angry">Angry</button>';
  toolbars.forEach(function(tb) {
    tb.innerHTML = btnHTML;
    tb.classList.add('price-id-widget');
  });

  function adj(base, m, d) {
    var n = base * m;
    if (d > 1) n = Math.floor((n * 10 / d + 5) / 10);
    return Math.max(1, n);
  }
  function computeBuy(base, surcharge) {
    // Replicates shk.c get_cost. Default Cha 11-15 no penalty: buy = base.
    var m = 1, d = 1;
    var cha = CHA_BUY[state.cha];
    m *= cha[0]; d *= cha[1];
    if (state.touristy) { m *= 4; d *= 3; }
    if (surcharge) { m *= 4; d *= 3; }
    var n = adj(base, m, d);
    // Angry-shopkeeper surcharge: added AFTER mult/div in shk.c:2986
    // (tmp + (tmp + 2) / 3, ~+33%). Stacks with Tourist. Buy-side only.
    if (state.angry) n = n + Math.floor((n + 2) / 3);
    return n;
  }
  function computeSell(base, unfamiliar) {
    // Replicates shk.c set_cost. Default no penalty: sell = base / 2.
    var m = 1, d = 1;
    if (state.touristy) d *= 3; else d *= 2;
    if (unfamiliar) { m *= 3; d *= 4; }
    return adj(base, m, d);
  }
  function pair(n1, n2) {
    return n1 === n2
      ? '' + n1
      : n1 + '<span class="pi-alt"> / ' + n2 + '</span>';
  }

  // Find every table whose first column header is "Price". Stash the base
  // price (which is what shows initially, since default state quotes buy =
  // base) on each row's price cell. We also tolerate "Sell" as a header
  // (e.g. after a previous render).
  var priceTables = [];
  document.querySelectorAll('table').forEach(function(t) {
    var hdrs = t.querySelectorAll('thead th');
    if (!hdrs.length) return;
    if (!/^(Price|Sell)$/i.test(hdrs[0].textContent.trim())) return;
    hdrs[0].classList.add('pi-col');
    t.querySelectorAll('tbody tr').forEach(function(tr) {
      var firstTd = tr.querySelector('td');
      if (!firstTd) return;
      var m = firstTd.textContent.trim().match(/^\$?(\d+)/);
      if (!m) return;
      if (!firstTd.dataset.basePrice) firstTd.dataset.basePrice = m[1];
      firstTd.classList.add('pi-price', 'pi-col');
    });
    priceTables.push(t);
  });

  function renderTables() {
    priceTables.forEach(function(t) {
      var hdr = t.querySelector('thead th.pi-col');
      if (hdr) hdr.textContent = state.sell ? 'Sell' : 'Price';
      t.querySelectorAll('td.pi-price').forEach(function(td) {
        var base = parseInt(td.dataset.basePrice, 10);
        if (state.sell) {
          td.innerHTML = pair(computeSell(base, false), computeSell(base, true));
        } else {
          td.innerHTML = pair(computeBuy(base, false), computeBuy(base, true));
        }
      });
    });
  }

  function syncToolbars() {
    toolbars.forEach(function(tb) {
      tb.querySelectorAll('button[data-group="cha"]').forEach(function(b) {
        b.classList.toggle('active', b.dataset.val === state.cha);
      });
      tb.querySelectorAll('button[data-group="toggle"]').forEach(function(b) {
        b.classList.toggle('active', !!state[b.dataset.val]);
      });
    });
  }

  toolbars.forEach(function(tb) {
    tb.addEventListener('click', function(ev) {
      var btn = ev.target.closest('button');
      if (!btn) return;
      var g = btn.dataset.group, v = btn.dataset.val;
      if (g === 'cha') state.cha = v;
      else state[v] = !state[v];
      syncToolbars();
      renderTables();
    });
  });

  syncToolbars();
  renderTables();
});
</script>

#### The Engrave Test (Wands)

The single most useful wand-identification trick costs only one
charge and preserves the rest.

1. **BUC-test the wand first.** A cursed wand used to engrave may
   **explode**. Drop the wand on an aligned altar, hand
   it to a priest, or otherwise determine its BUC before testing.
2. **Write a short message on the floor with your finger.** Engrave
   anything in the dust first (command `E`, then select "`-`" for
   fingers, then type a word or two). This matters because a few
   wands act on the *existing* engraving rather than producing a
   visible effect on bare floor: polymorph rewrites the message as a
   random new one, and cancellation, make-invisible, and
   teleportation each make it "vanish". Without a pre-written
   message you won't see those behaviors.
3. **Engrave again with the wand.** Use `E` and select the wand.
   Observe the result. The [Wand Table](#the-wand-table) lists the
   engrave-test result for each wand; most wands reveal themselves
   here. A few share results — see [Resolving Ambiguous Engrave
   Results](#resolving-ambiguous-engrave-results).

**Don't be afraid of the suspected wand of wishing.** Engraving with
it grants the wish: if a $500 candidate prompts you with *"For what
do you wish?"*, take the wish — that's the identification and the
reward in one step.

> *Procedure adapted from Kieron Dunbar's "Identifying Wands by
> Zapping" spoiler, originally posted to RGRN.*

<!-- audit
2026-05-18:
- dosinkring at do.c:498-650 — 28 ring types each give a distinctive message
- searching and slow digestion goto giveback, dropped back on the floor identified (do.c:507-516)
- other rings usually consumed: 1/20 backup chance, 1/5 buried chance (do.c:649-660)
-->
#### The Sink Test (Rings)

If you find a sink, you can drop a ring down it. Each ring type
produces a characteristic message, identifying the ring. See
[Sinks](#sinks) under Points of Interest for the full
message-to-ring table; the short version is that searching and
slow digestion come back to you (free identification), and every
other ring is consumed.

#### Use-Testing (The Careful Way)
<!-- audit
2026-05-18:
- engrave-test messages: fire "Flames fly", cold "A few ice cubes drop", lightning "Lightning arcs", digging "Gravel flies up", magic missile "riddled by bullet holes" (engrave.c, zap.c)
- polymorph randomizes existing engraving, not "vanishes" (engrave.c:618-633 WAN_POLYMORPH case calls random_engraving on existing engraving)
- cancellation, make-invisible, teleportation all share the "vanishes" message
- wand of wishing engrave DOES grant the wish (zap.c:2575-2585)
- unicorn horn dipped in sickness → fruit juice; in confusion/hallucination/blindness → water (potion.c:2151-2159)
- is_poisonable requires oc_skill in [-P_SHURIKEN, -P_BOW] (obj.h:264-268) — ranged ammo only
- daggers (skill +1) and spears (skill +17) are NOT poisonable
- confused remove curse via blessorcurse(obj, 2): 1/4 bless, 1/4 curse, 1/2 unchanged (mkobj.c:1841-1853)
- non-blessed confused remove curse touches only worn/wielded (read.c:1549-1552); blessed touches all
- 90% auto-curse branch (mkobj.c:1087-1090) covers fumble boots, levitation boots, gauntlets of fumbling, helm of opposite alignment
- cursed worn armor refuses to be taken off via the otmp->cursed check (do_wear.c:1900); cursed loadstone refuses to drop (do.c:685-695)
-->

When you don't have access to a shop or a sink, you can sometimes
figure out what an item is by using it carefully. Here's the approach
for each category:

**Potions.** The safest test is to throw a potion at a monster and
observe the effect. Throwing avoids the risk of drinking something
lethal. If a potion heals the monster, it's some kind of healing
potion. If the monster speeds up, it's speed. If the monster becomes
invisible, well, you've learned something (and now have an invisible
monster to deal with).

You can also dip items into potions. Dipping a stack of poisonable
ammunition (arrows, crossbow bolts, darts, shuriken, or sling stones)
into a potion of sickness will poison it, confirming the potion's
identity (it won't poison a sword or any non-missile weapon).
Dipping a unicorn horn into a potion of **confusion**,
**hallucination**, or **blindness** turns it into water; dipping
into a potion of **sickness** turns it into fruit juice.

**Testing a $200 potion.** The $200 group (enlightenment, full
healing, levitation, polymorph, speed) has the best payouts but
two hidden traps. Quaff levitation and you're stuck off the
floor for a few hundred turns. Quaff polymorph and you may turn
into a form that destroys or sheds your body armor. Strip down
to a shirt before you test, and quaff somewhere nothing is
hunting you.

**Scrolls.** Reading is risky. Some scrolls (destroy armor, amnesia,
punishment) are outright harmful. The safest approach is to price-ID
first, then read scrolls from safe price groups. If you must test
blind: take off your armor before reading a scroll that might be
destroy armor. Read from a position where teleportation won't be
disastrous.

Confused reading produces different effects for many scrolls and is
sometimes useful. A confused scroll of remove curse **randomizes
the BUC of your uncursed items** (about a quarter end up blessed,
a quarter end up cursed, and half stay uncursed) and leaves
already-cursed items cursed. A non-blessed confused scroll only
touches your worn and wielded gear (plus loadstones and active
leashes); a blessed confused scroll touches your whole inventory.
So it's a way to get a few cheap blessings on worn items, not a
curse-removal tool. Don't read it confused if you need to uncurse
something.

**Rings.** First, confirm the ring is not cursed (altar or pet test).
Then put it on. Many rings produce an immediate message or visible
effect: you start levitating, you become invisible, you feel
stronger. If nothing obvious happens, check your stats and inventory
for subtle changes (protection, searching). Take it off quickly if
you feel hungry faster than normal (hunger ring) or if monsters
seem newly aggressive (aggravate monster).

**Amulets.** Most amulets are safe to wear briefly. Put it on, wait
a few turns, take it off. The dangerous ones (strangulation, restful
sleep) are usually cursed, so check BUC first. An amulet of ESP
reveals itself if you go blind while wearing it (you'll see monsters
as brain-shapes). Amulet of reflection is trickier to detect, but
you'll notice it when a ray bounces off you.

**Armor.** Magical armor reveals itself when worn: speed boots
make you faster, a cloak of invisibility makes you invisible. But
trying on unknown armor in a shop is dangerous: if it's cursed it
welds itself on, you can't drop it, and the shopkeeper still
expects payment. Worse, the auto-cursed types (fumble boots,
levitation boots, gauntlets of fumbling, helm of opposite alignment)
masquerade as the desirable ones. **Verify BUC before wearing
unknown armor in a shop.** Without an altar, your options are the
pet-step test, Priest intrinsic BUC sense, or a scroll of identify
from your own inventory.

Each type of special armor has a **randomized appearance**, so
the same "snow boots" that were safe levitation in your last game
might be jumping or fumble boots this time. The four shuffled
pools are:

- 4 magical **helms** share 4 appearances: plumed / etched /
  crested / visored helmet → one of helmet, helm of caution, helm
  of opposite alignment, helm of telepathy. (Helm of brilliance is
  always "crystal helmet"; dunce cap and cornuthaum both look like
  "conical hat"; that pair *is* a fixed pun.)
- 4 magical **cloaks** share 4 appearances: tattered cape / opera
  cloak / ornamental cope / piece of cloth → one of cloak of
  protection, invisibility, magic resistance, or displacement.
- 4 **gloves** share 4 appearances: old / padded / riding / fencing
  gloves → leather gloves or one of the three gauntlet types
  (fumbling, power, dexterity).
- 7 magical **boots** share 7 appearances: combat / jungle / hiking
  / mud / buckled / riding / snow boots → one of speed, water
  walking, jumping, elven, kicking, fumble, or levitation boots.

The good news: prices *don't* shuffle, and prices within each pool
fall into informative tiers.

##### Armor Prices

| Price | Type     | Possibilities                                                    |
| ----- | -------- | ---------------------------------------------------------------- |
|     8 | Boots    | elven (stealth), kicking                                         |
|    30 | Boots    | fumble, levitation (both commonly cursed!)                       |
|    50 | Boots    | speed, water walking, jumping (all desirable)                    |
|     8 | Gloves   | leather gloves (only)                                            |
|    50 | Gloves   | gauntlets of fumbling, power, or dexterity                       |
|    50 | Cloaks   | cloak of protection or displacement                              |
|    60 | Cloaks   | cloak of invisibility or magic resistance                        |

<div class="price-id-toolbar"></div>

A $30 boot is the warning sign: both candidates are common
auto-curse items and putting them on without BUC-checking can ruin
a run. A $50 boot is almost always one you want. A $60 cloak is one
of two excellent cloaks, but you still need BUC and a free body
before wearing. $8 boots and $50 gauntlets are the cases where you
can't tell stealth-from-kicking or fumbling-from-power by price
alone. Try them on (BUC-checked) and watch for the messages.

#### Gray Stones: Four Stones, One Correct Answer
<!-- audit
2026-05-18:
- loadstones are cursed at object creation (mkobj.c:978-979), not on pickup
- cursed-on-creation state is what blocks dropping; "auto-curse on pickup" would be a different mechanic
- prices: luckstone 60, touchstone 45, loadstone 1, flint 1 (objects.h:1598-1605)
- weights: loadstone 500, others 10 (objects.h:1598-1605)
- blessed touchstone (or Archeologist/Gnome holding uncursed) IDs gems on rub (apply.c rub_on_stone)
- Mine's End luckstone is guaranteed not-cursed (minend-1.lua:77, minend-2.lua:116, minend-3.lua:67)
-->

Gray stones deserve their own section because they look identical
but have wildly different value. There are four types:

| Price | Stone                | Effect                                     |
| ----- | -------------------- | ------------------------------------------ |
|     1 | flint **or** loadstone | flint is useless ammunition; loadstone weighs 500 units, usually cursed, and won't drop once carried. Use the kick test (loadstones don't scoot). |
|    45 | touchstone           | Identifies gems when rubbed. Very useful.  |
|    60 | luckstone            | Preserves luck. Essential.                 |

<div class="price-id-toolbar"></div>

The problem: all four look like "a gray stone" until identified.
Here's how to tell them apart:

**The kick test.** Kick an unidentified gray stone on the floor.
If it scoots away normally, it's not a loadstone. A loadstone is
abnormally heavy and resists being kicked. Take off gauntlets of
power and kicking boots first, or you may overpower a real
loadstone and fool yourself.

**The weight-menu test.** Drop any junk item onto the gray stone
to force a pickup menu the next time you walk over it. The menu
shows weight; a loadstone is 500, everything else is 10. The
menu test gives a clean read without committing to picking the
stone up.

**The pick-up test.** Loadstones are cursed when they generate,
and a cursed loadstone refuses to be dropped at all — the game
prints "For some reason, you cannot drop the stone!" and the
stone stays in your pack. If you pick up a gray
stone and it weighs you down suspiciously, try to drop it. If
you can't, you're stuck with a cursed loadstone until you can
uncurse it (holy water, scroll of remove curse, prayer) — then
drop it.

**The `#tip` escape.** Or, more elegantly: stow the cursed
loadstone in any container you carry (a 2z sack is enough), then
apply `#tip` to the container. The contents spill onto your
square, loadstone included, because `#tip` extracts items
directly and bypasses the cursed-drop check. Step off and walk
away. The trick has worked through every NetHack edition and the
5.0 source still leaves the asymmetry in place.

**The price test.** If you can reach a shop: a $60 gray stone is a
luckstone. A $45 gray stone is a touchstone. A $1 gray stone is
flint or a loadstone.

**The rub test.** Apply (`a`) a gray stone to a gem in your pack.
A touchstone produces a colored-streak message — and if the
touchstone is **blessed** (or you're an Archeologist or Gnome
holding an uncursed one), the streak also identifies the gem.
Other gray stones produce similar streak messages, so a streak
alone doesn't prove touchstone; an *identification* result does.
A cursed touchstone can shatter the gem.

**Location clue.** The luckstone at Mine's End is guaranteed. If
you find a gray stone at the bottom of the Mines, it's almost
certainly the luckstone. Bless-test it at an altar to confirm
(the guaranteed one is always uncursed).

The rule of thumb: if you find a gray stone, don't pick it up
until you've tested it. A loadstone can ruin your encumbrance, and
if it's cursed, you're stuck with it until you find a way to
uncurse. Kick it first. Check BUC second. Then pick it up.

#### Naming What You've Learned
<!-- audit
2026-05-21:
- mergable() requires identical otyp, enchantment (spe), BUC, erodeproof state, erosion (oeroded, oeroded2), greased state, oeaten/orotten for food; coins merge unconditionally (invent.c:4379-4460)
- on merge that propagates a previously-unknown property, the game prints "You learn more about your items by comparing them." (invent.c:938-942); guarded against LOST_THROWN to avoid spam when monsters strip ID
2026-05-18:
- `#name` and `#call` aliases at cmd.c:1773-1774
- class naming at do_name.c:571-588
- rename-by-overwrite at do_name.c:660-672
- N keystroke only works in number_pad mode; default vi-keys binds N to run-north — cross-layout shortcut is C for #call
-->

As you gather clues, use the `#name` command to track what you
know. You can **call** an entire item class by a name you choose.
For example, if you've determined that "fizzy potions" are in the $200
price group, call them "fizzy=$200" so you don't forget. If you later
throw one at a monster and it speeds up, you can rename the class to
"speed."

This habit of annotating your discoveries is what separates adventurers
who die on level 8 from adventurers who reach the Castle. The dungeon
doesn't keep notes for you. You have to do it yourself.

**Identification by stacking.** When you pick up an item, the game
merges it into an existing slot only if the two are *identical*:
same type, same enchantment, same BUC, same erodeproofing. So
whether a new item stacks with one you already understand leaks
information for free. When a merge actually teaches you something
the game says so explicitly: *"You learn more about your items by
comparing them."* That message is your cue that the merge
propagated a known property (BUC, enchantment, erosion) to the
previously unknown side. Two same-appearance items that *don't*
merge are a different potion, a different BUC, or one side has
been diluted or eroded.

#### A Practical Strategy
<!-- audit
2026-05-18:
- altar-flash BUC at do.c:379-389
- engrave-test costs one charge (engrave.c:792, zap.c:2520)
- wand of digging auto-IDs from engrave message (engrave.c:684-704)
- all 12 amulet appearances are priced at 150 gp (objects.h:834)
- WAN_COLD fresh-floor engrave message: "A few ice cubes drop from the wand" (engrave.c:658-661)
- the vanish/freeze branch only triggers when overwriting an existing BURN engraving
-->


All of these techniques combine into a workflow. Here's what a
seasoned traveler does on a typical descent:

**At an altar** (priority one). Ferry everything you've found to the
altar. Drop each item. Sort your pack into blessed, uncursed, and
cursed piles. Wield or wear the blessed stuff. Stash or discard the
cursed stuff.

**At a shop** (priority two). Pick up and put down unidentified items
to get price quotes. Group them by price. Cross-reference with the
tables above. Suddenly half your inventory is narrowed to two or three
possibilities.

**Engrave-test your wands** as soon as you find them. It's fast, it
costs only one charge, and it immediately sorts wands into categories.
A wand that digs the floor is digging. A wand that drops ice cubes
is cold. Simple.

**Experiment cautiously** with the rest. Wear non-cursed rings one at
a time. Throw potions at monsters. Read scrolls from safe price groups
after removing your armor.

**Save your scrolls of identify** for the items that resist other
methods, in roughly this order: **spellbooks first** (reading an
unknown high-level book is the most lethal mistake on the
identification table), **amulets** next (all the same price), then
the resistance/utility rings in the $200 group, then any wands
that engrave-tested ambiguously.

The system is about reducing uncertainty with the cheapest, safest
method first: altars and shops are free, engrave-testing costs one
charge, use-testing costs more and carries risk, and scrolls of
identify are the precious last resort.

---

### Provisions and Dining
<!-- audit
2026-05-21:
- vegan classes: S_BLOB, S_JELLY, S_FUNGUS, S_VORTEX, S_LIGHT, S_ELEMENTAL (except stalker), S_GOLEM (except flesh/leather), and noncorporeal (S_GHOST) (mondata.h:232-238)
- vegetarian = vegan + S_PUDDING except black pudding (mondata.h:239-241); brown pudding and gray ooze are vegetarian, black pudding is not
- corpse_intrinsic picks one mconveys property uniformly at random per eat, then should_givit rolls mlevel/15 (or mlevel-vs-rn2(15)); killer bee/scorpion poison-res has a 25% boosted-chance branch (eat.c:961-989, 1351-1373)
2026-05-20:
- tin opening is an occupation; opentin is called per turn, gives up after svc.context.tin.usedtime >= 50 turns (eat.c:1710-1719, 1794)
- tin open time by tool: blessed tin opener wielded = 0; uncursed tin opener rn2(2); cursed rn2(3); dagger family = 3; axe/pick-axe = 6; bare hands = rn1(1 + 500/(Dex+Str), 10) which is ~11-26 at avg stats, up to the 50-turn cap (eat.c:1740-1786)
- tin of spinach grants +1 Str on eat (eat.c spinach branch)
2026-05-18:
- gelatinous cube corpse: fire/cold/shock/sleep only (not poison/acid/stoning) (monsters.h:160-162 mresists has MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP|MR_POISON|MR_ACID|MR_STONE but mconveys row is MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP only)
- disenchanter corpse STRIPS an intrinsic, doesn't grant one (eat.c:1270-1275 PM_DISENCHANTER calls attrcurse)
- encumbrance kicks in at Stressed, not Burdened (eat.c:3197 near_capacity > SLT_ENCUMBER)
- fire giant corpse grants Str on eat via is_giant(ptr) (eat.c:1345-1352); separate row from fire ant
- red and brown mold corpses also grant poison resistance (monsters.h:1627-1659, MR_POISON defense)
- eggs count as vegetarian but not vegan (eat.c:585-597 violated_vegetarian and EGG handling)
- Weak status is -1 Str ATEMP, not slowed movement (attrib.c:471, eat.c:3455)
- blessed tin opens instantly only with a blessed tin opener (eat.c:1740-1745)
- ordinary tin opener on a blessed tin: 50/50 instant vs one turn via rn2(2)
- globs lose 1 weight per ~25 turns; a weight-20 glob lasts ~500 turns (mkobj.c:1487-1490)
- corpses stay safe to eat for ~30-50 turns before rotting (eat.c:1887-1939)
- strategy aligned with NetHackWiki Resistance, Poison resistance, Partial intrinsic: corpse-eating to bank resistances is canonical, gelatinous cube and dragon corpses are the highest-density sources (https://nethackwiki.com/wiki/Resistance, https://nethackwiki.com/wiki/Poison_resistance, https://nethackwiki.com/wiki/Partial_intrinsic)
- sprig of wolfsbane cures lycanthropy on eat via you_unwere (eat.c:2513-2516)
-->

Of all the things that kill adventurers in the Mazes of Menace (the
dragons, the liches, the cockatrices, the inexplicable decision to
kick a sink), none is quite as embarrassing as starving to death
while carrying forty thousand gold pieces. Hunger is the dungeon's
most persistent clock: every turn you spend costs nutrition, and
when the tank hits empty, you faint. Faint a few times without
eating and you die. It is, in the grand tradition of roguelikes,
completely your fault.

#### How Hunger Works

Your nutrition starts at 900 and ticks down steadily. The rate
depends on what you're doing:

- **Base consumption** costs 1 point per turn (less while sleeping).
- **Regeneration** (from a ring or intrinsic) costs extra on odd turns.
- **Encumbrance** costs extra on odd turns if you're **stressed** or worse (burdened alone is free).
- **Rings** cause additional hunger while worn. Two rings drain faster.

When nutrition drops below certain thresholds, you get warnings:

| Nutrition  | Status    | Effect                                    |
| ---------- | --------- | ----------------------------------------- |
| above 1000 | Satiated  | Overfull. Eating more risks choking.      |
| 151–1000   | Normal    | Fine.                                     |
| 51–150     | Hungry    | Warning message. Time to eat.             |
| 1–50       | Weak      | Strength penalty (-1 Str). Pray if possible. |
| 0 or below | Fainting  | Collapse randomly. Eat NOW or die.        |

Eat when you get the "Hungry" message; don't wait for "Weak." If
you hit Fainting and have no food, pray to your god (see
[Divine Relations](#divine-relations)); a willing god cures hunger.

#### What to Eat

**Eat the things you kill.** The single most important food fact
for new players: unless you're playing a vegetarian role (Monk,
or any role pursuing a vegan/vegetarian conduct), the bulk of
your nutrition comes from **monster corpses you leave on the
floor**. Every fresh kill is a meal. Don't burn food rations
while there's a freshly dead rat at your feet. A few rules:

- Eat corpses within 30 to 50 turns of the kill. Past that they risk
  being tainted, which means food poisoning (lethal without treatment).
- Never eat old corpses. If in doubt, don't eat it.
- Some corpses grant intrinsic resistances (poison resistance from
  killer bees, fire resistance from fire giants, etc.). Eat these
  deliberately, even when you're not hungry — see the table below.
- Some corpses are harmful (cockatrice corpses petrify you, green
  slimes turn you into slime, kobold meat is poisonous). Know which
  corpses are safe before eating.

**Food rations** are the emergency backup. 800 nutrition, weight
20, common in shops. Carry two or three for the times you don't
have a fresh kill in front of you. You don't need to hoard them.

**Lembas wafers** are the gold standard: 800 nutrition at only 5
weight, the best ratio in the game. Elven characters find these
more often.

**Tripe rations** are terrible for you (your character retches) but
pets love them. Save tripe for your pet.

**Tins** are preserved food that never spoils, but they are also
a *trap if you're sloppy about where you open them*. Opening a
tin is an occupation: you cannot act while you work, and a
monster can wander up and attack you mid-open. A tin opener
finishes in zero or one turn, a dagger in three, an axe in six,
and bare hands in as many as fifty turns of helpless effort.
Don't pop a tin in a corridor next to a sleeping room. Blessed
tins are the one exception: they open in zero or one turn no
matter the tool (instantly with a blessed tin opener). A tin of
spinach increases your Strength.

**Vegetarian characters** have to live on rations, lembas, fruits,
and the small set of non-meat corpses (fungi, molds, lichens,
jellies, plus eggs). **Vegans** lose the eggs, so they're stricter still: rations,
lembas, fruits, and plant corpses only. Plan ahead — the corpse-pile
strategy doesn't work for either, so rations and fruit are the
budget items to hoard.

#### Dangerous Foods

**Cockatrice corpse:** instant death by stoning. Never eat this.

**Acidic corpses** (acid blob, etc.): damage unless acid resistant.

**Poisonous corpses:** damage and stat drain unless poison resistant.

**Rotten corpses:** food poisoning. Pray immediately if affected.

**Cannibalism** (eating your own race): costs 2 to 5 luck and
gives the aggravate monster intrinsic. Cavemen and orcs are exempt.

#### Useful Corpse Effects

Eating for intrinsics is the highest-leverage habit in the early
and mid game. Each resistance is a *chance* per eat, not a
guarantee, so eat *every* one of these you find, not just the
first. Two tables follow: meat corpses and vegetarian-safe
corpses, each ordered roughly by when you'll first meet the
creature on a typical descent.

**Meat corpses:**

| Corpse                  | Effect                                                                 |
| ----------------------- | ---------------------------------------------------------------------- |
| Newt                    | May restore 1 to 3 mana                                                |
| Cave spider, centipede, killer bee | Poison resistance                                           |
| Lizard                  | Cures stoning in progress                                              |
| Floating eye            | **Telepathy.** (Great to eat.)                                         |
| Fire ant                | Fire resistance                                                        |
| [Wraith](#a-note-on-wraiths) | **Gain an experience level**                                      |
| Yeti                    | Cold resistance                                                        |
| Tengu                   | Teleportitis / teleport control                                        |
| Giant (any)             | Increase strength                                                      |
| Winter wolf             | Cold resistance                                                        |
| Stalker                 | Invisibility (and see invisible)                                       |
| [Black pudding](#a-note-on-puddings) (glob) | Cold, shock, and poison resistance                       |
| Fire giant              | Fire resistance + Strength                                             |
| Disenchanter            | **STRIPS** a random intrinsic. Never eat.                              |

[]{#vegetarian-safe-corpses}
**Vegetarian-safe corpses** (those marked **†** are also vegan):

| Corpse                  | Effect                                                                 |
| ----------------------- | ---------------------------------------------------------------------- |
| Acid blob †             | Acid and stoning resistance                                            |
| Yellow mold †           | Poison resistance                                                      |
| Brown mold †            | Cold and poison resistance                                             |
| Red mold †              | Fire and poison resistance                                             |
| Quivering blob †        | Poison resistance                                                      |
| Gray ooze (glob)        | Fire, cold, and poison resistance                                      |
| Blue jelly †            | Cold and poison resistance                                             |
| [Brown pudding](#a-note-on-puddings) (glob) | Cold, shock, and poison resistance                       |
| Gelatinous cube †       | Fire, cold, shock, and sleep resistance                                |

A gelatinous cube is the highest-density source of ascension-kit
intrinsics in the game; poison resistance off any of the early
corpses is the most important single intrinsic to bank.

**Sprig of wolfsbane.** Not a corpse but the same shelf. Eating one
cures lycanthropy outright. If you're heading anywhere were-things
roam (the Mines, the Quest for some roles), carry a sprig or two.
It weighs almost nothing.

**Eat the puddings, cubes, molds, and blobs.** They look like
inedible terrain, but every one of them yields an intrinsic when
eaten. Puddings and acid blobs leave **globs** rather than
corpses (a 5.0 food-handling detail that doesn't change the
strategy), and the globs of one color stack and shrink slowly,
so a pile of brown-pudding globs is a re-rollable chance at
shock resistance.

#### Food Strategy

1. Eat fresh corpses as your primary food source.
2. Save food rations and lembas wafers for emergencies.
3. Eat intrinsic-granting corpses deliberately (even if not hungry).
4. Pray when Weak or Fainting if you have nothing to eat.
5. Buy food from shops when you can afford it.
6. Don't carry more food than you need. It's heavy.

---

### The Apothecary
<!-- audit
2026-05-19:
- dip_potion_explosion tests the DIPPING potion's BUC, not the receiver (potion.c:2279, 2541)
- the receiving potion is consumed regardless via useup(potion) (potion.c:2538)
- never dip a CURSED potion into another — guaranteed explosion
2026-05-18:
- potion of speed grants permanent intrinsic Fast when !cursed (potion.c:1066)
- uncursed extra/full healing also raise maxHP (potion.c:1398-1440)
- strategy aligned with NetHackWiki Potion, Alchemy, Dip: alchemy odds and the guaranteed-blast cases for cursed/acid potions match (https://nethackwiki.com/wiki/Potion, https://nethackwiki.com/wiki/Alchemy, https://nethackwiki.com/wiki/Dip)
- dipping an item (including a single arrow/dart) into a polymorph potion changes its type via poly_obj and identifies the potion (potion.c:2468-2499)
-->

The dungeon is full of mysterious bottles. Ruby liquids, milky
fluids, smoky concoctions: each one a small gamble between salvation
and catastrophe. The colors are shuffled every game, so the "bubbly
potion" that healed you last time might polymorph you this time.
Identification is everything.

#### The Potion Table

As with all randomized items, price is your best friend. A shop
visit narrows a mysterious bottle from "could be anything" to a
short list of candidates:

| Price | Potions                                                                     |
| ----- | --------------------------------------------------------------------------- |
|    20 | [healing](#potion-healing)                                                                     |
|    50 | booze, fruit juice, see invisible, sickness                                 |
|   100 | confusion, [extra healing](#potion-healing), hallucination, restore ability, sleeping, [water](#potion-holy-water)   |
|   150 | blindness, gain energy, invisibility, monster detection, object detection   |
|   200 | enlightenment, [full healing](#potion-healing), levitation, [polymorph](#potion-polymorph), [speed](#potion-speed)                   |
|   250 | acid, oil                                                                   |
|   300 | [gain ability](#potion-gain-ability), [gain level](#potion-gain-level), paralysis                                         |

<div class="price-id-toolbar"></div>

Water is the oddity in the $100 group: it always appears as "clear
potion," identifiable on sight. Don't underestimate it; water is
the raw material for holy water, which is the foundation of
everything.

#### Key Potions

[]{#potion-healing}
**Healing, extra healing, full healing.** The healing chain, and
your lifeline in combat. Extra healing is the workhorse: it always
cures blindness and (non-cursed) also cures sickness in addition
to restoring HP. Non-cursed extra and full healing raise your
maximum HP if the heal would otherwise overflow; blessed versions
give the biggest boost. You can never have too many of these.

[]{#potion-gain-ability}
**Gain ability.** When blessed, raises *all* your stats by 1.
Uncursed raises a random stat. This is liquid gold: save every
one until you can bless it.

[]{#potion-speed}
**Speed.** One non-cursed quaff and you're permanently faster for
the rest of the game; blessing only stretches the temporary timer
that overlays the intrinsic. Speed is arguably the single most
important buff in NetHack; the difference between moving at normal
speed and fast speed is the difference between trading blows and
hitting twice before they swing once. In 5.0, the wand of speed
monster no longer grants permanent speed when self-zapped, only a
temporary burst of 50–74 turns. The potion is the real prize.

[]{#potion-holy-water}
**Holy water.** Not a potion you find: a potion you *make*. Drop
uncursed water on a co-aligned altar, pray, and the gods bless it
for you (pile every water you own on the same square and a single
prayer blesses the whole stack). Holy water then blesses any item
you dip into it. A holy water can even bless *more water* by
dipping into it. Keep one to make more.

[]{#potion-gain-level}
**Gain level.** Raises your experience level by 1. Useful for
reaching quest eligibility quickly, or converting into something
better through alchemy.

[]{#potion-polymorph}
**Identifying a polymorph potion.** A clean test: dip a single
arrow or dart into an unknown potion. If the arrow turns into a
different item, the potion was polymorph and identifies itself.
You spend one arrow and one potion; you save the gamble of
quaffing it.

#### Alchemy

Here's where potions get interesting. Dip one potion into another
and you might create something better, or you might cause an
explosion. Most combinations are duds, but the useful recipes are
worth memorizing:

| Dip this            | Into this           | Result               |
| ------------------- | ------------------- | -------------------- |
| Healing             | Gain energy/level   | Extra healing        |
| Extra healing       | Gain energy/level   | Full healing         |
| Full healing        | Gain energy/level   | Gain ability         |
| Fruit juice         | Gain energy/level   | See invisible        |
| Speed               | Healing             | Extra healing        |
| Booze               | Gain energy/level   | Hallucination        |
| Levitation          | Enlightenment       | Gain level (2/3)     |

The chain from healing → extra healing → full healing → gain ability
via gain energy or gain level is the core alchemy sequence, and it's
extraordinarily powerful. A handful of common healing potions and a
gain energy or two can be transmuted into the rarest potions in the
game. Treat every gain energy potion like the catalyst it is.

A side-loop worth knowing: **Levitation + Enlightenment → Gain level
(2/3 chance, or nothing 1/3)**. Both inputs are reasonably common
and individually low-value, but the output is one of the catalysts
that feeds the main healing chain. If you find a stack of each, this
is a way to manufacture gain-level potions rather than wait for the
dungeon to drop them.

**A note on the current state of dungeon chemistry.** The old alchemy
trick (dilute a large stack of potions by dipping them in water, then
convert the whole diluted stack at once) no longer works. Current
editions cap diluted dips at two potions per operation. The chain from
healing up to gain ability is still there; you just do it in small batches
with undiluted inputs. Think of it as artisanal alchemy rather than
industrial production.

Alchemy carries an explosion risk: roughly 10% on any non-water combination. An
alchemy smock (if you find one) reduces this to about 1 in 30, which
is the difference between "risky hobby" and "acceptable profession." Do
your chemistry in an isolated room, away from your stash, and never
dip a cursed potion into another. The dipping potion (not the one it
goes into) is the one the game tests for explosion, and a cursed
dip detonates every time. The dungeon is consistent about this if
nothing else.

#### Unicorn Horn Interactions

A unicorn horn dipped into certain potions purifies them:

- **Blindness, confusion, hallucination** → uncursed water
- **Sickness** → fruit juice

This turns dangerous potions into useful raw materials. The water
can be blessed into holy water; the fruit juice can be alchemized
into see invisible. Nothing is wasted in a well-run dungeon
pharmacy.

---

### The Scroll Rack
<!-- audit
2026-05-21:
- blessed class genocide kills the player on the spot if any of the genocided species i matches gu.urole.mnum OR gu.urace.mnum: u.uhp = -1, done(GENOCIDED) (read.c:2769-2780)
- player race mnum mappings: Dwarf is PM_DWARF in class h (monsters.h:485 S_HUMANOID); Gnome is PM_GNOME in class G; Elf is PM_ELF in class @; Orc is PM_ORC in class o; Human is PM_HUMAN in class @
- mind flayers are also class h, so the popular "blessed-genocide h" pick is fatal for Dwarves
2026-05-19:
- confused destroy armor erodeproofs ONLY if cursed; uncursed/blessed strip erodeproofing (read.c:1341)
- confused enchant armor/weapon erodeproofs when !cursed — opposite BUC condition (read.c:1138)
- confused taming radius widens to 11×11 (read.c:1689)
- confused teleportation forces a level teleport (read.c:2015-2025)
- confused gold detection routes through trap_detect (read.c:2041)
- confused light spawns cancelled tame yellow lights (or black lights if cursed) (read.c:1756-1783)
- confused charging restores u.uen / u.uenmax instead of charging an item (read.c:1799-1812)
- confused scare monster wakes monsters and prints sad wailing (read.c:1467-1485)
- confused genocide forces PLAYER bit: confused+uncursed = REALLY|PLAYER = self-genocide; confused+cursed = PLAYER without REALLY, spawns 4-6 of your race/role (read.c:1737, 2826-3015)
2026-05-18:
- above +5 with amount >= 0, chwepon has 2/3 destroy chance via rn2(3) (wield.c:999-1009)
- safe enchantment ceiling for weapons is +5
- charging success is n^3/7^3 per try (read.c:746-758)
- charging odds: 2nd 0.29%, 3rd 2.33%, 4th 7.87%, 5th 18.66%, 6th 36.44%, 7th 62.97%, 8th 100%
- WAN_WISHING lim=1; cursed strips charges; blessed gives the same +1 as uncursed (read.c:738-789)
- second recharge on a wand of wishing is a 100% explosion via the recharged>0 branch (read.c:761-764)
- strategy aligned with NetHackWiki Scroll of charging, Scroll of enchant weapon, Scroll of destroy armor: +5 safe ceiling for weapons, wand-of-wishing-recharges-exactly-once rule, confused destroy-armor erodeproofs (https://nethackwiki.com/wiki/Scroll_of_charging, https://nethackwiki.com/wiki/Scroll_of_enchant_weapon, https://nethackwiki.com/wiki/Scroll_of_destroy_armor)
2026-05-23:
- identify_pack iterates gi.invent only (invent.c:2711-2735) — bag contents and floor items are not touched
- read.c:2087-2092 sets cval: blessed always rolls cval=rn2(5); uncursed rolls only on 1/5; cursed always cval=1
- cval==0 (1-in-5 of the blessed roll) identifies ALL inventory items; blessed+Luck>0 promotes cval=1 to 2 so minimum is two
- citation: NetHackWiki Scroll of identify (https://nethackwiki.com/wiki/Scroll_of_identify)
-->

Scrolls are the dungeon's single-use spells: read once, triggered,
gone. They appear with absurd randomized labels ("ZELGO MER,"
"DAIYEN FOOELS," "PRATYAVAYAH") that stay consistent within a game
but mean nothing until you identify them. The labels are part of
the charm. You'll develop superstitious favorites.

#### The Scroll Table

Price-identification is especially powerful for scrolls, because the
cheapest scroll (base 20) is always identify, the one you need most:

| Price | Scrolls                                                                                                           |
| ----- | ----------------------------------------------------------------------------------------------------------------- |
|    20 | [identify](#scroll-identify)                                                                                                          |
|    50 | light                                                                                                             |
|    60 | blank paper, [enchant weapon](#scroll-enchant)                                                                                       |
|    80 | [enchant armor](#scroll-enchant), [remove curse](#scroll-remove-curse)                                                                                       |
|   100 | confuse monster, destroy armor, fire, food detection, gold detection, [magic mapping](#scroll-magic-mapping), [scare monster](#scroll-scare-monster), [teleportation](#scroll-teleportation) |
|   200 | amnesia, create monster, earth, taming                                                                            |
|   300 | [charging](#scroll-charging), [genocide](#scroll-genocide), punishment, stinking cloud                                                                    |

<div class="price-id-toolbar"></div>

The $60 group is treasure (enchant weapon lurks there alongside
innocent blank paper). The $80 group is equally good: enchant armor
and remove curse, two scrolls you'll always want more of. The $100
group is the danger zone, a grab-bag mixing magic mapping and
teleportation with destroy armor. At $300, you'll find both
genocide (the nuclear option) and punishment (a ball and chain
attached to your ankle). Choose wisely.

#### Key Scrolls

[]{#scroll-identify}
**Identify.** The bread and butter of dungeon life. The scroll
only inspects your **main inventory**: items inside a bag or
sitting on the floor are invisible to it. Pull everything out of
your bag, pick up nearby unknowns, and consolidate them in your
pack before reading. Blessed identify with positive Luck names at
least two items, and on a 1-in-5 roll it names your whole
inventory at once. You will never have enough of these.

[]{#scroll-enchant}
**Enchant weapon / enchant armor.** The path to endgame power.
Uncursed enchant *weapon* raises by +1. Blessed raises by up to 3,
less the more the weapon is already enchanted (no more than +1 once
the weapon is +6 or higher). And there's a catch: at +6 or higher,
each read has a 2/3 chance of destroying the weapon outright. **Safe
ceiling: +5.** Enchant *armor* raises by a small
random amount that's larger when armor is unenchanted, larger again
for elven or non-magic armor, and +1 extra when blessed. Once worn
armor exceeds **+3** (or **+5** for elven / Wizard's Cornuthaum),
each further enchant attempt can destroy the armor; the scroll
"evaporates" your gear. Blessed scrolls don't bypass this cap.

[]{#scroll-remove-curse}
**Remove curse.** Frees you from cursed equipment. Uncursed version
works on worn and wielded items only; blessed version uncurses your
entire inventory. Every adventurer has a "put on a cursed ring"
story. This scroll is the happy ending.

[]{#scroll-charging}
**Charging.** Recharges wands and rechargeable tools. Save these
for your wand of wishing: one charge means one more wish. Blessed
charging restores more charges. Each recharge has an `n³/7³` chance
of the wand exploding (where `n` is the count of previous recharges):
0% on first, 0.3% on second, 2% on third, 8% on fourth, 19% on fifth,
36% on sixth, 63% on seventh — and on the eighth, always. Wand of wishing is the
exception: it explodes 100% of the time on the second recharge, so
recharge it exactly once and no more.

[]{#scroll-genocide}
**Genocide.** The nuclear option. Uncursed eliminates a single
species; blessed wipes an entire monster class from the game
forever. Liches (`L`) are the canonical blessed target.
**Never blessed-genocide a class that contains your own race
or role.** Dwarves are `h`, Gnomes are `G`, Elves and Humans
are `@`, Orcs are `o`; a blessed scroll targeting one of those
ends the game with "killed by a scroll of genocide". (That
makes the popular "wipe mind flayers" pick a Dwarf trap, since
mind flayers are also `h`.) Read one while confused and you
genocide your own role's species the same way. Read carefully.

[]{#scroll-reverse-genocide}
**Reverse genocide.** A cursed scroll of genocide doesn't remove
its target; it spawns 4 to 6 of the named species at your feet.
The named species must be one that can ordinarily be created.
Naming wraiths gives you a corpse pile for level recovery; naming
mind flayers buys an Int-fed feast if you're polymorphed into one;
naming an easy-to-tame creature gives you instant pet candidates.
Don't try unique monsters (the gods refuse).

[]{#scroll-magic-mapping}
**Magic mapping.** Reveals the entire level layout; blessed also
shows secret doors. Invaluable in Gehennom's maddening mazes,
where mapping by hand could take a lifetime you don't have.

[]{#scroll-scare-monster}
**Scare monster.** The trick: don't read it. Drop it on the floor
and stand on it. It works like a permanent [Elbereth](#elbereth), frightening
most monsters away. The catch: pick it up after it's been dropped
and it crumbles to dust. So choose your standing spot wisely.

[]{#scroll-teleportation}
**Teleportation.** Uncursed teleports you randomly on the level.
Cursed or confused reading sends you to a random dungeon level.
With teleport control, *you* choose where you land — the game's
most flexible escape hatch.

[]{#scroll-stinking-cloud}
**Stinking cloud.** Reading places a poison-gas fog at any square
you can see (about fifteen squares of coverage uncursed,
twenty-five if blessed) that blinds anything inside and deals
roughly 6–13 HP per turn to anything not poison-resistant. A
clean way to clear a throne room or the Wizard's Tower from a
safe corridor, as long as *you* are poison-resistant or
unbreathing: the gas doesn't pick sides. Kills inside the cloud
still count as yours for XP and alignment.

#### Confused Reading

Here's a trick the dungeon doesn't advertise: many scrolls do
something completely different when read while confused. Some of
these alternate effects are *better* than the normal ones:

**Confused destroy armor**, *if cursed*, doesn't destroy anything:
it erodeproofs a piece of armor. (Uncursed or blessed strips
erodeproofing instead.) One of the best tricks in the game.

**Confused enchant armor / enchant weapon**, *if uncursed or
blessed*, erodeproofs the item instead of enchanting. Useful when
you need protection from rust more than another +1.

**Confused remove curse** has a 25% chance of blessing *or* cursing
each uncursed item. Risky, but it's a clever way to create holy
water if you confuse-read while carrying uncursed potions of water.

**Confused taming** widens the scroll's reach from a 3×3 area
around you to 11×11. The trick is scroll-only; confused charm
monster just fizzles.

**Confused teleportation** sends you to a random *dungeon level*
instead of a random spot on this floor. Useful as a panic button,
dangerous if you're shallow and want to keep exploring.

**Confused gold detection** detects every trap on this level
instead of gold. Far faster than searching tile by tile.

**Confused charging** restores Pw, and if you're already at full,
*raises your max Pw* by 4–16 (6–24 blessed). A spellcaster's
permanent buff if you can spare the scroll. Cursed reading zeroes
your Pw instead.

The cleanest way to confuse yourself on purpose is a **potion of
confusion**: drink one and the timer runs about 25–80 turns. A
non-blessed **potion of booze** will also confuse you for a few
turns.

---

### Wands and Staves
<!-- audit
2026-05-18:
- wand of stasis: NODIR, $150, prob 45, freezes the level (objects.h:1460, zap.c:2559-2568)
- wand of nothing is IMMEDIATE, not NODIR (objects.h:1462)
- undead turning revives corpses to their original species via unturn_dead — NOT as zombies (zap.c:1156-1228 unturn_dead, zap.c:900 revive uses corpse->corpsenm; only cant_revive-rejected types fall back to zombie/doppelganger at zap.c:982-985)
- engrave-test: cancellation and make-invisible erase in place (engrave.c:618-633)
- engrave-test: teleportation moves the engraving elsewhere; polymorph rewrites it
- nothing, undead turning, opening, locking, probing produce NO engrave message (engrave.c:635-640)
- magic missile engraves "riddled by bullet holes" — distinctive (engrave.c:642-648)
- sleep and death share "the bugs on the <surface> stop moving" (engrave.c:651-656)
- striking message: "wand unsuccessfully fights your attempt to write" (engrave.c:602-605)
- slow/speed monster: distinctive "bugs slow down" / "speed up" (engrave.c:606-616)
- self-polymorph into a small form (sliparm) drops body armor (cursed or not) into inventory via Armor_gone+dropp (polyself.c:1198-1228); large forms (breakarm) destroy it instead (polyself.c:1162-1197)
- engrave-test ambiguity between cancellation, make-invisible, teleportation, polymorph can be resolved by zapping a known item: make-invisible turns it invisible; teleportation moves it; cancellation dulls it (zap.c:2313-2317); polymorph changes its type (zap.c:weffects branch)
- strategy aligned with NetHackWiki Wand, Engraving, Wand of wishing: engrave-test as the safest wand-ID method, $500 narrowed to death-or-wishing, wand of wishing recharge mechanics (https://nethackwiki.com/wiki/Wand, https://nethackwiki.com/wiki/Engraving, https://nethackwiki.com/wiki/Wand_of_wishing)
-->

Wands are reusable magical items that produce directed effects when
zapped. They come in three types: **ray wands** fire a beam in a
direction that bounces off walls, **beam wands** affect what they
hit in a straight line, and **non-directional wands** affect the
area around you.

#### The Wand Table

Unlike scroll and potion prices, wand prices alone rarely pin down a
specific wand — a $150 wand is one of thirteen possibilities. The
**engrave-test result** in the rightmost column is far more useful:
most wands reveal themselves in one zap. See [The Engrave Test
(Wands)](#the-engrave-test-wands) for the procedure and [Resolving
Ambiguous Engrave Results](#resolving-ambiguous-engrave-results) for
the few shared results.

<div class="price-id-toolbar"></div>

| Price | Wand | Type | Max Charges | Engrave-test result |
| --- | --- | --- | --- | --- |
|   100 | Light                                       | NODIR | 15 | room lights up         |
|   100 | Nothing                                     | BEAM  | 15 | no message             |
|   150 | [Digging](#wand-digging)                    | RAY   | 8  | gravel flies up        |
|   150 | Enlightenment                               | NODIR | 15 | you feel enlightened   |
|   150 | Magic missile                               | RAY   | 8  | bullet holes           |
|   150 | [Make invisible](#wand-make-invisible)      | BEAM  | 8  | engraving vanishes ¹   |
|   150 | Opening                                     | BEAM  | 8  | no message             |
|   150 | Probing                                     | BEAM  | 8  | no message             |
|   150 | Secret door detection                       | NODIR | 15 | doors revealed         |
|   150 | Slow monster                                | BEAM  | 8  | bugs slow down         |
|   150 | Speed monster                               | BEAM  | 8  | bugs speed up          |
|   150 | [Stasis](#wand-stasis)                      | NODIR | 15 | no message             |
|   150 | Striking                                    | BEAM  | 8  | wand fights you        |
|   150 | Undead turning                              | BEAM  | 8  | no message             |
|   150 | Locking                                     | BEAM  | 8  | no message             |
|   175 | [Cold](#wand-fire-cold-lightning)           | RAY   | 8  | ice cubes drop         |
|   175 | [Fire](#wand-fire-cold-lightning)           | RAY   | 8  | flames fly             |
|   175 | [Lightning](#wand-fire-cold-lightning)      | RAY   | 8  | lightning arcs         |
|   175 | Sleep                                       | RAY   | 8  | bugs stop moving ²     |
|   200 | [Cancellation](#wand-cancellation)          | BEAM  | 8  | engraving vanishes ¹   |
|   200 | Create monster                              | NODIR | 15 | bugs appear            |
|   200 | [Polymorph](#wand-polymorph)                | BEAM  | 8  | engraving rewrites     |
|   200 | [Teleportation](#wand-teleportation)        | BEAM  | 8  | engraving vanishes ¹   |
|   500 | [Death](#wand-death)                        | RAY   | 8  | bugs stop moving ²     |
|   500 | [Wishing](#wand-wishing)                    | NODIR | 3  | prompts for a wish     |

<small>¹ Shared by cancellation, make-invisible, and teleportation.
² Shared by sleep and death.</small>

<div class="price-id-toolbar"></div>

#### Key Wands

[]{#wand-wishing}
**Wishing.** The most valuable item in the game. Each zap grants one
wish. In 5.0, wands of wishing generate with only **1
charge** and can be recharged once (and only once) to a maximum of
1 additional charge. This means the Castle wand of wishing typically
yields 2 wishes plus a possible wrested third, a significant
reduction from older versions where it could provide 5 to 7. Plan
your wishes carefully before you find one.

[]{#wand-death}
**Death.** Fires a death ray that instantly kills most things it
hits. Reflected by reflection. Blocked by magic resistance. One
of the best offensive tools in the late game.

[]{#wand-digging}
**Digging.** Essential utility. Dig through walls to create
shortcuts, dig down to escape dangerous situations, dig through
rock to reach vaults and hidden areas. Every ascension kit should
include a wand of digging. It also doubles as the universal "I'm
leaving" button: a downward zap drops you straight onto the next
floor, the same direction you wanted to go anyway. One quirk: a
*cursed* wand of digging zaps downward no matter which direction
you point it.

[]{#wand-teleportation}
**Teleportation.** Zap monsters to send them somewhere else on the
level. Zap yourself to teleport. Enormously useful for escaping
trouble or removing a dangerous monster from your path.

[]{#wand-fire-cold-lightning}
**Fire, cold, lightning.** Offensive ray wands that bounce off walls.
Fire burns scrolls and spellbooks on the floor. Cold freezes water
(useful for creating paths). Lightning blinds monsters.

[]{#wand-cancellation}
**Cancellation.** Removes special properties from items and monsters.
A cancelled monster loses most of its special attacks — a cancelled
cockatrice can't petrify, a cancelled mind flayer can't suck brains,
and a cancelled clay golem dissolves on the spot. Do NOT put this
wand in a bag of holding (it will explode the bag). Pointed at a
pile of unidentified scrolls and potions, it converts them into
blank scrolls and water, which feed the magic-marker and holy-water
production lines. Keep it separate in your main inventory.

[]{#wand-polymorph}
**Polymorph.** Transforms monsters into random other monsters and
items into random other items of the same class. Can be used
creatively (polymorph a pile of junk armor hoping for dragon scale
mail, polymorph a weak monster hoping for a useful corpse). Risky
but powerful.

[]{#wand-make-invisible}
**Make invisible.** Turns a target (or yourself, if you zap it
reflexively) invisible. In older editions, self-zapping granted a
permanent invisibility intrinsic, which made this a coveted find. In
5.0, it gives you 31–45 turns of temporary invisibility.
Still useful for slipping through a dangerous area or turning a fight
in your favor, but not a permanent upgrade. For lasting invisibility,
you want a ring of invisibility or a cloak. The wand is now a tactical
tool rather than a build enabler: think of it as "invisibility on
demand for the next minute" rather than "invisibility forever from one
lucky find."

[]{#wand-stasis}
**Stasis.** A new 5.0 wand that freezes every monster on the level
for **10–30 turns**. No ray, no aim, no message — just a hush. Use
it when you're surrounded and need a free moment to engrave
[Elbereth](#elbereth), drink a potion, change weapons, or just walk past. The
silence on engraving makes it harder to identify by the engrave
test, but if you sit on a charge for a fight you'll know.

**Probing.** A diagnostic wand: zap at a monster to learn its HP,
max HP, level, and *what it's carrying*. Useful on shopkeepers,
soldiers, and named adventurers whose inventory might be worth
the trouble. A stethoscope reports HP and status but not gear; if
you want to know what's in the pack, probing is the tool.

#### Resolving Ambiguous Engrave Results

A few engrave-test results are shared by more than one wand.

**"The engraving vanishes!"** belongs to **cancellation**,
**make-invisible**, or **teleportation**. Drop a known item and zap
each candidate: make-invisible hides it, teleportation sends it
elsewhere on the level, cancellation dulls its magic.

**"The bugs on the floor stop moving!"** belongs to **sleep** or
**death**. Death is the only $500 ray wand.

**No engrave message at all** narrows to one of six: **nothing**,
**opening**, **locking**, **probing**, **undead turning**, or
**stasis**. Test each at a safe target:

- **Opening** unlocks a chest or door. **Locking** locks one.
- **Probing** reveals a nearby monster's stats.
- **Undead turning** revives a fresh corpse to its original species
  (and animates any corpses the target was carrying).
- **Stasis** halts every monster on the level — the silent freeze is
  unmistakable mid-combat.
- **Nothing** does nothing.

For non-ambiguous wands, a follow-up zap at a safe target confirms
what the engrave-test already suggested: **slow monster** /
**speed monster** at a tame or weak monster, **striking** at a
closed door, **polymorph** at a pile of junk gear. Avoid zapping
unidentified wands at yourself.

#### Recharging

Wands can be recharged with a scroll of charging. The most prized
use is on a wand of wishing, where one recharge safely turns a
single wish into two. Each successive recharge raises the risk of
the wand exploding. The formula is (recharges cubed) / 343, so:

- First recharge: 0.3% explosion chance.
- Second: 2.3%.
- Third: 7.9%.
- Seventh: 100%.

Use blessed charging for the best results — except on a wand of
wishing, which follows its own rules. A fresh wand of wishing is
always generated with **exactly one** charge. A scroll of charging
adds **one more** wish whether blessed or uncursed; blessing
doesn't help here, and a cursed scroll strips the wand to zero
like any other. You can recharge once safely; a second attempt is
a **guaranteed explosion**. So the lifetime cap on a single wand
of wishing is two wishes reliably, or three if you successfully
wrest the final charge at the end.

Rings are chargeable too, but with a practical ceiling. The
explosion chance scales with the ring's current enchantment:
roughly 1/7 per point. A +0 or +1 ring of protection is virtually
free to charge; a +3 ring explodes about 43% of the time; +7 is a
guaranteed bang. The popular cap is around +5.

#### Wresting

When a wand has 0 charges, you can still try to zap it. There is a
1/121 chance of "wresting" one final charge from the wand before it
turns to dust. This is a last resort, but it works on wands of
wishing too.

#### Polymorph as a Tool

Self-polymorph is one of the most interesting tools in the game.
A wand of polymorph zapped at yourself, a potion of polymorph, the
polymorph self spell, or stepping on a polytrap all do the same
thing: roll a new form for you. With **polymorph control** (the
ring or intrinsic) the game lets you *choose* the form, which is
where the real fun begins.

- **Travel where your legs can't.** A xorn phases through walls.
  An eel breathes underwater. A vampire becomes a bat or a fog
  cloud and slips under doors. A floating eye drifts past traps
  you can't disarm.
- **Bring your own resistances and attacks.** A red dragon form
  gives you fire breath. A brown mold form burns anything that
  hits you in melee. A purple worm swallows your problems whole.
  Most monster powers are yours when you wear their shape.
- **Grow a bigger body.** A stronger form rolls a new max HP and
  your current HP scales with the ratio. A dying Wizard at 50/100
  wakes up at 200/400 as a fresh titan.
- **Escape cursed body armor.** A *bigger* form breaks out and
  destroys the suit. A *smaller* form drops it intact into your
  inventory, where you can holy-water it back to neutral.
- **Eat what you can't.** A metallivore form eats iron bars. A
  green dragon shrugs off poisonous corpses.

Caveat: cursed polymorph items strip control, and rough
transformations can hit you with system shock. Don't be at 5 HP
when you reach for the wand.

A wand of polymorph zapped at a *pile* of junk items reshuffles
each one into a random item of the same class. This trick is
called "polypiling," because it can turn a pile of dross into a
selection of stuff you need. Drop the fodder on a square far from your real pack:
a misaimed zap that catches your bag of holding rolls the bag too.
Max your Luck first. When polypile fails, one of the zapped items
can turn into a hostile golem made from its material, and every
point of Luck lowers the chance of that going wrong.

---

### Rings and Amulets
<!-- audit
2026-05-18:
- ring prices match objects.h:741-827
- teleportation, polymorph, aggravate-monster, hunger rings 90% cursed (mkobj.c:1143-1146)
- aggravate-monster effective-depth doubling is capped at 50 (dungeon.c:2080-2082)
- free action gives paralysis immunity via Free_action (apply.c:1044, mcastu.c:506)
- ring hunger cost ticks at turns 4 and 12 (eat.c:3237-3267)
- amulet of guarding: +2 AC, +2 MC (do_wear.c:2496, mhitu.c:1121-1126)
- restful sleep regenerates +1 HP per sleep tick (allmain.c:663-664)
- restful sleep is 90% cursed at generation, not 100% (mkobj.c:1063-1066 via rn2(10))
- ring of protection subtracts from AC (do_wear.c:2492-2495)
- conflict makes pets attack you (dogmove.c:1046-1054, mhitm.c:104-145)
- blessed polymorph control rolls from base form only (potion.c:1322-1325)
- strategy aligned with NetHackWiki Ring strategy, Ring of free action, Ring of conflict, Amulet of life saving: free action against late-game paralysis, conflict for crowd control, life saving for risky endgame moments (https://nethackwiki.com/wiki/Ring_strategy, https://nethackwiki.com/wiki/Ring_of_free_action, https://nethackwiki.com/wiki/Ring_of_conflict, https://nethackwiki.com/wiki/Amulet_of_life_saving)
-->


Two ring fingers. One neck. These are the most constrained equipment
slots in the game, which makes choosing what to wear a genuine
strategic decision. Both rings and amulets have randomized
appearances, and some of the best items in the game hide behind
unassuming descriptions like "granite ring" or "circular amulet."

#### The Ring Table

<div class="price-id-toolbar"></div>

| Price | Ring                           | Notes                          |
| ----- | ------------------------------ | ------------------------------ |
|   100 | Adornment                      | +CHA, chargeable               |
|   100 | Hunger                         | Increases hunger (auto-curse)  |
|   100 | Protection                     | +AC, chargeable                |
|   100 | Protection from shape changers | Useful against werebeasts      |
|   100 | Stealth                        | Reduces noise                  |
|   100 | Sustain ability                | Prevents stat drain            |
|   100 | Warning                        | Shows nearby monsters          |
|   150 | Aggravate monster              | Bad (auto-curse)               |
|   150 | Cold resistance                | Resist cold attacks            |
|   150 | Gain constitution              | +CON, chargeable               |
|   150 | Gain strength                  | +STR, chargeable               |
|   150 | Increase accuracy              | +hit, chargeable               |
|   150 | Increase damage                | +dmg, chargeable               |
|   150 | Invisibility                   | You become invisible           |
|   150 | Poison resistance              | Immune to poison               |
|   150 | See invisible                  | See invisible creatures        |
|   150 | Shock resistance               | Resist electric attacks        |
|   200 | Fire resistance                | Resist fire attacks            |
|   200 | Free action                    | Immune to paralysis            |
|   200 | Levitation                     | Float in the air               |
|   200 | Regeneration                   | Heal faster (costs hunger)     |
|   200 | Searching                      | Auto-search each turn          |
|   200 | Slow digestion                 | Reduces hunger                 |
|   200 | Teleportation                  | Random teleports (auto-curse)  |
|   300 | Conflict                       | Monsters fight each other      |
|   300 | Polymorph                      | Random polymorphs (auto-curse) |
|   300 | Polymorph control              | Choose polymorph form          |
|   300 | Teleport control               | Choose teleport destination    |

<div class="price-id-toolbar"></div>

Rings marked "auto-curse" generate cursed 90% of the time. If you
slip on a ring and can't remove it, you've just learned what
auto-curse means the hard way.

**Ring of aggravate monster** deserves a footnote in the "niche uses
of terrible things" category. In 5.0, wearing it roughly
doubles the effective dungeon level for purposes of monster generation,
so creatures well above your current depth start appearing. This is
obviously catastrophic if you forget you're wearing it. But for a
chaotic player who needs high-difficulty sacrifice fodder for the next
artifact gift, deliberately wearing the ring to force harder spawns
(then removing it) is a calculated risk with an actual payoff. The key
word is "deliberately." The ring is auto-cursed 90% of the time. If it
goes on and won't come off, the fact that you're now generating liches
on dungeon level 8 is no longer a feature.

**The rings that matter most:** Free action is arguably the single
best ring in the game: paralysis is death in the late game, and
this ring makes you immune. Teleport control turns random
teleportation from a nuisance into on-demand transportation.
Conflict makes monsters attack each other instead of you, which
is devastating on crowded levels (though it also turns your pets
hostile). Slow digestion lets you go indefinitely between meals.

In 5.0, a blessed potion of polymorph grants you polymorph
control for that specific transformation: you choose the form, no ring
required. This makes the ring of polymorph control less of a critical
acquisition: you no longer need to find it or wish for it just to do a
single controlled polymorph. The ring remains useful if you want ongoing
control for repeated transformations, but it's no longer a hard
prerequisite for the opening act of any polymorph strategy. Save that
wish for something else.

**The hidden cost:** Every ring you wear increases your hunger rate.
Two rings drain food noticeably faster. The veteran habit is to
keep rings in inventory and slip them on only when needed: free
action before fighting mind flayers, conflict before entering a
throne room. Economy of fingers is an art. (One curiosity for the
ring-of-slow-digestion holder: the two hands tick hunger on
different turns, so wearing two slow-digestion rings doesn't
double the saving, and swapping a hungry ring onto the *other*
hand briefly skips the tick entirely.)

#### Amulets

Amulets are simpler in theory but harder to identify: they all cost
$150, so price is no help. You'll need to wear-test or use a scroll
of identify. The stakes are high, because the range runs from "saves
your life" to "slowly strangles you to death":

| Amulet                 | Effect                                      |
| ---------------------- | ------------------------------------------- |
| Life saving            | Revives you once from death, then crumbles  |
| Reflection             | Reflects ray attacks                        |
| Magical breathing      | Survive underwater and without air          |
| ESP                    | Detect monsters via telepathy               |
| Unchanging             | Prevents involuntary polymorph              |
| Versus poison          | Poison resistance                           |
| Flying                 | Grants flight (new in 5.0)     |
| Guarding               | +2 AC and +2 MC (new in 5.0)   |
| Strangulation          | Slowly kills you (always cursed)            |
| Restful sleep          | Puts you to sleep randomly (usually cursed); grants +1 HP/turn regen while asleep |

**Life saving** is the crown jewel. When you die (any kind of
death) it triggers, revives you at full HP, and crumbles to dust.
Wear it whenever you're going somewhere dangerous. Take it off when
you're safe. You only get the one miracle.

**Reflection** is excellent if you didn't get a shield of reflection
from Perseus's statue or elsewhere. Wearing it as an amulet frees
up your shield slot for a small shield or two-weapon fighting.

**Guarding** provides +2 AC and +2 magic cancellation (MC). This
is a new addition in 5.0 that neatly solves the MC
puzzle: pair it with a cloak of magic resistance (MC1) and you
reach MC3, freeing you from needing the less versatile cloak of
protection.

**Magical breathing** prevents drowning, which sounds niche until
you reach Medusa's level (surrounded by water) or the Plane of
Water (entirely underwater). Then it's existential.

**Flying** is the late-addition cousin of levitation: you stay in
the air the same way, but you can still pick things up and you
can choose to drop down on your turn. The under-appreciated bonus
is that **your steed flies with you**. A flying warhorse skips
over moats, fountains, pools, and the Castle's drawbridge entirely
— a fast Knight can cross Medusa's island and the Castle from edge
to edge without worrying about the water at all. Stack with boots
of speed and a wand of speed monster on the mount and you have a
terrifying cavalry unit.

**Restful sleep** puts you to sleep randomly and is usually cursed,
which should tell you everything you need to know about when to put it
on unexamined. However, in 5.0, wearing it while asleep
grants +1 HP per turn via accelerated regeneration, stacking with your
normal healing. In a fully secured room with the door spiked shut and
nothing actively trying to kill you, this turns a nearly useless item
into a slow but functional field hospital. The conditions required
(safety, time, and nothing better to do) describe a situation you rarely
find in the Mazes. When you do, the amulet is less embarrassing to wear
than it looks.

---

### Tools of the Trade
<!-- audit
2026-05-21:
- weight_cap = 25 * (Str + Con) + 50, capped at MAX_CARR_CAP = 1000 (hack.c:4295-4312, weight.h:12-25)
- encumbrance tier = (excess_weight * 2 / cap) + 1, clamped to OVERLOADED; tier names "Burdened/Stressed/Strained/Overtaxed/Overloaded" (hack.c:4372-4382, botl.c:12-13)
- Stressed+ encumbrance triggers extra hunger on odd turns (eat.c:3197 near_capacity > SLT_ENCUMBER)
- Large box base weight 350, chest 600, ice box 900 (objects.h:899-904)
- door diagonal-move rules: cannot move diagonally INTO an intact doorway (hack.c:1140-1149); cannot move diagonally OUT of one (hack.c:1209-1213)
- low-intelligence monsters cannot open closed doors; intelligent monsters open/unlock per monmove.c:1567-1585
- inventory letter limit is invlet_basic = 52 (hack.h:584); inv_cnt(FALSE) >= 52 triggers "Your pack is too full" (invent.c:5246-5251); items in containers are not in gi.invent and don't count against the limit
- #adjust (doorganize, also M-a binding) swaps items between letters and can force-merge mergable stacks (cmd.c:1673-1674, invent.c:4981)
-->
<!-- audit
2026-05-18:
- Bell of Opening is carried by the quest nemesis; loot from the corpse (makemon.c:1378-1379)
- quest leader chides you if you finish without the Bell but doesn't grant it (quest.c:267-268)
- uncursed scroll of charging restores a magic lamp to at least 50 (read.c:880-883)
- blessed scroll of charging pushes the floor to 75 (read.c:866-871)
- magic lamp 1/3 djinni emergence is independent of bless; bless only affects the wish-grant odds (apply.c:1817)
- scroll of charging write cost is rn1(basecost/2, basecost/2) = rn1(8,8) = 8-15 charges (write.c:44, 265)
- class genocide skips uniquely-named demon lords via G_UNIQ (read.c:2998)
- strategy aligned with NetHackWiki Bag of holding, Magic lamp, Unicorn horn: never bag a cancellation wand/bag-of-tricks/another BoH, bless magic lamps before rubbing, blessed unicorn horn for ailments (https://nethackwiki.com/wiki/Bag_of_holding, https://nethackwiki.com/wiki/Magic_lamp, https://nethackwiki.com/wiki/Unicorn_horn)
- BoH explosion fires only on insertion via mbag_explodes (pickup.c:2658-2669); zapping a wand of cancellation at the bag just calls cancel_item which uncurses (zap.c:1239-1361 cancel_item)
-->

The `(` symbol covers the dungeon's most eclectic category: pickaxes,
magic lamps, unicorn horns, musical instruments, crystal balls, and
bags that eat other bags. Some of the most powerful items in the game
hide in this grab-bag.

#### Containers

Sooner or later every adventurer runs out of carrying capacity.
The bag of holding is the dungeon's most coveted answer to the
problem, and the other containers below have their places too.

| Container      | Weight | Special                                  |
| -------------- | ------ | ---------------------------------------- |
| Sack           | 15     | Basic storage                            |
| Oilskin sack   | 15     | Protects contents from water             |
| Bag of holding | 15     | Reduces weight of contents dramatically  |
| Bag of tricks  | 15     | Creates monsters when opened (not a bag) |
| Large box      | 350    | Comes with 0 to 3 items (0 to 5 if locked) |
| Chest          | 600    | Comes with 0 to 5 items (0 to 7 if locked) |
| Ice box        | 900    | Preserves corpses from rotting           |

Note the weights. Sacks are 15 (carry one). Boxes and chests are
furniture, not luggage: a large box weighs 350, a chest 600, an
ice box 900 — comparable to your *entire* carrying capacity. Use
them as floor stash, not as something to drag from level to level.

The **bag of holding** deserves special mention because it
transforms how you play. A blessed bag reduces the weight of
everything inside to roughly one quarter, meaning you can carry your
entire potion supply, your backup armor, your scroll library, and
still have room for loot. Almost every ascending player carries
one. Sokoban's prize is a bag of holding half the time; otherwise
wish for one when you can.

A warning: **never** put a wand of cancellation, another bag of
holding, or a charged bag of tricks inside a bag of holding. The
explosion scatters your inventory across the floor.

If you find a *cursed* bag of holding (in a bones pile, perhaps),
don't open it. Drop it on the floor and zap a wand of cancellation
at it. The explosion rule only fires on insertion, not on a zap,
so the bag uncurses safely.

##### Carrying capacity

Your carrying capacity is roughly **25 × (Strength + Constitution)
+ 50**, capped at 1000. Average human stats land you near 950;
a low-Str spellcaster might start closer to 700. As you load up,
the status line walks through these tiers:

| Tier         | When                                    | Cost                                        |
| ------------ | --------------------------------------- | ------------------------------------------- |
| Unencumbered | weight at or below capacity             | None                                        |
| Burdened     | up to about 1.5× capacity               | Status flag, but movement and nutrition fine |
| Stressed     | up to about 2× capacity                 | Extra hunger every odd turn                 |
| Strained     | up to about 2.5× capacity               | Worse hunger, harder to dodge water         |
| Overtaxed    | up to about 3× capacity                 | Bad                                         |
| Overloaded   | beyond 3× capacity                      | You can't even pick anything else up        |

Practical rule: stay **Unencumbered** in normal play, accept
**Burdened** during loot runs, and never linger at **Stressed**
or worse without a reason. The bag of holding is the standard
answer to the encumbrance problem; carrying everything inside one
reduces the effective weight to roughly a quarter, which is why
veteran players treat finding one as a turning point in the run.

**Running out of inventory letters.** Weight isn't the only limit.
Your inventory has **52 slots** (`a-z` plus `A-Z`), and a 53rd
item hits *"Your pack is too full."* Stackable items consolidate
into a single slot only when the game can tell they're the same
thing — five identified scrolls of identify share one letter, but
identified and unidentified scrolls of the same type stay in
separate slots, and weapons of different enchantments don't
merge. So clutter is usually an identification problem in
disguise: the more you ID, the more your inventory consolidates.
The bag of holding doubles as the answer here too — items inside
any container don't count against your 52, so a stash of
twenty potions in a BoH costs you a single letter. The `#adjust`
command lets you swap items between letters, force-merge stacks
that didn't merge, or split a stack to a new letter — purely
relabeling, no game effect.

One 5.0 hazard that you will need to be aware of:
**intelligent monsters can now loot unlocked containers**.
They can remove items, carry containers away, and unlock chests with
keys. If you've been leaving your secondary stash in an unlocked chest
on a partially-cleared level while you scouted ahead, stop. The Castle
chest in particular (containing the wand of wishing) can be emptied
by the level's residents if you leave them time and opportunity. Clear
levels before abandoning valuables, and **keep your most important
containers locked**. The dungeon has gotten better at wanting what
you have.

#### Unlocking Tools

The dungeon is full of locked things, and brute force is noisy and
slow. A **skeleton key** is the gold standard (70%+ success on
doors, 75%+ on boxes). A **lock pick** is respectable. A **credit
card** is the worst but still better than kicking. Always carry one
of these. The weight is negligible and the utility is constant.

Skeleton keys and lock picks can also **lock** what they can unlock,
so they double as your way to relock a chest after stashing loot.
Credit cards are unlock-only.

#### Light Sources

**Oil lamps** and **candles** light dark corridors, which is
pleasant but not essential. The real prize is the **magic lamp**:
rub it and there's a 1-in-3 chance the djinni emerges, then a
chance it grants you a wish — 80% if the lamp is blessed (so
~27% wish per rub overall), less if it isn't. Try again on the
same lamp until the djinni shows. Never, ever use a magic lamp
for light. That's like using a winning lottery ticket as a
bookmark.

The **Candelabrum of Invocation** is a unique candelabra found in
Vlad's Tower. It's one of three items needed for the invocation
ritual to enter Moloch's Sanctum. You'll need seven candles to
fill it, so start hoarding candles when you find them.

#### Musical Instruments

Music has power in the Mazes. Any tonal instrument (wooden flute,
magic flute, tooled horn, frost or fire horn, bugle, or harp) can
play the passtune at the Castle drawbridge — you'll find the notes
nearby, so listen carefully. A **magic harp** charms monsters into
tameness. A **magic flute** puts them to sleep. A **drum of
earthquake** creates pits around you, which is as chaotic as it
sounds.

Non-magical instruments (wooden flute, leather drum) produce noise
but no special effects, useful only for confusing the issue.

#### Other Notable Tools

| Tool               | Use                                           |
| ------------------ | --------------------------------------------- |
| Pickaxe / mattock  | Dig through walls and floors                  |
| Unicorn horn       | Cure confusion, blindness, sickness, hallucination, stunning, vomiting, deafness |
| Stethoscope        | Check HP and status of a monster              |
| Tin opener         | Open tins in one turn                         |
| Tinning kit        | Preserve corpses as tins                      |
| Can of grease      | Coat armor, weapons, bags                     |
| Blindfold          | Voluntarily go blind (useful for telepathy)   |
| Towel              | Wipe cream pie from face, use as blindfold    |
| Magic marker       | Write scrolls and spellbooks on blank paper   |
| Crystal ball       | Pick a glyph class per gaze (objects, traps, monsters, etc.); each gaze answers one question |
| Bell of Opening    | Invocation item; carried by your quest nemesis, looted from their corpse |
| Leash              | Tie a pet to you so it follows through stairs |

The **unicorn horn** is the dungeon's all-purpose first-aid kit.
Apply it to cure confusion, blindness, sickness, hallucination,
stunning, vomiting, and (new in 5.0) deafness: most of the status
ailments that matter. Carry one at all times. If you don't have one,
getting one should be near the top of your priority list.

Bless your horn. A blessed horn can fix up to seven ailments in a
single application; an uncursed horn maxes out at three, with a 35%
chance of doing nothing even when you have troubles to fix. A cursed
horn will *inflict* a random ailment from the same list (including
the new deafness one), so be sure of bless status before applying.
Horns don't get used up, so a non-emergency test apply is free.

A 5.0 caveat: the unicorn horn **no longer restores lost ability
scores** the way it used to. Drained Strength, Intelligence, Wisdom,
and so on now require a *potion of restore ability* (or its spell)
to bring back. The horn remains the universal cure for *status*
problems, but not for attribute drain. Earlier guides that described
it as a complete cure-all are out of date; budget for restore ability
separately.

The **magic marker** is a printing press for scrolls (and, more
expensively, spellbooks). A fresh marker has 30-99 charges; one
non-cursed scroll of charging restores it to at least 50 (more if
the scroll is blessed), but only once. The second recharge attempt
always fails. Each write costs roughly half to all of the target
scroll's basecost: magic mapping 4-7 charges, identify 7-13,
enchant weapon / enchant armor / charging 8-15, teleportation
10-19, and **genocide 15-29**. Spellbooks cost about 10 × spell
level: a level-3 book averages ~22 charges, a level-7 ~52.

To write a scroll intentionally you must have **identified** it
first. Writing by appearance gives a random scroll of that
appearance, which is usually wasted charges. If charges run out
mid-write, scrolls disappear entirely (paper + charges wasted); a
spellbook's paper survives but the writing fades.

The big-ticket writes for an ascension kit are scrolls of
**genocide** (three of these wipe the worst monster letters L, &,
and h out of the game, though uniquely-named demon lords survive
any class genocide; see [Genocide](#scroll-genocide) for the
race-trap warning), **charging** (a blessed one restores one
additional wish to an empty wand of wishing for 8-15 charges very
well spent, though a second charging attempt always explodes the
wand), and **enchant weapon / enchant armor** for the +7 ascension
kit. A well-used marker can produce a meaningful share of your
ascension kit.

The marker also feeds the **wraith feast**: write a *cursed*
scroll of genocide, read it on a non-graveyard level, and the
game reverse-genocides four to six fresh wraiths at your feet
(see [Farming wraiths](#a-note-on-wraiths)). At ~1.6 corpses per
scroll, a marker plus a stack of blank paper is a small XP
factory for the late game.

The **tinning kit** turns a fresh corpse (`a`pply, then select the
corpse) into a tin: 450 nutrition's worth of preserved food that
keeps indefinitely. The interesting part is that tin-eating skips
the raw-corpse poison and acid damage checks. A tinned killer bee
or acid blob is safe to eat with no resistance, and the
intrinsic-grant still applies — so the kit doubles as a way to
grind poison or acid resistance without taking the per-corpse
hits. One warning the kit doesn't give: tinning a cockatrice
without gloves petrifies you on the spot.

The **crystal ball** is a one-question oracle when applied (`a`):
pick a glyph class, point at a square, learn what's there or what's
on the level. Beautiful in theory; ruinous in practice if your
Intelligence is low. A blessed ball wants Int 16+ to be reliable,
and a cursed ball can hallucinate, blind, or simply shatter. Drop
it on an altar before the first use.

The **magic lamp** must be blessed before you rub it: cursed magic
lamps never grant the wish, uncursed are around 40%, blessed are
~80%. Take it to a co-aligned altar first.

The **can of grease** is the cheapest hardening upgrade in the
dungeon. Apply it to a worn armor piece and the slick coat makes
the wearer harder to grab and steal from: nymphs slide off, the
Riders' grab attacks miss, and weapon-snatch attempts fail. Applied
to a bag of holding, it waterproofs the contents like an oilskin
sack — handy before crossing Medusa's moat or the Plane of Water.
The coat wears off after a few hits, so it's per-fight protection,
not a long-lasting investment.

---

### The Armory
<!-- audit
2026-05-18:
- shield of drain resistance is a second non-artifact source (objects.h:656-658)
- warning glyph levels: white, red ×3, magenta, bright-magenta — no yellow (drawing.c:39-52)
- cloak of protection MC3; cloak of magic resistance MC1 (objects.h:637-646)
- MC formula at uhitm.c:87 — MC3 blocks 90% of monster spells
- helm of caution grants the WARNING intrinsic (do_wear.c:448-450)
- DSM dual-property pattern: armor + per-color intrinsic (do_wear.c:806-883)
- gray and silver DSM grant no extra intrinsic
- DSM scroll-of-enchant transformation requires spe ≥ 0 (read.c:1225)
- small shield is the only shield with no spellcast penalty (spell.c:2269)
- strategy aligned with NetHackWiki Dragon scale mail, Cloak of protection, Magic cancellation, Speed boots: GDSM as the popular MR wish, MC3 from cloak of protection, speed boots make turns more numerous (https://nethackwiki.com/wiki/Dragon_scale_mail, https://nethackwiki.com/wiki/Cloak_of_protection, https://nethackwiki.com/wiki/Magic_cancellation, https://nethackwiki.com/wiki/Speed_boots)
-->

Weapons and armor are the bread and butter of combat. Your choice
of equipment determines how hard you hit, how well you dodge, and
what special resistances you carry. This section covers the
strategy of choosing equipment; the
[Weapons Tables](#weapons-tables) and [Armor Tables](#armor-tables)
appendices give the full stats for every item.

#### Armor and AC

Armor Class is what decides how often you get hit, and it's the
most important defensive number in the game. Each point you push
down means more monster swings whiff past you. AC starts at 10 and
drops as you add protection. Lower is better. At AC −10 or below,
you're quite difficult to damage with physical attacks; community consensus is that −20 is the practical target
for an ascension kit, with diminishing returns past −25. The
**cloak of displacement** should not be underrated: monsters waste
attacks on your phantom image, which complements low AC instead of
competing with it.

The key armor slots:

| Slot   | Primary pick                               | Specialty pick                        |
| ------ | ------------------------------------------ | ------------------------------------- |
| [Body](#body-armor-suits)   | Splint mail, banded mail                   | Dragon scale mail (two extrinsics)    |
| [Cloak](#cloaks)  | Cloak of protection                        | Cloak of magic resistance             |
| [Helmet](#helmets) | Helm of caution (early game)               | Helm of telepathy / helm of brilliance |
| [Gloves](#gloves) | Gauntlets of power                         | Gauntlets of dexterity                |
| [Boots](#boots)  | Speed boots                                | Water walking boots, levitation boots |
| [Shield](#shields) | Shield of reflection                       | Small shield (for spellcasters)       |

The **helm of caution** is new in 5.0: it grants
*warning*, the same intrinsic the ring provides, in the helmet
slot. Warning fills the screen with colored markers indicating
nearby threats by danger level (white for the least threat,
through red, with magenta for the worst) without you having to
see the monsters yet. It is the
ideal early-game helm slot: cheap (50 zm), light, and a real
edge against ambushes. Late game it competes with helm of
brilliance (Wizards) and helm of telepathy (everyone), but the
warning bonus stays useful all the way down.

**Dragon scale mail** is the endgame body armor of choice. **Gray**
grants magic resistance and is the most-wished color, **silver**
grants reflection, and other colors carry one or two intrinsics
each. See [Dragon Scale Mail](#dragon-scale-mail) below for the
full list and the forge recipe.

**Speed boots** are worth wishing for. Being faster than your
enemies means you get more turns — more chances to attack, cast
spells, or run away. Casters with surplus Pw (Wizard or Monk
late game, especially with the Eye of the Aethiopica) can lean
on **haste self** as a substitute and free the boots slot for
water walking or jumping. Haste self alone reaches *very fast*
just like the boots; maintenance costs about 10 Pw every 150
turns at Skilled.

**Cloak of magic resistance** provides magic resistance in the cloak
slot and frees up other slots for different resistances. However,
be aware that since 3.6, **magic cancellation (MC) values were
overhauled**: the cloak of magic resistance now provides only MC1,
not MC3. The **cloak of protection** is now the only single item
that provides MC3, which blocks 90% of monster special attacks (down
from 98% in older editions). A ring of protection now contributes
+1 MC, and the new amulet of guarding provides +2 MC, giving you
more ways to assemble full magic cancellation coverage.

For the AC, MC, weight, cost, and granted-power numbers on every
piece of armor in the game, see the
[Armor Tables](#armor-tables) appendix.

#### Weapons

Weapon choice depends heavily on your role and skill caps.

| Weapon         | Damage (sm/lg) | Notes                              |
| -------------- | -------------- | ---------------------------------- |
| [Long sword](#long-sword)     | d8 / d12       | Lawfuls can dip for Excalibur      |
| [Katana](#long-sword)         | d10 / d12      | Best base damage for a one-hander  |
| [Silver saber](#saber)   | d8 / d8        | +d20 vs silver-hating monsters     |
| [Crysknife](#knife)      | d10 / d10      | Excellent damage, fragile          |
| [Tsurugi](#two-handed-sword)        | d16 / d8+2d6   | Two-handed, bisects small monsters |
| [Runesword](#broadsword)      | d4 / d6+d4     | Chaotic weapon                     |
| [Battle-axe](#axe)     | d8+d4 / d6+2d4 | Two-handed, good damage            |
| [Rubber hose](#whip)    | d4 / d3        | No, seriously, don't use this      |

**Excalibur** (long sword dipped in a fountain while Lawful) is one
of the best weapons: +d5 to hit and +d10 damage, level drain resistance,
automatic searching. For Lawful characters, getting Excalibur early
is a priority.

**Silver saber** deserves special mention. Many endgame threats
(demons, undead, werecreatures) are vulnerable to silver. A silver
saber does an extra d20 damage against them, making it one of the
best late-game weapons.

**Your quest artifact** is often your primary weapon or at least
worth carrying for its properties. Check what your role's artifact
does.

For the full damage/weight/cost numbers on every weapon in the
game, see the [Weapons Tables](#weapons-tables) appendix.

<!-- audit
2026-05-19:
- Weapon enchant scrolls: no destruction risk at any +; above +9 just becomes probabilistic (read.c:1669-1671).
- Uncursed enchant weapon always adds +1 (read.c:1669-1671).
- Armor enchant destruction risk begins above +3; above +5 for "special" armor (elven, cornuthaum) (read.c:1179).
- BLS/curse status changes success rate only, not the destruction threshold (read.c:1179).
- Wearing dragon scales and reading a non-cursed scroll of enchant armor merges them into the corresponding scale mail; blessed scroll bumps spe and blesses the result; cursed reading skips the merge (read.c:1225-1252).
- Greasing armor: applying a can of grease (apply.c:2603-2645) sets obj->greased; deflects monster grab via mhitu.c:1063-1083.
-->
#### Enchantment

Weapons and armor can be enchanted using scrolls of enchant weapon
and enchant armor. Each scroll adds +1 (uncursed) or potentially
more (blessed). For **weapons** there's no destruction limit at
all: above +9 the scroll just becomes less likely to add a point,
but the weapon is never lost. **Armor** is different — above +3
each new scroll has a chance to destroy the item (above +5 for
"special" armor like elven pieces, or the Wizard's cornuthaum).
Blessed scrolls give more points per read but don't change the
destruction threshold; cursed scrolls can subtract enchantment
and shouldn't be used for enchanting at all.

#### Erosion and Proofing

Weapons and armor can be damaged by rust (iron items), fire
(organic items), and corrosion (copper items). A badly damaged
item provides less AC or damage.

To fix erosion, read a confused scroll of enchant weapon (for your
weapon) or confused scroll of enchant armor (for a random worn armor
piece). This erodeproofs the item permanently without changing its
enchantment. It also repairs any existing damage.

You can also slow erosion without magic. Coat an armor piece with
grease (apply a can of grease). The grease layer also makes the
piece slippery to monster steal and to grab attacks, but it wears
off after a few hits.

#### Dragon Scale Mail

Dragon scales are prized for their toughness and their magical
protections, and mail forged from those scales is among the best
body armor in the game.

Dragons don't always drop scales, and they never drop the mail
itself. A fresh kill yields scales about one time in three, and a
revived dragon only one time in twenty. **Scales** can be worn as
body armor just like mail and carry the color's full intrinsic
property (gray gives magic resistance, silver reflection, and so on,
identical to the mail). But the AC of scales is only +3 whereas
fully formed scale mail is +9. Same weight.

To upgrade scales into scale mail: wear the scales and read a
non-cursed scroll of enchant armor. The scales merge and harden
into the corresponding dragon scale mail at +0 (or higher if
blessed; a blessed scroll also blesses the result). A cursed
scroll just gives the usual bad enchant effect; no merge.

---

### Curses and How to Break Them
<!-- audit
2026-05-18:
- bones items are 80% cursed at pickup (bones.c:290)
- rings of teleport/polymorph and amulet of strangulation generate 90% cursed (mkobj.c:1063-1066, 1143-1147)
- cursed bag of holding doubles its contents' weight (mkobj.c:1950-1953)
- confused remove-curse uncurses 25/curses 25/no-op 50 per item (read.c:1556-1557, mkobj.c:1846-1852)
- blessed remove-curse hits all worn+carried; uncursed only worn (read.c:1524, 1549)
- temple priests do NOT reveal BUC for a fee; only Priest CLASS sees BUC free (priest.c:629-718 sets HClairvoyant + Protection, not bknown)
- shop price-id can infer BUC indirectly
- strategy aligned with NetHackWiki BUC, Scroll of remove curse, Potion of holy water: altar/pet test, blessed remove-curse hits entire inventory, holy water dip uncurses (https://nethackwiki.com/wiki/BUC, https://nethackwiki.com/wiki/Scroll_of_remove_curse, https://nethackwiki.com/wiki/Potion_of_holy_water)
- polymorph into a sliparm form drops body armor (cursed or not) into inventory (polyself.c:1198-1228)
-->


Sooner or later, you will put on something cursed. Maybe it's a
ring you didn't test. Maybe it's boots from a bones level. Maybe
a monster touched your inventory and you didn't notice. However it
happens, you're now wearing an item that refuses to come off, and
it's probably doing something terrible. The curse problem is one
of the dungeon's quieter ways to kill you.

#### How Items Get Cursed

- **Born that way.** Some items generate cursed most of the time
  (rings of teleportation, rings of polymorph, amulets of
  strangulation; anything the dungeon thinks is funny)
- **Bones inheritance.** Items on a bones level have an 80% chance
  of being cursed. That tempting armor on the dead adventurer's
  corpse? Probably trapped
- **Monster interference.** Certain monsters can curse items in
  your inventory
- **Confused remove curse.** Reading it confused has a chance of
  *cursing* items instead of uncursing them
- **Unholy water.** The evil twin of holy water

#### Effects of Cursed Items

- **Cursed armor and rings** bond to you and can't be removed: a
  cursed ring of teleportation means random teleports you can't
  stop, and a cursed pair of levitation boots means you can never
  touch the ground again
- **Cursed weapons** can't be unwielded. Hope you like that -3
  orcish dagger
- **Cursed potions and scrolls** often do the opposite of what
  you want, or a weakened version of the normal effect
- **Cursed tools** malfunction spectacularly. A cursed bag of
  holding *doubles* the weight of its contents instead of reducing
  it
- **Cursed food** is unpleasant but rarely fatal. Small mercies

#### Detecting Curses

Prevention is better than cure. Test items *before* wearing them:

- **Altar test.** Drop an item on an altar. A black flash means
  cursed. This is free, instant, and should become instinct
- **Pet test.** Your pet refuses to step on cursed items. Drop
  and observe
- **Scroll of identify.** Always reveals the full status
- **Formal price-ID via shop appraisal.** Shopkeepers don't reveal
  BUC directly, but the sell-back offer they make narrows the
  item to a few possibilities; combined with the altar test you
  can often pin it down

(Temple donation does *not* reveal BUC — that's a common spoiler
myth. Donating to a priest grants temporary clairvoyance and a
Protection bonus, but inventory BUC stays hidden.)

#### Removing Curses

When prevention fails, you have three remedies:

- **Scroll of remove curse.** Uncursed removes curses from worn
  and wielded items. Blessed uncurses your entire inventory — a
  real relief when the curse problem has gotten out of hand
- **Holy water.** Dip a cursed item in holy water and it becomes
  uncursed. Simple, reliable, and reason enough to stockpile holy
  water
- **Prayer.** A pleased god uncurses your worn items as a side
  benefit of answering prayer. Don't waste a prayer solely on this,
  but it's a nice bonus

Stuck in cursed body armor? Polymorphing into a form too small for
the suit drops it off into your inventory (curse and all), even
though it would normally refuse to come off. From there, dip in
holy water and re-wear. See [Polymorph as a Tool](#polymorph-as-a-tool).

Always carry holy water and a scroll of remove curse. The moment
you find yourself stuck with cursed levitation boots over a moat,
you'll understand why veterans never leave home without them.

---

## Part Five: Mastery

### Spellcasting
<!-- audit
2026-05-21:
- spellbook of type SPE_NOVEL appears as "paperback" until read (objects.h:1433-1436)
- reading the first novel in a game grants more_experienced(20, 0) and the ACH_NOVL achievement; u.uevent.read_tribute gates the once-per-game bonus (spell.c:513-535)
- 20 XP is the XL 1->2 threshold so a fresh character gains an experience level on the first paperback read
- novel title is rolled at game start per novelidx; titles come from a list of Terry Pratchett Discworld novels stored in the tribute file (do_name.c:297 noveltitle, files.c:3474 read_tribute)
2026-05-18:
- force bolt damage is 2d12; school skill does NOT scale damage (zap.c:2720-2724)
- chain lightning is level 4 NODIR, not level 7, not a bouncing ray (objects.h:1409-1411)
- failed spellbook read effects: teleport (lvl 1+), aggravate (lvl 2+), blindness (lvl 3+), take-gold (lvl 4+), confusion (lvl 5+), contact poison (lvl 6+), exploding rune (lvl 7+, 2d10+5 dmg, antimagic resists). Default rndcurse branch never fires: max spell level is 7 so rn2(lev) maxes at 6 (spell.c:130-185)
- failed read has a single 1/3 destruction chance (spell.c:612)
- spellbook fade ceiling is 4 successful reads: MAX_SPELL_STUDY=3 with `> MAX_SPELL_STUDY` (spell.c:400-418)
- no Pw drain from memorized spells exists; "spell maintenance" is fabricated (allmain.c moveloop has no per-spell Pw decrement; only cast_spell at spell.c:1245 decrements via SPELL_LEV_PW)
- drain_en only ever DECREASES Pw — no reflection+vortex max-Pw trick (trap.c:5202-5240 drain_en only subtracts from u.uen and decreases u.uenmax)
- blessed book bypasses the read-ability check entirely (auto-success)
- Pw cost per spell = 5 × level: SPELL_LEV_PW(spellev) (spell.c:1245)
- confused casts fail outright (spell.c:1372); charm monster has no confused-area mode
- Skilled+ casting acts like a blessed scroll (spell.c:1524-1525) or blessed potion (spell.c:1540-1541)
- Pw regen: (Wis + Int)/15 + 1; Wizards tick on factor 3 vs 4 (allmain.c:605-607)
- Valkyries restricted in divination, so reading scroll of identify is occasional at best (u_init.c:525-546)
- strategy aligned with NetHackWiki Spellbook, Spellcasting: Int + 4 + XL/2 − 2·level success formula, blessed book auto-success, Pw = 5 × level (https://nethackwiki.com/wiki/Spellbook, https://nethackwiki.com/wiki/Spellcasting)
-->

Magic in the Mazes is less "wave a wand and sparkles happen" and
more "laboriously study a crumbling book, hope it doesn't go off in
your face, and then set things on fire with your mind." Spells are
reusable abilities learned from spellbooks. Unlike scrolls (consumed
on use) or wands (limited charges), spells can be cast repeatedly as
long as you have mana (Pw, power) and the spell hasn't expired from
your increasingly overtaxed brain.

#### Learning Spells

Read a spellbook to learn the spell it contains. Reading takes
several turns and can fail. A failed reading can teleport you, take
your gold, blind, confuse, or poison you, blow up in your face for
HP damage, or randomly curse one of your items. A book that survives
failures can be retried.

The book's level decides which effects are on the table. A level-1
book can teleport you somewhere random when you fail to read it. A
level-2 book might aggravate nearby monsters instead. Misread a
level-3 book and it can blind you for 250 to 350 turns. A level-4
book can take all your gold, and level 5 can leave you confused
for 16 to 22 turns. Misread a level-6 book and you may be
contact-poisoned: gloves take corrosion damage, bare hands take
1 or 2 points of Strength plus 1d10 HP (1d6 with poison
resistance). And a level-7 book can have an exploding rune. Magic
resistance blocks the explosion; without it, you take 2d10+5
damage. Practical rule: don't read books you can't afford to fail.

The chance of successfully reading a spellbook depends on the
**spell level**, your **Intelligence**, and your **experience
level**. The exact formula is `Int + 4 + XL/2 − 2·level` versus a
roll of 1d20, so read 20 or more always succeeds, 10 is a coin
flip, and anything below that is dicey. Reading a level-7 spell at
Int 15, XL 2 gives a read score of 6: only a 30% chance of
success. Lenses add +2. A **blessed** spellbook bypasses the check
entirely and always succeeds. A **cursed** spellbook fails
automatically and applies one of the failure effects above.

In the table below, the *"Minimum Int + XL needed"* column means
the sum of your Intelligence and your experience level. With 18
Intelligence at level 14, your sum is 32, so you can reliably read
up to level 6 spells.

| Spell Level | Minimum Int + XL needed | Who can read it reliably     |
| ----------- | ----------------------- | ---------------------------- |
| 1           | ~10                     | Almost anyone, early game    |
| 2           | ~14                     | Most characters by mid-game  |
| 3           | ~18                     | Wizards easily, others with effort |
| 4           | ~22                     | Wizards with decent stats    |
| 5           | ~26                     | Wizards with boosted Int     |
| 6           | ~30                     | Wizards with serious investment |
| 7           | ~34                     | Only well-built Wizards      |

**A blessed book skips the difficulty check entirely and always
succeeds**, no matter what your Int and level are, which is one
reason to save holy water for your hardest unread spellbooks.

**Wizards** are the undisputed masters of magic: they learn faster,
fail less, and have the widest range of useful spells. A well-built
Wizard can eventually learn *every* spell in the game, which is the
closest the Mazes come to letting you cheat. **Monks** are the
surprising second. They have access to all seven spell schools too,
and their no-body-armor restriction actually helps casting because
body armor adds a failure penalty; the monk-favored robe grants
another bonus on top. Priests and Healers cast meaningfully in their
own schools. Other roles can manage the occasional spell with help.
A Valkyrie can sometimes read identify (level 3) if her Intelligence
is boosted by gain-ability potions, but non-spellcasters are usually
better off with scrolls. Tourists, Barbarians, and Cavemen should
probably stick to hitting things.

[]{#wizards-identify-books}
**Wizards identify books by training.** In 5.0, advancing
a spell school skill to each rank automatically reveals the appearances
of spellbooks in that school: unskilled unlocks level-1 appearances,
basic level-3, skilled level-5, expert level-7. A Wizard starts knowing
all level-1 appearances and level-3 in attack and enchantment, which
means they begin the game with a meaningful identification advantage in
their core schools.

Each spell stays in memory for about 20,000 turns, then fades and
must be relearned. The spell list (`+`) shows time-remaining. You
can also `a`pply a spellbook to check how worn it is: each
**successful** read counts toward a fixed total of four before the
book fades to blank paper. Failed reads don't add to that counter,
but each failure has its own 1-in-3 chance to destroy the book
outright. Carry important spellbooks with you if you plan to rely
on their spells in the late game.

**Paperbacks.** A spellbook that appears as a *paperback* is a
novel rather than a real spellbook. Read it: the first novel you
pick up in a game grants 20 XP, which is exactly enough to lift
a fresh character from experience level 1 to 2. (The 20 XP only
fires once; subsequent paperbacks just display a quote.) Each
paperback is a Terry Pratchett **Discworld** title, and reading
it opens a passage from the novel.

#### Key Spells

| Spell           | Level | Effect                                  |
| --------------- | ----- | --------------------------------------- |
| Force bolt      | 1     | 2d12 ranged hit; an Int/XL bonus adjusts by −3 to +3 |
| Healing         | 1     | Restore hit points                      |
| Detect monsters | 1     | Sense nearby monsters                   |
| Identify        | 3     | Identify items (saves scrolls)          |
| Remove curse    | 3     | Uncurse worn/wielded items              |
| Chain lightning | 2     | Shock that spreads from the caster in all directions, chaining to nearby monsters |
| Magic mapping   | 5     | Reveal the level (saves scrolls)        |
| Charm monster   | 5     | Tame nearby creatures in a 3×3 area; Skilled+ acts like a blessed scroll |
| Finger of death | 7     | Kill in a beam; MR resists              |

The other 34 spells, along with their schools, types, and
rank-gated upgrades, are in the [Spell Tables](#spell-tables)
appendix.

For Wizards, learning **identify** and **magic mapping** as spells
dramatically reduces your need for scrolls: it's like having
infinite scrolls, except they cost mana instead of inventory space.
**Finger of death** is the ultimate argument-ender. **Charm
monster** turns your enemies into your friends, which is even better
than killing them because friends carry things and absorb hits.

**Chain lightning** is the 5.0 room-clearer. At level 2 it's
within reach of any character who can cast at all. The spell
auto-fires in all eight directions without a target prompt, deals
2d6 per hit, and stops dead at any peaceful or tame monster — so
you can clear a hostile room without lighting up your pet or a
shopkeeper down the hall. Shock-resistant hostiles eat one hit,
then end that beam.

#### Mana Management

Your power (Pw) pool determines how many spells you can cast before
you need to sit in a corner and regenerate like a phone battery.
Casting a spell costs **5 Pw per spell level** (so finger of death
is 35 Pw). A failed cast still spends half. Power regenerates over
time, faster with higher Wisdom and Intelligence, faster still for
Wizards or with a regeneration source.

High-level spells cost serious power. Plan your casting and carry
backup wands and scrolls: a Wizard out of Pw is just a person in a
bathrobe holding a stick.

---

### Luck and Fortune
<!-- audit
2026-05-19:
- cursed luckstone holds NEGATIVE Luck in place, but positive Luck still decays toward baseline (timeout.c:616-619)
- any non-cursed luckstone (blessed or uncursed) gives +3 max-Luck cap (attrib.c:441-450)
- killing peaceful: -1 with 50% probability (mon.c:3665); -5 reserved for co-aligned unicorns (mon.c:3667)
- prayer is rejected on ANY negative Luck (pray.c:2155), not just <= -10
- no Sokoban-down-stairs Luck penalty exists
- thrown gem to cross-aligned unicorn: identified -3..+3 (dothrow.c:2334 rn2(7)-3); unidentified -1..+1 (dothrow.c:2349 rn2(3)-1)
- "ID gems for shopkeeper +1" is fabricated; shk.c has no such hook (shk.c contains no change_luck or adjalign call on GEM_CLASS sale)
- killing quest leader: -4 baseline, immediate change_luck(-20), u.ugangr += 7 (mon.c:3680, timeout.c:600)
- killing pet: -1 plus alignment -15 via adjalign (mon.c:3664, 3704)
- only mirror breaks for Luck -2 (uhitm.c:1133, dothrow.c:2496, dokick.c:445/1724); crystal balls/armor don't
- full-moon/Friday-the-13th baseline shift (timeout.c:595-598)
- carrying the Amulet or u.ugangr > 0 doubles drift rate (300 turns, timeout.c:607)
- Archeologists start with TOUCHSTONE knowledge only (u_init.c:50, 903); gems are NOT pre-identified
- strategy aligned with NetHackWiki Luck, Luckstone, Luck item: ±13 cap with non-cursed luckstone, drift toward 0 every 600 turns, cursed luckstone locks negative Luck (https://nethackwiki.com/wiki/Luck, https://nethackwiki.com/wiki/Luckstone, https://nethackwiki.com/wiki/Luck_item)
-->


The Mazes are rigged. Not unfairly (the dungeon doesn't *hate*
you), but there is a hidden number attached to your character that
quietly tilts every die roll, every prayer, every scroll, every
combat swing. It's called Luck, and it's one of the most important
stats you can't see.

Players who ignore Luck die to things that "shouldn't have happened."
Players who cultivate it find that the dungeon is mysteriously
generous. This is not a coincidence.

#### How Luck Works

Luck ranges from -13 to +13. It starts at 0, the universe's way of
saying "prove yourself." Left alone, luck drifts back toward zero
over time; the Mazes don't give anything for free.

**Luck timeout.** Every 600 turns, your luck moves one point toward
0. If you have +5 luck, it will drop to +4 after 600 turns, then
+3 after 1200, eventually reaching 0. Your good deeds are forgotten.
Your sins, alas, are also forgiven.

**Luckstone.** Carrying a luckstone in your open inventory
(not inside a container) freezes the timer. Your luck stays wherever
it is until something changes it. For this reason, getting the
luckstone from Mine's End early is recommended. It's a small gray stone that makes the universe remember you
fondly.

**Bless state matters.** Any **non-cursed** luckstone (blessed
*or* uncursed) freezes drift toward your baseline and adds **+3
to your effective Luck on most rolls**. A **cursed** luckstone is
dangerous: it subtracts 3 from your effective Luck and holds
*negative* Luck in place (preventing the usual drift back toward
zero from below). Always BUC-check a luckstone before carrying
it, and bless it on an altar if you can. (The +3 bonus comes
from `set_moreluck`; the curse doesn't speed positive Luck's
decay, but it locks bad Luck in.)

**The Heart of Ahriman, Tsurugi of Muramasa, and Orb of Fate all
count as luckstones.** Barbarian, Samurai, and Valkyrie quest
artifacts confer the same drift-freeze and bless-state bonus, so
those three roles get a "free luckstone" from their quest reward.
Carrying both a blessed luckstone *and* one of these artifacts
doesn't stack the +3 bonus (the bonus is binary, not additive), but
it does add an extra unit of "blessed" to the count if you somehow
end up with a cursed luckstone, partially offsetting it.

**Calendar Luck.** The drift target isn't always 0:

- On a **full moon** night, baseline Luck is +1: Luck drifts toward
  +1 instead of 0. If you started the session on a full moon, you
  have +1 Luck for free.
- On **Friday the 13th**, baseline Luck is −1. Avoid stair-up runs
  on this day if you can; your accumulated good Luck will sap toward
  −1 even if you've been virtuous.

(NetHack uses your computer's real date for this; set your clock
back if you've planned an ascension on the 13th and don't want the
penalty, though most players just embrace the theme.)

#### Gaining and Losing Luck

| Action                                              | Luck change          |
| --------------------------------------------------- | -------------------- |
| Throw identified real gem to co-aligned unicorn     | **+5**      |
| Throw named-but-unidentified real gem to co-aligned | +2          |
| Throw unknown real gem to co-aligned unicorn        | +1          |
| Throw fully-identified real gem to cross-aligned unicorn | −3 to +3 (random) |
| Throw unidentified real gem to cross-aligned unicorn | −1 to +1 (random)  |
| Sacrificing on your own altar (varies by corpse value) | typically +1 |
| Sitting on a throne (lucky outcome)                 | +1          |
| Breaking a Sokoban rule (squeeze, fracture, polymorph boulder, scroll of earth) | −1 each |
| Killing a peaceful creature                         | −1 (50% chance per kill) |
| Killing a same-alignment unicorn                    | −5          |
| Killing your quest leader                           | −20 immediate (floor at −10), +7 god-anger, plus permanent −4 to baseline luck |
| Killing your pet                                    | −1 plus −15 alignment |
| Cannibalism                                         | −2 to −5    |
| Breaking a mirror                                   | −2          |

Be virtuous and the numbers smile on you. Be a monster and they
frown. The Mazes have a moral compass, and it's embedded in the
math.

**Unicorn gem-throwing is the strongest active Luck source in the
game.** Throw a properly-identified real gem (not glass) at a unicorn
whose alignment matches yours and you gain +5 Luck immediately. The
unicorn turns peaceful, accepts the gift, and teleports away, and
will accept another later if you find it again. Identify your gems
*first* (touchstone or scroll of identify); the bonus drops from
+5 to +1 if you don't actually know what you're throwing. Glass
gems are harmless but yield nothing; throwing them is a safe way
to pacify an unwanted unicorn without spending real gems. Avoid
throwing real gems at cross-aligned unicorns: the result is a
random Luck change between -3 and +3 and is rarely worth the
gamble. Archeologists start with a **touchstone**, which lets
them verify whether a gem is real before throwing it at a
unicorn.

There is a ceiling on the luck you can obtain from any given kind of offering.
If your current luck score already exceeds the difficulty rating of the
monster you just sacrificed, you gain nothing. The altar accepts your
offering politely and gives you nothing in return, because the gods have
standards.

Before 5.0, players used to be able to sit at a co-aligned altar
with a pile of kobold corpses and grind luck to maximum. That no
longer works once your luck is already above modest levels. To
raise luck via sacrifice in the mid-to-late game, you need fresh
corpses of monsters whose difficulty exceeds your current luck
value. A luckstone, occasional mid-tier sacrifices, and care to
avoid killing peacefuls is the standard path to high luck.

#### Why Luck Matters

At Luck +5 (or higher, with a luckstone), life is *noticeably*
better:

- You hit more often in combat. Swings that would have missed
  connect instead.
- Your prayers are more likely to be answered. Your god likes
  lucky people. (Gods are fickle that way.)
- Scrolls of enchant weapon/armor succeed more often at high
  enchantment levels.
- Wands of wishing are more likely to work perfectly on wresting.
- Fountain wishes become slightly more likely.

At negative luck, all of these go wrong. Even one point of negative
Luck causes prayer to backfire. Instead of helping, your god
responds with punishment: a stat loss with a *"thou hast strayed
from the path"* sermon, a black glow that curses your gear, or in
the worst case bolts of damage. You'll miss attacks you should
have hit. Scrolls will backfire. The dungeon
becomes a place that is trying to kill you even harder than
usual, which is saying something.

The practical advice: get a luckstone early, sacrifice occasionally
to keep luck positive, and don't kill peacefuls. Treat the universe
well and it will return the favor, in the form of slightly better
random numbers, which in the Mazes is the closest thing to love.

---

### Enhancing Skills
<!-- audit
2026-05-18:
- skill ranks P_UNSKILLED through P_GRAND_MASTER; practice formula level²×20 (skills.h:92-106)
- cumulative practice thresholds: 20/80/180/320/500
- weapon slot costs 1/2/3 per rank; non-weapon costs 1/1/2/2/3
- two-weapon uses the WEAPON slot column (weapon.c:1141)
- bare-hand and martial-arts bonuses apply every hit (weapon.c:1611-1613)
- bare-hand 50% / martial-arts 75% rate is the practice-training check, not bonus gating (uhitm.c:847 `dmg = rnd(!martial_bonus() ? 2 : 4)`; uhitm.c:849 `train_weapon_skill = (dmg > 1)` — rnd(2)>1 is 1/2, rnd(4)>1 is 3/4)
- riding trains after 100 mounted squares (steed.c:393-396, u.urideturns >= 100)
- Knights start at Basic riding; target is Skilled (weapon.c:1787-1789)
- pickup/loot/dip/trap/engrave actions gated at Basic riding
- slot ceiling 32 for an XL-30 crowned hero: 2 starting + 29 level-ups + 1 crowning (u_init.c:884, pray.c:992-993)
- Ranger divination caps at Expert (u_init.c:461)
- Wizard restricted from long sword: no P_LONG_SWORD entry in Skill_W (u_init.c:548-569)
- spell schools start with a 20-use precredit at Basic
- Skilled cone-of-cold and fireball: cluster of 3×3 explosions (spell.c:1419-1452), not room-clearing
- Valkyrie 6+6+2 = 14 slot example math
- crown gives +1 slot
- strategy aligned with NetHackWiki Skill, Twoweapon: slot budget tied to XL + crowning, non-weapon skills cost half, restricted skills only unrestrict to Basic via artifact gift (https://nethackwiki.com/wiki/Skill, https://nethackwiki.com/wiki/Twoweapon)
2026-05-23:
- Wizard dagger Expert opening: Wizards are unrestricted in dagger (Skill_W u_init.c:548-569), cap at Expert; thrown daggers benefit from a class multishot bonus (dothrow.c:177-190); early Pw budget is tight at base regen (Wis+Int)/15+1 (allmain.c:605-607)
- six-slot Dagger Expert cost = 1+2+3 (weapon column, skills.h:92-106)
- citation: community Wizard opening guides on NetHackWiki Wizard strategy and Damerell, "How to play a Wizard" (https://nethackwiki.com/wiki/Wizard, https://www.steelypips.org/nethack/)
-->

Most adventurers discover the skill system the first time they
press `#enhance` and realize the broadsword they've been swinging
for several levels is finally ready to graduate from Basic to
Skilled. Weapons, fighting styles, and spell schools each track
their own proficiency, and you train them one slot at a time.

#### The Skill Ladder

Practice with a weapon improves how often you hit and how hard. The
game tracks this as a **skill rank**: more practice, higher rank,
more deadly swings. Most skills run **Unskilled → Basic → Skilled
→ Expert**. **Bare hands** and **martial arts** alone reach
**Master** and **Grand Master**. Each rank-up costs both
**practice** (uses of the skill) and **skill slots** (a finite
budget tied to your experience level).

| To reach     | Practice (cumulative) | Weapon slots | Non-weapon slots |
| ------------ | --------------------- | ------------ | ---------------- |
| Basic        | 20                    | 1            | 1                |
| Skilled      | 80                    | 2            | 1                |
| Expert       | 180                   | 3            | 2                |
| Master       | 320                   | —            | 2                |
| Grand Master | 500                   | —            | 3                |

Non-weapon skills — spell schools, riding, bare hands, martial
arts — cost roughly half as many slots as melee weapons, the
dungeon's quiet subsidy for magic. (Two-weapon uses the weapon
column despite the name.) You start with 2 slots, gain one per
experience level (29 more by XL 30), and one more if you are
crowned, so the absolute ceiling is **32 slots** for an XL-30
crowned hero. Lose an experience level and you lose a slot, which
can demote your most recent advancement.

Each role has a per-skill **cap** beyond which no amount of
training will help. A Wizard caps at Basic with a mace and is
restricted from long swords. Restricted skills don't appear on
`#enhance` and stay Unskilled, except for god-given artifact
weapons, which unrestrict the skill to Basic. The full role caps
appear in [Per-Role Skill Caps](#per-role-skill-caps) below.

#### Training a Skill

Practice accumulates through use:

- **Weapon skills** tick on every melee or thrown hit that does
  **more than 1 damage**. A pillow-soft punch for 1 point doesn't
  count. Spears, javelins, knives, daggers, and aklys train the
  same skill whether you stab with them or throw them.
- **Bare hands** counts **50%** of your hits; **martial arts**
  counts **75%**. The rank still applies on every hit; this just
  slows the climb.
- **Riding** earns one tick every **100 squares** ridden.
- **Spell schools** earn **N practice per successful cast of a
  level-N spell**. Every school has a level-1 option to grind.
  See the schools table below.

Skills your role starts at Basic come **pre-credited with 20
practice uses**, so you're already a quarter of the way to Skilled
before the first turn.

When you've earned enough practice, the game says **"You feel more
confident in your skills."** That's your cue to type `#enhance`.
If more advancements remain after you pick one, you'll see **"You
feel you could be more dangerous!"** — keep going.

#### What a Rank Buys You

For weapons and fighting styles, each rank shifts your to-hit and
damage bonuses by a flat amount (the values replace each other,
not stack):

| Rank         | Weapon  | Two-weapon | Riding | Bare hands | Martial arts |
| ------------ | ------- | ---------- | ------ | ---------- | ------------ |
| Unskilled    | −4 / −2 | −9 / −3    | −2 / 0 | +1 / 0     | +2 / +1      |
| Basic        | 0 / 0   | −7 / −1    | −1 / 0 | +1 / +1    | +3 / +3      |
| Skilled      | +2 / +1 | −5 / 0     | 0 / +1 | +2 / +1    | +4 / +4      |
| Expert       | +3 / +2 | −3 / +1    | 0 / +2 | +2 / +2    | +5 / +6      |
| Master       | —       | —          | —      | +3 / +2    | +6 / +7      |
| Grand Master | —       | —          | —      | +3 / +3    | +7 / +9      |

(Each cell is **to-hit / damage**.) Two-weapon penalties apply to
**each** of the two strikes. A Basic two-weaponer hits twice but
at −7 each, which is much worse than one solid swing. Bare hands
and martial arts bonuses apply on every hit; only the practice
counter is gated by the dmg>1 roll. The Expert weapon line
(+3 / +2) is why dedicating to a single weapon matters: that's
the difference between killing the monster and watching it shrug.

#### The Seven Spell Schools

Every spellbook belongs to one of seven schools, and your rank in
that school determines how reliably you can cast spells from it.
Higher rank also unlocks some spell upgrades. Cone of cold becomes
a cluster of 3×3 explosions at Skilled, identify IDs the whole
stack, haste self lasts longer, and so on.

| School      | Focus                                  | L1 grind        |
| ----------- | -------------------------------------- | --------------- |
| Attack      | Direct damage (force bolt, fireball)   | Force bolt      |
| Healing     | HP restore and cure status             | Healing         |
| Divination  | Sensing, identifying, mapping          | Light           |
| Enchantment | Buffs, debuffs, charm                  | Confuse monster |
| Cleric      | Divine protection and summoning        | Protection      |
| Escape      | Mobility, evasion, levitation          | Jumping         |
| Matter      | Manipulation, transmutation, polymorph | Knock           |

#### Per-Role Skill Caps
<!-- audit
2026-05-19:
- All 13 role skill tables sourced from u_init.c (Skill_A through Skill_W); skills not in def_skill are P_UNSKILLED-locked. (u_init.c:257-569 tables Skill_A/B/C/H/K/Mon/P/R/Ran/S/T/V/W; weapon.c:1738-1781 skill_init defaults all to P_ISRESTRICTED then walks the def_skill list)
- All 494 cells (27 weapons + 4 fighting styles + 7 spell schools × 13 roles) exact-match against u_init.c:257-572.
- Scimitar omitted: no role has it in 5.0 (merged into saber per skills.h header note).
- P_MARTIAL_ARTS appears only in Skill_Mon (P_GRAND_MASTER) and Skill_S (P_MASTER); Monks have P_BARE_HANDED_COMBAT restricted (they get martial arts instead).
- Wizard and Monk are the only roles with all 7 spell schools listed in their def_skill table (Skill_W u_init.c:562-568 has all 7 P_*_SPELL entries; Skill_Mon u_init.c:380-386 has all 7). Other roles list a subset (Priest at u_init.c:408-410 has only 3, Healer at u_init.c:342 has only 1, etc.).
-->

Three tables of fixed maxima follow: weapons, fighting styles,
and spell schools. Skills not listed for a role are
**restricted**: the rank is locked at Unskilled, with one
exception (a god-given artifact weapon unrestricts you to Basic
in its skill). Key: **B**=Basic, **S**=Skilled, **E**=Expert,
**M**=Master, **GM**=Grand Master, **—**=restricted.

A "—" doesn't mean the skill is unusable, just locked at
Unskilled forever. A Healer can still read a spellbook of force
bolt and try to cast it. A Wizard can still swing a long sword.
They'll just always pay the Unskilled penalty from the
[Skill Ladder](#the-skill-ladder) (−4/−2 for a weapon, −9/−3
per strike for two-weapon, the Unskilled cast-failure rate for
a spell school), with no path to improvement. Role abbreviations:
Arc=Archeologist, Bar=Barbarian, Cav=Caveman, Hea=Healer,
Kni=Knight, Mon=Monk, Pri=Priest, Rog=Rogue, Ran=Ranger,
Sam=Samurai, Tou=Tourist, Val=Valkyrie, Wiz=Wizard.

##### Weapon Skill Caps

::: dense-table

| Weapon           | Arc | Bar | Cav | Hea | Kni | Mon | Pri | Rog | Ran | Sam | Tou | Val | Wiz |
|------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| dagger           | B   | B   | B   | S   | B   | —   | —   | E   | E   | B   | E   | E   | E   |
| knife            | B   | —   | S   | E   | B   | —   | —   | E   | S   | S   | S   | —   | S   |
| axe              | —   | E   | S   | —   | S   | —   | —   | —   | S   | —   | B   | E   | S   |
| pick-axe         | E   | S   | B   | —   | B   | —   | —   | —   | B   | —   | B   | S   | —   |
| short sword      | B   | E   | —   | S   | S   | —   | —   | E   | B   | E   | E   | S   | B   |
| broadsword       | —   | S   | —   | —   | S   | —   | —   | S   | —   | S   | B   | S   | —   |
| long sword       | —   | S   | —   | —   | E   | —   | —   | S   | —   | E   | B   | E   | —   |
| two-handed sword | —   | E   | —   | —   | S   | —   | —   | B   | —   | E   | B   | E   | —   |
| saber            | E   | S   | —   | B   | S   | —   | —   | S   | —   | B   | S   | B   | —   |
| club             | S   | S   | E   | S   | B   | —   | E   | S   | —   | —   | —   | —   | S   |
| mace             | —   | S   | E   | B   | S   | —   | E   | S   | —   | —   | B   | —   | B   |
| morning star     | —   | S   | B   | —   | S   | —   | E   | B   | B   | —   | B   | —   | —   |
| flail            | —   | B   | S   | —   | B   | —   | E   | B   | S   | S   | B   | —   | —   |
| hammer           | —   | E   | S   | —   | B   | —   | E   | B   | B   | —   | B   | E   | —   |
| quarterstaff     | S   | B   | E   | E   | —   | B   | E   | —   | B   | B   | B   | B   | E   |
| polearms         | —   | —   | S   | B   | S   | —   | S   | B   | S   | S   | B   | S   | S   |
| spear            | —   | S   | E   | B   | S   | B   | S   | B   | E   | S   | B   | E   | B   |
| trident          | —   | S   | S   | B   | B   | —   | S   | —   | B   | —   | B   | B   | B   |
| lance            | —   | —   | —   | —   | E   | —   | B   | —   | —   | S   | B   | S   | —   |
| bow              | —   | B   | S   | —   | B   | —   | B   | —   | E   | E   | B   | —   | —   |
| sling            | S   | —   | E   | S   | —   | —   | B   | —   | E   | —   | B   | B   | S   |
| crossbow         | —   | —   | —   | —   | S   | B   | B   | E   | E   | —   | B   | —   | —   |
| dart             | B   | —   | —   | E   | —   | —   | B   | E   | E   | —   | E   | —   | E   |
| shuriken         | —   | —   | —   | S   | —   | B   | B   | S   | S   | E   | B   | —   | B   |
| boomerang        | E   | —   | E   | —   | —   | —   | B   | —   | E   | —   | B   | —   | —   |
| whip             | E   | —   | —   | —   | —   | —   | —   | —   | B   | —   | B   | —   | —   |
| unicorn horn     | S   | —   | B   | E   | —   | —   | S   | —   | —   | —   | S   | —   | —   |

:::

Scimitar was merged into saber in 5.0; both refer to the same skill
now.

##### Fighting Style Caps

::: dense-table

| Style        | Arc | Bar | Cav | Hea | Kni | Mon | Pri | Rog | Ran | Sam | Tou | Val | Wiz |
|--------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| bare hands   | E   | M   | M   | B   | E   | —   | B   | E   | B   | —   | S   | E   | B   |
| two-weapon   | B   | B   | —   | —   | S   | —   | —   | E   | —   | E   | S   | S   | —   |
| riding       | B   | B   | —   | —   | E   | —   | —   | B   | B   | S   | B   | S   | B   |
| martial arts | —   | —   | —   | —   | —   | GM  | —   | —   | —   | M   | —   | —   | —   |

:::

Only Monks and Samurai have martial arts at all, and only Monks
reach Grand Master.

##### Spell School Caps

::: dense-table

| School      | Arc | Bar | Cav | Hea | Kni | Mon | Pri | Rog | Ran | Sam | Tou | Val | Wiz |
|-------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Attack      | B   | B   | B   | —   | S   | B   | —   | —   | —   | B   | —   | B   | E   |
| Healing     | B   | —   | —   | E   | S   | E   | E   | —   | B   | —   | —   | —   | S   |
| Divination  | E   | —   | —   | —   | —   | B   | E   | S   | E   | B   | B   | —   | E   |
| Enchantment | —   | —   | —   | —   | —   | B   | —   | —   | —   | —   | B   | —   | S   |
| Cleric      | —   | —   | —   | —   | S   | S   | E   | —   | —   | S   | —   | —   | S   |
| Escape      | —   | B   | —   | —   | —   | S   | —   | S   | B   | —   | S   | B   | E   |
| Matter      | B   | —   | S   | —   | —   | B   | —   | S   | —   | —   | —   | —   | E   |

:::

Healers cap at Expert in healing but are restricted from every
other school — the only role with this kind of single-school
specialization. Wizards and Monks are the only roles with access
to all seven schools, though only Wizards can push four of them
to Expert; Monks reach Expert only in healing. Barbarians and
Valkyries cap at Basic in their two available schools (attack and
escape) and are restricted from the other five.

#### Spending Slots Wisely

Thirty slots sounds like plenty until you start counting. Expert
in a single weapon costs **6 slots** (1+2+3) by itself. A
Valkyrie aiming for Expert long sword, Expert two-weapon, and
Skilled riding is fourteen slots deep before any spell school.

A few principles:

- **Don't enhance reflexively.** Slots are spent permanently
  (short of losing experience). If you're not committed to a
  weapon, hold the slot until you are.
- **Cap-aware investment.** Pushing a skill to its role cap is
  fine: the menu just stops offering further advances. You can't
  waste enhancements past the cap because the option never
  appears.
- **Wizards get two benefits from spell schools.** Each rank-up
  improves casting success *and* reveals more spellbook
  appearances in that school (the [identification
  payoff](#wizards-identify-books) covered in the Spellcasting
  chapter). Schools containing your unidentified books deserve
  priority. This double benefit is Wizard-only; other roles only
  get the casting-success benefit.
- **Wizards: daggers before schools.** A common opening pushes
  **Dagger to Expert** (six slots) before serious investment in
  spell schools. Thrown daggers carry the early game while Pw is
  scarce, and school ranks then come online to upgrade the late
  game without leaving the early game starving.
- **Riding is a skill.** Without **Basic riding** you can't
  pick up items, loot, dip, set or disarm traps, or engrave on
  the floor while mounted. Knights start at Basic. Pushing to
  Skilled erases the −1 to-hit penalty in the saddle and adds
  +1 damage.
- **Bare hands and martial arts are the domain of Monks.** Grand Master
  needs **9 cumulative non-weapon slots**, which Monks reach
  naturally. Anyone else dabbling in unarmed combat should plan
  to stop at Basic.

A few spells get sharper at Skilled. Cone of cold and fireball
become a cluster of 3×3 **explosions** you can place at range.
Identify, remove curse, haste self, detect monsters, and several
others gain the blessed-scroll effect.

---

### Wishes and Wishing

There is a moment in every successful game where you're asked,
"For what do you wish?" It's the best question in all of gaming.
Don't panic. Don't mistype. And for the love of all that is holy,
don't wish for a +3 blessed cockatrice. (Actually, that *would*
be something. But no.)

Wishes are rare, powerful, and the difference between a character
who ascends and one who dies memorably on the Plane of Fire.

#### Sources of Wishes

The Mazes are stingy, but there are more wish sources than most
travelers realize:

- **Wand of wishing:** found in the Castle treasure room
  (see [Key Wands](#key-wands) for the 5.0 charge mechanics). The
  Castle chest also contains a potion of gain level, because the
  Mazes occasionally feel generous.
<!-- src/sit.c special_throne_effect(): cases 1-4 (of 13) = wish,
     throne only vanishes on wish, so guaranteed eventual wish. -->
- **Vlad's throne:** A special throne that grants a guaranteed
  wish if you keep sitting. Four of thirteen outcomes are a wish
  (which destroys the throne); the other nine are painful but
  the throne survives, so persistence pays off.
<!-- src/allmain.c: u.uhave.amulet && !u.uevent.amulet_wish -->
- **The Amulet of Yendor:** Grants a wish when you first pick
  it up. A reward for reaching the bottom of the dungeon. You can
  decline this wish if your kit is already complete; some
  minimalist ascenders skip it entirely on principle.
- **Magic lamp:** Rubbing a blessed lamp summons the djinni 1-in-3
  times; *if* it appears, it grants a wish 80% of the time, so
  roughly 27% wish per rub. Keep rubbing. Either a magic lamp or a
  magic marker is guaranteed in Orcus Town.
- **Fountain:** roughly 1 in 30 quaffs summons a water demon, and
  *that* demon grants a wish only about 1-in-5 times on shallow
  floors (less on deeper ones), so a true wish chance closer to
  1 in 150 per quaff. Far more likely to produce snakes, nymphs,
  curses, or vomiting.
- **Throne:** Very rare chance of a wish when sitting. Also a very
  real chance of everything going wrong.
- **Djinni from smoky potion:** Rare (1 in 13 base probability),
  and even then only 20% wish chance (80% if blessed). But when
  it works, you feel like a genius.

In practice, the number of wishes a run produces varies widely. A
sensible budget if you take each guaranteed source once is about
four (Castle wand, Vlad's throne, Amulet pickup, one magic lamp).
Anything beyond that is luck (extra lamps, fountain demons,
recharge chains) or commitment. Don't waste any of them on food.

#### What to Wish For

Generations of adventurers have argued about optimal wish order.
Here's the conventional wisdom, battle-tested by thousands of
ascensions:

1. **Gray dragon scale mail** (magic resistance + AC; magic resistance
   is the most important protection in the game, so this is highly recommended).
2. **Silver dragon scale mail** (reflection + AC, the second pillar
   of not dying to wands).
3. **Speed boots** (being fast gives you more actions per turn, excellent
   for both offense and escape).
4. **Gauntlets of power** (STR 25 if your role benefits;
   most roles benefit from punching harder).
5. **Amulet of life saving** (insurance for the endgame, when
   overconfidence kills more adventurers than monsters do).
6. **A specific artifact** (Grayswandir is a common target for the
   silver damage against everything in Gehennom).

Don't wish for consumables (scrolls, potions) unless you're in
dire straits. Items you can find through normal play aren't worth
a wish. A wish is for things that change the fundamental equation
of your survival.

#### Wish Syntax
<!-- audit
2026-05-18:
- bare "gray dragon scale mail" keeps random spe and rolls BUC via blessorcurse(otmp,10): ~5% blessed / ~5% cursed / ~90% uncursed (objnam.c:5094-5096, 5258-5268)
- artifact wishes are probabilistic: oartifact && rn2(nartifact_exist())>1 (objnam.c:5374), scaled by TOTAL existing artifacts including bones
- u.uconduct.wisharti increments whether the wish is granted or denied (objnam.c:5364)
- only quest artifacts are absolutely blocked: restrict_name SPFX_NOGEN|SPFX_RESTR check (artifact.c:618)
- silent substitutes: Amulet of Yendor, Bell of Opening, Book of the Dead, Candelabrum, magic lamp → oil lamp (objnam.c:5003-5006)
- all gloves give +1 AC (objects.h:686-697); gauntlets of power give STR 25, not bonus AC (attrib.c:1214)
- Vlad's throne wish rate is 4/13 per effective sit (sit.c:241-256)
- magic lamp ≈27% wish-blessed: 1/3 djinni × 4/5 wish (apply.c:1817, potion.c:2833-2845)
- fountain water-demon wish (fountain.c:78, 314); Amulet-of-Yendor pickup wish (allmain.c:446-451)
- strategy aligned with NetHackWiki Wish, Gray dragon scale mail, Speed boots, Magic lamp: GDSM/SDSM as top wishes, speed boots and gauntlets of power as standard follow-ups, bare wishes risk cursed/random spe (https://nethackwiki.com/wiki/Wish, https://nethackwiki.com/wiki/Gray_dragon_scale_mail, https://nethackwiki.com/wiki/Speed_boots, https://nethackwiki.com/wiki/Magic_lamp)
-->

When the game asks "For what do you wish?", be specific. This is
not the time for ambiguity:

- "blessed greased fixed +3 gray dragon scale mail" is the
  veteran's incantation. `blessed` because BUC defaults to random,
  `greased` deflects nymph theft and Rider grabs, `fixed` (or
  `erodeproof`) locks erosion, `+3` is the safe enchantment ceiling.
- "gray dragon scale mail" alone lets the dice pick blessed/
  cursed and enchantment — a bare wish can roll cursed. You
  had *one* wish; spell out the BUC and the plus. And don't
  forget "scale" — "gray dragon mail" hands you a scroll of
  mail instead.
- Artifact wishes get *harder* as artifacts accumulate. The
  denial roll scales with the total artifacts in the world
  (yours, generated, even bones-file ones), and your
  artifact-wish counter ticks whether or not the artifact
  actually appears. Quest artifacts are absolutely blocked.
- A few targets are silently nerfed into mundane substitutes:
  the **Amulet of Yendor** becomes a fake amulet, the **Bell
  of Opening** a plain bell, the **Book of the Dead** blank
  paper, the **Candelabrum** a tallow candle, and — relevant
  after all that lamp-rubbing — a wish for a **magic lamp**
  hands you an ordinary oil lamp.

---

### Artifacts
<!-- audit
2026-05-19:
- Magicbane effects (stun, magic resistance) require wielding, NOT just carrying (artilist.h:145-147, NO_CARY).
- All four Magicbane code paths gate on wielding (wield.c:1036, trap.c:2360, mplayer.c:273, sit.c:576).
- Master Key: Rogue needs !cursed; non-rogues need BLESSED (artifact.c:2778-2784).
- Eyes of the Overworld: magic resistance requires worn, NOT carried (artilist.h:262, NO_CARY; artifact.c:731).
- Tsurugi grants luck + protection, NOT magic resistance (artilist.h:285-289).
- Sceptre of Might (Lawful) does double damage vs chaotic, NEUTRAL, and unaligned (artifact.c:1031-1034).
- Mjollnir reliable return is Valkyrie-only (artilist.h:97-108).
- Frost Brand and Fire Brand have SNOWSTORM / FIRESTORM invokes (artilist.h:150, 154).
- Frost Brand grants cold resistance (DFNS=COLD); Fire Brand grants fire resistance (DFNS=FIRE) (artifact.c:730-736).
- Stormbringer is SPFX_INTEL: cross-alignment touch deals 4d10, not 4d4. (artilist.h:93-96 Stormbringer has SPFX_INTEL; artifact.c:953 `dmg = d((Antimagic ? 2 : 4), (self_willed ? 10 : 4))`)
- Grimtooth +d6 damage bonus applies to ALL targets, not just elves (artifact.c:1099-1102).
- Mitre of Holiness gives NO damage bonus vs undead; ATTK is NO_ATTK (artifact.c:1095-1098).
- M2_UNDEAD flag only enables shade_glare on weapons, not worn helms (artifact.c:554-571).
- Eye of the Aethiopica magic resistance requires worn, NOT carried (artilist.h:303-305, NO_CARY).
- Eye of the Aethiopica carry effects: energy regen, half spell damage (cspfx EREGEN, HSPDAM).
- strategy aligned with NetHackWiki Artifact weapon, Grayswandir, Magicbane, Mjollnir: Grayswandir/Magicbane/Mjollnir as the top wish artifacts; alignment-mismatched artifacts blast on touch (https://nethackwiki.com/wiki/Artifact_weapon, https://nethackwiki.com/wiki/Grayswandir, https://nethackwiki.com/wiki/Magicbane, https://nethackwiki.com/wiki/Mjollnir)
-->


Scattered throughout the Mazes are items of legend: named weapons,
amulets, and tools that carry powers no ordinary gear can match. Each
artifact exists only once per game, so when you find one, you're
holding a genuine one-of-a-kind. Here's how they come into your
hands:

- **Fountain dipping** (Excalibur, for Lawful characters).
- **Sacrifice** on an altar (your god may gift you an aligned artifact).
- **Quest completion** (each role's unique quest artifact).
- **Wishing** (you can wish for most artifacts, but they resist
  if they don't match your alignment).
- **Random generation** (rare, but weapons have a small chance of
  being generated as an artifact).

#### Alignment and Blasting

Each artifact has an alignment. If you try to handle an artifact
that doesn't match your alignment:

- **Intelligent artifacts** (most quest artifacts and certain
  alignment-restricted artifacts): 4d10 damage (or 2d10 with magic
  resistance) and the item evades your grasp. You cannot wield these.
- **Other misaligned artifacts**: 4d4 damage on first touch (2d4 with
  magic resistance), 1/4 chance of being blasted on each subsequent
  touch.

#### Wishable / random artifacts

These are the artifacts you can find, get from a sacrifice gift,
fountain-dip up (Excalibur), or wish for. Bonus damage is rolled fresh
on each hit (e.g. `+d10` means roll 1d10). The "extra" column is the
damage rolled *on top of* the base weapon's own damage. A weapon
listed as "×2 vs X" rolls its base damage *twice* against any member
of that monster class.

| Artifact               | Align    | Weapon            | Hit    | Extra damage           | Notable                                                |
|------------------------|----------|-------------------|--------|------------------------|--------------------------------------------------------|
| Excalibur         | Lawful   | long sword        | +d5    | +d10 physical               | drain resistance, automatic searching                  |
| Grayswandir       | Lawful   | silver saber      | +d5    | (base only)                 | half physical damage received, hallucination res.      |
| Mjollnir          | Neutral  | war hammer        | +d5    | +d24 shock                  | returns when thrown if STR 25                          |
| Magicbane         | Neutral  | athame            | +d3    | +d4 magic (stun)            | magic resistance and curse protection while *wielded*  |
| Stormbringer      | Chaotic  | runesword         | +d5    | +d2 drain life              | drains a level (you gain it); attacks peacefuls        |
| Vorpal Blade      | any      | long sword        | +d5    | +d1 physical                | chance to behead on hit                                |
| Frost Brand       | any      | long sword        | +d5    | (base only) cold            | cold resistance while wielded                          |
| Fire Brand        | any      | long sword        | +d5    | (base only) fire            | fire resistance while wielded                          |
| Sunsword          | Lawful   | long sword        | +d5    | (base only); ×2 vs undead   | wielded light; `#invoke` fires a blinding ray any direction (camera-style; works on any monster) |
| Snickersnee       | Lawful   | katana            | —      | +d8 physical                | one free reach attack per turn (the "Shkinng!" hit) at polearm distance, on top of normal katana melee |
| Cleaver           | Neutral  | battle-axe        | +d3    | +d6 physical                | one-handed wield → strikes target *and* both flanks    |
| Demonbane         | Lawful   | silver mace       | +d5    | (base only); ×2 vs demons   | banishes demons; Priest's first sacrifice gift         |
| Sting             | Chaotic  | elven dagger      | +d5    | (base only); ×2 vs orcs     | warns of orcs (the dagger glows blue)                  |
| Orcrist           | Chaotic  | elven broadsword  | +d5    | (base only); ×2 vs orcs     | warns of orcs                                          |
| Grimtooth         | Chaotic  | orcish dagger     | +d2    | +d6 physical (any target)   | warns of elves; defends vs poison                      |
| Dragonbane        | any      | broadsword        | +d5    | (base only); ×2 vs dragons  | reflection while wielded                               |
| Werebane          | any      | silver saber      | +d5    | (base only); ×2 vs were-    | defends against lycanthropy                            |
| Giantslayer       | Neutral  | long sword        | +d5    | (base only); ×2 vs giants   | —                                                      |
| Ogresmasher       | any      | war hammer        | +d5    | (base only); ×2 vs ogres    | —                                                      |
| Trollsbane        | any      | morning star      | +d5    | (base only); ×2 vs trolls   | regeneration while wielded                             |

Not every entry is equally desirable. **Grayswandir** and **Magicbane**
are the artifacts most players try to wish for first; **Mjollnir** is
the Valkyrie's archetypal wish; **Excalibur** is usually fountain-dipped
rather than wished. **Frost Brand**, **Vorpal Blade**, and **Stormbringer**
are common second wishes. **Snickersnee** and **Sunsword** were
historically considered flavour pieces, but their 5.0 effects (free
reach attack per turn; on-demand camera-style blind) have moved them
into the "worth wishing for, role permitting" tier. The remaining
entries (the bane weapons, Fire Brand, Cleaver) are usually accepted
as sacrifice gifts rather than spent wishes on.

**Excalibur** is the go-to weapon for Lawful characters; the drain
resistance alone is worth carrying it, even after you have a stronger
weapon. Knights start aligned to it and have unique 1-in-6 fountain-dip
odds; every other Lawful role faces 1-in-30.

**Grayswandir** is wishable and arguably the game's best melee
weapon. It's silver (extra damage to many monsters), halves
incoming physical damage, and grants hallucination resistance.

**Mjollnir** is the Valkyrie's signature throw-and-return weapon —
and only Valkyries get the reliable 99% catch-back. Other roles can
wield it for melee but won't reliably catch it on the return throw.
It needs Strength 25 to wield in either case (gauntlets of power
or rings of gain strength get you there). Its +d24 shock damage
is brutal against anything not shock-resistant.

**Magicbane** is the Wizard's go-to athame. Its stun damage, curse
protection, and magic resistance all require it to be **wielded**,
not just carried. Often the first gift from a Neutral sacrifice. One nuance for two-weapon Wizards: the curse
protection only applies while Magicbane is the *primary* wielded
weapon. If you stash Magicbane in the off-hand to swing a heavier
blade, you've also turned off its anti-curse aura.

**Stormbringer** is dangerous to use because it attacks peaceful
monsters automatically, which can cause alignment problems. But
each hit drains a level from the target and gives it to you, which
is huge in the early-to-mid game. Stormbringer is also
*intelligent*: a Lawful or Neutral wielder who touches it without
permission takes the heavier 4d10 magical-blast damage rather than
the 4d4 dealt by ordinary cross-alignment artifacts.

**Cleaver** is the Barbarian quest artifact. When wielded one-handed
(not two-weaponing), every swing strikes the primary target *and* one
square on each side of it: three monsters per attack when packed in
a corridor mouth or against a diagonal pair. The two-weapon penalty
suppresses the spin, so most Barbarians keep Cleaver as their primary
and a shield in the off slot.

**Frost Brand** and **Fire Brand** each have an `#invoke` power
the wishable table doesn't capture: Frost Brand summons a
snowstorm around you (cold damage to nearby squares), Fire Brand
summons a firestorm. Either one clears the room around you when
you're cornered.

**Snickersnee** got a major buff in 5.0: once per turn you can
`#apply` it for a free reach attack at a target up to two squares
away — a real free action that *doesn't* end your turn, leaving
you a normal melee swing on top. The free hit is announced by a
distinctive "Shkinng!" The combined output (one ranged + one
melee per turn) makes Snickersnee a contender for best Samurai
weapon in the game, not just a flavor piece. (Regular polearm
reach attacks via `#apply` end your turn; Snickersnee's is the
unique free version.)

**Sunsword** is the Lawful long sword that wants to be a tool. Wielded,
it lights its current radius (handy in caves and the Mines without
costing an oil lamp). `#invoke` it for a directed *blinding ray*,
mechanically a Camera flash in any direction (not limited to undead).
It costs 5×spell-level Pw to invoke, so save it for the fights that
demand it: Riders, mind flayers, the Wizard of Yendor. Invoking up
or down lights the room; invoking at yourself self-blinds you.

**Bane weapons** (Sunsword, Demonbane, Sting, Orcrist, Grimtooth,
Dragonbane, Werebane, Giantslayer, Ogresmasher, Trollsbane) deal
double base damage against their target class. Most are disappointing
as a primary weapon, but the defensive riders are often the real
reason to swap one in: Trollsbane regenerates while wielded
(genuinely useful for an early character holding the line),
Dragonbane reflects, Werebane neutralizes lycanthropy, Grimtooth
defends against poison.

#### Quest artifacts

Each role has exactly one quest artifact, awarded for completing the
role's quest. They are intelligent: only the rightful owner can
safely wield them; anyone else gets blasted. Most of the non-weapon
ones grant magic resistance just by sitting in your inventory, so
roles whose quest artifact is a passive object still benefit from
carrying it.

**A wishing quirk to know about.** The wish system blocks *your
own* role's quest artifact (you have to earn it the hard way), but
it doesn't block *other roles'* quest artifacts. A neutral
character can wish for any neutral quest artifact, a lawful one for
any lawful quest artifact, and so on. The alignment-blast rule
still applies if you actually wield or wear a misaligned one, but
carry bonuses (MR, drain resistance, regeneration, half spell
damage, energy regeneration, etc.) work for anyone. A neutral Monk
can wish for the Healer's *Staff of Aesculapius* for the
drain-life-on-hit and drain-resistance carry bonus, or the Wizard's
*Eye of the Aethiopica* for MR + half-spell-damage + energy regen,
even though those quests are closed to the Monk. Wishes for
artifacts of all kinds also have an increasing fizzle chance as
more artifacts already exist in the game.

`#invoke` (default `^A`) activates each artifact's special power; the
cost is some energy plus a wear-out interval before it can be used
again.

::: dense-table

| Role | Artifact                            | Form           | Wear/wield                          | Carry                    | `#invoke`           |
|------|------------------------------------------|----------------|-----------------------------------|--------------------------|---------------------|
| Arc  | The Orb of Detection                    | crystal ball | —                                     | MR, ESP, ½ spell dmg     | invisibility        |
| Bar  | The Heart of Ahriman                    | luckstone    | ×2 dmg as a projectile                | stealth, +luck           | levitation          |
| Cav  | The Sceptre of Might                    | mace         | +d5 hit; ×2 vs non-lawful             | magic resistance         | conflict            |
| Hea  | The Staff of Aesculapius                | quarterstaff | drain-life on hit                     | drain res., regen        | full heal + cure    |
| Kni  | The Magic Mirror of Merlin              | mirror       | (speaks to you)                       | MR, ESP                  | —                   |
| Mon  | The Eyes of the Overworld               | lenses       | astral vision, magic res. (when worn) | —                        | enlightenment       |
| Pri  | The Mitre of Holiness                   | helm         | +1 prot. (brilliance base)            | fire res.                | energy boost        |
| Ran  | The Longbow of Diana                    | bow          | +d5 hit; reflection                   | ESP                      | conjure arrows      |
| Rog  | The Master Key of Thievery              | skeleton key | —                                     | warn, t-ctrl, ½ phys     | guaranteed untrap   |
| Sam  | The Tsurugi of Muramasa                 | tsurugi      | +d8 phys; chance to behead            | +luck, +1 prot.          | —                   |
| Tou  | Platinum Yendorian Express Card         | credit card  | —                                     | MR, ESP, ½ spell dmg     | charge an item      |
| Val  | The Orb of Fate                         | crystal ball | —                                     | +luck, warn, ½ all dmg   | levitate / teleport |
| Wiz  | The Eye of the Aethiopica               | amulet       | —                                     | MR, ½ spell, +energy     | create portal       |

:::

**The Orb of Detection** (Archeologist): a crystal ball that grants
ESP and magic resistance just by being carried. `#invoke` toggles
invisibility. Archeologists are already exceptional at stealth, and
this turns them into a ghost.

**The Heart of Ahriman** (Barbarian): a luckstone that doubles as a
+1 luck talisman with stealth. Critically, it counts as a luckstone
for *all* the luckstone mechanics (mine's-end protection, gem-throw
luck math, luck cap +13 instead of +10). It's also a projectile
weapon: Barbarians can throw it for double damage and pick it back
up. `#invoke` is levitation.

**The Sceptre of Might** (Caveman): mace base, +d5 to-hit, double
damage against any monster whose alignment differs from the
artifact's (the Sceptre itself is Lawful, so it deals doubled
damage against chaotic, neutral, *and* unaligned monsters — most
of the dungeon's hostiles once you reach Gehennom). It also grants
magic resistance while *wielded*. `#invoke` casts conflict
(monsters fight each other) at a steep energy cost.

**The Staff of Aesculapius** (Healer): the Healer's salvation. Each
hit drains life (one of only three drain-life weapons; the others
are Stormbringer and the rider Death) and gives you regeneration
plus drain resistance just by carrying it. `#invoke` heals fully and
cures nearly every bad status. Few artifacts change a role's late
game as much as this one.

**The Magic Mirror of Merlin** (Knight): grants ESP and magic
resistance, and occasionally *speaks*, dropping hints. Knights
already have Excalibur for combat, so the Mirror is pure passive
utility.

**The Eyes of the Overworld** (Monk): lenses that, when worn, give
astral vision (see invisible, see through walls, spot secret doors)
**and** magic resistance. Both effects require them to be worn —
carrying them in inventory does nothing. `#invoke` enlightens you.
For a Monk who can't safely wear body armor, a powerful passive on
a slot they can use.

**The Mitre of Holiness** (Priest): a helm of brilliance with the
usual brilliance bonus to intelligence and wisdom (so spell-cast
more reliably), plus fire resistance while carried, plus a free
`-1` to AC. `#invoke` for an energy boost, useful for spell-heavy
Priests. Note: despite what older spoilers say, the Mitre does
**not** deal bonus damage against undead (the artifact has no
melee attack to carry the bonus), and it does not grant drain
resistance.

**The Longbow of Diana** (Ranger): a real artifact bow with +d5 to hit
plus reflection while wielded, ESP while carried. `#invoke` conjures
free arrows out of thin air. Combined with the Ranger's ranged
specialization this is the role's centerpiece.

**The Master Key of Thievery** (Rogue): a carry package of warning,
teleport control, half physical damage taken, and `#invoke` instantly
untraps a nearby trap. The unlocking
bonus depends on alignment: a Rogue gets it from any non-cursed
Key; everyone else needs a **blessed** Key. With those preconditions
met, `#untrap` also gains a perfect-detection bonus on doors and
chests.

**The Tsurugi of Muramasa** (Samurai): a katana-grade two-handed
sword with +d8 damage *and* a behead chance (like Vorpal Blade)
*and* a +1 protection bonus, and it acts as a luckstone. Note
that Tsurugi does **not** grant magic resistance, despite the
weapon's reputation. One of the strongest artifacts in the game,
the Samurai's reward for a hard quest.

**The Platinum Yendorian Express Card** (Tourist): the Tourist's
get-out-of-jail card. Carrying it grants ESP, magic resistance, and
half spell damage; `#invoke` charges an item (a wand, ring, or marker),
which in the Tourist's hands is roughly "a free wish per ~1000
turns." Pairs especially well with marker-stockpiling strategies.

**The Orb of Fate** (Valkyrie): the most generous passive in the
game: counts as a luckstone, grants warning, halves both spell *and*
physical damage taken. `#invoke` is levitate-or-teleport (a toggle,
very useful in the Sanctum). Valkyries also have Mjollnir to throw,
so the Orb sits in inventory as pure carry value.

**The Eye of the Aethiopica** (Wizard): grants magic resistance
when **worn** (a Wizard's wearing slot for it is the amulet, so
in practice always); carrying also gives half spell damage taken
and *extra energy regeneration*, a Wizard's most precious
resource. `#invoke` opens a portal that drops you in Vlad's Tower
(one-way; useful for shortcutting the Castle → Vlad's traversal).
For a spell-caster this is irreplaceable.

---

## Part Six: The Deep Dungeon

### The Castle
<!-- audit
2026-05-18:
- no minotaur or internal maze in castle.lua; minotaurs live in earth/fire/hellfill
- wand chest is locked at creation (castle.lua:144); monsters cannot unlock chests (muse.c:2273 mloot_container bails on olocked)
- Elbereth + cursed scroll target food-eaters, not shopkeepers (castle.lua:150 author comment)
- throne room is filled with random court monsters (L/N/E/H/M/O/R/T/X/Z), not soldiers (castle.lua:54, 195-221)
- soldiers and lieutenant guard the entry hall and tower corners
- five trap doors at columns 40/44/48/52/55 (gaps 4/4/4/3), not strictly even (castle.lua:156-160)
- trap door always sends you to Valley of the Dead (dlevel=1), not a random Gehennom level (trap.c:669-670, dungeon.c:1949-1953)
- storerooms hold four D-class dragons; moat holds sea monsters; fountain present (castle.lua:60, 180, 185)
- drawbridge passtune is 5 notes A-G, Mastermind-style miss feedback (music.c:793, 836-884)
- any instrument can attempt the passtune; flutes/horns/bugle require can_blow, harp and drums don't (music.c:769-771)
- wand of striking DESTROYS the drawbridge; wand of locking/spell of wizard lock closes it (zap.c:3290-3305)
- wand of opening or spell of knock opens the drawbridge (zap.c:3263-3273, 2184)
- strategy aligned with NetHackWiki Castle, Passtune, Drawbridge, Wand of wishing: passtune-as-Mastermind, wand-of-opening/spell-of-knock alternatives, wand of striking destroys, bring conflict for crowd control, plan a small wishlist, secure MR/reflection/fire-res/poison-res before descending (https://nethackwiki.com/wiki/Castle, https://nethackwiki.com/wiki/Passtune, https://nethackwiki.com/wiki/Drawbridge, https://nethackwiki.com/wiki/Wand_of_wishing)
-->

If you've reached the Castle, congratulations: you've survived the
easy part. Everything below is worse.

The Castle sits at the bottom of the Dungeons of Doom, guarded by
a drawbridge and whatever the dungeon decided to stuff inside this
time.

The drawbridge is the first puzzle. You can lower it four ways:

- **Play the passtune.** A five-note musical sequence played on
  any tonal instrument (wooden flute, magic flute, tooled horn,
  frost or fire horn, bugle, harp) opens the drawbridge. The
  notes are randomized per game. You can learn them by trying
  different sequences: the game tells you how many notes are
  correct after each attempt, like a game of Mastermind. Stand
  one knight's-move from the bridge while guessing — adjacent
  squares get crushed when the bridge opens or breaks. The notes
  are A–G; "H" is also accepted, in the German notation where it
  means B.
- **Wand of opening** pointed at the drawbridge.
- **Spell of knock** cast at the drawbridge.
- **Wand of striking** *destroys* the drawbridge entirely. The
  moat squares become walkable, but the bridge is gone and the
  tune is useless afterward. Use this as a one-way option.

Once you're across, the Castle contains:

- A **throne room** with a throne and a random court of
  high-letter monsters (liches, nymphs, eyes, giants, and the like).
  Sitting on the throne is tempting but risky (see
  [Points of Interest](#points-of-interest)). The throne room also
  holds a separate **treasure chest** with random loot — not the
  wand chest, just a side prize.
- **Barracks** full of soldiers carrying decent equipment, which is
  to say *your* equipment once you've dealt with them.
- **Four corner-tower alcoves**. One (and only one, randomly)
  contains the **wand of wishing** in a locked chest. *Search them
  all*, or quaff a potion of object detection from the courtyard
  to see which tower holds the chest and skip the other three.
  In 5.0, that chest also holds a **potion of gain level**,
  included as a small make-good for the wand's charge changes (see
  below). The chest's square is protected by a burned-in
  [*Elbereth*](#elbereth) engraving and sealed with a cursed scroll of
  scare monster. Those
  wards exist to keep wandering monsters from *eating* the chest
  itself (some species, like leprechauns and rats, gnaw containers);
  the cursed scroll is also a known gotcha — don't try to read it
  casually. The locked chest opens by force, by a key, or by a wand
  of opening.
- Four **storerooms** along the north and south walls, each guarded
  by a dragon (`D`-class). Don't confuse them with the corner
  alcoves; the storerooms hold random fodder.
- A **central hallway lined with five trap doors**. Stepping on
  one drops you straight to the Valley of the Dead, which is rarely
  what you want at this stage. Watch the floor.
- A **fountain** in the moat-side corridor — usable in emergencies
  but not worth risking the wand of wishing for.
- A **moat** surrounding the fortress, occupied by giant eels and
  the occasional shark.

Strategy: clear the Castle carefully. A ring of conflict turns
the guards against each other: walk in, put on the ring, and let
the soldiers solve your monster problem for you. Loot everything.
Then use your wand of wishing to fill critical gaps in your
equipment (gray dragon scale mail, silver dragon scale mail,
gauntlets of power, speed boots, whatever you're missing).

The locked Castle wand chest is **safe to leave temporarily**:
monsters in 5.0 can pick up and rummage through *unlocked*
containers, and they can unlock doors with keys, but they cannot
unlock chests. A chest that started life locked stays locked
until you or a wand of opening intervene. Unlocked containers are
fair game.

The Castle wand yields only two wishes reliably (one charge + one
recharge), so plan a *small* wishlist and accept that further
wishes will need to come from other guaranteed sources — Vlad's
throne, the Amulet pickup, Orcus Town's lamp/marker, fountain
luck, or wresting. The era of the bottomless wishing wand is over
(see [Key Wands](#key-wands) for the full mechanics).

Once you're fully equipped, the staircase down leads to Gehennom.
Take a moment before descending. Sit down. Have a snack. Check
your inventory twice. You should have **magic resistance**,
**reflection**, **fire** and **poison resistance**, a **wand of
digging**, a **unicorn horn**, plenty of food, holy water,
scrolls of teleportation and identify, and your **quest
artifact**.

---

### Gehennom
<!-- audit
2026-05-19:
- Asmodeus carries wands of cold AND fire (makemon.c:804-807)
- Asmodeus is fire-, cold-, AND poison-resistant: MR_FIRE|MR_COLD|MR_POISON (monsters.h:3124)
- Baalzebub: AT_BITE/AD_DRST (drain Str, poisonous) + AT_GAZE/AD_STUN (stun) — NO gas cloud, NO fly summons (monsters.h:3110-3119)
- Baalzebub's lair is beetle-shaped (mkmaze.c:471 baalz_fixup)
- demon-lord teleport blocked (teleport.c:21-34)
- Geryon/Dispater/Baalzebub/Asmodeus are the bribable major demons (MS_BRIBE) — minion.c:309-311 sets bribe price
- Vlad's throne effect rate: only rnd(6) > 4 (= 1/3 of sits) triggers anything; 4/13 of those are the wish (sit.c:45, 238-353)
- so unconditional wish rate is (1/3)·(4/13) = 4/39 ≈ 10%; ~10 sits average, ~7 bad effects absorbed
- Orcus drops magic lamp or magic marker, 50/50 (orcus.lua:107-111)
- Sanctum has noteleport + nommap (sanctum.lua:8)
- Valley of the Dead has noteleport + nommap + non-diggable walls (valley.lua:10, 74)
- strategy aligned with NetHackWiki Gehennom, Bribe, Demon lords and princes: prayer dead, bribery (gold in open inventory) for the lawful demon princes, Excalibur disables bribery, dig don't navigate (https://nethackwiki.com/wiki/Gehennom, https://nethackwiki.com/wiki/Bribe, https://nethackwiki.com/wiki/Demon_lords_and_princes)
- blessed scroll of genocide on class 'L' wipes lich/demilich/master lich/arch-lich (read.c:2638-3015 do_class_genocide, monsters.h:1864-1899 four S_LICH entries); Wizard of Yendor is S_HUMAN (monsters.h:2847-2858), not affected
-->

Below the Castle, the dungeon changes. The corridors give way to
mazes. The monsters give way to demons. The comforting knowledge
that you can pray to your god for help gives way to silence: in
Gehennom, you walk beyond the protective gaze of your god.

This is the part of the game that separates tourists from
ascenders. Everything you've prepared for has been leading here.

#### The Valley of the Dead

The very first level of Gehennom, immediately below the Castle, is
a named special level called the **Valley of the Dead**. You'll
see the arrival message — *"You arrive at the Valley of the
Dead..."* — and the dungeon overview will mark it for you. It's
a wide hand-designed map with three irregular graveyards scattered
across it and a permanent **shrine to Moloch** in the upper-left
corner (an unaligned high altar; do not pray here). Walls are
non-diggable everywhere, so you can't shortcut through them, and
the level is flagged `noteleport` and `nommap` — magic mapping
won't reveal it and teleportation doesn't work.

The morbid detail worth noticing: scattered across the level are
**dead bodies of every player role** the dungeon has ever seen
descend — two corpses each of Archeologists, Barbarians, Cavemen,
Healers, Knights, Rangers, Rogues, Samurai, Tourists, Valkyries,
and Wizards. Pointedly absent: **no Priests, no Monks** (maybe
Moloch has a special fate reserved for members of those classes).

#### What's Different in Gehennom

- **No prayer.** Your god is deaf to you in Gehennom (unless you're
  a Moloch worshipper, and you're not). No emergency healing. No
  food rescue. No curse removal via divine intervention. Pack
  accordingly, because down here, you are completely on your own
- **Fire everywhere.** Fire traps litter the corridors. Demons
  breathe fire as casually as you breathe air. If you don't have
  fire resistance by now, turn around
- **Hot ground.** In 5.0, the ground itself is hot
  enough to shatter potions dropped on the floor. Keep everything
  in a bag at all times
- **Demon lords.** Named demon lords (Orcus, Baalzebub, Asmodeus,
  Juiblex, Yeenoghu, and if you're very unlucky, Demogorgon) hold
  court on specific levels. Each is a major battle. Several can
  summon reinforcements. All of them are angry you're here.
  However, **most demon lords can be bribed.** On first sight, if
  you haven't already attacked them, a major demon will name a
  price in gold for safe passage. The demand is a random fraction
  (roughly 20–100%) of the gold sitting **in your main inventory**
  — not gold inside containers — so a well-known runner-up trick
  is to **stash most of your gold in a bag of holding before
  approaching the throne**: the demand shrinks proportionally, and
  a few hundred zm bribe can buy off a prince who would otherwise
  have demanded thousands. The alternative is fighting a high-level
  boss, so unless you specifically want the XP or sacrifice corpse,
  bribery is often the better trade. (Wielding Excalibur or
  Demonbane closes off the bribery option — they refuse to talk and
  attack on sight.) The Riders on the Astral Plane and a small
  handful of demons (notably Demogorgon) won't take a bribe; the
  rest usually will
- **Teleportation restrictions.** In 5.0, teleportation
  is blocked on a demon lord's lair level while that lord still
  lives. Kill or banish them and the restriction lifts. In older
  editions, most Gehennom levels permanently blocked teleportation
- **Mazes.** Nearly every level is a maze. A wand of digging or
  pickaxe isn't optional here; it's as essential as your weapon.
  Dig straight lines to the stairs and don't look back

#### The demon-prince lairs

Three of Gehennom's special levels are the personal thrones of
**Asmodeus** (fire-, cold-, and poison-resistant, casts cold
spells, carries wands of cold and fire), **Baalzebub** (the Lord
of the Flies — gaze that stuns you and a poisonous bite that
drains Strength; his lair is a beetle-shaped maze), and
**Juiblex** (the Faceless Lord, a slime that engulfs in melee
and spits acid). All three sit alone in their lairs and **won't pursue**
you, so you can avoid them entirely by skipping their level.

**Asmodeus and Baalzebub are bribable**: the demand is a random
fraction of the gold in your main inventory, so **stash gold in a
bag of holding before walking up to the throne** and a few hundred
zm will buy off a prince who would otherwise have demanded
thousands. Lawful characters get a sweetener: all four bribable
demon princes are themselves lawful, and they discount the demand
by half for a co-aligned visitor. **Juiblex is not bribable** —
only the Arch-Devil demons with the bribe disposition (Geryon,
Dispater, Baalzebub, Asmodeus) accept gold; Juiblex, Yeenoghu,
Orcus, and Demogorgon attack on sight regardless. Fighting Juiblex
is viable late game (wand of death works on all four), but expect
a real fight. None of their corpses is useful for sacrifice the
way a fresh weak monster's would be. One thing the demon never
forgets: a *refused* bribe converts the prince to permanent
hostility, and they will not offer terms again. Bribe or fight;
don't dither.

#### Vlad's Tower

A three-level tower branching **upward** off Gehennom (one of the
only side-branches in the lower dungeon). **Vlad the Impaler** —
a unique vampire lord — guards the **Candelabrum of Invocation**
at the top. Climb the tower, kill Vlad, take the Candelabrum.

The tower also contains a **special throne**, and 5.0 has made it
both more rewarding and more painful. The good news: it never
disintegrates from sheer use the way ordinary thrones do, so you
can sit on it again and again. The bad news: you will, because
the prize is rare. Each sit rolls one of thirteen effects. Four
of them grant a wish (the throne *does* disintegrate after the
wish, having spent its power). The other nine are bad: permanent
level drain, an inventory-coating layer of grease (your weapon
will slip, your shield will fall off), a stripped intrinsic, a
forced level teleport to the vibrating-square level (sometimes
useful, often not), three summoned demons, a confused-blessed
remove curse on your gear, forced polymorph, acid damage in
eighty-HP gulps if you don't have acid resistance, or a randomized
stat shuffle that will probably make several of your scores worse.

The arithmetic: only one sit in three picks an effect at all
(the other two roll "you feel out of place" and do nothing); of
those that fire, 4/13 are the wish. Unconditional rate is about
1 in 10, so plan on roughly ten sits before the wish lands, with
about seven bad effects absorbed along the way. Plan accordingly. Stand at full HP,
leave any precious gear behind (a grease hit coats your whole
pack and makes your hands slippery for 100 to 200 turns, dropping
items when you try to use them), and have acid
resistance or magic resistance ready before you sit. If you don't
want a forced wish (say, you've already used your Castle wish and
Amulet wish and want to keep this one for the ascension kit), you
can sit at any time; you don't have to do it right now. The
throne stays put unless something destroys it.

#### Orcus Town

**Orcus** is a god of the underworld in Roman mythology — a
chthonic figure who punishes broken oaths and devours the dead. In
NetHack he's a unique demon prince (`&`, level 66, fast flier),
the **Prince of Undead**, who casts spells, swings a weapon, claws
twice, and stings for strength drain. His signature artifact is
the **Wand of Orcus** — a wand of death by another name; his
fingertip cantrip is also a death ray, so wear an amulet of life
saving and consider opening with your own wand of death rather
than a melee approach.

His level is a ghost town: a normal shopping district with all
the shopkeepers and customers killed off by his ambient aura, the
buildings stocked with random loot instead of for-sale inventory.
What's left is an honor guard of liches, vampires, and ghouls.
Somewhere on the level the dungeon guarantees either a **magic
lamp** or a **magic marker** (50/50). Walk carefully (fire and
magic traps everywhere), deal with the residents, and lift the
lamp or marker on your way out. Either is a real supplement to
the Castle wand's single charge.

#### The Wizard's Tower

A sequence of three special Gehennom levels that lead to the
**Wizard of Yendor** himself and the **Book of the Dead**. He
is the most dangerous enemy in the game, not because he's the
strongest fighter, but because he **never stops**. He teleports to
your location, summons monsters, steals back his Amulet whenever
you grab it, curses your gear, and once you wake him he *will not
leave you alone* for the rest of the game.

Kill him cleanly the first time, grab the Book, and move on.
Subsequent kills don't yield new loot (he respawns), so don't
engage him voluntarily again. The "Run, don't fight" advice for
the Ascension Run is mostly about him.

#### Moloch's Sanctum

The bottom level of Gehennom. It is **sealed**: until the
Invocation ritual is performed (see "The Heist" below), the
down-stair to the Sanctum doesn't exist, and the level above is
just one more maze. Once the seal breaks, descend to find the
**High Priest of Moloch** standing on the **high altar** with the
**Amulet of Yendor**. The High Priest is a unique non-bribable
boss who casts spells, summons minions, and aggrieves anyone in
melee range — the standard answer is a wand of death or finger of
death from a safe distance.

#### The Heist

The climax of the game is a choreographed sequence: three
Invocation items, one vibrating square, one final boss, and one
frantic climb back to the surface. The steps:

1. **Collect the trio.** You need the **Bell of Opening** (the
   Quest goal, dropped by your quest nemesis), the **Candelabrum
   of Invocation** (the top of Vlad's Tower), and the **Book of
   the Dead** (the bottom of the Wizard's Tower). Missing any one
   means walking all the way back to fetch it; the Bell in
   particular is easy to leave behind on the nemesis's corpse
   the first time through the Quest.

2. **Attach all seven candles to the Candelabrum.** Apply (`a`)
   each candle and select the Candelabrum. Candles spawn often
   enough that you'll usually have enough, but you need a source
   for seven: **Izchak's lighting shop in Minetown** is the clean
   answer, or seven are scattered on that level if the shop is
   absent (Orcish Town layout).

3. **Find the vibrating square.** On the Gehennom level directly
   above Moloch's Sanctum, a single square vibrates when you step
   on it: *"You feel an unsettling vibration under your feet."*
   The square's position is random within the maze, so you have
   to search by walking — scrolls of magic mapping help enormously.

4. **Perform the Invocation.** Standing on the vibrating square,
   with the Candelabrum lit and the Book in your pack, **`#invoke`
   the Bell of Opening**. The floor opens; a down-stair to the
   Sanctum appears under your feet.

5. **Swipe the Amulet from Moloch.** Descend, take down the
   **High Priest** (wand of death is the clean answer), walk onto
   the high altar, and pick up the **Amulet of Yendor**.

6. **Begin the getaway.** The up-stair from the Sanctum now lifts
   you out (it wouldn't before you had the Amulet). You're now on
   the **Ascension Run** — every covetous monster in the game has
   noticed, the Wizard of Yendor will keep teleporting to you to
   take his Amulet back, and the Mysterious Force will keep
   yanking you back down. Climb fast (see [The Ascension Run](#the-ascension-run)
   below).

#### Survival Tips

- **Bring extra food** — you'll be moving fast and praying is not a reliable refill
- **Bring scrolls of remove curse** — fast inventory cleanup when something goes wrong
- **Dig, don't navigate.** Maze walls are faster to go through
  than around
- **Kill the Wizard quickly.** Every turn he lives is another
  summoned monster, another stolen item, another cursed piece of
  gear. He'll come back (he always comes back), but the intervals
  between his appearances give you breathing room
- **The Amulet anchors you.** Level teleportation doesn't work
  while you carry it. Every step back to the surface must be
  climbed by foot
- **Genocide the lich class.** A blessed scroll of genocide
  applied to **L** removes liches, demiliches, master liches, and
  arch-liches in one read. Some of the worst Gehennom threats,
  gone for the rest of the run

---

### The Ascension Kit
<!-- audit
2026-05-18:
- there is no "helm of holiness"; the artifact is Mitre of Holiness
- Mitre of Holiness = HELM_OF_BRILLIANCE base + CARY(AD_FIRE) + SPFX_PROTECT (+1) + M2_UNDEAD + ENERGY_BOOST invoke (artilist.h:265-269)
- Eye of the Aethiopica is Wizard-only: SPFX_RESTR + PM_WIZARD; other classes get the badclass blast (artilist.h:303-307, artifact.c:920-948)
- wand-of-death on the High Priest works: type=-1 skips saving throws (zap.c:4314); High Priest has no antimagic and mr1=70 does not gate ZT_DEATH
- prayer CAN cure hunger and uncurse worn items (pray.c)
- strategy aligned with NetHackWiki Ascension kit: GDSM/SDSM, cloak of MR, speed boots, gauntlets of power, life saving, bag of holding, wand of death, candles are the canonical kit (https://nethackwiki.com/wiki/Ascension_kit)
-->

By the time you're ready to invoke Moloch's Sanctum, the loadout
that experienced players actually wear has converged. A survey of
recent ascensions from the public NetHack server shows what most
winners carry. Here is the canonical kit, slot by slot:

| Slot | Canonical pick | Notes |
|--------|------------------------|---------------------------------------|
| **Body** | Dragon scale mail | Gray (magic resistance) or silver (reflection) are the popular picks; blue (shock) also works. |
| **Cloak** | Cloak of magic resistance | Or a robe for casters. Magic resistance is non-negotiable in Gehennom. |
| **Helm** | Helm of brilliance or helm of telepathy | Brilliance for casters; telepathy when you might be blind. |
| **Gloves** | Gauntlets of power | Skip them only if you have a different STR strategy (e.g. a Knight with a +STR ring). |
| **Boots** | Speed boots | **Universal.** |
| **Shirt** | Hawaiian shirt or T-shirt | A free body slot under everything else — winners enchant it heavily (typically blessed +4 or +5) for several extra AC at no cost. |
| **Shield** | Mostly skipped | Reflection comes from silver dragon scale mail or an amulet instead; two-weapon fighters can't use a shield anyway. |
| **Amulet** | Amulet of life saving | The "extra life" plan. |
| **Ring (L)** | Free action | Anti-paralysis is non-negotiable on the Astral Plane. |
| **Ring (R)** | Slow digestion, conflict, or regeneration | Conflict is the standard Astral-Plane crowd-control choice. |
| **Weapon** | Your role's quest artifact + a silver saber | Silver saber appears in most builds as the off-hand because silver bypasses demon resistances. |
| **Pack** | Bag of holding, magic lamp, unicorn horn, luckstone, wand of death, multiple wands of teleport, seven candles, ≥5 holy water, a couple of blessed potions of full healing, a cockatrice corpse | The "bag-of-holding bundle." Holy water re-blesses items the Wizard or liches keep cursing in Gehennom; full healing is a one-action panic button; a wielded cockatrice corpse one-shots Riders (and other non-stoning-resistant nasties). Candles are for the Candelabrum — Izchak's Minetown lighting shop is an easy source. |
| **Required loot** | Bell of Opening, Candelabrum of Invocation, Book of the Dead, Amulet of Yendor | The Invocation chain plus the prize. |

A typical ascension AC sits in the **−25 to −40** range, but AC
alone is not the difference between winners and losers.

#### What killed the runners-up

A look at characters who died in deep Gehennom (Dlvl 35-50) shows
that their *inventories were nearly indistinguishable* from the
winners'. Their AC was −23 to −40. They had wands of death, all
three Invocation items, silver dragon scale mail. What killed them
was *behavior*:

- **Inventory management mid-combat.** An Archeologist on Dlvl 35
  tried to open a tin while a jabberwock, a displacer beast, and a
  zruty were adjacent. The tin opener prompt took the turn she
  didn't have.
- **Eating when not hungry.** A Tourist with AC −40 and all three
  Invocation items, deep in Gehennom, chose to eat a stalker corpse
  while satiated and choked to death. The ring of slow digestion on
  her finger does not prevent choking.
- **Out of escape consumables.** A Wizard on Dlvl 50 — within sight
  of the Sanctum — burned the last wand-of-death charge without any
  further escape route, then died blind and surrounded.

Keep at least one escape consumable within reach: a scroll of
teleportation, a wand of digging, or an oilskin sack with a potion
of full healing.

---

### The Ascension Run
<!-- audit
2026-05-21:
- bones save converts the real Amulet of Yendor to FAKE_AMULET_OF_YENDOR and curses it when a previous adventurer dies carrying it (bones.c:170-173)
- wish for an Amulet of Yendor silently substitutes a fake (objnam.c:5003-5006 substitution list)
- Astral altar offering accepts only the real Amulet; fake amulets fail and the death message reads "(with a fake Amulet)" (end.c:1413-1414)
2026-05-19:
- Mysterious Force is gated on Gehennom only (do.c:1541); same-level shuffle is the majority outcome
- odds = 3 + ualign.type; diff = rn2(odds): Chaotics max -1, Neutrals max -2, only Lawfuls reach -3 (do.c:1544)
- never fires on bottom 4 levels (dunlev < dunlevs_in_dungeon-3)
- Force frequency tapers with each trigger (do.c:1536-1563)
- Amulet-pickup wish fires once on next moveloop iteration if !u.uevent.amulet_wish (allmain.c:446-451)
- Elbereth is DEAD in Gehennom, all four Elemental Planes, and Astral: onscary returns FALSE for Inhell || In_endgame (teleport.c:68-70)
- carrying the Amulet blocks level teleport via the u.uhave.amulet guard (teleport.c:1185-1189)
- strategy aligned with NetHackWiki Ascension run, Mysterious force, Amulet of Yendor: run-don't-fight, dig straight lines, kill the Wizard fast, the Force as the primary climb obstacle (https://nethackwiki.com/wiki/Ascension_run, https://nethackwiki.com/wiki/Mysterious_force, https://nethackwiki.com/wiki/Amulet_of_Yendor)
-->

You did it. You fought through Gehennom, defeated the High Priest,
and snatched the Amulet of Yendor from Moloch's Sanctum. Now all
you have to do is carry it from the absolute bottom of the dungeon,
through every level of Gehennom, past every demon lord you thought
you were done with, all the way back to the surface, and then
through the Elemental Planes to the Astral Plane where your god
awaits. Easy, right?

**A free wish on pickup.** The moment you pick up the Amulet of
Yendor, your god grants you a single wish on the next turn (it
fires automatically — you don't need to invoke it). This is one
of the most generous moments in the game. Have your wish list
ready *before* you reach the Sanctum: gauntlets of power, a
+5 weapon of your choice, blessed cloak of magic resistance, or
whatever you're missing for the climb. You only get it once. A
late-game favorite: a wish for a **cursed potion of gain level**.
Drinking one while carrying the Amulet skips you up a whole
Gehennom level without provoking the Mysterious Force.

**Bring the authentic Amulet.** The climb out is always open:
every up-stair in the Dungeons of Doom takes you closer to the
surface regardless of what you carry. The **Astral plane portal**
at the top of the Endgame ladder, however, won't open without
the real Amulet of Yendor in your inventory. Only the Amulet you
took off the High Priest's body in Moloch's Sanctum counts.
Bones-pile Amulets are fakes (the game converts a dead
adventurer's real Amulet to a fake when their corpse becomes a
bones level), and a wish for an Amulet of Yendor silently
substitutes a fake too. If you didn't pick yours up off the High
Priest, you don't have the real one.

The Ascension Run is the victory lap that keeps killing even the
strongest adventurers. You have the most powerful artifact in the
dungeon in your pack, every covetous monster in the Mazes knows
it, and the dungeon itself is fighting to keep you from leaving.
The most exhilarating and terrifying stretch of the game.

#### The Gauntlet

Four kinds of trouble run at once, all of them aimed at the
Amulet in your pack:

- **The Wizard of Yendor** periodically teleports to you, summoning
  nasty monsters and trying to steal back his Amulet. He will not
  stop.
  Kill him each time; he always comes back. He is the world's most
  persistent ex.
- **The Amulet blocks teleportation.** You can't level teleport
  while carrying the Amulet. You must climb every single staircase
  from the bottom of Gehennom to the surface. All of them. By foot.
- **Covetous monsters.** Demon lords and the Wizard can warp
  directly to your position and attack. They specifically target you
  for the Amulet, because apparently everyone wants this thing.
- **The Mysterious Force.** While carrying the Amulet in Gehennom,
  each time you climb stairs there's a chance the force grabs you
  instead. Often it just shuffles you elsewhere on the same level;
  sometimes it drops you **down** a level (Chaotic max), two
  levels (Neutral max), or even three (Lawfuls only). The
  worst yank is hardest on Lawfuls and gentlest on Chaotics: a
  Chaotic climb can never lose more than one level at a time. In
  5.0 the trigger chance also **decays** as it fires — every yank
  slightly reduces the chance of the next one, and decays faster
  when the yank was deeper, so over the whole climb the per-step
  trigger rate stays roughly even across alignments. The force
  stops the moment you climb out of Gehennom, and it never fires
  on the bottom four levels.
- **Consider a Chaotic detour.** A helm of opposite alignment
  worn just before the climb flips you to Chaotic and caps every
  yank at one level. The cost: your Astral offering then goes to
  the Chaotic altar, since the altar check uses your *current*
  alignment. An optimization choice, not a free lunch.

#### Strategy

You are no longer an explorer. You are a running back carrying the
ball through the entire opposing team. Speed is everything.

- **Run, don't fight.** Don't explore. Don't loot. Just go up.
  Every turn you spend fighting something optional is a turn the
  Wizard gets closer to stealing back his Amulet.
- **Dig.** Use your wand of digging to reach staircases quickly.
  Straight lines through walls beat wandering through corridors.
- **Zap problems away.** Teleportation wands move monsters out of
  your path. Death wands remove them permanently. Use both
  liberally.
- **Casters: drop the Amulet to cast.** Carrying the Amulet adds
  an extra 1–2× the spell's base cost on every cast, so you pay
  roughly 2–3× total. Drop the Amulet, cast your finger of death
  or magic mapping, pick it back up. The three-turn round trip is
  cheaper than the Pw burn.
- **Kill the Wizard fast.** When he shows up (and he will), don't
  try to be clever. Finger of death, wand of death, or brute force.
  The faster he's down, the fewer monsters he summons.
- **Don't rely on Elbereth past the Castle.** Elbereth is
  **completely ignored** in all of Gehennom and on all four
  Elemental Planes plus Astral. You can still write it for the
  alignment, but no monster will care. Plan your heal-and-recover
  breaks around corridors, scrolls of teleportation, and conflict
  instead.

The Ascension Run rewards preparation and punishes hesitation. If
you packed well at the Castle and your resistances are solid, this
is a sprint, not a marathon. Once you reach the top of the Dungeons
of Doom, the final staircase leads to the Elemental Planes: the
last obstacle between you and divinity.

---

### The Elemental Planes
<!-- audit
2026-05-19:
- Plane of Air: vortex AT_ENGL just damages you; it does NOT move bubbles or carry you (vortex rows monsters.h:1062-1109 are plain AT_ENGL damage; bubble drift loop at mkmaze.c:1674-1679 is independent of vortex monsters)
- bubble drift is a separate system: mv_bubble shifts cloud-bubbles each turn (mkmaze.c:1648-1685, 1951-1965)
- Plane of Water drowning is NOT instant death: done(DROWNING) honors life saving (trap.c:5171-5193); Breathless prevents it (trap.c:5106-5126)
- Astral wrong-altar offering ends the game immediately with done(ESCAPED) and the opposing god gains dominion (pray.c:1562-1572)
- the Amulet is consumed BEFORE the alignment branch (pray.c:1537-1540) — no retrieval
- altar farlook reveals alignment only when ADJACENT; otherwise just "aligned high altar" (pager.c:744-754)
- every plane has noteleport; self-zap WAN_TELEPORTATION prints "A mysterious force prevents you from teleporting!" (teleport.c:854-855)
- self-teleport reaches scrolltele() at line 844 from zap.c:2876-2878, so the wand still works on monsters
- strategy aligned with NetHackWiki Plane of Water, Scroll of genocide, Plane of Air, Astral Plane: genocide class `;` on the Plane of Water, conflict to clear Air's elementals, wrong-altar offering ends the game (https://nethackwiki.com/wiki/Plane_of_Water, https://nethackwiki.com/wiki/Scroll_of_genocide, https://nethackwiki.com/wiki/Plane_of_Air, https://nethackwiki.com/wiki/Astral_Plane)
-->

Beyond the top of the Dungeons of Doom, the world dissolves into
its raw elements. Four planes stand between you and the gods, each
one a different flavor of hostile. There are no stairs here, only
magic portals, hidden somewhere in each level, leading to the next.
Find the portal. Survive the plane. Move on. There is no going back.

**Two cheap ways to find a portal.** A scroll of gold detection
read while confused marks every trap on the level, the portal
included: one read, one map. And the Amulet of Yendor is itself a
compass while you carry it: wielded or worn, it occasionally
mutters *hot*, *very warm*, or *warm* as you get closer (within
3, 8, or 12 squares of the portal). It's a hot/cold game you can
play your way across the void.

#### Plane of Earth

You arrive encased in solid rock and boulders, surrounded by earth
elementals that hit like the mountain itself. The portal is buried
somewhere in the level. Dig. A wand of digging is essential; a
scroll of magic mapping or crystal ball reveals the portal's
location so you can dig *toward* it instead of blind. This level
is claustrophobic, dark, and punishing, but it's the gentlest of
the four.

#### Plane of Air

The opposite extreme: an open void with no walls, no floor you can
feel, just empty sky and air elementals moving faster than thought.
They attack multiple times per turn and they cannot be genocided.
A ring of conflict is devastating here: let them tear each other
apart while you search for the portal. A scroll of magic mapping
reveals it. The level is divided into drifting **cloud bubbles**
that move on their own each turn: if you're standing in a bubble
when it shifts, you shift with it. Walking with the drift can
carry you across the level faster than fighting against it,
and a bubble may eventually drift you onto the portal square
itself. (Teleportation is blocked on every plane, so a wand of
teleport on yourself just prints "A mysterious force prevents you
from teleporting!" It still works on monsters.)

#### Plane of Fire

Everything is on fire. The ground is fire. The air is fire. Fire
elementals fill the level, and fire traps dot every corridor. Fire
resistance isn't just recommended: without it, you'll be dead in
turns. Map the level, find the portal among the flames, and get
there. Don't stop to fight anything you don't have to.

#### Plane of Water

The entire level is underwater. Without magical breathing (an
amulet, the Amphibious intrinsic, or a polyform that breathes
water) you will drown. Drowning calls the standard death path,
so an **amulet of life saving** will rescue you, but you'll
drown again on your next turn unless something has changed.
The level is a labyrinth of water-filled chambers with occasional
air pockets. Sea monsters prowl the corridors.

**The standard tactic on arrival: genocide class `;`.** Read a
scroll of genocide, target the entire `;` class (eels, krakens,
sea monsters, sharks, jellyfish, piranhas), and the level instantly
empties of anything that can drag you under. This is the right
moment for that scroll. Class `;` is almost nowhere else in the
game (a kraken in Medusa's pool, a moccasin from a fountain are
isolated encounters not worth burning a class-wipe on), and on the
next plane it's irrelevant. Spend the scroll here. Then find the
portal and push through. This is the last barrier between you and
the gods.

#### The Astral Plane

You surface into the presence of the divine. Three altars stand
in the great temple: Lawful, Neutral, and Chaotic. You must
sacrifice the Amulet of Yendor on the altar matching your
alignment to ascend. **Choose wrong and the game ends on the
spot**: the opposing god gains dominion over your god, and you've
handed victory to the other side. There is no retrying. Pick
the right altar the first time. Farlook (`;`) shows an altar's
alignment only when you are *adjacent* to it. From across the
room you only see "an aligned high altar," so plan to walk
within one square of each in turn until one matches yours.

The plane is swarming with Angels and the three **Riders**:
Death, Famine, and Pestilence. They are level 30, regenerate
while you fight, see invisible, and shove monsters out of their
path. Each one hits twice per turn with a touch attack dealing
8d8 damage.

- **Death's** touch has a 3-in-20 chance of instant kill on
  every hit. Magic resistance blocks the instakill, but not the
  8d8 baseline.
- **Pestilence** inflicts a deadly illness that kills you over
  the next several turns. Sick resistance is the cleanest
  defense; a unicorn horn can sometimes clear the timer in time
  if you don't have intrinsic.
- **Famine** adds 40 to 79 hunger units to every hit. One swing
  won't drop you below Hungry, but a few in a row will starve
  you mid-fight.

A slight mercy that is new to 5.0: if Pestilence or Famine land
their first attack on a turn, their second downgrades to a stun.

**The Riders cannot be permanently killed.** They revive, they
pursue, they do not stop. **Eating any Rider corpse is
instantly fatal.** You are not here to fight; you are here to
reach one altar, make one sacrifice, and end this.

If you have to pick which Rider to engage first, the community
consensus is **Pestilence is the one to fear most**: the sickness
timer keeps killing you after you've moved away, and unicorn-horn
cures sometimes lose the race. Death's instakill is blocked by
magic resistance; Famine you can outrun with a stack of food.
Pestilence wants to be settled before either of the others.

**Defenses.** An **amulet of life saving** is the best insurance
on Astral. Magic resistance stops Death's instakill.
Sick resistance handles Pestilence (green dragon scale mail is
a source). Carry plenty of food (Famine
bypasses normal nutrition pacing) and a unicorn horn for the
stun side effects. A wielded cockatrice corpse (with gloves) can
remove a Rider on a single landed hit — they have no stoning
resistance. A ring of **conflict** keeps the Riders
tangled fighting Angels and minor demons instead of chasing you,
sometimes long enough to reach the altar; just don't put the ring
on while your own minion Angel is still alive — it vanishes and
your god replaces it with four hostile Angels. Teleportation wands
can clear a path through the crowds; note that **self-teleport
fails on every elemental plane**, so zapping the wand at
yourself does nothing. Only zapping it at others teleports them.

**Don't zap a wand of death at Death.** It heals him. Magic
missile works on all three Riders; use that instead.

When you offer the Amulet on the correct altar: you ascend. The
game is won. You've done what so few have done. Congratulations.

---

## Appendices

### Advanced Controls
<!-- audit
2026-05-19:
- F/G/g/m/O/v/_/;//, Ctrl+A/P/R/O, #overview, #chronicle, #annotate, #conduct all verified (cmd.c:1662-2065)
- `verbose` controls extra descriptive messages (wielding/digging/sounds/pets), NOT "why multi-commands stopped" (optlist.h:813-815 declares flags.verbose; gated at dig.c:711/1441/1468/2157, ball.c:61, attrib.c:176, apply.c:438 etc. — none are multi-command stop messages)
- double-tap F cancels the attack lock (cmd.c:1622-1633)
- `m` prefix on e/a/, opens a menu
- Ctrl+A repeats only the last EXECUTED command, not the last input (cmd.c:3732-3736)
- repeat-count cap is 32767 (global.h:135)
- number_pad/autopickup/pickup_types option semantics consistent with optlist.h
-->

The basic keys get you through every situation in NetHack. The
commands below get you through them faster. Once you've spent a
few thousand turns hammering `s` and walking corridors one square
at a time, you may find they become reflexive.

#### Command counts

Type a number before any command and the game repeats it that
many times: `10s` searches ten times, `20.` waits twenty turns,
`5h` walks west five times. The sequence interrupts automatically
as soon as anything interesting happens — a monster appears
adjacent, your HP changes, a `--More--` prompt fires, the search
turns up something. Press ESC to cancel early.

Counts up to 32,767 are accepted (five digits), but the practical
limit is "however long you'll watch the screen update without
losing patience." `99s` is plenty for any real searching job.

#### Repeat last command (Ctrl+A)

`Ctrl+A` runs whatever you just ran, with the same count if you
used one. After your first `10s` of searching, every subsequent
search is one keystroke. This is the most-used advanced command in
the game and you'll reach for it dozens of times per session. It
remembers the *last command that actually executed*, not attempts
that were canceled or bumped against a wall.

#### Movement prefixes

A handful of prefix keys modify the next command and then clear.
They are essential for moving safely through populated areas.

- **`F`** then a direction — **force attack** into that square,
  even if no monster is visible there. Use it on suspected
  invisible monsters, on a displaced creature whose image is one
  square off from its real position, or to break your own
  [Elbereth](#elbereth). Double-tap `F` to cancel without acting.
- **`G`** then a direction — **run** that direction until
  something interesting appears: a monster, an unknown item, a
  trap, a corridor branch, a closed door. Capital-letter
  directions (`H`, `J`, `K`, `L`, and the diagonals `Y`, `U`,
  `B`, `N`) are the same thing in one keystroke and are what
  most players actually use. `g` is a less-cautious variant of
  `G`, but in practice the difference is negligible.
- **`m`** then a direction — **move without attacking and without
  picking up**. Walk past your pet without striking it ("Pardon
  me, Fido"), step past an autopickup heap, refuse to walk into a
  known pool or lava square. With non-movement commands, `m`
  requests a menu instead of the default single-target prompt:
  `me` is "what would you like to eat?", `ma` is "which tool?",
  `m,` lets you pick from a floor pile.

#### Travel

The underscore key (`_`) is the "travel" command, a speedy
autopilot. Press `_`, point at a destination you've already
explored, then `.` to confirm, and your character walks the
shortest path there, stopping on any interruption — including
closed doors, which travel walks up to but doesn't open
(press a direction to step through them, or `o` first). `_<.` walks to the up-staircase; `__` walks
to a known altar; `_>.` walks to the down-staircase. After Ctrl+A,
this is the single biggest quality-of-life command in the game.

#### Forcing locked chests

`#force` (or `#f`) pries a locked chest open with your wielded
weapon when you don't have a lockpick or key. Bladed weapons risk
breaking the blade on the lock; blunt weapons risk destroying the
chest's contents.

#### Message history and redraw

`Ctrl+P` walks backward through the message history one message
at a time. A monster's special-attack warning, a shopkeeper's
price quote, or a status onset is preserved long enough to read it
twice. The buffer holds the last several dozen lines; older
messages roll off silently.

`Ctrl+R` redraws the screen — a useful reflex when the terminal
gets garbled or when something doesn't look right.

#### Dungeon overview and event journal

`Ctrl+O` (or `#overview`) lists the interesting levels you've
visited — anywhere with an altar, throne, fountain, sink, shop,
temple, vault, or branch stair, plus the Castle's tune once you
learn it. Prefix with `m` to see *all* visited levels in a menu
and add or edit annotations from there; `#annotate` does the
same for the level you're standing on. The classic use is
labeling stash floors so you remember which one held the bag.

`v` (or `#chronicle`) opens the **chronicle** — a chronological
journal of major events from this run: first kills, conduct
breaks, artifact gifts and crownings, prayer outcomes, level
milestones, and entries into major branches. Mainly for
end-of-run storytelling; for current conduct state use
`#conduct`.

---

### Customization {#options-worth-knowing-about}

NetHack's defaults are sensible, but a handful of options
dramatically improve quality of life. Flip them in-session with
`O` (capital O), or persist them in your rcfile: `~/.nethackrc` on
macOS/Linux, `nethack.cnf` in the install folder on Windows, or
the `NETHACKOPTIONS` environment variable.

**Status display.**

- **`hilite_status`** colorizes the bottom status line: HP turns
  yellow then red as you take damage, hunger goes yellow at Hungry
  and red at Weak, AC bands shift color as you improve. The single
  most-recommended setting in community rcfiles.
- **`menucolors`** colorizes menu entries by regex pattern. A
  common setup highlights holy water, magic markers, and blessed
  items so you can spot them at a glance.
- **`force_invmenu`** shows inventory as a menu rather than a
  letter prompt.
- **`pile_limit:5`** triggers the pile menu when 5 or more items
  are stacked on a tile.

**Safety.**

- **`paranoid_confirmation:Attack pray Remove quit`** requires you
  to type the full word `yes` for the listed actions: attacking
  peacefuls, praying, removing worn gear, and quitting. Catches
  almost every fat-finger accident.

**Pickup.**

- **`autopickup`** picks items up as you walk over them, filtered
  by **`pickup_types`** (e.g. `pickup_types:$?!=/` for gold,
  scrolls, potions, rings, and wands). The `m` prefix on movement
  suppresses autopickup for one step.
- **`autopickup_exception`** layers per-pattern rules on top:
  `autopickup_exception:">rock"` skips rocks even when the type
  filter would grab them; `autopickup_exception:"<holy water"`
  always grabs holy water.

**Movement.**

- **`number_pad`** turns the numeric keypad into movement keys
  (1–9 for directions). Off by default; enabling it changes
  digit-prefix behavior so you press `n` first to enter a count.
- **`runmode:walk`** slows the travel command down enough that
  you stop on interesting messages (default `runonly` blasts
  through everything until you hit something).

**Verbosity.**

- **`verbose`** turns on extra descriptive messages. Turn it off
  if the message log feels noisy.

**A starter rcfile.** A few lines that cover most of the above:

```
OPTIONS=hilite_status,menucolors,force_invmenu,pile_limit:5
OPTIONS=paranoid_confirmation:Attack pray Remove quit
OPTIONS=autopickup,pickup_types:$?!=/
OPTIONS=runmode:walk
```

**Curses for a paneled UI.** A bigger interface shift requires a
different binary. NetHack built with the **curses** windowtype
(`nethack-curses` on most distributions, or a custom build with
curses support) draws a properly paneled UI inside the terminal.
Set `windowtype:curses`, `align_message:right`, `align_status:bottom`,
`perm_invent`, and `windowborders` in your rc, open a 120×40
terminal, and you get a permanent inventory column, a multi-line
message panel, and bordered status and map regions. Plain tty
NetHack pins the message line at row 0 no matter what you set.

---

### Sokoban Solutions

Sokoban is a four-level boulder puzzle branch that goes *up* from
its entrance. Each level has two possible layouts, chosen randomly.
You push boulders onto pits to fill them and create a path to the
next staircase. The penalty for cheating (phasing through walls,
levitating over pits, destroying boulders) is a −1 Luck penalty
per infraction, and it stacks. Play fair.

In the maps below, boulders are labeled A through T so the
solutions can reference them. The `^` symbols mark pits; `<` marks
the upstairs. Your starting position is marked `@`.

The arrows mark rolling boulder traps. In sokoban, a boulder pushed
onto one keeps rolling in the direction you pushed until it falls
into a hole or hits something.

After solving a level, push leftover boulders into corners so they
can't block you if you return later. Items sometimes hide under
boulders.

**A note on mirroring.** Sokoban levels may be flipped
horizontally and/or vertically in 5.0. The solutions still work;
just mirror the directions.

> *Solutions originally compiled by Boudewijn Waijers, with
> contributions by Jukka Lahtinen and others, for the steelypips.org
> NetHack archive maintained by Kate Nepveu. Adapted for 5.0 and reformatted
> for this guide.*

#### Level 1, Version A
<!-- audit
2026-05-19:
- Scrolls land at spoiler (3,12) and (4,12); lua coords (02,11) and (03,11) (soko4-1.lua:94-95).
- Spoiler-to-lua mapping: lua_xy+1 = spoiler_col, row.
- Level flags noteleport, hardfloor, sokoban, solidify, premapped set (soko4-1.lua:38).
- All 19 push steps verified against soko4-1.lua by simulation.
- Final remainder (boulder A) is exact.
-->

```
            11111
   12345678901234
 1 ┌────┐  ┌───┐
 2 │····│  │···│
 3 │·A··└──┘·B·│
 4 │·C······D··│
 5 │··┌─┐@┌─┐E·│
 6 ├──┴─┴─┼─┘·─┴┐
 7 │·^·^·<│·····│
 8 │·^┌───┤F····│
 9 └┐^│   │·G···│
10  │↑└───┘·H···│
11  │^^^^^←I·J··│
12  │··┌────────┘
13  └──┘
```

1. Push A right one square.
2. Push C up one square.
3. Push D right one square.
4. Push D left to (4,4).
5. Push E down to (11,8).

The map now looks like this:

```
            11111
   12345678901234
 1 ┌────┐  ┌───┐
 2 │····│  │···│
 3 │·CA·└──┘·B·│
 4 │··D········│
 5 │··┌─┐>┌─┐··│
 6 ├──┴─┴─┼─┘·─┴┐
 7 │·^·^·<│··@··│
 8 │·^┌───┤F·E··│
 9 └┐^│   │·G···│
10  │↑└───┘·H···│
11  │^^^^^←I·J··│
12  │··┌────────┘
13  └──┘
```

6. Push H left one square.
7. Finish I, J, E, G, H, F, B, D, and C.

One boulder (A) remains. The two scrolls at (3,12) and (4,12)
are always scrolls of earth.

#### Level 1, Version B
<!-- audit
2026-05-19:
- Map walls/floors and all 12 boulders A-L match soko4-2.lua:9-21, 29-42.
- Upstair (2,2), branch portal (4,2) (soko4-2.lua).
- 10 pits: 5 at col 2 rows 3-7, plus 5 at row 9 cols 2-6 (soko4-2.lua:48-59).
- 2 rolling-boulder traps at (1,7) and (6,8) (soko4-2.lua:53, 60).
- 2 always-scrolls-of-earth at (2,10) and (3,10) (soko4-2.lua:63-64).
- Level flags noteleport, hardfloor, sokoban, solidify, premapped (soko4-2.lua:7).
- All 16 solution steps land on lua floor with cardinal approach squares.
- Final remainder (boulders D and E) is exact.
-->


```
            111111
   123456789012345
 1 ┌─┬────┐ ┌────┐
 2 │<│@···└─┘····│
 3 │^├┐·AB····C··│
 4 │^││··DE│·F·G·│
 5 │^││····│·····│
 6 │^├┴───┬┘H────┤
 7 │^│    │······│
 8 │↑└────┘······│
 9 │^^^^^←IJKL···│
10 │··┌───┐······│
11 └──┘   └──────┘
```

1. Push A down one square.
2. Push B right to (11,3).
3. Push H down to (10,8).
4. Push J up one square.
5. Finish I.
6. Push L up one square.
7. Finish K, J, H, and L.

The map now looks like this:

```
            111111
   123456789012345
 1 ┌─┬────┐ ┌────┐
 2 │<│>···└─┘····│
 3 │^├┐······BC··│
 4 │^││·ADE│·F·G·│
 5 │^││····│·····│
 6 │^├┴───┬┘·────┤
 7 │^│    │······│
 8 │↑└────┘······│
 9 │@····←·······│
10 │··┌───┐······│
11 └──┘   └──────┘
```

8. Push C down one square.
9. Push B left to (6,3).
10. Push G down one square, then left to (10,5).
11. Finish G.
12. Finish C and F like G.
13. Move B right to (11,3), then down two squares, then left
    to (10,5).
14. Finish B.
15. Move A up one square.
16. Finish A like B.

Two boulders (D and E) remain. The two scrolls at (2,10) and
(3,10) are always scrolls of earth.

<!-- audit
2026-05-19:
- Map walls/floors and all 20 boulders A-T match soko3-1.lua:9-73.
- Both stairs, locked door (27,9), rolling-boulder trap (11,10), 15 hole traps all verified.
- Hole row at row 10 cols 12-26 (soko3-1.lua:59-73); rolling boulder at (11,10) (soko3-1.lua:58).
- Level flags noteleport, sokoban, solidify, premapped (soko3-1.lua:7); no hardfloor on level 2.
- All solution steps land on floor with reachable cardinal approach squares.
- Step 8's "push F up to (3,4)" is required: F at (3,7) seals the N-S corridor through (3,6).
- 15 filled holes match the bowling-alley count; final remainder (B, C, D, I, Q) is exact.
-->
#### Level 2, Version A

```
            11111111112222222222
   12345678901234567890123456789
 1 ┌────┬────┐       ┌─────────┐
 2 │····│····└─┐     │·········│
 3 │··AB│CD···@│     │·········│
 4 │·····E···┌─┘     │·········│
 5 │····│····│       │····<····│
 6 ├─·──┼────┴┐      │·········│
 7 │··F·│·····│      │·········│
 8 │·GH·│I·J·K│      │·········│
 9 │··L·····M·│      │·········│
10 │·NOP│Q··R·└──────┴────────+┤
11 │····│··S·T→^^^^^^^^^^^^^^^·│
12 └────┴──────────────────────┘
```

1. Push E left to (3,4).
2. Push L right to (9,9).
3. Push R right one square.
4. Finish T, S, M, R, K, J, and L.
5. Finish N, O, P, G, and E.
6. Push F left one square.
7. Finish H.
8. Push F up to (3,4).
9. Finish F and A.

Five boulders (B, C, D, I, and Q) remain.

#### Level 2, Version B
<!-- audit
2026-05-19:
- 16-boulder layout and all 22 solution steps verified by simulation against soko3-2.lua.
- Source file is soko3-2.lua (Sokoban .lua numbering runs bottom up; spoiler "Level 2" = second-from-top).
- Map is a stylized but topologically equivalent rendering of soko3-2.lua.
- Level flags noteleport, sokoban, solidify, premapped (soko3-2.lua:7); no hardfloor at this depth.
- Intermediate diagrams at steps 9 and 16 match simulated boulder positions.
- Step 17 (push H left) is necessary, not cosmetic.
- Step 21's "G right 1, D up 1" is gratuitous but harmless: those boulders don't reach a hole.
-->

```
            11111111112222222
   12345678901234567890123456
 1  ┌──┐          ┌─────────┐
 2 ┌┘·@└──────┐   │·········│
 3 │··········│   │·········│
 4 │·A┌───┐B─·│   │·········│
 5 │··│···│·C·│   │····<····│
 6 │·D·E····F─┤   │·········│
 7 │·G··H··│··│   │·········│
 8 │·────I·└┐·│   │·········│
 9 │··J···K·│·└┐  │·········│
10 │·──┐L─···M·└──┴────────+┤
11 │···│··N─·O→^^^^^^^^^^^^·│
12 │··P······┌──────────────┘
13 └───┐··│··│
14     └──┴──┘
```

1. Push B down two squares.
2. Push C left one square.
3. Push P right three squares, then up one square, to (7,11).
4. Finish O.
5. Push N down one square, then left to (3,12).
6. Push M left one square.
7. Push F up one square.
8. Push B left two squares.
9. Push K down two squares.

The map now looks like this:

```
            11111111112222222
   12345678901234567890123456
 1  ┌──┐          ┌─────────┐
 2 ┌┘·>└──────┐   │·········│
 3 │··········│   │·········│
 4 │·A┌───┐·─·│   │·········│
 5 │··│···│CF·│   │····<····│
 6 │·D·E·B···─┤   │·········│
 7 │·G··H··│··│   │·········│
 8 │·────I·└┐·│   │·········│
 9 │··J·····│·└┐  │·········│
10 │·──┐L─@·M··└──┴────────+┤
11 │···│·PK─··→·^^^^^^^^^^^·│
12 │·N·······┌──────────────┘
13 └───┐··│··│
14     └──┴──┘
```

10. Push M right one square, then down to (11,11). Finish M.
11. Push N right to (10,12), then up to (10,10). Finish N
    like M.
12. Push K down one square, then left to (3,12). Finish K
    like N.
13. Push P right one square, then down one square. Finish P
    like N.
14. Push L down two squares, then left to (3,12). Finish L
    like N.
15. Push I down one square, then right one square, then down
    to (8,12). Finish I like N.
16. Push J right to (8,9), then down to (8,12). Finish J
    like N.

The map now looks like this:

```
            11111111112222222
   12345678901234567890123456
 1  ┌──┐          ┌─────────┐
 2 ┌┘·>└──────┐   │·········│
 3 │··········│   │·········│
 4 │·A┌───┐·─·│   │·········│
 5 │··│···│CF·│   │····<····│
 6 │·D·E·B···─┤   │·········│
 7 │·G··H··│··│   │·········│
 8 │·────··└┐·│   │·········│
 9 │········│·└┐  │·········│
10 │·──┐·─·····└──┴────────+┤
11 │···│···─@·→········^^^^·│
12 │·········┌──────────────┘
13 └───┐··│··│
14     └──┴──┘
```

17. Push H left one square.
18. Push B down one square, then right one square, then down
    to (8,12). Finish B.
19. Push C down one square, then left two squares, to (7,6).
    Finish C like B.
20. Push F left one square, then down one square, then left
    to (7,6). Finish F like C.
21. Push G right one square. Push D up one square.
22. Push E right two squares, to (7,6). Finish E like F.

Four boulders (A, D, G, and H) remain.

<!-- audit
2026-05-19:
- 13-boulder layout and all 13 solution steps verified against dat/soko2-1.lua:9-62.
- Upstair (17,5), downstair (7,11), locked door (19,9) all match.
- 10 hole traps at row 10 cols 9-18; rolling-boulder trap at (8,10).
- Level flags noteleport, sokoban, solidify, premapped (soko2-1.lua:7).
- Final "three boulders remain" tally is exact.
-->
#### Level 3, Version A

```
            11111111112
   12345678901234567890
 1 ┌────────┬───┬─────┐
 2 │········│···│·····│
 3 │·AB··─CD│·─·│·····│
 4 │··│·E·F·│GH·│·····│
 5 ├─·│··─··│·─·│··<··│
 6 │···┌─·······│·····│
 7 │···│·I·─···─┤·····│
 8 │·J·│K·│···──┤·····│
 9 ├─L·│··└─────┴────+┤
10 │··M···→^^^^^^^^^^·│
11 │···│·@┌───────────┘
12 └───┴──┘
```

1. Push M left one square. Finish M.
2. Push J right one square.
3. Finish L, J, A, and B.
4. Push D down to (9,6).
5. Finish I.
6. Push K down two squares, then left to (3,10). Finish K.
7. Push E up one square.
8. Push F right one square, then up one square, to (9,3).
9. Push E down one square, then left one square, to (5,4).
10. Push E up one square, then left two squares. Finish E.
11. Push C down one square, then left three squares, to (5,4).
    Finish C like E.
12. Push D right two squares, then left to (8,6).
13. Push D up two squares, then left to (5,4). Finish D like E.

Three boulders (F, G, and H) remain.

#### Level 3, Version B
<!-- audit
2026-05-19:
- Upstair at spoiler (16,7); lua (15,6) (soko2-2.lua:25).
- All 16 boulders A-P map exactly to soko2-2.lua coords.
- Downstair/start at (7,12); rolling-boulder trap at (8,12).
- 11 holes at row 12 cols 9-19; two locked doors at (20,10) and (20,12).
- Level flags noteleport, sokoban, solidify, premapped (soko2-2.lua:7).
- 15 solution steps compress Boudewijn Waijers's original 22; each push geometrically reachable.
- Final "five boulders remain" tally is exact.
-->

```
            1111111111222
   1234567890123456789012
 1   ┌─┬────┐  
 2 ┌─┘·│····│  
 3 │···A····├─┬───────┐  
 4 │·─·BC─DE│·│·······│  
 5 │·FG─······│·······│  
 6 │·─··H·│···│·······│  
 7 │····─I└─J─┤···<···│  
 8 │··KL··M···│·······│  
 9 │·──···│···│·······├─┐
10 │····─N├───┤·······+·│
11 └─┐··O·└───┴───────┤·│
12   │··P@→^^^^^^^^^^^+·│
13   └────────────────┴─┘
```

1. Push O left two squares, to (4,11).
2. Finish P and N.
3. Push L down one square, to (5,9).
4. Push O up one square, to (4,10).
5. Finish L.
6. Push K right one square, to (5,8). Finish K.
7. Push O right one square, to (5,10). Finish O.

The map now looks like this:

```
            1111111111222
   1234567890123456789012
 1   ┌─┬────┐  
 2 ┌─┘·│····│  
 3 │···A····├─┬───────┐  
 4 │·─·BC─DE│·│·······│  
 5 │·FG─······│·······│  
 6 │·─··H·│···│·······│  
 7 │····─I└─J─┤···<···│  
 8 │······M···│·······│  
 9 │·──···│···│·······├─┐
10 │····─·├───┤·······+·│
11 └─┐····└───┴───────┤·│
12   │··@>→····^^^^^^·+·│
13   └────────────────┴─┘
```

8. Push G down to (4,8), then one square right, to (5,8).
   Finish G.
9. Push F one square right. Finish F like G.
10. Push M two squares right, to (10,8), then left to (5,8).
    Finish M.
11. Push J up two squares, to (10,5).
12. Finish I.
13. Push H right one square. Finish H.
14. Push A right two squares, to (7,3).
15. Push C down two squares, to (6,6). Finish C like H.

Five boulders (A, B, D, E, and J) remain.

#### Level 4, Version A

The prize on this version is usually a bag of holding, with a 1
in 4 chance of being an amulet of reflection instead.

<!-- audit
2026-05-19:
- 18-boulder layout and all 19 solution steps verified against dat/soko1-1.lua.
- Player start at lua (1,1) = spoiler (2,2).
- 16 holes plus 1 rolling boulder at row 1: hole col 7, rolling boulder col 8, holes cols 9-23.
- Four chamber passages at lua row 3 col 7, row 6 col 8, row 9 col 5, row 13 col 7.
- Intermediate map after step 13 shows 8 holes filled (F, G, H, I, K, L, M, N).
- Level flags noteleport, sokoban, solidify, premapped (soko1-1.lua:7).
- Final remainder of 2 boulders (A and E) is exact.
- Prize odds: 75% bag of holding, 25% amulet of reflection (soko1-1.lua:102-111).
- "Next to the treasure zoo" chambers at spoiler (17,12) / (17,14) / (17,16); zoo region (18,10)-(22,16).
-->

```
            11111111112222222
   12345678901234567890123456
 1 ┌────────────────────────┐
 2 │@·····^→^^^^^^^^^^^^^^^·│
 3 │·······┌──────────────┐·│
 4 └┬─────·└────┐         │·│
 5  │···········│         │·│
 6  │·A·B·C·D·E·│         │·│
 7 ┌┴──────·────┤         │·│
 8 │···F·G··H·I·│         │·│
 9 │···J········│         │·│
10 └┬───·──────┬┘   ┌─────┤·│
11  │··K·L·M···│  ┌─┤·····│·│
12  │·····N····│  │·+·····│·│
13  │·O·P···Q·┌┘  ├─┤·····│·│
14 ┌┴─────·─┬─┘   │·+·····+·│
15 │··R·····│     ├─┤·····├─┘
16 │········│     │·+·····│
17 │···┌────┘     └─┤·····│
18 └───┘            └─────┘
```

1. Push A left one square.
2. Push B left one square.
3. Push C left one square.
4. Push E right one square.
5. Push D right one square.
6. Push G to (9,8), then up three squares, then left one
   square. Finish G.
7. Finish H and I like G.
8. Push J left two squares, to (3,9).
9. Finish F like G.
10. Push N right three squares, to (11,12).
11. Push L to (6,11), then up three squares. Finish L.
12. Finish M and K like L.
13. Push N left three squares, then up one square, to (8,11).
    Finish N like L.

The map now looks like this:

```
            11111111112222222
   12345678901234567890123456
 1 ┌────────────────────────┐
 2 │>·····@→·······^^^^^^^^·│
 3 │·······┌──────────────┐·│
 4 └┬─────·└────┐         │·│
 5  │···········│         │·│
 6  │A·B·C···D·E│         │·│
 7 ┌┴──────·────┤         │·│
 8 │············│         │·│
 9 │·J··········│         │·│
10 └┬───·──────┬┘   ┌─────┤·│
11  │··········│  ┌─┤·····│·│
12  │··········│  │·+·····│·│
13  │·O·P···Q·┌┘  ├─┤·····│·│
14 ┌┴─────·─┬─┘   │·+·····+·│
15 │··R·····│     ├─┤·····├─┘
16 │········│     │·+·····│
17 │···┌────┘     └─┤·····│
18 └───┘            └─────┘
```

14. Push R to (8,15), then up four squares. Finish R like L.
15. Push Q to (8,13), then down three squares, then left to
    (3,16). Push Q up one square. Finish Q like R.
16. Finish P and O like Q.
17. Push J to (6,9), then down three squares. Finish J like L.
18. Push C to (9,6), then down three squares. Finish C like J.
19. Finish B and D like C.

Two boulders (A and E) remain. There is a bag of holding in one
of the small chambers ((17,12), (17,14), or (17,16)) next to the
treasure zoo.

#### Level 4, Version B

The prize on this version is usually an amulet of reflection, with
a 1 in 4 chance of being a bag of holding instead.

<!-- audit
2026-05-19:
- prize odds: 25% bag of holding, 75% amulet of reflection (soko1-2.lua:105)
- 28-step solution simulates cleanly; final remainder boulder (13,7), sokoban prize (13,8) (soko1-2.lua)
- level flags noteleport, premapped, sokoban, solidify (soko1-2.lua:7); no hardfloor on prize level
- diagonal boulder pushes blocked (hack.c:441-448)
-->

```
            11111111112222222
   12345678901234567890123456
 1   ┌──────────────────────┐
 2   │··→^^^^^^^^^^^^^^^^^^·│
 3   │··┌─────────────────┐·│
 4 ┌─┴┐·│    ┌───┐        │·│
 5 │··│A└┐  ┌┘···│        │·│
 6 │·····├──┤·N··│        │·│
 7 │·BC··│··│··O·│        │·│
 8 └┐··DE│···PQ·┌┘        │·│
 9  │F··G···│R··│   ┌─────┤·│
10  │·HI·│··│··S│ ┌─┤·····│·│
11  │·J·K└──┤·T·│ │·+·····│·│
12  │·······│··┌┘ ├─┤·····│·│
13  └──┐·L··│·┌┘  │·+·····+·│
14     └┬─·─┘·│   ├─┤·····├─┘
15      │·M···│   │·+·····│
16      │@·│··│   └─┤·····│
17      └──┴──┘     └─────┘
```

1. Push M right three squares, then up four squares.
2. Push T up one square.
3. Push S up two squares.
4. Push Q up one square.
5. Push P left three squares.
6. Push G left two squares.
7. Push D up two squares, then left one square.
8. Finish A.
9. Push B up one square.
10. Push C right one square. Finish C.
11. Push B down one square.

The map now looks like this:

```
            11111111112222222
   12345678901234567890123456
 1   ┌──────────────────────┐
 2   │··→·^^^^^^^^^^^^^^^^··│
 3   │··┌─────────────────┐·│
 4 ┌─┴┐·│    ┌───┐        │·│
 5 │··│·└┐  ┌┘···│        │·│
 6 │·@D··├──┤·N··│        │·│
 7 │·B···│··│·QO·│        │·│
 8 └┐···E│P····S┌┘        │·│
 9  │FG·····│R··│   ┌─────┤·│
10  │·HI·│··│·T·│ ┌─┤·····│·│
11  │·J·K└──┤M··│ │·+·····│·│
12  │·······│··┌┘ ├─┤·····│·│
13  └──┐·L··│·┌┘  │·+·····+·│
14     └┬─·─┘·│   ├─┤·····├─┘
15      │·····│   │·+·····│
16      │>·│··│   └─┤·····│
17      └──┴──┘     └─────┘
```

12. Push D right one square. Finish D.
13. Push B right two squares. Finish B.
14. Finish I.
15. Push E down one square, then left one square. Finish E.
16. Push F up three squares, then right two squares. Finish F.

The map now looks like this:

```
            11111111112222222
   12345678901234567890123456
 1   ┌──────────────────────┐
 2   │·@→······^^^^^^^^^^^··│
 3   │··┌─────────────────┐·│
 4 ┌─┴┐·│    ┌───┐        │·│
 5 │··│·└┐  ┌┘···│        │·│
 6 │·····├──┤·N··│        │·│
 7 │·····│··│·QO·│        │·│
 8 └┐····│P····S┌┘        │·│
 9  │·G·····│R··│   ┌─────┤·│
10  │·H··│··│·T·│ ┌─┤·····│·│
11  │·J·K└──┤M··│ │·+·····│·│
12  │·······│··┌┘ ├─┤·····│·│
13  └──┐·L··│·┌┘  │·+·····+·│
14     └┬─·─┘·│   ├─┤·····├─┘
15      │·····│   │·+·····│
16      │>·│··│   └─┤·····│
17      └──┴──┘     └─────┘
```

17. Push G right one square. Finish G.
18. Finish H and J like G.
19. Push P down one square, then left three squares, to (5,9).
    Finish P.
20. Push K to (6,9), then left one square. Finish K.
21. Push L right one square, then up one square, then left two
    squares. Finish L like K.

The map now looks like this:

```
            11111111112222222
   12345678901234567890123456
 1   ┌──────────────────────┐
 2   │·@→············^^^^^··│
 3   │··┌─────────────────┐·│
 4 ┌─┴┐·│    ┌───┐        │·│
 5 │··│·└┐  ┌┘···│        │·│
 6 │·····├──┤·N··│        │·│
 7 │·····│··│·QO·│        │·│
 8 └┐····│·····S┌┘        │·│
 9  │·······│R··│   ┌─────┤·│
10  │····│··│·T·│ ┌─┤·····│·│
11  │····└──┤M··│ │·+·····│·│
12  │·······│··┌┘ ├─┤·····│·│
13  └──┐····│·┌┘  │·+·····+·│
14     └┬─·─┘·│   ├─┤·····├─┘
15      │·····│   │·+·····│
16      │>·│··│   └─┤·····│
17      └──┴──┘     └─────┘
```

22. Push T down one square.
23. Push R to (11,8), then left three squares. Finish R like P.
24. Finish M like R.
25. Push T left one square. Finish T like R.
26. Push N right one square.
27. Push Q down to (12,9), then left one square. Finish Q
    like R.
28. Push N left one square. Finish N like Q.

Two boulders (O and S) remain. There is an amulet of reflection
in one of the small chambers ((17,11), (17,13), or (17,15)) next
to the treasure zoo.

---

### Voluntary Challenges

> *The conduct system is documented in Dion Nicolaas's Conduct
> Spoiler, originally posted to RGRN and archived at steelypips.org.
> The information below has been updated for 5.0 of
> the Mazes.*

The game tracks a set of optional self-imposed restrictions called
**conducts**. You can check which ones you've maintained at any time
with `#conduct`. When you die or ascend, the end-of-game summary
lists every conduct you kept. No conduct is required for victory;
they exist for players who want a harder game or a more impressive
ascension.

Conducts are not declared in advance. The game simply watches your
actions and records whether you've broken each restriction. If you
eat a corpse on turn 1, you've broken foodless, vegan, and
vegetarian for the rest of the run. There's no going back.

#### The Food Conducts
<!-- audit
2026-05-19:
- vegetarian-safe puddings: gray ooze, brown pudding, green slime; not black pudding (mondata.h:241)
- no yellow pudding exists (monsters.h:2081-2113)
- puddings are G_NOCORPSE and leave globs, not corpses
- shriekers are S_FUNGUS, already covered by "all F (fungi and molds)"
- vegan-violating VEGGY foods: eggs, pancakes, royal jelly, cream pies, candy bars, fortune cookies (eat.c:3016-3018)
- fortune cookies contain eggs, so they break vegan
- ghosts are G_NOCORPSE; ghost corpses don't exist (monsters.h:2888,2897)
- watch out for: yellow mold, violet fungus, acid blob — vegetarian-by-macro but unsafe to eat (yellow mold M1_POIS monsters.h:1638; violet fungus AT_TUCH AD_STCK monsters.h:1670; acid blob AD_ACID monsters.h:139; eat.c:1303-1308 violet fungus corpse hallucinates)
- polymorph does NOT break foodless: polyself.c has no u.uconduct.food increment (polyself.c:750-751 only increments u.uconduct.polyselfs)
- prayer cures hunger at Hungry/Weak/Fainting (pray.c:275, uhs >= HUNGRY)
- wishing for slow digestion is a viable foodless route
- Monk: vegetarian is nearly free
- strategy aligned with NetHackWiki Conduct, Foodless, Veggy: vegetarian/vegan/foodless hierarchy and the slow-digestion / prayer / stone-to-flesh strategy for foodless are canonical (https://nethackwiki.com/wiki/Conduct, https://nethackwiki.com/wiki/Foodless, https://nethackwiki.com/wiki/Veggy)
-->

These form a hierarchy: foodless is stricter than vegan, which is
stricter than vegetarian.

**Vegetarian.** Don't eat meat. Specifically, don't eat the corpses
of non-vegetarian monsters, and avoid items made from animal
products (meat sticks, eggs from carnivorous creatures). In
practice, this means living on permissible corpses and globs.
Lichens, jellies, fungi and molds, and gray ooze or brown pudding
globs are all safe. Fortune cookies, lembas wafers, and whatever
vegetable food you find on the ground also work. Green slime is
technically vegan, but eating its glob slimes you. The vegetarian
monster list is broader than you might expect: all `b` (blobs),
all `j` (jellies), all `F` (fungi and molds), all `v` (vortices),
all `y` (lights), all `E` (elementals) except stalkers, and all
`'` (golems) except flesh and leather golems. Many [vegetarian
corpses grant useful intrinsics](#vegetarian-safe-corpses).
Vegetarian-safe is not the same as safe. Yellow mold corpses
poison, violet fungus paralyzes, and acid blobs sting going down.
Monks are a good role to play vegetarian; they already pay an
alignment penalty for meat.

**Vegan.** Follow all vegetarian restrictions, plus avoid eating
eggs, pancakes, lumps of royal jelly, cream pies, candy bars, *and*
fortune cookies. (Yes, fortune cookies are vegetarian-safe but not
vegan-safe. They contain eggs.) The conduct fires only on *eating*:
carrying or using animal-derived items is fine, so vegans can still
light the Candelabrum with wax or tallow candles, wear leather
armor, and apply bone horns. Vegan also excludes puddings.

**Foodless.** Don't eat anything at all. Your only nutrition
sources are prayer (which cures hunger from Hungry status onward,
not just Weak/Fainting), the spell of stone to flesh on rocks in
your inventory (which creates meatballs, but eating them breaks
the conduct), and a ring of slow digestion (which slows hunger
almost to a halt). Most foodless runs rely on finding a ring of
slow digestion early or praying through hunger until one appears.
Wishing for the ring is the usual plan if a wand of wishing or
magic lamp turns up. Chewing through walls also breaks this
conduct (it counts as eating rock).

#### Atheist
<!-- audit
2026-05-19:
- Atheist tracks u.uconduct.gnostic (insight.c:2134, topten.c:590)
- breaks on: #pray (pray.c:2221), #offer corpse (pray.c:1977), #turn (pray.c:2426), #chat with priest (priest.c:572)
- dropping any non-coin on an altar breaks the conduct via the BUC flash (do.c:370)
- final Amulet offering for ascension is exempt (pray.c:1529-1588 has no gnostic increment)
- Priest's starting holy water does NOT auto-break the conduct (u_init.c:716-722)
- strategy aligned with NetHackWiki Atheist: no prayer / sacrifice / chat-with-priest / altar drops; final ascension Amulet offering is exempt (https://nethackwiki.com/wiki/Atheist)
-->

Don't interact with the divine. Specifically: don't `#pray`, don't
`#offer` corpses at altars, don't `#turn` undead, and don't `#chat`
with priests. The altar BUC flash also counts: any non-coin item you
drop on an altar increments the conduct counter, so the original
identification trick is off-limits too. This removes your safety net
for starvation, stoning, illness, and cursed items. You'll need to
solve every problem through items and knowledge alone.

Atheist runs require careful resource management. Without prayer to
cure hunger, you need reliable food sources. Without sacrifice or
altar BUC, identification is harder and you'll get no artifact gifts.
The final Amulet offering for ascension is exempt, so a clean
atheist ascension is mechanically possible.

#### Weaponless
<!-- audit
2026-05-19:
- weaphit++ requires weapon non-NULL AND (WEAPON_CLASS OR is_weptool) (uhitm.c:616-617)
- weapon-tools that break: pick-axe, unicorn horn, other is_weptool items
- wielded polearm at range via #apply DOES break (HMON_APPLIED, dothrow.c:2199-2203)
- do NOT break: thrown weapons, fired ammo, wands, spells, barehand, martial arts, cockatrice-corpse-wield
- iron chain is CHAIN_CLASS, not a weptool; swinging it does NOT break (objects.h:101, 1631)
- aklys is WEAPON_CLASS, not a weptool; it breaks via the WEAPON_CLASS branch (objects.h:381-383)
- strategy aligned with NetHackWiki Weaponless, Martial arts: thrown/fired weapons and martial arts preserve the conduct, wielded-polearm-#apply still breaks it (https://nethackwiki.com/wiki/Weaponless, https://nethackwiki.com/wiki/Martial_arts)
-->

Never hit a monster with a wielded weapon or weapon-tool. You can
throw weapons, fire them from bows and crossbows, and use wands
and spells. You can also fight bare-handed or with martial arts
(Monks excel here). What you cannot do is swing a sword, axe,
mace, aklys, pick-axe, unicorn horn, or any other weapon-class or
weapon-tool item in melee while it's in your `w`ielded slot. The
one ranged exception that *does* break the conduct: using a
wielded polearm at range via `#apply`.

This is less restrictive than it sounds. Monks start with strong
martial arts and get better. Other classes can rely on spells,
wands, and thrown daggers. A wielded cockatrice corpse still works
(it's not a weapon). The main sacrifice is giving up the damage
output of late-game artifact weapons.

#### Pacifist
<!-- audit
2026-05-19:
- Pacifist tracks u.uconduct.killer; only xkilled (mon.c:3500) and pet-pushed-into-trap (hack.c:2201) increment
- pet kills and conflict kills do NOT break the conduct: xkilled() only increments on !noconduct branch (mon.c:3499-3502)
- charm-monster spell, Elbereth, and pet tactics are all safe (no killer++ in those code paths)
- strategy aligned with NetHackWiki Pacifist, Conflict: pacifist runs lean on strong pets (often polymorph-amplified) and a ring of conflict for crowds (https://nethackwiki.com/wiki/Pacifist, https://nethackwiki.com/wiki/Conflict)
-->

Don't kill any monsters. Not directly, not with pets, not through
any means that the game attributes to you. The pacifist runs on
pets doing the fighting, on conflict to make monsters attack each
other, on [Elbereth](#elbereth) to keep them at bay, and on creative use of
the dungeon environment.

Pacifist ascensions are possible but require deep knowledge of the
game's mechanics. The canonical late-game plan is a
**figurine of an Archon** (wished, broken, then re-tamed if it
turns hostile) as your champion fighter, the spell of *charm
monster* for crowd pacification, and a ring of conflict for fights
you can't talk your way out of.

#### Illiterate
<!-- audit
2026-05-19:
- only an "x" or "X" signature engrave is exempt; everything else breaks the conduct (engrave.c:1213)
- breaks: scrolls, spellbooks, fortune cookies, T-shirts, magic-marker writing (read.c:602, eat.c:2525, read.c:397, write.c:245)
- do NOT break: blank paper, unread novels, Book of the Dead, Hawaiian shirts, reading floor engravings (Elbereth)
- pet-on-scroll workaround for identifying scrolls is safe
- Wizard/Priest/Healer/Monk/Knight keep one pre-learned spell until it fades, ~20K turns (spell.h:17 KEEN)
- strategy aligned with NetHackWiki Illiterate: only an "x"-signature engrave is safe, scroll of scare monster is the rare exception that doesn't break the conduct (https://nethackwiki.com/wiki/Illiterate)
-->

Don't read anything. No scrolls, no spellbooks, no fortune cookies,
no T-shirts. You also can't engrave anything more than a single
"x" or "X" (the traditional illiterate's signature). You don't lose the conduct if you read blank scrolls or
spellbooks, or Hawaiian shirts, the Book of the Dead, or messages
already engraved on the floor.

Without scrolls, you lose access to identify, enchant weapon/armor,
teleportation, remove curse, and genocide in their most common
forms. Without spellbooks, you can't learn new spells or refresh
old ones, so any starting spell you have will eventually fade. This
forces extreme reliance on wands, potions, and creative workarounds.
The standard workarounds are **pet-step BUC testing** (does the dog
walk over it?) and **price-ID** (looking at a shopkeeper's quote
doesn't count as reading), which together cover most of the ID
table that scroll of identify would have handled.

#### No Genocide
<!-- audit
2026-05-19:
- genocide is only prompted by scroll of genocide and by sitting on a regular throne; wishes never offer it (do_genocide callers: read.c:1735-1737 SCR_GENOCIDE and sit.c:131 throne only)
- uncursed scroll: single species; blessed scroll: whole class (do_class_genocide, read.c:2638)
- throne prompt is single-species only: case 8 of 13 in throne_sit_effect, calls do_genocide(5) (sit.c:125-132)
- Vlad's tower thrones take a different path with no genocide case (special_throne_effect, sit.c:63-66)
- on a cursed scroll, empty input re-prompts and rndmonst() creates monsters; type "none" to escape (read.c:2848-2871)
- end-of-game tracking counts G_GENOD species in mvitals[], not a u_conduct counter (insight.c:2951-2966 num_genocides)
- cursed-scroll monster-creation preserves the conduct (no species gets G_GENOD'd)
- strategy aligned with NetHackWiki Genocide, Throne: answer "none" at the prompt, throne genocides are always safe, Plane of Water class-`;` wipe is off-limits for genocideless (https://nethackwiki.com/wiki/Genocide, https://nethackwiki.com/wiki/Throne)
-->

Never genocide any monster. Genocide is prompted by reading a
**scroll of genocide** (uncursed picks one species; blessed wipes
the whole class) and by **sitting on a throne**: one outcome in
the throne-effect table (case 8 of 13) prompts you to genocide a
single species. To preserve the conduct, type **"none"** at the
prompt — don't just press Enter, because empty input re-prompts
and on a *cursed* scroll the game will eventually conjure random
monsters instead of letting you escape.

This means you'll face the full bestiary throughout the game,
including master and arch-liches, mind flayers, cockatrices, and
everything else that experienced players routinely eliminate.
You'll also have to cross the **Plane of Water** the hard way: the
standard tactic of genociding class `;` to clear out the eels and
krakens is off-limits, so bring magical breathing and pay attention
to where the sea monsters can reach you.

This is one of the milder conducts: many players ascend without
genociding anything simply because they never find the scroll and
never roll case 8 on a throne. But deliberately maintaining it
against late-game threats takes discipline.

<!-- audit
2026-05-19:
- no SCR_POLYMORPH exists in 5.0; "cursed scroll of polymorph" is not a thing (objects.h:1187-1265 scroll list has no polymorph entry; no SCR_POLYMORPH token anywhere in source)
- breaks: genetic engineer claw (AD_POLY -> polyself)
- breaks: eating chameleon, doppelganger, or mimic corpses (eat.c:1244-1263, eat.c:1199)
- breaks: green slime auto-poly (timeout.c:493)
- breaks: stone-golem auto-poly via poly_when_stoned (trap.c:3848)
- Unchanging blocks all polymorph; system shock does NOT break the conduct (polyself.c:483-495)
- sandestins are G_NOCORPSE; their corpses are unreachable (eat.c:1246)
- poly_when_stoned only fires if already polymorphed into a non-stone golem; normal characters die (mondata.c:80-86)
- strategy aligned with NetHackWiki Polymorph, Amulet of unchanging, Polypiling: Unchanging blocks every involuntary path, polypileless forfeits the polypile item-generation trick (https://nethackwiki.com/wiki/Polymorph, https://nethackwiki.com/wiki/Amulet_of_unchanging, https://nethackwiki.com/wiki/Polypiling)
-->
#### Polymorph Restrictions

Two related conducts track polymorphing:

**No polymorph.** Never let your form change. Obvious sources: potion
or ring of polymorph, wand or spell of polymorph (zapped at you), and
polymorph traps. Less obvious: a genetic engineer's claw; eating a
chameleon, doppelganger, or mimic corpse; and failing to cure
slimedness (turns you into a green slime). The Amulet of Unchanging
blocks every path. A failed system shock does *not* break the
conduct. Keeping this conduct forgoes the advantages of powerful
monster forms (master mind flayer, xorn, various dragons).

**No polymorph objects.** Never polymorph items. Don't zap items
with a wand of polymorph, don't dip items in potions of polymorph,
and avoid other means of transforming objects. This eliminates a
powerful item-generation strategy (polypiling) that many players use
to obtain specific high-value items.

#### Wishing Restrictions
<!-- audit
2026-05-19:
- u.uconduct.wishes and u.uconduct.wisharti are separate counters with separate xlogfile achievements (you.h:157-158, topten.c:596-597)
- wishing for the literal string "nothing" doesn't tick the counter (zap.c:6369)
- Amulet-of-Yendor first-pickup wish must be declined for wishless (allmain.c:445)
- wisharti ticks even for DENIED artifact wishes: increment is before the deny branch (objnam.c:5362-5365)
- fountain water demon routes through mongrantswish -> makewish
- wresting empty wands routes through makewish (zap.c:2583)
- strategy aligned with NetHackWiki Conduct, Wish: wishless vs no-wishing-for-artifacts are separately tracked, "nothing" is the canonical escape for a forced wish (https://nethackwiki.com/wiki/Conduct, https://nethackwiki.com/wiki/Wish)
-->

Two related conducts:

**Wishless.** Never make a wish. Refuse wishes from wands, fountains,
smoky potion djinn, thrones, and all other sources. **Picking up
the Amulet of Yendor also triggers a wish prompt**: wish for "nothing"
(the literal string) and the counter doesn't tick. Wishing for
"nothing" is the standard escape hatch for any forced wish — keep
it in mind whenever something hands you an unwanted wish. This is
extremely challenging because wishes are the primary way to obtain
critical items (silver dragon scale mail, speed boots, a bag of
holding) when the dungeon doesn't provide them.

**No wishing for artifacts.** Make wishes, but never wish for an
artifact. This prevents the most efficient wish strategy (wishing
for Grayswandir, the Eye of the Aethiopica, or similar game-changing
artifacts) while still allowing wishes for mundane necessities. The
counter ticks even for *denied* artifact wishes (when the game
gives you "something in your hand" instead), so be sure you can
get the artifact before asking.

#### Combining Conducts
<!-- audit
2026-05-19:
- Pauper does NOT suppress the starting pet; makedog() only returns NULL on pettype:none (dog.c:219-229)
- Pauper's u_init.c:1308-1309 short-circuits ini_inv (items only, not pet creation)
- dog.c:262-267 skips the pony saddle for Pauper but still grants the pony
- only OPTIONS=pettype:none can skip the starting pet
- nudist and blind have been tracked since 3.6
- 5.0 added pauper, petless, permadeaf, sokoban, bonesless
- vegan is a strict subset of vegetarian
- all conducts appear in the show_conduct end-screen
-->

The real prestige comes from combining multiple conducts. A
vegetarian atheist run is substantially harder than either alone.
A pacifist illiterate vegan foodless atheist weaponless run is
the stuff of legends (and has been done). The game's end screen
lists all maintained conducts, and the community has long
celebrated players who push the boundaries of what's possible
within self-imposed constraints. For scale: on the public NAO
server, about one in nine ascensions is wishless, and only one
in eighty is foodless.

Recent editions of the Mazes have added several more tracked
conducts:

**Nudist.** Never wear any armor, shirt, cloak, gloves, boots,
helmet, or shield. Set the `nudist` option at game start. You
fight the entire dungeon in your underwear. Officially tracked
since 3.6.

**Blind (Zen).** Play the entire game without sight. Set the
`blind` option at game start. You'll need telepathy and other
senses to navigate. Officially tracked since 3.6.

Mazes 5.0 added five more tracked conducts: Pauper, Petless,
Permadeaf, Sokoban, and Bonesless. Pauper, Permadeaf, Petless, and
Bonesless are start-of-game options (you opt in or out before
play). Sokoban is tracked automatically based on what you do
during the run.

#### Pauper (new in 5.0)
<!-- audit
2026-05-19:
- Pauper is set_in_config: rcfile or NETHACKOPTIONS env only, not in-game O menu (optlist.h:559)
- ini_inv early-return suppresses starting items only, not the pet (u_init.c:1308-1309)
- Pauper does NOT suppress the starting pet (dog.c:219-229; only pettype:none does)
- dog.c:262-267 skips the pony saddle for Pauper
- Cleric, Knight, Monk start knowing SPE_PROTECTION (pauper_reinit, u_init.c:890-922)
- Cave Dweller starts knowing FLINT (pauper_reinit, u_init.c:890-922)
- Protection book is a load-bearing early-game pickup for those three roles
- nudist cascade triggers when pauper is set (options.c:5290-5293)
- end-of-game string at insight.c:2117-2119; xlogfile at topten.c:604
-->

Start with absolutely nothing: no gold, no inventory, no armor, no
starting weapon. Set `OPTIONS=pauper` in your rcfile (rcfile or
`NETHACKOPTIONS` env only; the in-game `O` menu cannot toggle it). Pauper
implicitly sets nudist as well, so you also begin without armor.
Pauper is a permanent conduct you never lose: it does not forbid
acquiring or spending gold later. The conduct is about starting
empty, not about staying penniless.

To keep the start from being impossible, the game compensates:
you get two unspent weapon-skill slots and your role knows one
signature spell or item. Wizard knows force bolt; Healer knows
healing; Cleric, Knight, and Monk all know protection (Cleric
also knows water); Archeologist knows touchstone; Cave Dweller
knows flint; Rogue and Tourist know sack; Samurai knows gunyoki
rations. The supply chests on early levels (see [What to
Pack](#what-to-pack)) can provide much of your first kit.

#### Petless (new in 5.0)
<!-- audit
2026-05-19:
- pettype:none bypasses pet_type (dog.c:225-229)
- tamedog increments u.uconduct.pets across all taming paths
- the endgame angel preserves petless (minion.c:533-539)
- xlogfile achievement "petless" via add_achieveX (topten.c)
- "dairy to foocubi" is fabricated: befriend_with_obj gates on is_domestic, and foocubi aren't (mondata.h:255-261)
- foocubus + ring of adornment is pacification, not taming (mhitu.c doseduce only reads mon->mtame at 2263 and mon->mpeaceful at 2279; never sets mtame nor calls tamedog)
- food thrown at hostile dogs and cats IS a taming path that breaks petless (dothrow.c:2268-2269 routes to tamedog)
-->

Never have a pet. Set `OPTIONS=pettype:none` in your rcfile to skip
the starting companion entirely (this overrides per-role defaults).
After that, you lose the conduct the moment anything becomes tame.
The game won't stop you — scrolls of taming, the charm monster
spell, food thrown at hostile dogs and cats, and magic-trap
accidents all still work. Each one just breaks Petless on the
spot.

#### Permadeaf (new in 5.0)
<!-- audit
2026-05-19:
- permadeaf is u.uroleplay.deaf, in xlogfile (topten.c:602) and show_conduct (insight.c:2113)
- Deaf macro at youprop.h:125
- rcfile option name is `permadeaf` (or `deaf`), NOT `!acoustics` (a different flavor flag, flags.acoustics) (optlist.h:267-269 declares `deaf` with alias "permadeaf" binding u.uroleplay.deaf; optlist.h:143-145 declares `acoustics` binding flags.acoustics — separate flag)
- permadeaf is set_in_config: rcfile only, not in-game O menu (options.c:5207)
- there is no `-Dpermadeaf` syntax; `-D` is the debug/wizard-mode flag (unixmain.c:359-365)
- Deaf only suppresses shrieker MESSAGES; makemon and aggravate still run (mon.c:4089-4106)
-->

Never hear anything. Set `OPTIONS=permadeaf` (or `OPTIONS=deaf`)
in your rcfile. This option is set-in-config only; the in-game
`O` menu cannot toggle it. (Don't confuse `permadeaf` with the
unrelated `acoustics` flavor toggle, which doesn't earn the
conduct.) The game then runs as if you had the Deaf intrinsic
from turn one and never recovered: all the "you hear water
falling", "you hear someone counting money", "you hear a door
open" messages and the ambient monster sounds ("you hear a
slurp" and friends) are suppressed.

The catch: only the *messages* are suppressed. A shrieker still
shrieks and still summons monsters and aggravates the level —
you just don't get the warning that it happened. Treat empty
silence near a `F`-class monster as the same threat as the usual
SCREECH.

Many monster warnings, environmental cues (vaults, fountains, doors
opening off-screen), and status messages arrive as sounds. Permadeaf
requires navigating the dungeon by sight and logic alone, which turns
out to be possible and occasionally educational about how much
information you normally get for free.

#### Sokoban (new in 5.0)
<!-- audit
2026-05-19:
- digging does NOT trigger sokoban_guilt; dig.c has no such call (sokoban_guilt callers limited to hack.c:299/307/398/403, read.c:1951, steed.c:767, zap.c:1711/5556 — none in dig.c)
- breaks: squeeze through (hack.c:299, 307), boulder fracture by wand of striking (zap.c:5556)
- breaks: polymorph a boulder (zap.c:1711), scroll of earth (read.c:1951), dismount onto a boulder (steed.c:767)
- each violation costs -1 Luck and increments u.uconduct.sokocheat (trap.c:7039-7054)
- achievement reported only if the branch was entered (insight.c:2215-2228)
- teleportation is blocked by the level's noteleport flag (teleport.c:1185); it's a level constraint, not a conduct trigger
-->

Complete Sokoban without breaking the rules. Each cheating action
costs **1 point of Luck** and increments the conduct counter: pushing
into a wall to **squeeze past** a boulder (when you drop your stuff
to fit), **fracturing** a boulder with a wand of striking or scroll
of earth, **polymorphing** a boulder, or **dismounting** onto a
boulder. Flying and levitation don't let you skip Sokoban's pit
traps — the air currents pull you down regardless. The game
tracks violations automatically. The conduct is for players who
enjoy Sokoban's
boulder-shoving and want their playthrough to acknowledge a
clean solve.

#### Bonesless (new in 5.0)
<!-- audit
2026-05-19:
- bonesless achievement requires !flags.bones; you must turn bones loading off (topten.c:605)
- not encountering bones is a separate Miscellaneous enlightenment line, NOT the conduct (insight.c:439)
- you cannot get bonesless by luck alone
- show_conduct never lists lifesaving uses; there is no amulet-of-life-saving tracking (insight.c:2089-2200 show_conduct enumerates rerolling/food/atheist/weaphit/pacifist/illiterate/pets/genocides/polypiles/polyselfs/wishes — no lifesaving counter; u.uconduct has no lifesave field)
- `bones` is set_in_config: config file or command line only, not in-game O menu (optlist.h:213-215)
- !flags.bones blocks both save (bones.c:360) and load (bones.c:642) — cuts both directions
- "never encountered any bones levels" enlightenment requires flags.bones true AND u.uroleplay.numbones==0 (insight.c:439-441)
-->

Never inherit from another player's grave. To get the bonesless
conduct, you have to turn bones off for the run: set
`OPTIONS=!bones` in your rcfile (rcfile or `NETHACKOPTIONS` env
only; the in-game `O` menu cannot toggle it). The same flag also stops
your *own* death from generating a bones file for future players,
so `!bones` cuts both directions of the bones cycle. The bonesless
achievement is recorded only when bones was disabled, not when
you happened not to encounter any. (Going a whole game without bones because the
dungeon directory has nothing eligible is a separate enlightenment
line — "never encountered any bones levels" — and doesn't earn
the conduct.)

---

### Shopping and Shopkeeper Pricing
<!-- audit
2026-05-19:
- 22 gem prices, Mohs hardness, hard-gem threshold >=8 verified (objects.h, shk.c)
- unidentified gem sell price: (tmp+3)*quan, tmp 0..divisor-1, min 3 zm (shk.c:3168-3172)
- dunce cap and low-XL Tourist (or visible touristy shirt) each multiply buy by 4/3 (shk.c:2947-2951)
- angry-shopkeeper surcharge adds (price+2)/3 per billed item, ~33% (shk.c:1365-1373)
- Charisma price tiers: ACURR>18 halves, =18 multiplier 2/3, 16-17 3/4, <=5 doubles, 6-7 3/2, 8-10 4/3 (shk.c:2953-2964)
- shopkeeper anti-Elbereth, see-invisible, Keystone Kops, "Closed for inventory", Orcus-level death verified (shk.c)
- amethyst dipped in booze yields fruit juice (potion.c:2161), NOT a hallucination cure
- shop walls ARE diggable from inside: dig.c:488-501 converts to door, shopkeeper bills SHOP_WALL_DMG and chases (shk.c:5061-5078)
- touchstone full-name ID requires blessed (or non-cursed for Archeologist/Gnome); uncursed gives only streak color (apply.c:2744-2751)
- touchstone hardness is irrelevant: works on all gems
- glass gems do NOT take the is_gem branch in unicorn gift handling — Luck never changes either direction (dothrow.c:2319, 2358-2368)
-->

Shops do more than sell: their pricing system is your most
powerful identification tool. You can find full mechanics and
interactive price tables in Part Four,
[The Price Is Right](#the-price-is-right). What follows here is
the rest: credit, debt, combat, and non-obvious rules.

#### Credit and Debt

Each shopkeeper keeps a per-customer ledger with three numbers:
credit, debit, and loan. The most common confusion is around credit,
so spell out exactly when it appears.

**How you get credit.** Two ways, neither automatic for a successful
sale:

1. **Shopkeeper runs short of gold while paying you.** When you sell
   an item, the shopkeeper pays in gold by default. If they don't
   have enough gold to cover the offer, the game prompts:
   "Shopkeeper cannot pay you at present. Will you accept *N*
   zorkmids in credit for that?" Answering yes converts the
   shortfall (or the whole price, if they have zero gold) into
   credit. A *normal* sale where the shopkeeper has enough gold
   just pays you in cash, no credit involved.
2. **You drop gold on a shop floor square.** Any gold you drop or
   throw inside the shop is added to your credit balance (after
   paying off any existing debt first). This is the "shop as
   safe-deposit box" trick: credit can't be stolen by nymphs,
   can't fall into pits, and can't be lost to a polymorph trap.

**How credit gets used.** When you buy something, the shopkeeper
applies your credit against the purchase price first ("the price is
deducted from your credit"). Any remainder comes out of your gold.
Credit is per-shop and per-shopkeeper, and cannot be withdrawn back
to gold.

**Is paying from credit better or worse than paying in gold?** The
price itself is identical: credit is deducted from the *post-
Charisma, post-Tourist, post-angry* cost at a strict 1:1 ratio, with
no markup or discount either way. The differences are about how
*safe* and *liquid* your money is, not how far it stretches:

- **Better** in that credit can't be stolen by nymphs, can't fall
  into a pit when you die, can't be lost to a polymorph trap, and
  doesn't bog you down with carry weight. A shop you'll come back
  to is a strong bank.
- **Worse** in that credit is locked to one shopkeeper. If you
  over-accumulate at a shop that doesn't have items you want (or
  the shopkeeper dies, or you anger them and they go hostile),
  the credit evaporates. You also can't tip altar donations, can't
  pay shrine fees, and can't bribe a demon out of credit.

Practical balance: park spare gold as credit at a shop you intend
to keep visiting (the Gnomish Mines general store is a popular
choice), but don't deposit more than you expect to spend there.

(A more inventive use, called *credit cloning*: drop gold inside
the shop, then lure a gold-loving monster — an orc, a leprechaun —
to pick it up, walk it outside, and kill it. The credit stays with
the shopkeeper and the gold comes back to you. It's one of
NetHack's older shop-cheese routines.)

**Debit** is the inverse: it accrues when you *use* an unpaid item
inside the shop (read a scroll, quaff a potion, zap a wand) and you
haven't completed the purchase. You're charged a fraction of the
item's price as a usage fee; future gold drops or sales pay it down
before any new credit accumulates.

**Loan** appears only in the unusual case where the shopkeeper has
*lent* you gold: you carry their coins as part of your inventory.
Dropping gold in the shop pays this off before adding credit.

**Walk-out hazard.** Leaving the shop with unpaid items or unpaid
debt turns the shopkeeper hostile. The Keystone Kops will pursue
you through the dungeon, and the shopkeeper themselves is one of
the toughest melee NPCs in the game: high HP, low AC, and
unfazed by [Elbereth](#elbereth). Pay the bill at the door.

#### Shopkeeper Behavior

A shopkeeper is one of the toughest NPCs in the game: high HP,
good AC, hits hard, and unfazed by Elbereth or by the kind of
clever escape that works on other monsters. They also see
everything — they track every item you pick up and every item
that enters the shop, even when you're invisible. The practical
consequences for the player:

- Shopkeepers block the door whenever you have unpaid items.
- If you break something in the shop (a potion, a wand), you pay
  for it.
- Digging through a shop wall or floor doesn't escape the bill.
  The dig works, but the shopkeeper bills you for wall damage and
  the chase happens anyway. Tunnel-out is no shortcut.
- Artifact items are priced at special high prices. For most named
  weapons that lands in the 10,000–30,000 zm range. An unidentified
  long sword priced at 16,000 zm is not something to glance over:
  that exorbitant price is a give-away.
- A shopkeeper *can* be killed for the entire stock plus the till
  (1,000–4,000 zm and a skeleton key on death), but they're a tough
  fight, and killing
  them summons a wave of Keystone Kops to pursue you, and costs you
  a chunk of alignment.
  Two techniques worth knowing: **polymorphing the shopkeeper
  first** (via wand or trap) means killing them no longer counts as
  murder, which is the preferred approach for Lawful and Neutral
  characters. And **chaotic humans** can sacrifice the shopkeeper's
  corpse on an unaligned altar to convert it, which is a niche but
  real motive. Strong late-game players sometimes do clear shops
  anyway, but it's not a casual mid-game move.

Beyond the rules, a few tactical habits pay off:

- **Drop everything at the door to see your bill.** Standing on
  the door square, drop your whole inventory; the shopkeeper's
  bill highlights the items you owe for. The shopkeeper isn't
  guessing — the game tracks unpaid items precisely — but it's a
  handy way to recall what you actually picked up when the shop
  has a hundred lookalikes.
- **Sell to build credit.** Credit acts as gold you can spend in
  that shop, and credit doesn't get stolen by nymphs or fall into
  pits. Selling a stack of useless daggers to a weapon shop is a
  way to "bank" gold safely while you're shopping in town.
- **Bones-shop gotcha.** When you find a shop in someone's bones
  file, all the items inside still belong to the dead adventurer's
  ghost shopkeeper; pick up anything and you owe the new
  shopkeeper full price. The shop floor is not free loot.
- **"Closed for inventory" engraving on a door.** This marks a
  shop whose door spawned **locked**, not an abandoned one. The
  shopkeeper is still inside, the stock is still unpaid, and
  breaking the door down to get in just earns you a normal shop
  visit plus an angry shopkeeper. (In Orcus Town the shopkeepers
  are usually dead by the time you arrive — Orcus killed them —
  so the items there often *are* ownerless.)

The best strategy is usually to play fair: sell what you don't need,
buy what you do, and use the pricing system to identify as much as
possible before spending your gold on scrolls of identify.

#### Gem Identification Through Selling

Selling unidentified gems is **not** a reliable price-ID method.
Shopkeepers offer 3 to 8 zm for any unidentified gem, real or
glass alike, and the exact amount varies by both the gem's true
identity and the shopkeeper. Real diamonds and worthless glass
diamonds both quote in the same 3-8 zm range; you cannot tell
them apart by price. Selling the same gem at two different shops
gives different prices for *any* unidentified gem, not just glass.

The practical method is a **touchstone** (gray stone, base price 45,
guaranteed at Mine's End and sometimes found elsewhere). Rubbing an
unidentified gem against a **blessed** touchstone names the gem
outright; with a merely uncursed touchstone you only get a streak
color. (Archeologists and Gnomes get the full name from a non-cursed
stone, a racial perk.) Hardness doesn't matter; every gem works.
Once identified, real gems sell for their real value (often hundreds
of zm each) while glass sells for almost nothing.

##### Real-gem prices

Once you know what a gem is, its type determines its base price.
Real gems are tiny piles of liquid gold by weight: every gem weighs
just 1, and gems of the same identified type stack into a single
inventory slot regardless of count, so the only cost of hoarding a
heap of identified rubies is one slot's worth of clutter.

Every real gem, with the unangry-shopkeeper buy price.

::: web-only
Use the Cha/Sell/Tourist/Angry toolbar to see how the modifiers shift things.
:::

The Mohs column is real-world mineral hardness on the Mohs scale
(talc 1, diamond 10), and the game uses it in two places. Gems of
Mohs 8 or higher count as **"hard"**, and hard gems do two things
softer gems and glass can't: they can be used as a stylus to
*engrave* [Elbereth](#elbereth) and other messages permanently into the dungeon
floor (instead of the temporary dust scratch a finger or soft gem
leaves), and they have about a 50% chance to *survive* being
thrown rather than shattering on impact. Below Mohs 8, the gem
only writes in dust and breaks on impact like glass. Hardness
doesn't affect touchstoning — every gem can be identified by a
blessed touchstone regardless.

<div class="price-id-toolbar"></div>

| Price | Gem                   | Color           | Mohs | Notes                          |
|------:|-----------------------|-----------------|-----:|--------------------------------|
|  4500 | Dilithium crystal     | white           |    5 | rarest white gem               |
|  4000 | Diamond               | white           |   10 | hardest material in the game   |
|  3500 | Ruby                  | red             |    9 |                                |
|  3250 | Jacinth               | orange          |    9 | one of two orange gems         |
|  3000 | Sapphire              | blue            |    9 |                                |
|  2500 | Black opal            | black           |    8 |                                |
|  2500 | Emerald               | green           |    8 |                                |
|  2000 | Turquoise             | green           |    6 |                                |
|  1500 | Citrine               | yellow          |    6 |                                |
|  1500 | Aquamarine            | green           |    8 |                                |
|  1000 | Amber                 | yellowish brown |    2 | softest gem; only dust-writes  |
|   900 | Topaz                 | yellowish brown |    8 |                                |
|   850 | Jet                   | black           |    7 |                                |
|   800 | Opal                  | white           |    6 |                                |
|   700 | Chrysoberyl           | yellow          |    5 |                                |
|   700 | Garnet                | red             |    7 |                                |
|   600 | Amethyst              | violet          |    7 |                                  |
|   500 | Jasper                | red             |    7 |                                |
|   400 | Fluorite              | violet          |    4 |                                |
|   300 | Jade                  | green           |    6 |                                |
|   200 | Obsidian              | black           |    6 |                                |
|   200 | Agate                 | orange          |    6 |                                |
|     0 | (worthless glass)     | any color       |    5 | sells for 3–8 zm unidentified  |

<div class="price-id-toolbar"></div>

The decision is rarely "carry or drop"; it's "if I'm slot-pressed
and have to thin the heap, which colors do I drop first." Black opals,
emeralds, and rubies are usually keepers; agate and obsidian first to go.

A few rules of thumb:

- **Every real gem is equally good for unicorn luck.** A 200 zm agate
  throws at an orange unicorn for the same +5 luck as a 3250 zm
  jacinth. Don't sell off your "junk" gems before you've found an
  alignment-matching unicorn to feed them to.
- **The price column matters only when selling or wishing.** If
  you're not in a shop and not weight-pressed, the price ranking is
  irrelevant.
- **If you must drop some gems** (you're in a Mine's End slot-crunch,
  or you're consolidating before a stash), drop *duplicates of the
  cheap colors first*. Keep at least one of every identified type,
  because the touchstone work is already done.
- **Top tier** (≥ 2500: dilithium, diamond, ruby, jacinth, sapphire,
  black opal, emerald) are worth selling individually as you find
  shops that buy them: 3000+ zm per gem is a real bankroll. Don't
  fire-sale them to a non-gem-buying shop for half price.
- **Worthless glass never costs luck.** Glass thrown at a unicorn is
  either rejected ("not interested in your junk") or quietly
  accepted. The Luck risk only fires on *real* gems thrown to a
  **wrong-alignment** unicorn (random −3 to +3).

Read the table as a **selling guide**, not a discard guide: real
gems near the top are worth making time to sell at a gem dealer
and worth wishing for if you're flush on wishes. Lower-priced gems
aren't trash — they still feed unicorns and still touchstone-identify
other gems by hardness comparison.


---

### Weapons Tables

Damage is shown as **vs small / vs large**, the dice rolled before enchantment and excluding silver/material bonuses. **Wt** is unit weight; **Cost** is the unenchanted shop base price in zorkmids. **Hit** is the to-hit bonus baked into the weapon itself (most are 0). Two-handed weapons that prevent shield use and two-weapon combat are flagged in the notes. Weapons are grouped by their skill class so you can see your options within each skill tree at a glance.

#### Dagger
<!-- audit
2026-05-19:
- Expert Rogue dagger multishot caps at rnd(4) = 1-4: 1 base + 1 Expert + 1 Skilled + 1 class (dothrow.c:177-190, 63-67)
- athame engraving Elbereth does NOT dull the weapon, so no enchantment is consumed (engrave.c:1306-1307, 1361). Duration is unchanged
- silver weapons hurt demons, vampires, lycanthropes, shades, and imps (except tengu) per mon_hates_silver (mondata.c:524-528)
- silver does NOT hurt liches, zombies, mummies, wraiths, ghouls, or ghosts (none of those classes appear in hates_silver, mondata.c:524-528)
- silver damage bonus is rolled in mhitm/hmon, +1d20 vs hates_silver targets for silver weapons (uhitm.c:1376-1377)
-->


::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| dagger | 1d4 / 1d3 | 10 | 4 | +2 | iron | Stackable; Expert-skill Rogues can multishot up to four in a single throw. |
| elven dagger | 1d5 / 1d3 | 10 | 4 | +2 | wood | Stackable. Sting is the artifact form. |
| orcish dagger | 1d3 / 1d3 | 10 | 4 | +2 | iron | Stackable. |
| silver dagger | 1d4 / 1d3 | 12 | 40 | +2 | silver | Stackable. Silver damage to demons, vampires, lycanthropes, shades, and imps. Common Rogue/Ranger off-hand. |
| athame | 1d4 / 1d3 | 10 | 4 | +2 | iron | Stackable. Engraving with an athame **doesn't dull the blade**. |

:::

<!-- audit
2026-05-19:
- 5 knife rows verified: P_KNIFE skill, scalpel METAL, knife/stiletto IRON, worm tooth/crysknife BONE (objects.h:215-233)
- scalpel is Healer's starter (u_init.c:77)
- crysknife reverts to worm tooth on drop via type-id swap, NOT poly (do.c:903-918)
- fixed (erodeproof) crysknife only reverts ~10% of drops (do.c:911)
-->
#### Knife

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| scalpel | 1d3 / 1d3 | 5 | 6 | +2 | metal | The Healer's starter. |
| knife | 1d3 / 1d2 | 5 | 4 | — | iron |  |
| stiletto | 1d3 / 1d2 | 5 | 4 | — | iron |  |
| worm tooth | 1d2 / 1d2 | 20 | 2 | — | bone |  |
| crysknife | 1d10 / 1d10 | 20 | 100 | +3 | bone | Reverts to a worm tooth when dropped (unwielding is fine; only dropping triggers it). An erodeproof one reverts only ~10% of the time. |

:::

<!-- audit
2026-05-19:
- 4 short sword rows verified: short 1d6/1d8, elven 1d8/1d8, orcish 1d5/1d8, dwarvish 1d7/1d8 (objects.h:244-255)
- all share P_SHORT_SWORD; scimitar uses P_SABER and is correctly excluded
- Rogue starter (u_init.c:134); Samurai "wakizashi" is a short sword aliased in objnam.c:106 (u_init.c:144)
- no artifact uses SHORT_SWORD as base type
-->
#### Short sword

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| short sword | 1d6 / 1d8 | 30 | 10 | — | iron | The Rogue's starter; Samurai's *wakizashi* is just a short sword by another name. |
| elven short sword | 1d8 / 1d8 | 30 | 10 | — | wood |  |
| orcish short sword | 1d5 / 1d8 | 30 | 10 | — | iron |  |
| dwarvish short sword | 1d7 / 1d8 | 30 | 10 | — | iron |  |

:::

#### Saber
<!-- audit
2026-05-19:
- 10 saber cells verified clean (objects.h)
- Grayswandir is a SILVER_SABER artifact, PHYS(5,0): +1d5 to-hit and double damage (artilist.h:170, artifact.c:1083-1086, 1106-1107)
- Werebane is also a silver saber artifact (artilist.h:166); +d5 vs lycanthropes via SPFX_DFLAG2 M2_WERE
- inline effects deferred to Artifacts chapter rather than duplicated
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| scimitar | 1d8 / 1d8 | 40 | 15 | — | iron |  |
| silver saber | 1d8 / 1d8 | 40 | 75 | — | silver | Silver does bonus damage to demons/weres/vampires/imps. Artifact forms: **Grayswandir** and **Werebane** (see [Artifacts](#artifacts)). |

:::

#### Broadsword
<!-- audit
2026-05-19:
- Stormbringer's base item is RUNESWORD, NOT broadsword (artilist.h:93)
- runesword and broadsword share P_BROAD_SWORD skill and 1d4+1d4 / 1d6+1 dice, hence the confusion
- artifact details kept in the Artifacts chapter, not duplicated here
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| broadsword | 1d4+1d4 / 1d6+1 | 70 | 10 | — | iron |  |
| elven broadsword | 1d6+1d4 / 1d6+1 | 70 | 10 | — | wood |  |
| runesword | 1d4+1d4 / 1d6+1 | 40 | 300 | — | iron | Stormbringer is the chaotic artifact form. |

:::

#### Long sword
<!-- audit
2026-05-19:
- long sword stats verified (objects.h:270-280)
- Excalibur dipping requires LONG_SWORD, XL >= 5, quan == 1, not already artifact, no extant Excalibur (fountain.c:404-408)
- dip roll: !rn2(6) for Knights, !rn2(30) otherwise (fountain.c:405)
- non-Lawfuls get the sword cursed, spe possibly decremented, oerodeproof cleared (fountain.c:411-421)
- LONG_SWORD artifacts: Excalibur, Frost Brand, Fire Brand, Giantslayer, Vorpal Blade, Sunsword (artilist.h:85, 149, 153, 174, 191, 209)
- Vorpal Blade is a LONG_SWORD artifact, NOT a two-handed sword (artilist.h:191)
- two-handed sword has no dedicated artifact (no TWO_HANDED_SWORD entries in artilist.h)
-->


::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| long sword | 1d8 / 1d12 | 40 | 15 | — | iron | At XL 5+, dipping in a fountain rolls 1-in-30. Knights get 1-in-6. On a hit, Lawfuls get **Excalibur**. Others get the sword cursed. Artifact forms: Excalibur, Frost Brand, Fire Brand, Giantslayer, Vorpal Blade, Sunsword. |
| katana | 1d10 / 1d12 | 40 | 80 | +1 | iron | +1 to-hit baked in. Snickersnee is the artifact form. |

:::

#### Two-handed sword
<!-- audit
2026-05-19:
- two-handed sword stats verified (objects.h:273-285)
- 5.0 bimanual weapons get 3/2 Str damage bonus, melee only (uhitm.c:1467-1468; gated on bimanual(uwep) + HMON_MELEE)
- bonus also applies to battle-axe, dwarvish mattock, bardiche
- Tsurugi is the two-handed sword artifact (artilist.h:285-289); Vorpal Blade is a LONG_SWORD (artilist.h:191), NOT the artifact form here
-->

Two-handed weapons get a **3/2 Strength damage bonus** in 5.0 —
your STR damage contribution is multiplied by 1.5 when wielding a
bimanual weapon. Combined with the high base dice below, that's a
big chunk of why two-handed swords compete with one-hand-plus-
shield even though you forfeit the shield slot. The same bonus
applies to the battle-axe, dwarvish mattock, bardiche, and any
other bimanual weapon.

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| two-handed sword | 1d12 / 1d6+2d6 | 150 | 50 | — | iron | Two-handed (no shield, no off-hand weapon). No dedicated artifact form. |
| tsurugi | 1d16 / 1d8+2d6 | 60 | 500 | +2 | metal | Two-handed. The Tsurugi of Muramasa is the artifact form. |

:::

#### Axe
<!-- audit
2026-05-19:
- axe 1d6/1d4, battle-axe 1d8+1d4 small / 1d6+2d4 large with bonus dice (objects.h:236-241, weapon.c:251-289)
- both use P_AXE skill; battle-axe is bimanual and gets 3/2 Str damage bonus in melee (uhitm.c:1467-1468)
- Cleaver is the BATTLE_AXE artifact (artilist.h:114-116)
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| axe | 1d6 / 1d4 | 60 | 8 | — | iron |  |
| battle-axe | 1d8+1d4 / 1d6+2d4 | 120 | 40 | — | iron | Two-handed (gets the 5.0 3/2 Str damage bonus). +1d4 small, +2d4 large. The Barbarian quest artifact **Cleaver** is a battle-axe. |

:::

<!-- audit
2026-05-19:
- pick-axe: WEPTOOL, wt 100, cost 50, 1d6/1d3, iron (objects.h:1007-1009)
- mattock stats verified (objects.h:345-347)
- both share P_PICK_AXE skill and route through use_pick_axe (apply.c:4290-4292)
- mattock is bimanual: gets 3/2 Str damage bonus in melee (uhitm.c:1467-1468)
- dig-down creates a pit, then a hole (dig.c:432-433, 372-374)
-->
#### Pick-axe

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| pick-axe | 1d6 / 1d3 | 100 | 50 | — | iron | Weapon-tool. Apply to dig through walls or down through floors (creates pit, then hole). Same `pick-axe` skill as the mattock. |
| dwarvish mattock | 1d12 / 1d8+2d6 | 120 | 50 | −1 | iron | Two-handed (3/2 Str damage bonus). Digs through walls like a pick-axe. Slight to-hit penalty (−1). |

:::

#### Club
<!-- audit
2026-05-19:
- club and aklys stats verified (objects.h:371-373, 381-383)
- starting inventory uses blessorcurse(otmp, 10): roughly 10% chance any starter item is cursed (mkobj.c:876-885)
- club is a Caveman starter
- aklys returns when thrown only if wielded (W_WEP), with ~1% misfire (dothrow.c:30-34, 1710-1759)
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| club | 1d6 / 1d3 | 30 | 3 | — | wood | Caveman starter. |
| aklys | 1d6 / 1d3 | 15 | 4 | — | iron | Returns when thrown if wielded as your primary weapon (it's tethered); occasional misfire. |

:::

#### Mace
<!-- audit
2026-05-19:
- mace stats verified (objects.h:355-361)
- Demonbane PHYS(5,0): +1d5 to-hit and double damage vs demons (artifact.c:1083-1085 spec_abon, 1106-1107 spec_dbon); also has banish invoke
- silver mace: +1d20 vs mon_hates_silver targets (uhitm.c:1376-1377)
- silver hates list: demons, weres, vampires, shades, most imps (mondata.c:524-528)
- silver does NOT hit "undead" or "shape-changers" generally (mummies, zombies, ghosts, chameleons excluded)
- Mjollnir is a war hammer, NOT a mace (artilist.h:109 `A("Mjollnir", WAR_HAMMER, ...)`)
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| mace | 1d6+1 / 1d6 | 30 | 5 | — | iron | The Priest's guaranteed first sacrifice gift, Demonbane: a silver mace with +1d5 to-hit and double damage versus demons, plus a banish invoke. |
| silver mace | 1d6+1 / 1d6 | 36 | 60 | — | silver | +1d20 versus demons, weres, vampires, shades, and most imps. |

:::

#### Morning star
<!-- audit
2026-05-19:
- morning star: 1d4+1d4 / 1d6+1, wt 120, cost 10, hit 0, iron (objects.h:363-365, weapon.c:225-289)
- P_MORNING_STAR is its own skill, distinct from P_MACE (skills.h:35)
- Trollsbane IS a MORNING_STAR artifact: regenerates while wielded, +d5 vs trolls (artilist.h:182-184)
-->


::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| morning star | 1d4+1d4 / 1d6+1 | 120 | 10 | — | iron | +1d4 small, +1 large — punches above its weight for a one-hander. |

:::

#### Flail
<!-- audit
2026-05-19:
- flail: base 1d6/1d4, +1 small (weapon.c:272-275), +1d4 large (weapon.c:239-243); objects.h:384-386
- grappling hook: 1d2/1d6, WEPTOOL that trains P_FLAIL (objects.h:1010-1012)
- grappling hook #apply pulls target toward you; range 4 (P_NONE/Basic), 5 (Skilled), 8 (Expert+) (apply.c:3686-3698)
- no flail artifact
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| flail | 1d6+1 / 1d4+1d4 | 15 | 4 | — | iron | +1 small, +1d4 large; one-handed. |
| grappling hook | 1d2 / 1d6 | 30 | 50 | — | iron | Tool, not a primary weapon, but trains P_FLAIL. `#apply` to hook and pull a target toward you. |

:::

#### Hammer
<!-- audit
2026-05-19:
- war hammer stats verified (objects.h:367-369, weapon.c); +1 small bonus matches sdam/ldam fields
- Mjollnir can be gifted to ANY Valkyrie, not just Neutral: hack_artifacts fixes alignment to player's initalign (artifact.c:92-95)
- aklys uses P_CLUB and is correctly placed elsewhere
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| war hammer | 1d4+1 / 1d4 | 50 | 5 | — | iron | Mjollnir is the artifact form (Valkyrie sacrifice gift; its alignment will match the player's). |

:::

#### Quarterstaff
<!-- audit
2026-05-19:
- quarterstaff: bimanual, 1d6/1d6, wt 40, cost 5, WOOD, P_QUARTERSTAFF (objects.h:377-379).
- Wizard starter weapon (u_init.c:168).
- bimanual: gets 3/2 Str damage bonus in melee (uhitm.c:1467).
- Expert caps: Wizard, Priest, Healer, Caveman (u_init.c:314,334,396,555 P_QUARTERSTAFF=P_EXPERT).
- No Knight or Rogue entry: P_QUARTERSTAFF absent from Skill_K and Skill_R (u_init.c:346-413).
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| quarterstaff | 1d6 / 1d6 | 40 | 5 | — | wood | Two-handed but light; the Wizard's starting weapon. |

:::

#### Polearms
<!-- audit
2026-05-19:
- 12 polearm rows verified: all two-handed, all P_POLEARMS, all iron (objects.h:294-341).
- per-row dice/weight/cost from objects.h:294-341 WEAPON() macros; +d4/+d6 vs-large bonuses applied in weapon.c dmgval.
- polearm reach is skill-dependent, NOT a fixed 2 squares (apply.c:3355-3382).
- use_pole has NO "empty intervening square" check (apply.c:3355-3382).
- polearms CAN bash an adjacent monster (uhitm.c:1467-1484).
- adjacent polearm bash: damage clamps to 1d2 base, no weapon-skill bonus, Strength still applies (uhitm.c:1075-1086, 1447-1469).
-->

All polearms are two-handed. To strike at range, `#apply` the weapon (not wield-and-attack): you can hit at distance 2 orthogonally at Basic skill, with extra positions opening up at Skilled. You can still hit an adjacent monster the normal way with a polearm in hand, but the attack is treated as bashing — damage clamps to 1d2 base before bonuses and the weapon-skill bonus doesn't apply (Strength still does). Reach is what makes polearms worth carrying, and it works the same across the class. Notes below describe each entry's extra damage.

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| partisan | 1d6 / 1d6+1 | 80 | 10 | — | iron | Reach. |
| ranseur | 1d4+1d4 / 1d4+1d4 | 50 | 6 | — | iron | +1d4 small, +1d4 large. |
| spetum | 1d6+1 / 1d6+1d6 | 50 | 5 | — | iron | +1 small, +1d6 large. |
| glaive | 1d6 / 1d10 | 75 | 6 | — | iron | Reach. |
| halberd | 1d10 / 1d6+1d6 | 150 | 10 | — | iron | +1d6 large. |
| bardiche | 1d4+1d4 / 1d4+2d4 | 120 | 7 | — | iron | +1d4 small, +2d4 large. |
| voulge | 1d4+1d4 / 1d4+1d4 | 125 | 5 | — | iron | +1d4 small, +1d4 large. |
| fauchard | 1d6 / 1d8 | 60 | 5 | — | iron | Reach. |
| guisarme | 1d4+1d4 / 1d8 | 80 | 5 | — | iron | +1d4 small. |
| bill-guisarme | 1d4+1d4 / 1d10 | 120 | 7 | — | iron | +1d4 small. |
| lucern hammer | 1d4+1d4 / 1d6 | 150 | 7 | — | iron | +1d4 small. |
| bec de corbin | 1d8 / 1d6 | 100 | 8 | — | iron | Reach. |

:::

#### Spear
<!-- audit
2026-05-19:
- 6 spear rows (spear/elven/orcish/dwarvish/silver/javelin) verified P_SPEAR (objects.h:174-191).
- silver spear: SILVER material, cost 40, +d20 vs silver-haters (objects.h:186-188; artifact.c spec_dbon).
- Valkyrie starts with a plain spear and trains to Expert (u_init.c:160-161, 537).
- spear kebab bonus: +2 to-hit vs xorns, dragons, jabberwocks, nagas, giants (weapon.c:71-73, 167-168, is_spear).
- trident uses P_TRIDENT, a separate skill from spears (objects.h:195 P_TRIDENT).
- +1 thrown-spear multishot belongs to Caveman (PM_CAVE_DWELLER), NOT Valkyrie (dothrow.c:47-52).
- Valkyrie has no class-specific spear multishot, only the generic Expert ceiling (dothrow.c).
-->

All spears share the same skill (trident uses a different class
— see below). The Valkyrie starts with one and can train to
Expert. The **Caveman** is the actual spear-multishot specialist:
Cavemen get +1 multishot on any thrown spear (regular, silver,
javelin alike), so a stack of javelins is real ranged firepower
for them.

Spears get a **+2 to-hit bonus** when used against the big
monsters — xorns, dragons, jabberwocks, nagas, and giants — the
kebab bonus.

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| spear | 1d6 / 1d8 | 30 | 3 | — | iron | Throwable. Valkyrie's starting weapon. |
| elven spear | 1d7 / 1d8 | 30 | 3 | — | wood |  |
| orcish spear | 1d5 / 1d8 | 30 | 3 | — | iron |  |
| dwarvish spear | 1d8 / 1d8 | 35 | 3 | — | iron |  |
| silver spear | 1d6 / 1d8 | 36 | 40 | — | silver | Silver damage to demons and weres. |
| javelin | 1d6 / 1d6 | 20 | 3 | — | iron | Stackable thrown weapon; Cavemen can ranged-spam them. |

:::

#### Trident
<!-- audit
2026-05-19:
- trident stats verified (objects.h:195)
- the +1/+2d4 large-creature bonus is the universal land bonus, NOT trident-specific (weapon.c:251-276)
- trident's signature bonus: +4 to-hit vs swimmers in water, +2 vs eels and snakes (weapon.c:170-176 hitval, not dmgval)
-->


::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| trident | 1d6+1 / 1d4+2d4 | 25 | 5 | — | iron | One-handed. **+4 to-hit vs swimmers in water, +2 vs eels and snakes** — the trident's signature bonus. Outside water it's an ordinary side-arm. |

:::

<!-- audit
2026-05-19:
- lance: P_LANCE, one-handed, IRON, 1d6/1d8 (objects.h:349)
- on foot lance still hits and damages normally, just NO joust bonus
- mounted joust bonus: +2d10 primary, +2d2 off-hand (objects.h:351-352, uhitm.c:1546)
- shatter chance 1/250 per successful joust (uhitm.c:2123-2125, 1559)
-->
#### Lance

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| lance | 1d6 / 1d8 | 180 | 10 | — | iron | One-handed, P_LANCE skill. Mounted only: chance to joust for +2d10 primary (+2d2 off-hand) extra damage; a critical can shatter the lance. No bonus on foot. |

:::

<!-- audit
2026-05-19:
- rubber hose and bullwhip stats verified; P_WHIP skill (objects.h:374-376, 390-392, skills.h:49)
- bullwhip #apply can disarm (apply.c:3127-3174) and yank from a pit (apply.c:3069-3125)
- rubber hose does NOT damage shades: it's PLASTIC, shade_glare needs SILVER (artifact.c:555-562, weapon.c:307-308)
- rubber hose prob=0: never randomly spawns (objects.h:374-376 WEAPON row, probability field is 0)
- Archeologist starts with bullwhip +1 at Basic (apply.c:2992-2993)
- no whip artifacts
-->
#### Whip

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| rubber hose | 1d4 / 1d3 | 20 | 3 | — | plastic | Joke weapon; never spawns randomly. |
| bullwhip | 1d2 / 1 | 20 | 4 | — | leather | Archeologist's starter. Apply to disarm an adjacent monster (only when the target is wielding a weapon), or to yank yourself out of a pit (anchors on a nearby boulder, furniture, or big monster). |

:::

<!-- audit
2026-05-19:
- 5 PROJECTILE arrow rows (objects.h:141-154); 4 BOW launcher rows (objects.h:395-402).
- arrows: 1d6/1d6 (1d7/1d6 elven, 1d5/1d6 orcish, 1d6/1d6 silver) wt 1, cost 2 (objects.h:141-152).
- ya: 1d7/1d7, +1 hit, METAL, cost 4 (objects.h:153-154).
- yumi prob=0: Samurai-only, never randomly spawns (objects.h:401-402).
-->
#### Bow

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| arrow | 1d6 / 1d6 | 1 | 2 | — | iron |  |
| elven arrow | 1d7 / 1d6 | 1 | 2 | — | wood |  |
| orcish arrow | 1d5 / 1d6 | 1 | 2 | — | iron |  |
| silver arrow | 1d6 / 1d6 | 1 | 5 | — | silver | Silver damage to demons and weres. |
| ya | 1d7 / 1d7 | 1 | 4 | +1 | metal |  |
| bow | — | 30 | 60 | — | wood |  |
| elven bow | — | 30 | 60 | — | wood |  |
| orcish bow | — | 30 | 60 | — | wood |  |
| yumi | — | 30 | 60 | — | wood | The Samurai's bow. |

:::

#### Crossbow
<!-- audit
2026-05-19:
- crossbow bolt: 1d4 / 1d6, NO +1 bonus (objects.h:155-156 PROJECTILE)
- crossbows CAN multishot: requires Str 18 (Str 16 for gnomes), with +1 baseline gnome bonus (dothrow.c:225-231, 205-209)
- skill caps: Rogue Expert, Ranger Expert, Knight Skilled (u_init.c)
- Valkyries cap at Unskilled, NOT Skilled: Skill_V has no P_CROSSBOW entry (u_init.c:525-547)
-->


::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| crossbow bolt | 1d4 / 1d6 | 1 | 2 | — | iron | Stackable. |
| crossbow | — | 50 | 40 | — | wood | Bolts pierce. Multishot kicks in at **Str 18** (Str 16 for gnomes, who also get a baseline +1 multishot); below that, one bolt per turn. Rogues and Rangers reach Expert, Knights Skilled. |

:::

#### Sling
<!-- audit
2026-05-19:
- sling stats verified (objects.h:403)
- sling skill trains from hits while wielding a sling, NOT from picking up rocks (weapon.c:1750)
- sling launches rocks, flint stones, and gems
- Caveman starts with one sling
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| sling | — | 3 | 20 | — | leather | Launches rocks, flint stones, and gems. Caveman starting weapon. |

:::

#### Dart
<!-- audit
2026-05-19:
- dart stats verified (objects.h:161)
- darts are poisonable (is_poisonable)
- Tourist starts with 21-40 darts via trquan() = 21+rn2(20), NOT ~25-60 (u_init.c:150-151)
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| dart | 1d3 / 1d2 | 1 | 2 | — | iron | Poisonable. Tourist starts with a stack of ~21–40 at +2. |

:::

#### Shuriken
<!-- audit
2026-05-19:
- shuriken: 1d8/1d6, wt 1, cost 5, +2 hit, iron, PIERCE missile, P_SHURIKEN (objects.h:163)
- is_poisonable (obj.h:264-268)
- Samurai trains to Expert (u_init.c:481)
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| shuriken | 1d8 / 1d6 | 1 | 5 | +2 | iron |  |

:::

#### Boomerang
<!-- audit
2026-05-19:
- boomerang stats verified (objects.h:166-168)
- boomerang does NOT always return: 10-step curved path that stops on monster, wall, door, or sink hits (zap.c:4148-4220 boomhit; loop ct<10, breaks on isok, monster, ZAP_POS or closed_door)
- catching the return requires a Dex check, auto-fails if Fumbling; a missed catch hits the thrower
- enchanted boomerang hits (spe+1) times
- useless underwater
-->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|--------------|----------------------------------------------------------------|
| boomerang | 1d9 / 1d9 | 5 | 20 | — | wood | Curves back on a clear path; stops on a monster, wall, door, or sink. Low Dex or Fumbling means you catch it in the face. |

:::

---

### Armor Tables
<!-- audit
2026-05-19:
- body armor: AC/Wt/Cost via ARMOR() macros (objects.h:556-600); plate mail AC+7 wt450 cost600 (line 556-558).
- mithril coats: AC+6/+5, wt 150, cost 240, MITHRIL material (objects.h:571-576).
- shirts wt 5 (Hawaiian/T-shirt, objects.h:603-608); cloaks at objects.h:611-650.
- helmets at objects.h:445-487; gloves at objects.h:686-697; boots at objects.h:700-727.
- shields at objects.h:653-679; cloak of protection MC 3 (objects.h:637-640).
- helm of brilliance: adds spe to Int and Wis (literal enchantment), NO dice (do_wear.c:3328-3334 adj_abon).
- gauntlets of dexterity: adds spe to Dex, NO dice (do_wear.c adj_abon).
- dunce cap is NOT pre-cursed at generation: follows standard mkobj; auto-curses when worn (do_wear.c:475-491).
- 9/10-cursed-on-generation items: FUMBLE_BOOTS, LEVITATION_BOOTS, HELM_OF_OPPOSITE_ALIGNMENT, GAUNTLETS_OF_FUMBLING (mkobj.c:1086-1090).
- mithril DOES suffer casting penalty: MITHRIL is in is_metallic range, spelarmr applies (objclass.h:194-196, spell.c:2191-2193).
- blue dragon scale mail and scales give extrinsic Very_fast tier matching speed boots, NOT intrinsic Fast (do_wear.c:817-828 EFast).
- speed boots mechanic: free action on 2/3 of turns, NOT "+1 speed". (allmain.c:125-128 `if (Very_fast) { if (rn2(3) != 0) moveamt += NORMAL_SPEED; }`)
- levitation boots: Boots_off handles in-air removal (do_wear.c:300-310); the trap is the 9/10 curse.
- robe casting bonus cancels most of the metal-armor penalty (spell.c:2192-2195 spelarmr subtraction).
- chain mail: all iron mails are Mines drops (the "Dwarves drop these" framing is misleading).
- follow-ups: build_armor_appendix.py may be stale; "yellow dragon scale mail | Rare." not verified against 5.0 generation rules.
-->

**AC** is the armor-class bonus the piece provides (higher number = more protection; this is the amount subtracted from your displayed AC). **MC** is the magic-cancellation level (1-3) — higher MC reduces the chance of magic attacks landing. **Wt** is weight; **Cost** is shop base price. The **Notes** column folds in the intrinsic property granted while the piece is worn, and tactical caveats. Armor is grouped by slot. Dragon scale mail is listed separately because of its sheer importance to the endgame.

#### Body armor (suits)

::: dense-table

| Armor | AC | MC | Wt | Cost | Material | Notes |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| plate mail | +7 | 2 | 450 | 600 | iron | Spellcasting penalty. |
| crystal plate mail | +7 | 2 | 415 | 820 | glass | Never rusts. Spellcasting penalty. |
| bronze plate mail | +6 | 1 | 450 | 400 | copper |  |
| splint mail | +6 | 1 | 400 | 80 | iron |  |
| banded mail | +6 | 1 | 350 | 90 | iron |  |
| dwarvish mithril-coat | +6 | 2 | 150 | 240 | mithril | Light, but mithril is metallic so the spellcasting penalty still applies (smaller than plate, larger than zero). Wizard mid-game goal. |
| elven mithril-coat | +5 | 2 | 150 | 240 | mithril | Light, expensive. Mithril is metallic, so a casting penalty still applies — smaller than plate but not zero. |
| chain mail | +5 | 1 | 300 | 75 | iron |  |
| orcish chain mail | +4 | 1 | 300 | 75 | iron |  |
| scale mail | +4 | 1 | 250 | 45 | iron |  |
| studded leather armor | +3 | 1 | 200 | 15 | leather | No spellcasting penalty. |
| ring mail | +3 | 1 | 250 | 100 | iron |  |
| orcish ring mail | +2 | 1 | 250 | 80 | iron |  |
| leather armor | +2 | 1 | 150 | 5 | leather |  |
| leather jacket | +1 | — | 30 | 10 | leather |  |
| gray dragon scale mail | +9 | — | 40 | 1200 | dragonhide | Magic resistance. Endgame body-armor goal. |
| silver dragon scale mail | +9 | — | 40 | 1200 | dragonhide | Reflection. |
| black dragon scale mail | +9 | — | 40 | 1200 | dragonhide | Disintegration resistance + drain resistance. |
| yellow dragon scale mail | +9 | — | 40 | 900 | dragonhide | Acid resistance + stoning resistance. Rare. |
| orange dragon scale mail | +9 | — | 40 | 900 | dragonhide | Sleep resistance + free action. |
| white dragon scale mail | +9 | — | 40 | 900 | dragonhide | Cold resistance + slow digestion. |
| red dragon scale mail | +9 | — | 40 | 900 | dragonhide | Fire resistance + infravision. |
| green dragon scale mail | +9 | — | 40 | 900 | dragonhide | Poison resistance + sickness resistance. |
| blue dragon scale mail | +9 | — | 40 | 900 | dragonhide | Shock resistance + speed, same tier as speed boots. |
| gold dragon scale mail | +9 | — | 40 | 900 | dragonhide | Hallucination resistance + permanent light (only body-slot light source). |

:::

#### Dragon scales

::: dense-table

| Armor | AC | MC | Wt | Cost | Material | Notes |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| gray dragon scales | +3 | — | 40 | 700 | dragonhide | Magic resistance. Make-into upgrade to scale mail. |
| silver dragon scales | +3 | — | 40 | 700 | dragonhide | Reflection. |
| black dragon scales | +3 | — | 40 | 700 | dragonhide | Disintegration resistance + drain resistance. |
| yellow dragon scales | +3 | — | 40 | 500 | dragonhide | Acid resistance + stoning resistance. |
| orange dragon scales | +3 | — | 40 | 500 | dragonhide | Sleep resistance + free action. |
| white dragon scales | +3 | — | 40 | 500 | dragonhide | Cold resistance + slow digestion. |
| red dragon scales | +3 | — | 40 | 500 | dragonhide | Fire resistance + infravision. |
| green dragon scales | +3 | — | 40 | 500 | dragonhide | Poison resistance + sickness resistance. |
| blue dragon scales | +3 | — | 40 | 500 | dragonhide | Shock resistance + speed, same tier as speed boots. |
| gold dragon scales | +3 | — | 40 | 500 | dragonhide | Hallucination resistance + permanent light. |

:::

#### Shirts

::: dense-table

| Armor | AC | MC | Wt | Cost | Material | Notes |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| Hawaiian shirt | +0 | — | 5 | 3 | cloth | Tourist starter. Worn under body armor. |
| T-shirt | +0 | — | 5 | 2 | cloth | Worn under body armor. |

:::

#### Cloaks

::: dense-table

| Armor | AC | MC | Wt | Cost | Material | Notes |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| mummy wrapping | +0 | 1 | 3 | 2 | cloth | Blocks invisibility while worn. |
| elven cloak | +1 | 1 | 10 | 60 | cloth | Stealth. |
| orcish cloak | +0 | 1 | 10 | 40 | cloth |  |
| dwarvish cloak | +0 | 1 | 10 | 50 | cloth |  |
| oilskin cloak | +1 | 2 | 10 | 50 | cloth | Resists grab attacks. |
| robe | +2 | 2 | 15 | 50 | cloth | Casting bonus. Cancels most of the metal-armor penalty. |
| alchemy smock | +1 | 1 | 10 | 50 | cloth | Poison resistance. Fantastic early-game safety. |
| leather cloak | +1 | 1 | 15 | 40 | leather |  |
| cloak of protection | +3 | 3 | 10 | 50 | cloth | Highest MC of any cloak. |
| cloak of invisibility | +1 | 1 | 10 | 60 | cloth | Invisibility. |
| cloak of magic resistance | +1 | 1 | 10 | 60 | cloth | Magic resistance. The lightest source. |
| cloak of displacement | +1 | 1 | 10 | 50 | cloth | Displacement. |

:::

#### Helmets

::: dense-table

| Armor | AC | MC | Wt | Cost | Material | Notes |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| elven leather helm | +1 | — | 3 | 8 | leather |  |
| orcish helm | +1 | — | 30 | 10 | iron |  |
| dwarvish iron helm | +2 | — | 40 | 20 | iron |  |
| fedora | +0 | — | 3 | 1 | cloth | Tourist starter; Eye of the Aethiopica base. |
| cornuthaum | +0 | 1 | 4 | 80 | cloth | Clairvoyance. Wizards only; blocks other clairvoyance for non-Wizards. |
| dunce cap | +0 | — | 4 | 1 | cloth | Int/Wis → 6. Auto-curses on wear. Needs remove curse to take off. |
| dented pot | +1 | — | 10 | 8 | iron |  |
| helm of brilliance | +1 | — | 40 | 50 | glass | Adds enchantment value to both Int and Wis while worn (a +3 helm gives +3 Int and +3 Wis). |
| helmet | +1 | — | 30 | 10 | iron |  |
| helm of caution | +1 | — | 50 | 50 | iron | Warning. |
| helm of opposite alignment | +1 | — | 50 | 50 | iron | Flips your alignment while worn. Cursed 90%. |
| helm of telepathy | +1 | — | 50 | 50 | iron | Telepathy while blind. |

:::

The helm of opposite alignment is mostly a trap, but the alignment
flip is sometimes useful on purpose: sacrifice on a cross-aligned
altar, claim the opposite alignment's quest artifact, or, on the
Astral Plane, change which altar accepts the Amulet.

#### Gloves

::: dense-table

| Armor | AC | MC | Wt | Cost | Material | Notes |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| leather gloves | +1 | — | 10 | 8 | leather |  |
| gauntlets of fumbling | +1 | — | 10 | 50 | leather | Causes frequent fumbling. Generated cursed 9 times in 10. Avoid. |
| gauntlets of power | +1 | — | 30 | 50 | iron | Sets Strength to 25. |
| gauntlets of dexterity | +1 | — | 10 | 50 | leather | Adds enchantment value to Dex while worn (a +3 pair gives +3 Dex). |

:::

#### Boots

::: dense-table

| Armor | AC | MC | Wt | Cost | Material | Notes |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| low boots | +1 | — | 10 | 8 | leather |  |
| iron shoes | +2 | — | 50 | 16 | iron |  |
| high boots | +2 | — | 20 | 12 | leather |  |
| speed boots | +1 | — | 20 | 50 | leather | Very fast. Free extra action on 2/3 of turns. |
| water walking boots | +1 | — | 15 | 50 | leather | Water walking. Critical for the Castle drawbridge. |
| jumping boots | +1 | — | 20 | 50 | leather | `#apply` to leap to a chosen nearby square. |
| elven boots | +1 | — | 15 | 8 | leather | Stealth. |
| kicking boots | +1 | — | 50 | 8 | iron |  |
| fumble boots | +1 | — | 20 | 30 | leather | Causes frequent fumbling. Generated cursed 9 times in 10. Avoid. |
| levitation boots | +1 | — | 15 | 30 | leather | Levitation. Generated cursed 9 times in 10. Cursed boots can't be taken off, so this is a trap item. |

:::

#### Shields

::: dense-table

| Armor | AC | MC | Wt | Cost | Material | Notes |
|--------------------------|----|----|----|------|----------|--------------------------------------------------------------------|
| small shield | +1 | — | 30 | 3 | wood |  |
| shield of drain resistance | +1 | — | 30 | 50 | wood | Drain resistance. |
| shield of shock resistance | +1 | — | 30 | 50 | wood | Shock resistance. |
| elven shield | +2 | — | 40 | 7 | wood |  |
| Uruk-hai shield | +1 | — | 50 | 7 | iron |  |
| orcish shield | +1 | — | 50 | 7 | iron |  |
| large shield | +2 | — | 100 | 10 | iron | Blocks two-handed weapons. |
| dwarvish roundshield | +2 | — | 100 | 10 | iron |  |
| shield of reflection | +2 | — | 50 | 50 | silver | Reflection. Saves the body-armor slot. |

:::

---

### Spell Tables
<!-- audit
2026-05-19:
- 41 spells, sourced from objects.h SPELL() macros (P_ATTACK..P_MATTER); SPELL macro signature at objects.h:1277-1281, oc_level=oc_oc2.
- attack spells at objects.h:1297-1330 (force bolt/magic missile/drain life/cone of cold/fireball/finger of death/chain lightning).
- healing spells at objects.h:1313-1408 (healing/cure blindness/cure sickness/extra healing/stone to flesh/restore ability).
- divination spells at objects.h:1308-1384 (light/detect monsters/detect food/clairvoyance/detect unseen/identify/detect treasure/magic mapping).
- enchantment spells at objects.h:1305-1354 (confuse monster/slow monster/cause fear/sleep/charm monster).
- cleric spells at objects.h:1337-1400 (protection/create monster/remove curse/create familiar/turn undead).
- escape spells at objects.h:1355-1404 (jumping/haste self/invisibility/levitation/teleport away).
- matter spells at objects.h:1293-1407 (knock/wizard lock/dig/polymorph/cancellation/stone to flesh).
- Flame sphere and freeze sphere are `#if 0 DEFERRED` (objects.h:1413-1422), NOT shipped in 5.0.
- Chain lightning is level 2 per macro (objects.h:1409-1411); body table at line 4986 and What's New at 8585 still say L4: follow-up fix.
- Magic missile IS Antimagic-blocked (zap.c:4410-4419, "missiles bounce off!"), NOT unresistable.
- Finger of death: monster MR resists, but player gets no Antimagic check on death-ray instakill (zap.c:2885-2902).
- Clairvoyance gets a P_SKILLED upgrade detecting nearby monsters per pulse (spell.c:1572-1576).
- Fireball/cone of cold become aimed explosions at P_SKILLED (spell.c spelleffects).
- Remove curse/confuse monster/detect food/cause fear/identify/charm monster get blessed-scroll behavior at P_SKILLED.
- Haste self/detect treasure/detect monsters/levitation/restore ability get blessed-potion behavior at P_SKILLED.
- Protection doubles uspmtime at P_EXPERT (spell.c:1169); jumping distance scales with role_skill.
- Charm monster is untargeted (read.c:1679-1708 seffect_taming is area-centered-on-caster, no direction prompt).
- Charm monster area: 3×3 normal, 11×11 confused (`bd = confused ? 5 : 1`, -bd..bd inclusive), NOT 5×5. (read.c:1689 seffect_taming)
- Charm monster P_SKILLED upgrade is blessed-scroll reliability, NOT a radius bump. (spell.c:1524-1525 sets pseudo->blessed when role_skill >= P_SKILLED; read.c:1689 radius `bd` depends only on `confused`, not on blessed)
- Cause fear blessed and uncursed are identical (read.c:1454-1486); loop hits every visible monster on the level, not just nearby.
- Remove curse blessed branch uncurses every non-coin inventory item (read.c:1514-1577), NOT just worn/wielded.
-->

The complete spellbook catalog, sorted by school then level. **Lvl**
is the spell level; **Pw cost** is always 5×level. **Type**
distinguishes how the spell targets:

- **aimed** — you pick a direction; the spell hits one square at that vector.
- **ray** — a beam from the caster through every square in a
  line until it stops.
- **untargeted** — no direction needed; the effect is on you,
  the level, or a fixed area.

**Upgrade** is the behavior change at **Skilled** rank or above
in that school (except for protection, which upgrades at Expert,
and jumping, which scales continuously).

::: dense-table

| Spell           | School      | Lvl | Type       | Effect                              | Upgrade                       |
|-----------------|-------------|-----|------------|-------------------------------------|-------------------------------|
| force bolt      | Attack      | 1   | aimed      | 2d12 magical hit                    | —                             |
| chain lightning | Attack      | 2   | untargeted | Shock damage to nearby monsters     | —                             |
| drain life      | Attack      | 2   | aimed      | Drains an XP level from target      | —                             |
| magic missile   | Attack      | 2   | ray        | 2d6 force ray; Antimagic blocks it  | —                             |
| cone of cold    | Attack      | 4   | ray        | 4d6 cold ray                        | Aimed explosion               |
| fireball        | Attack      | 4   | ray        | 4d6 fire ray                        | Aimed explosion               |
| finger of death | Attack      | 7   | ray        | Death-magic beam; monsters with magic resistance resist. (Against the player it's an instakill with no Antimagic check — only nonliving or demon forms are immune.) | —                             |
| healing         | Healing     | 1   | aimed      | Restore hit points                  | —                             |
| cure blindness  | Healing     | 2   | aimed      | Removes blindness                   | —                             |
| cure sickness   | Healing     | 3   | untargeted | Cures food poisoning and illness    | —                             |
| extra healing   | Healing     | 3   | aimed      | Heals more HP                       | —                             |
| stone to flesh  | Healing     | 3   | aimed      | Statue → corpse; cures stoning      | —                             |
| restore ability | Healing     | 4   | untargeted | Restores one drained stat           | Blessed: all stats            |
| detect monsters | Divination  | 1   | untargeted | Reveals monsters on level           | Blessed: longer duration      |
| light           | Divination  | 1   | untargeted | Lights the current room             | —                             |
| detect food     | Divination  | 2   | untargeted | Reveals food on level               | Blessed: identifies the food  |
| clairvoyance    | Divination  | 3   | untargeted | Periodic glimpses of nearby map     | Skilled: also detects nearby monsters during each pulse |
| detect unseen   | Divination  | 3   | untargeted | Reveals invisible monsters and traps | —                            |
| identify        | Divination  | 3   | untargeted | Identifies one inventory item       | Blessed: multiple items       |
| detect treasure | Divination  | 4   | untargeted | Reveals gold and gems               | Blessed: more detail          |
| magic mapping   | Divination  | 5   | untargeted | Reveals the entire level            | —                             |
| confuse monster | Enchantment | 1   | aimed      | Next melee hit confuses target      | Blessed: multiple hits        |
| slow monster    | Enchantment | 2   | aimed      | Slows target's speed                | —                             |
| cause fear      | Enchantment | 3   | untargeted | Visible monsters flee               | —                             |
| sleep           | Enchantment | 3   | ray        | Puts targets in line to sleep       | —                             |
| charm monster   | Enchantment | 5   | untargeted | Tames monsters in a 3×3 area              | Blessed-scroll behavior |
| protection      | Cleric      | 1   | untargeted | Temporary AC bonus paid from Pw     | **Expert**: 2× duration       |
| create monster  | Cleric      | 2   | untargeted | Summons a random monster nearby     | —                             |
| remove curse    | Cleric      | 3   | untargeted | Uncurses worn/wielded items         | Blessed: all carried items    |
| create familiar | Cleric      | 6   | untargeted | Creates a tame companion            | —                             |
| turn undead     | Cleric      | 6   | aimed      | Damages/turns undead and demons     | —                             |
| jumping         | Escape      | 1   | untargeted | Jump to a chosen nearby square      | Range scales with rank        |
| haste self      | Escape      | 3   | untargeted | Temporary fast movement             | Blessed: longer duration      |
| invisibility    | Escape      | 4   | untargeted | Become invisible                    | —                             |
| levitation      | Escape      | 4   | untargeted | Float over pits and water           | Blessed: longer duration      |
| teleport away   | Escape      | 6   | aimed      | Teleports target away               | —                             |
| knock           | Matter      | 1   | aimed      | Opens doors, picks locks            | —                             |
| wizard lock     | Matter      | 2   | aimed      | Closes and locks a door             | —                             |
| dig             | Matter      | 5   | ray        | Digs through walls, rock, floor     | —                             |
| polymorph       | Matter      | 6   | aimed      | Polymorphs target                   | —                             |
| cancellation    | Matter      | 7   | aimed      | Removes magical properties          | —                             |

:::

The to-hit chance of most rays (sleep, magic missile, finger of
death, and the unskilled forms of cone of cold and fireball) also
scales with rank.

---

### Bestiary Tables

Every monster you might meet. Grouped by ASCII symbol so you can flip to the right page mid-game. **Lvl** is the base monster level. **Spd** is movement rate (12 is normal player speed). **AC** is armor class (lower is better). **MR%** is the percentage chance the monster resists your spells and magic attacks. **Attacks** lists each attack's mode, damage dice, and side effect; multiple attacks separated by `·` are made per turn. **Notes** folds in the most tactically-relevant trait flags (flies, sees-invis, regenerates, poisonous-corpse, etc.) alongside specific heads-ups for monsters that deserve one.

#### Ants and insects `a`
<!-- audit
2026-05-19:
- 6 rows (S_ANT) sourced from monsters.h:89-133.
- giant ant L2/Spd18/AC3 bite 1d4 (monsters.h:89-95).
- killer bee L1/Spd18/AC-1 sting 1d3 AD_DRST, G_LGROUP, MR_POISON (monsters.h:96-102).
- soldier ant L3/Spd18/AC3 bite 2d4 + sting 3d4 AD_DRST, M1_POIS (monsters.h:103-110).
- fire ant L3/Spd18/AC3 bite 2d4 phys + 2d4 fire, MR_FIRE (monsters.h:111-118).
- giant beetle L5/Spd6/AC4 bite 3d6, M1_POIS, MR_POISON (monsters.h:119-125).
- queen bee L9/Spd24/AC-4 sting 1d8 AD_DRST, G_NOGEN, M2_FEMALE|M2_PRINCE (monsters.h:126-133).
- Killer/soldier/queen stings are AD_DRST (Str-drain, poison-family); shown as "poison" for beginner voice.
- Killer bee is G_LGROUP; others are smaller groups.
-->

Insects, often in groups. The soldier ant is the early game's infamous killer: its poison sting can two-shot a low-level hero. Killer bees swarm; the queen bee in a beehive room is tough on her own.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| giant ant | brown | 2 | 18 | 3 | 0 | bite 1d4 |  |
| killer bee | yellow | 1 | 18 | -1 | 0 | sting 1d3 poison | flies, poisonous-corpse, pois-res. Stings carry poison; a pack can wipe out an unprepared early hero. |
| soldier ant | blue | 3 | 18 | 3 | 0 | bite 2d4 · sting 3d4 poison | poisonous-corpse, pois-res. Poison sting. The most lethal `a` you'll meet in the early dungeon. |
| fire ant | red | 3 | 18 | 3 | 10 | bite 2d4 · bite 2d4 fire | fire-res. |
| giant beetle | black | 5 | 6 | 4 | 0 | bite 3d6 | poisonous-corpse, pois-res. |
| queen bee | magenta | 9 | 24 | -4 | 0 | sting 1d8 poison | flies, poisonous-corpse, pois-res. |

:::

#### Blobs `b`
<!-- audit
2026-05-19:
- 3 rows (S_BLOB) sourced from monsters.h:137-166.
- Acid blob passive: 50% splash + 1/30 corrode armor, plus passive_obj 1/6 erode on uwep/uarmg (uhitm.c:5906-5933).
- Gelatinous cube paralysis: 2/3 rate, free-action blocks (uhitm.c:6019-6064).
- Gelatinous cube in 5.0 is AT_TUCH only, NOT AT_ENGL like older versions. (monsters.h:157-158 AT_TUCH AD_PLYS 2d4 + AT_NONE AD_PLYS 1d4)
-->

Slow, mindless, immune to a lot. Don't melee an acid blob with bare hands or a metal weapon you care about: the passive acid corrodes both. Gelatinous cubes paralyse on touch.

All blobs are mindless, sleep-resistant, and poison-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| acid blob | green | 1 | 3 | 8 | 0 | passive 1d8 acid | amorphous, acid-res, ston-res. Passive acid damage — punching one corrodes your gloves. |
| quivering blob | white | 5 | 1 | 8 | 0 | touch 1d8 |  |
| gelatinous cube | cyan | 6 | 6 | 8 | 0 | touch 2d4 paralyse · passive 1d4 paralyse | fire-res, cold-res, shock-res, acid-res, ston-res. Slow but paralyses on touch. Don't melee without free-action. |

:::

#### Cockatrices `c`
<!-- audit
2026-05-19:
- 3 rows (chickatrice/cockatrice/pyrolisk) sourced from monsters.h:167-195.
- Chickatrice/cockatrice carry MR_POISON|MR_STONE; pyrolisk carries MR_POISON|MR_FIRE and does NOT stone. (monsters.h:174-175 chickatrice, 182-183 cockatrice both MR_POISON|MR_STONE; 191-192 pyrolisk MR_POISON|MR_FIRE; pyrolisk attacks are AT_GAZE AD_FIRE + AT_BITE AD_PHYS — no AD_STON)
- Wielding cockatrice corpse bare-handed instapetrifies regardless of role (wield.c:146-152).
-->

Medieval bestiary creature: a chicken with a serpent's tail whose touch turns flesh to stone. Carry a lizard corpse, fight gloved, and never wield a cockatrice corpse as a weapon unless your role explicitly resists stoning. See [Petrification](#petrification-stoning).

All cockatrices are poison-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| chickatrice | brown | 4 | 4 | 8 | 30 | bite 1d2 · touch petrify · passive petrify | ston-res. A small cockatrice. Same petrify rules apply. |
| cockatrice | yellow | 5 | 6 | 6 | 30 | bite 1d3 · touch petrify · passive petrify | ston-res. Touch petrifies. Always carry a lizard corpse. |
| pyrolisk | red | 6 | 6 | 6 | 30 | gaze 2d6 fire · bite 1d6 | fire-res. |

:::

<!-- audit
2026-05-19:
- 16 rows (S_DOG) sourced from monsters.h:199-320.
- Little-dog guaranteed roles: Caveman/Ranger/Samurai (role.c:128, 387, 428); Archeologist is NOT guaranteed (petnum=NON_PM coin-flips cat/dog).
- Cerberus carries only MR_FIRE (monsters.h:316), NOT Reflection; Cerberus is `#ifdef CHARON`-gated, not in default build.
- Werejackal/werewolf S_DOG and S_HUMAN are separate entries for shape-change machinery (monsters.h:264-266).
-->
#### Dogs and canines `d`

Wild canines hunt in packs. Domestic ones can be tamed by feeding (see [Making Friends](#making-friends)). Werejackals and werewolves can give lycanthropy.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| jackal | brown | 0 | 12 | 7 | 0 | bite 1d2 | The first thing that ever killed you. |
| fox | red | 0 | 15 | 7 | 0 | bite 1d3 |  |
| coyote | brown | 1 | 12 | 7 | 0 | bite 1d4 |  |
| werejackal | brown | 2 | 12 | 7 | 10 | bite 1d4 lyc | regenerates, poisonous-corpse, pois-res. |
| little dog | white | 2 | 18 | 6 | 0 | bite 1d6 | tameable. Guaranteed Caveman/Ranger/Samurai starting pet. |
| dingo | yellow | 4 | 16 | 5 | 0 | bite 1d6 |  |
| dog | white | 4 | 16 | 5 | 0 | bite 1d6 | tameable. |
| large dog | white | 6 | 15 | 4 | 0 | bite 2d4 | tameable. |
| wolf | gray | 5 | 12 | 4 | 0 | bite 2d4 |  |
| werewolf | gray | 5 | 12 | 4 | 20 | bite 2d6 lyc | regenerates, poisonous-corpse, pois-res. |
| winter wolf cub | cyan | 5 | 12 | 4 | 0 | bite 1d8 · breath 1d6 cold | cold-res. |
| warg | black | 7 | 12 | 4 | 0 | bite 2d6 |  |
| winter wolf | cyan | 7 | 12 | 4 | 20 | bite 2d6 · breath 2d6 cold | cold-res. |
| hell hound pup | red | 7 | 12 | 4 | 20 | bite 2d6 · breath 2d6 fire | fire-res. |
| hell hound | red | 12 | 14 | 2 | 20 | bite 3d6 · breath 3d6 fire | fire-res. |

:::

#### Eyes and spheres `e`
<!-- audit
2026-05-19:
- Roster sourced from monsters.h:325-366 (beholder omitted, `#if 0`).
- Floating eye paralysis requires mutual sight (canseemon + mon->mcansee per uhitm.c:6022-6053), NOT "in daylight."
- Floating eye corpse grants telepathy (eat.c:1071 TELEPAT case).
- No close-eyes command exists in 5.0; to break sight you must be Blind (status or worn blindfold/towel).
- Newbie-killer framing aligned with NetHackWiki: floating eye is "an infamous source of early game deaths" (https://nethackwiki.com/wiki/Floating_eye).
-->

The floating eye's passive paralysis gaze is the single most famous newbie killer in the game: never melee one without free action, blindness, or a ranged attack. Once it's dead, eat the corpse: it grants intrinsic telepathy.

All eyes and spheres fly. All except *floating eye* also are mindless.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| gas spore | gray | 1 | 3 | 10 | 0 | death-burst 4d6 |  |
| floating eye | blue | 2 | 1 | 9 | 10 | passive 0d70 paralyse | amphibious. (no mindless) Passive gaze paralyses on melee if you and the eye can both see each other. Use ranged, or wear a blindfold or towel to break sight. Corpse grants telepathy. |
| freezing sphere | white | 6 | 13 | 4 | 0 | explode 4d6 cold | cold-res. |
| flaming sphere | red | 6 | 13 | 4 | 0 | explode 4d6 fire | fire-res. |
| shocking sphere | bright-blue | 6 | 13 | 4 | 0 | explode 4d6 shock | shock-res. |

:::

#### Felines `f`
<!-- audit
2026-05-19:
- 8 rows (S_FELINE) sourced from monsters.h:381-444.
- kitten L2/Spd18/AC6 bite 1d6 (monsters.h:381-388).
- housecat L4/Spd16/AC5 bite 1d6 (monsters.h:389-396).
- large cat L6/Spd15/AC4 bite 2d4 (monsters.h:421-428).
- displacer beast L12/Spd12/AC-10 claw 4d4 + claw 4d4 + bite 2d10 (monsters.h:437-444).
- Tigers are M2_HOSTILE, difficulty 8: tameable only via charm-monster/scroll-of-taming/magic-flute, NOT tripe. (monsters.h:429-436 tiger has M2_HOSTILE only — no M2_DOMESTIC; befriend_with_obj at mondata.h:255-261 requires is_domestic for FOOD_CLASS items)
- Only Wizard guarantees a kitten (urole.petnum=PM_KITTEN per role.c:548); Valkyrie/Tourist roll 50/50 kitten-or-dog (dog.c:90-101).
-->

Cats. Kittens are common starting pets (Wizards always start with
one; Valkyries and Tourists roll 50/50 between kitten and little
dog). Wild felines (jaguar, lynx, panther, tiger, displacer beast)
are hostile by default; you'd need a charm-monster spell, scroll
of taming, or magic flute to flip them, and the wild rows aren't
really "early-game" creatures.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| kitten | white | 2 | 18 | 6 | 0 | bite 1d6 | tameable. Common pet. |
| housecat | white | 4 | 16 | 5 | 0 | bite 1d6 | tameable. |
| jaguar | brown | 4 | 15 | 6 | 0 | claw 1d4 · claw 1d4 · bite 1d8 |  |
| lynx | cyan | 5 | 15 | 6 | 0 | claw 1d4 · claw 1d4 · bite 1d10 |  |
| panther | black | 5 | 15 | 6 | 0 | claw 1d6 · claw 1d6 · bite 1d10 |  |
| large cat | white | 6 | 15 | 4 | 0 | bite 2d4 | tameable. |
| tiger | yellow | 6 | 12 | 6 | 0 | claw 2d4 · claw 2d4 · bite 1d10 |  |
| displacer beast | blue | 12 | 12 | -10 | 0 | claw 4d4 · claw 4d4 · bite 2d10 |  |

:::

#### Gremlins `g`
<!-- audit
2026-05-19:
- 3 rows (gremlin/gargoyle/winged gargoyle) sourced from monsters.h:448-473.
- Gremlin water/fountain trigger SPLIT: clones themselves, 2/3 chance per step (mon.c:987-992); does NOT touch your intrinsics.
- Gremlin night attack is AD_CURS: strips one random intrinsic, 1/10 per hit, night-only, blocked by cancellation (uhitm.c:3040-3057, sit.c:644+).
- Gargoyles do NOT petrify by touch or corpse: touch_petrifies is cockatrice/chickatrice only (mondata.h:200-201).
-->

At night, their touch strips a random intrinsic (fire resistance, telepathy, etc.). In water or fountains they split into more gremlins. Kill them on dry land, ideally during daylight.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| gremlin | green | 5 | 12 | 2 | 25 | claw 1d6 · claw 1d6 · bite 1d4 · claw curse | swims, poisonous-corpse, follows stairs, pois-res. |
| gargoyle | brown | 6 | 10 | -4 | 0 | claw 2d6 · claw 2d6 · bite 2d4 | ston-res. |
| winged gargoyle | magenta | 9 | 15 | -2 | 0 | claw 3d6 · claw 3d6 · bite 3d4 | flies, ston-res. |

:::

#### Humanoids `h`
<!-- audit
2026-05-19:
- 7 rows (S_HUMANOID) sourced from monsters.h:477-542.
- hobbit L1/Spd9/AC10 weapon 1d6 (monsters.h:477-484).
- dwarf L2/Spd6/AC10 weapon 1d8, M1_TUNNEL (monsters.h:485-493).
- dwarf lord L4/Spd6/AC10 weapon 2d4 ×2 (monsters.h:502-510).
- dwarf king L6/Spd6/AC10 weapon 2d6 ×2, MR 20% (monsters.h:511-520).
- mind flayer L9/Spd12/AC5 MR 90%, 3× tentacle AD_DRLI (monsters.h:521-530).
- master mind flayer L13/Spd12/AC0 MR 90%, 5× tentacle (monsters.h:531-542).
- helmet blocks mind-flayer tentacle 7/8 of the time (uhitm.c:3235, `uarmh && rn2(8)`).
- Any helmet blocks the mind flayer attack, NOT only alignment-matching or telepathy/free-action helmets.
- Bugbear is AT_WEAP only, no bite (monsters.h:494-501).
- Dwarf race peacefulness for Dwarf PCs via race_peaceful() at makemon.c:2283.
-->

Dwarves and similar. Dwarves carry better-than-average loot (weapons, armor, pick-axes) and can wreck low-level heroes with that loot.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| hobbit | green | 1 | 9 | 10 | 0 | weapon 1d6 |  |
| dwarf | red | 2 | 6 | 10 | 10 | weapon 1d8 | tunnels. |
| bugbear | brown | 3 | 9 | 5 | 0 | weapon 2d4 |  |
| dwarf lord | blue | 4 | 6 | 10 | 10 | weapon 2d4 · weapon 2d4 | tunnels. |
| dwarf king | magenta | 6 | 6 | 10 | 20 | weapon 2d6 · weapon 2d6 | tunnels. |
| mind flayer | bright-magenta | 9 | 12 | 5 | 90 | weapon 1d4 · tentacle 2d1 drain-Int · tentacle 2d1 drain-Int · tentacle 2d1 drain-Int | flies, sees-invis. Tentacle attacks drain Int; if Int hits 3 you die. Wear any helmet (blocks 7/8 of tentacles) or kill from range. |
| master mind flayer | bright-magenta | 13 | 12 | 0 | 90 | weapon 1d8 · tentacle 2d1 drain-Int · tentacle 2d1 drain-Int · tentacle 2d1 drain-Int · tentacle 2d1 drain-Int · tentacle 2d1 drain-Int | flies, sees-invis. Five tentacles per turn. Catastrophic adjacent without a helmet. Any helmet blocks 7/8 of tentacles. |

:::

<!-- audit
2026-05-19:
- 6 rows (`i` class) sourced from monsters.h:544-587; all carry M2_STALK.
- Imps only have AT_CLAW/AD_PHYS 1d4 (monsters.h:561-562); they do NOT steal or teleport (AD_SITM is nymphs, AD_SGLD is leprechauns).
- Imps MS_CUSS (verbal abuse, monmove.c:983-985, sounds.c:1148-1150).
- The `i` class is not M2_DEMON-tagged (is_demon() returns false). (monsters.h:544-587 S_IMP rows: no M2_DEMON flag set on any; mondata.h:110 is_demon checks mflags2 & M2_DEMON)
- Manes and lemure both carry G_NOCORPSE (monsters.h:545,567): no corpse.
- Lemure carries G_HELL (monsters.h:567): Gehennom-only generation.
-->
#### Imps and minor demons `i`

Annoying small fry. Imps mostly insult you and miss; quasits drain Dexterity. None individually scary.

All imps and minor demons follow you up and down stairs. All except *imp* are poison-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| manes | red | 1 | 3 | 7 | 0 | claw 1d3 · claw 1d3 · bite 1d4 | sleep-res. No corpse. |
| homunculus | green | 2 | 12 | 6 | 10 | bite 1d3 sleep | flies, poisonous-corpse, sleep-res. |
| imp | red | 3 | 12 | 2 | 20 | claw 1d4 | regenerates. (no pois-res) |
| lemure | brown | 3 | 3 | 7 | 0 | claw 1d3 | Gehennom-only, regenerates, sleep-res. No corpse. |
| quasit | blue | 3 | 15 | 2 | 20 | claw 1d2 drain-Dx · claw 1d2 drain-Dx · bite 1d4 | regenerates. |
| tengu | cyan | 6 | 13 | 5 | 30 | bite 1d7 | teleports, teleport-control. |

:::

#### Jellies `j`
<!-- audit
2026-05-19:
- 3 rows (blue/spotted/ochre jelly) sourced from monsters.h:591-620; all carry M1_AMORPHOUS|M1_MINDLESS.
- Blue jelly corpse conveys cold + poison resistance permanently (eat.c:983-988 should_givit).
- Spotted/ochre corpses convey acid + stone resistance TIMED (eat.c:991-997 temp_givit).
- Passive 0d6 still inflicts the AD_COLD/AD_ACID side effect (item damage on acid); dice damage is literally zero.
-->

Stationary or near-stationary. The blue jelly's passive cold and the spotted jelly's passive acid bite even when you hit them.

All jellies are amorphous and mindless.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| blue jelly | blue | 4 | 0 | 8 | 10 | passive 0d6 cold | corpse: cold + poison resistance. |
| spotted jelly | green | 5 | 0 | 8 | 10 | passive 0d6 acid | corpse: temp acid + stone resistance. |
| ochre jelly | brown | 6 | 3 | 8 | 20 | engulf 3d6 acid · passive 3d6 acid | corpse: temp acid + stone resistance. |

:::

#### Kobolds `k`
<!-- audit
2026-05-19:
- 4 rows (kobold/large/lord/shaman) sourced from monsters.h:624-657.
- kobold L0/Spd6/AC10 weapon 1d4 (monsters.h:624-631).
- large kobold L1/Spd6/AC10 weapon 1d6 (monsters.h:632-639).
- kobold lord L2/Spd6/AC10 weapon 2d4 (monsters.h:640-648).
- kobold shaman L2/Spd6/AC6 MR 10% (monsters.h:649-657).
- All four carry M1_POIS (poisonous corpse) and MR_POISON.
- Kobold shaman has only one AT_MAGC/AD_SPEL attack (monsters.h:651); notation is "cast spell," not "spell spell."
-->


Weak early-game fodder. Most are poisonous to eat — leave the corpses unless you have poison resistance.

All kobolds have poisonous corpses and are poison-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| kobold | brown | 0 | 6 | 10 | 0 | weapon 1d4 |  |
| large kobold | red | 1 | 6 | 10 | 0 | weapon 1d6 |  |
| kobold lord | magenta | 2 | 6 | 10 | 0 | weapon 2d4 |  |
| kobold shaman | bright-blue | 2 | 6 | 6 | 10 | cast spell |  |

:::

#### Leprechauns `l`
<!-- audit
2026-05-19:
- Leprechaun (Lvl 5, Spd 15, AC 8, MR 20, green, claw 1d2 AD_SGLD), M1_TPORT, AT_CLAW (not bite): monsters.h:660-666, steal.c:58-115.
- Stolen gold goes into mtmp->minvent and drops on death.
- An unseen leprechaun off the shop floor can bury its gold 1-in-4 per turn (monmove.c:1152-1171 leppie_stash); killing later may not recover it.
-->


Steals gold and teleports away. The fix is to carry no gold near them, or to kill from range. The corpse drops the gold back.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| leprechaun | green | 5 | 15 | 8 | 20 | claw 1d2 steal-gold | teleports. Steals gold and teleports away. Carry no gold near them. |

:::

#### Mimics `m`
<!-- audit
2026-05-19:
- 3 rows (small/large/giant mimic) sourced from monsters.h:670-698.
- All carry M1_AMORPHOUS|M1_HIDE|MR_ACID; large/giant also have AD_STCK and M2_STRONG.
- Disguise via set_mimic_sym (makemon.c:2393-2472), including STRANGE_OBJECT in shops at sufficient depth.
- AD_STCK is MC-blocked (uhitm.c:3310/3324).
-->

Disguised as items, walls, or fountains. Common in shops and zoos. The giveaway is the wrong object on the wrong square.

All mimics are amorphous, hide, and are acid-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| small mimic | brown | 7 | 3 | 7 | 0 | claw 3d4 |  |
| large mimic | red | 8 | 3 | 7 | 10 | claw 3d4 sticky |  |
| giant mimic | magenta | 9 | 3 | 7 | 20 | claw 3d6 sticky · claw 3d6 sticky |  |

:::

#### Nymphs `n`
<!-- audit
2026-05-19:
- 3 nymphs (wood/water/mountain): LVL 3, Spd 12, AC 9, MR 20%, AT_CLAW AD_SITM + AT_CLAW AD_SEDU, M1_TPORT (monsters.h:702-723).
- Water nymph has M1_SWIM (line 714); all three carry M1_TPORT|MR_POISON.
- AD_SITM steal-and-teleport at uhitm.c:4724,4798; AD_SEDU at uhitm.c:4642.
- Corpse grants intrinsic teleportitis at 10% per should_givit (eat.c:936-975).
-->


Steals one item and teleports away. The cure is to engage from range, block her path with pets, or wear an amulet of life saving and steal the item back from her corpse later.

All nymphs teleport.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| wood nymph | green | 3 | 12 | 9 | 20 | claw steal-item · claw seduce |  |
| water nymph | blue | 3 | 12 | 9 | 20 | claw steal-item · claw seduce | swims. |
| mountain nymph | brown | 3 | 12 | 9 | 20 | claw steal-item · claw seduce |  |

:::

#### Orcs `o`
<!-- audit
2026-05-19:
- 8 rows (S_ORC) sourced from monsters.h:727-796.
- goblin L0/Spd6/AC10 weapon 1d4 (monsters.h:727-733).
- hobgoblin L1/Spd9/AC10 weapon 1d6 (monsters.h:734-742).
- orc L1/Spd9/AC10 weapon 1d8, MR_POISON (monsters.h:743-751).
- hill orc L2/Spd9/AC10 weapon 1d6 (monsters.h:752-760).
- Mordor orc L3/Spd5/AC10 weapon 1d6 (monsters.h:761-769); Spd 5 is correct in 5.0.
- Uruk-hai L3/Spd7/AC10 weapon 1d8 (monsters.h:770-778).
- orc shaman L3/Spd9/AC5 single AT_MAGC/AD_SPEL (monsters.h:779-787); "spell," not "spell spell."
- orc-captain L5/Spd5/AC10 weapon 2d4 ×2 (monsters.h:788-796).
- Goblin is correctly placed in S_ORC (monsters.h:727).
-->

Pack hunters with mediocre loot but real numbers; bring a chokepoint to the Mines.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| goblin | gray | 0 | 6 | 10 | 0 | weapon 1d4 |  |
| hobgoblin | brown | 1 | 9 | 10 | 0 | weapon 1d6 |  |
| orc | red | 1 | 9 | 10 | 0 | weapon 1d8 | pois-res. |
| hill orc | yellow | 2 | 9 | 10 | 0 | weapon 1d6 | pois-res. |
| Mordor orc | blue | 3 | 5 | 10 | 0 | weapon 1d6 | pois-res. |
| Uruk-hai | black | 3 | 7 | 10 | 0 | weapon 1d8 | pois-res. |
| orc shaman | bright-blue | 3 | 9 | 5 | 10 | spell | pois-res. |
| orc-captain | magenta | 5 | 5 | 10 | 0 | weapon 2d4 · weapon 2d4 | pois-res. Hits hard. Drops decent loot. |

:::

<!-- audit
2026-05-19:
- 3 rows (rock/iron/glass piercer) sourced from monsters.h:800-826.
- rock piercer L3/Spd1/AC3 bite 2d6 (monsters.h:800-808).
- iron piercer L5/Spd1/AC0 bite 3d6 (monsters.h:809-817).
- glass piercer L7/Spd1/AC0 bite 4d6, MR_ACID (monsters.h:818-826).
- All carry M1_HIDE|M1_CLING (ceiling-hiders per mondata.h:43-45); hiding gated by has_ceiling (mon.c:4672).
- Drop-on-walk-under is d(4,6) for ALL species regardless of bite die (hack.c:3436).
-->
#### Piercers `p`

Clings to the ceiling and drops on you when you walk under. Hits hard for its level; you can't avoid the drop without flying or a clear ceiling.

All piercers hide.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| rock piercer | gray | 3 | 1 | 3 | 0 | bite 2d6 |  |
| iron piercer | cyan | 5 | 1 | 0 | 0 | bite 3d6 |  |
| glass piercer | white | 7 | 1 | 0 | 0 | bite 4d6 | acid-res. |

:::

#### Quadrupeds `q`
<!-- audit
2026-05-19:
- 7 rows (rothe through mastodon) sourced from monsters.h:831-885.
- rothe L2/Spd9/AC7 claw 1d3 + bite 1d3 + bite 1d8 (monsters.h:831-837).
- mumak L5/Spd9/AC0 butt 4d12 + bite 2d6 (monsters.h:838-845).
- leocrotta L6/Spd18/AC4 (monsters.h:846-853).
- wumpus L8/Spd3/AC2 bite 3d6, M1_CLING (monsters.h:854-861).
- mastodon L20/Spd12/AC5 butt 4d8 ×2 (monsters.h:878-885).
-->


Mixed bag. Rothes are early-game wreckers (three attacks per turn). Mumakil are slow but hit for 4d12 and shrug off blows.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| rothe | brown | 2 | 9 | 7 | 0 | claw 1d3 · bite 1d3 · bite 1d8 |  |
| mumak | gray | 5 | 9 | 0 | 0 | butt 4d12 · bite 2d6 |  |
| leocrotta | red | 6 | 18 | 4 | 10 | claw 2d6 · bite 2d6 · claw 2d6 |  |
| wumpus | cyan | 8 | 3 | 2 | 10 | bite 3d6 | clings. |
| titanothere | gray | 12 | 12 | 6 | 0 | claw 2d8 |  |
| baluchitherium | gray | 14 | 12 | 5 | 0 | claw 5d4 · claw 5d4 |  |
| mastodon | black | 20 | 12 | 5 | 0 | butt 4d8 · butt 4d8 |  |

:::

#### Rodents `r`
<!-- audit
2026-05-19:
- 6 rows (S_RODENT) sourced from monsters.h:889-936.
- Woodchuck color is brown (CLR_BROWN at monsters.h:936).
- Rock mole is M1_METALLIVORE: eats metal, including bag of gold and unattended weapons (mondata.c:561, hack.c:769-784).
-->

Mostly nuisance fodder. Giant rats are common in the early dungeon; their corpses are safe food.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| sewer rat | brown | 0 | 12 | 7 | 0 | bite 1d3 |  |
| giant rat | brown | 1 | 10 | 7 | 0 | bite 1d3 |  |
| rabid rat | brown | 2 | 12 | 6 | 0 | bite 2d4 drain-Co | poisonous-corpse, pois-res. |
| wererat | brown | 2 | 12 | 6 | 10 | bite 1d4 lyc | regenerates, poisonous-corpse, pois-res. |
| rock mole | gray | 3 | 3 | 0 | 20 | bite 1d6 | tunnels, eats metal. Will chew through your bag of gold or unattended weapons. |
| woodchuck | brown | 3 | 3 | 0 | 20 | bite 1d6 | swims, tunnels. |

:::

#### Arachnids and centipedes `s`
<!-- audit
2026-05-19:
- 5 rows (cave spider, centipede, giant spider, scorpion, Scorpius) sourced from monsters.h:940-972, 3713-3722.
- Webmaker only on cave spider + giant spider (mondata.h:147-148); M1_CONCEAL on all except giant spider.
- Cave spider/centipede corpses safe (no M1_POIS); giant spider/scorpion corpses poisonous (M1_POIS).
- Scorpius MR_STONE confers stoning resistance via corpse.
-->

Includes scorpions and centipedes. Many have poison stings. Spider-class monsters are common as the source of poisonous-corpse food poisoning.

All arachnids and centipedes are poison-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| cave spider | gray | 1 | 12 | 3 | 0 | bite 1d2 | hides. |
| centipede | yellow | 2 | 4 | 3 | 0 | bite 1d3 poison | hides. |
| giant spider | magenta | 5 | 15 | 4 | 0 | bite 2d4 poison | poisonous-corpse. |
| scorpion | red | 5 | 15 | 3 | 0 | claw 1d2 · claw 1d2 · sting 1d4 poison | hides, poisonous-corpse. |
| Scorpius | magenta | 15 | 12 | 10 | 0 | claw 2d6 · claw 2d6 steal-amulet · sting 1d4 disease | poisonous-corpse, follows stairs, ston-res. |

:::

#### Trappers and lurkers `t`
<!-- audit
2026-05-19:
- Lurker above (gray L10 Spd3 AC3 MR0, engulf 1d6 + wrap 2d6) and trapper (green L12 Spd3 AC3 MR0, engulf 1d8 + wrap 2d8): monsters.h:981-998.
- Both have M1_HIDE; lurker is M1_FLY (ceiling hider per mondata.h:43-45); trapper is floor hider.
- Damage is AD_WRAP+AD_PHYS, NOT AD_DGST (monsters.h:973-980 retcon).
- Both M2_STALK (follow stairs).
-->

Stationary engulfers that look like a piece of dungeon. Stepping into one starts a swallow attack you can't easily escape. Identify with `;` (farlook) before walking into obvious-trap squares.

All trappers and lurkers hide and follow you up and down stairs.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| lurker above | gray | 10 | 3 | 3 | 0 | engulf 1d6 wrap · engulf 2d6 | flies. |
| trapper | green | 12 | 3 | 3 | 0 | engulf 1d8 wrap · engulf 2d8 |  |

:::

<!-- audit
2026-05-19:
- 6 rows (pony/white/gray/black unicorn/horse/warhorse) sourced from monsters.h:1002-1049.
- Unicorn alignments: white lawful/+7, gray neutral/0, black chaotic/-7 (monsters.h:1011,1019,1027).
- Co-aligned unicorns spawn peaceful (makemon.c:1339-1342); killing co-aligned costs -5 Luck and triggers "feel guilty" (mon.c:3666-3669); cross-aligned: no Luck change.
- mpeaceful is set only for is_unicorn(); wild horses (ponies/horses/warhorses) spawn hostile. The 1/100 saddled-spawn (makemon.c:1447-1452) is NOT peaceful.
- Throwing any gem at a unicorn placates it unconditionally (dothrow.c:2087-2098, 2309-2382); worthless glass works without Luck change.
- Knight's pony starts saddled (dog.c:262-268).
- Killed unicorn drops its horn (mon.c:604-613).
-->
#### Unicorns and horses `u`

There are two equine `u`-class creatures. **Horses** (pony, horse, warhorse) spawn hostile in the wild but can be tamed, saddled, and ridden; the Knight starts on a saddled pony.

**Unicorns** (white, gray, black for Lawful, Neutral, Chaotic) are powerful kickers, peaceful when your alignment matches theirs and hostile otherwise. Killing a co-aligned unicorn is a −5 Luck penalty (the game tells you "You feel guilty..."). Killing a cross-aligned one has no Luck consequence either way. If you don't want the fight, throw any gem — even worthless glass — to pacify a hostile unicorn at no cost; throwing real gems also adjusts your Luck (see [Luck and Fortune](#luck-and-fortune)). A killed unicorn drops its horn.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| pony | brown | 3 | 16 | 6 | 0 | kick 1d6 · bite 1d2 | tameable. Knight's starting steed. |
| white unicorn | white | 4 | 24 | 2 | 70 | butt 1d12 · kick 1d6 | pois-res. |
| gray unicorn | gray | 4 | 24 | 2 | 70 | butt 1d12 · kick 1d6 | pois-res. |
| black unicorn | black | 4 | 24 | 2 | 70 | butt 1d12 · kick 1d6 | pois-res. |
| horse | brown | 5 | 20 | 5 | 0 | kick 1d8 · bite 1d3 | tameable. |
| warhorse | brown | 7 | 24 | 4 | 0 | kick 1d10 · bite 1d4 | tameable. |

:::

#### Vortices `v`
<!-- audit
2026-05-19:
- 6 rows (S_VORTEX) sourced from monsters.h:1053-1110.
- Damage types are physical/blinding/cold/shock+drain/fire; NO vortex deals poison.
- Speeds: fog cloud Lvl 3/Spd 1; dust/ice/energy Spd 20; steam/fire Spd 22. Only fog cloud is slow, NOT all stationary. (monsters.h:1052 fog cloud LVL(3,1,...); 1062 dust LVL(4,20,...); 1071 ice LVL(5,20,...); 1081 energy LVL(6,20,...); 1091 steam LVL(7,22,...); 1101 fire LVL(8,22,...))
- Energy vortex: AT_NONE+AD_ELEC passive 0d4 + AD_DREN drain (monsters.h:1081-1090).
- Fire vortex: AT_NONE+AD_FIRE passive 0d4 (monsters.h:1101-1110).
- All carry M1_FLY|M1_MINDLESS|G_NOCORPSE.
-->

Engulfing elemental clouds. Different colors deal different damage types: blinding sand, cold, shock (which also drains Pw), and fire. Only the fog cloud is slow; the rest move at speed 20-22 and will close on you.

All vortices fly, are mindless, and leave no corpse.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| fog cloud | gray | 3 | 1 | 0 | 0 | engulf 1d6 | amorphous. |
| dust vortex | brown | 4 | 20 | 2 | 30 | engulf 2d8 blind |  |
| ice vortex | cyan | 5 | 20 | 2 | 30 | engulf 1d6 cold |  |
| energy vortex | bright-blue | 6 | 20 | 2 | 30 | engulf 1d6 shock · engulf 2d6 drain-Pw · passive 0d4 shock |  |
| steam vortex | blue | 7 | 22 | 2 | 30 | engulf 1d8 fire |  |
| fire vortex | yellow | 8 | 22 | 2 | 30 | engulf 1d10 fire · passive 0d4 fire |  |

:::

#### Worms `w`
<!-- audit
2026-05-19:
- 4 rows (S_WORM) sourced from monsters.h:1114-1145: baby long worm 1118, baby purple 1124, long worm 1130, purple worm 1138.
- Long worm tail and segment mechanics in worm.c; purple worm AT_ENGL/AD_DGST swallow at monsters.h:1141.
- Long worm drops worm tooth on death; fires only for PM_LONG_WORM, not baby (mon.c:618-620).
- Long worm grown segments tracked via mtmp->wormno (mon.c:5451, get_wormno on polymorph to PM_LONG_WORM).
-->

Long worms become a maze of tail segments as they grow. Purple worms swallow you whole and digest. Don't get cornered.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| baby long worm | brown | 5 | 3 | 5 | 0 | bite 1d4 |  |
| baby purple worm | magenta | 8 | 3 | 5 | 0 | bite 1d6 |  |
| long worm | brown | 9 | 3 | 5 | 10 | bite 2d4 | drops a worm tooth. |
| purple worm | magenta | 15 | 9 | 6 | 20 | bite 2d8 · engulf 1d10 digest |  |

:::

#### Xans and fantastic insects `x`
<!-- audit
2026-05-19:
- Grid bug row at monsters.h:1149-1156; xan row at monsters.h:1157-1164.
- Grid bug AT_BITE/AD_ELEC 1d1; xan AT_STNG/AD_LEGS 1d4, M1_FLY plus M1_POIS (poisonous corpse).
- Xan AD_LEGS / Wounded_legs reduces carry capacity (hack.c:4331-4336) and abuses Dex (attrib.c:472, 581); it does NOT slow movement.
-->

Grid bugs are trivial; xans, the bigger relatives, sting your legs and cut your carrying capacity.

All xans and fantastic insects are poison-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| grid bug | magenta | 0 | 12 | 9 | 0 | bite 1d1 shock | shock-res. |
| xan | red | 7 | 18 | -4 | 0 | sting 1d4 leg-wound | flies, poisonous-corpse. |

:::

#### Lights `y`
<!-- audit
2026-05-19:
- 2 rows (yellow light L3 yellow, black light L5 black) sourced from monsters.h:1168-1191.
- Attacks AT_EXPL/AD_BLND 10d20 (yellow) and AT_EXPL/AD_HALU 10d12 (black).
- M1_FLY|M1_AMORPHOUS|M1_MINDLESS on both; black light adds M1_SEE_INVIS.
- 10d20 is blindness DURATION, NOT HP damage. (uhitm.c:2978-2985 mhitm_ad_blnd: `make_blinded(BlindedTimeout + (long) mhm->damage, FALSE); mhm->damage = 0;` — rolled value feeds timer, HP damage zeroed)
- AT_EXPL means the monster dies on attack ("bursts on contact").
-->

Yellow light bursts on contact and blinds you for 10d20 turns. Black light bursts and hallucinates you for 10d12 turns. See [Light Bursts](#light-bursts).

All lights fly and are amorphous and mindless.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| yellow light | yellow | 3 | 15 | 0 | 0 | explode 10d20 blind |  |
| black light | black | 5 | 15 | 0 | 0 | explode 10d12 hallu | sees-invis. |

:::

<!-- audit
2026-05-19:
- Zruty row LVL(9,8,3,0,0), CLR_BROWN, claw 3d4 · claw 3d4 · bite 3d6: monsters.h:1192-1202.
- freq G_GENO|2; M1_HUMANOID + M2_STRONG.
-->
#### Zruties `z`

Slavic folklore — a hairy wild man of the woods. One species, one role here: a nasty mid-game brute. Good XP if you can handle the three-attack flurry.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| zruty | brown | 9 | 8 | 3 | 0 | claw 3d4 · claw 3d4 · bite 3d6 |  |

:::

#### Angelic beings `A`
<!-- audit
2026-05-19:
- 5 rows at monsters.h:1206-1265 (couatl 1206, Aleax 1216, Angel 1225, ki-rin 1240, Archon 1252).
- All Angels have G_NOCORPSE; couatl leaves no corpse (MR_POISON still matters for combat).
- AD_MAGM ("magic") on Angel; AD_SPEL ("spell") on ki-rin/Archon.
- Ki-rin HI_GOLD = yellow; Archon HI_LORD = magenta (color.h:38,46).
- Archon has M1_REGEN, M1_SEE_INVIS, plus 5-attack chain (weapon, weapon, gaze, claw, spell).
-->

Powerful late-game spellcasters with weapons. Astral-Plane Angels guard each High Priest — see [The Ascension Run](#the-ascension-run).

All angelic beings follow you up and down stairs. All except *Aleax* also fly. All except *couatl* also see invisible.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| couatl | green | 8 | 10 | 5 | 30 | bite 2d4 poison · bite 1d3 · hug 2d4 wrap | pois-res. (no sees-invis, no corpse) |
| Aleax | yellow | 10 | 8 | 0 | 30 | weapon 1d6 · weapon 1d6 · kick 1d4 | (no flies) |
| Angel | white | 14 | 10 | -4 | 55 | weapon 1d6 · weapon 1d6 · claw 1d4 · spell 2d6 magic |  |
| ki-rin | yellow | 16 | 18 | -5 | 90 | kick 2d4 · kick 2d4 · butt 3d6 · spell 2d6 spell |  |
| Archon | magenta | 19 | 16 | -6 | 80 | weapon 2d4 · weapon 2d4 · gaze 2d6 blind · claw 1d8 · spell 4d6 spell | regenerates. |

:::

<!-- audit
2026-05-19:
- 4 rows (S_BAT) sourced from monsters.h:1269-1297.
- Vampire bat 2nd bite is AD_DRST (Str-drain, poison-flavored); NOT lycanthropy (AD_WERE is were-creatures, not bats). (monsters.h:1292 AT_BITE AD_PHYS + AT_BITE AD_DRST — no AD_WERE)
- Both AT_BITE slots roll independently each turn (uhitm.c:3149-3157, `!rn2(8)`); NOT sequential.
- Erratic-fly behavior from S_BAT class branch (monmove.c:1870-1871).
-->
#### Bats and birds `B`

Erratic flyers, mostly nuisance. Vampire bats drain Strength with a poisoned bite (poison resistance blocks it).

All bats and birds fly.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| bat | brown | 0 | 22 | 8 | 0 | bite 1d4 |  |
| giant bat | red | 2 | 22 | 7 | 0 | bite 1d6 |  |
| raven | black | 4 | 20 | 6 | 0 | bite 1d6 · claw 1d6 blind |  |
| vampire bat | black | 5 | 20 | 6 | 0 | bite 1d6 · bite drain-Str | regenerates, poisonous-corpse, sleep-res, pois-res. |

:::

#### Centaurs `C`
<!-- audit
2026-05-19:
- 3 rows (plains/forest/mountain) sourced from monsters.h:1301-1323; complete S_CENTAUR roster.
- Centaurs are half-horse, NOT mounted on a horse. (https://nethackwiki.com/wiki/Centaur)
- Forest centaurs spawn with BOW+arrows; plains and mountain centaurs spawn with CROSSBOW+bolts (50% armed rate per makemon.c:474-484).
-->

Half-horse archers with strong physical attacks. Forest centaurs wield bows; plains and mountain centaurs wield crossbows. They shoot at range.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| plains centaur | brown | 4 | 18 | 4 | 0 | weapon 1d6 · kick 1d6 |  |
| forest centaur | green | 5 | 18 | 3 | 10 | weapon 1d8 · kick 1d6 |  |
| mountain centaur | cyan | 6 | 20 | 2 | 10 | weapon 1d10 · kick 1d6 · kick 1d6 |  |

:::

#### Dragons `D`
<!-- audit
2026-05-19:
- 10 baby + 10 adult + Chromatic + Ixoth sourced from monsters.h:1325-1562; Ixoth at monsters.h:3642-3690.
- Shimmering dragon is `#if 0 DEFERRED`, NOT in 5.0 (monsters.h:1365-1374 baby and 1466-1482 adult shimmering dragon blocks are inside `#if 0 /* DEFERRED */`).
- Silver dragon color is CLR_BRIGHT_CYAN (color.h:54), NOT gray, for both baby and adult.
- Baby blue dragon has only bite 2d6; NO breath weapon (monsters.h:1408-1415, no AT_BREA). Babies don't breathe.
- Black dragon breath is AD_DISN 1d255 (instakill without reflection or disint-res), monsters.h:1494.
- Chromatic random-breath AT_BREA/AD_RBRE selects breath type per zap (mhitu.c).
-->


Each adult dragon breathes its element type. Reflection bounces the ranged breath back. **Babies don't breathe** — they're just biters until they grow up. Adults are the source of dragon scale mail. See [Dragon Scale Mail](#armor-tables).

All except *Chromatic Dragon* also fly.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| baby gray dragon | gray | 12 | 9 | 2 | 10 | bite 2d6 |  |
| baby gold dragon | yellow | 12 | 9 | 2 | 10 | bite 2d6 |  |
| baby silver dragon | bright-cyan | 12 | 9 | 2 | 10 | bite 2d6 |  |
| baby red dragon | red | 12 | 9 | 2 | 10 | bite 2d6 |  |
| baby white dragon | white | 12 | 9 | 2 | 10 | bite 2d6 |  |
| baby orange dragon | orange | 12 | 9 | 2 | 10 | bite 2d6 |  |
| baby black dragon | black | 12 | 9 | 2 | 10 | bite 2d6 |  |
| baby blue dragon | blue | 12 | 9 | 2 | 10 | bite 2d6 |  |
| baby green dragon | green | 12 | 9 | 2 | 10 | bite 2d6 | poisonous-corpse. |
| baby yellow dragon | yellow | 12 | 9 | 2 | 10 | bite 2d6 |  |
| gray dragon | gray | 15 | 9 | -1 | 20 | breath 4d6 magic · bite 3d8 · claw 1d4 · claw 1d4 | sees-invis. Anti-magic breath. Magic resistance helps; reflection doesn't. |
| gold dragon | yellow | 15 | 9 | -1 | 20 | breath 4d6 fire · bite 3d8 · claw 1d4 · claw 1d4 | sees-invis. Fire breath. Drops gold-colored scales (light source). |
| silver dragon | bright-cyan | 15 | 9 | -1 | 20 | breath 4d6 cold · bite 3d8 · claw 1d4 · claw 1d4 | sees-invis. Cold breath plus reflection scales: your reflection target. |
| red dragon | red | 15 | 9 | -1 | 20 | breath 6d6 fire · bite 3d8 · claw 1d4 · claw 1d4 | sees-invis. Cone of fire. Get fire resistance before you meet one. |
| white dragon | white | 15 | 9 | -1 | 20 | breath 4d6 cold · bite 3d8 · claw 1d4 · claw 1d4 | sees-invis. Cone of cold. Cold resistance. |
| orange dragon | orange | 15 | 9 | -1 | 20 | breath 4d25 sleep · bite 3d8 · claw 1d4 · claw 1d4 | sees-invis. Sleep ray. Sleep resistance trivialises. |
| black dragon | black | 15 | 9 | -1 | 20 | breath 1d255 disint · bite 3d8 · claw 1d4 · claw 1d4 | sees-invis. Disintegration breath. Disint resistance OR reflection. |
| blue dragon | blue | 15 | 9 | -1 | 20 | breath 4d6 shock · bite 3d8 · claw 1d4 · claw 1d4 | sees-invis. Cone of lightning. Shock resistance. |
| green dragon | green | 15 | 9 | -1 | 20 | breath 4d6 poison · bite 3d8 · claw 1d4 · claw 1d4 | sees-invis, poisonous-corpse. Poison breath; poison resistance is enough. |
| yellow dragon | yellow | 15 | 9 | -1 | 20 | breath 4d6 acid · bite 3d8 · claw 1d4 · claw 1d4 | sees-invis. Acid breath; rare. |
| Chromatic Dragon | magenta | 16 | 12 | 0 | 30 | breath 6d6 rnd-breath · spell spell · claw 2d8 steal-amulet · bite 4d8 · bite 4d8 · sting 1d6 | sees-invis, poisonous-corpse, follows stairs. (no flies) |
| Ixoth | red | 15 | 12 | -1 | 20 | breath 8d6 fire · bite 4d8 · spell spell · claw 2d4 · claw 2d4 steal-amulet | sees-invis, follows stairs. |

:::

#### Elementals `E`
<!-- audit
2026-05-19:
- 5 rows (stalker/air/fire/earth/water elemental) sourced from monsters.h:1566-1610.
- Stalker: sees-invis, M2_STALK; NOT mindless. (monsters.h:1566-1573 has M1_SEE_INVIS and M2_STALK; no M1_MINDLESS in flags1)
- Air: AT_ENGL AD_PHYS 1d10. "Air suffocates" is engulf flavor for AD_PHYS, NOT a separate AD_DRST. (monsters.h:1576 air elemental single AT_ENGL AD_PHYS 1d10; no AD_DRST attack)
- Fire: claw 3d6 AD_FIRE + passive 0d4 fire.
- Earth: claw 4d6; MR_FIRE|MR_COLD|MR_POISON|MR_STONE.
- Water: claw 5d6; M1_SWIM|M1_AMPHIBIOUS; MR_POISON|MR_STONE. Water elementals lack a drown attack, but spawn only on water tiles so encounters happen near drowning risk.
-->

Air engulfs and suffocates, fire deals fire damage, water drowns if you're adjacent in water, earth is slow but tough.

All except *stalker* also are mindless.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| stalker | white | 8 | 12 | 3 | 0 | claw 4d4 | flies, sees-invis, follows stairs. (no mindless) |
| air elemental | cyan | 8 | 36 | 2 | 30 | engulf 1d10 | flies. |
| fire elemental | yellow | 8 | 12 | 2 | 30 | claw 3d6 fire · passive 0d4 fire | flies. |
| earth elemental | brown | 8 | 6 | 2 | 30 | claw 4d6 | fire-res, cold-res, pois-res, ston-res. |
| water elemental | blue | 8 | 5 | 2 | 30 | claw 5d6 | swims, amphibious, pois-res, ston-res. |

:::

#### Fungi and molds `F`
<!-- audit
2026-05-19:
- 7 rows sourced from monsters.h:1614-1676; elemental molds are brown/green/red, NOT violet/yellow.
- Lichen corpse never rots (mkobj.c:1402, eat.c:59); also never out of season as iron rations.
- Yellow mold has M1_POIS (poisonous corpse, monsters.h yellow-mold row).
- Other molds have MR_POISON resistance but no M1_POIS, so their corpses are NOT poisonous.
- Brown mold passive 0d6 cold (HP drain), green 0d4 acid, red 0d4 fire, yellow 0d4 stun (monsters.h:1614-1666).
- Violet fungus AT_TUCH/AD_PHYS 1d4 plus AT_TUCH/AD_PLYS sticky (monsters.h:1668-1676).
-->

Stationary. Lichen corpses never rot — keep one in your pack as iron rations. Brown, green, and red molds bite back on melee with elemental passive damage (cold, acid, fire). Yellow mold stuns on passive contact; violet fungus has an active touch attack with sticking.

All fungi and molds are mindless.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| lichen | bright-green | 0 | 1 | 9 | 0 | touch sticky |  |
| brown mold | brown | 1 | 0 | 9 | 0 | passive 0d6 cold | cold-res, pois-res. |
| yellow mold | yellow | 1 | 0 | 9 | 0 | passive 0d4 stun | poisonous-corpse, pois-res. |
| green mold | green | 1 | 0 | 9 | 0 | passive 0d4 acid | acid-res, ston-res. |
| red mold | red | 1 | 0 | 9 | 0 | passive 0d4 fire | fire-res, pois-res. |
| shrieker | magenta | 3 | 1 | 7 | 0 | — | pois-res. |
| violet fungus | magenta | 3 | 1 | 7 | 0 | touch 1d4 · touch sticky | pois-res. |

:::

#### Gnomes `G`
<!-- audit
2026-05-19:
- All four S_GNOME entries match monsters.h:1681-1709.
- Gnomish wizard has one AT_MAGC/AD_SPEL attack, "cast spell" (monsters.h:1697), NOT two spell attacks.
- No "deep gnome" exists in 5.0 (correctly omitted).
- Gnome PCs (Archeologist default) see most S_GNOME as peaceful via MH_GNOME lovemask (makemon.c:2283).
-->

Mines residents. Gnomish PCs find most of them peaceful. The gnome lord and gnomish wizard are real threats; the gnome king is rare but dangerous.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| gnome | brown | 1 | 6 | 10 | 4 | weapon 1d6 |  |
| gnome lord | blue | 3 | 8 | 10 | 4 | weapon 1d8 |  |
| gnomish wizard | bright-blue | 3 | 10 | 4 | 10 | cast spell |  |
| gnome king | magenta | 5 | 10 | 10 | 20 | weapon 2d6 |  |

:::

#### Giant humanoids `H`
<!-- audit
2026-05-19:
- Frost giant and storm giant melee is AD_PHYS only; cold/shock resistance does NOT reduce damage (monsters.h frost/storm rows at 1748, 1772).
- Fire giant melee is AD_PHYS only; fire resistance does NOT make them weak offensively (monsters.h:1738).
- Cyclops is the Healer quest nemesis (Hea-goal.lua:74, monsters.h:1792-1800), NOT Caveman.
- Surtur does NOT carry Mjollnir (Mjollnir is a Valkyrie quest artifact, artilist.h).
- Ettin and minotaur are NOT M2_GIANT, so their corpses do not grant Str (eat.c:1345; monsters.h:1758, 1782).
- Minotaur roams Gehennom mazes (mkmaze.c:1112, makemon at maze fill), NOT vaults.
-->

Boulder throwers. Storm / fire / frost giants match the dragon elements; titans cast spells. Eating a true giant's corpse raises Strength; the ettin and minotaur don't count as giants for this purpose.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| giant | red | 6 | 6 | 0 | 0 | weapon 2d10 |  |
| stone giant | gray | 6 | 6 | 0 | 0 | weapon 2d10 |  |
| hill giant | cyan | 8 | 10 | 6 | 0 | weapon 2d8 |  |
| fire giant | yellow | 9 | 12 | 4 | 5 | weapon 2d10 | fire-res. Throws boulders. |
| frost giant | white | 10 | 12 | 3 | 10 | weapon 2d12 | cold-res. Throws boulders. |
| ettin | brown | 10 | 12 | 3 | 0 | weapon 2d8 · weapon 3d6 |  |
| storm giant | blue | 16 | 12 | 3 | 10 | weapon 2d12 | shock-res. Throws boulders for big damage. |
| titan | magenta | 16 | 18 | -3 | 70 | weapon 2d8 · spell spell | flies. Tough humanoid with magic missiles. Casts spells. |
| minotaur | brown | 15 | 15 | 6 | 0 | claw 3d10 · claw 3d10 · butt 2d8 | Two claws plus a butt. Heavy hitter; roams the Gehennom mazes. |
| Cyclops | gray | 18 | 12 | 0 | 0 | weapon 4d8 · weapon 4d8 · claw 2d6 steal-amulet | follows stairs, ston-res. Healer quest nemesis. Throws boulders. |
| Lord Surtur | magenta | 15 | 12 | 2 | 50 | weapon 2d10 · weapon 2d10 · claw 2d6 steal-amulet | follows stairs, fire-res, ston-res. Valkyrie quest nemesis. |

:::

#### Jabberwocks `J`
<!-- audit
2026-05-19:
- Jabberwock: L15 Spd12 AC-2 MR50, 4x 2d10 attacks, M1_FLY, G_GENO|1 (monsters.h:1806-1814).
- Speed 12 is player baseline, NOT slow; most dragons are speed 9 (slower).
- Vorpal Blade auto-beheads PM_JABBERWOCK, short-circuiting the dieroll==1 check (artifact.c:1595-1623).
- Deferred "vorpal jabberwock" at monsters.h:1816-1824 is wrapped in `#if 0` and correctly excluded.
-->

The monster from Lewis Carroll's *Jabberwocky* ("O frabjous day! Callooh! Callay!"). Tough, hits hard, and moves at player baseline speed: you can't simply walk away. Free XP if you're set up for the fight; lethal if you walk into one early. Vorpal Blade was made for beheading it.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| jabberwock | orange | 15 | 12 | -2 | 50 | bite 2d10 · bite 2d10 · claw 2d10 · claw 2d10 | flies. Powerful; baseline speed. Free XP if you're set up. |

:::

#### Keystone Kops `K`
<!-- audit
2026-05-19:
- All Kop stats match monsters.h:1829-1860.
- Shopkeeper-anger triggers Kop summoning via makekops (shk.c:623, 680, 5113).
- Dead Kops respawn per rnd(5) at mon.c:3147-3164: 1/5 near DOWN-stairs, 1/5 at random location, 3/5 stay dead.
- Respawn lands near DOWN-stairs, NOT up-stairs (stairs.c:89-95, mklev.c:2193).
- All four Kops carry G_GENO, so genocide permanently clears them.
-->

Police force triggered by stealing from shops or hurting shopkeepers. Mostly weak individually but they swarm — and dead Kops respawn: each fallen Kop has a 1-in-5 chance to come back near the down-stairs and a 1-in-5 chance to come back at a random location, so killing them isn't a stable solution. Get away or genocide them instead.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| Keystone Kop | blue | 1 | 6 | 10 | 10 | weapon 1d4 |  |
| Kop Sergeant | blue | 2 | 8 | 10 | 10 | weapon 1d6 |  |
| Kop Lieutenant | cyan | 3 | 10 | 10 | 20 | weapon 1d8 |  |
| Kop Kaptain | magenta | 4 | 12 | 10 | 20 | weapon 2d6 |  |

:::

#### Liches `L`
<!-- audit
2026-05-19:
- 4 lich rows at monsters.h:1864-1897 (lich 1864, demilich 1872, master lich 1880, arch-lich 1889).
- All carry G_NOCORPSE, so no eatable corpse regardless of M1_POIS flavor.
- Only the arch-lich (m_lev=25) reaches DEATH_TOUCH at spell-level 20; master lich m_lev=17 cannot (mcastu.c:111).
- Double-trouble is Wizard-of-Yendor only, NOT a lich ability.
- Arch-lich casts touch of death, NOT rays.
-->

Skeletal spellcasters. The arch-lich can cast touch of death; master and arch-liches both require magic resistance to survive their spell barrages.

All liches regenerate, leave no corpse, and are undead, cold-resistant, sleep-resistant, and poison-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| lich | brown | 11 | 6 | 0 | 30 | touch 1d10 cold · spell spell |  |
| demilich | red | 14 | 9 | -2 | 60 | touch 3d4 cold · spell spell |  |
| master lich | magenta | 17 | 9 | -4 | 90 | touch 3d6 cold · spell spell | fire-res. Casts wizard spells. Kill from afar. |
| arch-lich | magenta | 25 | 9 | -6 | 90 | touch 5d6 cold · spell spell | fire-res, shock-res. Casts touch of death; magic resistance mandatory. |

:::

#### Mummies `M`
<!-- audit
2026-05-19:
- Every mummy attack is plain AD_PHYS (monsters.h:1901-1968); mummies do NOT curse worn items (only gremlins have AD_CURS, monattk.h:92).
- All M-class rows carry G_NOCORPSE; mummies leave NO corpse, NOT a poisonous one (monsters.h:1902,1910,1918,1927,1936,1944,1953,1961).
- Mummies are vulnerable to undead-turning.
-->

Mindless undead. Wand and scroll of undead turning shred them.

All mummies are mindless undead and leave no corpse.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| kobold mummy | brown | 3 | 8 | 6 | 20 | claw 1d4 | cold-res, sleep-res, pois-res. |
| gnome mummy | red | 4 | 10 | 6 | 20 | claw 1d6 | cold-res, sleep-res, pois-res. |
| orc mummy | gray | 5 | 10 | 5 | 20 | claw 1d6 | cold-res, sleep-res, pois-res. |
| dwarf mummy | red | 5 | 10 | 5 | 20 | claw 1d6 | cold-res, sleep-res, pois-res. |
| elf mummy | green | 6 | 12 | 4 | 30 | claw 2d4 | cold-res, sleep-res, pois-res. |
| human mummy | gray | 6 | 12 | 4 | 30 | claw 2d4 · claw 2d4 | cold-res, sleep-res, pois-res. |
| ettin mummy | blue | 7 | 12 | 4 | 30 | claw 2d6 · claw 2d6 | cold-res, sleep-res, pois-res. |
| giant mummy | cyan | 8 | 14 | 3 | 30 | claw 3d4 · claw 3d4 | cold-res, sleep-res, pois-res. |

:::

<!-- audit
2026-05-19:
- All 8 naga rows match monsters.h:1972-2048 and carry MR_POISON.
- Guardian naga is NOT auto-peaceful to Healers; lawful PCs may find them peaceful (maligntyp +7, monsters.h:2040, peace_minded at makemon.c:2270-2285).
- Only red naga breathes (AT_BREA fire); black/guardian spit (AT_SPIT); golden casts spells (AT_MAGC AD_SPEL). NOT a uniform "breath weapon" group.
- Golden naga attack is "cast spell 4d6" via AT_MAGC, NOT "spell 4d6 spell".
- Black naga corpse confers poison + acid + stoning resistance.
-->
#### Nagas `N`

Long serpentine bodies with ranged attacks. All nagas are poison-resistant. Black naga corpses confer poison, acid, *and* stoning resistance. That's easily the best of the four eats.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| red naga hatchling | red | 3 | 10 | 6 | 0 | bite 1d4 | fire-res. |
| black naga hatchling | black | 3 | 10 | 6 | 0 | bite 1d4 | acid-res, ston-res. |
| golden naga hatchling | yellow | 3 | 10 | 6 | 0 | bite 1d4 |  |
| guardian naga hatchling | green | 3 | 10 | 6 | 0 | bite 1d4 |  |
| red naga | red | 6 | 12 | 4 | 0 | bite 2d4 · breath 2d6 fire | fire-res. |
| black naga | black | 8 | 14 | 2 | 10 | bite 2d6 · spit acid | acid-res, ston-res. |
| golden naga | yellow | 10 | 14 | 2 | 70 | bite 2d6 · cast spell 4d6 |  |
| guardian naga | green | 12 | 16 | 0 | 50 | spit 1d6 poison · bite 1d6 paralyse · touch · hug 2d4 wrap | poisonous-corpse. Lawful PCs may find them peaceful. |

:::

#### Ogres `O`
<!-- audit
2026-05-19:
- 3 ogre rows match monsters.h: ogre 2052, ogre lord 2060, ogre king 2068.
- Ogres wield weapons (AT_WEAP); they do NOT throw boulders (no M2_ROCKTHROW — that's giants/Cyclops/ettins/titans).
- All three carry M2_STRONG plus G_GENO|1 (genocidable, freq 1).
-->

Big melee brutes that wield weapons. Drop decent weapons and armor.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| ogre | brown | 5 | 10 | 5 | 0 | weapon 2d5 |  |
| ogre lord | red | 7 | 12 | 3 | 30 | weapon 2d6 |  |
| ogre king | magenta | 9 | 14 | 4 | 60 | weapon 3d5 |  |

:::

#### Puddings and oozes `P`
<!-- audit
2026-05-19:
- Green slime: make_slimed sets a 10-turn countdown, NOT 9 (uhitm.c:3199, 3570; polyself.c:456; eat.c:854). The 5-turn case is engulf+digest only (uhitm.c:5099).
- Brown puddings rot wood/leather/cloth/bone (AD_DCAY = ERODE_ROT, uhitm.c:2389). They do NOT corrode armor.
- Black puddings corrode metal (AD_CORR, uhitm.c:2338-2356).
- Gray ooze rusts armor (AD_RUST).
- Splitting on iron/metal melee is gated to PM_BLACK_PUDDING || PM_BROWN_PUDDING (uhitm.c:1609-1621). Gray ooze and green slime do NOT split.
-->


**Brown and black puddings split** when you hit them with an iron or metal melee weapon. Brown puddings **rot** your wood/leather/cloth/bone armor on bite; black puddings **corrode** your metal armor on bite *and* corrode your wielded metal weapon on the passive return-hit. Gray ooze **rusts** metal armor but doesn't split. Fire-kill puddings so they don't multiply, or pick a chokepoint.

**Green slime** is a Gehennom-only exception: doesn't split, leaves a glob, and one touch starts a 10-turn countdown to becoming one yourself. Fight at range, burn yourself with fire to clear it, or wear an **amulet of unchanging** (blocks and aborts the transformation). Prayer doesn't work in Gehennom, so don't rely on it. See *Delayed Deaths* for the full cure list.

All puddings and oozes are amorphous, mindless, cold-resistant, poison-resistant, acid-resistant, and petrification-resistant. All except *gray ooze* also are shock-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| gray ooze | gray | 3 | 1 | 8 | 0 | bite 2d8 rust | fire-res. (no shock-res) |
| brown pudding | brown | 5 | 3 | 8 | 0 | bite decay |  |
| green slime | green | 6 | 6 | 6 | 0 | touch 1d4 slime · passive slime | poisonous-corpse. |
| black pudding | black | 10 | 6 | 6 | 0 | bite 3d8 corrode · passive corrode |  |

:::

#### Quantum mechanics `Q`
<!-- audit
2026-05-19:
- Quantum mechanic teleports you (AD_TLPT, monsters.h:2127); genetic engineer polymorphs you (AD_POLY, monsters.h:2136, new in 5.0 per fixes5-0-0.txt:2696). NOT both teleporting.
- Both have speed 12 (NOT 24), poisonous corpses (M1_POIS), and self-teleport (M1_TPORT).
- Quantum corpse toggles Fast (eat.c:1227); genetic engineer corpse triggers polyself (eat.c:1247).
-->

The `Q` class is two creatures, both with random claw effects. The
**quantum mechanic** teleports you on a hit: the annoyance is the
lost position more than the damage, but in dangerous neighbourhoods
a random teleport CAN kill. The **genetic engineer** polymorphs
you: unless you have *Unchanging* or magic resistance, one claw
and you become something else.

Both species also teleport themselves at random, and both leave
poisonous corpses.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| quantum mechanic | cyan | 7 | 12 | 3 | 10 | claw 1d4 teleport | Self-teleports. Corpse toggles intrinsic Fast. |
| genetic engineer | green | 12 | 12 | 3 | 10 | claw 1d4 polymorph | Self-teleports. Corpse triggers polyself. |

:::

#### Rust monsters and disenchanters `R`
<!-- audit
2026-05-19:
- Rust monster active attack erodes worn iron armor (uhitm.c:2311); passive damages weapon when you hit it; greased weapons consume a charge instead. Silver/mithril/wood weapons immune (is_rustprone).
- Disenchanter active claw drains armor first (uhitm.c:3611-3644, some_armor + rn2(5) for rings/amulet/blindfold); weapon drain is passive-only.
- Active threat for both is armor, NOT weapons (e.g. long sword).
-->

Rust monsters rust iron equipment on touch. Disenchanters drain enchantment from your armor when they hit you, and drain enchantment from your weapon when you hit them (passive counterattack). Either way, strip irreplaceable kit before engaging, and switch to silver or non-iron weapons against the rust monster.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| rust monster | brown | 5 | 18 | 2 | 0 | touch rust · touch rust · passive rust | swims. Touch rusts iron. Strip armor before engaging or use silver. |
| disenchanter | blue | 12 | 12 | -10 | 0 | claw 4d4 disenchant · passive disenchant | Gehennom-only. Active drains armor; passive drains weapon when you melee it. |

:::

#### Snakes `S`
<!-- audit
2026-05-19:
- 6 snake rows at monsters.h:2167-2221: garter 2167, snake 2174, water moccasin 2182, python 2190, pit viper 2204, cobra 2213.
- "Pit viper" is the snake, NOT "pit fiend" (pit fiend is a `&` major demon at monsters.h:3104-3112).
- M1_SWIM universal across the section; M1_CONCEAL on all except python.
- Python has an AT_TUCH plus AT_HUGS pair (monsters.h:2193-2199), wrap and crush.
- Cobra AT_SPIT/AD_BLND blind at monsters.h:2218 (blind spit out to 6 squares).
-->

Mostly poisonous. The pit viper and the cobra are the dangerous ones; garter snakes are fodder.

All snakes swim. All except *python* also hide.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| garter snake | green | 1 | 8 | 8 | 0 | bite 1d2 |  |
| snake | brown | 4 | 15 | 3 | 0 | bite 1d6 poison | poisonous-corpse, pois-res. |
| water moccasin | red | 4 | 15 | 3 | 0 | bite 1d6 poison | poisonous-corpse, pois-res. |
| python | magenta | 6 | 3 | 5 | 0 | bite 1d4 · touch · hug 1d4 wrap · hug 2d4 | (no hides) |
| pit viper | blue | 6 | 15 | 2 | 0 | bite 1d4 poison · bite 1d4 poison | poisonous-corpse, pois-res. |
| cobra | blue | 6 | 18 | 2 | 0 | bite 2d4 poison · spit blind | poisonous-corpse, pois-res. |

:::

#### Trolls `T`
<!-- audit
2026-05-19:
- All 5 troll rows (troll, ice, rock, water, Olog-hai) match monsters.h:2225-2266.
- All carry M1_REGEN | M2_STALK; S_TROLL is is_reviver (mondata.h:170).
- Fire/water/force-bolt do NOT destroy corpses; burn_floor_objects only burns scrolls/spellbooks/slime.
- Trollsbane sets mkcorpstat_norevive (uhitm.c:1906, 4867; mhitm.c:1082).
- Stoning leaves a statue (mon.c:671), so no corpse to revive from.
-->

Regenerates from corpses on a timer. Three reliable ways to keep a troll dead: **eat the corpse** before it revives; **kill it with Trollsbane wielded** (the artifact disables the revive timer); or **stone it** so it leaves a statue instead of a corpse. A troll left behind on an old level will be alive when you come back.

All trolls regenerate and follow you up and down stairs.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| troll | brown | 7 | 12 | 4 | 0 | weapon 4d2 · claw 4d2 · bite 2d6 |  |
| ice troll | white | 9 | 10 | 2 | 20 | weapon 2d6 · claw 2d6 cold · bite 2d6 | cold-res. |
| rock troll | cyan | 9 | 12 | 0 | 0 | weapon 3d6 · claw 2d8 · bite 2d6 |  |
| water troll | blue | 11 | 14 | 4 | 40 | weapon 2d8 · claw 2d8 · bite 2d6 | swims. |
| Olog-hai | magenta | 13 | 12 | -4 | 0 | weapon 3d6 · claw 2d8 · bite 2d6 |  |

:::

<!-- audit
2026-05-19:
- Umber hulk stats and M1_TUNNEL match monsters.h:2267-2277.
- Free_action does NOT block AD_CONF (mhitu.c:1759-1777); it only protects against paralysis, holding, and sleep.
- Blindness blocks the gaze (gated by mcanseeu at mhitu.c:1681-1682).
- Confusion does NOT block spellcasting (only Stunned does, spell.c:687-708); it garbles spellbook study (spell.c:368, 620) and worsens forgetting when zapped (spell.c:1778-1782).
-->
#### Umber hulks `U`

Confusion gaze. Don't melee without some way to dodge the gaze — blindness defeats it (the gaze requires mutual sight); free action does *not* (it covers paralysis, holding, and sleep, never confusion). The confusion stacks and wrecks navigation, and confused spellbook study garbles the spell.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| umber hulk | brown | 9 | 6 | 2 | 25 | claw 3d4 · claw 3d4 · bite 2d5 · gaze confuse | tunnels. Confusion gaze. Hard to navigate around. Hits hard too. |

:::

#### Vampires `V`
<!-- audit
2026-05-19:
- 3 vampire rows at monsters.h: vampire 2282, vampire lord 2292, Vlad 2306.
- All carry G_NOCORPSE plus M2_UNDEAD; they leave NO corpse, NOT a poisonous one.
- All have M1_REGEN | M1_FLY plus M2_STALK (follows stairs) and shapeshift via M2_WERE-equivalent vamp branch (mon.c).
- Vampire mage is #if 0 DEFERRED in 5.0 (correctly omitted).
- Vlad inhabits Vlad's Tower; holds the Candelabrum of Invocation (mkobj.c spawn for PM_VLAD).
-->

Drains XL on bite. Shapeshifts to bat or cloud. Vlad the Impaler is the boss of Vlad's Tower.

All vampires fly, regenerate, are undead, follow you up and down stairs, and shapeshift.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| vampire | red | 10 | 12 | 1 | 25 | claw 1d6 · bite 1d6 drain-XL |  |
| vampire lord | blue | 12 | 14 | 0 | 50 | claw 1d8 · bite 1d8 drain-XL |  |
| Vlad the Impaler | magenta | 28 | 26 | -6 | 80 | weapon 2d10 · bite 1d12 drain-XL | Vampire boss in Vlad's Tower. Has the Candelabrum. |

:::

#### Wraiths `W`
<!-- audit
2026-05-19:
- 3 wraith rows at monsters.h: barrow wight 2326, wraith 2336, Nazgul 2343-2353.
- Only plain wraith leaves an eatable corpse; barrow wight and Nazgul carry G_NOCORPSE.
- Wraith corpse grants experience-level gain (eat.c:1141-1142, pluslvl).
- Nazgul AT_BREA/AD_SLEE breath 2d25 sleep (monsters.h Nazgul row); sleep resistance trivializes.
-->

Drains XL on touch. The wraith corpse, however, **gives** a level when eaten: one of the best food items in the game. Always eat a wraith corpse if you can.

All wraiths are undead and follow you up and down stairs.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| barrow wight | gray | 3 | 12 | 5 | 5 | weapon drain-XL · spell spell · claw 1d4 · touch 1d4 cold | cold-res, sleep-res, pois-res. |
| wraith | black | 6 | 12 | 4 | 15 | touch 1d6 drain-XL | flies. |
| Nazgul | magenta | 13 | 12 | 0 | 25 | weapon 1d4 drain-XL · breath 2d25 sleep | sees-invis. |

:::

#### Xorns `X`
<!-- audit
2026-05-19:
- Xorn stats match monsters.h:2357-2366: speed 9 (NOT fast), 3-claw + bite, MR_FIRE|MR_COLD|MR_STONE.
- Xorns phase through walls via M1_WALLWALK; they do NOT tunnel (no M1_TUNNEL, no rubble left behind).
- Xorn attacks are AD_PHYS only; worn weapons/armor are NOT at risk. Metallivore behavior eats metal off the floor only (monmove.c:1664).
- Xorn corpse grants temporary stone resistance.
-->

D&D's three-armed, three-eyed creatures from the Elemental Plane of Earth. They **phase through walls** (no rubble, no dig) and **eat metal items off the floor** — including the orcish dagger you were about to pick up. Their claws and bite are physical only, so worn armor and wielded weapons aren't directly at risk, but they hit hard for their level. The corpse grants temporary stoning resistance.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| xorn | brown | 8 | 9 | -2 | 20 | claw 1d3 · claw 1d3 · claw 1d3 · bite 4d6 | fire-res, cold-res, ston-res. |

:::

#### Apelike creatures `Y`
<!-- audit
2026-05-19:
- 6 ape/yeti rows at monsters.h:2372-2417 (monkey 2372, ape 2379, owlbear 2386, yeti 2393, carnivorous ape 2402, sasquatch 2409).
- Monkey steals via AT_CLAW/AD_SITM (monsters.h:2376); yeti M1_POIS-free, M2_BRUTE plus MR_COLD intrinsic donor.
- Sasquatch has M1_SEE_INVIS (monsters.h:2413); both yeti and sasquatch speed 15.
-->


Apes and great apes mostly; sasquatches are fast. Carnivore corpses are safe food.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| monkey | gray | 2 | 12 | 6 | 0 | claw steal-item · bite 1d3 |  |
| ape | brown | 4 | 12 | 6 | 0 | claw 1d3 · claw 1d3 · bite 1d6 |  |
| owlbear | brown | 5 | 12 | 5 | 0 | claw 1d6 · claw 1d6 · hug 2d8 |  |
| yeti | white | 5 | 15 | 6 | 0 | claw 1d6 · claw 1d6 · bite 1d4 | cold-res. |
| carnivorous ape | black | 6 | 12 | 6 | 0 | claw 1d4 · claw 1d4 · hug 1d8 |  |
| sasquatch | gray | 7 | 15 | 6 | 0 | claw 1d6 · claw 1d6 · kick 1d8 | sees-invis. |

:::

#### Zombies `Z`
<!-- audit
2026-05-19:
- All Z-class stats/attacks match monsters.h:2421-2504.
- All Z entries carry G_NOCORPSE; zombies leave NO corpse to eat, regardless of M1_POIS.
- Skeleton has G_NOGEN: never randomly generated, only from skeleton-trap or special-level placement.
- M2_UNDEAD is the class flag (NOT "M3_UNDEAD"); M2_STALK is universal across this section.
-->

Slow undead. Easy to kite. **Zombies never leave corpses on
death**, so eating is a non-issue, but undead-turning effects
(scroll, spell of turn undead, wand of undead turning) deal heavy
damage to the whole class. The **skeleton** doesn't generate
randomly: it only appears from a skeleton trap or a fixed
placement (e.g., Vlad's Tower). Big zombie populations live in
morgues.

All zombies are mindless and undead.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| kobold zombie | brown | 0 | 6 | 10 | 0 | claw 1d4 | poisonous-corpse, follows stairs, cold-res, sleep-res, pois-res. |
| gnome zombie | brown | 1 | 6 | 10 | 0 | claw 1d5 | poisonous-corpse, follows stairs, cold-res, sleep-res, pois-res. |
| orc zombie | gray | 2 | 6 | 9 | 0 | claw 1d6 | poisonous-corpse, follows stairs, cold-res, sleep-res, pois-res. |
| dwarf zombie | red | 2 | 6 | 9 | 0 | claw 1d6 | poisonous-corpse, follows stairs, cold-res, sleep-res, pois-res. |
| elf zombie | green | 3 | 6 | 9 | 0 | claw 1d7 | follows stairs. |
| human zombie | white | 4 | 6 | 8 | 0 | claw 1d8 | follows stairs. |
| ettin zombie | blue | 6 | 8 | 6 | 0 | claw 1d10 · claw 1d10 | follows stairs, cold-res, sleep-res, pois-res. |
| ghoul | black | 3 | 6 | 10 | 0 | claw 1d2 paralyse · claw 1d3 | poisonous-corpse, cold-res, sleep-res, pois-res. |
| giant zombie | cyan | 8 | 8 | 6 | 0 | claw 2d8 · claw 2d8 | follows stairs, cold-res, sleep-res, pois-res. |
| skeleton | white | 12 | 8 | 4 | 0 | weapon 2d6 · touch 1d6 slow | cold-res, sleep-res, pois-res, ston-res. |

:::

#### Humans and elves `@`
<!-- audit
2026-05-19:
- 43 human rows match monsters.h.
- Kops are class K, NOT @.
- Wizard of Yendor row: bright-magenta, L30 Spd12 AC-8 MR100, claw 2d12 steal-amulet + spell, flies/regen/sees-invis/fire-res/poison-res, covetous (monsters.h:2847-2858).
- Master of Thieves is the Rogue quest LEADER (Rog-strt.lua:106) AND the Tourist quest nemesis (Tou-goal.lua:117, monsters.h:3564), NOT the Rogue quest nemesis.
- Master Assassin is the primary Rogue quest nemesis (Rog-goal.lua:72), NOT a backup.
-->

The catch-all `@` class: shopkeepers, priests, watchmen, role nemeses, quest leaders, soldiers, ninja, doppelgangers, weres, Medusa, Croesus, the Wizard of Yendor, and the player. Most start peaceful; the ones that don't are very dangerous. (Kops are *not* in this class — they're `K`.)

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| human | white | 0 | 12 | 10 | 0 | weapon 1d6 |  |
| wererat | brown | 2 | 12 | 10 | 10 | weapon 2d4 | regenerates, poisonous-corpse. |
| werejackal | red | 2 | 12 | 10 | 10 | weapon 2d4 | regenerates, poisonous-corpse. |
| werewolf | orange | 5 | 12 | 10 | 20 | weapon 2d4 | regenerates, poisonous-corpse. |
| elf | white | 0 | 12 | 10 | 2 | weapon 1d8 | sees-invis. |
| Woodland-elf | green | 4 | 12 | 10 | 10 | weapon 2d4 | sees-invis. |
| Green-elf | bright-green | 5 | 12 | 10 | 10 | weapon 2d4 | sees-invis. |
| Grey-elf | gray | 6 | 12 | 10 | 10 | weapon 2d4 | sees-invis. |
| elf-lord | bright-blue | 8 | 12 | 10 | 20 | weapon 2d4 · weapon 2d4 | sees-invis. |
| Elvenking | magenta | 9 | 12 | 10 | 25 | weapon 2d4 · weapon 2d4 | sees-invis. |
| doppelganger | white | 9 | 12 | 5 | 20 | weapon 1d12 | shapeshifter. |
| shopkeeper | white | 12 | 16 | 0 | 50 | weapon 4d4 · weapon 4d4 | starts peaceful. Don't anger one. |
| guard | blue | 12 | 12 | 10 | 40 | weapon 4d10 | starts peaceful. |
| prisoner | white | 12 | 12 | 10 | 0 | weapon 1d6 | starts peaceful. |
| Oracle | bright-blue | 12 | 0 | 0 | 50 | passive 0d4 magic | starts peaceful. |
| priest | white | 12 | 12 | 10 | 50 | weapon 4d10 · kick 1d4 · spell cleric | starts peaceful. Temple defenders. Convert their altars or sacrifice on them. |
| high priest | white | 25 | 15 | 7 | 70 | weapon 4d10 · kick 2d8 · spell 2d8 cleric · spell 2d8 cleric | sees-invis. Endgame altar guardian. Don't fight one head-on. |
| soldier | gray | 6 | 10 | 10 | 0 | weapon 1d8 | follows stairs. |
| sergeant | red | 8 | 10 | 10 | 5 | weapon 2d6 | follows stairs. |
| nurse | white | 11 | 6 | 0 | 0 | claw 2d6 heal |  |
| lieutenant | green | 10 | 10 | 10 | 15 | weapon 3d4 · weapon 3d4 | follows stairs. |
| captain | blue | 12 | 10 | 10 | 15 | weapon 4d4 · weapon 4d4 | follows stairs. |
| watchman | gray | 6 | 10 | 10 | 0 | weapon 1d8 | follows stairs, starts peaceful. |
| watch captain | green | 10 | 10 | 10 | 15 | weapon 3d4 · weapon 3d4 | follows stairs, starts peaceful. |
| Medusa | bright-green | 20 | 12 | 2 | 50 | weapon 2d4 · claw 1d8 · gaze petrify · bite 1d6 poison | flies, swims, amphibious, poisonous-corpse. |
| Wizard of Yendor | bright-magenta | 30 | 12 | -8 | 100 | claw 2d12 steal-amulet · spell spell | flies, regenerates, sees-invis, fire-res, poison-res. Covetous: teleports to you in late Gehennom and on the planes. The final boss. |
| Croesus | magenta | 20 | 15 | 0 | 40 | weapon 4d10 | sees-invis, follows stairs. Vault guardian on Fort Ludios. Wields a two-handed sword and hoards gold, gems, and magic items off the floor. |
| Charon | white | 76 | 18 | -5 | 120 | weapon 1d8 · touch 1d8 paralyse | sees-invis, starts peaceful. |
| archeologist | white | 10 | 12 | 10 | 1 | weapon 1d6 · weapon 1d6 | tunnels. |
| barbarian | white | 10 | 12 | 10 | 1 | weapon 1d6 · weapon 1d6 |  |
| caveman | white | 10 | 12 | 10 | 0 | weapon 2d4 |  |
| healer | white | 10 | 12 | 10 | 1 | weapon 1d6 |  |
| knight | white | 10 | 12 | 10 | 1 | weapon 1d6 · weapon 1d6 |  |
| monk | white | 10 | 12 | 10 | 2 | claw 1d8 · kick 1d8 |  |
| priest | white | 10 | 12 | 10 | 2 | weapon 1d6 · spell cleric | Temple defenders. Convert their altars or sacrifice on them. |
| ranger | white | 10 | 12 | 10 | 2 | weapon 1d4 |  |
| rogue | white | 10 | 12 | 10 | 1 | weapon 1d6 · weapon 1d6 |  |
| samurai | white | 10 | 12 | 10 | 1 | weapon 1d8 · weapon 1d8 |  |
| tourist | white | 10 | 12 | 10 | 1 | weapon 1d6 · weapon 1d6 |  |
| valkyrie | white | 10 | 12 | 10 | 1 | weapon 1d8 · weapon 1d8 |  |
| wizard | white | 10 | 12 | 10 | 3 | weapon 1d6 · spell spell |  |
| Lord Carnarvon | magenta | 20 | 15 | 0 | 90 | weapon 4d10 · spell 4d8 spell | tunnels, starts peaceful. Archeologist quest leader. |
| Pelias | magenta | 20 | 15 | 0 | 90 | weapon 4d10 · weapon 4d10 | starts peaceful. |
| Shaman Karnov | magenta | 20 | 15 | 0 | 90 | weapon 4d10 · spell 2d8 cleric | starts peaceful. |
| Hippocrates | magenta | 20 | 15 | 0 | 90 | weapon 1d6 · spell 3d8 cleric · spell 3d8 cleric | starts peaceful. Healer quest leader. |
| King Arthur | magenta | 20 | 15 | 0 | 90 | weapon 4d10 · weapon 4d10 | starts peaceful. Knight quest leader. Holds Excalibur if you didn't get it. |
| Grand Master | black | 25 | 15 | 0 | 90 | claw 4d10 · kick 2d8 · spell 2d8 cleric · spell 2d8 cleric | sees-invis, starts peaceful. Monk quest leader. |
| Arch Priest | white | 25 | 15 | 7 | 90 | weapon 4d10 · kick 2d8 · spell 2d8 cleric · spell 2d8 cleric | sees-invis, starts peaceful. Priest quest leader. |
| Orion | magenta | 20 | 15 | 0 | 90 | weapon 4d10 · spell 4d8 spell | swims, amphibious, sees-invis, starts peaceful. Ranger quest leader. Bow user. |
| Master of Thieves | magenta | 20 | 15 | 0 | 90 | weapon 4d10 · weapon 2d6 · claw 2d4 steal-amulet | starts peaceful. Rogue quest leader; also Tourist quest nemesis. |
| Lord Sato | magenta | 20 | 15 | 0 | 90 | weapon 4d10 · weapon 4d10 | starts peaceful. |
| Twoflower | white | 20 | 15 | 10 | 90 | weapon 4d10 | starts peaceful. Tourist quest leader. |
| Norn | magenta | 20 | 15 | 0 | 90 | weapon 4d10 · weapon 4d10 | starts peaceful, cold-res. Valkyrie quest leader. |
| Neferet the Green | green | 20 | 15 | 0 | 90 | weapon 4d10 · spell 2d8 spell · spell 2d8 spell | starts peaceful. Wizard quest leader. |
| Thoth Amon | magenta | 16 | 12 | 0 | 10 | weapon 1d6 · spell spell · spell spell · claw 1d4 steal-amulet | follows stairs. |
| Master Kaen | magenta | 25 | 12 | -10 | 10 | claw 16d2 · claw 16d2 · spell cleric · claw 1d4 steal-amulet | sees-invis, follows stairs. |
| Master Assassin | magenta | 15 | 12 | 0 | 30 | weapon 2d6 poison · weapon 2d8 · claw 2d6 steal-amulet | follows stairs. Rogue quest nemesis. |
| Ashikaga Takauji | magenta | 15 | 12 | 0 | 40 | weapon 2d6 · weapon 2d6 · claw 2d6 steal-amulet | follows stairs. Samurai quest nemesis. |
| Dark One | black | 15 | 12 | 0 | 80 | weapon 1d6 · weapon 1d6 · claw 1d4 steal-amulet · spell spell | follows stairs. |
| student | white | 5 | 12 | 10 | 10 | weapon 1d6 | tunnels, starts peaceful. |
| chieftain | white | 5 | 12 | 10 | 10 | weapon 1d6 | starts peaceful. |
| neanderthal | white | 5 | 12 | 10 | 10 | weapon 2d4 | starts peaceful. |
| attendant | white | 5 | 12 | 10 | 10 | weapon 1d6 | starts peaceful. |
| page | white | 5 | 12 | 10 | 10 | weapon 1d6 · weapon 1d6 | starts peaceful. |
| abbot | white | 5 | 12 | 10 | 20 | claw 8d2 · kick 3d2 stun · spell cleric | starts peaceful. |
| acolyte | white | 5 | 12 | 10 | 20 | weapon 1d6 · spell cleric | starts peaceful. |
| hunter | white | 5 | 12 | 10 | 10 | weapon 1d4 | sees-invis, starts peaceful. |
| thug | white | 5 | 12 | 10 | 10 | weapon 1d6 · weapon 1d6 | starts peaceful. |
| ninja | white | 5 | 12 | 10 | 10 | weapon 1d8 · weapon 1d8 |  |
| roshi | white | 5 | 12 | 10 | 10 | weapon 1d8 · weapon 1d8 | starts peaceful. |
| guide | white | 5 | 12 | 10 | 20 | weapon 1d6 · spell spell | starts peaceful. |
| warrior | white | 5 | 12 | 10 | 10 | weapon 1d8 · weapon 1d8 | starts peaceful. |
| apprentice | white | 5 | 12 | 10 | 30 | weapon 1d6 · spell spell | starts peaceful. |

:::

<!-- audit
2026-05-19:
- Full demon roster stats/colors/attacks match monsters.h:2911-3194.
- Erinys DOES follow stairs (M2_STALK at monsters.h:2958); every row in this table carries M2_STALK.
- Amorous demon's displayed form is set by the demon's own randomly-assigned gender (Mgender(mon) at mhitu.c:1988-1989), NOT the player's.
- Balrog and amorous demon do NOT summon (mhitu.c:967).
- Bone devil, Orcus, Geryon stings are AD_DRST drain-Str, NOT AD_POISON (monsters.h:2999, 3082, 3093: ATTK(AT_STNG, AD_DRST, 2, 4)). Poison resistance does NOT protect.
- Riders (Death/Pestilence/Famine) at monsters.h:3144-3174 carry MS_RIDER and M3_DISPLACED-tier resistances; vanquish all three to ascend (end.c).
- Mail daemon AT_NONE, M1_FLY|M1_SWIM, freq G_NOGEN — never randomly generated, only spawned by mail delivery (monsters.h mail daemon row, mail.c).
-->
#### Major demons `&`
<!-- audit
2026-05-19:
- Bone devil, Orcus, Geryon "sting 2d4" and Baalzebub "bite 2d6" cells are AD_DRST drain-Str, NOT AD_POISON (monsters.h:2999, 3082, 3093, 3112).
- Poison-resistant players are NOT protected; Strength drops during combat.
-->

Major demons. Most can gate in reinforcements (a single barbed devil in your face can become five). Silver weapons and Demonbane do extra damage. Demon lords can be bribed with gold to leave.

They all follow you up and down stairs.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| water demon | blue | 8 | 12 | -4 | 30 | weapon 1d3 · claw 1d3 · bite 1d3 | swims, poisonous-corpse, demonic. |
| [amorous demon](#seduction) | gray | 6 | 12 | 0 | 70 | seduction (see Seduction) | flies, poisonous-corpse, demonic. Displays as succubus or incubus by the demon's own randomly-assigned gender. |
| horned devil | brown | 6 | 9 | -5 | 50 | weapon 1d4 · claw 1d4 · bite 2d3 · sting 1d3 | poisonous-corpse, demonic. |
| erinys | red | 7 | 12 | 2 | 30 | weapon 2d4 Str-drain | fire-res, pois-res. Variable attacks; can be amplified by alignment abuse. |
| barbed devil | red | 8 | 12 | 0 | 35 | claw 2d4 · claw 2d4 sticky · sting 3d4 | poisonous-corpse, demonic. |
| marilith | red | 7 | 12 | -6 | 80 | weapon 2d4 · weapon 2d4 · claw 2d4 · claw 2d4 · claw 2d4 · claw 2d4 | sees-invis, poisonous-corpse, demonic. |
| vrock | green | 8 | 12 | 0 | 50 | claw 1d4 · claw 1d4 · claw 1d8 · claw 1d8 · bite 1d6 | poisonous-corpse, demonic. |
| hezrou | green | 9 | 6 | -2 | 55 | claw 1d3 · claw 1d3 · bite 4d4 | poisonous-corpse, demonic. |
| bone devil | gray | 9 | 15 | -1 | 40 | weapon 3d4 · sting 2d4 drain-Str | poisonous-corpse, demonic. |
| ice devil | white | 11 | 6 | -4 | 55 | claw 1d4 · claw 1d4 · bite 2d4 · sting 3d4 cold · touch 1d1 slow | sees-invis, poisonous-corpse, demonic. |
| nalfeshnee | red | 11 | 9 | -1 | 65 | claw 1d4 · claw 1d4 · bite 2d4 · spell spell | poisonous-corpse, demonic. |
| pit fiend | red | 13 | 6 | -3 | 65 | weapon 4d2 · weapon 4d2 · hug 2d4 | sees-invis, poisonous-corpse, demonic. |
| sandestin | gray | 13 | 12 | 4 | 60 | weapon 2d6 · weapon 2d6 | shapeshifter, ston-res. |
| balrog | red | 16 | 5 | -2 | 75 | weapon 8d4 · weapon 4d6 | flies, sees-invis, poisonous-corpse, demonic. |
| Juiblex | bright-green | 50 | 3 | -7 | 65 | engulf 4d10 disease · spit 3d6 acid | flies, amphibious, amorphous, sees-invis, poisonous-corpse, demonic, fire-res, pois-res, acid-res, ston-res. |
| Yeenoghu | magenta | 56 | 18 | -5 | 80 | weapon 3d6 · weapon 2d8 confuse · claw 1d6 paralyse · spell 2d6 magic | flies, sees-invis, poisonous-corpse, demonic, fire-res, pois-res. |
| Orcus | magenta | 66 | 9 | -6 | 85 | weapon 3d6 · claw 3d4 · claw 3d4 · spell 8d6 spell · sting 2d4 drain-Str | flies, sees-invis, poisonous-corpse, demonic, fire-res, pois-res. |
| Geryon | magenta | 72 | 3 | -3 | 75 | claw 3d6 · claw 3d6 · sting 2d4 drain-Str | flies, sees-invis, poisonous-corpse, demonic, fire-res, pois-res. |
| Dispater | magenta | 78 | 15 | -2 | 80 | weapon 4d6 · spell 6d6 spell | flies, sees-invis, poisonous-corpse, demonic, fire-res, pois-res. |
| Baalzebub | magenta | 89 | 9 | -5 | 85 | bite 2d6 drain-Str · gaze 2d6 stun | flies, sees-invis, poisonous-corpse, demonic, fire-res, pois-res. |
| Asmodeus | magenta | 105 | 12 | -7 | 90 | claw 4d4 · spell 6d6 cold | flies, sees-invis, poisonous-corpse, demonic, fire-res, cold-res, pois-res. |
| Demogorgon | magenta | 106 | 15 | -8 | 95 | spell 8d6 spell · sting 1d4 drain-XL · claw 1d6 disease · claw 1d6 disease | flies, sees-invis, poisonous-corpse, demonic, fire-res, pois-res. |
| Death | hi_overlord | 30 | 12 | -5 | 100 | touch 8d8 death · touch 8d8 death | flies, regenerates, sees-invis, teleport-control. Rider of the Apocalypse. Vanquish three to ascend. |
| Pestilence | hi_overlord | 30 | 12 | -5 | 100 | touch 8d8 pestilence · touch 8d8 pestilence | flies, regenerates, sees-invis, teleport-control. Rider; spreads disease. |
| Famine | hi_overlord | 30 | 12 | -5 | 100 | touch 8d8 famine · touch 8d8 famine | flies, regenerates, sees-invis, teleport-control. Rider; drains nutrition to starvation. |
| mail daemon | bright-blue | 56 | 24 | 10 | 127 | — | flies, swims, sees-invis, poisonous-corpse, starts peaceful, fire-res, cold-res, sleep-res, shock-res, pois-res, ston-res. Delivers in-game mail. Don't attack one — they don't fight back. |
| djinni | yellow | 7 | 12 | 4 | 30 | weapon 2d8 | flies, poisonous-corpse, pois-res, ston-res. |
| Minion of Huhetotl | orange | 16 | 12 | -2 | 75 | weapon 8d4 · weapon 4d6 · spell spell · claw 2d6 steal-amulet | flies, sees-invis, poisonous-corpse, demonic. |
| Nalzok | orange | 16 | 12 | -2 | 85 | weapon 8d4 · weapon 4d6 · spell spell · claw 2d6 steal-amulet | flies, sees-invis, poisonous-corpse, demonic. |

:::

#### Golems `'`
<!-- audit
2026-05-19:
- 11 golem rows at monsters.h:2509-2594 (straw 2509, paper, rope, gold, leather, wood, flesh, clay, stone, glass, iron 2587).
- Iron golem has G_NOCORPSE (monsters.h:2587); it leaves NO corpse, NOT a poisonous one.
- poly_when_stoned (mondata.c:80-85) covers ALL golems except stone golem.
- Iron golem AT_BREA/AD_DRST 4d6 poison breath at monsters.h:2592 — poison resistance critical.
- Clay golem inscription "ATHEIST" wears off via shatter_floor message; clay golem corpse grants nothing on eat.
-->

Mindless constructs. Wood and leather golems are early-game fodder; iron, stone, and clay golems are dangerous. The rare gold golem is a walking treasure pile.

All golems are mindless, sleep-resistant, and poison-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| straw golem | yellow | 3 | 12 | 10 | 0 | claw 1d2 · claw 1d2 | cold-res. |
| paper golem | white | 3 | 12 | 10 | 0 | claw 1d3 | cold-res. |
| rope golem | brown | 4 | 9 | 8 | 0 | claw 1d4 · claw 1d4 · hug 6d1 |  |
| gold golem | yellow | 5 | 9 | 6 | 0 | claw 2d3 · claw 2d3 | acid-res. |
| leather golem | brown | 6 | 6 | 6 | 0 | claw 1d6 · claw 1d6 |  |
| wood golem | brown | 7 | 3 | 4 | 0 | claw 3d4 | cold-res. |
| flesh golem | red | 9 | 8 | 9 | 30 | claw 2d8 · claw 2d8 | fire-res, cold-res, shock-res. |
| clay golem | brown | 11 | 7 | 7 | 40 | claw 3d10 |  |
| stone golem | gray | 14 | 6 | 5 | 50 | claw 3d8 | ston-res. |
| glass golem | cyan | 16 | 6 | 1 | 50 | claw 2d8 · claw 2d8 | acid-res. |
| iron golem | cyan | 18 | 6 | 3 | 60 | weapon 4d10 · breath 4d6 poison | no corpse. fire-res, cold-res, shock-res. |

:::

<!-- audit
2026-05-19:
- All 6 sea-creature rows match monsters.h:3205-3256, carry M1_SWIM | M1_AMPHIBIOUS.
- AD_WRAP grab-and-drown applies only to giant eel, electric eel, and kraken (AT_TUCH/AT_HUGS+AD_WRAP at monsters.h:3230-3256), NOT all 6 rows. Jellyfish/piranha/shark just bite or sting.
- Jellyfish sting 3d3 is AD_DRST drain-Str (uhitm.c:3149, 3157), NOT plain poison.
- AD_WRAP grab-and-drown mechanic at uhitm.c:3378-3401.
-->
#### Sea monsters `;`

Live in water. Eels and the kraken wrap you and drag you under to drown: instadeath without magical breathing. Stay off the water-adjacent square unless you have it.

All sea monsters swim and are amphibious.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| jellyfish | blue | 3 | 3 | 6 | 0 | sting 3d3 drain-Str | poisonous-corpse, pois-res. |
| piranha | red | 5 | 18 | 4 | 0 | bite 2d6 · bite 2d6 |  |
| shark | gray | 7 | 12 | 2 | 0 | bite 5d6 |  |
| giant eel | cyan | 5 | 9 | -1 | 0 | bite 3d6 · touch wrap |  |
| electric eel | bright-blue | 7 | 10 | -3 | 0 | bite 4d6 shock · touch wrap | shock-res. |
| kraken | red | 20 | 3 | 6 | 0 | claw 2d4 · claw 2d4 · hug 2d6 wrap · bite 5d4 |  |

:::

#### Lizards `:`
<!-- audit
2026-05-19:
- 8 lizard rows at monsters.h:3260-3324 (newt 3260, gecko, iguana, baby croc, lizard, chameleon, croc, salamander 3317).
- Lizard corpse cures stoning (eat.c:827-830, fix_petrification) and never rots (eat.c:1483, 1510).
- Newt corpse occasionally restores 1-3 Pw via eye_of_newt_buzz (eat.c:1102-1123).
- Chameleon is M2_SHAPESHIFTER (monsters.h:3299, sets shifter via newcham).
- Salamander has 4-attack chain at monsters.h:3317-3324: weapon 2d8, touch 1d6 fire, hug 2d6, hug 3d6 fire.
- Salamander is G_HELL (Gehennom-only spawn flag).
-->


Mostly harmless. **Lizard corpses cure petrification and never rot.** Carry one at all times — this is the standard answer to cockatrices and Medusa.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| newt | yellow | 0 | 6 | 8 | 0 | bite 1d2 | swims, amphibious. |
| gecko | green | 1 | 6 | 8 | 0 | bite 1d3 |  |
| iguana | brown | 2 | 6 | 7 | 0 | bite 1d4 |  |
| baby crocodile | brown | 3 | 6 | 7 | 0 | bite 1d4 | swims, amphibious. |
| lizard | green | 5 | 6 | 6 | 10 | bite 1d6 | ston-res. |
| chameleon | brown | 6 | 5 | 6 | 10 | bite 4d2 | shapeshifter. |
| crocodile | brown | 6 | 9 | 5 | 0 | bite 4d2 · claw 1d12 | swims, amphibious. |
| salamander | orange | 8 | 12 | -1 | 0 | weapon 2d8 · touch 1d6 fire · hug 2d6 · hug 3d6 fire | poisonous-corpse, follows stairs, fire-res, sleep-res. |

:::

---

### What Changed Since Last Time
<!-- audit
2026-05-19:
- chain lightning is level 4 NODIR (objects.h:1409-1411 SPELL("chain lightning",..., P_ATTACK_SPELL, 25, 4, 2, 1, NODIR))
- "mummy withering" was fabricated; no such mechanic in 5.0
- Elbereth -5 alignment penalty is NOT a 5.0 change (engrave.c writeable_engrave, predates 5.0)
- supply chests appear strictly above the Oracle (mklev.c:1037 `u.uz.dlevel < oracle_level.dlevel`), not "the first ten levels"
- mind flayer: spell loss (uhitm.c:3266 losespells) and skill drain (uhitm.c:3270 drain_weapon_skill) persist; map/ID amnesia is gone (no forget_map call in eat_brains, eat.c:603)
- sink dipping is for potions only: non-potions just take water_damage (fountain.c:716-733)
- touch of death is still binary: !Antimagic && rn2(m_lev) > 12 kills; Antimagic shows shieldeff and "Lucky for you, it didn't work!" (mcastu.c:391-407)
- the 5.0 change is the unprotected outcome (instakill -> drain + damage) per fixes5-0-0.txt:538
- iron bars were added in 3.3.0, not 3.6 (fixes3-3-0.txt:349)
- gold dragon scale mail grants only hallucination resistance + innate light, not two resistances (do_wear.c:846-851, objects.h:505 DRGN_ARMR slot 0)
- bag-of-holding explosion scatters contents via scatter() rather than destroying them all; only 1/13 items vanish per is_boh_item_gone (pickup.c:2509-2532)
- death drops delobj() any rolled FOOD_CLASS item unless the monster has M2_COLLECT — corpses are still left (mon.c:3597-3604)
-->

If you're an experienced traveler returning after some time away, the
5.0 of the Mazes (NetHack 5.0.0, released May 2, 2026) includes
several notable changes from 3.6.x, the last widely-played version before
this one. (NetHack 3.7 was a long-running development branch and never
shipped as a numbered public release; 3.6.x is the natural comparison
point.) The most significant:

- **Themed rooms** are now a regular feature of dungeon generation.
  You'll encounter rooms with specific monster or item themes that
  didn't exist before.
- **Four new monster species**: the displacer beast, genetic
  engineer, gold dragon, and baby gold dragon now roam the Mazes.
- **The helm of caution** is a new piece of armor that grants
  warning. The helm of brilliance now always appears as a
  "crystal helmet" rather than a randomized appearance.
- **Chain lightning** is a new level 2 attack spell. Shock damage
  spreads from the caster in all directions and chains from one
  monster to the next, so it scales with the density of the room
  rather than the caster's aim.
- **Spellbooks** can be `a`pplied to check how worn they are.
- **Mind flayers** no longer wipe your map or identifications (the
  old "amnesia" effect on tentacle hit). They still drain
  Intelligence and have a separate chance to forget memorized
  spells and weapon-skill experience.
- **Unicorn horns** no longer restore lost attributes. This is a
  major change. In previous editions, the unicorn horn was a
  cure-all; now you'll need other solutions.
- **Dragon scale mail** now provides two extrinsic resistances
  instead of one. This makes it even more desirable.
- **Bags of holding** no longer destroy their contents on explosion.
  Items are scattered on the floor instead, which is bad but not
  catastrophic.
- **Loadstones** now resist knockback from combat attacks (the new
  knockback mechanic). A niche use if you can keep one uncursed.
- **Sacrifice** for artifact generation now requires a minimum
  sacrifice value.
- **Priest donations** are now randomized. The old fixed
  `400 × XL` formula is gone. The priest rolls a baseline between
  150 and 250 (×XL), and offering the worst-case ceiling of
  `500 × XL` guarantees protection. Offering too little when you
  could afford more sets a "Cheapskate" flag on that priest that
  permanently inflates future baselines.
- **Artifact effects** have been broadened. Several previously
  flavour-only artifacts now have real tactical edges. The most
  notable: **Snickersnee** now grants one free polearm-style reach
  attack per turn ("Shkinng!") on top of normal melee. **Sunsword**
  gains a `#invoke` blinding ray that works on any monster, not just
  undead — a 5-Pw on-demand Camera flash. **Trollsbane** regenerates
  while wielded, a real lifeline for an early character. **Amulet of
  flying** confers flight on your steed as well as you, turning
  warhorses into water-crossing cavalry.
- **Gehennom** levels are more varied and interesting.
- **Medusa's Island** now has four possible layouts.
- **Special levels** can now generate mirrored (flipped), so don't
  rely on fixed maps.
- **New conducts** are tracked: pauper, petless, permadeaf, and
  Sokoban (no cheating).
- **Touch of death** has been reworked: instead of an instant
  kill, an unresisted hit now deals heavy damage and drains max
  HP. Magic resistance still fully blocks the spell.
- **Black dragon scale mail** now grants drain resistance in
  addition to disintegration resistance: a second extrinsic that
  was historically hard to find outside artifacts.
- **Green dragon scale mail** now grants sickness immunity.
- **New wish sources**: Vlad's throne is guaranteed, and the
  Amulet of Yendor grants a wish on pickup. Either a magic lamp
  or magic marker is guaranteed in Orcus Town.
- **Charm monster** is now level 5 (was 3). **Sleep** is now
  level 3 (was 1). **Confuse monster** is now level 1 (was 2).
- **Cursed wands** may explode when used to engrave.
- **Monsters** can now use containers and unlock chests.
- **Valkyries** no longer start with a long sword. They start with
  a spear, making the Excalibur strategy less immediate.
- **Excalibur** fountain dipping is much harder for non-Knights:
  1/30 chance per dip instead of the Knight's 1/6.
- **New amulets**: the amulet of flying grants flight, and the
  amulet of guarding provides +2 AC and +2 MC.
- **Minetown** has a 1/7 chance of generating as Orcish Town,
  with no shops and no priest.
- **Blessed potions of polymorph** now grant controlled polymorph,
  eliminating the need for polymorph control when using blessed
  potions.
- **Gehennom** has hot ground that can shatter dropped potions.
  Teleportation is now blocked only while a demon lord is present,
  not permanently.
- **Wand of speed monster** no longer grants permanent speed when
  self-zapped; use potions of speed instead.
- **Supply chests** now appear on the dungeon levels above the
  Oracle (about a 2-in-3 chance per level, placed in one random
  ordinary room), containing useful early-game items like healing
  potions and enchant scrolls.
- **Pets** can gain resistances from eating corpses, and dead pets
  can be revived by praying at a co-aligned altar while standing
  on their corpse.
- **Sink dipping (potions)** is new: pour potions down a sink and
  the message identifies the potion type without consuming a scroll.
- **Demonbane** is now a silver mace (was a long sword) and is the
  guaranteed first sacrifice gift for Priests.
- **Two-handed weapons** get a 50% increase to the strength damage
  bonus, making them more competitive with dual-wielding.
- **HP regeneration** uses a new formula: (experience level +
  Constitution)% chance per turn. The regeneration intrinsic now
  heals 1 HP unconditionally every turn on top of natural regen.
- **Covetous monsters** (demon lords, liches) now warp to either
  upstairs or downstairs when fleeing to heal, not always upstairs.
- **Alchemy** is nerfed: diluted potion stacks only alchemize 2
  potions instead of the whole stack. Wearing an alchemy smock
  reduces the random blast chance to 1/30.
- **Glass items** (crystal ball, crystal plate mail) now crack in
  stages instead of instantly shattering, and can be made
  crackproof.
- **Candle light radius** now uses a square root formula: more
  candles in a stack give more light than before.
- **The Castle** no longer generates master liches or arch-liches
  at level creation, making it significantly less dangerous on
  arrival.
- **Corpses, tins, and eggs** from intrinsic-granting monsters
  now have higher shop prices, making price identification of tins
  and eggs possible.
- **Monsters** no longer drop food items as death drops (except
  their own corpse), reducing food availability in the early game.
- **Shopkeepers** can now remove pits and webs around them, nerfing
  the classic pit-pinning kill setup. Walking into a peaceful
  shopkeeper now auto-pays any debts before the inventory prompt.

---

#### New Dangers

**Sacrificing weak corpses no longer grinds Luck.** If your current
Luck exceeds the sacrificed monster's difficulty, you gain zero.
A luckstone handles maintenance; sacrifice mid-tier monsters when
you want to push higher.

**Cleared but not cleaned levels lose loot.** Monsters now loot
unlocked containers and animate corpse piles. Lock your stash
and don't haul speculative corpses through caster-heavy floors.

**Gehennom shatters potions.** Hot ground breaks any potion you
drop. Carry, don't stash.

#### New Hacks

A few 5.0 changes have tactical implications worth pulling out:

**Gold dragon scale mail is a light source.** Its innate 2-square
radius lets you skip the lamp and free that inventory slot.

**A blessed potion of polymorph is now a self-contained controlled
polymorph.** No ring of polymorph control required: blessing the
potion grants control for that one transformation. Single-use
polymorph strategies (iron golem form for extreme AC, bat form to
scout, pick something with a good intrinsic) are now accessible
without needing to find or wish for the ring first. The ring is
still useful for ongoing polymorphing, but for a single planned
transformation, one blessed potion does the same job.

**Vampire polymorph cycles between forms.** A polymorphed vampire
can `#monster` to switch between vampire, bat, and fog cloud. Fog
passes through doors, bat flies, vampire fights — plan routes by
form rather than direction, so traversing the dungeon map can be
a very different experience.

::: print-only

## Index of Useful Knowledge

```{=latex}
\begin{multicols}{2}
\footnotesize\raggedright\setlength{\parskip}{0.15em plus 0.05em}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000\exhyphenpenalty=10000

\par\smallskip{\normalsize\bfseries 0--9}\par\smallskip

\hyperref[golems]{`'` golems, p.~\pageref*{golems}}\par
\hyperref[use-testing-the-careful-way]{\$200 potions, the hidden traps, p.~\pageref*{use-testing-the-careful-way}}\par
\hyperref[armor-prices]{\$30 boots, the warning, p.~\pageref*{armor-prices}}\par
\hyperref[wand-prices]{\$500 wand, very good day, p.~\pageref*{wand-prices}}\par
\hyperref[major-demons]{`\&` major demons, p.~\pageref*{major-demons}}\par
5.0: \hyperref[what-changed-since-last-time]{new features, items, and mechanics, p.~\pageref*{what-changed-since-last-time}}; \hyperref[new-dangers]{new dangers and new hacks, p.~\pageref*{new-dangers}}\par
\hyperref[carrying-capacity]{52 inventory slots, the letter limit, p.~\pageref*{carrying-capacity}}\par
\hyperref[lizards]{`:` lizards, p.~\pageref*{lizards}}\par
\hyperref[sea-monsters]{`;` sea monsters, p.~\pageref*{sea-monsters}}\par
\hyperref[humans-and-elves]{`@` humans and elves (monster class), p.~\pageref*{humans-and-elves}}\par
\hyperref[a-note-on-mimics]{`]` strange object, always a mimic, p.~\pageref*{a-note-on-mimics}}\par
\hyperref[special-symbols]{`\textasciitilde{}` long worm tail, p.~\pageref*{special-symbols}}\par

\par\smallskip{\normalsize\bfseries A}\par\smallskip

\hyperref[angelic-beings-a]{`A` angelic beings, p.~\pageref*{angelic-beings-a}}\par
\hyperref[ants-and-insects-a]{`a` ants and insects, p.~\pageref*{ants-and-insects-a}}\par
AC: \hyperref[ac-and-defense]{the AC ladder to -20, special attacks ignore, p.~\pageref*{ac-and-defense}}\par
Acid: \hyperref[petrification-stoning]{blob corpse, timed stoning resistance, p.~\pageref*{petrification-stoning}}; \hyperref[vegetarian-safe-corpses]{blob corpse, stoning resistance (timed), p.~\pageref*{vegetarian-safe-corpses}}\par
\hyperref[engravings]{Ad aerarium engraving, vault closet marker, p.~\pageref*{engravings}}\par
\hyperref[carrying-capacity]{\#adjust, swap and merge letters, p.~\pageref*{carrying-capacity}}\par
Air: \hyperref[vortices-v]{fire, ice, steam, energy, dust vortex, p.~\pageref*{vortices-v}}; \hyperref[elementals-e]{elemental, engulfs and suffocates, p.~\pageref*{elementals-e}}\par
Alchemy: \hyperref[alchemy]{dip recipes, chain, healing → extra → full → gain ability, smock, blast chance \textasciitilde{}1 in 30, p.~\pageref*{alchemy}}; \hyperref[cloaks]{smock, poison resistance, p.~\pageref*{cloaks}}\par
Alignment: \hyperref[alignment]{it's a number, p.~\pageref*{alignment}}; \hyperref[alignment-and-blasting]{and blasting, misaligned artifact damage, p.~\pageref*{alignment-and-blasting}}\par
Altar: \hyperref[altars-_]{BUC test at, dropping the whole pile, converting a cross-aligned, p.~\pageref*{altars-_}}; \hyperref[altars-and-alignment]{conversion, the inversion trap, p.~\pageref*{altars-and-alignment}}\par
Altars: \hyperref[altars-_]{single most useful furniture, p.~\pageref*{altars-_}}; \hyperref[altars-and-alignment]{converting cross-aligned, p.~\pageref*{altars-and-alignment}}\par
\hyperref[seduction]{Amorous demon, expensive evening with, p.~\pageref*{seduction}}\par
Amulet: \hyperref[choking]{of strangulation, timer death, p.~\pageref*{choking}}; \hyperref[delayed-deaths]{of unchanging, blocks slime, p.~\pageref*{delayed-deaths}}; \hyperref[amulet-prices]{prices, all \$150, p.~\pageref*{amulet-prices}}; \hyperref[amulets]{of life saving, when to wear, of life saving, revives once, of reflection, ray bouncing, of magical breathing, underwater, of ESP (telepathy), of unchanging, blocks polymorph, of flying, mount flies too (new in 5.0), of guarding, +2 AC +2 MC (new in 5.0), of strangulation, 90\% cursed, of restful sleep, the rebrand, p.~\pageref*{amulets}}; \hyperref[the-gauntlet]{blocks teleportation, climb by foot, p.~\pageref*{the-gauntlet}}\par
Amulet of Yendor: \hyperref[molochs-sanctum]{the prize, p.~\pageref*{molochs-sanctum}}; \hyperref[the-ascension-run]{retrieving, pickup wish, on next turn, p.~\pageref*{the-ascension-run}}; \hyperref[the-elemental-planes]{the compass, p.~\pageref*{the-elemental-planes}}\par
\hyperref[angelic-beings-a]{Angel, on the Astral Plane, p.~\pageref*{angelic-beings-a}}\par
\hyperref[the-price-is-right]{Angry-shopkeeper +33\% surcharge, permanent, p.~\pageref*{the-price-is-right}}\par
\hyperref[dungeon-overview-and-event-journal]{Annotate (`\#annotate`), labeling stash floors, p.~\pageref*{dungeon-overview-and-event-journal}}\par
\hyperref[dangerous-traps]{Anti-magic field, hits harder with MR, p.~\pageref*{dangerous-traps}}\par
\hyperref[common-combat-deaths]{Ants, pack travelers, p.~\pageref*{common-combat-deaths}}\par
\hyperref[liches-l]{Arch-lich, touch of death, p.~\pageref*{liches-l}}\par
Archeologist: \hyperref[the-roles]{touchstone advantage, pickaxe from turn one, p.~\pageref*{the-roles}}\par
\hyperref[angelic-beings-a]{Archon, ultimate pet, p.~\pageref*{angelic-beings-a}}\par
Armor: \hyperref[the-early-shopping-list]{improvements, even basic, p.~\pageref*{the-early-shopping-list}}; \hyperref[use-testing-the-careful-way]{randomized appearances, pools, helms cloaks gloves boots, p.~\pageref*{use-testing-the-careful-way}}; \hyperref[armor-prices]{prices, the danger zones, p.~\pageref*{armor-prices}}\par
\hyperref[nuisance-traps]{Arrow trap, free ammunition farm, p.~\pageref*{nuisance-traps}}\par
Ascension: \hyperref[the-ascension-run]{how to not die during, p.~\pageref*{the-ascension-run}}; \hyperref[what-killed-the-runners-up]{three things winners do that runners-up don't, p.~\pageref*{what-killed-the-runners-up}}; \hyperref[strategy]{Run strategy, run don't fight, p.~\pageref*{strategy}}\par
\hyperref[the-demon-prince-lairs]{Asmodeus, bribable cold caster, p.~\pageref*{the-demon-prince-lairs}}\par
Astral: \hyperref[the-astral-plane]{Plane, three altars, choose wrong altar = game ends, farlook reveals altar only when adjacent, p.~\pageref*{the-astral-plane}}\par
\hyperref[engravings]{Athame, the non-dulling stylus, p.~\pageref*{engravings}}\par
Atheist: \hyperref[atheist]{conduct, ascension Amulet offering is exempt, p.~\pageref*{atheist}}\par
\hyperref[the-seven-spell-schools]{Attack school, force bolt grind, p.~\pageref*{the-seven-spell-schools}}\par
\hyperref[the-ascension-run]{Authentic Amulet, only from the High Priest, p.~\pageref*{the-ascension-run}}\par
Auto-curse: \hyperref[blessed-uncursed-cursed-buc]{items, read as uncursed (trap), p.~\pageref*{blessed-uncursed-cursed-buc}}; \hyperref[the-ring-table]{rings (teleport, polymorph, aggravate, hunger), p.~\pageref*{the-ring-table}}\par
\hyperref[options-worth-knowing-about]{Autopickup and pickup\_types, p.~\pageref*{options-worth-knowing-about}}\par

\par\smallskip{\normalsize\bfseries B}\par\smallskip

\hyperref[bats-and-birds-b]{`B` bats and birds, p.~\pageref*{bats-and-birds-b}}\par
\hyperref[blobs-b]{`b` blobs, p.~\pageref*{blobs-b}}\par
\hyperref[the-demon-prince-lairs]{Baalzebub, beetle-shaped lair, p.~\pageref*{the-demon-prince-lairs}}\par
\hyperref[dragons-d]{Baby dragon, doesn't breathe, p.~\pageref*{dragons-d}}\par
Bag of holding: \hyperref[containers]{the turning point, never insert wand of cancellation, p.~\pageref*{containers}}\par
\hyperref[containers]{Bag of tricks, not actually a bag, p.~\pageref*{containers}}\par
\hyperref[major-demons]{Balrog, slow but heavy, p.~\pageref*{major-demons}}\par
\hyperref[wishable-random-artifacts]{Bane weapons, defensive riders, p.~\pageref*{wishable-random-artifacts}}\par
Barbarian: \hyperref[the-roles]{just hit things harder, poison resistance gift, p.~\pageref*{the-roles}}\par
\hyperref[room-types]{Barracks, organized armed soldiers, p.~\pageref*{room-types}}\par
\hyperref[common-combat-deaths]{Bats and speedsters, doorway fighting, p.~\pageref*{common-combat-deaths}}\par
\hyperref[weapons]{Battle-axe, two-handed good damage, p.~\pageref*{weapons}}\par
\hyperref[dangerous-traps]{Bear trap, escape diagonally, p.~\pageref*{dangerous-traps}}\par
\hyperref[room-types]{Beehive, royal jelly inside, p.~\pageref*{room-types}}\par
Bell of Opening: \hyperref[the-quest]{looted from nemesis, p.~\pageref*{the-quest}}; \hyperref[other-notable-tools]{Invocation item, p.~\pageref*{other-notable-tools}}\par
\hyperref[a-note-on-dragons]{Black dragon scale mail, disintegration + drain res, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[nagas-n]{Black naga corpse, three resistances, p.~\pageref*{nagas-n}}\par
Black pudding: \hyperref[the-golden-rules-of-early-survival]{glob, resistances from a sink, p.~\pageref*{the-golden-rules-of-early-survival}}; \hyperref[a-note-on-puddings]{do not split with iron, p.~\pageref*{a-note-on-puddings}}\par
Blessed: \hyperref[potion-polymorph]{potion of polymorph, controlled poly (new in 5.0), p.~\pageref*{potion-polymorph}}; \hyperref[scroll-genocide]{genocide, class L wipe, p.~\pageref*{scroll-genocide}}; \hyperref[learning-spells]{spellbook, auto-success, p.~\pageref*{learning-spells}}\par
\hyperref[combining-conducts]{Blind / Zen conduct, p.~\pageref*{combining-conducts}}\par
\hyperref[other-notable-tools]{Blindfold, voluntary blindness, p.~\pageref*{other-notable-tools}}\par
\hyperref[a-note-on-dragons]{Blue dragon scale mail, shock + speed, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[jellies-j]{Blue jelly corpse, cold + poison resistance, p.~\pageref*{jellies-j}}\par
\hyperref[containers]{BoH, ascension carry, p.~\pageref*{containers}}\par
\hyperref[deadly-mistakes]{Boiling and shattering potions, Gehennom hot ground, p.~\pageref*{deadly-mistakes}}\par
Bones: \hyperref[things-that-will-kill-you]{level, 80\% cursed items, level, over-leveled monsters, p.~\pageref*{things-that-will-kill-you}}\par
\hyperref[shopkeeper-behavior]{Bones-shop gotcha, items still belong, p.~\pageref*{shopkeeper-behavior}}\par
\hyperref[the-wizards-tower]{Book of the Dead, at the Tower bottom, p.~\pageref*{the-wizards-tower}}\par
\hyperref[brainlessness]{Brainlessness, mind flayer drain, p.~\pageref*{brainlessness}}\par
Branch: \hyperref[the-map-symbols]{staircases, turn yellow, p.~\pageref*{the-map-symbols}}; \hyperref[branches-and-landmarks]{order, Sokoban or Mines first, p.~\pageref*{branches-and-landmarks}}\par
\hyperref[gaining-and-losing-luck]{Breaking a mirror, –2 Luck, p.~\pageref*{gaining-and-losing-luck}}\par
\hyperref[whats-different-in-gehennom]{Bribe demand, halved for Lawful visitors, p.~\pageref*{whats-different-in-gehennom}}\par
\hyperref[fungi-and-molds-f]{Brown mold, passive cold, p.~\pageref*{fungi-and-molds-f}}\par
\hyperref[a-note-on-puddings]{Brown pudding, vegetarian-safe glob, p.~\pageref*{a-note-on-puddings}}\par
BUC: \hyperref[blessed-uncursed-cursed-buc]{avoiding curses by checking, the altar amber/black flash, pet step-around, p.~\pageref*{blessed-uncursed-cursed-buc}}\par
\hyperref[feelings-and-sounds]{Bugle reveille, soldier woke neighbors, p.~\pageref*{feelings-and-sounds}}\par
Burdened: \hyperref[the-early-shopping-list]{status, two hits per yours, p.~\pageref*{the-early-shopping-list}}; \hyperref[carrying-capacity]{Stressed, Strained, Overtaxed, Overloaded, p.~\pageref*{carrying-capacity}}\par
\hyperref[room-types]{Buried treasure room, dig for it, p.~\pageref*{room-types}}\par

\par\smallskip{\normalsize\bfseries C}\par\smallskip

\hyperref[centaurs-c]{`C` centaurs, p.~\pageref*{centaurs-c}}\par
\hyperref[cockatrices-c]{`c` cockatrices, p.~\pageref*{cockatrices-c}}\par
\hyperref[other-notable-tools]{Can of grease, slip and waterproofing, p.~\pageref*{other-notable-tools}}\par
Candelabrum of Invocation: \hyperref[light-sources]{requires seven candles, p.~\pageref*{light-sources}}; \hyperref[vlads-tower]{at top of Vlad's Tower, p.~\pageref*{vlads-tower}}\par
\hyperref[dangerous-foods]{Cannibalism, –2 to –5 Luck plus aggravate, p.~\pageref*{dangerous-foods}}\par
\hyperref[strategy]{Carrying Amulet, casts cost more (drop to cast), p.~\pageref*{strategy}}\par
Castle: \hyperref[castle-overview]{gateway to Gehennom, p.~\pageref*{castle-overview}}; \hyperref[the-castle]{storming the, wand chest, sit on cursed scare monster, five trap doors in the hall, two reliable wishes, p.~\pageref*{the-castle}}\par
Cave: \hyperref[the-roles]{Dweller, sling and flint, p.~\pageref*{the-roles}}; \hyperref[arachnids-and-centipedes-s]{spider, eat for poison resistance, p.~\pageref*{arachnids-and-centipedes-s}}\par
\hyperref[key-spells]{Chain lightning, 5.0 room-clearer, p.~\pageref*{key-spells}}\par
\hyperref[lizards]{Chameleon corpse, polymorphs you, p.~\pageref*{lizards}}\par
\hyperref[alignment]{Chaotic, paired with Rogue for theme, p.~\pageref*{alignment}}\par
Charging: \hyperref[scroll-charging]{explosion chance (n³/7³), a wand of wishing, exactly once, p.~\pageref*{scroll-charging}}\par
\hyperref[the-price-is-right]{Charisma, buy-price bands, p.~\pageref*{the-price-is-right}}\par
\hyperref[key-spells]{Charm monster, 3×3 tame, p.~\pageref*{key-spells}}\par
\hyperref[humans-and-elves]{Charon, ferryman, p.~\pageref*{humans-and-elves}}\par
\hyperref[the-price-is-right]{Chat to shopkeeper, polite price-ID, p.~\pageref*{the-price-is-right}}\par
\hyperref[choking]{Choking, eating past Satiated, p.~\pageref*{choking}}\par
\hyperref[dragons-d]{Chromatic Dragon, random breath weapons, p.~\pageref*{dragons-d}}\par
\hyperref[dungeon-overview-and-event-journal]{Chronicle (`v` / \#chronicle), the journal, p.~\pageref*{dungeon-overview-and-event-journal}}\par
\hyperref[feelings-and-sounds]{Chugging sound, monster drank a potion, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[donating-to-priests]{Clairvoyance, lower-tier priest gift, p.~\pageref*{donating-to-priests}}\par
\hyperref[golems]{Clay golem, dissolves to cancellation, p.~\pageref*{golems}}\par
\hyperref[wishable-random-artifacts]{Cleaver (Barbarian), three-monster swing, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[armor-and-ac]{Cloak of displacement, the underrated layer, p.~\pageref*{armor-and-ac}}\par
Cloak of magic resistance: \hyperref[armor-and-ac]{MC1 in 5.0, p.~\pageref*{armor-and-ac}}; \hyperref[cloaks]{MC1, p.~\pageref*{cloaks}}\par
Cloak of protection: \hyperref[armor-and-ac]{MC3 the only single source, p.~\pageref*{armor-and-ac}}; \hyperref[cloaks]{MC3, p.~\pageref*{cloaks}}\par
\hyperref[shopkeeper-behavior]{Closed for inventory, locked shop door, p.~\pageref*{shopkeeper-behavior}}\par
Cockatrice: \hyperref[dungeon-hazards-and-how-to-survive-them]{corpse on the stairs, the most literal instadeath, p.~\pageref*{dungeon-hazards-and-how-to-survive-them}}; \hyperref[cockatrices-c]{instant petrification on touch, p.~\pageref*{cockatrices-c}}; \hyperref[petrification-stoning]{corpse, wielding (with gloves!), corpse, the rubber chicken, new moon hiss (1 in 3), p.~\pageref*{petrification-stoning}}; \hyperref[the-astral-plane]{corpse, one-shot Rider, p.~\pageref*{the-astral-plane}}\par
\hyperref[the-art-of-combat]{Combat, knowing when not to fight, p.~\pageref*{the-art-of-combat}}\par
\hyperref[command-counts]{Command counts (10s, 20., etc.), p.~\pageref*{command-counts}}\par
Conflict: \hyperref[fighting-smart]{sight required, Charisma scales reliability, p.~\pageref*{fighting-smart}}; \hyperref[the-astral-plane]{ring on Astral, Angels go hostile if your Angel dies, p.~\pageref*{the-astral-plane}}\par
Confused: \hyperref[searching-and-detection]{gold detection, cheap trap reveal, p.~\pageref*{searching-and-detection}}; \hyperref[deadly-mistakes]{genocide, self-extinction, p.~\pageref*{deadly-mistakes}}; \hyperref[genocide]{genocide, kills you, p.~\pageref*{genocide}}; \hyperref[taming-new-creatures]{taming, 11×11 area, p.~\pageref*{taming-new-creatures}}; \hyperref[use-testing-the-careful-way]{reading, alternate effects, p.~\pageref*{use-testing-the-careful-way}}; \hyperref[confused-reading]{enchant weapon/armor, erodeproofs, remove curse, randomizes BUC, gold detection, traps revealed, charging, raises max Pw, p.~\pageref*{confused-reading}}\par
\hyperref[fighting-smart]{Cornered scared monsters still fight, p.~\pageref*{fighting-smart}}\par
\hyperref[helmets]{Cornuthaum, Wizard's clairvoyance, p.~\pageref*{helmets}}\par
\hyperref[the-golden-rules-of-early-survival]{Corridor chokepoint, single-file enemies, p.~\pageref*{the-golden-rules-of-early-survival}}\par
\hyperref[angelic-beings-a]{Couatl, feathered serpent, p.~\pageref*{angelic-beings-a}}\par
\hyperref[the-gauntlet]{Covetous monsters, warp to you, p.~\pageref*{the-gauntlet}}\par
\hyperref[feelings-and-sounds]{Crashing rock, a tunneler at work, p.~\pageref*{feelings-and-sounds}}\par
Credit: \hyperref[unlocking-tools]{card, worst but works, p.~\pageref*{unlocking-tools}}; \hyperref[credit-and-debt]{two ways to accumulate, cloning, the gold-lure routine, p.~\pageref*{credit-and-debt}}\par
\hyperref[humans-and-elves]{Croesus, vault guardian, p.~\pageref*{humans-and-elves}}\par
Crowning: \hyperref[crowning]{alignment 20 and Luck 10, prayer-cooldown penalty, p.~\pageref*{crowning}}\par
\hyperref[weapons]{Crysknife, fragile excellence, p.~\pageref*{weapons}}\par
Crystal ball: \hyperref[searching-and-detection]{trap survey, p.~\pageref*{searching-and-detection}}; \hyperref[other-notable-tools]{the one-question oracle, p.~\pageref*{other-notable-tools}}\par
\hyperref[repeat-last-command-ctrla]{Ctrl+A, repeat last command, p.~\pageref*{repeat-last-command-ctrla}}\par
\hyperref[dungeon-overview-and-event-journal]{Ctrl+O / \#overview, the level list, p.~\pageref*{dungeon-overview-and-event-journal}}\par
\hyperref[message-history-and-redraw]{Ctrl+P, message history, p.~\pageref*{message-history-and-redraw}}\par
\hyperref[message-history-and-redraw]{Ctrl+R, redraw, p.~\pageref*{message-history-and-redraw}}\par
\hyperref[removing-curses]{Curse, removing, p.~\pageref*{removing-curses}}\par
Cursed: \hyperref[sokoban]{scare monster scroll, Sokoban-prize bait, p.~\pageref*{sokoban}}; \hyperref[blessed-uncursed-cursed-buc]{gain level, up through ceiling, p.~\pageref*{blessed-uncursed-cursed-buc}}; \hyperref[effects-of-cursed-items]{armor, won't come off, weapon, can't be unwielded, p.~\pageref*{effects-of-cursed-items}}; \hyperref[how-luck-works]{luckstone, locks negative, p.~\pageref*{how-luck-works}}\par
\hyperref[effects-of-cursed-items]{Cursed bag of holding, doubles weight, p.~\pageref*{effects-of-cursed-items}}\par
Cursed potion: \hyperref[alchemy]{dip, guaranteed explosion, p.~\pageref*{alchemy}}; \hyperref[the-ascension-run]{of gain level wish, free Gehennom skip, p.~\pageref*{the-ascension-run}}\par
\hyperref[options-worth-knowing-about]{Curses windowtype, the paneled UI, p.~\pageref*{options-worth-knowing-about}}\par
\hyperref[giant-humanoids-h]{Cyclops, Healer quest nemesis, p.~\pageref*{giant-humanoids-h}}\par

\par\smallskip{\normalsize\bfseries D}\par\smallskip

\hyperref[dogs-and-canines-d]{`d` dogs and canines, p.~\pageref*{dogs-and-canines-d}}\par
\hyperref[a-note-on-dragons]{`D` dragons, color cheat-sheet, p.~\pageref*{a-note-on-dragons}}\par
Damerell: \hyperref[acknowledgements]{Object Identification FAQ, prayer spoiler, p.~\pageref*{acknowledgements}}\par
\hyperref[dangerous-foods]{Dangerous foods, list, p.~\pageref*{dangerous-foods}}\par
\hyperref[deadly-poison]{Deadly poison, the 1-in-240 spike, p.~\pageref*{deadly-poison}}\par
Death: \hyperref[things-that-will-kill-you]{causes of (see: everything), p.~\pageref*{things-that-will-kill-you}}; \hyperref[the-astral-plane]{the Rider, instakill chance, p.~\pageref*{the-astral-plane}}\par
\hyperref[credit-and-debt]{Debt, using unpaid items in-shop, p.~\pageref*{credit-and-debt}}\par
\hyperref[delayed-deaths]{Delayed deaths, the runners, p.~\pageref*{delayed-deaths}}\par
\hyperref[major-demons]{Demogorgon, attacks on sight, no bribe, p.~\pageref*{major-demons}}\par
\hyperref[whats-different-in-gehennom]{Demon lord bribery, gold in main inventory, p.~\pageref*{whats-different-in-gehennom}}\par
\hyperref[wishable-random-artifacts]{Demonbane (Lawful silver mace), Priest first gift, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[common-combat-deaths]{Demons, summoning more demons, p.~\pageref*{common-combat-deaths}}\par
\hyperref[to-hit-calculation]{Dexterity, +to-hit bonus, p.~\pageref*{to-hit-calculation}}\par
\hyperref[use-testing-the-careful-way]{Dip ammo in sickness, poison arrows, p.~\pageref*{use-testing-the-careful-way}}\par
\hyperref[use-testing-the-careful-way]{Dipping unicorn horn in potions, p.~\pageref*{use-testing-the-careful-way}}\par
\hyperref[what-killed-the-runners-up]{Discipline, the difference, p.~\pageref*{what-killed-the-runners-up}}\par
Disenchanter: \hyperref[enchantment-drain]{mourning your former +5, range-kill don't melee, p.~\pageref*{enchantment-drain}}; \hyperref[useful-corpse-effects]{corpse, never eat, p.~\pageref*{useful-corpse-effects}}\par
\hyperref[disintegration]{Disintegration, only black dragon breath, p.~\pageref*{disintegration}}\par
\hyperref[major-demons]{Dispater, bribable arch-devil, p.~\pageref*{major-demons}}\par
\hyperref[felines-f]{Displacer beast, taming, p.~\pageref*{felines-f}}\par
\hyperref[donating-to-priests]{Donating to priests, AC stacks, p.~\pageref*{donating-to-priests}}\par
Doors: \hyperref[fighting-smart]{no diagonal entry, close for breathing room, p.~\pageref*{fighting-smart}}\par
\hyperref[dragon-scale-mail]{Dragon scale mail, upgrade from scales, p.~\pageref*{dragon-scale-mail}}\par
\hyperref[wishable-random-artifacts]{Dragonbane, reflection while wielded, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[a-note-on-dragons]{Dragons, a full briefing, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[the-castle]{Drawbridge, four ways to lower, p.~\pageref*{the-castle}}\par
\hyperref[shopkeeper-behavior]{Drop everything at the door, see your bill, p.~\pageref*{shopkeeper-behavior}}\par
\hyperref[drowning]{Drowning, preventable, p.~\pageref*{drowning}}\par
\hyperref[musical-instruments]{Drum of earthquake, pits around you, p.~\pageref*{musical-instruments}}\par
\hyperref[helmets]{Dunce cap, Int/Wis → 6, auto-curse, p.~\pageref*{helmets}}\par
\hyperref[the-big-picture]{Dungeon layout, the branching tree, p.~\pageref*{the-big-picture}}\par
\hyperref[the-big-picture]{Dungeons of Doom, upper trunk, p.~\pageref*{the-big-picture}}\par
Dwarf: \hyperref[the-races]{Str and Con caps, p.~\pageref*{the-races}}; \hyperref[humanoids-h]{dangerously underrated, p.~\pageref*{humanoids-h}}\par

\par\smallskip{\normalsize\bfseries E}\par\smallskip

\hyperref[elementals-e]{`E` elementals, p.~\pageref*{elementals-e}}\par
\hyperref[eyes-and-spheres-e]{`e` eyes and spheres, p.~\pageref*{eyes-and-spheres-e}}\par
Early: \hyperref[the-early-shopping-list]{shopping list, p.~\pageref*{the-early-shopping-list}}; \hyperref[things-that-will-kill-you]{dungeon, the deadliest stretch, p.~\pageref*{things-that-will-kill-you}}\par
\hyperref[elementals-e]{Earth elemental, phases through walls, p.~\pageref*{elementals-e}}\par
\hyperref[deadly-mistakes]{Eating mistakes, top forty, p.~\pageref*{deadly-mistakes}}\par
\hyperref[medusas-island]{Eels (giant, electric), at Medusa, p.~\pageref*{medusas-island}}\par
Elbereth: \hyperref[elbereth]{writing frantically, where the word comes from, the ward (basic), p.~\pageref*{elbereth}}; \hyperref[rules-of-the-ward]{rules of the ward, who ignores it, dead in Gehennom, the defile rule (important), p.~\pageref*{rules-of-the-ward}}; \hyperref[practical-use]{practical use, p.~\pageref*{practical-use}}; \hyperref[strategy]{dead past Castle, p.~\pageref*{strategy}}\par
\hyperref[sea-monsters]{Electric eel, six in medusa-2, p.~\pageref*{sea-monsters}}\par
\hyperref[the-elemental-planes]{Elemental Planes, four obstacles, p.~\pageref*{the-elemental-planes}}\par
\hyperref[the-races]{Elf, sleep resistance at XL 4, p.~\pageref*{the-races}}\par
\hyperref[boots]{Elven boots, stealth and silent walk, p.~\pageref*{boots}}\par
Enchant: \hyperref[scroll-enchant]{weapon, +5 ceiling safe, armor, +3 ceiling safe, p.~\pageref*{scroll-enchant}}\par
Enchantment: \hyperref[enchantment-drain]{drain, the silent ascension-killer, p.~\pageref*{enchantment-drain}}; \hyperref[enchantment]{weapon ceiling +9, armor +3/+5, p.~\pageref*{enchantment}}\par
Engrave: \hyperref[the-engrave-test-wands]{test, the procedure, test, pre-write a word in dust, p.~\pageref*{the-engrave-test-wands}}\par
\hyperref[resolving-ambiguous-engrave-results]{Engraving vanishes, three candidates, p.~\pageref*{resolving-ambiguous-engrave-results}}\par
\hyperref[engulfment]{Engulfment, two hidden monsters, p.~\pageref*{engulfment}}\par
Excalibur: \hyperref[fountains]{fountain dip, p.~\pageref*{fountains}}; \hyperref[finding-secret-doors]{search bonus, p.~\pageref*{finding-secret-doors}}; \hyperref[level-drain]{drain resistance, p.~\pageref*{level-drain}}; \hyperref[weapons]{fountain dipping odds, p.~\pageref*{weapons}}; \hyperref[wishable-random-artifacts]{(Lawful long sword), drain res + search, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[quest-artifacts]{Eye of the Aethiopica (Wizard), Vlad portal invoke, p.~\pageref*{quest-artifacts}}\par
\hyperref[quest-artifacts]{Eyes of the Overworld (Monk), astral vision when worn, p.~\pageref*{quest-artifacts}}\par

\par\smallskip{\normalsize\bfseries F}\par\smallskip

\hyperref[felines-f]{`f` felines, p.~\pageref*{felines-f}}\par
\hyperref[fungi-and-molds-f]{`F` fungi and molds, p.~\pageref*{fungi-and-molds-f}}\par
Fake: \hyperref[room-types]{Delphi, a geometric joke, p.~\pageref*{room-types}}; \hyperref[the-gnomish-mines]{luckstone mimic, BUC-test first, p.~\pageref*{the-gnomish-mines}}; \hyperref[the-ascension-run]{amulet, from bones or wish, p.~\pageref*{the-ascension-run}}\par
\hyperref[dungeon-hazards-and-how-to-survive-them]{Falling down stairs while burdened, p.~\pageref*{dungeon-hazards-and-how-to-survive-them}}\par
Famine: \hyperref[starvation]{the second Rider, p.~\pageref*{starvation}}; \hyperref[the-astral-plane]{the Rider, hunger per hit, p.~\pageref*{the-astral-plane}}\par
Feel: \hyperref[feelings-and-sounds]{feverish, lycanthropy infection, deathly sick, Pestilence or rot, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[fighting-style-caps]{Fighting style caps (bare hands, two-weapon, riding, martial arts), p.~\pageref*{fighting-style-caps}}\par
Finger: \hyperref[engravings]{in dust, fragile but instant, p.~\pageref*{engravings}}; \hyperref[key-spells]{of death, the argument-ender, p.~\pageref*{key-spells}}\par
Fire: \hyperref[dangerous-traps]{trap, sleeper threat for inventory, p.~\pageref*{dangerous-traps}}; \hyperref[useful-corpse-effects]{ant corpse, fire resistance, giant corpse, fire + Strength, p.~\pageref*{useful-corpse-effects}}; \hyperref[wishable-random-artifacts]{Brand, fire + firestorm invoke, p.~\pageref*{wishable-random-artifacts}}\par
First: \hyperref[your-first-descent]{descent, welcome to the dungeon, p.~\pageref*{your-first-descent}}; \hyperref[fighting-smart]{swing wakes the room, p.~\pageref*{fighting-smart}}\par
\hyperref[alignment]{First-game recommendation, p.~\pageref*{alignment}}\par
\hyperref[gray-stones-four-stones-one-correct-answer]{Flint, useless ammunition, p.~\pageref*{gray-stones-four-stones-one-correct-answer}}\par
Floating: \hyperref[dungeon-hazards-and-how-to-survive-them]{eye, do not hit, p.~\pageref*{dungeon-hazards-and-how-to-survive-them}}; \hyperref[eyes-and-spheres-e]{eye, never melee, eye corpse, telepathy, p.~\pageref*{eyes-and-spheres-e}}\par
\hyperref[seduction]{Foocubus, can strip cursed armor, p.~\pageref*{seduction}}\par
Food: \hyperref[how-hunger-works]{running out of, p.~\pageref*{how-hunger-works}}; \hyperref[what-to-eat]{rations, weight 20, p.~\pageref*{what-to-eat}}; \hyperref[the-food-conducts]{conducts, the hierarchy, p.~\pageref*{the-food-conducts}}\par
\hyperref[the-food-conducts]{Foodless conduct, p.~\pageref*{the-food-conducts}}\par
\hyperref[key-spells]{Force bolt, level 1 attack, p.~\pageref*{key-spells}}\par
\hyperref[forcing-locked-chests]{\#force, prying chests open, p.~\pageref*{forcing-locked-chests}}\par
\hyperref[movement-prefixes]{Force-attack (F), p.~\pageref*{movement-prefixes}}\par
\hyperref[centaurs-c]{Forest centaur, bow user, p.~\pageref*{centaurs-c}}\par
Fort: \hyperref[fort-ludios]{Ludios, vault full of gold, Ludios, Croesus across the moat, p.~\pageref*{fort-ludios}}\par
\hyperref[fountains]{Fountain dip, uncurses items, p.~\pageref*{fountains}}\par
\hyperref[fountains]{Fountains, gentle bubbling doom, p.~\pageref*{fountains}}\par
\hyperref[the-castle]{Four corner-tower alcoves, one with wishing wand, p.~\pageref*{the-castle}}\par
\hyperref[how-luck-works]{Friday the 13th, –1 baseline Luck, p.~\pageref*{how-luck-works}}\par
\hyperref[wishable-random-artifacts]{Frost Brand, cold + snowstorm invoke, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[how-luck-works]{Full moon, +1 baseline Luck, p.~\pageref*{how-luck-works}}\par
\hyperref[boots]{Fumble boots, 9-in-10 cursed, p.~\pageref*{boots}}\par

\par\smallskip{\normalsize\bfseries G}\par\smallskip

\hyperref[gnomes-g]{`G` gnomes, p.~\pageref*{gnomes-g}}\par
\hyperref[gremlins-g]{`g` gremlins and gargoyles, p.~\pageref*{gremlins-g}}\par
\hyperref[gaining-and-losing-luck]{Gaining and losing Luck, the table, p.~\pageref*{gaining-and-losing-luck}}\par
\hyperref[eyes-and-spheres-e]{Gas spore, walking explosion, p.~\pageref*{eyes-and-spheres-e}}\par
Gauntlets: \hyperref[gloves]{of power, Str 25, of dexterity, +spe to Dex, of fumbling, 9-in-10 cursed, p.~\pageref*{gloves}}\par
Gehennom: \hyperref[the-big-picture]{lower trunk, p.~\pageref*{the-big-picture}}; \hyperref[gehennom]{why is it so hot, no prayer, fire everywhere, hot ground shatters potions, p.~\pageref*{gehennom}}\par
Gelatinous: \hyperref[blobs-b]{cube, paralysis-cube of resistances, p.~\pageref*{blobs-b}}; \hyperref[vegetarian-safe-corpses]{cube corpse, four resistances, p.~\pageref*{vegetarian-safe-corpses}}\par
\hyperref[gem-identification-through-selling]{Gem identification through selling (not reliable), p.~\pageref*{gem-identification-through-selling}}\par
\hyperref[quantum-mechanics-q]{Genetic engineer, polymorph-on-claw, p.~\pageref*{quantum-mechanics-q}}\par
Genocide: \hyperref[scroll-genocide]{race trap (h, G, @, o), p.~\pageref*{scroll-genocide}}; \hyperref[plane-of-water]{class `;`, on Plane of Water, p.~\pageref*{plane-of-water}}\par
\hyperref[major-demons]{Geryon, bribable arch-devil, p.~\pageref*{major-demons}}\par
\hyperref[special-symbols]{Ghost, paints over the floor as a gap, p.~\pageref*{special-symbols}}\par
Giant: \hyperref[bats-and-birds-b]{bat, speed 22 swarmer, p.~\pageref*{bats-and-birds-b}}; \hyperref[giant-humanoids-h]{corpse, +1 Strength, p.~\pageref*{giant-humanoids-h}}; \hyperref[sea-monsters]{eel, grab and drown, p.~\pageref*{sea-monsters}}\par
\hyperref[giant-humanoids-h]{Giants throw boulders (storm, fire, frost), p.~\pageref*{giant-humanoids-h}}\par
\hyperref[wishable-random-artifacts]{Giantslayer, double vs giants, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[a-note-on-puddings]{Glob, instead of corpse, p.~\pageref*{a-note-on-puddings}}\par
\hyperref[gnomes-g]{Gnome lord, gnome king, p.~\pageref*{gnomes-g}}\par
Gnomish: \hyperref[gnomes-g]{wizard, sleep spell danger, p.~\pageref*{gnomes-g}}; \hyperref[the-gnomish-mines]{Mines, entry around Dlvl 2-4, p.~\pageref*{the-gnomish-mines}}; \hyperref[common-combat-deaths]{Mines, a choice not a routine stop, p.~\pageref*{common-combat-deaths}}\par
\hyperref[altars-and-alignment]{Gods, angering, p.~\pageref*{altars-and-alignment}}\par
\hyperref[a-note-on-dragons]{Gold dragon scale mail, the body-slot lantern, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[golems]{Gold golem, walking treasure pile, p.~\pageref*{golems}}\par
\hyperref[a-note-on-dragons]{Gray dragon scale mail, magic resistance, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[a-note-on-puddings]{Gray ooze, rusts armor, p.~\pageref*{a-note-on-puddings}}\par
\hyperref[gray-stones-four-stones-one-correct-answer]{Gray stones, four stones one answer, p.~\pageref*{gray-stones-four-stones-one-correct-answer}}\par
\hyperref[wishable-random-artifacts]{Grayswandir (Lawful silver saber), half phys, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[erosion-and-proofing]{Grease, applied to armor, p.~\pageref*{erosion-and-proofing}}\par
\hyperref[a-note-on-dragons]{Green dragon scale mail, poison + sickness resistance, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[a-note-on-puddings]{Green slime, ten-turn countdown, p.~\pageref*{a-note-on-puddings}}\par
Gremlin: \hyperref[gremlins-g]{strips intrinsic at night, multiplies in water, p.~\pageref*{gremlins-g}}\par
Grid: \hyperref[xans-and-fantastic-insects-x]{bug, can't move diagonally, p.~\pageref*{xans-and-fantastic-insects-x}}; \hyperref[deadly-mistakes]{bug, last-hit kills, p.~\pageref*{deadly-mistakes}}; \hyperref[acknowledgements]{bug, name and Tron reference, p.~\pageref*{acknowledgements}}\par
\hyperref[wishable-random-artifacts]{Grimtooth (Chaotic orcish dagger), warns of elves, p.~\pageref*{wishable-random-artifacts}}\par

\par\smallskip{\normalsize\bfseries H}\par\smallskip

\hyperref[giant-humanoids-h]{`H` giants and minotaurs, p.~\pageref*{giant-humanoids-h}}\par
\hyperref[humanoids-h]{`h` humanoids, p.~\pageref*{humanoids-h}}\par
\hyperref[acknowledgements]{Hack (1982), Jay Fenlason, p.~\pageref*{acknowledgements}}\par
\hyperref[real-gem-prices]{Hard gems (Mohs 8+), survive throws, p.~\pageref*{real-gem-prices}}\par
\hyperref[acknowledgements]{Hardfought, the variants server, p.~\pageref*{acknowledgements}}\par
\hyperref[armor-and-ac]{Haste self, alternative to speed boots, p.~\pageref*{armor-and-ac}}\par
Healer: \hyperref[the-roles]{sleep-wand surprise, sickness immunity, p.~\pageref*{the-roles}}\par
Healing: \hyperref[potion-prices]{potion, \$20 alone, p.~\pageref*{potion-prices}}; \hyperref[potion-healing]{chain, blessed pumps maxHP, p.~\pageref*{potion-healing}}; \hyperref[key-spells]{spell, level 1, p.~\pageref*{key-spells}}\par
\hyperref[feelings-and-sounds]{Health currently feels amplified, shock resistance, p.~\pageref*{feelings-and-sounds}}\par
Heart: \hyperref[how-luck-works]{of Ahriman, counts as luckstone, p.~\pageref*{how-luck-works}}; \hyperref[quest-artifacts]{of Ahriman (Barbarian), p.~\pageref*{quest-artifacts}}\par
\hyperref[the-heist]{Heist, the choreographed sequence, p.~\pageref*{the-heist}}\par
\hyperref[helmets]{Helm of brilliance, +spe to Int and Wis, p.~\pageref*{helmets}}\par
\hyperref[armor-and-ac]{Helm of caution, warning intrinsic (new in 5.0), p.~\pageref*{armor-and-ac}}\par
Helm of opposite alignment: \hyperref[the-gauntlet]{Chaotic detour, p.~\pageref*{the-gauntlet}}; \hyperref[helmets]{alignment-flip tactical uses, p.~\pageref*{helmets}}\par
\hyperref[helmets]{Helm of telepathy, when blind, p.~\pageref*{helmets}}\par
\hyperref[molochs-sanctum]{High Priest of Moloch, on the high altar, p.~\pageref*{molochs-sanctum}}\par
\hyperref[movement-traps]{Hole, like a trapdoor with manners, p.~\pageref*{movement-traps}}\par
Holy: \hyperref[blessed-uncursed-cursed-buc]{water, blesses items, p.~\pageref*{blessed-uncursed-cursed-buc}}; \hyperref[potion-holy-water]{water, making (altar prayer), water, multiplying via dip, p.~\pageref*{potion-holy-water}}\par
\hyperref[the-races]{Human, no infravision, no special talents, p.~\pageref*{the-races}}\par
\hyperref[the-defile-rule-important]{Hypocrite, alignment hit when defiling, p.~\pageref*{the-defile-rule-important}}\par

\par\smallskip{\normalsize\bfseries I}\par\smallskip

\hyperref[imps-and-minor-demons-i]{`i` imps and minor demons, p.~\pageref*{imps-and-minor-demons-i}}\par
\hyperref[special-symbols]{`I` invisible monster marker, p.~\pageref*{special-symbols}}\par
\hyperref[naming-what-youve-learned]{Identification by stacking, the merge clue, p.~\pageref*{naming-what-youve-learned}}\par
\hyperref[gaining-and-losing-luck]{Identified gem to co-aligned unicorn, +5, p.~\pageref*{gaining-and-losing-luck}}\par
Identify: \hyperref[scroll-prices]{scroll, \$20 alone, p.~\pageref*{scroll-prices}}; \hyperref[scroll-identify]{never enough scrolls of, p.~\pageref*{scroll-identify}}; \hyperref[key-spells]{spell, blessed multi-ID, p.~\pageref*{key-spells}}\par
Illiterate: \hyperref[illiterate]{conduct, only x signature allowed, p.~\pageref*{illiterate}}\par
\hyperref[delayed-deaths]{Illness (food poisoning), unicorn horn cure, p.~\pageref*{delayed-deaths}}\par
\hyperref[imps-and-minor-demons-i]{Imp, stream of insults, p.~\pageref*{imps-and-minor-demons-i}}\par
\hyperref[seduction]{Incubus, succubus, encounter table, p.~\pageref*{seduction}}\par
\hyperref[ways-to-die-instantly]{Instadeaths, recognizing the setup, p.~\pageref*{ways-to-die-instantly}}\par
\hyperref[alignment-and-blasting]{Intelligent artifacts, 4d10 blast, p.~\pageref*{alignment-and-blasting}}\par
\hyperref[the-heist]{Invocation ritual, three items on the vibrating square, p.~\pageref*{the-heist}}\par
Iron: \hyperref[golems]{golem, poison breath, p.~\pageref*{golems}}; \hyperref[iron-bars]{bars, light passes through, bars, dig around them, bars, wand of lightning melts (sometimes), p.~\pageref*{iron-bars}}; \hyperref[boots]{shoes, traps protection, p.~\pageref*{boots}}\par
\hyperref[the-map-symbols]{Item symbols, the punctuation marks, p.~\pageref*{the-map-symbols}}\par
\hyperref[dragons-d]{Ixoth, Quest dragon (Archeologist), p.~\pageref*{dragons-d}}\par
\hyperref[acknowledgements]{Izchak Miller, the lighting shopkeeper, p.~\pageref*{acknowledgements}}\par
\hyperref[the-gnomish-mines]{Izchak's lighting store, seven candles, p.~\pageref*{the-gnomish-mines}}\par

\par\smallskip{\normalsize\bfseries J}\par\smallskip

\hyperref[jabberwocks-j]{`J` jabberwock, four 2d10 attacks, p.~\pageref*{jabberwocks-j}}\par
\hyperref[jellies-j]{`j` jellies, p.~\pageref*{jellies-j}}\par
\hyperref[dogs-and-canines-d]{Jackal, leading cause of death, p.~\pageref*{dogs-and-canines-d}}\par
\hyperref[the-demon-prince-lairs]{Juiblex, Faceless Lord, swamp, p.~\pageref*{the-demon-prince-lairs}}\par
\hyperref[boots]{Jumping boots, leap-apply, p.~\pageref*{boots}}\par

\par\smallskip{\normalsize\bfseries K}\par\smallskip

\hyperref[keystone-kops-k]{`K` Keystone Kops, p.~\pageref*{keystone-kops-k}}\par
\hyperref[kobolds-k]{`k` kobolds, p.~\pageref*{kobolds-k}}\par
\hyperref[weapons]{Katana, best one-hander, p.~\pageref*{weapons}}\par
\hyperref[key-spells]{Key spells, the short list, p.~\pageref*{key-spells}}\par
\hyperref[angelic-beings-a]{Ki-rin, flying spellcaster, p.~\pageref*{angelic-beings-a}}\par
\hyperref[deadly-mistakes]{Kicking sinks, the foocubus surprise, p.~\pageref*{deadly-mistakes}}\par
Killer: \hyperref[ants-and-insects-a]{bee, swarm, p.~\pageref*{ants-and-insects-a}}; \hyperref[useful-corpse-effects]{bee corpse, poison resistance, p.~\pageref*{useful-corpse-effects}}\par
Killing: \hyperref[gaining-and-losing-luck]{peaceful, –1 Luck (50\%), pet, –1 Luck plus –15 alignment, co-aligned unicorn, –5, p.~\pageref*{gaining-and-losing-luck}}\par
\hyperref[felines-f]{Kitten, common starter pet, p.~\pageref*{felines-f}}\par
Knight: \hyperref[the-roles]{pony of, Excalibur odds (1 in 6), jousting on lance, p.~\pageref*{the-roles}}\par
\hyperref[kobolds-k]{Kobold meat, poisonous and pointless, p.~\pageref*{kobolds-k}}\par
\hyperref[keystone-kops-k]{Kops, summoned by shoplifting, p.~\pageref*{keystone-kops-k}}\par
Kraken: \hyperref[sea-monsters]{Medusa's pool variant, p.~\pageref*{sea-monsters}}; \hyperref[medusas-island]{only on medusa-4, p.~\pageref*{medusas-island}}\par

\par\smallskip{\normalsize\bfseries L}\par\smallskip

\hyperref[leprechauns-l]{`l` leprechauns, p.~\pageref*{leprechauns-l}}\par
\hyperref[liches-l]{`L` liches, p.~\pageref*{liches-l}}\par
\hyperref[dangerous-traps]{Land mine, items destroyed, p.~\pageref*{dangerous-traps}}\par
Large: \hyperref[a-note-on-mimics]{mimic, sticky claw, p.~\pageref*{a-note-on-mimics}}; \hyperref[containers]{box, chest, ice box (furniture), p.~\pageref*{containers}}\par
\hyperref[alignment]{Lawful, perks and pieties, p.~\pageref*{alignment}}\par
\hyperref[learning-spells]{Learning spells, success formula, p.~\pageref*{learning-spells}}\par
\hyperref[other-notable-tools]{Leash, pet follows through stairs, p.~\pageref*{other-notable-tools}}\par
\hyperref[what-to-eat]{Lembas wafers, best nutrition by weight, p.~\pageref*{what-to-eat}}\par
\hyperref[finding-secret-doors]{Lenses, +2 search (capped), p.~\pageref*{finding-secret-doors}}\par
\hyperref[leprechauns-l]{Leprechaun, steals gold and flees, p.~\pageref*{leprechauns-l}}\par
Level: \hyperref[movement-traps]{teleporter, separated from your pet, p.~\pageref*{movement-traps}}; \hyperref[level-drain]{drain, wraiths and friends, p.~\pageref*{level-drain}}\par
\hyperref[your-first-descent]{Levels 1 through 5, where most die, p.~\pageref*{your-first-descent}}\par
Levitation: \hyperref[drowning]{doesn't help vs eels, p.~\pageref*{drowning}}; \hyperref[alchemy]{+ Enlightenment dip = Gain level, p.~\pageref*{alchemy}}; \hyperref[boots]{boots, the cursed trap, p.~\pageref*{boots}}\par
Lichen corpse, never rots, pp.~\hyperref[the-golden-rules-of-early-survival]{\pageref*{the-golden-rules-of-early-survival}}, \hyperref[fungi-and-molds-f]{\pageref*{fungi-and-molds-f}}\par
Light: \hyperref[room-types]{source room, free lit lamp, p.~\pageref*{room-types}}; \hyperref[light-sources]{sources, candles and oil lamps, p.~\pageref*{light-sources}}\par
Lizard: \hyperref[the-golden-rules-of-early-survival]{corpse, carry one, p.~\pageref*{the-golden-rules-of-early-survival}}; \hyperref[lizards]{corpse, cures stoning, p.~\pageref*{lizards}}\par
Loadstone: \hyperref[gray-stones-four-stones-one-correct-answer]{cursed and refuses to drop, the kick test, the \#tip escape, p.~\pageref*{gray-stones-four-stones-one-correct-answer}}\par
\hyperref[credit-and-debt]{Loan, lent gold from shopkeeper, p.~\pageref*{credit-and-debt}}\par
\hyperref[unlocking-tools]{Lock pick, respectable, p.~\pageref*{unlocking-tools}}\par
\hyperref[worms-w]{Long worm, tail segments, p.~\pageref*{worms-w}}\par
\hyperref[quest-artifacts]{Longbow of Diana (Ranger), conjure arrows invoke, p.~\pageref*{quest-artifacts}}\par
\hyperref[giant-humanoids-h]{Lord Surtur, Valkyrie quest nemesis, p.~\pageref*{giant-humanoids-h}}\par
Luck: \hyperref[gaining-and-losing-luck]{secretly ruining yours, p.~\pageref*{gaining-and-losing-luck}}; \hyperref[how-luck-works]{the hidden number, timeout, 600 turns toward 0, p.~\pageref*{how-luck-works}}\par
Luckstone: \hyperref[gray-stones-four-stones-one-correct-answer]{preserves luck, p.~\pageref*{gray-stones-four-stones-one-correct-answer}}; \hyperref[how-luck-works]{freezes the drift, p.~\pageref*{how-luck-works}}\par
Lurker: \hyperref[engulfment]{above, looking up too late, above, ceiling drop, p.~\pageref*{engulfment}}\par

\par\smallskip{\normalsize\bfseries M}\par\smallskip

\hyperref[movement-prefixes]{m prefix, no-attack and menu, p.~\pageref*{movement-prefixes}}\par
\hyperref[mimics-m]{`m` mimics, p.~\pageref*{mimics-m}}\par
\hyperref[mummies-m]{`M` mummies, undead-turning shreds, p.~\pageref*{mummies-m}}\par
Magic: \hyperref[fountains]{fountain, one in seven, p.~\pageref*{fountains}}; \hyperref[movement-traps]{portal, branch entrances, p.~\pageref*{movement-traps}}; \hyperref[quest-artifacts]{Mirror of Merlin (Knight), p.~\pageref*{quest-artifacts}}\par
\hyperref[enchantment-drain]{Magic cancellation (MC), MC3 blocks 90\%, p.~\pageref*{enchantment-drain}}\par
\hyperref[musical-instruments]{Magic flute, sleep, p.~\pageref*{musical-instruments}}\par
\hyperref[musical-instruments]{Magic harp, charms monsters, p.~\pageref*{musical-instruments}}\par
\hyperref[light-sources]{Magic lamp, the wish gamble, p.~\pageref*{light-sources}}\par
Magic mapping: \hyperref[scroll-magic-mapping]{blessed shows secret doors, p.~\pageref*{scroll-magic-mapping}}; \hyperref[key-spells]{spell, level 5, p.~\pageref*{key-spells}}\par
Magic marker: \hyperref[other-notable-tools]{scroll printer, ascension-kit writes, p.~\pageref*{other-notable-tools}}\par
\hyperref[the-touch-of-death]{Magic missile, the answer to Riders, p.~\pageref*{the-touch-of-death}}\par
Magic trap: \hyperref[dangerous-traps]{random outcomes, Charisma farming, p.~\pageref*{dangerous-traps}}\par
\hyperref[what-pets-do-for-you]{Magic whistle, teleports tame creatures to you, p.~\pageref*{what-pets-do-for-you}}\par
\hyperref[drowning]{Magical breathing, breaks the drowning hold, p.~\pageref*{drowning}}\par
\hyperref[wishable-random-artifacts]{Magicbane (Neutral athame), wielded magic resistance, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[major-demons]{Mail daemon, do not attack, p.~\pageref*{major-demons}}\par
\hyperref[mana-management]{Mana, 5 Pw per spell level, p.~\pageref*{mana-management}}\par
\hyperref[the-map-symbols]{Map, learning to read, p.~\pageref*{the-map-symbols}}\par
\hyperref[the-price-is-right]{Mark, the sucker conditions, p.~\pageref*{the-price-is-right}}\par
\hyperref[room-types]{Massacre room, role corpses for sacrifice, p.~\pageref*{room-types}}\par
\hyperref[quest-artifacts]{Master Key of Thievery (Rogue), untrap invoke, p.~\pageref*{quest-artifacts}}\par
\hyperref[liches-l]{Master lich, magic resistance mandatory, p.~\pageref*{liches-l}}\par
Master mind flayer, five tentacles, pp.~\hyperref[humanoids-h]{\pageref*{humanoids-h}}, \hyperref[brainlessness]{\pageref*{brainlessness}}\par
\hyperref[room-types]{Mausoleum, mummy waiting, p.~\pageref*{room-types}}\par
\hyperref[the-big-picture]{Mazes of Menace, the whole thing, p.~\pageref*{the-big-picture}}\par
Medusa: \hyperref[humans-and-elves]{the Gorgon, p.~\pageref*{humans-and-elves}}; \hyperref[medusas-island]{surviving the gaze, p.~\pageref*{medusas-island}}\par
\hyperref[medusas-island]{Medusa's Island, three layered challenges, p.~\pageref*{medusas-island}}\par
Mind flayer: \hyperref[humanoids-h]{drains Int, p.~\pageref*{humanoids-h}}; \hyperref[brainlessness]{wear any helmet, greased helmet stacks, p.~\pageref*{brainlessness}}\par
\hyperref[the-gnomish-mines]{Mine's End, guaranteed luckstone, p.~\pageref*{the-gnomish-mines}}\par
\hyperref[the-gnomish-mines]{Minesflayer, the mind flayer surprise, p.~\pageref*{the-gnomish-mines}}\par
Minetown: \hyperref[the-gnomish-mines]{shops and temple, watch, don't attack peacefuls, p.~\pageref*{the-gnomish-mines}}\par
\hyperref[giant-humanoids-h]{Minotaur, \textasciitilde{}38 average damage per turn, p.~\pageref*{giant-humanoids-h}}\par
\hyperref[quest-artifacts]{Mitre of Holiness (Priest), p.~\pageref*{quest-artifacts}}\par
\hyperref[wishable-random-artifacts]{Mjollnir (Neutral war hammer), Str 25 return, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[real-gem-prices]{Mohs hardness, gems for engraving, p.~\pageref*{real-gem-prices}}\par
\hyperref[the-valley-of-the-dead]{Moloch shrine, do not pray, p.~\pageref*{the-valley-of-the-dead}}\par
\hyperref[molochs-sanctum]{Moloch's Sanctum, sealed level, p.~\pageref*{molochs-sanctum}}\par
Monk: \hyperref[the-roles]{no body armor, robe spellcasting bonus, p.~\pageref*{the-roles}}\par
\hyperref[carrying-capacity]{Monsters loot unlocked containers (new in 5.0), p.~\pageref*{carrying-capacity}}\par
\hyperref[deadly-mistakes]{Mount slip, riding accidents, p.~\pageref*{deadly-mistakes}}\par
\hyperref[centaurs-c]{Mountain centaur, two kicks plus weapon, p.~\pageref*{centaurs-c}}\par
\hyperref[movement-prefixes]{Movement prefixes (F force, G run, m no-attack), p.~\pageref*{movement-prefixes}}\par
\hyperref[quadrupeds-q]{Mumak, 4d12 butt, p.~\pageref*{quadrupeds-q}}\par
\hyperref[cloaks]{Mummy wrapping, blocks invisibility, p.~\pageref*{cloaks}}\par
\hyperref[musical-instruments]{Musical instruments, the passtune, p.~\pageref*{musical-instruments}}\par
Mysterious: \hyperref[the-gauntlet]{Force, downstairs reroll, Force, Chaotic discount, p.~\pageref*{the-gauntlet}}\par

\par\smallskip{\normalsize\bfseries N}\par\smallskip

\hyperref[nagas-n]{`N` nagas, p.~\pageref*{nagas-n}}\par
\hyperref[nymphs-n]{`n` nymphs, p.~\pageref*{nymphs-n}}\par
\hyperref[acknowledgements]{NAO (nethack.alt.org), the public server, p.~\pageref*{acknowledgements}}\par
\hyperref[wraiths-w]{Nazgul, sleep breath, p.~\pageref*{wraiths-w}}\par
\hyperref[why-luck-matters]{Negative Luck, prayer fails, p.~\pageref*{why-luck-matters}}\par
NetHack: \hyperref[acknowledgements]{DevTeam, Wiki, the living changelog, p.~\pageref*{acknowledgements}}\par
\hyperref[alignment]{Neutral, the most flexibility, p.~\pageref*{alignment}}\par
Newt: \hyperref[the-golden-rules-of-early-survival]{corpse, free mana sometimes, p.~\pageref*{the-golden-rules-of-early-survival}}; \hyperref[lizards]{corpse, restores 1-3 Pw, p.~\pageref*{lizards}}\par
No: \hyperref[no-genocide]{Genocide conduct, type \\"none\\", p.~\pageref*{no-genocide}}; \hyperref[wishing-restrictions]{wishing for artifacts conduct, p.~\pageref*{wishing-restrictions}}\par
\hyperref[combining-conducts]{Nudist conduct (since 3.6), p.~\pageref*{combining-conducts}}\par
\hyperref[options-worth-knowing-about]{Number\_pad option, p.~\pageref*{options-worth-knowing-about}}\par
\hyperref[a-note-on-nymphs]{Nymph, walks off the level with your bag of holding, p.~\pageref*{a-note-on-nymphs}}\par
Nymphs: \hyperref[a-note-on-nymphs]{the universal horror story, never engage carrying the Amulet, p.~\pageref*{a-note-on-nymphs}}\par

\par\smallskip{\normalsize\bfseries O}\par\smallskip

\hyperref[ogres-o]{`O` ogres, p.~\pageref*{ogres-o}}\par
\hyperref[orcs-o]{`o` orcs, p.~\pageref*{orcs-o}}\par
\hyperref[wishable-random-artifacts]{Ogresmasher, double vs ogres, p.~\pageref*{wishable-random-artifacts}}\par
Oilskin: \hyperref[drowning]{cloak, eel-slip, p.~\pageref*{drowning}}; \hyperref[containers]{sack, protects from water, p.~\pageref*{containers}}\par
\hyperref[a-note-on-trolls]{Olog-hai, the troll you fear, p.~\pageref*{a-note-on-trolls}}\par
Oracle: \hyperref[humans-and-elves]{peaceful by design, p.~\pageref*{humans-and-elves}}; \hyperref[the-oracle]{mid-levels, minor consultation (50 zm), major consultation, p.~\pageref*{the-oracle}}\par
\hyperref[a-note-on-dragons]{Orange dragon scale mail, sleep + free action, p.~\pageref*{a-note-on-dragons}}\par
Orb: \hyperref[how-luck-works]{of Fate, counts as luckstone, p.~\pageref*{how-luck-works}}; \hyperref[quest-artifacts]{of Detection (Archeologist), of Fate (Valkyrie), p.~\pageref*{quest-artifacts}}\par
\hyperref[the-races]{Orc, peaceful to other orcs, p.~\pageref*{the-races}}\par
\hyperref[orcs-o]{Orc-captain, two attacks, p.~\pageref*{orcs-o}}\par
\hyperref[the-gnomish-mines]{Orcish Town, 1-in-7 Minetown variant, p.~\pageref*{the-gnomish-mines}}\par
\hyperref[wishable-random-artifacts]{Orcrist (Chaotic elven broadsword), warns of orcs, p.~\pageref*{wishable-random-artifacts}}\par
Orcus: \hyperref[orcus-town]{Prince of Undead, Town, ghost shopping district, Town, guaranteed magic lamp or marker, p.~\pageref*{orcus-town}}\par

\par\smallskip{\normalsize\bfseries P}\par\smallskip

\hyperref[piercers-p]{`p` piercers, p.~\pageref*{piercers-p}}\par
\hyperref[puddings-and-oozes-p]{`P` puddings and oozes, p.~\pageref*{puddings-and-oozes-p}}\par
Pacifist: \hyperref[pacifist]{conduct, the figurine-of-Archon plan, p.~\pageref*{pacifist}}\par
\hyperref[things-that-will-kill-you]{Pacing, XL near Dlvl, p.~\pageref*{things-that-will-kill-you}}\par
Paperback: \hyperref[learning-spells]{the Discworld novel, +20 XP on first read, p.~\pageref*{learning-spells}}\par
\hyperref[the-castle]{Passtune, the five-note Mastermind, p.~\pageref*{the-castle}}\par
\hyperref[pauper-new-in-5.0]{Pauper conduct, no starting gear (new in 5.0), p.~\pageref*{pauper-new-in-5.0}}\par
\hyperref[per-role-skill-caps]{Per-role skill caps, p.~\pageref*{per-role-skill-caps}}\par
\hyperref[permadeaf-new-in-5.0]{Permadeaf conduct (new in 5.0), p.~\pageref*{permadeaf-new-in-5.0}}\par
\hyperref[medusas-island]{Perseus statue, looting the legend, p.~\pageref*{medusas-island}}\par
\hyperref[the-astral-plane]{Pestilence the Rider, the one to fear, p.~\pageref*{the-astral-plane}}\par
\hyperref[delayed-deaths]{Pestilence's terminal illness, Constitution timer, p.~\pageref*{delayed-deaths}}\par
Pet: \hyperref[deadly-mistakes]{kills (yours), via conflict ring, p.~\pageref*{deadly-mistakes}}; \hyperref[keeping-your-pet-alive]{accidentally killing your, revive at co-aligned altar, gains resistances from corpses, p.~\pageref*{keeping-your-pet-alive}}; \hyperref[starting-pets]{your best early asset, growth from feeding, curse detection, p.~\pageref*{starting-pets}}; \hyperref[what-pets-do-for-you]{shoplifting, store-without-paying, p.~\pageref*{what-pets-do-for-you}}\par
\hyperref[petless-new-in-5.0]{Petless conduct (new in 5.0), p.~\pageref*{petless-new-in-5.0}}\par
\hyperref[petrification-stoning]{Petrification (stoning), the five-turn ladder, p.~\pageref*{petrification-stoning}}\par
\hyperref[other-notable-tools]{Pickaxe and mattock, dig anywhere, p.~\pageref*{other-notable-tools}}\par
\hyperref[piercers-p]{Piercer, drop from ceiling, p.~\pageref*{piercers-p}}\par
Pit: \hyperref[snakes-s]{viper, cobra, poison bites, p.~\pageref*{snakes-s}}; \hyperref[movement-traps]{climb out, p.~\pageref*{movement-traps}}\par
Plane: \hyperref[the-elemental-planes]{portals, confused gold detection, of Earth, dig the portal, of Air, cloud bubbles drift, of Air, conflict tactic, p.~\pageref*{the-elemental-planes}}; \hyperref[plane-of-fire]{of Fire, fire resistance non-optional, of Water, magical breathing required, p.~\pageref*{plane-of-fire}}\par
\hyperref[quest-artifacts]{Platinum Yendorian Express Card (Tourist), charge an item, p.~\pageref*{quest-artifacts}}\par
Polymorph: \hyperref[dangerous-traps]{trap, free booth with control, p.~\pageref*{dangerous-traps}}; \hyperref[polymorph-as-a-tool]{control, the form-chooser, p.~\pageref*{polymorph-as-a-tool}}; \hyperref[polymorph-restrictions]{restrictions (poly self, poly objects), p.~\pageref*{polymorph-restrictions}}\par
Polymorphing: \hyperref[what-pets-do-for-you]{your pet, titan first choice, p.~\pageref*{what-pets-do-for-you}}; \hyperref[shopkeeper-behavior]{the shopkeeper, the prep, p.~\pageref*{shopkeeper-behavior}}\par
\hyperref[polymorph-as-a-tool]{Polypile, away from your bag, p.~\pageref*{polymorph-as-a-tool}}\par
Potion: \hyperref[potion-prices]{prices, \$20 to \$300, p.~\pageref*{potion-prices}}; \hyperref[the-potion-table]{table, by price, p.~\pageref*{the-potion-table}}\par
\hyperref[confused-reading]{Potion of confusion, the controlled confuser, p.~\pageref*{confused-reading}}\par
\hyperref[potion-gain-ability]{Potion of gain ability, blessed boosts all stats, p.~\pageref*{potion-gain-ability}}\par
\hyperref[potion-gain-level]{Potion of gain level, raises XL, p.~\pageref*{potion-gain-level}}\par
\hyperref[potion-polymorph]{Potion of polymorph, dip-arrow test, p.~\pageref*{potion-polymorph}}\par
\hyperref[potion-speed]{Potion of speed, permanent intrinsic, p.~\pageref*{potion-speed}}\par
Prayer: \hyperref[the-golden-rules-of-early-survival]{emergency button cooldown, p.~\pageref*{the-golden-rules-of-early-survival}}; \hyperref[prayer]{when to, what it fixes, cooldown, \textasciitilde{}1000 turns, p.~\pageref*{prayer}}\par
Priest: \hyperref[the-roles]{BUC sense for free, Demonbane first gift, p.~\pageref*{the-roles}}\par
\hyperref[donating-to-priests]{Protection racket, donation AC ladder, p.~\pageref*{donating-to-priests}}\par
\hyperref[worms-w]{Purple worm, swallows you whole, p.~\pageref*{worms-w}}\par
\hyperref[cockatrices-c]{Pyrolisk, fire-gaze cousin, p.~\pageref*{cockatrices-c}}\par

\par\smallskip{\normalsize\bfseries Q}\par\smallskip

\hyperref[quadrupeds-q]{`q` quadrupeds, p.~\pageref*{quadrupeds-q}}\par
\hyperref[quantum-mechanics-q]{`Q` quantum mechanics, teleport-on-claw, p.~\pageref*{quantum-mechanics-q}}\par
\hyperref[fountains]{Quaffing a fountain, slot-machine table, p.~\pageref*{fountains}}\par
\hyperref[quantum-mechanics-q]{Quantum mechanic corpse, toggles Fast, p.~\pageref*{quantum-mechanics-q}}\par
\hyperref[imps-and-minor-demons-i]{Quasit, drains Dex, p.~\pageref*{imps-and-minor-demons-i}}\par
\hyperref[ants-and-insects-a]{Queen bee, royal jelly source, p.~\pageref*{ants-and-insects-a}}\par
Quest: \hyperref[the-quest]{portal, magenta `\textasciicircum{}`, XL 14 and alignment 20, leader, first floor, nemesis, kill twice (life-saving), artifact, on the nemesis's square, p.~\pageref*{the-quest}}; \hyperref[quest-artifacts]{artifacts, the per-role list, p.~\pageref*{quest-artifacts}}\par

\par\smallskip{\normalsize\bfseries R}\par\smallskip

\hyperref[rodents-r]{`r` rodents, p.~\pageref*{rodents-r}}\par
\hyperref[rust-monsters-and-disenchanters-r]{`R` rust monster, disenchanter, p.~\pageref*{rust-monsters-and-disenchanters-r}}\par
\hyperref[the-races]{Races, the five, p.~\pageref*{the-races}}\par
Ranged: \hyperref[the-early-shopping-list]{attack, almost always safer, p.~\pageref*{the-early-shopping-list}}; \hyperref[fighting-smart]{attackers retreat, backing into corners, p.~\pageref*{fighting-smart}}\par
Ranger: \hyperref[the-roles]{+2 cloak of displacement at start, dagger and arrow stack, p.~\pageref*{the-roles}}\par
\hyperref[deadly-mistakes]{Reading unidentified scrolls in a shop, p.~\pageref*{deadly-mistakes}}\par
\hyperref[real-gem-prices]{Real gem prices, the table, p.~\pageref*{real-gem-prices}}\par
\hyperref[recharging]{Recharging, n³/343 explosion formula, p.~\pageref*{recharging}}\par
\hyperref[a-note-on-dragons]{Red dragon scale mail, fire + infravision, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[disintegration]{Reflection, bounces back but they resist, p.~\pageref*{disintegration}}\par
\hyperref[scroll-remove-curse]{Remove curse, the happy ending, p.~\pageref*{scroll-remove-curse}}\par
\hyperref[brainlessness]{Restore ability, returning lost stats, p.~\pageref*{brainlessness}}\par
\hyperref[scroll-reverse-genocide]{Reverse genocide, cursed scroll = spawn 4-6, p.~\pageref*{scroll-reverse-genocide}}\par
\hyperref[acknowledgements]{RGRN (rec.games.roguelike.nethack), p.~\pageref*{acknowledgements}}\par
\hyperref[the-astral-plane]{Rider corpse, instantly fatal to eat, p.~\pageref*{the-astral-plane}}\par
\hyperref[training-a-skill]{Riding, 100 squares per tick, p.~\pageref*{training-a-skill}}\par
Ring: \hyperref[ring-prices]{prices, \$100 to \$300, p.~\pageref*{ring-prices}}; \hyperref[the-ring-table]{of teleport control, on-demand transport, hunger, every ring costs nutrition, of sustain ability, prevents stat drain, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of aggravate monster, the niche use, p.~\pageref*{the-ring-table}}\par
Ring of conflict: \hyperref[fighting-smart]{in combat, p.~\pageref*{fighting-smart}}; \hyperref[the-ring-table]{monsters fight each other, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of free action, anti-paralysis, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of polymorph control, less critical now, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of protection, chargeable, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of regeneration, hungry healer, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of searching, auto-search each turn, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of slow digestion, foodless option, p.~\pageref*{the-ring-table}}\par
\hyperref[the-ring-table]{Ring of warning, threat-color overlay, p.~\pageref*{the-ring-table}}\par
\hyperref[cloaks]{Robe, casting bonus, p.~\pageref*{cloaks}}\par
\hyperref[rodents-r]{Rock mole, eats your metal, p.~\pageref*{rodents-r}}\par
Rogue: \hyperref[the-roles]{multishot dagger throw, backstab bonus, p.~\pageref*{the-roles}}; \hyperref[the-rogue-level]{Level, older more primitive world, Level, all uppercase wildlife, p.~\pageref*{the-rogue-level}}; \hyperref[acknowledgements]{(1980), Toy and Wichman, p.~\pageref*{acknowledgements}}\par
\hyperref[dangerous-traps]{Rolling boulder, fixed track, p.~\pageref*{dangerous-traps}}\par
\hyperref[golems]{Rope golem, grappling hug, p.~\pageref*{golems}}\par
\hyperref[quadrupeds-q]{Rothe, three attacks per turn, p.~\pageref*{quadrupeds-q}}\par
\hyperref[dungeon-hazards-and-how-to-survive-them]{Rotted corpse, the 30-turn window, p.~\pageref*{dungeon-hazards-and-how-to-survive-them}}\par
\hyperref[weapons]{Rubber hose, joke weapon, p.~\pageref*{weapons}}\par
\hyperref[movement-prefixes]{Run direction (G), p.~\pageref*{movement-prefixes}}\par
\hyperref[weapons]{Runesword, Stormbringer base, p.~\pageref*{weapons}}\par
Rust: \hyperref[rust-monsters-and-disenchanters-r]{monster, strip iron first, p.~\pageref*{rust-monsters-and-disenchanters-r}}; \hyperref[nuisance-traps]{trap, splashes water, p.~\pageref*{nuisance-traps}}\par

\par\smallskip{\normalsize\bfseries S}\par\smallskip

\hyperref[arachnids-and-centipedes-s]{`s` arachnids and centipedes, p.~\pageref*{arachnids-and-centipedes-s}}\par
\hyperref[snakes-s]{`S` snakes, p.~\pageref*{snakes-s}}\par
\hyperref[containers]{Sack, basic storage, p.~\pageref*{containers}}\par
Sacrifice: \hyperref[sacrifice]{fresh within 50 turns, role-biased first gift, minimum corpse value, p.~\pageref*{sacrifice}}; \hyperref[gaining-and-losing-luck]{luck ceiling, difficulty must exceed, p.~\pageref*{gaining-and-losing-luck}}\par
\hyperref[feelings-and-sounds]{Sad feeling, your pet died offscreen, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[lizards]{Salamander, Gehennom-only, p.~\pageref*{lizards}}\par
\hyperref[sacrifice]{Same-race sacrifice, forbidden, p.~\pageref*{sacrifice}}\par
Samurai: \hyperref[the-roles]{katana opening, wakizashi is dead weight, giri-breaking penalty, p.~\pageref*{the-roles}}\par
\hyperref[apelike-creatures-y]{Sasquatch, fast, p.~\pageref*{apelike-creatures-y}}\par
\hyperref[quest-artifacts]{Sceptre of Might (Caveman), conflict invoke, p.~\pageref*{quest-artifacts}}\par
\hyperref[arachnids-and-centipedes-s]{Scorpius, named quest nemesis, p.~\pageref*{arachnids-and-centipedes-s}}\par
\hyperref[scroll-charging]{Scroll of charging, save for wand of wishing, p.~\pageref*{scroll-charging}}\par
\hyperref[deadly-mistakes]{Scroll of earth on yourself, buried alive, p.~\pageref*{deadly-mistakes}}\par
\hyperref[scroll-genocide]{Scroll of genocide, the nuclear option, p.~\pageref*{scroll-genocide}}\par
Scroll of identify: \hyperref[scroll-identify]{main-inventory only, blessed jackpot 1-in-5, p.~\pageref*{scroll-identify}}\par
Scroll of scare monster: \hyperref[practical-use]{drop-and-stand, p.~\pageref*{practical-use}}; \hyperref[scroll-scare-monster]{drop don't read, p.~\pageref*{scroll-scare-monster}}\par
\hyperref[taming-new-creatures]{Scroll of taming, 3×3 area, p.~\pageref*{taming-new-creatures}}\par
\hyperref[scroll-teleportation]{Scroll of teleportation, escape hatch, p.~\pageref*{scroll-teleportation}}\par
Searching: \hyperref[searching-and-detection]{(`s` command), repeat with luck, p.~\pageref*{searching-and-detection}}; \hyperref[the-sink-test-rings]{ring, kept on drop, p.~\pageref*{the-sink-test-rings}}\par
\hyperref[finding-secret-doors]{Secret doors, the architects believed in them, p.~\pageref*{finding-secret-doors}}\par
\hyperref[seduction]{Seduction (foocubus encounter), p.~\pageref*{seduction}}\par
\hyperref[deadly-mistakes]{Self-zap wand, ray ricochet, p.~\pageref*{deadly-mistakes}}\par
Shield: \hyperref[level-drain]{of drain resistance, new in 5.0, p.~\pageref*{level-drain}}; \hyperref[shields]{of reflection, saves the body slot, of drain resistance (new in 5.0), of shock resistance (new in 5.0), p.~\pageref*{shields}}\par
\hyperref[shirts]{Shirts, Hawaiian and T-shirt, p.~\pageref*{shirts}}\par
Shopkeeper: \hyperref[humans-and-elves]{tougher NPC than you, p.~\pageref*{humans-and-elves}}; \hyperref[shopping-and-shopkeeper-pricing]{angering, p.~\pageref*{shopping-and-shopkeeper-pricing}}\par
\hyperref[fungi-and-molds-f]{Shrieker, summons neighbors, p.~\pageref*{fungi-and-molds-f}}\par
Silver: \hyperref[weapons]{saber, demon damage, saber bonus, late-game weapon, p.~\pageref*{weapons}}\par
\hyperref[a-note-on-dragons]{Silver dragon scale mail, reflection, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[room-types]{Single-monster-type room, almost always themed, p.~\pageref*{room-types}}\par
Sink: \hyperref[sinks]{kicking for rings and trouble, dishwasher demon (sink foocubus), dipping potions for messages, quaffing the drain, dropping a ring down, p.~\pageref*{sinks}}; \hyperref[the-sink-test-rings]{test, the ring drop, p.~\pageref*{the-sink-test-rings}}\par
\hyperref[delayed-deaths]{Sinking in lava, levitate or pray, p.~\pageref*{delayed-deaths}}\par
\hyperref[sinks]{Sinks, dungeon's underrated ID tool, p.~\pageref*{sinks}}\par
\hyperref[zombies-z]{Skeleton, only from a trap, p.~\pageref*{zombies-z}}\par
Skill: \hyperref[the-skill-ladder]{slots, 2 + XL + crowning, p.~\pageref*{the-skill-ladder}}; \hyperref[what-a-rank-buys-you]{rank effects, to-hit/damage, p.~\pageref*{what-a-rank-buys-you}}\par
\hyperref[common-combat-deaths]{Sleep without resistance, near-instadeath, p.~\pageref*{common-combat-deaths}}\par
\hyperref[dangerous-traps]{Sleeping gas trap, deadly in zoos, p.~\pageref*{dangerous-traps}}\par
\hyperref[delayed-deaths]{Sliming, ten-turn countdown, p.~\pageref*{delayed-deaths}}\par
\hyperref[the-sink-test-rings]{Slow digestion ring, kept on drop, p.~\pageref*{the-sink-test-rings}}\par
\hyperref[feelings-and-sounds]{Slowing down, you're turning to stone, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[feelings-and-sounds]{Slurping sound, gelatinous cube ate items, p.~\pageref*{feelings-and-sounds}}\par
Small: \hyperref[a-note-on-mimics]{mimic, top-ten killer, p.~\pageref*{a-note-on-mimics}}; \hyperref[shields]{shield, no spellcast penalty, p.~\pageref*{shields}}\par
\hyperref[wishable-random-artifacts]{Snickersnee (Samurai katana), Shkinng! free polearm reach, p.~\pageref*{wishable-random-artifacts}}\par
Sokoban: \hyperref[sokoban]{entry one level above Oracle, boulders into pits, no teleport here, cheating cost (–1 Luck each), prize, bag of holding or amulet of reflection, Strength training side effect, p.~\pageref*{sokoban}}; \hyperref[sokoban-solutions]{solving without cheating, mirrored variants (new in 5.0), scrolls of earth as fillers, p.~\pageref*{sokoban-solutions}}\par
\hyperref[ants-and-insects-a]{Soldier ant, speed 18 packs, p.~\pageref*{ants-and-insects-a}}\par
Speed: \hyperref[armor-and-ac]{boots, more turns equals more, p.~\pageref*{armor-and-ac}}; \hyperref[boots]{boots, free action on 2/3 turns, p.~\pageref*{boots}}\par
Spell: \hyperref[brainlessness]{amnesia, mind flayer side effect, p.~\pageref*{brainlessness}}; \hyperref[learning-spells]{memory, \textasciitilde{}20,000 turns, p.~\pageref*{learning-spells}}\par
Spellbook: \hyperref[spellbook-prices]{prices, 100 × level, p.~\pageref*{spellbook-prices}}; \hyperref[learning-spells]{failure effects by level, 4 successful reads to fade, level 7 explosion rune, p.~\pageref*{learning-spells}}\par
\hyperref[spellcasting]{Spellcasting, mana not sparkles, p.~\pageref*{spellcasting}}\par
\hyperref[room-types]{Spider nest, scales with depth, p.~\pageref*{room-types}}\par
\hyperref[movement-traps]{Spiked pit, possibly poisoned, p.~\pageref*{movement-traps}}\par
\hyperref[acknowledgements]{Spoilers, Hugo and O'Donnell, p.~\pageref*{acknowledgements}}\par
\hyperref[jellies-j]{Spotted jelly, passive acid, p.~\pageref*{jellies-j}}\par
\hyperref[useful-corpse-effects]{Sprig of wolfsbane, cures lycanthropy, p.~\pageref*{useful-corpse-effects}}\par
\hyperref[nuisance-traps]{Squeaky board, wakes the room, p.~\pageref*{nuisance-traps}}\par
Staff: \hyperref[level-drain]{of Aesculapius, drain res, p.~\pageref*{level-drain}}; \hyperref[quest-artifacts]{of Aesculapius (Healer), drain-life on hit, p.~\pageref*{quest-artifacts}}\par
\hyperref[the-map-symbols]{Stairs, up and down (`<`, `>`), p.~\pageref*{the-map-symbols}}\par
Stalker: \hyperref[elementals-e]{see-invisible corpse, p.~\pageref*{elementals-e}}; \hyperref[useful-corpse-effects]{corpse, invisibility and see invisible, p.~\pageref*{useful-corpse-effects}}\par
\hyperref[what-to-pack]{Starting kit, improving on, p.~\pageref*{what-to-pack}}\par
\hyperref[starvation]{Starvation, faint then die, p.~\pageref*{starvation}}\par
\hyperref[the-early-shopping-list]{Stashing, one level up, p.~\pageref*{the-early-shopping-list}}\par
\hyperref[acknowledgements]{Steelypips, Kate Nepveu's archive, p.~\pageref*{acknowledgements}}\par
\hyperref[other-notable-tools]{Stethoscope, HP check and crowning meter, p.~\pageref*{other-notable-tools}}\par
\hyperref[wishable-random-artifacts]{Sting (Chaotic elven dagger), warns of orcs, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[scroll-stinking-cloud]{Stinking cloud, area attack, p.~\pageref*{scroll-stinking-cloud}}\par
\hyperref[petrification-stoning]{Stoning, avoiding, p.~\pageref*{petrification-stoning}}\par
Stormbringer: \hyperref[level-drain]{drain res while wielded (chaotic), p.~\pageref*{level-drain}}; \hyperref[wishable-random-artifacts]{(Chaotic runesword), drain life, p.~\pageref*{wishable-random-artifacts}}\par
Strange: \hyperref[feelings-and-sounds]{wind, Oracle level, mental acuity, telepathy gained, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[delayed-deaths]{Strangulation, uncurse amulet first, p.~\pageref*{delayed-deaths}}\par
\hyperref[damage]{Strength bonus, capped at +6, p.~\pageref*{damage}}\par
\hyperref[wishable-random-artifacts]{Sunsword (Lawful), 5.0 blinding ray, p.~\pageref*{wishable-random-artifacts}}\par
Supply: \hyperref[supply-containers]{containers, chests, locked treasure, p.~\pageref*{supply-containers}}\par

\par\smallskip{\normalsize\bfseries T}\par\smallskip

\hyperref[trappers-and-lurkers-t]{`t` trappers and lurkers, p.~\pageref*{trappers-and-lurkers-t}}\par
\hyperref[a-note-on-trolls]{`T` trolls, do not stay dead, p.~\pageref*{a-note-on-trolls}}\par
\hyperref[feeding-and-loyalty]{Tameness, the invisible score, p.~\pageref*{feeding-and-loyalty}}\par
\hyperref[movement-traps]{Teleport trap, free transport with control, p.~\pageref*{movement-traps}}\par
\hyperref[room-types]{Teleportation hub, fixed-destination, p.~\pageref*{room-types}}\par
Temple: \hyperref[room-types]{altar plus priest, p.~\pageref*{room-types}}; \hyperref[detecting-curses]{donation, does NOT reveal BUC, p.~\pageref*{detecting-curses}}\par
Tengu: \hyperref[imps-and-minor-demons-i]{teleport and teleport-control corpse, p.~\pageref*{imps-and-minor-demons-i}}; \hyperref[useful-corpse-effects]{corpse, teleportitis / teleport control, p.~\pageref*{useful-corpse-effects}}\par
The: \hyperref[the-price-is-right]{Price Is Right, shopkeepers identify, p.~\pageref*{the-price-is-right}}; \hyperref[acknowledgements]{DevTeam is THINKING, the 12-year gap, p.~\pageref*{acknowledgements}}\par
Throne: \hyperref[room-types]{room, sit at your own risk, p.~\pageref*{room-types}}; \hyperref[thrones]{the purest gamble, wish only at positive Luck 7+, vanishes in a puff of logic, kicking for gold and gems, p.~\pageref*{thrones}}; \hyperref[the-castle]{room (Castle court), p.~\pageref*{the-castle}}\par
\hyperref[use-testing-the-careful-way]{Throw potions at monsters (potion test), p.~\pageref*{use-testing-the-careful-way}}\par
\hyperref[the-price-is-right]{Throw-into-shop trick, free quote, p.~\pageref*{the-price-is-right}}\par
Tin: \hyperref[what-to-eat]{of spinach, +1 Str, p.~\pageref*{what-to-eat}}; \hyperref[other-notable-tools]{opener, blessed instant, p.~\pageref*{other-notable-tools}}\par
\hyperref[other-notable-tools]{Tinning kit, intrinsic grinder bypass, p.~\pageref*{other-notable-tools}}\par
\hyperref[what-to-eat]{Tins, the occupation trap, p.~\pageref*{what-to-eat}}\par
\hyperref[giant-humanoids-h]{Titan, spell-casting pet target, p.~\pageref*{giant-humanoids-h}}\par
\hyperref[to-hit-calculation]{To-hit roll, the d20 of fate, p.~\pageref*{to-hit-calculation}}\par
\hyperref[things-that-will-kill-you]{Top ten killers, the list, p.~\pageref*{things-that-will-kill-you}}\par
Touchstone: \hyperref[gray-stones-four-stones-one-correct-answer]{real gem on rub, p.~\pageref*{gray-stones-four-stones-one-correct-answer}}; \hyperref[gem-identification-through-selling]{blessed names gems on rub, p.~\pageref*{gem-identification-through-selling}}\par
Tourist: \hyperref[the-roles]{hardest standard role, camera-flash plan, magic mapping scrolls at start, p.~\pageref*{the-roles}}\par
\hyperref[other-notable-tools]{Towel, cream pie and blindfold, p.~\pageref*{other-notable-tools}}\par
\hyperref[room-types]{Trap room, recognize and retreat, p.~\pageref*{room-types}}\par
\hyperref[movement-traps]{Trapdoor, 25\% chance to keep falling, p.~\pageref*{movement-traps}}\par
\hyperref[trappers-and-lurkers-t]{Trapper, floor in disguise, p.~\pageref*{trappers-and-lurkers-t}}\par
\hyperref[travel]{Travel (`\_`), shortest path autopilot, p.~\pageref*{travel}}\par
\hyperref[feeding-and-loyalty]{Tripe ration, dog food, p.~\pageref*{feeding-and-loyalty}}\par
Trolls: \hyperref[a-note-on-trolls]{revive timer, gear-and-corpse loop, p.~\pageref*{a-note-on-trolls}}\par
\hyperref[wishable-random-artifacts]{Trollsbane, regeneration while wielded, p.~\pageref*{wishable-random-artifacts}}\par
Tsurugi: \hyperref[how-luck-works]{of Muramasa, counts as luckstone, p.~\pageref*{how-luck-works}}; \hyperref[quest-artifacts]{of Muramasa (Samurai), p.~\pageref*{quest-artifacts}}\par
\hyperref[feelings-and-sounds]{Turning into slime, the 10-turn timer, p.~\pageref*{feelings-and-sounds}}\par
\hyperref[damage]{Two-handed weapons, 3/2 Strength damage, p.~\pageref*{damage}}\par
\hyperref[two-weapon-combat]{Two-weapon Expert, Rogue and Samurai only, p.~\pageref*{two-weapon-combat}}\par

\par\smallskip{\normalsize\bfseries U}\par\smallskip

\hyperref[unicorns-and-horses-u]{`u` horses and unicorns, p.~\pageref*{unicorns-and-horses-u}}\par
\hyperref[umber-hulks-u]{`U` umber hulk, confusion gaze, p.~\pageref*{umber-hulks-u}}\par
\hyperref[blessed-uncursed-cursed-buc]{Unholy water, the evil twin, p.~\pageref*{blessed-uncursed-cursed-buc}}\par
Unicorn: \hyperref[unicorns-and-horses-u]{gem-throwing playbook, p.~\pageref*{unicorns-and-horses-u}}; \hyperref[altars-and-alignment]{(co-aligned), never sacrifice, p.~\pageref*{altars-and-alignment}}; \hyperref[gaining-and-losing-luck]{gem-throwing, +5 luck max, p.~\pageref*{gaining-and-losing-luck}}\par
Unicorn horn: \hyperref[unicorn-horn-interactions]{dip table, no longer a cure-all, p.~\pageref*{unicorn-horn-interactions}}; \hyperref[other-notable-tools]{status-cure all, blessed seven ailments, p.~\pageref*{other-notable-tools}}\par
\hyperref[unlocking-tools]{Unlocking tools, skeleton key best, p.~\pageref*{unlocking-tools}}\par

\par\smallskip{\normalsize\bfseries V}\par\smallskip

\hyperref[vampires-v]{`V` vampires, p.~\pageref*{vampires-v}}\par
\hyperref[vortices-v]{`v` vortices, p.~\pageref*{vortices-v}}\par
Valkyrie: \hyperref[the-roles]{easy-mode recommendation, Mjollnir waiting, Female only, p.~\pageref*{the-roles}}\par
\hyperref[the-valley-of-the-dead]{Valley of the Dead, Gehennom entrance, p.~\pageref*{the-valley-of-the-dead}}\par
Vampire: \hyperref[vampires-v]{level drain, p.~\pageref*{vampires-v}}; \hyperref[bats-and-birds-b]{bat, Str-draining bite, p.~\pageref*{bats-and-birds-b}}\par
\hyperref[where-the-word-comes-from]{Varda Elentári, Star-Queen, p.~\pageref*{where-the-word-comes-from}}\par
Vault: \hyperref[vaults]{guard, name yourself Croesus, guard, lying costs Lawful alignment, p.~\pageref*{vaults}}\par
\hyperref[vaults]{Vaults, the 2×2 closet of gold, p.~\pageref*{vaults}}\par
Vegan: \hyperref[what-to-eat]{no eggs either, p.~\pageref*{what-to-eat}}; \hyperref[the-food-conducts]{conduct, p.~\pageref*{the-food-conducts}}\par
Vegetarian: \hyperref[what-to-eat]{allowed corpses, p.~\pageref*{what-to-eat}}; \hyperref[the-food-conducts]{conduct, p.~\pageref*{the-food-conducts}}\par
\hyperref[options-worth-knowing-about]{Verbose option, message-log noise, p.~\pageref*{options-worth-knowing-about}}\par
\hyperref[the-heist]{Vibrating square, search by walking, p.~\pageref*{the-heist}}\par
\hyperref[fungi-and-molds-f]{Violet fungus, sticky paralysis, p.~\pageref*{fungi-and-molds-f}}\par
Vlad: \hyperref[vampires-v]{the Impaler, top of his tower, p.~\pageref*{vampires-v}}; \hyperref[engravings]{was here, trap-door closet marker, p.~\pageref*{engravings}}\par
Vlad's: \hyperref[vlads-tower]{throne, fourth sit's the charm, Tower, branches upward, throne, four wishes in thirteen sits, throne, the nine bad outcomes, p.~\pageref*{vlads-tower}}\par
\hyperref[wishable-random-artifacts]{Vorpal Blade, behead chance, p.~\pageref*{wishable-random-artifacts}}\par

\par\smallskip{\normalsize\bfseries W}\par\smallskip

\hyperref[worms-w]{`w` worms, p.~\pageref*{worms-w}}\par
\hyperref[wraiths-w]{`W` wraiths, p.~\pageref*{wraiths-w}}\par
\hyperref[credit-and-debt]{Walk-out hazard, unpaid items, p.~\pageref*{credit-and-debt}}\par
Wand: \hyperref[wand-prices]{prices, \$100 to \$500, p.~\pageref*{wand-prices}}; \hyperref[the-engrave-test-wands]{identifying by engraving, p.~\pageref*{the-engrave-test-wands}}; \hyperref[orcus-town]{of Orcus, his fingertip death ray, p.~\pageref*{orcus-town}}\par
Wand of cancellation: \hyperref[wand-cancellation]{never in a bag, on cursed bag of holding, p.~\pageref*{wand-cancellation}}\par
\hyperref[wand-fire-cold-lightning]{Wand of cold, freezes water (ice path), p.~\pageref*{wand-fire-cold-lightning}}\par
Wand of death: \hyperref[the-touch-of-death]{don't zap at Death, p.~\pageref*{the-touch-of-death}}; \hyperref[wand-death]{the closer, p.~\pageref*{wand-death}}; \hyperref[the-astral-plane]{on Death, heals him, p.~\pageref*{the-astral-plane}}\par
Wand of digging: \hyperref[engulfment]{escape from inside, p.~\pageref*{engulfment}}; \hyperref[wand-digging]{ascension staple, cursed zaps down, p.~\pageref*{wand-digging}}\par
Wand of fire: \hyperref[engravings]{burns Elbereth permanently, p.~\pageref*{engravings}}; \hyperref[wand-fire-cold-lightning]{cold, lightning (rays), p.~\pageref*{wand-fire-cold-lightning}}\par
\hyperref[wand-make-invisible]{Wand of make invisible, 31-45 turns, p.~\pageref*{wand-make-invisible}}\par
\hyperref[the-castle]{Wand of opening / spell of knock, opens drawbridge, p.~\pageref*{the-castle}}\par
\hyperref[wand-polymorph]{Wand of polymorph, on a pile (polypile), p.~\pageref*{wand-polymorph}}\par
\hyperref[key-wands]{Wand of probing, HP / status check, p.~\pageref*{key-wands}}\par
Wand of secret door detection: \hyperref[searching-and-detection]{no aim, p.~\pageref*{searching-and-detection}}; \hyperref[wands-and-staves]{area reveal, p.~\pageref*{wands-and-staves}}\par
\hyperref[wand-stasis]{Wand of stasis, new in 5.0, p.~\pageref*{wand-stasis}}\par
\hyperref[the-castle]{Wand of striking, destroys drawbridge, p.~\pageref*{the-castle}}\par
\hyperref[wand-teleportation]{Wand of teleportation, monster removal, p.~\pageref*{wand-teleportation}}\par
Wand of wishing: \hyperref[wand-wishing]{found with one charge, recharge once and only once, p.~\pageref*{wand-wishing}}\par
\hyperref[unicorns-and-horses-u]{Warhorse, ridden into mid-game, p.~\pageref*{unicorns-and-horses-u}}\par
\hyperref[attack-wands-and-the-warning-shot]{Warning shot, monster's first wand zap, p.~\pageref*{attack-wands-and-the-warning-shot}}\par
Water: \hyperref[snakes-s]{moccasin, from fountain, p.~\pageref*{snakes-s}}; \hyperref[major-demons]{demon, fountain summons, p.~\pageref*{major-demons}}; \hyperref[fountains]{demon wish, roughly 1 in 150 quaffs, p.~\pageref*{fountains}}; \hyperref[the-potion-table]{potion, always clear, p.~\pageref*{the-potion-table}}; \hyperref[boots]{walking boots, Castle drawbridge, p.~\pageref*{boots}}\par
\hyperref[how-hunger-works]{Weak status, –1 Str, p.~\pageref*{how-hunger-works}}\par
\hyperref[weaponless]{Weaponless conduct, p.~\pageref*{weaponless}}\par
\hyperref[weapons]{Weapons, choice depends on role, p.~\pageref*{weapons}}\par
\hyperref[wishable-random-artifacts]{Werebane, lycanthropy defense, p.~\pageref*{wishable-random-artifacts}}\par
\hyperref[dogs-and-canines-d]{Werewolf, werejackal, lycanthropy, p.~\pageref*{dogs-and-canines-d}}\par
\hyperref[what-to-wish-for]{What to wish for, p.~\pageref*{what-to-wish-for}}\par
\hyperref[a-note-on-dragons]{White dragon scale mail, cold + slow digestion, p.~\pageref*{a-note-on-dragons}}\par
\hyperref[whats-different-in-gehennom]{Wielding Excalibur or Demonbane, no bribery, p.~\pageref*{whats-different-in-gehennom}}\par
Wish: \hyperref[sources-of-wishes]{sources, six in total, p.~\pageref*{sources-of-wishes}}; \hyperref[wish-syntax]{syntax, blessed greased fixed +3, silent substitutions (fake amulet, etc.), p.~\pageref*{wish-syntax}}; \hyperref[wishing-restrictions]{for \\"nothing\\", the escape hatch, p.~\pageref*{wishing-restrictions}}\par
\hyperref[what-to-wish-for]{Wishes, optimal use of, p.~\pageref*{what-to-wish-for}}\par
\hyperref[quest-artifacts]{Wishing for other roles' quest artifacts, carry bonuses, p.~\pageref*{quest-artifacts}}\par
\hyperref[wishing-restrictions]{Wishless conduct, refuse all, p.~\pageref*{wishing-restrictions}}\par
Wizard: \hyperref[the-roles]{kitten that won't share lunch, cloak of magic resistance from turn one, force bolt shatters potions, p.~\pageref*{the-roles}}; \hyperref[humans-and-elves]{of Yendor, the most persistent ex, p.~\pageref*{humans-and-elves}}; \hyperref[spending-slots-wisely]{dagger Expert opening, p.~\pageref*{spending-slots-wisely}}; \hyperref[the-wizards-tower]{of Yendor, never stops, p.~\pageref*{the-wizards-tower}}; \hyperref[the-gauntlet]{of Yendor, the eternal nuisance, p.~\pageref*{the-gauntlet}}\par
\hyperref[the-wizards-tower]{Wizard's Tower, three special levels, p.~\pageref*{the-wizards-tower}}\par
\hyperref[real-gem-prices]{Worthless glass, unicorn-safe junk, p.~\pageref*{real-gem-prices}}\par
\hyperref[feelings-and-sounds]{Wow! This makes you feel great!, magic fountain hit, p.~\pageref*{feelings-and-sounds}}\par
Wraith: \hyperref[a-note-on-wraiths]{corpse, gain an experience level, p.~\pageref*{a-note-on-wraiths}}; \hyperref[scroll-reverse-genocide]{reverse genocide, banquet, p.~\pageref*{scroll-reverse-genocide}}\par
\hyperref[deadly-mistakes]{Wrath of a god, prayer gone wrong, p.~\pageref*{deadly-mistakes}}\par
\hyperref[wresting]{Wresting, 1/121 final charge, p.~\pageref*{wresting}}\par

\par\smallskip{\normalsize\bfseries X}\par\smallskip

\hyperref[xans-and-fantastic-insects-x]{`x` xans and fantastic insects, p.~\pageref*{xans-and-fantastic-insects-x}}\par
\hyperref[xorns-x]{`X` xorn, phases through walls, p.~\pageref*{xorns-x}}\par
\hyperref[xans-and-fantastic-insects-x]{Xan, sting cripples your legs, p.~\pageref*{xans-and-fantastic-insects-x}}\par

\par\smallskip{\normalsize\bfseries Y}\par\smallskip

\hyperref[apelike-creatures-y]{`Y` apelike creatures, p.~\pageref*{apelike-creatures-y}}\par
\hyperref[lights-y]{`y` lights, p.~\pageref*{lights-y}}\par
\hyperref[acknowledgements]{YAFAP (Yet Another First Ascension Post), p.~\pageref*{acknowledgements}}\par
YASD: \hyperref[your-first-descent]{inevitability of, p.~\pageref*{your-first-descent}}; \hyperref[acknowledgements]{(Yet Another Stupid Death), p.~\pageref*{acknowledgements}}\par
\hyperref[major-demons]{Yeenoghu, attacks on sight, p.~\pageref*{major-demons}}\par
Yellow: \hyperref[light-bursts]{light, blinds 10d20 turns, p.~\pageref*{light-bursts}}; \hyperref[fungi-and-molds-f]{mold, stuns and poisons, p.~\pageref*{fungi-and-molds-f}}\par
Yellow dragon: \hyperref[a-note-on-dragons]{scale mail, stoning resistance bonus, p.~\pageref*{a-note-on-dragons}}; \hyperref[petrification-stoning]{scale mail, permanent stoning resistance, p.~\pageref*{petrification-stoning}}\par
Yeti: \hyperref[apelike-creatures-y]{cold resistance corpse, p.~\pageref*{apelike-creatures-y}}; \hyperref[useful-corpse-effects]{corpse, cold resistance, p.~\pageref*{useful-corpse-effects}}\par
\hyperref[dungeon-hazards-and-how-to-survive-them]{Your own pet, swapping places, p.~\pageref*{dungeon-hazards-and-how-to-survive-them}}\par

\par\smallskip{\normalsize\bfseries Z}\par\smallskip

\hyperref[zombies-z]{`Z` zombies, p.~\pageref*{zombies-z}}\par
\hyperref[zruties-z]{`z` zruty, three-attack brute, p.~\pageref*{zruties-z}}\par
\hyperref[room-types]{Zoo, wake them one at a time, p.~\pageref*{room-types}}\par
\hyperref[the-map-symbols]{Zorkmid, abbreviation zm, p.~\pageref*{the-map-symbols}}\par

\end{multicols}
```

:::


---

*You descend the stairs...*

---

### Acknowledgements
<!-- audit
2026-05-19:
- NetHack 1987, Fenlason -> Brouwer -> Stephenson lineage verified (Wikipedia, dat/history)
- DevTeam founders, Izchak Miller died 1994, Hack 1982 origin all verified
- WCST acronym is not expanded in the original Waterman file; Wheaton, IL distribution started 1991 (pdwaterman.com)
- Kevin Hugo is on the official 5.0 core team list (dat/history:314)
- nethackwiki.com returned 403, so wiki article counts and some spoiler-author attributions are unverified
-->

NetHack has been played, cursed at, loved, and documented since
1987. The game itself is the work of the NetHack DevTeam, a
loose collective of developers who have maintained one of the
longest-running continuously developed open source projects in existence. But the
documentation, the strategy, the collected wisdom about how to
actually survive the thing, that came from the players.

In the early days, knowledge spread through Usenet, on the
newsgroup **RGRN** (more formally, rec.games.roguelike.nethack).
Thousands
of players posted questions, argued about strategy, and slowly
assembled a shared body of knowledge about a game that refused to
explain itself. This was before wikis, before Reddit, before
Discord. If you wanted to know whether a cockatrice corpse could
be wielded as a weapon, you searched the RGRN archives and hoped
someone had asked before you. Someone usually had.

RGRN gave the community its vocabulary. A **YASD** (*Yet Another
Stupid Death*) is the post you make after dying to something you
should have known better than to do. A **YAFAP** (*Yet Another
First Ascension Post*) is the post you make when you finally win.
Both traditions persist today, in the wiki, on Reddit, in Discord.

Out of those conversations came the first spoiler files: plain-text
catalogs of every item, every monster, every interaction. Written
by hand, cross-referenced against the source code, and shared
freely.

This guide stands on their work. Specifically:

**Kevin Hugo** compiled the first comprehensive spoiler set for
NetHack 3.2.2, covering every item class, monster stat, spell
formula, and score calculation in methodical detail. **Dylan
O'Donnell** updated the entire set for 3.4.3, correcting, expanding,
and maintaining the files over several years. Together, the
Hugo/O'Donnell spoilers became the definitive reference: 38 files
covering potions, scrolls, wands, rings, amulets, tools, weapons,
armor, artifacts, food, monsters, spells, and more. The item data
tables throughout Parts Four and Five of this guide are verified
against their work. Published under BSD-like terms.

**Paul Waterman** wrote the WCST NetHack Spoilers (at Wheaton
College in 1991), a single sprawling document
that covered the entire game in a conversational, opinionated voice.
Where Hugo and O'Donnell wrote reference manuals, the WCST was
a travel guide. It told you not just what things did but what to do
about them. It was the original inspiration for the tone and
structure of this guide, though no text has been copied from it.

**Kate Nepveu** maintained steelypips.org, the web archive that
preserved the Hugo/O'Donnell spoilers, the RGRN community articles,
and her own excellent guides (including the Elbereth FAQ cited in
our traps chapter). Without Kate's patient archival work, much of
this material might have disappeared when Usenet faded.

The following **RGRN community authors** contributed articles,
FAQs, and guides that informed specific sections of this guide:

**David Damerell** wrote the Object Identification FAQ. **Kieron
Dunbar** wrote the wand identification guide. **Trevor Powell**
compiled the Instadeath Spoiler. **Arien Malec** wrote the Medusa
guide. **Matthew Lahut** wrote the prayer guide. **Boudewijn
Waijers** mapped all eight Sokoban variants. **Steven Bush**
calculated spellbook reading success rates. **Gregory Bond**
documented shopkeeper pricing formulas. **Dion Nicolaas**
cataloged the conducts. **David Goldfarb** wrote the air elemental
FAQ. **Hojita Discordia** documented XP value calculations.

And many others: Ray Chason, Pat Rankin, Geoduck, Topi Linkala,
Geoffrey Eadon, Roger Broadbent, Sebastian Haas, Jukka Lahtinen,
and the countless anonymous posters on the newsgroup who asked
"has anyone tried..." and then reported back.

**The [NetHack Wiki](https://nethackwiki.com/)** has been an
indispensable reference for this guide. Founded as "WikiHack" by
Sgeo in 2005, it migrated to its own domain in 2010 and now
contains over five thousand articles documenting every corner of
the game. Its creators and maintainers include Pasi Kallinen,
Drew Streib, Alex Smith, Shawn Moore, George Koehler, Tjr,
ZeroOne, and Ray Chason. The wiki's
[NetHack 5.0.0 page](https://nethackwiki.com/wiki/NetHack_5.0.0)
is the community's living changelog and was a major reference
for the 5.0 update of this guide.

**The public servers** where most NetHack is played today are
[nethack.alt.org](https://alt.org/nethack/) (the longest-running
public NetHack server, run by M. Drew Streib and Pasi Kallinen)
and [Hardfought](https://hardfought.org/) (run by K2, which also
hosts the major variants). Both are free to play and
log every ascension; the cause-of-death and ascension statistics
cited throughout this guide come from their public records (see
NAO's [top types of deaths](https://alt.org/nethack/topdeaths.html)).

**The [r/nethack](https://www.reddit.com/r/nethack/) community** on Reddit has kept NetHack discussion
alive for a new generation of players. Its moderators over the
years have maintained a welcoming space where veterans and newcomers
trade advice, share ascension stories, and argue about optimal wish
choices. The community's collective knowledge, passed along in
thousands of threads, has informed the practical advice throughout
this guide.

Above all, this guide exists because the game itself exists.
**[NetHack](https://www.nethack.org/)** has been developed since
1987 by the NetHack DevTeam, founded by Mike Stephenson, Izchak
Miller, and Janet Walz. Izchak Miller passed away in 1994; the
shopkeeper who bears his name in the Mines is a small measure of
how much his work meant. The source lives at
[github.com/NetHack](https://github.com/NetHack/NetHack).

The game itself descends from earlier roguelikes. **Hack** was
written by Jay Fenlason in 1982 as a class project at Lincoln-Sudbury
Regional High School, drawing on Toy and Wichman's *Rogue* (1980),
and extended by Andries Brouwer through the mid-1980s. NetHack
forked from Brouwer's Hack in 1987. Many of the most distinctive
NetHack monsters — including the **grid bug**, the orthogonal-only
critter whose name puns on both "insect" and "software bug" living
on a character-cell grid (with a likely nod to the bugs in the 1982
film *Tron*) — were already in Hack before NetHack inherited them.
The dungeon is older than the game.

The development was not always continuous. After version 3.4.3 in
December 2003, the DevTeam went quiet for twelve years: silent to
the public, working in private. The running community joke during
the gap was *The DevTeam is THINKING.* The dungeon was frozen.
New players descended into the same unchanging corridors that had
been killing people since 2003, writing new spoilers about a fixed
game, dying in the same newly-documented ways. The accumulated
community wisdom from those twelve silent years remained useful,
and the game was deep enough to sustain a decade of fresh analysis
without a single new line of code. Version 3.6 arrived in December
2015, and active development has continued since.

The current team, including Michael Allison, Ken Arromdee, David
Cohrs, Jessie Collet, Kevin Hugo, Pasi Kallinen, Ken Lorber, Dean
Luick, Patric Mueller, Pat Rankin, Derek S. Ray, Alex Smith, Mike
Stephenson, Janet Walz, Paul Winner, Bart House, and Warwick
Allison, has maintained and extended the game across nearly four
decades. Everything in these pages is downstream of their work.

All data in this guide has been verified against the current game
source code. Any errors are ours alone.

---

*A Traveler's Companion to the Mazes of Menace 5.0 Launch Edition,*<br>
*compiled by David Bau, using Claude 4.7 Opus to collate and check facts.*

*This work is licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
