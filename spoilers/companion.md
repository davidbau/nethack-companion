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

The Mazes have predecessors. Before this dungeon took its current form,
adventurers explored simpler places: a dungeon called Hack, and before
that the legendary Rogue, whose procedurally-generated corridors first
established what a dungeon could mean in the age of computing. Each
generation of explorers added to what the previous one learned, until
the Mazes became what they are today: one of the deepest, most thoroughly
documented, and most reliably fatal adventure destinations ever devised.
The knowledge in this guide is the inheritance of everything those
explorers found out, usually the hard way.

**A word of caution.** This guide will change how you experience the
Mazes forever. Once you know that a floating eye can paralyze you with
a glance, you can never un-know it. Once you learn what a cockatrice
corpse can do when wielded with gloves, the dungeon becomes a
different place. Some adventurers prefer the thrill of discovery over
the comfort of preparation. If that's you, close this guide now and
go learn things the hard way. There is real joy in that.

**Looking for the manual instead?** If you're just looking for game
commands, item lists, and mechanics without spoilers, you want the
**[Guide to the Mazes of Menace](../guidebook/)** instead. That's the
reference manual that comes with the game. This document is a
*strategic* guide. It assumes you already know how to play and want
to know how to *survive*.

But if you've died to one too many floating eyes you hit without
thinking, or you're tired of starving on dungeon level four thinking
the gods had abandoned you, read on. We'll do our best to keep
you alive.

---

## Table of Contents

**Part One: Before You Set Out**

1. [Choosing Your Expedition](#choosing-your-expedition) — Roles, races, and alignments
2. [What to Pack](#what-to-pack) — Starting equipment and early priorities
3. [Your First Descent](#your-first-descent) — Surviving the early dungeon

**Part Two: Reading the Terrain**

4. [The Lay of the Land](#the-lay-of-the-land) <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="#5a5a5a" stroke-width="1.1" style="vertical-align:-2px" aria-label="includes a map figure"><path d="M1 3 L5 2 L9 3.5 L13 2 L13 11 L9 12.5 L5 11 L1 12 Z"/><line x1="5" y1="2" x2="5" y2="11"/><line x1="9" y1="3.5" x2="9" y2="12.5"/></svg> — Rooms, corridors, and dungeon features (with map)
5. [Points of Interest](#points-of-interest) — Fountains, altars, thrones, and sinks
6. [Branches and Landmarks](#branches-and-landmarks) — The Mines, Sokoban, and beyond
7. [Traps and Hazards](#traps-and-hazards) — What the dungeon has in store for you
8. [Feelings and Sounds](#feelings-and-sounds) — Cryptic messages the dungeon uses to tell you what just happened

**Part Three: The Locals**

9. [A Field Guide to Dungeon Fauna](#a-field-guide-to-dungeon-fauna) — Monster classes at a glance
10. [What Actually Kills Adventurers](#what-actually-kills-adventurers) — Top-ten killers, bones-level hazards, mimics, dragons
11. [Dangerous Encounters](#dangerous-encounters) — Special abilities, instadeaths, and what to fear
12. [Making Friends](#making-friends) — Pets, taming, and peaceful coexistence

**Part Four: Gear and Provisions**

13. [A Practical Identification Strategy](#a-practical-identification-strategy) <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="#5a5a5a" stroke-width="1.1" style="vertical-align:-2px" aria-label="includes a flowchart figure"><rect x="2" y="1" width="10" height="3"/><rect x="2" y="5" width="10" height="3"/><rect x="2" y="9" width="10" height="3"/><line x1="7" y1="4" x2="7" y2="5"/><line x1="7" y1="8" x2="7" y2="9"/></svg> — Figuring out what you've found (with flowchart)
14. [Provisions and Dining](#provisions-and-dining) — Food, nutrition, and dining
15. [The Apothecary](#the-apothecary) — Potions and their many uses
16. [The Scroll Rack](#the-scroll-rack) — Scrolls, their effects, and confused reading
17. [Wands and Staves](#wands-and-staves) — Magical implements
18. [Rings and Amulets](#rings-and-amulets) — Jewelry, for better or worse
19. [Tools of the Trade](#tools-of-the-trade) — From pickaxes to magic lamps
20. [The Armory](#the-armory) — Weapons, armor, and hitting things
21. [Artifacts](#artifacts) — Legendary equipment and how to obtain it

**Part Five: The Craft of Adventuring**

22. [Divine Relations](#divine-relations) — Prayer, sacrifice, and altars
23. [The Art of Combat](#the-art-of-combat) — Hit probability, damage, and tactics
24. [Wishes and Wishing](#wishes-and-wishing) — Getting what you want
25. [Spellcasting](#spellcasting) — Magic for the studious adventurer
26. [Curses and How to Break Them](#curses-and-how-to-break-them)
27. [Luck and Fortune](#luck-and-fortune) — The hidden numbers that shape your fate

**Part Six: The Deep Dungeon**

28. [The Castle](#the-castle) — The gateway to Gehennom
29. [Gehennom](#gehennom) — A travel advisory
30. [The Ascension Kit](#the-ascension-kit) — What the winners actually carry
31. [The Ascension Run](#the-ascension-run) — Getting back out alive
32. [The Elemental Planes](#the-elemental-planes) — The final gauntlet

**Appendices**

33. [Advanced Controls](#advanced-controls) — Command counts, prefixes, and efficiency techniques
34. [Sokoban Solutions](#sokoban-solutions) — All eight level variants, solved
35. [Voluntary Challenges](#voluntary-challenges) — Conducts and self-imposed restrictions
36. [Shopping and Shopkeeper Pricing](#shopping-and-shopkeeper-pricing) — Commerce in the dungeon
37. [What Changed Since Last Time](#what-changed-since-last-time) — What's new in 5.0 vs 3.6.x, and what to do about it
38. [Acknowledgements](#acknowledgements) — Standing on the shoulders of giants

---

## Part One: Before You Set Out

---

### Choosing Your Expedition
<!-- audit 2026-05-18 #86: most role/race/alignment combos and starting gear claims verified vs u_init.c + role.c + attrib.c. Corrected: Elf "see invisible from the start" (no race grants it; sleep res is at XL 4 not 1); Knight code says fleeing-or-helpless not fleeing-or-peaceful (peaceful penalty is Samurai's giri); Cave Dweller starts with sling + flint, not "rocks for throwing"; Ranger also starts with +2 cloak of displacement; Wizard starts with cloak of magic resistance + wand + rings + scrolls + marker; Healer is immune to sickness (not "can see whether potions are safe"); added Knight intrinsic jumping; Ranger Stealth XL 7 / See Invis XL 15 (not "early"). v2 audit 2026-05-18 #46: two factual fixes and two beginner-affecting wisdom adjustments. (a) Healer paragraph: "convert them to fruit juice with an amethyst" — wrong, the amethyst converts BOOZE to fruit juice (potion.c:2161-2163). Sickness to fruit juice goes through the unicorn horn (potion.c:2151-2154). Reworded. (b) Knight starting lance is +1 not +0 (u_init.c:91-92 `{ LANCE, 1, ... }`). Fixed. (c) Cave Dweller "gain speed early" was misleading next to Samurai/Monk's true XL-1 speed — Cave Dweller's Fast is at XL 7 (attrib.c:37). Softened to "by mid-game" so a beginner picking a role doesn't expect XL-1 speed. (d) Closing recommendation "Mjollnir waiting at the first altar you can sacrifice on" — a cross-aligned altar won't deliver Mjollnir; clarified to "first co-aligned altar." Verified all 13 role alignments/race availabilities against role.c, intrinsic-by-XL tables against attrib.c, and all sacrifice-gift assignments. 0 other corrections. See companion-audit.md. -->

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

**Archeologist.** You start with a bullwhip, a pickaxe, and a tinning
kit. The pickaxe is the kit's quiet workhorse: it lets you dig through
walls and create your own escape routes from the very first level. The tinning kit lets you preserve corpses for
later. Archeologists are capable and flexible, though a bit fragile in
early combat. You begin knowing what all gems are, which is a nice
parlor trick and occasionally useful for unicorn negotiation.
*Alignment: Lawful or Neutral.*

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
simplicity is a virtue: fewer tools means fewer things to manage.
*Alignment: Lawful or Neutral.*

**Healer.** You begin with a stethoscope, healing potions, and poison
resistance. The stethoscope is remarkable: it lets you check a
monster's hit points and your own internal state. Healers are fragile
fighters, but their medical knowledge keeps them alive through
situations that would kill other roles. You're also **immune to
sickness**, so unknown potions of sickness become a free quaff-test
(and you can convert them to fruit juice by dipping a unicorn horn). *Alignment: Neutral.*

**Knight.** You start mounted on a saddled pony, with a +1 long sword
and a +1 lance among your gear. The pony is a decent combatant early
on and the basis of your unique trick: jousting from horseback with
the lance is devastating when it connects, though the lance is largely
useless on foot. As a Lawful character with a starting long sword, you
also have the best odds in the game at Excalibur. Dip your long sword
in a fountain at experience level 5+ and Knights get a 1-in-6 chance
per dip, far better than the 1-in-30 every other Lawful role faces.
Knights follow a code of conduct that imposes alignment penalties
for attacking fleeing or helpless monsters, so pick your fights
carefully. Knights also have intrinsic jumping, which lets you
reposition without spending an attack. *Alignment: Lawful.*

**Monk.** You fight best with bare hands and start with no weapon
at all. Monks gain martial arts abilities as they level, eventually
becoming formidable unarmed combatants. You start
with sleep resistance and see invisible, and you should avoid eating
meat if you want to maintain your spiritual discipline. One of the
more unusual roles, rewarding for experienced players.
*Alignment: Any.*

**Priest.** You start with a mace, four potions of holy water, and
the ability to intuitively sense whether items are blessed, cursed,
or uncursed, so you know on sight whether that cloak you just found
is safe to wear. Competent fighters with access to clerical spells.
Your first sacrifice gift is guaranteed: Demonbane (now a silver
mace), which aligns with your weapon skill — sacrifice early and
often. *Alignment: Any (matches your god).*

**Ranger.** You start with a bow, a generous supply of arrows, a
dagger, and a **+2 cloak of displacement** — one of the strongest
defensive starts in the game. You're unmatched as an early-game
ranged threat. Rangers gain Searching at XL 1, Stealth at XL 7,
and See Invisible at XL 15. Your elven racial option grants sleep
resistance at XL 4. If you enjoy picking off enemies from a
distance, this is your role. *Alignment: Neutral or Chaotic.*

**Rogue.** NetHack's thief class: lockpicking and stealthy
assassinations. You start with a short sword, six daggers for
throwing, leather armor, a lock pick, a sack, and a potion of
sickness (toss it at an enemy, or save it to coat any darts,
shuriken, or arrows you find — only missiles can be poisoned).
Your lock pick makes every locked door, chest, and box openable from
turn one. You get stealth from the beginning, which lets you walk up
to sleeping enemies without waking them, and your backstab ability
deals extra damage (+1 to +your level) when you hit a monster that's
fleeing or helpless. *Alignment: Chaotic.*

**Samurai.** You start with a katana, which is one of the better
one-handed weapons in the game, plus a wakizashi backup and a yumi
bow with arrows. Samurai get speed early and have a strong martial
kit overall. The katana's damage output carries you through the
early game with ease. *Alignment: Lawful.*

**Tourist.** You start with a Hawaiian shirt, a credit card, a
camera, and a truly absurd number of darts. Tourists have weak combat
and a fragile early game: this is the hardest of the standard roles.
The darts do train ranged skills fast, though, and the camera can
blind monsters in a pinch. A good role for players who have ascended
before and want a real challenge. *Alignment: Neutral.*

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
[Spellcasting](#spellcasting)). *Alignment: Neutral or Chaotic.*

#### The Races

Your race affects your starting attributes, maximum attributes, and
which intrinsics you begin with or can gain.

**Human.** You know what a human is. No infravision, no poison
resistance, no particular talents. On the bright side, every role is
open to you, and nobody in the dungeon singles you out for being one.
Perfectly serviceable.

**Dwarf.** Dwarves are sturdy and strong, with infravision (they can
see warm-blooded creatures in the dark). They're good fighters with
high Strength, Dex, and Con caps. Available for: Archeologist, Cave
Dweller, Valkyrie.

**Elf.** Elves start with infravision and gain sleep resistance at
XL 4. They're a bit more fragile than humans but have the highest
Int and Wis caps (20). Elf Priests and Wizards even get a free
musical instrument. Available for: Priest, Ranger, Wizard.

**Gnome.** Gnomes get infravision and a slightly higher Int cap (19).
They're small but resourceful. Available for: Archeologist, Cave
Dweller, Healer, Ranger, Wizard.

**Orc.** Orcs get infravision and poison resistance, which is
genuinely useful. Stat caps run lower than human (Str 18/50, Cha 16,
Wis 16). Humans, elves, and dwarves are race-hostile to orcs
(including shopkeepers, priests, and watchmen); other orcs aren't
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

For your first game: **Valkyrie, Human or Dwarf.** Strong
combat, cold resistance, and Mjollnir waiting at the first
co-aligned altar you can sacrifice on. It's the closest thing to
an easy mode the Mazes offer, which is to say it's still very
hard.

---

<!-- audit 2026-05-18 #170 (re-audit 2026-05-18 v2 #36): qualitative section, no numeric claims to refute. Spot-checked: tripe rations are "dog food" for typical PCs (eat.c:2138-2145) but orcs and carnivores enjoy them (eat.c:2132-2136); altar blessed/cursed flash at do.c:363-389 (amber/black) sets bknown; pets avoid cursed items per dogmove.c:535-536, 1065-1067; touchstone gem-ID at apply.c:2658-2696; floating-eye paralysis at uhitm.c:5853, 6022. v2 also confirmed Burdened status label at botl.c:12, food ration weight/nutrition at objects.h:1110, role inventory tables at u_init.c. 0 corrections. See companion-audit.md. -->
### What to Pack

Any good travel guide will tell you what to bring. Ours has the
awkward job of telling you that you don't get to choose. Your
starting kit is determined by your role, and you'll descend with
whatever your role provides, no more.

What you *can* choose is what to prioritize once you're down there.
Every role starts with equipment suited to its strengths. The
important thing isn't what's in your pack on turn one; it's knowing
what to scavenge from the first few levels to shore up your
weaknesses.

#### The Early Shopping List

No matter your role, here's what you should be looking for:

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

**Restraint.** New adventurers pick up everything they find. Veterans
pick up everything they need. The difference is about forty pounds
and the ability to outrun a gnome lord. If your status line reads
"Burdened," you're carrying more than you can use.

---

### Your First Descent

You step down the stairs. The air is cool and damp. A corridor
stretches before you, branching into darkness. Your starting pet
trots along behind you.

Welcome to the dungeon.

The first few levels of the Mazes are designed to ease you in, which
is a relative term. Monsters are weaker, but you are too. Your gear is
minimal, your hit points are low, and you don't yet have the
resistances that make the mid-game survivable. More experienced
adventurers will tell you that levels one through five are where the
most characters die, not because the threats are the greatest, but
because you have the fewest resources to deal with them.

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
the ground. The exceptions: you can always safely eat food rations,
lembas wafers, cram rations, and fruits. Lichen corpses are safe and
never rot. Lizard corpses are safe, never rot, and cure
petrification. Always carry one if you can.

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
pray about once every 300-500 turns, and praying at the wrong time
(when your god is angry, when you're in Gehennom, or when you've
prayed too recently) can make things much worse. Think of prayer as an
emergency button with a cooldown. Don't waste it on minor problems
(see [Divine Relations](#divine-relations) for the full mechanics).

**Rule 5: Explore thoroughly but move purposefully.** Every turn you
spend in the dungeon costs nutrition. If you stand around for hundreds
of turns, you'll starve. But rushing past rooms means missing
items you need. The sweet spot is to explore each level fairly
completely (check rooms, open doors, look for hidden passages) but
don't grind. When you've found what the level has to offer, move on.

**Rule 6: Chase the big three.** The short list of acquisitions that
keep you alive through the whole run is **magic resistance**,
**reflection**, and **poison resistance**, plus a **lizard corpse**
in your pack for petrification emergencies. Everything else is
luxury. Get these as early as you can — they decide which late-game
fights are survivable.

#### Things That Kill You (And How Not to Let Them)

Here's a short list of common early deaths and how to prevent them:

**Starvation.** Eat when you're Hungry (the status message), not
when you're Weak or Fainting. If you're Fainting, pray immediately.
Pick up every food ration you find.

**Floating eyes.** They're the `e` on the map. Small, blue, and
seemingly harmless. If you hit one in melee, you'll be paralyzed, and
every monster in the vicinity will take free shots at your frozen body.
Use ranged attacks, or just walk around them. They don't pursue you.

**Rotted corpses.** If you eat a corpse that's been on the ground too
long, you'll get food poisoning, which is lethal without treatment.
Eat corpses fresh — within about 50 turns of the kill for a guaranteed-safe meal. Past that, the rot roll turns random; past ~150 turns an uncursed corpse is certainly tainted.
If you do get food poisoning, pray immediately.

**Falling down stairs while overburdened.** If you're carrying too
much, taking the stairs can make you tumble for 1–3 HP. Annoying
rather than dangerous, but a habit worth avoiding — drop items
before descending or manage your inventory.

**Killer bees.** They come in swarms, they're fast, and in the early
game, a group of them can overwhelm you. If you see one bee, expect
more. Use a corridor to fight them one at a time.

**Your own pet.** If your pet is between you and a narrow corridor,
you might accidentally swap places with it repeatedly instead of
moving. Worse, if you attack it (because you got confused or forgot
it was there), you lose alignment and trust. Be aware of where your
pet is.

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
or — failing those — you can `#force` the issue with a weapon you
don't mind breaking. An orcish dagger off the first orc you kill is
a perfect tool (pet-test it first: could be cursed). The contents aren't guaranteed
to change your run, but finding a stack of healing potions on level
4 before you've learned the hard way how much you need them is the
dungeon's frequent act of goodwill.

---

## Part Two: Reading the Terrain

---

### The Lay of the Land
<!-- audit 2026-05-18 #81: 20 numeric claims verified against dungeon.lua + medusa-*.lua + castle.lua + minetn-*.lua. DoD 25-30 levels; Gnomish Mines DL 2-4; Sokoban-up off Oracle; 4 levels × 2 variants; Oracle DL 5-9; Big Room 40% chance DL 10-12; Rogue DL 15-18; Mine's End 3 variants with luckstone; Quest portal DL 11-16 (chainlevel oracle base=6 range=2); Fort Ludios DL 18-22 portal; Medusa DL ~21-25; Castle DL ~27 bottom of DoD; 4 Medusa layouts; Perseus loot 75/50/25/50; 1-in-7 orcish Minetown. 0 corrections. See companion-audit.md. -->

The Mazes are procedurally generated. No two visits are quite the
same. But the dungeon follows patterns, and understanding those
patterns is the first step toward navigating them effectively.

#### The Big Picture

Before we talk about what the symbols mean, here's the overall
shape of the place. The dungeon is a branching tree with a main
trunk (the Dungeons of Doom) and several side branches. The
diagram nearby shows the full layout. Knowing where you are in this
tree helps you plan your route and know what's coming.

The **Dungeons of Doom** form the upper half, roughly levels 1
through 27. Along the way you'll find branches leading to the
**Gnomish Mines** (luckstone, shops), **Sokoban** (a prize at the
top), your **Quest** (your role's special dungeon), and optionally
**Fort Ludios** (a vault full of gold). The main trunk ends at
**The Castle**, which guards the entrance to Gehennom.

**Gehennom** is the lower half: maze levels, demon lords, and
the ultimate objective: the **Amulet of Yendor** at the very
bottom in Moloch's Sanctum. Once you have it, you climb all the
way back up and pass through the **Elemental Planes** to reach
the **Astral Plane**, where your god awaits your offering.

<!-- DMAP-BEGIN -->
<div><figure style="margin: 1.5em 0; text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 611" role="img" aria-label="Dungeons of Doom map" style="display:block;margin:0 auto;max-width:760px;width:100%;height:auto;font-family:'EB Garamond','Garamond','Georgia',serif;"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker></defs><line x1="380" y1="55" x2="380" y2="611" stroke="#B5651D" stroke-width="2.5" fill="none"/><rect x="40" y="0" width="680" height="39" rx="4" fill="#B5651D"/><text x="380" y="26" font-size="22" font-weight="600" fill="#fff" text-anchor="middle" letter-spacing="0.08em">DUNGEONS OF DOOM</text><line x1="150" y1="140" x2="150" y2="246" stroke="#5B8E3A" stroke-width="2" fill="none"/><line x1="630" y1="166" x2="630" y2="194" stroke="#B58A1A" stroke-width="2" fill="none"/><line x1="630" y1="305" x2="630" y2="343" stroke="#3B6FA0" stroke-width="2" fill="none"/><rect x="290" y="55" width="180" height="40" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="72" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Dlvl 1 — Entry</text><text x="380" y="89" font-size="12" font-style="italic" fill="#555" text-anchor="middle">up-stair to exit</text><rect x="60" y="108" width="180" height="32" rx="6" fill="#E8F4DC" stroke="#5B8E3A" stroke-width="1.5"/><text x="150" y="129" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Gnomish Mines</text><rect x="60" y="168" width="180" height="40" rx="6" fill="#E8F4DC" stroke="#5B8E3A" stroke-width="1.5"/><text x="150" y="185" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Minetown</text><text x="150" y="202" font-size="12" font-style="italic" fill="#555" text-anchor="middle">shops, temple</text><rect x="60" y="246" width="180" height="40" rx="6" fill="#E8F4DC" stroke="#5B8E3A" stroke-width="1.5"/><text x="150" y="263" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Mine's End</text><text x="150" y="280" font-size="12" font-style="italic" fill="#555" text-anchor="middle">luckstone</text><rect x="290" y="163" width="180" height="40" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="180" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">The Oracle</text><text x="380" y="197" font-size="12" font-style="italic" fill="#555" text-anchor="middle">paid hints</text><rect x="540" y="126" width="180" height="40" rx="6" fill="#FFF4CC" stroke="#B58A1A" stroke-width="1.5"/><text x="630" y="143" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Sokoban prize</text><text x="630" y="160" font-size="12" font-style="italic" fill="#555" text-anchor="middle">bag of holding/amulet of reflection</text><rect x="540" y="194" width="180" height="32" rx="6" fill="#FFF4CC" stroke="#B58A1A" stroke-width="1.5"/><text x="630" y="215" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Sokoban entry</text><rect x="290" y="269" width="180" height="32" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="290" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Quest portal</text><rect x="540" y="265" width="180" height="40" rx="6" fill="#DDE9F5" stroke="#3B6FA0" stroke-width="1.5"/><text x="630" y="282" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Quest entry</text><text x="630" y="299" font-size="12" font-style="italic" fill="#555" text-anchor="middle">your role's dungeon</text><rect x="540" y="343" width="180" height="40" rx="6" fill="#DDE9F5" stroke="#3B6FA0" stroke-width="1.5"/><text x="630" y="360" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Quest goal</text><text x="630" y="377" font-size="12" font-style="italic" fill="#555" text-anchor="middle">★ Bell of Opening, role artifact</text><rect x="290" y="329" width="180" height="32" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="350" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Big Room (40%)</text><rect x="290" y="389" width="180" height="32" rx="6" fill="#FAF3E0" stroke="#B5651D" stroke-width="1.5"/><text x="380" y="410" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Rogue Level</text><rect x="60" y="420" width="180" height="40" rx="6" fill="#FFD966" stroke="#B5891A" stroke-width="1.5"/><text x="150" y="437" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Fort Ludios</text><text x="150" y="454" font-size="12" font-style="italic" fill="#555" text-anchor="middle">vault of gold</text><rect x="290" y="479" width="180" height="32" rx="6" fill="#B8D4F0" stroke="#2E5C8E" stroke-width="1.5"/><text x="380" y="500" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Medusa's Island</text><rect x="230" y="539" width="300" height="58" rx="8" fill="#FFFFFF" stroke="#B5891A" stroke-width="2.5"/><text x="380" y="565" font-size="17" font-weight="600" fill="#1f2933" text-anchor="middle">THE CASTLE</text><text x="380" y="582" font-size="14" font-style="italic" fill="#7A5A0A" text-anchor="middle">wand of wishing</text><line x1="380" y1="124" x2="240" y2="124" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><line x1="380" y1="210" x2="540" y2="210" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><line x1="470" y1="285" x2="540" y2="285" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><line x1="380" y1="440" x2="240" y2="440" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><text x="275" y="120" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">down</text><text x="500" y="206" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">up</text><text x="505" y="281" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">portal</text><text x="275" y="436" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">portal</text><circle cx="380" cy="124" r="4" fill="#B5651D"/><circle cx="380" cy="210" r="4" fill="#B5651D"/><circle cx="380" cy="440" r="4" fill="#B5651D"/><circle cx="380" cy="104.0" r="4" fill="#B5651D"/><circle cx="380" cy="114.0" r="4" fill="#B5651D"/><circle cx="150" cy="149.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="159.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="217.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="227.0" r="4" fill="#5B8E3A"/><circle cx="150" cy="237.0" r="4" fill="#5B8E3A"/><circle cx="380" cy="134.0" r="4" fill="#B5651D"/><circle cx="380" cy="144.0" r="4" fill="#B5651D"/><circle cx="380" cy="154.0" r="4" fill="#B5651D"/><circle cx="630" cy="175.0" r="4" fill="#B58A1A"/><circle cx="630" cy="185.0" r="4" fill="#B58A1A"/><circle cx="380" cy="220.0" r="4" fill="#B5651D"/><circle cx="380" cy="230.0" r="4" fill="#B5651D"/><circle cx="380" cy="240.0" r="4" fill="#B5651D"/><circle cx="380" cy="250.0" r="4" fill="#B5651D"/><circle cx="380" cy="260.0" r="4" fill="#B5651D"/><circle cx="630" cy="314.0" r="4" fill="#3B6FA0"/><circle cx="630" cy="324.0" r="4" fill="#3B6FA0"/><circle cx="630" cy="334.0" r="4" fill="#3B6FA0"/><circle cx="380" cy="310.0" r="4" fill="#B5651D"/><circle cx="380" cy="320.0" r="4" fill="#B5651D"/><circle cx="380" cy="370.0" r="4" fill="#B5651D"/><circle cx="380" cy="380.0" r="4" fill="#B5651D"/><circle cx="380" cy="430.0" r="4" fill="#B5651D"/><circle cx="380" cy="450.0" r="4" fill="#B5651D"/><circle cx="380" cy="460.0" r="4" fill="#B5651D"/><circle cx="380" cy="470.0" r="4" fill="#B5651D"/><circle cx="380" cy="520.0" r="4" fill="#B5651D"/><circle cx="380" cy="530.0" r="4" fill="#B5651D"/></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 681" role="img" aria-label="Gehennom map" style="display:block;margin:0 auto;max-width:760px;width:100%;height:auto;font-family:'EB Garamond','Garamond','Georgia',serif;"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker></defs><line x1="380" y1="0" x2="380" y2="39" stroke="#B5651D" stroke-width="2.5" fill="none"/><line x1="380" y1="0" x2="380" y2="625" stroke="#A14A3F" stroke-width="2.5" fill="none"/><rect x="40" y="0" width="680" height="39" rx="4" fill="#A14A3F"/><text x="380" y="26" font-size="22" font-weight="600" fill="#fff" text-anchor="middle" letter-spacing="0.08em">GEHENNOM</text><line x1="150" y1="288" x2="150" y2="306" stroke="#6B4E96" stroke-width="2" fill="none"/><rect x="290" y="53" width="180" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="70" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Valley of the Dead</text><text x="380" y="87" font-size="12" font-style="italic" fill="#555" text-anchor="middle">Gehennom's entrance</text><rect x="290" y="141" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="162" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Asmodeus's Lair</text><rect x="290" y="191" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="212" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Juiblex's Swamp</text><rect x="290" y="251" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="272" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Baalzebub's Lair</text><rect x="60" y="248" width="180" height="40" rx="6" fill="#E3D8F0" stroke="#6B4E96" stroke-width="1.5"/><text x="150" y="265" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Vlad the Impaler</text><text x="150" y="282" font-size="12" font-style="italic" fill="#555" text-anchor="middle">★ Candelabrum</text><rect x="60" y="306" width="180" height="32" rx="6" fill="#E3D8F0" stroke="#6B4E96" stroke-width="1.5"/><text x="150" y="327" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Vlad's Tower</text><rect x="290" y="351" width="180" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="368" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Orcus Town</text><text x="380" y="385" font-size="12" font-style="italic" fill="#555" text-anchor="middle">Wand of Orcus · magic lamp/marker</text><rect x="290" y="419" width="180" height="32" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="440" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Wizard's Tower</text><rect x="290" y="469" width="180" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="380" y="486" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Wizard of Yendor</text><text x="380" y="503" font-size="12" font-style="italic" fill="#555" text-anchor="middle">★ Book of the Dead</text><rect x="230" y="567" width="300" height="58" rx="8" fill="#2D2D2D" stroke="#FFC857" stroke-width="2.5"/><text x="380" y="593" font-size="17" font-weight="600" fill="#FFC857" text-anchor="middle">Moloch's Sanctum</text><text x="380" y="610" font-size="14" font-style="italic" fill="#FFE680" text-anchor="middle">the Amulet of Yendor</text><line x1="380" y1="322" x2="240" y2="322" stroke="#5a5a5a" stroke-width="1.5" marker-end="url(#arr)" fill="none"/><text x="275" y="318" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">up</text><circle cx="380" cy="322" r="4" fill="#A14A3F"/><circle cx="380" cy="102.0" r="4" fill="#A14A3F"/><circle cx="380" cy="112.0" r="4" fill="#A14A3F"/><circle cx="380" cy="122.0" r="4" fill="#A14A3F"/><circle cx="380" cy="132.0" r="4" fill="#A14A3F"/><circle cx="380" cy="182.0" r="4" fill="#A14A3F"/><circle cx="380" cy="232.0" r="4" fill="#A14A3F"/><circle cx="380" cy="242.0" r="4" fill="#A14A3F"/><circle cx="380" cy="292.0" r="4" fill="#A14A3F"/><circle cx="380" cy="302.0" r="4" fill="#A14A3F"/><circle cx="380" cy="312.0" r="4" fill="#A14A3F"/><circle cx="150" cy="297.0" r="4" fill="#6B4E96"/><circle cx="380" cy="332.0" r="4" fill="#A14A3F"/><circle cx="380" cy="342.0" r="4" fill="#A14A3F"/><circle cx="380" cy="400.0" r="4" fill="#A14A3F"/><circle cx="380" cy="410.0" r="4" fill="#A14A3F"/><circle cx="380" cy="460.0" r="4" fill="#A14A3F"/><circle cx="380" cy="518.0" r="4" fill="#A14A3F"/><circle cx="380" cy="528.0" r="4" fill="#A14A3F"/><circle cx="380" cy="538.0" r="4" fill="#A14A3F"/><circle cx="380" cy="548.0" r="4" fill="#A14A3F"/><circle cx="380" cy="558.0" r="4" fill="#A14A3F"/><line x1="380" y1="631" x2="380" y2="681" stroke="#5B8E3A" stroke-width="2.5" stroke-dasharray="7,5" fill="none"/><text x="400" y="661" font-size="15" font-weight="600" font-style="italic" fill="#5B8E3A">now go <tspan style="font-weight:800;font-size:17px">ALL</tspan> the way back up...</text></svg><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 299" role="img" aria-label="Elemental Planes and Ascension" style="display:block;margin:0 auto;max-width:760px;width:100%;height:auto;font-family:'EB Garamond','Garamond','Georgia',serif;"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker></defs><rect x="40" y="0" width="680" height="39" rx="4" fill="#5D3C8E"/><text x="380" y="26" font-size="22" font-weight="600" fill="#fff" text-anchor="middle" letter-spacing="0.08em">THE ELEMENTAL PLANES</text><rect x="68" y="89" width="120" height="40" rx="6" fill="#E8DDC8" stroke="#8B6F47" stroke-width="1.5"/><text x="128" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Earth</text><rect x="236" y="89" width="120" height="40" rx="6" fill="#E0F4FA" stroke="#3B9FA8" stroke-width="1.5"/><text x="296" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Air</text><rect x="404" y="89" width="120" height="40" rx="6" fill="#FAD7C0" stroke="#A14A3F" stroke-width="1.5"/><text x="464" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Fire</text><rect x="572" y="89" width="120" height="40" rx="6" fill="#DDE9F5" stroke="#3B6FA0" stroke-width="1.5"/><text x="632" y="115" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Water</text><rect x="260" y="179" width="240" height="42" rx="6" fill="#D8C6F0" stroke="#5D3C8E" stroke-width="1.5"/><text x="380" y="197" font-size="15" font-weight="600" fill="#1f2933" text-anchor="middle">Astral Plane</text><text x="380" y="213" font-size="12" font-style="italic" fill="#555" text-anchor="middle">three altars · pick yours</text><rect x="230" y="239" width="300" height="50" rx="10" fill="#FFE680" stroke="#B5891A" stroke-width="2.5"/><text x="380" y="262" font-size="18" font-weight="700" fill="#7A5A0A" text-anchor="middle" letter-spacing="0.1em">ASCENSION</text><text x="380" y="281" font-size="11" font-style="italic" fill="#7A5A0A" text-anchor="middle">offer the Amulet at your altar</text><path d="M 380 39 C 380 53 128 53 128 67 L 128 89" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><line x1="188" y1="109" x2="236" y2="109" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><text x="212" y="105" font-size="11" font-style="italic" fill="#5a5a5a" text-anchor="middle">portals</text><line x1="356" y1="109" x2="404" y2="109" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><line x1="524" y1="109" x2="572" y2="109" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><path d="M 632 129 C 632 143 380 143 380 157 L 380 179" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/><line x1="380" y1="221" x2="380" y2="239" stroke="#5a5a5a" stroke-width="1.5" fill="none" marker-end="url(#arr)"/></svg><figcaption style="font-style: italic; color: #5a5a5a; font-size: 0.9em; margin-top: 0.5em;">Branches extend left and right of the main trunk. Pearls (small colored dots) indicate the approximate number of intervening dungeon levels. ★ marks the three Invocation items (Bell of Opening, Candelabrum, Book of the Dead) needed to enter Moloch's Sanctum and claim the Amulet.</figcaption></figure></div>
<!-- DMAP-END -->

The typical trip: go down through the Dungeons, detour into the
Mines for a luckstone and Minetown's shops, clear Sokoban for a
prize, do your Quest, reach the Castle, descend through Gehennom
to get the Amulet, then climb all the way back up and through the
Planes. Simple enough on paper. Surviving it is another matter.

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
| `{`      | Fountain                      |
| `_`      | Altar                         |
| `\`      | Throne                        |
| `#`      | Sink                          |
| `^`      | Trap (once revealed)          |
| `@`      | You (or a human-type monster) |

Letters represent monsters: `d` for dogs, `D` for dragons, `Z` for
zombies. Colors help distinguish within a class: a red `D` is a red
dragon, while a gray `D` is a gray dragon (see
[A Field Guide to Dungeon Fauna](#a-field-guide-to-dungeon-fauna)).

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
| `$`    | Gold               |

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

**Throne rooms.** A room with a throne (`\`) and usually surrounded
by monsters. Sitting on the throne has random effects, sometimes
wonderful, sometimes terrible. See
[Points of Interest](#points-of-interest).

**Zoos.** A room packed with sleeping monsters and gold. They wake
not from opening the door (which is silent) but from the noise of
you fighting the first few. Fight from the doorway so they wake and
approach one or two at a time, not all at once.

**Barracks.** A room full of soldiers. They're organized and armed,
but they're also carrying good equipment. Worth clearing if you can
handle the fight.

**Beehives.** A room full of killer bees and royal jelly. The bees
are dangerous in numbers, but royal jelly is excellent food.

**Themed rooms.** New in 5.0 and the most visible
change to ordinary level generation: scattered through the
Dungeons of Doom, you'll occasionally walk into rooms that
aren't shops, aren't zoos, and aren't anything else from the
list above, but are also clearly not random. They're called
**themed rooms**, and there are dozens of them. Some have
unusual *shapes* (L-shaped, T-shaped, S-shaped, circular,
cross-shaped, four-leaf-clover-shaped, with pillars, with a
room-inside-a-room). Some have unusual *contents* (a buried-
treasure cache; a buried-zombies field that wakes up when
disturbed; a small massacre of statues and old corpses; a
mausoleum; a teleportation hub of stacked traps; a "fake
Delphi" room with a non-Oracle pretending to be one; a garden;
a spider nest; an ice room; a cloud room; a boulder room).

The interesting ones for the player:

- **Light source rooms.** They reliably contain a usable lit
  candle, lantern, or lamp. Free torches.
- **Buried treasure.** The floor needs digging, but the haul
  is real. A pick-axe earns its weight here.
- **Massacre / mausoleum.** Leave a few corpses for sacrifice.
  Old corpses sometimes carry surprises (a wraith corpse for the
  level boost is the famous one).
- **Spider nest, buried zombies, teleportation hub.** These
  are traps in everything but name. The encounter scales with
  level difficulty, so what looks innocuous on Dlvl 4 is rough
  on Dlvl 18. Recognize the pattern, retreat, prepare, return.
- **Fake Delphi.** The "Oracle" inside is just a regular human.
  Don't pay for advice.
- **Light-and-frame rooms (pillars, room-in-a-room, blocked
  center).** Tactically excellent for setting up Elbereth
  squares or anchoring a polearm fight.

Themed rooms are mixed in with ordinary rooms; you can have
several on a single level. They make the early dungeon less
predictable in a friendly way: more terrain types to fight in,
more item discovery, and the occasional educational ambush.

**A room full of one kind of monster is almost certainly a themed
room, not a coincidence.** Themed rooms have above-average monster
density concentrated around a single type, so any room that looks
curated deserves more respect than a random room of equivalent
apparent difficulty. Retreat, assess, and enter with a plan
rather than a direction.

---

### Points of Interest
<!-- audit 2026-05-17 #5: 40+ claims verified, 5 corrected (throne identify "up to 5" → 1-4 or all; sink polymorph message; rotten "fruit" → slime molds; "less" → "lesser"; sink-kick missing amorous demon outcome). See companion-audit.md. -->

Not everything interesting in the dungeon is trying to kill you.
Scattered throughout the levels are fixtures that reward the
curious, and occasionally punish them. Learning what to do (and what
*not* to do) with each of these is a rite of passage.

#### Fountains `{`

Ah, fountains. That gentle bubbling sound has lured more adventurers
to their doom than any trap. Every experienced player has a fountain
story: the time they summoned a water demon on dungeon level 3, the
time they quaffed and got a wish, the time snakes poured out of
the basin.

**Quaffing from a fountain** is a slot machine with these reels:

| Outcome         | Effect                                                |
| --------------- | ----------------------------------------------------- |
| Wish granted    | A water demon appears and grants a wish (rare, ~1/30, and falling off with depth — practically zero past DLvl 20) |
| Water demon     | A hostile water demon appears                         |
| Healing         | You regain hit points                                 |
| Attribute boost | A random attribute increases                          |
| Attribute loss  | A random attribute decreases                          |
| Water moccasin  | Snakes appear                                         |
| See invisible   | You gain the ability to see invisible creatures       |
| Nothing         | "The water is cool and refreshing"                    |

Most of the time, nothing happens. Sometimes something wonderful
happens. And sometimes a water demon appears and reminds you that
curiosity has a body count.

**Dipping in a fountain** is a different gamble, and one that Lawful
characters should know by heart. If you're at least experience level
5, dipping a long sword may transform it into Excalibur, one of the
finest weapons in the dungeon. Knights get a generous 1/6 chance per
dip; everyone else gets a meager 1/30. Otherwise, dipping can rust
your gear, summon hostile water creatures, or occasionally bless
the dipped item.

The conventional wisdom: if you're a lawful Knight carrying a long
sword, dip in every fountain you see until Excalibur appears. Other
lawful characters should try too, but pack patience. And if you're
not lawful? Walk past the fountain. It has nothing for you but wet
boots and regret.

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
before wearing.

**Sacrificing monster corpses on an altar** deepens your relationship
with your god. The corpse must be fresh (stale sacrifices are an
insult) and the bigger the monster, the more your god is impressed.
Sacrifice enough and your deity may reward you with an artifact
weapon aligned to your cause. See [Divine Relations](#divine-relations)
for the full theology.

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
strong enough to survive the worst row of that table, and ideally
when your luck is positive (for a shot at the wish). Even when
nothing happens, the throne may vanish in a puff of logic, so
you might get several tries or none at all. (Vlad's throne in
the Tower is special: it never vanishes without granting a wish
first.)
<!-- Throne mechanics: src/sit.c throne_sit_effect(), rnd(6)>4 for 1/3
     activation, rnd(13) for effect, !rn2(3) for vanishing.
     Vlad's throne: special_throne_effect(), cases 1-4 grant wish and
     destroy throne, cases 5-13 are negative but throne survives. -->

#### Sinks `#`

Sinks are the dungeon's most underrated identification tool.

**Kicking a sink** can shake loose a ring (useful!), summon a black
pudding (terrifying!), summon an *amorous demon* posing as "the dish
washer" (the same incubus/succubus as [a seduction
encounter](#seduction) — careful!), or just stub your toe. Each non-stub outcome fires at most
once per sink. Worth a kick in the early game if you can handle what
comes out.

**Pouring potions down a sink** (by dipping) produces telltale
effects — a clever way to narrow down potion identities without
risking a sip. Five potions print unique sink-only messages:

| Sink message                                                 | Potion             |
| ------------------------------------------------------------ | ------------------ |
| *"The sink transforms into a fountain/throne/altar!"* (or *"The sink vanishes."*) | polymorph (destroys the sink) |
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
free:

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

---

### Branches and Landmarks

The branch diagram we showed earlier gives the shape of the dungeon,
but it doesn't tell you what to actually do when you arrive. Here's
a more practical tour, in roughly the order you'll visit these places.

#### The Gnomish Mines
<!-- audit 2026-05-18 #124 (re-audit 2026-05-18 v2 #11): clean audit, no substantive corrections. Mines branch DL 2-4 (dungeon.lua:14-19), 7 Minetown variants with 1-in-7 being Orcish Town (minetn-1.lua), all three Mine's End layouts guarantee a not-cursed luckstone (minend-{1,2,3}.lua). Race-peaceful gnomes/dwarves for gnomish PCs via role.c:654 lovemask. Note: minend-1.lua:59 also places a fake-luckstone mimic (appear_as="obj:luckstone") near the real one — players should BUC-test before grabbing. The v2 sub-agent noted minefill.lua:36-44 places one gnome lord per level plus a random-humanoid roll that can rarely produce a mind flayer; an attempt to add that note to the prose introduced jargon ("minesflayer") and stat-dump phrasing, and was reverted to preserve the original conversational intro. See companion-audit.md. -->


The entrance appears somewhere around dungeon levels 2 through 4, as
a downward staircase. You'll know you're in the Mines because the
walls become rough stone and the corridors get irregular.

The Mines are populated primarily by gnomes, dwarves, and the
occasional dwarf lord. If you're playing a gnomish character, most
of them will be peaceful, which makes the Mines a relatively
comfortable detour. Everyone else will need to fight through a
modest but steady stream of hostile gnomes.

**Minetown** appears a few levels into the Mines. Usually it's a small
settlement with shops and a temple, and it's worth visiting early.
The shops let you sell unwanted items for gold and buy useful gear.
The temple has an altar (check the alignment) and a resident priest.
If the altar matches your alignment, you've found a safe place to
identify items by dropping them on it. The Minetown priest is also
the cheapest source of intrinsic AC bonuses in the game — donating
500 zorkmids at low XL stacks each visit (see
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
for the rest of the game. (One layout variant also seeds a **fake
luckstone mimic** disguised as a luckstone — BUC-test what you
pick up before relying on it.)

#### Sokoban

The entrance staircase appears somewhere around dungeon levels 6
through 10 (one level below the Oracle), and it goes up. Sokoban is a set of
four puzzle levels where you push boulders onto holes or into place
to open a path. No teleport works here, and you can't dig down off
the entrance level (its floor is reinforced).

The puzzles are fixed (two variants per level, randomly chosen).
<!-- audit 2026-05-18 #111: "break it ... by force-fighting it" is wrong. Force-fighting a bare boulder is harmless per hack.c:2287, 2318-2321 ("you harmlessly attack the boulder"). The cheat path is digging with a wielded pick-axe/mattock (hack.c:2269-2275). Reworded to fracture-via-striking/earth-scroll/polymorph and added the pick-axe caveat. Confirmed all other Sokoban claims: Oracle base 5-9 + Sokoban one above = entrance dlvl 6-10 (dungeon.lua:21-24, 60-66); 4 levels × 2 variants each; noteleport flag; sokoban_guilt() calls at hack.c:307 (squeeze), zap.c:5555 (fracture by striking), zap.c:1710 (polymorph), read.c:1951 (earth scroll); each triggers change_luck(-1) + u.uconduct.sokocheat (trap.c:7039-7054); conduct reported only when branch entered (insight.c:2215-2228). Levitation/flying free of penalty (hack.c:415-425). v2 audit 2026-05-18 #24: two fixes. (a) "Can't dig through the floors" was too broad — hardfloor is set only on the entrance level (soko4-{1,2}.lua:38,7); interior soko levels would let you dig down, but only onto another soko level (Sokoban is a single-direction up-branch). Narrowed to "can't dig down off the entrance level." (b) "Levitation or flying over unfinished pits is free of penalty" was misleading because hack.c:415-425 rejects boulder pushes while levitating ("you don't have enough leverage"), so levitation prevents Sokoban progress entirely. Split: flying is the useful tactic; levitation is no penalty but also no progress. See companion-audit.md. -->

Each level has exactly one correct solution. If you push a boulder
into a corner where it blocks your progress there is no way to
start over. You're left with a few ways to cheat, which might or
might not help: **squeeze past** the boulder (drop your stuff to
fit), **dig the boulder out** (dig the wall or dig the boulder
with a wielded pick-axe or mattock), or **fracture it** with a
wand of striking or a scroll of earth (or polymorph the boulder
into something else). Each of these costs a point of Luck and
breaks the Sokoban conduct. Flying lets you skip unfinished pits
without penalty. Levitation avoids pits too, but it also prevents
you from pushing boulders at all, so it's useless for solving.
**Teleport doesn't work here:** the level forbids it.

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
each level honestly if you can.
For complete solutions to all eight level variants, see
[Sokoban Solutions](#sokoban-solutions) in the appendices.

<!-- audit 2026-05-18 #164: level range DL 5-9 verified vs dungeon.lua:60-66 + dungeon.c:405-409. Corrected fountain count (4, not 1) per oracle.lua:19-22. Corrected minor-consultation framing: rumors.c:147-156 always passes truth=1 to getrumor, so minor consultations always pull from rumors.tru (true tips), not the false-rumor pool. Major consultation cost: 500 + 50*ulevel (rumors.c:699). See companion-audit.md. -->
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
<!-- audit 2026-05-17 #39: 8 role/artifact/nemesis pairs and entry mechanics verified against role.c + artilist.h. Corrected: "Most provide magic resistance" was wrong (only Platinum Yendorian Express Card grants carried MR; others vary). v2 audit 2026-05-18 #5: four factual corrections. (a) Portal range left at 11 through 16 (a transient v2 mis-edit to "11 through 17" was reverted after closer reading of dungeon.c:380-411 and a wiki cross-check; level_range() returns a count, so range=2 means base..base+1, giving max = 9 + 6 + 1 = 16, not 17). (b) "Only the Tourist's PYEC" was wrong on the carried-MR claim — Orb of Detection (Archeologist) and Magic Mirror of Merlin (Knight) also carry MR (CARY(AD_MAGM) at artilist.h:221,257,293). Reworded to "a few" without naming, since the Artifacts chapter has the per-role list. Same shape for the wielded/worn-MR clause — three artifacts have DFNS(AD_MAGM) at artilist.h:233,261,304 (Sceptre of Might / Eyes of the Overworld / Eye of the Aethiopica); kept the generic "a few others." (d) "Nemesis drops two things on the floor" misleads: only the Bell drops from inventory on kill; the quest artifact is placed under the nemesis at level generation (e.g. dat/Val-goal.lua:49,76 same square for both). Reworded. Wisdom additions: nemesis lifesaving (most carry an amulet of life saving — expect to kill twice); portal-back warning (the return portal is only on the first Quest level). Voice: "milestone that marks the transition from surviving to preparing for the endgame" softened to "major power spike"; trimmed three short sentences into two; em-dashes around "from attacking peacefuls, for instance" replaced with periods per the punctuation-ladder rule. See companion-audit.md. -->

Around dungeon levels 11 through 16, a magic portal drops you onto
your Quest. You'll need experience level 14 and a friendly word with
your quest leader on the first floor before they'll let you descend.
The leader sends you to retrieve your role's quest artifact from a
quest nemesis.

Each role has a unique Quest with unique maps, a unique nemesis, and
a unique artifact reward. The Valkyrie hunts the Orb of Fate from
Lord Surtur. The Wizard retrieves the Eye of the Aethiopica from
the Dark One. The Tourist battles the Master of Thieves for the
Platinum Yendorian Express Card. The Samurai duels Ashikaga Takauji
for the Tsurugi of Muramasa. The Monk faces Master Kaen for the
Eyes of the Overworld. And so on.

Quest artifacts are powerful. Each grants a unique mix of carried
or worn intrinsics: protection, luck, ESP, warning, reflection, or
stealth depending on role. A few grant magic resistance just by
being carried; a few others block magic attacks only when wielded
or worn. The Artifacts chapter has the per-role list. Getting your
quest artifact is a major power spike. The late game starts here.

**Two prizes wait on the nemesis's square.** The **Bell of Opening**
rides in the nemesis's pack and falls when you kill them (one of the
three invocation items you'll need for Gehennom). Your role's quest
artifact has been sitting under their feet the whole time, placed
when the level was generated. Pick both up. They don't auto-add to
your pack and they don't reappear, so if you leave the floor without
them you're walking back. The Quest is the only place in the game
you can get them.

Most nemeses carry an amulet of life saving, so expect to kill them
twice. The portal back is on the first Quest level only. If you
descend underprepared you may have a long climb home.

If your alignment record is too low, your quest leader will refuse
to send you. Attacking peacefuls is the usual cause. Keep your hands
clean.

#### The Rogue Level
<!-- audit 2026-05-18 #125: clean audit, no corrections needed. All claims verified: welcome line (do.c:1913), uppercase-only monsters (makemon.c:1672), symbol swaps for armor `]`/amulet `,`/food `:`/gold-same-as-gems (drawing.c:73-79), no closed doors (mklev.c:647-648), no fountains/sinks/altars/shops (mklev.c:988-989 skip_nonrogue branch), no spellbooks/tools/amulets in natural item pool (mkobj.c:58-64 rogueprobs). Dungeon level range is Dlvl 15-18 per dungeon.lua base=15, range=4. -->


Somewhere in the middle dungeon you'll cross a one-level
historical district. You'll know it when the welcoming line reads,
*"You enter what seems to be an older, more primitive world."*
The neighborhood is preserved as it was when **Rogue** was the
only dungeon-crawl anyone had heard of, and a few details give
the era away:

- All the wildlife is in capital letters — lowercase species
  hadn't been invented yet.
- Armor displays as `]`, food as `:`, amulets as `,`, and gold
  shares a symbol with gems (in Rogue they were the same thing).
- Doors don't close. Hinges came later.
- Tile mode switches off in favor of plain ASCII characters.
- No fountains, sinks, altars, shopkeepers, or priests — and
  no spellbooks, tools, or amulets in the natural item pool, all
  post-Rogue inventions.

Modern mechanics still work; you can engrave Elbereth here even
though that was a Hack-era addition. A small and forgivable
anachronism.

#### Fort Ludios
<!-- audit 2026-05-18 #138: 2 corrections + omitted features. (1) "Captains" overstated — knox.lua fixes only 17 soldiers + 1 lieutenant; captains can appear via barracks zoo squadmon but aren't a guaranteed garrison. (2) "Legendary wealth" — Croesus is the vault guardian/warden (MS_GUARD, monsters.h:2863), not a merchant; the gold belongs to the vault, not him. The companion's own bestiary row labels him "Vault guardian." Added the noteleport flag, four dragons, four giant eels in the moat, stone giant, and corner-tower gem caches (knox.lua:9, 144-167). v2 audit 2026-05-18 #14: four factual corrections. (a) Garrison is sixteen soldiers + one lieutenant from knox.lua:126-142, not "seventeen" or "roughly twenty"; the barracks zoo can spawn more once aggro. (b) Portal range is Dlvl 11 down to just above Medusa, not Dlvl 18-22 — the dungeon.lua hint is base 18 range 4 (so 18-21) but mklev.c:2647-2651 only requires depth >10 and above Medusa, and the wiki agrees. (c) The portal is always inside a vault per mklev.c:1331,2624-2658, not "often inside a small vault." (d) The level is non-diggable (knox.lua:35), so "through the walls" doesn't work; level teleport via scroll/wand still does (noteleport blocks only intra-level teleport). Wisdom: Croesus is covetous and dangerous in melee — community advice is to range-attack across the moat, not "engage him" in melee. Voice: dropped "the unique fortress warden" meta; replaced "(15x4 treasury, most tiles trapped)" parenthetical with plain prose noting the 1/3-trapped rate; trimmed "decent weapons" to "serviceable weapons" and dropped the "protection rackets" reference (Ludios gold is more often spent on ID/shop stock at that depth). See companion-audit.md. -->

Fort Ludios is optional and easy to miss entirely. It appears as a
magic portal anywhere from Dlvl 11 down to just above Medusa,
always inside a sealed vault, so you'll need to dig in. The portal
leads to a fortified military compound: sixteen soldiers and a
lieutenant, with more drifting out of the barracks once the alarm
trips. Four guard dragons. A stone giant. Four giant eels
patrolling the moat. And **Croesus** on the throne, the vault
guardian himself. The level is non-diggable as well as `noteleport`,
so once you're inside the only way out is back through the portal
or a scroll of teleportation. Kill Croesus, loot the place, leave.
Croesus is covetous and hits hard in melee, so shoot or zap him
from across the moat rather than walking up.

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

Medusa's level sits near the bottom of the Dungeons of Doom, around
level 25. You'll know it by the large body of water and the
statues scattered around (those used to be adventurers).

The level has three challenges stacked together:

1. **Crossing the water.** The island is surrounded by water.
   You'll need levitation, water walking boots, or some creative
   approach (freezing water with a wand of cold, building a boulder
   bridge, polymorphing into a flying creature). Don't wade in
   without preparation, because:

2. **Giant eels.** The water is home to giant eels that can grab
   and drown you on a successful hit. Stay unburdened while crossing,
   or avoid the water entirely.

3. **Medusa herself.** Her gaze turns you to stone. You need
   either **reflection** (a shield of reflection or amulet of
   reflection bounces the gaze back, stoning her instead) or
   **blindness** (you can't meet her gaze if you can't see). A
   mirror also works if you apply it at her. Reflection is the
   cleanest solution. If you got the amulet of reflection from
   Sokoban, you're already prepared.

There is a downward staircase (or ladder) on the island itself
that leads toward the Castle. The level has four possible layouts
(two added in 3.6), so don't rely on memorizing a
single map.

**The Perseus statue.** One of the statues on the island is named
**Perseus** — the mythological hero who killed Medusa with a
mirrored shield. `#loot` him: he carries a 75% chance of a (cursed)
shield of reflection, a 50% chance of a blessed +2 scimitar, a 25%
chance of levitation boots, and a 50% chance of a sack to put them
in. The shield is cursed, so plan to uncurse it before swapping it
in. The other statues on the level are intentionally empty.

> **Arien Malec's Medusa Checklist**
>
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
  gets a turn. Combine with speed or stealth for reliability.

**Crossing the water.** The island is surrounded by deep water.
Your options, from safest to most desperate:

- **Levitation** (ring, boots, potion, or spell). The easiest way
  to cross, but **does not protect you from eel grabs** in adjacent
  water (see *Drowning* in Dangerous Encounters). Use it to traverse
  fast, not as a defense.
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
  tile, not yours, so even standing on dry land or hovering above
  water doesn't help once the grab lands. Only oilskin/grease,
  magical breathing, or killing the eel first are reliable.

#### The Castle
<!-- audit 2026-05-17 #37: castle.lua/dungeon.lua-verified. 2 corrected: wand of striking destroys the drawbridge (not opens), and the wand of wishing is in a corner tower (not a treasure chamber). See companion-audit.md. -->

The Castle is the last level of the Dungeons of Doom proper, around
level 27. It's a large fortified structure surrounded by a moat,
with a drawbridge as the main entrance. A maze section to each
side may contain minotaurs.

To enter the Castle, you need to open the drawbridge. Options:

- **Play the passtune.** A five-note musical sequence played on
  any tonal instrument (wooden flute, magic flute, tooled horn,
  frost or fire horn, bugle, harp) opens the drawbridge. The notes
  are randomized per game. You can learn them by trying different
  sequences: the game tells you how many notes are correct after
  each attempt, like a game of Mastermind.
- **Wand of opening** pointed at the drawbridge.
- **Spell of knock** cast at the drawbridge.
- **Wand of striking** *destroys* the drawbridge entirely. The
  moat squares become walkable, but the bridge is gone and the
  tune is useless afterward. Use this as a one-way option.

Inside the Castle: a throne room, two barracks, and several
storerooms. The **wand of wishing** — one of the most important
items in the game — is in a chest in one of the four corner
towers (guarded by Elbereth and a cursed scroll of scare monster
to deter the court monsters from displacing it). See
[Wishes and Wishing](#wishes-and-wishing) for the full mechanics
and how many wishes a 5.0 Castle wand actually yields.

Below the Castle lies Gehennom. There is no going back to the
upper dungeon once you descend without climbing back up through
everything. Make sure you're prepared before you go down.

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
<!-- audit 2026-05-17 #26 (re-audit 2026-05-18 v2 #49): 4 trap entries verified, 1 broadened (rust trap also affects non-metal armor, lit lamps, potions). v2 re-verified all four rows: arrow trap at trap.c:1190-1248 (1/15 trap-empty chance once known); dart trap with 1-in-6 poisoned dart at trap.c:1273; squeaky board at trap.c:1402-1476 (wake_nearby/wake_nearto, skipped by Levitation OR Flying); rust trap at trap.c:1595-1654 (40% default branch hits cloak/suit/shirt in order plus dousing lamps). Missed arrows and darts land via place_object + stackobj, supporting "Veterans sometimes trigger them deliberately to stock up." 0 corrections. See companion-audit.md. -->

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
<!-- audit 2026-05-18 #123: trapdoor description "drops you to the next level down" understates the mechanic. hole_destination at trap.c:442-453 rolls each level: while dst->dlevel < bottom, increment; if rn2(4) break — 25% chance per level to keep falling. So a trapdoor can drop you several levels. Same for holes. Also clarified that Flying (not just Levitation) skips pits/holes/trapdoor (trap.c:635, 1850), with the !Sokoban guard that disables the skip on Sokoban puzzle levels. -->


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
<!-- audit 2026-05-18 #132: 3 corrections. (1) Anti-magic implosion damage "halved to 1d4 if you can pass through walls" — wrong; trap.c:2371-2372 dmgval2 = (dmgval2 + 3) / 4 — QUARTERED (rounded up), not halved. From max 4d4 the result is at most 4, not 1d4. (2) "Destroying it from range by zapping cancellation at it to defuse it without setting it off" — wrong; cancellation aimed at any magical trap (including ANTI_MAGIC per trap.h:118-122) triggers an explosion of 20 + d(3,6) damage at the trap's square (zap.c:3611-3621). It removes the trap but doesn't silent-defuse. (3) Polymorph trap "only PolyControl helps" — incomplete; Antimagic and Unchanging both block the polymorph entirely (trap.c:2486-2489). Added that to the polymorph-trap paragraph. v2 audit 2026-05-18 #42: one-sentence addition to the sleep-gas paragraph noting that sleep resistance (elven blood, the right ring) sidesteps it entirely (trap.c:2772-2773 — sleep gas check returns early on Sleep_resistance). Re-verified the anti-magic implosion math, polymorph trap Antimagic/Unchanging blocks, iron-footwear interactions, and cancellation-explosion damage formula. 0 other corrections. See companion-audit.md. -->


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
*not* your belongings.

Polymorph traps are a double-edged sword. With polymorph control,
they're a free polymorphing booth. Without it, you become something
random, possibly a newt that can't use any of its equipment.
**Magic resistance and the Unchanging intrinsic both block the
polymorph entirely** — Tcontrol is the only way to *use* the trap,
but MR or Unchanging let you walk through it untouched.

Sleeping gas is murder in monster-rich areas. You can't fight, you
can't run, you can't even wake up on purpose. Monsters line up
to hit you like it's a buffet. Sleep resistance (elven blood, the
right ring) sidesteps it.

**Anti-magic fields hit harder if you're magic-resistant.**
Counterintuitive enough to mislead returning players. The trap
drains spell energy, and having *magic resistance* also triggers
an "anti-magic implosion" that costs you HP. The damage is
`rnd(4)` base, plus another `rnd(4)` if you have half-physical or
half-spell damage, plus `rnd(4)` for wielding Magicbane, plus
`rnd(4)` for carrying any one magic-resistance artifact (only one
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
<!-- audit 2026-05-18 #92 (re-audit 2026-05-18 v2 #63): dosearch0 mechanics verified (detect.c:2016-2093); rnl Luck bias confirmed (rnd.c:112). Corrected: wand of secret door detection is NODIR; also reveals SDOOR/SCORR/traps/trapped chests/hidden mimics, not just traps. Levitation/Flying immune to most but not all floor traps. Search artifact/lenses bonus only helps door/corridor discovery (rnl(7-fund)); trap roll uses rnl(8) with no fund. v2 corrected the wand's area shape: it's a circular area of radius BOLT_LIM=8 (vision.c:27-45 circle_data + 2107-2148 do_clear_area) blocked by line of sight via couldsee(), NOT a square. Reworded "square radius around you" to "roughly circular area around you (radius about eight, blocked by line of sight)." Excalibur is the only SPFX_SEARCH artifact (artilist.h:85-86). See companion-audit.md. -->

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

A good time to search is when the dungeon has already hinted that
something is wrong: a stray corpse in the middle of an otherwise
empty room, a scatter of arrows or darts on the floor, a square
your pet refuses to cross, or a themed room whose gimmick is
hidden hazards.

<!-- audit 2026-05-18 #177: passes_bars (mondata.c:552-563) uses verysmall() = msize<MZ_SMALL = TINY only; kittens and little dogs are MZ_SMALL and do NOT pass through. Lightning shares the ZT_ACID branch at zap.c:5344-5369 (90% per tile melts bars). Wand/spell of striking and force bolt have no IRONBARS handler so they pass through harmlessly. Rock moles eat bars (metallivorous, hack.c:769-784). See companion-audit.md. -->
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
black naga), and a **wand of lightning** will melt bars too.

The practical early-game answer is to **dig around** them. Iron bars
sit in a single tile of wall with ordinary stone on the flanks, so a
pick-axe through the adjacent wall tunnels into the niche from the
side and the bars stay standing as decoration. Mid-game, polymorph
into something that breathes acid or lightning, passes walls (xorn,
earth elemental), is **tiny** enough to slip between, or eats metal
(rock mole). Starting pets won't fit, but a polymorphed pet can.

What's typically behind them: a scroll of teleportation (guaranteed
if teleport isn't suppressed on the level), occasionally a random
item or a previous adventurer's corpse. The scroll is a joke: you'd
need one already to read it from outside the bars.

#### Finding Secret Doors

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
- **Excalibur** (or any artifact with the searching aura), wielded, adds its enchantment to your search bonus (capped at +5; a freshly-dipped +0 Excalibur adds nothing)
- **Lenses** worn (and you not blind) add +2 to the search bonus
- **Wand of secret door detection** instantly reveals nearby secrets in a radius
- **Blessed scroll of magic mapping** shows every secret door on the level (only the blessed version)

**The wisdom of patience:**

Secret doors are NetHack's way of teaching you that brute force
doesn't solve every problem. Sometimes you need brute force applied
methodically to every wall section in sequence. The downstairs you
seek is behind one of these walls. Finding it is a matter of
systematic elimination. The only mistake is giving up after three
searches and declaring the level "impossible."

<!-- audit 2026-05-18 #176 (re-audit 2026-05-18 v2 #53): Three corrections. (1) Athame is INSTANT for Elbereth-length engravings: uncursed athame is not in dulling_wep (engrave.c:1306), and as a WEAPON_CLASS it doesn't trigger the rate=1 branch (engrave.c:1321-1325) — rate stays at 10, finishing 8 chars in one occupation action. Cursed athame does dull and would use rate=1. (2) Edged weapon dulls by ~1 enchantment per 2 chars engraved (engrave.c:1357-1382, comment at 1360-1361: "-2=>3, -1=>5, 0=>7, +1=>9, +2=>11 chars"); Elbereth costs ~-4 enchantment, not -1. (3) Impairment garble: only the DUST/BLOOD surface-garble (engrave.c:1223, 1/25) is bypassed by BURN/ENGRAVE; the Blind 1/11, Confused 1/7, Stunned 1/4, and Hallucinating 1/2 per-character scrambles at engrave.c:1224-1225 apply to ALL types including wand-of-fire BURN. "ad aerarium" also marks LEVEL_TELEP niches (mklev.c:809-811), not only vault niches (mklev.c:820-824). v2 re-verified: rate=10 default with rate=1 only on dulling_wep/RING/GEM branches; uncursed athame dulling-exempt at engrave.c:1306-1307; BURN damage on ice or magical fire @ 50% at engrave.c:278; strict-match Elbereth at engrave.c:256; vault 2×2 + makevtele() at mklev.c:1320-1333; "ad aerarium" niche placement at mklev.c:728-737. DUST monster-step erodes 1 char per monster-turn (monmove.c:734 + engrave.c:271-289). 0 corrections. See companion-audit.md. -->
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
near a secret closet containing either a **vault teleporter** (a
one-shot TELEP_TRAP that drops you into Croesus's 2×2 gold vault
on the same level — pick up the gold, then escape ahead of the
vault guard) or a **level teleporter** (a LEVEL_TELEP that sends
you to a random dungeon level, often unwelcome without Teleport
control); *"Vlad was here"* marks a secret closet containing a
**trap door**. Both are easy to miss in the message log, and
worth investigating when you see them — but be ready for what's
on the other side.

#### Elbereth
<!-- audit 2026-05-18 #122: 2 corrections. (1) "Levitation trick" (engrave Elbereth in dust while floating) is non-functional in 5.0: engrave.c:198 requires can_reach_floor() which returns FALSE under Levitation; finger-engrave is refused outright at engrave.c:1003-1006, and wand zaps only "gesture toward the floor below you" per engrave.c:1008-1010 — no actual writing happens. Replaced with the 5.0 reality. (2) "−5 alignment hit" stated as flat; mon.c:4280 is adjalign((u.ualign.record > 5) ? -5 : -rnd(5)), so it's flat −5 only with healthy alignment, otherwise rnd(5) (avg −3). Reworded. -->


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

If you melee-attack a monster while standing on Elbereth (and that
monster *would* have feared the ward, or is peaceful), the
engraving is **deleted instantly, in full, regardless of how it was
made.** Even a burned-permanent Elbereth disappears in one swing.
You take an **alignment hit** ("You feel like a hypocrite") and see
the message *"The engraving beneath you fades."* The hit is a flat
−5 if your alignment record is comfortably positive (above +5);
otherwise it's a random −1 to −5.

The durability table doesn't show this: "permanent" and
"semi-permanent" describe resistance to *passive* wear (monster
footsteps, erosion). Your own hostile action wipes the word
regardless of tier. So Elbereth is strictly **defensive**.
Use it to heal, drink a potion, read a scroll, swap gear — and step
off (or kill at range) when you want to attack.

##### Practical use

In an emergency, write Elbereth in the dust with your finger: free,
instant, and good enough to buy a turn or two. Most monsters will
back off and let you act. Once the immediate danger passes, you can
either step off the dust ward to keep it for next time (it survives
until a monster steps on the square), or upgrade to something more
durable.

For a permanent safe spot — useful for stashing items, resting at a
fixed retreat point, or anchoring a corridor fight — burn the word
with a wand of fire or lightning. One turn, no interruption risk,
no impairment penalty, no wear. A semi-permanent engraving (athame,
weapon, gem, wand of digging) is the middle ground: durable, but
the slow methods can be interrupted mid-word.

In 5.0, engraving requires you to be **able to reach the floor**.
Levitation makes that impossible — finger-engrave is refused
outright, and a wand zap only "gestures toward the floor below
you" rather than writing anything. The old levitation-locks-dust
trick from earlier editions no longer works; if you want a
durable spot you have to land first and use fire/lightning/
athame.

---

### Feelings and Sounds
<!-- audit 2026-05-18 #140: 5 corrections. (1) "Counting gold coins" message specifically means a vault WITH gold; an empty vault gives "someone searching" (sounds.c:253-262). (2) "Wow! This makes you feel great!" is the blessed-tier restore ability OR blessed magic fountain; the spoiler attributed it generically to restore-ability (potion.c:658-661, fountain.c:257). (3) "Move very quietly" doesn't include elven boots — boots produce "walk very quietly" (do_wear.c:123-129). (4) Lycanthropy cure is QUAFFING holy water, not dipping (potion.c:728-737 set_ulycn in the blessed-water branch). (5) "Seem faster" from quantum mechanic corpse only fires if you don't already have intrinsic speed; otherwise you "seem slower" instead (eat.c:1227-1235). Also added the global suppressor: Deaf/!flags.acoustics/u.uswallow/Underwater silences all dosounds() messages (sounds.c:208-209). -->

Much of the most important information in NetHack comes to you as
cryptic feelings and sounds. They sound like atmosphere, but most
of them are specific signals. If you don't know what they mean,
you'll miss the cues entirely. They are worth memorizing.

(Caveat: being **Deaf**, **swallowed**, or **underwater** silences
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
| *"You feel feverish."*                 | Lycanthropy infection from a were-monster. **Quaff** holy water, eat wolfsbane, or pray. (Dipping doesn't cure it; only drinking does.) |
| *"You are slowing down."*              | You're turning to stone. Immediately eat a lizard corpse, drink acid, or pray.         |
| *"You are turning into slime."*        | Green-slime contagion. Burn it off (fire scroll/spell/wand) or pray.                   |
| *"You feel deathly sick."*             | Terminal illness (Pestilence, Demogorgon). Quaff extra healing, eat eucalyptus, or pray. |

---

## Part Three: The Locals

---

### A Field Guide to Dungeon Fauna
<!-- audit 2026-05-18 #130: chapter overview verified against include/defsym.h symbols and individual monsters.h entries. 2 corrections: (1) "Xan, a leg-wound trapper" misreads — xan does AT_STNG AD_LEGS (sting cripples legs) but is NOT a trapper (S_TRAPPER is the engulfer t-class). Reworded. (2) "Leprechaun single bite drains gold" — leprechaun is AT_CLAW AD_SGLD (monsters.h:660), not bite. Reworded. All other class-symbol mappings, monster stats, and tactical claims verified clean. -->


The Mazes are home to hundreds of monster species, organized into
classes denoted by letters. Lowercase letters are generally smaller
or less dangerous; uppercase letters are larger or more threatening.
Color further distinguishes individual species within a class.

Here is a quick field guide to what each letter means, roughly ordered
by how early you might encounter them. For the full level / speed /
AC / attack details on every monster, see the
[Bestiary Tables](#bestiary-tables) appendix.

#### Common Early Encounters

| Symbol | Class                  | Notes                                                                      |
| ------ | ---------------------- | -------------------------------------------------------------------------- |
| `a`    | Ants      | **Soldier ants are the famous early killer**: speed 18, two attacks per turn (bite + strength-draining sting), and they travel in packs. A wandering soldier-ant group on Dlvl 4 can end a careless run. Killer bees, giant ants, fire ants are all the same shape of problem. |
| `b`    | Blobs     | Acidic or gelatinous. Acid blobs have no active attack — they only splash 1d8 acid back when *you* hit *them*, and the splash can corrode your weapon. Kill at range, or walk past. |
| `B`    | Bats      | The `B` class is **deceptively dangerous because of speed**. Bats and giant bats clock in at speed 22 — nearly twice the player's base 12, so they get roughly two bites per one of your swings. Giant bats bite for 1d6 each; the math catches up fast. Vampire bats are still in the bat class but their second bite drains Strength (not levels). |
| `d`    | Dogs and other canines | The `d` class covers your starting pet (little dog, kitten via cat-class) **and** the most numerous early-game predators. **Jackals** are the single most common cause of death on the public server — they only bite for 1d2, but they spawn in packs and there are a *lot* of them on the upper levels. **Foxes** bite for 1d3 and are faster (speed 15) but spawn alone. Coyotes, dingos, wolves get progressively worse. Tame `d` (your pet, larger dogs you've fed up) help fight everything else. |
| `e`    | Eyes      | **Floating eyes paralyze on melee hit.** Never hit an `e` in melee. Use ranged attacks. Spheres (flaming/freezing/shocking) explode in a 3×3 area; kill them at range. Melee finishes them but you eat the blast. |
| `f`    | Cats      | Like dogs, often starting pets. Felines can be tamed with tripe.                        |
| `G`    | Gnomes    | The standard inhabitants of the Gnomish Mines. Individually weak, but the Mines have a lot of them — and **plain gnomes, gnome lords, and (later) gnome rulers are all in the top fifteen causes of death** on the public server, because mid-game players treat the Mines as a milk run and walk into a four-on-one with full-strength enemies. If you're a gnome yourself, most of them are peaceful. |
| `h`    | Humanoids | Dwarves, bugbears, mind flayers. Wide range of difficulty. **Dwarves in particular are dangerously underrated**: they hit harder than they look, they're armored, and they're the second most common cause of death on the public server because of how many you meet in the Mines. Don't trade blows with one in melee until your AC is solid. |
| `i`    | Imps      | Minor pests. Weak claw, regeneration, and a stream of insults — annoying but not dangerous. |
| `j`    | Jellies   | Spotted and ochre jellies. Passive acid damage on melee.                                |
| `k`    | Kobolds   | Weak individually but sometimes carry poisoned weapons.                                 |
| `o`    | Orcs      | Numerous and modest in strength one-on-one; dangerous in packs. Hill orcs and Mordor orcs are the common upper-dungeon variants. |
| `r`    | Rodents   | Rats and rock moles. Rock moles eat metal items, so protect your gear.                  |
| `s`    | Spiders   | Cave spiders are weak. Giant spiders poison.                                            |
| `x`    | Grid bugs | The weakest monster in the game; they can't even move diagonally. Free XP — they don't leave corpses. The `x` class also covers the much-later **xan**, whose sting cripples your legs (slow movement until it heals). |
| `:`    | Lizards   | Newts, geckos, and iguanas are individually weak — usually not too dangerous if you're paying attention. The class matters mostly for the corpses: **lizard corpses cure petrification** (always carry one for cockatrice/Medusa insurance), and newt corpses may restore 1–3 mana to spellcasters. |

#### Mid-Dungeon Threats

| Symbol | Class             | Notes                                                                                                |
| ------ | ----------------- | ---------------------------------------------------------------------------------------------------- |
| `A`    | Angels            | Powerful, usually aligned. Don't fight your own.                                                     |
| `C`    | Centaurs          | Fast (speed 18-20). Half spawn with a bow or crossbow, but they'll still close into melee for weapon and kick attacks. Mountain centaurs hit hardest: 1d10 weapon plus *two* 1d6 kicks per turn. |
| `E`    | Elementals        | Hard to kill. Air elementals engulf; earth elementals phase through walls.                           |
| `f`    | Displacer beast   | Cat-class, but vicious: AC −10, three-attack melee, and a 50% chance on each player melee to swap places with you instead. Eat the corpse for temporary intrinsic Displacement. |
| `F`    | Fungi             | Yellow mold, green mold, shriekers. Shriekers summon other monsters.                                 |
| `G`    | Gnome lords/kings | Tougher gnomes. Still fairly manageable.                                                             |
| `'`    | Golems            | Built things. Iron golems hit hard and resist nearly everything; clay, stone, and wood golems are softer. Glass golems leave gems on death. |
| `H`    | Giants            | Strong melee, throw boulders. Giants carry gems.                                                     |
| `J`    | Jabberwock        | Rare, but if you see one you're in for a fight. Four 2d10 attacks per turn (two bites and two claws) at normal speed. |
| `K`    | Keystone Kops     | The shopkeeper-summoned constabulary. They appear when you steal, refuse to pay, or anger a shopkeeper. Individually weak but they swarm, and they jeer at you. |
| `l`    | Leprechauns       | Steal your gold and teleport away. A single claw can grab up to *all* of your purse. Hide gold in a sack, drop it elsewhere, or fight at range. |
| `L`    | Liches            | Spellcasters. Arch-liches are among the most dangerous monsters in the game.                         |
| `m`    | Mimics            | Disguised as items, walls, doors, fountains, altars, or boulders. See the mimics note below.         |
| `M`    | Mummies           | Aggressive undead with physical claw attacks. Their corpses are dangerous to eat (age you). Mummy wrappings worn as a cloak block invisibility — usually a downside, but useful if you've gone invisible and need a shopkeeper to interact with you. |
| `n`    | Nymphs            | Steal items from your inventory, then teleport away. Fight from range.                               |
| `N`    | Nagas             | Large serpent-bodied creatures. Red nagas breathe fire, black nagas spit acid, golden nagas cast spells, guardian nagas spit Str-drain poison and have a paralyzing bite. Tough; speeds 12–16. |
| `O`    | Ogres             | Strong melee fighters. Ogre lords and kings are tougher.                                             |
| `p`    | Piercers          | Disguise as stalactites; drop from the ceiling onto whatever walks below. The fall does serious damage. Hard to spot in advance. |
| `P`    | Puddings          | Black AND brown puddings split when hit in melee with an iron or metal weapon (scalpel and tsurugi count). Use silver, dragonhide, or spells.                                     |
| `q`    | Quadrupeds        | Multi-attack mid-game bruisers. The **rothe** is the famous one (three attacks per turn at sluggish speed 9, dangerous in packs); mumakil are solo two-attack bruisers (4d12 butt + 2d6 bite).                              |
| `R`    | Rust monster / disenchanter | Rust monsters corrode worn iron armor when they hit you, and your wielded iron weapon when you hit them. Use non-iron alternatives (mithril, silver, dragonhide) or take iron gear off before the fight; iron items kept in your inventory aren't touched. **Disenchanters** drain enchantment on hit and have their own write-up under Dangerous Encounters. |
| `S`    | Snakes            | Cobras and pit vipers poison. Water moccasins come from fountains.                                   |
| `t`    | Trappers / lurkers above | Hide in plain sight on floor or ceiling and engulf you when you walk under/onto them. See the engulfment write-up under Dangerous Encounters. |
| `T`    | Trolls            | Regenerate. They come back from the dead unless you eat or tin the corpse.                           |
| `u`    | Horses / unicorns | Horses are usually mountable, mostly peaceful in the wild. Unicorns are color-coded by alignment: same-aligned spawn peaceful, cross-aligned hostile. The gem-throwing negotiation playbook is in the Luck chapter. |
| `U`    | Umber hulk        | Confuses on sight. Avoid looking at them directly.                                                   |
| `v`    | Vortices          | Engulfing wisps. Air, fire, ice, and steam vortices each apply their element to whatever they engulf. Kill at range. |
| `w`    | Worms             | Long worms grow tail segments after each hit and can be a corridor in themselves. Purple worms swallow you whole (see Don't Want, below). |
| `W`    | Wraiths           | Drain levels on hit. But their corpses grant a level, so eat them fresh.                             |
| `y`    | Yellow/black lights | Explode adjacent. Yellow blinds you; black hallucinates you. Black lights are invisible without *see invisible*. Kill at range. |
| `Y`    | Yetis             | Tough melee combatants. Corpses may grant cold resistance.                                           |
| `z`    | Zruty             | Three-attack mid-game brute. Uncommon but a fair fight if you've geared up.                          |
| `Z`    | Zombies           | Slow, numerous, come in many varieties. Zombie corpses are old and will rot.                         |

#### Things You Don't Want to Meet

| Symbol | Class            | Notes                                                                                                    |
| ------ | ---------------- | -------------------------------------------------------------------------------------------------------- |
| `c`    | Cockatrices      | **Touch = instant petrification.** Never hit one barehanded. Wield their corpse with gloves as a weapon. |
| `D`    | Dragons          | Each color has its own breath weapon, resistance, and scale mail property. See note below.               |
| `h`    | Mind flayers     | Drain intelligence on hit. **If Int hits your racial minimum (3 for humans), you die.** Keep distance or kill fast.                    |
| `V`    | Vampires         | Drain levels. Vampire lords fly and are fast.                                                            |
| `w`    | Purple worms     | The big worm: swallows you whole on a hit, then digests. Cut your way out from inside.                  |
| `X`    | Xorn             | Phases through walls and floors. Three claws and a bite per turn; hard to ambush and hard to escape from. |
| `;`    | Sea monsters     | Drowning is an instadeath. Don't fight in water without a plan.                                          |
| `&`    | Demons           | Major demons (Orcus, Demogorgon, Asmodeus) are boss-level threats.                                       |
| `@`    | Humans (hostile) | Includes the Wizard of Yendor, who is the most persistent nuisance in the game.                          |
| `Q`    | Quantum mechanics / genetic engineers | Quantum mechanics teleport their target on a hit; genetic engineers (new in 5.0) polymorph their target. The `Q` class is small but every one of them is a surprise. |

#### Special Symbols

A few map glyphs aren't monsters in the conventional sense, but you'll see them and need to know what they mean.

| Symbol | What it is               | Notes                                                                                                |
| ------ | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| `I`    | Invisible monster marker | The game remembers the last spot you sensed something you couldn't see. The `I` stays there until you bump it or step on the square; the monster has usually moved. |
| `~`    | Long worm tail segment   | Part of a long worm's body. Hitting the tail damages the worm and shortens the chain; hitting the head (the `w`) is full melee. |
| `]`    | Strange object           | **Always a mimic.** No ordinary item ever displays as `]` (compare `[`, armor — `]` is its mirror). See the mimics note below. |
| ` ` (space) | Ghost               | Ghosts left from bones files. The glyph is a literal space, which paints over the floor underneath: in a room, a ghost shows as a one-square *gap* in the floor where a `.` should be. Walk into the gap to identify it. |

---

### What Actually Kills Adventurers
<!-- audit 2026-05-17 #29: ~30 claims verified, 3 corrected (mount slip 10-14 HP not 11-15; mumakil 2-attack solo not 4-attack pack; shimmering DSM removed since it's #if 0 DEFERRED in 5.0). Also caught my own audit-#15 errors: shimmering DSM and missing Blue DSM speed. See companion-audit.md. -->

Only about **0.4% of games end in ascension.** The other 99.6%
are deaths. NetHack ends in death by default; survival is the
exception.

**The early dungeon is where you die.** The top ten killers are,
in order: jackals, dwarves, soldier ants, gnome lords, sewer rats,
giant bats, small mimics, gnomes, foxes, water moccasins. Every
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

**Specific tips beyond the top ten, where players consistently
underestimate the threat.**

- **Mines residents** (`g`, `h`). Plain dwarves, gnomes, and gnome
  lords are all top-fifteen killers because the Gnomish Mines
  funnel a lot of armed humanoids into a confined space. Dwarves
  in particular hit harder than they look. Don't try to clear the
  Mines as a routine errand — treat each room of dwarves like
  several real fights stacked on top of each other.
- **Bats** (`B`). Giant bats and ordinary bats are fast (speed 22
  vs your 12), so they double-attack every turn. A 1d4 bite (1d6
  for giant bats) at double rate eats through low-level HP pools
  quickly.
- **Quadrupeds** (`q`). Rothes are three-attack pack hunters at
  sluggish speed 9: dangerous mostly in numbers. Mumakil are
  solo two-attack bruisers (4d12 butt + 2d6 bite) that hit harder
  than anything else in the Mines.
- **Eating mistakes.** Rotted corpse, poisonous corpse, and
  choking each show up high on the list. Don't eat old corpses.
  Don't eat while satiated. Pray immediately if you ate something
  you shouldn't have.
- **Water demons.** Quaffing a fountain summons one ~1 in 30
  times, and they hit hard before they think about granting a
  wish. Wish odds also drop with depth, so casual quaffing pays
  worse the deeper you go.
- **Mount slips and riding accidents.** More heroes die slipping
  off saddled ponies than die to mind flayers. Getting on a steed
  rolls against your XP level plus the steed's tameness; if you
  fail, you take 10–14 HP. Don't mount while Confused, Fumbling,
  or Glib, don't mount with a cursed or greased saddle, and don't
  mount a barely-tame pony at experience level 2.
- **Boiling potion (Gehennom).** Hot ground shatters potions
  dropped on the floor. The shrapnel is deadly. Keep potions in a
  bag once you're below the Castle.
- **Pet kills.** Kittens, little dogs, housecats, and ponies all
  appear on the list — almost always because the player put on a
  ring of conflict and forgot to take it off. Remove the ring
  before walking back to your pet.
- **Golems.** The rope golem in particular grapples you, and
  several Quest dungeons have them in numbers. Gold golems are
  another quiet killer.

**The colorful deaths.**

- **Killed by your own wand.** Self-zapped attack wands, rays
  ricocheting off the wall in a narrow corridor and back into your
  face. Identify wands before pointing them at yourself.
- **Killed by a grid bug.** The *weakest monster in the game*
  kills more than 11,000 adventurers per year. They get the last
  hit on someone who walked away from a real fight at 2 HP. Don't
  read a scroll on the turn a grid bug is adjacent.
- **Killed by kicking.** Kicking sinks, doors, locked chests. The
  reaction can break a toe, summon a black pudding, or electrocute
  you. (Electric shock is a top-100 cause of death in its own
  right.) Stop kicking things.
- **Wrath of a god.** You prayed when your god wasn't willing.
  See the Divine Relations chapter.
- **Scroll of genocide.** Read while confused → genocides your
  own role's species (Valkyrie, Wizard, etc.) → instant kill.
  Don't read scrolls under confusion unless you know what they are.
- **Scroll of earth.** Buried under a pile of boulders you summoned
  on yourself.

The pattern across the whole list: routine mistakes kill far more
adventurers than exotic instadeaths. Floating eyes, cockatrices,
mind flayers, and disenchanters all matter (and they're catalogued
under Dangerous Encounters below). But the median death is a
preventable swarm of jackals on Dlvl 3.

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

**Yellow** dragon scale mail is the sleeper pick. Listed power is
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
**speed** (the Fast property — same as speed boots, only stackable
with them for **Very Fast**). One of the most powerful body slots
in the game.

**Gold** dragons are new in 5.0 and breathe fire. Their scale mail
has no resistance power but is permanently lit (radius 4 blessed, 3
uncursed, 2 cursed) — the only body-slot light source in the game,
and it lets you abandon torches and oil. It also confers
hallucination resistance.

All scale mails are dragonhide, body-slot, AC 1 worn, and resist
disenchantment naturally. The choice of which color to chase is
usually whichever dragon's territory you can reach safely; killing
a dragon yields scales you can wear immediately or convert to
scale mail.

---

### Dangerous Encounters

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

<!-- audit 2026-05-18 #172 (re-audit 2026-05-18 v2 #50): stoning timer starts at 5 (uhitm.c:3937) and ticks 5→1 with five distinct messages (timeout.c:128-148). At tick 3 "Your limbs have turned to stone" the hero is paralyzed via nomul(-3) (timeout.c:163-165), closing the action window. Corrected: acid-blob corpse confers only TIMED stoning resistance (HStone_resistance += d(3,6) at eat.c:932-934, 1089-1094), not permanent. Removed amulet-of-unchanging "interrupt": Unchanging doesn't affect stoning (only blocks poly per polyself.c:1381-1384), and wearing it WHILE stoning is actively bad — it blocks the stone-golem auto-poly escape. Plain wand of polymorph isn't an "interrupt" either: only `poly_when_stoned` monsters (golems, mondata.c:80-85) auto-cure stoning, and the wand can't target that outcome. Stepping on a cockatrice corpse is safe ONLY without Fumbling — Fumbling can trip and instapetrify (timeout.c:1256-1261). v2 fixes: "the next message kills you" was off by two — after "Your limbs have turned to stone" (counter 3) two more messages appear ("You have turned to stone" counter 2, "You are a statue" counter 1) before done(STONING) fires at counter 0. Reworded to "the final messages kill you." Softened the Unchanging warning: poly_when_stoned at mondata.c:80-85 requires you to ALREADY be polymorphed into a non-stone golem, so the "blocks the rescue" framing was over-strong for an unpolymorphed hero who was never going to get the rescue anyway. See companion-audit.md. -->
#### Petrification (Stoning)

Touching a cockatrice without gloves, eating a cockatrice corpse,
catching Medusa's gaze, or **kicking** a cockatrice corpse barefoot
will turn you to stone. *Stepping* on the corpse is safe so long as
you don't have Fumbling — Fumbling can trip you over the corpse for
instant death. The process is sometimes immediate; otherwise a
five-turn countdown announces itself with *"You are slowing down,"*
*"Your limbs are stiffening,"* *"Your limbs have turned to stone"*
(at which point you are **paralyzed** and can no longer act),
*"You have turned to stone,"* and *"You are a statue"* (death).

**Defenses ahead of time:** wear gloves around cockatrice corpses,
use reflection against Medusa, and pile up *timed* stoning
resistance from acid blob corpses (each one grants d(3,6) turns of
HStone resistance — useful, but not permanent). For something
permanent, wear yellow dragon scale mail.

**Defenses while it's happening:** eat a lizard corpse (this is
why you carry one), eat an acidic corpse, drink a potion of acid,
pray, or cast stone-to-flesh on yourself. Note: act *before* the
"Your limbs have turned to stone" message — after that you're
paralyzed for three turns and the final messages kill you. Amulet
of Unchanging does **not** interrupt stoning. If you happen to be
polymorphed into a non-stone golem, wearing it during the countdown
is actively harmful — it blocks the stone-golem auto-poly that
would otherwise save you on death.

**The other side of the coin:** a wielded cockatrice corpse (with
gloves on) is one of the game's most devastating weapons —
anything you hit that lacks stoning resistance turns to stone.

#### Drowning
<!-- audit 2026-05-17 #11 (re-audit 2026-05-18 v2 #28): 5 claims verified, 2 corrected (encumbrance doesn't gate grab-drown; "stay unburdened" doesn't defend against the grab path). v2 re-verified: drown check uses monster's tile (uhitm.c:3389-3390), Swimming/Amphibious/Breathless all defeat it (youprop.h:264-277), pool-entry check at hack.c:3272 also lets Flying skip (left unmentioned — Levitation is the canonical defense), emergency_disrobe gated by Stressed+ at trap.c:4897-4941, krakens generate only on Medusa-4 and the Water Plane (the "swamp rooms" reference is to eels not krakens per mkroom.c:557-565 comment). 0 corrections. See companion-audit.md. -->

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

#### Attack Wands and the Warning Shot
<!-- audit 2026-05-17 #21: 6 claims verified, 0 corrected; added the late-game carve-out (Stronghold/Knox/Quest/Gehennom/endgame monsters start mwandexp=TRUE per makemon.c:1290). See companion-audit.md. -->

The first time any given monster zaps a beam wand (death, sleep,
fire, cold, lightning, magic missile) at you, the shot misses. If
you can see the monster, the wand identifies itself in the same
moment, so now you know what was just aimed at you and you have a
turn to do something about it before the next zap connects.
**Late-game exception:** monsters generated in the Stronghold,
Knox, the Quest, Gehennom, Vlad's Tower, or the endgame planes
start with their "experience" flag already set, so their first
zap can connect. The freebie is an early-to-mid-game courtesy.

#### The Touch of Death
<!-- audit 2026-05-18 #116 (re-audit 2026-05-18 v2 #52): corrected MR-blocks-everything claim. Self-zap of WAN_DEATH / SPE_FINGER_OF_DEATH at zap.c:2885-2902 does NOT check Antimagic — only the ray-bolt path at zap.c:4497-4502 checks it. Magic resistance protects you from being hit by a death ray, but not from misfiring your own wand into yourself. The only escape for self-zap is being nonliving (poly into vampire/skeleton/etc.) or is_demon. Also clarified the 8d6+50 damage applies only on Rider Death's rolls 17-19; the more common 5-16 rolls deliver a smaller permdrain that MR doesn't reduce (uhitm.c:3858-3882 + mcastu.c:326-337). v2 re-confirmed: Death rolls rn2(20) with 19/18/17 = full touch (15%), 5-16 = permdrain=1 (60%), 0-4 = miss (25%); 17-19 with MR FALLS THROUGH to the smaller drain rather than being harmless; nonliving covers undead/manes/golems/S_VORTEX per mondata.h:219-220. 0 corrections. See companion-audit.md. -->

Some monsters, most notably Death (one of the Riders on the Astral
Plane), can kill you with a single touch. The Finger of Death spell
and the wand of death work similarly.

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

<!-- audit 2026-05-18 #174: hunger thresholds at eat.c:3369-3372 (Satiated >1000, Not Hungry >150, Hungry >50, Weak >0, Fainting ≤0). Faint path at eat.c:3410-3432; STARVED death at u.uhunger < -(100 + 10*Con), eat.c:3437-3447. Initial u.uhunger = 900 (eat.c:129). TROUBLE_STARVING covers Weak through STARVED (pray.c:216-217). Section makes no factual errors. 0 corrections. See companion-audit.md. -->
#### Starvation

This isn't technically instant, but it feels like it. If your
nutrition drops to zero, you faint. If you don't eat something while
fainted, you die. In the early game before you've established a food
supply, starvation is a real threat.

**Defenses:** Eat corpses promptly. Pray when your god is willing
and you are Weak or Fainting (prayer cures hunger). Carry food
rations, tripe rations, or lembas wafers. Don't let nutrition
management slide.

#### Brainlessness
<!-- audit 2026-05-17 #63: mind flayer / master mind flayer tentacle counts (3/5) + AD_DRIN + AT_WEAP 1d8 verified against monsters.h:523-535. INT loss rnd(2) per hit, max 10 per master turn (uhitm.c:3263). Brainlessness death + lifesaving-still-dies in eat.c:698-715. 1-in-5 losespells per uhitm.c:3264. Polymorph-into-mindflayer brain-eating recovers INT (eat.c:679-688). Corrected: any helmet blocks 7/8 attacks (uhitm.c:3235 `uarmh && rn2(8)`); greasing is only an extra slip-roll on top. Removed false claim that blessed full-healing restores attributes (potion.c:1144-1162 restores HP and one lost level only, not stats). See companion-audit.md. -->

Mind flayers drain Intelligence with their tentacle attacks. If
your Intelligence drops to your racial minimum (3 for humans), the
next drain kills you: "brainlessness." A regular mind flayer has
three tentacle attacks per turn; the **master mind flayer** has
*five*, plus a heavier weapon strike, and is widely called the
most lethal non-boss monster in the dungeon. A single unprepared
turn next to a master mind flayer can drop your Int by up to ten.
Each hit also has a 1-in-5 chance to trigger **spell amnesia**: a
random number of your memorized spells (zero to all of them) drop
to zero retention; re-study from spellbooks to restore. (Before
5.0 amnesia used to wipe maps and identification also, but no
longer.)

**Defenses:** **Wear any helmet.** Even a plain orcish helm blocks
seven of every eight tentacle drains. Greasing the helmet stacks an
additional slip-off roll on top, so a greased helmet is the gold
standard. Better yet, kill them at range (wands, spells) so the
question doesn't arise. To recover drained Intelligence you need a
*potion of restore ability* (uncursed restores one stat; blessed
restores all), the spell of restore ability, or prayer when you're
in good standing. In 5.0 the unicorn horn no longer restores lost
attributes, so don't rely on it. Stockpile at least one restore
ability before pushing into mind flayer territory.

#### Level Drain
<!-- audit 2026-05-17 #43: corrected "vampire bats" from drain-life list (their second bite is AD_DRST, drain Strength, not AD_DRLI). Added shield of drain resistance (new in 5.0). Verified wraith corpse mechanic (eat.c:1141 pluslvl), drained-level HP/power math (exper.c:251-273 u.uhpinc/u.ueninc), drain-resistance carriers (artilist + do_wear.c). Fixed awkward "zero nutritional weight" framing (real reason is cnutrit==0). v2 audit 2026-05-18 #44: two fixes. (a) Dropped "the bite of a hostile incubus or succubus (see Seduction below)" — under default sysopt.seduce=1 (sys.c:100) the demon's bite is AD_SSEX, not AD_DRLI; AD_SSEX→AD_DRLI substitution at mhitu.c:327-334 only fires when SEDUCE is disabled, so stock-options foocubi don't drain levels. (b) Added potion-of-restore-ability to the recovery options (potion.c:687-691 blessed restores all lost levels at once, uncursed/plain restores one per quaff). Also synced the vampire-bat parenthetical to match the v2 #37 reword ("poisoned bite" not "second bite"). See companion-audit.md. -->

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
problem and the section on *Enchantment Drain* covers its cousin.)

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
<!-- audit 2026-05-17 #73 (re-audit 2026-05-18 v2 #26): corrected substantial errors. Active claw uses some_armor (do_wear.c:2629) — armor only (cloak > body armor > shirt > 1/4 chance for helm/gloves/boots/shield), or if naked a 5-way rn2(5) for ring/amulet/blindfold. NEVER targets weapon. Weapon drain is passive-only (mhitm_ad_ench when YOU melee them, mhitu.c:2509-2514). Active attack DOES print "Your X seems less effective." (uhitm.c:3641). Added Gehennom-only generation, MC defense, corpse warning (eats an intrinsic). v2 re-verified: G_HELL gates generation (monsters.h:2156, makemon.c:1935,1998); some_armor target selection at uhitm.c:3619 (weapon never in scope); passive weapon drain at mhitu.c:2508-2515 with no message; obj_resists 10%/90% at zap.c:1392-1394; Invocation items + Rider corpses always resist at zap.c:1462-1467; MC defense via mhitm_mgc_atk_negated at uhitm.c:3613 (does not apply to passive); corpse attrcurse at eat.c:1270-1275. 0 corrections. See companion-audit.md. -->

**Disenchanters** (`R`, blue) appear only in Gehennom. Their
claw is the silent ascension-killer it's reputed to be, but the
mechanic is more constrained than common lore suggests.

Their **active** claw picks one of your worn armor pieces (cloak
first, then suit, shirt, helm/gloves/boots/shield by weighted
chance) and shaves 1 off its enchantment. If you have no armor at
all, it can instead chew a ring, amulet, or blindfold. **It can't
reach your wielded weapon** with the active attack. The game does
print "Your *thing* seems less effective" each time, so you'll
know when it lands.

Your weapon only takes enchantment damage as a **passive** counter
when you hit them in melee. Three or four melee strikes will take
a +7 sword to +3; that passive drain is silent. Range-killing
sidesteps both attacks at once.

**Defenses.** Every artifact has a 90% chance to resist each
enchantment-drain attempt on itself; ordinary items resist 10% of
the time. The Invocation items (Amulet, Bell, Candelabrum, Book
of the Dead) and Rider corpses always resist. **Magic-cancellation
armor** is the strongest non-artifact armor defense for the active
claw: at MC3 the claw will mostly fail to land. (MC doesn't help
against the passive counter, so still don't melee them.) Range-kill
is the cleanest plan; rings of conflict and pets reliably redirect
them. **Don't eat the corpse**: it strips a random intrinsic.

<!-- audit 2026-05-18 #179: lurker above (ceiling-hider, M1_HIDE+M1_FLY) and trapper (floor-hider, M1_HIDE) verified vs monsters.h:973-998. Both use AT_ENGL with AD_WRAP+AD_PHYS — NOT AD_DGST (header comment at monsters.h:973-980 explicitly notes the 5.0 retcon away from digestion). Damage handler at mhitu.c:1437-1453. Search/telepathy/warning all valid defenses (detect.c:2016-2092 for search; both have no M1_MINDLESS; warnreveal at detect.c:2107-2120 triggers on mlev/4 ≥ warning level). 0 corrections. See companion-audit.md. -->
#### Engulfment from Hiding

Two monsters hide in plain sight until you walk into them. The
**lurker above** (`t`, gray, level 10) hides on the ceiling and
drops onto whoever passes underneath; the **trapper** (`t`,
green, level 12) hides on the floor and engulfs whoever steps
onto it. Both look like ordinary terrain until they trigger.
Engulfment wraps and crushes rather than digesting, but you still
take damage every turn until you cut your way out, with limited
movement
options while inside.

**Defenses:** Searching reveals hidden monsters. *Telepathy*
shows them through the deception. Wearing a *ring of warning* or
a *helm of caution* tips you off before you step. Once engulfed,
attack the host repeatedly; weapons still work from inside.

#### Light Bursts
<!-- audit 2026-05-17 #66: AT_EXPL/AD_BLND yellow light + AT_EXPL/AD_HALU black light verified against monsters.h:1169-1191 and mhitu.c:1623-1650. Both die in their own explosion. Black light is perminvis (makemon.c:1317-1320). Corrected: yellow light is monster level 3, black light is level 5 (not "level 3-5" — that read as a range per monster). Telepathy does NOT help vs black lights (M1_MINDLESS in monsters.h:1188-1189); only warning does. Plain potion of healing only cures blindness when blessed (potion.c:1994-2004); extra/full healing always cures. See companion-audit.md. -->

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

#### Seduction
<!-- audit 2026-05-17 #33: self-audit caught 2 errors in my prior rewrite — items aren't dropped on floor (just unequipped to inventory); demon's succubus/incubus form is random, not based on player gender. v2 audit 2026-05-18 #17: one factual fix plus one safety note. (1) "Depending on its randomly assigned gender" was incomplete: could_seduce at mhitu.c:1980 requires opposite-sex genagr/gendef, so a same-sex foocubus never seduces and just claws. Reworded. (2) Added XL-1 caveat to the "keep one alive to farm" note (the level-drain outcome is fatal at XL 1). The ring-of-adornment interactions (mhitu.c:2019-2110) were added in an initial v2 edit and then reverted as trivia — the section is about the encounter, not a complete catalogue. See companion-audit.md. -->

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
demons charge ⅕). Being asleep or otherwise unresponsive defers
the attempt entirely.

**Strategic note.** At high Cha+Int the encounter is net-positive,
and the armor-removal step strips *cursed* worn pieces too — an
amorous demon can be the cheapest curse-removal in the dungeon.
Some players keep one alive to farm XP and attributes. Don't try
this at experience level 1, though: the level-drain outcome is
fatal.

#### The Riders
<!-- audit 2026-05-18 #150: 4 corrections. (1) "permanently displaced" misreads M3_DISPLACES (monflag.h:175) — that flag means "moves monsters out of its way," not the cloak-of-displacement evasion. (2) "Ignore magic resistance for their signature attacks" — wrong for Death. uhitm.c:3858-3883 shows Antimagic DOES block the 3/20 touch-of-death instakill case. (3) "Eating their corpses is fatal in different ways for each" — wrong; all three trigger the same done(DIED) with killer text "unwisely ate the body of <name>" (eat.c:831-849). (4) "Famine drives you instantly to Weak or Fainting" — overstated; uhitm.c:3791-3795 adds 40-79 hunger units, which doesn't reach Weak from Satiated. -->

On the Astral Plane, three unique `&`-class beings guard the way
to the high altars: **Death**, **Famine**, and **Pestilence**, the
Riders. They are level 30, regenerate while you fight, see
invisible, and shove monsters out of their path. Each hits twice
per turn with AT_TUCH 8d8. **Death's** touch has a 3-in-20 chance
of instant-kill on every hit — magic resistance blocks the
instakill specifically; the regular damage still goes through.
**Pestilence** inflicts the disease that turns into food poisoning
over the next several turns; **Sick resistance** is the only
complete defense (a unicorn horn won't clear the non-vomitable
sickness once it lands). **Famine** adds 40–79 hunger units to a
normal hit, which won't drop you below Hungry in one swing but
will starve you fast across an encounter. Eating any Rider corpse
is straight-up fatal (`done(DIED)`). A mercy in 5.0: if Pestilence
or Famine land their first attack on a turn, the second downgrades
to a stun.

**Defenses:** An **amulet of life saving** is the best insurance
on Astral, full stop. Magic resistance is what stops Death's
instakill (but not its 8d8 baseline). Sick resistance handles
Pestilence. Carry plenty of food (Famine's drain bypasses normal
nutrition) and a unicorn horn for the stun secondary effects. In
a crowd, a ring of conflict can keep the Riders tangled fighting
nearby monsters instead of chasing you, sometimes long enough to
reach the altar.

#### Choking
<!-- audit 2026-05-17 #68: eat-while-satiated death (eat.c:248, 286 done(CHOKING)) and warning string (eat.c:3314) verified. Corrected "if you confirm, you're dead" — the prompt only appears with paranoid_confirmation:eating enabled (default off); death only fires at uhunger >= 2000 with a 1/20 escape, AND Breathless creatures never choke (eat.c:258-266). Added the amulet of strangulation path (timeout.c) which is the other major choking death. See companion-audit.md. -->

If you push past Satiated and keep eating, you can choke and die.
The game prints "You're having a hard time getting all of it down"
as a warning; if you have eating-confirmations turned on it'll also
prompt you. Past a hard nutrition threshold the choke check fires
and, unless you're Breathless or pass a 1-in-20 escape, kills you
instantly.

**The other path to choking is the amulet of strangulation.** Worn,
it puts a short countdown on your throat and kills you when it runs
out. Take it off. Magic resistance doesn't help (it's a physical
attack); polymorphing into a Breathless form does.

**Defense:** Don't eat above Satiated. Be paranoid about unidentified
amulets.

#### Deadly Poison
<!-- audit 2026-05-17 #7: 7 claims verified, 1 corrected (Famine corpse missing from instakill list). See companion-audit.md. -->

A handful of monsters (pit vipers, killer bees, cobras, some
spiders) have a poison-damage branch that can deliver 10 to 34
extra HP of damage on top of the normal hit. At full HP you
usually survive; at low HP or while burdened, it can outright
kill you. The "extra-damage" roll fires about 1 in 240 per
qualifying hit. Eating any Rider corpse (Death, Pestilence, *or*
Famine) is genuinely instantly fatal regardless of HP.

**Defenses:** Poison resistance makes you immune. Most characters
can get this early by eating enough appropriate corpses. It's one
of the first intrinsics worth acquiring.

#### Disintegration
<!-- audit 2026-05-18 #137: corrected the "wide-angle disintegration beam" claim — there's no such thing in 5.0. The only player-facing AD_DISN source is the black dragon's breath (monsters.h:1520, ZT_BREATH(ZT_DEATH) at zap.c:4464-4493). The beholder is the only other AD_DISN monster and it's #if 0-gated. Also clarified worn-armor priority destruction (shield first per zap.c:4476-4479, then suit+cloak per zap.c:4480-4486), and that amulet of life saving does rescue you (end.c:1081 catches DIED; the breath-handling at zap.c:4487-4492 explicitly destroys cloak/shirt "in case of life-saving or bones"). -->

A black dragon's breath is the only thing in the game that
disintegrates you. There's no other monster, spell, or wand that
deals the same damage type.

**Defenses:** Disintegration resistance (from eating a black dragon
corpse or wearing black dragon scale mail) gives full immunity.
**Reflection** bounces the beam back — and since the dragon has
no reflection of its own, the bounce often kills it outright. Magic
resistance does **not** help.

**Without disintegration resistance**, the game tries to save your
worn armor before disintegrating you: the breath destroys your
**shield** first if you have one, then your **body armor**; only
if neither is worn do you die outright (with your cloak and shirt
destroyed in the process). So a shield of reflection that *fails*
to reflect at least eats one breath for you before being lost.
An amulet of life saving still rescues you from the fatal case,
though you lose any armor it took.

#### Genocide
<!-- audit 2026-05-17 #71: confused-uncursed-scroll self-genocide verified at read.c:1737 + do_genocide PLAYER+REALLY branch at lines 2838-2972 (killer = "genocidal confusion"). Section is 2 sentences with a single correct factual claim. 0 corrections. See companion-audit.md. -->

Reading an uncursed scroll of genocide while confused can genocide
your own race. Don't do this.

#### Delayed Deaths
<!-- audit 2026-05-18 #93: timer + cure mechanics verified vs timeout.c/pray.c/eat.c/potion.c/trap.c. Corrected: sliming polymorph cure requires a flame-bodied or slime-proof form (polyself.c:842), not any polymorph; "burdened may not get even one turn" + "stay unburdened near water" duplicated the drowning error already fixed elsewhere; vomiting only cures SICK_VOMITABLE (food poisoning), not Pestilence's SICK_NONVOMITABLE. Withering correctly absent (doesn't exist in 5.0). Added 10-turn slime timer, food-poisoning 10-19 turn range, and Pestilence-specific paragraph. See companion-audit.md. -->

Not every fatal threat kills instantly. Several give you a few
turns to react. Knowing the warning signs and the cures can save
a run.

**Sliming.** Being hit by a green slime (or eating its glob, or
being digested by one as a polyform) starts a ~9-turn transformation
into a green slime yourself — dead. **Cures:** burn the slime off
with fire (a wand of fire zapped at yourself, a scroll of fire read
at self, a fire trap, a red dragon's breath); polymorph into a
flame-bodied or slime-immune form; cancellation negates the touch
attack; the spell of *cure sickness* clears the timer. An **amulet
of unchanging** blocks the contagion entirely and even aborts a
transformation already underway. Prayer would cure it, but green
slime lives in Gehennom where prayer fails, so don't plan on it.
Fire is the most reliable cure.

**Illness (food poisoning).** Eating a rotten corpse or certain
attacks (giant ant, etc.) gives you food poisoning, which kills in
10–19 turns ("You feel deathly sick."). **Cures:** a unicorn horn
(apply it), pray, eat a eucalyptus leaf, or vomit (by being
satiated and eating more). Vomiting from other causes also cures
food poisoning. Poison resistance does NOT protect against food
poisoning — that's *sickness resistance*, a separate intrinsic.

**Pestilence's terminal illness** is the harder cousin: it's
`SICK_NONVOMITABLE`, so vomiting won't clear it, and the timer is
Constitution-dependent (~20+Con turns). The cures that *do* work:
unicorn horn, prayer, eucalyptus leaf.

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
*Drowning* in Dangerous Encounters for the full picture.

**Strangulation.** Wearing a cursed amulet of strangulation slowly
kills you over a few turns. **Cure:** remove the amulet (requires
uncursing it first, since cursed amulets can't be removed: use a
scroll of remove curse, holy water, or prayer).

#### The Displacer Beast
<!-- audit 2026-05-17 #42: rewrote section. Prior version described it as having cloak-of-displacement style image-offset; this is wrong. The "displacer" mechanic is M3_DISPLACES (barge-through): 50% chance on player melee that it swaps places with you instead of being attacked (hack.c:1972). Corpse intrinsic Displacement claim verified (eat.c:1265). See companion-audit.md. -->
<!-- audit 2026-05-18 #106: dropped the "lure it adjacent to a moat or lava and let it swap itself in" tactic — wrong. hack.c:1972 ends with goodpos(u.ux0, u.uy0, mtmp, GP_ALLOW_U); teleport.c:134-162 goodpos refuses to place a non-swimmer/non-flier in water and a non-fire-resistant non-flier in lava. Displacer beasts have none of those. Even if the hero were standing IN the hazard via water-walking/levitation, the beast still can't swap there. -->


The **displacer beast** (`f`, blue, 5.0 addition) is a tiger-sized
feline with AC −10 and three attacks per turn (4d4 / 4d4 / 2d10).
The misleading name: it isn't displaced in the cloak-of-displacement
sense. Its trick is the opposite, when you melee it, half the time
it **swaps places with you** instead of taking the hit, which can
pull you off Elbereth, out of a doorway, or onto a trap. Ranged
attacks (wand, spell, thrown) bypass the swap entirely. It also
has **MR 0** — extremely unusual for a level-12 monster, where
most peers carry 10–70% resistance — so sleep, paralysis, and
charm/taming all land with no save. Speed 12, so a speed-boosted
hero outpaces it. (Don't bother trying to swap it into a moat or
lava — the swap only fires if the destination square is
survivable for the beast, and water/lava aren't.)

**Tame one and you have one of the best pets in the game.** AC
−10, three attacks (4d4 claw / 4d4 claw / 2d10 bite), speed 12,
and the swap mechanic still works in your favor: hostiles meleeing
your pet displacer beast trigger the same 50% place-swap, so the
attacker often ends up next to *you* instead of biting the pet.
Charm monster works first try; a scroll of taming with no MR roll
to fail is essentially guaranteed. A tame displacer beast will
walk into late-game fights and walk out, eating tough hostiles
while taking minimal retaliation.

Eating the corpse gives you cloak-style displacement for a few turns:
monsters target a phantom image one square off from where you
really are and miss accordingly. Note that this is a different
mechanic from the beast's own place-swap, despite the shared
name: you get the same effect as wearing a cloak of displacement,
not the ability to swap places with attackers.

#### The Genetic Engineer
<!-- audit 2026-05-17 #12: 14 claims verified, 1 corrected (hit message wording was the corpse string); added magic resistance to defenses. See companion-audit.md. -->

The **genetic engineer** (`Q`, green) shares its symbol class
with the quantum mechanic but plays differently: where a quantum
mechanic *teleports* its target on a hit, a genetic engineer
*polymorphs* its target. One claw and, unless you have
*Unchanging* or magic resistance, you become something else: same
roll as any other uncontrolled polymorph source, with the dramatic
message "you are subjected to a freakish metamorphosis."
Engineers also teleport on their own, so range alone won't save
you forever.

**Defenses:** *Unchanging* (immune), magic resistance (also fully
blocks the polymorph), kill it before it closes, or accept the
next several turns of the dungeon playing as something else. The
engineer has a short cooldown between successful polymorph hits,
so the encounter is survivable even without unchanging if you can
finish quickly.

**The corpse is a tool.** Eating a genetic engineer corpse is
mechanically identical to eating a doppelganger corpse: the
same uncontrolled polymorph, just with louder flavor text. The
practical use is the same as the doppelganger's: tin it, and you
have a portable polymorph source. Pair a tin with *polymorph
control* and you have a controlled polymorph that survives
Gehennom's hot ground. The first engineer that kills you is a
loss; the second one in your bag is a kit.

---

### Making Friends
<!-- audit 2026-05-17 #36: ~25 claims verified, 4 corrected (pet-curse-avoidance overstated, tameness loss sources narrowed, displacement guards corrected, charm monster spell is multi-target not single). See companion-audit.md. -->

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
across many turns is a strong tell.

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
  a 3×3 radius (5×5 when confused)
- **Magic trap effects** occasionally produce taming

Taming isn't limited to small animals: with a scroll of taming or
the charm monster spell, you can recruit a purple worm to swallow
your enemies whole, a dragon to breathe fire at them, a titan to
crush them underfoot. The exclusion list is substantial, though:
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

#### Keeping Your Pet Alive

Pets die from the same things you do: traps, poison, powerful
monsters, drowning in water. Keep an eye on your companion's
health (`;` to farlook) and don't lead it into fights it can't
win. A dead pet is not just a loss of utility; it's a cold feeling
in the pit of your stomach.

If you change levels and your pet isn't adjacent, it won't follow.
The game tells you: *"You have a sad feeling for a moment."* Your
pet is still alive on the previous level, but its loyalty is
ticking down. Go back for it before it forgets you were friends.

Current editions have added two things that veteran pet-owners should know.

First: your pet eats for a reason beyond loyalty. The same corpse
mechanics that grant you resistances apply to pets as well. A pet that
dines on the right monsters will gain resistances: fire resistance, cold
resistance, whatever the dungeon's terrible buffet was offering. A
well-fed pet is also a better-armored one. This is not something you can
reliably engineer, but it's a reason to let your pet eat rather than
scooping up every corpse yourself.

Second, and more importantly: pets can now be revived. If your companion
falls in battle, stand on its corpse at a co-aligned altar and pray.
The gods, in their occasional mercy, may return it to you. This is a
last-resort miracle, not a renewable strategy: your prayer timeout,
your alignment, and a certain amount of luck all factor in. But it means
that the large cat you've carried since level 3, the one who has earned
names and battle scars and the terrified respect of every dungeon denizen
you've walked past, is worth a detour to the nearest temple before you
write it off. The dungeon kept this secret for a long time. Now you know.

---

## Part Four: Gear and Provisions

> *Much of the item data in Part Four has been verified against
> Kevin Hugo and Dylan O'Donnell's comprehensive 3.4.3 spoiler
> files, updated where 5.0 of the game has changed.
> Identification methods owe a debt to David Damerell's Object
> Identification FAQ and Kieron Dunbar's wand ID guide, both
> cornerstones of the RGRN community spoiler tradition.*

---

### A Practical Identification Strategy

Here is the central puzzle of the Mazes, and the thing that kills
more promising expeditions than any monster: you will find dozens of
items, and you won't know what most of them are.

That potion might heal you or it might make you hallucinate. That
scroll could enchant your armor or destroy it. That ring could grant
you invisibility or slowly starve you to death. In the Mazes,
ignorance is not bliss. Ignorance is death by unidentified wand.

Every game, the dungeon shuffles the deck. Potions, scrolls, wands,
rings, amulets, and spellbooks are all given randomized appearances.
The "milky potion" in this game might be healing; in your next game
it might be paralysis. The only things that stay consistent between
games are the item classes themselves (a `!` is always a potion, a
`?` is always a scroll) and the prices, which turn out to be the
single most powerful identification tool you have.

<div><figure style="margin: 1.5em 0; text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 736" role="img" aria-label="The identification flowchart" style="max-width: 760px; width: 100%; height: auto; font-family: 'EB Garamond', 'Garamond', 'Georgia', serif;"><title>The Identification Flowchart</title><defs><marker id="arrowhead" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a5a5a"/></marker><style>.start{fill:#E8F4FD;stroke:#3B6FA0;stroke-width:2}.decision{fill:#FFF4E6;stroke:#B5651D;stroke-width:2}.action{fill:#F0F9E8;stroke:#5B8E3A;stroke-width:2}.final{fill:#FCE8E6;stroke:#A14A3F;stroke-width:2}.label{font-size:18px;fill:#1f2933;text-anchor:middle}.startlbl{font-size:19px;font-weight:600;fill:#1f2933;text-anchor:middle}.branch{font-size:16px;font-style:italic;fill:#5a5a5a}.edge{fill:none;stroke:#5a5a5a;stroke-width:1.5}</style></defs><rect class="start" x="40" y="20" width="320" height="50" rx="25" ry="25"/><text class="startlbl" x="200" y="51">Found an item</text><path class="edge" d="M 200 70 L 200 100" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="100" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="133">Can you reach an altar?</text><path class="edge" d="M 360 128 L 430 128" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="121" text-anchor="middle">yes</text><rect class="action" x="430" y="100" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="133">Drop it. Check BUC.</text><text class="branch" x="210" y="172">no</text><path class="edge" d="M 200 156 L 200 190" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="190" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="223">Is your pet nearby?</text><path class="edge" d="M 360 218 L 430 218" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="211" text-anchor="middle">yes</text><rect class="action" x="430" y="184" width="290" height="62" rx="8" ry="8"/><text class="label" x="575" y="210">Drop it. Pet avoids it?</text><text class="label" x="575" y="232" style="font-size: 16px;"><tspan style="font-style: italic; fill:#5a5a5a;">yes</tspan>: it's cursed; <tspan style="font-style: italic; fill:#5a5a5a;">no</tspan>: it's safe</text><text class="branch" x="210" y="262">no</text><path class="edge" d="M 200 246 L 200 290" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="290" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="323">Can you reach a shop?</text><path class="edge" d="M 360 318 L 430 318" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="311" text-anchor="middle">yes</text><rect class="action" x="430" y="290" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="323">Check price.</text><text class="branch" x="210" y="362">no</text><path class="edge" d="M 200 346 L 200 380" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="380" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="413">Is it a wand?</text><path class="edge" d="M 360 408 L 430 408" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="401" text-anchor="middle">yes</text><rect class="action" x="430" y="380" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="413">Engrave-test it.</text><text class="branch" x="210" y="452">no</text><path class="edge" d="M 200 436 L 200 470" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="470" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="503">Spare ring or potion with a sink?</text><path class="edge" d="M 360 498 L 430 498" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="491" text-anchor="middle">yes</text><rect class="action" x="430" y="470" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="503">Drop ring or dip potion.</text><text class="branch" x="210" y="542">no</text><path class="edge" d="M 200 526 L 200 560" marker-end="url(#arrowhead)"/><rect class="decision" x="40" y="560" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="593">Is it safe to use-test?</text><path class="edge" d="M 360 588 L 430 588" marker-end="url(#arrowhead)"/><text class="branch" x="395" y="581" text-anchor="middle">yes</text><rect class="action" x="430" y="560" width="290" height="56" rx="8" ry="8"/><text class="label" x="575" y="593">Try it carefully.</text><text class="branch" x="210" y="632">no</text><path class="edge" d="M 200 616 L 200 660" marker-end="url(#arrowhead)"/><rect class="final" x="40" y="660" width="320" height="56" rx="10" ry="10"/><text class="label" x="200" y="693">Read a scroll of identify.</text></svg><figcaption style="font-style: italic; color: #5a5a5a; font-size: 0.9em; margin-top: 0.5em;">The identification flowchart: cheapest method first, scroll of identify last.</figcaption></figure></div>

#### Blessed, Uncursed, Cursed
<!-- audit 2026-05-18 #88 (re-audit 2026-05-18 v2 #68): altar/pet test mechanics, Priest BUC sense, cursed armor sticks, cursed gain-level rises, luckstone +luck, holy/unholy water dipping all verified vs do.c/dogmove.c/objnam.c/attrib.c/potion.c. Corrected: blessed scroll of identify gives at least 2 items + 1-in-5 chance whole pack (was "every item"); cursed scroll IDs only itself on first cursed read (read.c:2074-2081), not "single item." Cursed teleport scroll is a *level* teleport (not "somewhere terrible"). Added how to make holy water (pray on co-aligned altar with potions of water). v2 re-confirmed: altar flash do.c:379-388; pet step-around dogmove.c:535-538 (with starvation exception); cursed gain-level message at potion.c:1083-1109; level-tele on cursed/confused scroll at read.c:2015-2025; holy water making at pray.c:2336-2339; Priest natural BUC at invent.c:2763,3545; blessed scroll identify branch at read.c:2086-2092; cursed scroll only-IDs-itself first read at read.c:2074-2081. 0 corrections. See companion-audit.md. -->

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

The pattern is consistent: blessed items are helpful beyond their
description, uncursed items work as advertised, and cursed items find
creative ways to ruin your day. A blessed luckstone passively
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
works anywhere.

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
read one of that type, then one item per cursed read after.

#### The Price Is Right
<!-- audit 2026-05-17 #32: 50+ price/multiplier claims verified across all item classes, 1 corrected (sell-offer blurb ¼ → ½ and ³⁄₁₆ → ³⁄₈). Live JS computeBuy/computeSell match shk.c exactly. Close call: angry-shop surcharge is sticky beyond bill payment (only cleared on new-customer transition). v2 audit 2026-05-18 #29: one factual fix. The Angry-shop paragraph said the +33% surcharge stays "until you pay your bill in full" — backwards. shk.c:2663 pacify_shk(shkp, FALSE) does NOT clear the surcharge flag; it's only cleared by pacify_shk(shkp, TRUE) at shk.c:302, 793 (bones-load and new-customer transitions). The pass-1 close-call note had it right, but the body text was never corrected. Reworded: paying the bill clears the bill but not the surcharge; the flag sticks for the rest of your visits to that shopkeeper. Verified every Cha/Tourist multiplier and shop-state edge against shk.c. JS widget computeBuy/computeSell still match get_cost/set_cost exactly. See companion-audit.md. -->

Shopkeepers are, without exaggeration, your most important
identification tool. Every unidentified item has a fixed base price
that depends on what it actually is. When you pick up an item in a
shop, the shopkeeper quotes you a price derived from that base price,
modified by your Charisma and the shopkeeper's markup.

> *Shopkeeper pricing was first documented in detail by Gregory
> Bond's Shopping Spoiler, HTML-formatted by Kate Nepveu and
> hosted on steelypips.org. David Damerell's Object Identification
> Spoiler expanded the price-based identification techniques. The
> mechanics below draw from both.*

The key insight: items in the same category that share a base price
are in the same **price group**. If you know the price, you can
narrow down the possibilities enormously, sometimes to just two or
three candidates.

Here's how to do it. Pick up an item in a shop and note the price
quoted. With average Charisma (11-15) the quoted **buy** price equals
the base price exactly, while the **sell** offer is half of base. Low
Charisma pushes buy prices up sharply (×2 at Cha ≤ 5); high Charisma
pulls them down (×½ at Cha ≥ 19). Sell prices are mostly unaffected
by Charisma; they only shift when the player looks like a mark, in
which case sell drops to a third of base and buy rises to 4/3. Three
visible cues count as "looking like a mark," and they all have the
same effect (and don't stack): wearing a **dunce cap**, playing a
**Tourist** below experience level 15, or wearing a **Hawaiian shirt
visibly** (no body armor or cloak over it). All three trigger the same
+33% buy markup; the rest of this guide refers to them collectively
as *Tourist*. You don't need to memorize the exact formulas — what
matters is grouping: items quoted at similar prices are in the same
price tier.

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

##### Quoted-price conversion

The per-class tables below show **buy prices at Cha 11–15 with no
Tourist markup** (the baseline). To recover the base price from a
quoted price under different conditions, find the row that matches
your situation and read across; or, given a base price you suspect,
read the price you'd be quoted. *T Cha* rows are the same Cha bands
with the Tourist surcharge stacked on.

| Modifier            |   Mult |  20 |  50 |  60 |  80 | 100 | 150 | 175 | 200 | 300 |
|---------------------|-------:|----:|----:|----:|----:|----:|----:|----:|----:|----:|
| Cha 6–7             |  ×1.5  |  30 |  75 |  90 | 120 | 150 | 225 | 263 | 300 | 450 |
| Cha 8–10            |  ×1.33 |  27 |  67 |  80 | 107 | 133 | 200 | 233 | 267 | 400 |
| Cha 11–15           |  ×1.00 |  20 |  50 |  60 |  80 | 100 | 150 | 175 | 200 | 300 |
| Cha 16–17           |  ×0.75 |  15 |  38 |  45 |  60 |  75 | 113 | 131 | 150 | 225 |
| Cha 18              |  ×0.67 |  13 |  33 |  40 |  53 |  67 | 100 | 117 | 133 | 200 |
| Cha 19+             |  ×0.5  |  10 |  25 |  30 |  40 |  50 |  75 |  88 | 100 | 150 |
| T Cha 6–7           |  ×2.0  |  40 | 100 | 120 | 160 | 200 | 300 | 350 | 400 | 600 |
| T Cha 8–10          |  ×1.78 |  36 |  89 | 107 | 142 | 178 | 267 | 311 | 356 | 533 |
| T Cha 11–15         |  ×1.33 |  27 |  67 |  80 | 107 | 133 | 200 | 233 | 267 | 400 |
| T Cha 16–17         |  ×1.00 |  20 |  50 |  60 |  80 | 100 | 150 | 175 | 200 | 300 |
| T Cha 18            |  ×0.89 |  18 |  44 |  53 |  71 |  89 | 133 | 156 | 178 | 267 |
| T Cha 19+           |  ×0.67 |  13 |  33 |  40 |  53 |  67 | 100 | 117 | 133 | 200 |

Numbers are NetHack's integer-rounded prices, not the round-number
multiplier reapplied. Sell offers are unaffected by Charisma, so
they aren't shown; an unangry shopkeeper offers ½ of base on a sell
(³⁄₈ on unidentified items from an unfamiliar shop).

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
Yendor imitations ($0). Price doesn't help here. You'll need to rely
on other methods.

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

The single most useful wand-identification trick costs you nothing.
Apply a wand by engraving on the floor with it
(command: `E`, then select the wand). What happens tells you what
the wand is:

| What you see when you engrave              | Wand type                       |
| ------------------------------------------ | ------------------------------- |
| *"A lit field surrounds you"*              | light                           |
| *"The floor is riddled by bullet holes"*   | magic missile                   |
| *"Gravel flies up from the floor"*         | digging                         |
| *"A few ice cubes drop from the wand"*     | cold                            |
| *"Flames fly from the wand"*               | fire                            |
| *"Lightning arcs from the wand"* (may blind) | lightning                     |
| *"The bugs on the floor stop moving!"*     | sleep or death                  |
| You feel self-knowledgeable                | enlightenment                   |
| Floor reveals secret features              | secret door detection           |
| Monsters appear next to you                | create monster                  |
| Pre-existing engraving randomizes          | polymorph                       |
| Pre-existing engraving "vanishes"          | cancellation, make invisible, or teleportation (test against floor with no prior writing to disambiguate) |
| "*The wand unsuccessfully fights your attempt to write!*" | striking (this exact phrasing is striking-only) |
| "*The bugs on the floor slow down!*"       | slow monster                    |
| "*The bugs on the floor speed up!*"        | speed monster                   |
| You write in the dust with no special-case message | nothing, undead turning, opening, locking, probing, or stasis — zap-test to disambiguate |
| Wish prompt appears                        | **wand of wishing** (yes, engrave gives you the wish — don't be afraid to engrave the suspected $500 wand) |

The engrave test costs one charge per wand but preserves the rest.
With one zap you can sort most wands into clear categories. For
wands that just write in the dust, you'll need further testing:
zap them at a monster or in a safe direction.

**Warning:** In 5.0, cursed wands may **explode** when used to
engrave. BUC-test your wands before engraving with them.

<!-- audit 2026-05-18 v2 #34: dosinkring at do.c:498-650 verified — 28 ring types each produce a distinctive message; searching and slow digestion "goto giveback" and are dropped back on the floor identified (do.c:507-516); other rings usually consumed with a 1/20 backup chance and 1/5 buried chance (do.c:649-660). Section correctly defers detail to the Sinks subsection. 0 corrections. See companion-audit.md. -->
#### The Sink Test (Rings)

If you find a sink, you can drop a ring down it. Each ring type
produces a characteristic message, identifying the ring. See
[Sinks](#sinks) under Points of Interest for the full
message-to-ring table; the short version is that searching and
slow digestion come back to you (free identification), and every
other ring is consumed.

#### Use-Testing (The Careful Way)
<!-- audit 2026-05-18 #79 (re-audit 2026-05-18 v2 #21): substantial engrave-test table rewrite. Verified against engrave.c + zap.c: real messages are "Flames fly from the wand" (fire), "A few ice cubes drop" (cold), "Lightning arcs from the wand" (lightning), "Gravel flies up" (digging), "riddled by bullet holes" (magic missile not digging), polymorph randomizes existing engraving (not "vanishes"), cancellation/make-invisible/teleportation all share the same "vanishes" message. Wand-of-wishing engrave DOES grant the wish (zap.c:2575-2585) — reverse of previous warning. Also corrected unicorn-horn neutralization (sickness → fruit juice, not water; blindness/confusion/hallucination → water). Confused remove curse randomizes BUC of uncursed items (blessorcurse, 50/50), doesn't strictly curse. v2 re-audit confirmed every wand message against engrave.c:604-728 (striking unique "fights your attempt to write", sleep+death both "bugs stop moving", slow/speed/poly distinctive, dust-class wands silent), zapnodir light at zap.c:2549, wishing at zap.c:2575-2585, cursed-wand explosion at engrave.c:794 (1% per cursed engrave per hack.h:1410). 0 corrections. See companion-audit.md. -->

When you don't have access to a shop or a sink, you can sometimes
figure out what an item is by using it carefully. Here's the approach
for each category:

**Potions.** The safest test is to throw a potion at a monster and
observe the effect. Throwing avoids the risk of drinking something
lethal. If a potion heals the monster, it's some kind of healing
potion. If the monster speeds up, it's speed. If the monster becomes
invisible, well, you've learned something (and now have an invisible
monster to deal with).

You can also dip items into potions. Dipping a poisonable weapon
(dagger, arrow, spear) into a potion of sickness will poison it,
confirming the potion's identity (it won't poison a long sword or
other non-poisonable weapon). Dipping a unicorn horn into a potion
of **confusion**, **hallucination**, or **blindness** turns it
into water; dipping into a potion of **sickness** turns it into
fruit juice.

**Scrolls.** Reading is risky. Some scrolls (destroy armor, amnesia,
punishment) are outright harmful. The safest approach is to price-ID
first, then read scrolls from safe price groups. If you must test
blind: take off your armor before reading a scroll that might be
destroy armor. Read from a position where teleportation won't be
disastrous.

Confused reading produces different effects for many scrolls and is
sometimes useful. A confused scroll of remove curse **randomizes
the BUC of your uncursed items** (about half end up blessed, half
cursed) and leaves already-cursed items cursed, so it's a way to
get blessings cheaply, not a curse-removal tool. Don't read it
confused if you need to uncurse something.

**Rings.** First, confirm the ring is not cursed (altar or pet test).
Then put it on. Many rings produce an immediate message or visible
effect: you start levitating, you become invisible, you feel
stronger. If nothing obvious happens, check your stats and inventory
for subtle changes (protection, searching). Take it off quickly if
you start feeling hungry faster than normal (hunger ring) or if
monsters seem to be approaching more aggressively (aggravate monster).

**Amulets.** Most amulets are safe to wear briefly. Put it on, wait
a few turns, take it off. The dangerous ones (strangulation, restful
sleep) are usually cursed, so check BUC first. An amulet of ESP
reveals itself if you go blind while wearing it (you'll see monsters
as brain-shapes). Amulet of reflection is trickier to detect, but
you'll notice it when a ray bounces off you.

**Armor.** Magical armor reveals itself when worn: speed boots make
you faster, a cloak of invisibility makes you invisible. But trying
on unknown armor is **dangerous in a shop**: if the item is cursed,
it welds itself to you, you can't drop it, and the shopkeeper still
expects payment. Worse, the most commonly auto-cursed armor types
(fumble boots, levitation boots, gauntlets of fumbling) are exactly
the ones that masquerade as desirable boots and gloves. **Always
verify BUC before wearing unknown armor in a shop.** Shops don't
have altars, so the standard altar-drop BUC check isn't available
in-store; the in-shop options are the pet-step test (your pet
refuses to walk over cursed items, so lure it past the suspect
square), Priest intrinsic BUC sense, or a scroll of identify from
your own inventory.

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
abnormally heavy and resists being kicked.

**The pick-up test.** A loadstone auto-curses itself the moment
you pick it up, and a cursed loadstone refuses to be dropped at
all — the game prints "For some reason, you cannot drop the
stone!" and the stone stays in your pack. If you pick up a gray
stone and it weighs you down suspiciously, try to drop it. If
you can't, you're stuck with a cursed loadstone until you can
uncurse it (holy water, scroll of remove curse, prayer) — then
drop it.

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
<!-- audit 2026-05-17 #2: 5 claims verified, 1 corrected (N keystroke only works in number_pad mode; default vi-keys binds N to run-north — the cross-layout shortcut is C for #call). See companion-audit.md. -->

As you gather clues, use the `#name` command to track what you
know. You can **call** an entire item class by a name you choose.
For example, if you've determined that "fizzy potions" are in the $200
price group, call them "fizzy=$200" so you don't forget. If you later
throw one at a monster and it speeds up, you can rename the class to
"speed."

This habit of annotating your discoveries is what separates adventurers
who die on level 8 from adventurers who reach the Castle. The dungeon
doesn't keep notes for you. You have to do it yourself.

#### A Practical Strategy
<!-- audit 2026-05-18 #151 (re-audit 2026-05-18 v2 #45): ~39 lines, no substantive errors. Altar-flash BUC verified (do.c:379-389); engrave-test costs one charge (engrave.c:792 + zap.c:2520); wand of digging auto-IDs from engrave message (engrave.c:684-704); all 12 amulet costs are 150 (objects.h:834). One prose nit: "A wand that freezes your engraving is cold" — actual WAN_COLD engrave message is "A few ice cubes drop from the wand" (engrave.c:658-661); the vanish/freeze branch only triggers when overwriting an existing BURN engraving. Reworded to "drops ice cubes." v2 re-confirmed all mechanical claims: ice-cubes wand message accurate for the fresh-floor engrave-test, amulet uniform 150gp pricing, escalation order (altar/shop free → engrave-test cheap → use-test risky → identify scrolls last) matches standard NetHack identification priority. 0 corrections. See companion-audit.md. -->


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
methods: amulets (all the same price), spellbooks (dangerous to
read if unknown), and the one stubborn potion in the $50 group that
you can't quite pin down.

The whole system is about reducing uncertainty with the cheapest,
safest method first. Altars and shops are free. Engrave-testing costs
one charge. Use-testing costs more and carries risk. Scrolls of
identify are the precious last resort. Work through the list in order
and you'll rarely be surprised.

---

### Provisions and Dining
<!-- audit 2026-05-18 #77: many claims verified clean (food nutritions, cannibalism penalty, prayer tiers, slow digestion, tin opening, lizard cures stoning, newt-zap, wraith corpse level, stalker corpse invis+see-invis). Corrected 6: gelatinous cube grants only fire/cold/shock/sleep (not poison/acid/stoning); disenchanter corpse STRIPS an intrinsic (not "intrinsic protection"); hunger threshold table off-by-one (now uses strict bounds); encumbrance kicks in at Stressed not Burdened (eat.c:3197 near_capacity > SLT_ENCUMBER); split fire-giant from fire-ant row (giants give Str on eat); red/brown mold also grant poison resistance; clarified vegetarian-vs-vegan eggs distinction. v2 audit 2026-05-18 #38: three factual fixes. (a) Weak status effect was "movement slowed" — actually a -1 Str ATEMP penalty (attrib.c:471 via eat.c:3455), not a speed change. (b) "Blessed tins open instantly" was incomplete — that's only with a blessed tin opener (eat.c:1740-1745); with an ordinary tin opener a blessed tin still rolls rn2(2), so 50/50 between instant and one turn. (c) Glob lifetime "about 25 turns to vanish" misread the shrink interval — globs lose 1 weight unit per ~25 turns (mkobj.c:1487-1490 comment "twice as long as the average corpse"), so a fresh weight-20 glob lasts ~500 turns. Also corpse-eat window expanded from "a few turns" to 30-50 turns (rotted threshold at eat.c:1887-1939 makes corpses safe for ~50 turns). See companion-audit.md. -->

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
[Divine Relations](#divine-relations)). Prayer cures hunger if
your god is willing to help.

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
- Some corpses are harmful (floating eyes paralyze you, green slimes
  turn you into slime, cockatrice corpses kill you). Know which
  corpses are safe before eating.

**Food rations** are the emergency backup. 800 nutrition, weight
20, common in shops. Carry two or three for the times you don't
have a fresh kill in front of you. You don't need to hoard them.

**Lembas wafers** are the gold standard: 800 nutrition at only 5
weight, the best ratio in the game. Elven characters find these
more often.

**Tripe rations** are terrible for you (your character retches) but
pets love them. Save tripe for your pet.

**Tins** are preserved food that never spoils. They take several
turns to open (one turn with a tin opener, three with a dagger,
more with bare hands). Blessed tins open quickly — instantly with
a blessed tin opener, otherwise a coin-flip between instant and
one turn. A tin of spinach increases your strength.

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

| Corpse                  | Effect                                                                 |
| ----------------------- | ---------------------------------------------------------------------- |
| Floating eye            | Telepathy (but paralyzes you too)                                      |
| Killer bee              | Poison resistance                                                      |
| Fire giant              | Fire resistance + Strength                                             |
| Fire ant                | Fire resistance                                                        |
| Red mold                | Fire resistance + poison resistance                                    |
| Winter wolf             | Cold resistance                                                        |
| Blue jelly              | Cold and poison resistance                                             |
| Brown mold              | Cold resistance + poison resistance                                    |
| Yeti                    | Cold resistance                                                        |
| Quivering blob          | Poison resistance                                                      |
| Acid blob               | Acid and stoning resistance                                            |
| Gelatinous cube         | Fire, cold, shock, and sleep resistance (chance for each per eat)      |
| Brown or black pudding  | Cold, shock, and poison resistance                                     |
| Gray ooze               | Fire, cold, and poison resistance                                      |
| Wraith                  | Gain an experience level                                               |
| Giant                   | Increase strength                                                      |
| Lizard                  | Cures stoning in progress                                              |
| Newt                    | May restore 1 to 3 mana                                                |
| Stalker                 | Invisibility (and see invisible)                                       |
| Tengu                   | Teleportitis / teleport control                                        |
| Disenchanter            | **STRIPS** a random intrinsic. Never eat.                              |

Eating for intrinsics is the highest-leverage habit in the early
and mid game. Poison resistance should be a top
priority, and a gelatinous cube is the highest-density source of
ascension-kit intrinsics in the game. Each resistance is a *chance*
per eat (not a guarantee), so eat *every* one of these you find,
not just the first.

**Globs vs corpses.** Puddings (gray ooze, brown pudding, black
pudding) and acid blobs in 5.0 leave **globs** instead of corpses.
Globs sit on the floor and shrink slowly (about one weight unit
every 25 turns, so a fresh glob lasts about 500 turns — twice as
long as a corpse) — and globs of the same color stack, so saving
up a pile of brown pudding globs lets you re-roll shock resistance
until you get it.

#### Food Strategy

1. Eat fresh corpses as your primary food source.
2. Save food rations and lembas wafers for emergencies.
3. Eat intrinsic-granting corpses deliberately (even if not hungry).
4. Pray when Weak or Fainting if you have nothing to eat.
5. Buy food from shops when you can afford it.
6. Don't carry more food than you need. It's heavy.

---

### The Apothecary
<!-- audit 2026-05-17 #34: 50+ price/effect/alchemy claims verified, 1 corrected (uncursed extra/full healing also raise maxHP, not blessed-only). v2 audit 2026-05-18 #15: one factual fix — potion of speed grants permanent intrinsic Fast whenever `!cursed` (potion.c:1066), not just when blessed; blessing only extends the temporary timer that overlays it. Voice: replaced colon-stitched sentences with periods in the lead-in, the Water clarification, and the Speed line per the punctuation ladder. Trimmed the "artisanal alchemy vs industrial production" closer to its essential clause. Clarified the cursed-dip-target phrasing ("never use a cursed potion as a dipping target" → "never let the receiving potion be cursed"), since target/source language can confuse readers. See companion-audit.md. -->

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
|    20 | healing                                                                     |
|    50 | booze, fruit juice, see invisible, sickness                                 |
|   100 | confusion, extra healing, hallucination, restore ability, sleeping, water   |
|   150 | blindness, gain energy, invisibility, monster detection, object detection   |
|   200 | enlightenment, full healing, levitation, polymorph, speed                   |
|   250 | acid, oil                                                                   |
|   300 | gain ability, gain level, paralysis                                         |

<div class="price-id-toolbar"></div>

Water is the oddity in the $100 group: it always appears as "clear
potion," identifiable on sight. Don't underestimate it; water is
the raw material for holy water, which is the foundation of
everything.

#### Key Potions

**Healing, extra healing, full healing.** The healing chain, and
your lifeline in combat. Extra healing is the workhorse: it always
cures blindness and (non-cursed) also cures sickness in addition
to restoring HP. Non-cursed extra and full healing raise your
maximum HP if the heal would otherwise overflow; blessed versions
give the biggest boost. You can never have too many of these.

**Gain ability.** When blessed, raises *all* your stats by 1.
Uncursed raises a random stat. This is liquid gold: save every
one until you can bless it.

**Speed.** One non-cursed quaff and you're permanently faster for
the rest of the game; blessing only stretches the temporary timer
that overlays the intrinsic. Speed is arguably the single most
important buff in NetHack; the difference between moving at normal
speed and fast speed is the difference between trading blows and
hitting twice before they swing once. In 5.0, the wand of speed
monster no longer grants permanent speed when self-zapped, only a
temporary burst of 50–74 turns. The potion is the real prize.

**Holy water.** Not a potion you find: a potion you *make*. Drop
uncursed water on a co-aligned altar, pray, and the gods bless it
for you. Holy water can then bless any item you dip into it. This
is the engine that drives your entire inventory: blessed scrolls
of identify, blessed potions of gain ability, blessed scrolls of
enchant weapon. You will never have enough holy water.

**Gain level.** Raises your experience level by 1. Useful for
reaching quest eligibility quickly, or converting into something
better through alchemy.

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

The explosion risk is real: roughly 10% on any non-water combination. An
alchemy smock (if you find one) reduces this to about 1 in 30, which
is the difference between "risky hobby" and "acceptable profession." Do
your chemistry in an isolated room, away from your stash, and never use
a cursed potion as a dipping target. Cursed targets always explode. The
dungeon is consistent about this if nothing else.

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
<!-- audit 2026-05-17 #1: 26 claims verified, 2 corrected (enchant +5/+7 destruction wrong; charging "second/third recharge" overstated). See companion-audit.md. -->

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
|    20 | identify                                                                                                          |
|    50 | light                                                                                                             |
|    60 | blank paper, enchant weapon                                                                                       |
|    80 | enchant armor, remove curse                                                                                       |
|   100 | confuse monster, destroy armor, fire, food detection, gold detection, magic mapping, scare monster, teleportation |
|   200 | amnesia, create monster, earth, taming                                                                            |
|   300 | charging, genocide, punishment, stinking cloud                                                                    |

<div class="price-id-toolbar"></div>

The $60 group is treasure (enchant weapon lurks there alongside
innocent blank paper). The $80 group is equally good: enchant armor
and remove curse, two scrolls you'll always want more of. The $100
group is the danger zone, a grab-bag mixing magic mapping and
teleportation with destroy armor. And at $300, you'll find both
genocide (the game's nuclear option) and punishment
(a ball and chain permanently attached to your ankle). Choose wisely.

#### Key Scrolls

**Identify.** The bread and butter of dungeon life. Blessed identify
reveals multiple items at once (with positive luck, always at least
two). You will never have enough of these.

**Enchant weapon / enchant armor.** The path to endgame power.
Uncursed enchant *weapon* raises by +1. Blessed raises by up to 3,
less the more the weapon is already enchanted (no more than +1 once
the weapon is +6 or higher). Past +9 the scroll usually does nothing
but never destroys the weapon. Enchant *armor* raises by a small
random amount that's larger when armor is unenchanted, larger again
for elven or non-magic armor, and +1 extra when blessed. Once worn
armor exceeds **+3** (or **+5** for elven / Wizard's Cornuthaum),
each further enchant attempt can destroy the armor; the scroll
"evaporates" your gear. Blessed scrolls don't bypass this cap.

**Remove curse.** Frees you from cursed equipment. Uncursed version
works on worn and wielded items only; blessed version uncurses your
entire inventory. Every adventurer has a "put on a cursed ring"
story. This scroll is the happy ending.

**Charging.** Recharges wands and rechargeable tools. Save these
for your wand of wishing: one charge means one more wish. Blessed
charging restores more charges. Each recharge has an `n³/7³` chance
of the wand exploding (where `n` is the count of previous recharges):
0% on first, 0.3% on second, 2% on third, 8% on fourth, 19% on fifth,
36% on sixth — and on the seventh, always. Wand of wishing is the
exception: it explodes 100% of the time on the second recharge, so
recharge it exactly once and no more.

**Genocide.** The nuclear option. Uncursed eliminates a single
species; blessed wipes an entire monster class from the game
forever. Liches and mind flayers are popular targets. Read one
while confused and you genocide your own role's species
(Valkyrie, Wizard, etc.), which kills you instantly. Read
carefully.

**Magic mapping.** Reveals the entire level layout; blessed also
shows secret doors. Invaluable in Gehennom's maddening mazes,
where mapping by hand could take a lifetime you don't have.

**Scare monster.** The trick: don't read it. Drop it on the floor
and stand on it. It works like a permanent Elbereth, frightening
most monsters away. The catch: pick it up after it's been dropped
and it crumbles to dust. So choose your standing spot wisely.

**Teleportation.** Uncursed teleports you randomly on the level.
Cursed or confused reading sends you to a random dungeon level.
With teleport control, *you* choose where you land — the game's
most flexible escape hatch.

#### Confused Reading

Here's a trick the dungeon doesn't advertise: many scrolls do
something completely different when read while confused. Some of
these alternate effects are *better* than the normal ones:

- **Confused destroy armor** doesn't destroy anything: it
  *erodeproofs* a piece of armor. One of the best tricks in the game
- **Confused enchant armor / enchant weapon** also erodeproof
  instead of enchanting. Useful when you need protection from rust
  more than another +1
- **Confused remove curse** has a 25% chance of blessing *or*
  cursing each uncursed item. Risky, but it's a clever way to create
  holy water if you confuse-read while carrying uncursed potions of
  water
- **Confused genocide** genocides your own role. This kills you.
  Don't get confused at the wrong moment

---

### Wands and Staves
<!-- audit 2026-05-18 #105: five corrections. (1) Wand of stasis was missing entirely from the table and the NODIR list; objects.h:1460 defines WAN_STASIS (NODIR, $150, prob 45), zap.c:2559-2568 freezes the level. (2) "Nothing" prose said NODIR, but it's IMMEDIATE per objects.h:1462 (the table already had BEAM, prose was inconsistent — fixed prose). (3) "Wand of undead turning raises it as a zombie" is wrong; zap.c:WAN_UNDEAD_TURNING calls unturn_dead() which revives held/floor corpses to their original species (see also montraits revival path). (4) Engrave-test outcomes for "vanishes" / "disappears" / silent group were muddled. Per engrave.c: cancellation and make-invisible erase the engraving in place; teleportation moves it elsewhere on the level; polymorph rewrites it to a different random engraving (engrave.c:618-633); nothing, undead-turning, opening, locking, probing produce no message at all (engrave.c:635-640). (5) The silent-IMMEDIATE group was unmentioned. Also dropped "raises as zombie" misreading. See companion-audit.md. -->

Wands are reusable magical items that produce directed effects when
zapped. They come in three types: **ray wands** fire a beam in a
direction that bounces off walls, **beam wands** affect what they
hit in a straight line, and **non-directional wands** affect the
area around you.

#### The Wand Table

| Price | Wand                    | Type  | Max Charges |
| ----- | ----------------------- | ----- | ----------- |
|   100 | Light                   | NODIR | 15          |
|   100 | Nothing                 | BEAM  | 15          |
|   150 | Digging                 | RAY   | 8           |
|   150 | Enlightenment           | NODIR | 15          |
|   150 | Magic missile           | RAY   | 8           |
|   150 | Make invisible          | BEAM  | 8           |
|   150 | Opening                 | BEAM  | 8           |
|   150 | Probing                 | BEAM  | 8           |
|   150 | Secret door detection   | NODIR | 15          |
|   150 | Slow monster            | BEAM  | 8           |
|   150 | Speed monster           | BEAM  | 8           |
|   150 | Stasis                  | NODIR | 15          |
|   150 | Striking                | BEAM  | 8           |
|   150 | Undead turning          | BEAM  | 8           |
|   150 | Locking                 | BEAM  | 8           |
|   175 | Cold                    | RAY   | 8           |
|   175 | Fire                    | RAY   | 8           |
|   175 | Lightning               | RAY   | 8           |
|   175 | Sleep                   | RAY   | 8           |
|   200 | Cancellation            | BEAM  | 8           |
|   200 | Create monster          | NODIR | 15          |
|   200 | Polymorph               | BEAM  | 8           |
|   200 | Teleportation           | BEAM  | 8           |
|   500 | Death                   | RAY   | 8           |
|   500 | Wishing                 | NODIR | 3           |

<div class="price-id-toolbar"></div>

#### Key Wands

**Wishing.** The most valuable item in the game. Each zap grants one
wish. In 5.0, wands of wishing generate with only **1
charge** and can be recharged once (and only once) to a maximum of
1 additional charge. This means the Castle wand of wishing typically
yields 2 wishes plus a possible wrested third, a significant
reduction from older versions where it could provide 5 to 7. Plan
your wishes carefully before you find one.

**Death.** Fires a death ray that instantly kills most things it
hits. Reflected by reflection. Blocked by magic resistance. One
of the best offensive tools in the late game.

**Digging.** Essential utility. Dig through walls to create
shortcuts, dig down to escape dangerous situations, dig through
rock to reach vaults and hidden areas. Every ascension kit should
include a wand of digging.

**Teleportation.** Zap monsters to send them somewhere else on the
level. Zap yourself to teleport. Enormously useful for escaping
trouble or removing a dangerous monster from your path.

**Fire, cold, lightning.** Offensive ray wands that bounce off walls.
Fire burns scrolls and spellbooks on the floor. Cold freezes water
(useful for creating paths). Lightning blinds monsters.

**Cancellation.** Removes special properties from items and monsters.
A cancelled monster loses most of its special attacks. Do NOT put
this wand in a bag of holding (it will explode the bag). Keep it
separate in your main inventory.

**Polymorph.** Transforms monsters into random other monsters and
items into random other items of the same class. Can be used
creatively (polymorph a pile of junk armor hoping for dragon scale
mail, polymorph a weak monster hoping for a useful corpse). Risky
but powerful.

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

**Stasis.** A new 5.0 wand that freezes every monster on the level
for **10–30 turns**. No ray, no aim, no message — just a hush. Use
it when you're surrounded and need a free moment to engrave
Elbereth, drink a potion, change weapons, or just walk past. The
silence on engraving makes it harder to identify by the engrave
test, but if you sit on a charge for a fight you'll know.

#### Identification by Engraving

The engrave test (described in
[A Practical Identification Strategy](#a-practical-identification-strategy)) is the
fastest way to sort wands. Every wand type produces a distinctive
result when used to engrave on the floor.

> *Kieron Dunbar's "Identifying Wands by Zapping" spoiler,
> originally posted to RGRN, describes a systematic protocol for
> narrowing down wand identity through controlled experiments. The
> approach below is adapted from his checklist.*

Before you start writing on the floor: in 5.0, a *cursed* wand used
to engrave may explode, so BUC-test before you test (see [The Engrave
Test (Wands)](#the-engrave-test-wands) for the full safety procedure).

#### Beyond Engraving: Systematic Wand Testing

The engrave test sorts most wands immediately, but a few produce
ambiguous results. For those, a systematic testing protocol helps:

**Step 1: Note the wand category.** When you engrave, the result
tells you whether the wand is NODIR (non-directional), RAY, or
BEAM (immediate). This alone cuts the possibilities dramatically.

- **NODIR wands** (light, enlightenment, create monster, secret
  door detection, stasis, wishing): Most reveal themselves through
  the engrave-test message. Light creates a lit field.
  Enlightenment makes you feel self-knowledgeable. Create monster
  says "bugs appear." Wishing prompts you for a wish. **Stasis**
  is deliberately silent on engraving — the C code hides it among
  the other silent wands so the engrave test can't single it out.
- **RAY wands** (digging, magic missile, fire, cold, lightning,
  sleep, death): Digging riddles the floor with holes. Fire, cold,
  and lightning produce obvious elemental effects. Sleep stops bugs
  from moving. Magic missile and death just write in dust. Of these
  two, death is $500; check the price first.
- **BEAM wands** (everything else): The engrave test only
  distinguishes some of them. **Cancellation and make invisible**
  erase the engraving in place. **Teleportation** moves it
  elsewhere on the level (look around to spot it). **Polymorph**
  rewrites your engraving as a different random one. **Striking**
  scatters dust around. Five BEAM wands — **nothing, undead
  turning, opening, locking, probing** — produce *no engrave
  message at all*. Combined with the silent NODIR stasis (above),
  a wand that engraves in silence is one of six possibilities; the
  zap tests below will resolve them.

**Step 2: Safe zapping tests.** For wands that remain unidentified
after engraving, zap them at safe targets:

- **Zap at a locked chest or door.** A wand of opening unlocks it.
  A wand of locking locks it. A wand of striking breaks it.
- **Zap at a corpse on the floor.** A wand of undead turning
  revives the corpse to its original species (and animates any
  carried corpses too). A wand of polymorph transforms it.
- **Zap at a tame or weak monster.** Speed monster makes it faster.
  Slow monster makes it slower. Make invisible makes it vanish.
  Probing reveals its stats.
- **Zap at a cancellable item** (a potion, a figurine). Cancellation
  will dull it. Note: cancellation does NOT affect booze, fruit
  juice, or oil, so don't use those as test subjects.

**Step 3: When in doubt, check the price.** If testing hasn't
resolved the wand, its shop price narrows the field further. A
$150 wand is one of thirteen types. A $200 wand is one of four.
A $500 wand is death or wishing, and you should be very careful
with it either way.

#### Recharging

Wands can be recharged with a scroll of charging. Each recharge
increases the risk of the wand exploding. The formula is
(recharges cubed) / 343, so:

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

#### Wresting

When a wand has 0 charges, you can still try to zap it. There is a
1/121 chance of "wresting" one final charge from the wand before it
turns to dust. This is a last resort, but it works on wands of
wishing too.

---

### Rings and Amulets
<!-- audit 2026-05-18 #139: ~144 lines, no substantive corrections. All ring prices match objects.h:741-827; auto-curse list (TELEPORTATION/POLYMORPH/AGGRAVATE_MONSTER/HUNGER at 90% per mkobj.c:1143-1146) is correct; aggravate-monster effective-depth doubling capped at 50 (dungeon.c:2080-2082); free-action paralysis immunity via Free_action checks (apply.c:1044, mcastu.c:506); per-ring hunger cost at turns 4 and 12 (eat.c:3237-3267); amulet of guarding +2 AC +2 MC (do_wear.c:2496, mhitu.c:1121-1126); restful-sleep regen +1 HP while sleeping (allmain.c:663-664). Minor close calls: (a) restful sleep is *always* cursed per mkobj.c:1065, not "usually"; (b) blessed polymorph potion grants control only from base form (potion.c:1318-1329, POLY_LOW_CTRL restricts forms); (c) protection-from-shape-changers covers chameleons/doppelgangers/sandestins too, not just werebeasts (makemon.c:1355-1358). Not corrected inline — section is illustrative. -->


Two ring fingers. One neck. These are the most constrained equipment
slots in the game, which makes choosing what to wear a genuine
strategic decision. Both rings and amulets have randomized
appearances, and some of the best items in the game hide behind
unassuming descriptions like "granite ring" or "circular amulet."

#### The Ring Table

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
throne room. Economy of fingers is an art.

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
genuinely terrifying cavalry unit.

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
<!-- audit 2026-05-17 #28 (re-audit 2026-05-18 v2 #62): ~40 claims verified, 5 corrected (container locked counts, unicorn horn cure list, crystal ball one-class-per-gaze, Bell of Opening is Quest reward not Vlad, passtune any tonal instrument). v2 audit found four corrections. (a) Bell of Opening "granted by your quest leader on Quest completion" was wrong — the Bell is carried by the quest *nemesis* and looted from their corpse (makemon.c:1378-1379 BELL_OF_OPENING goes to MS_NEMESIS); the quest leader chides you if you finish without it (quest.c:267-268) but doesn't grant it. (b) "One blessed scroll of charging restores it to at least 50" misleads — an uncursed scroll also reaches 50 (read.c:880-883); blessing pushes the floor to 75. Reworded to "non-cursed scroll of charging restores it to at least 50 (more if blessed)." (c) Magic lamp "rub it while blessed and there's a 1-in-3 chance" implies blessing affects emergence; bless only affects the wish-grant probability (apply.c:1817) — 1/3 emergence is independent. Reworded. (d) "~16 charges very well spent" was the basecost; actual scroll-of-charging write cost is rn1(8,8) = 8-15 charges. Updated. Also added the G_UNIQ-skip caveat to class genocide: "uniquely-named demon lords survive any class genocide" (read.c:2998). See companion-audit.md. -->

The `(` symbol covers the dungeon's most eclectic category: pickaxes,
magic lamps, unicorn horns, musical instruments, crystal balls, and
bags that eat other bags. If it doesn't fit neatly into any other
class, it's a tool. Some of the most powerful items in the game hide
in this grab-bag.

#### Containers

| Container      | Weight | Special                                  |
| -------------- | ------ | ---------------------------------------- |
| Sack           | 15     | Basic storage                            |
| Oilskin sack   | 15     | Protects contents from water             |
| Bag of holding | 15     | Reduces weight of contents dramatically  |
| Bag of tricks  | 15     | Creates monsters when opened (not a bag) |
| Large box      | 350    | Comes with 0 to 3 items (0 to 5 if locked) |
| Chest          | 600    | Comes with 0 to 5 items (0 to 7 if locked) |
| Ice box        | 900    | Preserves corpses from rotting           |

The **bag of holding** deserves its own paragraph because it
transforms how you play. A blessed bag reduces the weight of
everything inside to roughly one quarter, meaning you can carry your
entire potion supply, your backup armor, your scroll library, and
still have room for loot. Get one from Sokoban or wish for one
early. It's that important.

The cardinal rule: **never** put a wand of cancellation, another bag
of holding, or a charged bag of tricks inside a bag of holding. The
resulting magical explosion scatters your carefully curated
inventory across the floor. In older editions it *destroyed*
everything. Either way, it's a game-ending mistake that every
veteran has made exactly once.

One 5.0 hazard that the adventuring community is still
adjusting to: intelligent monsters can now loot unlocked containers.
They can remove items, carry containers away, and unlock chests with
keys. If you've been leaving your secondary stash in an unlocked chest
on a partially-cleared level while you scouted ahead, stop. The Castle
chest in particular (containing the wand of wishing) can be emptied
by the level's residents if you leave them time and opportunity. Clear
levels before abandoning valuables, and keep your most important
containers locked. The dungeon has gotten better at wanting what you
have.

#### Unlocking Tools

The dungeon is full of locked things, and brute force is noisy and
slow. A **skeleton key** is the gold standard (70%+ success on
doors, 75%+ on boxes). A **lock pick** is respectable. A **credit
card** is the worst but still better than kicking. Always carry one
of these. The weight is negligible and the utility is constant.

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
**genocide** (three of these wipe the worst monster letters — L,
&, h — out of the game; uniquely-named demon lords survive any
class genocide), **charging** (a blessed one restores one
additional wish to an empty wand of wishing for 8-15 charges very
well spent, though a second charging attempt always explodes the
wand), and **enchant weapon / enchant armor** for the +7 ascension
kit. A well-used marker can produce a meaningful share of your
ascension kit.

---

### The Armory

Weapons and armor are the bread and butter of combat. Your choice
of equipment determines how hard you hit, how well you dodge, and
what special resistances you carry. This section covers the
strategy of choosing equipment; the
[Weapons Tables](#weapons-tables) and [Armor Tables](#armor-tables)
appendices give the full stats for every item.

#### Armor and AC

Armor Class (AC) starts at 10 and decreases as you add protection.
Lower is better. Each point of AC reduces the chance of being hit.
At AC -10 or below, you're quite difficult to damage with physical
attacks.

The key armor slots:

| Slot   | Best mundane options                       | Best magical options                  |
| ------ | ------------------------------------------ | ------------------------------------- |
| Body   | Splint mail, banded mail                   | Dragon scale mail (two extrinsics)    |
| Cloak  | Cloak of protection                        | Cloak of magic resistance             |
| Helmet | Helm of caution (early game)               | Helm of telepathy / helm of brilliance |
| Gloves | Gauntlets of power                         | Gauntlets of dexterity                |
| Boots  | Speed boots                                | Water walking boots, levitation boots |
| Shield | Shield of reflection                       | Small shield (for spellcasters)       |

The **helm of caution** is new in 5.0: it grants
*warning*, the same intrinsic the ring provides, in the helmet
slot. Warning fills the screen with colored markers indicating
nearby threats by danger level (yellow for moderate, red for
deadly) without you having to see the monsters yet. It is the
ideal early-game helm slot: cheap (50 zm), light, and a real
edge against ambushes. Late game it competes with helm of
brilliance (Wizards) and helm of telepathy (everyone), but the
warning bonus stays useful all the way down.

**Dragon scale mail** is the endgame body armor of choice. In
5.0, most colors provide two extrinsic resistances (gray and
silver provide only the named one). Gray dragon scale mail
provides magic resistance and is the most popular wish target.
Silver provides reflection. Black provides disintegration
resistance and drain resistance (the only non-artifact source).
Green provides poison resistance and sickness immunity.

To get dragon scale mail: kill a dragon, pick up the scales it
drops, then read a (non-cursed) scroll of enchant armor while
wearing them (they transform into scale mail); or wish for the
mail directly.

**Speed boots** are worth wishing for. Being faster than your
enemies means you get more turns — more chances to attack, cast
spells, or run away.

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
| Long sword     | d8 / d12       | Lawfuls can dip for Excalibur      |
| Katana         | d10 / d12      | Best base damage for a one-hander  |
| Silver saber   | d8 / d8        | +d20 vs silver-hating monsters     |
| Crysknife      | d10 / d10      | Excellent damage, fragile          |
| Tsurugi        | d16 / d8+2d6   | Two-handed, bisects small monsters |
| Runesword      | d4 / d6+d4     | Chaotic weapon                     |
| Battle-axe     | d8+d4 / d6+2d4 | Two-handed, good damage            |
| Rubber hose    | d4 / d3        | No, seriously, don't use this      |

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

<!-- audit 2026-05-18 #175: Weapon enchantment has no destruction risk at all — read.c:1669-1671 just becomes probabilistic above +9 (uncursed always adds +1). Armor destruction risk begins above +3 (above +5 for "special" armor like elven items or the Wizard's cornuthaum) per read.c:1179; cursing/uncursing doesn't change the threshold, only the success rate. Reworded. -->
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

---

### Artifacts
<!-- audit 2026-05-18 #113: 4 substantive corrections + 3 useful additions. (1) Magicbane "curse protection while carried" wrong — Magicbane has SPFX_RESTR|SPFX_ATTK|SPFX_DEFN, STUN(3,4), DFNS(AD_MAGM), NO_CARY (artilist.h:145-147); all four code paths at wield.c:1036, trap.c:2360, mplayer.c:273, sit.c:576 require wielding. Reworded table and prose. (2) Master Key non-rogue: spoiler said "non-blessed Key carried by anyone else" — opposite of C. artifact.c:2778-2784: Rogue needs !cursed, non-rogues need blessed. (3) Eyes of the Overworld "carried gives magic resistance" wrong — DFNS(AD_MAGM), NO_CARY (artilist.h:262); MR only when worn (per artifact.c:731 wp_mask check). Both table row and prose fixed. (4) Tsurugi "grants magic resistance" wrong — cspfx=SPFX_LUCK|SPFX_PROTECT only, no MR via spfx/defn/cary (artilist.h:285-289). Added: Sceptre of Might double-damage hits chaotic/NEUTRAL/unaligned (SPFX_DALIGN at artifact.c:1031-1034 triggers for any sgn(maligntyp)!=weap.alignment, and the Sceptre is Lawful); Mjollnir return is Valkyrie-only-reliable per artilist.h:97-108; Frost/Fire Brand have SNOWSTORM/FIRESTORM invokes (artilist.h:150, 154); Stormbringer is SPFX_INTEL so cross-alignment touch deals 4d10 not 4d4. -->


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
| Frost Brand       | any      | long sword        | +d5    | (base only) cold            | fire resistance + cold defense                         |
| Fire Brand        | any      | long sword        | +d5    | (base only) fire            | cold resistance + fire defense                         |
| Sunsword          | Lawful   | long sword        | +d5    | (base only); ×2 vs undead   | wielded light; `#invoke` fires a blinding ray any direction (camera-style; works on any monster) |
| Snickersnee       | Lawful   | katana            | —      | +d8 physical                | acts as a polearm without a steed; one free reach-attack per turn (the "Shkinng!" hit) |
| Cleaver           | Neutral  | battle-axe        | +d3    | +d6 physical                | one-handed wield → strikes target *and* both flanks    |
| Demonbane         | Lawful   | silver mace       | +d5    | (base only); ×2 vs demons   | banishes demons; Priest's first sacrifice gift         |
| Sting             | Chaotic  | elven dagger      | +d5    | (base only); ×2 vs orcs     | warns of orcs (the dagger glows blue)                  |
| Orcrist           | Chaotic  | elven broadsword  | +d5    | (base only); ×2 vs orcs     | warns of orcs                                          |
| Grimtooth         | Chaotic  | orcish dagger     | +d2    | +d6 physical; ×2 vs elves   | warns of elves; defends vs poison                      |
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

**Magicbane** is the Wizard's go-to athame. The combined effect of
its stun damage, curse protection, and magic resistance — all of
which require it to be **wielded**, not just carried — makes it
Wizard's preferred melee weapon. Often the first gift from a
Neutral sacrifice.

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

**Snickersnee** got a major buff in 5.0: it now counts as a polearm
even when you're on foot (regular pole weapons require a steed). Once
per turn you can `#apply` it for a free reach attack at a target up
to two squares away — a real free action that *doesn't* end your
turn, leaving you a normal melee swing on top. The free hit is
announced by a distinctive "Shkinng!" The combined output (one
ranged + one melee per turn) makes Snickersnee a contender for
best Samurai weapon in the game, not just a flavor piece.

**Sunsword** is the Lawful long sword that wants to be a tool. Wielded,
it lights its current radius (handy in caves and the Mines without
costing an oil lamp). `#invoke` it for a directed *blinding ray* —
mechanically a Camera flash in any direction, *not* limited to
undead. It costs 5×spell-level Pw to invoke, so save it for the
fights that demand it (Riders, mind flayers, the Wizard of Yendor),
but a blind monster is a monster that misses you. Invoking up or
down lights the room; invoking at yourself self-blinds (don't).

**Bane weapons** (Sunsword, Demonbane, Sting, Orcrist, Grimtooth,
Dragonbane, Werebane, Giantslayer, Ogresmasher, Trollsbane) deal
double base damage against their target class. Most are disappointing
as a primary weapon, but the defensive riders are often the real
reason to swap one in: Trollsbane regenerates while wielded (genuinely
useful for an early character holding the line), Dragonbane reflects,
Werebane neutralizes lycanthropy, Grimtooth defends against poison.
Sting and Orcrist are notable because elves can start with elven
daggers and broadswords as their base weapons.

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

| Role       | Artifact                                     | Form         | Wear/wield                  | Carry                  | `#invoke`        |
|-----------|-------------------------------------------------------------|--------------|--------------------------|------------------------|-----------------|
| Archeologist| The Orb of Detection                | crystal ball | —                              | MR, ESP, ½ spell dmg   | invisibility      |
| Barbarian   | The Heart of Ahriman                | luckstone    | ×2 dmg as a projectile         | stealth, +luck         | levitation        |
| Caveman     | The Sceptre of Might                | mace         | +d5 hit; ×2 vs non-lawful      | magic resistance       | conflict          |
| Healer      | The Staff of Aesculapius            | quarterstaff | drain-life on hit              | drain res., regen      | full heal + cure  |
| Knight      | The Magic Mirror of Merlin          | mirror       | (speaks to you)                | MR, ESP                | —                 |
| Monk        | The Eyes of the Overworld           | lenses       | astral vision, magic res. (when worn) | —              | enlightenment     |
| Priest      | The Mitre of Holiness               | helm         | ×2 vs undead, +1 prot.         | fire res.              | energy boost      |
| Ranger      | The Longbow of Diana                | bow          | +d5 hit; reflection            | ESP                    | conjure arrows    |
| Rogue       | The Master Key of Thievery          | skeleton key | —                              | warn, t-ctrl, ½ phys   | guaranteed untrap |
| Samurai     | The Tsurugi of Muramasa             | tsurugi      | +d8 phys; chance to behead     | +luck, +1 prot.        | —                 |
| Tourist     | Platinum Yendorian Express Card     | credit card  | —                              | MR, ESP, ½ spell dmg   | charge an item    |
| Valkyrie    | The Orb of Fate                     | crystal ball | —                              | +luck, warn, ½ all dmg | levitate/teleport |
| Wizard      | The Eye of the Aethiopica           | amulet       | —                              | MR, ½ spell, +energy   | create portal     |

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

**The Magic Mirror of Merlin** (Knight): doesn't fight (it's a
mirror), but grants ESP and magic resistance, and occasionally
*speaks*, dropping hints. Knights already have Excalibur for combat,
so the Mirror is pure passive utility.

**The Eyes of the Overworld** (Monk): lenses that, when worn, give
astral vision (see invisible, see through walls, spot secret doors)
**and** magic resistance. Both effects require them to be worn —
carrying them in inventory does nothing. `#invoke` enlightens you.
For a Monk who can't safely wear body armor, a powerful passive on
a slot they can use.

**The Mitre of Holiness** (Priest): a helm of brilliance that grants
double damage vs undead while worn, plus the brilliance bonus to
intelligence and wisdom (so spell-cast more reliably), plus fire
resistance while carried, plus a free `-1` to AC. `#invoke` for an
energy boost, useful for spell-heavy Priests. Note: despite what
older spoilers say, it does **not** grant drain resistance.

**The Longbow of Diana** (Ranger): a real artifact bow with +d5 to hit
plus reflection while wielded, ESP while carried. `#invoke` conjures
free arrows out of thin air. Combined with the Ranger's ranged
specialization this is the role's centerpiece.

**The Master Key of Thievery** (Rogue): doesn't fight, but the carry
package is enormous: warning, teleport control, half physical damage
taken, and `#invoke` instantly untraps a nearby trap. The unlocking
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
get-out-of-jail card. Carry grants ESP, magic resistance, and half
spell damage; `#invoke` charges an item (a wand, ring, or marker),
which in the Tourist's hands is roughly "a free wish per ~1000
turns." Pairs especially well with marker-stockpiling strategies.

**The Orb of Fate** (Valkyrie): the most generous passive in the
game: counts as a luckstone, grants warning, halves both spell *and*
physical damage taken. `#invoke` is levitate-or-teleport (a toggle,
very useful in the Sanctum). Valkyries also have Mjollnir to throw,
so the Orb sits in inventory as pure carry value.

**The Eye of the Aethiopica** (Wizard): worn or carried, it grants
magic resistance, half spell damage taken, and *extra energy
regeneration*, a Wizard's most precious resource. `#invoke` opens a
portal that drops you in Vlad's Tower (one-way; useful for
shortcutting the Castle → Vlad's traversal). For a spell-caster this
is irreplaceable.

---

## Part Five: The Craft of Adventuring

> *Part Five draws on Matthew Lahut's RGRN prayer guide, Steven
> Bush's spellbook reading tables, and the Hugo/O'Donnell files on
> gods, combat, gems, and luck mechanics, all updated for 5.0.*

---

### Divine Relations
<!-- audit 2026-05-18 #121: 3 corrections. (1) Trouble list had Punishment as #10 major trouble — wrong; TROUBLE_PUNISHED = -1 in pray.c:91, i.e. MINOR trouble, handled in the "additional blessings" tier. Demoted Punishment to that tier and added the genuine missing major troubles (stinking cloud TROUBLE_REGION, collapsing under load, stuck in wall, cursed levitation boots, unusable hands, cursed blindfold per pray.c:218-243). (2) "Crowning raises the prayer timeout to at least 1000 turns" — wrong; pray.c:1356-1361 adds rnz(1000) * kick on top of the ordinary rnz(350), so the post-crowning total averages much higher but can be lower than 1000. Reworded to "adds a large random penalty on top of the ordinary post-prayer wait, on the order of ~1000 turns on average." (3) "Crowning locks your alignment (you can never change it)" — wrong; gcrownu at pray.c:805-996 sets no alignment lock. The actual one-way conversion gate is the u.ualignbase[A_CURRENT] == u.ualignbase[A_ORIGINAL] check at pray.c:1638, independent of crowning. Dropped the claim. -->


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
10. Blindness, confusion, stunning, hallucination
11. Stuck in a wall, collapsing under load, cursed levitation boots, unusable hands (cursed glove + cursed wielded weapon), cursed blindfold

After resolving your problems, your god may grant additional
blessings: fixing minor afflictions (plain hunger, ordinary
punishment with iron ball and chain, low-priority annoyances),
improving your alignment, or even gifting intrinsics like
telepathy or speed.

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

Offering fresh monster corpses at an altar (`#offer`) builds favor
with your god. The rules:

- The corpse must be fresh — killed within the last **50 turns**.
  A corpse older than that has zero sacrifice value (the gods
  simply ignore it).
- Bigger monsters are more valuable sacrifices.
- The altar must match your alignment, or you're praying to someone
  else's god (which has its own consequences).
- Same-race sacrifice is forbidden and severely punished (with one
  exception: it can convert an altar to your alignment).

With enough sacrifice credit, your god may gift you an artifact
weapon. The first gift comes after relatively modest sacrifice;
subsequent gifts require substantially more. Gift artifacts are
always aligned to your god and always match a weapon skill you can
use.

There is a minimum. In 5.0, not every corpse you drop on
the altar moves you toward the next artifact gift. The gods have
opinions about what constitutes a worthy offering, and a kobold doesn't
make the cut. Fresh corpses of appropriately challenging monsters are
what advances your standing. If you've been feeding the altar with
early-dungeon sweepings and wondering why the gifts aren't arriving,
this is why.

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
  visits. Granted if you offer in the upper tier. Each successful
  donation pushes the bonus up by 1 (rarely more), capped at 20.
  The bonus persists for life, unlike clairvoyance.

**The cost.** Pay enough and the benefit is yours. The priest's
prompt always shows you the exact ask, which scales with your
experience level and how much gold you're carrying:

- **Clairvoyance:** a randomized 150–250 zorkmids × experience
  level as the base ask
- **Protection:** twice that — 300–500 zorkmids × experience level

If you walk in carrying far more gold than the baseline, the
priest scales the ask up to match — roughly a third of your purse
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
(success), costs you Luck (failure), or — if your god is
already angry — converts *you* to the altar's alignment instead.
Better odds at higher experience level. Worth the risk when you
need a co-aligned altar for sacrifice gifts, holy water, or BUC
testing.

Two things to **never** sacrifice on any altar:

- **A same-race corpse** (humans for most roles; also elves if
  you're elven). Punished on every altar; on a Chaotic one it
  summons a demon.
- **A unicorn whose alignment matches the altar.** Counts as an
  insult to that god.

#### Crowning

If your alignment record is very high (through sacrifice and good
behavior), your god may crown you. Crowning grants:

- A special title (e.g., "Hand of Elbereth" for lawful characters).
- An artifact weapon appropriate to your alignment, if one is
  available that you can use.
- Intrinsic fire resistance, cold resistance, shock resistance,
  sleep resistance, poison resistance, and see invisible.
- A class-specific bonus: Wizards get the *finger of death* spell;
  Monks get *restore ability*.

The catch is that crowning **adds a large random penalty to your
prayer timeout** — on the order of an extra ~1000 turns on
average, on top of the ordinary post-prayer wait. Many experienced
players avoid being crowned because that hike turns prayer into an
unreliable emergency tool during the most dangerous part of the
game. If you're sacrificing a lot to fish for an artifact gift,
know that you might accidentally trigger a crowning instead. Some
players deliberately keep their alignment record modest until
they've secured the items they need.

---

### The Art of Combat
<!-- audit 2026-05-18 #82: many claims verified (XL/Str/Luck/enchantment/AC factors in find_roll_to_hit, dbon Str cap, 3/2 two-handed Str bonus, conflict requires mutual sight + Cha-Lvl resist roll, shields forbidden with two-weapon). Three corrections: (1) Two-weapon roles wrong — actual EXPERT roles are Rogue + Samurai, not Rangers + Barbarians (Rangers can't two-weapon at all per u_init.c); penalty is a flat negative replacement table per skill, not a "split." (2) Luck to-hit caps around ±5 but Luck itself goes to ±10 (±13 with luckstone). (3) Reworded "monster spellcasters no longer get free extra step" — left as plausible but unverified. v2 audit 2026-05-18 #43: two factual fixes. (a) The to-hit list "Your Strength bonus (muscles still matter underground)" was incomplete — abon() at weapon.c:950-988 includes BOTH Strength AND Dexterity (dex 25 yields +11, often dominant at high levels). Reworded to "Your Strength and Dexterity bonuses (muscles plus agility, both matter)". (b) Dropped the "Monster spellcasters no longer get a free extra step after casting" bullet entirely — the pass-1 audit flagged it as "plausible but unverified", and the v2 auditor confirmed no such fix exists in git history. Monsters still move via m_move() (PHASE THREE) then attack/cast via mattacku()/castmu() (PHASE FOUR) on the same turn (monmove.c:911, 943-944, 971). Fabricated 5.0 change. See companion-audit.md. -->

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
<!-- audit 2026-05-18 #82: corrected. Per u_init.c skill tables: Rogue and Samurai are the only roles that reach Expert in P_TWO_WEAPON_COMBAT; Valkyrie and Knight cap at Skilled; Barbarian caps at Basic; **Rangers can't two-weapon at all** (no P_TWO_WEAPON_COMBAT entry). Penalty structure is a flat negative replacement at each skill tier (-9/-7/-5/-3 to hit, -3/-1/0/+1 damage), not a "split." See companion-audit.md. -->

Some roles can fight with a weapon in each hand, which looks
impressive and gives more attacks per turn. The catch: each strike
takes a flat to-hit and damage penalty determined by your
two-weapon skill (−9/−7/−5/−3 to hit, −3/−1/0/+1 damage from
Unskilled through Expert), and you can't use a shield. Only
**Rogue** and **Samurai** can reach Expert; Valkyrie and Knight
cap at Skilled; everyone else lower or none. Rangers don't have
the skill at all. If you're not sure, just use one really good
weapon. In 5.0, two-handed weapons got a buff (3/2 strength damage
bonus) that makes them a good alternative.

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
  which is exactly how you want them.
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
  recover. If you've carved Elbereth in a corridor and then backed a
  monster into a dead end, be ready for it to make a decision about
  that arrangement. Keep an exit behind the monster, or expect contact.

---

### Enhancing Skills
<!-- audit 2026-05-18 #98 (revised 2026-05-18 #181): ranks (P_UNSKILLED..P_GRAND_MASTER) and the level²×20 practice formula (20/80/180/320/500 cumulative) verified against skills.h:92-106. Slot costs (weapon 1/2/3, non-weapon 1/1/2/2/3) and crowning bonus from u_init.c skill tables and weapon.c:can_advance. Bare-hand 50% / martial-arts 75% damage-bonus check from weapon.c:weapon_hit_bonus. Riding 100-square threshold (steed.c:393-396, ++u.urideturns >= 100) and action-gating (pickup/loot/dip/trap/engrave require Basic) from u_init.c + do.c. Slot ceiling is 32 for an XL-30 crowned hero (2 starting + 29 level-ups + 1 crowning) per u_init.c:884 and pray.c:992-993. Ranger divination caps Expert (u_init.c:461). Wizard restricted from long sword per u_init.c skill table; artifact-gift unrestrict in artifact.c:artifact_hit. Spell-school precredit of 20 uses at starting Basic per u_init.c. Skilled cone-of-cold / fireball / identify rank gating per spell.c spelleffects. "You feel more confident in your skills" / "You feel you could be more dangerous" message strings in weapon.c. v2 audit 2026-05-18 #13: three factual fixes. (a) Two-weapon uses the WEAPON slot column (1/2/3), not the non-weapon column — per weapon.c:1141 `if (skill <= P_LAST_WEAPON || skill == P_TWO_WEAPON_COMBAT)`. Pre-3.7 lore had it on the non-weapon side. (b) Valkyrie example math was 11 with the old assumption; with correct costs it is 6+6+2 = 14. Fixed. (c) "Bare-hand and martial-arts bonuses still only apply to 50%/75% of hits" conflates practice-training rate with bonus application; the bonuses apply on every hit per weapon.c:1611-1613. Wisdom: cone-of-cold and fireball Skilled upgrade is a cluster of 3×3 explosions (spell.c:1419-1452), not "room-clearing" — corrected both mentions; Knights start at Basic riding (weapon.c:1787-1789), so the advancement target is Skilled, not Basic. Voice: dropped invented in-world reason "the dungeon's quiet subsidy for magic"; trimmed "restricted from long swords entirely. Restricted skills..."; replaced colorful "killing blow vs monster shrug" line with the bare numbers; cut "Specialization by decree." meta; clarified "past level 3" as spell-level. See companion-audit.md. -->

Most adventurers discover the skill system the first time they
press `#enhance` and realize the broadsword they've been swinging
for several levels is finally ready to graduate from Basic to
Skilled. Weapons, fighting styles, and spell schools each track
their own proficiency, and you train them one slot at a time.

#### The Skill Ladder

Most skills run **Unskilled → Basic → Skilled → Expert**. **Bare
hands** and **martial arts** alone reach **Master** and **Grand
Master**. Each rank-up costs both **practice** (uses of the skill)
and **skill slots** (a finite budget tied to your experience
level).

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
`#enhance` and stay Unskilled, with one exception: if your god
grants you an artifact weapon, you're auto-unrestricted in its
skill up to Basic. The full role caps live in the appendix.

#### Training a Skill

Practice accumulates through use:

- **Weapon skills** tick on every melee or thrown hit that does
  **more than 1 damage**. A pillow-soft punch for 1 point doesn't
  count. Spears, javelins, knives, daggers, and aklys train the
  same skill whether you stab with them or throw them.
- **Bare hands** counts **50%** of your hits; **martial arts**
  counts **75%**. The rank still applies on every hit — this just
  slows the climb.
- **Riding** earns one tick every **100 squares** ridden.
- **Spell schools** earn **N practice per successful cast of a
  level-N spell**. Every school has a level-1 option to grind —
  see the schools table below.

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
the difference between landing the killing blow and watching the
monster shrug.

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

Role caps vary sharply across schools:

- **Wizards** have access to all seven schools and cap at Expert
  in attack, divination, escape, and matter.
- **Monks** also have access to all seven, but cap at Expert only
  in healing — Skilled in cleric and escape, Basic elsewhere.
- **Priests** reach Expert in healing, divination, and cleric.
- **Healers** cap at Expert in healing and are *restricted*
  from every other school. Specialization by decree.
- **Knights** train attack, healing, and cleric to Skilled.
- **Rangers** push divination to Expert — their one specialty school.
- **Rogues, Tourists, Samurai** each get two or three schools at
  Skilled or lower, usually built around divination or escape.
- **Cavemen** reach Skilled in matter and Basic in attack — two
  schools only.
- **Barbarians and Valkyries** cap at Basic in their two schools
  (attack and escape) and can't reliably cast spells past
  spell-level 3.

Full role caps for every weapon, fighting style, and spell school
are in the [Skill Caps](#skill-caps) appendix; the full list of
43 spells is in the [Spell Tables](#spell-tables) appendix.

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
  fine: the menu just stops offering further advances. Aiming
  beyond the cap costs nothing because the option never appears.
- **Wizards train spell schools twice over.** Each rank up
  improves casting success *and* reveals more spellbook
  appearances in that school (the identification payoff from the
  Spellcasting chapter). Schools containing your unidentified
  books deserve priority.
- **Riding's silent gate.** Without **Basic riding** you can't
  pick up items, loot, dip, set or disarm traps, or engrave on
  the floor while mounted. Knights start at Basic. Pushing to
  Skilled erases the −1 to-hit penalty in the saddle and adds
  +1 damage.
- **Bare hands and martial arts are a Monk story.** Grand Master
  needs **9 cumulative non-weapon slots**, which Monks reach
  naturally. Anyone else dabbling in unarmed combat should plan
  to stop at Basic.

A few spells also get sharper at Skilled, not just more reliable.
Cone of cold and fireball stop being beams and become a cluster
of 3×3 **explosions** you can place at range. Identify, remove
curse, haste self, detect monsters, and several others gain the
blessed-scroll effect (multi-item ID, full uncurse, longer
duration). If you cast those spells regularly, the extra slots
earn themselves back.

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
  (see Wands → Key Wands for the 5.0 charge mechanics). The
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
<!-- audit 2026-05-18 #102: corrected three claims in the wish-syntax bullets. (1) Bare "gray dragon scale mail" does NOT force uncursed +0; objnam.c:5094-5096 retains the random mksobj spe, and objnam.c:5258-5268 only sets BUC when a buc adjective is given — blessorcurse(otmp,10) leaves ~10% blessed, ~10% cursed, ~80% uncursed. (2) "Cannot wish for artifacts already generated" is wrong: objnam.c:5374 makes denial probabilistic (oartifact && rn2(nartifact_exist())>1), scaled by TOTAL artifacts in existence (including bones-file ones), and u.uconduct.wisharti increments either way. Only quest artifacts are absolutely blocked. (3) "Cannot wish for the Amulet of Yendor" is misleading — objnam.c:5003-5006 silently substitutes a FAKE_AMULET_OF_YENDOR. Same trapdoor for Bell of Opening, Book of the Dead, Candelabrum, and (particularly relevant here) magic lamp -> oil lamp. Also dropped "+AC" from gauntlets of power notes — all gloves give +1 AC, the gauntlets just give +6 to-hit/dmg via STR 25. See companion-audit.md. -->

When the game asks "For what do you wish?", be specific. This is
not the time for ambiguity:

- "blessed +3 gray dragon scale mail" gets you exactly that.
- "gray dragon scale mail" alone lets the dice pick blessed/
  cursed and enchantment — a bare wish can roll cursed. You
  had *one* wish; spell out the BUC and the plus.
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

### Spellcasting
<!-- audit 2026-05-17 #59: corrected 6 substantive claims. (1) Force bolt damage is 2d12, not "d6 to 4d6 by skill"; spell-school skill doesn't scale damage. (2) Chain lightning is level 4, not 7, NODIR not "bouncing ray." (3) Failed reading does NOT paralyze or summon monsters; cursed_book enumerates teleport/aggravate/blindness/take-gold/confusion/contact poison/exploding rune/rndcurse (spell.c:130). (4) Spellbook decay is by SUCCESS count (MAX_SPELL_STUDY successful reads, spell.c:401-418), not failure wear; failures use a single 1/3 random destruction (spell.c:612). (5) "Spell maintenance" system is fabricated — no Pw drain from memorized spells anywhere in spell.c. (6) "Energy vortex + amulet of reflection = +max Pw" is fabricated; drain_en only ever decreases Pw. Also: blessed books bypass the read-ability check entirely (auto-success), not "equivalent to a few points of Int." Pw cost per spell is 5 × level. v2 audit 2026-05-18 #9: three factual fixes. (a) Spellbook fade ceiling is "four" not "about five" — MAX_SPELL_STUDY = 3 with `> MAX_SPELL_STUDY` check at spell.c:401 caps at 4 successful reads; the comment at spell.c:400 explicitly says "a normal book can be read and re-read a total of 4 times." (b) Charm monster "5×5 confused" implied confused casting works; spell.c:1372 fails confused casts outright. Reworded the row to drop the unreachable area and mention the Skilled+ blessed-scroll behavior. (c) Power-regen prose missed Intelligence and the Wizard-rate factor: allmain.c:605-607 uses `(Wis + Int)/15 + 1` with Wizards ticking on a factor of 3 instead of 4. Voice: full-paragraph parenthetical (Min Int+XL explainer) promoted to plain prose; the "1-in-3 destruction on failed read" caveat consolidated to the spellbook-fade paragraph (was duplicated earlier in the Learning Spells paragraph). Wisdom: softened the Valkyrie-identify line — Valkyries are restricted in divination per Skill_V (u_init.c:525-546), so reading identify is occasional-at-best. See companion-audit.md. -->

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

The chance of successfully reading a spellbook depends on the
**spell level**, your **Intelligence**, and your **experience
level**. The exact formula is `Int + 4 + XL/2 − 2·level` versus a
roll of 1d20, so read 20 or more always succeeds, 10 is a coin
flip, and anything below that is dicey. Reading a level-7 spell at
Int 15, XL 2 gives a read score of 6: only a 30% chance of
success. Lenses add +2. A **blessed** spellbook bypasses the check
entirely and always succeeds. A **cursed** spellbook fails
automatically and applies one of the failure effects above.

Here's a rough guide to what you can safely read:

| Spell Level | Minimum Int + XL needed | Who can read it reliably     |
| ----------- | ----------------------- | ---------------------------- |
| 1           | ~10                     | Almost anyone, early game    |
| 2           | ~14                     | Most characters by mid-game  |
| 3           | ~18                     | Wizards easily, others with effort |
| 4           | ~22                     | Wizards with decent stats    |
| 5           | ~26                     | Wizards with boosted Int     |
| 6           | ~30                     | Wizards with serious investment |
| 7           | ~34                     | Only well-built Wizards      |

The "Minimum Int + XL" column means the sum of your Intelligence
and experience level. With 18 Intelligence at level 14, your sum is
32, so you can reliably read up to level 6 spells. A blessed book
effectively adds 2-3 to this number.

**Wizards identify books by training.** In 5.0, advancing
a spell school skill to each rank automatically reveals the appearances
of spellbooks in that school: unskilled unlocks level-1 appearances,
basic level-3, skilled level-5, expert level-7. A Wizard starts knowing
all level-1 appearances and level-3 in attack and enchantment, which
means they begin the game with a meaningful identification advantage in
their core schools.

So training your spell schools pays off twice: better casting *and*
free book-ID. The unknown book you've been carrying since level 5?
Train up the right school and suddenly you know what it is.
Prioritize the schools containing your most-wanted unidentified
books, not just the ones that improve your current casting.

Wizards are the undisputed masters of magic: they learn faster, fail
less, and have the widest range of useful spells. A well-built Wizard
can eventually learn *every* spell in the game, which is the closest
the Mazes come to letting you cheat. Other roles can cast some spells
but with less panache. A Valkyrie can occasionally read identify
(level 3) if her Intelligence is boosted by gain-ability potions, but
non-spellcasters are usually better off with scrolls. Tourists,
Barbarians, and Cavemen should probably stick to hitting things.

Each spell stays in memory for about 20,000 turns, then fades and
must be relearned. The spell list (`+`) shows time-remaining. You
can also `a`pply a spellbook to check how worn it is: each
**successful** read counts toward a fixed total of four before the
book fades to blank paper. Failed reads don't add to that counter,
but each failure has its own 1-in-3 chance to destroy the book
outright. Carry important spellbooks with you if you plan to rely
on their spells in the late game.

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

#### Mana Management

Your power (Pw) pool determines how many spells you can cast before
you need to sit in a corner and regenerate like a phone battery.
Casting a spell costs **5 Pw per spell level** (so finger of death
is 35 Pw). A failed cast still spends half. Power regenerates over
time, faster with higher Wisdom and Intelligence, faster still for
Wizards or with a regeneration source.

High-level spells cost serious power. You can't spam finger of
death unless you have a colossal power pool, and even then you'll
run dry faster than you'd like. Plan your casting, carry backup
options (wands, scrolls) for when your mana runs low, and remember
that a Wizard who can't cast spells is just a person in a bathrobe
holding a stick.

---

### Curses and How to Break Them
<!-- audit 2026-05-18 #117: dropped the "Temple priest will identify BUC status for a fee" claim — fabricated. priest.c:629-718 shows temple donation grants HClairvoyant + u.ublessed (Protection); nothing in temple-donation code sets bknown on inventory. The "priest auto-bknown" code at invent.c:2763, 3545 and objnam.c:1964 refers to the PLAYER being a Priest class character (Priests see BUC for free), not to NPC temple priests. Common spoiler myth. Replaced with a brief myth-bust + added the formal price-ID-via-shop angle. -->


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

The lesson: always carry holy water and a scroll of remove curse.
The moment you find yourself stuck with cursed levitation boots
over a moat, you'll understand why veterans never leave home
without them.

---

### Luck and Fortune
<!-- audit 2026-05-18 #144: 7 corrections. (1) Cursed luckstone doesn't "reverse the drift" — timeout.c:616-619 cursed-only luckstone holds negative Luck in place but positive Luck still decays normally toward baseline. (2) "Uncursed luckstone freezes drift but gives no bonus" — wrong; attrib.c:441-450 set_moreluck gives +3 to any non-cursed luckstone (uncursed counts the same as blessed for the bonus). (3) Killing peaceful is -1 with 50% probability, not "-1 to -5" — mon.c:3665. -5 is for killing co-aligned unicorns specifically (mon.c:3667). (4) "At Luck -10 or worse, prayer always fails" — wrong threshold; pray.c:2155 rejects prayer on ANY negative Luck. (5) "Going down stairs in Sokoban -1" — fabricated; no luck penalty for descending Sokoban stairs. (6) "Throw real gem to cross-aligned unicorn -3 to +3" — that's only for fully identified gems (dothrow.c:2334 rn2(7)-3); unidentified is -1 to +1 (rn2(3)-1 at dothrow.c:2349). (7) "Identifying gems for a shopkeeper +1" — no such mechanic in shk.c; fabricated. Added killed_leader (-4 to baseline, timeout.c:600), full-moon/Friday baseline shift (timeout.c:595-598), and the doubled drift rate (300 turns) when carrying the Amulet of Yendor or u.ugangr > 0 (timeout.c:607). -->


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
it is until something changes it. This is why getting the luckstone
from Mine's End is one of the first things every experienced player
does. It's a small gray stone that makes the universe remember you
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
| Killing your quest leader                           | −4 to baseline luck (lasting penalty) |
| Attacking your pet                                  | −1          |
| Cannibalism                                         | −2 to −5    |
| Breaking a mirror or crystal                        | −2          |

The pattern is consistent: be virtuous and the numbers smile on you.
Be a monster and they frown. The Mazes have a moral compass, and
it's embedded in the math.

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
gamble. Archeologists begin with all gems identified, which is
why their class description mentions "unicorn negotiation" as a
class perk.

There is a ceiling on the luck you can harvest from any given corpse.
If your current luck score already exceeds the difficulty rating of the
monster you just sacrificed, you gain nothing. The altar accepts your
offering politely and gives you nothing in return, because the gods have
standards.

This closes a beloved old strategy: sitting at a co-aligned altar with
a pile of kobold corpses and grinding luck to maximum. It no longer
works once your luck is already above modest levels. To raise luck via
sacrifice in the mid-to-late game, you need fresh corpses of monsters
whose difficulty exceeds your current luck value. In practice: a
luckstone, occasional mid-tier sacrifices, and not killing peacefuls is
now the standard path to high luck. The dungeon made luck feel like luck
again.

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

At negative luck, all of these go wrong. **Any** negative Luck
causes prayer to fail with the "too naughty" rejection
(`pray.c:2155`) — not just at the floor of −10. You'll miss
attacks you should have hit. Scrolls will backfire. The dungeon
becomes a place that is trying to kill you even harder than
usual, which is saying something.

The practical advice: get a luckstone early, sacrifice occasionally
to keep luck positive, and don't kill peacefuls. Treat the universe
well and it will return the favor, in the form of slightly better
random numbers, which in the Mazes is the closest thing to love.

---

## Part Six: The Deep Dungeon

---

### The Castle
<!-- audit 2026-05-18 #109: 3 corrections to the Castle section. (1) "Maze section with a minotaur guarding it" is fabricated — castle.lua has no minotaur and no internal maze room (only mazewalk fill outside the fortress for entry corridors); minotaurs are placed in earth/fire/hellfill, not the Castle. Dropped the bullet. (2) "Elbereth keeps shopkeeper-class wanderers from stealing the treasure" — wrong target. The lua author's comment at castle.lua:150 says the engraving + cursed scroll are there to "Prevent monsters from eating it. (@'s never eat objects)" — i.e., they repel non-@ monsters that gnaw containers. Shopkeepers aren't repelled by Elbereth. Reworded. (3) "Intelligent monsters can unlock locked chests if they carry keys" — wrong for chests. muse.c:2273 mloot_container bails on olocked; monsters can unlock doors (monmove.c:1554) but never chests. The Castle wand chest is created locked at castle.lua:144, so it's safe from monster looting. Dropped the warning. Also added the storerooms (4 D-class dragons), central trap-door row (5 trap doors), fountain, and moat sea-monsters that the spoiler had omitted. v2 audit 2026-05-18 #32: three factual fixes. (a) "Throne room with a throne and guards" was wrong — castle.lua:54,195-221 fills the throne room with random L/N/E/H/M/O/R/T/X/Z court monsters, not soldiers; the soldiers/lieutenant guard the entry hall and tower corners. Reworded. (b) "Five trap doors at evenly-spaced squares" — castle.lua:156-160 places them at columns 40/44/48/52/55 (gaps 4/4/4/3), not strictly even. Dropped "evenly-spaced." (c) "Stepping on one drops you to a random Gehennom level" was wrong — trap.c:669-670 takes the Is_stronghold branch and calls find_hell (dungeon.c:1949-1953) which always sets dlevel=1, i.e. the Valley of the Dead. Reworded. See companion-audit.md. -->

If you've reached the Castle, congratulations: you've survived the
easy part. Everything below is worse.

The Castle sits at the bottom of the Dungeons of Doom, guarded by
a drawbridge and whatever the dungeon decided to stuff inside this
time. (5.0 at least no longer pre-loads the place with arch-liches
to greet you on arrival.) We covered how to find and enter it in
[Branches and Landmarks](#branches-and-landmarks). Here's what to
do once the drawbridge is down and you're standing in the foyer
wondering what you've gotten yourself into.

The Castle contains:

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
  all.* In 5.0, that chest also holds a **potion of gain level**,
  included as a small make-good for the wand's charge changes (see
  below). The chest's square is protected by a burned-in *Elbereth*
  engraving and sealed with a cursed scroll of scare monster. Those
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
(see Wands → Key Wands for the full mechanics).

Once you're fully equipped, the staircase down leads to Gehennom.
Take a moment before descending. Sit down. Have a snack. Check your
inventory twice. Make sure you have:

- Magic resistance
- Reflection
- Fire resistance
- Poison resistance
- A wand of digging
- A unicorn horn
- Plenty of food
- Holy water
- Scrolls of teleportation and identify
- Your quest artifact

If you're missing any of these, go back up and find them.

---

### Gehennom

Below the Castle, the dungeon changes. The corridors give way to
mazes. The monsters give way to demons. The comforting knowledge
that you can pray to your god for help gives way to silence, because
your god can't hear you in Gehennom. You are deeper than faith
reaches.

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
**Asmodeus** (cold- and poison-resistant, casts spells, carries a
wand of cold), **Baalzebub** (Lord of the Flies, surrounded by
a poison-gas cloud, summons swarms of flies), and **Juiblex**
(the Faceless Lord, a slime that engulfs in melee and splashes
acid). All three sit alone in their lairs and **won't pursue**
you, so you can avoid them entirely by skipping their level.

**Asmodeus and Baalzebub are bribable**: the demand is a random
fraction of the gold in your main inventory, so **stash gold in a
bag of holding before walking up to the throne** and a few hundred
zm will buy off a prince who would otherwise have demanded
thousands. **Juiblex is not bribable** — only the Arch-Devil
demons with the bribe disposition (Geryon, Dispater, Baalzebub,
Asmodeus) accept gold; Juiblex, Yeenoghu, Orcus, and Demogorgon
attack on sight regardless. Fighting Juiblex is viable late game
(wand of death works on all four), but expect a real fight.
None of their corpses is useful for sacrifice the way a fresh
weak monster's would be.

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

The arithmetic: 4/13 chance per sit of the wish ending it, so on
average you sit ~3 times before the wish (and absorb two of the
bad effects on the way). Plan accordingly. Stand at full HP,
don't carry potions you can't afford to grease, and have acid
resistance or magic resistance ready before you sit. If you don't
want a forced wish (say, you've already used your Castle wish and
Amulet wish and want to keep this one for the ascension kit), you
can sit at any time; you don't have to do it right now. The
throne stays put until something on the level destroys it.

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

His level is a *ghost town*: the layout of a normal shopping
district is preserved, but the shopkeepers and customers are all
dead — Orcus's presence ambient-kills everything not already
undead, and what's left is his honor guard of liches, vampires,
and ghouls. The buildings are stocked with random loot rather than
for-sale inventory; somewhere on the level the dungeon guarantees
either a **magic lamp** or a **magic marker** (50/50). The level
is studded with fire traps and magic traps, so don't sprint. Walk
it carefully, deal with the residents, and lift the lamp or marker
on your way out. Either is a meaningful supplement to the Castle
wand's single charge: a djinni wish (rub the lamp; the lamp
becomes ordinary afterward) or however many high-value scrolls
you can write before the marker runs dry.

#### The Wizard's Tower

Three sequential Gehennom levels (wizard1 → wizard2 → wizard3,
each reached by the normal down-stair from the level above) leading
to the **Wizard of Yendor** himself and the **Book of the Dead**.
He is the most dangerous enemy in the game — not because he's the
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

The Sanctum's up-stair lets you leave whenever you like, but the
**Astral plane portal at the top of the Endgame ladder won't open
without the Amulet** in your inventory.

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
   yanking you back down. Climb fast (see the Ascension Run
   section below).

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

---

### The Ascension Kit
<!-- audit 2026-05-17 #15: ~30 claims verified, 3 corrected (helm of holiness doesn't exist; prayer CAN cure hunger and uncurse worn items per pray.c). See companion-audit.md. -->

By the time you're ready to invoke Moloch's Sanctum, the loadout
that experienced players actually wear has converged. A survey of
recent ascensions from the public NetHack server shows what most
winners carry. Here is the canonical kit, slot by slot:

| Slot | Canonical pick | Notes |
|--------|------------------------|---------------------------------------|
| **Body** | Dragon scale mail | Gray (magic resistance) or silver (reflection) are the popular picks; blue (shock) also works. |
| **Cloak** | Cloak of magic resistance | Or a robe for casters. Magic resistance is non-negotiable in Gehennom. |
| **Helm** | Helm of brilliance or helm of telepathy | Brilliance for casters; telepathy when you might be blind. (Priest can wear the Mitre of Holiness for fire resistance + see invisible.) |
| **Gloves** | Gauntlets of power | Skip them only if you have a different STR strategy (e.g. a Knight with a +STR ring). |
| **Boots** | Speed boots | **Universal.** |
| **Shirt** | Hawaiian shirt or T-shirt | A free body slot under everything else — winners enchant it heavily (typically blessed +4 or +5) for several extra AC at no cost. |
| **Shield** | Mostly skipped | Reflection comes from silver dragon scale mail or an amulet instead; two-weapon fighters can't use a shield anyway. |
| **Amulet** | Amulet of life saving | The "extra life" plan. (An ascended Monk wore the Eye of the Aethiopica instead — a viable alternative for casters.) |
| **Ring (L)** | Free action | Anti-paralysis is non-negotiable on the Astral Plane. |
| **Ring (R)** | Slow digestion, conflict, or regeneration | Conflict is the standard Astral-Plane crowd-control choice. |
| **Weapon** | Your role's quest artifact + a silver saber | Silver saber appears in most builds as the off-hand because silver bypasses demon resistances. |
| **Pack** | Bag of holding, magic lamp, unicorn horn, luckstone, wand of death, multiple wands of teleport, seven candles | The "bag-of-holding bundle." Candles are for the Candelabrum — Izchak's Minetown lighting shop is an easy source. |
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
  of the Sanctum — burned the last wand-of-death charge before
  reserving an escape route, then died blind and surrounded.

The gear gets you to Gehennom. **Discipline** gets you to the
Sanctum. Keep at least one escape consumable (scroll of
teleportation, wand of digging, oilskin sack with a potion of full
healing) within reach at all times. Don't take a turn that isn't
moving you toward the Sanctum unless every adjacent square is
clear.

---

### The Ascension Run
<!-- audit 2026-05-18 #134: corrected three claims and added the missing Amulet-wish note. (1) "Mysterious Force yanks you back to a random location on the level instead of going up" — wrong; do.c:1541-1573 mostly sends you DOWN one to three levels (assign_rnd_level diff = rn2(3 + ualign.type)); the same-level teleport is the fallback when assign_rnd_level returns a no-op. Distance is alignment-biased (chaotic worst). (2) "Stops once you're above Gehennom, where the dungeon's grip weakens" — misleading; it's a hard Inhell gate at do.c:1541, not a gradient. Also never fires on the bottom 4 levels per dunlev < dunlevs_in_dungeon-3. (3) "Use Elbereth when you need a turn to heal" — wrong for almost the entire run; teleport.c:68-70 onscary() returns FALSE for Inhell || In_endgame, so Elbereth is dead in all of Gehennom and on all four Elemental Planes plus Astral. Added the Amulet-pickup wish (allmain.c:446-451 fires on next moveloop iteration after pickup, if !u.uevent.amulet_wish) and the 5.0 Mysterious-Force decay (do.c:1536-1563 — frequency tapers with each trigger). -->

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
whatever you're missing for the climb. You only get it once.

The Ascension Run is the victory lap that keeps killing even the
strongest adventurers. You have the most powerful artifact in the
dungeon in your pack, every covetous monster in the Mazes knows
it, and the dungeon itself is fighting to keep you from leaving.
The most exhilarating and terrifying stretch of the game.

#### The Problems

Everything that can go wrong will try:

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
  each time you climb stairs there's a chance you'll be dropped
  back **down** one to three levels instead of going up — the
  dungeon is literally holding onto you. (A smaller chance just
  teleports you elsewhere on the same level.) The pull is hardest
  on Chaotics, softest on Lawfuls, and in 5.0 it **decays** as
  it triggers: every yank slightly reduces the chance of the next
  one. The force is a hard `Inhell` gate — it stops the moment
  you climb out of Gehennom, and it also never fires on the
  bottom four levels.

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
- **Kill the Wizard fast.** When he shows up (and he will), don't
  try to be clever. Finger of death, wand of death, or brute force.
  The faster he's down, the fewer monsters he summons.
- **Don't rely on Elbereth past the Castle.** The `Inhell` and
  `In_endgame` checks in `onscary()` mean Elbereth is **completely
  ignored** in all of Gehennom and on all four Elemental Planes
  plus Astral. You can still write it for the alignment, but no
  monster will care. Plan your heal-and-recover breaks around
  corridors, scrolls of teleportation, and conflict instead.

The Ascension Run rewards preparation and punishes hesitation. If
you packed well at the Castle and your resistances are solid, this
is a sprint, not a marathon. Once you reach the top of the Dungeons
of Doom, the final staircase leads to the Elemental Planes: the
last obstacle between you and divinity.

---

### The Elemental Planes
<!-- audit 2026-05-18 #104: four substantive corrections. (1) Plane of Air vortex/bubble conflation: vortex AT_ENGL attacks just damage you, they do not move bubbles or carry you across the level. Bubble drift is a separate system implemented by mv_bubble in mkmaze.c:1648-1685, 1951-1965 — being inside a cloud-bubble whose position shifts each turn is what drifts you toward the portal. (2) Plane of Water drowning is NOT instant death — done(DROWNING) at trap.c:5171-5193 honors amulet of life saving; Breathless intrinsic (e.g. magical breathing amulet, Amphibious) prevents drowning entirely (trap.c:5106-5126). (3) Astral wrong-altar offering does NOT lose the Amulet for retrieval; pray.c:1562-1572 ends the game immediately with done(ESCAPED) and the opposing god gains dominion. The Amulet is consumed at pray.c:1537-1540 before the alignment branch. (4) Farlook on an altar only reveals alignment when you are ADJACENT to it; otherwise pager.c:744-754 returns "aligned high altar" with no alignment word. Also flagged in notes: every plane has noteleport, so wand-of-teleport on self silently fails (still works on monsters). See companion-audit.md. -->

Beyond the top of the Dungeons of Doom, the world dissolves into
its raw elements. Four planes stand between you and the gods, each
one a different flavor of hostile. There are no stairs here, only
magic portals, hidden somewhere in each level, leading to the next.
Find the portal. Survive the plane. Move on. There is no going back.

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
itself. (Note that teleportation is blocked on every plane, so
wand of teleport on yourself silently fails — it still works on
monsters for clearing space.)

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
so an **amulet of life saving** will rescue you — but you'll
drown again on your next turn unless something has changed.
The level is a labyrinth of water-filled chambers with occasional
air pockets. Sea monsters prowl the corridors.

**The standard tactic on arrival: genocide class `;`.** Read a
scroll of genocide, target the entire `;` class (eels, krakens,
sea monsters, sharks, jellyfish, piranhas), and the level instantly
empties of anything that can drag you under. This is the right
moment for that scroll — class `;` is almost nowhere else in the
game (a kraken in Medusa's pool, a moccasin from a fountain are
isolated encounters not worth burning a class-wipe on), and on the
next plane it's irrelevant. Spend the scroll here. Then find the
portal and push through. This is the last barrier between you and
the gods.

#### The Astral Plane

You surface into the presence of the divine. Three altars stand in
the great temple: Lawful, Neutral, and Chaotic. You must sacrifice
the Amulet of Yendor on the altar matching your alignment to
ascend. **Choose wrong and the game ends on the spot**: the
opposing god gains dominion over your god, and you've handed
victory to the other side. There is no retrieval — pick the
right altar the first time.

The plane is swarming with Angels and the three Riders: Death,
Famine, and Pestilence. The Riders cannot be permanently killed;
they revive, they pursue, they do not stop. Don't try to clear
the level. You are not here to fight. You are here to reach one
altar, make one sacrifice, and end this.

- Conflict and teleportation wands clear a path through the crowds
  — though note teleportation on **yourself** silently fails on
  every elemental plane (only monster-targeted teleport works).
- Identify the correct altar by walking adjacent to it: farlook
  (`;`) reveals an altar's alignment only when you're standing
  next to it. From across the room you only see "an aligned high
  altar." Plan to visit each in turn if necessary.
- The Riders will follow you. Outrun them, don't outfight them
- When you offer the Amulet on the correct altar: you ascend.
  The game is won. You've done what so few have done. Congratulations.

---

## Appendices

---

### Advanced Controls
<!-- audit 2026-05-17 #48: keystrokes (F, G, g, m, O, v, _, ;, /, Ctrl+A/P/R/O, #overview, #chronicle, #annotate, #conduct) all verified in cmd.c:1662-2065. number_pad/autopickup/pickup_types option semantics verified vs optlist.h. Corrected `verbose` claim: it controls extra descriptive messages (wielding/digging/sounds/pets), not "why multi-commands stopped." See companion-audit.md. -->

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
  Elbereth. Double-tap `F` to cancel without acting.
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

#### Options worth knowing about

Open the options screen with `O` (capital O, not zero). The
defaults are reasonable, but a few settings change how the
commands above feel:

- **`number_pad`** turns the numeric keypad into movement keys
  (1–9 for directions). Off by default; enabling it changes
  digit-prefix behavior so you press `n` first to enter a count.
- **`autopickup`** picks items up as you walk over them, filtered
  by `pickup_types` (e.g. `pickup_types:$?!` for gold, scrolls,
  and potions). The `m` prefix on movement suppresses autopickup
  for one step.
- **`verbose`** turns on a layer of extra descriptive messages
  (more detailed feedback when wielding, digging, hearing monsters,
  watching your pet, and so on). Turn it off if the message log
  feels noisy.

The full options list is deep, but the rest is taste and
convenience. If something about the interface annoys you, there is
almost certainly a setting for it.

A bigger interface shift requires a different binary: NetHack
built with the **curses** windowtype (`nethack-curses` on most
distributions, or a recompile with `WANT_WIN_CURSES`) draws a
properly paneled UI inside the terminal. Set `windowtype:curses`,
`align_message:right`, `align_status:bottom`, `perm_invent`, and
`windowborders` in your rc, open a 120×40 terminal, and you get a
permanent inventory column, a multi-line message panel, and
bordered status and map regions. Plain tty NetHack pins the
message line at row 0 no matter what you set.

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

**A note on mirroring.** In 5.0 of the game,
Sokoban levels may be flipped horizontally and/or vertically.
The solutions still work; just mirror the directions.

> *Solutions originally compiled by Boudewijn Waijers, with
> contributions by Jukka Lahtinen and others, for the steelypips.org
> NetHack archive maintained by Kate Nepveu. Adapted for 5.0 and reformatted
> for this guide.*

#### Level 1, Version A
<!-- audit 2026-05-17 #30: map/step internal consistency verified, 1 corrected (scroll coordinates "(3,12) and (4,12)" → "(2,12) and (3,12)" — column 4 is the ┌ wall character). See companion-audit.md. -->

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

One boulder (A) remains. The two scrolls at (2,12) and (3,12)
are always scrolls of earth.

#### Level 1, Version B
<!-- audit 2026-05-18 #153: clean. Map walls/floors and all 12 boulders A-L verified against soko4-2.lua:9-21, 29-42. Upstair (2,2), branch portal (4,2), 10 pits (5 cols 2 rows 3-7 plus 5 row 9 cols 2-6), 2 rolling-boulder traps, 2 always-scrolls-of-earth at (2,10)/(3,10). All 16 numbered solution steps land on lua floor with cardinal approach squares. "Two boulders (D and E) remain" tally checks out. -->


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

<!-- audit 2026-05-18 #154 (re-audit 2026-05-18 v2 #6): map walls/floors, all 20 boulders A-T, both stairs, locked door (27,9), rolling-boulder trap (11,10), and 15 hole traps verified clean vs soko3-1.lua:9-73. Steps 1-3 destinations are floor, approach squares reachable, cardinal-only pushes. v2 re-audit extended geometric verification through steps 4-9 and the final tally: the "Push F up to (3,4)" maneuver in step 8 is required, not gratuitous (after step 6 places F at (3,7), F seals the only N-S corridor through (3,6), so the only way to access the upper chamber for finishing F and A is to push F upward through the opening). All 15 finished boulders match the bowling-alley hole count; the "five remain" tally (B, C, D, I, Q) is exact. 0 corrections. See companion-audit.md. -->
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
<!-- audit 2026-05-18 #94 (re-audit 2026-05-18 v2 #56): 16-boulder layout + all 22 solution steps verified geometrically by simulation (player connectivity + clear-path checks). Intermediate diagrams at steps 9 and 16 match the simulated boulder positions. Both end-of-solution boulder lists correct. Close call: step 21's "G right 1, D up 1" is gratuitous (those boulders aren't going to a hole) but harmless. v2 corrected the pass-1 badge: the actual source file is soko3-2.lua, not soko2-2.lua (NetHack Sokoban numbers .lua files from bottom up, so spoiler "Level 2" = second-from-top = soko3-X). Map is a stylized rendering of soko3-2.lua, topologically equivalent. v2 re-verified all 16 boulders and step 17 (push H left) is necessary, not cosmetic. 0 spoiler-text corrections. See companion-audit.md. -->

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

<!-- audit 2026-05-18 v2 #1: 13-boulder layout and all 13 solution steps verified geometrically against dat/soko2-1.lua:9-62. Upstair (17,5), downstair (7,11), locked door (19,9), 10 hole traps row 10 cols 9-18, rolling-boulder trap (8,10) all match. Final "three boulders remain" tally checks. Backfill: this section had no pass-1 badge while neighbors (Levels 2A, 2B, 3B) did. See companion-audit.md. -->
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
<!-- audit 2026-05-18 #112 (re-audit 2026-05-18 v2 #60): upstair < was placed at spoiler (16,8) in both the initial and intermediate maps; soko2-2.lua:25 puts it at (15,6) which translates to spoiler (16,7). Moved up one row in both maps. Otherwise clean: 16 boulders match, 15 solution steps verified against soko2-2.lua. v2 re-verified: all 16 boulders A-P map exactly to lua coords; upstair at (16,7), downstair/start at (7,12), rolling-boulder trap at (8,12) with 11 holes at cols 9-19, two locked doors at (20,10) and (20,12). 15 steps compress Boudewijn Waijers's original 22; each push geometrically reachable. "Five boulders remain" tally exact. 0 corrections. See companion-audit.md. -->

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

#### Level 4, Version A (prize: usually bag of holding, 25% amulet of reflection)

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

#### Level 4, Version B (prize: usually amulet of reflection, 25% bag of holding)
<!-- audit 2026-05-17 #31: prize odds verified (25% BoH / 75% AoR per soko1-2.lua:105). Map data + step instructions are tactical, not statically verifiable. See companion-audit.md. -->

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
<!-- audit 2026-05-18 #142: 5 corrections. (1) "Brown and yellow puddings" — there is no yellow pudding; S_PUDDING per monsters.h:2081-2113 is gray ooze / brown pudding / green slime / black pudding, and per mondata.h:241 the vegetarian-safe ones are all but black pudding (so gray ooze, brown pudding, green slime). (2) Shriekers are S_FUNGUS — already covered by "all F (fungi and molds)," so the separate mention is misleading. (3) "Avoid eating eggs, pancakes, lumps of royal jelly, cream pies, and candy bars" — incomplete: fortune cookies ALSO break vegan (eat.c:3016 lists FORTUNE_COOKIE as VEGGY-but-vegan-violating), so the spoiler's "vegetarian-friendly fortune cookie" advice contradicts itself. (4) Foodless: "polymorphing breaks foodless" — wrong. polyself.c has no u.uconduct.food increment; polymorph only breaks the polyself conduct. (5) "Prayer cures hunger when you're Weak or Fainting" — wrong threshold; pray.c:275 TROUBLE_HUNGRY fires at uhs >= HUNGRY (Hungry / Weak / Fainting all qualify). v2 audit 2026-05-18 #2: corrected pudding "corpses" to globs (puddings are G_NOCORPSE per monsters.h:2081-2113); replaced fabricated "internal egg-derived material flag" claim with the in-world reason that fortune cookies contain eggs (the eat.c:3016-3018 list is hardcoded otyp, no such flag); dropped "all ghosts" from the vegan corpse list (S_GHOST is G_NOCORPSE per monsters.h:2888,2897); removed S_PUDDING C-identifier from prose; added vegetarian-not-safe warning (yellow mold, violet fungus, acid blob); added Monk vegetarian-is-mostly-free note; added wish-for-slow-digestion route to foodless; trimmed two filler sentences and the orphan polyself clarification; checked data.base:570-576 — the "dairy" reason for vegan-excluding puddings is not lore-supported (puddings are described as amoeboid slimes), so the rule is stated without a fabricated reason. See companion-audit.md. -->

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
`'` (golems) except flesh golems and leather golems. Vegetarian-safe
is not the same as safe. Yellow mold corpses poison, violet fungus
paralyzes, and acid blobs sting going down. Monks already pay an
alignment penalty for meat, so vegetarian is mostly free for them.

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
<!-- audit 2026-05-17 #64: u.uconduct.gnostic verified (insight.c:2134, topten.c:590). #pray (pray.c:2221), #offer corpse (pray.c:1977), #turn (pray.c:2426), and #chat with priest (priest.c:572) all confirmed as breaking the conduct. Corrected false claim about altar BUC: do.c:370 increments gnostic on any non-coin drop, so the BUC flash is a religious interaction. Added: the final Amulet offering for ascension is exempt (pray.c:1529-1588 has no gnostic increment). See companion-audit.md. -->

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
<!-- audit 2026-05-18 #128: clean conduct logic per uhitm.c:616-617 (weaphit++ requires weapon non-NULL AND (WEAPON_CLASS || is_weptool)). Added the missing weapon-tool list (pick-axe, unicorn horn, aklys, iron chain etc. all break conduct via the is_weptool branch), and the one ranged exception that DOES break weaponless: wielded polearm at range via #apply, the HMON_APPLIED path at dothrow.c:2199-2203. Confirmed thrown weapons / fired ammo / wands / spells / barehand / martial arts / cockatrice-corpse-wield all do NOT break the conduct. -->

Never hit a monster with a wielded weapon or weapon-tool. You can
throw weapons, fire them from bows and crossbows, and use wands
and spells. You can also fight bare-handed or with martial arts
(Monks excel here). What you cannot do is swing a sword, axe,
mace, pick-axe, unicorn horn, aklys, iron chain, or any other
weapon-class or weapon-tool item in melee while it's in your
`w`ielded slot. The one ranged exception that *does* break the
conduct: using a wielded polearm at range via `#apply`.

This is less restrictive than it sounds. Monks start with strong
martial arts and get better. Other classes can rely on spells,
wands, and thrown daggers. A wielded cockatrice corpse still works
(it's not a weapon). The main sacrifice is giving up the damage
output of late-game artifact weapons.

#### Pacifist
<!-- audit 2026-05-17 #53: all claims verified. u.uconduct.killer incremented only by xkilled (mon.c:3500) and the explicit "pet killed by trap you pushed it into" case (hack.c:2201); pet/conflict kills don't count. Charm-monster spell + Elbereth + pet tactics all verified. 0 corrections. See companion-audit.md. -->

Don't kill any monsters. Not directly, not with pets, not through
any means that the game attributes to you. The pacifist runs on
pets doing the fighting, on conflict to make monsters attack each
other, on Elbereth to keep them at bay, and on creative use of
the dungeon environment.

Pacifist ascensions are possible but require deep knowledge of the
game's mechanics. Most pacifist players use a large, well-trained
pet (often polymorphed into a purple worm or similar), the spell
of charm monster, and extremely patient tactics.

#### Illiterate
<!-- audit 2026-05-18 #87 (re-audit 2026-05-18 v2 #54): corrected "engraving is fine" — only an "x" or "X" signature engrave is exempt (engrave.c:1213); anything else breaks the conduct. Confirmed: scrolls, spellbooks, fortune cookies, T-shirts, magic-marker writing all count (read.c:602, eat.c:2525, read.c:397, write.c:245). Blank paper, novel-if-unread, Book of the Dead, Hawaiian shirts, and reading floor engravings (Elbereth) do NOT count. Pet-on-scroll workaround verified. v2: softened "Without spellbooks, you have no spells" — starting spells last ~20K turns per spell.h:17 KEEN, so a Wizard/Priest/Healer/Monk/Knight has access to one pre-learned spell until it fades. The full forbidden-reads list (coins, credit cards, candy bars, magic markers, dunce caps, Orb of Fate signature, artifact naming, Archeologist auto-decipher on pickup) is real but per no-trivia, the section deliberately gives the headline cases rather than enumerating every edge. See companion-audit.md. -->

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

#### No Genocide
<!-- audit 2026-05-18 #108: three corrections to the No Genocide conduct text. (1) "Astral Plane's final wish" path is fabricated — wishes never offer genocide. Genocide is only prompted by reading a scroll of genocide (uncursed = single species; blessed = whole class via do_class_genocide at read.c:2638) and by sitting on Vlad's throne (sit.c:131 do_genocide(5)). (2) "Leave it blank" is misleading for cursed scrolls — empty input re-prompts (read.c:2865-2871) and on a cursed scroll the random rndmonst() path (read.c:2848-2849) creates monsters rather than letting you escape; type "none" instead. (3) End-of-game tracking is by counting G_GENOD species in mvitals[] (insight.c:2951-2966 num_genocides), not a u_conduct counter — but the conduct is preserved as long as no species ever gets G_GENOD'd. The conduct survives even on a cursed scroll's monster-creation path because no species is flagged. See companion-audit.md. -->

Never genocide any monster. Genocide is prompted by reading a
**scroll of genocide** (uncursed picks one species; blessed wipes
the whole class) and by **sitting on Vlad's throne**, which has
one outcome that prompts you to genocide a class. To preserve the
conduct, type **"none"** at the prompt — don't just press Enter,
because empty input re-prompts and on a *cursed* scroll the game
will eventually conjure random monsters instead of letting you
escape.

This means you'll face the full bestiary throughout the game,
including master and arch-liches, mind flayers, cockatrices, and
everything else that experienced players routinely eliminate.
You'll also have to cross the **Plane of Water** the hard way: the
standard tactic of genociding class `;` to clear out the eels and
krakens is off-limits, so bring magical breathing and pay attention
to where the sea monsters can reach you.

This is one of the milder conducts: many players ascend without
genociding anything simply because they never find the scroll and
never sit Vlad's throne. But deliberately maintaining it against
late-game threats takes discipline.

<!-- audit 2026-05-18 #161: dropped "cursed scroll of polymorph" (no SCR_POLYMORPH exists in 5.0). Added missing conduct-breaking sources: genetic engineer claw (AD_POLY → polyself); eating chameleon/doppelganger/sandestin corpses (eat.c:1244-1263) and mimic corpses (eat.c:1199); green slime auto-poly (timeout.c:493); stone-golem auto-poly via poly_when_stoned (trap.c:3848 etc.). Added Unchanging-blocks-all and system-shock-doesn't-break notes per polyself.c:483-495. v2 audit 2026-05-18 #20: two narrow factual fixes (everything else proposed by the sub-agent was reverted as scope-creep — the section is about the conduct, not an encyclopedia of polymorph mechanics). Dropped "sandestin" from the corpse list since sandestins are G_NOCORPSE (eat.c:1246 comment, unreachable). Dropped "surviving a stoning attack (auto-transforms to stone golem)" because poly_when_stoned (mondata.c:80-86) only fires if you're already polymorphed into a non-stone golem; a normal character just dies. See companion-audit.md. -->
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
<!-- audit 2026-05-18 #83 (re-audit 2026-05-18 v2 #58): u.uconduct.wishes and u.uconduct.wisharti are two separate counters with two separate xlogfile achievements (you.h:157-158, topten.c:596-597). Wishing for the literal string "nothing" doesn't increment the counter (zap.c:6369). Amulet-of-Yendor first-pickup wish (allmain.c:445) must be declined for wishless conduct. v2 re-verified: wisharti counter ticks even for *denied* artifact wishes per objnam.c:5362-5365 (before the deny branch); fountain water demon routes through mongrantswish → makewish; wresting empty wands also routes through makewish at zap.c:2583. 0 corrections. See companion-audit.md. -->

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
<!-- audit 2026-05-17 #52: u_conduct/u_roleplay fields verified against insight.c + you.h + topten.c. Verified: nudist/blind tracking since 3.6, 5.0 added pauper/petless/permadeaf/sokoban/bonesless, vegan ⊂ vegetarian hierarchy, show_conduct end-screen listing. Cross-section fix in Bonesless below removed false claims about lucky-no-bones earning the conduct and about #conduct tracking lifesaving uses. See companion-audit.md. -->

The real prestige comes from combining multiple conducts. A
vegetarian atheist run is substantially harder than either alone.
A pacifist illiterate vegan foodless atheist weaponless run is
the stuff of legends (and has been done). The game's end screen
lists all maintained conducts, and the community has long
celebrated players who push the boundaries of what's possible
within self-imposed constraints.

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
Permadeaf, Sokoban, and Bonesless. The first three are start-of-game
options; the latter two are tracked automatically based on what you
do during the run.

#### Pauper (new in 5.0)
<!-- audit 2026-05-17 #72: ini_inv early-return at u_init.c:1308-1309 confirmed (no starting items at all, not just no armor/gold). nudist cascade at options.c:5290-5293. End-of-game string at insight.c:2117-2119. xlogfile at topten.c:604. Corrected "permanent conduct, set at birth and never lost" — pauper flag itself is permanent, but the cascading nudist flag IS cleared the moment you wear armor (worn.c:135-136). Added the pauper compensations from u_init.c:870+ (weapon-skill slots, known spell/item per role, supply chests). See companion-audit.md. -->

Start with absolutely nothing: no gold, no inventory, no armor, no
starting weapon. Set `OPTIONS=pauper` in your rcfile (rcfile or
command line only; the in-game `O` menu cannot toggle it). Pauper
implicitly sets nudist as well, so you also begin without armor.
Pauper is a permanent conduct you never lose: it does not forbid
acquiring or spending gold later. The conduct is about starting
empty, not about staying penniless.

To keep the start from being impossible, the game compensates:
you get two unspent weapon-skill slots and your role knows one
signature spell or item (Wizard knows force bolt, Healer knows
healing, Archeologist knows touchstone, Rogue and Tourist know
sack, Cleric knows water, Samurai knows gunyoki rations). The
**supply chests** scattered on early levels above the Oracle (a
feature in every 5.0 game, not just pauper) can provide much of
your first kit.

#### Petless (new in 5.0)
<!-- audit 2026-05-17 #50: all claims verified. pettype:none bypasses pet_type via dog.c:225-229; tamedog increments u.uconduct.pets across all taming paths; minion.c:533-539 explicitly preserves petless on the endgame angel. xlogfile achievement at topten.c (add_achieveX "petless"). 0 corrections. v2 audit 2026-05-18 #59: corrected one fabricated mechanism. "Dairy products to foocubi" is not a thing — befriend_with_obj at mondata.h:255-261 gates food-throw taming on is_domestic(ptr) (plus monkey/ape + banana), and foocubi aren't domestic. The wiki-known foocubus interaction is throwing a ring of adornment (pacification, not taming), not dairy. Replaced with "food thrown at hostile dogs and cats" — the actual food-throw taming path that was missing from the list. See companion-audit.md. -->

Never have a pet. Set `OPTIONS=pettype:none` in your rcfile to skip
the starting companion entirely (this overrides per-role defaults).
After that the conduct enforces itself: don't tame anything via
scrolls of taming, charm-monster spells, food thrown at hostile
dogs and cats, or magic-trap accidents. You lose the curse-detection
trick, the combat assist, the shoplifting option, and the
companionship. What you gain is the particular satisfaction of
knowing that everything that died did so by your hand, and that you
never had to feel guilty about leading something loyal into a
polymorph trap.

#### Permadeaf (new in 5.0)
<!-- audit 2026-05-17 #62: confirmed permadeaf is u.uroleplay.deaf (optlist.h:267-269), recorded in xlogfile (topten.c:602) and shown in show_conduct (insight.c:2113). Deaf macro at youprop.h:125. Corrected the rcfile option name: was `!acoustics` (a different per-session flavor flag — flags.acoustics — that doesn't earn the conduct), should be `permadeaf` (or `deaf`). Also removed the in-game O-menu instruction: this option is `set_in_config` (options.c:5207), rcfile/command-line only. See companion-audit.md. -->

Never hear anything. Set `OPTIONS=permadeaf` (or `OPTIONS=deaf`)
in your rcfile, or pass `-Dpermadeaf` on the command line. This
one is rcfile or command line only; the in-game `O` menu cannot
toggle it. (Don't confuse `permadeaf` with the unrelated
`acoustics` flavor toggle, which doesn't earn the conduct.) The
game then runs as if you had the Deaf intrinsic from turn one and
never recovered: all the "you hear water falling", "you hear
someone counting money", "you hear a door open" messages and the
ambient monster sounds ("you hear a slurp" and friends) are
suppressed.

Many monster warnings, environmental cues (vaults, fountains, doors
opening off-screen), and status messages arrive as sounds. Permadeaf
requires navigating the dungeon by sight and logic alone, which turns
out to be possible and occasionally educational about how much
information you normally get for free.

#### Sokoban (new in 5.0)
<!-- audit 2026-05-18 #145: corrected "No digging through the puzzle levels" — digging doesn't trigger sokoban_guilt (dig.c has no such call). The conduct-violating actions are squeeze (hack.c:299, 307), boulder fracture by wand of striking (zap.c:5556), polymorph boulder (zap.c:1711), scroll of earth (read.c:1951), and dismount onto a boulder (steed.c:767). Each costs -1 Luck (trap.c:7039-7054) and increments u.uconduct.sokocheat. Achievement reported only if the branch was entered (insight.c:2215-2228). Teleportation IS blocked by the level's noteleport flag (teleport.c:1185), so "no teleportation" is a level constraint, not a conduct trigger. -->

Complete Sokoban without breaking the rules. Each cheating action
costs **1 point of Luck** and increments the conduct counter: pushing
into a wall to **squeeze past** a boulder (when you drop your stuff
to fit), **fracturing** a boulder with a wand of striking or scroll
of earth, **polymorphing** a boulder, or **dismounting** onto a
boulder. Levitation and flying skip pits without penalty. The game
tracks violations automatically. The conduct is for players who
enjoy Sokoban's
boulder-shoving and want their playthrough to acknowledge a
clean solve.

#### Bonesless (new in 5.0)
<!-- audit 2026-05-17 (sweep from #52) (re-audit 2026-05-18 v2 #48): the xlogfile bonesless achievement is set only if !flags.bones (topten.c:605), i.e. you turned bones loading off. Just *not encountering* bones is a separate Miscellaneous enlightenment line ("never encountered any bones levels", insight.c:439) and is NOT the bonesless conduct. Earlier text wrongly said you could "get bonesless by luck." Also removed false "amulet of life saving" tracking claim (show_conduct never lists lifesaving uses). v2 re-confirmed: `bones` is set_in_config per optlist.h:213-215 (config file / command line only, not the in-game O menu); !flags.bones blocks both save (bones.c:360) and load (bones.c:642) — "cuts both directions"; the "didn't encounter any bones levels" enlightenment is distinct (insight.c:439-441 requires flags.bones true + u.uroleplay.numbones==0). 0 corrections. See companion-audit.md. -->

Never inherit from another player's grave. To get the bonesless
conduct, you have to turn bones off for the run: set
`OPTIONS=!bones` in your rcfile (rcfile or command line only;
the in-game `O` menu cannot toggle it). The same flag also stops
your *own* death from generating a bones file for future players,
so `!bones` cuts both directions of the bones cycle. The bonesless
achievement is recorded only when bones was disabled, not when
you happened not to encounter any. (Going a whole game without bones because the
dungeon directory has nothing eligible is a separate enlightenment
line — "never encountered any bones levels" — and doesn't earn
the conduct.)

---

### Shopping and Shopkeeper Pricing
<!-- audit 2026-05-17 #47: 22 gem prices, Mohs hardness, hard-gem threshold (>= 8), unidentified-gem 3-8 zm formula, Tourist/dunce-cap surcharge, unicorn luck mechanics, Excalibur 16000 example, shopkeeper anti-Elbereth + see-invisible behavior, Keystone Kops trigger, "Closed for inventory" engraving, Orcus-level shopkeeper death, credit/debit/loan ordering all verified against shk.c + objects.h + shknam.c. Corrected one Wrong: amethyst+booze produces fruit juice (potion.c:2161), NOT cure for hallucination — fixed in both the gem table and the Amethyst special-case paragraph. See companion-audit.md. -->

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
Credit is per-shop and per-shopkeeper: you can't carry it between
shops, withdraw it back to gold, or hand it to a different
shopkeeper.

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
unfazed by Elbereth. Pay the bill at the door.

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
- Shop walls are non-diggable from inside, so tunneling out with
  unpaid items is not on the menu.
- Artifact items are priced at special high prices. For most named
  weapons that lands in the 10,000–30,000 zm range. An unidentified
  long sword priced at 16,000 zm is not something to glance over:
  that exorbitant price is a give-away.
- A shopkeeper *can* be killed for the entire stock plus the till
  (1,000–4,000 zm and a skeleton key on death), but they're a tough
  fight (high HP, low AC, hits hard with their weapon), and killing
  them summons a wave of Keystone Kops to pursue you, costs you a
  chunk of alignment, and leaves the shop permanently empty: no more
  buying, no more selling, no more price-ID from that shopkeeper.
  Two community notes worth knowing: **polymorphing the shopkeeper
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
  so the items there often *are* ownerless, but that's because of
  Orcus, not the engraving.)

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
unidentified hard gem against a non-cursed touchstone produces a
streak that names the gem. Once identified, real gems sell for their
real value (often hundreds of zm each) while glass sells for almost
nothing.

##### Real-gem prices

Once you know what a gem is, its type determines its base price.
Real gems are tiny piles of liquid gold by weight: every gem weighs
just 1, and gems of the same identified type stack into a single
inventory slot regardless of count, so the only cost of hoarding a
heap of identified rubies is one slot's worth of clutter.

Every real gem, with the unangry-shopkeeper buy price. Use the
Cha/Sell/Tourist/Angry toolbar to see how the modifiers shift
things.

The Mohs column is real-world mineral hardness on the Mohs scale
(talc 1, diamond 10), and the game uses it in two places. Gems of
Mohs 8 or higher count as **"hard"**, and hard gems do two things
softer gems and glass can't: they can be used as a stylus to
*engrave* Elbereth and other messages permanently into the dungeon
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
|     0 | (worthless glass)     | any color       |    5 | sells for 0–8 zm unidentified  |

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
  accepted with no effect. The luck risk on unicorn throws comes
  from *real* gems thrown at the **wrong-alignment** unicorn, which
  rolls a random −3 to +3.

Read the table as a **selling guide**, not a discard guide: real
gems near the top are worth making time to sell at a gem dealer
and worth wishing for if you're flush on wishes. Lower-priced gems
aren't trash — they still feed unicorns and still touchstone-identify
other gems by hardness comparison.


---

### Weapons Tables

Damage is shown as **vs small / vs large**, the dice rolled before enchantment and excluding silver/material bonuses. **Wt** is unit weight; **Cost** is the unenchanted shop base price in zorkmids. **Hit** is the to-hit bonus baked into the weapon itself (most are 0). Two-handed weapons that prevent shield use and two-weapon combat are flagged in the notes. Weapons are grouped by their skill class so you can see your options within each skill tree at a glance.

#### Dagger
<!-- audit 2026-05-18 #119: 3 corrections. (1) "Rogues multishot up to three" — wrong; Expert Rogue gets 1 base + 1 Expert + 1 Skilled-fallthrough + 1 class bonus = max 4, then rnd(4) yields 1-4. dothrow.c:177-190, 63-67. (2) Athame Elbereth "lasts longer" — wrong mechanism; the athame's real property is that it doesn't dull when engraving (engrave.c:1306-1307, comment at :1361), so you can write Elbereth without consuming enchantment. Duration is unchanged. (3) Silver dagger "Silver damage to demons" — scope too narrow; silver hurts anything where mon_hates_silver() returns true: demons, undead, lycanthropes, shades (uhitm.c:896, 1035, 1376). Also flagged stackable consistency for silver dagger and athame (both have mg=1). -->


::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| dagger | 1d4 / 1d3 | 10 | 4 | +2 | iron | Stackable; Expert-skill Rogues can multishot up to four in a single throw. |
| elven dagger | 1d5 / 1d3 | 10 | 4 | +2 | wood | Stackable. Sting is the artifact form. |
| orcish dagger | 1d3 / 1d3 | 10 | 4 | +2 | iron | Stackable. |
| silver dagger | 1d4 / 1d3 | 12 | 40 | +2 | silver | Stackable. Silver damage to demons, undead, lycanthropes, and shades. Common Rogue/Ranger off-hand. |
| athame | 1d4 / 1d3 | 10 | 4 | +2 | iron | Stackable. Engraving with an athame **doesn't dull the blade** — you can write Elbereth in dust without spending an enchantment, the way other weapons must. |

:::

<!-- audit 2026-05-18 #169: all 5 rows verified clean vs objects.h:215-233 (P_KNIFE skill; scalpel METAL, knife/stiletto IRON, worm tooth/crysknife BONE). Added Healer's-starter note for scalpel (u_init.c:77). Rewrote crysknife note: "polymorphs" → "reverts" (type-id swap path at do.c:903-918, not poly machinery); a fixed (erodeproof) crysknife only reverts on ~10% of drops (do.c:911). See companion-audit.md. -->
#### Knife

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| scalpel | 1d3 / 1d3 | 5 | 6 | +2 | metal | The Healer's starter. |
| knife | 1d3 / 1d2 | 5 | 4 | — | iron |  |
| stiletto | 1d3 / 1d2 | 5 | 4 | — | iron |  |
| worm tooth | 1d2 / 1d2 | 20 | 2 | — | bone |  |
| crysknife | 1d10 / 1d10 | 20 | 100 | +3 | bone | Reverts to a worm tooth when dropped. Keep it wielded; a fixed (erodeproof) crysknife reverts on only ~10% of drops. |

:::

<!-- audit 2026-05-18 #163 (re-audit 2026-05-18 v2 #16): all 4 rows verified clean vs objects.h:245-254. All share P_SHORT_SWORD (scimitar is P_SABER, correctly excluded). No artifact uses SHORT_SWORD base type. Samurai's "wakizashi" is a SHORT_SWORD aliased in objnam.c:106; added to plain short sword's Notes. 0 numeric corrections. v2 re-audit confirmed: all four rows match objects.h:244-255 exactly (short sword 1d6/1d8, elven 1d8/1d8, orcish 1d5/1d8, dwarvish 1d7/1d8). Rogue starter at u_init.c:134; Samurai wakizashi alias at u_init.c:144 + objnam.c:106. No SHORT_SWORD-base artifact exists. See companion-audit.md. -->
#### Short sword

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| short sword | 1d6 / 1d8 | 30 | 10 | — | iron | The Rogue's starter; Samurai's *wakizashi* is just a short sword by another name. |
| elven short sword | 1d8 / 1d8 | 30 | 10 | — | wood |  |
| orcish short sword | 1d5 / 1d8 | 30 | 10 | — | iron |  |
| dwarvish short sword | 1d7 / 1d8 | 30 | 10 | — | iron |  |

:::

#### Saber
<!-- audit 2026-05-17 #38 (re-audit 2026-05-18 v2 #33): 10 cells verified, 1 corrected (silver saber notes mentioned only Werebane; Grayswandir is the better-known silver saber artifact). v2 found the silver-saber row described Grayswandir as "+5 hit, hallucination resistance" — PHYS(5,0) at artilist.h:172 gives +1d5 to-hit AND doubles damage (artifact.c:1083-1086, 1106-1107), same shape as Demonbane (already corrected in #12). The Artifacts chapter at line 4219 has the correct phrasing. Per no-trivia rule, replaced the inline parenthetical effects with "see Artifacts" rather than duplicating the canonical chapter. See companion-audit.md. -->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| scimitar | 1d8 / 1d8 | 40 | 15 | — | iron |  |
| silver saber | 1d8 / 1d8 | 40 | 75 | — | silver | Silver does bonus damage to demons/weres/vampires/imps. Artifact forms: **Grayswandir** and **Werebane** (see Artifacts). |

:::

#### Broadsword
<!-- audit 2026-05-18 #103: Stormbringer's base item is RUNESWORD per artilist.h:93, not broadsword. Moved the attribution and added the drain-life detail. Both share the same skill class (P_BROAD_SWORD) and the same 1d4+1d4/1d6+1 dice, which is what makes the confusion easy. v2 audit 2026-05-18 #7: dropped the redundant "+d4 small, +1 large" Notes-cell formula on the broadsword row (already encoded in the Damage column). An initial v2 edit named Dragonbane (BROADSWORD, artilist.h:157-160) and Orcrist (ELVEN_BROADSWORD, artilist.h:134-136) with their effects, plus expanded the Stormbringer note; reverted as trivia — the Artifacts chapter is the canonical home for artifact details. See companion-audit.md. -->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| broadsword | 1d4+1d4 / 1d6+1 | 70 | 10 | — | iron |  |
| elven broadsword | 1d6+1d4 / 1d6+1 | 70 | 10 | — | wood |  |
| runesword | 1d4+1d4 / 1d6+1 | 40 | 300 | — | iron | Stormbringer is the chaotic artifact form. |

:::

#### Long sword
<!-- audit 2026-05-18 #78: stats verified vs objects.h:270-280. Excalibur dipping note rephrased to clarify ANY alignment rolls 1-in-30 at XL 5+, but only Lawfuls succeed (non-Lawfuls get the sword cursed). Listed all four artifact forms (Excalibur, Vorpal Blade, Frost Brand, Fire Brand). Also corrected adjacent two-handed-sword row: "Vorpal Blade is the artifact form" was wrong (Vorpal Blade is a LONG_SWORD artifact per artilist.h:191); two-handed sword has no dedicated artifact. v2 audit 2026-05-18 #10: an initial v2 edit added Giantslayer (artilist.h:174) and Sunsword (artilist.h:209) to bring the LONG_SWORD artifact list to six; reverted as trivia, restored to the original four (Excalibur, Vorpal Blade, Frost Brand, Fire Brand). Voice: Excalibur dipping line reworked from a semicolon-and-parenthetical chain into four periods per the punctuation ladder. See companion-audit.md. -->


::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| long sword | 1d8 / 1d12 | 40 | 15 | — | iron | At XL 5+, dipping in a fountain rolls 1-in-30. Knights get 1-in-6. On a hit, Lawfuls get **Excalibur**. Others get the sword cursed. Artifact forms: Excalibur, Vorpal Blade, Frost Brand, Fire Brand. |
| katana | 1d10 / 1d12 | 40 | 80 | +1 | iron | +1 to-hit baked in. Snickersnee is the artifact form. |

:::

#### Two-handed sword
<!-- audit 2026-05-18 #127: clean stats vs objects.h:273-285. Added the 5.0 3/2 Str damage bonus for bimanual weapons (uhitm.c:1467-1468, gated on bimanual(uwep) + HMON_MELEE) which the section had previously omitted; bonus also applies to battle-axe, dwarvish mattock, bardiche. Confirmed Tsurugi is the artifact form (artilist.h:285-289), not Vorpal Blade (which was a corrected misattribution in earlier audit #78). -->

Two-handed weapons get a **3/2 Strength damage bonus** in 5.0 —
your STR damage contribution is multiplied by 1.5 when wielding a
bimanual weapon. Combined with the high base dice below, that's a
big chunk of why two-handed swords compete with one-hand-plus-
shield even though you forfeit the shield slot. The same bonus
applies to the battle-axe, dwarvish mattock, bardiche, and any
other bimanual weapon.

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| two-handed sword | 1d12 / 1d6+2d6 | 150 | 50 | — | iron | Two-handed (no shield, no off-hand weapon). No dedicated artifact form. |
| tsurugi | 1d16 / 1d8+2d6 | 60 | 500 | +2 | metal | Two-handed. The Tsurugi of Muramasa is the artifact form. |

:::

#### Axe

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| axe | 1d6 / 1d4 | 60 | 8 | — | iron |  |
| battle-axe | 1d8+1d4 / 1d6+2d4 | 120 | 40 | — | iron | Two-handed (gets the 5.0 3/2 Str damage bonus). +1d4 small, +2d4 large. The Barbarian quest artifact **Cleaver** is a battle-axe. |

:::

<!-- audit 2026-05-18 #160: pick-axe row was missing entirely. Added per objects.h:1007-1009 (WEPTOOL, wt=100, cost=50, 1d6/1d3, iron). Mattock stats verified vs objects.h:345-347. Both share P_PICK_AXE skill and both route through use_pick_axe() (apply.c:4290-4292). See companion-audit.md. -->
#### Pick-axe

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| pick-axe | 1d6 / 1d3 | 100 | 50 | — | iron | Weapon-tool. Apply to dig through walls or down through floors (creates pit, then hole). Same `pick-axe` skill as the mattock. |
| dwarvish mattock | 1d12 / 1d8+2d6 | 120 | 50 | −1 | iron | Two-handed (3/2 Str damage bonus). Digs through walls like a pick-axe. Slight to-hit penalty (−1). |

:::

#### Club
<!-- audit 2026-05-17 #6 (re-audit 2026-05-18 v2 #66): 11 cells verified, 1 corrected (aklys "Strength" → tethered when wielded). v2 fixed the club Notes cell: "basic but free of curses early" was wrong — starting inventory uses blessorcurse(otmp, 10) per mkobj.c:876-885, so about a 10% chance the starting club is cursed. Trimmed to "Caveman starter." matching the convention used in the short-sword row. Stats re-verified vs objects.h:371-373 (club) and 381-383 (aklys); aklys return mechanic at dothrow.c:30-34, 1710-1759 confirmed (W_WEP required; ~1% misfire). See companion-audit.md. -->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| club | 1d6 / 1d3 | 30 | 3 | — | wood | Caveman starter. |
| aklys | 1d6 / 1d3 | 15 | 4 | — | iron | Returns when thrown if wielded as your primary weapon (it's tethered); occasional misfire. |

:::

#### Mace
<!-- audit 2026-05-18 v2 #12: stats verified vs include/objects.h:355-361. Two factual fixes. (1) Demonbane row corrected: PHYS(5,0) means +1d5 to-hit and double damage versus demons (artifact.c:1083-1085 spec_abon, 1106-1107 spec_dbon), not "+d5/+0". Demonbane also has a banish invoke. (2) Silver mace row: the silver bonus is +1d20 versus hates_silver targets per uhitm.c:1376-1377 — demons, weres, vampires, shades, and most imps (mondata.c:524-528). "Undead" and "shape-changers" generally are too broad (mummies/zombies/ghosts and chameleons don't qualify). Also notes: Sceptre of Might is a MACE artifact at artilist.h:232-235 (mentioned in the row in an initial v2 edit, reverted as trivia); Mjollnir is a war hammer, correctly excluded. See companion-audit.md. -->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| mace | 1d6+1 / 1d6 | 30 | 5 | — | iron | The Priest's guaranteed first sacrifice gift, Demonbane: a silver mace with +1d5 to-hit and double damage versus demons, plus a banish invoke. |
| silver mace | 1d6+1 / 1d6 | 36 | 60 | — | silver | +1d20 versus demons, weres, vampires, shades, and most imps. |

:::

#### Morning star
<!-- audit 2026-05-18 #148 (re-audit 2026-05-18 v2 #23): clean. Damage 1d4+1d4 / 1d6+1, weight 120, cost 10, hit 0, iron — all match objects.h:363-365 with bonus dice from weapon.c:225-289. P_MORNING_STAR is its own skill class (skills.h:35, id 12), distinct from P_MACE (id 11). v2 corrected the pass-1 claim "No artifact morning star exists" — Trollsbane is a MORNING_STAR artifact at artilist.h:182-184 (regenerates while wielded, +d5 vs trolls). Documented in the Artifacts chapter; the row prose is correct as-is. 0 user-facing corrections. See companion-audit.md. -->


::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| morning star | 1d4+1d4 / 1d6+1 | 120 | 10 | — | iron | +1d4 small, +1 large — punches above its weight for a one-hander. |

:::

#### Flail
<!-- audit 2026-05-17 #70 (re-audit 2026-05-18 v2 #35): flail stats verified vs objects.h:384-386 + weapon.c. Tightened notes to show both +1 small and +1d4 large bonuses. Added grappling hook (P_FLAIL skill, but a WEPTOOL); #apply pulls a target toward you. v2 re-confirmed: flail base 1d6/1d4 + small +1 (weapon.c:272-275) + large +1d4 (weapon.c:239-243); grappling hook 1d2/1d6 trains P_FLAIL despite being a WEPTOOL (objects.h:1010-1012); use_grapple range 4/4/5/8 by skill (apply.c:3686-3698). No artifact form. 0 corrections. See companion-audit.md. -->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| flail | 1d6+1 / 1d4+1d4 | 15 | 4 | — | iron | +1 small, +1d4 large; one-handed. |
| grappling hook | 1d2 / 1d6 | 30 | 50 | — | iron | Tool, not a primary weapon, but trains P_FLAIL. `#apply` to hook and pull a target toward you. |

:::

#### Hammer
<!-- audit 2026-05-17 #45: war hammer stats verified vs objects.h:367-369 + weapon.c. Mjollnir note corrected: "Neutral Valkyrie sacrifice gift" wrongly implied alignment restriction. hack_artifacts at artifact.c:92-95 fixes the artifact's alignment to match player's initalign, so any Valkyrie can receive Mjollnir. Same wording fix applied at line ~242. See companion-audit.md. -->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| war hammer | 1d4+1 / 1d4 | 50 | 5 | — | iron | Mjollnir is the artifact form (Valkyrie sacrifice gift; its alignment will match the player's). |

:::

#### Quarterstaff
<!-- audit 2026-05-17 #19: 7 cells verified, 0 corrected. Matches objects.h:377. See companion-audit.md. -->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| quarterstaff | 1d6 / 1d6 | 40 | 5 | — | wood | Two-handed but light; the Wizard's starting weapon. |

:::

#### Polearms
<!-- audit 2026-05-17 #41: 12 rows / stats verified against objects.h + weapon.c dmgval. Corrected: "reach of two squares" was a class invariant claim (actually skill-dependent in apply.c:3355-3382); "with one empty intervening square" was fabricated (no such check in use_pole); "can't be used in melee against an adjacent monster" was wrong (adjacent attack works as bashing per uhitm.c:1467-1484, just without strength/skill bonus). See companion-audit.md. -->

All polearms are two-handed. To strike at range, `#apply` the weapon (not wield-and-attack): you can hit at distance 2 orthogonally at Basic skill, with extra positions opening up at Skilled. You can still hit an adjacent monster the normal way with a polearm in hand, but the attack is treated as bashing (no strength bonus, no weapon-skill bonus), so reach is what makes them worth carrying. Notes below describe each entry's extra damage; the reach mechanic is identical across the class.

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
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
<!-- audit 2026-05-18 #115: stats verified vs objects.h:174-191. Added context the table omitted: Valkyrie starts with a plain spear at Expert (u_init.c:160-161, 537); kebab bonus is +2 to-hit vs the big monsters (xorns, dragons, jabberwocks, nagas, giants) per weapon.c:71-73, 167-168 is_spear() check. Trident is correctly in its own section since it uses P_TRIDENT, a separate skill class. v2 audit 2026-05-18 #57: corrected a significant factual error. The pass-1 audit attributed the +1 spear multishot to Valkyrie; per dothrow.c:47-52, the bonus actually belongs to PM_CAVE_DWELLER (Caveman), not Valkyrie. Valkyrie has no class-specific spear multishot — she gets only the generic Expert multishot ceiling. Reworded the strategic framing: the Valkyrie still starts with the spear and reaches Expert, but it's the Caveman who can spam thrown javelins. Updated the javelin Notes cell from "Valkyries can ranged-spam them" to "Cavemen can ranged-spam them". See companion-audit.md. -->

All spears share the `P_SPEAR` skill (trident is a different
class — see below). The Valkyrie starts with one and can train to
Expert. The **Caveman** is the actual spear-multishot specialist:
Cavemen get +1 multishot on any thrown spear (regular, silver,
javelin alike), so a stack of javelins is real ranged firepower
for them.

Spears get a **+2 to-hit bonus** when used against the big
monsters — xorns, dragons, jabberwocks, nagas, and giants — the
kebab bonus.

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| spear | 1d6 / 1d8 | 30 | 3 | — | iron | Throwable. Valkyrie's starting weapon. |
| elven spear | 1d7 / 1d8 | 30 | 3 | — | wood |  |
| orcish spear | 1d5 / 1d8 | 30 | 3 | — | iron |  |
| dwarvish spear | 1d8 / 1d8 | 35 | 3 | — | iron |  |
| silver spear | 1d6 / 1d8 | 36 | 40 | — | silver | Silver damage to demons and weres. |
| javelin | 1d6 / 1d6 | 20 | 3 | — | iron | Stackable thrown weapon; Cavemen can ranged-spam them. |

:::

#### Trident
<!-- audit 2026-05-18 #129: stats verified vs objects.h:195. The Note "giant-killer" was misleading — the +1/+2d4 bonus dice are the universal land-creature bonus shared by two-handed sword, battle-axe, bardiche etc. (weapon.c:251-276), not trident-specific. The trident's actual signature is the swimmer-only bonus at weapon.c:170-176: +4 vs is_swimmer(ptr) when in a pool, +2 vs S_EEL or S_SNAKE. Reworded the Notes column accordingly. -->


::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| trident | 1d6+1 / 1d4+2d4 | 25 | 5 | — | iron | One-handed. **+4 damage vs swimmers in water, +2 vs eels and snakes** — the trident's signature bonus. Outside water it's an ordinary side-arm. |

:::

<!-- audit 2026-05-18 #165: stats clean vs objects.h:349 (P_LANCE skill, one-handed, IRON). "Useless on foot" overstated — without a steed it's a regular 1d6/1d8 piercer with no joust bonus, but it still hits and damages normally. Reworded to "no bonus on foot." See companion-audit.md. -->
#### Lance

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| lance | 1d6 / 1d8 | 180 | 10 | — | iron | One-handed, P_LANCE skill. Mounted only: chance to joust for +2d10 primary (+2d2 off-hand) extra damage; a critical can shatter the lance. No bonus on foot. |

:::

<!-- audit 2026-05-18 #162 (re-audit 2026-05-18 v2 #51): stats clean vs objects.h:374-376 (rubber hose) and 390-392 (bullwhip), P_WHIP at skills.h:49. Bullwhip apply-to-disarm at apply.c:3127-3174 and apply-to-yank-from-pit at apply.c:3069-3125 verified. Removed the "Damages even Shades" claim on rubber hose — false; rubber hose is PLASTIC and shade_glare only returns TRUE for SILVER (artifact.c:555-562, weapon.c:307-308). v2 re-confirmed rubber hose prob=0 (never randomly spawns); Archeologist starter bullwhip +1 proficient at apply.c:2992-2993. No whip artifacts. 0 corrections. See companion-audit.md. -->
#### Whip

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| rubber hose | 1d4 / 1d3 | 20 | 3 | — | plastic | Joke weapon; never spawns randomly. |
| bullwhip | 1d2 / 1 | 20 | 4 | — | leather | Archeologist's starter. Apply to disarm an adjacent monster (only when the target is wielding a weapon), or to yank yourself out of a pit (anchors on a nearby boulder, furniture, or big monster). |

:::

<!-- audit 2026-05-18 #157: all 9 rows (arrow/elven/orcish/silver/ya + bow/elven/orcish/yumi) verified clean vs objects.h:141-154, 395-402. Yumi prob=0 (Samurai-only) — note correct. 0 corrections. See companion-audit.md. -->
#### Bow

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
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
<!-- audit 2026-05-18 #118: 2 corrections. (1) Crossbow bolt damage was "1d4+1 / 1d6+1" — wrong; per objects.h:155-156 PROJECTILE macro sdam=4, ldam=6 = 1d4 / 1d6, no +1 bonus. (2) "Crossbows fire one shot per turn at most" — wrong; dothrow.c:225-231 enables multishot at ACURRSTR >= 18 (>= 16 for gnomes), and PM_GNOME gets a baseline +1 multishot bonus per dothrow.c:205-209. Added role/race context (Rogue/Ranger Expert per u_init.c). -->


::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| crossbow bolt | 1d4 / 1d6 | 1 | 2 | — | iron | Stackable. |
| crossbow | — | 50 | 40 | — | wood | Bolts pierce. Multishot kicks in at **Str 18** (Str 16 for gnomes, who also get a baseline +1 multishot); below that, one bolt per turn. Rogues and Rangers reach Expert, Valkyries Skilled. |

:::

#### Sling
<!-- audit 2026-05-18 #90: sling stats verified vs objects.h:403. Corrected "Trains sling skill from any rock you pick up" — wrong. Per weapon.c:1750, ammo alone doesn't train skill (comment explicitly notes touchstone-Archeologist exclusion); training comes from hits while wielding a sling. Caveman starts with one sling. Sling launches rocks, gems, and flint stones. See companion-audit.md. -->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| sling | — | 3 | 20 | — | leather | Trains sling skill from any rock you pick up. |

:::

#### Dart
<!-- audit 2026-05-18 #95: dart stats clean vs objects.h:161. Added "Poisonable; Tourist starts with a stack" note (verified via is_poisonable + u_init.c:151). See companion-audit.md. -->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| dart | 1d3 / 1d2 | 1 | 2 | — | iron | Poisonable. Tourist starts with a stack of ~25–60 at +2. |

:::

#### Shuriken
<!-- audit 2026-05-17 #23 (re-audit 2026-05-18 v2 #55): 5 cells verified, 0 corrected. Matches objects.h:163. v2 re-confirmed: 1d8/1d6, wt 1, cost 5, +2 hit, iron, PIERCE, missile, P_SHURIKEN. is_poisonable per obj.h:264-268. Samurai trains to Expert per u_init.c:481. 0 corrections. See companion-audit.md. -->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| shuriken | 1d8 / 1d6 | 1 | 5 | +2 | iron |  |

:::

#### Boomerang
<!-- audit 2026-05-18 #96: stats clean vs objects.h:166-168. Corrected "Returns when thrown. Always." — false. Per zap.c:boomhit, the boomerang flies a 10-step curved path, stops on monster/wall/door/sink hits, and catching on return requires a DEX check (auto-fails if Fumbling); failed catch hits the thrower. Enchanted boomerangs get multi-hit (spe+1). Useless underwater. See companion-audit.md. -->

::: dense-table

| Weapon | Damage (S/L) | Wt | Cost | Hit | Material | Notes |
|--------------------|--------------|----|------|-----|----------|--------------------------------------------------------------------|
| boomerang | 1d9 / 1d9 | 5 | 20 | — | wood | Returns when thrown. Always. |

:::

---

### Armor Tables
<!-- audit 2026-05-18 #110: seven corrections to the armor tables. (1) "+d4 Int/Wis when blessed and enchanted" for helm of brilliance is wrong; do_wear.c:3328-3334 adj_abon adds the literal enchantment (uarmh->spe) to both Int and Wis — no dice. (2) Same shape for gauntlets of dexterity ("+d3 Dex per enchantment" -> adds spe to Dex). (3) "dunce cap always cursed on generation" is wrong; dunce cap follows the standard mkobj distribution. The cap auto-curses when worn (do_wear.c:475-491). The items actually 9/10-cursed-on-generation are FUMBLE_BOOTS, LEVITATION_BOOTS, HELM_OF_OPPOSITE_ALIGNMENT, GAUNTLETS_OF_FUMBLING (mkobj.c:1086-1090) — flagged in those rows. (4) "mithril coats: no casting penalty" is wrong; MITHRIL is in the is_metallic range (objclass.h:194-196 IRON=11..MITHRIL=17), so spelarmr at spell.c:2191-2193 applies — they're lighter than plate, not penalty-free. (5)-(7) Three duplicated-clause typos: jumping boots ("#apply to leap. #apply to leap."), levitation boots ("cannot be removed while in the air. Can't remove while levitating."), helm of telepathy ("Telepathy. Telepathy while blind."). v2 audit 2026-05-18 #4: 100% spot-check of every AC/MC/Wt/Cost/Material cell against objects.h:445-727; all numbers clean. Three factual fixes: levitation-boots note corrected (Boots_off at do_wear.c:300-310 handles in-air removal — the trap is the 9/10 curse, not the air); blue dragon scale mail and scales corrected from "intrinsic speed (Fast)" to extrinsic Very_fast tier matching speed boots (do_wear.c:817-828 EFast); speed boots "+1 speed" replaced with the actual mechanic (free action on 2/3 of turns). Two wisdom adjustments: dropped misleading "Dwarves drop these" note on chain mail (all iron mails are Mines drops); robe casting bonus reworded from "+1" (which is a magnitude that doesn't exist) to "cancels most of the metal-armor penalty" reflecting spell.c:2192-2195 spelarmr subtraction. Four voice tightenings: intro "alongside any tactical caveats" → "and tactical caveats"; cloak of MR de-duplicated; dunce cap and helm-of-opposite-alignment notes trimmed of meta-language and em-dashes. Follow-ups for later: build_armor_appendix.py may be out of sync with hand-edits; "yellow dragon scale mail | Rare." not verified against 5.0 generation rules. See companion-audit.md. -->

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
| cloak of protection | +3 | 3 | 10 | 50 | cloth | Best non-magical defensive cloak. |
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
| helm of opposite alignment | +1 | — | 50 | 50 | iron | Flips alignment while worn. Generated cursed 9 times in 10. Trap item. |
| helm of telepathy | +1 | — | 50 | 50 | iron | Telepathy while blind. |

:::

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
<!-- audit 2026-05-18 #99 (re-audit 2026-05-18 #182): 43 spells extracted from objects.h SPELL() macros (P_ATTACK..P_MATTER). SPELL macro signature in objects.h:1078 confirms field order (name, desc, sub, prob, delay, level, mgc, dir, color, sn) and oc_level=oc_oc2. Chain lightning level=2 per macro; spoiler body still says L4 in Spellcasting Key Spells table at line 4986 and What's New at line 8585 — flag for follow-up fix. Rank-gated effects from spell.c spelleffects: SPE_FIREBALL/CONE_OF_COLD become aimed explosions at P_SKILLED; SPE_REMOVE_CURSE/CONFUSE_MONSTER/DETECT_FOOD/CAUSE_FEAR/IDENTIFY/CHARM_MONSTER get blessed-scroll behavior at P_SKILLED; SPE_HASTE_SELF/DETECT_TREASURE/DETECT_MONSTERS/LEVITATION/RESTORE_ABILITY get blessed-potion behavior at P_SKILLED; SPE_PROTECTION doubles uspmtime at P_EXPERT (spell.c:1169); SPE_JUMPING distance scales directly from role_skill. Re-audit 2026-05-18 #182 fixed two errors: magic missile is Antimagic-blocked (zap.c:4410-4419, "missiles bounce off!"), not "no resistance"; clairvoyance has a P_SKILLED upgrade at spell.c:1572-1576 (also detects nearby monsters during each pulse). Finger of death note clarified: monster MR resists but the player gets no Antimagic check on the death-ray instakill (zap.c:2885-2902). v2 audit 2026-05-18 #18: four corrections. (a) Dropped flame sphere and freeze sphere rows — both are `#if 0 DEFERRED` in objects.h:1413-1422 with no implementation anywhere in 5.0 src/, so 41 spells, not 43. (b) Charm monster row: Type "untargeted" not "aimed" (read.c:1679-1708 seffect_taming is area-centered-on-caster, no direction prompt); area is 3×3 normal and **11×11** confused (`bd = confused ? 5 : 1`, -bd..bd inclusive), not 5×5; the Skilled+ upgrade is blessed-scroll behavior (more reliable taming), not a radius bump. (c) Cause fear: blessed and uncursed are identical at read.c:1454-1486 — no radius difference — and the loop hits every visible monster on the level, not just "nearby." Dropped "Blessed: wider radius" and reworded Effect. (d) Remove curse blessed branch uncurses every non-coin item in inventory (read.c:1514-1577), not just worn/wielded. See companion-audit.md. -->

The complete spellbook catalog, sorted by school then level. **Lvl**
is the spell level; **Pw cost** is always 5×level. **Type**
distinguishes how the spell targets:

- **aimed** — a single-square IMMEDIATE; you pick a direction.
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
| charm monster   | Enchantment | 5   | untargeted | Tames monsters in a 3×3 area (11×11 if confused) | Blessed-scroll behavior |
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
scales with rank, even when the spell's behavior doesn't otherwise
change.

---

### Skill Caps
<!-- audit 2026-05-18 #100 (re-verified 2026-05-18 #183): all 13 role skill tables extracted from u_init.c (Skill_A through Skill_W) and grouped by skill category. Skills not listed in a role's def_skill array are restricted (P_UNSKILLED, locked). Scimitar omitted because no role has it in 5.0 (merged into saber, per skills.h header note and audit #82). Note "Monks/Samurai only roles with martial arts" verified: P_MARTIAL_ARTS appears only in Skill_Mon (P_GRAND_MASTER) and Skill_S (P_MASTER). Monks have P_BARE_HANDED_COMBAT restricted (—) — they get martial arts instead. Re-audit 2026-05-18 #183: every cell of all three sub-tables (27 weapon rows, 4 fighting-style rows, 7 spell-school rows) × 13 role columns confirmed exact-match against u_init.c:257-572. 0 corrections. -->

Every role has fixed maximum ranks for each weapon, fighting style,
and spell school. Skills not listed for a role are **restricted**
(the rank is locked at Unskilled) — except that a god-given
artifact weapon unrestricts you to Basic in its skill. Key:
**B**=Basic, **S**=Skilled, **E**=Expert, **M**=Master,
**GM**=Grand Master, **—**=restricted.

A "**—**" does *not* mean the skill is unusable — it means the
rank is locked at Unskilled forever, so you always pay the
Unskilled penalty from the rank table (−4/−2 for a weapon, −9/−3
per strike for two-weapon, the Unskilled cast-failure rate for a
spell school) and no rank-gated upgrades ever unlock. A Healer
can still read a spellbook of force bolt and try to cast it; a
Wizard can still swing a long sword; they'll just always do it
clumsily, with no path to improvement. Roles are abbreviated: Arc=Archeologist,
Bar=Barbarian, Cav=Caveman, Hea=Healer, Kni=Knight, Mon=Monk,
Pri=Priest, Rog=Rogue, Ran=Ranger, Sam=Samurai, Tou=Tourist,
Val=Valkyrie, Wiz=Wizard.

#### Weapon Skill Caps

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

#### Fighting Style Caps

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

#### Spell School Caps

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

---

### Bestiary Tables

Every monster you might meet. Grouped by ASCII symbol so you can flip to the right page mid-game. **Lvl** is the base monster level. **Spd** is movement rate (12 is normal player speed). **AC** is armor class (lower is better). **MR%** is the percentage chance the monster resists your spells and magic attacks. **Attacks** lists each attack's mode, damage dice, and side effect; multiple attacks separated by `·` are made per turn. **Notes** folds in the most tactically-relevant trait flags (flies, sees-invis, regenerates, poisonous-corpse, etc.) alongside specific heads-ups for monsters that deserve one.

#### Ants and insects `a`
<!-- audit 2026-05-17 #40: 48 cells / 6 rows verified, 0 corrected. All entries match monsters.h:89-133. See companion-audit.md. -->

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
<!-- audit 2026-05-17 #8: 24 cells across 3 rows verified, 0 corrected. All stats match monsters.h:137-166. See companion-audit.md. -->

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
<!-- audit 2026-05-17 #20: 22 cells verified, 0 corrected. All three rows (chickatrice/cockatrice/pyrolisk) match monsters.h:167-195. See companion-audit.md. -->

Medieval bestiary creature: a chicken with a serpent's tail whose touch turns flesh to stone. Carry a lizard corpse, fight gloved, and never wield a cockatrice corpse as a weapon unless your role explicitly resists stoning. See [Petrification](#petrification-stoning).

All cockatrices are poison-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| chickatrice | brown | 4 | 4 | 8 | 30 | bite 1d2 · touch petrify · passive petrify | ston-res. A small cockatrice. Same petrify rules apply. |
| cockatrice | yellow | 5 | 6 | 6 | 30 | bite 1d3 · touch petrify · passive petrify | ston-res. Touch petrifies. Always carry a lizard corpse. |
| pyrolisk | red | 6 | 6 | 6 | 30 | gaze 2d6 fire · bite 1d6 | fire-res. |

:::

<!-- audit 2026-05-18 #159: 16 rows + intro verified vs monsters.h:199-320. Corrected little-dog starting roles (Archeologist isn't guaranteed; petnum=NON_PM coin-flips cat/dog. Guaranteed roles are Caveman/Ranger/Samurai per role.c:128, 387, 428). Corrected Cerberus row: "Reflection" was unsupported (only MR_FIRE in monsters.h:316); Cerberus is `#ifdef CHARON`-gated and not in the default build. See companion-audit.md. -->
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
| Cerberus | red | 12 | 10 | 2 | 20 | bite 3d6 · bite 3d6 · bite 3d6 | fire-res. Three-headed hellhound. Compiled in only with `CHARON` defined; not in the default build. |

:::

#### Eyes and spheres `e`
<!-- audit 2026-05-17 #57: roster matches monsters.h:325-366 (beholder correctly omitted, #if 0). All stats clean. Corrected floating-eye paralysis trigger: was "in daylight", really requires mutual sight (canseemon + mon->mcansee per uhitm.c:6022-6053). Added the corpse-grants-telepathy note (eat.c:1071 TELEPAT case). See companion-audit.md. -->

The floating eye's passive paralysis gaze is the single most famous newbie killer in the game: never melee one without free action, blindness, or a ranged attack. Once it's dead, eat the corpse: it grants intrinsic telepathy.

All eyes and spheres fly. All except *floating eye* also are mindless.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| gas spore | gray | 1 | 3 | 10 | 0 | death-burst 4d6 |  |
| floating eye | blue | 2 | 1 | 9 | 10 | passive 0d70 paralyse | amphibious. (no mindless) Passive gaze paralyses on melee if you and the eye can both see each other. Use ranged, blind yourself, or close eyes first. Corpse grants telepathy. |
| freezing sphere | white | 6 | 13 | 4 | 0 | explode 4d6 cold | cold-res. |
| flaming sphere | red | 6 | 13 | 4 | 0 | explode 4d6 fire | fire-res. |
| shocking sphere | bright-blue | 6 | 13 | 4 | 0 | explode 4d6 shock | shock-res. |

:::

#### Felines `f`
<!-- audit 2026-05-18 #147 (re-audit 2026-05-18 v2 #40): all stats clean against monsters.h:381-444. Two minor reframings: (1) "Tigers are good early companions if tamed" — tigers are M2_HOSTILE (not M2_DOMESTIC) and difficulty 8, so they're tameable only with charm-monster/scroll-of-taming/magic-flute, not via tripe-feeding, and not really "early." (2) Kittens — only Wizard guarantees a kitten via urole.petnum=PM_KITTEN (role.c:548); Valkyrie/Tourist roll 50/50 kitten-or-dog via dog.c:90-101. Reworded the intro. v2 re-verified all 8 rows against monsters.h:381-444. 0 corrections. See companion-audit.md. -->

Cats. Kittens are common starting pets (Wizards always start with
one; Valkyries and Tourists roll 50/50 between kitten and little
dog). Wild felines (jaguar, lynx, panther, tiger, displacer beast)
are hostile by default; you'd need a charm-monster spell, scroll
of taming, or magic flute to flip them, and the wild rows aren't
really "early-game" creatures.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| kitten | white | 2 | 18 | 6 | 0 | bite 1d6 | tameable. Common Valkyrie/Wizard/Tourist starting pet. |
| housecat | white | 4 | 16 | 5 | 0 | bite 1d6 | tameable. |
| jaguar | brown | 4 | 15 | 6 | 0 | claw 1d4 · claw 1d4 · bite 1d8 |  |
| lynx | cyan | 5 | 15 | 6 | 0 | claw 1d4 · claw 1d4 · bite 1d10 |  |
| panther | black | 5 | 15 | 6 | 0 | claw 1d6 · claw 1d6 · bite 1d10 |  |
| large cat | white | 6 | 15 | 4 | 0 | bite 2d4 | tameable. |
| tiger | yellow | 6 | 12 | 6 | 0 | claw 2d4 · claw 2d4 · bite 1d10 |  |
| displacer beast | blue | 12 | 12 | -10 | 0 | claw 4d4 · claw 4d4 · bite 2d10 |  |

:::

#### Gremlins `g`
<!-- audit 2026-05-18 #152: headnote conflated two distinct mechanics. Water/fountain triggers gremlin SPLIT (mon.c:987-992, 2/3 chance per step) — clones themselves, doesn't touch your intrinsics. Night triggers AD_CURS (uhitm.c:3040-3057, sit.c:644+ attrcurse) which strips ONE random intrinsic (1/10 chance per hit, only at night, only if not cancelled). Reworded to keep them separate. -->

At night, their touch strips a random intrinsic (fire resistance, telepathy, etc.). In water or fountains they split into more gremlins. Kill them on dry land, ideally during daylight.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| gremlin | green | 5 | 12 | 2 | 25 | claw 1d6 · claw 1d6 · bite 1d4 · claw curse | swims, poisonous-corpse, follows stairs, pois-res. |
| gargoyle | brown | 6 | 10 | -4 | 0 | claw 2d6 · claw 2d6 · bite 2d4 | ston-res. |
| winged gargoyle | magenta | 9 | 15 | -2 | 0 | claw 3d6 · claw 3d6 · bite 3d4 | flies, ston-res. |

:::

#### Humanoids `h`
<!-- audit 2026-05-17 #27: 50+ cells verified, 2 corrected (mind flayer "alignment-matching helmet" → any helmet; "telepathy + free action" defenses → any helmet; both per uhitm.c:3235). See companion-audit.md. -->

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

<!-- audit 2026-05-18 #171: all 6 rows verified clean vs monsters.h:544-587. Corrected imp prose: imps only carry AT_CLAW/AD_PHYS 1d4 (monsters.h:561-562) — no AD_SITM, no AD_TLPT. Steal-and-teleport belongs to nymphs (AD_SITM) and leprechauns (AD_SGLD). Imps actually MS_CUSS (verbal abuse, monmove.c:983-985 / sounds.c:1148-1150). Note: the `i` class is not actually M2_DEMON-tagged (is_demon() returns false). All 6 carry M2_STALK. v2 audit 2026-05-18 #22: two factual fixes. (a) manes and lemure both carry G_NOCORPSE (monsters.h:545,567), so their "poisonous-corpse" tags were dormant — replaced with "No corpse." (b) lemure carries G_HELL (monsters.h:567), so it only generates in Gehennom; added "Gehennom-only" tag matching the spoiler's disenchanter-row convention. See companion-audit.md. -->
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
<!-- audit 2026-05-18 #91 (re-audit 2026-05-18 v2 #47): 3 rows verified clean vs monsters.h:591-620. Added corpse-intrinsic notes per eat.c mconveys: blue jelly = cold + poison resistance, spotted/ochre = temporary acid + stone resistance. 0d6 passive still inflicts the AD_COLD/AD_ACID side effect (item damage on acid), but damage on the dice is literal. v2 re-confirmed: blue jelly LVL(4,0,8,10), spotted LVL(5,0,8,10), ochre LVL(6,3,8,20); all three carry M1_AMORPHOUS|M1_MINDLESS. Blue's MR_COLD|MR_POISON conveys permanently via should_givit (eat.c:983-988); spotted/ochre's MR_ACID|MR_STONE convey TIMED via temp_givit (eat.c:991-997). 0 corrections. See companion-audit.md. -->

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
<!-- audit 2026-05-18 #143 (re-audit 2026-05-18 v2 #39): clean. All four stat rows match monsters.h:624-656. Kobold/large-kobold/kobold-lord/kobold-shaman all carry M1_POIS (poisonous corpse) and MR_POISON (poison resistance). Shaman uses AT_MAGC/AD_SPEL via mcastu.c. v2 fixed the shaman attack notation: kobold shaman has only one AT_MAGC/AD_SPEL attack (monsters.h:651), so "spell spell" implied two attacks; changed to "cast spell" matching the AT_MAGC convention used elsewhere (already in golden naga row after v2 #25). Same notation bug also fixed in the gnomish wizard row at line 8569. See companion-audit.md. -->


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
<!-- audit 2026-05-18 #133: clean. Stats (Lvl 5, Spd 15, AC 8, MR 20, green, claw 1d2 AD_SGLD), M1_TPORT, AT_CLAW (not bite) all verified against monsters.h:660-666 and steal.c:58-115. Stolen gold is added to mtmp->minvent and drops on death. -->


Steals gold and teleports away. The fix is to carry no gold near them, or to kill from range. The corpse drops the gold back.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| leprechaun | green | 5 | 15 | 8 | 20 | claw 1d2 steal-gold | teleports. Steals gold and teleports away. Carry no gold near them. |

:::

#### Mimics `m`
<!-- audit 2026-05-18 #76: 3 rows (small/large/giant) verified clean against monsters.h:670-698. All stats, M1_AMORPHOUS|M1_HIDE|MR_ACID flags, AD_STCK on large/giant, M2_STRONG on large+giant verified. set_mimic_sym disguise mechanics (makemon.c:2393-2472) including STRANGE_OBJECT in shops at sufficient depth. 0 corrections. See companion-audit.md. -->

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
<!-- audit 2026-05-18 #131 (re-audit 2026-05-18 v2 #67): clean. All three nymph stats (wood/water/mountain — LVL 3, Spd 12, AC 9, MR 20%, AT_CLAW AD_SITM + AT_CLAW AD_SEDU, M1_TPORT) match monsters.h:702-723. Water nymph has M1_SWIM (line 714). Corpse grants intrinsic teleportitis with 10% chance per should_givit (eat.c:936-975). v2 re-verified: AD_SITM steal-and-teleport at uhitm.c:4724,4798; AD_SEDU at uhitm.c:4642; all three carry M1_TPORT|MR_POISON. 0 corrections. See companion-audit.md. -->


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
<!-- audit 2026-05-18 #89: 8 rows verified clean against monsters.h:727-796 (covers all of S_ORC). Stats, colors (incl. HI_LORD/HI_ZAP), attacks, MR_POISON flags all match. Corrected: orc shaman row was "spell spell" (2 attacks) but C gives only one ATTK(AT_MAGC,AD_SPEL); now "spell". Goblin is correctly placed in S_ORC. See companion-audit.md. -->

Pack hunters with mediocre loot but real numbers. The Mines are full of them; bring a chokepoint.

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

<!-- audit 2026-05-18 #168 (re-audit 2026-05-18 v2 #30): 3 rows (rock/iron/glass) verified clean vs monsters.h:800-826. All carry M1_HIDE | M1_CLING so qualify as ceiling-hiders (mondata.h:43-45); hiding gated by has_ceiling (mon.c:4672). Drop-on-walk-under is d(4,6) for ALL species regardless of bite die (hack.c:3436). Glass piercer has MR_ACID. v2 re-confirmed every cell against monsters.h:800-826. 0 corrections. See companion-audit.md. -->
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
<!-- audit 2026-05-17 #58: 7 rows × 8 cells verified against monsters.h:831-885. All stats clean. Added "clings" note to wumpus (M1_CLING). v2 audit 2026-05-18 #3: re-verified all 56 cells against monsters.h:831-885 (rothe through mastodon); 0 factual corrections. Tightened the Mumakil line to mention damage and thick hide explicitly. See companion-audit.md. -->


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
<!-- audit 2026-05-17 #44: 48 cells / 6 rows verified against monsters.h:889-936. 1 corrected (woodchuck color was —, should be brown per CLR_BROWN at L936). See companion-audit.md. -->

Mostly nuisance fodder. Giant rats are common in the early dungeon; their corpses are safe food.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| sewer rat | brown | 0 | 12 | 7 | 0 | bite 1d3 |  |
| giant rat | brown | 1 | 10 | 7 | 0 | bite 1d3 |  |
| rabid rat | brown | 2 | 12 | 6 | 0 | bite 2d4 drain-Co | poisonous-corpse, pois-res. |
| wererat | brown | 2 | 12 | 6 | 10 | bite 1d4 lyc | regenerates, poisonous-corpse, pois-res. |
| rock mole | gray | 3 | 3 | 0 | 20 | bite 1d6 | tunnels. |
| woodchuck | brown | 3 | 3 | 0 | 20 | bite 1d6 | swims, tunnels. |

:::

#### Arachnids and centipedes `s`
<!-- audit 2026-05-17 #25: 30+ cells verified, 0 corrected. All 5 entries (cave spider, centipede, giant spider, scorpion, Scorpius) match monsters.h. See companion-audit.md. -->

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

Stationary engulfers that look like a piece of dungeon. Stepping into one starts a swallow attack you can't easily escape. Identify with `;` (farlook) before walking into obvious-trap squares.

All trappers and lurkers hide and follow you up and down stairs.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| lurker above | gray | 10 | 3 | 3 | 0 | engulf 1d6 wrap · engulf 2d6 | flies. |
| trapper | green | 12 | 3 | 3 | 0 | engulf 1d8 wrap · engulf 2d8 |  |

:::

<!-- audit 2026-05-18 #178: all 6 rows (pony/white/gray/black unicorn/horse/warhorse) verified clean vs monsters.h:1002-1049. Unicorn alignments lawful/+7, neutral/0, chaotic/-7 (monsters.h:1011,1019,1027). Same-aligned spawn peaceful (makemon.c:1339-1342); killing co-aligned = -5 Luck (mon.c:3666-3669). Gem-throw at unicorn: dothrow.c:2082-2098, 2309-2382 (worthless glass placates without Luck change). Knight's pony arrives saddled (dog.c:263-267). 0 corrections. See companion-audit.md. -->
#### Unicorns and horses `u`

There are two equine `u`-class creatures. **Horses** (pony, horse, warhorse) are usually peaceful in the wild and can be saddled and ridden; the Knight starts on a saddled pony.

**Unicorns** (white, gray, black for Lawful, Neutral, Chaotic) are powerful kickers, peaceful when your alignment matches theirs and hostile otherwise. Killing a co-aligned unicorn is a −5 Luck penalty (the game tells you "You feel guilty..."). Killing a cross-aligned one has no Luck consequence either way. If you don't want the fight, throw any gem — even worthless glass — to pacify a hostile unicorn at no cost; throwing real gems also adjusts your Luck (see the Luck chapter). A killed unicorn drops its horn.

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
<!-- audit 2026-05-17 #56 (re-audit 2026-05-18 v2 #31): 6 rows × 8 cells verified against monsters.h:1053-1110. Corrected intro damage-type list (no vortex deals poison; types are physical/blinding/cold/shock+drain/fire). Corrected "stationary" framing (only fog cloud is slow; others are speed 20-22). v2 re-verified all six rows against monsters.h:1053-1110: fog cloud Lvl 3/Spd 1, dust/ice/energy Spd 20, steam/fire Spd 22; energy vortex's AT_NONE+AD_ELEC passive 0d4 and AD_DREN drain confirmed at monsters.h:1081-1090; fire vortex's AT_NONE+AD_FIRE passive 0d4 at monsters.h:1101-1110. All carry M1_FLY|M1_MINDLESS|G_NOCORPSE. 0 corrections. See companion-audit.md. -->

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
<!-- audit 2026-05-18 #84: 4 rows × 8 cells verified against monsters.h:1114-1145. Long worm tail mechanic in worm.c, purple worm AT_ENGL/AD_DGST swallow in mhitu.c. Added "drops worm tooth" note to long worm (mon.c:619). 0 corrections beyond that. See companion-audit.md. -->

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
<!-- audit 2026-05-17 #16 (re-audit 2026-05-18 v2 #64): 9 cells/claims verified, 0 corrected. All grid bug and xan stats match monsters.h. v2 fixed the intro: "sting your legs and slow you down" was wrong — AD_LEGS / Wounded_legs reduces carry capacity (hack.c:4331-4336) and abuses Dex (attrib.c:472, 581) but does NOT reduce movement speed. Reworded to "sting your legs and cut your carrying capacity." Stats re-verified vs monsters.h:1149-1164. See companion-audit.md. -->

Grid bugs are trivial; xans, the bigger relatives, sting your legs and cut your carrying capacity.

All xans and fantastic insects are poison-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| grid bug | magenta | 0 | 12 | 9 | 0 | bite 1d1 shock | shock-res. |
| xan | red | 7 | 18 | -4 | 0 | sting 1d4 leg-wound | flies, poisonous-corpse. |

:::

#### Lights `y`
<!-- audit 2026-05-18 #80: 2 rows (yellow light lvl 3 yellow + black light lvl 5 black) verified vs monsters.h:1168-1191. Attacks AT_EXPL/AD_BLND 10d20 and AT_EXPL/AD_HALU 10d12. M1_FLY|M1_AMORPHOUS|M1_MINDLESS on both, M1_SEE_INVIS adds for black. Corrected prose "(10d20 damage if unresistant)" — it's blindness DURATION not HP damage. See companion-audit.md. -->

Yellow light bursts on contact and blinds you for 10d20 turns. Black light bursts and hallucinates you for 10d12 turns. See [Light Bursts](#light-bursts).

All lights fly and are amorphous and mindless.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| yellow light | yellow | 3 | 15 | 0 | 0 | explode 10d20 blind |  |
| black light | black | 5 | 15 | 0 | 0 | explode 10d12 hallu | sees-invis. |

:::

<!-- audit 2026-05-18 #155: zruty row verified clean vs monsters.h:1192-1202. LVL(9,8,3,0,0), CLR_BROWN, claw 3d4 · claw 3d4 · bite 3d6 all match. 0 corrections. See companion-audit.md. -->
#### Zruties `z`

Slavic folklore — a hairy wild man of the woods. One species, one role here: a nasty mid-game brute. Good XP if you can handle the three-attack flurry.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| zruty | brown | 9 | 8 | 3 | 0 | claw 3d4 · claw 3d4 · bite 3d6 |  |

:::

#### Angelic beings `A`
<!-- audit 2026-05-18 #97: 5 rows (couatl/Aleax/Angel/ki-rin/Archon) verified clean vs monsters.h:1206-1265. All stats, colors, attacks, M1_FLY/M1_SEE_INVIS/M2_STALK flags match. Corrected couatl "poisonous-corpse" — all Angels have G_NOCORPSE; the couatl leaves no corpse at all (MR_POISON still matters for combat interactions). See companion-audit.md. -->

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

<!-- audit 2026-05-18 #156 (re-audit 2026-05-18 v2 #37): vampire bat — "lycanthropy" claim was wrong (AD_WERE is were-creatures, not bats); the 2nd bite is AD_DRST (Str-drain, poison-flavored). Roster + flags otherwise match monsters.h:1269-1297. v2: replaced "on the second bite" framing — both AT_BITE slots roll independently each turn (uhitm.c:3149-3157, !rn2(8)), not sequentially. Also confirmed all four rows match monsters.h:1269-1297. Erratic-fly behavior from S_BAT class branch at monmove.c:1870-1871. 0 other corrections. See companion-audit.md. -->
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
<!-- audit 2026-05-17 #49: all 3 rows (plains/forest/mountain) match monsters.h:1301-1323 exactly. Roster complete for S_CENTAUR. 0 corrections. See companion-audit.md. -->

Mounted archers with strong physical attacks. They wield bows and shoot at range.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| plains centaur | brown | 4 | 18 | 4 | 0 | weapon 1d6 · kick 1d6 |  |
| forest centaur | green | 5 | 18 | 3 | 10 | weapon 1d8 · kick 1d6 |  |
| mountain centaur | cyan | 6 | 20 | 2 | 10 | weapon 1d10 · kick 1d6 · kick 1d6 |  |

:::

#### Dragons `D`
<!-- audit 2026-05-17 #54: 10 baby + 10 adult + Chromatic + Ixoth all verified against monsters.h:1325-1562 + 3642-3690 (shimmering correctly omitted, #if 0 DEFERRED). All breath types/damage and adult attack lines clean. Corrected silver dragon color (was "gray", actually CLR_BRIGHT_CYAN per color.h:54; fixed both baby and adult rows). See companion-audit.md. -->


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
| baby blue dragon | blue | 12 | 9 | 2 | 10 | bite 2d6 | Lightning breath, ditto. |
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
<!-- audit 2026-05-17 #14 (re-audit 2026-05-18 v2 #61): 32 cells/claims verified, 0 corrected. All stats match monsters.h. Close call: fire/air rows could enrich Notes with their resistances (MR_FIRE etc.) like earth/water rows do. v2 re-confirmed every row vs monsters.h:1566-1610: stalker (no mindless, sees-invis, M2_STALK), air (AT_ENGL AD_PHYS 1d10), fire (claw 3d6 AD_FIRE + passive 0d4 fire), earth (claw 4d6 + MR_FIRE|MR_COLD|MR_POISON|MR_STONE), water (claw 5d6 + M1_SWIM|M1_AMPHIBIOUS + MR_POISON|MR_STONE). "Water drowns if you're adjacent in water" is defensible flavor — water elementals don't have a drown attack themselves, but spawning only on water tiles means encountering one already places you near the standard water-tile drowning risk. "Air suffocates" is engulf-flavor for AT_ENGL AD_PHYS, not a mechanical AD_DRST. 0 corrections. See companion-audit.md. -->

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
<!-- audit 2026-05-17 #35: 49 cells / 7 rows verified, 0 corrected. Lead-in reworded (violet/yellow molds → brown/green/red elemental molds). See companion-audit.md. -->

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
<!-- audit 2026-05-17 #22: 22 cells verified, 0 corrected. All four S_GNOME entries match monsters.h. No "deep gnome" exists in 5.0 (correctly omitted). v2 audit 2026-05-18 #39 (drive-by): gnomish wizard row had the same "spell spell" two-attacks-implied bug as kobold shaman — gnomish wizard has only one AT_MAGC/AD_SPEL at monsters.h:1697. Changed to "cast spell". -->

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
<!-- audit 2026-05-18 #101: section intro and minotaur note corrected. (1) Eating-a-giant-raises-Strength is gated on is_giant(ptr) (M2_GIANT) at eat.c:1345; ettin (no M2_GIANT) and minotaur (no M2_GIANT) corpses do NOT confer Strength. The C even comments at eat.c:1758: "ettin is a two-headed giant but its corpse doesn't confer strength." (2) Minotaur "usually guards a vault" is wrong; minotaurs are placed in Gehennom mazes by mkmaze.c:1102-1113 populate_maze(). Vaults are guarded by PM_GUARD, not minotaurs. All stat values match monsters.h 1714-1793. See companion-audit.md. -->

Boulder throwers. Storm / fire / frost giants match the dragon elements; titans cast spells. Eating a true giant's corpse raises Strength; the ettin and minotaur don't count as giants for this purpose.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| giant | red | 6 | 6 | 0 | 0 | weapon 2d10 |  |
| stone giant | gray | 6 | 6 | 0 | 0 | weapon 2d10 |  |
| hill giant | cyan | 8 | 10 | 6 | 0 | weapon 2d8 |  |
| fire giant | yellow | 9 | 12 | 4 | 5 | weapon 2d10 | fire-res. Throws boulders. Surprisingly poor offensively if you have fire res. |
| frost giant | white | 10 | 12 | 3 | 10 | weapon 2d12 | cold-res. Throws boulders. Has cold attacks. |
| ettin | brown | 10 | 12 | 3 | 0 | weapon 2d8 · weapon 3d6 |  |
| storm giant | blue | 16 | 12 | 3 | 10 | weapon 2d12 | shock-res. Throws boulders for big damage. Carries shock attacks. |
| titan | magenta | 16 | 18 | -3 | 70 | weapon 2d8 · spell spell | flies. Tough humanoid with magic missiles. Casts spells. |
| minotaur | brown | 15 | 15 | 6 | 0 | claw 3d10 · claw 3d10 · butt 2d8 | Two claws plus a butt. Heavy hitter; roams the Gehennom mazes. |
| Cyclops | gray | 18 | 12 | 0 | 0 | weapon 4d8 · weapon 4d8 · claw 2d6 steal-amulet | follows stairs, ston-res. Caveman quest nemesis. Throws boulders. |
| Lord Surtur | magenta | 15 | 12 | 2 | 50 | weapon 2d10 · weapon 2d10 · claw 2d6 steal-amulet | follows stairs, fire-res, ston-res. Valkyrie quest nemesis. Has Mjollnir if you don't. |

:::

#### Jabberwocks `J`
<!-- audit 2026-05-17 #55 (re-audit 2026-05-18 v2 #27): single jabberwock entry verified against monsters.h LVL(15,12,-2,50,0) + 4× 2d10 attacks + M1_FLY + G_GENO|1. Vorpal Blade auto-behead vs PM_JABBERWOCK confirmed at artifact.c:1595-1623 (short-circuits the dieroll==1 check). Corrected "slow" framing (twice): speed 12 is player baseline; most dragons are speed 9 which is actually slower. v2 re-confirmed every cell against monsters.h:1806-1814. The deferred "vorpal jabberwock" entry at monsters.h:1816-1824 is wrapped in `#if 0 /* DEFERRED */` and correctly excluded. 0 corrections. See companion-audit.md. -->

The monster from Lewis Carroll's *Jabberwocky* ("O frabjous day! Callooh! Callay!"). Tough, hits hard, and moves at player baseline speed: you can't simply walk away. Free XP if you're set up for the fight; lethal if you walk into one early. Vorpal Blade was made for beheading it.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| jabberwock | orange | 15 | 12 | -2 | 50 | bite 2d10 · bite 2d10 · claw 2d10 · claw 2d10 | flies. Powerful; baseline speed. Free XP if you're set up. |

:::

#### Keystone Kops `K`
<!-- audit 2026-05-18 #114: stats all match monsters.h:1829-1860; shopkeeper-anger trigger confirmed at shk.c:623, 680 + makekops at shk.c:5113. Added the respawn note: dead Kops respawn per mon.c:3147-3164 (rnd(5): 1-in-5 returns near up-stairs, 2-in-5 returns at random location, 2-in-5 stays dead). All four are G_GENO so genocide does work to clear them permanently. -->

Police force triggered by stealing from shops or hurting shopkeepers. Mostly weak individually but they swarm — and dead Kops respawn: each fallen Kop has a 1-in-5 chance to come back near the up-stairs and a 2-in-5 chance to come back at a random location, so killing them isn't a stable solution. Get away or genocide them instead.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| Keystone Kop | blue | 1 | 6 | 10 | 10 | weapon 1d4 |  |
| Kop Sergeant | blue | 2 | 8 | 10 | 10 | weapon 1d6 |  |
| Kop Lieutenant | cyan | 3 | 10 | 10 | 20 | weapon 1d8 |  |
| Kop Kaptain | magenta | 4 | 12 | 10 | 20 | weapon 2d6 |  |

:::

#### Liches `L`
<!-- audit 2026-05-17 #4: 12 claims verified, 3 corrected (no corpse not poisonous; double-trouble is Wizard-of-Yendor only; arch-lich casts touch of death not rays). See companion-audit.md. -->

Skeletal spellcasters. The higher tiers can cast touch of death; master and arch-liches require magic resistance to survive their spell barrages.

All liches regenerate, leave no corpse, and are undead, cold-resistant, sleep-resistant, and poison-resistant.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| lich | brown | 11 | 6 | 0 | 30 | touch 1d10 cold · spell spell |  |
| demilich | red | 14 | 9 | -2 | 60 | touch 3d4 cold · spell spell |  |
| master lich | magenta | 17 | 9 | -4 | 90 | touch 3d6 cold · spell spell | fire-res. Draws from the wizard spell list. Disperse or kill from afar. |
| arch-lich | magenta | 25 | 9 | -6 | 90 | touch 5d6 cold · spell spell | fire-res, shock-res. End-game tier. Casts touch of death; magic resistance mandatory. |

:::

#### Mummies `M`
<!-- audit 2026-05-18 #149: corrected the "touch curses your worn items" advice — every mummy's attack in monsters.h:1901-1968 is plain AD_PHYS; only gremlins have AD_CURS (monattk.h:92). No special curse logic for S_MUMMY in mhitu.c/uhitm.c/mhitm.c. The note was residue from the prior "mummy withering" myth that audit #46 was supposed to scrub. Reworded to factual physical-only + undead-turning vulnerability. v2 audit 2026-05-18 #41: dropped "All mummies have poisonous corpses" — every M-class row carries G_NOCORPSE (monsters.h:1902,1910,1918,1927,1936,1944,1953,1961), so mummies never leave any corpse. Reworded the intro to "leave no corpse." Same shape as the Vampires fix in v2 #8. See companion-audit.md. -->

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

<!-- audit 2026-05-18 #173: all 8 rows verified clean vs monsters.h:1972-2048. All carry MR_POISON. Removed false claim "Healers find the guardian naga peaceful" — guardian naga is MS_MUMBLE (not MS_GUARDIAN), no M2_PEACEFUL, and PM_GUARDIAN_NAGA's appearance in the Rogue's role.c:338 entry is as a Rogue-quest creature slot, not a Healer/Rogue peace mechanism. peace_minded (makemon.c:2270-2285) finds no path that auto-peaces it. Black naga corpse confers poison + acid + stoning resistance — worth eating but companion doesn't currently surface this. v2 audit 2026-05-18 #25: pass-1 thought it had removed the wrong Healer-peaceful note, but the table still carried "Friendly to the Healer. Hostile otherwise." in the guardian-naga row. Replaced with "Lawful PCs may find them peaceful" — guardian naga maligntyp = +7 (lawful) per monsters.h:2040, so peace_minded matches via sgn(mal)==sgn(ual) for lawful heroes. Other fixes: dropped the wrong "breath weapons (acid / fire / poison)" enumeration in the intro — only red naga actually breathes (AT_BREA fire); black/guardian spit (AT_SPIT); golden casts spells (AT_MAGC AD_SPEL) — narrowed to "with ranged attacks." Fixed "spell 4d6 spell" duplication to "cast spell 4d6" matching AT_MAGC notation elsewhere. Dropped duplicate "All nagas are poison-resistant" sentence-paragraph. See companion-audit.md. -->
#### Nagas `N`

Long serpentine bodies with ranged attacks. All nagas are poison-resistant. Black naga corpses confer poison, acid, *and* stoning resistance — easily the best of the four eats.

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
<!-- audit 2026-05-18 #85: 3 rows (ogre/lord/king) verified clean against monsters.h:2052-2075. All stats, colors, attack dice match. Corrected "Ogre kings throw boulders" — ogres lack M2_ROCKTHROW (that's giants/Cyclops/ettins/titans). Ogres wield weapons (AT_WEAP), they don't throw rocks. See companion-audit.md. -->

Big melee brutes that wield weapons. Drop decent weapons and armor.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| ogre | brown | 5 | 10 | 5 | 0 | weapon 2d5 |  |
| ogre lord | red | 7 | 12 | 3 | 30 | weapon 2d6 |  |
| ogre king | magenta | 9 | 14 | 4 | 60 | weapon 3d5 |  |

:::

#### Puddings and oozes `P`
<!-- audit 2026-05-18 #126: 2 corrections. (1) Green slime "9-turn countdown" — wrong; make_slimed(10L,...) sets 10 turns at uhitm.c:3199, uhitm.c:3570, polyself.c:456, eat.c:854. The only 5-turn case is engulf+digest at uhitm.c:5099. (2) "Brown puddings corrode armor on touch" — wrong; AD_DCAY is ROT (ERODE_ROT for wood/leather/cloth/bone) per uhitm.c:2389 mhitm_ad_dcay. CORRODE (metal) is the black pudding effect (AD_CORR, uhitm.c:2338-2356). Also added the omitted gray-ooze rust effect (AD_RUST), and clarified that the split trigger requires iron/metal melee weapons (hmon_hitmon_splitmon, uhitm.c:1609-1621). -->


Splits when you hit them with an iron or metal melee weapon. Brown puddings **rot** your wood/leather/cloth/bone armor on bite; black puddings **corrode** your metal armor on bite *and* corrode your wielded metal weapon on the passive return-hit. Gray ooze **rusts** metal armor. Fire-kill them so they don't split, or pick a chokepoint.

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
<!-- audit 2026-05-17 #69: stats verified vs monsters.h:2127, 2136. Quantum mechanic = AD_TLPT (teleports you), genetic engineer = AD_POLY (polymorphs you, new in 5.0 per fixes5-0-0.txt:2696). Corrected "All quantum mechanics teleport" — only the quantum mechanic does; genetic engineer polymorphs. Both have poisonous corpses (M1_POIS). Both self-teleport (M1_TPORT). Added corpse-effect notes (quantum corpse toggles Fast per eat.c:1227; genetic engineer corpse triggers polyself per eat.c:1247). See companion-audit.md. -->

The `Q` class is two creatures, both with random claw effects. The
**quantum mechanic** teleports you on a hit: the annoyance is the
lost position more than the damage, but in dangerous neighbourhoods
a random teleport CAN kill. The **genetic engineer** polymorphs
you: unless you have *Unchanging* or magic resistance, one claw and
you become something else. See **Dangerous Encounters → The Genetic
Engineer** for the full treatment.

Both species also teleport themselves at random, and both leave
poisonous corpses.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| quantum mechanic | cyan | 7 | 12 | 3 | 10 | claw 1d4 teleport | Self-teleports. Corpse toggles intrinsic Fast. |
| genetic engineer | green | 12 | 12 | 3 | 10 | claw 1d4 polymorph | Self-teleports. Corpse triggers polyself. |

:::

#### Rust monsters and disenchanters `R`
<!-- audit 2026-05-17 #60: 2 rows verified against monsters.h:2147-2161. Rust active erodes worn iron armor (uhitm.c:2311 erode_armor), passive on weapon when you hit it; greased weapons consume a charge instead. Silver/mithril/wood weapons immune (is_rustprone). Disenchanter active claw drains armor first (uhitm.c:3611-3644 some_armor + 5-way rn2(5) for rings/amulet/blindfold); weapon drain is passive-only. Corrected "long sword" prose to match (active threat is armor, not weapon). See companion-audit.md. -->

Rust monsters rust iron equipment on touch. Disenchanters drain enchantment from your armor when they hit you, and drain enchantment from your weapon when you hit them (passive counterattack). Either way, strip irreplaceable kit before engaging, and switch to silver or non-iron weapons against the rust monster.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| rust monster | brown | 5 | 18 | 2 | 0 | touch rust · touch rust · passive rust | swims. Touch rusts iron. Strip armor before engaging or use silver. |
| disenchanter | blue | 12 | 12 | -10 | 0 | claw 4d4 disenchant · passive disenchant | Gehennom-only. Active drains armor; passive drains weapon when you melee it. |

:::

#### Snakes `S`
<!-- audit 2026-05-17 #51: all 6 rows verified against monsters.h:2167-2221 (garter snake, snake, water moccasin, python, pit viper, cobra). Corrected "pit fiend" typo (pit fiend is `&` demon, not a snake). AD_DRST shorthand as "poison" left as-is per common convention. See companion-audit.md. -->

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
<!-- audit 2026-05-17 #3 (re-audit 2026-05-18 v2 #65): 17 stat claims verified. Self-audit caught the rewrite's "fire/water/force-bolt destroy corpses" claim was wrong (burn_floor_objects only burns scrolls/spellbooks/slime; no general corpse-destruction by these means). Trimmed to verified options only. v2 re-confirmed all five rows vs monsters.h:2225-2266 (troll/ice/rock/water/Olog-hai). All carry M1_REGEN | M2_STALK; S_TROLL is is_reviver per mondata.h:170. Trollsbane sets mkcorpstat_norevive at uhitm.c:1906,4867 + mhitm.c:1082. Stoning leaves a statue (mon.c:671), so no corpse to revive from. 0 corrections. See companion-audit.md. -->

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

<!-- audit 2026-05-18 #166: row stats and M1_TUNNEL verified vs monsters.h:2267-2277. Removed wrong "free action" defense — Free_action is checked only against paralysis, holding, and sleep (mhitu.c grep); AD_CONF at mhitu.c:1759-1777 makes no Free_action check. Blindness still works (gaze gated by mcanseeu at mhitu.c:1681-1682). See companion-audit.md. -->
#### Umber hulks `U`

Confusion gaze. Don't melee without some way to dodge the gaze — blindness defeats it (the gaze requires mutual sight); free action does *not* (it covers paralysis, holding, and sleep, never confusion). The confusion stacks and makes spellcasting impossible.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| umber hulk | brown | 9 | 6 | 2 | 25 | claw 3d4 · claw 3d4 · bite 2d5 · gaze confuse | tunnels. Confusion gaze. Hard to navigate around. Hits hard too. |

:::

#### Vampires `V`
<!-- audit 2026-05-17 #9: 25 cells/claims verified, 0 corrected. All stats match monsters.h; vampire mage is #if 0 DEFERRED in 5.0, correctly omitted. Close call: vampire lord/Vlad can also shapeshift to wolf, not just bat/fog. v2 audit 2026-05-18 #8: one factual fix. "Have poisonous corpses" was wrong: all three rows carry G_NOCORPSE (monsters.h:2282,2292,2314 + monflag.h:201), so vampires leave no corpse at all. Dropped. The wolf-form addition (PM_VAMPIRE_LEADER and Vlad shift to wolf per mon.c:4956-4967) was added in an initial v2 edit and reverted as trivia — the bat/cloud gloss is sufficient at this section's level. Voice: Vlad lead-in reworded to use the proper "Vlad's Tower" rather than "his Tower". See companion-audit.md. -->

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
<!-- audit 2026-05-17 #13: 24 claims/cells verified, 0 corrected. All stats match monsters.h. Close call: wraith row could enrich Notes with stone-res + unsolid. See companion-audit.md. -->

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
<!-- audit 2026-05-18 #75: stats clean against monsters.h:2357-2366. Corrected two prose errors: (1) xorns DON'T tunnel — M1_WALLWALK phases through walls without leaving rubble, NOT M1_TUNNEL. (2) Player's worn weapons/armor are NOT at risk: xorn attacks are AD_PHYS only; metallivore behavior in monmove.c:1664 only eats metal off the floor. Eating xorn corpse grants temporary stone resistance. See companion-audit.md. -->

D&D's three-armed, three-eyed creatures from the Elemental Plane of Earth. They **phase through walls** (no rubble, no dig) and **eat metal items off the floor** — including the orcish dagger you were about to pick up. Their claws and bite are physical only, so worn armor and wielded weapons aren't directly at risk, but they hit hard for their level. The corpse grants temporary stoning resistance.

::: dense-table

| Name | Color | Lvl | Spd | AC | MR% | Attacks | Notes |
|----------------|-------|-----|-----|----|-----|--------------------------------------------|--------------------------------------------------------|
| xorn | brown | 8 | 9 | -2 | 20 | claw 1d3 · claw 1d3 · claw 1d3 · bite 4d6 | fire-res, cold-res, ston-res. |

:::

#### Apelike creatures `Y`
<!-- audit 2026-05-17 #61: 6 rows × 8 cells verified against monsters.h:2372-2417. All stats, attacks, AD_SITM monkey steal, MR_COLD yeti corpse, M1_SEE_INVIS sasquatch clean. 0 corrections. See companion-audit.md. -->


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
<!-- audit 2026-05-18 #141: stats and attacks all match monsters.h:2421-2504. All Z-class entries carry G_NOCORPSE — zombies NEVER leave corpses on death, so the "corpses are unsafe to eat" framing was misleading (there's nothing to eat). M1_POIS varies (kobold/gnome/orc/dwarf/ghoul have it; elf/human/ettin/giant zombies don't), but again moot for eating. Skeleton has G_NOGEN — never randomly generated, only from skeleton-trap or special-level placement. Reworded intro. -->

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
<!-- audit 2026-05-17 #17: 43 rows / 200+ cells verified, 1 corrected (Kops are class K not @). All numeric stats match monsters.h exactly. Close calls: intro promises ninja/Wizard of Yendor/quest nemeses coverage that the table doesn't include. See companion-audit.md. -->

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
| Master of Thieves | magenta | 20 | 15 | 0 | 90 | weapon 4d10 · weapon 2d6 · claw 2d4 steal-amulet | starts peaceful. Rogue quest nemesis. |
| Lord Sato | magenta | 20 | 15 | 0 | 90 | weapon 4d10 · weapon 4d10 | starts peaceful. |
| Twoflower | white | 20 | 15 | 10 | 90 | weapon 4d10 | starts peaceful. Tourist quest leader. |
| Norn | magenta | 20 | 15 | 0 | 90 | weapon 4d10 · weapon 4d10 | starts peaceful, cold-res. Valkyrie quest leader. |
| Neferet the Green | green | 20 | 15 | 0 | 90 | weapon 4d10 · spell 2d8 spell · spell 2d8 spell | starts peaceful. Wizard quest leader. |
| Thoth Amon | magenta | 16 | 12 | 0 | 10 | weapon 1d6 · spell spell · spell spell · claw 1d4 steal-amulet | follows stairs. |
| Master Kaen | magenta | 25 | 12 | -10 | 10 | claw 16d2 · claw 16d2 · spell cleric · claw 1d4 steal-amulet | sees-invis, follows stairs. |
| Master Assassin | magenta | 15 | 12 | 0 | 30 | weapon 2d6 poison · weapon 2d8 · claw 2d6 steal-amulet | follows stairs. Rogue quest nemesis backup. |
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

<!-- audit 2026-05-18 #167: stats/colors/attacks for the full roster verified vs monsters.h:2911-3194. Two corrections: erinys does follow stairs (M2_STALK at monsters.h:2958 — every row in this table carries M2_STALK), so the "except erinys" qualifier is bogus. Amorous demon's displayed form depends on the demon's own randomly-assigned gender (doseduce at mhitu.c:1988-1989 reads Mgender(mon)), not the player's. balrog and amorous demon don't summon (mhitu.c:967). See companion-audit.md. -->
#### Major demons `&`

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
| bone devil | gray | 9 | 15 | -1 | 40 | weapon 3d4 · sting 2d4 poison | poisonous-corpse, demonic. |
| ice devil | white | 11 | 6 | -4 | 55 | claw 1d4 · claw 1d4 · bite 2d4 · sting 3d4 cold · touch 1d1 slow | sees-invis, poisonous-corpse, demonic. |
| nalfeshnee | red | 11 | 9 | -1 | 65 | claw 1d4 · claw 1d4 · bite 2d4 · spell spell | poisonous-corpse, demonic. |
| pit fiend | red | 13 | 6 | -3 | 65 | weapon 4d2 · weapon 4d2 · hug 2d4 | sees-invis, poisonous-corpse, demonic. |
| sandestin | gray | 13 | 12 | 4 | 60 | weapon 2d6 · weapon 2d6 | shapeshifter, ston-res. |
| balrog | red | 16 | 5 | -2 | 75 | weapon 8d4 · weapon 4d6 | flies, sees-invis, poisonous-corpse, demonic. |
| Juiblex | bright-green | 50 | 3 | -7 | 65 | engulf 4d10 disease · spit 3d6 acid | flies, amphibious, amorphous, sees-invis, poisonous-corpse, demonic, fire-res, pois-res, acid-res, ston-res. |
| Yeenoghu | magenta | 56 | 18 | -5 | 80 | weapon 3d6 · weapon 2d8 confuse · claw 1d6 paralyse · spell 2d6 magic | flies, sees-invis, poisonous-corpse, demonic, fire-res, pois-res. |
| Orcus | magenta | 66 | 9 | -6 | 85 | weapon 3d6 · claw 3d4 · claw 3d4 · spell 8d6 spell · sting 2d4 poison | flies, sees-invis, poisonous-corpse, demonic, fire-res, pois-res. |
| Geryon | magenta | 72 | 3 | -3 | 75 | claw 3d6 · claw 3d6 · sting 2d4 poison | flies, sees-invis, poisonous-corpse, demonic, fire-res, pois-res. |
| Dispater | magenta | 78 | 15 | -2 | 80 | weapon 4d6 · spell 6d6 spell | flies, sees-invis, poisonous-corpse, demonic, fire-res, pois-res. |
| Baalzebub | magenta | 89 | 9 | -5 | 85 | bite 2d6 poison · gaze 2d6 stun | flies, sees-invis, poisonous-corpse, demonic, fire-res, pois-res. |
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
<!-- audit 2026-05-17 #24: 60+ cells across 11 rows verified, 0 corrected. All entries match monsters.h:2509-2594 exactly. See companion-audit.md. -->

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
| iron golem | cyan | 18 | 6 | 3 | 60 | weapon 4d10 · breath 4d6 poison | poisonous-corpse, fire-res, cold-res, shock-res. |

:::

<!-- audit 2026-05-18 #158: all 6 entries (jellyfish/piranha/shark/giant eel/electric eel/kraken) verified clean vs monsters.h:3205-3256. All carry M1_SWIM | M1_AMPHIBIOUS. AD_WRAP grab-and-drown mechanic confirmed at uhitm.c:3378-3401. 0 corrections. v2 audit 2026-05-18 #19: two factual fixes. (a) The wrap-and-drown intro applied to all 6 rows, but only giant eel, electric eel, and kraken have AT_TUCH/AT_HUGS+AD_WRAP per monsters.h:3230-3256. Jellyfish/piranha/shark just bite or sting. Reworded. (b) Jellyfish "sting 3d3 poison" loses the AD_DRST detail — the sting is a poisonous strength-drain (uhitm.c:3149,3157). Changed to "sting 3d3 drain-Str" matching the spoiler's own drain-stat notation elsewhere. See companion-audit.md. -->
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
<!-- audit 2026-05-18 #146: clean. All 8 entries (newt, gecko, iguana, baby crocodile, lizard, chameleon, crocodile, salamander) match monsters.h:3260-3324 for stats, attacks, and special flags. Lizard corpse cures stoning (eat.c:827-830, fix_petrification), never rots (eat.c:1483, 1510). Newt corpse occasionally restores 1-3 Pw via eye_of_newt_buzz (eat.c:1102-1123). Chameleon is M2_SHAPESHIFTER. Salamander has the 4-attack chain weapon 2d8 / touch 1d6 fire / hug 2d6 / hug 3d6 fire. -->


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
<!-- audit 2026-05-17 #46: ~30 5.0 changes verified against fixes5-0-0 + source (themed rooms, 4 new monsters, helm of caution, helm of brilliance rename, spell-level rebalance, unicorn horn no-attribute-restore, BoH scatter-not-destroy, Valkyrie starts with spear, Excalibur 1/30 dip, demonbane = silver mace, HP regen formula, 3/2 two-handed Str bonus, covetous-monster either-staircase warp, Castle no master/arch-lich, hot-ground potion destruction, alchemy smock 1/30, crystal armor cracks, candle sqrt formula, MC overhaul attribution to 3.6, all 4 new conducts, intelligent-monster containers). Corrected 4: chain lightning is level 4 not 7; "mummy withering" was fabricated (no such mechanic; mummies do AD_PHYS); Elbereth -5 alignment penalty is not a 5.0 change; supply chests appear above the Oracle, not "the first ten levels." Also clarified: mind flayer change is map/ID amnesia is gone, spell/skill loss persists; sink dipping for potions only. See companion-audit.md. -->

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
  attack per turn ("Shkinng!") even on foot. **Sunsword** gains a
  `#invoke` blinding ray that works on any monster, not just undead
  — a 5-Pw on-demand Camera flash. **Trollsbane** regenerates while
  wielded, a real lifeline for an early character. **Amulet of
  flying** confers flight on your steed as well as you, turning
  warhorses into water-crossing cavalry.
- **Gehennom** levels are more varied and interesting.
- **Medusa's Island** now has four possible layouts.
- **Special levels** can now generate mirrored (flipped), so don't
  rely on fixed maps.
- **New conducts** are tracked: pauper, petless, permadeaf, and
  Sokoban (no cheating).
- **Touch of death** has been reworked: instead of binary kill,
  it now deals heavy damage and drains max HP. Magic resistance
  reduces but no longer fully prevents it.
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
- **Magic cancellation** was overhauled in 3.6. The cloak of
  magic resistance is now MC1 (was MC3). The cloak of protection is
  the only single item providing MC3. MC3 now blocks 90% (was 98%).
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
  Oracle (about a 2-in-3 chance per fillable room), containing
  useful early-game items like healing potions and enchant scrolls.
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
- **Iron bars** are a dungeon feature (since 3.6). You can't break
  them with a weapon or dig through them; the practical way past is
  to dig around the side through the adjacent wall, or polymorph into
  something with acid breath. (Potions of acid don't work on bars.)
- **Shopkeepers** can now remove pits and webs around them, nerfing
  the classic pit-pinning kill setup. Walking into a peaceful
  shopkeeper now auto-pays any debts before the inventory prompt.

---

#### What to Lean Into

A few 5.0 changes have tactical implications worth pulling out:

**A blessed potion of polymorph is now a self-contained controlled
polymorph.** No ring of polymorph control required: blessing the
potion grants control for that one transformation. Single-use
polymorph strategies (iron golem form for extreme AC, bat form to
scout, pick something with a good intrinsic) are now accessible
without needing to find or wish for the ring first. The ring is
still useful for ongoing polymorphing, but for a single planned
transformation, one blessed potion does the same job.

**Vampire polymorph supports genuine form cycling.** A polymorphed
vampire can `#monster` to switch between vampire, bat, and fog
cloud forms. This used to be a one-way door; in 5.0 it's a loop.
Fog cloud passes through doors and certain barriers, bat form
offers flight and mobility, vampire form does the fighting. A
polyed vampire plans routes by form rather than by direction: fog
through the chokepoint, fight in the open room, reposition as bat,
repeat.

**Gold dragon scale mail eliminates your light source slot.** The
mail provides a 2-square innate light radius in addition to its
two resistances. In the late game, when inventory is a puzzle and
every slot counts, wearing it lets you retire the lamp and use
that slot for something that actually matters.

#### What to Watch Out For

**Luck-grinding by sacrificing weak corpses no longer works.** In
3.6.x, a stack of kobold corpses on a co-aligned altar could push
your luck to maximum through sheer volume. In 5.0, if your current
luck score already exceeds the difficulty rating of the monster
being sacrificed, you gain zero luck. The gods accept your kobold,
bless the corpse, and give you nothing. To push luck higher once
you're past the low positives, you need fresh corpses of monsters
whose difficulty actually exceeds your luck value. In practice: a
luckstone handles maintenance; sacrifice mid-tier monsters when
you want to push higher.

---

#### What to Change in Your Gameplay Habits in 5.0

- Stop leaving containers unattended in cleared-but-not-cleaned
  areas, and stop hauling speculative corpse collections through
  caster-heavy floors (monsters now loot and animate).
- Stop dropping potions on the floor in Gehennom (hot ground
  shatters them).
- Start checking every container in the first ten levels for
  supply caches.

---

*For more than forty years, NetHack has challenged and surprised
generations of players, and for 5.0 the dungeon has been
thoughtfully redesigned by people who wanted it to be better and
more dangerous simultaneously. Welcome, adventurer.*

*You descend the stairs...*

---

### Acknowledgements
<!-- audit 2026-05-17 #18: historical claims spot-checked against Wikipedia + bundled dat/history. NetHack 1987, Fenlason→Brouwer→Stephenson lineage, DevTeam founders, Izchak Miller 1994 death, Hack 1982 origin all verified. WikiHack founding year, article counts, and some spoiler-author attributions could not be independently verified (nethackwiki.com 403). See companion-audit.md. -->

NetHack has been played, cursed at, loved, and documented since
1987. The game itself is the work of the NetHack DevTeam, a
loose collective of developers who have maintained one of the
longest-running continuously developed open source projects in existence. But the
documentation, the strategy, the collected wisdom about how to
actually survive the thing, that came from the players.

In the early days, knowledge spread through Usenet, specifically
the newsgroup **rec.games.roguelike.nethack** (RGRN). Thousands
of players posted questions, argued about strategy, and slowly
assembled a shared body of knowledge about a game that refused to
explain itself. This was before wikis, before Reddit, before
Discord. If you wanted to know whether a cockatrice corpse could
be wielded as a weapon, you searched the RGRN archives and hoped
someone had asked before you. Someone usually had.

RGRN gave the community its vocabulary. A **YASD** (*Yet Another
Stupid Death*) is the post you make after dying to something you
should have known better than to do. The term captures something
important: NetHack kills you in ways that feel obvious in retrospect,
and the community's response to that is not bitterness but
documentation. A **YAFAP** (*Yet Another First Ascension Post*)
is the post you make when you finally win. Both traditions persist
today, in the wiki, on Reddit, in Discord servers: the ritual
confession of failure and the ritual celebration of survival. They
are the two poles around which the whole community orbits.

Out of those conversations came the first spoiler files: plain text
documents that attempted to catalog every item, every monster, every
interaction. They were written by hand, cross-referenced against the
source code, and shared freely. They represented hundreds of hours
of work by people who simply loved the game and wanted to help
others play it.

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

**Paul Waterman** wrote the WCST NetHack Spoilers (originally the
"World's Encyclopaedia of NetHack"), a single sprawling document
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

**David Damerell** wrote the Object Identification FAQ, the
original systematic guide to figuring out what you've found
without wasting scrolls of identify.
**Kieron Dunbar** wrote the wand identification guide, laying
out the engrave-test method that remains the fastest way to sort
wands.
**Trevor Powell** compiled the Instadeath Spoiler, the definitive
catalog of ways to die in a single turn, cited in our Dangerous
Encounters chapter.
**Arien Malec** wrote the Medusa guide, collecting crossing
strategies from dozens of RGRN posters and organizing them into
a clear checklist.
**Matthew Lahut** wrote the prayer guide that untangled the
timeout and alignment systems.
**Boudewijn Waijers** mapped solutions for all eight Sokoban
level variants.
**Steven Bush** calculated spellbook reading success rates.
**Gregory Bond** documented shopkeeper pricing formulas.
**Dion Nicolaas** cataloged the voluntary challenge conducts.
**David Goldfarb** wrote the air elemental FAQ.
**Hojita Discordia** documented experience value calculations.

And many others: Ray Chason, Pat Rankin, Geoduck, Topi Linkala,
Geoffrey Eadon, Roger Broadbent, Sebastian Haas, Jukka Lahtinen,
and the countless anonymous posters on RGRN who asked "has anyone
tried..." and then reported back.

**The [NetHack Wiki](https://nethackwiki.com/)** has been an
indispensable reference for this guide. Founded as "WikiHack" by
Sgeo in 2005, it migrated to its own domain in 2010 and now
contains over five thousand articles documenting every corner of
the game. Its creators and maintainers include Pasi Kallinen,
Drew Streib, Alex Smith, Shawn Moore, George Koehler, Tjr,
ZeroOne, and Ray Chason. The wiki's
[NetHack 5.0.0 page](https://nethackwiki.com/wiki/NetHack_5.0.0)
is the community's living changelog and was a major reference
for the 5.0 update of this guide. The wiki is hosted alongside
[nethack.alt.org](https://alt.org/nethack/), the longest-running
public NetHack server.

**The r/nethack community** on Reddit has kept NetHack discussion
alive for a new generation of players. Its moderators over the
years have maintained a welcoming space where veterans and newcomers
trade advice, share ascension stories, and argue about optimal wish
choices. The community's collective knowledge, passed along in
thousands of threads, has informed the practical advice throughout
this guide.

Above all, this guide exists because the game itself exists.
**NetHack** has been developed since 1987 by the NetHack DevTeam,
founded by Mike Stephenson, Izchak Miller, and Janet Walz. Izchak
Miller passed away in 1994; the shopkeeper who bears his name in
the Mines is a small measure of how much his work meant.

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
December 2003, the DevTeam went quiet (not absent, but silent)
for twelve years. The dungeon was frozen. New players descended into
the same unchanging corridors that had been killing people since
2003, writing new spoilers about a fixed game, dying in the same
newly-documented ways. That the accumulated community wisdom from
those twelve silent years remained useful, that the game was deep
enough to sustain a decade of fresh analysis without adding a line
of new code, tells you something about what kind of artifact
NetHack is. Version 3.6 arrived in December 2015, and active
development has continued since.

The current team, including Michael Allison, Ken Arromdee, David
Cohrs, Jessie Collet, Pasi Kallinen, Ken Lorber, Dean Luick,
Patric Mueller, Pat Rankin, Derek S. Ray, Alex Smith, Mike
Stephenson, Janet Walz, Paul Winner, Bart House, and Warwick
Allison, has maintained and extended the game across nearly four
decades. Everything in these pages is downstream of their work.

This is what a community looks like over decades. People writing
things down so that others don't have to die the same stupid death.
It's generous, it's nerdy, and it's one of the best things about
NetHack.

All data in this guide has been verified against the current game
source code. Any errors are ours alone.

---

*A Traveler's Companion to the Mazes of Menace 5.0 Launch Edition,*<br>
*compiled by David Bau.*

*This work is licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
