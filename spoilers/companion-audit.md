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

---

## 2026-05-17 — Chapter audit #18: Acknowledgements

Source: `spoilers/companion.md` lines 8416-8540
Verified ~15 historical claims; 0 corrected; ~5 unverifiable.

### Verified
- NetHack since 1987 — Wikipedia + dat/history (NetHack 1.3d July 1987).
- DevTeam founders Mike Stephenson, Izchak Miller, Janet Walz — Wikipedia.
- Izchak Miller died 1994 — Wikipedia (April 1, 1994).
- Hack by Jay Fenlason 1982 at Lincoln-Sudbury HS — Wikipedia + history file.
- Rogue 1980 (Toy and Wichman) — Wikipedia.
- Hack extended by Andries Brouwer mid-1980s — Wikipedia + history file (Hack 1.0 Dec 1984 through 1.0.3 July 1985 at Stichting Mathematisch Centrum).
- NetHack forked from Brouwer's Hack 1987 — consistent with history file.
- rec.games.roguelike.nethack — verified.
- Fenlason → Brouwer → Stephenson lineage — exactly as the chapter describes.

### Could not verify (close calls)
- WikiHack founding by Sgeo 2005, migration 2010, "over 5000 articles" — nethackwiki.com 403; community-knowledge plausible.
- Hugo/O'Donnell spoilers "38 files" — consistent with steelypips.org archive citations but unverified.
- Various individual spoiler-author attributions (Damerell, Dunbar, Powell, Malec, Waijers, Bond, Nicolaas, Goldfarb) — match standard community lore; couldn't positively verify each.
- WCST expansion "World's Encyclopaedia of NetHack" — less standard than "Waterman's Comprehensive Spoiler Treatise"; worth checking.

---

## 2026-05-17 — Chapter audit #19: Weapons Tables → Quarterstaff

Source: `spoilers/companion.md` lines 6830-6838
Verified 7 cells; 0 corrected.

### Verified
- quarterstaff: 1d6/1d6, wt 40, cost 5, hit 0, wood, two-handed — `objects.h:377` WEAPON entry.
- Wizard starts with quarterstaff — matches role intro.

### Close calls
- "Light" descriptor for wt 40 is subjective (light for two-hander, moderate by general standard).

---

## 2026-05-17 — Chapter audit #20: Bestiary Tables → Cockatrices `c`

Source: `spoilers/companion.md` lines 7183-7198
Verified 22 cells; 0 corrected.

### Verified
- chickatrice: CLR_BROWN, LVL 4/4/8/30, bite 1d2 + touch petrify + passive petrify, ston-res. Matches monsters.h:170-177.
- cockatrice: CLR_YELLOW, LVL 5/6/6/30, bite 1d3 + touch petrify + passive petrify, ston-res. Matches monsters.h:178-186.
- pyrolisk: CLR_RED, LVL 6/6/6/30, gaze 2d6 fire + bite 1d6, fire-res. Correctly NO petrify attacks, NO ston-res. Matches monsters.h:187-195.
- All three poison-resistant (MR_POISON) — verified.

---

## 2026-05-17 — Chapter audit #21: Dangerous Encounters → Attack Wands and the Warning Shot

Source: `spoilers/companion.md` lines 1888-1894
Verified 6 claims; 0 corrected; 1 substantive omission added.

### Verified
- First shot always misses for inexperienced monsters — `muse.c:1830-1834`, comment literally says "the first shot always misses".
- `buzz_force_miss()` at muse.c:1815-1818 calls `dobuzz(forcemiss=TRUE)`; `zap.c:4962` skips zap_hit when forcemiss.
- Per-monster flag mwandexp (monst.h:166), set TRUE after the first zap.
- Wand identifies itself if monster visible — `use_offensive` at muse.c:1849-1850 `if (oseen) makeknown(otmp->otyp)`.
- Player gets a turn before next zap connects.

### Added (was omitted in original)
- **Late-game carve-out**: monsters generated in Stronghold, Knox, Quest, Gehennom, Vlad's Tower, or endgame planes start with `mwandexp = TRUE` (`makemon.c:1290-1293`). They do NOT give the warning shot.

### Close call
- "Any offensive wand" was slightly broad: force-miss applies to beam wands (death, sleep, fire, cold, lightning, magic missile) and fire/frost horns, but not WAN_TELEPORTATION / WAN_UNDEAD_TURNING / WAN_STRIKING (which use mbhit, not buzzfn). Tightened to "beam wand" with the specific list.

---

## 2026-05-17 — Methodology follow-up

Tightened the survival-tips bullets in The Ascension Run section.
The prior fix correctly noted prayer CAN cure hunger and uncurse
items, but the resulting bullet wording was wordy. The actual
strategy advice (bring food, bring scrolls) is sound on its own;
dropped the prayer caveat entirely. The reader doesn't need to
know WHY to bring food — just that they should.

---

## 2026-05-17 — Chapter audits #22 #23 #24 #25: all clean

### #22 Bestiary Tables → Gnomes `G`
22 cells verified, 0 corrected. All 4 S_GNOME entries (gnome, gnome lord, gnomish wizard, gnome king) match `monsters.h`. No "deep gnome" exists in 5.0 (correctly omitted).

### #23 Weapons Tables → Shuriken
5 cells verified, 0 corrected. Matches `objects.h:163` shuriken WEAPON entry (1d8/1d6, wt 1, cost 5, hit +2, iron).

### #24 Bestiary Tables → Golems `'`
60+ cells across 11 rows verified, 0 corrected. All entries match `monsters.h:2509-2594`. Includes straw, paper, rope, gold, leather, wood, flesh, clay, stone, glass, iron — each with correct dmg/AC/MR/resistances. Optional enrichment: flesh golem is the only one without G_NOCORPSE (uniquely useful corpse with conferred resistances).

### #25 Bestiary Tables → Arachnids and centipedes `s`
30+ cells verified, 0 corrected. All 5 entries (cave spider, centipede, giant spider, scorpion, Scorpius) match `monsters.h:940-972, 3713-3722`. Scorpius's AD_SAMU steal-amulet attack and AD_DISE disease sting correctly labeled.

### Close calls (none requiring action)
- Gnomes: gnome king's M2_PRINCE not flagged in Notes (minor consistency gap vs other tables).
- Shuriken: empty Notes column (could flag highest to-hit among basic thrown missiles).
- Golems: flesh golem corpse uniqueness not surfaced (could be pedagogical).
- Arachnids: "common as source of poisonous-corpse food poisoning" is loose (only 2 of 4 regulars are M1_POIS).

---

## 2026-05-17 — Chapter audit #26: Traps and Hazards → Nuisance Traps

Source: `spoilers/companion.md` lines 1165-1176
Verified 4 trap entries; 1 broadened; 0 wrong.

### Verified
- Arrow trap "Fires an arrow at you (modest damage)" — `trap.c:1190` thitu(8, dmgval(arrow), ...). Modest single-digit damage. Missed arrows stack on the floor (verified at 1217-1221).
- Dart trap "Fires a dart, may be poisoned" — `trap.c:1251` `if (!rn2(6)) otmp->opoisoned = 1` — 1-in-6 poison chance. AD_DRST poisoned() path.
- Squeaky board "Makes noise, wakes nearby monsters" — `trap.c:1403` `wake_nearby(FALSE)` → `wake_nearto_core(u.ux, u.uy, u.ulevel*20, FALSE)`.

### Broadened
- Rust trap was described as "Splashes water, rusting exposed metal equipment" — incomplete. `trap.c:1595` `trapeffect_rust_trap` calls `water_damage()` on multiple worn slots (helm, weapons, gloves, cloak/suit/shirt) and additionally iterates inventory to splash any `lamplit` items via `splash_lit()`. Non-metal armor takes water damage too (potions in worn containers dilute, lamps go out). The "only metal" framing misleads a leather-armor reader into false security.
   - Fix: "Splashes water — rusts iron worn armor, soaks cloak/suit/shirt, douses lit lamps".

---

## 2026-05-17 — Chapter audit #27: Bestiary Tables → Humanoids `h`

Source: `spoilers/companion.md` lines 7285+
Verified 50+ cells across 7 rows; 2 corrected in Notes column.

### Verified
- All stats: hobbit (1/9/10/0), dwarf (2/6/10/10), bugbear (3/9/5/0), dwarf lord (4/6/10/10), dwarf king (6/6/10/20), mind flayer (9/12/5/90), master mind flayer (13/12/0/90) — `monsters.h:477-540`.
- All colors and attack dice correct.
- M1_TUNNEL | M1_NEEDPICK on dwarves; M1_FLY | M1_SEE_INVIS on mind flayers.
- Int=ATTRMIN(3) brainlessness death — `eat.c:698`.

### Corrected
1. **mind flayer Notes: "Wear an alignment-matching helmet"** — WRONG. There's no alignment check on helmet protection. `uhitm.c:3235` `if (uarmh && rn2(8))` — ANY helmet blocks 7/8 of tentacle attacks. The only helmet special-case is DUNCE_CAP, which actually fully prevents brain-eating (dunce can't be dumbed further). Fix: "Wear any helmet (blocks 7/8 of tentacles) or kill from range."

2. **master mind flayer Notes: "Catastrophic without telepathy + free action"** — WRONG defenses listed. Telepathy doesn't defend; it just helps see them when blind. Free action defends paralysis (floating eye, sleeping), not Int drain. The actual defense is any helmet (same 7/8 block) and not standing adjacent. Fix: "Catastrophic adjacent without a helmet. Any helmet blocks 7/8 of tentacles."

### Notes
- "If Int hits 3 you die" wording is accurate enough for spoiler prose.
- "Five tentacles per turn" technically right but `gs.skipdrin` short-circuits after helmet-blocked hit, so the expected damage per turn is less than 5× implies.

---

## 2026-05-17 — Chapter audit #28: Tools of the Trade

Source: `spoilers/companion.md` lines 3668-3812 (144 lines)
Verified ~40 claims; 5 corrected; 4 close calls.

### Verified
- Container weights match `objects.h:899-912` (sack/oilskin/bag of holding/bag of tricks=15; large box=350; chest=600; ice box=900).
- Magic lamp wish odds: 1/3 djinni emerges (apply.c:1817), 80% wish from blessed (potion.c:2833) → ~27% total. ✓
- Magic marker initial charges 30-99 (mkobj.c:1026 `rn1(70,30)`).
- Marker recharge: blessed scroll of charging restores to ≥50, second attempt fails (read.c:854-879).
- Marker write costs match basecost/2 to basecost-1 (write.c:265) for all items listed.
- Unicorn horn ailment cap of 7 (blessed), 3 (uncursed) with 35% no-effect (apply.c:2336-2341 comment).
- Cursed horn inflicts random ailment from {sick, blind, confused, stunned, vomiting, hallucinated, deaf} (apply.c:2297-2301).
- Unicorn horn does NOT restore drained ability scores in 5.0; no fix_attrib path (apply.c).
- Skeleton key on doors 70% + Dex (lock.c:640); on boxes 75% + Dex (lock.c:528).
- Magic harp/flute/drum effects match music.c (charm, sleep, earthquake).
- Candelabrum held by Vlad (M3_WANTSCAND); 7 candles required.
- Towel: wipes cream pie + serves as blindfold (apply.c).

### Corrected
1. **Chest/large box capacities** omitted locked variants. mkobj.c:315-320: `box->olocked ? 7 : 5` for chests, `? 5 : 3` for large boxes. Fix: added "(0 to 7 if locked)" / "(0 to 5 if locked)".

2. **Unicorn horn cure list "poison, confusion, blindness, nausea"** was wrong:
   - No "poison" cure exists (SICK in apply.c is food poisoning/illness, not the resistance line).
   - Missing stun, hallucination, deafness (all in apply.c:2312-2327).
   - "Nausea" should be "vomiting".
   - Fix: full list "confusion, blindness, sickness, hallucination, stunning, vomiting, deafness".

3. **Crystal ball "Detect objects, traps, and portals on a level"** — misleading. detect.c:1300 prompts for one symbol class per gaze; one gaze = one question. Fix: "Pick a glyph class per gaze; each gaze answers one question."

4. **Bell of Opening "found in Vlad's Tower area"** — WRONG. Vlad holds the Candelabrum (M3_WANTSCAND). The Bell is the Quest reward, granted by the role's quest leader on Quest completion. Fix: "Invocation item (granted by your quest leader on Quest completion)".

5. **Passtune "tooled horn or bugle"** — WRONG. music.c:769-772 lists wooden flute, magic flute, tooled horn, frost horn, fire horn, bugle as blowable; harps can play too. Only earthquake/leather drums are excluded. Fix in both the Castle section (line 1130) and the Musical Instruments paragraph (line 3738): "any tonal instrument".

### Close calls
- "rub it while blessed and there's a 1-in-3 chance the djinni emerges" — the 1/3 emergence test doesn't depend on bless status; only the wish does. The 27% figure is correct only for blessed lamps.
- BoH "in older editions destroyed everything" — overstated even historically. Current is `is_boh_item_gone = !rn2(13)` (~7.7% per item).
- "Tin opener: open tins in one turn" — true for blessed wielded; otherwise 50/50 between 0 and 1 turn. Reasonable simplification.
- "Bag of tricks (not a bag)" — IS a container code-side (Is_container/Is_mbag). Parenthetical is usage hint, not code-level fact.

---

## 2026-05-17 — Chapter audit #29: What Actually Kills Adventurers

Source: `spoilers/companion.md` lines 1623+ (204 lines)
Verified ~30 claims; 3 corrected; also caught 2 self-audit errors in my prior DSM rewrite.

### Verified
- Bat speeds (22 vs hero 12) and damage match monsters.h.
- Mimic mechanics: small/large/giant attacks, sticking, eating durations (20/40/50 turns).
- Mimic appears as gold (or orange hallucinating) — eat.c:1196.
- ILLOBJ symbol `]` vs ARMOR `[` — defsym.h:466.
- Water demon ~1 in 30 — fountain.c:247 `rnd(30)`.
- Wish odds drop with depth — fountain.c:78.
- Mount fails on Confused/Fumbling/Glib/cursed-saddle — steed.c:339.
- Bones items ~80% cursed — bones.c:290 `if (rn2(5)) curse(otmp)`.
- Confused genocide kills you — read.c:1737.
- Earth scroll boulders crush — read.c:1919.
- Petrification messages — timeout.c:129-130.

### Corrected
1. **Mount slip damage "11-15 HP"** — `steed.c:354 losehp(Maybe_Half_Phys(rn1(5,10)), ...)`. `rn1(x,y) = rn2(x)+y`, so `rn1(5,10) = 10..14`. Off by one.
2. **Mumakil "four-attack pack hunters"** — `monsters.h:840` shows 2 attacks (AT_BUTT 4d12 + AT_BITE 2d6) and `(G_GENO | 1)` no group flag. Solo, not pack. Rothes are correctly three-attack pack hunters.

### Self-audit catches (from earlier DSM rewrite, audit #15 response)
3. **Shimmering DSM doesn't exist in 5.0** — `objects.h:509-512, 536-539` shows both shimmering dragon scale mail and scales are wrapped in `#if 0 /* DEFERRED */`. Not in the game. I'd added them in the all-DSM rewrite. Removed entirely from prose, both appendix tables (scales + scale mail), and the displacer beast cross-reference.
4. **Blue DSM also grants Fast (intrinsic speed)** — `do_wear.c:817-828` `if (puton) { ... EFast |= W_ARM; }`. I had Blue DSM as "shock resistance only". Updated both the prose section (now notes the Very Fast stack with speed boots) and the appendix tables.

### Close calls
- Rope golem AT_HUGS isn't AD_STCK; calling it "grapples" is loose but defensible.
- "Bats double-attack every turn" — speed ratio 1.83, so 2 moves on most turns, occasionally 1.
- "Potion shrapnel is deadly" — depends on potion; "sometimes harmful" more accurate.

### Methodology note
- The agent's self-audit prompt asked me to be skeptical of my own prior rewrites. This audit caught two such errors in the DSM rewrite, illustrating why every fix needs grep-verification at apply-time. Shimmering DSM was added based on monsters.h having a `MON("shimmering dragon")` entry, which exists, but I didn't check whether the SCALES/SCALE MAIL items exist (they're `#if 0`). Blue DSM speed was missed because I'd only grepped for the FROMOUTSIDE properties and not for EFast.

---

## 2026-05-17 — Chapter audit #31: Sokoban Solutions → Level 4, Version B

Source: `spoilers/companion.md` lines 6042-6175 (137 lines)
Verified prize odds + level mapping; step instructions tactical (not statically verifiable).

### Verified
- Prize odds "usually amulet of reflection, 25% bag of holding" — `soko1-2.lua:105-110` `if percent(25) then bag of holding else amulet of reflection` = 25% BoH / 75% AoR.
- Level numbering: "Level 4" (topmost from player POV) = `soko1` C name. `dungeon.lua:218-244` Sokoban has `entry = -1` (ascending). Version A maps to `soko1-1.lua`, Version B to `soko1-2.lua` — inverse prize odds correctly distinguished.
- Treasure-zoo structure: 3 small chambers + locked door + zoo region. `soko1-2.lua:98-102` matches.
- Down-stair location: `soko1-2.lua:34` `des.stair("down", 06,15)` matches map.

### Close calls
- Chamber-coordinate references use spoiler's 1-indexed grid system with possible 1-row offset from lua's 0-indexed system. Internally consistent within the spoiler.

### Notes
- Step-instruction script is tactical, not falsifiable.
- Two-boulders-remain final state can't be verified without simulating.

---

## 2026-05-17 — Chapter audit #30: Sokoban Solutions → Level 1, Version A

Source: `spoilers/companion.md` lines 5627+
Verified map/step consistency; 1 typo corrected.

### Verified
- Boulder positions in initial map line up with step descriptions.
- Steps 1-2 path (reach A via row 4) reachable.
- Step 3-4 D right-then-far-left requires loop through upper-right chamber (10,3)→(10,2)→(11,2)→(12,2)→(12,3)→(12,4) — verified passable.
- Step 5 E push down (11,5)→(11,8) — column 11 is open through the row-6 cross-wall gap.
- General Sokoban mechanics (boulders fill pits, rolling-boulder traps, −1 Luck cheats, ascending) all correct.

### Corrected
1. **Scroll coordinates "(3,12) and (4,12)"** — col 4 row 12 is the `┌` wall character. Only (2,12) and (3,12) are open floor. Version B note correctly cites the analogous nook as "(2,10) and (3,10)". Fix: "(2,12) and (3,12)".

---

## 2026-05-17 — Chapter audit #32: A Practical Identification Strategy → The Price Is Right

Source: `spoilers/companion.md` lines 2439+ (292 lines)
Verified ~50 price/multiplier claims across all item classes; 1 corrected; 1 close call.

### Verified
- All scroll base prices match `objects.h:1187-1265` SCROLL entries.
- All potion base prices match `objects.h:1125-1177`.
- All ring base prices match `objects.h:741-827`.
- All wand base prices match `objects.h:1449-1499`. Wand of striking at 150 is correct.
- Amulets all 150 zm (objects.h:834).
- Tourist/dunce/visible-shirt 4/3 markup — single multiplier (don't stack) per `shk.c:2947-2951`.
- Tourist threshold `<15` = `ulevel < MAXULEV/2` where MAXULEV=30.
- Per-item 4/3 unID surcharge, 1-in-4 frequency, item-stable via `o_id` — `shk.c:2870`.
- Unfamiliar shopkeeper 3/4 sell discount, 1-in-4 shopkeepers via `m_id` — `shk.c:3173`.
- Angry +33% buy surcharge — `shk.c:1372` `(price+2)/3`.
- All Cha multipliers match shk.c:2953-2964.
- Live JS `computeBuy`/`computeSell` in the toolbar mirror C exactly including rounding.

### Corrected
1. **Sell-offer blurb at line 2521** — "an unangry shopkeeper offers ¼ of base" should be **½** (set_cost default is `divisor*=2`), and "(³⁄₁₆ on unidentified items from an unfamiliar shop)" should be **³⁄₈** (½ × ¾ = ⅜). The narrative paragraph above (line 2461) correctly says "half of base", and the JS computeSell also correctly produces ½ and ⅜. Just the blurb was off by a factor of 2 in both fractions.

### Close call
- "Angry shopkeeper +33% surcharge until you pay your bill in full" — the `ESHK->surcharge` flag is only cleared by `pacify_shk(..., TRUE)`, which is called on the new-customer transition (shk.c:302, 793), not on bill payment per se. The surcharge is stickier than the spoiler implies. Acceptable spirit though.

---

## 2026-05-17 — Chapter audit #33: Dangerous Encounters → Seduction (skeptical self-audit)

Source: `spoilers/companion.md` lines 2035-2071 (my prior rewrite from earlier today)
Verified all quantitative claims; 2 factual errors in my own rewrite caught + fixed.

### Verified (every number/formula in the rewrite)
- PM_AMOROUS_DEMON identity `&` gray MS_SEDUCE — monsters.h:2931.
- Demon adjacent + cooldown precondition `mcan || mspec_used` — mhitu.c:1994.
- Armor strip order (cloak, suit-if-no-cloak, boots, gloves, shield, helm, shirt-if-naked) — mhitu.c:2119-2128.
- `rn2(20) < ACURR(A_CHA)` Cha confirmation prompt — steal.c:2325.
- Body armor/cloak still on → encounter ends — mhitu.c:2139.
- Outcome formula `rn2(35) > min(Cha+Int, 32)` — mhitu.c:2177-2178.
- 5.7% bad-outcome rate at Cha+Int=32 — 2/35, source comment confirms.
- All 5 bad outcomes (Pw drain, -1 Con, -1 Wis, lose XP w/ DRLI block, 6-15 HP).
- All 5 good outcomes (+Pw, +1 Con, +1 Wis, gain XP, full HP).
- 500+ zm charge with `rnd(umoney+10)+500` — mhitu.c:2278.
- Peaceful demon charge /5 — mhitu.c:2280.
- High Cha refuse payment — mhitu.c:2265.
- Cursed worn items stripped (no curse check in remove_worn_item) — steal.c:213.

### Corrected (self-audit catches)
1. **"Dropped on the floor at your feet, not stolen"** — WRONG. `mayberem` calls `remove_worn_item(obj, TRUE)` at mhitu.c:2351, which only unequips (Cloak_off, Armor_off, etc.). The item stays in your inventory. Not dropped, not stolen. Fix: "unequipped to your inventory, not taken or dropped on the floor".

2. **"Appears as a succubus to male characters and an incubus to female"** — WRONG. The demon's gender is set by `makemon` (makemon.c:1262-1279); with no MM_MALE/MM_FEMALE flag from the caller (the random spawn path) it falls through to `mtmp->female = femaleok ? rn2(2) : 0` — 50/50 random, INDEPENDENT of player gender. The only place where player gender determines demon gender is sink-kicked "dishwasher" spawns (dokick.c:1228-1230), and there the relationship is opposite-sex (male hero → succubus; female hero → incubus). Fix: "appears as a succubus or an incubus depending on its randomly assigned gender".

### Close calls
- Bad outcomes don't set mspec_used cooldown (mhitu.c:2179 comment "didn't get tired"), so back-to-back bad attempts possible. Spoiler doesn't mention.
- "-1d10 max Pw" — with Half_physical_damage becomes -1d5 (line 2186). Minor omission.
- "Sleep defers" — technically the attempt is wasted, demon walks away. Acceptable looseness.

### Methodology note
This is exactly the kind of error the user flagged earlier (drowning section's "levitation" claim). Self-rewrites need their own claims grep-verified. In this case the "dropped on the floor" and gender claims were both inherited from my mental model rather than from C source. The skeptical audit caught both.

---

## 2026-05-17 — Chapter audit #35: Bestiary Tables → Fungi and molds `F`

Source: `spoilers/companion.md` lines 7706-7724
Verified 49 cells / 7 rows; 0 wrong; 1 close call addressed.

### Verified
- All 7 entries (lichen, brown mold, yellow mold, green mold, red mold, shrieker, violet fungus) match monsters.h:1614-1676 exactly.
- Stats, colors, attacks, resistances all correct.

### Corrected (lead-in wording)
- "Violet and yellow molds bite back on melee with elemental passive damage" — mis-paired. Yellow mold's passive is stun (AD_STUN); violet fungus's attacks are active touch (AT_TUCH), not passive. The actual elemental-passive molds are brown (cold), green (acid), red (fire). Reworded the lead-in to call out the three elemental molds separately from yellow mold (stun) and violet fungus (active+sticking).

---

## 2026-05-17 — Chapter audit #34: The Apothecary

Source: `spoilers/companion.md` lines 3121-3239
Verified 50+ price/effect/alchemy claims; 1 corrected; 4 close calls.

### Verified
- All 24 potion prices + the water special case match objects.h.
- Speed potion non-cursed grants intrinsic Fast (potion.c:1066).
- Wand of speed monster: only grants timed Fast 50-74 turns, no longer intrinsic (zap.c:2845).
- Gain ability: blessed=all stats, uncursed=random stat (potion.c:1030).
- Alchemy recipes match `mixtype()` exactly (potion.c:2143-2199).
- Smock cuts explosion rate to 1/30 (potion.c:2421).
- Cursed dip target always explodes (potion.c:2419).
- Unicorn horn dip: sickness→fruit juice; halu/blind/conf→water (potion.c:2151).

### Corrected
1. **"Blessed extra healing and full healing also raise your maximum HP permanently"** — too restrictive. Per healup() (potion.c:1428): uncursed extra healing raises maxHP by up to 2, uncursed full healing raises maxHP by 4 (when heal would overflow). Both blessed AND uncursed raise maxHP; blessed gives the biggest boost. Cursed doesn't. Fix wording.

### Close calls
- Extra healing cures blindness ALWAYS (cureblind=TRUE unconditionally) but cures sickness only when non-cursed. Spoiler implies both gated by blessing. Tightened.
- "Drop uncursed water" for holy water — `water_prayer()` operates on all POT_WATER regardless of bcstatus; the "uncursed" qualifier is practical advice but not a mechanical requirement.
- 10% explosion baseline is right for ordinary combos; acid-as-target and lit-oil-as-target both = 100%.
- Speed potion: both blessed AND uncursed grant intrinsic Fast (only cursed doesn't). Spoiler's "one blessed quaff" is conservative.

---

## 2026-05-17 — Chapter audit #37: Branches and Landmarks → The Castle

Source: `spoilers/companion.md` lines 1121+
Verified castle.lua + dungeon.lua + music.c claims; 2 corrected.

### Verified
- "Last level of Dungeons of Doom" — dungeon.lua chain.
- "Surrounded by moat, drawbridge as main entrance" — castle.lua perimeter, drawbridge at (5,8).
- Passtune is 5 notes A-G, randomized — dungeon.c:1115 `init_castle_tune`.
- Mastermind-style feedback — music.c:850-887.
- Tonal instruments (flutes, horns, bugle, harp) — music.c:769-771.
- Wand of opening / spell of knock open drawbridge — zap.c:3263.
- Throne room + 2 barracks — castle.lua:234, 248-249.
- Wand of wishing in chest — castle.lua:142-149.
- Gehennom below — dungeon.lua:39.

### Corrected
1. **"Wand of striking on the portcullis"** — listed as opening method, but zap.c:3290 WAN_STRIKING calls `destroy_drawbridge`. The drawbridge is permanently destroyed and tune becomes useless (dbridge.c:1018 sets uheard_tune=3). It's a destruction option, not opening. Fix: separate it as a one-way destroy option with consequences spelled out.

2. **"Wand of wishing in one of the treasure chambers"** — actually in a corner tower, not a treasure chamber. castle.lua makes a structural distinction: four storerooms hold weapon/armor/gem/food stacks; the wand-of-wishing chest is placed in one of four corner towers (04,02 / 58,02 / 04,14 / 58,14), guarded by Elbereth and a cursed scroll of scare monster. Fix: clarify.

### Also corrected (cross-section bug)
- The "Surviving the eels" bullet list at lines 1109-1119 (Medusa section) had the same "stay unburdened" error that the Drowning section had. Same fix applied: removed encumbrance claim; clarified that levitation/water-walking don't help with grab-drown (eel's tile is what matters); oilskin/grease verified to work via u_slip_free (mhitu.c).

### Close call
- "Around level 27" — Castle dlvl is RNG-determined within dungeon bounds. 27 is the common range. Reasonable.
- "Maze section contains a minotaur" — castle.lua has 2 mazewalk calls, each may have 0-1 minotaurs. Changed to "may contain minotaurs".

---

## 2026-05-17 — Chapter audit #36: Making Friends

Source: `spoilers/companion.md` lines 2237+
Verified ~25 claims; 4 corrected; close calls addressed.

### Verified
- Starting pet growth (little dog → dog → large dog; kitten → housecat → large cat) — mondata.c:1230.
- Pets pick up items and eat food — dogmove.c, dog_eat().
- Separation tameness loss every 150 moves — dog.c:689.
- Starvation untames — dog.c:702.
- Food preferences (tripe for dogs/cats, apple/carrot for horses) — dog.c:995.
- Throwing food tames — tamedog() in dog.c:1143.
- Scroll of taming + spell of charm monster both use seffect_taming() — read.c:2236.
- Magic trap can produce taming — trap.c:4423.
- Peaceful displacement guards (priest/shopkeeper/vault guard/Oracle/quest leader) — mundisplaceable in monst.h:227.
- Cannot displace peaceful onto trap/unsafe terrain — hack.c:2155.

### Corrected
1. **Pet "will not step on cursed items willingly"** — overstated. dogmove.c:1065 explicit comment "Normally dogs don't step on cursed items, but if they have no other choice they will". Pet aversion uses `rn2(13 * uncursedcnt)` — probabilistic, not absolute. Reworded to be honest about probabilistic nature.

2. **"Tameness decreases over time and when they take damage"** — combat damage from monsters doesn't reduce tameness. Only YOU hitting them does (abuse_dog from uhitm.c, hack.c), plus the separation/hunger paths. Reworded to list the actual sources.

3. **"When tameness hits zero, goes feral and turns on you"** — actually goes EITHER untame-peaceful or hostile, per dog.c:694 (random branch). Reworded to acknowledge both outcomes.

4. **Displacement guards "any monster that is sleeping or paralyzed"** — not in code. hack.c:2110-2200 doesn't special-case msleeping/mcanmove. Removed that incorrect claim; kept the real list (shopkeepers/priests/etc. + trapped peacefuls).

5. **"Spell of charm monster tames a single adjacent creature"** — WRONG. read.c:2236 routes SCR_TAMING AND SPE_CHARM_MONSTER through identical seffect_taming(). Same 3×3 radius (5×5 confused). Reworded to mention both routing to the same multi-target handler.

6. **"Only unique monsters (Medusa, the Wizard) and a few special creatures resist your charms entirely"** — misleading. tamedog() at dog.c:1240 has a large exclusion list: all humans (priests, watchmen, soldiers, kings, shopkeepers), quest leaders, the Wizard (covetous), all covetous monsters, demons, shopkeepers, vault guards, priests, minions. Expanded the list.

---

## 2026-05-17 — Chapter audit #38: Saber

Source: `spoilers/companion.md` line 6751
Verified 10 table cells; 1 corrected.

### Verified
- Saber base damage 1d8/1d8, weight 40, cost 75, slash damage.
- Silver bonus damage vs demons/weres/vampires/imps (artifact.c silver test).

### Corrected
1. **Silver saber notes** — listed only Werebane as the silver-saber artifact.
   Grayswandir is the more famous one (Lawful, +5 to-hit, hallucination
   resistance). Added Grayswandir to the notes column.

---

## 2026-05-17 — Chapter audit #39: The Quest

Source: `spoilers/companion.md` line 951
Verified 8 role/artifact/nemesis pairs + entry mechanics; 1 corrected.

### Verified
- Quest portal dlvl 11-16 (dungeon.lua chainlevel="oracle" base=6 range=2; Oracle base=5 range=5).
- XP-level 14 entry requirement (include/quest.h MIN_QUEST_LEVEL; quest.c not_capable).
- Leader on first Quest level (qstart_level / Is_qstart).
- Val/Wiz/Tou/Sam/Mon role-artifact-nemesis triples (role.c + artilist.h confirmed).
- Bell of Opening drops from every MS_NEMESIS via makemon.c:1378 mitem + mon.c:2779 relobj on death.
- Alignment-record gate (quest.c is_pure/chat_with_leader: u.ualign.record < MIN_QUEST_ALIGN (20) → badalign + expulsion(FALSE); converted alignment → banished).

### Corrected
1. **"Most provide magic resistance, which you need"** — wrong. Of the 12
   living quest artifacts in artilist.h, only the Tourist's Platinum
   Yendorian Express Card grants carried MR. A few others (Sceptre of
   Might, Eye of the Aethiopica) block magic only when wielded/worn.
   Most quest artifacts give other intrinsics: luck, stealth, ESP,
   warning, reflection, protection. Rewrote the paragraph to be honest
   about the variety.

### Close calls (not corrected; phrasing reasonable as-is)
- "Quest artifact lands on the floor at their square" — really it was
  pre-placed by level gen at the same square; the Bell is genuinely
  dropped. End-state is what the spoiler describes.
- "If you leave the floor without them, the Quest is the only place
  in the game you can get them" — true on respawn, but you can re-enter
  the Quest later: expulsion(FALSE) doesn't seal the portal. Covetous
  monsters can pick up the Bell. Wording reads slightly more terminal
  than the actual mechanic. Left as-is for now.

---

## 2026-05-17 — Chapter audit #40: Ants and insects `a`

Source: `spoilers/companion.md` line 7189
Verified 48 cells across 6 rows. No corrections.

All entries match monsters.h:89-133 exactly: stats, attacks, AC,
resistances, special notes for fire ant (FF), giant beetle, killer
bee (sleep poison), soldier ant (poison + AC -4), queen bee
(MM_FEMALE only).

---

## 2026-05-17 — Chapter audit #42: The Displacer Beast

Source: `spoilers/companion.md` line 2185
Major rewrite. The original premise was wrong from start to finish.

### Verified
- `f` class (S_FELINE), CLR_BLUE, AC -10, three attacks (4d4 / 4d4 / 2d10)
  — monsters.h:437-444.
- 5.0 addition (not in 3.7 monst.c).
- Eating corpse grants temporary intrinsic Displacement via
  `incr_itimeout(&HDisplaced, d(6, 6))` — eat.c:1265-1268. Only
  intrinsic Displacement source in the game (HDisplaced set nowhere else).
- Displacer beasts SEE THROUGH the player's Displaced intrinsic
  (monmove.c:2218 `notthere = Displaced && data != PM_DISPLACER_BEAST`).
  They are *anti*-displacement.

### Corrected — major
1. **Entire "image-offset / swing at empty floor" premise was wrong.**
   The prior version described the displacer beast as having
   cloak-of-displacement style permanent image displacement. It does
   not. Its flag is `M3_DISPLACES` ("moves monsters out of its way"
   — monflag.h:175), a barge-through ability. The actual mechanic
   when the player melees it is hack.c:1972: 50% chance the beast
   **swaps places with you** instead of taking the hit (no attack
   happens, you've been yanked one square). There is no image-offset,
   no per-turn reshuffle, no "misses against an image."

2. **"See invisible does not help; the beast isn't invisible, it's
   displaced."** False premise — not displaced in that sense.

3. **"Until the displacement is broken (a successful melee hit, or a
   sense that ignores sight), expect misses that look correct."**
   No such mechanic exists. Displacer-beast melee misses aren't a thing.

4. **"What works" list (area-effect spells, scrolls of fire, etc.)**
   was framed as workarounds for the non-existent image. Rewritten to
   focus on the actual issue: ranged attacks bypass the swap entirely.

5. **Bestiary table row at line 1580** had the same false "permanent
   displacement aura" claim. Rewrote to describe the 50% place-swap.

### Notes
- The genuinely useful spoiler content (corpse grants intrinsic
  Displacement) survives the rewrite. Added tactical implication of
  the swap: it can pull you off Elbereth, out of a doorway, onto a
  trap, or into worse adjacency.


---

## 2026-05-17 — Chapter audit #41: Polearms

Source: `spoilers/companion.md` line 6882
12 rows / 84 cells verified clean against objects.h + weapon.c dmgval bonuses.
3 prose corrections.

### Verified
- All 12 polearm rows: names, S/L damage dice, weights, costs, materials,
  +small/+large bonus notes match objects.h and weapon.c:215-309 (dmgval).
- All polearms two-handed (bi=1 in objects.h).
- All use P_POLEARMS skill class.
- Apply (`#apply` / `a`) is the reach attack: doapply → use_pole (apply.c).

### Corrected
1. **"Reach of two squares"** — overstated as class invariant. apply.c:3355-3382
   shows reach is skill-dependent: Basic = orthogonal at distu==4; Skilled adds
   knight-jump (distu 4-5); Expert adds diagonals out to distu==8. Reworded
   to mention the two-square Basic reach and that Skilled opens up more.

2. **"With one empty intervening square"** — fabricated. use_pole has no
   check requiring the intervening square to be empty. Removed.

3. **"They can't be used in melee against an adjacent monster — the haft
   gets in the way"** — wrong. uhitm.c:1075-1091 routes adjacent polearm
   attacks through the bashing path: the attack works, just without
   strength bonus or weapon-skill bonus. uhitm.c:1467-1484 comment
   explicitly says "hero is simply bashing with one of those." Reworded
   to be accurate.

---

## 2026-05-17 — Chapter audit #43: Level Drain

Source: `spoilers/companion.md` line 1972
~20 mechanic claims verified; 1 corrected; 1 added.

### Verified
- Drain-attack monster list (vampire family, wraith, barrow wight, Nazgul,
  hostile incubus/succubus): all AD_DRLI in monsters.h, plus AD_SSEX
  fallback to AD_DRLI at mhitu.c:333 for hostile demons.
- Stormbringer in enemy hand drains (artilist DRLI + SPFX_ATTK via mhitm_ad_drli).
- Drain resistance carriers: Excalibur (Lawful), Stormbringer (Chaotic),
  Staff of Aesculapius (Healer quest) — all DRLI defense in artilist.h.
- Black dragon scales/scale mail grant drain resistance (do_wear.c:809-815
  EDrain_resistance |= W_ARM); also disintegration resistance.
- Wraith corpse: eat.c:1141 pluslvl(FALSE) grants exactly one experience
  level; exper.c:349. Weightless (SIZ WT_ETHEREAL=0). Not tinnable
  (apply.c:2167 tinnable() requires cnutrit > 0; wraith cnutrit = 0).
- Drained-level HP/power math (exper.c:251-273): losexp subtracts
  u.uhpinc[u.ulevel] and u.ueninc[u.ulevel] — the exact amounts the
  player gained at that level.
- Drained levels do not auto-regenerate (no restoration outside pluslvl).

### Corrected
1. **"Vampire bats" listed as level drainers** — false. monsters.h:1291-1297
   gives vampire bat ATTK(AT_BITE, AD_PHYS) and ATTK(AT_BITE, AD_DRST):
   second bite drains *Strength*, not level. Removed from list and added
   a brief parenthetical to flag the bat / vampire distinction.

### Added (not error but a 5.0 omission)
- **Shield of drain resistance** (new in 5.0, objects.h SHIELD_OF_DRAIN_RESISTANCE,
  do_wear.c). Strange omission given the section explicitly flags black
  dragon scale mail as new in 5.0. Added it.

### Close calls (not changed)
- "Drain resistance makes you immune" — true (mhitu.c:2482 short-circuits
  on Drain_resistance), but the section doesn't mention the 1-in-3 hostile
  drain chance or magic-cancellation interaction. Reasonable omission for
  a short section.
- Other drain-resistance sources not mentioned: lycanthropy (attrib.c:885
  DRAIN_RES if u.ulycn set) and polyself into resists_drli monster
  (polyself.c:77 PROPSET). Edge cases.

---

## 2026-05-17 — Chapter audit #44: Rodents `r`

Source: `spoilers/companion.md` line 7487
48 cells / 6 rows verified against monsters.h:889-936. 1 corrected.

### Verified
- All 6 rodent rows (sewer rat, giant rat, rabid rat, wererat, rock mole,
  woodchuck) — complete coverage of S_RODENT in C.
- All stats (Lvl/Spd/AC/MR/attacks/flags) match. AD_DRCO=drain Con,
  AD_WERE=lycanthropy, M1_REGEN, M1_TUNNEL, M1_SWIM, MR_POISON all
  verified per row.

### Corrected
1. **Woodchuck color shown as `—`** — should be `brown`. monsters.h:936
   explicitly assigns CLR_BROWN.

### Close calls (not changed)
- Rock mole notes omit M1_METALLIVORE / M2_JEWELS / M2_GREEDY / M2_COLLECT
  (eats metal, picks up gems). Borderline omission. Not added; would
  bloat the table.

---

## 2026-05-17 — Chapter audit #45: Hammer

Source: `spoilers/companion.md` line 6861
War hammer stats verified clean; 1 corrected; same correction applied
cross-section.

### Verified
- War hammer: 1d4+1 / 1d4 (oc_wsdam=4 + tmp++ in weapon.c:271 for small),
  weight 50, cost 5, iron, one-handed. Matches objects.h:367-369.
- P_HAMMER skill contains only war hammer (verified by grep). Aklys is
  P_CLUB, lucern hammer is P_POLEARMS — correctly elsewhere.
- Mjollnir is the artifact form of war hammer (artilist.h:109).

### Corrected
1. **"Neutral Valkyrie sacrifice gift"** — wrong implication. artifact.c:92-95
   hack_artifacts() overwrites the artifact's alignment to match the
   player's initalign for any Valkyrie. So Mjollnir is a sacrifice gift
   to *any* Valkyrie (Lawful or Neutral). Reworded.

### Also corrected (cross-section: chargen at line ~242)
- "**Neutral** Valkyries get **Mjollnir** as a sacrifice gift ... **Lawful**
  Valkyries can dip for Excalibur instead" — same alignment misconception.
  Both alignments get Mjollnir; only Lawful can dip for Excalibur
  (fountain.c:411 requires A_LAWFUL). Reworded to: "Valkyries get
  Mjollnir as a sacrifice gift regardless of alignment ... Lawful
  Valkyries can also dip a long sword in a fountain for Excalibur."


---

## 2026-05-17 — Chapter audit #49: Centaurs `C`

Source: `spoilers/companion.md` line 7677
All 3 rows (plains/forest/mountain) match monsters.h:1301-1323 exactly.
Roster complete (3 of 3 S_CENTAUR entries). 0 corrections.

### Verified
- plains centaur: brown, lvl 4, spd 18, AC 4, MR 0, weapon 1d6 + kick 1d6.
- forest centaur: green, lvl 5, spd 18, AC 3, MR 10, weapon 1d8 + kick 1d6.
- mountain centaur: cyan, lvl 6, spd 20, AC 2, MR 10, weapon 1d10 + 2× kick 1d6.

### Close calls (not changed)
- Intro prose "mounted archers ... shoot at range" — not in attack table
  (no AT_ARRO), but they have M2_COLLECT and AI to pick up and wield bows.
  Gameplay-accurate description; left as is.

---

## 2026-05-17 — Chapter audit #50: Petless (new in 5.0)

Source: `spoilers/companion.md` line 6418
All claims verified against C source. 0 corrections.

### Verified
- u.uconduct.pets is a real conduct field (you.h:161).
- End-of-game line "You have never had a pet" (insight.c:2155-2156).
- xlogfile achievement at topten.c:606 `add_achieveX(buf, "petless", !u.uconduct.pets)`.
- pettype:none mechanism: optfn_pettype (options.c:3221-3222) sets
  gp.preferred_pet = 'n'; makedog (dog.c:225-229) short-circuits before
  pet_type() is called, so no starting pet is created (overrides role
  defaults).
- All taming paths increment u.uconduct.pets (read.c, spell.c, trap.c,
  potion.c, timeout.c, dothrow.c).
- minion.c:533-539 explicitly does NOT tame the endgame guardian angel
  when u.uconduct.pets == 0 — the game has a special-case to avoid
  unexpectedly breaking petless conduct on the final level.

### Close calls (not changed)
- "New in 5.0" framing not directly verifiable from current C tree alone
  (the conduct counter has long existed; the explicit "petless" achievement
  bit + xlogfile encoding look like 5.0-era cleanup making it first-class).

---

## 2026-05-17 — Chapter audit #51: Snakes `S`

Source: `spoilers/companion.md` line 7951
6 rows × 8 columns verified against monsters.h:2167-2221. 1 corrected.

### Verified
- All 6 snake stats: garter snake, snake, water moccasin, python,
  pit viper, cobra. Names/colors/levels/speeds/AC/MR/attacks match.
- Python is the only non-hider (no M1_CONCEAL); all 6 swim (M1_SWIM).
- Poisonous-corpse notes track M1_POIS correctly (snake/water moccasin/
  pit viper/cobra have it; garter/python don't).
- pois-res notes track MR_POISON.
- Cobra spit-blind attack verified (AT_SPIT AD_BLND 0d0).
- Python four-attack combo verified.
- No "sea snake" or "mamba" in C — spoiler correctly omits them.

### Corrected
1. **"The pit viper and pit fiend are the dangerous ones"** — pit fiend
   is `&` (major demon), not a snake. Changed "pit fiend" to "cobra".

### Close calls (not changed)
- "bite Nd_ poison" — the C attack is AD_DRST (drain Strength), not
  pure poison HP loss. Common in-game shorthand; left as is.

---

## 2026-05-17 — Chapter audit #52: Combining Conducts

Source: `spoilers/companion.md` line 6372
Conduct list and listing-mechanism claims verified. Cross-section
correction in adjacent Bonesless section.

### Verified
- u_conduct fields (insight.c:2126-2228): foodless, vegan, vegetarian,
  atheist (gnostic), weaponless (weaphit), pacifist (killer), illiterate
  (literate), polypileless (polypiles), polyselfless (polyselfs),
  wishless (wishes), petless (pets), sokoban (sokocheat).
- u_roleplay fields (you.h:169-180): permablind, nudist, permadeaf, pauper.
- "Vegan ⊂ vegetarian" hierarchy via insight.c:2126-2132 else-if chain.
- "End screen lists all maintained conducts" — show_conduct (insight.c:2089)
  invoked via disclose() at game end and via #conduct command.
- "Nudist: never wear armor/shirt/cloak/gloves/boots/helmet/shield" —
  OPTIONS=nudist via optlist.h:530.
- "Blind (Zen): set blind option" — optlist.h:210-211.
- "Officially tracked since 3.6" for nudist/blind — fixes3-6-0.txt:1160.
- "5.0 added Pauper, Petless, Permadeaf, Sokoban, Bonesless" —
  all five appear as 5.0-tracked.

### Cross-section corrections (Bonesless section)
1. **"You can also get bonesless by luck"** — false. topten.c:605
   `add_achieveX(buf, "bonesless", !flags.bones)` requires bones loading
   to have been disabled (`!flags.bones`). Going a whole game without
   encountering bones because the dungeon directory had nothing eligible
   is reported as a separate Miscellaneous enlightenment line
   ("never encountered any bones levels", insight.c:439), NOT as the
   bonesless achievement. Rewrote the Bonesless paragraph.

2. **"Your `#conduct` screen also tracks whether you've used an amulet
   of life saving"** — false. show_conduct (insight.c:2089-2236) does
   NOT list lifesaving uses. Lifesaving count lives in u.umortality
   and is shown only by attribute enlightenment (insight.c:1977-2004)
   as "you have been killed N times" — a different display. Removed the
   paragraph entirely.


---

## 2026-05-17 — Chapter audit #53: Pacifist

Source: `spoilers/companion.md` line 6301
All claims verified against C source. 0 corrections.

### Verified
- "Don't kill any monsters — not directly, not with pets" — correct.
  u.uconduct.killer is incremented only by xkilled() (mon.c:3500) and the
  explicit "pet killed by trap you pushed it into" case (hack.c:2201).
  Pet kills via mhitm.c route through monkilled()/mondied() which do NOT
  increment killer. Conflict-induced fights also don't count.
- Conflict, Elbereth, pet combat all real and work as described.
- SPE_CHARM_MONSTER spell confirmed (objects.h:1352, spell.c:1522).
- Pacifist conduct displayed in show_conduct (insight.c:2144).

### Notes
- The section is unusually short (13 lines) and makes only verifiable,
  hedged claims. The audit prompt's red-herring questions (wand-of-digging
  collapse, sink dipping demons, foodless+pacifist viability, recommended
  classes, score impact) are not claimed in the text. Good restraint.

---

## 2026-05-17 — Chapter audit #54: Dragons `D`

Source: `spoilers/companion.md` line 7691
20 dragon rows + Chromatic + Ixoth verified against monsters.h.
1 corrected (applied to 2 rows).

### Verified
- All 10 baby variants (gray/gold/silver/red/white/orange/black/blue/green/
  yellow) at monsters.h:1341-1431. Shimmering correctly omitted as
  `#if 0 DEFERRED`.
- All 10 adult variants present with identical roster.
- Baby stats: Lvl 12, Spd 9, AC 2, MR 10, bite 2d6 — all rows match.
- Adult stats: Lvl 15, Spd 9, AC -1, MR 20 — all rows match.
- Adult attack lines (bite 3d8, claw 1d4 ×2) verified.
- All breath types/damage verified per color: gray 4d6 magic (AD_MAGM),
  gold 4d6 fire, silver 4d6 cold, red 6d6 fire, white 4d6 cold,
  orange 4d25 sleep, black 1d255 disint, blue 4d6 shock,
  green 4d6 poison (AD_DRST), yellow 4d6 acid.
- Chromatic Dragon: Lvl 16, Spd 12, AC 0, MR 30, AD_RBRE 6d6 + AD_SPEL
  + AD_SAMU claw 2d8 + bite 4d8 ×2 + sting 1d6, sees-invis, M2_STALK,
  no M1_FLY. monsters.h:3642-3656.
- Ixoth: Lvl 15, Spd 12, AC -1, MR 20, breath 8d6 fire, bite 4d8,
  spell, claw 2d4 ×2 (steal-amulet AD_SAMU).
- Green/Chromatic poisonous-corpse (M1_POIS) — correct in spoiler.
- "All except Chromatic fly" — verified (Chromatic lacks M1_FLY).
- Gold dragon "yellow" color — HI_GOLD = CLR_YELLOW (color.h:46).
- No "shimmering dragon" claims (correctly omitted).

### Corrected
1. **Silver dragon color "gray"** (both baby and adult rows). Wrong.
   DRAGON_SILVER = CLR_BRIGHT_CYAN per color.h:54. The map character
   actually displays as bright cyan. Fixed both rows to "bright-cyan".

### Close calls (not changed)
- Yellow dragon Notes "rare" — generation flag (G_GENO | 1) is same as
  every other adult dragon; "rare" is mild editorializing. Left.
- Yellow dragon also gives stoning resistance (MR_ACID | MR_STONE) —
  not noted, but the table doesn't surface MR flags either. Left.
- "Reflection bounces the ranged breath back" lead-in vs gray dragon's
  carve-out "Magic resistance helps; reflection doesn't" — there's a
  slight tension but the per-row note disambiguates. Acceptable.

### Notes
- Per-color DSM intrinsic effects (Blue=Fast, Black=Drain_resistance new
  in 5.0, etc.) are NOT claimed in this section — it links to Armor
  Tables for the details. Verified that do_wear.c:796-884 implements:
  black=EDrain_resistance, blue=EFast (with speed-change message),
  green=ESick_resistance, red=Infravision, gold=clear hallucination,
  orange=EFree_action, yellow=EStone_resistance (on top of base ACID_RES),
  white=ESlow_digestion. Audit those when the Armor Tables unit comes up.

---

## 2026-05-17 — Chapter audit #55: Jabberwocks `J`

Source: `spoilers/companion.md` line 7804
1 row verified clean. 1 correction (applied twice — prose + table notes).

### Verified
- jabberwock is the only Jabberwock-class monster (vorpal jabberwock at
  monsters.h:1815 is `#if 0 DEFERRED` and correctly omitted).
- Level 15, Speed 12, AC -2, MR 50, alignment 0, color orange.
- Attacks: 2× bite 2d10 + 2× claw 2d10.
- Flies (M1_FLY).
- Rare generation (G_GENO | 1).
- Vorpal Blade auto-behead vs PM_JABBERWOCK: artifact.c:1595-1623
  short-circuits the dieroll==1 check (mdef->data == &mons[PM_JABBERWOCK]
  forces beheading on every successful hit; damage = 2*mhp + FATAL_DAMAGE_MODIFIER).

### Corrected
1. **"Slow, tough, hits hard"** in prose + **"Powerful but slow"** in
   notes — wrong. Speed 12 is the player's baseline. Most level-15
   monsters (purple worm, all dragons) are speed 9, actually slower
   than the jabberwock. Reworded to "moves at player baseline speed:
   you can't simply walk away" / "Powerful; baseline speed."

---

## 2026-05-17 — Chapter audit #56: Vortices `v`

Source: `spoilers/companion.md` line 7563
6 rows × 8 cells verified clean against monsters.h:1053-1110.
2 prose corrections.

### Verified
- All 6 stats clean: fog cloud (3,1,0,0), dust (4,20,2,30), ice (5,20,2,30),
  energy (6,20,2,30), steam (7,22,2,30), fire (8,22,2,30).
- Colors correct (HI_ZAP→bright-blue for energy, etc.).
- All attack types/damage match: AD_PHYS / AD_BLND / AD_COLD /
  AD_ELEC+AD_DREN / AD_FIRE (×2).
- "fog cloud ... amorphous" — M1_AMORPHOUS only on fog cloud.
- "All vortices fly and are mindless" — all have M1_FLY | M1_MINDLESS.
- Implicit "no corpse" — every entry has G_NOCORPSE.

### Corrected
1. **Intro: "fire / cold / lightning / poison"** — false. No vortex
   deals poison. Actual types: physical (fog), blinding sand (dust),
   cold (ice), shock + Pw drain (energy), fire (steam, fire). Rewrote
   the damage-type list.

2. **"Stationary elemental clouds. They wait for you to step in."**
   — only fog cloud is slow (Spd 1). The other five move at speed
   20-22 and close on the player. Reworded.


---

## 2026-05-17 — Chapter audit #57: Eyes and spheres `e`

Source: `spoilers/companion.md` line 7276
Roster matches monsters.h:325-366 (beholder correctly omitted, #if 0).
All stats clean. 1 correction + 1 useful omission added.

### Verified
- 5 entries (gas spore, floating eye, freezing/flaming/shocking sphere)
  all match monsters.h. Colors, levels, speeds, AC, MR, attacks all clean.
- "All fly" — M1_FLY on every entry.
- "All except floating eye are mindless" — verified.
- Floating eye amphibious (M1_AMPHIBIOUS).
- Sphere resistances (MR_COLD / MR_FIRE / MR_ELEC) verified.
- Gas spore death-burst (AT_BOOM, mon.c:3199 "Gas spores always explode upon death").

### Corrected
1. **"Passive gaze paralyses if you melee in daylight"** — wrong. uhitm.c:6022-6053
   requires canseemon(mon) AND mon->mcansee — mutual sight, not light.
   Light conditions are irrelevant; what matters is that you can see it and
   it can see you. Reworded.

### Added (useful omission)
- Floating-eye corpse grants intrinsic telepathy (eat.c:1071 TELEPAT case).
  This is the most famous benefit of the monster and standard spoiler
  content. Added to both prose and table notes.

### Close calls (not changed)
- "0d70 paralyse" — when damn=0, the C code substitutes m_lev+1 (uhitm.c:5887),
  so actual roll is d(3, 70). Standard spoiler convention is to show the
  literal MON field. Left as is.

---

## 2026-05-17 — Chapter audit #58: Quadrupeds `q`

Source: `spoilers/companion.md` line 7477
7 rows × 8 cells verified against monsters.h:831-885. All stats clean.

### Verified
- All 7 rows (rothe, mumak, leocrotta, wumpus, titanothere, baluchitherium,
  mastodon) match LVL() macros exactly.
- Mumak attacks: butt 4d12 + bite 2d6 (NOT gore — uses AT_BUTT).
- Baluchitherium: M2_HOSTILE | M2_STRONG, not peaceful (rumor was a
  red herring; the spoiler makes no peaceful claim).
- Rothe 3-attack claim (claw + bite + bite) matches.

### Added
- "clings." note on wumpus row (M1_CLING — clings to ceiling, distinctive
  trait worth surfacing).

---

## 2026-05-17 — Chapter audit #60: Rust monsters and disenchanters `R`

Source: `spoilers/companion.md` line 7944
2 rows verified clean. Prose framing corrected.

### Verified
- rust monster: brown, lvl 5, spd 18, AC 2, MR 0, attacks
  touch/rust + touch/rust + passive/rust, M1_SWIM — all match monsters.h:2147.
- disenchanter: blue, lvl 12, spd 12, AC -10, MR 0, attacks
  claw 4d4 disenchant + passive disenchant — all match monsters.h:2154.
- Rust active erodes hero worn iron armor (mhitm_ad_rust → erode_armor,
  uhitm.c:2311). "Strip armor before engaging" correct.
- Rust passive on hero weapon when hero melees rust monster (uhitm.c:5958-5968).
  Greased weapons consume a grease charge instead of rusting.
- Silver/mithril/wood weapons immune (is_rustprone, trap.c:212).
- Disenchanter passive on hero weapon when hero hits (mhitu.c:2508-2515
  drain_item).

### Corrected
1. **"Disenchanters remove the enchantment off your +5 long sword"** —
   misframed. uhitm.c:3611-3644 mhitm_ad_ench active attack drains hero's
   **armor** first (some_armor + 5-way rn2(5) to ring/amulet/blindfold);
   never targets weapon directly. Weapon drain only happens passively
   (when you hit them). Reworded to be honest about which slot the
   active vs passive attacks target. Same correction in the table notes.

### Added
- "Gehennom-only" note on disenchanter (G_HELL | G_GENO | 2 — generation
  is restricted to Gehennom).

---

## 2026-05-17 — Chapter audit #61: Apelike creatures `Y`

Source: `spoilers/companion.md` line 8053
48 cells (6 rows × 8 columns) verified against monsters.h:2372-2417 + monattk.h.
0 corrections.

### Verified
- All 6 rows ordered by level (2/4/5/5/6/7).
- monkey: claw AD_SITM (steals item, monattk.h:63) + bite 1d3 — verified.
- ape, owlbear (hug AT_HUGS AD_PHYS 2d8), yeti, carnivorous ape, sasquatch
  all stat-clean.
- Yeti cold-res: MR_COLD on both resists+conveys; eat.c:912-913 confirms
  corpse grants COLD_RES.
- Sasquatch sees-invis: M1_SEE_INVIS (monsters.h:2415).
- Intro "Carnivore corpses are safe food" — owlbear/yeti/carnivorous ape
  are M1_CARNIVORE with no M1_POIS, no MR_POISON.

### Notes
- The prompt's "snow ape" hint was a red herring; no such monster in C.
  Spoiler correctly uses "carnivorous ape".


---

## 2026-05-17 — Chapter audit #62: Permadeaf (new in 5.0)

Source: `spoilers/companion.md` line 6437
2 intertwined corrections + cross-section sweep.

### Verified
- Conduct option `deaf` with alias `permadeaf` (optlist.h:267-269).
- "New in 5.0" supported by fixes5-0-0.txt:2842.
- Deaf macro = (HDeaf || EDeaf || u.uroleplay.deaf) (youprop.h:125).
- You_hear() early-returns when Deaf && !Unaware (pline.c:441).
- dosounds() early-returns under Deaf || !flags.acoustics (sounds.c:208).
- Conduct recorded in xlogfile (topten.c:602) and end-screen (insight.c:2113).

### Corrected
1. **"Set `OPTIONS=!acoustics` in your rcfile"** — wrong option. `acoustics`
   (flags.acoustics) is a separate world-acoustics flavor toggle; it does
   NOT set u.uroleplay.deaf and does NOT earn the permadeaf conduct
   (topten.c:602 only checks u.uroleplay.deaf). Changed to `OPTIONS=permadeaf`.

2. **"or `acoustics:false` in the in-game O menu"** — wrong on two counts:
   wrong option name AND not settable in-game. The deaf option is marked
   `set_in_config` (options.c:5207), so it cannot be toggled from the in-game
   O menu. Replaced with explicit note that this is rcfile/command-line only.

### Cross-section sweep — same set_in_config bug fixed in:
- **Pauper** section: "(or `pauper:true` in the in-game `O` menu)" — pauper
  is also set_in_config, not in-game settable. Removed.
- **Bonesless** section: "(or `bones:false` in the in-game `O` menu)" — bones
  is also set_in_config (optlist.h). Removed.

### Notes
- Nudist and Blind (Zen) sections at lines 6391-6398 use the vaguer "Set the
  X option at game start" phrasing, which is technically not wrong (it just
  doesn't mention in-game O menu in the first place). Left as is.

---

## 2026-05-17 — Chapter audit #63: Brainlessness

Source: `spoilers/companion.md` line 1948
2 substantive corrections.

### Verified
- Mind flayer 3 tentacles, master 5 + AT_WEAP 1d8 (monsters.h:523-535).
- AT_TENT/AD_DRIN; INT loss rnd(2) per hit; 5 hits = up to 10 (uhitm.c:3263).
- Brainlessness death at racial ATTRMIN(A_INT) = 3 for all 5 races (role.c).
- Amulet of life saving fires but second done(DIED) finishes you with
  "Unfortunately your brain is still gone" (eat.c:701-715).
- 1-in-5 losespells per hit (uhitm.c:3264); spell.c:1763-1800 sets
  retention to 0; restudy from spellbook to recover.
- 5.0 amnesia no longer wipes maps/IDs (forget() in read.c:1020 doesn't
  call docrt/forget_objects).
- Polymorph into mind flayer brain-eats for INT recovery up to AMAX
  (eat.c:679-688).

### Corrected
1. **"Wear a greased helmet to prevent tentacle attacks from connecting"**
   — misleading by omission. ANY helmet blocks 7/8 (87.5%) of brain
   attacks via `uarmh && rn2(8)` (uhitm.c:3235). Greasing is a separate
   slip-off roll on top. A reader following the original spec would think
   only greased helmets help, when an unenchanted orcish helm already
   blocks most. Rewrote to lead with "any helmet" then mention greasing
   as an additive bonus.

2. **"A blessed potion of full healing also restores ability scores"**
   — false. peffect_full_healing (potion.c:1144-1162) restores HP and
   one lost LEVEL if blessed; does NOT touch attributes. This was
   confusion with potion of restore ability. Removed the claim.

### Close calls (not changed)
- "Uncursed potion of restore ability restores one random ability" —
  it's "first damaged from random start index" (potion.c:662-676), not
  pure random. Functionally close; left as "one stat".
- 1-in-5 drain_weapon_skill also fires (uhitm.c:3268-3271) — not mentioned
  in spoiler; minor omission, left out for brevity.
- Dunce cap special case (uhitm.c:3247 skips eat_brains but INT drain
  happens anyway) — niche; left out.

---

## 2026-05-17 — Chapter audit #64: Atheist

Source: `spoilers/companion.md` line 6273
1 correction + 1 useful addition.

### Verified
- u.uconduct.gnostic tracks atheist conduct (insight.c:2134 "have been
  an atheist"; topten.c:590 atheist achievement).
- #pray breaks it (pray.c:2221 in dopray).
- #offer corpse at altar breaks it (pray.c:1977 in offer_corpse).
- #turn undead breaks it (pray.c:2426 in doturn).
- #chat with priest breaks it (priest.c:572 in priest_talk).
- Prayer's safety net: stoning, starvation, sickness/illness, curse
  trouble all in pray.c:206-224.

### Corrected
1. **"You can still use [altars] passively by dropping items on an altar"**
   — false. do.c:370 increments u.uconduct.gnostic when YOU drop any
   non-coin item on an altar (gating on !svc.context.mon_moving). The
   BUC flash IS a religious interaction by the conduct's reckoning. Only
   coins are exempt. Reworded to be explicit that altar BUC also breaks
   atheist.

### Added
- Final Amulet offering for ascension is **exempt**: offer_real_amulet
  (pray.c:1529-1588) bypasses the corpse path and does NOT increment
  gnostic. So a clean atheist ascension is mechanically possible. Added
  this since it's a non-obvious gameplay-relevant fact and likely the
  first question an atheist player asks.

### Close calls (not changed)
- Quest leader/nemesis interactions — no gnostic touches in any quest C
  code; accepting quest artifact doesn't break atheist. Spoiler doesn't
  claim otherwise. Left silent.
- Water-prayer (#dip on altar) — water_prayer() only called from inside
  prayer_done, so #pray already covers it. No separate concern.

---

## 2026-05-17 — Chapter audit #66: Light Bursts

Source: `spoilers/companion.md` line 2038
3 corrections.

### Verified
- Yellow light: AT_EXPL/AD_BLND, 10d20 turn blindness (monsters.h:1169-79;
  mhitu.c:1623-34).
- Black light: AT_EXPL/AD_HALU, 10d12 turn hallucination (monsters.h:1181-91;
  mhitu.c:1636-50).
- Black light perminvis (makemon.c:1317-20 sets perminvis/minvis on
  PM_BLACK_LIGHT); see invisible reveals.
- Both die in the explosion.
- Single-target only — no area effect.
- Unicorn horn cures both (probabilistically).
- Status wears off naturally (timeout.c:743-83 BLINDED/HALLUC).

### Corrected
1. **"(`y`, level 3-5)"** — read as a range per monster. Actually yellow
   light is level 3, black light is level 5. Split the two with their
   own level callout.

2. **"recover by drinking a potion of healing"** — too loose. Plain
   potion of healing cures blindness ONLY when blessed (potion.c:1994-2004);
   uncursed plain healing doesn't. Extra healing cures unless cursed;
   full healing always cures. Clarified.

3. **"Telepathy or warning helps you see black lights coming"** — wrong
   half. Black lights have M1_MINDLESS (monsters.h:1188-89), so telepathy
   does NOT sense them. Warning does. Split into "warning detects them
   through invisibility, but telepathy does not (they're mindless)".

### Close calls (not changed)
- "Invisible until they hit you" — they die in the same turn they attack,
  so seeing them via see-invisible is brief. Reworded for clarity.


---

## 2026-05-17 — Chapter audit #68: Choking

Source: `spoilers/companion.md` line 2124
Section was bare-minimum (5 lines). Rewrote for accuracy + AoS coverage.

### Verified
- Eating-while-satiated death (eat.c:248, 286 done(CHOKING)).
- Exact warning string "You're having a hard time getting all of it down" (eat.c:3314).

### Corrected
1. **"if you confirm, you're dead"** — overstated and conflates two
   things. The warning at uhunger >= 1500 fires automatically with NO
   prompt by default; a "Continue eating?" prompt only appears with
   `paranoid_confirmation:eating` enabled. Even past uhunger 2000,
   death isn't certain: Breathless creatures and Hungry players never
   choke from over-eating, and others have a 1/20 escape on first
   occurrence (eat.c:258-266).

### Added
- Amulet of strangulation path (timeout.c + can_be_strangled in mondata.c)
  — the OTHER common choking death and one the section bizarrely
  didn't mention. Take it off; magic resistance doesn't help; Breathless
  polymorph form escapes both eating-choke and AoS strangle.

---

## 2026-05-17 — Chapter audit #69: Quantum mechanics `Q`

Source: `spoilers/companion.md` line 7953
2 rows verified clean against monsters.h:2127, 2136. 1 corrected.

### Verified
- quantum mechanic: cyan, lvl 7, spd 12, AC 3, MR 10, claw 1d4 teleport (AD_TLPT).
- genetic engineer: green, lvl 12, spd 12, AC 3, MR 10, claw 1d4 polymorph (AD_POLY).
  New in 5.0 per fixes5-0-0.txt:2696. From slash'em per monsters.h comment.
- Both poisonous corpses (M1_POIS).
- Both self-teleport (M1_TPORT) — the "random movement" behavior.

### Corrected
1. **"All quantum mechanics teleport"** — overgeneralization. Only the
   quantum mechanic itself does (AD_TLPT). The genetic engineer in the
   same class polymorphs (AD_POLY) without teleporting on hit. Reworded
   to handle both species separately.

### Added (useful corpse effects)
- Quantum mechanic corpse toggles intrinsic Fast (eat.c:1227-1236).
- Genetic engineer corpse triggers polyself (eat.c:1247-1264).

---

## 2026-05-17 — Chapter audit #71: Genocide

Source: `spoilers/companion.md` line 2165
2 sentences, 1 factual claim, verified correct. 1 minor tightening.

### Verified
- "Confused scroll of genocide can genocide your own race" — confirmed at
  read.c:1737: for an uncursed scroll, do_genocide produces how=3
  (REALLY | PLAYER), do_genocide PLAYER branch at lines 2838-2842 sets
  mndx=u.umonster, killplayer++; the REALLY block at lines 2955-2989
  calls done(GENOCIDED) with killer="genocidal confusion".

### Tightened
- Added "uncursed" before "scroll of genocide while confused" — the
  self-genocide path only fires for **uncursed** confused scrolls
  (blessed routes to do_class_genocide, cursed has how=2 which skips
  the REALLY block).

---

## 2026-05-17 — Chapter audit #72: Pauper (new in 5.0)

Source: `spoilers/companion.md` line 6421
1 correction + useful pauper-compensation details added.

### Verified
- "No gold, no inventory, no armor, no starting weapon" — ini_inv
  short-circuits at u_init.c:1308-1309 for pauper; no items at all
  are generated.
- "Implicitly sets nudist" — options.c:5290-5293 cascades the option.
- End-of-game line "you started out without possessions" — insight.c:2117-2119.
- xlogfile achievement — topten.c:604.
- No gold-spending conduct counter (struct u_conduct has no such field).

### Corrected
1. **"Permanent conduct, set at birth and never lost"** — misleading.
   The pauper flag itself is permanent, but the cascading nudist flag
   IS cleared the moment you wear armor (worn.c:135-136). The
   end-screen "faithfully nudist" line will then stop printing.
   Reworded to distinguish: pauper is permanent; pauper-plus-nudist
   is yours to lose.

### Added
- Pauper compensations from pauper_reinit (u_init.c:870+): unspent
  weapon-skill slots = 2; one role-specific known spell/item (Wizard:
  force bolt; Healer: healing; Archeologist: touchstone; Rogue/Tourist:
  sack; Cleric: water; Samurai: gunyoki); supply chests on early
  dungeon levels. Without these the start would be unplayable; the
  spoiler omitted them entirely.

---

## 2026-05-17 — Voice cleanup pass

User flagged "too much reference to the code" in recent edits.
Stripped C-source jargon (function names, struct names, file:line refs,
flag macros like `AD_TLPT`, `M1_TPORT`, `set_in_config`) from visible
prose across: #62 Permadeaf, #63 Brainlessness, #68 Choking, #69
Quantum mechanics, #72 Pauper, plus the pre-existing #11 Drowning
oilskin bullet. All such references remain in the HTML-comment audit
badges (which are invisible to the reader but greppable for tracking).

Updated feedback_spoiler_voice.md memory with a stronger rule
explicitly listing examples of what NOT to leak into prose.

---

## 2026-05-17 — Chapter audit #46: What Changed Since Last Time

Source: `spoilers/companion.md` line 8297. Verified ~30 changes against
fixes5-0-0.txt + source. 4 corrected, several clarified.

### Verified (sample)
- Themed rooms, 4 new monsters, helm of caution, "crystal helmet"
  appearance for helm of brilliance, charm/sleep/confuse level shifts,
  unicorn horn no longer restores attributes, BoH scatter-not-destroy,
  Valkyrie starts with spear, Excalibur 1/30 (1/6 Knight), wand of
  speed monster now temporary, Demonbane silver-mace + guaranteed
  Priest gift, HP regen `(XL + Con) > rn2(100)` plus +1/turn from
  Regen intrinsic, 3/2 strength damage bonus on two-handed, covetous
  monsters warp to either staircase, Castle no master/arch-lich,
  hot-ground potion destruction in Gehennom, alchemy smock 1/30 blast,
  crystal armor staged cracking, candle sqrt radius, 4 new conducts.

### Corrected
1. **"Chain lightning is a new level 7 attack spell"** — wrong. Spell
   level 4 (objects.h:1410). Single shock bolt with line-up multi-hit,
   not "bouncing." Same bug also fixed in #59 Spellcasting table.

2. **"Mummies now cause withering instead of draining experience"** —
   fabricated. "Withering" doesn't exist anywhere in 5.0 C source.
   Mummies in 5.0 deal AD_PHYS (claw damage). Wraiths/vampires are
   the XP drainers, not mummies. Entire bullet removed.

3. **"Elbereth now incurs a −5 alignment penalty when you attack a
   monster while standing on it"** — the alignment penalty (mon.c:4280)
   is real but is NOT a 5.0 change; not listed in fixes5-0-0. The
   AIS-style comment in source suggests it predates 5.0. Removed as
   misattributed.

4. **"Supply containers ... on early dungeon levels"** — wrong scope.
   Real name is "supply chests" (mklev.c:1044). They appear only on
   levels ABOVE the Oracle (i.e., DLs 1 through ~5 typically), not
   on "the first ten levels." Reworded.

### Clarified (oversimplified, not wrong)
- "Mind flayers no longer cause amnesia" — the *map/identifications*
  amnesia is gone, but the per-hit chance of forgetting memorized
  spells and weapon-skill experience persists. Reworded.
- "Sink dipping" — applies only to potions (fixes line 2869), not
  "items or potions."
- "Loadstones confer steadfastness (resistance to forced movement)" —
  overstated. Only blocks knockback from combat attacks, not
  teleport/displacement/levitation. Reworded.

### Notes
- "Spell maintenance drains maximum power while memorized" — fabricated
  per #59 audit; removed earlier in this batch (the maintenance
  mechanic doesn't exist in 5.0 C source).

---

## 2026-05-17 — Chapter audit #47: Shopping and Shopkeeper Pricing

Source: `spoilers/companion.md` line 6478. 22-row gem table verified
clean; ~15 other claims verified; 1 corrected.

### Verified (highlights)
- All 22 gem prices, Mohs ratings, colors match objects.h:1526-1570.
- Hard-gem threshold (Mohs >= 8) per objects.h:19.
- Unidentified gem 3-8 zm sell range, formula `(tmp+3)*quan` per
  shk.c:3169 — varies by shopkeeper m_id.
- Shopkeeper anti-Elbereth in own shop (monmove.c:266) + see-invisible
  (shk.c:5302).
- Keystone Kops trigger on debt walkout (shk.c:510-562).
- "Closed for inventory" engraving only marks D_LOCKED doors (shknam.c:750).
- Orcus-level shopkeeper killed by Orcus, items ownerless (shknam.c:794).
- Pay for broken shop items (shk.c:5174).
- Unicorn luck: co-aligned identified real gem → change_luck(5);
  cross-aligned identified gem → rn2(7)-3 (i.e. -3..+3); glass never
  changes luck (dothrow.c:2309).
- Excalibur 16000 zm price example matches 4 × arti_cost(4000).
- Tourist/dunce-cap/visible-shirt buy ×4/3 and sell /3 vs /2
  (shk.c:2947, 3154).
- Credit/debit/loan ordering on drop-gold-in-shop (shk.c:3884).

### Corrected
1. **"Amethyst + booze dispels hallucination"** — wrong. potion.c:2161
   shows amethyst + booze → fruit juice (the "a-methyst" / "not
   intoxicated" pun). Doesn't touch hallucination. Per user feedback,
   dropped the alchemy bullet entirely (it's trivia, not gameplay-
   actionable) and cleared the table cell.

### Close calls (not changed)
- "Artifact items priced at 4x the artifact's already-large base cost"
  — easy to misread as "4× oc_cost" when it's "4× arti_cost"
  (arti_cost itself = 100× oc_cost or artilist override). Wording
  works as written.
- Glass-gem unidentified footnote: "0-8 zm" — the floor is actually 3
  for unidentified pricing (formula adds +3 baseline). Minor.

---

## 2026-05-17 — Chapter audit #48: Advanced Controls

Source: `spoilers/companion.md` line 5511. Most claims verified clean.
1 corrected.

### Verified
- Count prefix (LARGEST_INT cap, ESC cancels), example commands `10s`,
  `20.`, `5h` all work.
- Ctrl+A `do_repeat` last-executed-command behavior (cmd.c:1822).
- `F` force-fight prefix, `G` run, `g` rush, capital-letter run/rush
  shortcuts via MOVEMENTCMD + CMD_M_PREFIX (cmd.c:2043-2057).
- `m` prefix → menu_requested; commands with CMD_M_PREFIX honor it
  (`a`, `e`, `,`, `O`).
- Ctrl+P prevmsg, Ctrl+R redraw, Ctrl+O overview (#overview),
  #annotate (M-A or Ctrl+N), #chronicle (`v`).
- `O` opens doset_simple; `m O` opens full doset.
- number_pad is in-game settable (set_in_game); when on, `n` becomes
  count prefix.
- autopickup + pickup_types in-game settable.
- windowtype is set_gameview (config/startup only); align_message /
  align_status are curses-only.
- Travel `_`, look `;`, what-is `/` all confirmed.

### Corrected
1. **"`verbose` makes interrupted multi-commands tell you *why* they
   stopped"** — false characterization. flags.verbose controls extra
   descriptive messages (wielding/digging/sounds/pets), not multi-
   command interrupt messaging. Reworded.

### Close calls (not changed)
- "Counts up to 32,767 (five digits)" — true number; "five digits" is
  cosmetic. Cap is LARGEST_INT, not a digit count.
- "Ctrl+A remembers the last command that actually executed" — half
  right; doesn't filter "bumped against a wall" exactly. Acceptable.

---

## 2026-05-17 — Chapter audit #59: Spellcasting

Source: `spoilers/companion.md` line 4662. Substantial rewrite. Six
corrections, two fabrications removed.

### Verified
- Spell level lookups in objects.h: force bolt 1, healing 1, identify 3,
  magic mapping 5, finger of death 7, charm monster 5, detect monsters 1,
  remove curse 3.
- Spell retention KEEN = 20000 turns (spell.c:17).
- Wizard-only skill-based spellbook ID (spell.c:864) reveals appearances
  at unskilled/basic/skilled/expert per level-1/3/5/7.
- Wizards start P_BASIC in P_ATTACK_SPELL and P_ENCHANTMENT_SPELL
  (weapon.c:1768) → know level-3 appearances in those two schools.
- Reading formula: `Int + 4 + XL/2 − 2·level` vs rnd(20) (spell.c:582).
  Blessed books skip the check entirely (auto-success).
- Cursed books always fail (too_hard = TRUE at spell.c:578).
- Spellbook fades after MAX_SPELL_STUDY successful reads (spell.c:401).
- `a`pply shows ink fadeness in 5 stages (apply.c:4509).
- Pw cost = 5 × spell level (SPELL_LEV_PW macro, spell.h:36).
- Failed cast costs half energy (spell.c:1374).

### Corrected
1. **Force bolt "d6 to 4d6 by skill"** — false. Hard-coded d(2,12) =
   2-24, plus −3 to +3 Int/XL bonus via spell_damage_bonus (zap.c:205).
   Spell-school skill does NOT scale damage at all. Fixed in table.

2. **Chain lightning level 7** — wrong. Level 4 (objects.h:1410). Also
   "bouncing ray" is wrong; it's a single bolt that can hit multiple
   targets if they line up. Fixed in table.

3. **"Failed reading can paralyze you, summon hostile monsters"** —
   wrong on both. cursed_book enumerates teleport, take-gold, blindness,
   confusion, contact poison, exploding rune, rndcurse (spell.c:130).
   No paralysis, no summons. Reworded.

4. **"Each failed attempt damages the spellbook. Fail enough times and
   the book crumbles"** — backwards. spestudied increments on
   **successful** reads (spell.c:411); book fades after MAX_SPELL_STUDY
   successes. Failures use a single 1-in-3 destruction roll
   (spell.c:612), no per-failure wear counter.

5. **"Spell maintenance system: known spells drain max Pw while
   memorized"** — fully fabricated. No such mechanic in spell.c.
   Each spell decays its own sp_know one per turn but does NOT touch
   uen or uenmax. Paragraph removed.

6. **"Energy Vortex trick: let one hit you while carrying an amulet
   of reflection, increases max power"** — fully fabricated.
   drain_en (trap.c:5202) only ever DECREASES uen/uenmax; no
   reflection branch. Paragraph removed.

7. **"Blessed spellbooks add a bonus (equivalent to a few points of
   Intelligence)"** — overhedged. Blessed books bypass the entire
   read-ability check (spell.c:577) — auto-success, not a soft bonus.
   Reworded.

### Notes
- "Cursed books always punish you" — close to right but the
  exploding-rune case is prevented by Antimagic (spell.c:170), and
  rndcurse can no-op if you have nothing curseable. Left as-is.


---

## 2026-05-18 — Chapter audit #65: Your First Descent

Source: `spoilers/companion.md` line 372. Mostly clean. 2 corrected.

### Verified (sample)
- Floating eye paralysis, lichen/lizard corpses never rot, lizard cures
  stoning, pets avoid cursed items, killer bee swarms + poison sting,
  prayer rejected in Gehennom, supply chests above Oracle 2/3 chance,
  hunger states ordering, prayer trouble triggers.

### Corrected
1. "Little dog or kitten" framing — Knight starts with pony; trimmed to
   generic "starting pet" per voice rules.
2. "Tumble and take significant damage" on overburdened stair fall —
   actually rnd(3) = 1-3 HP. Reworded to "annoying rather than dangerous."

### Close calls (not changed)
- Corpse age limits (50 / 150 turns) — actual guarantee at age 175 for
  uncursed (145 cursed). Acceptable for prose.

---

## 2026-05-18 — Chapter audit #67: Gehennom

Source: `spoilers/companion.md` line 5007. Largely well-grounded. 3 corrected.

### Verified (extensive)
- Valley of the Dead layout/contents (valley.lua).
- Prayer-in-Gehennom failure (pray.c:2307).
- Hot ground potion shatter (do.c:318 + mklev.c:898 temperature=1).
- Demon-lord-suppressed teleport (teleport.c:30).
- Bribery formula (minion.c:310 demand = cash * (rn(80)+20*Athome) /
  (100*(1+matching_align))).
- bag-of-holding gold-hiding trick (money_cnt only counts top-level coins).
- Vlad's Tower structure, special throne 13 effects with 4/13 wish.
- Orcus Town ghost-town design + 50/50 magic lamp/marker.
- Wizard of Yendor harassment (resurrect, intervene, summon nasties).
- Quest nemesis carries Bell of Opening (makemon.c:1378).
- 7 candles for Candelabrum.
- Astral entry gated by Amulet (do.c:1505).

### Corrected
1. **Asmodeus / Baalzebub level numbers** — chapter mixed mexp (XP
   reward) with mlevel (monster level), giving wrong numbers (53/56
   for Asmodeus/Baalzebub when those are mexp not mlevel; Baalzebub's
   mlevel is 89). Dropped the parenthetical numbers entirely — they
   add noise and the resistances/abilities matter more.
2. **"Asmodeus is the deepest of the three by base depth"** — wrong.
   Baalzebub has base offset 6 (vs Asmodeus 2) per dungeon.lua,
   making Baalzebub deeper on average. Reworded to drop the depth
   ranking.
3. **"All three [Asmodeus/Juiblex/Baalzebub] bribable on the same
   terms"** — wrong. Per monst.c, only Geryon/Dispater/Baalzebub/
   Asmodeus have MS_BRIBE. Juiblex has MS_GURGLE and is NOT bribable
   (nor are Yeenoghu, Orcus, Demogorgon). Reworded to spell out who
   accepts gold and who doesn't.
4. **"You cannot leave the Sanctum without the Amulet: the up-stair
   refuses to lift you out empty-handed"** — false. Sanctum's
   up-stair is a normal staircase (sanctum.lua:130 des.stair("up",...));
   the Amulet gate is on entering the Endgame Planes (do.c:1505).
   Reworded.

### Close calls (not changed)
- "Wizard's Tower is three sequential Gehennom levels reached by
  normal down-stair" — wizard1 is via Gehennom down-stair; wizard2/3
  are chainlevels with portals. Simplification, but acceptable.
- "Acid damage in eighty-HP gulps" — actually rnd(80) so 1-80 (or
  rnd(16) with acid res). Loose but fine.

---

## 2026-05-18 — Chapter audit #70: Flail

Source: `spoilers/companion.md` line 6874. Flail stats clean.

### Verified
- flail damage 1d6+1 / 1d4+1d4 (oc_wsdam=6 + tmp++ small; oc_wldam=4
  + rnd(4) large per weapon.c:239,272). Weight 15, cost 4, iron,
  one-handed, hitbon=0. All match objects.h:384-386.

### Added (per audit)
- Grappling hook row (P_FLAIL skill, but a WEPTOOL — appears in tools
  not weapon class). Sdam 1d2 / Ldam 1d6, wt 30, cost 50, iron.
  `#apply` mechanic pulls a target toward you. Important to include
  in the Flail skill subsection so readers training the skill see
  all weapons that train it.

### Improved
- Notes column: was "+1d4 large; one-handed". Now "+1 small, +1d4
  large; one-handed" for consistency with adjacent class entries
  (morning star, hammer) that show both bonuses.

---

## 2026-05-18 — Chapter audit #73: Enchantment Drain

Source: `spoilers/companion.md` line 2017. Substantial rewrite. The
section's active-vs-passive framing was inverted.

### Verified
- Disenchanter is `R` blue (monsters.h:2161).
- Active claw drains 1 enchantment per hit (drain_item, zap.c:1382-1405).
- 9/10 artifact resist + 1/10 ordinary resist via obj_resists(obj, 10, 90).
- Invocation items + Rider corpses always resist (zap.c:1387-1391).
- Magic cancellation defends against active attack only
  (mhitm_mgc_atk_negated, uhitm.c:3613).
- Eating disenchanter corpse calls attrcurse() to strip a random
  intrinsic (eat.c:1270-1275).
- Gehennom-only generation: G_HELL flag (monflag.h:0x0400) means
  "generated only in hell"; makemon's else branch in is_not_in_hell
  blocks G_HELL monsters from main dungeon. (Wiki cross-check
  mentions deep-dungeon spawns; that's stale 3.6 info — 5.0 C is
  strict Gehennom-only for random gen.)

### Corrected (major)
1. **"Each hit picks a random charged or enchanted object (including
   artifact weapon, dragon scale mail)"** — wrong. mhitm_ad_ench
   active path (uhitm.c:3608-3645) uses some_armor() — returns ARMOR
   only (cloak > suit > shirt; helm/gloves/boots/shield by 1/4 chance).
   If no armor at all, falls back to 5-way rn2(5) for ring/amulet/
   blindfold or nothing. The active claw NEVER targets your wielded
   weapon.
2. **"Damage is invisible during the fight (no announcement)"** —
   wrong for active. mhitm_ad_ench prints "Your <thing> seems less
   effective" (uhitm.c:3641). The "no message" comment in C is on
   the PASSIVE counter (mhitm_ad_ench mhitm/uhitm branches).
3. **"Three or four hits will take a +7 sword to +3"** — only via
   passive when YOU melee them (mhitm.c:1351-1354, mhitu.c:2509-2514).
   The active attack alone never touches the sword.

### Added
- Gehennom-only generation note.
- Magic-cancellation defense for active claw.
- Corpse-eating warning (strips intrinsic).
- Conflict-and-pet redirect strategy.

### Wiki cross-check note
- Wiki at nethackwiki.com/wiki/Disenchanter says "deeper levels of
  the dungeons and in Gehennom" — that's 3.6 behavior, not 5.0.
  G_HELL is strict in 5.0 source.
- Wiki agrees on passive-weapon, MC defense, corpse intrinsic strip,
  active-armor-targeting. Wiki was vague on the active vs passive
  message distinction; C is explicit (active = "less effective"
  message, passive = silent).


---

## 2026-05-18 — Chapter audit #74: Finding Secret Doors

Source: `spoilers/companion.md` line 1312. Mostly accurate; 2 prose fixes.

### Verified
- Search radius 1 (all 8 adjacent squares; detect.c:2033).
- Stride-3 gives full coverage with no overlap (geometric).
- 15-22 searches for "reliable" at Luck 0 with p=1/7 per try.
- Lenses +2 to fund (detect.c:2029, must be worn and not blind).
- Wand of secret door detection is a radius reveal (zap.c:2552 → findit).
- Blessed magic mapping reveals every secret door on level (read.c:2121).

### Corrected
1. **Excalibur (if wielded) improves search chances** — underspecified.
   Real mechanic: uwep->spe adds to the search bonus, capped at +5.
   A freshly-dipped +0 Excalibur adds nothing. Same for any artifact
   with the searching aura. Reworded.
2. **"Lenses (any kind, if worn)"** — there's only one kind of LENSES.
   Removed "any kind".

### Close calls (not changed)
- "Ring of searching auto-searches every turn you move" — actually
  every moveloop turn while multi >= 0, including waiting. Loose
  enough that "every turn while worn" works.

---

## 2026-05-18 — Chapter audit #75: Xorns `X`

Source: `spoilers/companion.md` line 8090. Stats clean; prose had 2 errors.

### Verified
- Single row "xorn" present in S_XORN (monsters.h:2357-2366).
- LVL(8, 9, -2, 20, 0), color brown.
- Attacks: claw 1d3 ×3 + bite 4d6.
- MR_FIRE | MR_COLD | MR_STONE resistances.
- M1_METALLIVORE eats metal floor items (monmove.c:1664).

### Corrected
1. **"Tunnel through rock"** — false. Xorns have M1_WALLWALK (phase
   through walls without rubble), NOT M1_TUNNEL. Reworded.
2. **"Your weapons and armor are at risk on touch"** — false. Xorn
   attacks are AD_PHYS only. Metallivore behavior only eats metal off
   the floor, never worn/wielded gear. Removed the false warning.

### Added
- Corpse grants temporary stoning resistance (only intrinsic in mconveys
  for xorn).

---

## 2026-05-18 — Chapter audit #76: Mimics `m`

Source: `spoilers/companion.md` line 7447. Verified clean.

### Verified
- 3 rows (small/large/giant) all match monsters.h:670-698.
- M1_AMORPHOUS | M1_HIDE | MR_ACID on all three.
- AD_STCK on large + giant; M2_STRONG on large + giant.
- set_mimic_sym disguise mechanics: STRANGE_OBJECT in shops at sufficient
  depth (makemon.c:2469), shop items in shops, gold in zoos, fountains
  in Delphi, items/walls/statues/boulders broadly.

### 0 corrections.

---

## 2026-05-18 — Chapter audit #77: Provisions and Dining

Source: `spoilers/companion.md` line 3028. Substantial corrections.

### Verified (sample)
- Hunger states + thresholds named correctly (hack.h:565-571, eat.c:3369).
- Food nutritions: ration 800, cram 600, lembas 800, tripe 200, apple 50.
- Cannibalism penalty: change_luck(-rn1(4,2)) + HAggravate; CAVEMAN/ORC exempt.
- Lizard corpse cures stoning (eat.c:3941).
- Newt corpse may restore 1-3 mana (eat.c:1103).
- Wraith corpse → +1 XP level (pluslvl).
- Stalker → invis + see-invis.
- Slow digestion mechanic (eat.c:3174).
- Tin opener vs dagger vs bare-hand timing.

### Corrected
1. **Gelatinous cube resistances** — granted only fire/cold/shock/sleep
   (mconveys = MR_FIRE|MR_COLD|MR_ELEC|MR_SLEEP). Was claiming also
   poison/acid/stoning. Fixed.

2. **Disenchanter "Intrinsic protection"** — opposite of truth. Eating
   disenchanter calls attrcurse() to STRIP a random intrinsic
   (eat.c:1270). Fixed with explicit "never eat" warning.

3. **Hunger threshold table off-by-one.** C uses strict `>` at 1000,
   150, 50, 0 (eat.c:3369-3372). Was: 150-999 Normal, 50-149 Hungry,
   0-49 Weak, "Below 0" Fainting. Corrected to 151-1000 Normal,
   51-150 Hungry, 1-50 Weak, "0 or below" Fainting.

4. **Encumbrance threshold.** Was "burdened or worse"; real C check
   is `near_capacity() > SLT_ENCUMBER` (eat.c:3197), i.e., stressed
   or worse. Burdened alone is free. Fixed.

5. **Fire giant / fire ant** were conflated in one row. Fire giants
   additionally grant Strength on eat (is_giant). Split the row.

6. **Red mold / Brown mold** also grant poison resistance (MR_POISON
   in mconveys for both). Added.

7. **Eggs as vegan-safe** — wrong. Eggs are FLESH material
   (eat.c:2998); vegans can't eat them. Split the paragraph to
   distinguish vegetarian (eggs OK) from vegan (rations/lembas/fruits/
   plant corpses only).

### Close calls (not changed)
- "Blessed tins open instantly" — actually 50/50 (rn2(2)). Acceptable
  shorthand.
- "Tengu corpse → teleportitis/teleport control" — also can grant
  poison resistance. Not noted.


---

## 2026-05-18 — Chapter audit #78: Long sword

Source: `spoilers/companion.md` line 6823. Stats clean; 2 prose fixes
+ 1 critical adjacent bug.

### Verified
- long sword 1d8 / 1d12, wt 40, cost 15, iron — objects.h:270-272.
- katana 1d10 / 1d12, wt 40, cost 80, hitbon +1 — objects.h:278-280.
- Both P_LONG_SWORD skill.
- Excalibur XL5+ + Knight 1/6 / others 1/30 (fountain.c:404-405).

### Corrected
1. **"1-in-30; 1-in-6 for Lawful Knights"** — misleading. The 1/30
   roll fires for any alignment at XL5+; non-Lawfuls who roll
   succeed get their sword cursed instead (fountain.c:411-424).
   Reworded to be honest about the bad outcome for non-Lawfuls.
2. **Artifact forms** — listed only Excalibur. Long sword has four
   (Excalibur, Vorpal Blade, Frost Brand, Fire Brand per artilist.h).
   Listed all.

### Critical adjacent bug fixed
- **Two-handed sword row claimed "Vorpal Blade is the artifact form"**
  — wrong. Per artilist.h:191, Vorpal Blade is a LONG_SWORD artifact.
  Two-handed sword has no dedicated artifact form. Fixed.

---

## 2026-05-18 — Chapter audit #79: Use-Testing (The Careful Way)

Source: `spoilers/companion.md` line 2828. Substantial rewrite —
the engrave-test table had multiple fabricated messages.

### Verified
- Cursed wand can explode on engrave (5.0 mechanic).
- Pet refuses to walk over cursed items (dogmove.c:535).
- Ring on-equip immediate effects (levitation, invisibility, gain Str).
- Armor / cloak / glove / boot appearance pools and prices match objects.h.
- Throwing potions at monsters identifies via effect.

### Corrected — Engrave-test table (per engrave.c)
1. WAN_FIRE — was "engraving catches fire"; actual: "Flames fly from
   the wand."
2. WAN_COLD — was "covered in frost"; actual: "A few ice cubes drop
   from the wand."
3. WAN_LIGHTNING — was "Lightning strikes the engraving"; actual:
   "Lightning arcs from the wand." May blind.
4. WAN_DIGGING — was "floor riddled by holes"; that's the MAGIC_MISSILE
   message. Actual digging: "Gravel flies up from the floor."
5. WAN_SECRET_DOOR_DETECTION — no "smudged" message; calls findit() with
   standard detection feedback.
6. WAN_CREATE_MONSTER — wasn't "bugs appear"; the wand summons real
   monsters via create_critters (zap.c:2571).
7. WAN_POLYMORPH vs WAN_TELEPORT vs cancellation/invis — was split into
   two rows ("in the floor is gone" vs "vanishes"). Per engrave.c:670-678
   all four produce the SAME message ("Your engraving vanishes"), and
   polymorph actually RANDOMIZES the existing engraving (different
   mechanic). Reworked.
8. **WAN_WISHING engrave** — was "does nothing special, just uses a
   charge; do NOT engrave with it." **Reversed in 5.0**. zap.c:2575-2585
   shows engrave with wishing calls makewish() (unless Luck+rn2(5)<0
   gives "Unfortunately, nothing happens"). Added a row that says
   to engrave-test the suspected $500 wand.

### Corrected — Other prose
9. **Unicorn horn neutralization** — was "confusion, hallucination, or
   sickness → water." Per potion.c:2153-2158: confusion → water,
   hallucination → water, **blindness → water**, **sickness → fruit
   juice**. Spoiler got sickness wrong and omitted blindness. Fixed.
10. **Confused remove curse "will *curse* items instead"** — misleading.
    blessorcurse(obj, 2) randomizes BUC of *uncursed* items (50/50
    bless/curse) and leaves already-cursed items cursed. It's a 50/50
    re-roll, not strict cursing, and it doesn't uncurse anything.
    Reworded.

### Notes
- "BEAM wands" category label was non-canonical (C uses NODIR/IMMEDIATE/
  RAY). Tightened the row to describe what readers will actually see.
- Dipping poisonable-only weapon caveat (long sword can't be poisoned).

---

## 2026-05-18 — Chapter audit #80: Lights `y`

Source: `spoilers/companion.md` line 7668. Table clean; 1 prose fix.

### Verified
- Yellow light: yellow, lvl 3, spd 15, AC 0, MR 0, AT_EXPL/AD_BLND 10d20.
- Black light: black, lvl 5, spd 15, AC 0, MR 0, AT_EXPL/AD_HALU 10d12.
- Both fly, amorphous, mindless. Black has M1_SEE_INVIS.
- Black light is perminvis (makemon.c:1317).

### Corrected
1. **"Yellow light bursts on death and blinds you (10d20 damage if
   unresistant)"** — wrong. Per mhitu.c:1623-1634, AD_BLND passes
   d(10,20) as the **blindness duration** to make_blinded(); there is
   no HP damage. Reworded to "blinds you for 10d20 turns / hallucinates
   for 10d12 turns" matching the #66 Light Bursts section.

---

## 2026-05-18 — Chapter audit #81: The Lay of the Land

Source: `spoilers/companion.md` line 509. 20 numeric claims verified
clean against dungeon.lua + branch lua files.

### Verified
- DoD 25-30 levels (base=25, range=5).
- Castle bottom of DoD.
- Gnomish Mines branch DL 2-4 (base=2, range=3).
- Sokoban goes UP from entry (direction="up").
- Sokoban 4 levels × 2 variants (nlevels=2 each).
- Oracle DL 5-9 (base=5, range=5).
- Big Room 40% chance (chance=40).
- Rogue Level DL 15-18 (base=15, range=4).
- Mine's End 3 variants with guaranteed luckstone.
- Quest portal DL 11-16 (chainlevel="oracle" base=6 range=2: 5+6=11 min,
  9+(6+2-1)=16 max).
- Fort Ludios portal DL 18-22.
- Medusa near bottom of DoD ~DL 21-25.
- 4 Medusa layouts.
- Perseus statue loot: 75% cursed shield of reflection, 50% blessed +2
  scimitar, 25% levitation boots, 50% sack.
- 1-in-7 Orcish Town in Minetown (7 minetn-*.lua variants).

### 0 corrections.


---

## 2026-05-18 — Chapter audit #82: The Art of Combat

Source: `spoilers/companion.md` line 4481. Mostly accurate; 3 fixes.

### Verified
- find_roll_to_hit factors (XL, weapon spe, Luck sgn-based, Str abon,
  monster AC find_mac) per uhitm.c:365-427.
- dbon() caps Str bonus at +6 for Str 25 (weapon.c:993).
- Two-handed weapon Str bonus is 3/2 (50%) per uhitm.c:1467.
- Conflict scales by Cha-Lvl per resist_conflict (mondata.c:1610).
- Conflict requires monster sees you (mon.c:1306).
- Shields forbidden with two-weapon (wield.c:789).

### Corrected
1. **Two-weapon roles wrong.** "High skill caps in it (Rangers,
   Barbarians)" — Rangers cannot two-weapon at all in 5.0 (no
   P_TWO_WEAPON_COMBAT entry in u_init.c:440-466). Barbarian caps at
   P_BASIC. Actual Expert roles: **Rogue** and **Samurai**. Valkyrie
   and Knight cap at Skilled. Reworded.
2. **Penalty framing.** "Splits your skill bonuses" — actually a flat
   negative replacement table: −9/−7/−5/−3 to hit, −3/−1/0/+1 damage
   from Unskilled through Expert (weapon.c:1578-1700). Reworded.
3. **Luck "up to +5 or -5"** — confused. LUCKMAX/LUCKMIN = 10
   (you.h:467); luckstone adds 3. The to-hit *contribution* caps
   around ±5, but Luck itself ranges further. Clarified.

### Close calls (not changed)
- "10 + AC - modifiers" formula — pedagogical approximation, real C
  uses rnd(20) vs sum-of-modifiers. Workable.
- "Strength +6 for STR 18/xx or more" — +6 requires STR 25 (post 18/99).
  Mildly misleading; the "or more" hedge covers it.

---

## 2026-05-18 — Chapter audit #83: Wishing Restrictions

Source: `spoilers/companion.md` line 6391. Useful additions.

### Verified
- u.uconduct.wishes + u.uconduct.wisharti two separate counters
  (you.h:157-158, topten.c:596).
- Wish sources: wand (zap.c:2583), fountain via water demon
  (fountain.c:82), smoky potion djinni (potion.c:2845), throne
  (sit.c:110, 251), wizard mode (wizcmds.c:38).

### Added
- **Amulet of Yendor first-pickup wish** (allmain.c:445) — wishless
  conduct requires declining this with "nothing." Standard escape
  hatch for any forced wish.
- Denied artifact wishes still increment u.uconduct.wisharti
  (objnam.c:5364 increments before the denial check), so
  artiwishless players need to be sure the artifact is obtainable.

---

## 2026-05-18 — Chapter audit #84: Worms `w`

Source: `spoilers/companion.md` line 7639. 4 rows × 8 cells verified
clean against monsters.h:1114-1145. Added "drops worm tooth" note to
adult long worm (mon.c:619).

---

## 2026-05-18 — Chapter audit #85: Ogres `O`

Source: `spoilers/companion.md` line 7952. 3 rows (ogre/lord/king)
verified clean against monsters.h:2052-2075.

### Corrected
1. **"Ogre kings throw boulders"** — false. Ogres lack M2_ROCKTHROW;
   that's giants/Cyclops/ettins/titans. Ogres wield weapons. Removed.


---

## 2026-05-18 — Chapter audit #86: Choosing Your Expedition

Source: `spoilers/companion.md` line 132. Many role/race/alignment
claims correct; 6 substantive corrections.

### Verified (sample)
- All role × race × alignment combos vs role.c roles[] allow masks.
- Race stat caps, female-only restrictions, infravision/sleep res for races.
- Mjollnir/Cleaver/Demonbane/Excalibur/Magicbane/Snickersnee role tags.
- Demonbane is silver mace in 5.0 (artilist.h:162).
- Excalibur dip 1/6 Knight vs 1/30 others (fountain.c:405).
- Stethoscope monster HP / self status (apply.c:380).
- Tourist surcharge under MAXULEV/2 (shk.c:2949).

### Corrected
1. **Elf "see invisible from the start"** — wrong. No race grants
   see-invisible. attrib.c shows only HInfravision at level 1;
   HSleep_resistance comes at level 4. Reworded.
2. **Knight "alignment penalty for attacking fleeing or peaceful"** —
   wrong. uhitm.c:336 penalizes attacking *helpless* or *fleeing*
   (check_caitiff); attacking peacefuls is the Samurai's giri penalty.
   Fixed. Also added Knight intrinsic jumping (u_init.c:691).
3. **Healer "can see whether potions of sickness are safe"** — wrong.
   Healers are *immune* to sickness (potion.c:977); they can safely
   quaff-test unknown potions of sickness. Reworded.
4. **Wizard starting inventory** — was "quarterstaff and a spellbook
   or two." Per u_init.c:167 they also start with **cloak of magic
   resistance** (endgame-quality), wand, 2 rings, 3 potions, 3 scrolls,
   force-bolt spell + random spellbook, high-enchantment magic marker.
   Added.
5. **Ranger starting inventory** — was "bow and a generous supply of
   arrows." Per u_init.c:124 they also start with a dagger and a
   **+2 cloak of displacement**. Added. Also corrected "stealth and
   see invisible early" — Stealth at XL 7, See Invisible at XL 15.
6. **Cave Dweller "club and some rocks for throwing"** — misleading.
   Per u_init.c:68 starting kit is club + **sling** + flint stones +
   rocks + leather armor. Fixed.

---

## 2026-05-18 — Chapter audit #87: Illiterate

Source: `spoilers/companion.md` line 6362. 1 correction + reorg.

### Verified
- u.uconduct.literate counter (you.h).
- Scroll reading triggers (read.c:602) with SCR_BLANK_PAPER, SCR_MAIL,
  SPE_BOOK_OF_THE_DEAD exempt.
- Spellbook reading triggers (same line, oclass == SPBOOK_CLASS).
- Fortune cookies + T-shirts trigger (eat.c:2525, read.c:397).
- Hawaiian shirts and floor engravings do NOT trigger.
- Pet-on-scroll workaround for the conduct (pet stepping doesn't
  increment literate — but stepping doesn't trigger the scroll
  either, so it's not a generally useful workaround).

### Corrected
1. **"You can still write (engraving is fine)"** — false. Per
   engrave.c:1213, engraving anything more than a single "x" or
   "X" (the traditional illiterate's signature) breaks the conduct.
   Reworded.

### Removed
- A bogus "pet stepping on a scroll of teleportation triggers it"
  workaround. Pets stepping on scrolls doesn't trigger the scroll's
  effect; monster scroll use goes through muse.c (pickup + active
  use), not the step itself.

---

## 2026-05-18 — Chapter audit #88: Blessed, Uncursed, Cursed

Source: `spoilers/companion.md` line 2449. 3 substantive corrections.

### Verified
- Altar BUC test mechanism (do.c:doaltarobj amber/black/no-flash).
- Priest BUC sense (objnam.c:629).
- Cursed armor sticks (do_wear.c).
- Cursed gain-level rises through ceiling (potion.c:1083).
- Blessed luckstone +luck; cursed -luck (attrib.c:423).
- Holy/unholy water dipping (potion.c:1498).
- Pet BUC test (dogmove.c probabilistic avoidance).

### Corrected
1. **"A blessed scroll of identify generously reveals every item in
   your pack"** — overpromising. Per read.c:2086, blessed scroll IDs
   at least 2 items (more with positive Luck), with only a 1-in-5
   chance to ID the whole pack. Corrected here and in the later
   detail paragraph.

2. **"A cursed one grudgingly identifies a single item"** — wrong in
   the common case. Per read.c:2074, a cursed scroll IDs only itself
   the first time you read one of that type, then one item per
   subsequent cursed read. Corrected.

3. **"A cursed scroll of teleportation sends you somewhere terrible"**
   — loose. Per read.c:2021, cursed teleport scroll triggers a
   **level** teleport (random dungeon level), not "somewhere terrible
   on the current level." Reworded.

### Added
- How to make holy water (pray on a co-aligned altar with potions of
  water in inventory). The section noted it was "precious" but never
  explained the creation path.

---

## 2026-05-18 — Chapter audit #89: Orcs `o`

Source: `spoilers/companion.md` line 7507. 8 rows verified clean
against monsters.h:727-796 (full S_ORC coverage). 1 corrected.

### Verified
- goblin (S_ORC, not S_GNOME), hobgoblin, orc, hill orc, Mordor orc,
  Uruk-hai, orc-captain, orc shaman — all stats, colors, MR_POISON.
- HI_LORD (CLR_MAGENTA) for orc-captain; HI_ZAP (CLR_BRIGHT_BLUE)
  for orc shaman.

### Corrected
1. **orc shaman "spell spell" (2 attacks)** — wrong. Per monsters.h:779,
   only one ATTK(AT_MAGC, AD_SPEL); the other 5 slots are NO_ATTK.
   Changed to a single "spell".


---

## 2026-05-18 — Chapter audit #90: Sling

Source: `spoilers/companion.md` line 7060. Stats clean. 1 correction.

### Verified
- sling wt 3, cost 20, leather, hitbon 0 — objects.h:403.
- BOW macro hardcoded 1d2 melee (consistent with bow/crossbow "—" notation).
- Caveman starts with one sling (u_init.c:70).

### Corrected
1. **"Trains sling skill from any rock you pick up"** — false. Per
   weapon.c:1750 comment, ammo alone doesn't train skill (explicitly
   prevents touchstone-Archeologist from giving sling skill).
   Training requires hits while wielding the sling.

---

## 2026-05-18 — Chapter audit #91: Jellies `j`

Source: `spoilers/companion.md` line 7439. 3 rows verified clean
vs monsters.h:591-620.

### Added
- Corpse-intrinsic notes: blue jelly = cold + poison res; spotted/ochre
  = temporary acid + stone res (per eat.c mconveys).

---

## 2026-05-18 — Chapter audit #92: Searching and Detection

Source: `spoilers/companion.md` line 1277. 1 correction + clarification.

### Verified
- `s` searches for hidden monsters, traps, secret doors, secret corridors
  (detect.c:2016-2093).
- Luck improves search via rnl bias (rnd.c:112).
- Pets avoid known traps with 39/40 chance (monmove.c:2287).
- Flying/levitation skip most floor traps.

### Corrected
1. **"Wand of secret door detection reveals traps in its path"** — wrong
   directional framing. WAN_SECRET_DOOR_DETECTION is NODIR (objects.h:1451);
   findit() reveals everything hidden in a square radius (BOLT_LIM) around
   the player: SDOOR, SCORR, traps, trapped chests, hidden mimics.
2. Clarified: artifact/lenses search bonus (the rnl(7-fund) path) only
   speeds up secret-door / secret-corridor discovery, not trap finding
   (which uses rnl(8) without fund).
3. Added: Flying/levitation immune to *most* floor traps but not magic,
   teleport, or anti-magic traps.

---

## 2026-05-18 — Chapter audit #93: Delayed Deaths

Source: `spoilers/companion.md` line 2212. Substantial corrections.

### Verified
- Sliming cure paths (timeout.c:448 burn_away_slime; pray.c:385).
- Food poisoning message (potion.c:154 "You feel deathly sick.").
- Eucalyptus cures both food poisoning and vomiting (eat.c:2576).
- Unicorn horn + prayer cure sickness/strangulation/lava.
- Strangulation timer 6 turns (do_wear.c:1036).
- Fire-resistant hero takes 1 HP/turn in lava but doesn't boil-away
  (trap.c:6965).
- Withering correctly absent (doesn't exist in 5.0 C source).

### Corrected
1. **"Change form via polymorph" cures sliming** — partially wrong.
   Per polyself.c:842, polymorph only cures sliming if you become a
   flaming form OR a green slime; a casual polymorph into a giant rat
   doesn't. Clarified.
2. **"Burdened, you may not get even one turn" + "stay unburdened
   near water"** for drowning — duplicates the error already fixed in
   the main Drowning section. Drown check uses the eel's tile, not
   yours; encumbrance is irrelevant once the grab lands. Reworded.
3. **"Vomiting from other causes also cures illness"** — only
   SICK_VOMITABLE (food poisoning). Pestilence's SICK_NONVOMITABLE
   cannot be vomited away. Split into separate paragraphs.
4. **Prayer as a slime cure** — would work outside Gehennom, but
   green slime is Gehennom-only and prayer fails there. Caveat added.

### Added
- 9-turn slime timer (eat.c:854, uhitm.c:3199, polyself.c:456).
- Food poisoning timer range 10-19 turns (eat.c:1909).
- Pestilence-specific paragraph (Con-based timer, non-vomitable).
- Amulet of unchanging blocks sliming entirely.
- Cancellation negates the slime touch attack.
- Cure-sickness spell cures sliming.

### Related — Puddings and oozes section update
- Added a paragraph in the bestiary "Puddings and oozes" intro
  explaining green slime is a Gehennom-only exception (no split,
  leaves glob not corpse, 9-turn touch transformation, defense
  list incl. amulet of unchanging, why prayer is unreliable here).


---

## 2026-05-18 — Chapter audit #94: Sokoban Level 2, Version B

Source: `spoilers/companion.md` line 5870.
All 22 numbered solution steps verified by mental simulation. 0 corrections.

### Verified
- 16-boulder layout (A-P), 12-hole grid, rolling-boulder trap, upstair,
  door, walls all internally consistent.
- Each push verifies: player has a reachable approach square, boulder
  destination is clear, no collisions.
- Both intermediate diagrams (after step 9, after step 16) match
  simulated boulder positions.
- Final "remaining: A, D, G, H" list correct.
- Funnel finish-shorthand ("like M", "like N", etc.) internally
  consistent.

### Close calls (not changed)
- Step 21 ("Push G right 1. Push D up 1.") repositions two boulders
  that won't be finished — gratuitous but harmless. Spoiler still works.
- Diagram is a stylized 26-col render vs the 22-col raw soko2-2.lua;
  topologically equivalent.

---

## 2026-05-18 — Chapter audit #95: Dart

Source: `spoilers/companion.md` line 7088. Stats clean. Added missing
Notes (Poisonable; Tourist starts with a stack at +2, per is_poisonable
+ u_init.c:151).

---

## 2026-05-18 — Chapter audit #96: Boomerang

Source: `spoilers/companion.md` line 7109. Stats clean. 1 correction.

### Verified
- 1d9/1d9, wt 5, cost 20, wood, hitbon 0 (objects.h:166).

### Corrected
1. **"Returns when thrown. Always."** — false. Per zap.c:boomhit
   (4148-4233): flies a 10-step curved path, stops on
   monster/wall/door/sink, only catches on return if you pass a DEX
   check (auto-fail if Fumbling — failed catch hits you for damage).
   Enchanted boomerangs multi-hit (spe+1 hits per throw). Useless
   underwater. Reworded.

---

## 2026-05-18 — Chapter audit #97: Angelic beings `A`

Source: `spoilers/companion.md` line 7744. 5 rows verified clean vs
monsters.h:1206-1265. 1 correction.

### Verified
- All stats, colors, attack dice (incl. Archon gaze-blind, ki-rin
  butt + spell, couatl wrap).
- "All except Aleax fly" (M1_FLY pattern).
- "All except couatl see invisible" (M1_SEE_INVIS pattern).
- "Follow stairs" (M2_STALK on all).
- Archon regenerates (M1_REGEN).

### Corrected
1. **couatl "poisonous-corpse"** — wrong. All S_ANGEL entries have
   G_NOCORPSE; couatl leaves no corpse at all. Replaced with "no
   corpse." MR_POISON still matters for damage interactions.


## 2026-05-18 — Chapter audit #98: Giant humanoids `H`

Source: `spoilers/companion.md` line 8228. All 11 rows' stats match
`monsters.h:1714-1793`. 2 corrections.

### Verified
- Lvl/Spd/AC/MR%/Color for giant, stone, hill, fire, frost, ettin,
  storm, titan, minotaur, Cyclops, Lord Surtur.
- M2_ROCKTHROW on all giants + Cyclops + Surtur ("throws boulders"
  notes correct).
- Titan M1_FLY + M2_MAGIC + AT_MAGC AD_SPEL.
- Element resistances: fire/frost/storm carry MR_FIRE/MR_COLD/MR_ELEC
  innately; Surtur MR_FIRE|MR_STONE; Cyclops MR_STONE.
- Surtur and Cyclops are quest nemeses (Valkyrie, Caveman); both
  G_UNIQ, both M3_WAITFORU + M2_STALK.

### Corrected
1. **"Eating a giant's corpse raises Strength"** — overbroad. Gated
   on `is_giant(ptr)` (M2_GIANT) at `eat.c:1345`. Ettin (no M2_GIANT)
   and minotaur (no M2_GIANT) corpses do NOT confer Strength. The C
   source explicitly notes at `eat.c:1758`: "ettin is a two-headed
   giant but its corpse doesn't confer strength." Reworded the
   section intro to call out the exception.
2. **Minotaur "usually guards a vault"** — wrong. Minotaurs are
   placed in random Gehennom mazes by `mkmaze.c:1102-1113`
   populate_maze() (rn2(3) per maze level). Vaults are guarded by
   PM_GUARD. Fixed to "roams the Gehennom mazes."

### Notes
- "Has cold attacks" / "Carries shock attacks" on frost/storm giants
  is loose — innate attack block is AT_WEAP AD_PHYS only; elemental
  flavor comes from carried weapons. Kept the prose because reader
  intent is "they often *appear* with element-flavored weapons."
- Plain giant (red) has G_NOGEN; only generated by special
  monstergen, never random spawn. Not flagged in the table.

---

## 2026-05-18 — Chapter audit #99: Wishes and Wishing

Source: `spoilers/companion.md` line 4812. 3 substantive corrections
in the wish-syntax bullets plus one trim to the wish-list above.

### Verified
- Vlad's throne 4/13 wish chance (`sit.c:241` cases 1-4 of 13).
- Magic lamp rubbing math: ~27% wish per rub (uwep spe>0 + !rn2(3),
  then 80% wish from blessed djinni at potion.c:2833-2845).
- Smoky potion 1/13 base + 20%/80% blessed wish (potion.c:2833-2837,
  hack.h:1409 POTION_OCCUPANT_CHANCE).
- Fountain demon 1/30 (fountain.c:247 case 23) + ~1/5 shallow-Dlvl
  wish chance (fountain.c:78).
- Castle wand of wishing in locked chest inside one of four towers
  (castle.lua:18, 144-147).
- Orcus Town 50/50 magic lamp vs marker (orcus.lua:107-111).
- Gauntlets of power = STR 25 (attrib.c:1214-1215).

### Corrected
1. **"Just gray dragon scale mail gives you an uncursed +0 version"**
   — wrong on both counts. `objnam.c:5094-5096`: a missing `spesgn`
   retains the random mksobj spe (not forced 0). `objnam.c:5258-5268`:
   without an explicit BUC adjective the conditional chain is
   skipped — `mksobj` calls `blessorcurse(otmp, 10)` which leaves
   ~10% blessed, ~10% cursed, ~80% uncursed. A bare wish can roll
   cursed.
2. **"You cannot wish for artifacts that are already generated"** —
   wrong. `objnam.c:5374` makes the denial probabilistic
   (`oartifact && rn2(nartifact_exist())>1`), scaled by the *total*
   number of existing artifacts in the world (including bones
   files), not specifically the wished-for one. `u.uconduct.wisharti`
   ticks at `objnam.c:5364` whether the artifact materializes or
   not. Only quest artifacts (any role's) are absolutely blocked.
3. **"You cannot wish for the Amulet of Yendor (nice try)"** —
   misleading. `objnam.c:5003-5006` silently substitutes a
   `FAKE_AMULET_OF_YENDOR`. Same trapdoor exists for Bell of Opening
   (→ plain bell), Book of the Dead (→ blank paper), Candelabrum (→
   tallow/wax candle), and — particularly relevant in this chapter
   — magic lamp (→ oil lamp). Reworded the bullet to enumerate all
   five fake-substitution targets.

### Trims
- Dropped "+AC" from the gauntlets-of-power line; all gloves give
  +1 AC, and the gauntlets' real value is STR 25, not the trivial
  AC bonus.

### Notes
- Amulet-of-Yendor pickup wish actually triggers at the *top of the
  next moveloop iteration*, not on pickup itself (allmain.c:446-451).
  And "you can decline" only by typing literal `nothing`; pressing
  Escape loops back (zap.c:6346-6352). Not flagged in the spoiler
  because the simplification is accurate for player behavior.

---

## 2026-05-18 — Chapter audit #100: Sokoban Level 3, Version A

Source: `spoilers/companion.md` line 5830. Map and solution are
internally consistent and faithful to `dat/soko2-1.lua`. No
corrections.

### Verified
- Spoiler "Level 3, Version A" ↔ `soko2-1.lua` (spoiler numbers
  Sokoban levels from the entry, lua names from the prize end:
  spoiler Level N ↔ lua soko(5−N)).
- Map layout — walls, doors, stairs, pits, traps — matches after
  converting lua 0-indexed coords to spoiler 1-indexed (+1 col,
  +1 row). Up-stair, locked door, rolling-boulder trap, hole row,
  down-stair / player start all line up.
- All 13 lettered boulders A–M map to the 13 `des.object("boulder",...)`
  entries in `soko2-1.lua`.
- Solution steps 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 all
  internally consistent: push destinations are floor, player
  approach squares are reachable.
- No diagonal-squeeze violations or pull operations.

### Close calls (no correction)
- Step 3 ("Finish L, J, A, and B") collapses four boulder
  evacuations into one line; order matters (J blocks L's passage,
  B blocks A's western approach). A literal reader could deadlock.
- Step 12's right-then-left detour is forced by the inner wall at
  spoiler col 10 rows 4-5 (lua col 9, rows 3-4), which prevents
  circling east of D directly. The maneuver is necessary but
  unexplained in the spoiler text.

---

## 2026-05-18 — Chapter audit #101: Broadsword

Source: `spoilers/companion.md` line 7027. 1 correction.

### Verified
- broadsword/elven broadsword/runesword damage (1d4+1d4 / 1d6+1
  variants), weights, costs, materials match objects.h:262-289.
- All three share P_BROAD_SWORD skill class.

### Corrected
1. **Stormbringer attribution placed on broadsword row** — wrong.
   `artilist.h:93` shows Stormbringer's base item is `RUNESWORD`,
   not BROAD_SWORD. They share the broadsword skill class and have
   identical dice, which is what makes the slip easy. Moved the
   attribution to the runesword row and added the drain-life
   detail and the peaceful-attack quirk.

---

## 2026-05-18 — Chapter audit #102: Wands and Staves

Source: `spoilers/companion.md` line 3437. ~180 lines. 5 corrections.

### Verified
- Wand prices in the table all match `objects.h:1449-1499`.
- Max charges: NODIR=15, non-NODIR=8 (`mkobj.c:1123-1124`).
- Wishing starts with exactly 1 charge (`mkobj.c:1116-1117`).
- Wresting: 1/121 chance (`hack.h:1411` WAND_WREST_CHANCE=121).
- Recharge explosion formula `n^3 / 343` (`read.c:761-762`).
- Wand of wishing **guaranteed** explodes on second recharge.
- Cursed wand may explode when engraved (`engrave.c:794`,
  ~1% per use).
- Make invisible duration 31-45 turns (`zap.c:2836`, `rn1(15,31)`).
- Elemental side effects: fire burns floor scrolls
  (`zap.c:burn_floor_objects`), cold freezes water
  (`zap.c:5288`), lightning blinds (`zap.c:4355`).
- Cancellation does NOT affect booze/fruit juice/oil.

### Corrected
1. **Wand of stasis was missing entirely** from the Wand Table and
   the systematic-testing protocol. Added to the table at $150
   NODIR 15-charges (`objects.h:1460`). Added a Key Wands callout
   for what it actually does: freezes every monster on the level
   for 10–30 turns (`zap.c:2559-2568`, `rn1(21, 10)`).
2. **"Nothing" was classified as NODIR in the testing prose** but
   IMMEDIATE in the table — the table was right (`objects.h:1462`).
   Removed "nothing" from the NODIR list in Step 1.
3. **"Wand of undead turning raises it as a zombie"** — wrong.
   `zap.c` WAN_UNDEAD_TURNING calls `unturn_dead()` which iterates
   the target's inventory (or the floor if zapped at a corpse) and
   revives each corpse to its **original species**, not as a
   zombie. Reworded.
4. **"If the engraving disappears entirely, it's teleportation or
   polymorph"** — wrong on both halves. Per `engrave.c:618-672`:
   cancellation, make invisible, and teleportation all produce
   "engraving vanishes" (`de->dengr = TRUE` or `de->teleengr`);
   teleportation specifically moves the engraving elsewhere on
   the level (`teleengr` at `engrave.c:680`); polymorph rewrites
   the engraving to a different random message (`engrave.c:618-633`).
   The old dichotomy was muddled. Reworded the BEAM bullet to
   describe each behavior accurately.
5. **Silent-IMMEDIATE engrave group unmentioned.** Five BEAM wands
   produce no engrave message at all: nothing, undead-turning,
   opening, locking, probing (`engrave.c:635-640`). Plus stasis
   (NODIR) is also silent. Added explicit callouts in both bullets
   so a silent engrave-test result narrows to one of six.

### Notes
- The "beam" label for IMMEDIATE wands is a non-standard
  simplification (they target the first monster hit, not all
  squares in a line). Tolerable. Kept as-is.
- Wand of magic missile only fires 2 bolts vs 6 for fire/cold/
  lightning at the same charge (`zap.c:3465`), making it
  noticeably weaker than other elemental rays. Spoiler doesn't
  mention this; could add later.
- Cancellation cancels worn armor on monsters and removes magical
  resistances — the actual mechanism behind "loses most of its
  special attacks." Spoiler is vague but not wrong.

---

## 2026-05-18 — Chapter audit #103: Trappers and lurkers `t`

Source: `spoilers/companion.md` line 7446. No corrections.

### Verified
- lurker above: Lvl 10, Spd 3, AC 3, MR 0, gray, M1_FLY, M1_HIDE,
  M2_STALK — all match `monsters.h:981-989`.
- trapper: Lvl 12, Spd 3, AC 3, MR 0, green, M1_HIDE, M2_STALK,
  no M1_FLY — all match `monsters.h:990-998`.
- Engulf attacks (engulf 1d6 wrap + 2d6 phys for lurker; engulf
  1d8 wrap + 2d8 phys for trapper) match `monsters.h:983, 992`.
- "Hide" and "follow you up and down stairs" claims match M1_HIDE
  + M2_STALK flags and `mondata.c:1224`.

### Notes
- Both monsters' AD_WRAP can suffocate non-breathless characters,
  which is the real danger beyond the listed dice. Not flagged in
  spoiler; potential future addition.
- 5.0 explicitly changed t-class away from AD_DGST (digestion) to
  AD_WRAP (`monsters.h:974-979` comment). The spoiler's loose
  "swallow attack" phrasing is colloquially accurate.

---

## 2026-05-18 — Chapter audit #104: The Elemental Planes

Source: `spoilers/companion.md` line 5683. 4 corrections.

### Verified
- Earth: buried random portal, no stairs, mostly diggable rock,
  noteleport/hardfloor/shortsighted flags
  (`dat/earth.lua:13-53`).
- Air: void with no walls/floor, mazelevel noteleport hardfloor
  shortsighted stormy, hostile air elementals
  (`dat/air.lua:7-9, 51-61`).
- Air elementals cannot be genocided (G_NOCORPSE | 1, no G_GENO).
- Fire: fire traps, fire elementals, lava terrain
  (`dat/fire.lua:9, 42-81`).
- Water: drowning is the killer; sea monsters in `;` class are
  G_GENO so scroll of genocide on `;` works
  (`monsters.h:3205-3256`).
- Astral: three altars (one per alignment), shuffled per game,
  with Riders + Angels + clerics (`dat/astral.lua:83-91`).
- Riders are M2_NOPOLY | G_UNIQ | G_NOGEN, cannot be genocided;
  revive from corpses (`monsters.h:3144-3173`, `mon.c:1558-1679`).
- Offering real Amulet on a matching sanctum altar ascends
  (`pray.c:1868-1880, 1573-1587`).

### Corrected
1. **"Choose wrong and the Amulet is lost: you'll need to fight
   to retrieve it"** — wrong. `pray.c:1562-1572` ends the game
   immediately on wrong-altar offering with `done(ESCAPED)`; the
   opposing god gains dominion over your god. The Amulet is
   consumed at `pray.c:1537-1540` *before* the alignment branch.
   No retrieval — it's a loss state.
2. **"Drowning is instant death, no saving throw"** — wrong.
   Drowning calls `done(DROWNING)` (`trap.c:5171-5193`), which
   honors amulet of life saving. Breathless intrinsic (magical
   breathing amulet, Amphibious polyform) prevents drowning
   entirely (`trap.c:5106-5126`).
3. **"Farlook (`;`) shows alignment"** on Astral — only when you
   are **adjacent** to the altar. From across the room, farlook
   returns "an aligned high altar" with no alignment word
   (`pager.c:744-754`). You have to walk up to each.
4. **"If a vortex engulfs you, it carries you randomly around the
   level"** — conflates two unrelated systems. Vortex AT_ENGL
   attacks just damage you; they don't move bubbles or transport
   the hero. The level's **cloud bubbles** drift each turn
   (`mkmaze.c:1648-1685, 1951-1965`); standing in a drifting
   bubble shifts you with it, and may eventually carry you onto
   the portal square. Reworded.

### Notes
- Every plane has `noteleport`, so wand-of-teleport on **self**
  silently fails. Still works for clearing crowds via monster
  teleport. Added to spoiler.
- Astral is `non_diggable | non_passwall` (`dat/astral.lua:103-104`)
  — phase-door / dig escapes don't work.
- Earth monsters include more than earth elementals: pit fiends,
  barbed devils, rock trolls, stone giants, stone golems, pit
  vipers, minotaurs, scorpion, rock piercer, umber hulk, dust
  vortex. Spoiler over-narrows the threat; could expand later.
- Fire roster includes red dragon, balrog, fire giants,
  salamanders, pit fiends, hell hounds.

---

## 2026-05-18 — Chapter audit #105: Sokoban Level 4, Version A

Source: `spoilers/companion.md` line 5927. No corrections.

### Verified
- Map matches `dat/soko1-1.lua:8-27` (Version A = soko1-1.lua per
  prize odds 75% BoH at soko1-1.lua:103-105 matching header text
  "usually bag of holding, 25% amulet of reflection").
- Stair down, locked door (24,14), three closed doors at
  (18,12)(18,14)(18,16), rolling-boulder trap at (9,2), hole row
  cols 8-24 in row 2 — all match lua.
- All 18 boulders A-R match `des.object("boulder",...)` entries
  at `soko1-1.lua:40-60`.
- Push destinations and player approach squares for all 19 steps
  land on floor in the lua; no diagonal squeezes; no pulls.
- "Three boulders (F, G, H) remain" — verified by counting.
- Prize candidate squares (17,12)/(17,14)/(17,16) match `place:set`
  at `soko1-1.lua:30-32`.

### Notes
- Engraving "Elbereth" and a cursed scroll of scare monster on the
  prize square (`soko1-1.lua:110-111`) — not mentioned by spoiler,
  no claims made about them.

---

## 2026-05-18 — Followup #106: Displacer beast lure-to-hazard tactic

Source: `spoilers/companion.md` line 2267 (Displacer Beast section).
1 correction.

### Corrected
- **"A neat trick: lure it adjacent to a moat or lava and let it
  swap itself in"** — wrong. The M3_DISPLACES swap at
  `hack.c:1972` ends with `goodpos(u.ux0, u.uy0, mtmp, GP_ALLOW_U)`,
  meaning the swap only fires if the hero's previous square is a
  valid placement for the displacer beast. `teleport.c:134-162`
  refuses water for a non-swimmer/non-flier and lava for a
  non-fire-resistant non-flier. Displacer beast has neither, so
  the swap is rejected and the beast just attacks normally. Even
  if the hero were standing IN the hazard via water-walking or
  levitation, the swap still wouldn't fire because the beast
  itself can't survive there. Replaced the tactic with a brief
  caveat that explicitly says it doesn't work.

### Notes
- Caught by reader after the #42 rewrite landed; the false tactic
  was held over from the pre-#42 version.

---

## 2026-05-18 — Followup #107: Displacer beast as a great pet

Source: `spoilers/companion.md` line 2267-2291. Added content.

### Added
- **MR-0-at-level-12 framing**: 86% of monsters at lvl 10+ carry
  some MR; displacer beast is in the 14% with MR=0. That makes
  charm monster, sleep, paralysis, and scroll of taming
  completely unresistable. Bumped the existing "no MR" line to
  flag this as unusual.
- **"Great pet" paragraph**: tame displacer beast has AC −10,
  three attacks (4d4/4d4 claw + 2d10 bite), and M3_DISPLACES
  flips in your favor — hostile melee against the pet has a 50%
  chance to swap them next to you instead of biting the pet.
  Charm monster works on the first cast. Among the most powerful
  tame-able monsters in the game.
- Index of Useful Knowledge entry retitled
  "Displacer beast, aiming next to the" → "Displacer beast,
  taming" to reflect the section's actual best-use angle.

### Notes
- Cohort of strong MR-0 monsters at lvl ≥ 10: kraken, mastodon,
  Cyclops, Goblin King, Scorpius, minotaur, baluchitherium,
  Olog-hai, disenchanter, displacer beast, prisoner, shade,
  skeleton, titanothere, trapper, nurse, black pudding, ettin,
  lurker above. Pattern: organic mundane creatures lack MR;
  magical/demonic/dragon-class carry it.

---

## 2026-05-18 — Chapter audit #106: Medusa's Island

Source: `spoilers/companion.md` line 1023. 2 corrections + identification-flowchart label fix.

### Verified
- PM_MEDUSA flags G_NOGEN | G_UNIQ, AT_GAZE/AD_STON gaze mechanic
  (`monsters.h:2836-2846`).
- Reflection bounces the gaze back and stones her
  (`mhitu.c:1721-1745`).
- Blindness defeats the gaze (`mcanseeu` gating at
  `mhitu.c:1681-1682, 1747-1748`).
- Applied mirror stones Medusa at melee range
  (`apply.c:1132-1138`).
- Perseus statue contents probabilities (75% cursed shield of
  reflection, 25% levitation boots, 50% blessed +2 scimitar, 50%
  sack) match `medusa-1.lua:60-76`.
- Four layout variants exist (`dat/medusa-{1..4}.lua`).
- Cold-wand freezing the moat is a real crossing tactic
  (`zap.c:5238-5264`).
- Levitation/Flying/Wwalking all permit pool crossing
  (`hack.c:1196-1197`).

### Corrected
1. **"Giant eels can grab and drown you if you're burdened"** —
   wrong precondition. Eel grab is a standard hit roll with no
   Burdened term (`mhitu.c:847-848`). Burden affects monster
   hit-rate generally but is not what enables the grab. Reworded
   to "on a successful hit."
2. **"water contains giant eels (and sometimes a kraken)"** —
   only `medusa-4.lua:122` places a kraken; medusa-1/2/3 have
   none. Reworded to "(and on one of the four layout variants,
   a kraken)."
3. **Identification-flowchart decision cell** "Ring or potion
   willing to lose in a sink?" was rendered at 16px while every
   other decision cell is 18px. Reworded to "Spare ring or
   potion with a sink?" (33 chars, fits at 18px). This is in
   the SVG inside companion.md line 2479.

### Notes
- Medusa has M3_WAITFORU — she starts asleep, so you choose the
  moment of engagement. Worth a brief mention.
- Level has noteleport (`medusa-1.lua:12`); you can't wand-teleport
  across the water.
- medusa-3 has a fountain (`medusa-3.lua:47`) — minor flavor.

---

## 2026-05-18 — Chapter audit #107: Armor Tables

Source: `spoilers/companion.md` line 7378. 7 corrections.

### Verified
- Body-armor stats for all 15 suits match `objects.h:556-600`.
- All dragon scale mail / scales AC, weights, costs, materials, and
  secondary intrinsics (drain res, FAST, sick res, infravision,
  free action, stone res, slow digestion, hallucination res)
  match `do_wear.c:806-883`.
- Gold DSM is a light source (`light.c:907, 920`).
- Cloak AC/weight/cost/MC/materials match `objects.h:611-650`;
  cloak of protection is the unique MC=3 piece (`objects.h:640`).
- Oilskin cloak grab/wrap resistance (`mhitu.c:1065`).
- Cornuthaum confers CLAIRVOYANT and blocks it for non-Wizards
  (`worn.c:40-44`).
- Helm of brilliance is GLASS in 3.7 to avoid metallic casting
  penalty (`objects.h:472`).
- Gauntlets of power set Str to STR19(25)=125
  (`attrib.c:1214, 1278`).
- Mummy wrapping blocks Invisibility while worn (`worn.c:39`).
- Shield of reflection is silver (`objects.h:678`).

### Corrected
1. **Helm of brilliance "+d4 Int/Wis when blessed and enchanted"**
   — wrong. `do_wear.c:3328-3334` adj_abon adds the literal
   enchantment (`uarmh->spe`) to both Int and Wis. No dice. A +3
   helm gives +3 Int and +3 Wis. Reworded.
2. **Gauntlets of dexterity "+d3 Dex per enchantment"** — same
   shape. `do_wear.c:3321-3326`: adds `uarmg->spe` to Dex. No
   dice. Reworded.
3. **Dunce cap "Always cursed on generation"** — wrong. Dunce cap
   follows the standard `mkobj.c:1085-1092` distribution
   (~1/11 cursed). The auto-curse happens when WORN
   (`do_wear.c:475-491`). Reworded to call out the auto-curse-
   on-wear mechanism.
4. **Mithril coats "no casting penalty"** — wrong. MITHRIL is in
   the is_metallic range (`objclass.h:194-196`, IRON..MITHRIL),
   so `spell.c:2191-2193` spelarmr penalty applies. Mithril coats
   are lighter than plate, not penalty-free. Both elven and
   dwarvish rows fixed.
5. **Jumping boots "`#apply` to leap. `#apply` to leap."** —
   duplicated clause typo. Trimmed.
6. **Levitation boots "(cannot be removed while in the air).
   Can't remove while levitating."** — duplicated clause typo.
   Rewrote into a single coherent sentence.
7. **Helm of telepathy "Telepathy. Telepathy while blind."** —
   duplicated phrase. Trimmed (telepathy is only useful while
   blind, so the second clause is the real description).

### Added
- The four items that ARE 9/10-cursed-on-generation per
  `mkobj.c:1086-1090` — fumble boots, levitation boots, helm of
  opposite alignment, gauntlets of fumbling — now have explicit
  "Generated cursed 9 times in 10" callouts in their Notes
  columns. The dunce-cap text had been wrongly carrying this
  flag.

### Notes
- Kicking boots note column is blank; they boost kick damage
  (`dokick.c:41, 1328`).
- Cornuthaum's CHA effect (−1 non-Wizard, +1 Wizard) not
  mentioned (`do_wear.c:458, 538`).
- Bronze plate mail is metallic (COPPER=13) so it also incurs
  the spelarmr penalty; spoiler doesn't flag this in its row.
- Robe's spell-cast bonus is conditional on metallic body armor;
  spoiler's "+1" is loose flavor.

---

## 2026-05-18 — Chapter audit #108: No Genocide

Source: `spoilers/companion.md` line 6627. 3 corrections.

### Verified
- Conduct is self-imposed: no `u_conduct` counter, tracked at
  end-of-game by counting `G_GENOD` species in `svm.mvitals[]`
  (`insight.c:2951-2966` num_genocides), reported as "You have
  never genocided any monsters" / "You genocided N type(s)…"
  (`insight.c:2158-2165`).
- Typing "none" at the prompt preserves the conduct
  (`read.c:2873-2880`, comment: "choosing 'none' preserves
  genocideless conduct").

### Corrected
1. **"Astral Plane's final wish" as a genocide source** —
   fabricated. There is no wish-grants-genocide path in 5.0;
   no SPE_GENOCIDE either. Genocide is offered only by scroll
   of genocide (`read.c:2240` do_genocide/do_class_genocide)
   and Vlad's throne (`sit.c:131` do_genocide(5)).
2. **"Answer 'none' or leave it blank"** — leave-it-blank is
   misleading for a cursed scroll: empty input re-prompts
   (`read.c:2865-2871`) and after 5 tries / on cursed scrolls
   the `rndmonst()` path (`read.c:2848-2849`) creates random
   monsters rather than letting you escape. Type "none"
   explicitly.
3. **Missing: throne path** at `sit.c:131` (sitting on Vlad's
   throne can prompt class genocide) and the blessed-scroll
   class-wipe distinction. Added both to the section text.

### Added
- Caveat about the Plane of Water: the standard genocide-class-`;`
  trick is off-limits under No Genocide, so the player has to
  cross with magical breathing and careful navigation.

---

## 2026-05-18 — Chapter audit #109: The Castle

Source: `spoilers/companion.md` line 5278. 3 corrections + 4 added
features that the spoiler had omitted.

### Verified
- Drawbridge mechanism, passtune for entry, levitation/Wwalking
  back-entry (`dat/castle.lua:8-12, 81`; `music.c:786-829`).
- Locked chest in one of four corner-tower alcoves contains the
  wand of wishing AND potion of gain level
  (`dat/castle.lua:142-149`).
- Throne, two barracks, soldiers + lieutenant in entry hall
  (`dat/castle.lua:170, 248-249`).
- Wand of wishing initial spe=1, one safe recharge, guaranteed
  explode on next recharge (`mkobj.c:1116-1117`,
  `read.c:738-740, 761-765, 781-787`).
- noteleport flag on the level (`dat/castle.lua:22`).

### Corrected
1. **"Maze section with a minotaur guarding it"** — fabricated.
   `dat/castle.lua` has no minotaur and no internal maze room.
   The `style="mazegrid"` is fill outside the fortress for entry
   corridors (`dat/castle.lua:223-224`), not a maze room.
   Minotaurs are placed in earth/fire/hellfill, not the Castle.
   Dropped the bullet.
2. **"Elbereth keeps shopkeeper-class wanderers from stealing"**
   — wrong target. The lua author's comment at
   `dat/castle.lua:150` says the Elbereth + cursed-scare-monster
   wards are there to "Prevent monsters from eating it.
   (@'s never eat objects)" — i.e., they repel **non-@**
   monsters that gnaw containers. Shopkeepers aren't repelled by
   Elbereth and aren't the threat. Reworded.
3. **"Intelligent monsters can unlock locked chests if they
   carry keys"** — wrong for chests. `muse.c:2273` mloot_container
   returns immediately if container->olocked. Monsters can
   unlock doors (`monmove.c:1554-1572`) but never chests. The
   Castle wand chest is created locked at `dat/castle.lua:144`,
   so it is safe from looting. Dropped the warning entirely;
   added an affirmative note that locked chests are
   monster-proof.

### Added (previously omitted Castle features)
- **Throne-room treasure chest** at (37,8) — separate from the
  wand chest, holds random loot (`dat/castle.lua:154`).
- **Four storerooms** along N/S walls, each guarded by a D-class
  dragon (`dat/castle.lua:82-141, 181-184`). Easy to confuse
  with the corner alcoves; players who search the wrong rooms
  will fight dragons for nothing.
- **Five trap doors** at evenly-spaced squares in the central
  hallway (`dat/castle.lua:156-160`) — drops you to a random
  Gehennom level.
- **Fountain** at (10,8) (`dat/castle.lua:60`).
- **Moat sea monsters** (giant eels, sharks) (`dat/castle.lua:186-193`).

### Notes
- Drawbridge responds to the passtune on any musical instrument
  (no specific "horn of warning"); also opens to wand of opening
  / spell of knock.
- The Castle's L-class court monsters include random lich species;
  the spoiler's "5.0 no longer pre-loads with arch-liches" claim
  is broadly consistent but not directly visible in castle.lua.

---

## 2026-05-18 — Chapter audit #110: Sokoban (branch overview)

Source: `spoilers/companion.md` line 894. 1 correction.

### Verified
- Entrance dlvl 6-10 (one above Oracle), `dungeon.lua:21-24, 60-66`.
- Branch goes up (`dungeon.lua:24`).
- Four puzzle levels, two variants each (`dungeon.lua:225-244`).
- noteleport on each level.
- Prize on top: 75/25 BoH/AoR per variant (`soko1-{1,2}.lua`).
- Cursed scroll of scare monster on the prize square.
- Cheating: squeeze → `change_luck(-1)` + sokocheat conduct
  (`hack.c:307`, `trap.c:7039-7054`).
- Fracture (wand of striking) → guilt (`zap.c:5555`).
- Polymorph boulders → guilt (`zap.c:1710`).
- Scrolls of earth → guilt (`read.c:1951`).
- Sokoban conduct reported only when branch entered
  (`insight.c:2215-2228`).
- Levitation/flying free of penalty (`hack.c:415-425`).
- Boulders can't be picked up in Sokoban (`pickup.c:1713-1717`).

### Corrected
1. **"break it ... by force-fighting it"** — wrong. Force-fighting
   a bare boulder is harmless (`hack.c:2287, 2318-2321`, message
   "you harmlessly attack the boulder"). The actual cheat path
   is digging with a wielded pick-axe or mattock
   (`hack.c:2269-2275` requires `dig_typ(uwep,...)`). Reworded to
   fracture-via-striking/earth-scroll/polymorph, plus a caveat
   that pick-axe digging is also a cheat but force-fighting is
   not.

### Notes
- "Can't dig through the floors" is true (`hardfloor` on
  soko4-1.lua) but walls CAN be dug (with sokoban_guilt).
- Diagonal-push prohibition (`hack.c:441-447`) goes through
  `cannot_push()` and the squeeze/guilt path.

---

## 2026-05-18 — Chapter audit #111: Artifacts

Source: `spoilers/companion.md` line 3899. ~271 lines. 4 substantive
corrections + 3 useful additions.

### Verified
- Alignment-blasting: 4d10/2d10 for intelligent, 4d4/2d4 for
  others; first touch + 1/4 chance on subsequent
  (`artifact.c:944-953`).
- All wishable artifact rows match `artilist.h:85-212` for alignment,
  base item, hit/extra-dmg bonuses, and special intrinsic types.
- Stormbringer is correctly on the runesword row (fixed in earlier
  audit #103).
- Excalibur fountain-dip odds 1-in-6 Knight / 1-in-30 other Lawful
  (`fountain.c:405`).
- Cleaver "spin" requires !u.twoweap (`uhitm.c:769-771`).
- Snickersnee polearm-on-foot + Shkinng! pline + free reach attack
  (`apply.c:3512-3518`, `wield.c:131`).
- All quest-artifact alignment/owner/form rows match
  `artilist.h:219-307`.
- Quest artifacts all have SPFX_INTEL.
- Wish-denial probabilistic formula (`objnam.c:5374`).
- Mitre fire-res via CARY(AD_FIRE), no SPFX_DRLI — spoiler
  correctly notes "does NOT grant drain resistance."

### Corrected
1. **Magicbane "curse protection while carried"** — wrong.
   `artilist.h:145-147` shows Magicbane has SPFX_RESTR|SPFX_ATTK|
   SPFX_DEFN, STUN(3,4), DFNS(AD_MAGM), NO_CARY. All four
   Magicbane code paths (`wield.c:1036`, `trap.c:2360`,
   `mplayer.c:273`, `sit.c:576`) require wielding. Fixed table
   row and prose to say "while wielded."
2. **Master Key non-rogue carrier**: spoiler said "non-cursed
   Key carried by a Rogue (or **non-blessed** Key carried by
   anyone else)" — opposite for non-rogues. `artifact.c:2778-2784`:
   Rogue needs !cursed, non-rogues need **blessed**. Reworded.
3. **Eyes of the Overworld "carried gives magic resistance"** —
   wrong. DFNS(AD_MAGM), NO_CARY (`artilist.h:262`); MR activates
   only when worn per `artifact.c:731` wp_mask gating. Fixed
   prose; fixed the Carry column of the quest-artifact table.
4. **Tsurugi "grants magic resistance"** — wrong. cspfx =
   SPFX_LUCK|SPFX_PROTECT only; no MR via spfx, defn, or cary
   (`artilist.h:285-289`). The quest-artifact table row was
   already correct (no MR); fixed only the prose.

### Added
- **Sceptre of Might** double-damage hits **chaotic, neutral, AND
  unaligned** monsters (SPFX_DALIGN at `artifact.c:1031-1034`
  triggers for any `sgn(maligntyp) != weap->alignment` or
  `maligntyp == A_NONE`); Sceptre is Lawful. Spoiler omitted
  neutrals. Also clarified "while held" → "while wielded" since
  DFNS is wielded-only.
- **Mjollnir return**: only Valkyries get the reliable 99%
  catch-back (per `artilist.h:97-108`). Other roles can throw it
  but won't reliably catch it.
- **Frost Brand / Fire Brand invokes**: snowstorm/firestorm
  area effects (`artilist.h:150, 154`). Spoiler's wishable table
  omits the invoke column; added a short prose note.
- **Stormbringer** has SPFX_INTEL — Lawful/Neutral wielders take
  4d10 cross-alignment damage instead of 4d4.

### Notes
- Sceptre prose "magic resistance while held" was tightened to
  "while wielded" (DFNS only fires when wielded).
- Snickersnee SPFX is just SPFX_RESTR; the polearm-on-foot
  behavior is implemented as special-cases in wield.c/apply.c,
  not via an SPFX bit.

---

## 2026-05-18 — Chapter audit #112: Sokoban Level 3, Version B

Source: `spoilers/companion.md` line 6267. 1 correction.

### Verified
- All 16 boulders A-P match `soko2-2.lua:33-48`.
- Stair down at lua (6,11) → spoiler (7,12).
- Doors at lua (19,9) and (19,11) → spoiler (20,10) and (20,12).
- Rolling-boulder trap at lua (7,11) → spoiler (8,12).
- 11 hole traps at lua (8-18, 11) → spoiler cols 9-19, row 12.
- All wall/floor characters match.
- All 15 solution steps verified: push destinations on lua floor,
  player approach squares reachable, no diagonal-squeeze
  violations.
- "Five boulders (A, B, D, E, J) remain" is correct.

### Corrected
1. **Upstair `<` position off by one row**. `soko2-2.lua:25`
   places `des.stair("up", 15, 6)` → spoiler (16,7). Both the
   initial and intermediate maps had it at (16,8). Moved up one
   row in both maps.

---

## 2026-05-18 — Chapter audit #113: Keystone Kops `K`

Source: `spoilers/companion.md` line 8376. No corrections.

### Verified
- Symbol K matches S_KOP (`monsters.h:1829-1860`).
- Lvl/Spd/AC/Attacks/Colors for all four Kops match
  `monsters.h:1830, 1838, 1846, 1854`.
- MR% values (10/10/20/20) correct.
- Shopkeeper-anger trigger (`shk.c:623, 680` via `call_kops()`;
  `makekops()` at `shk.c:5113`).
- Spoiler correctly does NOT attribute Kops to vault gold theft
  (that's PM_GUARD's job; vault.c has zero Kop references).
- All four are G_GENO (genocideable).
- G_NOGEN: Kops never random-generate, only via `makekops()`.

### Added
- **Respawn note**: dead Kops respawn per `mon.c:3147-3164`:
  `rnd(5)` gives a 1-in-5 chance to return near the up-stairs and
  a 2-in-5 chance to return at a random location; 2-in-5 stay
  dead. Killing them isn't a stable solution; getting away or
  genociding the class works.

### Notes
- MS_ARREST is the only Kop-specific behavior tag (governs speech
  "Keep your hands where I can see them!" rather than movement).
- No "pratfall" code in mon.c for S_KOP.

---

## 2026-05-18 — Chapter audit #114: Spear

Source: `spoilers/companion.md` line 7280. No corrections; useful
additions.

### Verified
- All six spear stats (damage, weight, cost, hit bonus, material)
  match `objects.h:174-191`.
- Trident is correctly in its own section (uses P_TRIDENT, separate
  skill class from P_SPEAR).

### Added
- **Valkyrie multishot bonus**: `dothrow.c:50-51 multishot_class_bonus`
  gives Valkyrie +1 multishot on any thrown P_SPEAR item (not just
  javelin; silver spear and regular spear too).
- **Valkyrie starts with a spear** (`u_init.c:160-161`) and reaches
  Expert in P_SPEAR (`u_init.c:537`).
- **Kebab bonus**: `weapon.c:71-73, 167-168` is_spear() gives +2
  to-hit vs the big monsters — xorns, dragons, jabberwocks, nagas,
  giants. Applies to all P_SPEAR items, not trident.

---

## 2026-05-18 — Chapter audit #115: Curses and How to Break Them

Source: `spoilers/companion.md` line 4719. 1 correction.

### Verified
- Bones items 80% cursed (`bones.c:290`).
- Born-cursed items: amulet of strangulation/change/restful sleep
  (`mkobj.c:1063-1065`); rings of teleportation/polymorph/aggravate/
  hunger (`mkobj.c:1143-1148`); fumble/levitation boots, gauntlets
  of fumbling, helm of opposite alignment (`mkobj.c:1086-1091`).
- Cursed weapon weld (`wield.c:67-69, 382, 472, 571, 703`).
- Cursed bag of holding doubles weight (`mkobj.c:1950-1953`).
- Altar BUC flash (`do.c:379-384`).
- Pet avoids cursed items (`dogmove.c:145-150, 535`).
- Scroll of identify reveals BUC (`read.c:2055-2092`).
- Uncursed remove-curse hits worn only; blessed hits whole pack
  (`read.c:1524, 1549`).
- Confused remove-curse can curse items (`read.c:1556-1557`).
- Holy water uncurses on dip (`potion.c:1514-1518`).
- Prayer uncurses worn items (`pray.c:253, 533, 597`).
- Monsters can curse inventory via rndcurse (`mcastu.c:831-833`,
  `sit.c:143`, `wizard.c:798`, `fountain.c:324`).

### Corrected
1. **"Temple priest. Will identify BUC status for a fee, convenient
   in Minetown"** — fabricated. `priest.c:629-718` shows temple
   donation grants temporary clairvoyance (HClairvoyant) and
   Protection (u.ublessed); nothing sets bknown on inventory. The
   "priest auto-bknown" code at `invent.c:2763, 3545` and
   `objnam.c:1964` refers to the PLAYER being a Priest class
   character (Priests see BUC for free), not to NPC temple priests.
   Common spoiler myth. Dropped the bullet; added a brief
   myth-bust caveat and a formal price-ID-via-shop angle.

### Notes
- "Monster touched your inventory" intro line is loose flavor; the
  actual mechanic is via rndcurse from spellcasters/thrones/
  fountains/Wizard. Acceptable simplification.

---

## 2026-05-18 — Chapter audit #116: Gray Stones

Source: `spoilers/companion.md` line 2853. 2 corrections.

### Verified
- Four gray stones (luckstone, loadstone, touchstone, flint) per
  `objects.h:1598-1605`.
- Weights (loadstone 500, others 10) and base costs (60/45/1/1).
- Loadstone auto-curses on pickup (`invent.c:1386-1387`); cursed
  loadstone can't be dropped (`do.c:685-698`,
  `pickup.c:2577-2580`).
- Mine's End guaranteed not-cursed luckstone in all three variants
  (`dat/minend-{1,2,3}.lua`).
- Luck cap +13 with carried luckstone (`include/you.h:465-467`).

### Corrected
1. **"Cursed loadstone magically returns to your inventory"** —
   wrong. The drop command is **refused outright** with "For some
   reason, you cannot drop the stone!" The loadstone never leaves
   inventory. Reworded.
2. **"Rubbing a valuable gem against it will produce a streak
   message identifying the gem. If nothing happens, it's not a
   touchstone"** — partially wrong on both halves. Per
   `apply.c:2742-2760, 2800-2808`: a touchstone only **identifies**
   a gem when it's **blessed**, OR when an Archeologist/Gnome is
   holding an uncursed one. For other roles with an unblessed
   touchstone, the streak appears but the gem isn't identified.
   Other gray stones also produce streak messages, so a streak
   alone doesn't prove touchstone — only an *identification*
   result does. Cursed touchstones can shatter gems. Reworded.

---

## 2026-05-18 — Chapter audit #117: The Touch of Death

Source: `spoilers/companion.md` line 1946. 1 substantive correction
+ damage-path clarification.

### Verified
- Death the Rider's AT_TUCH / AD_DETH attack (`uhitm.c:3837`
  mhitm_ad_deth; `mhitu.c:58`).
- 8d6+50 damage with permdrain = dmg/2 (`mcastu.c:326-327`).
- Roll 17-19 = high-damage path gated by Antimagic
  (`uhitm.c:3858-3882`).
- Rolls 5-16 = default permdrain unblocked by MR
  (`uhitm.c:3869-3872`).
- MR blocks demon/lich Finger of Death spell (`mcastu.c:402`,
  gated at `:394`).
- Amulet of life saving rescues from done(DIED)
  (`mcastu.c:340`, `zap.c:2901`).

### Corrected
1. **"The wand and Finger of Death spell, like the spell version,
   are blocked by MR"** — wrong for self-zap. `zap.c:2885-2902`
   self-zap path has NO Antimagic check. Only the ray-bolt path
   (`zap.c:4497-4502`) checks Antimagic. So MR protects you from
   incoming death rays, but if you misfire your own wand into
   yourself, the only escape is **nonliving** (polyform: vampire,
   lich, skeleton, etc.) or **is_demon**
   (`zap.c:2887`, `:4493`). Reworded the Defenses paragraph to
   distinguish ray-bolt (MR-blocked) from self-zap (nonliving/demon
   only) and to add the nonliving/demon protection as a useful
   tactical option.

### Notes
- Polymorphed into undead also takes only half damage from Rider
  Death's touch (`uhitm.c:3852-3857`, message "Was that the touch
  of death?"). Added to the spoiler.
- Low-HD caster gate (`mcastu.c:394` `rn2(mtmp->m_lev) > 12`)
  means most low-HD demons fizzle even without MR. Not folded in.

---

## 2026-05-18 — Chapter audit #118: Crossbow

Source: `spoilers/companion.md` line 7372. 2 corrections.

### Verified
- Crossbow: weight 50, cost 40, hit 0, wood (objects.h:405).
- Crossbow bolt: weight 1, cost 2, hit 0, iron, pierce
  (objects.h:155-157).

### Corrected
1. **Bolt damage "1d4+1 / 1d6+1"** — wrong. PROJECTILE macro
   sdam=4, ldam=6 → 1d4 / 1d6 (no +1 bonus). Same encoding as
   arrow.
2. **"Crossbows fire one shot per turn at most"** — wrong.
   dothrow.c:225-231 enables multishot at ACURRSTR >= 18 (>= 16
   for gnomes). PM_GNOME gets baseline +1 multishot bonus at
   dothrow.c:205-209.

### Added
- Role/race tactical context: Rogue + Ranger Expert
  (u_init.c:429, 455), Valkyrie Skilled (u_init.c:366). Gnomes
  start with crossbow + bolts (u_init.c:252-253).

---

## 2026-05-18 — Chapter audit #119: Dagger

Source: `spoilers/companion.md` line 7095. 3 corrections.

### Verified
- All five damage/weight/cost/hit/material values match
  objects.h:201-214.
- Artifact attributions: Sting → ELVEN_DAGGER, Magicbane →
  ATHAME (artilist.h:138, 145).

### Corrected
1. **"Rogues multishot up to three"** — wrong. Expert Rogue:
   1 base + 1 Expert + 1 Skilled-fallthrough + 1 Rogue class
   bonus = max 4, then rnd(4) yields 1–4 (dothrow.c:177-190,
   63-67).
2. **Athame "Elbereth on the floor lasts longer engraved with
   an athame"** — wrong mechanism. The athame's distinction is
   that it doesn't dull when engraving (engrave.c:1306-1307,
   comment at :1361), so you can write Elbereth without
   consuming enchantment. On-floor duration is unchanged.
3. **Silver dagger "Silver damage to demons"** — scope too narrow.
   Silver hurts anything where mon_hates_silver() returns true:
   demons, undead, lycanthropes, shades (uhitm.c:896, 1035, 1376).

### Notes
- Silver dagger (mg=1 at objects.h:210) and athame (mg=1 at
  objects.h:213) are stackable; Notes column was inconsistent.
  Added "Stackable" to both.

---

## 2026-05-18 — Chapter audit #120: Mace

Source: `spoilers/companion.md` line 7220. 1 correction.

### Verified
- mace: 1d6+1/1d6 wt 30 cost 5 iron P_MACE (objects.h:355-357,
  weapon.c:269-275 small-bonus).
- silver mace: 1d6+1/1d6 wt 36 cost 60 silver P_MACE
  (objects.h:359-361).
- Demonbane = silver mace (artilist.h:162-164).
- Priest starts with blessed +1 mace (u_init.c:115).

### Corrected
1. **Demonbane "+d4/+0"** — wrong. PHYS(5, 0) at artilist.h:163
   = +d5/+0.

---

## 2026-05-18 — Chapter audit #121: Divine Relations

Source: `spoilers/companion.md` line 4170. 3 corrections + missing
trouble entries added.

### Verified
**Prayer trouble enumeration:**
- HP fractions 1/5..1/9 by XL bands match critically_low_hp()
  (pray.c:114-156).
- Order Stoned > Slimed > Strangled > Lava > Sick > Starving >
  HP > Lycanthropy matches in_trouble() (pray.c:206-223).

**Sacrifice:**
- 50-turn freshness window (pray.c:1844).
- Value = mons[].difficulty + 1 (pray.c:1845).
- Same-race chaotic-altar demon summon (pray.c:1729-1762).
- Same-alignment unicorn insult (pray.c:1923-1930).
- Altar conversion roll rn2(8 + u.ulevel) > 5 (pray.c:1661).
- Angry-god altar drop converts hero (pray.c:1637-1647).

**Crowning:**
- Resistances: see invisible, fire, cold, shock, sleep, poison
  (pray.c:813-818).
- Class gifts: Wizard SPE_FINGER_OF_DEATH, Monk
  SPE_RESTORE_ABILITY (pray.c:824-832).
- "Hand of Elbereth" title for Lawful (pray.c:841).

**Donation:**
- Ask formula (ulevelpeak ?: 1) * rn1(101, 150 + cheapskate*40)
  (priest.c:637-638).
- Tier thresholds at clairvoyance and 2x-clairvoyance
  (priest.c:660, 671, 681).
- Protection cap at u.ublessed < 20 (priest.c:696).

### Corrected
1. **Crowning "locks your alignment (you can never change it)"**
   — wrong. gcrownu() (pray.c:805-996) sets no alignment lock.
   The one-way conversion gate is the u.ualignbase[A_CURRENT]
   == u.ualignbase[A_ORIGINAL] check at pray.c:1638 — independent
   of crowning. Dropped the claim entirely.
2. **"Raises the prayer timeout to at least 1000 turns"** —
   wrong. pray.c:1356-1361: u.ublesscnt = rnz(350); if crowned
   (uhand_of_elbereth) += kick * rnz(1000). Average post-crowning
   is much higher but rnz can yield less than 1000 in either
   term. Reworded to "adds a large random penalty (~1000 turns
   on average) on top of the ordinary post-prayer wait."
3. **Punishment listed as #10 major trouble** — wrong.
   TROUBLE_PUNISHED = -1 in pray.c:91, a MINOR trouble handled
   in the "additional blessings" tier. Demoted to that tier.
   Also added previously-missing major troubles: TROUBLE_REGION
   (stinking cloud), TROUBLE_COLLAPSING (encumbrance), TROUBLE_
   STUCK_IN_WALL, TROUBLE_CURSED_LEVITATION, TROUBLE_UNUSEABLE_
   HANDS, TROUBLE_CURSED_BLINDFOLD (pray.c:218-243).

### Notes
- Artifact gift gating: requires u.ulevel > 2 and u.uluck >= 0
  (pray.c:1784-1792); spoiler omits this prerequisite.
- After-gift cooldown rnz(300 + 50 * nartifacts) is distinct
  from ordinary post-prayer cooldown (pray.c:1819).
- Cross-aligned altar conversion of own alignment also
  change_luck(-3) and u.ublesscnt += 300 (pray.c:1646-1647) —
  spoiler doesn't note the luck cost.

---

## 2026-05-18 — Chapter audit #122: Elbereth

Source: `spoilers/companion.md` line 1447. 2 corrections.

### Verified
- Exact-word match (case-insensitive via strcmpi) at engrave.c:251-260.
- Ward applies only while hero is on the square (monmove.c:295-298).
- Ignored by S_HUMAN, uniques, Riders, Angels, Wizard of Yendor,
  lawful minions, minotaurs, shopkeepers, vault guards, peaceful,
  blind (monmove.c:251-302, mon.c:251-261).
- Doesn't work in Gehennom/Elemental Planes/Astral
  (`Inhell || In_endgame` at monmove.c:302).
- Cornered scared monster fights via panicattk (monmove.c:918-920).
- Defile rule deletes engraving in full and prints "engraving
  beneath you fades" (mon.c:4267-4284).
- Athame doesn't dull (engrave.c:1306-1307).
- Burn engraving erodes only on ice or with magical && !rn2(2)
  (engrave.c:278); dust/blood wipes every step.

### Corrected
1. **"Levitation trick" (engraving Elbereth in dust while
   floating)** — non-functional in 5.0. `engrave.c:198` requires
   can_reach_floor(), which Levitation makes false. Finger-engrave
   is refused outright (engrave.c:1003-1006); a wand only
   "gestures toward the floor below you" without writing
   (engrave.c:1008-1010). Replaced the trick with the 5.0 reality.
2. **"−5 alignment hit"** stated as flat. Actual: mon.c:4280
   `adjalign((u.ualign.record > 5) ? -5 : -rnd(5))` — flat -5 only
   with healthy alignment record (>5); otherwise random -1 to -5
   (avg -3). Reworded.

### Notes
- Lawful minions (`is_lminion`) are scare-immune too — relevant
  for Aligned Priest minions.
- The exclusion list is concrete monster types, not a generic
  "intelligence" check; dragons, liches, mind flayers all still
  fear Elbereth.

---

## 2026-05-18 — Chapter audit #123: Movement Traps

Source: `spoilers/companion.md` line 1174. 1 correction.

### Verified
- Pit/spiked pit immobilize via u.utrap (trap.c:1825-1892).
- Trapdoor/hole share same fall path (trap.c:519-520).
- Teleport trap → tele_trap → safe_teleds, Tcontrol respected
  at teleport.c:872.
- Magic portal → domagicportal at teleport.c:1444.
- Pit/trapdoor/hole skip on Levitation/Flying (trap.c:635, 1850).

### Corrected
1. **Trapdoor "Drops you to the next level down"** —
   understates the mechanic. hole_destination
   (trap.c:442-453) loops: while dst->dlevel < bottom, increment
   and break with rn2(4) — 25% chance per level to keep falling.
   So a trapdoor can drop multiple levels. Same applies to hole.
   Reworded. Also: spoiler attributed pit/hole immunity to
   "Levitation" only; Flying also skips them, except in Sokoban
   where the `!Sokoban` guard disables the skip entirely.

### Notes
- Magic portals lead to fixed destinations (Quest entry, Fort
  Ludios, Vlad's tower, endgame transitions) — not all branch
  entrances. Mines/Sokoban use stairs.

---

## 2026-05-18 — Chapter audit #124: The Gnomish Mines

Source: `spoilers/companion.md` line 842. No corrections; one
useful addition.

### Verified
- Mines branch DL 2-4 (dungeon.lua:14-19), mazelike + minefill.
- 7 Minetown variants (dungeon.lua:178-185), 1-in-7 Orcish Town
  (minetn-1.lua:9-10).
- Orcish Town has noaligned altar, dead shopkeepers/watchmen, no
  shops, 7 wax candles (minetn-1.lua:52, 79-88, 99).
- All three Mine's End layouts contain a not-cursed luckstone
  (minend-{1,2,3}.lua).
- Mines population (gnomes, dwarves, occasional dwarf lord)
  matches minefill.lua:36-44.
- Race-peaceful for gnomish PCs: lovemask = MH_DWARF | MH_GNOME
  (role.c:654), peace_minded() via race_peaceful() in
  makemon.c:2283.

### Added
- **Fake-luckstone mimic** in minend-1.lua:59 (`appear_as="obj:
  luckstone"`) sits near the real luckstone — players should
  BUC-test what they pick up.

---

## 2026-05-18 — Chapter audit #125: The Rogue Level

Source: `spoilers/companion.md` line 1014. No corrections.

### Verified
- Welcome line "You enter what seems to be an older, more
  primitive world." (do.c:1913).
- Uppercase-only monsters (makemon.c:1672, mon.c:4866, 4946).
- Symbol swaps for armor `]`, amulet `,`, food `:`, gold sharing
  gem symbol (drawing.c:73-79).
- No-close doors (mklev.c:647-648 forces D_NODOOR).
- No fountains/sinks/altars (mklev.c:988-989 skip_nonrogue).
- No shopkeepers / no shops (roguelike flag in dungeon.lua:54-58).
- No spellbooks/tools/amulets in natural item pool
  (mkobj.c:58-64 rogueprobs: WEAPON, ARMOR, FOOD, POTION, SCROLL,
  WAND, RING only).
- Plain ASCII via ROGUESET symset (do.c:1666-1667).
- Dungeon level range Dlvl 15-18 (dungeon.lua:54-58 base=15,
  range=4).

---

## 2026-05-18 — Chapter audit #126: Puddings and oozes `P`

Source: `spoilers/companion.md` line 7813. 2 corrections.

### Verified
- All four pudding stat lines match monsters.h:2081-2123.
- Splitting restricted to black/brown puddings via iron/metal melee
  weapon (uhitm.c:1609-1621 hmon_hitmon_splitmon).
- Black pudding passive (AD_CORR) corrodes wielded weapon
  (uhitm.c:5969-5978).
- Green slime Gehennom-only (G_HELL), poisonous corpse, passive
  AT_NONE/AD_SLIM.
- Amulet of unchanging blocks the slime transformation.

### Corrected
1. **Green slime "9-turn countdown"** — wrong. make_slimed(10L,...)
   sets 10 turns (uhitm.c:3199, 3570; polyself.c:456; eat.c:854).
   Only 5-turn case is engulf+digest (uhitm.c:5099).
2. **"Brown puddings corrode armor on touch"** — wrong mechanism.
   AD_DCAY is ROT (ERODE_ROT for wood/leather/cloth/bone) per
   uhitm.c:2389 mhitm_ad_dcay. CORRODE (metal) is the black pudding
   effect via AD_CORR at uhitm.c:2338-2356. Reworded to
   "rot/corrode/rust" per actual erosion class.

### Added
- Gray ooze rust mechanic (AD_RUST → ERODE_RUST) was unmentioned
  in the prose. Added.
- Clarified that the split trigger requires iron/metal melee
  weapons specifically.

---

## 2026-05-18 — Chapter audit #127: Two-handed sword

Source: `spoilers/companion.md` line 6715. Clean stats; one
important addition.

### Verified
- two-handed sword: 1d12/1d6+2d6 bonus, wt 150, cost 50, iron,
  bimanual (objects.h:273-276, weapon.c:259-261).
- tsurugi: 1d16/1d8+2d6 bonus, wt 60, cost 500, hit +2, metal,
  bimanual (objects.h:282-285).
- Bimanual blocks shield and two-weapon (wield.c:186, 724,
  786-787; uhitm.c:5497, 5510).
- Tsurugi is correctly The Tsurugi of Muramasa (artilist.h:285).
  No dedicated artifact for plain two-handed sword.

### Added
- **3/2 Strength damage bonus for bimanual weapons** (5.0 change)
  at uhitm.c:1467-1468, gated on bimanual(uwep) + HMON_MELEE.
  Section had omitted this — it's the headline 5.0 buff for
  two-handers and applies to battle-axe, dwarvish mattock,
  bardiche as well.

---

## 2026-05-18 — Chapter audit #128: Weaponless

Source: `spoilers/companion.md` line 6210. Clean conduct logic;
two omissions added.

### Verified
- Conduct breaks only via uhitm.c:616-617 weaphit++ — requires
  weapon non-NULL AND (WEAPON_CLASS || is_weptool).
- Thrown weapons / fired ammo / wands / spells / bare-hand /
  martial arts / cockatrice-corpse-wield do NOT break the conduct
  (zap.c has zero weaphit refs; dothrow.c thrown path doesn't
  increment).
- Miss / 0-damage exemption: uhitm.c:636-639 rolls back weaphit if
  mon->mhp == oldhp.

### Added
- **Weapon-tools also break conduct**: pick-axe, unicorn horn,
  aklys, iron chain, grappling hook etc. — anything is_weptool
  with non-P_NONE skill (obj.h:249-250). The "swing a sword, axe,
  mace" list was understated.
- **One ranged exception**: a wielded polearm used at range via
  `#apply` (HMON_APPLIED path at dothrow.c:2199-2203) DOES break
  the conduct.

---

## 2026-05-18 — Chapter audit #129: Trident

Source: `spoilers/companion.md` line 6847. 1 correction.

### Verified
- Damage S/L base 1d6/1d4 (objects.h:195 sdam=6, ldam=4).
- Bonus dice: +1 small, +2d4 large (weapon.c:251-255, 272-276).
- Weight 25, cost 5, hit 0, iron, one-handed (objects.h:195
  bi=0).
- Separate P_TRIDENT skill class.

### Corrected
1. **"+1 small, +2d4 large — the giant-killer"** — misleading.
   The +1/+2d4 bonus dice are the universal land-creature bonus
   shared by two-handed sword, battle-axe, bardiche, etc.
   (weapon.c:251-276). NOT trident-specific. The trident's
   actual signature bonus is missing: vs `is_swimmer(ptr)`
   monsters, +4 when target is in a pool, +2 when target is
   S_EEL or S_SNAKE (weapon.c:170-176). Reworded the Notes column.

---

## 2026-05-18 — Chapter audit #130: A Field Guide to Dungeon Fauna

Source: `spoilers/companion.md` line 1524. 2 corrections.

### Verified
- All class-symbol mappings (a, b, B, C, D, &, @, :, ;, ~, ], ', Q,
  etc.) match defsym.h:295-366.
- Individual monster facts spot-checked: soldier ant, bats, jackal,
  acid blob, floating eye, centaurs, displacer beast, rothe, mumak,
  jabberwock, cockatrice, grid bug, yellow/black light, purple worm,
  pudding split rules, rock mole, rust monster, disenchanter, mind
  flayer, genetic engineer, quantum mechanic, imp, wraith, vampire
  lord, yeti — all match individual monsters.h entries.

### Corrected
1. **Xan "leg-wound trapper"** — wrong. monsters.h:1157 shows
   AT_STNG AD_LEGS (sting that cripples legs), but "trapper"
   misleads — that's the S_TRAPPER (`t` class) engulfer, a
   completely different monster. Reworded to "whose sting cripples
   your legs."
2. **Leprechaun "A single bite"** — wrong. monsters.h:660 shows
   AT_CLAW AD_SGLD, not bite. Reworded to "A single claw."

### Notes
- Vampire bats drain Str (AD_DRST) on second bite; vampires proper
  drain levels (AD_DRLI). Spoiler called this distinction out
  correctly.

---

## 2026-05-18 — Chapter audit #131: Nymphs `n`

Source: `spoilers/companion.md` line 7342. No corrections.

### Verified
- All three nymph stats match monsters.h:702-723.
- AT_CLAW AD_SITM + AT_CLAW AD_SEDU attacks; both 0d0 dice
  (correctly omitted in spoiler).
- M1_TPORT on all three; water nymph has M1_SWIM (line 714).
- Corpse → intrinsic teleportitis 10% per should_givit
  (eat.c:936-975).
- AD_SEDU handled by doseduce() at mhitu.c:1984.

---

## 2026-05-18 — Chapter audit #132: Dangerous Traps

Source: `spoilers/companion.md` line 1193. 3 corrections.

### Verified
- Land mine, bear trap, sleeping gas, fire trap, magic trap
  damage/effects all match trap.c.
- Polymorph trap with PolyControl enters controllable_poly
  (polyself.c:481, 513).
- Anti-magic implosion damage formula breakdown matches
  trap.c:2353-2370.
- Iron shoes mitigations (bear trap, pit spikes, polymorph trap,
  anti-magic enchantment-drain) all verified.

### Corrected
1. **Anti-magic "halved to 1d4 if you can pass through walls"** —
   wrong. trap.c:2371-2372 dmgval2 = (dmgval2 + 3) / 4 is
   QUARTERED (rounded up), not halved. Max 4d4 = at most 4
   damage, not 1d4. Reworded.
2. **"Destroying it from range by zapping cancellation at it to
   defuse it without setting it off"** — wrong. Cancellation
   aimed at any magical trap (including ANTI_MAGIC per
   trap.h:118-122) triggers an explosion of 20 + d(3,6) damage
   at the trap's square per zap.c:3611-3621. Removes the trap
   but doesn't silent-defuse. Reworded the defense paragraph.
3. **Polymorph trap defenses incomplete** — spoiler implied only
   PolyControl helps; Antimagic and Unchanging both block the
   polymorph entirely (trap.c:2486-2489). Added.

### Notes
- Sleep gas full immunity from intrinsic Sleep_resistance not
  flagged.
- RUST_TRAP exists (trap.c:1072) and erodes armor; omitted from
  the dangerous-traps table (acceptable since it's minor).

---

## 2026-05-18 — Chapter audit #133: Leprechauns `l`

Source: `spoilers/companion.md` line 7314. No corrections.

### Verified
- Stats (Lvl 5, Spd 15, AC 8, MR 20, CLR_GREEN, claw 1d2 AD_SGLD)
  match monsters.h:660-666.
- M1_TPORT (self-teleports after steal).
- Steal mechanic: AD_SGLD → stealgold() → rloc() + monflee
  (uhitm.c:2821, steal.c:58-115).
- "Corpse drops the gold back": stolen gold added to mtmp->minvent
  via add_to_minv at steal.c:109.
- No gnaw-container behavior (M1_HUMANOID, no M3_METALLIVORE).
- LEPREHALL special room is C-generated by mkzoo (mklev.c:1355);
  no Lua file.

### Notes
- stealgold() also grabs floor gold on hero's square
  (steal.c:73-98) — "carry no gold" prevents inventory theft but
  not floor-pile theft. Minor incompleteness in the spoiler's
  "carry no gold" advice.

---

## 2026-05-18 — Chapter audit #134: The Ascension Run

Source: `spoilers/companion.md` line 5731. 3 corrections + the
missing Amulet-wish fact added.

### Verified
- Wizard of Yendor resurrects and summons nasties via resurrect()
  and nasty() at wizard.c:715-808.
- Amulet blocks level teleport (teleport.c:1185-1188).
- Amulet hampers self-teleport — 66% fail rate (teleport.c:865-871).
- Covetous monsters warp to player via mnexto/mnearto
  (wizard.c:236-326, 369-415).

### Corrected
1. **"Mysterious Force yanks you back to a random location on the
   level instead of going up"** — wrong. do.c:1541-1573 mostly
   sends you DOWN one to three levels via assign_rnd_level
   (diff = rn2(3 + ualign.type)); the same-level teleport is
   the fallback when assign_rnd_level returns a no-op. Distance
   is alignment-biased (Chaotic worst, Lawful softest).
2. **"Stops once you're above Gehennom, where the dungeon's grip
   weakens"** — misleading. It's a hard Inhell gate at do.c:1541,
   not a gradient. Also never fires on the bottom 4 levels
   (dunlev < dunlevs_in_dungeon - 3).
3. **"Use Elbereth when you need a turn to heal"** — wrong for
   almost the entire Ascension Run. teleport.c:68-70 onscary()
   returns FALSE for Inhell || In_endgame; Elbereth is dead in
   all of Gehennom and on all four Elemental Planes plus Astral.
   Reworded to flag this and direct the reader to corridors /
   teleport scrolls / conflict instead.

### Added
- **Amulet pickup grants a free wish** (allmain.c:446-451). Fires
  on the next moveloop iteration after pickup if
  !u.uevent.amulet_wish. The single most important tactical fact
  of the run; chapter omitted it. Added as a callout near the
  top.
- **Mysterious Force decay** (5.0 change). do.c:1536-1563
  svc.context.mysteryforce increases per trigger, !rn2(4 + mf)
  makes subsequent triggers rarer.

---

## 2026-05-18 — Chapter audit #135: Bonesless

Source: `spoilers/companion.md` line 6380. No corrections; one
useful clarification.

### Verified
- Achievement gated on !flags.bones (topten.c:605).
- The "never encountered any bones levels" enlightenment line is
  a separate Misc line, not the conduct (insight.c:434-441).
- OPTIONS=!bones is opt_out with set_in_config (optlist.h:213-215)
  — rcfile or CLI only.

### Added
- Clarified that !bones also stops the player's own death from
  generating bones for future players (bones.c:360
  can_make_bones), not just inheritance. Same flag gates both
  directions of the bones cycle.

---

## 2026-05-18 — Chapter audit #136: Axe

Source: `spoilers/companion.md` line 6726. 1 correction +
consistency improvements.

### Verified
- axe, battle-axe, dwarvish mattock damage/weight/cost/material
  match objects.h:236-241, 345-347.
- battle-axe and mattock are bimanual; pick-axe and axe are
  one-handed.
- Cleaver is the battle-axe artifact (artilist.h:114).

### Corrected
1. **Dwarvish mattock hit bonus** shown as `—` but objects.h:346
   has hitbon = -1. Updated.

### Added
- Battle-axe row now flags Cleaver as the artifact form (other
  weapon sections do this; battle-axe was omitted).
- Both bimanual axes now note the 5.0 3/2 Str damage bonus.

---

## 2026-05-18 — Chapter audit #137: Disintegration

Source: `spoilers/companion.md` line 2097. 1 correction +
mechanism clarifications.

### Verified
- AD_DISN attack on black dragon (monsters.h:1520).
- Reflection bounces the breath, redirecting it back at the
  dragon (zap.c:4966-4975 + zhitm bounce).
- Disintegration resistance gives full immunity (zap.c:4468-4471).
- Magic resistance does NOT block AD_DISN breath (zap.c:4464-4493
  has no Antimagic branch).

### Corrected
1. **"Touching a wide-angle disintegration beam also kills"** —
   fabricated. There's no such monster, sphere, or spell in 5.0.
   The beholder (the only other AD_DISN source) is #if 0-gated
   at monsters.h:367-377. AD_DISN comes from black dragon breath
   only. Dropped the claim.

### Added
- Worn-armor destruction priority: shield first (zap.c:4476-4479),
  then suit + cloak (zap.c:4480-4486); only if neither is worn
  does the hero actually die (with cloak/shirt destroyed in the
  process, zap.c:4487-4492). A shield of reflection that *fails*
  to reflect still eats one breath for you.
- Amulet of life saving does rescue (end.c:1081 DIED path); the
  breath code destroys cloak/shirt "in case of life-saving or
  bones."

---

## 2026-05-18 — Chapter audit #138: Fort Ludios

Source: `spoilers/companion.md` line 1004. 2 corrections + 5
additions.

### Verified
- Branch is "floating" — only inserted when a vault is generated
  at depth 11+ (mklev.c:2647-2651), 2/3 deferral per attempt.
- Magic-portal entry, placed inside a vault (mklev.c:1331).
- 17 soldiers + 1 lieutenant fixed (knox.lua:126-142).
- Croesus PM_CROESUS placed on throne, G_UNIQ + G_NOGEN.
- C/K-ration drops on soldiers (makemon.c:695-698).
- Treasury 15x4 = 60 tiles, 600-900 gold per tile ≈ 36k-54k
  (knox.lua:58, 68-70).
- Barracks fill drops chests 1-in-20 (mkroom.c:397-401).

### Corrected
1. **"Soldiers, lieutenants, captains"** — captains are NOT a
   fixed garrison, only a 1% rare from barracks zoo squadmon
   (mkroom.c:810-813). Dropped from the section text.
2. **"Croesus ... a unique human of legendary wealth"** —
   Croesus is the vault GUARDIAN (MS_GUARD, monsters.h:2863),
   not a merchant; the gold belongs to the vault, not him.
   Reworded.

### Added
- noteleport flag (knox.lua:9) — can't teleport in or out.
- Four dragons (knox.lua:144-148), four giant eels in the moat,
  stone giant (knox.lua:151-155).
- Corner-tower gem caches: diamond/emerald/ruby/amethyst x3
  each (knox.lua:156-167).
- Trap density on treasury tiles: 1/3 chance of spiked pit or
  land mine per tile (knox.lua:59-65).
- Military alarm quiets only when Croesus is dead
  (do.c:1894-1898).

---

## 2026-05-18 — Chapter audit #139: Rings and Amulets

Source: `spoilers/companion.md` line 3489. ~144 lines, no
substantive corrections.

### Verified
- All ring prices match objects.h:741-827.
- Auto-curse list (TELEPORTATION, POLYMORPH, AGGRAVATE_MONSTER,
  HUNGER) at 90% per mkobj.c:1143-1146 — spoiler's "90%" is
  exact.
- Aggravate-monster effective-depth doubling, capped at 50
  (dungeon.c:2080-2082).
- Free_action paralysis immunity (apply.c:1044, mcastu.c:506).
- Ring hunger cost: -1 nutrition on turns 4 and 12 per ring
  (eat.c:3237-3267).
- Amulet of guarding +2 AC and +2 MC (do_wear.c:2496-2497,
  mhitu.c:1121-1126); pairs with cloak of MR to MC 3.
- Restful sleep +1 HP regen while asleep (allmain.c:663-664).

### Close calls (not corrected inline; section is illustrative)
- Restful sleep is **always** cursed per mkobj.c:1065, not
  "usually."
- Blessed polymorph potion grants control only from base form
  (potion.c:1318-1329) and uses POLY_LOW_CTRL restricted form
  list.
- Protection from shape-changers covers chameleons, doppelgangers,
  sandestins, and genocidable shapechangers (makemon.c:1355-1358),
  not only werebeasts.

---

## 2026-05-18 — Chapter audit #140: Feelings and Sounds

Source: `spoilers/companion.md` line 1484. 5 corrections + 1
caveat added.

### Verified
- "Sad feeling" = pet died offscreen (mon.c:3100-3101).
- "Footsteps of a guard" = vault on level (sounds.c:269-270).
- "Strange wind" = Oracle (sounds.c:190).
- "Cursing shoplifters" = shop (sounds.c:321-325).
- "Bubbling water" / "water falling on coins" = fountain
  (sounds.c:214-218).
- "Bugle playing reveille" = soldier wake-up
  (muse.c:838-847).
- All corpse-feeling messages: poison/fire/cold/shock/sleep/
  disint res, telepathy, eye-of-newt mana (eat.c:1011-1075,
  1102-1122).
- "Like someone is helping you" = remove curse (read.c:1499-1500).
- "Feel feverish" = lycanthropy (uhitm.c:4282).
- "Slowing down" / "turning into slime" / "deathly sick" =
  stoning / slime / terminal illness (timeout.c:128-129,
  insight.c:1016, potion.c:154).

### Corrected
1. **"Counting gold coins" message** specifically means a vault
   with gold IN it; an empty vault gives "someone searching"
   instead (sounds.c:253-262). Split the row.
2. **"Wow! This makes you feel great!" = potion of restore
   ability** is incomplete. Per potion.c:658-661, the "great"
   phrasing is the **blessed** restore-ability variant with no
   remaining troubles, AND the same phrasing appears for a
   blessed magic fountain hit (fountain.c:257). Reworded.
3. **"Move very quietly" includes elven boots** — wrong.
   do_wear.c:123-129: boots produce "walk very quietly"
   instead. Fixed.
4. **Lycanthropy cure "dip in holy water"** — wrong action.
   potion.c:728-737: set_ulycn(NON_PM) fires when the blessed
   water is QUAFFED. Reworded to "quaff."
5. **"Seem faster" = quantum mechanic corpse** is incomplete.
   eat.c:1227-1235: only fires the speed branch if you don't
   already have intrinsic speed; otherwise you "seem slower."
   Added the toggle note.

### Added
- Global suppressor: Deaf/!flags.acoustics/u.uswallow/Underwater
  silences all dosounds() messages (sounds.c:208-209). Worth
  one line for Permadeaf players.

---

## 2026-05-18 — Chapter audit #141: Zombies `Z`

Source: `spoilers/companion.md` line 7968. No stat corrections;
intro reworded.

### Verified
- All 10 entries' stats match monsters.h:2421-2504.
- M1_POIS varies (kobold/gnome/orc/dwarf/ghoul have it;
  elf/human/ettin/giant zombies don't).
- Skeleton has MR_STONE and M2_WANDER (no follows-stairs).
- All zombies have M2_UNDEAD and M1_MINDLESS.

### Corrected
1. **"Corpses are usually unsafe to eat"** intro is misleading.
   All Z-class entries carry G_NOCORPSE — zombies NEVER leave
   corpses on death. M1_POIS still matters (for poison damage
   on were-strikes etc.) but is moot for eating. Reworded to
   "zombies never leave corpses on death" and added the
   tactical undead-turning hint.

### Added
- Skeleton has G_NOGEN — never randomly generated, only from
  skeleton trap or fixed placement (e.g., Vlad's Tower). Added
  to the intro.

---
