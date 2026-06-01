# Audit Changelog

Systematic audit of `companion.md` for accuracy (vs NetHack 5.0 source),
community wisdom (NetHackWiki + r/nethack), beginner-friendly language
(in-game voice, no code jargon), and helpful cross-references.

Order is shuffled with seed 42 for reproducibility (`.audit-sections.txt`).
Each batch is committed individually.

## Progress

- Total sections: 272
- Audited: 5 (+ 1 deferred: the giant Bestiary group)
- Status: in progress

## Findings

### Audit 1: Plane of Earth (companion.md:8183)

**Accuracy** — the original prose said the player arrives "encased in
solid rock and boulders, surrounded by earth elementals." Verifying
against `dat/earth.lua`:

- Arrival point is **(69,16)** in a small cavern, not stone.
- The arrival cavern contains a scripted Elvenking and a minotaur (both
  hostile), not earth elementals; the elementals cluster in the other
  caverns.
- The plane is a constellation of small caverns separated by diggable
  rock walls; the portal is randomly placed in one of the non-arrival
  caverns, not buried in undug stone.
- Other inhabitants: stone giants, rock trolls, stone golems, pit
  fiends, dust vortices, an umber hulk, pit vipers, barbed devils.
- Level flag `shortsighted` (rm.h:449) affects monster vision only, not
  the player's.
- Level flag `noteleport` blocks self-teleportation.

**Wisdom** — NetHackWiki's "Plane of Earth" page agrees: the Elvenking
and minotaur are a known scripted ambush; players are advised to read a
scroll of magic mapping immediately to locate the portal cavern.

**Language** — original prose was atmospheric but factually wrong.
Rewrote to keep the close, dim, claustrophobic feel while naming the
real arrival ambush and the actual cavern-network structure.

**Changes**: rewrote the paragraph (companion.md:8183). Followup: `lower right` -> `corner` per user feedback, since the level can be flipped on both axes (sp_lev.c:967 flip_level_rnd; only `castle.lua` and `bigrm-12.lua` opt out via noflipx/noflipy).

### Audit 2: The Early Shopping List (companion.md:429)

**Accuracy** — verified:
- Supply chests: `mklev.c:1041` confirms the 5.0 feature; appears on `dlevel < oracle_level.dlevel` with `rn2(3)` truthy chance (= 2/3 of qualifying levels). Book's "two-thirds" is correct.
- Supply chest contents (potions of healing/extra healing/speed/gain energy, scrolls of enchant weapon/armor/confuse monster/scare monster, wand of digging, spell of healing) verified at `mklev.c:1050-1060`.
- Tripe rations: `eat.c:2131-2146` — non-orc, non-carnivorous players vomit 50% of the time. Book's "for your pet, not for you" is correct.
- Burdened encumbrance vs fast monster math: verified against the new Speed section's allocation mechanics. A speed-18 monster gets 2× actions vs a Burdened (9 pts/turn) hero. Book's "two hits per one of yours" against "some monsters" is correct.

**Language** — clean, beginner-friendly. No code jargon.

**Hyperlinks** — added a cross-reference from the identification paragraph to the full identification chapter (`#a-practical-identification-strategy`).

**Changes**: added one hyperlink (companion.md:445).

### Audit 3: Travel (companion.md:8390)

**Accuracy** — verified travel mechanics against `getpos.c:194-218` and `hack.c:1263-1346`. The `_` command enters travel-target mode; typing a background symbol jumps the cursor to the next instance; `.` confirms.

**Language** — em-dash removed from "stopping on any interruption — including" (now a period).

**Consistency** — `__` (walk to known altar) was shown without trailing `.`, inconsistent with `_<.` and `_>.`. Fixed to `__.` for consistency. The pattern is "_" + background_symbol + "." across all three.

**Changes**: rewrote the paragraph to clarify the travel-symbol-shortcut pattern (companion.md:8390).

### Audit 4: Plane of Water (companion.md:8229)

**Accuracy** — the `;` class species list cited "sea monsters" (not a real species name; just the comment header for `S_EEL` in monsters.h). Real species: jellyfish, piranhas, sharks, giant eels, electric eels, krakens (`monsters.h` MON definitions for S_EEL). Also: "moccasin from a fountain" was wrong — water moccasins are `S_SNAKE`, not `;`. Class-`;` genocide does not affect moccasins.

**Changes**: corrected species list, replaced misleading moccasin reference with "kraken occasionally appears in Medusa's pool" (companion.md:8239).

### Audit 5: Gray Stones (companion.md:4864)

**Accuracy** — pre-existing audit notes verified prices (luckstone 60, touchstone 45, loadstone 1, flint 1 at objects.h:1598-1605), weights (loadstone 500, others 10), loadstone curse-at-creation (mkobj.c:978-979), blessed-touchstone rub-identification (apply.c rub_on_stone), Mine's End guaranteed luckstone (minend-*.lua). All correct.

**Language** — em-dash removed from "colored-streak message — and if the touchstone is".

**Hyperlink** — added link from "Mine's End" reference to the Gnomish Mines chapter (`#the-gnomish-mines`).

**Changes**: em-dash removed; hyperlink added (companion.md:4922).
</content>
