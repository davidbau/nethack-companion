# Editorial review: per-section reviewer reports

Source material for spoilers/companion-editorial-review.md (2026-09-04). Each report is a reviewer's findings for one range of companion.md, condensed; line numbers refer to companion.md at review time, file:line to nethack-c/upstream/.

# Whole-book structure review (agent W1) — full findings

1. Front matter (L69-99): sets stance but never says how to use the book. Conventions unexplained (`code` keystrokes, bold for both items and rules, "Dlvl" at 3321/3695 vs "dungeon levels 2 through 4" vs "levels one through five", "$"/"zm" prices, "(new in 5.0)" tags). Print build has inside-cover command reference + "Dungeon Emergency Checklist" (template.tex:405-451); web has no equivalent. Proposal: half-page "How to Use This Book" after L99: (a) first-descent path: ch1 (one role rec only), 2, 3, then 11's opening (3101-3166), delayed-death section (4216), BUC (4777); (b) lookup path; (c) conventions box. Emergency checklist in both builds.

2. Order: Part sequence right. Problems: Saving and Bones (3651, 94 lines) wedged between the two death chapters -> move to Part One after Your First Descent or appendix. Elbereth (2406, ~150 lines, 12 inbound links) is 7th section of "Traps and Hazards" inside "Dungeon Sights"; belongs in Part Three. Traps chapter is a grab-bag (Searching 2220, Secret Doors 2258, Engravings 2335, Iron Bars 2556). Shopping (11042) prose is in appendices while its price tables live in Part Four (4852-5254, ~400 lines): inverted. Luck (7972) matters from turn one; move to Part Three after Divine Relations; fold Exercising (8119, 47 lines) into it. What Changed (13963) buried between tables and Acknowledgements; make first appendix or front-matter note. Parts have no opening text (847, 2665, 4750, 7792, 9662). TOC: descriptions missing for 38-41 (158-161); #17 repeats its title; titles alternate register (Apothecary/Scroll Rack/Armory vs Wands/Spellcasting/Artifacts).

3. Section templates: Potions (5817), Scrolls (6026), Wands (6253) share table -> "Key X" anchored entries -> mechanics. Breaks for Rings (6563: price table, no Key Rings, strategic prose for free action/conflict/teleport control unanchored so index sends nine ring entries to one table 14677-14686), Amulets (6638), Tools (6733-6870: five category tables, no Key Tools; bag of holding and unicorn horn prose only), Armor (7018: prose by slot under #####, no summary table), Weapons (7344 groups "by how they're used" while Weapons Tables 11311 group by skill). Lead columns differ (potions/scrolls: chance; wands/rings: price). Proposal: one template (opener -> table Price|Item|Chance|One-line use -> Key X anchored entries -> mechanics); add Key Rings/Amulets/Tools; align weapon grouping with the appendix.

4. Length: Choosing Your Expedition 412 lines = thirteen role essays before the reader has played; needs one recommendation + comparison table. What to Pack (75) is the natural home of a pre-descent checklist. Identification (844) inflated by price tables. Spellcasting (178) light for a common first pick: "first spells by role" table. Curses (96) has one cross-ref.

5. Navigation: 503 links/205 targets none broken; 280 index targets none broken. Density uneven: Fauna 142, Rings 1, Curses 1, Spellcasting 1, Feelings 1, Saving 0, Customization 0. Curses should link remove curse (6107), holy water (5885), priests (4448), prayer (4311). Feelings table rows (2591-2607) should link to subjects. PRINT: latex-filter.lua:265-321 appends "(p. NN)" only after "see [X]" (27 occurrences) or five always-pageref anchors; ~475 of 503 links print as coloured words with no destination. Expand always_pageref to every ###/#### anchor or add page ref when target is outside the current chapter. Index (14157-14904, print-only) reads like a real index; fixes: duplicate heads "Altar:"/"Altars:" (14191-14192); glosses filed under wrong word ("The: Price Is Right" 14782, "Wow! This makes you feel great!" 14873, "Discipline, the difference" 14330); jargon ("BoH" 14241, "Minesflayer" 14562, "Foocubus" 14386); "Amulet:" (14194) twelve glosses to one page. HTML index would cost little. Sidebar TOC lists H2/H3 only (template.html:57).

6. Pedagogy: exists: Golden Rules 1-7 (708-788) as paragraphs; early hazards list (788); ID flowchart (4769); Ascension Kit table (9309); "Saving Yourself from Imminent Death" (4216) as last section of Ways to Die Instantly; print-only inside-cover checklist. Missing/buried: emergency page on web; pre-descent checklist (closest: pacing paragraph 3155); a single itinerary (altar -> Sokoban -> Mines -> Minetown -> Oracle -> Quest -> Castle; seed at 1500 "Sokoban or Mines first?"); boxed Golden Rules. Proposal: promote 4216 to short chapter opening Part Three ("When You Are About to Die"); pre-descent checklist in What to Pack; "The Route" in Branches.

7. Visuals inventory: 3 SVG maps (DoD 915, Gehennom, Planes; dungeon_map.py); ID flowchart (web 4769/print 4961); ASCII chokepoint diagram (714); room sketches (973); Mines sketch (1534); 16 Sokoban maps (9978-10576); ~150 tables (103 dense-table); rcfile samples (9807-9885). Most helpful additions: prayer decision flowchart (4311; priority list at 4325 ready-made); Elbereth quick card (2406); route strip in Branches (1495); status-line decoder near Your First Descent (hunger 5646 + encumbrance + HP prayer threshold 4327); Castle layout (8924).

8. Top 10: (1) How to Use This Book + conventions; (2) emergency checklist in both builds, promote 4216; (3) move Elbereth/Engravings to Part Three; (4) print page refs beyond "see" links; (5) apply item template to Rings/Amulets/Tools; (6) pre-descent checklist + Route itinerary; (7) unify Shopping with price tables; (8) move Saving and Bones, move Luck to Part Three; (9) What Changed first among appendices, Part openers, TOC 38-41; (10) index cleanup + HTML index, prayer flowchart, Castle map.

---

# Whole-book consistency review (agent W2)

## Contradictions
1. Enchant-weapon destruction: 7645-7647 "no destruction limit... never lost" vs 6122-6124 (+6 or higher, 2/3 chance) and table 6086 "above +6". wield.c:999-1000 spe > 5 && rn2(3) evaporates. 6122 right; fix 7645; 6086 -> "at +6 or higher".
2. Prayer timeout: 749 "about once every thousand turns", index 14643 "~1000" vs 4351-4352 "averages around 450", 4375 "roughly 500". pray.c:1356 rnz(350). 450-500 right.
3. Potion of healing vs blindness: 5851 "cures blindness unless cursed", 6001-6002 vs 3641 "a blessed potion of healing". potion.c:1999-2000 blessed only. 3641 right.
4. Sleep-resistance sources: 3191-3193 claims "Wizard's cloak of MR, Ranger's elven cloak" grant it. Ranger starts with cloak of displacement (u_init.c:129); elven cloak = stealth, cloak of MR = antimagic (objects.h:615,644). Book's own table 13864 is right.
5. Fedora: 7159-7160 "base item for the Eye of the Aethiopica, the Priest quest artifact" vs 1785, 8825, 8906 (Wizard's amulet), Mitre for Priest 8819, 8867 (artilist.h:265,303).
6. Drain resistance: 7271-7272 "no non-artifact source outside this shield" vs black DSM at 3483-3484, 4099-4101, 13870, 14052-14054 (do_wear.c:809-814).
7. Castle wand chest: 6821-6823 residents "can empty" the chest vs 9014-9018 "cannot unlock chests" (castle.lua:144 locked=1; muse.c:2273). 6821 wrong.
8. #invoke key: 8805 "default ^A" vs 9702-9704 Ctrl+A = repeat (cmd.c:1744 M('i') invoke; :1822 C('a') repeat).
9. Priest donation: 1572-1574 "a point of intrinsic protection" vs 4461-4463 "2-4 points" (priest.c:694-695 rn1(3,2)). 4461 right.
10. Mummy corpses: 1122 "corpses dangerous to eat (age you)" vs 5729-5730 "No corpse: M mummies" (monsters.h:1944 G_NOCORPSE). 1122 wrong; no aging mechanic.
11. Shimmering dragon: 5772 lists it; deferred in objects.h:509-512 (#if 0). Remove.
12. Print index contradicts body: throne wish "positive Luck 7+" 14783 vs non-negative 1339/1355; wish "+3" 14866 vs +2 advice 8566-8574; minotaur "~38" 14564 vs 42 at 3243; Grayswandir "half phys" 14428 vs double damage 8668/8704; wand of digging "cursed zaps down" 14844 (removed mechanic, see 6258); gnomish wizard "sleep spell" 14421 vs psi bolts 3179; alchemy "blast ~1 in 30" 14189 vs 10% 5979.
13. Mines readiness: 1507-1511/1566-1567 (Sokoban first, Minetown early) vs 3181-3183 (return only at XL5+, sleep res, AC<=0, which 2752 calls mid-game). Pick one bar.
14. Disenchanter: Mid-Dungeon Threats 1129 (and "dragonhide" weapons, none exist per audit 1063) vs Gehennom-only 4123.
15. Corpse freshness: 803-805 (safe 30, tainted ~175), 5666 (30-50), 5725 (50), 3453-3454 (globs ~500 "twice a normal corpse"). Align.
16. Shields and casting: 7251-7252 "penalty unless small shield" vs 7261-7262 "any shield still adds a flat penalty".

## Redundancy (home -> others shrink to a line + link)
17. Mine's End luckstone decoys 1594-1612 ≈ 5507-5514 verbatim. Home: Gray Stones.
18. Excalibur dip at 1275-1294, 344, 561-562, 7385-7390, 8698-8701, 14065-14066. Home: Fountains.
19. Wand of wishing charges at 6350-6357, 6467-6477, 6136-6144, 6933-6936, 8479-8480, 9020-9025; charging-explosion ladder twice (6139-6142, 6459-6465). Home: Wands -> Recharging.
20. Unicorn horn full treatment in Apothecary 5988-5997 and Tools 6887-6904 (+ table 6875); "no longer restores attributes" at 3898, 5994, 6899, 14012. Home: Tools.
21. Curse testing: pet test at 613-616, 740-741, 2770-2774, 4602-4610, 4672-4673, 4827-4835, 7756; altar flash at 1304-1311, 4818-4825, 5564, 7754. Home: Identification 4818-4835.
22. Encumbrance tiers tabled at 2830-2841 and 6785-6797; BoH quarter weight twice within 6753-6797.
23. Seven candles/Izchak at 1578-1583, 6851-6854, 9251-9256, 9337; "is the clean answer" verbatim at 1580 and 9254.
24. Elbereth: dead-in-Gehennom at 2473-2474, 2530, 9056, 9472-9477; defile rule at 2476-2494, 2644, 3038-3039, 3066-3068; scare-monster pickup at 2535-2537 and 6177-6180. Home 2406-2542.
25. Smaller: eel-grab 1999-2002/3944-3959/4264-4270; floating eyes 796-799/1091/3238-3240; Sokoban cheat penalties 1648-1673/9946-9955/11017-11022; same-race sacrifice 4419-4422/4526-4529; fountain-wish odds 1268-1273/3230-3236/8498-8502; magic-lamp odds 6844-6846/8494-8496; Vlad's throne 1358-1359/8485-8488/9155-9183.

## Terminology drift
26. "Cave Dweller" (281, 518, 7047, 10952) vs "Caveman/Cavemen" (640, 5717, 7423, 7449, 7595, 8334, 8840, 9075, 11541, 11693-11694, 12307) vs "Caveperson" (13889, 13905).
27. Money: $N (41x, ID/Scroll/Wand chapters) vs zm (34x, Armory/Tools/Shopping) vs "zorkmids" (1714, 3617), "gold pieces" 4925. Levels: "Dlvl 2 to 4" 1508 vs "dungeon levels 2 through 4" 1529, "Dungeon level 12" 3157, "level four" 89. Probabilities mixed within one passage ("about 1/30", "1/6", "1-in-3", "one in seven" 1241-1286; 8498-8501). Dominant: "1 in N". Keys: "Ctrl+A" 11x vs "^A" 8805. XL: "experience level N" (24x, roles chapter) vs "XL N" (28x later).
28. "pickaxe" (136, 241, 243, 255, 6729, 6954, 6960, 9110) vs in-game "pick-axe" (1639, 7428, 11511). "foocubus" (2853, 3303, 3586, 7108, 13949) vs "amorous demon" (1380, 3585); "BoH" 6812/14241; "Minesflayer" 14562; "mindflayer" once. Third person "the player" 3281, 3256.

## Formatting
29. Heading case: #### Title Case in Parts One-Four; sentence case in Advanced Controls (9689, 9710), Artifacts (8656, 8781), Gehennom (9113), Intrinsic tables (13852-13937); "A note on nymphs/mimics/puddings" vs "A note on Seduction" 3576, "A note on Light Bursts" 3628. Lead-ins "**Defenses.**" (3340, 3441, 4140, 9636) vs "**Defenses:**" (3782-4096). Curses chapter bullets drop terminal periods (7724-7733, 7754-7762, 7772-7780; also 4670-4681). Stale "the table above" 4890-4891 refers to print-only table that follows at 4998; 12958 links DSM to #armor-tables instead of #dragon-scale-mail.

## Repeated phrases
30. "the dungeon's [superlative]" 19x (2907, 3431, 3985, 5628, 5988, 6069, 6729, 6736, 6887, 7063, 7194, 7203, 7522, 7720...), five in Armory; "the single most" 7x (1090, 1299, 2790, 4767, 5256, 9747, 9818); "worth knowing" 8x; "The catch" 8x; "one of the most / the most important" 10x (2952, 3005, 4942, 5471, 6831...); "lifeline" 4x (307, 5889, 7125, 14040); "the real prize" 4x (1892, 5908, 6843); "the clean answer" twice.

---

## Chunk 1: Front matter + Choosing Your Expedition (L1-593)

Verdict: reads well; role portraits confident; strongest Archeologist (L240-262), Samurai wakizashi (L428-432). Weakest: Alignment (L545-572) thin, partly unsupported, never says what moves the number.

Correctness:
- L539 orcs "Don't eat anything on the o letter (cannibalism)": orcs exempt (eat.c:51 CANNIBAL_ALLOWED = Cave Dweller or orc). Propose: "You can even eat other orcs; your kind has no taboo against it."
- L540-542 "(shopkeepers, priests, watchmen included)" hostile to orcs: always-peaceful monsters exempt (makemon.c:2272-2286; shknam.c:666; priest.c:253). Propose: "...though shopkeepers, temple priests, and the Watch stay civil".
- L414-416 Rogue "coat your blades and darts ... a thrown dagger leaves venom": only ammo/missiles poisonable (obj.h:264-268); Rogue starts with daggers not darts (u_init.c:133-141). Propose: "Later, the potion of sickness you start carrying can coat darts or arrows with venom, though not your daggers."
- L510 humans "nobody singles you out": gnomes and orcs are always hostile to humans (role.c:595; makemon.c:2285-2286). Propose: "only the gnomes and orcs hold your race against you, which is why the Mines treat gnomes and dwarves more kindly than you."
- L361 Monk "Heavy body armor wrecks your aim": any body armor, flat 20 to-hit (uhitm.c:397-399). Propose: "Any body armor, even a leather jacket, wrecks your aim".
- L378-379 Priest "first worthy sacrifice is guaranteed to return Demonbane": gift chance 1/6 per worthy offering (pray.c:1781-1792); first GIFT is Demonbane for any alignment (artifact.c:87-95, 208-217). Propose: "Your first sacrifice gift, whenever your god sees fit to grant one (about one worthy offering in six), is Demonbane".
- L466-468 Mjollnir "flies back to your hand when you hurl it": throwing needs Str 25 (dothrow.c:127-129). Propose: "once you have the 25 Strength to throw it".
- L571-572 "Chaotic is often paired with Rogue for thematic consistency": Rogues always Chaotic (role.c:342). Propose: "Rogues are always Chaotic; Barbarians, Rangers, Wizards, Monks, and Priests may be."
- L574 "Lawful or Neutral Valkyrie, Human or Dwarf": dwarves Lawful only (role.c:632). Propose: "a Valkyrie, Human (Lawful or Neutral) or Dwarf (Lawful)".
- L385 "Do not anger shopkeepers or break mirrors" under guard your Luck: angering shk touches no Luck; killing a peaceful does (mon.c:3649-3665). Propose: "Do not kill peacefuls or break mirrors".
- L569-570 Chaotic "kill with relative impunity but should avoid pious behavior": killing a peaceful costs every alignment 5 (mon.c:3721-3722); no mechanic punishes piety. Propose: "Chaotic characters escape the Luck penalty for murdering peaceful humans, but killing any peaceful still costs alignment."
- L298 Cave Dweller "weakest spell access": Barbarian worse (role.c:106, 147). "among the weakest".
Verified: all 13 intrinsic ladders (attrib.c:27-89); starting kits; Excalibur 1/6 vs 1/30; 45% mount failure XL1 (steed.c:339-341); backstab; elf bow bonus; Tourist surcharge to XL15; race caps.

Style: L240 missing comma "explorer, not a warrior". L260 "never smash" -> "leave historic statues standing". L310-311 "never waste one" -> "rather than on easy kills". L347 "like a gentleman" (Knights can be women) -> "with honor". L537 "genuinely useful" hollow. L549-550 good/balanced/evil contrast never lands -> "...but the game doesn't judge you that way. Alignment is a number." L566-567 "Neutral has access to some excellent quest artifacts" vague -> "Neutral is open to ten of the thirteen roles, the widest choice."

Craft: Roles (L228): 13 portraits, no summary; add one-screen table (role, alignments, races, starting resistances, signature kit, difficulty) and move the 13 parenthetical intrinsic ladders into it or cross-ref Intrinsic tables (L13753); "Available for:" lists (L517-543) become a column. Opener (L224-226) promises a recommendation that arrives 350 lines later (L574): put the pick there. Knight (L338-339) "real damage" hides 10-14 HP (steed.c:354). Alignment (L545-572): give the three facts (hostile kills raise, peaceful kill costs 5, murder costs Luck) or shrink to pointer to L4510; no cross-ref exists. Best: Archeologist; Valkyrie closer L576-578.

Top 3: fix orc entry + Rogue poison; role-at-a-glance table; rewrite Alignment with cross-ref.

Main-agent additions (AI-filler lens on L228-493): L264-277 Barbarian "your strong early game becomes a strong whole game" (aphorism); L286-292 Cave Dweller "one careful meal at a time, which makes an amulet of life saving more precious to you than to almost anyone" (ornament + non-sequitur); L303 Healer "keeps you alive by keeping you well" (chiasmus); L333-334 Knight "The pony is both a friend and the key to your signature move"; L350-351 Monk "You carry no weapon, because you are the weapon" (cliché), L355-357 "resistances and senses unfolding one after another", L366-367 "It is an unusual path, and a graceful one in practiced hands" (closer says nothing), L364-366 "Guard that robe, keep to a vegetarian diet to honor your discipline, and trust your hands" (triplet closer); L372-374 Priest "a knowledge other adventurers would trade a great deal for"; L451-452 Tourist "a role nobody expects to cast turns quietly formidable" (vague); L468-469 Valkyrie "so the question of an endgame weapon is answered almost before you ask it", L472-473 "before the dungeon turns cruel"; L475-477 Wizard "Magic is your birthright, and by the end of a run there is little in the dungeon you cannot unmake with a spell", L486-487 "learning begets more learning". Your First Descent: L705-706 "not from the greatest threats but from your fewest resources" (strained antithesis) -> "Most adventurers die on levels one through five, with almost nothing in the pack to save them." L650-652 "New adventurers pick up everything they find. Veterans pick up everything they need." (parallel; witty, author's call).

---

## Chunk 2: What to Pack + Your First Descent (L594-852)
Verdict: brisk, friendly, mostly actionable; corridor diagram (L714-725) and Restraint (L650-658) high points. Holes: no Elbereth, no `s` command; Rule 6 pulls mid-game strategy into first descent. Weakest: Rule 4 (contradicts Divine Relations, omits Luck gate).
Correctness:
- L642-643 silver "bonus against demons, undead, and lycanthropes": only weres, vampires, demons, shades, imps (mondata.c:524-528); zombies/mummies/wraiths/liches unaffected.
- L808-811 stair tumble with cockatrice corpse: only a WIELDED corpse (do.c:1796; trap.c:3888-3893), gloves irrelevant; one in the pack is harmless.
- L753-756 alignment grind on "always-hostile classes (fungi, fluids, insects)": same-alignment hostiles worth nothing (makemon.c:2352-2357); lichens/molds/blobs/bees/jackals are neutral -> zero for neutrals, five each for lawful/chaotic. Neutrals should hunt kobolds/orcs.
- L747-749 Rule 4: (1) negative Luck fails prayer (pray.c:2155); peaceful kill costs Luck half the time (mon.c:3664-3665), recovers only every 600 turns; (2) timeout starts at 300, must be <= 200 for life-threatening prayer (u_init.c:1005; pray.c:2151) -> no prayer in the first ~100 turns; (3) "thousand turns" vs L4350-4352 ~450 (rnz(350)). Propose: "if alignment and Luck are both non-negative and the game is at least a hundred turns old, prayer will almost certainly save you. But your god needs roughly five hundred turns to recover between prayers..."
- L842-843 "#force it with a weapon you don't mind breaking": blade ~0.8% snap (lock.c:228-240); blunt never breaks but 1 in 3 successes smash the box and every potion inside (lock.c:252, 186), and half these chests hold healing (mklev.c:1063). Propose: "pry with a dagger, not a mace."
- L813-814 jackal packs "two to four": extras rnd(3), quartered below XL3, halved below XL5 (makemon.c:85-114) -> pairs until XL5.
- L785-786 shift-run "yields control the instant something warrants attention": shift-run stops only for a monster ahead or one that hits you (hack.c:3933-3934; mhitu.c:512-513), walks past items/doors; G stops beside any monster/item/door (cmd.c:1615).
- L615 pet "won't step on cursed items": occasionally does (dogmove.c:1237-1238), as L4602-4609 says -> "reluctant".
- L840-841 "first ten levels": supply chests only above the Oracle (mklev.c:1036-1037).
Checked fine: 20-zm identify/healing, stair fall rnd(3), lizard cure, Weak = major trouble, kobolds convey nothing, reroll option, newt Pw, supply-chest odds.
Style: L702-706 "not from the greatest threats but from your fewest resources" mangled parallel -> "More adventurers die on levels one through five than anywhere else, not because the monsters are fierce but because you have so little to answer them with." L772-773 "MR" abbreviation -> spell out. L815 "all kill in this same shape" -> "arrive the same way". L610-611 vs L794 contradiction (two or three rations vs pick up every ration) -> "Keep two or three food rations in reserve."
Craft: Golden Rules lack Elbereth (add to Rule 1 with E - Elbereth and link L2406). Rule 5 "look for hidden passages" needs `s`/`10s` and link L2278-2289. Rule 6 (L764-774) not actionable on first descent; cut to two sentences + link. Starvation (L792-793): "If you're Fainting, pray" is a turn late; Weak already qualifies (pray.c:216-217; L5811) -> "If you reach Weak with nothing to eat, pray." Mines hazard (L819-822): hostile dwarves with picks from the first Mines level. Supply Containers pool (L831-835) as a short list. Rerolling (L660-665) belongs in Customization. Best: corridor diagram, Restraint.
Top 3: rewrite Rule 4; add Elbereth + search command to Golden Rules; fix blunt #force / wielded cockatrice / silver scope.

---

## Chunk 3: Lay of the Land + Field Guide (L853-1170)

Verdict: reads well; map figure, symbol tables, three-tier Field Guide are the right shape; B/d/e rows best. Weakest: Massacre bullet (sends human hero into cannibalism/altar offense); Field Guide rows k, u, M, F, j, S, @ give trivia instead of the one needed fact.

Correctness:
- L1027-1029 Massacre "Useful for sacrifice and for eating the safe ones for intrinsics": all massacre corpses are role monsters (themerms.lua:173-189), M2_HUMAN, convey nothing (monsters.h:3345-3460). Human hero eating = cannibalism (eat.c:770-786); non-chaotic sacrifice = infamous offense (pray.c:1698-1771). Propose: "Floor strewn with adventurer corpses (valkyrie, samurai, wizard...). They are human, so unless you are an elf, dwarf, gnome, or orc, neither eat one (cannibalism) nor offer one at an altar (your god calls it an infamous offense). None grants an intrinsic."
- L1122 mummy "corpses dangerous to eat (age you)": mummy drops base-race corpse already rotten (mon.c:629-645) -> food poisoning risk. Propose: "Their corpses are already rotten when they drop, so eating one risks food poisoning."
- L1097 kobolds "sometimes carry poisoned weapons": darts poisoned 1 in 100 (mkobj.c:887); real fact is kobold corpses are poisonous (monsters.h:624-639). Propose: "Weak individually, but don't eat them: kobold corpses are poisonous."
- L1133 horses "mostly peaceful in the wild": alignment 0; hostile to lawfuls and chaotics, ~half peaceful to neutrals (makemon.c:2290-2307). Propose: "Wild horses are hostile unless you're neutral, and even then only about half are peaceful. Tame one with food and you can ride it."
- L1004-1006 zoo "wake not when you enter, but from the noise of fighting": sleeping monster in LOS within 10 squares wakes 1/7 per turn unless Stealth (monmove.c:327-357). Propose: "They're asleep when you arrive, but each one has a chance to wake every turn you're in view (Stealth keeps them under). Fight from the doorway."
- L929 "# Corridor or fog": # is corridor, tree, or cloud (defsym.h:111,116,149); fog clouds are v. 
- Minor: L1150 all vampires fly; L1152 xorns through walls only, not floors; L1165 worm tail hit 20% (50% blade) cuts and piece usually becomes second worm (worm.c:388-425).
Checked clean: sphere explosions, buried treasure, trap rooms, leprechaun gold, newt mana, naga speeds, mind-flayer helmet, Orcus Town, jackal top NAO killer.

Style: L996-997 missing period after "bonus". L1090 em-dash -> period. L1134 "Avoid looking at them directly" not actionable -> "Their gaze confuses you whenever you can see them. A blindfold makes you immune." L1039 "Light-and-frame rooms" not a name anyone meets. L1101 "But they don't leave corpses" -> "They leave no corpse." L1166 tangled parenthetical.

Craft: e row (L1091) add gas spore (gray e, 4d6 3x3 blast, shoot from two squares). Room Types (L968-1015) lists only friendly rooms; add leprechaun halls (DL6+), graveyards (DL12+), antholes (DL13+), cockatrice nests (DL17+) with retreat rule (mklev.c:1354-1375). F/j rows: molds/jellies never move, walk around. S row: snakes hide under items. @ row: first @ a beginner meets are peaceful watchmen/shopkeepers/priests and werecreatures; cross-ref L3408. H row: giant corpse raises Strength (eat.c:1345) beats "carry gems". Gnome lords row L1114 duplicates G row L1093. ASCII diagram L973-983 uses Z for sleeping right after Z = zombie. Map symbols L926-938 add ` boulder and } water/lava.

Top 3: rewrite Massacre bullet; gas spore + fix k/u/M rows; add dangerous special rooms with depths + correct zoo waking.

---

## Chunk 4: Points of Interest (L1171-1494) — spot-checked: fountain.c:255-271, sit.c:139-143, do.c:649-660 all confirmed

Verdict: reads well; fountain section strongest (L1237-1239, Excalibur routine L1283-1294); throne section weakest (3 of 12 outcomes + kick sentence wrong); altar-conversion paragraph contradicts L4512-4517.

Correctness:
- L1245-1246 "raises a random attribute by one": at Luck >= 4 every attribute rises (fountain.c:255,264-271). Propose: "raises one attribute by a point, or every attribute if your Luck is 4 or better".
- L1241-1243 "If you don't have bad luck, about one in seven is a magic fountain": 1-in-7 is placement (mklev.c:2296-2297) regardless of Luck; Luck only gates the drink (fountain.c:254).
- L1247-1249 "sink-kicked fountains": kicking a sink never yields a fountain (dokick.c:1194-1241); sinks become fountains via polymorph (do.c:404-424) or broken pipes (fountain.c:580-591). Propose "fountains that used to be sinks".
- L1266 quoted messages: actual are "The cool draught refreshes you." / "This tepid water is tasteless." (fountain.c:280,384).
- L1270 "dropping to zero past Dlvl 20": already impossible at depth 20 (fountain.c:78). Propose "zero from Dlvl 20 down".
- L1314-1315 "stale sacrifices are an insult": value 0 -> "Nothing happens.", no penalty (pray.c:1843-1848, 2010-2014).
- L1317-1319 "the alignment penalty is steep": it is -3; the real cost is god anger + immediate smiting (pray.c:2002-2005, 1592-1599, 1436-1443).
- L1322-1328 conversion: no "nothing" outcome; negative alignment => converted outright (or if converted before: -5 align, Luck -5, Wis -2, angry god); otherwise rn2(8+XL) > 5 flips (Luck+1) or fails (Luck-1), either can summon a minion (pray.c:1637-1694). L4512-4517 already correct. Propose: "Each attempt either flips the altar (Luck +1) or fails (Luck -1), with better odds at higher level, and either result can summon a hostile minion. If your god is already angry with you, don't try: the altar's god takes you instead."
- L1340 "Genocide of a monster class": single species (sit.c:131, read.c:2826-2830).
- L1347 "A curse on one of your items": Luck <= 0: rndcurse() up to six items; Luck > 0: 250-349 turns blindness + Luck loss (sit.c:139-143). CONFIRMED.
- L1355-1356 "wish branch needs non-negative luck": at Luck -1 still 4 in 5 (sit.c:106). Propose "guaranteed only at non-negative Luck".
- L1359-1362 throne kick: only 1-in-3 roll, once per throne; otherwise 1/4 of kicks trap-door you down, rest just hurt (dokick.c:1035-1063).
- L1387-1389 + table "gone nineteen times out of twenty": 1/20 spat back, further 1/5 buried under sink (do.c:649-660). CONFIRMED. Searching and slow digestion always come back.
- L1409 sink teleport message inverted: "The sink vanishes." = moved; "momentarily vanishes" = failed (do.c:575-580).
- L1427 "a random potion pours out to drink": drunk for you (fountain.c:648).
- L1451-1452 sink potion vapors: hallucination gives "momentary vision" not hallucination (potion.c:2024-2026); sleeping/paralysis freezes 1-5 turns (potion.c:2041-2063); only invis/paralysis/sleeping/blindness self-identify (potion.c:2111-2116).
- L1490 "see historic statues by name": see the word "historic" in the name (objnam.c:806-808).

Style: L1247-1250 two sentences + colon inside parentheses -> plain sentences. L1327 "It's a real gamble" -> "It's a gamble". L1335-1337 two colons in one sentence. L1431-1433 "more hazard than help ... not something to rely on" dismissive + repeats L1372-1374.

Craft: Thrones list missing the teleport/aggravate outcome (sit.c:185-193). Altars paragraph should be a 2-line pointer to L4512. Sinks: lead with the common case (4 of 5 kicks harmless "Klunk", dokick.c:1201-1208).

Top 3: fix thrones; rewrite altar-conversion to match L4512; correct sink-ring odds + teleport message + magic-fountain Luck>=4 payoff.

---

## Chunk 5: Branches and Landmarks (L1495-2028)
Verdict: brisk, in-world, mostly scannable; Rogue Level (L1834-1853) and eel rules (L1992-2002) best. Medusa's Island weakest (three actionable claims wrong). Sokoban states cheating rule twice; Fort Ludios one dense paragraph.
Correctness:
- L1962-1966 "a cockatrice corpse, you can kill Medusa ... bypasses the reflection requirement": Medusa resists stoning (monsters.h:2842 MR_STONE; uhitm.c:1152-1161 -> trap.c:3860-3861). Propose: "A wand of death or finger of death kills her before she gets a turn. A cockatrice corpse does nothing to her; she is stoning-proof."
- L1942 "#loot him" (Perseus statue): #loot opens containers only (pickup.c:2031); statues give contents when broken (zap.c:2288; dig.c:449). Propose: "Break the statue open (force bolt, wand of striking, or a pick-axe applied to it)".
- L1959-1961 mirror "you need to be adjacent": mirror uses bhit with full range (apply.c:1096); real condition is she must be awake (apply.c:1112-1115), and every layout generates her asleep (medusa-1..4.lua). Propose: "reaches down a straight line like a wand, but she must be awake and looking your way, so she gets gaze turns first: riskier than passive reflection."
- L1670-1672 Sokoban penalty "clears the moment you legitimately finish the level above": no such mechanic; sokoban_guilt is change_luck(-1) (trap.c:7039-7054); Luck drifts to zero 1 per 600 turns (timeout.c:606-619), luckstone freezes it.
- L1557-1559 mind flayer "any random Mines level outside Minetown and Mine's End": Mine's End rolls one too (minend-1.lua:119, minend-2.lua:159); filler levels half the time (minefill.lua:44).
- L1553-1554 "If you're playing a gnomish character": dwarves get the same peace (role.c:634, 654).
- L1572-1574 Minetown donation "at least the amount the priest names ... a point": two amounts named (priest.c:645-646); protection needs the larger; first grant 2-4 (priest.c:695), as L4462 says.
- L1812-1817 Quest refusal "climb back out, mend your standing, and return": expelled automatically (quest.c:349-353, 186-198); same below XL14 (333-336); alignment-converted hero banished permanently (337-341).
- L1978-1980 "Ice is safe to walk on": each step 1 in 2 slip (1 in 3 with cold res), two helpless turns (hack.c:2396-2411; timeout.c:905-907); zapped ice melts after 50-2000 turns (zap.c:5319, 5081-5082).
Checked correct: Mines 2-4, Oracle 5-9, Sokoban 6-10, Quest 11-16, Rogue 15-18, Ludios placement, Medusa 21-28, Orcish Town 1/7, Ludios garrison/treasury, Perseus odds, Sokoban 75/25, Bell on nemesis.
Style (AI-filler): L1511 "Slashing through the Mines early is exciting, but patient players return stronger and better equipped" -> "The Mines are a fairer fight after Sokoban: you come back with reflection or a bag of holding and a few more levels." L1788-1793 "your role's signature relic, attuned to you as no other item in the game can be, and it tends to anchor your kit ... Each carries a blend of powers suited to its owner" -> "Most quest artifacts are worth carrying for the rest of the game; each gives some mix of magic resistance, telepathy, warning, reflection, or luck." L1597-1598 "which affects everything from combat to fountain wishes" -> "Luck feeds your to-hit rolls, your prayers, and every wish." L1897-1899 Ludios "good place to visit for gold, identification scrolls, or shop stock, but it's not essential for victory" (no ID scrolls placed in knox.lua) -> "None of it is required to win; the gold is the reason to come, and it buys protection from priests." L1685-1686 "the HP penalty isn't worth what you'd gain" dismissive + wrong mechanic (Stressed stops regen while moving, allmain.c:629; loss begins at Strained). L1578-1579 candles corrective-hedge opener duplicating L9252-9254. L1592 "they'll call for reinforcements" invented -> "Anger one and the whole watch turns on you." L1656 "pit traps are inescapable" -> "pits can't be avoided". L1610 em-dash. L1885-1886 "The level is non-diggable. The level prevents teleportation" -> one sentence.
Craft: Sokoban cheat list/penalty at L1648-1655 and L1668-1673: merge. Sokoban opener (L1616) is a locator; lead with the prize. Medusa: gaze checklist before Perseus loot. Minetown watch (L1590-1592): add door-breaking/digging trigger. Fort Ludios (L1877-1899): split "What's inside" / "The prize"; move escape rule up.
Top 3: fix Medusa list/#loot/mirror; fix Quest refusal + Minetown donation; merge Sokoban text, replace "penalty clears" with 600-turn drift.

---

## Chunk 6: Traps and Hazards + Feelings and Sounds (L2029-2666)
Verdict: strong practical chapters; Elbereth material (L2447-2542: defile rule, scare-monster comparison) best. Feelings table least audited: wrong attributions, mixes emergencies with trivia.
Correctness:
- L2646 "monsters have difficulty pinpointing your location ... Stealth just turned on": that is the cloak of displacement toggle (do_wear.c:148-176).
- L2647 pet kill "-15 alignment and your god is now angry. Expect prayer to backfire": adjalign(-15) and change_luck(-1) only (mon.c:3664-3665, 3703-3708); no anger; prayer fails until the record climbs back above zero.
- L2183 magic trap "uncurses your whole inventory": uncursed remove curse, worn and wielded only (trap.c:4430-4443).
- L2177 "Sleep resistance (elven blood, the right ring)": no ring grants it; elves, orange dragon armor, corpses.
- L2616 "gnome miner" digging sound: gnomes don't tunnel; dwarves, rock moles, umber hulks.
- L2363-2366 "Monster traffic doesn't smudge it ... lasts indefinitely": every monster step chips a scratched engraving 1 in 26 (monmove.c:734; engrave.c:280-288); dust erodes while you stand there (allmain.c:360-361).
- L2352 "'Elbereth' costs about -4": dulling truncates at -3; a +0 blade yields "Elberet" (engrave.c:1355-1380); +1 or better finishes the word.
- L2194-2197 teleport trap "press Ctrl+T first": only fires a discovered trap under you (teleport.c:1041-1060); step on it, then Ctrl+T.
- L2642 "It tasted bad." / can't rise off: message is "You have an uneasy feeling." (potion.c:1092-1107); "It tasted bad" unreachable.
- L2650 "wizard, demon, lich ... summoned a monster": that message is the clerical insect/snake summons (mcastu.c:645, 685-697); mage summons print "Monsters appear from nowhere!"
- L2653 "just left your awareness ...": printed by wand of secret door detection clearing an I marker (zap.c:2557; detect.c:1792-1881).
- L2654 "...working on your reflexes!" ends with a period; L2660 "You are turning into slime." is "a green slime."; L2617 "A rumbling stop abruptly" full text "You hear a rumbling stop abruptly."; L2395 "Ad aerarium" lowercase and aged five characters (mklev.c:733, 768-772).
- L2632 "Eye of newt corpse": plain newt corpse.
- L2649 water demon "isn't visible to you yet": blind only, demon already adjacent (fountain.c:69-74). Cut.
- L2300 "Rangers have the Searching skill from the start": Archeologists too; intrinsic not skill.
- L2245-2246 levitation "still trigger magic, teleport, and anti-magic traps": also polymorph, level teleport, webs (trap.c:1061-1080).
- L2050-2052, L2244, L2255 pets "hesitate to step on traps it knows about": pets avoid only traps YOU have discovered (dogmove.c:1195-1207); reveals nothing. Cut all three.
Checked correct: magic-trap odds, anti-magic damage, polymorph/iron-shoe blocks, trapdoor cascade, bear-trap escape, search odds rnl(7)/rnl(8), scare-scroll pickup, Castle chest, onscary exclusions, hypocrite penalty, other quoted messages.
Style: L2600-2602 restatement -> "Many odd little messages are precise signals; this table decodes the ones that matter." L2604-2607 deaf caveat + Permadeaf jargon; cut. L2150-2153 "threaten your pack, not just your health ... the real catastrophe" -> "A fire trap burns the scrolls, potions, and spellbooks in your open inventory; the hit points are the smaller loss." L2158 "a double-edged sword" cliché. L2174-2176 "is murder ... You can't fight, you can't run, you can't even wake up ... like it's a buffet" -> "Sleeping gas leaves you helpless for a stretch of turns while everything nearby takes free swings." L2204-2205 "(only one counts; the check breaks on first match)" implementation talk. L2212-2213 "in 5.0" meta. L2470-2472 "anything intelligent enough ... anything that can't perceive ... anything with nothing to lose" triplet re-saying the list; cut. L2314-2319 "The wisdom of patience ... the Mazes' way of teaching you" lesson framing; cut. L2518-2521 "Never engrave ... anything — Elbereth included — engraves nothing" -> "Don't engrave on an altar or a grave..." L2566-2568 heavy iron ball vs bars rarely actionable; a wielded war hammer works (mthrowu.c:1471-1487). L2641 second quote fires only for names starting "Maud".
Craft: Feelings table (L2609-2661) 51 unsorted rows: split into Emergencies / Level sounds / Corpse intrinsics / Item identification. Dangerous Traps table (L2139-2148): add a "Blocked by" column. Traps opener (L2045) opens with a definition; lead with the stake (separation from pet and stash). Engravings durability belongs in one place (L2357-2369) with Elbereth pointing back. Best: defile rule L2476-2494; scare-monster comparison L2527-2542.
Top 3: fix mis-attributed messages; fix engraving durability + Ctrl+T; regroup Feelings table, cut pet-avoids-traps advice.

---

## Chunk 7: The Art of Combat (L2667-3100)
Verdict: teaches the right instincts (speed-ratio rule L2790-2804; retreat-and-regenerate L3043-3053) but the arithmetic is the weak part: to-hit formula stated backwards, AC -20 promise false, several tactical claims wrong; life-saving tactics buried under 250 lines of formulas.
Correctness:
- L2716 "roll at or above (10 + defender's AC - your modifiers)": backwards, no 10. uhitm.c:376-378 sums 1 + Str/Dex bonus + target AC + Luck/3 + level (+ enchantment, skill); uhitm.c:780-781 hits when total exceeds d20. Propose: "Add one, your level, your Strength and Dexterity bonus, about a third of your Luck, your weapon's enchantment and skill bonus, and the target's AC. You hit when a d20 rolls under that total."
- L2755 "At AC -20, almost nothing hits you": negative AC is rolled (hack.h:1538 -rnd(20)); mhitu.c:709-710 adds 10 + monster level. Ogre (L5) connects ~1 in 4; level-15 monster 2 in 3.
- L2767 "extrinsic Protection bought from priests of your alignment": no alignment test (priest.c:681-699); book's L4460/L4497 call it intrinsic and cross-aligned.
- L2836 "Overtaxed ~1.5": integer math 12-10 = 2 (allmain.c:149).
- L2839 "At Stressed, a speed-6 zombie acts more often than you": Stressed is 6 (allmain.c:143), zombie 6: a tie; Strained = twice.
- L2883 "Rangers stay unskilled (-9)": Rangers cannot two-weapon at all (mondata.h:129-132; monsters.h:3405-3408; wield.c:765-771). Tourist caps Skilled, Archeologist Basic (u_init.c:521, 275). Propose: "Rangers, Healers, Monks, and Wizards cannot use two weapons at all."
- L2902 "a cursed weapon in either hand jams the whole arrangement": only off-hand, slips to floor (wield.c:797-800); artifacts refused as off-hand (791-793).
- L2945-2949 multishot: Skilled +1, Expert +2 (dothrow.c:177-185); count is rnd(max) (dothrow.c:233): Expert Ranger 1-4, avg ~2.5.
- L2989 "ordinary monsters cannot follow you up or down stairs": adjacent stalkers follow (mondata.c:1224): soldiers, watchmen, vampires, trolls, wraiths, imps.
- L3003 "jumping boots (use a)": command is #jump (apply.c:1988).
- L3029 "Sleeping monsters stay asleep while you walk past": 1 in 7 per turn wake within 10 squares in view; dogs/humans at once; Stealth prevents (monmove.c:341-352).
- L3096-3097 "lock a Knight or Samurai out of the Quest for the rest of the run": caitiff/giri -1 each (uhitm.c:341, 345); record climbs back with hostile kills (mon.c:3725).
Checked correct: Luck cap, two-weapon table, role caps, two-handed 3/2, speed tiers, encumbrance order, regen rates, growl radius, ammo breakage, crossbow Str gates, conflict Cha, hypocrite penalty, cornered monsters, ranged retreat.
Style (AI-filler): L2734-2739 "This narrows the gap ... considerably ... measurably more damage ... run those numbers again" -> "At 18/100 Strength the +6 bonus becomes +9 on a two-handed sword, so d12+9 beats a long sword's d8+6 by about five points a swing." L2823-2824 "a worn passive that costs no inventory slot and no spell-pool drain" gamer jargon -> "Speed boots are the easiest way: put them on once and stop worrying about potions and spell energy." L2960-2962 "thinking about where you stand, when you swing, and what happens if it goes wrong" decorative triplet previewing sub-headings: cut. L2954-2955 "best damage budget in the game" -> "will carry a Ranger through the midgame." L3025 "the best damage soak in the game" + L3023 "absorbs one hit per round" not a mechanic -> "A pet next to the monster draws some of its attacks and adds its own." L3087-3088 "be ready for it to make a decision about that arrangement" -> "expect it to turn and fight." L2977-2978 "spends a turn rounding the corner, and you get a free hit" -> real effect (monmove.c:945-955): a monster stepping adjacent doesn't swing that action. L2967/L2986 "Never fight a mob"/"Never let yourself be surrounded" -> softer. L2991-2992 "your retreat consumables". L3007 "non-fire/non-portal/non-Sokoban trap" slash-list. L3072-3084 version-diff framing ("now back away", "no longer works", "This change"). L2815 "two probabilistic tiers".
Craft: ordering (L2705-2957) formulas first, tactics last; move "Fighting Smart" ahead or add a five-line short version after L2703. Speed centaur example at L2793-2796, L2860-2863, L2980-2984 (three times). Two-handed bonus at L2731-2739 and L2892-2894. "Edge cases worth knowing" (L3070) are core behaviour. Best: "Divide before you engage" (L2790-2804).
Top 3: fix to-hit direction + AC -20; fix stairs/sleepers/Rangers; reorder tactics before formulas, cut duplicated speed/two-handed passages.

---

## Chunk 8: Things That Will Kill You (L3101-3650)
Verdict: the book's most useful chapter; strongest mimic "Sticking" (L3393-3402), nymph "Already robbed?" (L3350-3354). Weakest: "Deadly Mistakes" (frequency claim and wand entry don't match server data), "A note on dragons" (scale-mail catalogue, no "what to do about a dragon").
Correctness:
- L3191-3193 sleep resistance from "Wizard's cloak of MR, Ranger's elven cloak": neither (objects.h:616, 644-646); elves at XL4 (attrib.c:94-95).
- L3232-3233 water demon "attack first and grant a wish only if you survive": roll at summoning; success = wish at once and demon vanishes (fountain.c:78-84).
- L3250-3251 demon summoning "Every melee hit 1-in-13": once per attack round hit or miss, 1 in 16 outside Gehennom, 1 in 10 inside (mhitu.c:733, 966-969).
- L3256 "sorted roughly by frequency on the public server" + L3292 "Killed by your own wand": alt.org ranks: mount slips 13, rotted corpse 17, shopkeeper 19, kitten 23, grid bug 54, choking 63, boiling potion 75, wrath 77; "zapped herself with a wand" rank 109; "killed by a wand" (rank 12, 45,574) = a monster zapping striking at you. Re-aim the entry.
- L3277 pony "coin flip": slip when XL + tameness < rnd(20), mounting spends a tameness point (steed.c:308, 338-341): fresh pet at XL2 slips 9 in 20; barely tame ~17 in 20.
- L3284-3286 "shatters any potion you drop ... the shrapnel is deadly": hot ground breaks ~half of dropped potions, no damage (do.c:318-353); "boiling potion" death is fire heating potions in your pack (zap.c:5781, 5842).
- L3302-3304 sink "or worse"/"Kicking doors can break your toe": third sink outcome is a backed-up drain; failed door kick is harmless "Whammm"; HP/wounded legs from kicking walls (dokick.c:889-903, 960-966, 1235-1237).
- L3335-3338 nymph claws "one lifts an item, the other peels a worn ring": both claws same theft routine (uhitm.c:4756-4799).
- L3414 "a werewolf destroys your body armor, cloak, and shirt": cloak's clasp breaks and it drops intact (polyself.c:1188-1192).
- L3441 "athame" among silver/wooden weapons: iron, splits puddings.
- L3443-3444 "Wands of cold and fire kill puddings": brown and black puddings resist cold (monsters.h:2097, 2118).
- L3460-3461 globs "each bite is an independent roll": one roll per finished glob; same-kind globs merge.
- L3490 "Yellow dragons are rare": all dragons frequency 1.
- L3516 dragonhide "resist disenchantment naturally": no exemption (zap.c:1382-1394); it never rusts/corrodes/burns.
- L3534-3535 troll corpse "wand of teleportation ... off-level, or destroy it with a wand of striking": teleport moves it on the same level; striking breaks only glass-like objects. Cut both.
- L3554-3555 level drain "stat points ... no easy undo": loses max HP, energy, a skill slot, no attributes (exper.c:227-278); restore ability gives levels back (potion.c:687-691).
- L3563 "Wraith corpses spoil quickly": ordinary rot.
- L3529 "the same five trolls": about three in four revive (hack.h:1405).
Checked correct: 0.4% ascension; top-ten list; bats/ravens/centaurs/rothes/mumakil/minotaurs/lights/Olog-hai stats; mimic speed/colours/escape; pudding globs 500 turns; seduction odds; reverse-genocide 4-6.
Style: L3171 "The shape of the threat is usually pack tactics, surprising speed, or one catastrophic special attack." -> "They come in packs, move faster than you, or have one attack you can't afford to take." L3201 "The defense is positioning, not HP totals" -> "Fight from a doorway so they can't circle you, or kill them at range." L3321 "The median death is a preventable swarm of jackals on Dlvl 3." invented statistic; cut. L3474-3475 "most likely to make you regret trying" -> "their breath is magic missile, so a cloak of magic resistance makes the hunt safe." L3478 "The second pillar of not dying to wands." L3502 "A pair of niche defenses in one slot." / L3506-3507 "One of the most powerful body slots in the game." cut. L3527-3528 "is a timer, not a kill count" -> "About three troll corpses in four get back up within fifty turns." L3572-3574 "Some ascending heroes credit a wraith binge..." testimonial; cut. L3183/L3193 sleep resistance before the Mines rarely actionable. L3340/L3356 "never" imperatives. L3383 "Telepathy, ESP" same thing. L3224 "the endgame model" designer jargon. L3622 comma splice. L3645 em-dash.
Craft: Minotaurs (L3242): add that they ignore Elbereth (monmove.c:284-287). Dragons (L3466): add the breath rule (reflection or matching resistance; MR stops gray). Trolls (L3531-3537): eat, tin, pet, lava. Deadly Mistakes: lead with mount slips and monster wands.
Top 3: fix water-demon timing, puddings/cold, sleep-res sources, troll disposal, restore ability; re-base Deadly Mistakes; dragon threat briefing.

---

## Chunk 9: Saving and Bones + Ways to Die Instantly (L3651-4277)
Verdict: instadeath catalog scannable; Petrification (L3985-4024) best. Weakest: "Saving Yourself" appendix (L4228-4275): lava backwards, lethal "cure" for food poisoning, contradicts Drowning/Choking above. Bones has wrong details.
Correctness:
- L4257-4258 lava "without levitation or fire resistance gives you a few turns": without fire res you burn on contact (trap.c:6811, 6871-6935); WITH fire res you sink, 12-15 turns (trap.c:6964-6973, 7010-7016).
- L4247-4248 food poisoning "or vomit (by being satiated and eating more)": that is the choking death; vomiting is its 1-in-20 escape (eat.c:258-267, 3296-3299). Real cures: extra/full healing non-cursed, blessed healing (potion.c:1122, 1131-1132, 1147).
- L3715-3717 bones "80% cursed, even items in containers": containers untouched (bones.c:274-300).
- L3999-4000 acid blobs "a few hundred turns of resistance": 1 in 6, 3-18 turns (eat.c:994-996, 1094).
- L4029-4030 cockatrice corpse "handles demon lords, Medusa, and even a Rider": Medusa and Riders resist stoning (monsters.h:2842, 3149, 3159, 3169).
- L3912-3914 "Dragons and purple worms can swallow": no dragon engulfs (monsters.h:1484-1494).
- L3782-3786 warning shot: monsters native to Castle/Ludios/Quest/Gehennom/Vlad's/Planes never miss the first shot (makemon.c:1291-1293; muse.c:1830-1834).
- L3892-3894 mind blast "only fires if you have telepathy": locks on every time if sensing by telepathy, 1 in 2 with unused telepathy, 1 in 10 otherwise (monmove.c:599-601).
- L4180-4181 touch of death "MR fully blocks this branch": with MR the 17-19 roll falls to the smaller drain (uhitm.c:3862-3872); outright death only if half the damage >= max HP (mcastu.c:326-352).
- L3845-3846 system shock "10 to 34": 6+4d6 = 10-30 (attrib.c:365); dies when current HP <= roll.
- L4264-4265 drowning "a few turns to escape": next landed wrap drowns (uhitm.c:3389-3396), as L3945 says.
- L4272 strangulation "slowly kills": six turns (do_wear.c:1040).
- L3696-3698 bones levels: Quest filler/locate carry bones (dungeon.lua:196-216); all three Vlad's levels lack them (262-283).
- L3702-3704 "This place looks familiar": only for your own past character (do.c:1448-1454); overview lists "Final resting place for..." (dungeon.c:3253-3260).
- L4062-4064 disintegration "then your body armor": cloak goes with it (zap.c:4480-4485).
- L4231-4232 "digested by [green slime] as a polyform": no source; cut.
- Minor: L3875 "(3 for humans)" is every race; L3924 "(no direction needed)" you are asked, any works.
Style (AI-filler): L3753-3758 "Not by whittling down ... not by wearing you down ... but by ending your life ... the difference between a promising run and a one-line epitaph" -> "Some things in the Mazes kill you in one move no matter how many hit points you have. Players call them instadeaths, and nearly every one gives a warning a turn or two ahead if you know what to look for." L3729-3733 triplet with opaque third item -> "Whatever killed the previous adventurer is usually still there, and often far too strong for the depth." L4124-4125 "the silent ascension-killer it's reputed to be, but the mechanic is more constrained than common lore suggests" meta. L3821-3822 "starvation is a real threat" hollow. L3886 "plan any drawn-out mind flayer fight carefully" vague. L4242 "Fire is the most reliable cure" restates. L4233 "Dead." / L4213-4214 "Don't do this." fragments. L3681-3684 "anti-scum mechanism... what the community calls" designer framing. L3805/L3846/L3811/L4178-4183 "the choke check fires", "roll fires", "timer death", "Rolls 17-19" implementation talk -> percentages. L4092-4094 "Enchantment Drain covers its cousin" muddled. Rarely actionable: L4016-4018, L3926-3928, L4239-4240. L4028 lowercase after period.
Craft: Attack Wands (L3777) never names reflection/MR. Petrification (L3991): split instant triggers (touch, eat, kick, Medusa gaze) from countdown (hiss, thrown egg). Saving Yourself appendix (L4216): Drowning/Strangulation/Choking already above; table (threat, message, turns, cures). Enchantment Drain (L4106) not an instadeath. Genocide (L4205) no prevention rule. Audit comments at L4146-4157, L4196-4204 under wrong headings.
Top 3: fix appendix (lava, vomiting, drowning); fix bones + stoning claims; warning-shot exceptions + reflection/MR in Attack Wands; split Petrification triggers.

---

## Chunk 10: Divine Relations + Making Friends (L4278-4751)
Verdict: prayer and turning read cleanly; pet chapter has the book's best light touch (L4593 "a self-propelled, self-feeding trap detector with teeth"; #chat table L4632). Weakest: sacrifice-gift paragraphs (L4413-4446) misexplain the source in three places; priest "walk away" advice (L4500-4503) backwards. Prayer gives a checklist of invisible quantities, not a rule.
Correctness:
- L4413-4416 "your god expects more impressive offerings as you advance ... 'feeling of inadequacy'": value = difficulty+1, nothing scales with XL (pray.c:1839-1849); the message fires only when god is angry and the corpse too small (value < 8, < 12 chaotic; pray.c:1959-2060).
- L4404-4405 sacrifice "pays out as artifact weapons, holy water, restored alignment, and eventually a crown": holy water and crowning come from praying, not sacrificing.
- L4433-4434 "second gift is more like 1 in 16 to 1 in 26": 1/(6 + 2*gifts*artifacts) (pray.c:1792): 1 in 8 with one artifact in existence.
- L4438-4446 first-gift "bias"/"Worthiness floor": role artifact is the ONLY candidate, ignores the value cap, takes your alignment (artifact.c:92-95, 195, 212-216); others roll among alignment artifacts capped by corpse value (prices 1-10; corpse unlocks up to difficulty+1: newt 2, dwarf 5, soldier ant 8, troll 10). "Sacrifice early before the pool dilutes" has no basis. CONFIRMED by editor.
- L4477-4478 "politely thanked but not blessed": a rich hero offering the base is called Cheapskate, counter rises (priest.c:660-664).
- L4500-4503 "decline the prompt entirely rather than offering a token sum": declining = offer 0, costs 1 alignment AND increments cheapskate (priest.c:655-659; minion.c:376-378). -> "Don't chat unless you can pay the first number. If you must lowball, offer at least half the gold you carry."
- L4457-4459 "A few hundred turns" of clairvoyance-ish: 500-999 turns per suggested amount (priest.c:673-674).
- L4514-4515 altar "if your god is already angry, converts you": test is negative alignment record (pray.c:1638-1640).
- L4519-4522 "a pair of hostile minions": one minion, on failure too, only at XL 8+ with high record (pray.c:1680-1694).
- L4539-4548 crowning "if one is available... class-specific bonus": lawful gets no sword unless wielding a long sword; Wizards and Monks get the spellbook instead (pray.c:822-956).
- L4550 crowning "adds ~1000 turns": every later prayer adds rnz(1000) (pray.c:1356-1361).
- L4396-4397 "Spellcasters get the same from the turn undead spell": a directional bolt that makes one undead flee (zap.c:244-260); works in Gehennom.
- L4614-4616 tameness "decreases when they go hungry": hunger confuses, cuts max HP, then kills; tameness untouched (dogmove.c:10-12). Only separation, your blows, leash-dragging lower it (dog.c:689-696, 899, 1360-1375).
- L4726-4728 "Sokoban also doesn't let pet loyalty decay": no such exemption. Cut.
- L4656-4658 purple worm "growing tail": long worms have the tail.
- L4709 Archon "magic resistance": that's its saving-throw stat.
- L4718-4719 "; to farlook" for pet health: compiled out (pager.c:138-160); stethoscope.
- L4739 "better-armored" from eating: resistances only (mon.c:1726).
- L4609 message is "steps reluctantly onto" (dogmove.c:1307). L4589: Knights start with a pony.
Style: L4313-4314 "When conditions are right... When conditions are wrong, it can kill you" parallel -> "Prayer can pull you back from stoning, starvation, or near-death, but a prayer your god isn't ready for brings punishment instead, sometimes fatal." L4353-4354 "some forgiveness if your timeout is close to expiring" -> "for a major trouble you may pray with up to 200 turns still on the clock, 100 for a minor one" (pray.c:2146-2150). L4357-4359 "unless you worship Moloch, which no standard role does ... one of the things that makes Gehennom so dangerous" cut both. L4521-4522 "arriving just as you exhale ... the 'victory' comes with company" ornament. L4524 "Two things to never sacrifice" imperative + repeats L4419-4422. L4598-4599 "a genuine combat asset" hollow -> "kills the dwarves and soldier ants that give a low-level hero trouble." L4610 "That message is a giveaway." cut. L4624-4627 "Always pick them up ..." -> "Pick up tripe rations: revolting for you, a feast for a dog or cat." L4649-4650 "both route through the same handler" implementation talk -> "both tame everything in the 3x3 around you." L4672-4673 "free, reliable, and available from turn one" triplet ("reliable" contradicts L4603) -> "free from turn one". L4734 "Current editions added two things worth knowing. First:... Second:..." scaffolding. L4743-4746 vague -> "It is an ordinary prayer, so with no trouble of your own the timeout must be fully expired, and the corpse must not have rotted." Rarely actionable: L4695-4696 warhorse "early"; L4706-4708 Archon via whistle/conflict accident (conflict tames nothing).
Craft: Prayer (L4368-4378): boxed rule: "Pray when you are in a listed trouble AND (a) you have never prayed and it is past turn 300 (100 if major; you start with a 300 timeout, u_init.c:1005), or roughly 1000 turns since your last prayer, AND (b) you have not killed a peaceful or been told your god is angry, AND (c) you are not in Gehennom or on another god's altar." "Count roughly 500 turns" (L4375) fails one prayer in eight. Enlightenment prints "You can safely pray" (insight.c:1943-1953). Sacrifice (L4427): payout order with messages (angry god "mollified" -> negative alignment "partially absolved" -> timeout "hopeful feeling"/"reconciliation" -> Luck and gifts; pray.c:2026-2115); sacrificing right after a prayer never rolls for a gift. Upgrading your pet (L4690): "Three moves" precedes four bullets; whistle repeats at L4725.
Top 3: boxed prayer rule; rewrite L4427-4446 (role guarantee, price-vs-corpse cap, odds, payout order); fix cheapskate advice + cut four pet myths.

---

## Chunk 11: A Practical Identification Strategy (L4752-5595)

Verdict: gives a usable order of operations (flowchart L4772 + "A Practical Strategy" L5562-5592 agree: altar -> shop -> engrave -> careful use -> identify). Prices almost entirely correct. Strongest: The Engrave Test (L5254-5282). Weakest: The Price Is Right (L4866-4937): simple rule buried under three explanations of the sucker markup and three paragraphs of shopkeeper relations; throw/chat tips half wrong.

Correctness:
- L5059 "flame sphere ... freeze sphere" spellbooks: deferred (#if 0, objects.h:1413-1422). Propose: "confuse monster, detect monsters, force bolt, healing, jumping, knock, light, protection".
- L4796-4798, L4844-4846 "blessed scroll identifies at least 2 items": read.c:2084-2092 rn2(5): 0 = everything (1 in 5), else 1-4; roll of 1 becomes 2 only with positive Luck. Uncursed: one item 4 in 5, blessed table 1 in 5. Propose: "A blessed scroll identifies one to four items, or one time in five your whole pack; with positive Luck the minimum is two. An uncursed scroll usually identifies one item, and one read in five rolls the blessed table instead."
- L4840-4841 "praying on a co-aligned altar while carrying potions of water": water_prayer walks the altar square, not inventory (pray.c:1393-1400). Propose "dropping potions of water on a co-aligned altar and praying".
- L4832-4835 autocurse list: only helm of opposite alignment and dunce cap self-curse on wear (do_wear.c:462-482); gauntlets of fumbling and levitation boots don't (they're 9-in-10 cursed at creation, mkobj.c:1086-1092, which tests catch).
- L5043-5047 closet tip: scroll only in doorless niche (mklev.c:779-795); "ad aerarium" niche is separate with secret door, no scroll. Propose: "a single unidentified scroll in a sealed one-square niche off a room, no door at all (sometimes iron bars), is a scroll of teleportation, left so anyone who lands in there can leave. One time in three a random object lies beside it."
- L5327 "or sling stones" poisonable: no (obj.h:264-268; flint/rocks are gems). Drop.
- L5347 levitation "a few hundred turns": uncursed 10-149, blessed 250-299 with > to descend (potion.c:1208-1215).
- L5494-5495 "$60 gray stone is a luckstone": surcharged touchstone (45 x 4/3 = 60) also quotes $60 (shk.c:2864-2872, 2941-2944). Propose: "$80 or $60 is a luckstone unless a touchstone drew the surcharge (also $60); $45 is a touchstone for certain."
- L4915-4917 shopkeeper anger causes wrong ("fired a wand from a doorway", "picked up unpaid item while broke"): real causes: attacking (mon.c:4355-4360), zapping a wand at them (zap.c:555-557), leaving with unpaid goods (shk.c:3868), refusing to pay for damage (shk.c:5170, 5242, 5343).
- L4878-4880 throw-into-shop quote trick: no quote from outside (dothrow.c:1181-1214); shopkeeper pockets it (shk.c:4372-4393). Real free quote: stand on item and press `:` (invent.c:4282, objnam.c:1666-1673) or #chat on it (sounds.c:1280-1289).
- L5263 "Drop the wand on an aligned altar, hand it to a priest": any altar flashes (do.c:379-382); no handing to priests.
- L4890-4891 "the Charisma bands in the table above": table is below (L4998) and print-only.
Checked correct: all scroll/potion/ring/wand/amulet/armor/gray-stone prices; Charisma bands; sucker multipliers; 1000-gold buy-off; engrave messages; unicorn-horn dips; loadstone message.

Style: L4815-4816 "tells you something about clerical paranoia" -> "(Priests are the exception: they sense it at a glance, an occupational habit.)". L5279 "Don't be afraid of the suspected wand of wishing." -> "A suspected wand of wishing is safe to engrave-test." L5436-5437 "can ruin a run" -> specific consequence. L5472 "flint is useless ammunition" dismissive -> "flint is sling ammunition". L5584-5586 "the most lethal mistake on the identification table" -> "(a botched read can paralyze you for many turns among whatever is nearby)". L4928-4929 "minus the usual surcharge" reads as removed; it stays.

Craft: BUC identify-scroll rules appear twice (L4796-4800 vs L4844-4850). Price Is Right: lead with L4898 one-liner (average Charisma quotes base; sell is half), one markup paragraph; sucker condition explained at L4885, L4901, L4979-4996. After a fight / Invisible (L4923-4937) belongs in Shopping chapter. Armor Prices table (L5423-5431) missing helms ($10 plain vs $50 opposite alignment/telepathy). Engrave Test step 1: explosion odds 1 in 100 (engrave.c:794). Gray stones rule (L5516-5517) "Check BUC second" on floor stone = pet test. Best: engrave procedure L5265-5272; shuffled-armor pools L5397-5419.

Top 3: fix decision-changing slips (identify counts, holy water on altar, autocurse list, sealed niche, $60 touchstone); rewrite price-quote paragraph around `:` and #chat, lead with base-price rule; consolidate sucker-markup explanations, move shop-relations paragraphs to Shopping.

---

## Chunk 12: Provisions and Dining + The Apothecary (L5596-6025)
Verdict: reads well; hunger opener, corpse table, holy-water manufacture best. Weak: false "plain, eat freely" verdicts (pets, nymphs, leprechauns, stalker, i), stoning cure filed under sickness, two potion rows describing blessed behaviour 5.0 lacks.
Correctness:
- L5732-5735/L5760 cats and dogs "eat freely/plain": kitten/housecat/large cat/little dog/dog/large dog give permanent aggravate monster unless Cave Dweller or orc (eat.c:814-826).
- L5734 leprechauns/nymphs "no effect": teleportitis at level/10 odds (eat.c:936-938, 974-988): leprechaun 1 in 2, nymph ~1 in 3.
- L5773 "Stalker -> invisibility + see invisible": visible eater gets 50-149 turns invisibility + stun; permanent + see invisible only if already invisible (eat.c:1162-1178).
- L5764 "i ... Mostly no corpse": imp/homunculus/quasit/tengu leave corpses (monsters.h:552, 560); homunculus poisonous, conveys sleep/poison res; tengu teleportitis/control.
- L6010-6012 "Eating a lizard or acidic corpse also cures it" under Sickness: cures stoning not sickness (eat.c:827-830, 860-861); food cure for sickness is eucalyptus leaf (eat.c:2576-2578). Add a Stoning bullet.
- L5873 enlightenment "blessed tells more": identical readout; blessed +1 Int +1 Wis (potion.c:802-806).
- L5858 see invisible "permanent when blessed": 1 in 10 permanent, else 750-849 turns (potion.c:844, 867-870); booze/fruit juice $50 (objects.h:1165-1169).
- L5682 lembas "Elven characters find these more often": no generation bias; elves 1000 nutrition, orcs 600 (eat.c:345-349).
- L5983-5984 alchemy "The dipping potion is the one that breaks": target always used up (potion.c:2538); blast destroys dipped batch too (potion.c:2432); dipped potion's curse triggers it (potion.c:2419).
- L5923 fountain dipping "where you stand safely": every dip rolls the fountain table and dries it 1 in 3 (fountain.c:458-481, 203-204, 553), as L1282 says.
- L5911-5913 "pray, and the gods bless it": only a SUCCESSFUL prayer (pray.c:2334-2339); water must be on the altar square (pray.c:1393-1396).
- L5803-5804 pudding globs "re-rollable chance": globs merge on drop/pickup (do.c:303-314; invent.c:928-930); one roll per finished meal (eat.c:562) -> eat off the floor one at a time.
- Minor: L5640-5641 "on odd turns" -> "about every other turn" (eat.c:3182-3192); L5697 cursed spinach lowers Str (attrib.c:215).
Style: em-dashes in cells L5747, L5759, L5777. L5800-5802 "(a 5.0 food-handling detail that doesn't change the strategy)" meta. L5903-5906 "trading blows vs hitting twice before they swing once" overstates Fast (free action ~1 in 3, allmain.c:129-132). L5668 "Never eat old corpses" duplicates L5666. L5652 "Eat NOW or die." shouty.
Craft: Dangerous Foods (L5706) needs a five-line safe-to-eat checklist (fresh under 50 turns; not c or Medusa; not green slime; not own race; not dog/cat; then check table). Potion table BUC notes only where they change a decision. Neutralizing Ailments (L5986) most useful page; add Stoning bullet; lizard also cuts confusion/stun to two turns (eat.c:1237-1241). "Eat the puddings" (L5798-5804) repeats table. Best: hunger opener L5628-5632; holy water L5911-5924.
Top 3: fix corpse table verdicts; stoning bullet + safe-to-eat checklist; fix see invisible/enlightenment/alchemy + prayer-safety/fountain caveats.

---

## Chunk 13: Scroll Rack + Wands (L6026-6533)
Verdict: scroll half tight and decision-driven; "Confused Reading" (L6211-6249) is the model template. Wand half weaker: three overlapping recharging/wresting treatments; Max Charges column wrong for the two wands that matter; "Polymorph as a Tool" has invented HP mechanic and invented cursed-control rule.
Correctness:
- L6226-6228 confused remove curse holy-water trick: only a BLESSED scroll reaches carried water (read.c:1549-1557); unblessed touches worn/wielded only. Propose: "Confused remove curse, if blessed, gives every uncursed item in your pack a 25% chance of turning blessed and an equal chance of turning cursed (unblessed, it touches only what you wear and wield)."
- L6086 "above +6" -> "+6 and up" (wield.c:999-1000); contradicts L6122.
- L6338 Wishing Max Charges "3": generated with 1 (mkobj.c:1116-1117); recharge adds 1. Propose "1".
- L6325 Stasis "15": fresh 3-6 (mkobj.c:1118-1121); 15 is recharge cap.
- L6400-6401 make invisible "31-45 turns": self only (zap.c:2836); monsters permanently (zap.c:357).
- L6509-6511 polymorph "HP scales with the ratio, 50/100 -> 200/400": new form rolls d(level,8) full (polyself.c:866-872); own HP returns after. 
- L6518 "cursed polymorph items strip control": no such check (zap.c:2804-2808, potion.c:1689-1692); real caveat: without control a failed Con roll costs up to 30 HP (polyself.c:488-493).
- L6471 wresting "a few tries": 1 in 121 per zap (hack.h:1411).
- L6481-6483 ring charging "+0 or +1 virtually free, cap around +5": explode when spe > rn2(7) (read.c:807): +1 1/7, +3 43%, +7 always.
- L6191/L6205 scare/teleport "any square you can see": also within ~5 squares (read.c:1080-1085).
- L6093 create monster "confused or cursed makes several": 13; confused = acid blobs (read.c:1615-1618).
- L6506 "brown mold form burns": freezes.
Checked: 22 scroll probabilities, wand prices, n^3/343, wishing recharge rules, 1/100 backfire, ray range, stasis 10-30, engrave messages, amnesia, armor cap.
Style: L6104 "read $300 scrolls blind" collides with Blind. L6150-6153 "Never blessed-genocide" + repeat. L6208-6209 "Never price-ID it by reading" muddled. L6386-6390 "Do NOT put this wand in a bag of holding" shouted, twice. L6278-6283 opener defines heading; propose orienting opener. L6312 "NODIR" in table -> "None".
Craft: recharging ladder + wishing rule appear 3x (L6136-6144, L6350-6357, L6454-6490); keep once. Enchant armor L6127-6129: past cap evaporation rn2(spe): +4 ordinary armor dies 3 in 4 (read.c:1178-1188). Death wand L6360-6362 fragments. Sleep ray missing from L6377-6379: bounced sleep = 6d25 turns helpless (zap.c:4454-4461). Lightning engrave blinds up to 50 turns (engrave.c:1248-1250), not in Engrave Test. Punishment row: remove curse frees you. Best: Stasis L6406-6415, Confused Reading list.
Top 3: fix blessed requirement + polymorph claims; fix charge column + make-invisible permanence; collapse recharging to one place, add sleep-ray/bounced-death warnings.

## Chunk 17: Enhancing Skills + Wishes (L8166-8598)
Verdict: strong; two skill tables + wish-syntax bullets exactly right. All 494 role-cap cells match u_init.c (script). Weakest: wish sources list (wand location contradicts Castle chapter; wish budget undercounts), "greased" gloss error. Strongest: enchantment-collapse bullet (L8562-8574).
Correctness:
- L8479 wand "found in the Castle treasure room": in one of four corner towers (castle.lua:142-147); Castle chapter L8977-8986 says the throne-room chest is not the wand chest.
- L8564 "greased deflects nymph theft and Rider grabs": no theft check in steal.c; only u_slip_free for wrap/hug/tentacle (mhitu.c:1047-1083). Same error at L6983.
- L8297 "identify IDs the whole stack": Skilled = blessed scroll = rn2(5) (spell.c; read.c). "several items at once, sometimes your whole pack".
- L8509-8511 wish budget "about four": wand = two wishes with wresting; "about five".
- L8265-8266 message names the category ("weapon skills"/"spell casting skills"/"fighting skills", weapon.c:78-82).
- L8534-8535 "silver damage against everything in Gehennom": silver hits demons/imps/vampires/weres/shades only (mondata.c:524-529).
- L8419 "Thirty slots" vs L8234 32.
Verified: practice thresholds, slot costs, 2 starting slots +1 crowning, bonus tables, unarmed training, riding, Vlad's throne 4/13, Amulet wish, lamp odds, fountain odds, smoky 1/13, enchant collapse, artifact denial.
Style: L8288-8289 "gated by the dmg>1 roll" implementation talk. L8290 "is why ... matters" hollow. L8452-8453 "Anyone else dabbling ... should plan to stop at Basic" dismissive + wrong (Barbarians, Cavemen, Samurai reach Master). L8503-8504 "a very real chance of everything going wrong" hollow, no number (throne 1 in 39 wish). L8531-8532 "overconfidence kills more adventurers than monsters do" death-flourish.
Craft: What to Wish For (L8519-8524) items 1 and 2 both body armor; add "gray if no MR, silver if cloak/Magicbane covers it" rule; Luck check bullet (L8575-8580) should come first; spell upgrades duplicated (L8296-8298, L8455-8458); "Cap-aware investment" (L8429-8432) says nothing to do. Best: enchantment bullet, Skill Ladder table (L8221-8227).
Top 3: fix wand location + wish budget; fix "greased" here and L6983; gray-or-silver rule ahead of wish list.

---

## Chunk 14: Rings and Amulets + Tools of the Trade (L6534-6989)
Verdict: tables scannable; tools chapter has the book's best in-world voice ("Boxes and chests are furniture, not luggage"). Tools half carries many decision-changing slips. Weakest: L6981-6986 grease, wrong on all three examples.
Correctness:
- L6632-6636 ring-juggling hunger trick: 5.0 randomized accessory-hunger trigger to kill it (eat.c:3181-3191). Cut.
- L6628-6629 "Two rings drain food noticeably faster": ring = 1 nutrition per ~20 turns (eat.c:3237-3266); regeneration/conflict/hunger 1 per 2 turns.
- L6682-6683 "Stack with speed boots on the mount": steeds can't wear boots; your speed doesn't augment steed (allmain.c:119-121). -> wand of speed monster on the horse.
- L6762 bag explosion "scatters your inventory": scatters the bag's contents, ~1 in 13 destroyed, 6d6 to you (pickup.c:2515-2534, 2692).
- L6796-6797 "cuts weight to a quarter": blessed only; uncursed halves, cursed doubles (mkobj.c:1950-1953).
- L6792 Overloaded "can't pick anything else up": can't move (hack.c:2629).
- L6817-6823 monsters "unlock chests with keys ... Castle chest can be emptied": refuse locked containers (muse.c:2273, 2768-2770); keys for doors only (monmove.c:94-102); wishing chest locked (castle.lua:144). CONFIRMED by editor.
- L6847-6849 "Never, ever use a magic lamp for light": lit magic lamp never burns down (timeout.c:1722-1724); rubbing ignores lit state (apply.c:1815-1830).
- L6867-6868 non-magical instruments "no special effects": tooled horn/leather drum wake and scare (music.c:639-648, 703-721); drum deafens 30-49 turns.
- L6916-6918 marker "Writing by appearance gives a random scroll": writing by label yields exactly that type (write.c:165-168) once you've seen the label (write.c:313-316).
- L6949-6950 "grind poison or acid resistance": acid res timed 3d6 turns (eat.c:1082-1087), as L13868 says.
- L6958-6959 "most of Gehennom non-diggable": Gehennom fillers dig fine (hellfill.lua); hardfloor only Valley, Sanctum, Wizard's, Vlad's.
- L6964-6965 crystal ball "point at a square or . for the whole level": always whole level (detect.c:1298-1300).
- L6977 "Drop a fresh ball on an altar to bless it": altars reveal, don't bless.
- L6982-6984 grease "nymphs slide off, Riders' grabs miss, weapon-snatch fails": only hug/wrap/sticky/tentacle (mhitu.c:1047-1085); no grease check in steal.c; Riders have touch attacks.
- L6934-6935 "a blessed [charging] restores one additional wish": uncursed too (read.c:737-779).
- L6658 life saving "(any kind of death)": not genocide; costs 1 Con (end.c:1081-1096).
Checked correct: ring prices, 90% auto-curse, aggravate cap, life-saving HP, guarding MC, box contents, key odds, lamp odds, marker charges, unicorn horn odds, crystal ball thresholds, cursed-bag loss.
Style (AI-filler): L6632 "Economy of fingers is an art." cut. L6642-6643 "The stakes are high, because the range runs from 'saves your life' to 'slowly strangles you to death'" -> "One of them revives you from death and one of them strangles you, so don't put an unknown amulet on without checking its curse status first." L6673-6675 "which sounds niche until you reach ... Then it's existential." L6833-6834 "The weight is negligible and the utility is constant." -> "It weighs almost nothing and you'll use it on every level." L6857 "Music has power in the Mazes." L6937-6938 "A well-used marker can produce a meaningful share of your ascension kit." cut. L6610-6611 "The key word is 'deliberately.'" cut. L6686-6687 "which should tell you everything you need to know". L6956-6957 "the straight-shaft escape that ends many ascension runs" ambiguous. L6812 "BoH". L6613-6614 "paralysis is death in the late game". L6618-6619 conflict "turns your pets hostile" -> "makes your pets attack you while it's on". L6689 "spiked shut". L6868 "useful only for confusing the issue" dismissive + wrong. Rarely actionable: L6978-6979, L6603-6611 aggravate-for-sacrifice.
Craft: Amulets (L6640-6656) need the safety rule (strangulation: six turns, do_wear.c:1040; remove or pray); table omits amulet of change. Life saving "Take it off when you're safe" -> "wear it and forget it". Aggravate aside precedes "rings that matter most": swap. Stethoscope: first use each turn free (apply.c:341-342). Passtune "You will find the notes nearby" -> cross-ref L8955. Best: Containers L6748-6762.
Top 3: fix magic lamp/marker label/Gehennom digging/grease/Castle chest; amulet safety rule + complete table; cut ring-juggling aside and ornamental closers, restate ring hunger.

---

## Chunk 15: The Armory (L6990-7695)
Verdict: reads well; slot-by-slot and class-by-class with lively flavor; but more factual errors than an audited chunk should carry. Strongest: dagger paragraph (L7524-7531). Weakest: MC/cloak block (L7289-7338), wrong in places, says the same thing three times.
Correctness:
- L7645-7647 "no destruction limit ... never lost": evaporates 2 in 3 at +6 or higher (wield.c:998-1010; read.c:1667-1672). CONFIRMED by editor.
- L7250/L7264-7267 "large shields exclude two-handed weapons": any shield blocks any two-hander (wield.c:186-187).
- L7251-7252 vs L7261-7262 shield casting penalty: flat penalty for any shield (spell.c:2196-2197), quartering above small-shield weight (2269-2274).
- L7065-7066 mithril "penalty much smaller than plate's": every metallic suit same penalty (spell.c:2191-2193; Wizard 10, role.c:570); robe halves it.
- L7422 quarterstaff "only two-hander with no spellcasting penalty": no weapon carries one; quarterstaff gives a small bonus (spell.c:2199-2200).
- L7285-7287, L7304-7309 MC from Protection "+1 per source": bought Protection lifts MC0 to MC1 only; ring of protection/cloak of protection +1, amulet of guarding +2, once (mhitu.c:1121-1135).
- L7292-7293, L7316-7317 what MC blocks: cockatrice hiss not MC-checked (uhitm.c:4212-4251); brain suck blocked by helmet 7 in 8 (uhitm.c:3207-3212); gazes/breath not checked. MC negates level drain, poison, paralysis, sleep, slow, confusion, stun, lycanthropy, disease, sliming, teleport touch.
- L7159-7160 fedora/Eye of the Aethiopica: Eye is Wizard's amulet (artilist.h:303-305); Mitre is Priest's helm; fedora gives an Archeologist +1 Luck (timeout.c:603-604). CONFIRMED.
- L7175-7176 helm of telepathy "requires actively blinding yourself": worn telepathy shows minds within 8 squares eyes open (display.h:46-50).
- L7229-7231 jumping "as an a (apply) ability": #jump (cmd.c:1746). Same at L3003.
- L7252-7253 "Monks can't use a shield at all; zeros Martial Arts": costs the martial-arts to-hit bonus (uhitm.c:397-401).
- L7474-7476, L7564-7566 grappling hook "yank a target into melee range", "4 squares (8 Expert)": polearm reach (2 squares); pulls only very small monsters 1 in 4, snags objects, or drags you (apply.c:3826-3860).
- L7580-7581 "Rangers, Samurai, and Rogues reach Expert [bow]": Rogues can't use bows (u_init.c:414-439).
- L7600 "Shuriken (Samurai get +1 multishot)": Monks do (dothrow.c:53-56).
- L7624 "silver short sword": no such item.
- L7238-7239 fumbling "fumble every other turn ... dropping your weapon": trip every 1-20 turns, two turns, nothing drops (timeout.c:906-924).
- L7247-7249 shields "block rays you can't see": no such mechanic.
- L7481-7482 Mjollnir "returns when thrown while wielded": Valkyrie only, Str 25.
- L7107-7109 shopkeeper "fingerprints your suit": unsupported; nymph takes the cloak instead of the suit (steal.c:440-441).
- L7166-7167 dunce cap "cannot be BUC-tested": BUC works but doesn't distinguish; price does (80 vs 1 zm).
- L7271-7272 drain res "no non-artifact source": lycanthropy grants it (attrib.c:885); black DSM is disintegration.
- L7644-7645 enchant armor "+1 (uncursed)": 1-2 (1-3 plain) at low enchantment (read.c:1194-1218); confused CURSED strips proofing (L7660 should say non-cursed).
Style (AI-filler): L7345-7348 "how far away you strike, whether you can also throw, how fast you swing per turn, which artifacts you can ever hold" decorative quartet with false item -> "Your weapon decides your reach, whether you can throw it, and which artifacts you can hope for." L7132-7133 "each anchor a defensive strategy"; L7220-7221 "each redefine what your character can do" -> plain lead-ins. L7105-7106 "real magic cancellation and often a defining intrinsic". L7444-7447 "no blood spilled, in the cleric flavor sense ... in the historical sense" invented reasons. L7618-7619 "the price Samurai pay for the two-weapon flavor" hollow + wrong. L7625-7626 vague comparative. L7157 "dead weight for casters" dismissive (penalty is 4). L7201 "Never wear", L7241 "Always altar-test". L7028 "Try armor" -> "Test armor". L7180-7182 rarely actionable. L7487 vs L7395 Snickersnee long sword vs katana.
Craft: MC needs its own ##### heading; merge cloak-of-protection/MR explanations (L7135-7141, L7321-7331, L7332-7338); name MC2 suits (mithril, plate, crystal plate). Per-slot "wear now / look for / skip" table. Per-role first-weapon line. w/x swap muddled (L7397-7401). Mummy wrapping (L7128-7130): shopkeepers bar invisible customers.
Top 3: fix enchant-weapon + any-shield rules; rewrite MC block once under its own heading; per-slot table + per-role weapon line.

---

## Chunk 16: Curses / Spellcasting / Luck / Exercising (L7696-8165)
Verdict: reads well, mostly checks out. Strongest: failure-effects ladder (L7840-7850). Weakest: "Why Luck Matters" (L8098-8115) overstates punishment for slightly negative Luck, never states plain rules; reading table (L7867-7875) axis contradicts the formula above it.
Correctness:
- L7837 "or randomly curse one of your items" (book failure): unreachable (spell.c:133-182). Cut.
- L7867-7875 "Minimum Int + XL needed": formula counts XL at half weight, 2 points per spell level (spell.c:582-584). Column should be "Int + half your XL (for 80%+)": 14, 16, 18, 20, 22, 24, 26.
- L7884-7885 "body armor adds a failure penalty": only metallic (spell.c:2191-2195).
- L7924 detect monsters "Sense nearby monsters": every monster on the level (detect.c:809).
- L7932 "The other 34 spells": 41 exist, spheres deferred -> 32.
- L7778-7780 "A pleased god uncurses your worn items": cursed gear is minor trouble; off an altar the god fixes at most the single worst trouble, one item, only with Luck >= 1 and alignment >= 4 (pray.c:93, 253-254, 1126-1157); cursed levitation, welded weapon with no free hand, cursed blindfold are major (pray.c:87-89, 228-243).
- L8026 "bless it on an altar": altars reveal only; holy water blesses.
- L8033-8036 cursed luckstone "partially offsetting": cursed luckstone + one non-cursed luck artifact sums to zero, full +3 (attrib.c:428-448).
- L8061 "Sitting on a throne (lucky outcome) +1": only while Luck negative; otherwise a wish (sit.c:106-110).
- L8091 "a pile of kobold corpses" for Luck: gain = value*10/48, value = difficulty+1; kobolds give ~nothing.
- L8110-8115 "Even one point of negative Luck causes prayer to backfire ... stat loss ... black glow ... bolts": at Luck -1/-2 with no anger, only "displeased" + timer reset (pray.c:715-730, 780-782); sermon/curses/bolts need Luck <= -3 with poor alignment, <= -9 otherwise, or an angry god. "Scrolls will backfire" false; L8000 "every scroll" overclaims (only blessed identify reveals more at Luck > 0).
- L8158 "Wis for prayer success": prayer never checks Wisdom (pray.c:2149-2162).
Verified: remove-curse scope, curse rates, holy-water dip, reading formula, ladder, fade/crumble, novel XP, force bolt, chain lightning, Pw cost/regen, Luck range/drift/luckstone, gem rows, sacrifice ceiling, books-by-skill, exercise rows.
Style (AI-filler): L7719-7720 "one of the dungeon's quieter ways to kill you" -> "and you can't take it off until you break the curse." L7755 "free, instant, and should become instinct" -> "It costs nothing, so do it with everything you find." L7776-7777 "Simple, reliable, and reason enough to stockpile holy water" -> "This is the main reason to hoard holy water." L7879-7880 "learn faster, fail less, and have the widest range" (learn faster not a mechanic). L7998-8001 "every die roll, every prayer, every scroll, every combat swing" anaphora + overclaim. L8006-8008 "the universe's way of saying 'prove yourself' ... the Mazes don't give anything for free" -> "It starts at 0 and, left alone, drifts back toward 0." L8107-8108 "Luck feeds the game's luck-adjusted die" implementation talk. L8043-8049 "stair-up runs" unexplained, rarely actionable. L8152-8153 "The vow of restraint pays in wisdom." cut; L8159-8162 "a small but real upgrade ... a small but real loss" machine parallel. L7764-7766 "that's a common spoiler myth" meta.
Craft: Learning Spells: price = 100 x level (cross-ref Spellbook Prices); 5.0 Wizard prompt "This spellbook is difficult to comprehend. Continue?" (spell.c:587-597) so declining is free. Spellcasting never says why Fail is 100% or how to lower it (metal body armor, any shield, metal helm/gloves/boots, stat and school skill, quarterstaff bonus; spell.c:2187-2274). Detecting Curses: price-ID bullet doesn't detect curses; cut. Uncursed remove curse frees a cursed loadstone (read.c:1549). Luck: open with four plain rules (keep >= 0 so prayer works; uncursed luckstone; gems to co-aligned unicorn; don't kill peacefuls or break mirrors); add murder row (-2 and lost telepathy, mon.c:3648-3663). Exercising: move "Why Exercise Matters" up; Wis row: studying and successful casts exercise it.
Top 3: rewrite the two prayer claims; fix reading table + make "can't afford to fail" actionable + failure-rate paragraph; Luck plain rules + corrections.

---

## Chunk 18: Artifacts (L8599-8914) — most error-dense chunk; ~1/3 of specific mechanics wrong

Verdict: framing good (opener, how-they-come list, wishable table, ranking paragraph). Strongest: Naming Sting and Orcrist (L8768-8779). Weakest: thirteen quest-artifact prose entries (L8829-8911) repeating the table and carrying most errors.

Correctness:
- L8805 "#invoke (default ^A) ... for an energy cost": key is M-i (cmd.c:1744); no energy cost; artifact ignores you rnz(100) turns after; only Sunsword and Grimtooth can pay 25 Pw to fire during cooldown (artifact.c:2091-2127). Propose: "#invoke (default M-i) activates an artifact's power. Afterwards it ignores you for a while, typically around a hundred turns."
- L8756 "50 Pw per invocation", L8758 "up or down lights the room": free when rested; up/down lights your own square (artifact.c:2059-2063).
- L8824, L8903-8904 Orb of Fate "levitate-or-teleport toggle": LEV_TELE = level_tele() (artifact.c:2160). Propose: "#invoke is a level teleport (pick the level if you have teleport control)."
- L8825, L8909-8911 Eye of the Aethiopica "portal that drops you in Vlad's Tower": menu of any branch already visited; refuses with the Amulet (artifact.c:1867-1931).
- L8816, L8851 Staff "full heal + cure": heals half missing HP, cures sickness/sliming/blindness (artifact.c:1780-1815).
- L8671, L8726-8727 Stormbringer "drains a level (you gain it)": victim loses a level; you heal half the HP it lost (artifact.c:1673-1686).
- L8673-8674 Frost/Fire Brand "(base only)": both double damage vs non-resistant (artilist.h:149-155; artifact.c:1042-1043, 1107). Reason Frost Brand is a top wish.
- L8677, L8731-8736 Cleaver "wielded one-handed ... shield": battle-axe two-handed (objects.h:239-240); cleave fires every swing (uhitm.c:766-771).
- L8669, L8708-8714 Mjollnir "Needs Str 25 to wield ... return often misses": Str 25 to throw (dothrow.c:127); non-Valkyries never get it back (dothrow.c:30-34). Propose: "Anyone can wield it. Throwing needs Str 25, and only a Valkyrie gets it back."
- L8652-8654 blast "4d4 first touch, 1/4 subsequent": 1/4 every touch incl. first (artifact.c:944-945). Missing: intelligent artifact blasts 4d10 for wrong role alone (artifact.c:922-924, 944), so L8790-8803 Monk + Eye takes 4d10 (2d10 with MR) every touch. L8798-8800 wrong: MR is a carry bonus on Orb of Detection, Mirror, Card (artilist.h:221, 257, 293).
- L8786-8788 "Most of the non-weapon ones grant MR by sitting in inventory": three of nine.
- L8846 Sceptre conflict "steep energy cost": toggled, no cost, no hunger (artifact.c:2178-2208; eat.c:3203).
- L8836-8837 Heart "+1 luck bonus": stealth only; luck is ordinary luckstone +3.
- L8849-8851 Staff "one of only three drain-life weapons; others Stormbringer and Death ... just by carrying": Stormbringer only; regen/drain res need wielding (artilist.h:249-251).
- L8870, L8890 "-1 to AC" / "+1 protection bonus": artifact Protection = +1 magic cancellation, never AC (do_wear.c:2492-2502; mhitu.c:1113-1125).
- L8884-8886 Master Key "opens any lock without effort": finds traps while picking (lock.c:100-112); #untrap on doors/chests always succeeds (trap.c:5866-5868).
- L8898-8899 Card "a free wish per ~1000 turns": wand of wishing survives exactly one recharge (read.c:738-762); cooldown rnz(100). Propose: "the classic use is one extra charge on a wand of wishing, which survives a single recharge."
- L8856-8857 Magicbane-ish "old wizard's voice murmurs a hint": whispers a rumor when applied/wielded (apply.c:4421-4422, wield.c:242).
- L8861 Eyes "see invisible, see through walls, spot secret doors": x-ray vision radius 3 only (artifact.c:859-866).
- L8700 Excalibur: add "from experience level 5" (fountain.c:404).
- L8665-8686 alignment column: role artifact takes hero's alignment (artifact.c:92-95); footnote.
Verified: naming (artifact.c:611-619: Sting and Orcrist only), damage dice, Excalibur 1/6 vs 1/30, Master Key BUC, Snickersnee reach, Grimtooth, bane doublings, Sceptre vs non-lawful.

Style: L8693 "flavour" vs L8750 "flavor". L8695-8696 "usually accepted as sacrifice gifts rather than spent wishes on" -> "usually arrive as sacrifice gifts rather than wishes." L8727 "huge in the early-to-mid game" hollow. Em-dashes at L8650, L8747, L8795-8798, L8884-8885, L8902-8903.

Craft: quest-artifact entries (L8829-8911) 80 lines repeating the table; keep prose only where a decision/trap exists (Master Key BUC, Eyes/Eye must be worn, Staff, Card, Orb of Fate, Heart). Alignment and Blasting (L8643-8654) as three rules naming the intelligent artifacts. How you get one (L8629-8641): link Sacrifice and Wishes; say first artifact is nearly always a sacrifice gift or Excalibur.

Top 3: fix invoke powers; correct combat mechanics (Brands, Cleaver, Mjollnir, Stormbringer, blast odds); cut quest-artifact prose to decision-relevant entries.

---

## Chunk 19: Into Gehennom (L8915-9302)
Verdict: Castle bullets, pre-descent kit checklist (L9027-9032), "What's Different in Gehennom" list scannable and useful. But plan-breaking errors: passtune stance makes the tune silently fail, Invocation instructions wrong, Book placed at wrong end of Wizard's Tower, wand of death recommended against demons twice. Weakest: Wizard's Tower never says how to get in.
Correctness:
- L8960-8962 "Stand one knight's-move from the bridge while guessing; adjacent squares get crushed": tune works only with the span/portcullis in the 8 squares around you (music.c:816-832) CONFIRMED; opening crushes only span + doorway (dbridge.c:811-815). Propose: "Stand next to the moat, diagonally off the end of the bridge. The only squares crushed when it moves are the bridge itself and the doorway behind it."
- L8968 "The moat squares become walkable" after striking: span reverts to moat (dbridge.c:924).
- L8988-8990 "leprechauns and rats gnaw containers": invented; object-eaters are gelatinous cubes and metal-eaters (mon.c:1533).
- L8993-8995 "storerooms hold random fodder": one room each armor, weapons, gems, food (castle.lua:27-28, 65-125).
- L9066 Valley "shrine to Moloch in the upper-left corner": temple mid-left; down stair upper-left (1,1); arrive lower right (valley.lua:48-58, 68).
- L9097-9098 lava "sink and burn within a few turns": burn at once without fire res (trap.c:6874-6936); with it, sink and can climb out.
- L9121-9123 demon princes "will not pursue you": wait until they see you (monmove.c:710-712); M2_STALK follow on stairs.
- L9126-9128 bribery: no gold in open inventory -> demand zero -> attack (minion.c:309-316); demand 21-100% of visible gold, halved if lawful.
- L9137 "a wand of death works on all four" and L9194: demons immune to death rays (zap.c:4308-4313) CONFIRMED.
- L9167 Vlad's throne "eighty-HP gulps": rnd(80) (sit.c:339). L9174-9175 "about seven bad effects": expected 9/4. L9179 "or magic resistance": blocks none (sit.c:326-327).
- L9192 Orcus "signature artifact is the Wand of Orcus": plain wand of death (makemon.c:506-507).
- L9246 "the bottom of the Wizard's Tower": Wizard and Book on the top level (wizard1.lua:7,56,60; portal enters at wizard3, fakewiz1.lua:29).
- L9260 "You feel an unsettling vibration": actual "a strange vibration under your feet" (hack.c:3079).
- L9264-9266 "#invoke the Bell of Opening": sequence is apply Candelabrum (light), apply Bell (ring), read Book within four turns; none cursed (spell.c:241-291; apply.c:1355-1360).
- L9273-9274 Sanctum up stair "(it would not before you had the Amulet)": no such gate (sanctum.lua:130; do.c:1502-1506 gates only the Planes).
- L9227, L9270-9271 Amulet "on the high altar": High Priest carries it (priest.c:260-263).
- L9107-9108 "most Gehennom levels permanently blocked teleportation" (older editions): only special levels did.
Style (AI-filler): L9086-9087 "demons breathe fire as casually as you breathe air" (no demon breathes fire) -> "Fire traps are common and hell hounds breathe fire; without fire resistance, go back up and get it." L9100-9101 "Each fight is a major battle, several can summon reinforcements, and all of them are angry you are here" triplet. L9133-9135 "Arch-Devil demons with the bribe disposition ... how friendly your wallet looks" -> "Only Asmodeus, Baalzebub, Geryon, and Dispater take gold; the others attack on sight." L9144 "Those artifacts refuse to talk and attack on sight" -> "A prince who sees either blade in your hand attacks at once, so sheathe it." L9199 "killed off by his ambient aura" invented. L9211 "dangerous not for raw combat power but because he never stops" -> "His attacks are survivable; the problem is that he keeps coming back." L9240 "no longer any such thing as a safe turn" hollow. L9290-9291 "another summoned monster, another stolen item, another cursed piece of gear" machine triplet -> "While he lives he casts, summons, and steals." L9284 "prayer is not a reliable refill" contradicts L9082 -> "prayer cannot fix hunger in Gehennom." Rarely actionable: L9138-9139, L9002-9003.
Craft: Wizard's Tower (L9207) needs the way in (two moated fake towers with a portal to the real tower's bottom; climb to the top). Valley corpse paragraph (L9073-9078) is trivia; replace with arrive/exit plan. Candles: Vlad's Tower holds two chests with 4-8 candles each (tower1.lua:56-65). Vlad's throne effects as a short list. Best: L9027-9032 kit list.
Top 3: rewrite Heist step 4 (light, ring, read; no cursed relics); fix passtune stance + striking outcome; remove wand-of-death-vs-demons, add the Wizard's Tower portal plan with the Book at the top.

---

## Chunk 20: The Ascension (L9303-9663)
Verdict: usable plan (kit table, runners-up post-mortems, Gauntlet/Strategy bullets). Planes and Astral weak half: several 5.0 mechanics wrong; Astral prose slips into sermon cadence. Best: "What killed the runners-up" (L9342-9364).
Correctness:
- L9337, L9641-9643 "a wielded cockatrice corpse one-shots Riders / no stoning resistance": all three Riders MR_STONE in 5.0 (monsters.h:3149, 3159, 3169).
- L9399-9402 "cursed potion of gain level ... without provoking the Mysterious Force": Force fires on any upward level change in Gehennom that isn't a portal (do.c:1541-1543, 1489). Cut.
- L9534-9536, L9545-9546 magic mapping "tells you which cavern holds the portal / reveals it": mapping draws only traps already seen (detect.c:1406-1408); Air map is uniform. Use confused gold detection or a crystal ball.
- L9571-9577 Plane of Water "you will drown ... the next turn drowns you again", "chambers", "corridors": you arrive inside a moving air bubble (water.lua:10; mkmaze.c:1626-1631); stepping into water beside air you crawl straight back out (trap.c drown(): Is_waterlevel); map is open water. Propose bubble/eel rewrite.
- L9643-9645 "conflict keeps the Riders tangled": 5.0 resist_conflict: rnd(20) > min(19, CHA - mlev + ulevel) (mondata.c:1607-1613) CONFIRMED; L14 hero with 18 Cha conflicts a L30 Rider ~10%.
- L9646-9647 "four hostile Angels": two to four (minion.c:486-487).
- L9445-9447 helm of opposite alignment "flips you to Chaotic": Neutral gets Lawful or Chaotic by coin flip (do_wear.c:468-471).
- L9433-9435 Force "Often it just shuffles you": same-level 1/4 Lawful, 1/3 Neutral, 1/2 Chaotic (do.c:1544-1545); L9440-9443 decay relieves Lawfuls most (do.c:1563).
- L9406-9408 "Astral plane portal ... will not open": the gate is the Dlvl 1 up staircase; without the Amulet, climbing out ends the game as an escape (dungeon.c:1529-1530).
- L9336 "quest artifact + a silver saber ... silver bypasses demon resistances": only four quest artifacts are weapons; silver adds d20 vs demons/vampires/weres (uhitm.c:1376-1377).
- L9613-9617 Pestilence "finishes you a few turns after": first touch sets 20+CON turns; each further touch cuts remaining to a third (mhitu.c:1033-1042).
- L9619-9620 Famine "Three swings in a row will [starve you]": each touch 40-79 nutrition (uhitm.c:3795).
- L9474 "write it for the alignment": engraving grants no alignment.
- L9591 "Three altars stand in the great temple": three separate temples (astral.lua:82-89).
Verified: Amulet wish, spell drain, Elbereth dead past Castle, warm/hot distances, Death 3/20, stun downgrade, green DSM sick res, death ray heals Death, Rider corpse fatal.
Style (sermon cadence): L9453-9454 "You are no longer an explorer. You are a running back carrying the ball through the entire opposing team. Speed is everything." -> "From here on you are not exploring, you are leaving. Every turn spent on anything but the next staircase is a turn for the Wizard to catch up." L9456 "Run, don't fight. Don't explore. Don't loot. Just go up." -> "Skip fights you can walk around, skip loot, and head for the up staircase." L9423-9424 "He will not stop. Kill him each time. He always comes back." L9479-9483 "a sprint, not a marathon ... the last obstacle between you and divinity". L9625-9628 "They revive, they pursue, they do not stop ... You are not here to fight; you are here to reach one altar, make one sacrifice, and end this." -> "Killing a Rider only buys time; the corpse revives within about seventy turns, and eating it is instantly fatal. You are here to reach one altar." L9537 "The plane is claustrophobic and punishing." cut. L9560-9561 "Everything is on fire. The ground is fire. The air is fire." -> "Lava lakes cover the plane, fire traps are scattered between them, and fire elementals and hell hounds roam." L9566-9567 "you'll be dead in a few turns". L9327 "Magic resistance keeps you alive through Gehennom." -> "blocks the death ray and Death's touch." L9362-9364 oilskin sack tip rarely actionable.
Craft: "self-teleport fails on the planes" said three times (L9532, L9553, L9648). Strategy Elbereth bullet: add scroll of scare monster still works in Gehennom (monmove.c:280-283), not on Riders/Angels/humans. Plane of Air 5.0: lightning out of the clouds one turn in eight for 8d6, frying wands/rings a third of the time (air.lua:9; timeout.c:1855-1875): shock res or reflection changes the kit. Astral: add a four-step ordered list before "Defenses". Kit table Required loot: link Sanctum.
Top 3: fix 5.0 mechanics (Riders resist stoning, cursed gain level, magic mapping, conflict); rewrite Water around bubbles + add Air lightning; replace pep-talk with numbers, ordered Astral checklist.

---

## Chunk 21: Advanced Controls + Customization (L9664-9912)
Verdict: Controls half reads like a friend showing you the keys; Travel best. Customization half carries 3.6-era claims wrong in 5.0; the starter rcfile as printed produces a config error and removes the water/lava stop the Controls section relies on. Weakest: Safety/Pickup (L9842-9865).
Correctness:
- L9809-9813, L9887-9891 hilite_status rules split with trailing backslash: continuation joins with a space (cfgfiles.c:1720-1756); hilite_status treats a space as end of rule (botl.c:2605-2624) -> "Unknown status field" (botl.c:2859); only the <66% and Satiated rules survive. One rule per line (Guidebook.txt:6517-6522).
- L9844-9847 "paranoid_confirmation:Attack pray Remove quit": a list without + clears the defaults pray swim trap (options.c:2917-2947) -> removes the "You avoid stepping into the water" stop (hack.c:1911-1914) that L9730 relies on; pray already on; Remove means "ask which item". -> "paranoid_confirmation:+attack quit".
- L9803-9805 "without statushilites nothing colors": 5.0 turns highlighting on when any rule exists (botl.c:2643-2645; fixes5-0-0.txt:1023).
- L9720-9726 G/Shift/g: Shift = mode 1, g = mode 2, G = mode 3 (cmd.c:1545-1615). Mode 1 runs past objects/doors/traps; only mode 2 stops at corridor forks (hack.c:3952-4028). -> "Shift+direction runs until something blocks you, following corridor bends. G also stops beside items, doors and traps. g stops at corridor forks too."
- L9731-9734 "me is 'what would you like to eat?', ma is 'which tool?'": m before e skips the floor-food offer (eat.c:3596); apply has no menu; only m, forces a menu (pickup.c:759).
- L9839-9840 "pile_limit:5 triggers the pile menu when 5 or more": inverted, and 5 is default (options.c:71).
- L9795-9796 "nethack.cnf in the install folder on Windows": .nethackrc in %USERPROFILE%\NetHack\ (Guidebook.txt:3951-3952).
- L9794 "Flip them in-session with O": most need mO (Guidebook.txt:1599-1601).
- L9770-9772 overview list "vault": no vault; graves and trees, annotations, bones, deepest level per branch (dungeon.c:2873-2922).
- L9762 message history "several dozen lines": default 20 (options.c:7177).
- L9862-9865 pickup_burden: asks "Continue?" on any pickup that would push you PAST the named level (pickup.c:1757-1790).
- L9779-9780 chronicle "first kills ... prayer outcomes": first kill (singular), gifts, crowning, atheism-breaking first prayer; ordinary prayers not.
- L9829-9830 "unbleached" / "blessed-cure-injury": neither word exists; real reason is "uncursed".
- L9903 "nethack-curses on most distributions": doubtful; tty-only unless WANT_WIN_CURSES.
- Minor: L9695 --More-- never interrupts; L9708 canceled commands dropped but wall-bump stays queued.
Verified: 32767 cap, F double-tap, #f, v chronicle, Ctrl+O with m, _<. / __., travel stops at closed doors, m over water, runmode default, red&inverse+blink, "Fainted", menucolors auto-on.
Style: L9684-9687 "Once you've spent a few thousand turns hammering s ... reflexive" -> "The basic keys handle everything; these handle it faster. Learn Ctrl+A and _ first." L9706 "the most-used advanced command in the game" / L9747-9748 "the single biggest quality-of-life command in the game" cut. L9713 "essential for moving safely through populated areas" cut. L9760-9762 triplet -> "Use it when a message flashed past before you read it." L9793-9794 "dramatically improve quality of life" -> concrete. L9817-9818 "the single most-recommended setting in community rcfiles" cut. L9880-9881 verbose subsection rarely actionable. L9801, L9829 em-dashes.
Craft: Customization opener: five-line ranked list with one-clause why (HP colors; +attack quit; autopickup + pickup_types:$?!=/; pickup_burden:unencumbered; menucolors for cursed), then the file. Starter rcfile: runmode:walk never justified. Forcing locked chests (L9750) misfiled. Best: Travel (L9738-9747).
Top 3: fix the starter rcfile; correct run modes and m-prefix claims; ranked five-option opener, cut superlatives.

---

## Chunk 22: Sokoban Solutions (L9913-10612)
Verdict: sound. All eight maps exact against dat/soko*.lua (cell-by-cell diff: walls, 125 boulders, pits/holes, stairs, @ start, doors, prize chambers, scroll-of-earth squares, prize odds 75/25, remaining-boulder counts). Level naming matches game convention (trap.c:7074-7076). Flipping note right (no noflip; sp_lev.c:975-978). Rolling-boulder squares behave as L9966-9968 says. Weakness: notation key (L9962-9972): "Finish" (69 uses) never defined, nor "like G", nor that coordinates are (column,row); mirroring note too thin for print readers.
Correctness (small):
- L9963 "^ symbols mark pits": only Level 1 has pits; Levels 2-4 have holes; a Sokoban hole drops you a level even flying/levitating (trap.c:633-634).
- L9950-9951 "destroying boulders with wands": force bolt shatters too (zap.c:2278-2286 -> fracture_rock) and counts as cheating.
- L10461, L10607 "There is a bag of holding / amulet in one of the small chambers" contradicts L10373-10374 "usually" (75/25). -> "The prize sits in one of the three small chambers, at (17,12), (17,14), or (17,16), beside the treasure zoo."
Style: no AI-filler found. L9966 "sokoban" capitalize. L9949-9952 "penalty ... penalty" with list in mid-sentence parentheses -> "Cheating costs 1 Luck each time, and the losses add up. Cheating means squeezing past or stepping onto a boulder, smashing one with force bolt or a wand of striking, or reading a scroll of earth." L10098/L10101 "Move" vs "Push" everywhere else. L10500/L10504 spaced tuples. L10461-10462 nested parentheses.
Craft: define notation after L9968: "Coordinates are (column, row). Finish X means push X to the trap row and along it into the nearest unfilled pit; do the boulders in the order listed. Finish C like G means take G's route. In the game the arrow squares show as ^." Mirroring (L9974-9976): the level is fully mapped on arrival, so match the outline to the two diagrams; if mirrored swap left/right in every step and count columns from the other edge; web edition has flip buttons (template.html:661-666). Intro: hole warning belongs before the first solution. Level 4A/4B ends: cross-ref the zoo and the cursed scare-monster scroll under the prize (L1663-1664). A5/phone: maps <= 32 columns x 18 rows fit; checkpoint maps (Level 2B L10188-10242, 4B L10512-10596) are the model.
Top 3: define notation; rewrite mirroring note for print; holes warning + force bolt in intro.

---

## Chunk 23: Voluntary Challenges (L10613-11041)
Verdict: usable lookup with sound skeleton; 5.0 entries (Pauper, Petless, Permadeaf) best. Weakest: Pacifist contradicts itself about pets; "Combining Conducts" is a grab-bag hosting Nudist, Blind, and a preview of following sections.
Correctness:
- L10663 "Green slime is technically vegan": it is a pudding; vegetarian, not vegan (monsters.h:2103; mondata.h:239-241), as L10680 says.
- L10670 "violet fungus paralyzes": it makes you hallucinate (eat.c:1303-1306); audit note L10645 already says so.
- L10753 Pacifist "Not directly, not with pets": pet kills do NOT break it (mon.c:3499-3501 xkilled; monkilled never counts); displacing a pet into a fatal trap does (hack.c:2201). Next sentence contradicts. -> "Never kill a monster yourself. Kills by pets or by monsters under conflict don't count."
- L10811-10814 genocide "type none ... Don't just press Enter": on a cursed scroll "none" also summons monsters (read.c:2870-2875); Enter re-prompts (2859-2867). Conduct survives in every case.
- L11019-11020 Sokoban "fracturing a boulder with a wand of striking": fracture_rock charges guilt whenever you caused it, incl. force bolt (zap.c:2276-2286) and pick-axe (dig.c:299-300, 456-457).
- L11017 "Complete Sokoban without breaking the rules": conduct reported once you have entered (insight.c:2216, 2517-2525); finishing not required.
- L10951 "Cleric, Knight, and Monk": role is Priest (46 uses in book).
- L10921 "5.0 added five more tracked conducts": six, including "unrerolled" (topten.c:608; insight.c:2103-2110).
- L10684-10686 stone to flesh listed as a nutrition source for Foodless then "eating them breaks the conduct": not a source; prayer works from Hungry (pray.c:275-276).
Checked correct: altar/chat/offer/pray/turn atheist triggers, Amulet exemption, weaponless, x/X signature, blank/Book/Hawaiian shirt exemptions, "nothing" wish, Amulet wish, denied-artifact tick, pettype:none, pauper, shrieker, bonesless, 3.6 origin.
Style (AI-filler): L10754-10757 "runs on pets doing the fighting, on conflict..., on Elbereth..., and on creative use of the dungeon environment" -> "A pacifist lets pets do the killing, holds monsters off with Elbereth, and later wears a ring of conflict so they kill each other." L10759-10760 "possible but require deep knowledge" cut. L10904-10905 "the stuff of legends" flourish; foodless implies vegan. L11004 "Permadeaf navigates by sight and logic alone." cut. L10788 "forces extreme reliance on ... creative workarounds" cut. L11000-11002 "Treat empty silence near a F-class monster as the same threat as the usual SCREECH" (no such message; mon.c:4092 "shrieks"). L10810/L10826 "case 8 of 13" implementation talk. L10912-10913 over-enumeration -> "Never wear anything in an armor slot, shirt included." L10632 lichen breaks only foodless -> "a newt corpse". L10627 "RGRN" jargon. L10791-10792 "cover most of the ID table" jargon.
Craft: give each conduct three beats (what it means / what breaks it / what it costs) + a one-glance table (conduct | broken by | how to set or check). Nudist and Blind get their own #### (index L14237 points here). Cut the 5.0 preview L10921-10925. Sokoban entry cross-ref L1655. Illiterate: #name with an artifact name breaks it (do_name.c:411-415); Archeologists decipher labels on pickup (invent.c:1036-1047). NAO one-in-nine / one-in-eighty figures unsourced. Best: Pauper (L10941-10955), Permadeaf catch (L10998-11002).
Top 3: fix Pacifist + four wrong mechanics; three-beat shape + table, move Nudist/Blind; cut ornamental closers and "case 8".

---

## Chunk 24: Shopping and Shopkeeper Pricing (L11042-11310)
Verdict: grab-bag: solid credit/debt explainer, loose "behavior" list, then gems. Best: credit numbered list (L11079-11094), "Closed for inventory" (L11192-11200). Weakest: Shopkeeper Behavior (L11145-11204): wrong claims, unusable tips, the rule a beginner needs (what angers, what it costs, how to fix) scattered.
Correctness:
- L11086-11089 credit offered only when the shopkeeper has NO gold, at 90% (shk.c:4046-4073); if merely short they pay cash they have (4088-4091).
- L11093-11094, L11108-11110 "can't be stolen by nymphs, can't fall into a pit ... polymorph trap": nymphs never take gold (steal.c:52); leprechauns do; no pit/polytrap gold loss.
- L11136-11138 "shopkeeper has lent you gold": loan = shop gold picked up off its floor (shk.c:5745-5788).
- L11157-11159 digging: through a wall = 10 zm per Str point demanded on the spot (hack.h:80; shk.c:5295-5317); digging DOWN while owing = shopkeeper grabs your whole pack (dig.c:781-782; shk.c:5061-5108).
- L11161 artifact prices "10,000-30,000": value x4: 800 (Giantslayer/Ogresmasher/Trollsbane) to 32,000 (Stormbringer, Grayswandir); Excalibur 16,000.
- L11166-11168 killing a shopkeeper "summons Kops": Kops only on walk-out (shk.c:623, 680); killing costs -5 alignment, and for non-chaotics -2 Luck + lost telepathy (mon.c:3644-3661, 3722).
- L11172-11174 "sacrifice the corpse on an unaligned altar to convert it": same-race sacrifice converts a lawful/neutral altar to chaotic; on an unaligned altar -2 Luck + demon (pray.c:1717-1760); contradicts L4512-4526.
- L11196-11198 kicked door "angry shopkeeper": demands 400 zm at the door (dokick.c:953-955); pay and welcome.
- L11217 touchstone "guaranteed at Mine's End": only a mimic there (minend-1.lua:71); guaranteed stone is the luckstone; contradicts L5456.
- L11246-11248 gem breakage "50% ... Below Mohs 8 breaks like glass": breaks only on a hit, 2/3 of the time, hard gems get a coin-flip reprieve: hard survive 2 in 3, soft/glass 1 in 3; a miss never breaks (dothrow.c:1976-2000, 2220).
- L11288 "an orange unicorn": no such thing.
- L11291 gem value "matters only when selling or wishing": selling and final score (end.c:1444, 1509-1510).
- L11296-11299 "3000+ zm per gem ... non-gem-buying shop for half price": identified gems sell for half base (diamond 2,000, black opal 1,250); a shop that doesn't deal in gems won't buy (shk.c:4033-4043).
Checked correct: 22 gem prices/colors/Mohs/weight; touchstone 45; unID gem sell 3-8; shopkeeper gold/key; Elbereth immunity; unicorn Luck rules; Kops on walk-out.
Style (AI-filler): L11104-11106 "how safe and liquid your money is, not how far it stretches" -> "Credit buys exactly what gold buys; the difference is that nobody can take it, and you can only spend it here." L11147-11149 "one of the toughest NPCs ... the kind of clever escape that works on other monsters" -> "A shopkeeper hits hard, ignores Elbereth inside the shop, and sees you when you're invisible." L11162-11163 filler. L11174-11175 hedge; cut. L11177 "Beyond the rules, a few tactical habits pay off" cut. L11182 "(the game tracks unpaid items precisely)". L11202-11204 "Many players play fair: sell what you don't need, buy what you do, and use..." triplet; cut. L11228 "tiny piles of liquid gold by weight" -> "each weighs 1 and identical ones share a slot." L11281-11283 contrived, duplicates L11292-11295. L11298 "is a real bankroll". L11128 "shop-cheese routines" jargon. Rarely actionable: L11122-11125 leprechaun-luring; L11179-11184 "Drop everything at the door" (nothing sells on the door square, shk.c:3943-3944) -> "I then u lists every unpaid item with its price"; L11185-11187 "Sell to build credit" contradicts L11079 -> "Sell for gold, then drop the gold."
Craft: heading contains no pricing; rename "Shops: Credit, Debt, and Trouble"; gems own heading. Open with the walk-out warning (now under Loan L11140). One table: offence / response / fix (leave owing -> Kops; break door -> 400 zm; dig wall -> 10 x Str; dig down owing -> lose pack; attack -> 1000 zm buy-off; use unpaid item -> fee; arrive invisible or with a pick-axe -> refused at the door, shk.c:794-803, 856-895; the pick-axe rule appears nowhere in the book). L11150-11151 invisibility needs pointer to L4931. Bones (L11188-11191) muddled.
Top 3: fix dig/door consequences + one punishment table incl. pick-axe rule; correct artifact prices, Kops, sacrifice altar, touchstone, gem breakage; replace the two unusable tips, cut filler closers.

---

## Chunk 25: Weapons/Armor/Spell Tables (L11311-12205)
Verdict: numbers solid; regenerated both tables from build scripts: every numeric cell matches except crossbow bolt; 20+ cells spot-checked against objects.h. Errors are in prose glosses; Spell Tables weakest: six Effect/Type/Upgrade cells contradict spell.c/zap.c, one contradicts Spellcasting chapter on MR. Best: Polearms lead-in (L11658), Spear "kebab bonus" (L11695-11704).
Correctness:
- L11849 bow "Two-handed launcher ... cancels shield" (also L11868 crossbow): bows are one-handed (objects.h:126-130); only two-weaponing blocked (wield.c:75-78).
- L11824 crossbow bolt "1d4 / 1d6": +1 vs both sizes (weapon.c:229-236, 267-275); script emits 1d4+1/1d6+1; hand edit wrong.
- L11825, L11869 "below that, one bolt per turn": below Str 18 the volley is rolled twice (dothrow.c:225-231), not capped at one.
- L11916 "Samurai get +1 multishot on shuriken": Monks do (dothrow.c:53-56); Samurai bonus is ya from a yumi.
- L11364 crysknife "only dropping triggers it": throwing too (dothrow.c:1808 -> do.c:904-918).
- L11960 yellow DSM "Rare.": delete.
- L12162 finger of death "instakill with no Antimagic check": MR blocks an incoming death ray (zap.c:4493-4502); only self-zap skips it. Contradicts L4186, L7930.
- L12159-12161 magic missile "2d6", fireball/cone "4d6": (XL/2+1)d6 (zap.c:3462, 4256, 4264).
- L12164 cure blindness "aimed", L12177 confuse monster "aimed": untargeted (spell.c:1518-1551).
- L12167 stone to flesh "Statue -> corpse": animates a live monster (zap.c:2017-2029).
- L12175 detect treasure "gold and gems": every object (potion.c:1372-1374).
- L12172 detect food "Blessed: identifies the food": blessed warns you before eating something bad (detect.c:517-546; eat.c:2834-2841).
- L12181 charm monster "Blessed-scroll behavior": no blessed branch (read.c:1044-1063).
- L12163 healing upgrade "—": Skilled also cures blindness (zap.c:2909-2912); dice 6d4 / extra 6d8.
- L12190 levitation "Blessed: longer": blessed can be ended with > (potion.c:1210-1213).
- L12037 helm of opposite alignment "Cursed 90%": also self-curses on wear; L12041 should say remove curse needed after.
- L12140 "hits one square at that vector": travels 7-13 squares, hits first monster (zap.c:4823).
Style: L11317 "skill tree" jargon. L11658 em-dash. L11934 em-dash + "listed separately because of its sheer importance" hollow/inaccurate. L11711 "ranged-spam" jargon. L11751 "P_LANCE skill" C identifier; "a critical can shatter the lance" -> "about one joust in 250 breaks the lance" (uhitm.c:2122-2125). L11742-44 "Charging ... triggers a joust; on foot unremarkable" -> "Any hit while riding can become a joust; on foot it is a reach weapon like a polearm." L12074 "Critical for the Castle drawbridge" overclaims. L12031 "Wizards only" reads as unwearable. L11796-97 "(elf volley bonus)" cryptic. L11864 "~21-40" exact.
Craft: Spell Tables in the PDF (p.230): School column too narrow, "Enchantment" collides with level digit; abbreviate or widen. Weapons intro: point to Per-Role Skill Caps (L8310). Sling: Cavemen +1 per volley (dothrow.c:49-51). Helm of opposite alignment note: self-curse consequence first.
Top 3: fix finger of death cell; correct Spell Table cells; fix bow/crossbow two-handed claim and bolt +1.

---

## Chunk 26: Bestiary Tables first half (L12206-13000)
Verdict: solid; regenerated appendix from monsters.h and diffed all 156 rows in range: every Lvl/Spd/AC/MR/attack matched (hand-corrections for were-forms, silver dragon color, woodchuck color confirmed). Strongest: Unicorns (L12748-12750), Eyes/Gremlin/Mimic intros. Weakest: locator intros ("Cats.", "Dwarves and similar."), Piercer intro gives wrong defensive advice.
Correctness:
- L12624 piercer "you can't avoid the drop without flying or a clear ceiling": a hard helmet makes it glance off entirely; otherwise a dodge roll (uac+3 <= rnd(20)); flat 4d6 (hack.c:3420-3437).
- L12496 kobolds "Most are poisonous to eat": all four (M1_POIS); next line says so.
- L12274 "never wield a cockatrice corpse unless your role explicitly resists stoning": no role does; gloves are the protection (wield.c:143-146).
- L12427 mind flayer "if Int hits 3 you die": at Int 3 the next tentacle that lands kills (eat.c:698).
- L12698 "Spider-class ... common source of poisonous-corpse food poisoning": only giant spider and scorpion are poisonous; cave spider/centipede safe; "food poisoning" is the tainted-corpse term.
- L12723 "Identify with ; (farlook) before walking into obvious-trap squares" (trappers): hidden lurkers aren't displayed (display.h:86-89); searching adjacent reveals (detect.c:1702-1708).
- L12359-12361 "Valkyries and Tourists roll 50/50 between kitten and little dog": every role without a fixed pet rolls (role.c; dog.c:93-100).
- L12985 yellow dragon "rare": no rarer than the others (G_GENO|1).
Verified: floating-eye mutual-sight/reflection/free action; telepathy guaranteed from corpse; gremlin curse 1/10 night, 2/3 water split; helmet 7/8 tentacles; unicorn -5 Luck co-aligned only; any non-mineral gem pacifies; acid blob corrodes gloves; gold dragon scales light; long worm tooth; jelly resistances timed.
Style: L12212 "folds in the most tactically-relevant trait flags ... heads-ups for monsters that deserve one" -> "Notes lists the traits that change how you fight it (flies, sees invisible, regenerates, poisonous corpse) and a warning where one is needed." L12748 "There are two equine u-class creatures." -> "Horses and unicorns share this letter." L12750 "either way" dangling. L12609 "Hits hard. Drops decent loot." cut. L12331 "never melee one without free action, blindness, or a ranged attack" -> "never melee one without free action or blindness; kill it from range." L12698 "Includes scorpions and centipedes." restates heading. L12567 "her corpse drops what she stole" -> "she drops what she stole when she dies." L12684 "chew through your bag of gold or unattended weapons" -> "Eats metal objects left on the floor." L12958 "element type". L12416 "Dwarves and similar." locator -> "A dwarf swinging the mattock or axe it carries is the most dangerous thing on the first Mines levels; deeper down, mind flayers are the h to fear. Dwarves also drop the best early loot."
Craft: "(no mindless)", "(no pois-res)", "(no flies)" parentheticals (L12340, 12453, 12894, 12895, 12986) cryptic and redundant with intro; drop. Collapse repeated identical attacks ("tentacle 2d1 drain-Int x5") for A5 rows (L12428, 12986, 12898). Floating eye note (L12340) repeats intro. Leprechaun note (L12526) duplicates intro. "cast spell" vs "spell" (L12507, L12608). Dragon notes shapes vary; make parallel "<element> breath; <what stops it>." Class intros: first sentence = the danger or the opportunity. Best: Unicorns; "The giveaway is the wrong object on the wrong square" (L12539).
Top 3: fix Piercer intro; replace unactionable tips (farlook, role resists stoning, Valkyries/Tourists, "Most", "food poisoning"); trim cells for print.

---

## Chunk 27: Bestiary second half (L13000-13752)
Verdict: generated columns solid (regenerated, diffed all 223 rows; 3 hand-fixed rows correct). Hand-written prose carries life-or-death errors. Strongest: Trolls (L13354), Puddings (L13255-13257). Weakest: Elementals (L13002), Mummies (L13178), @/& tables with "poisonous-corpse" on 32 no-corpse monsters.
Correctness:
- L13734 lizard corpse "the standard answer to cockatrices and Medusa": Medusa's gaze is instant death (mhitu.c:1748-1756); reflection or blindness. Same error at L1102.
- L13178 "Wand and scroll of undead turning shred them"; L13489-13491 "heavy damage": no scroll exists; wand/spell does rnd(8) and makes the target flee (zap.c:243-259).
- L13491-13493 skeleton "skeleton trap or fixed placement (e.g., Vlad's Tower)": no such trap; Orcus Town only (orcus.lua:123-127) or bone devil summons (minion.c:95-97).
- L13624 "Demon lords can be bribed": only Geryon, Dispater, Baalzebub, Asmodeus (MS_BRIBE); cancelled if wielding Excalibur or Demonbane (makemon.c:1397-1402). L9133-9145 has it right.
- L13002 elementals "Air engulfs and suffocates ... water drowns if adjacent in water": air pummels with debris (mhitu.c:1450-1451); water elemental single 5d6 claw, no drowning.
- L13558 Charon row: #ifdef CHARON, never defined. Delete.
- L13207 black naga "poison, acid, and stoning resistance ... best of the four eats": acid and stoning resistance timed d(3,6) turns (eat.c:1082-1094); only poison permanent.
- L13354 troll "will be alive when you come back": ~75% (hack.h:1405).
- L13232 ogres "Drop decent weapons and armor": club, sometimes battle-axe; no armor (makemon.c:446-451).
- "passive 0d6 cold" (L13037), "passive 0d4" (L13010, L13038-13040, L13545): 0dN means (Lvl+1)dN (uhitm.c:5885-5888); brown mold 2d6, fire elemental 9d4. Audit at L12466 "literally zero" wrong. Script should emit real dice.
- 32 rows "poisonous-corpse" on G_NOCORPSE monsters (all & rows L13632-13660, zombies L13502-13505, ghoul L13509, green slime L13267, weres L13532-13534). Script fix: suppress on G_NOCORPSE.
- Note: audit comments L13612-13613, L13620-13621 claim poison res doesn't stop sting Str-drain; it does (uhitm.c:3131-3149; attrib.c:338-341).
Checked: Kop respawn, wraith level, giant Str, lichen/lizard rot, quantum/genetic corpses, green slime, polymorph claw guards, touch of death, Trollsbane, Vorpal Blade, eel drowning, Croesus, pudding splitting.
Style: L13635 erinys "Variable attacks; can be amplified by alignment abuse" (C comment transcribed) -> "Grows stronger the more you have offended your alignment: harder blows, flight, regeneration, a second attack." L13657 "Don't attack one — they don't fight back." em-dash, never actionable -> "Appears only to deliver mail, then leaves." L13056 "are real threats" hollow. L13080 "match the dragon elements" vague. L13129 "isn't a stable solution" engineering diction. L13525 "very dangerous" vague. L13464 doesn't orient.
Craft: "spell spell" 15 times; Str-drain labelled three ways ("poison", "drain-Str", "Str-drain"); script fix: AT_MAGC -> "casts", one label for AD_DRST. Quest labels missing for Pelias, Shaman Karnov, Lord Sato, Thoth Amon, Master Kaen, Dark One. L13565 second "priest" row inherits temple note. L13556 Wizard of Yendor "poison-res" spelling; missing teleport flags. Kops (L13129): paying the shopkeeper dismisses every Kop (shk.c:1395-1443); L11139-11142 also omits. STALE GENERATOR: build_bestiary_appendix.py still emits pre-audit text (Cyclops "Caveman quest nemesis", master lich "double-trouble", Surtur "Has Mjollnir", snakes "pit fiend", mummies "curse your worn items", trolls "burn it with fire", guardian naga "Friendly to the Healer", header "MR%"); one rerun undoes three audit passes. Port corrections into NOTES/CLASS_PROSE or mark hand-maintained. A5: marilith six attacks, Juiblex ten flags, @ table 75 rows; collapse repeats.
Top 3: fix lizard-vs-Medusa and undead turning; make the generator honest (no-corpse label, 0dN dice, Charon, labels, port corrections); fix bribe rule, elementals, add Kops pay line.

---

## Chunk 28: Intrinsic/Extrinsic Tables + What Changed (L13753-14156)
Verdict: source columns solid (every role/race level matches attrib.c:23-103); "What it does" column riddled with wrong mechanics; two rows contradict What Changed in the same chunk. What Changed well researched (30+ bullets verified) but unsorted 50-item list incl. two 3.6.0 features. Strongest: New Dangers sacrifice paragraph (L14100). Weakest: Damage resistances table.
Correctness:
- L13847/13848/13851 "Halves fire/cold/electrical damage": resistances zero it (zap.c:4423-4516). "Immune to fire damage (scrolls and potions can still burn)."
- L13850 disintegration "(still does ordinary damage)": nothing (zap.c:4468-4471).
- L13848 "lets you eat cold-resistant corpses safely": no such mechanic.
- L13844, L13853-54, L13868 multiplier notation "1/2x, 1/4x": acid chance 3 and stoning 6 vs standard 15 (eat.c:972-996) => 5x and 2.5x MORE likely; telepathy chance 1 => floating eye always grants. Plain odds: acid blob 1 in 3 (timed); lizard 5 in 6, acid blob 1 in 6 (timed); floating eye always; killer bee ~1 in 3, scorpion ~1 in 2.
- L13857 MR "magic-trap effects at 100%": no MR check (trap.c:2300-2311).
- L13858 hallucination resistance: gold dragon scales GRANT it (do_wear.c:846-850), missing; violet fungus has no hallucination attack; black light does.
- L13859 "yellow / black light bursts" blind: only yellow blinds.
- L13855 "(Stormbringer, Vorpal Blade)" drain: Vorpal beheads.
- L13871 warning "whose hit-dice exceed yours": any hostile level 4+ within ~10 squares; digit = level/4 (display.h:64-66).
- L13885 searching "every few hundred turns": rn2(85), ~every 85 turns (allmain.c:308).
- L13924 Protection row: "same-aligned", "prayer-pool", "400 zm per +1" all 3.6/invented; no alignment check (priest.c:685-691); L14028 says the 400 formula is gone.
- L13926 regeneration "about one per turn at high XL": flat +1 HP every turn (allmain.c:659-662), as L14078 says.
- L13930 Free action "(mind flayer hold, gas-spore explosion...) and to slow": mind flayers don't paralyze; slow wand ignores it (zap.c:2870). -> "Immune to paralysis (floating eye's gaze, gelatinous cube, ghoul claws, monster-cast paralysis)."
- L13932 invisibility "don't attack you unless they see-invisible": they guess your square.
- L13943 slow digestion "about 1/4 the normal rate": stops ordinary hunger entirely; only ring upkeep (eat.c:3172-3178).
- L13946 life saving "restores you to one HP": 50 + 10 x (Con/2), capped at max (end.c:707, 716).
- L13947 adornment "+1 Charisma": its enchantment.
- L13950 conflict "keeps shopkeepers from selling": a shopkeeper under conflict attacks you (shk.c:4897).
- L13944/13945 no scroll polymorphs you; sustain ability blocks potions not scrolls.
- L13821 "a Wizard with XL 17 antimagic": Wizards get teleport control at 17.
- L14030 "500 x XL guarantees protection": needs an offer in [2x, 3x) of the stated amount; 3x or more earns only thanks (priest.c:685, 706-708).
- L14049 Medusa four layouts / L14061 Orcish Town 1/7: both 3.6.0. Cut.
- L14056 monsters "unlock chests": rummage unlocked containers only.
- L14068 Gehennom teleport "not permanently": 5.0 ADDS a within-level block while a demon lord/prince is on the level (teleport.c:33-35; fixes5-0-0.txt:2679); level teleport blocked until invocation.
- L14115 "breaks any potion you drop": "usually" (fixes5-0-0.txt:2885).
- Sacrifice cap (L14025) right; gift roll 1/6 vs 3.6's 1/10.
Style: L13809 recites the headings. L13820 em-dash + restatement. L13832 "the universal extrinsic gateway for the resistance system" -> "Dragon scale mail covers more of this table than any other item." L13841 "the late-game-defining piece" vague. L13864 "the two senses that change how you play — both let you act on information..." -> "Telepathy and warning show you monsters before they reach you." L13878 "The speed system, the air-walking gear, and the niche-access tools" cut. L13958 "Not strategy-shaping outside polymorph play" jargon. L14013 "steadfast against the new knockback mechanic". L14038 "real tactical edges" / L14043 "a real lifeline" hollow. L14047 "more varied and interesting" cut. L14124-14130 three restatements. L14137 "Fog passes through doors, bat flies, vampire fights. Plan routes by form rather than direction." machine-gun.
Craft: What Changed unsorted: group "habits that now get you killed" first (unicorn horns, touch of death, monsters looting/reviving, Gehennom potions/teleport, wand of speed, alchemy, Luck cap), then "new things to use", then "numbers that moved"; merge New Dangers/New Hacks. Placement in appendix fine; add a one-line pointer in the Introduction for 3.6 veterans. Tables: link Fast, Warning, Protection rows to their chapters.
Top 3: rewrite "What it does" column vs source; cut 3.6.0 items, fix Gehennom-teleport and 500xXL, regroup; plain odds + gold dragon scales.

---

## Chunk 29: Index + Acknowledgements (L14157-15073)
Verdict: print index technically sound (280 labels resolve; zero ?? refs in book.pdf). Acknowledgements warm and well-sourced; DevTeam list matches dat/history:312-316; "May 2026" confirmed by dat/history:300 ("released on May 2, 2026"); README.md "2025" is wrong. Weak: HTML readers never see the index; ~60 entries index-audit.md marked CUT still ship; no see-also; a dozen glosses wrong.
Correctness:
- L14743 "Sokoban: entry one level above Oracle": below (L1617; dungeon.lua:21-24).
- L14317 "Damerell: ... prayer spoiler": Lahut's (L14986).
- L14866 "Wish: sources, six in total": seven (L8479-8506).
- L14832 "Vlad's: throne ... four wishes in thirteen sits": ~one sit in ten, once.
- L14643 "Prayer: cooldown, ~1000 turns": body says ~450-500 (L4350-4376).
- L14734 "Skill: slots, 2 + XL + crowning": XL+1 (+1 crowned) (u_init.c:884; L8232-8235).
- L14358 "Electric eel, six in medusa-2", L14501 "medusa-4": level-file names, from audit comments only.
- Wrong-page anchors: L14249, L14324, L14865 (bribery -> What's Different, text is in demon-prince lairs L9126-9144); L14443 Haste self -> armor-and-ac (Speed L2818); L14308 cursed bag -> effects-of-cursed-items (Containers L6764); L14431 green slime -> puddings (Delayed deaths L4231); L14762 stethoscope crowning meter -> Other Notable Tools (Crowning L4553); L14498 Excalibur odds -> the-roles (L1278/L7387); L14632 Plane of Water -> plane-of-fire; Earth/Air go to parent.
- L14375 "Fake: Delphi, a geometric joke": exists only in an audit comment. Cut.
Acknowledgements checked: Hugo/O'Donnell 38 files, Waterman/Wheaton 1991, WikiHack 2005/Sgeo, >5,000 articles, all author credits, 3.4.3 Dec 2003, 3.6 Dec 2015, Izchak 1994, DevTeam roster. No errors.
Style: L14927-14928 "longest-running continuously developed" contradicted by L15045 twelve-year gap -> "one of the longest-running open source projects in existence". L15048-15052 "The dungeon was frozen. New players descended into the same unchanging corridors ... dying in the same newly-documented ways." -> "For twelve years the dungeon did not change. Players kept writing spoilers about it anyway, and the game was deep enough to sustain a decade of fresh analysis without a single new line of code." L15039-15043 grid bug nested aside -> "the grid bug, a pun on 'software bug' that can only move along the grid". L14745 "Speed: boots, free action on 2/3 turns" ("free action" is the paralysis property) -> "an extra move two turns in three". L14384 "Flint, useless ammunition" vs L14266. L14499 "Kobold meat, poisonous and pointless". Jargon: farlook (L14208), instakill (L14320), range-kill (L14331), polypile head (L14636).
Craft: web readers get no index (::: print-only L14155); template.html:614-655 hand-typed 32-entry "humorous index" in the search box with two dead anchors (the-displacer-beast, identification-by-engraving) and stale ones (Elbereth -> engravings; unicorn horn -> changelog). Generate the HTML index from index-draft.md. index-audit.md recommends 189 cuts; ~60 still ship (L14190, L14550, L14557, L14345, L14516, L14355 "Eating mistakes, top forty" no such list). No see-also entries; no head word for Magic resistance, Free action, Telepathy, Poison resistance, Intrinsics, Price identification, Hunger, Corpses, Conducts, Options, Saving/Bones, Touch of death, Riders, Shops, Lycanthropy. Word-split heads: "No:" (L14590), "First:", "Feel:", "Early:", "Mysterious:", "Strange:", "Supply:", "Holy:", "Killing:", "Large:". Run-on sub-glosses fused into one link (L14286 Cockatrice, L14290, L14473, L14632, L14743, L14832). Symbols filed under "0-9" (L14167-14178). L14518, L14555 "pp." format. Best: RGRN paragraph L14932-14940.
Top 3: HTML index from the print list; apply index-audit cuts + see-also heads; fix seven wrong glosses, re-anchor eleven.

---

## Prose sweep L4752-5595 (Identification)
1. L5034 "it's identify. Period. That's one of the most useful scrolls in the game and you just found it for free." -> "it's identify; nothing else shares that price."
2. L5036 "The $60 and $80 groups are pure upside too" -> "safe to read too: enchant weapon or blank paper at $60, enchant armor or remove curse at $80."
3. L5516 "The rule of thumb: ... Kick it first. Check BUC second. Then pick it up." staccato, and the pick-up test requires picking up -> "So kick a gray stone, or let your pet walk over it, before you lift it."
4. L5585 "the most lethal mistake on the identification table" -> "(a failed read can paralyze or teleport you, and the price tells you the level but not the spell)".
5. L4807 "Blessed items are helpful beyond their description, uncursed items work as advertised, and cursed items find creative ways to ruin your day." -> "A blessed item does its job a little better than the uncursed version, and a cursed one does it worse or backwards."
6. L4815 "tells you something about clerical paranoia" -> "(Priests are the exception: they see it on sight.)"
7. L5435 "can ruin a run" -> "both candidates curse themselves when worn, and cursed fumble or levitation boots stay on until you lift the curse."
8. L4956 "This is the shop's own stock talking. An item you or a monster dropped..." closer re-says -> one sentence.
9. L5544 "That message is your cue that the merge propagated a known property..." restates; cut.
10. L4908 "unfamiliar" vs L4992 "pennypinching" for the same 1-in-4 surcharge: one name.
11. L5590 "Reach for the cheapest, safest method first: altars and shops are free, engrave-testing costs one charge, use-testing costs more and carries risk, and scrolls of identify are the precious last resort." re-says the workflow; cut or "Cheapest method first; a scroll of identify only for what's left."
12. L5101 "extremely informative" -> "Only four rings cost $300, and three of them (conflict, polymorph control, teleport control) are among the best in the game."
13. L5468 "look identical but have wildly different value" -> "Four different stones share the 'gray stone' look, from a luckstone worth carrying all game to a loadstone you can't put down."
14. L5086 "(one very good, one very bad). The $200 group is packed with excellent potions." -> concrete sickness description; drop the $200 sentence.
15. L4895 "narrow down the possibilities enormously" -> "narrow the possibilities to a handful".
16. L5571 "Suddenly half your inventory is narrowed" -> "Most of what you carry drops to two or three candidates."
17. L4793 "and those opinions have consequences" throat-clearing; cut.
18. L5346 "has the best payouts but two hidden traps" gambling metaphor -> "is all worth having, but two of them are awkward to test by drinking."
19. L4983 "(deterministic per object; ...)" implementation voice -> "fixed for that item's whole life, so two stacks of the same appearance quoting differently is the giveaway".
20. L5418 "fall into informative tiers" -> "the price separates the safe boots and cloaks from the cursed ones."
Reads best: opener L4758-4767; BUC bullets ("abandonment issues", "in the most literal architectural sense"); pet-testing paragraph; closet-scroll tip; "If a wand costs $500, you are having a very good day"; $200-potion testing; armor-in-a-shop warning; four gray-stone tests.

---

## Prose sweep L5596-6533 (Provisions, Apothecary, Scrolls, Wands)
1. L5903-5908 "Speed is one of the most important buffs ... the difference between trading blows and hitting twice before they swing once. ... The potion is the real prize." -> "Intrinsic speed gives you an extra move about every third turn: over a long fight, a free hit or a free step back. ... The potion is the one to drink."
2. L6494-6499 "Self-polymorph is one of the most interesting tools in the game ... which is where the real fun begins." -> "Self-polymorph puts you in another monster's body. With polymorph control you choose which, and that is when it becomes worth doing on purpose:"
3. L6365-6369 digging "Essential utility. Dig through walls, dig down, dig through rock. It also doubles as..." -> "A zap at a wall opens a passage. A zap at the floor drops you to the level below, the quickest exit from a fight you're losing."
4. L5790-5792 "the highest-density source of ascension-kit intrinsics in the game; poison resistance ... the most important single intrinsic to bank" -> "A gelatinous cube can hand you fire, cold, shock, or sleep resistance in one meal. Get poison resistance first, from the first spider or bee you kill; without it, poisoned stings and arrows drain your Strength."
5. L6362 death "One of the best offensive tools in the late game." -> "It does nothing to the undead or to demons."
6. L6171-6172 "Invaluable in Gehennom's maddening mazes, where mapping by hand could take a lifetime you don't have." -> "Most useful in Gehennom's mazes, which take hundreds of turns to walk out by hand."
7. L5799-5802 "every one of them yields an intrinsic when eaten ... (a 5.0 food-handling detail...)" -> "most of them yield an intrinsic when eaten (a lichen or shrieker is just food)."
8. L6208-6209 "Never price-ID it by reading it on your own square." -> "An unblessed read burns your own scrolls and potions, so it is a bad scroll to test-read."
9. L5962-5964 "Both inputs are reasonably common and individually low-value, but the output is one of the catalysts that feeds the main healing chain." -> "Both are common finds, and gain level is the ingredient the healing chain keeps running out of."
10. L6401-6402 "Useful for slipping through a dangerous area or turning a fight in your favor." -> "Monsters that can't see invisible have to guess where you are, and often swing at empty air."
11. L6153-6155 "@ is lethal for every role, not just elves and humans, since your role-self is an @" -> "Blessed-genociding @ kills every character, whatever the race, because your role is itself an @ species."
12. L6164-6165 "naming mind flayers buys an Int-fed feast if you're polymorphed into one" rarely actionable; cut.
13. L6386-6390 "Do NOT put this wand in a bag of holding ... Keep it separate" -> "Don't put it in a bag of holding: the bag and everything inside vanish."
14. L5923 "where you stand safely on the tile to dip" -> "which supplies the water without spending a bottle of it" (dips can curse or summon moccasins).
15. Hollow closers to cut: L5893 "You can never have too many of these."; L6116 "You will never have enough of these."; L6110 "The bread and butter of dungeon life."; L6119 "The path to endgame power."; L6373-6374 "Enormously useful for escaping trouble..."; L6158 "Read carefully."; L6396-6397 "Risky but powerful."; L5668 "Never eat old corpses. If in doubt, don't eat it."
16. Accuracy: L6505-6506 brown mold burns (cold); L6509-6511 polymorph HP ratio (new form's own hit dice).
Reads best: hunger opener (L5628-5632); tin-opening (L5688-5697); holy-water pair (L5911-5925); "Chained alchemy climbs two at a time" (L5968-5977); sickness-cure bullet (L6008-6012); "the gas doesn't pick sides" (L6191-6198); ray-bounce (L6285-6290); stasis (L6406-6415); polymorph bullets (L6501-6516).

---

## Prose sweep L8166-8914 (Skills, Wishes, Artifacts)
1. L8699 "the drain resistance alone is worth carrying it, even after you have a stronger weapon" contradicts L8811-8815 (needs wielding) -> "its drain resistance works only while it is wielded, so switching to a stronger weapon gives that up."
2. L8898-8899 "'a free wish per ~1000 turns.' Pairs especially well with marker-stockpiling strategies." -> "#invoke recharges one wand, ring, or magic marker, then needs a cooldown. Its best single use is putting a charge back into the Castle's wand of wishing."
3. L8504 "a very real chance of everything going wrong" -> "A wish is one of about a dozen possible outcomes of a sit; the others include an electric shock, a drained attribute, and a summoned court."
4. L8892 "despite the weapon's reputation"; L8871 "despite what older spoilers say": cut, state the fact.
5. L8693 "were historically considered flavour pieces"; L8749-8750 "not the flavor piece it used to be" -> "Snickersnee and Sunsword gained new powers in 5.0: a free reach attack each turn and an on-demand blinding flash." / "Two hits a turn from one weapon puts it ahead of a plain katana for most Samurai."
6. L8852 "Few artifacts change a role's late game as much as this one." -> "With it a Healer can hold a corridor in melee, which the role otherwise cannot."
7. L8727 "huge in the early-to-mid game" -> "a steady gain while your own level is still low."
8. L8911 "For a spell-caster this is irreplaceable." -> "Energy is what a Wizard runs out of first, so the regeneration matters more than the portal."
9. L8892-8893 "One of the strongest artifacts in the game, the Samurai's reward for a hard quest." closer; cut.
10. L8864 "a powerful passive on a slot they can use"; L8901-8902 "the most generous carried passive in the game" gamer jargon -> "Monks fight without body armor, so magic resistance that sits on the face fills a gap." / "the strongest carry effect of any quest artifact: it counts as a luckstone, grants warning, and halves both spell and physical damage taken."
11. L8443-8444 "come online to upgrade the late game without leaving the early game starving" -> "and school ranks can wait until you have enough energy to cast often."
12. L8532 "when overconfidence kills more adventurers than monsters do" -> "(one free death; most valuable on the Astral Plane, where there is nowhere to retreat and heal)."
13. L8214-8215 "more practice, higher rank, more deadly swings" -> "The game tracks this as a skill rank."
14. L8290 "is why dedicating to a single weapon matters" -> "Going from Unskilled to Expert with one weapon moves your to-hit by 7 and your damage by 4 on every blow."
15. L8488 "so persistence pays off" -> "so keep sitting until it does."
16. L8522-8523 "the second pillar of not dying to wands" -> "(reflection + AC; bounces wand rays and dragon breath back at the source)."
17. L8879 "Combined with the Ranger's ranged specialization this is the role's centerpiece." -> "A Ranger with the Longbow never runs out of arrows."
18. L8493 "some minimalist ascenders skip it entirely on principle" cut.
19. L8513 "or commitment" -> "Anything beyond that is luck: extra lamps, fountain demons, a recharged wand."
20. L8848 "the Healer's salvation" apposition -> "(Healer)".
Reads best: Wish Syntax bullets (L8561-8595), "You had one wish; spell out the BUC and the plus"; Enhancing Skills opener ("a shinier sword you have no training in is usually a downgrade"); blank-cell explanation; Cleaver, Magicbane off-hand, Sunsword, Naming Sting and Orcrist paragraphs; cockatrice joke at top of Wishes (keep).

---

## Prose sweep L853-1494 (Lay of the Land, Field Guide, Points of Interest)
1. L1129 "Use non-iron alternatives (mithril, silver, dragonhide)": no dragonhide weapons (audit L1063) -> "Fight one with a wooden or silver weapon (elven blades are wood) and take iron armor off first; mithril armor is safe."
2. L1134 "Confuses on sight. Avoid looking at them directly." -> "Its gaze confuses you whenever you can see it; a blindfold is the only way around that."
3. L1090 "the single most common cause of death on the public server" -> "on the first few levels a pack of them kills more characters than anything else."
4. L1043-1046 "less predictable in a friendly way: more terrain types to fight in, more item discovery, and the occasional educational ambush" designer triplet: cut.
5. L1033-1038 "traps in everything but name ... recognize the pattern, retreat, prepare, return" sermon -> "Treat these as traps. Spider nests and buried zombies scale with depth ... back out and return with what the room calls for."
6. L1299-1300 "the single most useful piece of furniture in the dungeon" cut.
7. L1308-1310 "free, unlimited, and works on everything ... your testing laboratory" -> "It costs nothing and never runs out, so haul every unknown piece of gear to the first altar you find before putting it on."
8. L886-888 + L896-897 same thought twice -> one opener: "The Mazes are laid out fresh every game, but the branches, the special levels, and their rough depths are the same, so you can always tell what is coming next."
9. L1431-1433 "more hazard than help ... not something to rely on" verdict, repeats L1372: cut.
10. L1094 "Don't trade blows with one in melee until your AC is solid" -> "A dwarf with a mattock hits for 1d8 plus the mattock's d12, enough to kill a first-level character in two swings."
11. L1089 "the math catches up fast" -> "two 1d6 bites a turn wear a low-level character down faster than the fight looks."
12. L1117 "Rare, but if you see one you're in for a fight." -> "Rare. Four 2d10 attacks a turn, about 44 damage if all land, at speed 12."
13. L1126 "The fall does serious damage. Hard to spot in advance." -> "The bite is 2d6 (iron piercers 3d6, glass 4d6), and you get no warning."
14. L1139 "the real prize is the corpse: a chance at cold resistance you can bank early" -> "The corpse gives cold resistance about one time in three."
15. L1140 "Uncommon but a fair fight if geared up." -> "Two 3d4 claws and a 3d6 bite each turn, but slow (speed 8)."
16. L1275-1276 "is a different gamble, and one that Lawful characters should know by heart" -> "is how a lawful character gets Excalibur."
17. L1283 "The conventional wisdom: a lawful Knight" -> "A lawful Knight".
18. L1314 "deepens your relationship with your god" -> "earns your god's favor".
19. L1004-1006 "They wake not when you enter, but from the noise" (see chunk 3 correction).
20. L1016-1020 three sentences of restatement about themed rooms -> "The dungeon also has dozens of themed rooms, odd in shape (pillars, a room inside a room) or in contents. Some to look out for:"
Reads best: Excalibur paragraph (L1283-1294); vault section (L1466-1482); sink kitchen-sink joke (L1370); "a wish list shuffled with a hit list" (L1336); "vanish in a puff of logic"; long worm "can be a corridor in themselves" (L1136); ghost-as-a-gap (L1167); magic-fountain and water-demon paragraphs (L1241-1273).

---

## yba strategy analysis vs the book (agent)
Sources: yendorbound/ STRONG_PLAYER_GAP_ANALYSIS.md (GAP), HUMAN_STRATEGY_GAPS.md (HSG), STRATEGY_REPAIR_PLAN.md (REPAIR), LESSONS.md. Caveat: yba is an AutoAscend descendant: no long-horizon planning, never wears untested armor, flees only when 2+ monsters adjacent. Bot-specific findings flagged.

1. Kills/keeps alive. Bot deaths (39-layout panel): 34/39 died; 16 attrition, 9 melee-commit, 5 unseen attacker, 3 bursts, 1 starvation (GAP:1138-1142). 104-run fleet: 83 deaths; 34 attrition, 15 unseen, 14 melee-commit, 10 starvation (LESSONS:1260-1265). Re-baseline: 28 of 38 deaths on D3-D5 trading blows with hill orc/rothe/dwarf/centaur/killer bee/gnome pack (REPAIR:657-679). Mines: 54/104 enter, 33 stall on Mines:1, 21 die there, entering at XL3-4/AC3-8 (HSG:107). Werebeasts 18/130 deaths, Dlvl 1-3, median turn 4200 (LESSONS:12021-12026). Human early deaths (565, before T5000): dwarf 5.5%, gnome lord 4.2%, slipped mounting a pony 3.9%, small mimic 3.7%, giant bat 3.0%, wand 2.5% (GAP:1538-1549); humans starve 0.2%. Bot survives better per turn (T2000 94.9% vs 62.3%) yet converts D3->D5 at 21% vs 72.5% (GAP:1794-1798): 32% of turns searching, 82% yielding nothing; 55% of searches with a known down stair (GAP:2104-2110).
What helped: Elbereth the instant a werebeast "summons help" (-7 fleet deaths, best single change, LESSONS:12030-12035); not spending prayer at Weak so Fainting still had a window (-10 deaths, LESSONS:2592-2625); wearing body armor under the cloak; standing still and receiving the fight rather than stepping toward it (deaths 105->94, LESSONS:12446-12454); XL4 floor before leaving D1; Minetown protection donation (GAP:1604-1610).
What failed: pre-emptive retreat to corridor chokepoint (save 3/lose 4, LESSONS:8096-8105); deferring melee vs homunculus (+4 deaths); flee gate for losing 1v1 (over-flees); door-closing on pursuers (flat); pet retention (bot-specific).

2. Matters more than the book says:
- Wear the armor you find. 73% of bot heroes have no body armor at D3 (REPAIR:60); 300 pieces carried never worn; owner's ruling: only boots and gloves are genuinely dangerous cursed (REPAIR:1143-1144). Book L7028-7030 "BUC-test before donning" + flowchart ending at identify -> a beginner with no altar and a lost pet fights dwarves at AC8. Book cites ~10% curse rates (L11529, L11924).
- Werecreatures (L3408-3427) cover lycanthropy, nothing about the fight: Elbereth at the summons message is the fix; silver never found before Dlvl 4 in were-death sessions; human-form @ ignores Elbereth (LESSONS:5794-5800).
- Throwables as survival item: every non-combat D3-D5 death class collapses into "no ranged option" (REPAIR:721-724; floating eyes blocking routes in 36 games REPAIR:1514; rothe "correct behavior is not to be adjacent at all" LESSONS:10901-10904). Book: one packing line (L646-648).
- Retreat upstairs as ordinary play: 79.4% of humans go up before T2000; more-retreating half reaches D15 ~2x as often (GAP:1481-1500). Stair tiles accumulate monsters on return (LESSONS:10803-10805). Book: one line (L2986-2991); Rule 1 sends beginners to a corridor.
- Full-HP discipline: humans spend 93% of early turns at >=80% HP; 88.5% of descents at >=90% (GAP:1369-1436). Book: "at high HP" (L3162).
- Hunger means go down: "a stripped level has no food by definition" (REPAIR:1225-1228); prayer at Weak spent the window, fainted to death 865 turns later. Book L5651/L5811 "pray when Weak", no instruction to leave the level.

3. Matters less / backfires:
- Corridor chokepoint (L710-725, 815-817, 3210-3211): corridor has two faces; only a closed door has zero (LESSONS:11351-11361); rothe still gets three attacks.
- Mines bar "XL5, sleep res, AC<=0" (L3181-3183): humans reach D5 at XL4/HP38/AC3 (GAP:1132-1133); waiting has its own body count. Book also says Minetown "worth visiting early" (L1567).
- Wall-tapping (L2289-2298, Rule 5): squares searched 30+ times found one staircase in 12,379 turns (GAP:2549-2560).
- "XL near Dlvl" (L3155-3165): winners and losers descend at the same pace; max HP not depth is the only stock positive (GAP:1752-1765). Fine as a floor; "clear, identify, level up, then descend" is the non-converting grind.
- Elbereth "free, instant" (L2498-2499, 3063): five of five rothe death tails died mid-write (LESSONS:10887-10892).
- Burdened: book already firm; keep.

4. Bot failures = beginner failures: caution that never converts (untested armor, not descending hungry, searching with known stair); swinging until dead at one strong monster because "not surrounded yet" (REPAIR:671-679); entering Mines at XL3-4 AC8; losing the pet by D2 then no curse test; writing Elbereth after contact; "cautious becomes stalled".

5. Human play not in book: HP discipline and retreat numbers above; 0.2% starvation; a quarter to half of humans use healing/scare/prayer/teleport/Elbereth before T2000 (GAP:1516-1525); gold is spent, median 34 zm at T3000; Healer worst role D3->D5 (57.5%), Knight best (84.6%) (GAP:1957-1958); casters who cast 6-20 spells before D3 cross more (77% vs 67%, n=35); a strong Valkyrie leaves D1 at T285 without searching or clearing, Elbereth by T460, price-ID by T560, altar T1746, sacrifice T13k (GAP:414-446). Pony-mounting is 3.9% of early human deaths; book warns (L338-339) without the number.

6. Ten changes: (1) Armory L7028-7030: at AC 6 or worse with no altar/pet, wear found body armor, helms, shields, cloaks now; test only boots and gloves. (2) Werecreatures L3408: Elbereth at "summons help"; human-form @ walks through it; silver isn't found at that depth. (3) Rule 1 + "Caught in the open" (L710-712, 813-817): order escapes stairs > closable door > corridor; stop and let the pack arrive rather than stepping toward it. (4) What to Pack L646: promote a throwing stack to a golden rule; name never-adjacent monsters (floating eye, rothe, homunculus, soldier ants). (5) Mines readiness L3181-3183: reachable bar (AC ~5, XL5, full HP, throwing stack, escape item); waiting has a cost. (6) Provisions L5654-5656 + Rule 5: when Hungry with no food, take the stairs down; prayer resets hunger once. (7) Searching L2276-2298: if a down stair is known, take it. (8) "Trade hits"/"Know when to run" (L3013-3017, 3043-3053): decide after the first exchange. (9) Elbereth practical use (L2498-2503, 3063-3068): write before contact; below half HP with a multi-attacker adjacent, stairs beat a dust write. (10) Pacing L3155-3165: rest to full after every fight; don't take stairs below ~90%; expect the pack at the stair on return.

---

