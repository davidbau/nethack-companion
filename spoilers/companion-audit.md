# Companion spoilers — audit trail

Running record of claims in `companion.md` that have been verified against
NetHack 5.0 source (`nethack-c/upstream/src/`, `include/`, `dat/`).

Format per entry:
- **Claim** — the statement as it appears (or appeared) in the spoiler
- **Spoiler line** — line number in `companion.md` at time of audit
- **Source ref** — C file:line that decides the answer
- **Verdict** — Correct / Wrong / Defensible / Ambiguous
- **Notes** — interpretation and any caveat

Sort key: ascending spoiler line number within each audit session.

---

## 2026-05-11 — first systematic pass

Audit by Claude Opus 4.7. Covered Tier 1-4 from the audit candidate list:
specific numeric claims, "in current editions" version-change claims, and
monster level / mechanic specifics. NetHack 5.0 source HEAD.

### Class and starting-inventory claims

**Claim**: "Knight pony will get you into trouble if it wanders into a shop."
- **Spoiler line**: 169 (pre-fix, replaced 2026-05-11)
- **Source ref**: `steal.c:618` `mpickobj()` (specifically the `subfrombill()`
  call at line ~641), `mkobj.c:3184` (sanity-check comment confirming
  `no_charge` is valid for pet-held shop items)
- **Verdict**: Wrong
- **Notes**: Pet picking up shop merchandise removes the item from the
  player's bill (`subfrombill`) and sets `no_charge = 0`; only when the
  shopkeeper enters `hot_pursuit` does `clear_no_charge_pets()` flip the
  flag. So pet-aided "shoplifting" is actually favorable to the player.
  Replaced with Excalibur + lance discussion. Section now line 167.

**Claim**: Knight Excalibur dipping odds = 1/6 vs 1/30 for other Lawfuls.
- **Spoiler line**: 172-174 (added 2026-05-11)
- **Source ref**: `fountain.c:405` — `!rn2(Role_if(PM_KNIGHT) ? 6 : 30)`
- **Verdict**: Correct
- **Notes**: Knight gets `rn2(6)`, every other Lawful gets `rn2(30)`.

**Claim**: Rogue starts with short sword, 6 daggers, +1 leather armor,
lock pick, sack, and potion of sickness.
- **Spoiler line**: 207-213 (rewritten 2026-05-11)
- **Source ref**: `u_init.c:133`
- **Verdict**: Correct
- **Notes**: The Rogue inventory table in u_init.c matches exactly.

### Dungeon features

**Claim**: Castle is around level 27; Medusa around level 25.
- **Spoiler line**: 951, 1039
- **Source ref**: `dat/dungeon.lua:78-84` — Medusa `base = -5 range = 4`,
  Castle `base = -1`
- **Verdict**: Defensible
- **Notes**: Both are approximations; Castle is "level (max-1)" and Medusa
  is somewhere in `[max-5, max-2]`. Internally consistent; main dungeon
  depth varies by seed.

**Claim**: Supply containers appear in 2/3 of levels above the Oracle
(new in NetHack 5.0).
- **Spoiler line**: 480-503 (rewritten 2026-05-11)
- **Source ref**: `mklev.c:1009-1126`, especially comment at lines 1014-1022
  ("on other levels above the Oracle, 2/3 chance of a 'supply chest'")
  and the content pool at `mklev.c:1051-1059`.
- **Verdict**: Correct
- **Notes**: Content pool exactly: `POT_EXTRA_HEALING, POT_SPEED,
  POT_GAIN_ENERGY, SCR_ENCHANT_WEAPON, SCR_ENCHANT_ARMOR,
  SCR_CONFUSE_MONSTER, SCR_SCARE_MONSTER, WAN_DIGGING, SPE_HEALING`,
  with 50% override to `POT_HEALING` (and 50% of those drop a stack of 2).
  Container is 2/3 chest 1/3 large box (`rn2(3) ? CHEST : LARGE_BOX`);
  5/6 locked (`!!(rn2(6))`). Mines branch level gets the food cache.

**Claim**: Iron bars can be dissolved with a potion of acid.
- **Spoiler line**: 1192-1196 (pre-fix, replaced 2026-05-11)
- **Source ref**: `zap.c:5348` (`zap_over_floor` with `ZT_ACID`),
  `dothrow.c:812` (thrown-potion bounces off bars), `potion.c:1297`
  (potion's `peffect_acid` operates on creatures only)
- **Verdict**: Wrong
- **Notes**: Bars only dissolve under `ZT_ACID` zap (i.e., monster acid
  breath or you-breathing-acid-while-polymorphed). Thrown potions of acid
  do not trigger this path. Rewritten to recommend dig-around-the-side
  via pick-axe as the practical answer. Also fixed the matching appendix
  bullet at line 5488 (was "broken with a war hammer" — also wrong).

**Claim**: What's behind barred niches: scroll of teleportation
(guaranteed), random object (1/3), human corpse (1/3).
- **Spoiler line**: 1207-1211
- **Source ref**: `mklev.c:782-794`
- **Verdict**: Correct
- **Notes**: Niche generation: `rn2(5) == 0 && IS_WALL` → place IRONBARS;
  `rn2(3) == 0` → human corpse on outside square; SCR_TELEPORTATION
  always placed inside (unless `noteleport` flag); `rn2(3) == 0` → random
  RANDOM_CLASS object also placed.

### Monsters

**Claim**: Lurker above is level 10.
- **Spoiler line**: 1605
- **Source ref**: `include/monsters.h:981` `MON(NAM("lurker above"), ...,
  LVL(10, ...), ...)`
- **Verdict**: Correct

**Claim**: Trapper is level 12.
- **Spoiler line**: 1607
- **Source ref**: `include/monsters.h:990` `LVL(12, ...)`
- **Verdict**: Correct

**Claim**: Yellow/black lights, "level 3-5".
- **Spoiler line**: 1622
- **Source ref**: `include/monsters.h:1169` (yellow light LVL 3),
  `monsters.h:1181` (black light LVL 5)
- **Verdict**: Correct

**Claim**: The Riders are level 30.
- **Spoiler line**: 1657
- **Source ref**: `include/monsters.h:3144` (Death LVL 30),
  `monsters.h:3154` (Pestilence LVL 30), `monsters.h:3164` (Famine LVL 30)
- **Verdict**: Correct

**Claim**: Touch of Death deals 8d6+50 and drains half the damage as
max-HP.
- **Spoiler line**: 1519-1521
- **Source ref**: `mcastu.c:323-355` — `int dmg = 50 + d(8, 6); int drain = dmg / 2;`
- **Verdict**: Correct
- **Notes**: Permanent max-HP reduction applies. Outright death if
  `drain >= u.uhpmax`.

**Claim**: "Magic resistance does not save you from Touch of Death."
- **Spoiler line**: 1527-1528
- **Source ref**: `mcastu.c:395-407` (`mcast_death_touch` gated by
  `!Antimagic`), `uhitm.c:3837-3884` (`mhitm_ad_deth`)
- **Verdict**: Partially wrong (corrected 2026-05-11)
- **Notes**: MR fully blocks the spell-cast version; on the Death rider's
  touch (rolls 17-19 of 20), MR blocks the full 8d6+50, leaving only
  permdmg life-drain from the default (rolls 5-16). So MR substantially
  mitigates but doesn't fully neutralize the Death rider's attack.

**Claim**: Spheres "explode in a 3x3 area in current editions" (line 1371).
- **Spoiler line**: 1371
- **Source ref**: `explode.c:198-215` — `explmask[3][3]` and "adjacent
  spots are also affected"; `mhitu.c:839-842` invokes `explmu`, which
  in turn calls `explode()` for AD_FIRE/COLD/ELEC.
- **Verdict**: Correct

**Claim**: Gold dragons breathe fire.
- **Spoiler line**: 1430
- **Source ref**: `include/monsters.h:1444` —
  `MON("gold dragon", ..., ATTK(AT_BREA, AD_FIRE, 4, 6), ...)`
- **Verdict**: Correct

### Engravings and alignment

**Claim**: Attacking from Elbereth costs -5 alignment.
- **Spoiler line**: 1285
- **Source ref**: `mon.c:4267-4299` — `if (via_attack && sengr_at("Elbereth",...
  ... adjalign(-5)`
- **Verdict**: Correct

### Tools and items

**Claim**: Unicorn horn cures sickness, blindness, hallucination,
vomiting, confusion, stunning, deafness (deaf new in 5.0). Effectiveness:
blessed can fix up to 7 troubles per apply, uncursed maxes at 3 with
35% no-effect rate; cursed inflicts a random ailment.
- **Spoiler line**: 3111-3128 (rewritten 2026-05-11)
- **Source ref**: `apply.c:2259-2381` `use_unicorn_horn`. Probability
  table is inline in the function comments:
  `blessed: 22.7%/22.7%/19.5%/15.4%/10.7%/5.7%/2.6%/0.8%`
  `uncursed: 35.4%/35.4%/22.9%/6.3%/0/0/0/0`
- **Verdict**: Correct
- **Notes**: The "no longer restores ability scores" caveat is still
  accurate; the horn cures only the seven status ailments listed, never
  drained stats.

**Claim**: Magic marker has 30-99 starting charges; blessed scroll of
charging restores to ≥50 (once only). Scroll write costs: identify 7-13,
enchant 8-15, charging 8-15, magic mapping 4-7, **genocide 15-29**.
Spellbooks 10 × spell level.
- **Spoiler line**: 3132-3155 (rewritten 2026-05-11)
- **Source ref**: `mkobj.c:1025` (`spe = rn1(70, 30)`),
  `read.c:857-880` (charging restoration),
  `write.c:14-57` (cost table by scroll type),
  `write.c:265` (`actualcost = rn1(basecost / 2, basecost / 2)`)
- **Verdict**: Correct
- **Notes**: The earlier spoiler claim "writing identified scrolls costs
  fewer charges" was wrong — `actualcost` depends only on the target
  scroll's basecost, not identification status. **Self-correction
  needed**: in the rewrite I claimed blessed charging gives "two more
  wishes" to a wand of wishing — that's wrong; it gives exactly one
  more wish per recharge (see wand of wishing entry below).

**Claim**: Confused remove curse has "25% chance of blessing or cursing"
each uncursed item.
- **Spoiler line**: 2690
- **Source ref**: `read.c:1556-1561` (uses `blessorcurse(obj, 2)`),
  `mkobj.c:1010-1023` (`blessorcurse` definition: `!rn2(chance)` then
  `!rn2(2)` to choose direction)
- **Verdict**: Correct but ambiguous
- **Notes**: Actual is 25% bless, 25% curse, 50% no change. The phrasing
  "25% of blessing or cursing" could be misread as "25% combined" — but
  the per-direction numbers are right.

### Magic-cancellation / armor

**Claim**: MC3 blocks 90% of monster special attacks (down from 98% in
older editions).
- **Spoiler line**: 3214
- **Source ref**: `uhitm.c:86-87` — `armpro = magic_negation(mdef);
  negated = !(rn2(10) >= 3 * armpro);` → MC3 = `rn2(10) < 9` = 90%
- **Verdict**: Correct (90%); the "98% historical" not verified against
  any older source

### Weapons and combat

**Claim**: Two-handed weapons get a 50% STR damage bonus.
- **Spoiler line**: 3506-3514
- **Source ref**: `uhitm.c:1463-1470` —
  `if (bimanual(uwep)) strbonus = ((3 * absbonus + 1) / 2) * sgn(strbonus);`
  → 3/2 = 1.5x = +50%
- **Verdict**: Correct
- **Notes**: Spoiler states the same fact in two consecutive paragraphs
  (3506 and 3510), minor stylistic redundancy.

**Claim**: Cursed wands may explode when zapped.
- **Spoiler line**: 2154
- **Source ref**: `zap.c:2647` (`obj->cursed && !rn2(WAND_BACKFIRE_CHANCE)`
  → `backfire(obj)`), `hack.h:1410` (`WAND_BACKFIRE_CHANCE = 100`)
- **Verdict**: Correct
- **Notes**: 1/100 chance per zap of a cursed wand. Damage is
  `d(spe + 2, 6)`.

**Claim**: Recharge explosion chances 0.3% / 2.3% / 7.9% / 100% for
recharges 1 / 2 / 3 / 7.
- **Spoiler line**: 2858-2861
- **Source ref**: `read.c:747-762` — inline comment table lists
  `0.29% / 2.33% / 7.87% / 100%` cumulative odds.
- **Verdict**: Correct (spoiler is the same numbers, rounded)
- **Notes**: Formula is `n*n*n > rn2(7*7*7)`. Wand of wishing additionally
  always explodes if `recharged > 0`.

**Claim**: Wand of wishing yields "2-3 wishes with wresting".
- **Spoiler line**: 3644
- **Source ref**: `mkobj.c:1083` (`WAN_WISHING spe = 1` initial),
  `zap.c:2515-2525` (`zappable` and wrest at `rn2(WAND_WREST_CHANCE)`
  with `WAND_WREST_CHANCE = 121`), `read.c:739-792` (recharge: lim = 1
  for WAN_WISHING, gives +1 spe; second recharge always explodes).
- **Verdict**: Defensible
- **Notes**: Initial 1 wish + 1 safe recharge with blessed charging
  scroll + 1/121 wresting chance on each post-empty zap = 2-3 wishes
  realistically achievable. Self-correction: my magic marker section
  said charging gives "two more wishes" — that's wrong (one more).

### Wish sources

**Claim**: Magic lamp rubbed blessed = 80% chance of wish.
- **Spoiler line**: 3074, 3633
- **Source ref**: `apply.c:1816-1834` (rub mechanic: djinni emerges on
  `!rn2(3)` = 1/3 of rubs); `potion.c:2840-2842` (djinni_from_bottle:
  blessed = 80% wish conditional on djinni emerging)
- **Verdict**: Wrong
- **Notes**: 80% is conditional on djinni emerging. True per-rub wish
  chance ≈ 1/3 × 80% = ~27% for blessed. Spoiler conflates the two
  probabilities.

**Claim**: Smoky potion djinni: 20% wish (80% if blessed).
- **Spoiler line**: 3640-3642
- **Source ref**: same `potion.c:2840-2842`
- **Verdict**: Correct
- **Notes**: These are conditional on djinni-emerges, which the spoiler
  separately notes is "1 in 13 base probability."

**Claim**: Fountain ~1 in 30 chance of a wish per quaff.
- **Spoiler line**: 3636
- **Source ref**: `fountain.c:243` `drinkfountain` (`fate = rnd(30)`,
  case 23 = water demon), `fountain.c:64-89` `dowaterdemon` (wish on
  `rnd(100) > 80 + level_difficulty()`)
- **Verdict**: Wrong
- **Notes**: 1/30 is just the water-demon spawn rate. Conditional wish
  from the demon is ~20% on shallow floors (less deeper). True per-quaff
  wish chance is closer to 1/150 (~0.67%).

**Claim**: Vlad's throne: 4 of 13 outcomes are a wish.
- **Spoiler line**: 3626-3629
- **Source ref**: `sit.c:240-255` `special_throne_effect`, cases 1-4 of 13
  each call `makewish()` then disintegrate the throne.
- **Verdict**: Correct

**Claim**: Throne (ordinary): very rare chance of a wish.
- **Spoiler line**: 3638
- **Source ref**: `sit.c:64-110` ordinary throne effects, case 6 calls
  `makewish()` conditional on `u.uluck + rn2(5) >= 0` (so positive Luck
  ≈ guaranteed wish on that branch). 1/13 cases gives ~7.7% per sit.
- **Verdict**: Defensible
- **Notes**: "Very rare" is roughly accurate; spoiler doesn't pin the
  exact %.

**Claim**: Amulet of Yendor grants a wish when first picked up.
- **Spoiler line**: 3631
- **Source ref**: `allmain.c:446-450` —
  `if (u.uhave.amulet && !u.uevent.amulet_wish) { u.uevent.amulet_wish = 1;
  pline("The Amulet is bestowing a wish upon you!"); makewish(); }`
- **Verdict**: Correct

### Cursing and item generation

**Claim**: Rings of teleportation / polymorph / aggravate / hunger and
amulets of strangulation / change / restful sleep generate cursed 90%
of the time.
- **Spoiler line**: 2916, 2928
- **Source ref**: `mkobj.c:1063` (amulets), `mkobj.c:1143` (rings) — both
  use `rn2(10)` (truthy 9/10 = 90% of the time → `curse(otmp)`)
- **Verdict**: Correct

**Claim**: Items on a bones level have an 80% chance of being cursed.
- **Spoiler line**: 3822
- **Source ref**: `bones.c:290` `if (rn2(5)) curse(otmp);` → 4/5 = 80%
- **Verdict**: Correct

### Locks

**Claim**: Skeleton key — 70%+ on doors, 75%+ on boxes.
- **Spoiler line**: 3066
- **Source ref**: `lock.c:299` (boxes: `ch = 75 + ACURR(A_DEX)`),
  `lock.c:639` (doors: `ch = 70 + ACURR(A_DEX)`)
- **Verdict**: Correct (matches base constants exactly)

### Potions and rings

**Claim**: Dipping a potion mix has ~10% explosion chance on non-water
combinations.
- **Spoiler line**: 2583
- **Source ref**: `potion.c:2420-2428` `dip_potion_explosion` —
  `!rn2((uarmc && uarmc->otyp == ALCHEMY_SMOCK) ? 30 : 10)` → 10% base,
  always for cursed/acid/lit-oil
- **Verdict**: Correct
- **Notes**: Wearing alchemy smock reduces it to 1/30.

**Claim**: Throwing a ring down a sink loses it 95% of the time
(searching and slow digestion always returned).
- **Spoiler line**: 2194-2196
- **Source ref**: `do.c:649-664` —
  `!rn2(20)` (5%) returns ring; otherwise `!rn2(5)` (19/100 overall)
  buries it; otherwise (76/100) `useup`. RIN_SEARCHING/SLOW_DIGESTION
  exit early via `goto giveback` at `do.c:510-518`.
- **Verdict**: Correct

---

## 2026-05-11 — second systematic pass

Audit by Claude Opus 4.7. Covered version-change claims, quest artifact
assignments, branch entry levels, weapon damages, artifact bonuses,
specific mechanics flagged after first pass. Source: NetHack 5.0 HEAD.

### Version-change claims

**Claim**: Themed rooms "new in current editions".
- **Spoiler line**: 669
- **Source ref**: `dat/themerms.lua` plus infrastructure in
  `dungeon.c:1003-1071` and `mklev.c:375-389`.
- **Verdict**: Correct (new in 5.0)

**Claim**: Mummies cause withering, curable by prayer.
- **Spoiler line**: 1394
- **Source ref**: `include/monsters.h:1901-1965` — all 9 mummy variants
  have only `ATTK(AT_CLAW, AD_PHYS, ...)` attacks. There is no
  `AD_WTHR` attack type anywhere in the codebase.
- **Verdict**: Wrong
- **Notes**: Mummies in 5.0 deal physical damage only. The "withering"
  mechanic and prayer cure do not exist for mummies.

**Claim**: Mind flayers no longer cause amnesia (only Int drain).
- **Spoiler line**: 1556-1557
- **Source ref**: `uhitm.c:3168-3260` `mhitm_ad_drin` and
  `eat.c:603-700` `eat_brains`. Int drain via `adjattrib(A_INT, -rnd(2))`.
  No `forget_levels`/amnesia call in the AD_DRIN path.
- **Verdict**: Correct
- **Notes**: `detect.c:1189` comment "amnesia no longer causes levels
  to be forgotten" confirms the broader retcon.

**Claim**: Black dragon scale mail grants drain resistance ("new in
current editions").
- **Spoiler line**: 1582
- **Source ref**: `do_wear.c:810-815`:
  `case BLACK_DRAGON_SCALES: case BLACK_DRAGON_SCALE_MAIL:
  EDrain_resistance |= W_ARM;` and the corresponding takeoff clears it.
- **Verdict**: Correct
- **Notes**: This is in addition to the disintegration resistance the
  scale mail provides via the `DRGN_ARMR(... DISINT_RES ...)` macro.

**Claim**: Engulfment "wraps and crushes rather than digesting" in
current editions.
- **Spoiler line**: 1613-1614
- **Source ref**: `mhitu.c:1289-1340` `gulpmu` — message varies by
  engulfer type. For lurker above/trapper (enfolders) the message is
  "folds itself around you"; for digesters "swallows you whole"; for
  amorphous (Juiblex) "oozes" or "engulfs". The 5.0 code already
  treats lurkers/trappers as enfolders, not digesters.
- **Verdict**: Defensible
- **Notes**: Editorial paraphrase. The mechanic is real (different
  engulfer types behave differently) but "wraps and crushes" is the
  spoiler's framing, not the literal code text.

**Claim**: Pestilence/Famine "mercy in current editions" — second-attack
becomes less severe.
- **Spoiler line**: 1665
- **Source ref**: `mhitu.c` second-attack downgrade —
  `if (... && (attk->adtyp == AD_DISE || AD_PEST || AD_FAMN) &&
  attk->adtyp == mptr->mattk[indx - 1].adtyp) { attk->adtyp = AD_STUN; }`
- **Verdict**: Correct
- **Notes**: Riders' subsequent attacks of the same type on the same
  turn drop to AD_STUN rather than compound the disease/pest/famine.

**Claim**: Helm of caution "new in current editions" — grants warning.
- **Spoiler line**: 3189
- **Source ref**: `include/objects.h:479-481`
  (`HELM("helm of caution", "etched helmet", ... WARNING, ...)`),
  `do_wear.c:448` (`case HELM_OF_CAUTION: see_monsters(); break;`)
- **Verdict**: Correct

**Claim**: Wand of speed monster "no longer grants permanent speed
when self-zapped".
- **Spoiler line**: 2543
- **Source ref**: `zap.c` (self-zap case for WAN_SPEED_MONSTER):
  `case WAN_SPEED_MONSTER: /* no longer gives intrinsic, but gives
  very fast speed instead */ speed_up(rn1(25, 50));`
- **Verdict**: Correct (the code comment confirms the change)

### Quest artifacts (role.c)

**Claim**: Valkyrie → Orb of Fate.
- **Spoiler line**: 916
- **Source ref**: `role.c:516` `ART_ORB_OF_FATE`.
- **Verdict**: Correct

**Claim**: Wizard → Eye of the Aethiopica.
- **Spoiler line**: 917
- **Source ref**: `role.c:556` `ART_EYE_OF_THE_AETHIOPICA`.
- **Verdict**: Correct

**Claim**: Tourist → Platinum Yendorian Express Card.
- **Spoiler line**: 918
- **Source ref**: `role.c:476` `ART_YENDORIAN_EXPRESS_CARD`;
  `artilist.h: A("The Platinum Yendorian Express Card", ...)`.
- **Verdict**: Correct

**Claim**: Monk → Eyes of the Overworld (lenses).
- **Spoiler line**: 3325-3326
- **Source ref**: `role.c:257` `ART_EYES_OF_THE_OVERWORLD`;
  `artilist.h: A("The Eyes of the Overworld", LENSES, ...)`.
- **Verdict**: Correct

**Claim**: Mitre of Holiness is a classic source of drain resistance.
- **Spoiler line**: 1581
- **Source ref**: `artilist.h:265-269` Mitre entry has `NO_DFNS`. The
  artifacts that defend against `AD_DRLI` (drain) are Excalibur
  (PHYS attack + DRLI defense), Stormbringer (DRLI attack + DRLI
  defense), and Staff of Aesculapius (DRLI defense).
- **Verdict**: Wrong
- **Notes**: Mitre grants fire resistance (carry), energy boost
  (invoke), and bonus damage vs undead — not drain resistance.
  Correct list of drain-resistance sources: Excalibur, Stormbringer,
  Staff of Aesculapius, and black dragon scale mail.

### Artifact damage bonuses (artilist.h)

The general formula in `artifact.c:1090-1106` (`spec_dbon`) treats
`damn` as the bonus-to-hit roll (`rnd(damn)`) and `damd` as the
bonus-damage roll (`rnd(damd)`). So `PHYS(5, 10)` = +d5 to hit, +d10
to damage.

**Claim**: Excalibur "+d5 to hit and damage".
- **Spoiler line**: 3305
- **Source ref**: `artilist.h: A("Excalibur", ..., PHYS(5, 10), ...)`
- **Verdict**: Wrong (damage portion)
- **Notes**: +d5 to hit is correct, +d10 to damage (not +d5).

**Claim**: Grayswandir "+d5 to hit and damage, double damage dealt".
- **Spoiler line**: 3309
- **Source ref**: `artilist.h: A("Grayswandir", ..., PHYS(5, 0), ...)`
- **Verdict**: Partially wrong
- **Notes**: +d5 hit is correct, but `damd=0` means no extra-damage
  roll on top of base silver saber damage; the "double damage dealt"
  claim relates to the silver-against-undead bonus, not a separate
  doubling mechanic. Worth re-checking.

**Claim**: Mjollnir "+d5 hit and +d24 damage; returns at STR 25".
- **Spoiler lines**: 3313-3314 (and 238)
- **Source refs**: `artilist.h: A("Mjollnir", ..., ELEC(5, 24), ...)`;
  `dothrow.c:127, 327` checks `ACURR(A_STR) >= STR19(25)`;
  `include/attrib.h: STR19(x) = 100 + x`.
- **Verdict**: Correct

**Claim**: Magicbane "+d3 to hit and damage".
- **Spoiler line**: 3317
- **Source ref**: `artilist.h: A("Magicbane", ..., STUN(3, 4), ...)`
- **Verdict**: Partially wrong
- **Notes**: +d3 hit is correct, +d4 damage (not +d3).

**Claim**: Stormbringer "+d5 to hit and damage".
- **Spoiler line**: 3321
- **Source ref**: `artilist.h: A("Stormbringer", ..., DRLI(5, 2), ...)`
- **Verdict**: Partially wrong
- **Notes**: +d5 hit is correct, +d2 damage (not +d5).

**Claim**: Misaligned intelligent artifact rejection = 8d6 damage.
- **Spoiler line**: 3298
- **Source ref**: `artifact.c:947-952` `touch_artifact` —
  `dmg = d((Antimagic ? 2 : 4), (self_willed ? 10 : 4));`
  → 4d10 for self-willed (intelligent) when not magic-resistant.
- **Verdict**: Wrong
- **Notes**: Actual is 4d10 (range 4-40), not 8d6 (range 8-48).
  The non-intelligent value of 4d4 in the spoiler is correct.

**Claim**: Non-intelligent misaligned artifact rejection = 4d4 damage,
1/4 chance.
- **Spoiler line**: 3300
- **Source ref**: same `touch_artifact:947` plus the condition
  `(badalign && (!yours || !rn2(4)))` for non-self-willed artifacts.
- **Verdict**: Correct

### Branch / dungeon entry levels

**Claim**: Gnomish Mines at "level 2-4".
- **Spoiler line**: 541
- **Source ref**: `dat/dungeon.lua`: Mines `base = 2, range = 3`.
- **Verdict**: Correct

**Claim**: Sokoban branch around dungeon levels 5-9.
- **Spoiler line**: 545
- **Source ref**: `dat/dungeon.lua`: Sokoban `chainlevel = "oracle",
  base = 1, direction = "up"`; Oracle is `base = 5, range = 5` → 5-9.
  Sokoban entrance is one level above Oracle, so 6-10.
- **Verdict**: Slightly off
- **Notes**: Entrance is on levels 6-10, not 5-9.

**Claim**: Quest portal "around level 11-16".
- **Spoiler line**: 548
- **Source ref**: `dat/dungeon.lua`: Quest `chainlevel = "oracle",
  base = 6, range = 2`. Oracle 5-9 + 6-7 = 11-16... wait, base = 6
  range = 2 means Oracle level + (6..7), so 11-15 (Oracle 5 + 6 = 11
  through Oracle 9 + 6 = 15; range 2 = base..base+1).
- **Verdict**: Slightly off
- **Notes**: 11-15, not 11-16. Off by one at the upper end.

**Claim**: Quest minimum experience level 14.
- **Spoiler line**: 911
- **Source ref**: `include/quest.h:45 #define MIN_QUEST_LEVEL 14`.
- **Verdict**: Correct

### Sokoban prize

**Claim**: Sokoban top prize is bag of holding or amulet of reflection.
- **Spoiler lines**: 891-893
- **Source ref**: `dat/soko1-1.lua:103-109` and `soko1-2.lua:106-112` —
  both variants use `if percent(75) then bag-of-holding else
  amulet-of-reflection end`.
- **Verdict**: Correct (item list)

**Claim**: "Which prize you get is weighted by the level variant".
- **Spoiler line**: 893
- **Source ref**: Same as above — both variants use the same 75/25
  weighting; variant has no effect on which prize spawns.
- **Verdict**: Wrong
- **Notes**: The weighting is per-roll (75% bag, 25% amulet),
  independent of the level variant.

### Mine's End

**Claim**: "One of its level variants contains a guaranteed luckstone".
- **Spoiler line**: 874
- **Source ref**: `minend-1.lua:77`, `minend-2.lua:116`, `minend-3.lua:67`
  — all three variants place a guaranteed luckstone with
  `achievement=1` flag.
- **Verdict**: Misleading
- **Notes**: All three Mine's End variants have the luckstone, not
  just one. The luckstone is always present at Mine's End.

### Other 5.0 mechanics

**Claim**: Wraith corpse grants an experience level.
- **Spoiler line**: 2475
- **Source ref**: `eat.c:1141` `case PM_WRAITH: pluslvl(FALSE);`
- **Verdict**: Correct

**Claim**: Restful sleep amulet grants "+1 HP/turn regen while asleep".
- **Spoiler line**: 2977
- **Source ref**: `allmain.c:621` `#define U_CAN_REGEN() (Regeneration
  || (Sleepy && u.usleep))`; `allmain.c:660-665`:
  base regen chance `(XL + CON > rn2(100))` plus `+1` from
  `U_CAN_REGEN()` plus `+1` from explicit `Sleepy && u.usleep` check.
- **Verdict**: Approximately correct (slightly understates)
- **Notes**: While asleep wearing restful sleep, you get +1 from
  U_CAN_REGEN and another +1 from the explicit Sleepy check =
  effectively +2 HP/turn on top of the base regen chance.

**Claim**: HP regeneration uses formula (experience level +
Constitution)% chance per turn.
- **Spoiler line**: 5512-5514
- **Source ref**: `allmain.c:660` —
  `heal = (u.ulevel + (int)ACURR(A_CON)) > rn2(100);`. With
  Regeneration intrinsic, an unconditional +1 HP is also granted.
- **Verdict**: Correct

**Claim**: Tsurugi damage d16 / d8+2d6, Battle-axe d8+d4 / d6+2d4.
- **Spoiler lines**: 3236-3238
- **Source refs**: `objects.h: WEAPON("tsurugi", ... 16, 8, ...)`;
  `WEAPON("battle-axe", ... 8, 6, ...)`. `weapon.c:255-261` adds
  `d(2, 6)` to TSURUGI vs large; `weapon.c:283-291` adds `rnd(4)`
  to BATTLE_AXE for the base + `d(2, 4)` vs large.
- **Verdict**: Correct

---

## 2026-05-11 — third systematic pass

Audit by Claude Opus 4.7. Triggered by question about whether Orcus-town
is a real special level. Pass focused on: location/place-name verification
(is X a real special level?), gameplay-number checks not yet covered
(food, prayer, corpse rotting), and re-verification of recently-edited
section's factual claims. NetHack 5.0 source HEAD.

### Locations / special levels

**Claim**: Orcus-town is a real place; lamp or marker guaranteed there.
- **Spoiler lines**: 3678, 4075, 4132-4140, 5511
- **Source refs**:
  - `dat/orcus.lua` — level layout file exists.
  - `dat/dungeon.lua:150` — registered `name = "orcus"` in Gehennom.
  - `include/hack.h:401` — `orcus_level` location tracked.
  - `src/shknam.c:794-797` — comment "Hack for Orcus's level: it's a
    ghost town, get rid of shopkeepers" + the actual `mongone(mtmp)`
    call confirms the ghost-town design.
  - `dat/orcus.lua:106-110` — 50/50 random pick between `"magic marker"`
    and `"magic lamp"` placement, with code comment "An object that's
    worth most of a wish (this is part of the compensation for the
    reduced wishes at the Castle)".
- **Verdict**: Correct

**Claim**: Fort Ludios is a real branch.
- **Spoiler lines**: 529, 551, 931-946
- **Source refs**: `dat/knox.lua` + `dat/dungeon.lua:248-255` (branch
  registered with map `"knox"`); `src/botl.c:449` `Is_knox()`.
- **Verdict**: Correct

**Claim**: Astral Plane has three altars (one per alignment).
- **Spoiler lines**: 571, 4173 (Astral pilgrimage)
- **Source ref**: `dat/astral.lua:89-91` —
  `des.altar({ x=07, y=09, align=align[1], type="sanctum" })` and two
  more for align[2] and align[3].
- **Verdict**: Correct

**Claim**: Moloch's Sanctum is the bottom of Gehennom.
- **Spoiler lines**: 534, 564
- **Source ref**: `dat/sanctum.lua` exists; `dat/dungeon.lua:111`
  registers `name = "sanctum"` at the bottom of Gehennom.
- **Verdict**: Correct

**Claim**: The Wizard's Tower contains the Book of the Dead.
- **Spoiler line**: 562
- **Source refs**: `dat/dungeon.lua:133` registers level `"wizard1"`
  (no explicit "Wizard's Tower" string in code, but the spoiler's name
  is reasonable for player-facing prose); `dat/wizard1.lua:60` places
  `des.object("Book of the Dead", 16, 05)`.
- **Verdict**: Correct

**Claim**: Vlad's Tower contains the Candelabrum.
- **Spoiler line**: 3084
- **Source refs**: `dat/dungeon.lua: Vlad's Tower` branch registered;
  `src/makemon.c:1353-1354` —
  `if (mndx == PM_VLAD_THE_IMPALER) mitem = CANDELABRUM_OF_INVOCATION;`
  plus the explicit comment a few lines down "Vlad stays in his normal
  shape so he can carry the Candelabrum".
- **Verdict**: Correct
- **Notes**: Vlad himself (in `dat/tower1.lua:113`) carries the
  candelabrum — not placed on the floor.

### Eating mechanics

**Claim**: Food ration = 800 nutrition.
- **Spoiler line**: 345
- **Source ref**: `objects.h:1111` —
  `FOOD("food ration", 380, 5, 20, 0, VEGGY, 800, ...)` — the 800
  field is nutrition per FOOD macro definition.
- **Verdict**: Correct

**Claim**: Lembas wafer = 800 nutrition at only 5 weight.
- **Spoiler line**: 2435
- **Source ref**: `objects.h:1107` —
  `FOOD("lembas wafer", 20, 2, 5, 0, VEGGY, 800, ...)` — fields are
  (name, prob, delay, weight, unk, foodtype, nutrition, ...). So
  weight = 5, nutrition = 800.
- **Verdict**: Correct
- **Notes**: Delay-to-eat is 2 turns (the "2" field), weight is 5.

**Claim**: Lichen and Lizard corpses never rot.
- **Spoiler lines**: 420-421
- **Source refs**: `eat.c:59` macro checks `PM_LIZARD || PM_LICHEN`;
  `mkobj.c:1403` `if (body->corpsenm == PM_LIZARD || PM_LICHEN)`
  bypasses the normal age timer; `mkobj.c:2053` similar guard.
- **Verdict**: Correct

**Claim**: Lizard corpse cures stoning in progress.
- **Spoiler lines**: 1462, 1492
- **Source ref**: `eat.c:827-829` — `case PM_LIZARD: if (Stoned)
  fix_petrification(); break;`
- **Verdict**: Correct

### Prayer

**Claim**: Pray about once every 300-500 turns.
- **Spoiler line**: 435
- **Source ref**: `pray.c:1356` `u.ublesscnt = rnz(350);` plus
  additional `rnz(1000)` increments for Demigod / Hand of Elbereth
  status. `rnz()` returns roughly base/2 to 2x base.
- **Verdict**: Approximately correct
- **Notes**: Base cooldown after a successful prayer is `rnz(350)` —
  roughly 175-700 turns (typically clustered near 350). The
  300-500 range in the spoiler is a reasonable rule of thumb but
  the actual variance is wider.

**Claim**: Successful prayer raises the prayer timeout to at least
1000 turns.
- **Spoiler line**: 3506
- **Source ref**: `pray.c:1360-1362` adds `rnz(1000)` per
  Demigod / Hand-of-Elbereth status; for a basic successful prayer
  `rnz(350)` is the base. The "at least 1000" claim is more
  appropriate for elevated-status prayers.
- **Verdict**: Approximately correct (caveat about status applies)

### Boulders / Sokoban

**Claim**: Squeezing past boulders costs a point of luck each time.
- **Spoiler line**: 903 (in Sokoban context)
- **Source ref**: `hack.c:401-404` —
  `You("squeeze yourself %s the boulder."); sokoban_guilt();`
  `trap.c:7042-7045` `sokoban_guilt`:
  `u.uconduct.sokocheat++; change_luck(-1);` — guarded by `Sokoban`,
  so only happens inside Sokoban.
- **Verdict**: Correct (in Sokoban context)
- **Notes**: Important caveat — the luck penalty is Sokoban-only.
  Outside Sokoban, squeezing past boulders has no luck cost. The
  spoiler is in the Sokoban section so the context is right.

### Items and artifacts (additional checks)

**Claim**: Mine's End luckstone is always uncursed.
- **Spoiler line**: 2304
- **Source refs**: All three Mine's End variant files explicitly
  mark the luckstone `buc="not-cursed"`:
  - `dat/minend-1.lua:77` (also has a mimic decoy)
  - `dat/minend-2.lua:116`
  - `dat/minend-3.lua:67`
- **Verdict**: Correct
- **Notes**: `buc="not-cursed"` means it can be blessed or uncursed
  (just never cursed). The "uncursed" rule of thumb holds.

**Claim**: Demonbane is a silver mace and Priest's first sacrifice gift.
- **Spoiler lines**: 192, 3324, 5543, 5644
- **Source refs**: `artilist.h: A("Demonbane", SILVER_MACE, ...,
  A_LAWFUL, PM_CLERIC, ...)`. The CLERIC role and SILVER_MACE base
  confirm both parts of the claim.
- **Verdict**: Correct

### Summary

3rd pass focused on the kinds of claims that 1st and 2nd passes
exposed as fragile: place names, gameplay specifics, items.
Of 14 newly-checked claims, all 14 are correct or approximately
correct. No new corrections needed.

---

## Artifact-table expansion pass (2026-05-12)

The "Key Artifacts" table had 14 of 34 artifacts (5.0 ships 33 active
entries; one is the STRANGE_OBJECT terminator and one — Palantir of
Westernesse — is `#if 0`'d out). Three big gaps:

1. The six "bane" weapons (Grimtooth, Dragonbane, Werebane,
   Giantslayer, Ogresmasher, Trollsbane) weren't in the table at all.
2. Cleaver's three-square spin attack wasn't mentioned anywhere.
3. The 13 quest artifacts only appeared as a single comma-separated
   prose line at the end of the section.

This pass verifies each of those facts against `artilist.h` and
relevant code, then expands the table.

**Claim**: Grimtooth = orcish dagger, anti-elf, poison defense.
- **Source**: `artilist.h:123-132` `A("Grimtooth", ORCISH_DAGGER,
  (SPFX_RESTR | SPFX_WARN | SPFX_DFLAG2), 0, M2_ELF, PHYS(2, 6),
  DFNS(AD_DRST), ...)`. PHYS(2,6) → +d2 to-hit, +d6 damage. Chaotic.
- **Verdict**: Correct (added).

**Claim**: Dragonbane = broadsword, vs S_DRAGON, grants reflection.
- **Source**: `artilist.h:157-160` `A("Dragonbane", BROADSWORD,
  (SPFX_RESTR | SPFX_DCLAS | SPFX_REFLECT), 0, S_DRAGON, PHYS(5, 0),
  ...)`. SPFX_REFLECT is in the s1 (wield-flag) bitset.
- **Verdict**: Correct (added).

**Claim**: Werebane = silver saber, vs M2_WERE, defends vs AD_WERE.
- **Source**: `artilist.h:166-168` `A("Werebane", SILVER_SABER,
  (SPFX_RESTR | SPFX_DFLAG2), 0, M2_WERE, PHYS(5, 0), DFNS(AD_WERE),
  ...)`.
- **Verdict**: Correct (added).

**Claim**: Giantslayer = long sword, Neutral, vs M2_GIANT.
- **Source**: `artilist.h:174-176` `A("Giantslayer", LONG_SWORD,
  (SPFX_RESTR | SPFX_DFLAG2), 0, M2_GIANT, PHYS(5, 0), ...,
  A_NEUTRAL, ...)`.
- **Verdict**: Correct (added).

**Claim**: Ogresmasher = war hammer, vs S_OGRE.
- **Source**: `artilist.h:178-180` `A("Ogresmasher", WAR_HAMMER,
  (SPFX_RESTR | SPFX_DCLAS), 0, S_OGRE, PHYS(5, 0), ...)`.
- **Verdict**: Correct (added).

**Claim**: Trollsbane = morning star, vs S_TROLL, regeneration.
- **Source**: `artilist.h:182-184` `A("Trollsbane", MORNING_STAR,
  (SPFX_RESTR | SPFX_DCLAS | SPFX_REGEN), 0, S_TROLL, PHYS(5, 0),
  ...)`. SPFX_REGEN is in the wield-flag set (effective while wielded).
- **Verdict**: Correct (added).

**Claim**: Bane weapons deal "×2 base" damage on a class match.
- **Source**: `artifact.c:1091` (`spec_dbon`): returns `rnd(damd)` if
  the artifact has a positive `damd` extra-damage die; otherwise
  returns `max(tmp, 1)` where `tmp` is the *base weapon's* damage
  roll. For weapons with `damd == 0` (every bane weapon except
  Grimtooth, which has its own +d6), this effectively doubles the
  base damage against a matching target. Grimtooth has PHYS(2,6), so
  it still benefits from the +d6 extra against elves *plus* the
  doubled base — i.e. base + base + d6.
- **Verdict**: Mechanics documented correctly in the new table prose.

**Claim**: Cleaver hits two flanking squares when wielded
one-handed.
- **Source**: `uhitm.c:766` comment `/* Cleaver attacks three spots,
  'mon' and one on either side of 'mon'. */` and the code at lines
  766-..., gated on `u_wield_art(ART_CLEAVER) && !u.twoweap`. So
  two-weapon configuration *suppresses* the spin. Added to the table
  notable column and called out in narrative.
- **Verdict**: Correct (added).

**Claim**: Palantir of Westernesse is not active in 5.0.
- **Source**: `artilist.h:237-246` is bracketed by `#if 0 ... #endif`
  with a comment block explaining the Elf role was retired in 3.3
  and the artifact "is a bit overpowered to be an ordinary artifact
  so leave it excluded". So 5.0 has exactly 13 quest artifacts, not
  14.
- **Verdict**: Adjusted the spoiler narrative to mention this rather
  than implying a 14th race artifact exists.

**Claim**: Quest artifact damage formulas and passives.
- **Source**: `artilist.h:219-307`. Each row in the new quest-artifact
  table was traced individually:
  - Orb of Detection: CARY(AD_MAGM) + SPFX_ESP + SPFX_HSPDAM, INVIS.
  - Heart of Ahriman: SPFX_LUCK (via the luckstone otyp), SPFX_STLTH,
    LEVITATION, with the explicit comment "this stone does double
    damage if used as a projectile weapon" (artilist.h:227).
  - Sceptre of Might: PHYS(5,0), SPFX_DALIGN (×2 vs different align),
    DFNS(AD_MAGM), CONFLICT.
  - Staff of Aesculapius: DRLI attack & defense (drain-resistance),
    SPFX_REGEN, HEALING invoke.
  - Magic Mirror of Merlin: CARY(AD_MAGM) + SPFX_ESP + SPFX_SPEAK,
    no invoke.
  - Eyes of the Overworld: DFNS(AD_MAGM), SPFX_XRAY, ENLIGHTENING.
  - Mitre of Holiness: SPFX_DFLAG2 vs M2_UNDEAD, SPFX_PROTECT,
    CARY(AD_FIRE), ENERGY_BOOST. No drain resistance — corrected
    elsewhere in 2nd-pass audit.
  - Longbow of Diana: PHYS(5,0), SPFX_REFLECT + SPFX_ESP, CREATE_AMMO.
  - Master Key of Thievery: SPFX_WARN + SPFX_TCTRL + SPFX_HPHDAM,
    UNTRAP. Comment at artilist.h:276-278 documents the extra
    `#untrap` bonus when curse state matches role.
  - Tsurugi of Muramasa: PHYS(0,8), SPFX_BEHEAD, SPFX_LUCK,
    SPFX_PROTECT.
  - Platinum Yendorian Express Card: CARY(AD_MAGM) + SPFX_ESP +
    SPFX_HSPDAM, CHARGE_OBJ invoke.
  - Orb of Fate: SPFX_LUCK + SPFX_WARN + SPFX_HSPDAM + SPFX_HPHDAM,
    LEV_TELE invoke.
  - Eye of the Aethiopica: DFNS(AD_MAGM) + SPFX_EREGEN + SPFX_HSPDAM,
    CREATE_PORTAL.
- **Verdict**: All 13 entries match.

### Summary

Expanded the artifact section from 14 rows + a comma-list to a full
20-row wishable/random table plus a 13-row quest table with per-
artifact discussion. The 6 bane weapons and Cleaver's spin attack
were entirely new content; the quest artifacts were upgraded from
prose-list to first-class table + per-role notes. Numbers and
passives traced through `artilist.h`, `artifact.c`, and `uhitm.c`.

---

## 2026-05-17 — Chapter audit #1: The Scroll Rack

Source: `spoilers/companion.md` lines 3211-3308 (98 lines)
Verified 26 claims; 2 corrected; 0 flagged for human review.

### Verified correct
- All scroll prices in the price table (21 entries) match `objects.h` SCROLL macros.
- Identify scroll: blessed gives `rn2(5)` items (0=all, 1-4 fixed), with `if cval==1 && sblessed && Luck>0` bumping to 2 — minimum is "all" or 2 — `read.c:2085` seffect_identify.
- Identify scroll multi-item count for blessed+Luck — `read.c:2087-2089`.
- Remove curse: uncursed → worn/wielded only; blessed → entire inventory — `read.c:1488-1555` seffect_remove_curse (`if (sblessed || wornmask || ...)` gate).
- Magic mapping: blessed reveals secret doors — `read.c:1750+` `if (sblessed) { coordxy x, y;` (then reveals SDOORs).
- Scare monster: drop-and-stand creates a scare zone — `monmove.c:onscary` `if (sobj_at(SCR_SCARE_MONSTER, x, y)) return TRUE`.
- Scare monster: pickup degradation — `pickup.c:1832-1862`. Blessed → unbless (preserved). Uncursed+spe=0 → spe bumps to 1 (preserved). Cursed OR spe≠0 → "scroll turns to dust as you pick it up", `useupf`. So fresh-uncursed survives one drop-pickup cycle; blessed survives two; cursed crumbles immediately.
- Teleportation: cursed or confused → level teleport; uncursed → on-level scrolltele — `read.c:1297-1320` seffect_teleportation.
- Genocide: blessed → whole class; uncursed → species; confused → own species (suicide) — `read.c:1731+` seffect_genocide.
- Confused destroy armor: cursed scroll → erodeproof; uncursed → strip erodeproofing — `read.c:1330-1350`. Spoiler glosses this as "erodeproofs" which is the cursed-only outcome but the more memorable one.
- Confused enchant armor / weapon: uncursed → erodeproof; cursed → strip — `read.c:1135+` (armor) and `read.c:1639+` (weapon).
- Confused remove curse: 25% bless, 25% curse, 50% unchanged per uncursed item — `read.c:1555` `blessorcurse(obj, 2)` + `mkobj.c blessorcurse` (1/2 chance of any change, then 1/2 bless vs curse).

### Corrected
1. **Enchant weapon/armor "+5 destruction, blessed safe to +7"** — WRONG.
   - Spoiler claim: "enchanting beyond +5 risks destroying the item entirely, but blessed scrolls can safely push to +7"
   - C source: `read.c:1180-1190` armor destruction fires when `spe > (special_armor ? 5 : 3) && rn2(s)`. Normal armor threshold is +3, not +5. Special (elven/Cornuthaum) is +5. Blessed does NOT bypass the destruction check. Weapons: `read.c:1668-1672` doesn't destroy at all — it just stops responding past +9 (1-in-spe chance of +1, otherwise no effect).
   - Fix: Reworded to give actual mechanic; specify +3/+5 destruction thresholds for armor, explain weapon "stops responding" behavior, drop "blessed safely to +7" false claim.

2. **Charging "second recharge pushes luck, third usually fatal"** — WRONG.
   - Spoiler claim: "The second recharge is pushing your luck; the third is usually fatal."
   - C source: `read.c:recharge` documents the n³/7³ chance: n=1 → 0.29%, n=2 → 2.33%, n=3 → 7.87%, n=4 → 18.66%, n=5 → 36.44%, n=6 → 62.97%, n=7 → 100%. So second recharge is 2.3%, not "pushing your luck"; third is 7.87%, not "usually fatal". Wand of wishing IS special: `obj->otyp == WAN_WISHING` short-circuits to always-explode on any recharge after the first.
   - Fix: Quoted the n³/7³ table directly, noted wand of wishing's special case (explodes 100% on second recharge, so do it exactly once).

### Notes
- "Always at least two with positive Luck" wording for blessed identify is technically true (minimum is 2 when cval rolls to 1 and gets bumped; 0=all is also possible). Could be tightened to "blessed identify with positive luck always reveals at least 2 items, sometimes more, sometimes everything" but the current wording is close enough.
- Scare monster "Pick it up after it's been dropped and it crumbles to dust": true with caveats — depends on BUC and prior pickup history. Cursed crumbles first time; uncursed survives one pickup; blessed survives two. The takeaway (don't pick it up casually) is right; the precise timing is glossed.

---

## 2026-05-17 — Chapter audit #2: A Practical Identification Strategy → Naming What You've Learned

Source: `spoilers/companion.md` lines 2898-2909 (12 lines)
Verified 5 claims; 1 corrected; 0 flagged for human review.

### Verified
- `#name` extended command exists — `cmd.c:1773` `{ M('n'), "name", "same as call ...", docallcmd, ... }`.
- Class-naming applies to all items of the same random appearance — `do_name.c:533-588` (`'o'` case in `docallcmd`); appearance stored in `objects[obj->otyp].oc_uname`.
- Re-calling overwrites prior name — `do_name.c:660-672` `docall()` frees old `*uname_p` and stores new `dupstr(buf)`.
- "fizzy" is a real randomized potion descriptor — `objects.h:1167` `POTION("sickness", "fizzy", ...)`.

### Corrected
1. **`#name` keystroke `N`** — partial. `cmd.c:2768` binds `N` to name in the default cmd table, but `reset_commands` at `cmd.c:3433-3473` immediately reassigns the uppercase forms of dir-keys (Y, K, U, L, N, J, B, H) to MV_RUN movement when not in `number_pad` mode (which is the default vi-keys layout). So `N` only invokes name when `number_pad` is enabled. The reliable shortcut across layouts is `C` (cmd.c:1687 `{ 'C', "call", ... }` — same `docallcmd` entry point).
   - Fix: changed parenthetical to "use the `#name` command (or `C` for the equivalent `#call` menu)".

### Notes
- Example uses `=` inside the player-supplied name; `getlin()`/`mungspaces()` accept arbitrary text per `do_name.c:651-672`, so no issue.

---

## 2026-05-17 — Chapter audit #3: Bestiary Tables → Trolls `T`

Source: `spoilers/companion.md` lines 7886-7902 (17 lines)
Verified 17 claims; 0 corrected; 0 flagged. One wording tightening applied.

### Verified
- All five troll rows match `monsters.h:2225-2266` exactly (color, level, speed, AC, MR%, attacks):
  - troll: CLR_BROWN, LVL(7,12,4,0,-3), AT_WEAP 4d2 + AT_CLAW 4d2 + AT_BITE 2d6
  - ice troll: CLR_WHITE, LVL(9,10,2,20,-3), with AT_CLAW AD_COLD + MR_COLD
  - rock troll: CLR_CYAN, LVL(9,12,0,0,-3)
  - water troll: CLR_BLUE, LVL(11,14,4,40,-3), M1_SWIM
  - Olog-hai: CLR_MAGENTA (HI_LORD per color.h:38), LVL(13,12,-4,0,-7)
- All trolls regenerate — M1_REGEN on all five.
- All trolls follow stairs — M2_STALK on all five.
- Corpses revive on old levels — `is_reviver` switch at `mon.c:830-831`; revive timer set in `mkobj.c:1416-1421` via `TROLL_REVIVE_CHANCE`.

### Wording tightened
- "Eat the corpse, burn it with fire, or zap it with magic to keep it dead" — "zap with magic" was vague; what really keeps trolls dead is corpse destruction. Rewrote to: "destroy the corpse: eat it, burn it (fire wand/spell, lava), drop it into water, or use force-bolt/striking on it. Stoning the troll leaves a statue, not a corpse, so it never revives."

---

## 2026-05-17 — Chapter audit #4: Bestiary Tables → Liches `L`

Source: `spoilers/companion.md` lines 7750-7763 (14 lines)
Verified 12 claims; 3 corrected; 0 flagged.

### Verified
- All four lich rows match `monsters.h:1864-1897` exactly (color, level, speed, AC, MR%, attacks, resistances):
  - lich: CLR_BROWN, LVL(11,6,0,30,-9)
  - demilich: CLR_RED, LVL(14,9,-2,60,-12)
  - master lich: CLR_MAGENTA (HI_LORD), LVL(17,9,-4,90,-15), MR_FIRE added
  - arch-lich: CLR_MAGENTA, LVL(25,9,-6,90,-15), MR_FIRE | MR_ELEC added
- All liches regenerate (M1_REGEN), are undead (M2_UNDEAD), cold/sleep/poison resistant (MR_COLD | MR_SLEEP | MR_POISON).
- Magic resistance defeats arch-lich death-spell — `mcastu.c:389` `mcast_death_touch` is blocked by Antimagic.

### Corrected
1. **"have poisonous corpses"** — WRONG. All four lich `MON()` entries carry `G_NOCORPSE` flag (`monflag.h:201` = "no corpse left ever"). Liches leave no corpse at all, so the corpse can't be poisonous because it doesn't exist.
   - Fix: "leave no corpse" instead of "have poisonous corpses".
2. **"Higher tiers cast double-trouble"** — WRONG. `MCAST_CLONE_WIZ` is in the wizard spell list but `mcast_clone_wiz()` at `mcastu.c:411-418, 940-944` is gated on `mtmp->iswiz`. Only the Wizard of Yendor casts Double Trouble. Liches cannot.
   - Fix: dropped from prose; master-lich note rewritten to "Draws from the wizard spell list".
3. **Arch-lich "Casts death rays"** — IMPRECISE. The mechanic is `MCAST_DEATH_TOUCH` (touch of death), not a death ray. Per `mcastu.c:320` comment: "unlike the finger of death spell which behaves like a wand of death".
   - Fix: "Casts touch of death; magic resistance mandatory".

### Notes
- "spell spell" attack notation matches the project's bestiary convention (AT_MAGC AD_SPEL 0d0).
- "Skeletal" is conventional flavor; liches are flagged M1_HUMANOID + M2_UNDEAD + M2_MAGIC (no S_SKELETON involvement).

---

## 2026-05-17 — Audit #2 follow-up correction

Reader feedback (mrkelee/user): `#call` is not equivalent to `#name`.
Although both invoke `docallcmd` in 5.0 src, the conventional usage
differs and the spoiler shouldn't equate them. Reverted the parenthetical
to just "use the `#name` command".

---

## 2026-05-17 — Chapter audit #5: Points of Interest

Source: `spoilers/companion.md` lines 687-841 (155 lines)
Verified 40+ claims; 5 corrected; 4 flagged for human review.

### Verified
- Fountain quaff outcomes match `fountain.c:drinkfountain`: water demon, healing, attribute change, snakes, see-invisible, "cool draught" nothing-message.
- Wish source is water demon path — `fountain.c:69-85` "Grateful for %s release, %s grants you a wish!"
- Excalibur conditions: Lawful, XL ≥ 5, Knight 1/6 vs others 1/30 — `fountain.c:404-447`.
- Altar drop-flash: amber = blessed, black = cursed, no flash = uncursed — `do.c:379-389` (`hcolor(obj->blessed ? NH_AMBER : NH_BLACK)`).
- Throne 1/3 activation — `sit.c:45` `rnd(6) > 4`.
- Throne ~1/3 destruction "puff of logic" — `sit.c:224-233`.
- Vlad's throne never vanishes without a wish — `sit.c:241-353` (cases 1-4 grant wish + destroy; cases 5-13 negative but throne survives).
- Sink-quaff outcomes match `fountain.c:604-711` (gain level case 8, find ring case 5, random potion case 4, water elemental case 7, polymorph case 10, scalding water, sewer rat, vomit).
- Sink-drop ring messages match `do.c:dosinkring`: searching, slow digestion, levitation, aggravate, shock, conflict, sustain ability, gain strength, increase accuracy, increase damage, hunger, teleportation.
- Pouring polymorph potion into sink → fountain/throne/altar/grave — `do.c polymorph_sink`.
- Pouring oil leaves film on basin — `fountain.c:dipsink` case POT_OIL.

### Corrected
1. **Throne "Free identification of up to five items"** — `sit.c:198` calls `identify_pack(rn2(5), FALSE)`. `rn2(5)` returns 0-4. When `id_limit == 0`, `identify_pack` identifies EVERYTHING (`invent.c:2711-2745`). So it's 1-4 items, OR 1-in-5 chance the throne ids your entire inventory.
   - Fix: "Free identification of one to four items in your pack — or, one time in five, your entire inventory."

2. **Sink polymorph "The sink vanishes"** — `do.c:450-453` actual message: `"The sink transforms into %s!"` with the new feature name. The "vanishes" string only fires in the sub-case where polymorph picked "grave" but `make_grave` failed.
   - Fix: rewrote table row to show transforms message with vanish fallback noted.

3. **Sink-drop ring of poison resistance "smell rotten fruit"** — `do.c:521` `"You smell rotten %s."` with `makeplural(fruitname(FALSE))`. Default fruit is "slime mold", so default message is "You smell rotten slime molds." With a custom `fruit:` option it changes.
   - Fix: "You smell rotten slime molds." with note about custom fruit.

4. **Sink-drop ring of gain constitution "greater/less"** — `do.c:542-545` `"The %s flow seems %ser now."` produces "greater" and "lesser" (not "less").
   - Fix: "greater/lesser".

5. **Sink kick outcomes missing the amorous demon** — `dokick.c:1224-1234` `"The dish washer returns!"` calls `makemon(PM_AMOROUS_DEMON ...)`. Once-per-sink, similar gate to black pudding branch.
   - Fix: added "summon an amorous demon posing as the dish washer" with link to seduction context. Noted once-per-sink behaviour.

### Close calls (human review)
- Fountain wish probability rate "~1/30, falling off with depth": the math is more like `(1/30) * max(0, 20-LD)/100` — at most ~0.6% on DL1, essentially 0 by DL20. The "~1/30" headline is the water-demon-appearance rate, not the wish rate. Question for human: spell this out, or leave as approximate?
- Throne wish luck threshold "if your luck is positive": C check is `u.uluck + rn2(5) < 0`, so with Luck=0 there's 4/5 chance of wish. "Non-negative luck almost always gives a wish" — current "positive" undersells. Tighten?
- Throne case 11 not listed in the spoiler at all: aggravate monsters (Luck<0) or teleport (Luck≥0). Add?
- Excalibur dip: requires `obj->quan == 1L` (single sword, not stack). Worth mentioning?

### Notes
- The sink ring-drop table is exact game output and players use it as a lookup; verbatim accuracy matters here.

---

## 2026-05-17 — Chapter audit #6: Weapons Tables → Club

Source: `spoilers/companion.md` lines 6762-6768
Verified 11 cells; 1 corrected; 0 flagged.

### Verified
- club row: damage 1d6/1d3, wt 30, cost 3, hit 0, wood — `objects.h:355-373`.
- aklys row: damage 1d6/1d3, wt 15, cost 4, hit 0, iron — `objects.h:381-383`.
- Note "What a Caveman starts with" — `u_init.c:68-75` Caveman starting inventory.

### Corrected
1. **aklys "Returns when thrown if Strength is high enough"** — WRONG. The Str gate is for **Mjollnir**, not aklys. The aklys return mechanic at `dothrow.c:1577-1587, 1709-1721` keys on `tethered_weapon` / `iflags.returning_missile` with an `rn2(100)` miss chance — it returns when wielded as primary weapon (tethered), no Str check.
   - Fix: "Returns when thrown if wielded as your primary weapon (it's tethered); occasional misfire."

---

## 2026-05-17 — Chapter audit #7: Dangerous Encounters → Deadly Poison

Source: `spoilers/companion.md` lines 2091-2100
Verified 7 claims; 1 corrected; 2 flagged.

### Verified
- Eating Death/Pestilence/Famine corpses instantly fatal — `eat.c:831-849`.
- "Instantly lethal poison attacks" mechanism — `attrib.c:317-408` poisoned() function; instakill branch when `i == 0` and `typ != A_CHA`.
- Pit viper has AD_DRST — `monsters.h:2204-2212`; mhitm_ad_drst → poisoned().
- Poison resistance fully blocks — `attrib.c:338-343`.
- POISON_RES gainable from corpses — `eat.c:924`, `eat.c:967`, `eat.c:1049` (M1_POIS monsters).

### Corrected
1. **"Death, Pestilence" omits Famine** — eat.c:831-833 handles PM_DEATH, PM_PESTILENCE, AND PM_FAMINE identically with "Eating that is instantly fatal." + done(DIED). All three Riders' corpses are instakill.
   - Fix: "Eating any Rider corpse (Death, Pestilence, *or* Famine)".

### Close calls
- Example list "pit vipers, some spiders" is technically true but very narrow. Killer bees, centipedes, scorpions, soldier ants, snakes, water moccasins, cobras, quasits — all AD_DRST attackers route through the same poisoned()/instakill path. Broadened the example list and added quantitative odds (~1 in 240 per hit at full HP) to convey scale better.

### Notes
- "Instantly lethal" is shorthand: the kill is HP-gated (only fires when current HP ≤ 6+d(4,6), i.e. 10-30). Above that HP the bad branch survives with damage. Acceptable shorthand.

---

## 2026-05-17 — Chapter audit #8: Bestiary Tables → Blobs `b`

Source: `spoilers/companion.md` lines 7147-7163
Verified 24 cells/claims; 0 corrected.

### Verified
- All three blob rows match `monsters.h:137-166` exactly: acid blob (CLR_GREEN, lvl 1, spd 3, AC 8, passive 1d8 acid), quivering blob (CLR_WHITE, lvl 5, spd 1, AC 8, touch 1d8), gelatinous cube (CLR_CYAN, lvl 6, spd 6, AC 8, touch 2d4 paralyse + passive 1d4 paralyse).
- All three carry M1_MINDLESS and MR_SLEEP | MR_POISON.
- Acid blob also has MR_ACID | MR_STONE (per spoiler notes).
- Cube has MR_FIRE | MR_COLD | MR_ELEC + others (per notes).

---

## 2026-05-17 — Chapter audit #9: Bestiary Tables → Vampires `V`

Source: `spoilers/companion.md` lines 7924-7938
Verified 25 cells/claims; 0 corrected; 1 flagged.

### Verified
- All three rows match `monsters.h`: vampire (CLR_RED, LVL 10/12/1/25), vampire lord (CLR_BLUE, LVL 12/14/0/50), Vlad (HI_LORD = CLR_MAGENTA, LVL 28/26/-6/80, weapon 2d10 + bite 1d12 drain-XL, boss/M3_WANTSCAND).
- All three vampires: M1_FLY, M1_REGEN, M1_POIS, M2_UNDEAD, M2_STALK, M2_SHAPESHIFTER.
- vampire mage is `#if 0 DEFERRED` in monsters.h:2301-2312 — correctly omitted.

### Close calls
- "Shapeshifts to bat or cloud" undersells: per `mon.c:4956` vampire lord and Vlad can also become a wolf. "Bat or cloud" is correct for basic vampire; incomplete for higher tiers.

---

## 2026-05-17 — Chapter audit #10: A Practical Identification Strategy → The Sink Test (Rings)

Source: `spoilers/companion.md` lines 2745-2749 (the rest of the 2741-2749 range is the tail of the prior subsection)
Verified 3 claims; 0 corrected; 1 close call.

### Verified
- Drop ring into sink → invokes `dosinkring()` at `do.c:753-756` (IS_SINK + RING_CLASS gate).
- Each ring produces a characteristic message (when sighted) — `do.c:dosinkring`.
- Cross-reference to Sinks section at line 799 (Points of Interest) — exists.

### Close calls
- "Each ring type produces a characteristic message" — true when sighted. When `Blind`, several types fall through to the generic "ring bouncing down the drainpipe" message and don't ID. The summary glosses this.

### Notes
- This is a pointer/summary section — no factual redundancy with Unit #5's detailed table.

---

## 2026-05-17 — Chapter audit #12: Dangerous Encounters → The Genetic Engineer

Source: `spoilers/companion.md` lines 2182-2208
Verified 14 claims; 1 corrected; 0 flagged.

### Verified
- Symbol Q green — `monsters.h:2143`.
- Shares S_QUANTMECH with quantum mechanic — both `S_QUANTMECH`.
- One AT_CLAW AD_POLY 1d4 attack — `monsters.h:2138`.
- Unchanging grants immunity — `mhitm.c:1130`.
- Polymorph is same uncontrolled roll — calls `polyself(POLY_NOFLAGS)`.
- M1_TPORT (engineers self-teleport) — `monsters.h:2141`.
- Cooldown via mspec_used between successful poly hits — `mhitu.c:368-392`.
- Corpse mechanically identical to doppelganger — `eat.c:1244-1263` (same case block).
- Tin works for portable polymorph — `eat.c:1253`.

### Corrected
1. **Hit message wording: "you undergo a freakish metamorphosis"** — that's actually the CORPSE-eating message (`eat.c:1260`). The melee-hit message is "**You are subjected to a freakish metamorphosis.**" (`mhitm.c:1135`). The spoiler had the two messages swapped.
   - Fix: changed in-text quote to the correct melee-hit string.
2. **Defenses list omitted magic resistance** — `mhitm.c:1128` `if (Antimagic) { shieldeff(...); }` blocks both poly and damage. Added "magic resistance (also fully blocks the polymorph)" to defenses.

---

## 2026-05-17 — Chapter audit #13: Bestiary Tables → Wraiths `W`

Source: `spoilers/companion.md` lines 7940-7954
Verified 24 cells/claims; 0 corrected; 1 close call.

### Verified
- barrow wight: CLR_GRAY, LVL 3/12/5/5, with weapon DRLI + spell + claw 1d4 + touch 1d4 cold + cold/sleep/poison-res.
- wraith: CLR_BLACK, LVL 6/12/4/15, touch 1d6 drain-XL, M1_FLY.
- Nazgul: HI_LORD = CLR_MAGENTA (bright magenta), LVL 13/12/0/25, weapon 1d4 drain-XL + breath 2d25 sleep, M1_SEE_INVIS.
- Prose: drains XL, fresh corpse grants level (eat.c:1141 `pluslvl(FALSE)`), all undead and follow stairs (M2_UNDEAD + M2_STALK).

### Close calls
- Wraith row omits MR_STONE and M1_UNSOLID from Notes — wraith is uniquely stoning-resistant and incorporeal among W-class. Optional enrichment.

---

## 2026-05-17 — Chapter audit #11: Dangerous Encounters → Drowning

Source: `spoilers/companion.md` lines 1868-1877
Verified 5 claims; 2 corrected; 0 flagged.

### Verified
- Magical breathing (amulet / spell) allows underwater survival — `trap.c:5106-5126` `drown()` returns FALSE if Amphibious || Breathless || Swimming. `youprop.h:270-277` Magical_breathing → Amphibious || Breathless.
- Range attacks bypass the AD_WRAP grab (requires adjacency).
- Eels and krakens carry the grab attack — giant eel and electric eel have AT_TUCH AD_WRAP (`monsters.h:3230-3256`); kraken has AT_HUGS AD_WRAP.

### Corrected
1. **"If you're burdened or worse when grabbed, you can drown before you get a turn"** — WRONG. Two separate mechanics conflated:
   - Grab-then-drown by eel/kraken (`uhitm.c:3389-3401` `mhitm_ad_wrap`): triggers on the monster's turn when `u.ustuck == magr` and tile is a pool, no Swimming/Amphibious/Breathless. Encumbrance not checked.
   - Fall-into-water crawl-out (`trap.c:5157` → `emergency_disrobe` at 4901): threshold is `near_capacity() > SLT_ENCUMBER` = stressed (not burdened); only matters when you fall in, not when grabbed.
   - Fix: rewrote to clarify the grab-drown is not encumbrance-gated; encumbrance only affects the unrelated fall/crawl-out scenario.
2. **"Stay unburdened near water"** defense — WRONG, doesn't defend against the eel grab. Removed. Defenses now correctly listed: magical breathing, levitation, kill at range.

### Notes
- Added electric eels to the grab-list (the spoiler had only giant eels and krakens). Added swamps and moats to the encounter locations.

---

## 2026-05-17 — Methodology note

User correctly flagged that fixes themselves are unverified claims.
The Drowning rewrite (audit #11) introduced "levitation" as a defense
without grep-verifying it; one grep of `Levitation` against the
AD_WRAP handler in uhitm.c:3389 would have caught that `Levitation`
is NOT in the drown-check (only Swimming/Amphibious/Breathless).

New discipline: after applying any factual correction, grep the C
source for each new specific claim in the rewrite. Especially for
"X defends against Y" wording — these need explicit verification
before commit.

Self-audit pass found two more rewrites with the same issue:

1. **Troll corpse destruction methods** (audit #3 rewrite): I'd
   listed "fire wand/spell, lava, water, force-bolt/striking" as
   ways to destroy a troll corpse. burn_floor_objects in zap.c
   only burns SCROLL_CLASS, SPBOOK_CLASS, and GLOB_OF_GREEN_SLIME
   — NOT corpses. force-bolt code in zap.c targets monsters, not
   floor objects. The verified ways to prevent troll revival are:
   eat the corpse, kill it with Trollsbane wielded (uhitm.c
   comment "troll killed by Trollsbane won't auto-revive"), or
   stone it (monstone() drops a statue instead of make_corpse).
   Re-trimmed to verified options.

2. **Drowning defenses**: Already re-fixed to remove the false
   "levitation prevents grab-drown" claim. Levitation only
   prevents walking into water; the eel grab-drown check uses
   monster's tile + only Swimming/Amphibious/Breathless.

---

## 2026-05-17 — Chapter audit #14: Bestiary Tables → Elementals `E`

Source: `spoilers/companion.md` lines 7670-7686 (after the rewrite shift; originally 7638)
Verified 32 cells/claims; 0 corrected; 5 close calls.

### Verified
- All 5 rows (stalker, air, fire, earth, water) match `monsters.h` exactly.
- "All except stalker are mindless" — M1_MINDLESS on all four elementals, not stalker.
- Resistance notes on earth/water rows complete.

### Close calls
- Fire elemental notes omit MR_FIRE / MR_POISON / MR_STONE; air elemental notes omit MR_POISON / MR_STONE. Asymmetric vs earth/water rows. Optional enrichment.

---

## 2026-05-17 — Chapter audit #15: The Ascension Kit

Source: `spoilers/companion.md` lines 5274-5298
Verified ~30 claims; 3 corrected; 2 close calls.

### Verified
- All DSM mappings (gray=ANTIMAGIC, silver=REFLECTING, blue=SHOCK_RES) — `objects.h:502-522`.
- Cloak of magic resistance exists — `objects.h:644`.
- Helm of brilliance, helm of telepathy exist — `objects.h:470, 485`.
- Gauntlets of power → STR boost — `attrib.c:1214`.
- Speed boots → FAST — `objects.h:707`.
- Hawaiian/T-shirt in ARM_SHIRT slot — `objects.h:604-608`.
- Amulet of life saving / LIFESAVED — `objects.h:838`.
- Eye of the Aethiopica is Wizard quest artifact — `artilist.h:303`.
- Ring of free action blocks paralysis — `mcastu.c:506`.
- Level teleport blocked while carrying Amulet — `teleport.c:1185`.
- Candelabrum needs 7 candles — `apply.c:1351-1420`.
- Mysterious Force still active in 5.0 — `do.c:1541-1573`.
- Wizard respawns — `wizard.c:713`.
- Silver does bonus damage to demons — `mondata.c:524` `hates_silver()`.

### Corrected
1. **"Helm of holiness"** — doesn't exist. The Mitre of Holiness is the Priest quest artifact (`artilist.h:265`), based on a helm of brilliance. The spoiler conflated the artifact's name with a regular item type.
   - Fix: "Helm of brilliance or helm of telepathy" with a note that Priests can use the Mitre.
2. **"You can't pray for [food]"** — WRONG. `TROUBLE_HUNGRY` is a real god-trouble (`pray.c:98, 275-276, 408`). Reworded to clarify prayer *can* but it's high-cost.
3. **"You can't pray curses away"** — WRONG. `TROUBLE_CURSED_ITEMS` is a real trouble category (`pray.c:93, 253`); `worst_cursed_item()` at `pray.c:288` picks the cursed item the god will uncurse. Reworded to "prayer can uncurse a cursed worn item but only one at a time".

### Close calls
- "Silver bypasses demon resistances" — actually triggers bonus-damage via `hates_silver()`, not resistance bypass. Practical effect right, mechanism described wrong.
- "Up-stair from the Sanctum lifts you out" — the Sanctum's exit is actually the ritual portal, not regular stairs. Loose framing.

---

## 2026-05-17 — Chapter audit #16: Bestiary Tables → Xans and fantastic insects `x`

Source: `spoilers/companion.md` lines 7540-7553
Verified 9 cells; 0 corrected; 2 close calls.

### Verified
- grid bug: CLR_MAGENTA, LVL 0/12/9/0, AT_BITE/AD_ELEC 1d1, MR_ELEC + MR_POISON.
- xan: CLR_RED, LVL 7/18/-4/0, AT_STNG/AD_LEGS 1d4, M1_FLY + M1_POIS.
- Preamble "poison-resistant" verified for both.

### Close calls
- Grid bug `G_NOCORPSE` flag not flagged in this Notes column (mentioned in another section).
- Preamble omits grid bugs can't move diagonally (mentioned elsewhere).

---

## 2026-05-17 — Chapter audit #17: Bestiary Tables → Humans and elves `@`

Source: `spoilers/companion.md` lines 8027+ (43 rows of human/elf monsters)
Verified 200+ cells; 1 corrected; multiple close calls.

### Verified
- All 43 rows match `monsters.h` exactly: human, were-X, elf-X, elf-lord, Elvenking, doppelganger, shopkeeper, guard, prisoner, Oracle, priest, high priest, soldier, sergeant, nurse, lieutenant, captain, watchman, watch captain, Medusa, Croesus, Charon, all 13 player roles, all 3 Archeologist-line quest leaders.
- HI_DOMESTIC=white, HI_LORD=magenta, HI_ZAP=bright-blue color mappings — `color.h:37-55`.
- M2_STALK = "follows stairs" attribution correct row-by-row.

### Corrected
1. **Intro "shopkeepers, priests, watchmen, Kops, role nemeses..."** — Kops are `S_KOP` (`K` glyph, `defsym.h:338`), not `S_HUMAN`. Removed from the `@` class intro and added an explicit note "(Kops are *not* in this class — they're K)".

### Close calls
- Intro mentions ninja but ninja (S_HUMAN at monsters.h:3867) isn't in the table — omission.
- Intro implies quest-leader coverage but only the Archeologist line is in the table (the other 11 quest leaders + Wizard of Yendor + Norn + nemeses are S_HUMAN but absent).
- Barbarian/Healer have MR_POISON, Valkyrie has MR_COLD — none called out in Notes column even though these are well-known traits.
- Charon row assumes `#ifdef CHARON` build option (compiled out by default in 5.0).
