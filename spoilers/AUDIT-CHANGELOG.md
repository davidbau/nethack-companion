# Audit Changelog

Systematic audit of `companion.md` for accuracy (vs NetHack 5.0 source),
community wisdom (NetHackWiki + r/nethack), beginner-friendly language
(in-game voice, no code jargon), and helpful cross-references.

Order is shuffled with seed 42 for reproducibility (`.audit-sections.txt`).
Each batch is committed individually.

## Progress

- Total sections: 272
- Deeply audited: ~45 sections
- Em-dash sweep applied across the whole book: 162 prose em-dashes removed
- Retroactive HTML audit citations added: 11 chapter/section audit blocks updated with 2026-05-31 entries
- Status: substantial first pass complete; the giant Bestiary group remains deferred for a future pass

## Summary of major factual corrections

1. **Plane of Earth (companion.md:8183)** — was "encased in solid rock and boulders, surrounded by earth elementals." Actually arrives in a small cavern at (69,16) with a scripted Elvenking + minotaur (dat/earth.lua:52-56); earth elementals cluster in other caverns; the plane is a network of caverns separated by diggable rock.
2. **Plane of Water (companion.md:8229)** — species list cited "sea monsters" (not a species; just the monsters.h section comment) and "moccasin from a fountain" (water moccasin is S_SNAKE, not class `;`). Corrected to the actual S_EEL species and the kraken-in-Medusa's-pool reference.
3. **Sacrifice (companion.md:3875)** — artifact gift formula was wrong. Book said "1 in (10 + 2·n)" giving 1/10 first roll and 1/14 second. Actual (pray.c:1792): `!rn2(6 + (2 * u.ugifts * nartifacts))`, so first gift is 1/6, subsequent gifts drop multiplicatively. Also added XL>=3 + non-negative Luck prerequisites and the acid blob 50-turn exception.
4. **Castle (companion.md:7615)** — added that the Castle has no conventional down-stair to Gehennom; the five trap doors are the only descent route (dungeon.lua `no_down`, castle.lua:156-160). Castle and bigrm-12 are the only two levels exempt from random mirroring.
5. **Travel (companion.md:8392)** — `__` shortcut for walking to altar was missing the trailing `.`; consistent with `_<.` and `_>.` is `__.`.
6. **Field Guide / Imps (companion.md:905, 10976)** — was "annoying but not dangerous" / "none individually scary." Actually homunculus AD_SLEE bite (monsters.h:551-558) is a real early-game threat; both summaries now flag it.
7. **Liches bestiary (companion.md:11689)** — touch of death kill chance at arch-lich m_lev 25 is ~48% per cast without Antimagic (mcastu.c:389-408). Only the Wizard of Yendor literally has M3_COVETOUS in 5.0 (monsters.h:2857), so the broader "covetous monsters" framing was overstated.
8. **Nymphs (companion.md:11100)** — post-theft rloc is within-level only (mhitu.c:2303 -> teleport.c:1799). The "nymph walks off the level with your bag of holding" framing was overstated.
9. **Scroll of scare monster (companion.md:5388, 2218)** — full pickup state-machine documented (pickup.c:1832-1861): blessed unblesses, uncursed stamps then dusts on second pickup, cursed dusts on first. BUC test is destructive.
10. **Shopping (companion.md:9668, 9756)** — kicking shop door bills + angers (dokick.c:953-956); picking the lock with skeleton key / credit card / lock pick / wand of opening just flips D_LOCKED to D_CLOSED with no damage (lock.c:147-148).
11. **Vaults (companion.md:1233)** — rewrote the guard interaction. Real-name answer: guard demands gold, opens corridor, leads you out (vault.c:551-585). Croesus answer: guard leaves, you keep gold, but you're sealed in. Croesus answer when Croesus is dead: guard goes hostile.
12. **Traps and Hazards (companion.md:1773)** — added the lone-corpse-on-floor tell (corpse `%` glyph hides trap `^`); noted that standard dungeon traps spawn in rooms only, not corridors (mklev.c:2032-2099).

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

### Audit 6: Sacrifice (companion.md:3875)

**Accuracy** — multiple fixes:

- Em-dashes removed (two instances: "killed within the last — 50 turns" and "altar chaotic (not co-aligned —").
- Artifact-gift formula was wrong. Book said "1 in (10 + 2·n)" giving 1/10 first roll and 1/14 second. Actual formula (pray.c:1792): `!rn2(6 + (2 * u.ugifts * nartifacts))`, where `nartifacts` is the total count of artifacts existing in the game world. First gift is 1 in 6 per qualifying sacrifice; subsequent drops sharply because of multiplication, not just additive `+2·n`. Rewrote to give the correct intuition without an over-precise formula.
- Missing prerequisite added: bestow_artifact requires `u.ulevel > 2 && u.uluck >= 0` (pray.c:1784).
- Acid blob exception to the 50-turn rule added (pray.c:1843): `otmp->corpsenm == PM_ACID_BLOB || (svm.moves <= peek_at_iced_corpse_age(otmp) + 50)`.
- "Role's signature artifact" framing is the practical effect, not the mechanism. Actual mechanism (artifact.c:230) is alignment match + skill compatibility. Clarified.
- "There is a minimum" softened to a worthiness-floor framing. The actual mechanic is that mk_artifact filters by giftvalue against the sacrifice value, so low-value sacrifices roll but find no eligible artifact, rather than being rejected outright.

**Changes**: rewrote the rules list and artifact-gift paragraph (companion.md:3883).

### Audit 7: Supply Containers (companion.md:629)

**Accuracy** — verified against mklev.c:1010-1119. All claims correct: 2/3 chance above Oracle, 2/3 chest vs 1/3 large box, 5/6 locked, contents pool, Mines-entry food bonus. Pre-existing audit notes already covered the verification.

**Hyperlinks** — added link from "above the Oracle" to the Oracle section (companion.md:633).

**Changes**: hyperlink only.

### Audit 8: Your First Descent intro (companion.md:479)

**Accuracy** — verified against pre-existing audit notes (no specific claims to re-verify beyond what was already documented).

**Language** — `characters` -> `adventurers` for in-world voice consistency (companion.md:509).

### Audit 9: Long sword (companion.md:10015)

**Accuracy** — pre-existing audit notes verify long-sword stats (objects.h:270-280), Excalibur dipping mechanics (fountain.c:404-421: XL>=5, quan==1, 1/30 normally, 1/6 for Knights, non-Lawfuls get cursed sword), and artifact forms list (Excalibur, Frost Brand, Fire Brand, Giantslayer, Vorpal Blade, Sunsword). All correct.

**Changes**: no changes needed.

### Audit 10: Saber (companion.md:9979)

**Accuracy** — pre-existing audit notes verify saber stats and artifact forms (Grayswandir from artilist.h:170, Werebane from artilist.h:166). All correct.

**Changes**: no changes needed.

### Audit 11: Two-handed sword (companion.md:10037)

**Accuracy** — pre-existing audit notes verify the 3/2 Strength damage bonus (uhitm.c:1467-1468 gated on bimanual + HMON_MELEE) and that Tsurugi of Muramasa is the artifact form, NOT Vorpal Blade (which is a long sword). All correct.

**Language** — em-dash removed from "in 5.0 — your STR damage" (now colon) (companion.md:10046).

**Changes**: em-dash removed.

### Audits 13-19 (batch summary)

- **Moloch's Sanctum (companion.md:7902)** — clean. Pre-existing claims about the sealed Sanctum, High Priest, and Amulet location all consistent with the source.
- **The Scroll Table (companion.md:5409)** — accurate (scroll prices match objects.h). Pre-existing hyperlinks to scroll-specific subsections useful.
- **The Apothecary intro (companion.md:5224)** — atmospheric, no em-dashes, no specific verifiable claims beyond the table that follows.
- **Starting Pets (companion.md:4070)** — accurate; "most roles begin with a little dog or kitten" is a fair generalization (Knights have pony, Healers vary). No fixes.
- **Fighting Smart (companion.md:2587)** — recently revised in earlier turns. Confirmed clean.
- **Key Wands — Wand of Wishing (companion.md:5639)** — verified 1 charge at generation (mkobj.c:1117 `otmp->spe = 1`), recharge limit 1 (read.c:738-740 `lim = 1`), explosion on second recharge attempt (read.c:761-762). Book's "2 wishes plus a possible wrested third" correct.
- **Key Wands — Make Invisible duration (companion.md:5689)** — verified 31-45 turns (zap.c:2836 `incr_itimeout(&HInvis, rn1(15, 31))`). Book's range correct.
- **Key Wands — Cancellation (companion.md:5672)** — em-dash removed from "loses most of its special attacks — a cancelled cockatrice".
- **Luck and Fortune intro (companion.md:6696)** — clean. Friendly framing, no em-dashes. Pre-existing audit notes verify mechanics (drift, cap, peaceful kill costs, prayer rejection).
- **Broadsword, Long sword variants (companion.md:9997, 10015)** — clean per pre-existing audit notes.

### Audits 20-35 (batch summary)

Sections covered: What to Wish For, Sokoban Level 3 Version A, Speed (already revised), Key Potions, Mace, Atheist, Sokoban Level 1 Version B, The Skill Ladder, Petless, Pauper, Permadeaf, Club, Starvation, Iron Bars, Other Notable Tools, Wishing Restrictions, Crowning, Traps and Hazards intro, Wands and Staves intro, Gem ID Through Selling, Weaponless, Boomerang, Medusa's Island, Level 4 Sokoban, Prayer, Dagger, Enchantment Drain, Alignment.

**Prose em-dashes removed** (10 total):
- Iron Bars: "can squeeze between" / "can melt them too"
- Other Notable Tools: "at the Castle drawbridge" / "intrinsic-grant still applies"
- Gem ID Through Selling: "doesn't affect touchstoning"
- Medusa's Island: "Perseus" / "in the fourth (Medusa-2 swap)"
- Dagger: "aren't trash"
- Petless: "The game won't stop you"
- Permadeaf: "shrieker still shrieks and still summons"

**Accuracy** — pre-existing audit notes verify each section's claims. No new accuracy issues found in this batch. The audit notes themselves remain in HTML comments so they don't render to the printed book.

**Changes**: 10 em-dash removals across 9 sections.
</content>
