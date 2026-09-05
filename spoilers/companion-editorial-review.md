# Editorial Review of *A Traveler's Companion to the Mazes of Menace*

*Prepared 2026-09-04. Every line number is `spoilers/companion.md` at the
time of review; every `file:line` is `nethack-c/upstream/`. Findings
marked (sc) were re-verified by the collating editor against
the source; the rest come from section reviewers whose citations were
sampled and held up in every case tried.*

The book is in good shape. Three fact audits have left the body prose
almost free of implementation talk, C identifiers, and the flourishes
the style rules forbid; the voice is consistent and the structure is
sound. What this pass found is different in kind from the earlier
audits: a scatter of confidently stated mechanics that are wrong
(concentrated in Artifacts, Points of Interest, and the Field Guide), a
set of contradictions between chapters that grew as chapters were
edited separately, and a layer of ornament in the prose that reads as
written by a machine rather than a person. Below: what a great game
guide does, the ten changes with the most leverage, then the detail.

## 1. What makes a game guide people keep on the shelf

The guides that outlive their games share ten habits. The Companion
already has most of them; the gaps are noted.

1. **A voice you want at your shoulder.** Opinionated, warm, funny in
   passing, never performing. Tells you what to *do*. The Companion
   has this. Where it slips is into ornament: parallel triplets,
   restated nouns, closers that say nothing. Section 5 quotes them.
2. **Dual use.** Reads cover to cover as a journey and answers a lookup
   in thirty seconds. Needs a "how to use this book" page, one
   template per item chapter, an index in the reader's words, and
   page references in print. The Companion has the index (print only)
   and a strong TOC, but no usage page, no conventions box, and print
   cross-references that mostly print as coloured words with no page.
3. **Progressive disclosure.** First-hour survival first, a marked
   "come back later" tier, deep reference last. The Companion's Part
   order is right, but a beginner meets thirteen role essays before
   the one-line recommendation, and Elbereth lives in a chapter about
   traps.
4. **Decision rules, not fact heaps.** "If HP is under a seventh of
   max, pray" beats a paragraph of prayer mechanics. Every mechanic
   chapter should end in a rule the reader can act on, and the
   life-or-death ones deserve a box: pre-descent, emergency,
   ascension kit. The emergency page exists only on the print cover.
5. **Worked examples.** The best guides teach with a short story then
   generalise. The Companion's fountain routine for Knights (L1283)
   and the engrave-test procedure (L5265) are the model; most sections
   have no example at all.
6. **Pictures that carry information.** One figure per big decision.
   The Companion has three dungeon maps, an identification flowchart,
   sixteen Sokoban maps, and one ASCII corridor sketch. Prayer,
   Elbereth, the route through the branches, the status line, and the
   Castle have none.
7. **Consistency of shape.** Same template per potion, scroll, wand,
   ring, tool; same columns; same notation for levels, prices, odds.
   Potions, scrolls, and wands share a template; rings, amulets,
   tools, and armor each do something else.
8. **Earned trust.** Verified, version-pinned, honest about
   uncertainty, never inventing a reason. This is the book's brand
   and it mostly holds; the invented reasons that remain ("sacrifice
   early to lock in that bias", the closet "teleport-trap clue") are
   listed in section 6.
9. **Economy.** Every sentence pays rent. The role essays, the
   quest-artifact catalogue, and three separate treatments of wand
   recharging are where it doesn't.
10. **A physical object worth owning.** A5 trim, tables that fit,
    part openers, a real index, an inside-cover reference. The print
    build has the cover reference and index; it lacks part openers
    and usable page cross-references.

## 2. The ten changes with the most leverage

Ranked by how much they improve the book per hour of work.

1. **Fix the confirmed factual errors** in section 6, starting with
   Artifacts (a third of its specific mechanics are wrong), Points of
   Interest (thrones, altar conversion, sinks), the Field Guide
   (Massacre, mummies, horses), the corpse table (pets, nymphs,
   stalker), and the Golden Rules (prayer gate, silver, stair-fall).
2. **Reconcile the sixteen contradictions** in section 4, each of
   which has one right answer already in the book.
3. **A "How to Use This Book" page** after L99: the first-descent
   reading path, the lookup path, and a conventions box (bold, code,
   Dlvl, $ vs zm, "(new in 5.0)").
4. **One item template** for Rings, Amulets, Tools, and Armor, matching
   Potions/Scrolls/Wands: table (Price, Item, Chance, one-line use),
   then anchored "Key X" entries (what it does, how you recognise it,
   what to do), then mechanics.
5. **Move Elbereth (L2406) and Engravings into Part Three**, promote
   "Saving Yourself from Imminent Death" (L4216) to open Part Three,
   and put the emergency checklist in both builds.
6. **A role-at-a-glance table** at the top of Choosing Your
   Expedition, with the thirteen parenthetical intrinsic ladders folded
   into it, and the one-line recommendation moved up from L574 to the
   chapter opener.
7. **Collapse the duplicates** in section 4 (wand recharging ×3,
   unicorn horn ×2, Excalibur dip ×6, curse testing ×7, Mine's End
   luckstone ×2) to one home each plus a sentence and a link.
8. **Print page references** for every cross-reference outside the
   current chapter (`latex-filter.lua:265-321` currently pagerefs only
   "see" links and five anchors).
9. **A prose pass for register** using the quoted list in section 5:
   replace ornament with the concrete sentence a person would say,
   and cut the closers that restate the paragraph.
10. **Five figures**: a prayer decision flowchart, an Elbereth card, a
    route strip with Dlvl ranges, a status-line decoder, and a Castle
    layout.

## 3. Structure and navigation

**Front matter (L69-99).** Sets the stance well ("close the Companion
now and learn the hard way") but never says how to use the book. The
historical introduction (L11-65) is LaTeX-only, so web readers never
see it. The print build has an inside-cover command reference and a
"Dungeon Emergency Checklist" (`template.tex:405-451`); the web has no
equivalent. TOC descriptions are missing for chapters 38-41
(L158-161), and chapter 17's description repeats its title.

**Chapter order.** The Part sequence (character, world, survival,
gear, mastery) is right. Misfiled chapters:

- *Saving and Bones* (L3651, 94 lines) sits between the two death
  chapters. Move to Part One after Your First Descent, or to the
  appendices.
- *Elbereth* (L2406, ~150 lines, 12 inbound links, on the print
  emergency page) is the seventh section of "Traps and Hazards" inside
  "Dungeon Sights". It is the book's most important survival tool and
  belongs in Part Three. The same chapter also holds Searching,
  Secret Doors, Engravings, and Iron Bars: a grab-bag.
- *Shopping and Shopkeeper Pricing* (L11042) is prose in the
  appendices while its price tables live in Part Four (L4852-5254).
  Put them together.
- *Luck and Fortune* (L7972) matters from turn one; move it to Part
  Three after Divine Relations and fold the 47-line *Exercising Your
  Stats* into it.
- *What Changed Since Last Time* (L13963) is for returning veterans,
  who will look for it first. Make it the first appendix.
- Parts have no opening text (L847, 2665, 4750, 7792, 9662). Three to
  five lines naming which chapter to read first would carry the
  beginner path.

**Section templates.** Potions (L5817), Scrolls (L6026), and Wands
(L6253) share table, then anchored "Key X" entries, then mechanics.
Rings (L6563) has a price table with one-phrase notes and no Key
Rings, so the index sends nine ring entries to the same table
(L14677-14686). Amulets (L6638) is table then unanchored prose. Tools
(L6733-6870) is five category tables with no Key Tools; the bag of
holding and unicorn horn are prose only. Armor (L7018) is prose by slot
under `#####` with no summary table. Weapons (L7344) groups "by how
they're used" while the Weapons Tables appendix groups by skill, so
the reader translates between two groupings. Lead columns differ:
potions and scrolls lead with chance, wands and rings with price.

**Length balance.** Choosing Your Expedition runs 412 lines with
three sections and 120-word average paragraphs; the role essays are
210-273 words each. What to Pack (75 lines) is the shortest chapter
in Part One and the natural home of a pre-descent checklist.
Identification (844 lines) is inflated by ~400 lines of price tables.
Spellcasting (178 lines) is light for a common first pick; a "first
spells by role" table would fix it. The Bestiary appendix is 1547
lines.

**Navigation.** 503 internal links to 205 anchors, none broken; 280
index targets, none broken. Density is uneven: the Field Guide has 142
links, while Rings, Curses, Spellcasting, and Feelings have one each
and Saving and Customization have none. Curses (L7696) should link
remove curse, holy water, priests, and prayer. The Feelings table rows
(L2591-2607) should link to their subjects. The sidebar TOC lists only
H2/H3 (`template.html:57`). Duplicate heading texts: "The Castle" at
L2004 (explicit id) and L8924; the armor slot names (Shirts, Cloaks,
Helmets, Gloves, Boots, Shields) appear as `#####` in the Armory and
`####` in Armor Tables, so the print TOC shows two of each.

**Index (L14157-14904, print only).** Hand-built with subentries and
wit; reads like a real index. Fixes: duplicate heads "Altar:" and
"Altars:" (L14191-14192); glosses filed under the wrong word ("The:
Price Is Right" L14782, "Wow! This makes you feel great!" L14873,
"Discipline, the difference" L14330); jargon the prose avoids ("BoH"
L14241, "Minesflayer" L14562, "Foocubus" L14386); "Amulet:" (L14194)
is twelve glosses pointing at one page. Seven index entries
contradict the body (section 4, item 12). The anchors exist, so a web
index would cost little.

**Pedagogy.** Exists: Golden Rules 1-7 (L708-788, as paragraphs), the
early hazards list (L788), the ID flowchart (L4769), the Ascension Kit
table (L9309), "Saving Yourself from Imminent Death" (L4216, filed as
the last section of Ways to Die Instantly), and the print-only cover
checklist. Missing or buried: the emergency page on the web, a
pre-descent checklist, a single itinerary of the recommended route
(altar, Sokoban, Mines, Minetown, Oracle, Quest, Castle; the seed is
"Sokoban or Mines first?" at L1500), and a boxed one-line version of
the Golden Rules. The Golden Rules themselves omit Elbereth and the
`s` search command, so "retreat" and "look for hidden passages" are
not executable from that page.

**Visuals.** Three SVG dungeon maps, the ID flowchart (web SVG at
L4772, print PDF at L4961), the ASCII chokepoint diagram (L714), room
sketches (L973), a Mines sketch (L1534), sixteen Sokoban maps, and
about 150 tables. Highest-value additions: a prayer decision flowchart
(the priority list at L4325 is ready-made), an Elbereth quick card
(who ignores it, the defile rule, the three ways to write it), a
route strip in Branches with Dlvl ranges in recommended order, a
status-line decoder near Your First Descent (hunger, encumbrance, the
HP prayer threshold), and a Castle layout (drawbridge, standing
square, trap doors, wand tower).

## 4. Contradictions and duplicates across chapters

Each contradiction below has one right answer already in the book.
(W2 = whole-book continuity reviewer; sc = spot-checked by the editor.)

1. **Enchant weapon.** L7645-7647 "no destruction limit ... never
   lost" vs L6122-6124 (+6 and up, 2/3 chance) and the table at L6086
   "above +6". `wield.c:999-1000`: `spe > 5 && rn2(3)` evaporates
   (sc). L6122 is right; fix L7645 and make L6086 "at +6 or higher".
2. **Prayer timeout.** L749 "about once every thousand turns" and the
   index (L14643) vs L4351 "averages around 450" and L4375 "roughly
   500". `pray.c:1356` is `rnz(350)`: median 350, mean about 450, a
   long tail. Both can stand if L749 becomes the safe waiting rule
   ("count on about a thousand turns between prayers to be safe; the
   actual wait averages about five hundred but can run much longer").
   The audit badge at L691 claiming "averages ~1000" is the wrong one.
3. **Potion of healing and blindness.** L5851 "cures blindness unless
   cursed" and L6001-6002 vs L3641 "a *blessed* potion of healing".
   `potion.c:1999-2000`: blessed only. L3641 is right.
4. **Sleep resistance sources.** L3191-3193 says the Wizard's cloak
   of magic resistance and the Ranger's elven cloak grant it. The
   Ranger starts with a cloak of displacement; neither cloak grants
   sleep resistance (`objects.h:615,644`) (sc). The book's own table
   at L13864 is right.
5. **Fedora.** L7159-7160 calls it "the base item for the Eye of the
   Aethiopica, the Priest quest artifact". The Eye is the Wizard's
   amulet (L1785, L8825); the Priest's is the Mitre (L8819) (sc).
6. **Drain resistance.** L7271-7272 "no non-artifact source outside
   this shield" vs black dragon scale mail at L3483, L4099, L13870.
7. **Castle wand chest.** L6821-6823 warns residents "can empty" it;
   L9014-9018 says monsters cannot unlock chests. `castle.lua:144`
   locks it and `muse.c:2273` refuses locked containers (sc). L6821 is
   wrong.
8. **`#invoke` key.** L8805 "default `^A`" vs L9702-9704 Ctrl+A as
   repeat. `cmd.c:1744` binds invoke to `M-i` (sc).
9. **Priest donation.** L1572-1574 "a point of intrinsic protection"
   vs L4461-4463 "2-4 points". `priest.c:694-695` `rn1(3,2)`. L4461 is
   right.
10. **Mummy corpses.** L1122 "dangerous to eat (age you)" vs
    L5729-5730 "No corpse: `M` mummies". A mummy drops its base race's
    corpse, already rotten (`mon.c:629-645`); nothing ages you.
11. **Shimmering dragon.** L5772 lists it; it is deferred in 5.0
    (`objects.h:509-512`, `#if 0`). Remove.
12. **Index vs body.** Throne wish "positive Luck 7+" (L14783) vs
    non-negative (L1339, L1355); wish syntax "+3" (L14866) vs the +2
    advice (L8566-8574); minotaur "~38" (L14564) vs 42 (L3243);
    Grayswandir "half phys" (L14428) vs double damage (L8668, L8704);
    wand of digging "cursed zaps down" (L14844), a removed mechanic;
    gnomish wizard "sleep spell" (L14421) vs psi bolts (L3179);
    alchemy "blast ~1 in 30" (L14189) vs 10% (L5979).
13. **Mines readiness.** L1507-1511 and L1566-1567 recommend Sokoban
    first and Minetown early; L3181-3183 says return only at XL 5+
    with sleep resistance and AC 0 or better, which L2752 calls
    mid-game. Pick one bar.
14. **Disenchanter.** Listed under Mid-Dungeon Threats (L1129, with
    "dragonhide" weapons that don't exist) vs Gehennom-only (L4123).
15. **Corpse freshness.** L803-805 (safe 30, tainted ~175), L5666
    (30-50), L5725 (50), and L3453-3454 (globs ~500, "twice a normal
    corpse"). Align.
16. **Shields and casting.** L7251-7252 "penalty unless small shield"
    vs L7261-7262 "any shield still adds a flat penalty" twelve lines
    later.

**Duplicates** (home in bold; the others shrink to a sentence and a
link): Mine's End luckstone decoys L1594-1612 and L5507-5514 nearly
verbatim (**Gray Stones**); Excalibur dip at L1275-1294, L344,
L561-562, L7385-7390, L8698-8701, L14065-14066 (**Fountains**); wand
of wishing charges at L6350-6357, L6467-6477, L6136-6144, L6933-6936,
L8479-8480, L9020-9025, with the charging-explosion ladder twice
(**Wands, Recharging**); unicorn horn in full at L5988-5997 and
L6887-6904, with "no longer restores attributes" at L3898, L5994,
L6899, L14012 (**Tools**); pet curse test at L613-616, L740-741,
L2770-2774, L4602-4610, L4672-4673, L4827-4835, L7756 and altar flash
at L1304-1311, L4818-4825, L5564, L7754 (**Identification**);
encumbrance tiers tabled twice (L2830-2841, L6785-6797); seven
candles at L1578-1583, L6851-6854, L9251-9256, L9337 with "is the
clean answer" verbatim twice (**The Heist**); Elbereth dead-in-Gehennom
at L2473-2474, L2530, L9056, L9472-9477 and the defile rule at four
places (**Elbereth**); plus eel grabs, floating eyes, Sokoban
penalties, same-race sacrifice, fountain-wish odds, magic-lamp odds,
and Vlad's throne, each in two or three places.

**Terminology drift.** "Cave Dweller" (the 5.0 name; L281, L518,
L7047, L10952) vs "Caveman" (L640, L5717, L7423, L7449, L7595, L8334,
L8840, L9075, L11541, L11693, L12307) vs "Caveperson" (L13889,
L13905). Money: `$N` (41 uses, Identification, Scrolls, Wands) vs `zm`
(34 uses, Armory, Tools, Shopping) vs "zorkmids" and "gold pieces".
Levels: "Dlvl 2 to 4" (L1508) vs "dungeon levels 2 through 4" (L1529)
vs "Dungeon level 12" (L3157) vs "level four" (L89). Odds within one
passage: "about 1/30", "1/6", "1-in-3", "one in seven" (L1241-1286);
the dominant form is "1 in N". Keys: "Ctrl+A" (11 uses) vs "`^A`"
(L8805). "experience level N" in the roles chapter vs "XL N" later.
"pickaxe" (8 uses) vs the in-game "pick-axe" (3). "foocubus" (5 uses)
vs "amorous demon" (2). "BoH" in prose at L6812. Third person "the
player" at L3256 and L3281.

**Formatting.** `####` headings are Title Case in Parts One to Four
and sentence case in Advanced Controls, Artifacts, Gehennom, and the
Intrinsic tables; "A note on nymphs" vs "A note on Seduction".
"**Defenses.**" (L3340, L3441, L4140, L9636) vs "**Defenses:**"
(L3782-4096). The Curses chapter's bullets drop terminal periods
(L7724-7780). "The table above" at L4890 refers to a print-only table
that follows at L4998. L12958 links dragon scale mail to
`#armor-tables` instead of `#dragon-scale-mail`.

**Repeated phrases.** "the dungeon's [superlative]" 19 times (five in
the Armory alone); "the single most" 7; "worth knowing" 8; "The catch"
8; "one of the most / the most important" 10; "lifeline" 4; "the real
prize" 4; "the clean answer" twice verbatim.

## 5. Style: where the prose sounds like a machine

The body prose is clean of the old sins (no C identifiers, no
implementation talk, no "the lesson is", almost no em-dashes outside
tables). What remains is ornament: parallel triplets built for rhythm,
closers that re-say the paragraph, apposition that restates its noun,
vague comparatives, and the occasional sermon cadence. These are the
sentences a reader hears as written by a machine. The list below is
the reviewers' selection, most damaging first within each chapter,
each with the plainer sentence a person would say. (Two examples from
the roles chapter were fixed during this review: the Valkyrie/Wizard/
Archeologist triplet at L231 and the Archeologist's "crack open a
statue" clause at L247.)

**Choosing Your Expedition.** L264-277 Barbarian: "your strong early
game becomes a strong whole game" (aphorism; cut). L286-292 Cave
Dweller: "one careful meal at a time, which makes an amulet of life
saving more precious to you than to almost anyone" (ornament plus a
non-sequitur; end at "by eating the right corpse"). L303 Healer: "a
role that keeps you alive by keeping you well" (chiasmus; cut the
clause). L333-334 Knight: "The pony is both a friend and the key to
your signature move" (cut). L350-351 Monk: "You carry no weapon,
because you are the weapon" (cliché); L355-357 "resistances and senses
unfolding one after another"; L366-367 "It is an unusual path, and a
graceful one in practiced hands" (closer that says nothing; cut);
L364-366 "Guard that robe, keep to a vegetarian diet to honor your
discipline, and trust your hands" (triplet closer). L372-374 Priest:
"a knowledge other adventurers would trade a great deal for" (cut).
L451-452 Tourist: "a role nobody expects to cast turns quietly
formidable" (vague; say what: "and with Int and the Card's magic
resistance a Tourist casts well"). L468-469 Valkyrie: "so the question
of an endgame weapon is answered almost before you ask it"; L472-473
"before the dungeon turns cruel". L475-477 Wizard: "Magic is your
birthright, and by the end of a run there is little in the dungeon you
cannot unmake with a spell"; L486-487 "learning begets more learning".
L549-550: the good/balanced/evil contrast never lands; propose "It's
tempting to think of these as good, balanced, and evil, but the game
doesn't judge you that way. Alignment is a number."

**Your First Descent.** L702-706 "Levels one through five kill the
most adventurers, not from the greatest threats but from your fewest
resources" (mangled antithesis) → "More adventurers die on levels one
through five than anywhere else, not because the monsters are fierce
but because you have so little to answer them with." L815 "Killer
bees, soldier ants, and gnomes all kill in this same shape" → "arrive
the same way". L650-652 "New adventurers pick up everything they find.
Veterans pick up everything they need." is a parallel of the kind the
style rules discourage, but it is funny and concrete; author's call.

**Branches and Landmarks.** L1511 "Slashing through the Mines early is
exciting, but patient players return stronger and better equipped"
(vague comparative) → "The Mines are a fairer fight after Sokoban: you
come back with reflection or a bag of holding and a few more levels."
L1788-1793 "your role's signature relic, attuned to you as no other
item in the game can be, and it tends to anchor your kit ... Each
carries a blend of powers suited to its owner" → "Most quest artifacts
are worth carrying for the rest of the game; each gives some mix of
magic resistance, telepathy, warning, reflection, or luck." L1597-1598
"which affects everything from combat to fountain wishes" → "Luck feeds
your to-hit rolls, your prayers, and every wish." L1897-1899 Ludios "a
good place to visit for gold, identification scrolls, or shop stock,
but it's not essential for victory" (restatement; no identification
scrolls are placed there) → "None of it is required to win; the gold
is the reason to come, and it buys protection from priests."
L1578-1579 candles: corrective-hedge opener that duplicates L9252.
L1592 "they'll call for reinforcements" (invented) → "Anger one and the
whole watch turns on you." L1885-1886 "The level is non-diggable. The
level prevents teleportation" → one sentence.

**The Art of Combat.** L2734-2739 "This narrows the gap ...
considerably ... measurably more damage ... run those numbers again"
→ "At 18/100 Strength the +6 bonus becomes +9 on a two-handed sword, so
d12+9 beats a long sword's d8+6 by about five points a swing."
L2823-2824 "a worn passive that costs no inventory slot and no
spell-pool drain" (gamer jargon) → "Speed boots are the easiest way:
put them on once and stop worrying about potions and spell energy."
L2960-2962 "thinking about where you stand, when you swing, and what
happens if it goes wrong" (triplet previewing the sub-headings; cut).
L2954-2955 "the best damage budget in the game"; L3025 "the best
damage soak in the game" and L3023 "absorbs one hit per round" (not a
mechanic) → "A pet next to the monster draws some of its attacks and
adds its own." L3087-3088 "be ready for it to make a decision about
that arrangement" → "expect it to turn and fight." L2977-2978 "spends a
turn rounding the corner, and you get a free hit" → the real effect: a
monster that steps next to you does not swing that same action.
L2967, L2986 "Never fight a mob", "Never let yourself be surrounded" →
"Don't fight a crowd in an open room when a corridor is in reach."
L3072-3084 version-diff framing ("now back away", "no longer works",
"This change") → plain present tense.

**Ways to Die Instantly.** L3753-3758 "Not by whittling down ... not by
wearing you down ... but by ending your life ... the difference between
a promising run and a one-line epitaph" → "Some things in the Mazes
kill you in one move no matter how many hit points you have. Players
call them instadeaths, and nearly every one gives a warning a turn or
two ahead if you know what to look for." L3729-3733 (triplet with an
opaque third item) → "Whatever killed the previous adventurer is
usually still there, and often far too strong for the depth."
L4124-4125 "the silent ascension-killer it's reputed to be, but the
mechanic is more constrained than common lore suggests" (meta). L3821
"starvation is a real threat" (cut). L3886 "plan any drawn-out mind
flayer fight carefully" → "don't stand and trade blows with one."
L4242 "Fire is the most reliable cure" (restates; cut). L4233 "Dead."
and L4213-4214 "Don't do this." (fragments). L3681-3684 "anti-scum
mechanism ... what the community calls" → "there is no reloading after
a death. Copying the save file to retry one is called save scumming,
and is cheating." L3805, L3811, L3846-3847, L4178-4183 "the choke check
fires", "a timer death", "roll fires per qualifying hit", "Rolls
17-19" → percentages ("15% full touch, 60% smaller drain, 25% miss").

**A Practical Identification Strategy.** L4815-4816 "which tells you
something about clerical paranoia" → "(Priests are the exception: they
sense it at a glance, an occupational habit.)" L5279 "Don't be afraid
of the suspected wand of wishing." → "A suspected wand of wishing is
safe to engrave-test." L5436-5437 "putting them on without BUC-checking
can ruin a run" → "put on cursed, they leave you floating out of reach
of the floor or tripping every few steps until you can uncurse them."
L5472 "flint is useless ammunition" (dismissive) → "flint is sling
ammunition". L5584-5586 "the most lethal mistake on the identification
table" → "(a botched read can paralyze you for many turns among
whatever is nearby)". L4928-4929 "minus the usual surcharge" reads as
removed; it stays.

**Provisions and Dining / The Apothecary.** L5903-5906 "the difference
between trading blows and hitting twice before they swing once"
(overstates intrinsic Fast, a free action one turn in three) → "Speed
is one of the best buffs in the Mazes: intrinsic Fast hands you a free
action about one turn in three, which across a fight means extra hits
and a head start on every retreat." L5800-5802 "(a 5.0 food-handling
detail that doesn't change the strategy)" (meta; cut). L5668 "Never
eat old corpses. If in doubt, don't eat it." duplicates L5666. L5652
"Eat NOW or die." → "Collapse at random; eat or pray at once."

**The Scroll Rack / Wands.** L6104 "read $300 scrolls blind" collides
with the Blind status. L6150-6153 "Never blessed-genocide ..." then a
sentence saying the same thing; keep one. L6208-6209 "Never price-ID
it by reading it on your own square" → "Bless it and keep it; an
unblessed test-read goes off in your own pack." L6386-6390 "Do NOT put
this wand in a bag of holding (it will explode the bag) ... Keep it
separate" (shouted, twice) → "Keep it out of a bag of holding: the wand
destroys the bag and everything inside." L6278-6283 the Wands opener
defines the heading; open with what a wand does for anyone ("A wand
puts a spellcaster's tricks in anyone's hands..."). L6312 "NODIR" in a
reader-facing table → "None".

**Rings and Amulets / Tools of the Trade.** L6632 "Economy of fingers
is an art." (cut). L6642-6643 "The stakes are high, because the range
runs from 'saves your life' to 'slowly strangles you to death'" → "One
of them revives you from death and one of them strangles you, so don't
put an unknown amulet on without checking its curse status first."
L6673-6675 "which sounds niche until you reach ... Then it's
existential." L6833-6834 "The weight is negligible and the utility is
constant." → "It weighs almost nothing and you'll use it on every
level." L6857 "Music has power in the Mazes." (throat-clearing; open
with the passtune). L6937-6938 "A well-used marker can produce a
meaningful share of your ascension kit." (cut). L6610-6611 "The key
word is 'deliberately.'" (cut). L6686-6687 "which should tell you
everything you need to know about putting it on unexamined" → "and is
usually cursed, so it won't come off." L6613-6614 "paralysis is death
in the late game" → name the paralysers. L6618-6619 conflict "turns
your pets hostile" → "makes your pets attack you while it's on."
L6812 "in a BoH" → "in a bag of holding". L6868 "useful only for
confusing the issue" (dismissive, and wrong: horns and drums scare).

**The Armory.** L7345-7348 "how far away you strike, whether you can
also throw, how fast you swing per turn, which artifacts you can ever
hold" (quartet with a false item) → "Your weapon decides your reach,
whether you can throw it, and which artifacts you can hope for."
L7132-7133 "each anchor a defensive strategy"; L7220-7221 "each
redefine what your character can do" → plain lead-ins. L7105-7106
"real magic cancellation and often a defining intrinsic". L7444-7447
"no blood spilled, in the cleric flavor sense ... in the historical
sense" (invented reasons). L7618-7619 "the price Samurai pay for the
two-weapon flavor" (hollow, and Samurai reach Expert in short sword).
L7157 "dead weight for casters" (the penalty is 4 points). L7201
"Never wear", L7241 "Always altar-test" → "Altar-test boots and gloves
before wearing them." L7028 "Try armor before you wear it" → "Test".

**Curses / Spellcasting / Luck.** L7719-7720 "one of the dungeon's
quieter ways to kill you" → "and you can't take it off until you break
the curse." L7755 "free, instant, and should become instinct" → "It
costs nothing, so do it with everything you find." L7776-7777 "Simple,
reliable, and reason enough to stockpile holy water" → "This is the
main reason to hoard holy water." L7879-7880 "learn faster, fail less,
and have the widest range" ("learn faster" is not a mechanic).
L7998-8001 "every die roll, every prayer, every scroll, every combat
swing" (anaphora plus overclaim). L8006-8008 "the universe's way of
saying 'prove yourself' ... the Mazes don't give anything for free" →
"It starts at 0 and, left alone, drifts back toward 0." L8107-8108
"Luck feeds the game's luck-adjusted die" (implementation talk).
L8152-8153 "The vow of restraint pays in wisdom." (cut). L8159-8162 "a
small but real upgrade ... a small but real loss" (machine parallel).
L7764-7766 "that's a common spoiler myth" (meta).

**Enhancing Skills / Wishes.** L8288-8289 "gated by the dmg>1 roll"
(implementation talk) → "only the practice count skips the weakest
hits." L8290 "is why dedicating to a single weapon matters" → "is the
payoff for dedicating to a single weapon." L8452-8453 "Anyone else
dabbling in unarmed combat should plan to stop at Basic" (dismissive,
and Barbarians, Cave Dwellers, and Samurai reach Master). L8503-8504
"Also a very real chance of everything going wrong" → the number (a
throne wish is one sit in thirty-nine). L8531-8532 "when
overconfidence kills more adventurers than monsters do" → "(an extra
life for the Planes)".

**Artifacts.** L8695-8696 "usually accepted as sacrifice gifts rather
than spent wishes on" → "usually arrive as sacrifice gifts rather than
wishes." L8727 "huge in the early-to-mid game" → "a steady edge in the
early and middle game." L8693 "flavour" vs L8750 "flavor".

**Into Gehennom.** L9086-9087 "demons breathe fire as casually as you
breathe air" (no demon breathes fire) → "Fire traps are common and hell
hounds breathe fire; without fire resistance, go back up and get it."
L9100-9101 "Each fight is a major battle, several can summon
reinforcements, and all of them are angry you are here" (triplet).
L9133-9135 "Arch-Devil demons with the bribe disposition ... how
friendly your wallet looks" → "Only Asmodeus, Baalzebub, Geryon, and
Dispater take gold; the others attack on sight." L9144 "Those
artifacts refuse to talk and attack on sight" → "A prince who sees
either blade in your hand attacks at once, so sheathe it before you
approach." L9199 "killed off by his ambient aura" (invented). L9211
"dangerous not for raw combat power but because he never stops" → "His
attacks are survivable; the problem is that he keeps coming back."
L9240 "no longer any such thing as a safe turn". L9290-9291 "another
summoned monster, another stolen item, another cursed piece of gear" →
"While he lives he casts, summons, and steals."

**Rarely actionable tips the reviewers would cut:** L1685-1686
(training Strength while Stressed), L4016-4018 (Unchanging in golem
form), L3926-3928 (a tame purple worm under conflict), L4239-4240
(cancelling a green slime), L6978-6979 ("aim the crystal ball at the
most baffling level you've ever mapped"), L6603-6611 (aggravate
monster for sacrifice), L7180-7182 (helm of opposite alignment at the
Astral altar), L8043-8049 ("stair-up runs"), L8429-8432 ("cap-aware
investment", which says nothing to do), L9138-9139 (demon corpses for
sacrifice; they leave none), L9002-9003.

**Word-level habits worth a global search:** "the dungeon's
[superlative]" (19), "the single most" (7), "worth knowing" (8), "The
catch" (8), "one of the most" (10), "lifeline" (4), "the real prize"
(4), "genuinely" and "real" as intensifiers (L537, L1327, L3821,
L7105, L8503), sentence-initial "Never"/"Always" outside conduct
definitions (L2967, L4624, L5708, L6208, L6833, L7201, L7241, L8025,
L13422), and "the player" for "you" (L3256, L3281).

### Additional flags from the dedicated prose sweep

Four ranges reviewed before the "sounds like a person" rule was added
were swept again with that rule alone. The sweeps also named what
reads best, which is worth keeping in mind before editing: the
Excalibur routine (L1283-1294), the vault section (L1466-1482), the
Identification opener (L4758-4767) and its BUC jokes, the hunger opener
(L5628-5632), the holy-water pair (L5911-5925), the Wish Syntax bullets
(L8561-8595), and the Naming Sting and Orcrist paragraph are the voice
the rest of the book should sound like.

**Lay of the Land / Field Guide / Points of Interest (L853-1494).**
L886-897 says the same thing twice ("No two visits are quite the same.
And yet the dungeon follows patterns ... Knowing where you are in this
tree helps you know what's coming") → one opener: "The Mazes are laid
out fresh every game, but the branches, the special levels, and their
rough depths are the same, so you can always tell what is coming
next." L1016-1020 three sentences introducing themed rooms → "The
dungeon also has dozens of themed rooms, odd in shape (pillars, a room
inside a room) or in contents. Some to look out for:" L1033-1038
"traps in everything but name ... recognize the pattern, retreat,
prepare, return" (sermon) → "Treat these as traps. Spider nests and
buried zombies scale with depth, so back out and return with what the
room calls for." L1043-1046 "less predictable in a friendly way: more
terrain types to fight in, more item discovery, and the occasional
educational ambush" (designer triplet; cut). L1090 "the single most
common cause of death on the public server" → "on the first few levels
a pack of them kills more characters than anything else." Field Guide
rows that gesture instead of stating: L1089 "the math catches up fast"
→ "two 1d6 bites a turn wear a low-level character down faster than
the fight looks"; L1094 "until your AC is solid" → "A dwarf with a
mattock hits for 1d8 plus d12, enough to kill a first-level character
in two swings"; L1117 "you're in for a fight" → "Four 2d10 attacks a
turn, about 44 if all land"; L1126 "The fall does serious damage" →
"2d6 (iron piercers 3d6, glass 4d6), and you get no warning"; L1139
"a chance at cold resistance you can bank early" → "about one time in
three"; L1140 "a fair fight if geared up" → "Two 3d4 claws and a 3d6
bite each turn, but slow." L1275-1276 "a different gamble, and one
that Lawful characters should know by heart" → "is how a lawful
character gets Excalibur." L1283 "The conventional wisdom:" (cut).
L1299-1300 "the single most useful piece of furniture in the dungeon"
(cut). L1308-1310 "free, unlimited, and works on everything ... your
testing laboratory" → "It costs nothing and never runs out, so haul
every unknown piece of gear to the first altar you find before putting
it on." L1314 "deepens your relationship with your god" → "earns your
god's favor."

**A Practical Identification Strategy (L4752-5595).** L4793 "and those
opinions have consequences" (cut). L4807 "Blessed items are helpful
beyond their description, uncursed items work as advertised, and
cursed items find creative ways to ruin your day" → "A blessed item
does its job a little better than the uncursed version, and a cursed
one does it worse or backwards." L4895 "narrow down the possibilities
enormously" → "to a handful". L4908 "unfamiliar" and L4992
"pennypinching" name the same 1-in-4 surcharge; use one. L4956 closer
re-says the paragraph. L4983 "(deterministic per object ...)" →
"fixed for that item's whole life, so two stacks of the same appearance
quoting differently is the giveaway". L5034 "it's identify. Period.
That's one of the most useful scrolls in the game and you just found
it for free." → "it's identify; nothing else shares that price." L5036
"pure upside" → "safe to read too: enchant weapon or blank paper at
$60, enchant armor or remove curse at $80." L5086 "packed with
excellent potions" (cut). L5101 "extremely informative" → "Only four
rings cost $300, and three of them (conflict, polymorph control,
teleport control) are among the best in the game." L5346 "the best
payouts but two hidden traps" → "all worth having, but two of them are
awkward to test by drinking." L5418 "fall into informative tiers" →
"the price separates the safe boots and cloaks from the cursed ones."
L5468 "wildly different value" → "from a luckstone worth carrying all
game to a loadstone you can't put down." L5516 "Kick it first. Check
BUC second. Then pick it up." (staccato, and the pick-up test needs
picking up) → "So kick a gray stone, or let your pet walk over it,
before you lift it." L5544 restates the previous sentence (cut).
L5571 "Suddenly half your inventory is narrowed" → "Most of what you
carry drops to two or three candidates." L5590 restates the workflow
and the flowchart caption → "Cheapest method first; a scroll of
identify only for what's left."

**Provisions / Apothecary / Scrolls / Wands (L5596-6533).** L5790-5792
"the highest-density source of ascension-kit intrinsics in the game;
poison resistance ... the most important single intrinsic to bank" →
"A gelatinous cube can hand you fire, cold, shock, or sleep resistance
in one meal. Get poison resistance first, from the first spider or bee
you kill; without it, poisoned stings and arrows drain your Strength."
L5903-5908 speed (see above). L5962-5964 "individually low-value, but
the output is one of the catalysts that feeds the main healing chain"
→ "Both are common finds, and gain level is the ingredient the healing
chain keeps running out of." L6153-6155 "your role-self is an `@`" →
"because your role is itself an `@` species." L6164-6165 mind-flayer
feast under a cursed genocide (rarely actionable; cut). L6171-6172
"Gehennom's maddening mazes, where mapping by hand could take a
lifetime you don't have" → "Gehennom's mazes, which take hundreds of
turns to walk out by hand." L6362 death "One of the best offensive
tools in the late game" → "It does nothing to the undead or to
demons." L6365-6369 digging enumeration → "A zap at a wall opens a
passage. A zap at the floor drops you to the level below, the quickest
exit from a fight you're losing." L6401-6402 "Useful for slipping
through a dangerous area or turning a fight in your favor" → "Monsters
that can't see invisible have to guess where you are, and often swing
at empty air." L6494-6499 "one of the most interesting tools in the
game ... where the real fun begins" → "Self-polymorph puts you in
another monster's body. With polymorph control you choose which, and
that is when it becomes worth doing on purpose." Hollow closers to
cut: L5893 "You can never have too many of these."; L6116 "You will
never have enough of these."; L6110 "The bread and butter of dungeon
life."; L6119 "The path to endgame power."; L6373-6374 "Enormously
useful for escaping trouble..."; L6158 "Read carefully."; L6396-6397
"Risky but powerful."

**Enhancing Skills / Wishes / Artifacts (L8166-8914).** L8214-8215
"more practice, higher rank, more deadly swings" → "The game tracks
this as a skill rank." L8290 → "Going from Unskilled to Expert with one
weapon moves your to-hit by 7 and your damage by 4 on every blow."
L8443-8444 "come online to upgrade the late game without leaving the
early game starving" → "and school ranks can wait until you have
enough energy to cast often." L8488 "so persistence pays off" → "so
keep sitting until it does." L8513 "or commitment" → "Anything beyond
that is luck: extra lamps, fountain demons, a recharged wand." L8522
"the second pillar of not dying to wands" → "(reflection plus AC;
bounces wand rays and dragon breath back at the source)." L8693
"historically considered flavour pieces" and L8749-8750 "not the
flavor piece it used to be" → "Snickersnee and Sunsword gained new
powers in 5.0: a free reach attack each turn and an on-demand blinding
flash." L8699 "the drain resistance alone is worth carrying it, even
after you have a stronger weapon" contradicts L8811 (needs wielding).
L8848 "the Healer's salvation" (apposition; cut). L8852 "Few artifacts
change a role's late game as much as this one" → "With it a Healer can
hold a corridor in melee, which the role otherwise cannot." L8864 "a
powerful passive on a slot they can use" → "Monks fight without body
armor, so magic resistance that sits on the face fills a gap." L8871
"despite what older spoilers say", L8892 "despite the weapon's
reputation" (cut; state the fact). L8879 "this is the role's
centerpiece" → "A Ranger with the Longbow never runs out of arrows."
L8892-8893 closer restating the list (cut). L8901-8902 "the most
generous carried passive in the game" → "the strongest carry effect of
any quest artifact: it counts as a luckstone, grants warning, and
halves both spell and physical damage taken." L8911 "For a
spell-caster this is irreplaceable" → "Energy is what a Wizard runs
out of first, so the regeneration matters more than the portal."
## 6. Confirmed errors, chapter by chapter

Each entry: the claim as written, what the source says, and a proposed
fix where the reviewer offered one. Entries marked (sc) were
spot-checked by the collating editor.

### Choosing Your Expedition (L182-593)
- L539 orcs "Don't eat anything on the `o` letter (cannibalism)": orcs
  are exempt from the cannibalism penalty (`eat.c:51,770`). "You can
  even eat other orcs; your kind has no taboo against it."
- L540-542 orcs hated by "shopkeepers, priests, watchmen included":
  always-peaceful monsters stay peaceful (`makemon.c:2272-2286`,
  `shknam.c:666`, `priest.c:253`).
- L414-416 Rogue "coat your blades and darts ... a thrown dagger
  leaves venom": only arrows, bolts, darts, and shuriken take poison
  (`obj.h:264-268`); Rogues start with daggers.
- L510 humans "nobody singles you out": gnomes and orcs are always
  hostile to humans (`role.c:595`, `makemon.c:2285`), which is why the
  Mines treat gnomes and dwarves better.
- L361 Monk "Heavy body armor wrecks your aim": any body armor, a flat
  20 to-hit (`uhitm.c:397-399`).
- L378-379 Priest "Your first worthy sacrifice is guaranteed to return
  Demonbane": the gift is one worthy offering in six
  (`pray.c:1781-1792`); what is guaranteed is that the first gift is
  Demonbane, for any alignment (`artifact.c:87-95, 208-217`) (sc).
- L466-468 Mjollnir "flies back to your hand when you hurl it":
  throwing it needs Strength 25 (`dothrow.c:127-129`).
- L571-572 "Chaotic is often paired with Rogue for thematic
  consistency": Rogues are always Chaotic (`role.c:342`).
- L574 "Valkyrie, Human or Dwarf" under Lawful or Neutral: dwarves are
  Lawful only (`role.c:632`).
- L385 "Do not anger shopkeepers or break mirrors" (under Luck):
  angering a shopkeeper costs no Luck; killing a peaceful does
  (`mon.c:3649-3665`).
- L569-570 Chaotic "can kill with relative impunity": killing a
  peaceful costs every alignment 5 points (`mon.c:3721-3722`); no
  mechanic punishes piety.
- L298 Cave Dweller "the weakest spell access": the Barbarian's is
  worse (`role.c:106,147`). "among the weakest".

### What to Pack / Your First Descent (L594-852)
- L642-643 silver "against demons, undead, and lycanthropes": silver
  hurts werecreatures, vampires, demons, shades, and imps only
  (`mondata.c:524-528`); zombies, mummies, wraiths, and liches ignore
  it.
- L808-811 stair tumble with "a cockatrice corpse": only a *wielded*
  corpse stones you (`do.c:1796`, `trap.c:3888`) (sc); one in the pack
  is harmless.
- L753-756 alignment grind on "always-hostile classes (fungi, oozes,
  insects)": those are neutral, so a neutral hero gains nothing
  (`makemon.c:2352-2357`); neutrals should hunt kobolds and orcs.
- L747-749 Rule 4 prayer: negative Luck also fails prayer
  (`pray.c:2155`); the timeout starts at 300 and must fall to 200
  before a life-threatening prayer works, so no prayer in the first
  hundred turns (`u_init.c:1005`, `pray.c:2151`); recovery averages
  about 500 turns, not 1000 (see section 4, item 2).
- L842-843 "`#force` it with a weapon you don't mind breaking": a blade
  snaps 0.8% per try; a blunt weapon never breaks but one success in
  three smashes the box and every potion in it (`lock.c:186,228-252`),
  and half these chests hold healing. "Pry with a dagger, not a mace."
- L813-814 jackal packs "two to four": pairs until XL 5
  (`makemon.c:85-114`).
- L785-786 shift-running "yields control the instant something
  warrants your attention": it stops only for a monster ahead or one
  that hits you and walks past items and doors; `G` stops beside any
  monster, item, or door (`hack.c:3933-4011`, `cmd.c:1615`).
- L615 pets "won't step on cursed items": reluctant, not never
  (`dogmove.c:1237`), as L4602 says.
- L840-841 "On your first ten levels": supply chests appear only above
  the Oracle (`mklev.c:1036`).
- L792-793 "If you're Fainting, pray": Weak already qualifies
  (`pray.c:216-217`), as L5811 says.

### The Lay of the Land / Field Guide (L853-1170)
- L1027-1029 Massacre rooms "useful for sacrifice and for eating the
  safe ones for intrinsics": every corpse there is a human adventurer
  (`themerms.lua:173-189`); a human hero eating one is cannibalism, a
  non-chaotic offering one is the "infamous offense"
  (`pray.c:1698-1771`); none conveys anything.
- L1122 mummies "corpses dangerous to eat (age you)": no aging
  mechanic; the corpse is already rotten (`mon.c:629-645`) (sc).
- L1097 kobolds "sometimes carry poisoned weapons": 1 in 100 darts;
  the fact that matters is that kobold corpses are poisonous.
- L1133 horses "mostly peaceful in the wild": hostile to lawfuls and
  chaotics, half peaceful to neutrals (`makemon.c:2290-2307`).
- L1004-1006 zoo sleepers wake "from the noise of you fighting": each
  wakes with a 1-in-7 chance per turn you are in view within ten
  squares, unless you have Stealth (`monmove.c:327-357`).
- L929 "`#` Corridor or fog": corridor, tree, or cloud; fog clouds are
  `v`.
- Minor: all vampires fly (L1150); xorns pass walls, not floors
  (L1152); a worm tail hit cuts 20% (50% blade) and the piece usually
  becomes a second worm (L1165).

### Points of Interest (L1171-1494)
- L1245-1246 magic fountain "raises a random attribute by one": at Luck
  4 or better every attribute rises (`fountain.c:255-271`) (sc).
- L1241-1243 "If you don't have bad luck, about one in seven is a magic
  fountain": one in seven is placement regardless of Luck; Luck gates
  the drink.
- L1247-1249 "sink-kicked fountains": kicking a sink never makes a
  fountain; polymorph or a broken pipe does.
- L1266 quoted messages: "The cool draught refreshes you." / "This
  tepid water is tasteless." (`fountain.c:280,384`).
- L1314-1315 "stale sacrifices are an insult": a stale corpse does
  nothing, no penalty (`pray.c:1843-1848, 2010-2014`).
- L1317-1319 cross-aligned sacrifice "the alignment penalty is steep":
  it is 3; the cost is an angry god who smites at once.
- L1322-1328 altar conversion "a chance of doing nothing, and a chance
  of backfiring (you get converted)": no "nothing" outcome; a negative
  alignment converts you outright; otherwise `rn2(8+XL) > 5` flips the
  altar (+1 Luck) or fails (−1), either can summon a minion
  (`pray.c:1637-1694`). L4512-4517 already says this correctly.
- L1340 throne "Genocide of a monster class": a single species
  (`sit.c:131`).
- L1347 throne "A curse on one of your items": up to six items at Luck
  0 or less; at positive Luck a long blindness and lost Luck instead
  (`sit.c:139-143`) (sc).
- L1355-1356 throne wish "needs your luck to be non-negative": at Luck
  −1 the wish still comes 4 times in 5 (`sit.c:106`).
- L1359-1362 throne kick "dislodges 300-500 gold and gems": one kick
  in three, once per throne; a quarter of the rest drop you through a
  trap door (`dokick.c:1035-1063`).
- L1387-1389 sink ring "gone nineteen times out of twenty": one in
  twenty comes back, and one in five of the rest is buried under the
  sink for a pick-axe (`do.c:649-660`) (sc).
- L1409 sink message inverted: "The sink vanishes." means it moved
  (`do.c:575-580`).
- L1427 sink potion "pours out to drink": it is drunk for you.
- L1451-1452 sink vapors: hallucination gives only a "momentary
  vision"; sleeping and paralysis leave you helpless 1-5 turns.
- L1490 Archeologists "see historic statues by name": the word
  "historic" appears in the name.
- Missing throne outcome: teleport, or with bad luck every monster
  roused (`sit.c:185-193`).

### Branches and Landmarks (L1495-2028)
- L1962-1966 "with a cockatrice corpse you can kill Medusa ... bypasses
  the reflection requirement": Medusa resists stoning
  (`monsters.h:2842`). A wand of death or finger of death works.
- L1942 "`#loot` him" (Perseus): statues give up contents only when
  broken (force bolt, striking, pick-axe).
- L1959-1961 mirror "you need to be adjacent": it reaches down a
  straight line like a wand; the real condition is that she is awake,
  and every layout generates her asleep (`apply.c:1096-1115`,
  `medusa-*.lua`).
- L1670-1672 Sokoban penalty "clears the moment you legitimately finish
  the level above": no such mechanic; Luck drifts back a point per 600
  turns (`timeout.c:606-619`), frozen by a luckstone.
- L1557-1559 mind flayer "outside Minetown and Mine's End": Mine's End
  rolls one too (`minend-*.lua`).
- L1553-1554 "If you're playing a gnomish character": dwarves get the
  same peace (`role.c:634,654`).
- L1572-1574 Minetown donation "at least the amount the priest names
  ... a point of protection": the larger of two amounts; 2-4 points
  the first time (`priest.c:645-699`), as L4462 says.
- L1812-1817 Quest refusal "climb back out, mend your standing, and
  return": you are expelled automatically; below XL 14 the same; a hero
  who changed alignment is banished for good (`quest.c:333-353`).
- L1978-1980 "Ice is safe to walk on": every other step slips for two
  helpless turns (`hack.c:2396-2411`), and zapped ice melts again.

### Traps and Hazards / Feelings and Sounds (L2029-2666)
- L2646 "monsters have difficulty pinpointing your location ...
  Stealth just turned on": that message is the cloak of displacement
  toggling (`do_wear.c:148-176`).
- L2647 killing your pet "−15 alignment and your god is now angry.
  Expect prayer to backfire": −15 alignment and −1 Luck, no anger
  (`mon.c:3664-3708`); prayer fails until the record is back above
  zero.
- L2183 magic trap "uncurses your whole inventory": worn and wielded
  items only (`trap.c:4430-4443`).
- L2177 "Sleep resistance (elven blood, the right ring)": no ring
  grants it; elves, orange dragon armor, corpses.
- L2363-2366 scratched engraving "Monster traffic doesn't smudge it ...
  lasts indefinitely": every monster step chips it one time in 26
  (`monmove.c:734`, `engrave.c:280-288`).
- L2352 "'Elbereth' costs about −4" of a blade: dulling stops at −3,
  so a +0 blade runs out a letter short ("Elberet"); +1 or better
  finishes the word (`engrave.c:1355-1380`).
- L2194-2197 teleport trap "press `Ctrl+T` first": `Ctrl+T` fires only
  a discovered trap you are standing on (`teleport.c:1041-1060`).
- L2616 digging sound "gnome miner": gnomes don't tunnel; dwarves,
  rock moles, umber hulks.
- L2642 "It tasted bad." row: unreachable; the can't-rise message is
  "You have an uneasy feeling." (`potion.c:1092-1107`).
- L2650 "summoned a monster" attributed to "wizard, demon, lich": that
  message is the priestly insect/snake summons (`mcastu.c:685-697`);
  mage summoning prints "Monsters appear from nowhere!"
- L2653 "just left your awareness": printed by a wand of secret door
  detection clearing an `I` marker (`zap.c:2557`).
- Quoted messages that don't match the source: L2654 (ends with a
  period), L2660 ("a green slime"), L2617 ("You hear a rumbling stop
  abruptly."), L2395 ("ad aerarium", lowercase and aged five
  characters at creation).
- L2632 "Eye of newt corpse": a plain newt corpse.
- L2300 "Rangers have the Searching skill from the start":
  Archeologists too, and it is an intrinsic.
- L2245-2246 levitation "still trigger magic, teleport, and anti-magic
  traps": also polymorph, level teleport, and webs
  (`trap.c:1061-1080`).
- L2050-2052, L2244, L2255 pets "hesitate to step on traps it knows
  about": pets avoid only traps *you* have already found
  (`dogmove.c:1195-1207`), so watching them reveals nothing. Cut all
  three.

### The Art of Combat (L2667-3100)
- L2716 to-hit "roll at or above (10 + defender's AC − your
  modifiers)": backwards, and there is no 10. The sum is 1 + level +
  Str/Dex bonus + Luck/3 + enchantment and skill + target AC, and you
  hit when a d20 rolls under it (`uhitm.c:376-378, 780-781`) (sc).
- L2755 "At AC −20, almost nothing hits you": negative AC is rolled
  each attack and the monster's level adds to its chance; an ogre
  connects one swing in four, a level-15 monster two in three
  (`hack.h:1538`, `mhitu.c:709-710`).
- L2767 "Protection bought from priests of your alignment": no
  alignment test (`priest.c:681-699`); the book's own L4460 says so.
- L2836 Overtaxed "~1.5": it is 2 (`allmain.c:149`).
- L2839 "At Stressed, a speed-6 zombie acts more often than you": a
  tie; at Strained it acts twice per move.
- L2883 "Rangers stay unskilled (−9)": Rangers, Healers, Monks, and
  Wizards cannot two-weapon at all (`wield.c:765-771`).
- L2902 "a cursed weapon in either hand jams the whole arrangement":
  only the off-hand, and it slips to the floor (`wield.c:797-800`).
- L2945-2949 multishot: Skilled +1, Expert +2, and the count is a
  random 1 to max, so an Expert Ranger averages about 2.5
  (`dothrow.c:177-233`).
- L2989 "ordinary monsters cannot follow you up or down [stairs]":
  adjacent stalkers do: soldiers, watchmen, vampires, trolls, wraiths,
  imps (`mondata.c:1224`).
- L3003 jumping boots "(use `a`)": the command is `#jump`.
- L3029 "Sleeping monsters stay asleep while you walk past them":
  1-in-7 per turn to wake in view; dogs and humans at once; Stealth
  prevents it (`monmove.c:341-352`).
- L3096-3097 caitiff "can lock a Knight or Samurai out of the Quest for
  the rest of the run": −1 each, and the record climbs back with
  hostile kills (`uhitm.c:341,345`, `mon.c:3725`).

### Things That Will Kill You (L3101-3650)
- L3191-3193 sleep resistance from "the Wizard's cloak of MR, the
  Ranger's elven cloak": neither cloak grants it (`objects.h:616,
  644`) (sc); elves get it at experience level 4.
- L3443-3444 "Wands of cold and fire kill puddings": brown and black
  puddings resist cold (`monsters.h:2097, 2118`).
- L3232-3233 water demon "attack first and grant a wish only if you
  survive": the roll is made at summoning; a grateful demon grants the
  wish at once and vanishes (`fountain.c:78-84`).
- L3250-3251 demon summoning "every melee hit ... 1-in-13": once per
  attack round, 1 in 16 outside Gehennom and 1 in 10 inside
  (`mhitu.c:733, 966-969`).
- L3256 "sorted roughly by frequency on the public server" and L3292
  "Killed by your own wand": alt.org ranks mount slips 13th, rotted
  corpses 17th, shopkeepers 19th; "zapped herself with a wand" is
  109th, while "killed by a wand" (12th) is a monster zapping striking
  at you. Drop the frequency claim and re-aim the wand entry.
- L3277 pony "coin flip at experience level 2": a fresh pet slips 9
  times in 20, a barely tame one about 17 in 20 (`steed.c:308-341`).
- L3284-3286 Gehennom "shatters any potion you drop ... shrapnel is
  deadly": hot floors break about half of dropped potions harmlessly;
  the "boiling potion" death is fire reaching your pack
  (`do.c:318-353`, `zap.c:5781`).
- L3302-3304 "Kicking doors can break your toe": a failed door kick is
  a harmless "Whammm"; walls hurt (`dokick.c:889-966`).
- L3335-3338 nymph "one claw lifts an item, the other peels a worn
  ring": both claws steal the same way (`uhitm.c:4756-4799`).
- L3414 "a werewolf destroys your body armor, cloak, and shirt": the
  cloak drops intact (`polyself.c:1188-1192`).
- L3441 "athame" among silver and wooden weapons: it is iron.
- L3460-3461 pudding globs "each bite is an independent roll": one
  roll per finished glob, and globs merge.
- L3490 "Yellow dragons are rare": every dragon is equally common.
- L3516 dragonhide "resist disenchantment naturally": no exemption
  (`zap.c:1382-1394`); it never rusts, corrodes, or burns.
- L3534-3535 troll corpse "wand of teleportation ... off-level, or
  destroy it with a wand of striking": teleport moves it on the same
  level; striking breaks only glass-like objects. Cut both.
- L3554-3555 level drain "stat points ... no easy undo": you lose max
  HP, energy, and a skill slot, no attributes, and a potion of restore
  ability gives the levels back (`exper.c:227-278`, `potion.c:687`).
- L3563 "Wraith corpses spoil quickly": ordinary rot.
- L3529 "the same five trolls": about three in four revive.
- L3242 minotaurs: missing the fact that they ignore Elbereth
  (`monmove.c:284-287`).

### Saving and Bones / Ways to Die Instantly (L3651-4277)
- L4257-4258 lava "without levitation or fire resistance gives you a
  few turns": without fire resistance you burn to death on contact and
  your pack burns first; *with* it you sink, with a dozen turns to get
  out (`trap.c:6811-7016`) (sc).
- L4247-4248 food-poisoning cure "or vomit (by being satiated and
  eating more)": that is the choking death (`eat.c:258-267`). The cures
  are a non-cursed extra or full healing, or a blessed healing.
- L4264-4265 drowning "a few turns to escape": the next landed wrap
  drowns you (`uhitm.c:3389-3396`), as L3945 says.
- L4272 strangulation "slowly kills you": six turns
  (`do_wear.c:1040`).
- L3715-3717 bones "80% cursed, even items in containers": containers
  are untouched (`bones.c:274-300`).
- L3696-3698 bones levels: Quest filler levels can leave bones; none of
  Vlad's can (`dungeon.lua:196-283`).
- L3702-3704 "This place looks familiar": only for your own past
  character; the overview lists "Final resting place for..."
- L3999-4000 acid blobs "a few hundred turns of resistance": one in
  six, 3-18 turns (`eat.c:994-1094`).
- L4029-4030 cockatrice corpse "handles demon lords, Medusa, and even a
  Rider": Medusa and the Riders resist stoning.
- L3912-3914 "Dragons ... can swallow": no dragon engulfs; purple
  worms digest, vortices and fog clouds only hurt.
- L3782-3786 warning shot: monsters native to the Castle, Ludios, the
  Quest, Gehennom, Vlad's, and the Planes never miss the first shot
  (`makemon.c:1291`, `muse.c:1830`).
- L3892-3894 mind blast "only fires if you have telepathy": locks on
  every time when sensed by telepathy, one in ten otherwise
  (`monmove.c:599-601`).
- L4180-4181 touch of death "Magic resistance fully blocks this
  branch": it drops to the smaller drain; outright death only if half
  the damage reaches your max HP (`uhitm.c:3862-3872`,
  `mcastu.c:326-352`).
- L3845-3846 system shock "10 to 34": 10-30, and it kills whenever
  current HP is at or below the roll (`attrib.c:365-366`).
- L4062-4064 disintegration "then your body armor": the cloak goes with
  it (`zap.c:4480-4485`).
- L4231-4232 "digested by [green slime] as a polyform": no such thing.

### Divine Relations / Making Friends (L4278-4751)
- L4438-4446 "The first gift is biased toward ... your role's
  signature artifact ... Sacrifice early to lock in that bias before
  the random pool dilutes it": for Valkyries, Wizards, Barbarians,
  Samurai, and Priests the role's artifact is the *only* first-gift
  candidate, exempt from the sacrifice-value cap, and it takes your
  alignment (`artifact.c:92-95, 195, 212-216`) (sc). The "lock in the
  bias" reason is invented.
- L4444-4446 "Worthiness floor ... a kobold corpse can roll for a gift
  but nothing interesting will come of it": the concrete 5.0 rule is
  that an artifact is on the table only if the corpse's difficulty
  plus one reaches the artifact's worth (1 to 10; Sting, Ogresmasher,
  Trollsbane 1; Vorpal Blade and Fire Brand 5; Frost Brand 9;
  Grayswandir 10), so the endgame weapons need a troll-class corpse
  (`pray.c:1845`, `artifact.c:195`, `artilist.h`) (sc).
- L4433-4434 "second gift is more like 1 in 16 to 1 in 26": the odds
  are 1 in (6 + 2 × gifts × artifacts in existence) (`pray.c:1792`),
  so 1 in 8 with only your first gift in play.
- L4413-4416 "your god expects more impressive offerings as you
  advance ... 'feeling of inadequacy'": nothing scales with level;
  the message fires only when your god is angry and the corpse is too
  small to help (`pray.c:1959-2060`).
- L4404-4405 sacrifice "pays out as ... holy water ... and eventually a
  crown": those come from praying on the altar, not sacrificing.
- L4500-4503 priest "decline the prompt entirely rather than offering
  a token sum": declining is an offer of zero, which costs a point of
  alignment and counts as cheapskate (`priest.c:655-659`,
  `minion.c:376`).
- L4477-4478 "politely thanked but not blessed": a rich hero offering
  the base amount is called Cheapskate (`priest.c:660-664`).
- L4457-4459 "A few hundred turns" of clairvoyance: 500-999 per
  suggested amount (`priest.c:673`).
- L4514-4515 altar conversion "if your god is already angry, converts
  you": the test is a negative alignment record.
- L4519-4522 "a pair of hostile minions": one, and only past
  experience level 8 (`pray.c:1680-1694`).
- L4539-4548 crowning "if one is available": a Lawful gets no sword
  unless wielding a long sword; Wizards and Monks get the spellbook
  instead (`pray.c:822-956`).
- L4550 crowning "adds ~1000 turns": every later prayer adds about
  1000 turns of timeout (`pray.c:1356-1361`).
- L4396-4397 "Spellcasters get the same from the turn undead spell": a
  directional bolt that scares one undead, and it works in Gehennom.
- L4614-4616 tameness "decreases when they go hungry": hunger never
  touches tameness; separation, your own blows, and leash-dragging do
  (`dog.c:689-696, 899, 1360`).
- L4726-4728 "Sokoban also doesn't let pet loyalty decay": no such
  exemption.
- L4656-4658 purple worm "growing tail": long worms have the tail.
- L4718-4719 farlook for pet health: compiled out; use a stethoscope.
- L4739 pets "better-armored" from eating: resistances only.
- L4609 message is "steps reluctantly onto".

### A Practical Identification Strategy (L4752-5595)
- L5059 "$100 spellbooks: flame sphere, freeze sphere": neither exists
  in 5.0 (`objects.h:1413-1422`, `#if 0`).
- L4796-4798, L4844-4846 "A blessed scroll identifies at least 2
  items": one to four, or everything one time in five; the minimum
  becomes two only with positive Luck; an uncursed scroll rolls the
  blessed table one read in five (`read.c:2084-2092`).
- L4840-4841 holy water "praying on a co-aligned altar while carrying
  potions of water": the water must be on the altar
  (`pray.c:1393-1400`).
- L4832-4835 autocurse list: only the helm of opposite alignment and
  dunce cap curse themselves on wear (`do_wear.c:462-482`); fumbling
  gauntlets and levitation boots are merely usually cursed, which the
  tests catch.
- L5043-5047 closet tip "behind a door or in a niche ... the level's
  teleport-trap clue": the scroll is placed only in a doorless sealed
  niche (`mklev.c:777-795`) (sc); the reason is invented. "A single
  scroll sealed in a one-square closet with no door (sometimes behind
  iron bars) is a scroll of teleportation, left so anyone who lands in
  there can leave."
- L5327 poisonable "or sling stones": no (`obj.h:264-268`).
- L5347 levitation "a few hundred turns": 10-149 uncursed; 250-299
  blessed, with `>` to come down (`potion.c:1208-1215`).
- L5494-5495 "$60 gray stone is a luckstone": a surcharged touchstone
  quotes $60 too; $45 is a touchstone for certain (`shk.c:2864-2944`).
- L4915-4917 what angers a shopkeeper: not "a wand fired from a
  doorway" or "picking up an unpaid item while broke"; attacking,
  zapping a wand at them, leaving with unpaid goods, or refusing to pay
  for damage (`mon.c:4355`, `zap.c:555`, `shk.c:3868,5170`).
- L4878-4880 the throw-into-shop quote trick: no quote from outside,
  and the shopkeeper pockets it. Stand on the item and press `:`, or
  `#chat` (`invent.c:4282`, `sounds.c:1280`).
- L5263 "Drop the wand on an aligned altar, hand it to a priest": any
  altar flashes; no handing to priests.

### Provisions and Dining / The Apothecary (L5596-6025)
- L5732-5735, L5760 cats and dogs "eat freely / plain": kitten,
  housecat, large cat, little dog, dog, large dog give permanent
  aggravate monster unless you are a Cave Dweller or orc
  (`eat.c:814-826`) (sc).
- L5734 leprechauns and nymphs "no effect": teleportitis, one in two
  from a leprechaun, about one in three from a nymph
  (`eat.c:936-988`) (sc).
- L5773 "Stalker → invisibility + see invisible": eaten while visible,
  a short invisibility and a stun; permanent plus see invisible only if
  already invisible (`eat.c:1162-1178`).
- L5764 "`i` ... mostly no corpse": imp, homunculus, quasit, and tengu
  all leave corpses; homunculus is poisonous and conveys sleep and
  poison resistance; tengu conveys teleportitis or control.
- L6010-6012 "Eating a lizard or acidic corpse also cures it" (under
  Sickness): they cure stoning, not sickness (`eat.c:827-861`); the
  only food cure for sickness is a eucalyptus leaf.
- L5873 enlightenment "blessed tells more": same readout; blessed adds
  +1 Int and +1 Wis (`potion.c:802-806`).
- L5858 see invisible "permanent when blessed": one time in ten
  (`potion.c:844-870`); booze and fruit juice share the $50 price.
- L5682 lembas "Elven characters find these more often": no; elves get
  a quarter more nutrition, orcs a quarter less (`eat.c:345-349`).
- L5983-5984 alchemy "The dipping potion is the one that breaks": the
  target is always used up and a blast takes both; the dipped potion's
  curse triggers it (`potion.c:2419-2538`).
- L5923 fountain dipping "where you stand safely": every dip rolls the
  fountain table and dries it one time in three, as L1282 says.
- L5911-5913 "pray, and the gods bless it": only a *successful* prayer,
  with the water on the altar (`pray.c:1393, 2334`).
- L5803-5804 pudding globs "a re-rollable chance": globs merge into one
  glob and a glob is one meal and one roll (`do.c:303-314`,
  `eat.c:562`); eat them one at a time off the floor.

### The Scroll Rack / Wands (L6026-6533)
- L6226-6228 confused remove curse "makes holy water from carried
  water": only a *blessed* scroll reaches carried items; unblessed
  touches worn and wielded only (`read.c:1549-1557`) (sc).
- L6086 enchant weapon "above +6": at +6 and up (`wield.c:999`).
- L6338 wand of wishing "Max Charges 3": generated with 1
  (`mkobj.c:1116`); recharge adds one.
- L6325 wand of stasis "15": 3-6 when found; 15 is the recharge cap.
- L6400-6401 make invisible "31-45 turns": that is self only; a zapped
  monster stays invisible for good (`zap.c:357,2836`).
- L6509-6511 polymorph "your current HP scales with the ratio ...
  wakes up at 200/400": the new form rolls its own full HP (a titan
  16d8) and your own HP waits underneath (`polyself.c:866-872`).
- L6518 "cursed polymorph items strip control": no such check; the real
  caveat is a failed Con roll costing up to 30 HP without control.
- L6471 wresting "a few tries": one in 121 per zap (`hack.h:1411`).
- L6481-6483 charging rings "+0 or +1 virtually free ... cap around
  +5": explodes when `spe > rn2(7)`: +1 one in seven, +3 about 43%, +7
  always (`read.c:807`).
- L6191, L6205 scare monster / teleport "any square you can see": also
  within about five squares (`read.c:1080-1085`).
- L6093 create monster "confused or cursed makes several": thirteen;
  confused makes acid blobs.
- L6506 "brown mold form burns": freezes.

### Rings and Amulets / Tools (L6534-6989)
- L6632-6636 the two-hands ring-juggling hunger trick: 5.0 randomized
  the trigger to kill it (`eat.c:3181-3191`). Cut.
- L6628-6629 "Two rings drain food noticeably faster": a ring costs one
  nutrition per twenty turns; regeneration, conflict, and hunger ten
  times that (`eat.c:3192-3266`).
- L6682-6683 "Stack with speed boots on the mount": steeds wear no
  boots and your speed does not add to theirs (`allmain.c:119`).
- L6762 bag explosion "scatters your inventory": scatters the bag's
  contents, loses about one in thirteen, and does 6d6 to you
  (`pickup.c:2515-2692`).
- L6796-6797 bag of holding "roughly a quarter": blessed only;
  uncursed halves, cursed doubles (`mkobj.c:1950-1953`).
- L6792 Overloaded "can't pick anything else up": can't move
  (`hack.c:2629`).
- L6817-6823 monsters "unlock chests with keys ... the Castle chest can
  be emptied": they refuse locked containers (`muse.c:2273`) (sc).
- L6847-6849 "Never, ever use a magic lamp for light": a lit magic lamp
  never burns down and still answers to rubbing (`timeout.c:1722`,
  `apply.c:1815`) (sc).
- L6867-6868 non-magical instruments "no special effects": a tooled
  horn or leather drum wakes and scares nearby monsters; the drum
  deafens you 30-49 turns (`music.c:639-721`).
- L6916-6918 magic marker "writing by appearance gives a random scroll":
  writing by label gives exactly that scroll once you have seen the
  label (`write.c:165-168, 313-316`).
- L6949-6950 "grind poison or acid resistance": acid resistance from
  corpses is timed (3-18 turns), as L13868 says.
- L6958-6959 "most of Gehennom is non-diggable": the filler mazes dig
  fine; only the Valley floor, Sanctum, and the two towers refuse
  (`hellfill.lua`, `valley.lua:10`).
- L6964-6965 crystal ball "point at a square or `.` for the whole
  level": you name a symbol and it scans the whole level
  (`detect.c:1298`).
- L6977 "Drop a fresh ball on an altar to bless it": altars reveal,
  holy water blesses.
- L6982-6984 grease "nymphs slide off, Riders' grabs miss, weapon-snatch
  fails": grease defeats hugs, wraps, sticky attacks, and mind-flayer
  tentacles only (`mhitu.c:1047-1085`); the same error at L8564.
- L6934-6935 charging a wand of wishing "a blessed one restores one
  additional wish": uncursed does too (`read.c:737-779`).
- L6658 life saving "(any kind of death)": not genocide, and it costs a
  point of Constitution (`end.c:1081-1096`).

### The Armory (L6990-7695)
- L7645-7647 enchant weapon "no destruction limit at all ... never
  lost": two in three evaporate at +6 and up (`wield.c:999`) (sc).
- L7250, L7264-7267 "the large shields exclude two-handed weapons": any
  shield does (`wield.c:186`) (sc).
- L7251-7252 vs L7261-7262 shield casting penalty: every shield adds a
  flat penalty, heavier ones far more (`spell.c:2196-2274`).
- L7065-7066 mithril "much smaller than plate's" casting penalty: every
  metallic suit pays the same; a robe halves it (`spell.c:2191`).
- L7422 quarterstaff "the only two-hander with no spellcasting
  penalty": no weapon carries one; the quarterstaff gives a small
  bonus (`spell.c:2199`).
- L7285-7287, L7304-7309 magic cancellation from Protection "+1 per
  source": bought Protection lifts MC0 to MC1 only; a ring or cloak of
  protection adds +1 (amulet of guarding +2), once
  (`mhitu.c:1121-1135`).
- L7292-7293, L7316-7317 what MC blocks: not cockatrice touch, brain
  suck (a helmet blocks it 7 in 8), gazes, or breath; it negates level
  drain, poison, paralysis, sleep, slow, confusion, stun, lycanthropy,
  disease, sliming, and teleport touch.
- L7159-7160 fedora "base item for the Eye of the Aethiopica, the
  Priest quest artifact": the Eye is the Wizard's amulet; an
  Archeologist in a fedora gets +1 Luck (`timeout.c:603`) (sc).
- L7175-7176 helm of telepathy "requires actively blinding yourself":
  worn telepathy shows minds within eight squares with eyes open.
- L7229-7231 jumping boots "as an `a` (apply) ability": `#jump`.
- L7252-7253 Monk shield "zeros Martial Arts": costs the martial-arts
  to-hit bonus (`uhitm.c:397-401`).
- L7474-7476, L7564-7566 grappling hook "yank a target into melee
  range", "4 squares (8 at Expert)": polearm reach (two squares); pulls
  only very small monsters, snags objects, or drags you a step
  (`apply.c:3826-3860`).
- L7580-7581 bows "Rangers, Samurai, and Rogues reach Expert": Rogues
  cannot use bows.
- L7600 "Shuriken (Samurai get +1 multishot)": Monks do
  (`dothrow.c:53-56`).
- L7624 "silver short sword": no such item.
- L7238-7239 fumbling "every other turn ... dropping your weapon": a
  trip every 1-20 turns costing two turns; nothing drops.
- L7247-7249 shields "block rays you can't see": no such mechanic.
- L7481-7482 Mjollnir "returns when thrown while wielded": Valkyries
  only, Strength 25.
- L7107-7109 shopkeeper "fingerprints your suit": unsupported.
- L7166-7167 dunce cap "cannot be BUC-tested": it can; price tells it
  apart (80 vs 1 zm).
- L7644-7645 enchant armor "+1 (uncursed)": 1-2, more on plain armor
  (`read.c:1194-1218`); and a confused *cursed* scroll strips proofing
  (L7660 should say non-cursed).

### Curses / Spellcasting / Luck / Exercising (L7696-8165)
- L7778-7780 "A pleased god uncurses your worn items": off an altar a
  prayer fixes at most the worst trouble; cursed gear is minor, fixed
  one item at a time, only when nothing worse is wrong and Luck is
  positive (`pray.c:1126-1157`) (sc). Cursed levitation, a welded weapon
  with no free hand, and a cursed blindfold are major.
- L8110-8115 "Even one point of negative Luck causes prayer to backfire
  ... stat loss ... black glow ... bolts": at Luck −1 or −2 with no
  anger the only result is "displeased" and a reset timer
  (`pray.c:715-782`); "Scrolls will backfire" is false.
- L7867-7875 reading table "Minimum Int + XL": the formula counts XL at
  half weight and costs 2 per spell level (`spell.c:582-584`): 14, 16,
  18, 20, 22, 24, 26.
- L7837 book failure "randomly curse one of your items": unreachable.
- L7884-7885 "body armor adds a failure penalty": metallic only.
- L7924 detect monsters "Sense nearby monsters": the whole level.
- L7932 "The other 34 spells": 32.
- L8026 luckstone "bless it on an altar": holy water blesses.
- L8033-8036 cursed luckstone "partially offsetting": with one other
  non-cursed luck item the sum is zero and the full +3 applies
  (`attrib.c:428-448`).
- L8061 "Sitting on a throne (lucky outcome) +1": only while Luck is
  negative; otherwise that result is a wish.
- L8091 "a pile of kobold corpses" for Luck: gain scales with corpse
  difficulty; kobolds give nothing.
- L8158 "Wis for prayer success": prayer never checks Wisdom.

### Enhancing Skills / Wishes and Wishing (L8166-8598)
- L8479 wand of wishing "found in the Castle treasure room": in one of
  the four corner towers (`castle.lua:142-147`); the book's Castle
  chapter says so.
- L8564 "`greased` deflects nymph theft and Rider grabs": see Tools.
- L8297 "identify IDs the whole stack" at Skilled: acts as a blessed
  scroll (several items, sometimes all).
- L8509-8511 "about four wishes": about five, counting the wand's
  wrested charge.
- L8265-8266 "You feel more confident in your skills": the message
  names the category (`weapon.c:78-82`).
- L8534-8535 "silver damage against everything in Gehennom": silver
  bites demons, imps, vampires, weres, and shades.
- L8419 "Thirty slots" vs L8234 "32".

### Artifacts (L8599-8914)
- L8805 "`#invoke` (default `^A`) ... for an energy cost": the key is
  `M-i`; invoking is free and then the artifact ignores you for about a
  hundred turns; only Sunsword and Grimtooth can pay 25 Pw to fire
  during the cooldown (`artifact.c:2091-2127`) (sc).
- L8756 "50 Pw per invocation"; L8758 "up or down lights the room": no
  cost when rested; up or down lights your own square.
- L8824, L8903-8904 Orb of Fate "levitate-or-teleport toggle": a level
  teleport (`artifact.c:2160`).
- L8825, L8909-8911 Eye of the Aethiopica "portal that drops you in
  Vlad's Tower": a menu of any branch you have visited
  (`artifact.c:1867-1931`).
- L8816, L8851 Staff of Aesculapius "full heal + cure": half your
  missing HP, plus sickness, sliming, and blindness.
- L8671, L8726-8727 Stormbringer "drains a level (you gain it)": the
  victim loses a level; you heal half the HP it lost.
- L8673-8674 Frost and Fire Brand "(base only)": both double damage
  against anything not resistant (`artilist.h:149-155`) (sc).
- L8677, L8731-8736 Cleaver "one-handed ... shield in the off slot": a
  battle-axe is two-handed; the cleave fires every swing.
- L8669, L8708-8714 Mjollnir "Needs Strength 25 to wield ... the
  return often misses": anyone wields it; Strength 25 to throw; only a
  Valkyrie gets it back.
- L8652-8654 blast "4d4 first touch, 1/4 subsequent": one in four on
  every touch; an intelligent artifact blasts 4d10 for the wrong role
  alone, so a Monk with the Eye of the Aethiopica (L8790-8803) is hit
  every time; magic resistance is a carry bonus on the Orb of
  Detection, Mirror, and Card (L8798-8800 says the opposite).
- L8786-8788 "Most of the non-weapon ones grant magic resistance":
  three of nine.
- L8846 Sceptre conflict "at a steep energy cost": toggled, no cost.
- L8836-8837 Heart of Ahriman "+1 luck bonus": stealth only, plus the
  ordinary luckstone +3.
- L8849-8851 "one of only three drain-life weapons; the others are
  Stormbringer and the rider Death": Stormbringer only; Death is not a
  weapon.
- L8870, L8890 artifact Protection "−1 to AC": +1 magic cancellation,
  never AC (`do_wear.c:2492`, `mhitu.c:1113`).
- L8884-8886 Master Key "opens any lock without effort": finds traps
  while picking; `#untrap` on doors and chests always succeeds.
- L8898-8899 Card "a free wish per ~1000 turns": one extra charge on a
  wand of wishing, which survives a single recharge.
- L8861 Eyes of the Overworld "see invisible, see through walls, spot
  secret doors": x-ray vision, radius three.
- L8700 Excalibur: dipping also needs experience level 5.

### Into Gehennom (L8915-9302)
- L8960-8962 "Stand one knight's-move from the bridge while guessing;
  adjacent squares get crushed": the tune only works with the bridge in
  the eight squares around you (`music.c:816-832`) (sc), and only the
  span and doorway are crushed.
- L8968 after striking "The moat squares become walkable": the span
  drops into the moat and becomes water again (`dbridge.c:924`).
- L8988-8990 "leprechauns and rats gnaw containers": invented; a
  gelatinous cube would.
- L8993-8995 "storerooms hold random fodder": armor, weapons, gems,
  food, one class per room.
- L9066 Valley "shrine to Moloch in the upper-left corner": the down
  stair is the upper-left corner; the temple is mid-left; you arrive
  lower right (`valley.lua:48-68`).
- L9097-9098 lava "you sink and burn within a few turns": see Ways to
  Die.
- L9121-9123 demon princes "will not pursue you": they wait until they
  see you, then follow on stairs.
- L9126-9128 bribery: a hero with no gold in open inventory is attacked
  (`minion.c:309-316`).
- L9137, L9194 "a wand of death works on all four": demons are immune
  to death rays (`zap.c:4308-4313`) (sc).
- L9167, L9174-9175, L9179 Vlad's throne: up to 80 HP (rnd), about two
  bad effects on the way to the wish, and magic resistance blocks
  nothing there.
- L9192 Orcus "the Wand of Orcus": a plain wand of death.
- L9246 "the bottom of the Wizard's Tower": the Wizard and the Book are
  at the top; the portal enters at the bottom (`wizard1.lua`,
  `fakewiz1.lua`).
- L9260 "You feel an unsettling vibration": "a strange vibration under
  your feet" (`hack.c:3079`).
- L9264-9266 "`#invoke` the Bell of Opening": apply the Candelabrum to
  light it, apply the Bell to ring it, then within four turns read the
  Book; none may be cursed (`spell.c:241-291`).
- L9273-9274 Sanctum up stair "(it would not before you had the
  Amulet)": no such gate.
- L9227, L9270-9271 Amulet "on the high altar": the High Priest carries
  it (`priest.c:260-263`).

### The Ascension (L9303-9663)
- L9337, L9641-9643 "a wielded cockatrice corpse one-shots Riders /
  they have no stoning resistance": all three Riders resist stoning in
  5.0 (`monsters.h:3149, 3159, 3169`) (sc).
- L9399-9402 "a cursed potion of gain level ... without provoking the
  Mysterious Force": the Force fires on any upward level change in
  Gehennom that is not a portal (`do.c:1541-1543`). Cut.
- L9534-9536, L9545-9546 "magic mapping tells you which cavern holds
  the portal": mapping draws only traps already seen
  (`detect.c:1406-1408`), and the Plane of Air map is uniform. Confused
  gold detection or a crystal ball finds it.
- L9571-9577 Plane of Water "you will drown ... the next turn drowns
  you again", "chambers", "corridors": you arrive inside a drifting
  air bubble; a misstep into the water beside a bubble only means
  scrambling back out (`trap.c` `drown()`, `Is_waterlevel`); the map is
  open water (`water.lua:16-37`). The real drowning risk is a kraken or
  eel wrapping you.
- L9643-9645 "conflict keeps the Riders tangled fighting Angels": 5.0
  resistance is `rnd(20) > min(19, Cha − monster level + your level)`
  (`mondata.c:1607-1613`) (sc), so a level-14 hero with 18 Charisma
  conflicts a level-30 Rider about one turn in ten.
- L9646-9647 "four hostile Angels": two to four (`minion.c:486`).
- L9445-9447 helm of opposite alignment "flips you to Chaotic": a
  Neutral lands Lawful half the time (`do_wear.c:468-471`).
- L9433-9435 Force "Often it just shuffles you": same-level one time in
  four for Lawfuls, three for Neutrals, two for Chaotics
  (`do.c:1544-1545`); the decay relieves Lawfuls most (`do.c:1563`),
  not "roughly even".
- L9406-9408 "The Astral plane portal ... will not open": the gate is
  the Dlvl 1 up staircase; without the Amulet, climbing out ends the
  game as an escape (`dungeon.c:1529-1530`).
- L9336 "quest artifact + a silver saber ... silver bypasses demon
  resistances": only four quest artifacts are weapons; silver adds a
  d20 against demons, vampires, and weres.
- L9613-9617 Pestilence "finishes you a few turns after": the first
  touch sets a clock of 20 plus Constitution turns; each further touch
  cuts what remains to a third (`mhitu.c:1033-1042`).
- L9619-9620 Famine "Three swings in a row will [starve you]": each
  touch costs 40-79 nutrition (`uhitm.c:3795`).
- L9474 Elbereth "write it for the alignment": engraving grants none.
- L9591 "Three altars stand in the great temple": three separate
  temples (`astral.lua:82-89`).
- Missing 5.0 change: on the Plane of Air, lightning strikes out of
  the clouds about one turn in eight for 8d6, and fries wands and
  rings a third of the time (`air.lua:9`, `timeout.c:1855-1875`);
  shock resistance or reflection belongs in the kit discussion.

### Advanced Controls / Customization (L9664-9912)
- L9809-9813, L9887-9891 the `hilite_status` rules are split across
  lines with a trailing backslash; the continuation is joined with a
  space, which ends a rule, so every rule after the first on each line
  is rejected with "Unknown status field" (`cfgfiles.c:1720-1756`,
  `botl.c:2605-2624, 2859`). One rule per line.
- L9844-9847 `paranoid_confirmation:Attack pray Remove quit`: a list
  without a leading `+` clears the defaults (`options.c:2917-2947`)
  (sc), removing the "You avoid stepping into the water" stop that
  L9730 tells the reader to rely on; `pray` is already on; `Remove`
  means "ask which item". Use `paranoid_confirmation:+attack quit`.
- L9803-9805 "without `statushilites` the rules below parse but nothing
  colors": 5.0 turns highlighting on when any rule exists
  (`botl.c:2643-2645`). Cut.
- L9720-9726 Shift-run, `G`, and `g`: Shift is mode 1 and runs past
  items, doors, and traps; `G` stops beside them; only `g` stops at
  corridor forks (`cmd.c:1545-1615`, `hack.c:3952-4028`). The chapter
  has the cautious one and the fast one swapped.
- L9731-9734 "`me` is 'what would you like to eat?', `ma` is 'which
  tool?'": `me` skips the offer to eat floor food; `ma` does nothing
  special; only `m,` forces a menu.
- L9839-9840 "`pile_limit:5` triggers the pile menu when 5 or more
  items": inverted, and 5 is the default.
- L9795-9796 Windows config "`nethack.cnf` in the install folder":
  `.nethackrc` in `%USERPROFILE%\NetHack\`.
- L9794 "Flip them in-session with `O`": most of these need `mO`.
- L9770-9772 overview list includes "vault": no; graves, trees,
  annotations, bones, and the deepest level per branch.
- L9762 message history "several dozen lines": default 20.
- L9862-9865 `pickup_burden`: asks before any pickup that would push
  you past the named level, manual pickups included.
- L9779-9780 chronicle "first kills ... prayer outcomes": first kill,
  gifts, crowning, and the first prayer; ordinary prayers are not
  logged.
- L9829-9830 "unbleached" / "blessed-cure-injury": neither word exists
  in the game; the leading space keeps " cursed " from matching
  "uncursed".
- L9903 "`nethack-curses` on most distributions": doubtful; 5.0 is tty
  only unless built with curses.

### Sokoban Solutions (L9913-10612)
All eight maps match the level files cell for cell (boulders, pits,
holes, stairs, doors, prize chambers, prize odds, remaining-boulder
counts; verified by script). Three small things:
- L9963 "The `^` symbols mark pits": pits on Level 1 only; Levels 2-4
  have holes, and a Sokoban hole drops you a level even while flying
  (`trap.c:633`).
- L9950-9951 cheating by "destroying boulders with wands": the force
  bolt spell counts too (`zap.c:2278-2286`), and so does a pick-axe.
- L10461, L10607 "There is a bag of holding / an amulet of reflection in
  one of the small chambers" contradicts the 75/25 "usually" at
  L10373.

### Voluntary Challenges (L10613-11041)
- L10753 Pacifist "Not directly, not with pets": pet kills do not break
  it; only your own kills, and displacing a pet into a fatal trap, do
  (`mon.c:3499`, `hack.c:2201`). The next sentence contradicts this
  one.
- L10663 "Green slime is technically vegan": vegetarian, not vegan; it
  is a pudding (`mondata.h:239-241`), as L10680 says.
- L10670 "violet fungus paralyzes": it makes you hallucinate
  (`eat.c:1303`); the audit note at L10645 already says so.
- L10811-10814 genocide "type none ... Don't just press Enter": Enter
  re-prompts; a cursed scroll summons monsters whatever you type, and
  the conduct survives either way (`read.c:2859-2875`).
- L11019-11020 Sokoban conduct "fracturing a boulder with a wand of
  striking": force bolt and a pick-axe count too (`zap.c:5555`,
  `dig.c:456`).
- L11017 "Complete Sokoban without breaking the rules": reported once
  you have entered; finishing is not required (`insight.c:2517`).
- L10951 "Cleric" for the role: Priest, as everywhere else.
- L10921 "five more tracked conducts": six, with "unrerolled"
  (`topten.c:608`).
- L10684-10686 stone to flesh listed as a Foodless nutrition source,
  then "eating them breaks the conduct": not a source.
- L11000-11002 "the usual SCREECH": the message is "shrieks".

### Shopping and Shopkeeper Pricing (L11042-11310)
- L11157-11159 digging out "the shopkeeper bills you ... and the chase
  happens anyway": a wall dig costs 10 zm per point of Strength,
  demanded on the spot; digging *down* while owing anything makes the
  shopkeeper grab your whole pack first (`dig.c:781`,
  `shk.c:5061-5108, 5295-5317`).
- L11196-11198 kicked door "an angry shopkeeper": they meet you at the
  door demanding 400 zm; pay and you are welcome (`dokick.c:953`).
- L11086-11089 credit "for the shortfall": credit only when the
  shopkeeper has no gold, at nine-tenths (`shk.c:4046-4073`).
- L11093-11094, L11108-11110 gold "stolen by nymphs ... pit ...
  polymorph trap": nymphs never take gold (`steal.c:52`); leprechauns
  do; nothing else applies.
- L11136-11138 "loan": shop gold you picked up off its floor
  (`shk.c:5745`).
- L11161 artifacts "10,000-30,000 zm": 800 (Giantslayer) to 32,000
  (Stormbringer, Grayswandir), value times four.
- L11166-11168 killing a shopkeeper "summons a wave of Keystone Kops":
  Kops come only when you walk out owing (`shk.c:623,680`); the cost is
  alignment, and for non-chaotics 2 Luck and telepathy.
- L11172-11174 "sacrifice the shopkeeper's corpse on an unaligned altar
  to convert it": that costs 2 Luck and a demon; same-race sacrifice
  converts a lawful or neutral altar to chaotic (`pray.c:1717-1760`),
  as L4512 says.
- L11217 touchstone "guaranteed at Mine's End": the only one there is a
  mimic (`minend-1.lua:71`); contradicts L5456.
- L11246-11248 gem breakage "about 50% ... below Mohs 8 breaks like
  glass": breaks only on a hit; hard gems survive two throws in three,
  soft gems and glass one in three (`dothrow.c:1976-2000`).
- L11288 "an orange unicorn": alignment sets the color.
- L11291 gem value "when selling or wishing": selling and final score.
- L11296-11299 "3000+ zm per gem ... non-gem-buying shop for half":
  identified gems sell for half base (diamond 2,000); a shop that does
  not deal in gems will not buy them.
- L11179-11184 "Drop everything at the door" to get quotes: nothing
  sells on the door square (`shk.c:3943`); use `I` then `u`.
  L11185-11187 "Sell to build credit" contradicts L11079: sell for
  gold, then drop the gold.

### Weapons, Armor, and Spell Tables (L11311-12205)
The generated numbers match the build scripts and `objects.h` except one
hand edit. The prose cells are where the errors are:
- L12162 finger of death "an instakill with no Antimagic check": magic
  resistance blocks an incoming death ray (`zap.c:4493-4502`); only a
  self-zap skips it. This contradicts the book's own L4186 and L7930
  and would tell a beginner magic resistance won't save them.
- L11849, L11868 bows and crossbows "Two-handed launcher ... cancels
  shield": bows are one-handed (`objects.h:126-130`); only two-weapon
  fighting is blocked.
- L11824 crossbow bolt "1d4 / 1d6": +1 against both sizes
  (`weapon.c:229-275`); the script emits it, the hand edit removed it.
- L11825, L11869 crossbow "below that, one bolt per turn": the volley
  is rolled twice below Strength 18, not capped at one
  (`dothrow.c:225-231`).
- L11916 "Samurai get +1 multishot on shuriken": Monks do
  (`dothrow.c:53-56`).
- L12159-12161 magic missile "2d6", fireball and cone of cold "4d6":
  the dice are (XL/2 + 1)d6 (`zap.c:3462, 4256, 4264`).
- L12164 cure blindness and L12177 confuse monster "aimed": neither
  asks a direction.
- L12167 stone to flesh "Statue → corpse": animates a live monster
  (`zap.c:2017-2029`).
- L12175 detect treasure "Reveals gold and gems": every object on the
  level.
- L12172 detect food "Blessed: identifies the food": blessed warns you
  before you eat something bad (`eat.c:2834-2841`).
- L12181 charm monster "Blessed-scroll behavior": no blessed branch
  (`read.c:1044-1063`); the same claim is at L7929.
- L12163 healing upgrade "—": at Skilled it also cures blindness
  (`zap.c:2909-2912`).
- L12190 levitation "Blessed: longer duration": blessed can be ended
  at will with `>`.
- L11364 crysknife "only dropping triggers it": throwing too.
- L11960 yellow dragon scale mail "Rare.": no rarer than gray.
- L11751 lance "a critical can shatter the lance": about one joust in
  250 (`uhitm.c:2122-2125`); and `P_LANCE` is a C identifier in a
  reader-facing cell.
- L11742-11744 "Charging into a target on horseback triggers a joust":
  any mounted hit can joust; on foot the lance is a reach weapon, not
  "unremarkable".
- Print: on PDF page 230 the Spell Tables' School column is too narrow
  and "Enchantment" collides with the level digit.

### Bestiary Tables (L12206-13752)
The generated columns are clean: a reviewer regenerated the appendix
from `monsters.h` and diffed every row in the first half (156 rows);
all matched, including the hand-corrections for were-forms and colors.
The errors are in the hand-written notes:
- L12624 piercer "you can't avoid the drop without flying or a clear
  ceiling": a hard helmet makes it glance off entirely, and good AC
  gives a dodge roll; the drop is a flat 4d6 (`hack.c:3420-3437`).
- L12274 "never wield a cockatrice corpse as a weapon unless your role
  explicitly resists stoning": no role does; gloves are the
  protection (`wield.c:143-146`).
- L12723 trappers "Identify with `;` (farlook)": a hidden lurker is not
  displayed at all; searching next to the square reveals it.
- L12359-12361 "Valkyries and Tourists roll 50/50 between kitten and
  little dog": every role without a fixed pet does.
- L12496 kobolds "Most are poisonous to eat": all of them, as the next
  line says.
- L12427 mind flayer "if Int hits 3 you die": at Int 3 the next
  tentacle that lands kills (`eat.c:698`).
- L12698 "Spider-class monsters are a common source of poisonous-corpse
  food poisoning": only giant spider and scorpion corpses are
  poisonous, and "food poisoning" is the tainted-corpse term.
- L12985 yellow dragon "rare": no rarer than the others.
- L12684 rock mole "chew through your bag of gold or unattended
  weapons": eats metal objects left on the floor (`mon.c:1463-1482`).

### Bestiary Tables, second half (L13000-13752)
A reviewer regenerated all 223 rows from `monsters.h` and every
generated cell matched. The hand-written notes carry the errors:
- L13734 lizard corpse "the standard answer to cockatrices and
  Medusa": Medusa's gaze is instant death (`mhitu.c:1748-1756`); a
  lizard does nothing against her. The same error is at L1102.
- L13178 "Wand and scroll of undead turning shred them", L13489-13491
  "heavy damage": no scroll of undead turning exists; the wand and
  spell do 1d8 and make the target flee (`zap.c:243-259`).
- L13491-13493 skeletons "from a skeleton trap or ... Vlad's Tower": no
  such trap; Orcus Town only, or a bone devil's summons.
- L13624 "Demon lords can be bribed with gold": only Geryon, Dispater,
  Baalzebub, and Asmodeus, and not if you wield Excalibur or Demonbane
  (`makemon.c:1397-1402`); the Gehennom chapter has this right.
- L13002 elementals "Air engulfs and suffocates ... water drowns": air
  batters you with debris; the water elemental has one 5d6 claw and no
  drowning attack.
- L13558 Charon: inside `#ifdef CHARON`, which is never defined. Delete
  the row.
- L13207 black naga "confer poison, acid, and stoning resistance ...
  the best of the four eats": acid and stoning resistance from corpses
  last a few turns; only poison is permanent.
- L13232 ogres "Drop decent weapons and armor": a club, sometimes a
  battle-axe, no armor.
- L13354 trolls "will be alive when you come back": usually (about
  three in four).
- "passive 0d6" and "passive 0d4" (L13010, L13037-13040, L13545): 0dN
  means (level+1)dN (`uhitm.c:5885-5888`), so brown mold is 2d6 and a
  fire elemental's passive is 9d4; the audit note at L12466 calling it
  "literally zero" is wrong. The script should emit the real dice.
- 32 rows tagged "poisonous-corpse" on monsters that leave no corpse
  (every `&` row, zombies, ghoul, green slime, weres); the Zombies
  prose at L13488 says "never leave corpses" above rows that say
  "poisonous-corpse". Suppress the tag on `G_NOCORPSE`.
- The generator `build_bestiary_appendix.py` still emits pre-audit
  text (Cyclops "Caveman quest nemesis", master lich "double-trouble",
  Surtur "Has Mjollnir", mummies "curse your worn items", trolls "burn
  it with fire", "MR%" header). One rerun would undo three audit
  passes. Port the corrections into the script or mark the appendix
  hand-maintained.
- Missing from Kops (L13129) and Shops (L11139): paying the shopkeeper
  back dismisses every Kop at once (`shk.c:1395-1443`).

### Intrinsic and Extrinsic Tables / What Changed (L13753-14156)
The source columns are right (every role and race level matches
`attrib.c:23-103`); the "What it does" column is not:
- L13847, L13848, L13851 "Halves fire / cold / electrical damage":
  resistance zeroes it (`zap.c:4423-4516`).
- L13850 disintegration resistance "(still does ordinary damage)":
  nothing happens (`zap.c:4468-4471`).
- L13848 "lets you eat cold-resistant corpses safely": no such
  mechanic.
- L13844, L13853-13854, L13868 the "½×", "¼×" multipliers: acid and
  stoning corpses are 5× and 2.5× *more* likely than standard
  (`eat.c:972-996`), and a floating eye *always* grants telepathy.
  Use plain odds.
- L13857 magic resistance "magic-trap effects at 100%": no check.
- L13858 hallucination resistance omits gold dragon scales, which
  grant it (`do_wear.c:846-850`); violet fungus has no hallucination
  attack, black light does. L13859: only yellow lights blind.
- L13855 "(Stormbringer, Vorpal Blade)" as drain sources: Vorpal Blade
  beheads.
- L13871 warning "whose hit-dice exceed yours": any hostile of level 4
  or more within about ten squares; the digit is level ÷ 4.
- L13885 automatic searching "every few hundred turns": about every 85.
- L13924 Protection "same-aligned ... prayer-pool ... 400 zm per +1":
  all 3.6 or invented; no alignment check (`priest.c:685-691`), and
  L14028 in the same chunk says the 400 formula is gone.
- L13926 regeneration "about one per turn at high XL": a flat +1 every
  turn, as L14078 says.
- L13930 free action "(mind flayer hold, gas-spore explosion) and slow":
  mind flayers don't paralyze; the slow wand ignores it. It blocks
  paralysis: floating eye, gelatinous cube, ghoul, cast paralysis.
- L13943 slow digestion "about ¼ the normal rate": stops ordinary
  hunger entirely (`eat.c:3172-3178`).
- L13946 life saving "restores you to one HP": 50 + 10 × (Con ÷ 2),
  capped at your maximum (`end.c:707-716`).
- L13947 adornment "+1 Charisma": its enchantment.
- L13950 conflict "keeps shopkeepers from selling things": a
  shopkeeper caught in it attacks you (`shk.c:4897`).
- L13821 "a Wizard with XL 17 antimagic": Wizards get teleport control
  at 17.
- L14030 "500 × XL guarantees protection": the offer must be between
  two and three times the amount the priest names; more earns only
  thanks (`priest.c:685-708`).
- L14049 Medusa's four layouts and L14061 Orcish Town: both date from
  3.6.0. Cut from What Changed.
- L14056 monsters "unlock chests": unlocked containers only.
- L14068 Gehennom teleport "not permanently" blocked: 5.0 *adds* a
  within-level block while a demon lord or prince is on the level
  (`teleport.c:33-35`).
- L14115 Gehennom "breaks any potion you drop": usually.

### Index and Acknowledgements (L14157-15073)
The Acknowledgements check out: every author credit, date, and the
DevTeam roster match the archives and `dat/history`. The front matter's
"May 2026" (L48-49) is right (`dat/history:300`, "released on May 2,
2026"); `README.md` says 2025 and is the one to fix. The index has
wrong glosses beyond the seven listed in section 4:
- L14743 "Sokoban: entry one level above Oracle": below (L1617).
- L14317 "Damerell: ... prayer spoiler": Lahut's (L14986).
- L14866 "Wish: sources, six in total": seven (L8479-8506).
- L14832 "Vlad's: throne, four wishes in thirteen sits": about one
  sit in ten, once.
- L14643 "Prayer: cooldown, ~1000 turns": the body it points to says
  about 500.
- L14734 "Skill: slots, 2 + XL + crowning": one per level plus one,
  plus one if crowned (`u_init.c:884`).
- L14358, L14501 "medusa-2", "medusa-4": level-file names lifted from
  audit comments.
- L14375 "Fake: Delphi, a geometric joke": exists only in an audit
  comment.
- Eleven entries point at the wrong section (bribery rules → "What's
  Different" instead of the demon-prince lairs; haste self → Armor and
  AC; cursed bag of holding → Effects of Cursed Items; green slime → A
  note on puddings; the stethoscope's crowning meter → Other Notable
  Tools; Excalibur odds → The Roles; Plane of Water → Plane of Fire).

## 7. Craft: chapter-by-chapter suggestions

What the reviewers would change about shape, order, and usefulness,
after the errors are fixed. Additions are limited to things that
change a beginner's decision.

**Choosing Your Expedition.** A role-at-a-glance table at the top
(role, alignments, races, starting resistances, signature kit, first
gift, difficulty), with the thirteen parenthetical intrinsic ladders
folded into it or replaced by a cross-reference to the Intrinsic
tables. Put the one-line recommendation (L574) into the chapter
opener. The Knight's "real damage" for a slipped mount is 10-14 HP,
most of a starting Knight's total; say so. Rewrite Alignment around
the three facts (hostile kills raise it, a peaceful kill costs 5,
murder costs Luck) with a link to Altars and Alignment (L4510).

**What to Pack / Your First Descent.** Add Elbereth to Rule 1 ("If
you can't walk away, engrave Elbereth in the dust: `E`, `-`, the word")
and the `s`/`10s` search command to Rule 5; neither "retreat" nor
"look for hidden passages" is executable from that page. Cut Rule 6
to two sentences (poison resistance from corpses now, magic resistance
and reflection from gear later). Starvation: pray at Weak, not
Fainting. Move the reroll paragraph to Customization. Promote a
throwing stack to a Golden Rule (see section 8). Order the escapes
stairs, closable door, corridor.

**The Lay of the Land / Field Guide.** Add the four dangerous special
rooms with depths (leprechaun halls Dlvl 6+, graveyards 12+, antholes
13+, cockatrice nests 17+) to Room Types. Field Guide rows should each
give the one fact that changes what a beginner does: gas spore in the
`e` row (explodes 4d6 when killed; shoot it from two squares), molds
and jellies never move (walk around), snakes hide under items, the
first `@` you meet are peaceful watchmen and shopkeepers, giants'
corpses raise Strength, dwarves with mattocks kill first-level heroes
in two swings. Fold the gnome lords row into the `G` row. Change the
sleeping-monster diagram's `Z` to mixed letters. Add `` ` `` and `}`
to the symbol table.

**Points of Interest.** Add the missing throne outcome. Make the
altar-conversion paragraph a two-line pointer to L4512. Lead Sinks with
the common case (four kicks in five are a harmless "Klunk").

**Branches and Landmarks.** Merge the two Sokoban cheating passages
(L1648-1655, L1668-1673). Open Sokoban with the prize, not a locator.
Put the Medusa gaze checklist before the Perseus loot. Add "or break a
door or dig in town" to the Minetown watch trigger. Split Fort Ludios
into "What's inside" and "The prize", with the level-teleport escape
rule beside "dig in". Add "The Route": the recommended order of
branches with Dlvl ranges.

**Traps and Hazards / Feelings and Sounds.** Split the 51-row
Feelings table into four blocks (emergencies first: feverish, slowing
down, slime, deathly sick; then level sounds, corpse intrinsics, item
identification) and link each row to its subject. Add a "Blocked by"
column to the Dangerous Traps table (magic resistance or Unchanging,
iron footwear, sleep resistance). Open Traps with the stake (a
trapdoor or level teleporter separates you from pet and stash) rather
than a definition. Keep the engraving-durability facts in one place
and let Elbereth point back. Move Elbereth and Engravings to Part
Three.

**The Art of Combat.** Move "Fighting Smart" ahead of the to-hit
arithmetic, or add a five-line short version after the opener. Keep
the centaur speed example once (it appears at L2793, L2860, L2980).
Keep the two-handed bonus once. "Edge cases worth knowing" (L3070)
are core 5.0 behaviour; fold into "During the fight". Add a "decide
after the first exchange" rule and the retreat-upstairs habit.

**Things That Will Kill You.** Re-base "Deadly Mistakes" on the real
server ranks (mount slips and monsters' wands lead). Give the dragon
section one breath rule (reflection or the matching resistance makes
it harmless; magic resistance stops gray) and cut the scale-mail
catalogue. Add "minotaurs ignore Elbereth". Trolls: eat, tin, pet,
lava. Werecreatures: Elbereth at "summons help"; the human form walks
through it.

**Saving and Bones / Ways to Die Instantly.** Attack Wands should name
reflection and magic resistance. Split Petrification's triggers into
instant (touch, eat, kick, Medusa's gaze) and countdown (the hiss, a
thrown egg) so the reader knows when the lizard helps. Replace the
"Saving Yourself" appendix with a table (threat, warning message,
turns, cures) and promote it to open Part Three. Enchantment Drain is
not an instadeath.

**Divine Relations / Making Friends.** A boxed prayer rule: pray when
in a listed trouble AND (you have never prayed and it is past turn 300,
or about 1000 turns since your last prayer) AND you have not killed a
peaceful or been told your god is angry AND you are not in Gehennom or
on another god's altar. Rewrite the sacrifice-gift paragraphs around
the role-artifact guarantee, the corpse-value cap, and the odds; add
the payout order (angry god, alignment, timeout, then Luck and gifts).
Fix the priest cheapskate advice. Cut the four pet myths.

**A Practical Identification Strategy.** Lead "The Price Is Right" with
the base-price rule (average Charisma quotes base; sell is half), then
one markup paragraph; the sucker condition is explained three times.
Rewrite the price-quote paragraph around `:` and `#chat`. Move the
buy-off and invisibility paragraphs to Shopping. Keep the
identify-scroll rules once. Add helms ($10 plain vs $50 opposite
alignment or telepathy) to the armor price table. State the 1-in-100
explosion odds in the engrave test.

**Provisions and Dining / The Apothecary.** Open Dangerous Foods with a
five-line safe-to-eat checklist (fresh under 50 turns; not a `c` or
Medusa; not green slime; not your own race; not a dog or cat; then
check the table). Add a Stoning bullet to Neutralizing Ailments and
note that a lizard also cuts confusion and stun to two turns. Keep
BUC notes only where they change a decision. Add "when Hungry with no
food, take the stairs down".

**The Scroll Rack / Wands.** Collapse the three recharging treatments
into one under Wands. Add the sleep-ray warning (a bounced sleep ray is
6d25 turns helpless) and the bounced-death warning to Key Wands. Note
lightning's engrave test blinds for up to 50 turns in the Engrave Test
section. Give enchant armor the same "past the cap" clause as enchant
weapon. Punishment row: remove curse frees you.

**Rings and Amulets / Tools.** Apply the potion/scroll/wand template:
anchored Key Rings, Key Amulets, Key Tools. Add the amulet safety rule
(strangulation kills in six turns; take it off or pray) and the
missing amulet of change row. Life saving: wear it and forget it. Swap
the aggravate-monster aside below "the rings that matter most".
Stethoscope: the first use each turn is free. Passtune: cross-reference
the Castle chapter.

**The Armory.** Give magic cancellation its own heading and explain it
once (the cloak-of-protection/MR text is at L7135, L7321, and L7332);
name the MC2 suits. A per-slot "wear now / look for / skip" table.
One line per role naming the weapon to train first. Fix the `w`/`x`
swap description. Align the weapon grouping with the Weapons Tables
appendix. Per section 8: when AC is 6 or worse with no altar or pet,
wear found body armor, helms, shields, and cloaks now; test only
boots and gloves.

**Curses / Spellcasting / Luck / Exercising.** Learning Spells: price
is 100 × level (cross-reference Spellbook Prices) and 5.0 asks a
Wizard "This spellbook is difficult to comprehend. Continue?" so
declining is free. Spellcasting never says why the `+` menu shows 100%
Fail or how to lower it; one paragraph (metal body armor, any shield,
metal helm/gloves/boots, casting stat, school skill, quarterstaff
bonus). Cut the price-ID bullet from Detecting Curses. Open Luck with
four plain rules (keep it at 0 or above so prayer works; carry an
uncursed luckstone; gems to a unicorn of your alignment; don't kill
peacefuls or break mirrors) and add the murder row. Move "Why
Exercise Matters" up.

**Enhancing Skills / Wishes.** Put a gray-or-silver decision rule ahead
of the wish list so items 1 and 2 (both body armor) don't read as a
sequence. Move the Luck check to the first bullet. Keep the spell
upgrades once. Cut "Cap-aware investment".

**Artifacts.** Cut the thirteen quest-artifact prose entries to the
ones where a decision or trap exists (Master Key BUC, Eyes and Eye must
be worn, Staff, Card, Orb of Fate, Heart) and let the table carry the
rest. Restate Alignment and Blasting as three rules naming the
intelligent artifacts. Link Sacrifice and Wishes from "How you get
one" and say plainly that a first artifact is nearly always a
sacrifice gift or Excalibur.

**Into Gehennom.** Rewrite Heist step 4 (light the Candelabrum, ring
the Bell, read the Book within four turns; nothing cursed). Give the
Wizard's Tower its way in (the fake towers' portal enters at the
bottom; the Wizard and the Book are at the top). Replace the Valley
corpse paragraph with the arrive-lower-right, exit-upper-left plan.
Note the candle chests in Vlad's Tower. List Vlad's throne effects.
Add a Castle layout figure.

**The Ascension.** Say "self-teleport fails on the planes" once. Add a
scroll of scare monster to the Elbereth bullet. Add the Plane of Air
lightning note. Give Astral a four-step ordered list before
"Defenses". Link the kit table's "Required loot" to the Sanctum.

**Advanced Controls / Customization.** Open Customization with a
ranked five-option list and reasons (HP colors; `+attack quit`;
autopickup with `pickup_types:$?!=/`; `pickup_burden:unencumbered`;
menucolors for cursed), then the corrected starter file. Drop
`runmode:walk` or justify it. Move "Forcing locked chests" beside the
Locks material.

**Sokoban Solutions.** Define the notation after L9968: coordinates
are (column, row); "Finish X" means push X to the trap row and along it
into the nearest unfilled pit, in the order listed; "Finish C like G"
means take G's route; the arrow squares show as `^` in the game.
Rewrite the mirroring note for print readers (the level is fully
mapped on arrival; match the outline; swap left and right in every
step and count columns from the other edge; the web edition has flip
buttons). Warn that Levels 2-4 use holes that drop you a level. Link
the zoo and the scroll under the prize.

**Voluntary Challenges.** Give every conduct the same three beats
(what it means, what breaks it, what it costs) and a one-glance table
(conduct, broken by, how to set or check). Move Nudist and Blind out of
"Combining Conducts" into their own headings (the index points there)
and cut the 5.0 preview paragraph. Illiterate: naming an item with an
artifact name breaks it; Archeologists decipher labels on pickup.

**Shopping.** Rename to match the content ("Shops: Credit, Debt, and
Trouble"), give gems their own heading, open with the walk-out
warning, and replace the scattered bullets with one table: offence,
the shopkeeper's response, the fix (leave owing: Kops, pay first;
break a door: 400 zm; dig a wall: 10 zm per point of Strength; dig
down owing: your pack; attack: the 1000 zm buy-off; arrive invisible
or carrying a pick-axe: refused at the door). The pick-axe rule appears
nowhere in the book. Replace "drop everything at the door" with `I`
then `u`, and "sell to build credit" with "sell, then drop the gold".
Add "paying the shopkeeper dismisses every Kop".

**Weapons, Armor, Spell Tables.** Point the Weapons intro at the
Per-Role Skill Caps table. Widen or abbreviate the Spell Tables'
School column for print. Put the helm of opposite alignment's
self-curse first.

**Bestiary.** Make the generator honest so a rerun is safe: suppress
"poisonous-corpse" on no-corpse monsters, render `0dN` as real dice,
delete Charon, unify "spell spell" and the three Str-drain labels,
collapse repeated identical attacks ("tentacle 2d1 drain-Int ×5"),
drop the "(no X)" parentheticals, and port the audit corrections into
the script. Class intros: first sentence is the danger or the
opportunity, not a locator ("Cats.", "Dwarves and similar."). Add the
quest-leader labels missing from Pelias, Shaman Karnov, Lord Sato,
Thoth Amon, Master Kaen, and the Dark One.

**Intrinsic and Extrinsic Tables / What Changed.** Rewrite the "What
it does" column against the source (immunity, not halving; plain odds
instead of multipliers; the real free-action and warning rules) and
link the Fast, Warning, and Protection rows to their chapters. Regroup
What Changed by what will hurt a returning 3.6 player first (unicorn
horns, touch of death, monsters looting and reviving, Gehennom potions
and teleport, wand of speed, alchemy, the Luck cap), then new things
to use, then numbers that moved; merge New Dangers and New Hacks into
those groups. Add a one-line pointer for 3.6 veterans in the
introduction.

**Index / Acknowledgements.** Generate the HTML index from the same
entry list as the print index (`index-draft.md`) and retire the
hand-typed "humorous index" in `template.html` (two of its anchors are
dead). Apply the roughly sixty cuts `index-audit.md` recommended that
still ship. Add head words with "see" lines for Magic resistance,
Free action, Telepathy, Poison resistance, Intrinsics, Price
identification, Hunger, Corpses, Conducts, Options, Bones, Touch of
death, Riders, Shops, Lycanthropy. Remove the word-split heads ("No:",
"First:", "Feel:", "Early:", "Holy:", "Large:"), give each sub-entry
its own page number instead of a fused run-on, move the symbols out
of "0-9", and fix the wrong glosses in section 6. Fix `README.md`'s
"2025" to May 2026.
## 8. What the yba bot evidence says

The user's yba/yendorbound project bred an automated player and
compared it against a large sample of human games on the public
servers. A reviewer read its analysis documents
(`STRONG_PLAYER_GAP_ANALYSIS.md`, `HUMAN_STRATEGY_GAPS.md`,
`STRATEGY_REPAIR_PLAN.md`, `LESSONS.md`) against the book. The bot is
an AutoAscend descendant with no long-horizon planning, never wears
untested armor, and flees only when two monsters are adjacent, so
some of its lessons are bot-specific; those are marked.

**What kills, what keeps alive.** In the bot's fleets most deaths were
attrition (trading blows with a mid-tier monster on Dlvl 3-5: hill
orc, rothe, dwarf, killer bee, gnome pack) and being hit by something
unseen; starvation was 5-13%. In 565 human games, the top early
killers were dwarves (5.5%), gnome lords (4.2%), slipping while
mounting a pony (3.9%), small mimics, giant bats, and wands zapped by
monsters; humans starve in 0.2% of early deaths. The bot survived
better per turn than humans (95% alive at turn 2000 vs 62%) but
converted Dlvl 3 to Dlvl 5 at 21% against 72%, because it spent a
third of its turns searching (82% of them finding nothing, 55% with a
down stair already known) and sat on Dlvl 1-2. Measured wins: writing
Elbereth the instant a werebeast "summons help" (the single best
change, −7 deaths in a fleet); not spending prayer at Weak so the
Fainting emergency still had a window (−10 deaths); putting body armor
on under the cloak; standing still and letting a pack arrive rather
than stepping toward it; an experience-level-4 floor before leaving
Dlvl 1. Measured losses: retreating pre-emptively to a corridor
chokepoint (3 saved, 4 lost); deferring melee against a homunculus;
closing doors on pursuers (no effect).

**Where the book's emphasis is off, by this evidence.**

- *Wear the armor you find.* 73% of bot heroes had no body armor at
  Dlvl 3 because nothing was ever proven uncursed (the pet was gone by
  Dlvl 2 in 15 of 16 games). The book's "BUC-test before donning"
  (L7028-7030) reproduces this for a beginner with no altar and no
  pet. The owner's own ruling in the repair plan: only boots and gloves
  are dangerous cursed; body armor, helms, shields, and cloaks should
  go on now when AC is 6 or worse.
- *Werecreatures.* The book's note (L3408-3427) covers lycanthropy and
  says nothing about the fight. Elbereth at the summons message is the
  whole fix; the human-form `@` walks through it; silver weapons were
  never found before Dlvl 4 in any werebeast death.
- *A throwing stack.* Every non-combat Dlvl 3-5 death class collapsed
  into "no ranged option" (floating eyes blocking routes in 36 games;
  rothes, which win the damage race from full HP). The book gives this
  one packing line (L646-648).
- *Retreat upstairs is ordinary play.* 79% of humans go up before turn
  2000, and the more-retreating half reaches Dlvl 15 twice as often.
  The book has stairs as one line (L2986-2991) and Rule 1 sends
  beginners to a corridor. Also: the stair square accumulates monsters,
  so expect a pack on return.
- *Full HP.* The median human spends 93% of early turns above 80% HP
  and descends at full; the book says "at high HP" (L3162).
- *Hungry means go down.* A cleared level has no food; praying at
  Weak spends the window. The book says "pray when Weak" (L5651,
  L5811) and never says to leave the level.

**Where the book overweights something.** The corridor chokepoint
(L710-725, L815-817): a corridor has two faces and a rothe still gets
three attacks; only a closed door has zero. The Mines bar of "XL 5,
sleep resistance, AC 0 or below" (L3181-3183): humans reach Dlvl 5 at
XL 4, AC 3, and waiting has its own body count. Wall-tapping (L2289,
Rule 5): squares searched 30+ times found one staircase in 12,379
turns. "XL near Dlvl" pacing (L3155-3165): winners and losers descend
at the same pace; max HP, not depth, is the one stock that predicts
survival at every landmark (the bot-specific counterweight: XL 3 was
worse for it). Elbereth as "free, instant" (L2498, L3063): five of
five rothe deaths died mid-write.

**Bot failures that are beginner failures.** Caution that never
converts (untested armor, not descending hungry, searching with a
known stair). Swinging until dead at one strong monster because "I'm
not surrounded yet". Entering the Mines at XL 3-4 and AC 8. Losing the
pet by Dlvl 2 and then having no curse test. Writing Elbereth after
contact. A retreat with no destination.

**The reviewer's ten changes**, ranked: (1) Armory L7028: at AC 6 or
worse with no altar or pet, put found body armor, helms, shields, and
cloaks on now; test only boots and gloves. (2) Werecreatures L3408:
Elbereth at "summons help"; the human form ignores it. (3) Rule 1 and
"Caught in the open": order the escapes stairs, then a door you can
close, then a corridor; let the pack arrive rather than stepping
toward it. (4) What to Pack: promote a throwing stack to a Golden Rule
and name the never-adjacent monsters (floating eye, rothe, homunculus,
soldier ants). (5) Mines readiness: a reachable bar (AC about 5, XL 5,
full HP, a throwing stack, an escape item). (6) Provisions and Rule 5:
when Hungry with no food, take the stairs down. (7) Searching: if a
down stair is known, take it. (8) "Trade hits"/"Know when to run":
decide after the first exchange, alone or not. (9) Elbereth: write it
before contact; below half HP with a multi-attacker adjacent, the
stairs beat a dust write. (10) Pacing: rest to full after every fight,
don't take stairs below about 90%, and expect the pack at the stair on
return.

Two of these (4 and 8) also came up independently from the chapter
reviewers; 1 and 6 are the ones most likely to change a beginner's
survival. Note that 5 conflicts with the book's current Mines bar and
with the contradiction listed in section 4, item 13, which needs one
answer.

## 9. Mechanical checks and process notes

- **Links.** 503 internal links to 205 anchors, none broken; 280 index
  targets, none broken.
- **Em-dashes.** 276 lines still carry one, but almost all are in the
  generated tables (Weapons 62, Armor 58, Spell 26), the TOC (40), and
  two prose chapters (Enhancing Skills 42, Artifacts 18). Body prose
  elsewhere is clean.
- **Banned-phrase scan.** No C identifiers, implementation talk,
  "the lesson is", designer jargon, or sensory caveats survive a regex
  pass. What does: "BoH" in prose (L6812), "tells you something about"
  (L4815), nine sentence-initial "Never"/"Always" outside conduct
  definitions, and one borderline dismissal (L8493).
- **Format-specific content.** The historical introduction (L11-65) is
  LaTeX-only, so web readers never see it. The identification
  flowchart exists in both builds. The Shopping "toolbar" note
  (L11235) is web-only and the print reader gets no equivalent.
- **Audit badges that are themselves wrong** and would mislead the next
  pass: L691 "prayer cooldown averages ~1000 turns" (it is rnz(350),
  mean about 450); L12466 "0dN means literally zero" (it means
  (level+1)dN); L13612-13621 "poison resistance doesn't protect against
  sting Strength drain" (it does, `attrib.c:338-341`); L11009 searched
  only direct calls of the Sokoban guilt routine and missed force bolt
  and pick-axes; L1063 says no dragonhide weapons exist while L1129
  and L3516 still mention dragonhide.
- **Generated appendices.** The bestiary generator emits pre-audit
  text; the weapons script emits the correct crossbow bolt "+1/+1"
  that a hand edit removed. Either port the corrections into the
  scripts or stop rerunning them.
- **How this review was done.** Two whole-book reviewers (structure;
  consistency), twenty-nine section reviewers with a shared brief
  (correctness against the 5.0 source, style rules, reader usefulness),
  four prose-register sweeps over ranges reviewed before the "sounds
  like a person" rule was added, and one reviewer for the yba material.
  The collating editor spot-checked about thirty citations across the
  reports by opening the cited source; every one held. Reviewers were
  told to report only claims they were confident were wrong and to
  open every file they cited; a handful of their proposals still
  deserve a second look before editing (marked "confirm" above where
  the reviewer said so). The per-section reports, with fuller
  proposed replacement text, are collected in
  `spoilers/companion-editorial-review-reports.md`.
