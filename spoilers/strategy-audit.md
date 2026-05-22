# Strategy Audit: Community-Sourced Additions Worth Considering

*Compiled 2026-05-22 from a parallel sweep of NetHackWiki, the Fandom
mirror, RGRN archives at steelypips.org, Damerell's strategy texts at
chiark.greenend.org.uk, and Reddit r/nethack.*

This is a **planning document** — none of the ideas below have been
incorporated into the spoiler. Each entry names a topic, names a
source, identifies which section of the spoiler it would extend, and
notes the strategic payoff. Items deliberately filter out trivia
(per the book's "no trivia" rule), and only flag things that either
save a beginner's life, change a strategic decision, or carry real
community color.

Six clusters, ~160 candidate additions in total. Treat as a menu.

---

## Cluster 1: Character & Early Game

### Choosing Your Expedition / Roles
- **Wizard cat is the default; Wizard food crisis is the most common early death.** Wizards always start with a kitten and zero food rations, and many Wizard runs end to starvation before the first altar. Standard advice: always eat fresh corpses, and don't try to coexist with a hungry pony.
  - **Source**: [Wizard - NetHack Wiki](https://nethackwiki.com/wiki/Wizard), [Spellbook of force bolt](https://nethackwiki.com/wiki/Spellbook_of_force_bolt)
  - **Apply to**: Roles (Wizard paragraph) — a one-sentence "starts with no food" warning would save lives.
  - **Why interesting**: It's a class-specific death trap not currently signposted; "Wizards starve" is a community proverb.

- **Force bolt is the Wizard's early answer, but skip nymphs and avoid potion stacks with it.** Force bolt shatters potions on the ground and breaks nymph-carried mirrors (−2 Luck per shattered mirror).
  - **Source**: [Spellbook of force bolt - NetHack Wiki](https://nethackwiki.com/wiki/Spellbook_of_force_bolt)
  - **Apply to**: Roles (Wizard paragraph) or a "Wizard early game" note
  - **Why interesting**: Concrete tactical guidance for the role's signature spell; a beginner won't guess that their main attack destroys loot.

- **Samurai: drop the wakizashi.** Community consensus is that the starting wakizashi is dead weight — find a long sword as a second weapon to share katana skill in #twoweapon.
  - **Source**: [Samurai - NetHack Wiki](https://nethackwiki.com/wiki/Samurai)
  - **Apply to**: Roles (Samurai paragraph)
  - **Why interesting**: Changes a decision (whether to lug the backup blade) and clarifies what "Samurai martial kit" means in practice.

- **Monk: never wear body armor; the robe is a spellcasting powerhouse.** Body armor inflicts a −20 to-hit penalty for Monks (effectively unhittable), while the starting robe gives a spellcasting bonus larger than the Wizard's.
  - **Source**: [Monk - NetHack Wiki](https://nethackwiki.com/wiki/Monk)
  - **Apply to**: Roles (Monk paragraph)
  - **Why interesting**: A new Monk will absolutely pick up the first leather armor they see and wonder why they can no longer hit anything. Saves a run.

- **Archeologist starts with a stack of food rations and a fresh tinning kit — starvation should never kill them.** The combination of starting rations plus on-demand tin-of-monster lets an Archeologist preserve poison-resistance corpses (killer bee, etc.) for safe eating later.
  - **Source**: [Archeologist - NetHack Wiki](https://nethackwiki.com/wiki/Archeologist), [Tinning kit - NetHack Wiki](https://nethackwiki.com/wiki/Tinning_kit)
  - **Apply to**: Roles (Archeologist paragraph) and What to Pack
  - **Why interesting**: The tinning kit's strategic role (intrinsic delivery vehicle, not just food preservation) is non-obvious from the description.

- **Priest: keep one holy water in reserve at all times so you can renew the cache.** A Priest with a single holy water + potions of water + altar can dilute and re-bless indefinitely.
  - **Source**: [Potion of holy water - NetHack Wiki](https://nethackwiki.com/wiki/Potion_of_holy_water)
  - **Apply to**: Roles (Priest paragraph)
  - **Why interesting**: Changes a decision — beginners drink or pour their starting holy water and lose the renewable cycle.

- **Rogue: throw daggers, don't stab.** Rogues get +1 multishot on thrown daggers even at Unskilled, and the backstab bonus applies to throws against fleeing monsters. Elbereth + thrown daggers is the canonical Rogue combo.
  - **Source**: [Rogue - NetHack Wiki](https://nethackwiki.com/wiki/Rogue), [Backstab - NetHack Wiki](https://nethackwiki.com/wiki/Backstab)
  - **Apply to**: Roles (Rogue paragraph)
  - **Why interesting**: The book describes Rogues as melee assassins; in practice, they're throw-centric. Beginners often try to melee with the short sword and die.

- **Ranger: hoard the +2 stack, mulch the +0 stack last.** +2 arrows break at ~25% per hit vs. ~67% for +0; blessed +2 arrows break ~1 in 200. Save the good ammo.
  - **Source**: [Arrow - NetHack Wiki](https://nethackwiki.com/wiki/Arrow), [Ranger - NetHack Wiki](https://nethackwiki.com/wiki/Ranger)
  - **Apply to**: Roles (Ranger paragraph)
  - **Why interesting**: New Rangers blow through their +2 stack on level-1 newts. Concrete mulch-rate guidance changes behavior.

- **Tourist: Elbereth + camera + pet is the early-game survival kit.** The standard Tourist play is to write Elbereth in dust, blind threats with the camera flash, and let the pet finish them off while you sit still.
  - **Source**: [Tourist - NetHack Wiki](https://nethackwiki.com/wiki/Tourist)
  - **Apply to**: Roles (Tourist paragraph)
  - **Why interesting**: The book mentions the camera but not the integrated survival loop. Tourists are famously hard early; this is the move.

### What to Pack / Early Shopping List
- **Stash near the down-stairs of the previous level.** Veteran players drop their non-essentials one level up so monsters can't loot the pile while they explore.
  - **Source**: [Stash - NetHack Wiki](https://nethackwiki.com/wiki/Stash)
  - **Apply to**: What to Pack (Restraint paragraph) or a new "Stashing" note
  - **Why interesting**: Directly addresses the "I want to keep it but can't carry it" problem the Restraint paragraph hints at without solving.

- **Burdened is more dangerous than it looks because of speed.** Burdened drops you under speed 12, which lets monsters land double hits on a single player turn — surprise deaths.
  - **Source**: [Encumbrance - NetHack Wiki](https://nethackwiki.com/wiki/Encumbrance)
  - **Apply to**: What to Pack (Restraint paragraph) and Dungeon Hazards
  - **Why interesting**: Gives a concrete mechanical reason for the "don't be Burdened" rule beyond "annoying."

### Your First Descent / Golden Rules of Early Survival
- **Elbereth in dust works ~73% of the time and erodes the moment you move.** Each letter has a 1/25 chance to garble, and dust engravings smudge with any action. Burned (wand of fire/lightning) is the only durable form.
  - **Source**: [Elbereth - NetHack Wiki](https://nethackwiki.com/wiki/Elbereth)
  - **Apply to**: Golden Rules — add a brief "Elbereth, briefly" note for early game; the existing Elbereth section is much later in the book.
  - **Why interesting**: Beginners read "engrave Elbereth" advice on forums and don't know it requires a re-engrave after every step. The garble rate also explains why their first attempt sometimes attracts more attacks (botched engravings can scare you).

- **Always eat newt corpses if you cast spells.** Eye-of-newt has a 2/3 chance to restore 1–3 Pw and can occasionally raise max Pw by 1. The book mentions this in the field guide but not in the early-game corpse-eating rule.
  - **Source**: [Newt - NetHack Wiki](https://nethackwiki.com/wiki/Newt)
  - **Apply to**: Golden Rules (Rule 2) — promote from trivia tier to "Wizards/Priests should always eat newts"
  - **Why interesting**: Free mana on demand for spellcasters; the first sustainable mana source they encounter.

- **Quick alignment-record repair: kill always-hostile fungi and insects.** New players who accidentally swing at a peaceful watchman get scared off prayer for the rest of the run; the recovery move is to grind alignment back with always-hostile easy kills.
  - **Source**: [Alignment record - NetHack Wiki](https://nethackwiki.com/wiki/Alignment_record)
  - **Apply to**: Golden Rules (Rule 4, prayer) or Dungeon Hazards
  - **Why interesting**: Saves a run after an honest mistake. Most beginners don't realize alignment is recoverable.

### Dungeon Hazards
- **Falling down stairs is lethal if you're wielding a cockatrice corpse.** The "1–3 HP nuisance" footnote in the book is incomplete; the famous death scenario is the petrified-while-falling case.
  - **Source**: [Encumbrance - NetHack Wiki](https://nethackwiki.com/wiki/Encumbrance), [Lessons learned the hard way](https://nethack.fandom.com/wiki/Lessons_learned_the_hard_way)
  - **Apply to**: Dungeon Hazards (Falling down stairs)
  - **Why interesting**: Changes a "minor annoyance" warning into a real survival lesson once cockatrices enter the picture.

### Making Friends — Starting Pets
- **Default pet by role: Wizard always gets a kitten; Caveman always gets a little dog (Slasher); Samurai's dog is named Hachi by default.** Other roles randomize.
  - **Source**: [Pet name - NetHack Wiki](https://nethackwiki.com/wiki/Pet_name)
  - **Apply to**: Starting Pets
  - **Why interesting**: Colorful, character-building detail (Hachiko reference); also reframes the kitten-vs-dog "choice" as mostly fixed.

### Feeding and Loyalty
- **Pets only need to eat — the food doesn't have to come from your hand.** Tameness +1 per meal regardless of source, including shop tripe the pet steals (no shopkeeper bill if you didn't pick it up). Apport is the only stat that requires hand-feeding.
  - **Source**: [Pet - NetHack Wiki](https://nethackwiki.com/wiki/Pet), [Tripe ration - NetHack Wiki](https://nethackwiki.com/wiki/Tripe_ration)
  - **Apply to**: Feeding and Loyalty
  - **Why interesting**: Distinguishes loyalty (auto) from fetching behavior (requires personal feeding) — currently conflated in the book.

- **Knight starvation trick: let the pony go feral, let it nearly starve, then re-tame with one carrot.** Re-taming resets hunger to Satiated, so you save apples/carrots over the long haul.
  - **Source**: [Pony - NetHack Wiki](https://nethackwiki.com/wiki/Pony), [Knight - NetHack Wiki](https://nethackwiki.com/wiki/Knight)
  - **Apply to**: Feeding and Loyalty or Knight paragraph
  - **Why interesting**: Counterintuitive, colorful, role-specific tactic that solves the steed-food problem.

### What Pets Do / Keeping Your Pet Alive
- **Sokoban exempts pets from tameness loss.** Pets left in Sokoban do not decay loyalty no matter how long you're away — the safest off-level pet boarding house in the dungeon.
  - **Source**: [Sokoban - NetHack Wiki](https://nethackwiki.com/wiki/Sokoban), [Pet - NetHack Wiki](https://nethackwiki.com/wiki/Pet)
  - **Apply to**: Keeping Your Pet Alive
  - **Why interesting**: Concrete strategic guidance — Sokoban is the recommended kennel while you do the Quest or Mines runs.

- **Pet polymorph pantheon: Archon > silver/gray dragon > winged gargoyle > guardian naga > balrog.** The book mentions titan, balrog, gray dragon, Archon; community ranks silver dragon highly for reflection-from-beams and gargoyle/naga for self-replicating pets via eggs and paralysis/blinding multi-attacks.
  - **Source**: [Forum:Best ever pet polymorphs - NetHack Wiki](https://nethackwiki.com/wiki/Forum:Best_ever_pet_polymorphs.), [What are the best pets?](https://www.alt.org/nethack/mirror/www.nethack.de/spoiler/32pets.txt)
  - **Apply to**: What Pets Do (Upgrading your pet)
  - **Why interesting**: Expands the existing tier list with the silver-dragon-for-beam-reflection insight and the gargoyle-egg trick (pet self-replication) — both genuinely change endgame planning.

- **Pet-shoplifting via doorway: items dropped in the shop doorway count as outdoors.** A pet (or any monster) can shuffle inventory to the threshold square, where the shopkeeper considers it leaving the shop — no bill.
  - **Source**: [Stealing from shops - NetHack Wiki](https://nethackwiki.com/wiki/Stealing_from_shops)
  - **Apply to**: What Pets Do (Shoplifting)
  - **Why interesting**: The mechanism — *what counts as outside* — is the missing piece; the book describes the trick but not the actual rule beginners can exploit.

- **Wand of polymorph on your own pet risks system shock; polymorph traps don't.** Zapping yourself or zapping the pet can kill it via shock; a polymorph trap reroll is the canonical safe way to upgrade a beloved companion.
  - **Source**: [Polymorph - NetHack Wiki](https://nethackwiki.com/wiki/Polymorph), [Wand of polymorph - NetHack Wiki](https://nethackwiki.com/wiki/Wand_of_polymorph)
  - **Apply to**: What Pets Do (Upgrading your pet)
  - **Why interesting**: Saves the pet you've raised since level 3 from a misuse of the wand.

---

## Cluster 2: Identification

### A Practical Identification Strategy / BUC
- **Sell prices are more reliable than buy prices for ID** — the ~25% random buy surcharge applies to buying only, not selling; selling gives a cleaner read on base price.
  - **Source**: [Price identification](https://nethackwiki.com/wiki/Price_identification)
  - **Apply to**: The Price Is Right (the book mentions both surcharges but doesn't tell readers which side to *prefer* for ID)
  - **Why interesting**: A simple workflow change ("get a sell quote, then buy if you want it") cuts the ambiguity tier-jumping the book already warns about.

- **The "no food in the way" rule for pet curse-testing** — pets will happily walk over a cursed pile if there's food on or adjacent to it; remove food before testing, or your pet's behavior is meaningless.
  - **Source**: [Pet](https://nethackwiki.com/wiki/Pet) / [Curse-testing](https://nethackwiki.com/wiki/Curse-testing)
  - **Apply to**: BUC (the Pet testing paragraph)
  - **Why interesting**: A common silent-failure mode of the technique the book recommends — beginners get a "safe" reading on a cursed item because their pet was hungry.

- **"Moves reluctantly" is the actual cursed-item tell** — when a pet *does* step on a cursed pile (because it's chasing food or whistled), the game prints a "reluctantly" message; that's still useful BUC info.
  - **Source**: [Curse-testing](https://nethackwiki.com/wiki/Curse-testing)
  - **Apply to**: BUC (Pet testing)
  - **Why interesting**: The book treats pet testing as binary (walks or doesn't); the message also fires on partial-walks and is the more reliable signal.

- **Pets can't distinguish blessed from uncursed, and autocurse-on-wear items defeat the test** — a non-cursed helmet your dog walked over may still be a dunce cap or helm of opposite alignment that will curse itself the moment you put it on.
  - **Source**: [Autocursing](https://nethack.fandom.com/wiki/Autocursing) / [Pet](https://nethackwiki.com/wiki/Pet)
  - **Apply to**: BUC (Pet testing) and Use-Testing (Armor)
  - **Why interesting**: This is the load-bearing limitation of pet testing — the book mentions auto-curse items in the armor section but doesn't connect the two.

### Price Is Right / Scroll Prices / Potion Prices / Ring Prices / Wand Prices / Amulet Prices
- **Throw items into a shop to price-ID outside the shop's class** — you forfeit ownership, but the shopkeeper will then quote you the buy price.
  - **Source**: [Price identification](https://nethackwiki.com/wiki/Price_identification) / [Shop](https://nethackwiki.com/wiki/Shop)
  - **Apply to**: The Price Is Right
  - **Why interesting**: Lets a traveler price-ID a ring in a scroll shop, or wand in a potion shop — a strategically meaningful unlock the book doesn't mention.

- **Use #chat to get the price without picking up** — when you have teleportitis or can't safely carry an item, stand on it and chat with the shopkeeper for the quote.
  - **Source**: [Stealing from shops](https://nethackwiki.com/wiki/Stealing_from_shops)
  - **Apply to**: The Price Is Right
  - **Why interesting**: Useful trick for teleportitis-afflicted runs that would otherwise lose price-ID access entirely.

- **A scroll alone in a one-square closet is "practically always" teleportation** — extremely high-probability dungeon-feature heuristic.
  - **Source**: [Talk:Scroll of teleportation](https://nethackwiki.com/wiki/Talk:Scroll_of_teleportation) / [Damerell ID FAQ](https://www.steelypips.org/nethack/id_faq.html)
  - **Apply to**: Scroll Prices (or A Practical Strategy)
  - **Why interesting**: A vivid free-ID trick the book doesn't mention; teleportation is one of the most useful $100 scrolls and disambiguating it saves an identify.

- **Spellbook price = 100 × spell level** — price-ID a spellbook to know if it's safely readable before risking the book.
  - **Source**: [Spellbook](https://nethackwiki.com/wiki/Spellbook) / [Damerell ID FAQ](https://www.steelypips.org/nethack/id_faq.html)
  - **Apply to**: a new mini-section under The Price Is Right, since spellbook prices aren't in the book at all
  - **Why interesting**: The book covers scroll/potion/ring/wand/amulet/armor price tables but is silent on spellbooks, whose price tells you the danger of reading them.

- **All amulets weigh 20 and cost 150** — confirms price-ID is a dead end for amulets and you should save scrolls of identify for them.
  - **Source**: [Identification](https://nethackwiki.com/wiki/Identification)
  - **Apply to**: Amulet Prices / A Practical Strategy
  - **Why interesting**: The book says amulets need other methods but doesn't make the inverse positive prescription — "amulets are your highest-priority scroll-of-identify target."

### The Engrave Test (Wands)
- **Engrave "Elbereth" with your finger as the pre-message** — doubles as Wisdom exercise and a useful safety engraving if the wand turns out to be a no-op.
  - **Source**: [Wand](https://nethackwiki.com/wiki/Wand)
  - **Apply to**: The Engrave Test (the "write a short message" step)
  - **Why interesting**: Costs nothing, hardens the player's habit of Elbereth use, and the wand-of-nothing case leaves a useful engraving behind.

- **A 0-charge wand has a 1-in-121 chance to wrest a final charge when engraved** — so even "empty" wands can sometimes still ID via engraving, but it destroys the wand.
  - **Source**: [Wresting](https://nethackwiki.com/wiki/Wresting) / [Wand](https://nethackwiki.com/wiki/Wand)
  - **Apply to**: The Engrave Test
  - **Why interesting**: Strategically meaningful — a player who knows wresting exists will be cautious about engrave-testing a wand they suspect is wishing at 0:0, since wresting a wish-charge for an ID is a tragic waste.

### The Sink Test (Rings)
- **Never sink-test in a shop's sink, and never sink-test a ring of teleportation in a populated room** — dropping a ring of teleportation in a sink teleports the sink, and teleporting a shopkeeper out of their shop makes them hostile.
  - **Source**: [Sink](https://nethackwiki.com/wiki/Sink) / [Stealing from shops](https://nethackwiki.com/wiki/Stealing_from_shops)
  - **Apply to**: The Sink Test
  - **Why interesting**: Strategically meaningful safety rail; the book mentions the sink test but not these specific hazards.

- **Bouncing-down-the-drain ambiguity** — if you're blind, or there's no object on the sink for the hunger-ring case, you just get a generic "ring bouncing down the drain" message and learn nothing.
  - **Source**: [Sink](https://nethackwiki.com/wiki/Sink)
  - **Apply to**: The Sink Test
  - **Why interesting**: A failure mode that wastes a (likely lost) ring; warning saves the test from being a coin flip.

### Use-Testing (The Careful Way)
- **The artifact-name slip test** — try to #name an unknown item as an artifact of that class; if your hand "slips," the item is the base type for that artifact (e.g., naming an amulet "The Eye of the Aethiopica" slips if and only if it's an amulet of ESP).
  - **Source**: [Naming artifacts](https://nethackwiki.com/wiki/Naming_artifacts) / [Damerell ID FAQ](https://www.steelypips.org/nethack/id_faq.html)
  - **Apply to**: Use-Testing (Amulets) and Naming What You've Learned
  - **Why interesting**: A nearly-free, completely safe formal-ID method that works on amulets, gray stones, and a handful of other classes — exactly the items that resist other ID methods.

- **Wear-test amulets only after BUC, because the dangerous ones are 90%+ generated cursed** — strangulation, restful sleep, and change all bias heavily cursed, so a confirmed-non-cursed amulet is safe to briefly wear.
  - **Source**: [Amulet of strangulation](https://nethackwiki.com/wiki/Amulet_of_strangulation)
  - **Apply to**: Use-Testing (Amulets)
  - **Why interesting**: The book says "most amulets are safe to wear briefly" but doesn't quantify why; the "BUC first" rule is what makes it safe.

- **Test-quaff $200 potions only in a locked room with no body armor or cloak and a sink nearby** — strips cursed-levitation problems, prevents armor lockout from polymorph.
  - **Source**: [Damerell ID FAQ, potions](https://www.steelypips.org/nethack/id_faq.html)
  - **Apply to**: Use-Testing (Potions)
  - **Why interesting**: A specific safe-quaff procedure for the dangerous-but-rewarding tier; the book mentions throwing at monsters but not the locked-room ritual.

### Gray Stones
- **The pickup-menu weight test** — drop any junk item onto an unidentified gray stone to force the pickup menu; the menu shows weight (10 vs 500), instantly distinguishing loadstone from everything else without picking it up.
  - **Source**: [Loadstone](https://nethackwiki.com/wiki/Loadstone)
  - **Apply to**: Gray Stones
  - **Why interesting**: Cleaner than the kick test (which can give a false negative if the player is strong, wearing kicking boots, or polymorphed) and the book doesn't mention it at all.

- **Kick-test caveats** — remove gauntlets of power and kicking boots, and don't be polymorphed into a strong form before kicking, or a real loadstone may move and fool you.
  - **Source**: [Loadstone](https://nethackwiki.com/wiki/Loadstone)
  - **Apply to**: Gray Stones (the kick test paragraph)
  - **Why interesting**: A documented false-negative path on a test the book presents as definitive.

- **Loadstones inside containers** — picking up a container with a loadstone in it gives you a pickup_burden warning; #tip the container and apply the other tests.
  - **Source**: [Loadstone](https://nethackwiki.com/wiki/Loadstone)
  - **Apply to**: Gray Stones
  - **Why interesting**: A common trap (a chest contains "a gray stone" and the player blindly empties it into their pack); strategically meaningful.

### Naming What You've Learned
- **Annotate the price in the call name itself** — `#call` the appearance with the price (e.g. "fizzy=100") so the price-tier evidence travels with the item even if you forget which shop quoted it.
  - **Source**: [Damerell ID FAQ](https://www.steelypips.org/nethack/id_faq.html) (book already gestures at this; community formalizes the convention)
  - **Apply to**: Naming What You've Learned
  - **Why interesting**: A concrete shorthand convention the book gestures at but doesn't fully prescribe.

- **Stack-size frequency heuristic** — large stacks of an unidentified potion are statistically very likely to be a common cheap potion (water, booze, fruit juice); a "lonely" appearance among many is more likely the rare item.
  - **Source**: [Damerell ID Spoiler](http://www.chiark.greenend.org.uk/~damerell/games/nhid.html)
  - **Apply to**: Naming What You've Learned (or A Practical Strategy)
  - **Why interesting**: A free informal-ID heuristic; useful for prioritizing which unknown to risk-test first.

### A Practical Strategy
- **Identify priority ranking** — when scrolls of identify are scarce, the canonical order is: spellbooks first (reading-unknown is lethal), then amulets (no price-ID possible), then resistance/utility rings in the $200 tier, then wands that resist engrave-testing.
  - **Source**: [Identification](https://nethackwiki.com/wiki/Identification) / [Damerell ID FAQ](https://www.steelypips.org/nethack/id_faq.html)
  - **Apply to**: A Practical Strategy (the "save your scrolls of identify for" paragraph)
  - **Why interesting**: The book lists targets but not the priority order; spellbooks-first is the meaningful change because reading unknown high-level books can outright kill.

---

## Cluster 3: Items

### Provisions and Dining
- **Lizard corpses must be kept in open inventory, not in a bag**: a lizard cures stoning only if you can eat it before stoning completes (2 turns after the warning), and pulling it out of a bag takes too long.
  - **Source**: [Lizard - NetHack Wiki](https://nethackwiki.com/wiki/Lizard)
  - **Apply to**: Useful Corpse Effects (or Dangerous Foods)
  - **Why interesting**: Beginners stuff everything into the BoH; this rule literally saves a life and the book currently doesn't say where to carry a lizard.
- **Lizard corpse in open inventory also blocks the new-moon cockatrice hiss instadeath**: just carrying it (no eating needed) suppresses the delayed-stoning hiss that triggers on a new moon.
  - **Source**: [Lizard - NetHack Wiki](https://nethackwiki.com/wiki/Lizard)
  - **Apply to**: Dangerous Foods / Useful Corpse Effects
  - **Why interesting**: This is the only mitigation for a real-clock-based instadeath and almost nobody knows about it.
- **Tinning kit converts poisonous and acidic corpses into safe tins**: kobolds, killer bees, etc. become food you can eat without poison-resistance prerequisites.
  - **Source**: [Tinning kit - NetHack Wiki](https://nethackwiki.com/wiki/Tinning_kit)
  - **Apply to**: What to Eat (or Other Notable Tools)
  - **Why interesting**: Turns a niche tool into a vegetarian-or-poison-vulnerable character's lifeline; book lists tinning kit but doesn't say what it does for risky food.

### Potions
- **Water prayer at a co-aligned altar converts every potion of water on the square to holy water at once**: bulk-make holy water by piling water potions on the altar before #pray.
  - **Source**: [Potion of holy water - NetHack Wiki](https://nethackwiki.com/wiki/Potion_of_holy_water)
  - **Apply to**: Key Potions (Holy Water)
  - **Why interesting**: The book says "drop uncursed water on a co-aligned altar, pray" — singular. Beginners drop one at a time, costing many prayer cooldowns. The pile trick is the actual technique.
- **Holy water self-replicates by dipping**: dip uncursed water into a holy water potion and you make more holy water indefinitely.
  - **Source**: [Potion of holy water - NetHack Wiki](https://nethackwiki.com/wiki/Potion_of_holy_water)
  - **Apply to**: Key Potions (Holy Water)
  - **Why interesting**: Mentioned by the wiki as a core production technique; turns one holy water and a stack of plain water into unlimited holy water without further prayers.
- **Throw an unknown potion at a monster to price-narrow it for free**: acid screams ("writhes in pain"/"shrieks"), paralysis/sleep/blindness all show distinctive effects on the target.
  - **Source**: [Potion of acid - NetHack Wiki](https://nethackwiki.com/wiki/Potion_of_acid)
  - **Apply to**: The Apothecary / Key Potions
  - **Why interesting**: A safe identification path for the dangerous $250/$300 group that the book doesn't currently describe.
- **Object detection finds the Castle wand of wishing without touring all four towers**: quaffing a potion of object detection on the Castle floor lights up which tower's chest contains the wand.
  - **Source**: [Potion of object detection - NetHack Wiki](https://nethackwiki.com/wiki/Potion_of_object_detection)
  - **Apply to**: Key Potions (add a stub for object detection)
  - **Why interesting**: Concrete, named application of a potion the book otherwise doesn't mention; saves real risk at the Castle.
- **Confusion + gain level/energy alchemy → enlightenment (3/10), feeding the levitation+enlightenment → gain level loop**: another rung in the alchemy ladder.
  - **Source**: [Potion of enlightenment - NetHack Wiki](https://nethackwiki.com/wiki/Potion_of_enlightenment)
  - **Apply to**: Alchemy
  - **Why interesting**: The book lists the levitation+enlightenment recipe but not where enlightenment comes from. Closing the loop turns confusion (currently described as a problem potion) into a feedstock.
- **Alchemy smock is the price-of-admission for any serious alchemy**: drops explosion chance from ~10% per dip to 1/30, and grants poison + acid resistance.
  - **Source**: [Alchemy smock - NetHack Wiki](https://nethackwiki.com/wiki/Alchemy_smock)
  - **Apply to**: Alchemy
  - **Why interesting**: The book mentions the 1/30 figure but doesn't flag that the smock also doubles as a corpse-safety cloak for low-poison-resistance characters eating killer-bee corpses to *gain* poison resistance.

### Scrolls
- **Pile every unidentified item before reading blessed scroll of identify**: blessed-with-positive-luck reads at least 2 items and has a 20% chance to identify everything in inventory.
  - **Source**: [Scroll of identify - NetHack Wiki](https://nethackwiki.com/wiki/Scroll_of_identify)
  - **Apply to**: Key Scrolls (Identify)
  - **Why interesting**: The book mentions blessed reads multiple items but not the "stage everything first" habit or the 20%-everything jackpot — a real behavior change for a beginner.
- **Cancel useless scrolls and potions to mass-produce blank scrolls and water**: zapping a wand of cancellation at a pile of junk scrolls blanks them all, refilling your magic-marker stock and your holy-water stock at once.
  - **Source**: [Wand of cancellation - NetHack Wiki](https://nethackwiki.com/wiki/Wand_of_cancellation)
  - **Apply to**: Wand of Cancellation, also tie-in to Magic Marker
  - **Why interesting**: Reframes cancellation from "bag-killer trap" to "production engine," which is the wiki's recommended use.

### Wands
- **Burn Elbereth into the floor with a wand of fire or lightning for a permanent engraving**: dust Elbereth wears off after one trample, burned Elbereth never degrades, and only the player can erase it (cold/cancellation/make-invisible).
  - **Source**: [Elbereth - NetHack Wiki](https://nethackwiki.com/wiki/Elbereth), [Engraving - NetHack Wiki](https://nethackwiki.com/wiki/Engraving)
  - **Apply to**: Key Wands (or Elbereth cross-reference)
  - **Why interesting**: This is the single most powerful safe-spot technique in the game and isn't in the book; lightning has the side risk of self-blinding.
- **Engrave Elbereth before doing the engrave-test on a no-message wand**: lets you survive the create-monster or lightning that some no-message and unknown wands turn out to be.
  - **Source**: [Wand - NetHack Wiki](https://nethackwiki.com/wiki/Wand)
  - **Apply to**: Resolving Ambiguous Engrave Results
  - **Why interesting**: Concrete safety upgrade to the procedure the book already teaches.
- **A cursed wand of digging zaps downward when zapped in any direction**: useful for emergency escape, but a hazard if you didn't know.
  - **Source**: [Wand of digging - NetHack Wiki](https://nethackwiki.com/wiki/Wand_of_digging)
  - **Apply to**: Key Wands (Digging)
  - **Why interesting**: The book sells digging as an escape but doesn't flag the cursed-zap behavior, which changes how you should test an unidentified digging wand.
- **Polypile separates stacks into singletons for best item-yield**: name stacks individually with #name so they polymorph independently rather than as one shuddering pile.
  - **Source**: [Polypiling - NetHack Wiki](https://nethackwiki.com/wiki/Polypiling)
  - **Apply to**: Polymorph as a Tool (or a new "Polypiling" subsection)
  - **Why interesting**: The book mentions "polymorph a pile of junk armor" but not the actual technique that makes it work — stacks of 5+ shudder and shrink instead of polymorphing.
- **Avoid polypiling mineral items**: most stone rings (jade, agate) and stone wands shudder away into nothing instead of polymorphing; exceptions are granite, opal, clay, coral, moonstone, black onyx rings and marble wands.
  - **Source**: [Polypiling - NetHack Wiki](https://nethackwiki.com/wiki/Polypiling)
  - **Apply to**: Polymorph as a Tool
  - **Why interesting**: Strategy-meaningful: a player polypiling for rings of slow digestion is bricking half their fodder without this rule.
- **Wand of cancellation strips dangerous monster powers without killing**: cancelling a cockatrice removes its touch-stoning; cancelling a mind flayer removes the brain-suck; cancelling a clay golem destroys it instantly.
  - **Source**: [Wand of cancellation - NetHack Wiki](https://nethackwiki.com/wiki/Wand_of_cancellation)
  - **Apply to**: Key Wands (Cancellation)
  - **Why interesting**: The book describes cancellation purely as an item tool. Its monster use cancels two of the worst instadeath threats in the game.
- **Wand of probing auto-identifies on first successful zap and reveals a target's inventory**: useful on shopkeepers, soldiers, and predefined monsters to ID their gear.
  - **Source**: [Wand of probing - NetHack Wiki](https://nethackwiki.com/wiki/Wand_of_probing)
  - **Apply to**: Wand Table / Other Notable Tools (stethoscope comparison)
  - **Why interesting**: The book lists probing as "no message" but doesn't say it reads inventory; stethoscope vs. probing is a real choice the book skips.

### Rings and Amulets
- **Charging a ring of protection past +6 is statistically a waste**: above +6 explosion is guaranteed, and the cost-per-point in scrolls and rings to reach the cap reliably exceeds the supply you'll see in any run.
  - **Source**: [Ring strategy - NetHack Wiki](https://nethackwiki.com/wiki/Ring_strategy), [Charging - NetHack Wiki](https://nethackwiki.com/wiki/Charging)
  - **Apply to**: The Ring Table (chargeable note) or Recharging
  - **Why interesting**: Strategically caps a tempting investment; the book mentions chargeable rings but doesn't give the practical ceiling.
- **The two-ring slow-digestion trick lets you toggle off ring hunger for free**: ring hunger ticks on different turns per hand; swap one ring out on its hunger tick to net zero food while keeping intrinsics.
  - **Source**: [Ring of slow digestion - NetHack Wiki](https://nethackwiki.com/wiki/Ring_of_slow_digestion)
  - **Apply to**: Rings and Amulets (The hidden cost)
  - **Why interesting**: A genuine veteran trick around the "every ring drains food" rule the book just states.
- **Test a suspected ring of conflict by isolating yourself with a leashed weak pet**: leashes break under conflict, so the leash snap-break is a free positive signal.
  - **Source**: [Ring of conflict - NetHack Wiki](https://nethackwiki.com/wiki/Ring_of_conflict)
  - **Apply to**: The Ring Table (Conflict)
  - **Why interesting**: A specific identification routine for a ring whose ID-by-wearing is otherwise dangerous to your pet.
- **Helm of opposite alignment converts your alignment as long as it's worn, enabling cross-aligned altar tricks**: holy water at the wrong altar, sacrifice corpses to the opposite god, even claim the opposite-aligned quest artifact.
  - **Source**: [Helm of opposite alignment - NetHack Wiki](https://nethackwiki.com/wiki/Helm_of_opposite_alignment)
  - **Apply to**: Helmets (or Amulets, near alignment-shifting items)
  - **Why interesting**: A whole subsystem the book skips — the helm autocurses, so the conversion is sticky, and players need to know that before testing.

### Tools
- **Magic marker → genocide → wraith corpses pipeline**: write blessed scrolls of genocide, blessed-genocide L (liches), or reverse-genocide wraiths for an XP buffet (~1.6 wraith corpses per scroll).
  - **Source**: [Wraith - NetHack Wiki](https://nethackwiki.com/wiki/Wraith), [Scroll of genocide - NetHack Wiki](https://nethackwiki.com/wiki/Scroll_of_genocide)
  - **Apply to**: Other Notable Tools (Magic marker) or Reverse Genocide
  - **Why interesting**: Concrete numbers; the book mentions reverse-genociding wraiths but not the 1.6-per-scroll yield or the "skip levels with graveyards" caveat.
- **Crystal ball is reliable at Int 16 if blessed, or Int 8+ if it's your quest artifact**: the book lists crystal-ball uses but not the Int gate, which makes most non-Wizard/Priest characters explode the ball.
  - **Source**: [Crystal ball - NetHack Wiki](https://nethackwiki.com/wiki/Crystal_ball)
  - **Apply to**: Other Notable Tools (Crystal ball)
  - **Why interesting**: A real "don't use this yet" gate. Low-Int characters lose the ball or get hallucinated.
- **Magic lamp must be blessed before rubbing**: cursed = no wish ever, uncursed = ~40% wish, blessed = 80%. Drop on an altar and pray-bless before the first rub.
  - **Source**: [Magic lamp - NetHack Wiki](https://nethackwiki.com/wiki/Magic_lamp)
  - **Apply to**: Light Sources (Magic lamp)
  - **Why interesting**: The book mentions "80% if blessed" but doesn't explicitly tell beginners to bless first or list the cursed=zero outcome that's the most common YASD.
- **Apply grease to your bag of holding to make it waterproof**: spares the contents from drowning damage if you fall into Medusa's moat or the Plane of Water without an oilskin sack.
  - **Source**: [Bag of holding - NetHack Wiki](https://nethackwiki.com/wiki/Bag_of_holding)
  - **Apply to**: Containers
  - **Why interesting**: The book warns about the explosion list but not about water destroying scrolls/potions inside. Grease is the cheap fix.
- **Nested blessed bags of holding don't explode and stack their weight reduction**: a blessed bag inside a blessed bag puts inner items at ~1/16 weight (though both bags count for the inner-bag-into-outer-bag explosion rule and need separate handling).
  - **Source**: [Bag of holding - NetHack Wiki](https://nethackwiki.com/wiki/Bag_of_holding)
  - **Apply to**: Containers
  - **Why interesting**: Nuance the book misses — bag-into-bag is forbidden by insertion, but if both already exist nested you keep the stacking benefit.

### Armor and Curses
- **Wish format matters: "blessed greased fixed +2 gray dragon scale mail"**: "greased" and "fixed" (or "erodeproof") are the safety options every veteran adds to every wish, and omitting "scale" gives you a scroll of mail instead of armor.
  - **Source**: [Wish - NetHack Wiki](https://nethackwiki.com/wiki/Wish)
  - **Apply to**: Dragon Scale Mail / Wand of Wishing
  - **Why interesting**: The single most common newbie-wish mistake in the game; the book describes the wish system but not the standard incantation.
- **Apply a can of grease to armor before any encounter with grabby or stealing monsters**: greased armor deflects nymph theft and the Riders' grab attacks; greased gloves give slippery-finger protection against weapon theft.
  - **Source**: [Can of grease - NetHack Wiki](https://nethackwiki.com/wiki/Can_of_grease), [Gloves - NetHack Wiki](https://nethackwiki.com/wiki/Gloves)
  - **Apply to**: Erosion and Proofing (extend the existing grease note)
  - **Why interesting**: The book mentions grease only for erosion/grab; it doesn't mention the nymph-theft and Rider-grab applications that change how you walk into the Mines or the Astral Plane.
- **Cursed scroll of destroy armor read while confused erodeproofs a random worn piece**: the book already covers this, but the same effect is available from confused uncursed/blessed enchant armor — and the destroy-armor route is preferable because it doesn't burn a precious enchant scroll.
  - **Source**: [Erosion - NetHack Wiki](https://nethackwiki.com/wiki/Erosion), [Scroll of destroy armor (Fandom)](https://nethack.fandom.com/wiki/Scroll_of_destroy_armor)
  - **Apply to**: Confused Reading / Erosion and Proofing
  - **Why interesting**: Re-prioritization: the book treats confused-enchant as the canonical erodeproofing path; community treats confused destroy armor as the cheap one.
- **Bag from a bones pile is probably cursed but full of loot — uncurse from outside before opening**: drop on the floor, zap a wand of cancellation at it (cancellation just uncurses bags from outside), or holy-water-dip it.
  - **Source**: [Bones - NetHack Wiki](https://nethackwiki.com/wiki/Bones), [Wand of cancellation - NetHack Wiki](https://nethackwiki.com/wiki/Wand_of_cancellation)
  - **Apply to**: How Items Get Cursed (Bones inheritance) or Containers
  - **Why interesting**: Cursed BoH doubles weights and could brick you if you scoop it up first; the cancel-from-outside trick is in the book for cursed bags generally but not tied to the bones-bag case.
- **Altar-test items by dropping them in a stack, not one at a time**: the altar flashes per item and the flash is colored by BUC, so a pile resolves the whole inventory in one drop-and-look.
  - **Source**: [Curse-testing - NetHack Wiki](https://nethackwiki.com/wiki/Curse-testing)
  - **Apply to**: Detecting Curses (Altar test)
  - **Why interesting**: The book describes altar-test for "an item"; bulk-testing is faster and is what veterans do at their first altar.
- **Pet refuses-to-step is a free BUC test for piles, but only without food in the stack and without using the magic whistle**: corridor-and-doorway forcing makes pet-testing routine.
  - **Source**: [Curse-testing - NetHack Wiki](https://nethackwiki.com/wiki/Curse-testing)
  - **Apply to**: Detecting Curses (Pet test)
  - **Why interesting**: The "no food in the stack" and "no whistle" caveats are exactly what break the pet test for unwary players; without them the test silently lies.

---

## Cluster 4: Combat & Dangers & Divine Relations

### Combat (To-Hit, Damage, AC, Fighting Smart)
- **AC diminishing returns and the -25 cliff**: the marginal value of each extra AC point starts dropping fast around AC -25; community consensus is that -20 is the practical baseline for an ascension kit, and chasing further is mostly cosmetic.
  - **Source**: [Armor class](https://nethackwiki.com/wiki/Armor_class)
  - **Apply to**: AC and Defense
  - **Why interesting**: the book's table goes to "-20 to -10" but doesn't tell the reader where to stop — and that "where to stop" is a real strategic decision.

- **Two-weapon-skill cap follows your weapon skill**: the two-weapon to-hit/damage math takes the *lesser* of your two-weapon rank and your weapon skill, so a Rogue who can only reach Skilled in long sword gains nothing from Expert two-weapon with long swords; lead with a dagger instead.
  - **Source**: [Twoweapon](https://nethackwiki.com/wiki/Twoweapon)
  - **Apply to**: Two-Weapon Combat
  - **Why interesting**: changes the advice from "Rogue/Samurai can reach Expert" to "and here's how to actually use it" — a concrete decision a beginner gets wrong.

- **Cloak of displacement is the underrated defensive layer**: monsters lose pinpoint targeting and miss disproportionately often; it complements low AC rather than competing with it, and unlike invisibility doesn't get sniffed out as fast.
  - **Source**: [Cloak of displacement](https://nethackwiki.com/wiki/Cloak_of_displacement)
  - **Apply to**: AC and Defense / Fighting Smart
  - **Why interesting**: the book mentions cloaks for MC but never names displacement as a survival tier; a beginner who finds one shouldn't disenchant or trade it.

- **Wand of digging downward as the universal "I'm leaving" button**: zap straight down, fall through the hole, lose the pursuit. This is the canonical "I'm in over my head" escape, since the direction of escape (down) is also the direction you want to travel.
  - **Source**: [Wand of digging](https://nethackwiki.com/wiki/Wand_of_digging), [Wand strategy](https://nethackwiki.com/wiki/Wand_strategy)
  - **Apply to**: Fighting Smart (Know when to run)
  - **Why interesting**: the book says "use a scroll/wand of teleportation, or just run." The wand of digging is the more reliable escape because it works even on no-teleport levels and the destination is downstairs anyway.

- **Scroll of scare monster as a stash-protector**: dropped on the floor, it functions like a portable, durable Elbereth that works while you're *not* standing on it — the modern (3.6+) way to protect a stash, since Elbereth no longer protects empty squares.
  - **Source**: [Scroll of scare monster](https://nethackwiki.com/wiki/Scroll_of_scare_monster), [NetHack Elbereth FAQ](https://www.steelypips.org/nethack/elbereth_faq.html)
  - **Apply to**: Fighting Smart (Elbereth)
  - **Why interesting**: corrects a common holdover from pre-3.6 lore; the book talks about Elbereth defenses but never tells the reader how to protect an unattended stash.

- **Burned Elbereth never degrades**: an Elbereth engraving made by zapping a wand of fire is permanent — it can only be erased by you, with cancellation/cold. The classic "stash camp" floor.
  - **Source**: [Wand of fire](https://nethackwiki.com/wiki/Wand_of_fire), [Engraving](https://nethackwiki.com/wiki/Engraving)
  - **Apply to**: Fighting Smart (Elbereth)
  - **Why interesting**: gives the burn-engrave tactic a concrete strategic payoff (a permanent safe-room floor) rather than just "use a wand."

### Things That Will Kill You
- **Floating eye + newt = canonical YASD**: melee a floating eye, get paralyzed, get nibbled to death by anything passing — explicitly cited as the second-most-common stupid death after cockatrices.
  - **Source**: [Yet Another Stupid Death](https://nethackwiki.com/wiki/Yet_Another_Stupid_Death), [Floating eye](https://nethackwiki.com/wiki/Floating_eye)
  - **Apply to**: Common Combat Deaths (new note) or Deadly Mistakes
  - **Why interesting**: floating eyes do not appear in the current Common Combat Deaths / Deadly Mistakes lists at all despite being a top-tier preventable killer; a beginner reading the book learns nothing about them.

- **Minotaurs hit hardest in the game outside Riders**: three-attack package averages ~38 damage per turn with the highest melee damage ceiling short of the Riders themselves. Wand of sleep + dig down, or wield-and-smash a potion of paralysis with free action, are the standard answers.
  - **Source**: [Minotaur](https://nethackwiki.com/wiki/Minotaur)
  - **Apply to**: Common Combat Deaths (or new note in More Ways to Die)
  - **Why interesting**: the book covers dragons, mind flayers, trolls, etc. but doesn't name minotaurs even though they're the dominant maze threat below the Castle.

- **Major demons gate in more demons**: every major demon has a 1/13 chance per landed hit to summon another major demon (foocubi and balrogs excepted). A single Asmodeus encounter handled poorly becomes an arena of nasties.
  - **Source**: [Major demon](https://nethackwiki.com/wiki/Major_demon), [Demon summoning](https://nethackwiki.com/wiki/Demon_summoning)
  - **Apply to**: Common Combat Deaths (Gehennom note) or new subsection
  - **Why interesting**: explains why a single bad Gehennom fight cascades — the book covers water demons and Vlad but never names the gating mechanic.

### A note on dragons / mimics / nymphs / puddings / trolls / wraiths
- **Pudding farming was nerfed and doesn't work anymore**: black/brown pudding splits no longer drop corpses, and cloned puddings give significantly less XP. The "infinite altar food" reputation is from 3.4.x, not current play.
  - **Source**: [Pudding farming](https://nethackwiki.com/wiki/Pudding_farming)
  - **Apply to**: A note on puddings
  - **Why interesting**: the puddings section pitches splitting as a positive ("every divided pudding is one more glob to eat") — true for glob nutrition, but a beginner who reads the old wiki/community lore will expect to farm for sacrifice corpses and XP. Brief correction is a strategic decision-saver.

- **Adult dragon corpses have a 1/3 chance to drop scales**: scales convert to scale mail with a scroll of enchant armor, so killing a dragon is the standard non-wish path to dragon scale mail.
  - **Source**: [Dragon scales](https://nethackwiki.com/wiki/Dragon_scales)
  - **Apply to**: A note on dragons
  - **Why interesting**: the book's dragon section names every color's power but never says where scales come from or how to upgrade them — a player who kills their first dragon and sees scales drop may not know what to do with them.

- **Lurkers above and trappers are silent and don't need search**: they move at speed 3 and weapons hit fine while engulfed; a ring of slow digestion or a wand of digging from inside is the canonical answer. The book covers the wand-of-digging escape but the silence-and-warning-only detection chain is worth surfacing for a beginner.
  - **Source**: [Trapper or lurker above](https://nethackwiki.com/wiki/Trapper_or_lurker_above)
  - **Apply to**: Engulfment
  - **Why interesting**: clarifies that telepathy *or* warning reveals them in time; the engulfment section already mentions warning, but the slow-3 detail makes engagement much less scary than the prose suggests.

### Petrification (Stoning)
- **The cockatrice corpse "rubber chicken" routine**: wield gloved, hit anything without stoning resistance, watch it turn to stone. Works on demon lords and princes. Drop and pick up safely between fights. The two failure modes: falling into a pit/hole (instant stoning even with gloves) or losing the gloves.
  - **Source**: [Cockatrice](https://nethackwiki.com/wiki/Cockatrice), [Stoning](https://nethackwiki.com/wiki/Stoning)
  - **Apply to**: Petrification (other side of the coin)
  - **Why interesting**: the book mentions wielded cockatrice corpses as a weapon in one line; the *named* community routine ("rubber chicken") and its failure modes — pits, holes, trapdoors, losing gloves — are real beginner-killers.

- **Thrown cockatrice eggs petrify**: cockatrice eggs work as petrification grenades at range, including for monsters who can throw them at you.
  - **Source**: [Cockatrice](https://nethackwiki.com/wiki/Cockatrice)
  - **Apply to**: Petrification
  - **Why interesting**: the book doesn't mention the egg path either as offense or as incoming threat; a thrown cockatrice egg from a monster killing you with no melee touch is a real instadeath.

### The Touch of Death
- **Pestilence, not Death, is the rider feared most**: Pestilence's incurable sickness countdown is what kills ascending heroes; Death's HP loss is actually survivable for the well-built. The standard Astral move is to telepathically scout for Pestilence and approach that altar last.
  - **Source**: [Pestilence](https://nethackwiki.com/wiki/Pestilence), [Astral Plane](https://nethackwiki.com/wiki/Astral_Plane), [Riders](https://nethackwiki.com/wiki/Riders)
  - **Apply to**: The Touch of Death (or new note on Riders)
  - **Why interesting**: the book treats Death's touch as the headline rider threat; community consensus is the opposite and the targeting-order advice is concrete.

- **Wand of death heals Death**: zap Death with a wand of death or finger of death and you make the problem worse — Death absorbs death rays and gains max HP. Use magic missile instead; all three Riders are vulnerable to magic missile.
  - **Source**: [Death (monster)](https://nethackwiki.com/wiki/Death_(monster)), [Riders](https://nethackwiki.com/wiki/Riders)
  - **Apply to**: The Touch of Death
  - **Why interesting**: a beginner reading the book would reasonably try wand-of-death on Death; the trap is famous and the safer route (magic missile) is concrete.

### Starvation
- **Famine's hunger drain has no resistance**: 40–80 nutrition per hit, no extrinsic blocks it. Standard advice: enter the Astral Plane Satiated. The "Famine pasted me to the ceiling" anecdote tradition starts here.
  - **Source**: [Famine](https://nethackwiki.com/wiki/Famine)
  - **Apply to**: Starvation (or note in The Touch of Death)
  - **Why interesting**: book covers starvation generally but doesn't name the one monster who weaponizes it as an instadeath. Easy fix.

### Brainlessness
- **Stash extrinsic telepathy before fighting a mind flayer**: the mind blast only fires if you currently have telepathy. Take off the amulet/helm of telepathy, kill the mind flayer, put it back on.
  - **Source**: [Mind flayer](https://nethackwiki.com/wiki/Mind_flayer), [Mind blast](https://nethackwiki.com/wiki/Mind_blast)
  - **Apply to**: Brainlessness
  - **Why interesting**: a counterintuitive trick that the book doesn't surface — a beginner who's just put on their first amulet of ESP doesn't realize that mind flayers can now hit them from across the level.

### Engulfment
- **Knock spell / wand of opening releases you from non-hostile engulfers without killing**: useful if your pet purple worm or a conflicted engulfer has swallowed you; the wand of digging would do too much damage to a tame engulfer.
  - **Source**: [Wand of striking](https://nethackwiki.com/wiki/Wand_of_striking), [Spellbook of knock](https://nethackwiki.com/wiki/Spellbook_of_knock)
  - **Apply to**: Engulfment
  - **Why interesting**: the book mentions knock and wand of opening as engulfer-escape tools but doesn't explain the niche (pet swallows you / conflict) where they beat wand of digging.

### Seduction
- **Foocubi can be the cheapest curse remover in the dungeon**: the armor-removal step works on cursed items too, so a high-Cha hero with a cursed cloak can engineer a curse cleanup as part of an otherwise net-positive seduction.
  - **Source**: [Foocubus](https://nethackwiki.com/wiki/Incubus)
  - **Apply to**: Seduction
  - **Why interesting**: the book already mentions this in passing ("strips cursed worn pieces too") but the practical setup — engineer the encounter when you have a cursed body armor — could be a one-liner.

### Disintegration
- **Wide-angle disintegration is the angry-god second strike**: when an angry god's lightning is blocked by reflection or shock resistance, the next zap is a wide-angle disintegration beam. Reflection doesn't block it; only disintegration resistance does.
  - **Source**: [Wide-angle disintegration beam](https://nethack.fandom.com/wiki/Wide-angle_disintegration_beam), [Anger](https://nethackwiki.com/wiki/Anger)
  - **Apply to**: Disintegration / Prayer
  - **Why interesting**: connects two threats the book treats separately. A player who reflects a god's first bolt may think they survived; the follow-up is the actual killer.

### Genocide
- **Confused-cursed wraith scroll**: the wraith-XP banquet trick the book describes (reverse-genocide wraiths with a cursed scroll) is one of the most popular community recipes for fast XP late game. Worth flagging that this is the *intended* use of the cursed-scroll-of-genocide path, not a hack.
  - **Source**: [Wraith](https://nethackwiki.com/wiki/Wraith), [Scroll of genocide](https://nethackwiki.com/wiki/Scroll_of_genocide)
  - **Apply to**: A note on wraiths
  - **Why interesting**: the book already describes the trick. The community framing — "wraith binge" is a *standard* part of the Gehennom plan — could anchor the existing advice.

### Divine Relations / Prayer
- **Prayer-timeout gambling**: when in genuine emergency (HP critical, starving), the timeout is forgiving if it's "close enough" — the game permits an early prayer rather than smiting you, on the order of within ~50 turns of expiry. Don't rely on it casually, but don't despair if you've prayed recently and you're dying.
  - **Source**: [Prayer](https://nethackwiki.com/wiki/Prayer), [Praying spoiler](https://www.steelypips.org/nethack/pray.html)
  - **Apply to**: Prayer
  - **Why interesting**: the book mentions "some forgiveness if your timeout is close to expiring" — but the *amount* of forgiveness and the genuine-emergency framing is decision-relevant for a beginner who thinks "I just prayed, I can't pray again, I die."

- **Stethoscope reads your alignment record**: applying a stethoscope to yourself reports your alignment record (also: wand of probing, enlightenment). Use this before donating, before praying near 20, to avoid surprise crownings.
  - **Source**: [Alignment record](https://nethackwiki.com/wiki/Alignment_record)
  - **Apply to**: Prayer / Crowning
  - **Why interesting**: the book's crowning advice ("watch the alignment record") gives no tool to actually read it. A one-liner here saves the reader from reading the source.

### Sacrifice
- **Artifact-gift odds: 1 / (10 + 2·existing_artifacts·gifts_received)**: the gift probability per qualified sacrifice. Concretely: first gift is roughly 1 in 10; second drops to 1 in ~14, then 1 in 22. Don't be surprised when the second gift takes ten times the work.
  - **Source**: [Sacrifice](https://nethackwiki.com/wiki/Sacrifice), [Artifact](https://nethackwiki.com/wiki/Artifact)
  - **Apply to**: Sacrifice
  - **Why interesting**: the book mentions "subsequent gifts require substantially more" but the formula is striking and explains why most players get exactly one gift artifact.

- **First-gift role priority**: your first sacrifice gift bypasses the per-artifact minimum-sacrifice value and is biased toward your role's signature artifact (Magicbane for Wizards, Sting/Orcrist for Valkyrie alignment, etc.). Don't wait — sacrifice early to lock in your role's gift before another co-aligned artifact takes the slot.
  - **Source**: [Sacrifice](https://nethackwiki.com/wiki/Sacrifice), [Artifact](https://nethackwiki.com/wiki/Artifact)
  - **Apply to**: Sacrifice
  - **Why interesting**: explains why beginners are told "sacrifice as soon as you find an altar" — it's not random hunting, it's role bias on the first gift.

- **Same-race blood always makes the altar chaotic**: not co-aligned with you, *chaotic* specifically. On a chaotic altar same-race blood summons a demon. The book covers this but the "Chaotic *no matter your alignment*" detail is the punchline.
  - **Source**: [Altar](https://nethackwiki.com/wiki/Altar), [Sacrifice](https://nethackwiki.com/wiki/Sacrifice)
  - **Apply to**: Sacrifice / Altars and Alignment
  - **Why interesting**: a Lawful or Neutral character cannot use same-race sacrifice as a desperate altar-conversion shortcut; the only beneficiary is a Chaotic character who happens to find a co-aligned same-race corpse, and they still get a demon.

### Donating to Priests (Protection racket)
- **2–4 protection per donation up to 9 points, then 1-in-N per donation**: the first donation gives 2–4 random points; each subsequent gives 1 point flat up to 9; past 9, the chance drops to 1-in-(current points) per donation. Hitting 20 from scratch is realistically 6–8 donations.
  - **Source**: [Protection racket](https://nethackwiki.com/wiki/Protection_racket), [Intrinsic protection](https://nethackwiki.com/wiki/Intrinsic_protection)
  - **Apply to**: Donating to Priests
  - **Why interesting**: the book says "each successful donation pushes the bonus up by 1 (rarely more)" but the *first donation* is the special one (2–4 points), and the diminishing returns past 9 explain why protection-racket builds aim for the early visit.

- **The protection racket: rush to Minetown temple at low XL with maximum gold**: donation cost scales with XL, so 4000 gold at XL 1 buys what 30000+ gold buys at XL 14. Healers are the canonical class (gold start, healing spell to keep pet alive while the pet does the fighting).
  - **Source**: [Protection racket](https://nethackwiki.com/wiki/Protection_racket)
  - **Apply to**: Donating to Priests (or new metastrategy note)
  - **Why interesting**: a named, real strategic plan that the book hints at ("Donate early, donate often") but doesn't anchor with the XL-cost math.

### Altars and Alignment
- **Altar conversion can send hostile minions even when it succeeds**: a successful cross-aligned conversion has a chance to summon two hostile minions from the displaced god. Have an exit plan ready before sacrificing on an altar you're trying to flip.
  - **Source**: [Altar](https://nethackwiki.com/wiki/Altar), [Convert](https://nethackwiki.com/wiki/Convert)
  - **Apply to**: Altars and Alignment
  - **Why interesting**: book says "Worth the risk" but doesn't warn about the post-success retaliation; this can drop a low-HP hero who thought the fight was over.

- **Negative-alignment failure converts *you*, not the altar**: if you attempt to convert a cross-aligned altar while your alignment record is negative, the altar wins — you become a permanent worshipper of the altar's god. Mind your alignment record before risking the dip.
  - **Source**: [Altar](https://nethackwiki.com/wiki/Altar)
  - **Apply to**: Altars and Alignment
  - **Why interesting**: book covers altar conversion as a risk tradeoff but the specific "you become *converted* to their alignment" outcome is the disaster scenario.

### Crowning
- **Crowning trigger: alignment record ≥ 20 AND Luck ≥ 10**: keep alignment record below 20 or Luck below 10 to avoid surprise crownings if you don't want the prayer timeout penalty. A stethoscope read on yourself shows the alignment record.
  - **Source**: [Crowning](https://nethackwiki.com/wiki/Crowning)
  - **Apply to**: Crowning
  - **Why interesting**: the book says "If your alignment record is very high" but doesn't name the threshold or the Luck requirement, both of which the player can directly manage.

- **Lawful crowning consumes your wielded long sword**: a lawful character wielding a non-artifact long sword at crowning has it transformed *in place* into Excalibur — so a +7 enchanted long sword becomes a +7 Excalibur. Wielding a junk long sword at the moment of crowning is a waste of the upgrade.
  - **Source**: [Crowning](https://nethackwiki.com/wiki/Crowning), [Excalibur](https://nethackwiki.com/wiki/Excalibur)
  - **Apply to**: Crowning
  - **Why interesting**: actionable — players who know crowning is imminent can pre-enchant a long sword to maximize the gift.

- **Crowning also unrestricts your sword slot and teaches your role's special spell**: long sword for Lawful/Neutral, broadsword for Chaotic, plus permanent knowledge of your role's special spell — useful even when you don't get a usable artifact.
  - **Source**: [Crowning](https://nethackwiki.com/wiki/Crowning)
  - **Apply to**: Crowning
  - **Why interesting**: the book's crowning section lists fire/cold/etc. resistances but misses the skill unrestriction and role-spell, both of which are concretely useful for some role-alignment combos.

---

## Cluster 5: Mastery & Endgame

### Spellcasting / Mana
- **Train Attack school by force-bolting boulders into stone piles for thrown ammo**: Wizards can cast force bolt at boulders, pick up the resulting stones, and quiver them as ranged ammunition that kills weak monsters before they close, saving Pw for harder fights.
  - **Source**: [Spellbook of force bolt — NetHackWiki](https://nethackwiki.com/wiki/Spellbook_of_force_bolt)
  - **Apply to**: Key Spells (or Mana Management)
  - **Why interesting**: Concrete combo (force bolt → stones → quiver) that turns a school-grinding spell into a renewable ranged attack — exactly the "mana into resources" trick the book hints at but doesn't show.
- **Practice a school with its level-1 spell until you can reliably cast the level-5/7 spell you want**: Grind light to expert before relying on magic mapping/identify; grind force bolt for finger of death; etc.
  - **Source**: [Skill — NetHackWiki](https://nethackwiki.com/wiki/Skill)
  - **Apply to**: Training a Skill (Spellcasting cross-link)
  - **Why interesting**: The book lists L1 grinds but doesn't say "use them ahead of time so the big spell actually works." This is a decision-changing prep tip.
- **Carry a duplicate spellbook for spells you'll cast in Gehennom**: A spellbook fades after 4 successful reads, but you can re-read it just before the 1000-turn window to refresh 20,000 turns — running a single book through endgame is risky.
  - **Source**: [Spellbook — NetHackWiki](https://nethackwiki.com/wiki/Spellbook)
  - **Apply to**: Learning Spells / Mana Management
  - **Why interesting**: Concrete inventory advice that prevents the "my finger of death book just turned to blank paper at Dlvl 49" disaster.
- **Haste self can replace speed boots entirely for casters with high Pw regen**: At Skilled escape, haste lasts ~160 turns; with Eye of the Aethiopica's energy regen a Wizard or Monk can maintain it indefinitely, freeing the boot slot for water walking or jumping.
  - **Source**: [Spellbook of haste self — NetHackWiki](https://nethackwiki.com/wiki/Spellbook_of_haste_self)
  - **Apply to**: Key Spells / Ascension Kit
  - **Why interesting**: A real alternative to the universally-recommended speed boots that changes the slot-allocation puzzle for casters.

### Luck / Fortune
- **Sokoban guilt persists even if you don't pick up the prize**: The luck penalty applies the moment you commit the cheating act, regardless of whether you ever take the bag/amulet. (5.0 still applies on-the-spot per the audit.) So there is no "just leave before grabbing the prize to dodge the penalty" loophole.
  - **Source**: [Sokoban — NetHackWiki](https://nethackwiki.com/wiki/Sokoban)
  - **Apply to**: Gaining and Losing Luck (or Sokoban subsection)
  - **Why interesting**: A specific misconception worth correcting — beginners sometimes plan a "cheat and bail" route that doesn't actually save them luck.
- **High Luck can crown you prematurely and lengthen prayer timeout**: At ≥10 Luck plus ≥20 alignment record, prayer can crown you instead of granting your real request, which doubles future prayer timeouts. To pray safely while ascension-ready, drop the luckstone (or bag it) and check your alignment via stethoscope/probing.
  - **Source**: [Crowning — NetHackWiki](https://nethackwiki.com/wiki/Crowning)
  - **Apply to**: Why Luck Matters
  - **Why interesting**: Inverted-incentive case that catches careful players — the Luck you cultivated bites your prayer timeout.

### Skills / Training
- **Dagger Expert before any spell school is the conventional Wizard start**: Spend the first 6 slots on dagger to Expert (reached around XL 7), then start enhancing schools one at a time. Daggers are throwable, multishot, and let force bolt rest until you actually need it.
  - **Source**: [Wizard — NetHackWiki](https://nethackwiki.com/wiki/Wizard)
  - **Apply to**: Spending Slots Wisely / Wizard role
  - **Why interesting**: A specific opening sequence that contradicts the "Wizard = caster" instinct. The book has the cap table but not the standard order.

### Wishes / Artifacts
- **Canonical wish phrase: "blessed greased fixed +3 gray dragon scale mail"**: "Fixed" (or "erodeproof") locks erosion, "greased" stops monsters from corroding/cursing it, "+3" is the safe enchantment ceiling on the first wish. Spelling "gray dragon mail" without "scale" gives you a scroll of mail instead.
  - **Source**: [Wish — NetHackWiki](https://nethackwiki.com/wiki/Wish), [Dragon scale mail — NetHackWiki](https://nethackwiki.com/wiki/Dragon_scale_mail)
  - **Apply to**: Wish Syntax
  - **Why interesting**: A concrete wish string that's saved many ascensions — and the "scroll of mail" trap is the most famous wish-typo in the game.
- **Recharge the Castle wand of wishing once, then wrest for a 5-7 wish total**: Use the wand to 0:0, blessed-charge for +3 more, drain those, then keep zapping at 1/121 wrest odds until it crumbles. Don't recharge a wand that still has charges — overcharging risks explosion.
  - **Source**: [Wand of wishing — NetHackWiki](https://nethackwiki.com/wiki/Wand_of_wishing), [Wresting — NetHackWiki](https://nethackwiki.com/wiki/Wresting)
  - **Apply to**: Sources of Wishes / The Castle
  - **Why interesting**: A specific, repeatable wish-extraction protocol — the book says "two wishes reliably" but the community routinely gets 5-7.
- **Postpone wishes until you actually need them**: You may find the item naturally, or solve the problem a different way, and few wishes have more impact than a wished cursed potion of gain level on the climb out of the Sanctum.
  - **Source**: [Speed ascension — NetHackWiki](https://nethackwiki.com/wiki/Speed_ascension)
  - **Apply to**: What to Wish For
  - **Why interesting**: Reframes wishing as an opportunity cost rather than a checklist, and introduces the "cursed gain level for level skip" idea covered below.
- **Cursed potion of gain level skips a Gehennom level instantly when carrying the Amulet**: One of the most powerful single wish targets after the basics — it bypasses the Mysterious Force on that climb. Pair with the Amulet pickup wish for max efficiency.
  - **Source**: [Potion of gain level — NetHackWiki](https://nethackwiki.com/wiki/Potion_of_gain_level), [Ascension run — NetHackWiki](https://nethackwiki.com/wiki/Ascension_run)
  - **Apply to**: What to Wish For / The Ascension Run
  - **Why interesting**: A real tactical wish that the book's priority list omits — directly counters the Mysterious Force, which is the book's identified primary obstacle.
- **Magicbane's curse protection is 19/20 against rndcurse, but only when wielded as the primary weapon**: A two-weaponing Wizard with Magicbane in the off-hand loses the protection. Either keep Magicbane primary or accept that the protection lapses while two-weaponing.
  - **Source**: [Magicbane — NetHackWiki](https://nethackwiki.com/wiki/Magicbane)
  - **Apply to**: Artifacts (Magicbane entry)
  - **Why interesting**: Strategic decision point — the book says Magicbane curse protection applies "while wielded" but doesn't mention the primary-vs-secondary distinction that breaks two-weapon builds.

### The Castle
- **Quaff a blessed potion of object detection before crossing the drawbridge to find the wand chest directly**: One potion reveals which of the four corner towers holds the wand of wishing — walk to it, skip the other three searches, and also see the storeroom loot (sometimes magical armor or an artifact weapon, which can change what you wish for).
  - **Source**: [Potion of object detection — NetHackWiki](https://nethackwiki.com/wiki/Potion_of_object_detection)
  - **Apply to**: The Castle
  - **Why interesting**: A specific item-saving tactic that turns a 4-search slog into a one-step move. The book mentions "search them all"; this is the upgrade.
- **Stand a knight's-move away from the drawbridge while trying the passtune**: Standing adjacent is hazardous — the bridge can open, close, or be destroyed under you. A knight's-move keeps you safe but in range.
  - **Source**: [Passtune — NetHackWiki](https://nethackwiki.com/wiki/Passtune)
  - **Apply to**: The Castle (drawbridge)
  - **Why interesting**: The Mastermind explanation in the book doesn't mention positioning — beginners die crushed in the moat.
- **"H" is accepted as a passtune note**: From German musical notation (H = B). Useful when the game prompts for a note and you forget what's valid.
  - **Source**: [Passtune — NetHackWiki](https://nethackwiki.com/wiki/Passtune)
  - **Apply to**: The Castle (drawbridge)
  - **Why interesting**: Small flavor/UI note that confuses players who tried "H" once and got rejected.

### Gehennom
- **The Wizard's Tower portal from the Eye of the Aethiopica drops you in Vlad's Tower, skipping several Gehennom levels on the descent**: For Wizards specifically, this is a major routing shortcut. The portal is one-way and bypasses much of the maze grind.
  - **Source**: [Vlad's Tower — NetHackWiki](https://nethackwiki.com/wiki/Vlad's_Tower)
  - **Apply to**: Vlad's Tower / The Eye of the Aethiopica artifact entry
  - **Why interesting**: Concrete role-specific routing that the artifact's #invoke description hints at but doesn't put in strategic context.
- **Blessed scrolls of genocide on demon-prince summon classes don't work — but genocide of arch-liches via class L is the canonical Gehennom prep**: A blessed scroll of genocide on 'L' wipes lich/demilich/master lich/arch-lich in one read, removing among the worst Gehennom threats. The book mentions this; community sources emphasize it's the single most impactful scroll use of the late game.
  - **Source**: [Arch-lich — NetHackWiki](https://nethackwiki.com/wiki/Arch-lich), [Genocide — NetHackWiki](https://nethackwiki.com/wiki/Genocide)
  - **Apply to**: Gehennom Survival Tips
  - **Why interesting**: Already in the book but worth reinforcing as the canonical priority — every Gehennom guide on the wiki opens with this.
- **Use stinking cloud to clear the Castle throne room and the Wizard's Tower from a safe corridor**: A blessed scroll generates a 4×4 cloud; poison-resistant or unbreathing players sit in it while monsters who can't move out of it die. Monsters killed by the cloud count as your kills (XP and alignment).
  - **Source**: [Scroll of stinking cloud — NetHackWiki](https://nethackwiki.com/wiki/Scroll_of_stinking_cloud)
  - **Apply to**: The Castle / Wizard's Tower
  - **Why interesting**: A specific room-clearing technique the book doesn't mention. Particularly impactful in the Castle throne room where Lich/Vampire density is high.

### The Ascension Kit
- **Carry at least five holy water bottles in the kit**: The Wizard, liches, and curse-items monsters will repeatedly curse worn items in Gehennom; holy water is the only convenient route to re-bless a bag of holding or armor. Five is the conventional minimum.
  - **Source**: [Ascension kit — NetHackWiki](https://nethackwiki.com/wiki/Ascension_kit)
  - **Apply to**: The Ascension Kit
  - **Why interesting**: A specific count that's a real survival difference; the book's kit table doesn't include holy water at all.
- **Blessed potions of full healing as emergency reset**: They restore HP in big chunks and cure illness, blindness, and hallucination in one quaff — a one-action panic button for Riders, Pestilence touches, and accidental fountain quaffs.
  - **Source**: [Ascension kit — NetHackWiki](https://nethackwiki.com/wiki/Ascension_kit)
  - **Apply to**: The Ascension Kit / The Astral Plane
  - **Why interesting**: Specific item with multiple end-game uses; the book mentions wand of digging and scroll of teleportation as escape consumables but skips full healing.
- **Carry a cockatrice corpse to the Astral Plane**: Hit Riders with a wielded cockatrice corpse to stone them out of the equation; you must wear gloves or be stoning-resistant. A go-to speed-ascension trick.
  - **Source**: [Speed ascension — NetHackWiki](https://nethackwiki.com/wiki/Speed_ascension)
  - **Apply to**: The Ascension Kit / The Astral Plane
  - **Why interesting**: A specific item the runners-up section says winners brought — the book never names cockatrice corpse as ascension cargo.

### The Ascension Run
- **The Amulet drains extra Pw from spellcasters — drop it before casting big spells, pick it up after**: Carrying the Amulet costs additional mana per cast. Drop it on the floor to cast finger of death or magic mapping, then pick it back up. The few turns spent dropping/picking up are cheaper than the Pw drain.
  - **Source**: [Amulet of Yendor — NetHackWiki](https://nethackwiki.com/wiki/Amulet_of_Yendor)
  - **Apply to**: The Ascension Run (or the Amulet of Yendor entry)
  - **Why interesting**: Concrete tactical move that experienced casters do reflexively — beginners don't know about the drain at all.
- **Convert to chaotic after grabbing the Amulet to minimize the Mysterious Force**: Chaotics max at -1 levels per yank vs Neutrals at -2 and Lawfuls at -3. A helm of opposite alignment swap after the pickup makes the climb cheaper on average, at the cost of being a temporary chaotic on Astral.
  - **Source**: [Mysterious force — NetHackWiki](https://nethackwiki.com/wiki/Mysterious_force)
  - **Apply to**: The Ascension Run
  - **Why interesting**: Strategic alignment-juggling that some speed ascensions use. The book describes the Force but doesn't suggest converting.
- **Helm of opposite alignment on Astral guarantees ascension at the second altar tried, no matter what**: Wear it, walk to any altar, sacrifice — 2/3 chance to ascend immediately, and if not, swap helm back and the next altar works. Removes one of the riskiest decisions on the plane.
  - **Source**: [Astral Plane — NetHackWiki](https://nethackwiki.com/wiki/Astral_Plane)
  - **Apply to**: The Astral Plane
  - **Why interesting**: A high-impact, specific item-pairing that changes Astral routing — directly addresses the "pick the right altar or game over" trap.
- **Don't put on a ring of conflict while your minion Angel is alive**: It vanishes and your god replaces it with four hostile Angels. Either kill the minion first, wait for it to die, or wear conflict only after entering Astral with the Angel already engaged with the Riders.
  - **Source**: [Astral Plane — NetHackWiki](https://nethackwiki.com/wiki/Astral_Plane)
  - **Apply to**: The Astral Plane
  - **Why interesting**: Specific gotcha that turns the standard "wear conflict on Astral" advice into a death sentence if mistimed.

### Elemental Planes
- **A cursed scroll of gold detection on each plane reveals the portal location**: It marks all traps (including the portal) with the gold symbol. Confused gold detection also works. Saves the random-walk search across an open plane.
  - **Source**: [Portal detection methods — NetHackWiki](https://nethackwiki.com/wiki/Portal_detection_methods)
  - **Apply to**: The Elemental Planes (each plane)
  - **Why interesting**: A specific consumable that solves the "where's the portal?" problem on every plane — a real planning item to stash before Astral.
- **The Amulet of Yendor detects portals when wielded on the Planes**: Yes, you can wield the Amulet itself as a portal-finder on the Planes (and only on the Planes). Lets you skip the scroll of gold detection if you have nothing else.
  - **Source**: [Portal detection methods — NetHackWiki](https://nethackwiki.com/wiki/Portal_detection_methods)
  - **Apply to**: The Elemental Planes
  - **Why interesting**: The Amulet has a plane-only power players forget about — the book doesn't mention it at all.

### Quest / Reaching XL 14
- **Stash wraith corpses and gain-level potions for the Quest gate**: At quest-ready depth, XP-per-monster slows so much that natural leveling is glacial. Save wraith corpses (a guaranteed level each) and any blessed potions of gain level to push from ~XL 10-12 to 14 fast.
  - **Source**: [Wraith — NetHackWiki](https://nethackwiki.com/wiki/Wraith), [Experience level — NetHackWiki](https://nethackwiki.com/wiki/Experience_level)
  - **Apply to**: The Quest (XL 14 gate)
  - **Why interesting**: Practical strategy for the most universal "stuck" moment in mid-game runs; the book states the XL 14 requirement but not how winners actually hit it.
- **Kill wraiths off-graveyard for guaranteed corpses**: Undead killed on a graveyard level have a heavily reduced corpse drop. Lead wraiths upstairs to a normal level before killing them, otherwise the corpse vanishes.
  - **Source**: [Wraith — NetHackWiki](https://nethackwiki.com/wiki/Wraith)
  - **Apply to**: The Quest / Valley of the Dead
  - **Why interesting**: Tactical detail that changes how you engage wraiths in the Valley of the Dead (where every kill is on a graveyard) — directly saves you XLs.

### Gnomish Mines / Minesflayer
- **"Minesflayer" warning: a mind flayer can spawn anywhere in the Mines outside Minetown/Mine's End at level generation**: The message "you sense a faint wave of psychic energy" is your only warning. A mid-game adventurer who reads this on an unexplored Mines level should retreat, telepathy-prep, or skip the level. Mid-game mind-flayer attacks drain Int 1d4 per hit and can permanently strip your spellcasting.
  - **Source**: [Mind flayer — NetHackWiki](https://nethackwiki.com/wiki/Mind_flayer)
  - **Apply to**: The Gnomish Mines
  - **Why interesting**: A specific named community warning ("minesflayer") that saves runs — the book describes Mines as a "comfortable detour" without flagging this real and notorious early-game killer.

### Sokoban / Bag of Holding / Polypile
- **Polypiling rule: never put your real bag of holding next to the polyfodder**: People have lost their entire kit because they zapped polymorph at a pile that contained the wrong bag. Always polypile on a marked floor square far from your main pack.
  - **Source**: [Polypiling — NetHackWiki](https://nethackwiki.com/wiki/Polypiling)
  - **Apply to**: Wishes/Artifacts or Castle (wand of polymorph use)
  - **Why interesting**: A specific catastrophic-failure mode the book doesn't warn against — players read "polypile for magic items" and immediately do this wrong.
- **Max your Luck before polypiling to reduce golem creation rate**: Polypile failures create golems that often destroy adjacent items; high Luck cuts the golem rate substantially.
  - **Source**: [Polypiling — NetHackWiki](https://nethackwiki.com/wiki/Polypiling)
  - **Apply to**: Why Luck Matters (or polypile mention)
  - **Why interesting**: Concrete Luck-pays-off case beyond the "to-hit and prayer" examples in the book.

### Demon Bribery
- **Lawful demon princes accept half the usual bribe**: If you're co-aligned with Geryon/Dispater/Baalzebub/Asmodeus (all lawful), the demand is halved. So lawful characters get the cheapest passage through Gehennom, on top of the already-known bag-of-holding-the-gold trick.
  - **Source**: [Bribe — NetHackWiki](https://nethackwiki.com/wiki/Bribe)
  - **Apply to**: Gehennom (Demon-prince lairs)
  - **Why interesting**: An alignment-specific tactical detail the book's bribery passage doesn't mention — Lawfuls get a real discount.
- **Refused bribes turn the demon permanently hostile and offer never repeats**: If you decline the offer, that prince won't ever ask again — you've committed to fighting them. Bribe-and-commit, don't bribe-and-dither.
  - **Source**: [Bribe — NetHackWiki](https://nethackwiki.com/wiki/Bribe)
  - **Apply to**: Gehennom (Demon-prince lairs)
  - **Why interesting**: A one-shot decision point the book describes as merely "they may attack" — the actual rule is sharper.

### Medusa's Island
- **Throw a cockatrice corpse at Medusa for a guaranteed kill that bypasses reflection requirements**: A wielded or thrown cockatrice corpse stones her on contact (she's not stoning-resistant). Useful for early-arrival kills before you have the amulet of reflection from Sokoban.
  - **Source**: [Medusa — NetHackWiki](https://nethackwiki.com/wiki/Medusa), [Stoning — NetHackWiki](https://nethackwiki.com/wiki/Stoning)
  - **Apply to**: Medusa's Island
  - **Why interesting**: A specific alternative-kill route. The book lists "cockatrice corpse" in passing under one-shot kills; this is the dedicated tactic.
- **Don't eat Medusa's corpse**: It stones you instantly. Common impulse since her corpse is high-difficulty and feels like a sacrifice candidate.
  - **Source**: [Medusa — NetHackWiki](https://nethackwiki.com/wiki/Medusa)
  - **Apply to**: Medusa's Island
  - **Why interesting**: Specific instadeath warning the book's medusa section doesn't include.

### Identification / Altar Use
- **Damerell's name-the-stack trick**: Drop part of a stack on an altar, see the BUC flash, name the stack "blessed"/"uncursed"/"cursed", and now you've identified every other stackable copy you find without revisiting the altar.
  - **Source**: [NetHack Object Identification Spoiler — Damerell](http://www.chiark.greenend.org.uk/~damerell/games/nhid.html)
  - **Apply to**: Identification / Luck (altar mechanics) — possibly the Mines/Minetown altar context
  - **Why interesting**: A specific named technique used by experienced players that the book doesn't cover at all. Saves significant time identifying potions/scrolls.

### Pet Routes / Stash Management
- **Magic whistle warps all pets on the current level to your side**: Works on no-teleport levels, ignores ridden steeds, and is the standard way to keep pets with you through stair runs without waiting. The book doesn't mention this exists.
  - **Source**: [Magic whistle — NetHackWiki](https://nethackwiki.com/wiki/Magic_whistle)
  - **Apply to**: Pets / Ascension Run prep
  - **Why interesting**: A specific tool that solves the "I left my pet on Dlvl 3" problem most ascensions hit.
- **A pet purple worm grown on graveyard wraiths can engulf the Wizard of Yendor**: Engulf damage isn't subject to "no corpse drop" rules, and a high-level purple worm reliably swallows and kills covetous monsters including the Wizard. A long-investment but real tactic for keeping the Wizard suppressed during the Ascension Run.
  - **Source**: [Wraith — NetHackWiki](https://nethackwiki.com/wiki/Wraith)
  - **Apply to**: The Ascension Run / Wizard's Tower
  - **Why interesting**: A genuine flavor-rich, source-citable pet strategy that meaningfully changes the climb.

### Excalibur / Fountain Dipping
- **Knights dip at 1-in-6 odds, all other Lawfuls at 1-in-30**: At XL 5+, a Lawful character dipping a non-artifact long sword in a non-Minetown fountain has these per-dip odds. Burns the fountain on success or on the worst failure outcomes. Knights converge fast; everyone else should expect to chew through several fountains.
  - **Source**: [Excalibur — NetHackWiki](https://nethackwiki.com/wiki/Excalibur)
  - **Apply to**: Artifacts (Excalibur) / Fountains
  - **Why interesting**: The book has the numbers but doesn't lay out the "Minetown fountains don't count, plan to visit several elsewhere" detail.

---

## Cluster 6: Mechanics & Extras

### Altars / Thrones / Sinks / Vaults
- **Convert Minetown altar safely with a scroll of earth (boulder-trap the priest)**: a known community technique for flipping the Minetown altar without dying to the angry priest.
  - **Source**: [Aligned priest — NetHack Wiki](https://nethackwiki.com/wiki/Aligned_priest) and [Safely converting the minetown altar (RGRN)](https://groups.google.com/g/rec.games.roguelike.nethack/c/CN7lUjtzw3Q)
  - **Apply to**: Altars (1038) — sidebar on cross-alignment conversion
  - **Why interesting**: Minetown's altar is often the only altar a beginner sees for a long stretch; if it's the wrong alignment, the scroll-of-earth trick is the strategic answer (and changes whether you commit early or wait).

- **Don't sacrifice your starting pet — aggravate monster + god anger is permanent**: sacrificing pets (or any tame creature) costs alignment, gives intrinsic aggravate monster, and adds to the god's anger counter; sacrificing your own race when non-chaotic costs 5 alignment and 5 Luck.
  - **Source**: [Sacrifice — NetHack Wiki](https://nethackwiki.com/wiki/Sacrifice)
  - **Apply to**: Altars (1038) — under sacrificing
  - **Why interesting**: Players new to altar sacrifice routinely throw their kitten on the altar because "fresh corpse, easy meat"; this can sink the run.

- **Throne wishes require Luck ≥ 7, not just "positive Luck"**: the wish branch of the throne table only fires above a real luck threshold; sitting at +1 luck for a wish is a waste.
  - **Source**: [Throne — NetHack Wiki](https://nethackwiki.com/wiki/Throne)
  - **Apply to**: Thrones (1072) — tighten the "positive luck" claim
  - **Why interesting**: The current book says "ideally when your luck is positive (for a shot at the wish)" — actually it's a Luck ≥ 7 gate, which changes the calculus completely (you usually want to luckstone-grind first).

- **Kicking thrones — the deterministic gem-count luck readout**: with positive Luck, kicking a throne dislodges 201–500 gold and Luck+1 gems (max 6). Because the gem count is deterministic, kicking a fresh throne can be used as a luck-meter to read your Luck if it's under 5.
  - **Source**: [Throne — NetHack Wiki](https://nethackwiki.com/wiki/Throne)
  - **Apply to**: Thrones (1072) — add #kick mechanic, not currently covered
  - **Why interesting**: Whole throne action (`#kick`) is missing from the book; gems-as-luckometer is a colorful, strategically useful trick.

- **Vault as a gold safe via pet teleportation closet**: park your pet on the vault-teleporter trap square in the niche; the pet is forced to take the trap diagonally, and the trap isn't consumed, letting you re-enter at will.
  - **Source**: [Vault — NetHack Wiki](https://nethackwiki.com/wiki/Vault)
  - **Apply to**: Vaults (1168) — repeatable-access section
  - **Why interesting**: Changes vaults from "one-shot gold pickup" to "permanent gold safe" — material strategic upgrade.

- **Vault gold detection via gold-detect scroll / object detection / magic mapping**: the engraving isn't your only locator; uncursed gold detection reveals the vault's gold pile, magic mapping reveals the closet, and object detection sees the gold pile through walls.
  - **Source**: [Vault — NetHack Wiki](https://nethackwiki.com/wiki/Vault)
  - **Apply to**: Vaults (1168) — finding vaults
  - **Why interesting**: Currently the book only mentions the *"ad aerarium"* engraving and digging; the detection-scroll routes are the practical answer when those don't exist.

- **Sink ring-drop: leave one sink unkicked / unquaffed for ring ID**: kicking summons monsters, quaffing rolls bad effects, and either can destroy or move the sink before you've used it for rings. Reserve one virgin sink.
  - **Source**: [Sink — NetHack Wiki](https://nethackwiki.com/wiki/Sink)
  - **Apply to**: Sinks (1103) — strategy paragraph
  - **Why interesting**: A common YASD: kick the only sink, summon a black pudding, escape, then realize you can't ID the rings anymore.

- **Sink-ring-of-hunger needs an object on the sink to identify**: the "items vanish" message only fires if there's already an item on the square. With a bare sink, the ring of hunger gives the generic "bouncing down the drainpipe" message instead.
  - **Source**: [Sink — NetHack Wiki](https://nethackwiki.com/wiki/Sink)
  - **Apply to**: Sinks (1103) — drop-ring table caveat
  - **Why interesting**: Subtle rule that changes the per-ring outcome table; a beginner won't otherwise know to seed the sink with junk.

### Traps / Engravings / Elbereth
- **Magic-trap charisma grind**: stepping on a magic trap has a chance to raise Charisma (averaging about 1.4 points per zap), and a patient player can ride a found magic trap to maximum Cha. Often paired with shop price-ID grinding.
  - **Source**: [Magic trap — NetHack Wiki](https://nethackwiki.com/wiki/Magic_trap)
  - **Apply to**: Dangerous Traps (1736) — magic trap row, note positive uses
  - **Why interesting**: Book lists magic traps as "random effects (some good, some very bad)" without naming the headline good outcome; Cha-grinding directly affects shop prices and is genuinely strategic.

- **Polymorph-trap removal: dig down or cancel**: a pick-axe through the trap removes it (the resulting pit overrides the trap); cancellation also works but detonates 23–38 damage in 3×3.
  - **Source**: [Polymorph trap — NetHack Wiki](https://nethackwiki.com/wiki/Polymorph_trap)
  - **Apply to**: Dangerous Traps (1736) — polymorph trap entry
  - **Why interesting**: Book mentions the cancellation blast for magical traps generally but doesn't note the cleaner pick-axe option; relevant for players without MR/Unchanging who still want the trap gone.

- **Fire-trap defense: bag/sack inventory protection**: scrolls, potions, and spellbooks inside a sack survive fire traps; oilskin sacks add cold/shock/cancellation/water protection on top. Once a Wand of Polymorph turns a sack into something better, you lose this protection.
  - **Source**: [Fire trap — NetHack Wiki](https://nethackwiki.com/wiki/Fire_trap), [Oilskin sack — NetHack Wiki](https://nethackwiki.com/wiki/Oilskin_sack)
  - **Apply to**: Dangerous Traps (1736) — fire trap section
  - **Why interesting**: Book identifies the danger but doesn't give the standard defense; "keep scrolls in a sack" is the canonical answer for Gehennom and fire traps both.

- **Bear-trap escape: diagonal moves are ~5× faster than orthogonal**: trying to step diagonally out frees you in 4–7 turns; orthogonal attempts take roughly 5× longer. A wand/spell of opening (or knock cast at self) frees you immediately.
  - **Source**: [Beartrap — NetHack Wiki](https://nethackwiki.com/wiki/Beartrap)
  - **Apply to**: Dangerous Traps (1736) — bear trap row
  - **Why interesting**: Book lists the bear trap effect but no escape strategy; the diagonal rule is a real time-saving fact that beginners do not discover by themselves.

- **Teleport trap with Ctrl+T forces use despite Magic Resistance**: `Ctrl+T` (#teleport) on a teleport trap takes the trap intentionally, bypassing MR's block. Critical for vault entry on non-noteleport levels when you have MR equipped.
  - **Source**: [Teleportation trap — NetHack Wiki](https://nethackwiki.com/wiki/Teleportation_trap), [Teleportation — NetHack Wiki](https://nethackwiki.com/wiki/Teleportation)
  - **Apply to**: Movement Traps (1706) / Advanced Controls (7579)
  - **Why interesting**: Most MR builders forget they can still use a teleport trap voluntarily; this changes vault entry strategy materially.

- **Permanent Elbereth still erodes 1/26 per scared-monster trigger**: even burned-with-wand-of-fire Elbereth has a small per-fleeing-monster character-erosion chance (1/26 semi-permanent, 1/52 permanent). It's effectively eternal in most fights, but a long siege does eventually chew it.
  - **Source**: [Elbereth — NetHack Wiki](https://nethackwiki.com/wiki/Elbereth)
  - **Apply to**: Elbereth (1994), "Rules of the ward"
  - **Why interesting**: Book says burned Elbereth "doesn't erode at all under normal conditions" — there's a small but real per-event erode. Matters during long anchor-the-corridor fights.

- **Scroll of scare monster as a portable "stronger Elbereth"**: a dropped scroll of scare monster has the same effect as Elbereth on its square but stronger — and it doesn't erode. Pick it up to move it. With holy water to keep it blessed it can last the whole game.
  - **Source**: [Scroll of scare monster — NetHack Wiki](https://nethackwiki.com/wiki/Scroll_of_scare_monster)
  - **Apply to**: Elbereth (1994), "Practical use"
  - **Why interesting**: Not currently in the book at all, despite being one of the most useful "found-scroll" items in 5.0 — and it's the only known way to defile-attack from safety, since attacking *doesn't* destroy the scroll the way it destroys Elbereth.

- **Iron chain as a permanent Elbereth anchor on dust**: pets never pick up iron chains, so a chain dropped on a dust-Elbereth square stops a wandering pet from smudging it. (Combine with the rule that the chain itself doesn't block your standing on the square.)
  - **Source**: [Iron chain — NetHack Wiki](https://nethackwiki.com/wiki/Iron_chain)
  - **Apply to**: Elbereth (1994) / Engravings (1923) — dust engraving durability
  - **Why interesting**: Tiny but life-saving for early-game characters who can only finger-write Elbereth and don't want their pet wiping it on the next turn.

- **Wand engraving as wand ID via the dust-overwrite test**: write any word in dust first ("Elbereth" or "x"), then *overwrite* it with the unknown wand. The overwrite message (and effect on the engraving) reveals the wand type for nine wands unambiguously.
  - **Source**: [Wand — NetHack Wiki](https://nethackwiki.com/wiki/Wand), [Engraving — NetHack Wiki](https://nethackwiki.com/wiki/Engraving)
  - **Apply to**: Engravings (1923) — wand identification cross-reference
  - **Why interesting**: Book mentions the engrave-test exists ("covered in the wand chapter") but the *write-then-overwrite* procedure isn't sketched, and the overwrite step matters: without prior dust, several wands give an ambiguous "you write in the dust" line.

- **Iron bars + dwarvish mattock = dig diagonally past the niche**: the standard community workaround for early game iron bars is to wield a mattock or pick-axe and dig diagonally into the stone wall next to the bars, bypassing the bars themselves.
  - **Source**: [Iron bars — NetHack Wiki](https://nethackwiki.com/wiki/Iron_bars), [Dwarvish mattock — NetHack Wiki](https://nethackwiki.com/wiki/Dwarvish_mattock)
  - **Apply to**: Iron Bars (2114)
  - **Why interesting**: Book gives the dig-around idea but not the practical "wield a digging tool, target the diagonal stone, not the bars" recipe; helps players who don't realize bars block the swing.

### Feelings and Sounds
- **"You hear a slurping sound" = a gelatinous cube ate items off the floor on this level**: directly tells you something was just *eaten*, often loot or a corpse on a level you haven't fully cleared.
  - **Source**: [You hear — NetHack Wiki](https://nethackwiki.com/wiki/You_hear)
  - **Apply to**: Feelings and Sounds (2144) table
  - **Why interesting**: Missing from the current table. A slurp on a level with a stash is actionable: rush back, your stuff is being digested.

- **"You hear a crunching sound" = metallivore ate metal on this level**: a rock mole, rust monster, or xorn just ate something metallic — important if you left armor or weapons on the floor.
  - **Source**: [You hear — NetHack Wiki](https://nethackwiki.com/wiki/You_hear), [Metallivore — NetHack Wiki](https://nethackwiki.com/wiki/Metallivore)
  - **Apply to**: Feelings and Sounds (2144) table
  - **Why interesting**: Currently absent; pairs with the "monsters loot containers" 5.0 change in the New Dangers section.

- **"You hear a wolf/jackal howling at the moon" = a werecreature is on this level**: a foreknown were-monster ID before you stumble into a fight cursed-into-lycanthropy.
  - **Source**: [You hear — NetHack Wiki](https://nethackwiki.com/wiki/You_hear)
  - **Apply to**: Feelings and Sounds (2144) table
  - **Why interesting**: Lycanthropy is a serious early-game derailer; this warning lets you prepare wolfsbane or holy water before the bite.

- **"You hear crashing rock" = a tunneler dug through stone on this level**: a dwarf, gnome miner, rock mole, or umber hulk just tunneled. Lets you know a peaceful gnome layout is being redesigned, or to expect new paths.
  - **Source**: [You hear — NetHack Wiki](https://nethackwiki.com/wiki/You_hear)
  - **Apply to**: Feelings and Sounds (2144) table
  - **Why interesting**: Sounds-as-intel theme; tells you whether the Mines map you remember is still accurate.

- **"You hear a chugging sound" / "a nearby zap" = a monster drank a potion or zapped a wand**: monster behavior intel — somebody offscreen just used a consumable on themselves (often healing) or zapped a directional wand at something.
  - **Source**: [You hear — NetHack Wiki](https://nethackwiki.com/wiki/You_hear)
  - **Apply to**: Feelings and Sounds (2144) table
  - **Why interesting**: With the 5.0 change that monsters use containers and unlock chests, audible item-use becomes more common; lets a careful player anticipate a healed-up covetous boss.

### Advanced Controls
- **Travel command `_` + destination + `.`**: the keystroke `_` then point-to-target then `.` runs the shortest-path autopilot to any explored square, opening doors and stopping on interrupt. `_<.` walks to the upstairs, `__` to an altar.
  - **Source**: [Travel — NetHack Wiki](https://nethackwiki.com/wiki/Travel)
  - **Apply to**: Advanced Controls (7579)
  - **Why interesting**: Travel is missing from the book's controls section entirely. It's the single biggest QoL command after Ctrl+A — players who don't know it are walking levels one G-key at a time.

- **`#force` extended command for locked chests**: with a wielded weapon, `#force` pries or smashes a lock open — bladed weapons risk breaking the blade, blunt weapons risk destroying the chest contents.
  - **Source**: [Force — NetHack Wiki](https://nethackwiki.com/wiki/Force), [Lock — NetHack Wiki](https://nethackwiki.com/wiki/Lock)
  - **Apply to**: Advanced Controls (7579) — or a Chests subsection
  - **Why interesting**: A standard early-game chest-cracking technique not in the book; matters when no unlocking tool dropped.

### Sokoban (general tips)
- **The "and still get the prize" rule: cheating costs Luck only until the level is solved**: each infraction is −1 Luck, but the penalty *clears* when you finish the level legitimately. The prize itself isn't gated on a clean solve in 3.6 / 5.0 — only Sokoban-conduct tracking is.
  - **Source**: [Sokoban — NetHack Wiki](https://nethackwiki.com/wiki/Sokoban), [Sokoban prize](https://nethack.fandom.com/wiki/Sokoban_prize)
  - **Apply to**: Sokoban Solutions (7705) preamble
  - **Why interesting**: Beginners often think breaking one rule poisons the entire prize; really it's "lose some luck now, regain it on completion, prize still drops" — relevant when stuck and considering a desperate boulder-fracture.

- **Push leftover boulders into corners after solving**: keeps you from accidentally re-shoving one into your own path on a return trip, and reveals items that might be hidden under them.
  - **Source**: [Sokoban — NetHack Wiki](https://nethackwiki.com/wiki/Sokoban)
  - **Apply to**: Sokoban Solutions (7705) preamble (already mentioned but as a "general tips" section worth elaborating)
  - **Why interesting**: Already partly covered ("push leftover boulders into corners") — but the item-under-boulder reason adds practical value.

### Conducts
- **Polypile-less is the easiest conduct to break by accident**: a single step on an unidentified polymorph trap while carrying any item that gets polymorphed by the magic trap effect, or any zap-on-self with a wand of polymorph, breaks it forever. ~58% of NAO ascensions broke this conduct.
  - **Source**: [Polymorph — NetHack Wiki](https://nethackwiki.com/wiki/Polymorph), [Conduct — NetHack Wiki](https://nethackwiki.com/wiki/Conduct)
  - **Apply to**: Polymorph Restrictions (8600)
  - **Why interesting**: Book mentions "no polymorph objects" but doesn't flag the *accidental break* risk, which is the actual gotcha. Wandering into an unknown poly trap while carrying gear can quietly end the conduct.

- **Foodless ascensions are 1.2% of NAO wins; wishless is 11.5%**: real difficulty-ranking from public-server data, plus the canonical foodless strategy: pray-through-hunger or wish for slow digestion early. Wishless includes the "answer 'nothing' to forced wishes" rule (smoky potion djinn, Amulet pickup, wresting an empty wand).
  - **Source**: [Foodless — NetHack Wiki](https://nethackwiki.com/wiki/Foodless), [Wishless — NetHack Wiki](https://nethackwiki.com/wiki/Wishless)
  - **Apply to**: Combining Conducts (8671)
  - **Why interesting**: Concrete numbers turn the "stuff of legends" sentence into actionable rarity ranking; helps players pick which conduct stack to attempt.

- **Pacifist Castle/Gehennom: pet Archon + spell of charm monster**: the canonical pacifist endgame plan is a polymorphed-up pet (often Archon via figurine), the spell of charm monster for crowd-pacification, and conflict for swarm fights.
  - **Source**: [Pacifist — NetHack Wiki](https://nethackwiki.com/wiki/Pacifist)
  - **Apply to**: Pacifist (8491)
  - **Why interesting**: Book gestures vaguely at "large, well-trained pet" — the *figurine of an Archon* wish recipe is the actual go-to and changes how players plan their early wishes.

- **Illiterate ID via pets and prices, not scrolls**: pet-step-on-item reveals BUC (cursed items get stepped on with hesitation messages), and price-ID still works because *looking at* a shop price tag is not reading. Throne-sit identification works too; reading already-engraved Elbereth on the floor does not break the conduct.
  - **Source**: [Illiterate — NetHack Wiki](https://nethackwiki.com/wiki/Illiterate)
  - **Apply to**: Illiterate (8511)
  - **Why interesting**: Book mentions "creative workarounds" without naming the two big ones (pet + price-ID); these are what makes illiterate playable.

### Shopping
- **Sucker pricing: shopkeepers offer 1/3 instead of 1/2 base price to "suckers"**: low-Cha or low-XL characters get the sucker rate. Charisma also flips the buy-price markup: ACURR ≤ 5 doubles prices, ACURR > 18 halves them.
  - **Source**: [Price identification — NetHack Wiki](https://nethackwiki.com/wiki/Price_identification), [Shop — NetHack Wiki](https://nethackwiki.com/wiki/Shop)
  - **Apply to**: Shopping (8804) — Credit and Debt section already touches Charisma; sucker rule worth its own callout
  - **Why interesting**: Knowing you are being "sucker-priced" gives a reason to magic-trap-grind Cha before serious shopping runs.

- **Credit cloning via gold-loving monsters**: drop gold in shop → orcs/leprechauns/etc. wander in and pick it up → kill them outside the shop → keep the gold *and* the credit. (Pet-based variants work only if gold is bagged first, since 3.6 pets only grab one coin at a time.)
  - **Source**: [Credit cloning — NetHack Wiki](https://nethackwiki.com/wiki/Credit_cloning), [Stealing from shops — NetHack Wiki](https://nethackwiki.com/wiki/Stealing_from_shops)
  - **Apply to**: Credit and Debt (8826)
  - **Why interesting**: Mentioned in book only as "shop as safe-deposit"; the actual *exploit* (recover gold AND keep credit) is one of NetHack's most famous bits of shop-cheese. Worth a single sentence noting the technique exists even if discouraged.

- **Web-trap or pit-pin the shopkeeper for safe assassination**: spinning webs (as a giant spider) where the shopkeeper stands, or digging pits around their patrol square, immobilizes them for ranged kills. Note 5.0 nerfs pits-and-webs — shopkeepers can now clear pits and webs around themselves.
  - **Source**: [Shopkeeper — NetHack Wiki](https://nethackwiki.com/wiki/Shopkeeper), [Stealing from shops — NetHack Wiki](https://nethackwiki.com/wiki/Stealing_from_shops)
  - **Apply to**: Shopkeeper Behavior (8891) / What Changed (11410)
  - **Why interesting**: Book already notes the 5.0 pit-and-web nerf at line 11548 ("Shopkeepers can now remove pits and webs around them") — but doesn't connect it to the *historical* exploit it was nerfing. Naming the technique is what makes the nerf comprehensible.

- **400×XL is the "guaranteed protection" floor for priest donations**: not 250×XL minimum (book) — community-consensus number is 400×XL, where guaranteed up to 9 points of intrinsic protection accumulate. (5.0 randomizes this and adds Cheapskate-flag punishment for low offers; the floor still works.)
  - **Source**: [Aligned priest — NetHack Wiki](https://nethackwiki.com/wiki/Aligned_priest), [Intrinsic protection — NetHack Wiki](https://nethackwiki.com/wiki/Intrinsic_protection)
  - **Apply to**: What Changed (11410) — already mentions 400×XL is gone; clarifying old vs new is useful
  - **Why interesting**: The book's 5.0 entry describes "Priest donations are now randomized" but doesn't explain *what was being randomized* — it's the canonical 400×XL → 9 pip pipeline that returning players will remember.

### Gem ID / What Changed / New Hacks
- **Touchstone formal-ID gates on blessed (or non-cursed for Gnomes/Archeologists)**: book covers this. **Additional point worth surfacing**: gnomes / archaeologists also start *knowing* the touchstone's appearance, so they can identify the gray-stone touchstone-vs-luckstone-vs-loadstone problem instantly without any ID work.
  - **Source**: [Touchstone — NetHack Wiki](https://nethackwiki.com/wiki/Touchstone)
  - **Apply to**: Gem Identification (8951)
  - **Why interesting**: Book mentions the *use* perk but not the *knowledge* perk; for gnomes this turns a dangerous gray-stone puzzle into a trivial inspect.

- **Named glass is rejected by unicorns; un-named glass is "graciously" accepted (no luck change)**: throwing un-#named worthless glass at a co-aligned unicorn is safe — they accept and drop it. #named glass is rejected outright. This lets you offload glass for ID without breaking your Luck even on cross-aligned unicorns.
  - **Source**: [Gem — NetHack Wiki](https://nethackwiki.com/wiki/Gem)
  - **Apply to**: Gem Identification (8951) section
  - **Why interesting**: Already noted that "Worthless glass never costs luck" — but the #name distinction is the practical trigger.

- **Confused gold-detection scroll reveals all magical traps**: reading any scroll of gold detection while confused turns the level-wide gold reveal into a level-wide *trap* reveal — particularly polymorph and teleport traps. Useful in Gehennom and on the Gnomish Mines stash hunt.
  - **Source**: [Scroll of gold detection — NetHack Wiki](https://nethackwiki.com/wiki/Scroll_of_gold_detection)
  - **Apply to**: Searching and Detection (1816)
  - **Why interesting**: Confused-scroll trickery is a category not currently in the trap-finding list; a single confused gold-detect can replace half a dozen search marathons.
