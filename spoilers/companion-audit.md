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

## 2026-05-18 — Chapter audit #142: The Food Conducts

Source: `spoilers/companion.md` line 6142. 5 corrections.

### Verified
- Vegan / vegetarian / foodless hierarchy.
- vegan(ptr) = S_BLOB|S_JELLY|S_FUNGUS|S_VORTEX|S_LIGHT|
  S_ELEMENTAL(except PM_STALKER)|S_GOLEM(except flesh/leather)|
  noncorporeal (mondata.h:232-241).
- Vegetarian = vegan OR S_PUDDING except black pudding.
- Royal jelly / pancakes / cream pies / candy bars break vegan
  only (eat.c:3016-3018).
- Wax/leather/bone/dragon-hide non-food objects break vegan when
  eaten (eat.c:2772-2786); wax also exempt from vegetarian.
- Meatballs (stone-to-flesh) break vegan + vegetarian.
- Lembas wafers VEGGY material (objects.h:1103-1107).
- Chewing through walls/doors/boulders breaks foodless
  (hack.c:722 u.uconduct.food++).

### Corrected
1. **"Brown and yellow puddings"** — no yellow pudding exists;
   vegetarian-safe puddings are gray ooze, brown pudding, green
   slime (all S_PUDDING except black). Fixed.
2. **Shriekers listed separately** — they're S_FUNGUS, already
   covered by "all F (fungi and molds)." Removed.
3. **Vegan list omitted fortune cookies** — eat.c:3016 lists
   FORTUNE_COOKIE as VEGGY-but-vegan-violating. Spoiler had
   contradictory advice (fortune-cookies-OK in vegetarian, but
   not vegan). Added to vegan-violating list explicitly.
4. **"Polymorphing breaks foodless"** — wrong. polyself.c has no
   u.uconduct.food increment; polymorph only breaks the polyself
   conduct. Reworded to point this out.
5. **"Prayer cures hunger when you're Weak or Fainting"** —
   wrong threshold. pray.c:275 TROUBLE_HUNGRY fires at
   uhs >= HUNGRY (Hungry / Weak / Fainting all qualify). Fixed.

### Notes
- Slow_digestion suppresses the main hunger tick (eat.c:3178) but
  the ring still consumes a small amount via the moves%20 wear
  cost. Effectively but not literally "stops entirely."
- Sacrifice value for Luck is per-corpse `value` (mr1), not
  monster `difficulty`.

---

## 2026-05-18 — Chapter audit #143: Kobolds `k`

Source: `spoilers/companion.md` line 7297. No corrections.

### Verified
- All four kobolds match monsters.h:624-656 for Lvl, Spd, AC,
  MR%, color, attacks.
- All carry M1_POIS (poisonous corpse) and MR_POISON.
- Shaman uses AT_MAGC/AD_SPEL via mcastu.c.

---

## 2026-05-18 — Chapter audit #144: Luck and Fortune

Source: `spoilers/companion.md` line 4790. 7 corrections.

### Verified
- Luck range -10..+10 baseline, ±13 with luckstone
  (you.h:465-468).
- Timeout cadence 600 turns, target = baseluck (timeout.c:606-619).
- Full moon +1 baseline, Friday 13 -1 (timeout.c:595-598).
- Three luck-conferring artifacts (Heart of Ahriman, Tsurugi,
  Orb of Fate) confirmed via SPFX_LUCK / confers_luck.
- Mirror break -2 (uhitm.c:1133, dokick.c:445).
- Cannibalism -5..-2 (eat.c:784).
- Killing same-alignment unicorn -5 (mon.c:3667).
- Throne lucky outcome +1 (sit.c:108).

### Corrected
1. **"Cursed luckstone reverses the drift, positive Luck slides
   down even faster"** — wrong. timeout.c:616-619 cursed-only
   luckstone holds negative Luck in place but positive Luck
   decays at the normal 1/600 rate toward baseline.
2. **"Uncursed luckstone freezes drift but gives no bonus"** —
   wrong. attrib.c:441-450 set_moreluck gives +3 to any
   non-cursed luckstone, blessed or uncursed alike.
3. **"Killing a peaceful creature: -1 to -5"** — wrong as a
   range. mon.c:3665 gives change_luck(-1) with 50% probability.
   The -5 result is only for co-aligned unicorns (mon.c:3667),
   a separate case.
4. **"At Luck -10 or worse, prayer always fails"** — wrong
   threshold. pray.c:2155 rejects prayer on ANY negative Luck,
   not just at -10.
5. **"Going down stairs in Sokoban: -1"** — fabricated. No luck
   penalty for descending Sokoban stairs. sokoban_guilt fires
   on boulder squeeze, fracture, polymorph, scroll of earth,
   and dismount-onto-boulder — not stair use.
6. **"Throw real gem to cross-aligned unicorn -3 to +3"** —
   that's only for fully identified gems (dothrow.c:2334
   rn2(7)-3). Unidentified is -1 to +1 (dothrow.c:2349
   rn2(3)-1). Split into two rows.
7. **"Identifying gems for a shopkeeper +1"** — no such mechanic
   in shk.c. Fabricated. Dropped from the table.

### Added
- killed_leader penalty: -4 to baseline luck for the rest of the
  game (timeout.c:600-601).
- Doubled drift rate (300 turns) when carrying the Amulet of
  Yendor or u.ugangr > 0 (timeout.c:607).
- Archeologist + fedora gives +1 baseline luck (timeout.c:603-604)
  — not added inline yet, noted for future polish.

---

## 2026-05-18 — Chapter audit #145: Sokoban conduct

Source: `spoilers/companion.md` line 6370. 1 correction.

### Verified
- u.uconduct.sokocheat exists (you.h:160), incremented by
  sokoban_guilt() which also calls change_luck(-1)
  (trap.c:7039-7054).
- Trigger sites: squeeze (hack.c:299, 307, 398, 403), polymorph
  boulder (zap.c:1711), fracture (zap.c:5556), scroll of earth
  (read.c:1951), dismount onto boulder (steed.c:767).
- Teleportation blocked by level noteleport flag
  (teleport.c:1185).
- Achievement reported only if branch entered
  (insight.c:2215-2228); set only if !u.uconduct.sokocheat
  (topten.c:600).

### Corrected
1. **"No digging through the puzzle levels"** — digging doesn't
   trigger sokoban_guilt. dig.c has no such call. The
   pick-axe/mattock conduct path is via fracturing a boulder
   (zap.c:5556 breakobj), not via floor digging. Reworded to
   enumerate the actual triggers with Luck cost.

---

## 2026-05-18 — Chapter audit #146: Lizards `:`

Source: `spoilers/companion.md` line 8159. No corrections.

### Verified
- All 8 entries (newt, gecko, iguana, baby crocodile, lizard,
  chameleon, crocodile, salamander) match monsters.h:3260-3324
  for stats, attacks, and flags.
- Lizard corpse cures stoning (eat.c:827-830 fix_petrification).
- Lizard corpses never rot (eat.c:1483, 1510).
- Newt corpse → 1-3 Pw via eye_of_newt_buzz (eat.c:1102-1123).
- Chameleon is M2_SHAPESHIFTER (monsters.h:3305).
- Salamander 4-attack chain (weap 2d8 / touch 1d6 fire / hug 2d6 /
  hug 3d6 fire) matches monsters.h:3318-3320.

---

## 2026-05-18 — Chapter audit #147: Felines `f`

Source: `spoilers/companion.md` line 7211. 2 reframings; no
substantive errors.

### Verified
- All 8 felines (kitten, housecat, jaguar, lynx, panther, large
  cat, tiger, displacer beast) match monsters.h:381-444.
- Displacer beast row consistent with prior #42/#106/#107 prose
  (lvl 12, AC -10, 4d4/4d4/2d10, MR 0, speed 12, M3_DISPLACES).
- Tameable (M2_DOMESTIC) entries: kitten, housecat, large cat.

### Reframed
- "Tigers are good early companions if tamed" — tigers are
  M2_HOSTILE, difficulty 8, only tameable via magic. Not really
  "early."
- "Kittens are common Valkyrie/Wizard/Tourist starting pets" —
  Wizard guarantees a kitten (role.c:548 PM_KITTEN); Valkyrie and
  Tourist roll 50/50 via dog.c:90-101. Clarified.

---

## 2026-05-18 — Chapter audit #148: Morning star

Source: `spoilers/companion.md` line 6769. No corrections.

### Verified
- Damage 1d4+1d4 / 1d6+1 (objects.h:364 sdam=4, ldam=6; weapon.c:
  225-289 bonus dice).
- Weight 120, cost 10, hit 0, iron — all match.
- P_MORNING_STAR is its own skill (skills.h:35 id 12).
- No artifact form (no MORNING_STAR entry in artilist.h).

---

## 2026-05-18 — Chapter audit #149: Mummies `M`

Source: `spoilers/companion.md` line 7757. 1 correction +
consistency fixes.

### Verified
- All 8 mummies (kobold/gnome/orc/dwarf/elf/human/ettin/giant) match
  monsters.h:1901-1968 for stats, attacks, colors.
- All mummy attacks are AT_CLAW AD_PHYS (no special status effect).
- All mummies have MR_COLD | MR_SLEEP | MR_POISON, M1_POIS,
  M1_MINDLESS, M2_UNDEAD.

### Corrected
1. **"Touch curses your worn items. Bring uncursing on hand."** —
   wrong. AD_CURS is gremlins (monattk.h:92); mummies do plain
   AD_PHYS. No special mummy curse logic in mhitu.c/uhitm.c/
   mhitm.c. The line was residue from the "mummy withering" myth
   that audit #46 was supposed to scrub. Reworded to factual
   plain-physical + undead-turning vulnerability.

### Consistency
- elf mummy and human mummy rows were missing the "cold-res,
  sleep-res, pois-res" notes that all other mummy rows carry.
  Added.

---

## 2026-05-18 — Chapter audit #150: The Riders

Source: `spoilers/companion.md` line 2054. 4 corrections.

### Verified
- Three Riders are unique, level 30, M1_REGEN, M1_SEE_INVIS, HP
  100, AC -5 (monsters.h:3144-3173).
- All have AT_TUCH 8d8 ×2 attacks.
- Pestilence/Famine second-hit stun-downgrade real (mhitu.c:337-346).
- Famine's hit adds rn1(40,40) = 40-79 hunger (uhitm.c:3791-3795).
- Astral placement: each in a different round room
  (dat/astral.lua:113, 121, 129).
- Revival: minimum 6 turns for Death, 12 for others; 1/3 chance/turn
  (mkobj.c:1371-1382).

### Corrected
1. **"Permanently displaced"** — wrong. M3_DISPLACES at
   monflag.h:175 means "moves monsters out of its way" (shoves
   them aside as it walks), NOT the cloak-of-displacement evasion.
2. **"Ignore magic resistance for their signature attacks"** —
   wrong for Death. uhitm.c:3858-3883 shows Antimagic blocks the
   3/20 touch-of-death instakill case; base damage still goes
   through but the kill is blocked.
3. **"Eating their corpses is fatal in different ways for each"**
   — wrong. All three trigger the same `done(DIED)` with killer
   text "unwisely ate the body of <name>" (eat.c:831-849).
4. **"Famine drives you instantly to Weak or Fainting"** —
   overstated. 40-79 hunger units won't drop a Satiated hero
   below Hungry in one swing.

### Added
- **Sick resistance is the only complete defense against
  Pestilence** (mhitu.c:1033-1043 make_sick with SICK_NONVOMITABLE).
  Unicorn horn does not cure the resulting food poisoning once
  contracted.

---

## 2026-05-18 — Chapter audit #151: A Practical Strategy

Source: `spoilers/companion.md` line 2911. 1 prose fix.

### Verified
- Altar BUC reveal (do.c:379-389 doaltarobj).
- Engrave-test costs one charge (engrave.c:792-799 + zap.c:2520).
- Wand of digging auto-IDs from engrave message
  (engrave.c:684-704 doknown=TRUE).
- All 12 amulet costs are 150 (objects.h:834 AMULET() macro).

### Corrected
1. **"A wand that freezes your engraving is cold"** — actual
   WAN_COLD engrave message is "A few ice cubes drop from the
   wand" (engrave.c:658-661). The vanish/freeze branch only
   triggers when overwriting an existing BURN engraving (FALLTHROUGH
   at engrave.c:662-664). Reworded to "drops ice cubes."

---

## 2026-05-18 — Chapter audit #152: Gremlins `g`

Source: `spoilers/companion.md` line 7230. 1 correction.

### Verified
- All three stats rows match monsters.h:448-473 for
  Lvl/Spd/AC/MR/attacks/colors.
- gremlin attacks claw 1d6 / claw 1d6 / bite 1d4 / claw curse
  (AD_CURS).
- gremlin M1_SWIM, M1_POIS, M2_STALK, MR_POISON.
- gargoyle/winged-gargoyle M1_THICK_HIDE, MR_STONE; winged also
  M1_FLY.

### Corrected
1. **Headnote conflated water-split with night-curse**. Per
   mon.c:987-992, water/fountain triggers a gremlin SPLIT (2/3
   chance per step). Per uhitm.c:3040-3057 + sit.c:644+
   attrcurse(), the AD_CURS attack only fires at NIGHT (early-
   returns during day) and strips a random hero intrinsic, not
   curses items. Reworded to separate the two mechanics.

---

## 2026-05-18 — Chapter audit #153: Sokoban Level 1, Version B

Source: `spoilers/companion.md` line 5642. No corrections.

### Verified
- Map walls/floors and all 12 boulders A-L match soko4-2.lua:9-21,
  29-42.
- Upstair (2,2), branch portal (4,2), 10 pits + 2 rolling-boulder
  traps, 2 always-scrolls-of-earth at (2,10)/(3,10).
- All 16 numbered solution steps land on lua floor with cardinal
  approach squares; no diagonal pushes; no pulls.
- "Two boulders (D and E) remain" tally consistent with 10 pits +
  H-square wall-gap fill = 11 targets; 12 boulders − 11 = 1
  surplus, plus the H-square filling makes the D/E pair the
  remainder.

---

## 2026-05-18 — Chapter audit #155: Zruties

Source: `spoilers/companion.md` line 8354. No corrections.

### Verified
- LVL(9, 8, 3, 0, 0) at monsters.h:1196 → table Lvl 9, Spd 8, AC 3,
  MR% 0 all match.
- Color brown matches CLR_BROWN (monsters.h:1202).
- Attacks claw 3d4 · claw 3d4 · bite 3d6 match AT_CLAW/AD_PHYS x2 +
  AT_BITE/AD_PHYS (monsters.h:1197-1198).
- Symbol `z` matches MONSYM(26, 'z', ZRUTY, S_ZRUTY) at defsym.h:325.
- Single species in S_ZRUTY class; table has one row, correct.
- Slavic-folklore framing matches data.base entry ("wild and gigantic
  beings, living in the wildernesses of the Tatra mountains").

### Notes
- Notes column left blank; M2_STRONG (can force locks/boulders) and
  M1_CARNIVORE flags exist but are not surfaced. Not wrong — peer
  rows in the section are equally terse.

---

## 2026-05-18 — Chapter audit #156: Bats and birds

Source: `spoilers/companion.md` line 8385. 1 correction.

### Wrong → fixed
- Prose claimed "Vampire bats can give lycanthropy." This is wrong:
  the vampire bat's second attack is AD_DRST (Strength drain, poison-
  flavored), not AD_WERE (lycanthropy, value 29). Lycanthropy comes
  only from were-creatures (`@`). Rewrote prose to:
  "Vampire bats drain Strength on the second bite (poison-flavored;
  poison resistance blocks it)."
- Table cell "bite poison" for the second vampire-bat attack
  conflated the poison resistance gate with the actual damage type.
  Changed to "bite drain-Str" to match the convention used elsewhere
  in companion.md for AD_DRST attacks.

### Verified
- All four roster entries present and ordered correctly: bat, giant
  bat, raven, vampire bat (monsters.h:1269-1297).
- bat: Lvl 0, Spd 22, AC 8, MR 0, bite 1d4, brown — matches.
- giant bat: Lvl 2, Spd 22, AC 7, MR 0, bite 1d6, red — matches.
- raven: Lvl 4, Spd 20, AC 6, MR 0, bite 1d6 + claw-blind 1d6 (AD_BLND),
  black — matches.
- vampire bat: Lvl 5, Spd 20, AC 6, MR 0, black; MR_SLEEP | MR_POISON;
  M1_REGEN; M1_POIS (poisonous corpse) — flags match.
- "All bats and birds fly" — all four carry M1_FLY.

---

## 2026-05-18 — Chapter audit #157: Bow

Source: `spoilers/companion.md` line 7477. No corrections.

### Verified
- arrow: wt=1, cost=2, 1d6/1d6, hit=0, iron — objects.h:141-143.
- elven arrow: wt=1, cost=2, 1d7/1d6, hit=0, wood — objects.h:144-146.
- orcish arrow: wt=1, cost=2, 1d5/1d6, hit=0, iron — objects.h:147-149.
- silver arrow: wt=1, cost=5, 1d6/1d6, hit=0, silver — objects.h:150-152.
- ya: wt=1, cost=4, 1d7/1d7, hit=+1, metal — objects.h:153-154.
- bow / elven bow / orcish bow / yumi: wt=30, cost=60, hit=0, wood —
  objects.h:395-402.
- Yumi prob=0 in C → never spawns randomly, only via Samurai start
  inventory; "The Samurai's bow" note is accurate.

### Notes
- Section is silent on bow multishot mechanics (Ranger +1, Samurai
  +1 on ya+yumi, race-launcher matching, Longbow of Diana, skill
  bonuses). Not wrong — but the analogous Crossbow section explains
  multishot. Coverage gap rather than a correction; left as-is for
  this audit pass.

---

## 2026-05-18 — Chapter audit #154: Sokoban Level 2, Version A

Source: `spoilers/companion.md` line 6212. No corrections.

### Verified
- Map walls/floors match `soko3-1.lua:9-22` exactly under spoiler→lua
  offset (subtract 1 from each coord).
- Down stair at spoiler (12,3) = lua (11,2) matches
  `des.stair("down", 11, 02)` (soko3-1.lua:23).
- Up stair `<` at spoiler (24,5) = lua (23,4) matches
  `des.stair("up", 23, 04)` (soko3-1.lua:24).
- Locked door `+` at spoiler (28,10) = lua (27,9) matches
  `des.door("locked", 27, 09)` (soko3-1.lua:25).
- All 20 spoiler boulders A-T map exactly onto the 20
  `des.object("boulder",...)` calls at soko3-1.lua:31-53.
- Rolling-boulder trap → at spoiler (12,11) = lua (11,10) matches
  soko3-1.lua:58.
- 15 hole traps ^ at spoiler cols 13-27 row 11 = lua cols 12-26
  row 10 match soko3-1.lua:59-73.
- Sample solution steps 1-3 verified: destinations are floor, approach
  squares reachable, all cardinal pushes (no diagonals, no pulls).
- "5 boulders remain (B, C, D, I, Q)" tally consistent: 20 placed −
  15 finish-push targets (15 holes) = 5 surplus.

### Close calls
- Step 4 prose lists completion order "T, S, M, R, K, J, and L."
  Reading this as a strict push order is infeasible (L at lua (8,8)
  blocks J pushing straight down column 8); feasible only if the
  solver reroutes J right first. The order should be read as "which
  boulders to finish next," not a literal sequence.

---

## 2026-05-18 — Chapter audit #158: Sea monsters `;`

Source: `spoilers/companion.md` line 8998. No corrections.

### Verified
- All 6 entries match monsters.h:3205-3256 for color, Lvl, Spd, AC,
  MR%, and attack chains:
  - jellyfish: blue, 3/3/6/0, sting 3d3 AD_DRST, MR_POISON.
  - piranha: red, 5/18/4/0, bite/bite 2d6 AD_PHYS.
  - shark: gray, 7/12/2/0, bite 5d6 AD_PHYS.
  - giant eel: cyan, 5/9/-1/0, bite 3d6 + tuch AD_WRAP.
  - electric eel: bright-blue, 7/10/-3/0, bite 4d6 AD_ELEC + tuch
    AD_WRAP, MR_ELEC.
  - kraken: red, 20/3/6/0, claw/claw 2d4 + hug 2d6 AD_WRAP + bite 5d4.
- "All sea monsters swim and are amphibious" — every entry carries
  `M1_SWIM | M1_AMPHIBIOUS` (monsters.h:3210, 3218, 3226, 3235, 3244,
  3254).
- AD_WRAP grab-and-drown is real: `mhitm_ad_wrap` sets `u.ustuck`,
  then on a subsequent turn the hero in a pool without Swimming /
  Amphibious / Breathing dies via `done(DROWNING)` (uhitm.c:3378-3401).
- jellyfish poison-resistance + poisonous-corpse justified by
  M1_POIS + MR_POISON.

### Close calls
- Prose "drags you under" is metaphorical — the C code does not move
  the hero; it grabs them while they are already on a water tile.
  Reasonable shorthand.
- jellyfish sting rendered as "3d3 poison" — AD_DRST is Str-drain
  (poison-flavored), not generic poison damage. Loose label,
  consistent with the section's tone.

---

## 2026-05-18 — Chapter audit #159: Dogs and canines `d`

Source: `spoilers/companion.md` line 7954. 2 corrections.

### Wrong → fixed
- **little dog starting roles**: companion claimed "Common
  Archeologist/Caveman/Samurai starting pet." Archeologist is wrong
  — role.c:46 sets Archeologist `petnum = NON_PM`, falling through to
  the cat/dog coin flip in dog.c:100, so no guaranteed dog.
  Guaranteed-little-dog roles are Caveman (role.c:128), Ranger
  (role.c:387), and Samurai (role.c:428). Rewrote to "Guaranteed
  Caveman/Ranger/Samurai starting pet."
- **Cerberus "Reflection"**: companion claimed Cerberus has
  "Reflection + fire resistance only." Cerberus carries only
  `MR_FIRE, MR_FIRE` (monsters.h:316). No `MR_*` reflection flag
  exists in C, and grep on `nethack-c/upstream/src/` returns no
  special-case reflection code for Cerberus. Dropped the claim;
  added build-flag caveat (see below).

### Verified
- Pack-hunting intro: jackal/coyote/wolf/warg/winter wolf cub/hell
  hound pup all carry `G_SGROUP` (monsters.h:200, 214, 258, 277,
  284, 298).
- Werejackal/werewolf lycanthropy: both `AT_BITE, AD_WERE`
  (monsters.h:222, 269).
- All 15 mainline rows (jackal, fox, coyote, werejackal, little dog,
  dingo, dog, large dog, wolf, werewolf, winter wolf cub, warg,
  winter wolf, hell hound pup, hell hound) match monsters.h:199-310
  exactly for color, Lvl, Spd, AC, MR, attack dice, and resistance
  flags.
- HI_DOMESTIC = CLR_WHITE (color.h:37), so the "white" color on
  little dog / dog / large dog is correct.

### Close calls
- Cerberus is `#ifdef CHARON`-gated (monsters.h:311, 321) and
  `CHARON` is not `#define`d in any default header — Cerberus does
  not compile into the default build. Added the build-flag caveat to
  the row note rather than removing the row outright, since players
  building with `-DCHARON` will encounter it.
- Werejackal/werewolf carry `G_NOCORPSE` (monsters.h:221, 268) plus
  `M1_POIS` (monsters.h:225, 272). The "poisonous-corpse" flag is
  technically about a corpse that cannot exist. Left as-is — peer
  rows use the same notation for monsters with G_NOCORPSE.

---

## 2026-05-18 — Chapter audit #160: Pick-axe

Source: `spoilers/companion.md` line 7316. 1 correction.

### Wrong → fixed
- **Pick-axe row missing entirely.** The section header was "Pick-axe"
  but the table held only the dwarvish mattock. Added the pick-axe row
  per objects.h:1007-1009 (WEPTOOL, wt=100, cost=50, 1d6/1d3, iron) and
  noted that both share `P_PICK_AXE` skill and both route through
  `use_pick_axe()` at apply.c:4290-4292.

### Verified
- Dwarvish mattock stats match objects.h:345-347: wt=120, cost=50,
  1d12 / 1d8+2d6 (sdam=12, ldam computed via the bigmonst bonus at
  weapon.c:257-261), hit −1, iron, bimanual.
- Both `PICK_AXE` and `DWARVISH_MATTOCK` are `is_pick()` true
  (obj.h:220-222), routed through `use_pick_axe()` at apply.c:4290-4292.
- "Two-handed (3/2 Str damage bonus)" matches the bimanual strength
  bonus path at uhitm.c:1455-1468.
- Slight hit penalty (−1) is `oc_hitbon` direct (weapon.c:159).

### Notes
- No role/race damage or hit bonus exists for either weapon; the
  section correctly omits any such claim.
- Dwarves prefer mattocks as a weapon-of-choice listing
  (weapon.c:693, 821, 833) — selection only, no numerical bonus.

---

## 2026-05-18 — Chapter audit #161: Polymorph Restrictions

Source: `spoilers/companion.md` line 6806. Substantive rewrite.

### Wrong → fixed
- **"Don't read a cursed scroll of polymorph"**: there is no
  `SCR_POLYMORPH` in NetHack 5.0. The polymorph item set is
  RIN_POLYMORPH, RIN_POLYMORPH_CONTROL, POT_POLYMORPH, SPE_POLYMORPH,
  WAN_POLYMORPH (objects.h). The cursed-scroll claim is a holdover
  from older lore. Dropped.
- **Missing monster-induced poly source.** Genetic engineer's claw
  (AD_POLY) calls `polyself(POLY_NOFLAGS)` on the hero
  (mhitm_ad_poly at uhitm.c:3729; mon_poly at mhitm.c:1122-1144),
  which increments `polyselfs` via `polymon()`. Added.
- **Missing corpse-eating sources.** Eating a chameleon /
  doppelganger / sandestin corpse routes through `polyself`
  (eat.c:1244-1263); eating any mimic corpse directly increments
  `u.uconduct.polyselfs` at eat.c:1199 before forcing mimic form.
  Added.
- **Missing forced-transformation sources.** Failing to cure
  slimedness ticks `polymon(PM_GREEN_SLIME)` at timeout.c:493 (with
  comment at 484-485 explicitly noting `polymon` now handles the
  conduct increment). Surviving a stoning attack via
  `poly_when_stoned` calls `polymon(PM_STONE_GOLEM)` (trap.c:3848,
  uhitm.c:2155 / 3928 / 5951, mhitu.c:1751, eat.c:797). Both added.

### Verified
- Two separate conducts with separate counters: `u.uconduct.polyselfs`
  and `u.uconduct.polypiles` (you.h:155-156); achievement names
  `polyselfless` and `polyless` (topten.c:594-595).
- Self-poly sources that DO break the conduct: potion of polymorph
  quaff (potion.c:1322-1323), ring of polymorph (worn), wand/spell
  of polymorph zapped at self (zap.c:2804-2808), polymorph trap
  (trap.c:2495).
- Polypile sources: wand/spell zapped at object (zap.c:2191-2200),
  dipping an item into POT_POLYMORPH or vice versa
  (potion.c:2468-2478).

### Close calls / now in prose
- **System shock**: failed shock returns BEFORE `polymon()` runs
  (polyself.c:488-495), so it does NOT break polyselfless. Added.
- **Amulet of Unchanging**: short-circuits every poly path
  (polyself.c:483-486; potion.c:1321; trap.c:2486-2488). Added as
  the canonical safety blanket.
- **newman()** (~1-in-5 polyself outcomes): bypasses the achievement
  per the header comment at polyself.c:446. Left out of prose to
  keep the section terse — the conduct counter doesn't advance, but
  no player relies on this for the conduct.
- **Polymorph-trap iron-shoes swap**: trap.c:2481 uses `poly_obj`
  directly without incrementing `polypiles`. Left out — the spoiler's
  "other means of transforming objects" already covers polypile
  enough.

---

## 2026-05-18 — Chapter audit #162: Whip

Source: `spoilers/companion.md` line 7479. 1 correction.

### Wrong → fixed
- **Rubber hose "Damages even Shades"**: false. Rubber hose is PLASTIC
  (objects.h:375); `shade_glare()` returns TRUE only for SILVER
  material (or undead-bonus artifacts) per artifact.c:555-562 and
  weapon.c:307-308. Rubber hose hits Shades for 0 like any other
  non-silver mundane weapon. Removed the claim; reworded the joke-
  weapon note to "never spawns randomly" (prob=0 in C, so it only
  appears via wishing/polypile).

### Verified
- Bullwhip stats: wt=20, cost=4, 1d2/1, hitbon=0, LEATHER —
  objects.h:390-392.
- Rubber hose stats: wt=20, cost=3, 1d4/1d3, hitbon=0, PLASTIC —
  objects.h:374-376.
- P_WHIP = skill 26 (skills.h:49); both weapons share it.
- Archeologist starter: BULLWHIP in u_init.c:42-44; gets P_WHIP at
  Expert (u_init.c:268). Ranger and Tourist train it at Basic
  (u_init.c:459, 515) without any damage/hit bonus.
- Apply-to-disarm at apply.c:3127-3174 — adjacent direction
  (`rx = u.ux + u.dx`), gated on `MON_WEP(mtmp)` non-NULL and
  `proficient && (!Fumbling || !rn2(10))`.
- Apply-to-yank at apply.c:3069-3125 — anchors on boulder
  (`sobj_at(BOULDER, rx, ry)`), furniture (`IS_FURNITURE`), or big
  monster (`bigmonst(mtmp->data) && canspotmon(mtmp)`).

### Close calls
- Added "(only when the target is wielding a weapon)" to the disarm
  note. Against an unarmed visible monster, the whip falls through
  to a regular melee attack — worth being precise about.

---

## 2026-05-18 — Chapter audit #163: Short sword

Source: `spoilers/companion.md` line 7242. 0 numeric corrections;
1 small content addition.

### Added
- Plain short sword's Note expanded to mention that Samurai's
  *wakizashi* is just a short sword aliased in objnam.c:106.

### Verified
- All 4 rows match objects.h:245-254 exactly:
  - short sword: 30/10, 1d6/1d8, hit 0, iron.
  - elven short sword: 30/10, 1d8/1d8, hit 0, wood.
  - orcish short sword: 30/10, 1d5/1d8, hit 0, iron.
  - dwarvish short sword: 30/10, 1d7/1d8, hit 0, iron.
- All four share P_SHORT_SWORD; scimitar is P_SABER (objects.h:257)
  and correctly excluded.
- Rogue's starter: SHORT_SWORD at u_init.c:133-134.
- Barbarian carries SHORT_SWORD as secondary (u_init.c:63) — not
  surfaced in the table, consistent with sibling rows.
- No artifact uses SHORT_SWORD base (artilist.h grep confirms).

---

## 2026-05-18 — Chapter audit #165: Lance

Source: `spoilers/companion.md` line 7467. 1 correction.

### Wrong → fixed
- **"Useless on foot"**: overstated. Without a steed, the lance is a
  regular one-handed piercing weapon (1d6/1d8, P_LANCE skill, hit
  bonus 0); it hits and damages normally, just without the joust
  bonus. Reworded to "No bonus on foot" and quantified the joust
  bonus.

### Verified
- Stats match objects.h:349: wt=180, cost=10, 1d6/1d8, hitbon=0, IRON.
- P_LANCE is its own skill (not P_POLEARMS) per the comment at
  objects.h:343-344.
- Knight starter: LANCE at u_init.c:92.
- Joust mechanic: gated on `u.usteed` at uhitm.c:1041-1043;
  skill-based hit chance (expert 80%, skilled 60%, basic 40%,
  unskilled 20%) at uhitm.c:2121-2122; +2d10 primary damage (+2d2
  off-hand) at uhitm.c:1546; rare crit can shatter the lance
  (uhitm.c:2123-2125, "shatters on impact!" at uhitm.c:1559).
- One-handed: per the comment at objects.h:344 "lance isn't even
  two-handed."

---

## 2026-05-18 — Chapter audit #164: The Oracle

Source: `spoilers/companion.md` line 966. 2 corrections.

### Wrong → fixed
- **"a fountain" (singular)**: actually four fountains. `oracle.lua:19-22`
  places fountains at (0,1), (1,0), (1,2), (2,1) around the Oracle
  in the inner Delphi sub-room. Rewrote to "four fountains."
- **"Minor consultations ... occasionally useful but mostly
  atmospheric"**: misleading. `doconsult()` calls
  `outrumor(1, BY_ORACLE)` at rumors.c:747; `getrumor()` with
  `truth=1` always returns TRUE rumors (rumors.c:147-156). Minor
  consultations always pull from `dat/rumors.tru` — real, reliable
  game hints (same source fortune cookies use). Rewrote to clarify
  the tone (fortune-cookie-style) without implying the content is
  random. Also surfaced both numeric prices: 50 zorkmids minor,
  500 + 50 × ulevel major (rumors.c:699).

### Verified
- Level range DL 5-9: dungeon.lua:60-66 (`base = 5, range = 5`) +
  dungeon.c:405-409 interprets as `base..base+range-1`.
- "Flanked by centaur statues" matches oracle.lua:9-16 (eight S_CENTAUR
  statues around the inner room).
- Peaceful behavior: PM_ORACLE has `AT_NONE`, `M2_PEACEFUL`, and
  `G_NOGEN | G_UNIQ` (monsters.h:2738-2745). She has a passive 0d4
  AD_MAGM but doesn't initiate combat.
- No role-specific cost branch in doconsult() (rumors.c:696-767).

### Close calls
- Refusal behavior is asymmetric: minor refuses outright if you have
  fewer than 50 gold (rumors.c:724-727); major takes ALL your gold as
  a "cheapskate" consultation that delivers a random non-special
  oracle (rumors.c:738, 753-760). Not currently in prose, but worth
  knowing — the major-but-broke path is a trap for short-on-gold
  players. Left out to keep the section terse.

---

## 2026-05-18 — Chapter audit #166: Umber hulks `U`

Source: `spoilers/companion.md` line 8756. 1 correction.

### Wrong → fixed
- **"Don't melee without blindness or free action"**: Free Action does
  NOT block AD_CONF. A grep across `src/*.c` shows `Free_action` is
  only checked against paralysis, holding, and sleep; AD_CONF in
  `mhitu.c:1759-1777` makes no Free_action check. Blindness still
  works because the gaze is gated by `mcanseeu` (mhitu.c:1681-1682)
  which requires mutual sight. Reworded to spell out that free
  action doesn't help.

### Verified
- Row stats match monsters.h:2267-2277: L9, Spd 6, AC 2, MR 25,
  brown, claw 3d4 · claw 3d4 · bite 2d5 · gaze confuse (AT_GAZE,
  AD_CONF, 0, 0).
- M1_TUNNEL set (monsters.h:2275); mon.c:2073 grants ALLOW_DIG
  (mon.c:2096-2097), so they can dig through walls.
- Confusion stacks: make_confused(HConfusion + conf, FALSE) at
  mhitu.c:1768-1773 with `conf = d(3, 4)`.

---

## 2026-05-18 — Chapter audit #167: Major demons `&`

Source: `spoilers/companion.md` line 8949. 2 corrections.

### Wrong → fixed
- **"All except erinys also follow you up and down stairs"**: erinys
  carries M2_STALK (monsters.h:2958) and does follow. In fact every
  row in this section carries M2_STALK, so the qualifier is unsup-
  ported. Rewrote to "They all follow you up and down stairs." The
  erinys row's "(no follows stairs)" note was also dropped; the row
  also had "—" for color and attacks where the C source clearly says
  CLR_RED with AT_WEAP/AD_DRST 2d4 — fixed both.
- **Amorous demon "Displays as succubus (to male PCs) or incubus
  (to female PCs)"**: form is determined by the demon's own randomly-
  assigned gender (Mgender(mon) at mhitu.c:1988-1989), not by the
  player's gender. Reworded to match the Seduction section (audit
  #33's earlier finding).

### Verified
- Roster stats verified against monsters.h:2911-3194 for every row.
- M2_PRINCE princes (Orcus 3086, Geryon 3097, Dispater 3107,
  Baalzebub 3117, Asmodeus 3127, Demogorgon 3138). Yeenoghu/Juiblex
  are M2_LORD (3064, 3075).
- Riders excluded from M2_DEMON (lines 3151/3161/3171) so Demonbane
  bonus + bribery don't apply — table correctly lists them with the
  "Rider" note elsewhere.
- Lord Surtur is S_GIANT (monsters.h:3749), correctly excluded from
  `&`.
- Bribery prose accuracy: minion.c:267-276 (Demonbane disable),
  cross-alignment halves demand, money_cnt skips containers.

### Close calls
- balrog and amorous demon don't summon (mhitu.c:967). Not surfaced
  in the table — could be added.

---

## 2026-05-18 — Chapter audit #168: Piercers `p`

Source: `spoilers/companion.md` line 8199. No corrections.

### Verified
- 3 rows match monsters.h:800-826: rock (L3/Spd1/AC3/bite 2d6, gray),
  iron (L5/Spd1/AC0/bite 3d6, cyan), glass (L7/Spd1/AC0/bite 4d6,
  white, MR_ACID).
- All three carry `M1_HIDE | M1_CLING`, qualifying as ceiling-hiders
  (mondata.h:43-45).
- Hiding gated by `has_ceiling(&u.uz)` at mon.c:4672 — they can't
  hide on ceiling-less levels like Plane of Air.
- Drop-on-walk-under at hack.c:3417-3441; the drop damage is `d(4,6)`
  for ALL species regardless of the AT_BITE die (rock's drop is 4d6,
  not 2d6).

### Notes
- Re-hiding: piercers can `restrap()` when unwatched (mon.c:1286-1294,
  4662-4689), gated by `rn2(3)` plus the ceiling check. Not currently
  in the row notes; could be added.

---

## 2026-05-18 — Chapter audit #169: Knife

Source: `spoilers/companion.md` line 7231. 0 numeric corrections; 2
content additions.

### Added
- Scalpel Notes: "The Healer's starter." (u_init.c:77).
- Crysknife note rewritten: "polymorphs" → "reverts" (in-game
  message at do.c:905 is the type-id swap path, not poly). Added
  that an erodeproof crysknife only reverts on ~10% of drops
  (do.c:911) — the canonical preservation play.

### Verified
- All 5 rows match objects.h:215-233 (P_KNIFE skill):
  - scalpel: prob=0, wt=5, cost=6, 1d3/1d3, +2 hit, METAL.
  - knife: prob=20, wt=5, cost=4, 1d3/1d2, hit=0, IRON.
  - stiletto: prob=5, wt=5, cost=4, 1d3/1d2, hit=0, IRON.
  - worm tooth: prob=0, wt=20, cost=2, 1d2/1d2, hit=0, BONE.
  - crysknife: prob=0, wt=20, cost=100, 1d10/1d10, +3, BONE.
- Crysknife→worm tooth swap on drop: `obj_no_longer_held` at
  do.c:903-918 switches `otyp` (not poly machinery). Wielded ones
  don't trigger this. Worm-tooth → crysknife fusion on enchant at
  wield.c:951-956.
- Athame is correctly NOT in this section — it's P_DAGGER skill
  (objects.h:213) and lives in the Dagger table.

---

## 2026-05-18 — Chapter audit #170: What to Pack

Source: `spoilers/companion.md` line 326. No corrections.

### Verified (qualitative)
- Tripe-rations-as-pet-food: dog/cat happy at dog.c:1055; humans get
  "Yak - dog food!" at eat.c:2138-2145.
- Altar BUC flash: amber for blessed, black for cursed; sets bknown
  (do.c:363-389).
- Pet cursed-item avoidance: dogmove.c:535-536, 1065-1067.
- Touchstone gem ID: apply.c:2658-2696.
- Floating-eye paralysis: uhitm.c:5853, 6022.

### Close calls
- "Tripe rations are for your pet" technically wrong for orc PCs
  (eat.c:2132-2136) and orc-route Caveman/Barbarian, but the
  simplification is fine for a beginner-targeted section.

---

## 2026-05-18 — Chapter audit #171: Imps and minor demons `i`

Source: `spoilers/companion.md` line 8075. 1 correction.

### Wrong → fixed
- **"Imps steal items and teleport away"**: imps only have AT_CLAW /
  AD_PHYS 1d4 (monsters.h:561-562). There is no AD_SITM and no
  AD_TLPT on any S_IMP entry — steal-and-teleport belongs to nymphs
  (AD_SITM) and leprechauns (AD_SGLD). The imp's distinctive trait
  is MS_CUSS (verbal abuse; handler at monmove.c:983-985 and
  sounds.c:1148-1150). Reworded the intro.

### Verified
- All 6 rows match monsters.h:544-587 for Lvl/Spd/AC/MR%/color and
  attack dice.
- All 6 carry M2_STALK (follow stairs).
- "All except imp are poison-resistant": imp has MR=0 (monsters.h:563);
  the other five carry MR_POISON.
- Tengu carries M1_TPORT | M1_TPORT_CNTRL (monsters.h:586) —
  intrinsics conferred when polymorphed / corpse-eaten; not a
  player-displacement attack.

### Notes
- M2_DEMON is NOT set on any S_IMP-class monster — they're not
  mechanical demons (`is_demon()` returns false). The section's
  title is class flavor. Not surfaced; left as-is.

---

## 2026-05-18 — Chapter audit #173: Nagas `N`

Source: `spoilers/companion.md` line 8627. 1 correction + 1 addition.

### Wrong → fixed
- **"Healers find the guardian naga peaceful"**: no mechanism exists.
  Guardian naga is `MS_MUMBLE` (monsters.h:2044), not MS_GUARDIAN or
  MS_LEADER, so `peace_minded()` at makemon.c:2270-2285 doesn't
  auto-peace it. No M2_PEACEFUL. PM_GUARDIAN_NAGA appears in the
  Rogue's role.c:338 entry (the Rogue's quest creature list), not
  the Healer's. Healer's quest creatures are S_RODENT / S_YETI /
  PM_SNAKE per role.c:173-176. Removed the false claim from prose
  and from the table row note.

### Added
- Black naga corpse confers poison + acid + stoning resistance
  (eat.c corpse-confer paths via the 2nd MR field at
  monsters.h:2020). This is genuinely useful — surfaced in the
  section intro so players know the eat is worth the acid splash.

### Verified
- All 8 rows match monsters.h:1972-2048 for Lvl/Spd/AC/MR%/Color.
- All 8 carry MR_POISON (intrinsic to S_NAGA, monsters.h:1976/1985/
  1994/2002/2011/2020/2029/2044).
- Red naga + red hatchling carry MR_FIRE (monsters.h:2010, 1979).
- Black naga + black hatchling carry MR_ACID | MR_STONE
  (monsters.h:1985, 2020).
- Guardian naga attack order spit / bite / touch / hug matches
  monsters.h:2041-2043.

### Close calls
- guardian naga's spit shown as "1d6 poison" — C is AD_DRST
  (str-drain, poison-flavored). The index row at line 1671 says
  "spit Str-drain poison" which is precise; the detailed table's
  "poison" shorthand loses that detail. Left as-is for now;
  could tighten in a future pass.

---

## 2026-05-18 — Chapter audit #172: Petrification (Stoning)

Source: `spoilers/companion.md` line 1937. Substantive rewrite — 3
corrections + 2 clarifications.

### Wrong → fixed
- **"acid blob corpses (which makes you immune outright)"**: acid
  blob corpse confers only TIMED stoning resistance —
  `HStone_resistance += d(3,6)` at eat.c:932-934 and eat.c:1089-1094
  (with debugpline literally noting "Giving timed stoning resistance
  temporarily"). Reworded to "pile up *timed* stoning resistance ...
  each one grants d(3,6) turns." Added that yellow dragon scale
  mail is the permanent alternative.
- **"amulet of unchanging to interrupt the process"**: Unchanging
  has no interaction with the stoning counter. It only blocks
  polymorph paths (polyself.c:1381-1384, do_wear.c:996, 1110). Worse,
  wearing it during stoning is harmful: it blocks the stone-golem
  auto-poly that polyself.c:807-811 grants when `poly_when_stoned`
  applies. Removed from defenses list and flagged in prose that
  wearing Unchanging during the countdown is actively bad.
- **"wand of polymorph ... to interrupt the process"**: misleading.
  Only `poly_when_stoned` monsters (golems, mondata.c:80-85) auto-
  cure stoning, and a plain wand-of-polymorph zap on self can't
  target that outcome. Removed from the active-defenses list.

### Added
- The five-tick countdown messages and the fact that message 3
  ("Your limbs have turned to stone") paralyzes the hero for three
  turns via `nomul(-3)` (timeout.c:163-165). Acting on tick 3 or
  later is impossible — the player must respond by tick 4 at the
  latest.
- Fumbling exception: stepping on a cockatrice corpse is safe only
  if you don't have Fumbling. Fumbling can trip-over the corpse and
  instapetrify per timeout.c:1256-1261.

### Verified
- Counter starts at 5: `make_stoned(5L, ...)` at uhitm.c:3937.
- Touching corpse without gloves: pickup.c:283-299 calls
  `instapetrify()`; `u_safe_from_fatal_corpse` checks `uarmg`
  (pickup.c:272-281).
- Kicking corpse without boots: dokick.c:542-555 checks `!uarmf`.
- Eating cockatrice/Medusa corpses: eat.c:795-797.
- Lizard corpse cures: eat.c:827-829.
- Acidic corpse cures: eat.c:860-861.
- Potion of acid cures: potion.c:1312-1313.
- Prayer cures (TROUBLE_STONED is first major trouble): pray.c:206-207.
- Stone-to-flesh self cures: zap.c:2974-2977.
- Wielded cockatrice with gloves as weapon: wield.c:140-153 path
  + `do_stone_mon()` at uhitm.c:3944+.

### Notes
- Section still doesn't cover cockatrice eggs (separate
  petrification paths: mthrowu.c:782, dothrow.c:1308/1403). Worth
  a follow-up pass but not corrected here to keep this audit
  focused.

---

## 2026-05-18 — Chapter audit #175: The Armory

Source: `spoilers/companion.md` line 3777 (heading), ~120 lines. 2
corrections + 1 close call addressed.

### Wrong → fixed
- **Enchantment "absolute safe limit is +5 for weapons and +3 for
  armor"**: weapons have NO destruction risk at all — above +9 the
  scroll just becomes probabilistic (read.c:1669-1671). Armor
  destruction begins above +3 (above +5 for special armor like
  elven items or the Wizard's cornuthaum, read.c:1179); cursing
  doesn't change the threshold. Reworded the section to spell this
  out.
- **DSM transformation "read a blessed scroll of enchant armor"**:
  the transformation triggers at `s >= 0` (read.c:1225), so any
  non-cursed scroll works. Reworded to "(non-cursed)".

### Close calls → fixed
- **"each color provides two extrinsic resistances"**: gray and
  silver DSM provide only the named one (do_wear.c:806-807 explicit
  "no extra effect" comments). Reworded to "most colors provide
  two extrinsic resistances; gray and silver provide only the
  named one."

### Verified
- Helm of caution: WARNING intrinsic, 50 zm, weight 50
  (objects.h:479-481).
- Gray DSM ANTIMAGIC, Silver DSM REFLECTING, Black DSM
  DISINT_RES + drain resistance, Green DSM POISON_RES + sickness
  immunity (objects.h:502-523; do_wear.c:807-883).
- Cloak of protection MC3 (single-item, objects.h:637-640);
  cloak of magic resistance MC1 (objects.h:643-645).
- Ring of protection +1 MC; amulet of guarding +2 MC; MC3 blocks
  90% of monster special attacks (uhitm.c:87 formula).
- Speed boots → FAST (objects.h:702); shield/amulet of reflection
  → REFLECTING (objects.h:676-678, 850-851).
- No body-armor speed penalty mechanic exists in C — section
  correctly does not claim one.

---

## 2026-05-18 — Chapter audit #176: Engravings

Source: `spoilers/companion.md` line 1408. 3 corrections + 1
clarification.

### Wrong → fixed
- **Athame "Several turns"**: uncursed athame is not in dulling_wep
  (engrave.c:1306), and as a WEAPON_CLASS it doesn't trigger the
  rate=1 branch (engrave.c:1321-1325). Rate stays at 10, so an
  8-char Elbereth finishes in a single occupation action — INSTANT.
  Cursed athame would dull and trigger rate=1. Split the table row
  into "uncursed athame (instant)" and "other edged weapon (several
  turns)".
- **Edged weapon "dulls weapon by −1"**: actually 1 enchantment per
  2 characters engraved (engrave.c:1357-1382, with comment table at
  1360-1361: -2 → 3 chars, -1 → 5, 0 → 7, +1 → 9, +2 → 11). An
  8-char Elbereth costs roughly -4 enchantment. Reworded.
- **Impairment "Instant methods (wand of fire, lightning, digging)
  bypass the per-letter check"**: only the DUST/BLOOD surface-
  garble (engrave.c:1223) is bypassed. The Blind 1/11, Confused
  1/7, Stunned 1/4, and Hallucinating 1/2 per-character scrambles
  at engrave.c:1224-1225 apply to ALL engraving types including
  wand-of-fire BURN. A hallucinating player using a wand of fire
  still scrambles roughly half the letters. Reworded.

### Clarified
- **"ad aerarium"** can mark either a same-level vault TELEP_TRAP
  (makevtele at mklev.c:820-824) OR a LEVEL_TELEP niche
  (mklev.c:809-811). Surfaced both outcomes — vault drops you into
  Croesus's 2×2 gold vault; level-teleporter sends you to a random
  dungeon level (teleport.c:1165-1234).

### Verified
- Engrave command `E` (engrave.c:956); finger writes DUST
  (engrave.c:558 default).
- Edged weapon engraves at ENGRAVE durability when not welded and
  spe > -3 (engrave.c:819-833).
- Wand of digging → ENGRAVE; wand of fire/lightning → BURN
  (engrave.c:684-734).
- DUST eroded by step (1 char per monster turn, monmove.c:734);
  BURN survives unless ice or magical (engrave.c:278).
- "Vlad was here" → TRAPDOOR (mklev.c:733 index 14).

---

## 2026-05-18 — Chapter audit #177: Iron Bars

Source: `spoilers/companion.md` line 1333. 1 substantive correction
plus material additions.

### Wrong → fixed
- **"small creatures can squeeze between"**: actually only TINY
  passes. `passes_bars` uses `verysmall(ptr)` = msize < MZ_SMALL
  (mondata.c:552-563 + mondata.h:11). Kittens and little dogs are
  MZ_SMALL (monsters.h:381-388) and do NOT pass through. Reworded
  to "tiny creatures (grid bugs, bats, rats)" and clarified that
  starting pets are too big. Pet-fetch path needs the pet to be
  polymorphed into a tiny form first.

### Added
- Wand/spell of **striking** and **force bolt** have no IRONBARS
  handler and pass through the bars without effect (zap.c:3676-3679,
  3122). Worth knowing because players sometimes try them.
- Wand of **lightning** melts bars too: ZT_LIGHTNING shares the
  ZT_ACID branch at zap.c:5344-5369 with a ~90% per-tile dissolve
  chance.
- **Rock mole** eats bars (metallivorous, hack.c:769-784) — viable
  polymorph form for clearing them.

### Verified
- Pick-axes bounce: "Clang!" at dig.c:1221-1223.
- Wand of digging fizzles horizontally: dig.c:1799-1802.
- Kicking just hurts: dokick.c:1131-1133.
- Thrown items stopped: hits_bars() at zap.c:3900-3913.
- Acid blob splash is passive-only (no IRONBARS path).
- Niche placement: mklev.c:782-794 (with rn2(3) corpse / rn2(3)
  random item; scroll of teleportation guaranteed if level allows
  teleport).

---

## 2026-05-18 — Chapter audit #178: Unicorns and horses `u`

Source: `spoilers/companion.md` line 8310. No corrections.

### Verified
- All 6 rows (pony / white/gray/black unicorn / horse / warhorse)
  match monsters.h:1002-1049.
- Unicorn alignments: white = lawful (maligntyp +7), gray = neutral
  (0), black = chaotic (-7) per monsters.h:1011, 1019, 1027.
- Same-aligned unicorns spawn peaceful (makemon.c:1339-1342);
  killing a co-aligned unicorn = -5 Luck + "you feel guilty"
  (mon.c:3666-3669).
- Throwing a gem to a unicorn: dothrow.c:2082-2098, 2309-2382 path
  pacifies + drops Luck change for real gems; worthless glass
  placates without Luck change but the gem is consumed.
- Knight's pony arrives saddled (dog.c:263-267).
- Unicorn-horn apply cures status troubles (apply.c:2259+).

---

## 2026-05-18 — Chapter audit #179: Engulfment from Hiding

Source: `spoilers/companion.md` line 2130. No corrections.

### Verified
- Lurker above: M1_HIDE | M1_FLY (ceiling-hider via mondata.h:43-45),
  monsters.h:981-989.
- Trapper: M1_HIDE on the floor (no fly), monsters.h:990-998.
- Both use AT_ENGL with AD_WRAP + AD_PHYS — NOT AD_DGST. The
  header comment at monsters.h:973-980 explicitly notes the 5.0
  retcon: "prior to 5.0, these were defined to do AD_DGST damage,
  but they don't swallow ... they enfold and crush or suffocate."
- Damage handler at mhitu.c:1437-1453.
- While engulfed, attacking in any direction targets `u.ustuck`
  (hack.c:2733-2737).
- Search reveals adjacent hidden monsters (detect.c:2016-2092);
  neither lurker nor trapper has M1_MINDLESS so telepathy works.
- Warning (ring / helm of caution) reveals via `warnreveal()` at
  detect.c:2107-2120: lurker mlev/4=2, trapper mlev/4=3 both
  pass the warning threshold.

---

## 2026-05-18 — Chapter audit #180: The Engrave Test (Wands)

Source: `spoilers/companion.md` line 2919. 1 correction + 2
additions.

### Wrong → fixed
- **"Wand unsuccessfully fights you (striking and others that
  can't engrave)"**: the unsuccessfully-fights string is striking-
  ONLY (engrave.c:602-605). Two other "immediate" wands have
  distinct diagnostic messages:
  - WAN_SLOW_MONSTER → "The bugs on the floor slow down!"
    (engrave.c:608-609)
  - WAN_SPEED_MONSTER → "The bugs on the floor speed up!"
    (engrave.c:614-615)
  Split the row to show these explicitly. Substituted the literal
  "floor" for the C `%s` (it's `surface(u.ux, u.uy)`, which is
  "floor" on a normal tile).
- **"You write in the dust ... wand has no engrave special-case
  (most beams)"**: misleading. The silent-dust outcome covers
  exactly five wands: WAN_NOTHING, WAN_UNDEAD_TURNING, WAN_OPENING,
  WAN_LOCKING, WAN_PROBING (engrave.c:635-640 empty cases). Plus
  WAN_STASIS (zapnodir with no message, zap.c:2562-2563). Reworded
  to enumerate them.

### Verified
- All other table entries match engrave.c per-wand cases at lines
  583-738 and the zapnodir handlers in zap.c:2538-2602.
- Wand-of-wishing engrave-test DOES grant a wish (engrave.c:594 →
  zap.c:2575-2585 calls makewish, gated on Luck+rn2(5)).
- Cursed wands may explode on engrave (engrave.c:794-797,
  WAND_BACKFIRE_CHANCE).

---

## 2026-05-18 — Chapter audit #181: Enhancing Skills

Source: `spoilers/companion.md` line 4790 (chapter, ~168 lines). 3
numeric corrections.

### Wrong → fixed
- **"Riding earns one tick every 101 squares ridden"**: actually
  100 (steed.c:393-396, `if (++u.urideturns >= 100)` resets to 0).
  The chapter header's audit comment also cited 101 — both fixed.
- **"absolute ceiling is 30 slots for an XL-30 crowned hero"**:
  actually 32 — start with 2 (u_init.c:884), gain one per XL
  (29 more by XL 30, pray.c:992-993), plus 1 for crowning.
  P_SKILL_LIMIT itself is 60 (skills.h:120) — the cap on
  advancements, not slots. Reworded to spell out the arithmetic.
- **"Rogues, Rangers, Tourists, Samurai each get two or three
  schools at Skilled or lower"**: Ranger divination caps at Expert
  (u_init.c:461). Split the line to call out Rangers separately.

### Verified
- Rank ladder Unskilled/Basic/Skilled/Expert/Master/Grand Master
  (skills.h:90-104).
- Practice thresholds 20/80/180/320/500 from `level² * 20`
  (skills.h:106; P_ADVANCE is not reset on rank-up so cumulative
  practice equals the threshold).
- Weapon to-hit/damage bonuses: -4/-2 (Unskilled), 0/0 (Basic),
  +2/+1 (Skilled), +3/+2 (Expert) at weapon.c:1559-1577, 1656-1675.
- Two-weapon penalty -9/-3, -7/-1, -5/0, -3/+1 (weapon.c:1582-1600,
  1680-1695); applied per swing.
- Practice trains only on `dmg > 1` hits (uhitm.c:849, 946, 1059,
  1494-1498).
- Spell practice = spell level per successful cast (spell.c:1597-1599).
- Starting at Basic = 20 practice pre-credit (weapon.c:1801).
- Crowning bonus slot (pray.c:992-994); one slot per XL gain
  (attrib.c:1068-1070).
- Restricted skills can never leave Unskilled except via artifact
  gift (weapon.c:1410-1421, `unrestrict_weapon_skill`).
- Wizard caps: long sword restricted, mace Basic, quarterstaff
  Expert (u_init.c:548-572).
- Wizard spell schools: Expert in attack/divination/escape/matter;
  Skilled in healing/enchantment/cleric.

### Close calls
- "You feel more confident in your skills" has four variants
  depending on which skill becomes advanceable (weapon.c:78-82):
  "...in your skills" / "weapon skills" / "spell casting skills" /
  "fighting skills". The bare form is the P_NONE/new-slot variant;
  for a melee weapon advance, the player actually sees "weapon
  skills." Left as-is to keep the prose compact.

---

## 2026-05-18 — Chapter audit #182: Spell Tables (appendix)

Source: `spoilers/companion.md` line 7760, 43 spells × 6 columns.
2 corrections + 1 clarification.

### Wrong → fixed
- **magic missile "no resistance"**: actually Antimagic fully blocks
  it. `zap.c:4410-4419` (`case ZT_MAGIC_MISSILE: if (Antimagic) ...
  "The missiles bounce off!"`). Reworded the row to "2d6 force ray;
  Antimagic blocks it."
- **clairvoyance upgrade shown as "—"**: it actually has a Skilled
  upgrade. `spell.c:1572-1576` sets `pseudo->blessed = 1` when
  `role_skill >= P_SKILLED`, which adds nearby-monster detection to
  each vicinity-map pulse. Added "Skilled: also detects nearby
  monsters during each pulse."

### Clarified
- **finger of death "MR resists"**: applies only to monsters
  (`resist_death_ray`). Against the player it's an instakill with
  no Antimagic check (`zap.c:2885-2902`) — only nonliving or demon
  forms are immune. Added the player-side caveat to the row.

### Verified
- All 43 spells map exactly to objects.h SPELL() macros at
  objects.h:1293-1421. School counts: 7 attack, 6 healing, 8
  divination, 5 enchantment, 5 cleric, 5 escape, 7 matter.
- Pw cost = 5 × spell level (SPELL_LEV_PW at spell.h:36).
- Rank-gated upgrades all match spell.c:1419-1587:
  - fireball / cone of cold aimed-explosion at Skilled.
  - remove curse / confuse monster / detect food / cause fear /
    identify / charm monster all behave as blessed-scroll at
    Skilled.
  - haste self / detect treasure / detect monsters / levitation /
    restore ability all behave as blessed-potion at Skilled.
  - protection doubles `uspmtime` at Expert (spell.c:1169).
  - jumping range scales with `role_skill` (spell.c:1585).

### Close calls
- Chain lightning is L2 in the table here, and the body uses are
  correct (Key Spells table at 5159 shows L2; What's New at 9107
  says "new level 2 attack spell"). The historical mismatch noted
  in audit #99 is resolved.
- jumping is dir=IMMEDIATE in objects.h but uses cursor-pick rather
  than a direction key. Table labels it "untargeted" — a UX
  classification, not the C oc_dir field. Left as-is.

---

## 2026-05-18 — Chapter audit #183: Skill Caps (appendix) — re-audit

Source: `spoilers/companion.md` line 7834. No corrections.

### Verified
Re-checked every cell of all three sub-tables against
`u_init.c:257-572` (Skill_A through Skill_W):
- 27 weapon-skill rows × 13 role columns.
- 4 fighting-style rows × 13 role columns.
- 7 spell-school rows × 13 role columns.
Every entry, including every "—" (restricted = not in role's
`Skill_*[]` array), is correct.

### Notes
- The audit prompt's spec was off on two points; the companion
  is right:
  - Samurai short sword is `P_EXPERT` (u_init.c:470), not Basic.
  - Valkyrie two-weapon and riding are both `P_SKILLED`
    (u_init.c:543-544), not Expert.
- Scimitar correctly excluded from every role's array — merged
  into saber in 5.0 (no `P_SCIMITAR` in any `Skill_*[]`).
- The original audit #100 already verified everything; this
  re-audit confirms no drift.

---

## 2026-05-18 — v2 pilot batch — kickoff

Pass 2 of the chapter-by-chapter audit started today, with three
criteria instead of the prior pass's single criterion:

1. **Accuracy** against NetHack 5.0 C source (same as pass 1, focused
   on what was missed).
2. **Wisdom of advice**, cross-checked against community lore (wiki /
   alt.org / data.base) when the claim goes beyond pure mechanics.
3. **Voice**: friendly and humorous when fluent, but tighter on
   punctuation. New rule: prefer periods > commas > colons > semicolons
   > parentheticals > em-dashes when there is a fluent option. The
   prior AUDIT.md rule "em-dashes for parentheticals" is superseded.

Pass 2 queue: `companion-audit-queue-2.md` (seed
`companion-audit-2026-05-18-pass2`, 183 reshuffled units).

The pilot batch (#1-#5 in the new queue) is below.

---

## 2026-05-18 — v2 audit #1: Sokoban Solutions — Level 3, Version A

Source: `spoilers/companion.md` line 6373. No corrections (badge
backfill only).

### Verified
- 13-boulder layout and all 13 solution steps verified geometrically
  against `dat/soko2-1.lua:9-62` (spoiler coords = lua + 1).
- Boulder positions A-M, rolling-boulder trap (8,10), 10 hole traps
  row 10 cols 9-18, upstair (17,5), downstair (7,11), locked door
  (19,9) all match.
- Final "three boulders remain" tally checks.

### Notes
- This section had no pass-1 audit badge while its neighbors (Levels
  2A, 2B, 3B) did. Added a fresh pass-2 badge to close the gap.
- Step 1 ("Push M left one square") looks counterintuitive but is
  the only way to reach the west side of M via the row 11 detour.
  Spoiler doesn't explain this, which is consistent with the rest
  of the section's terse style. Left as-is.

---

## 2026-05-18 — v2 audit #2: Voluntary Challenges — The Food Conducts

Source: `spoilers/companion.md` line 6707. 3 factual corrections,
3 wisdom additions, 4 voice tightenings.

### Wrong → fixed
- **"Permissible corpses (... gray ooze / brown pudding / green
  slime — all puddings except black — and most others)"**: puddings
  are G_NOCORPSE per `monsters.h:2081-2113`. They drop **globs**, not
  corpses. Green slime corpse doesn't exist either; eating its glob
  slimes you. Reworded to "permissible corpses and globs" with the
  pudding rows treated as globs, and added a note about green slime.
- **"They share an internal 'egg-derived' material flag in the C
  source."**: fabricated. The vegan-violating comestibles are a
  hardcoded otyp list at `eat.c:3016-3018`, no such flag exists.
  Replaced with the in-world reason: "They contain eggs."
- **"And all ghosts."** in the vegan corpse list: S_GHOST is
  G_NOCORPSE per `monsters.h:2888,2897`. Dead weight. Dropped.

### Verified
- Vegan / vegetarian macros at `mondata.h:232-241` unchanged: vegan
  is `S_BLOB|S_JELLY|S_FUNGUS|S_VORTEX|S_LIGHT|S_ELEMENTAL` (except
  stalker) `|S_GOLEM` (except flesh/leather) and noncorporeal;
  vegetarian adds `S_PUDDING` (except black pudding).
- Vegan-violating comestibles list (PANCAKE, FORTUNE_COOKIE,
  CREAM_PIE, CANDY_BAR, LUMP_OF_ROYAL_JELLY) at `eat.c:3016-3018`.
- Prayer cures hunger from HUNGRY threshold at `pray.c:275`
  (TROUBLE_HUNGRY). `init_uhunger()` at `eat.c:126` touches no
  conduct.
- Wall/door/boulder chewing breaks foodless at `hack.c:722`.
- Polymorph itself does not increment `u.uconduct.food` (no such
  increment in polyself.c).

### Wisdom additions
- Vegetarian-safe ≠ safe: added warning that yellow mold corpses
  poison, violet fungus paralyzes, and acid blobs sting going down.
- Added Monk note: Monks already pay an alignment penalty for meat,
  so the vegetarian conduct is mostly free for them.
- Foodless route: added "wishing for the ring is the usual plan if
  a wand of wishing or magic lamp turns up."

### Voice tightenings
- Dropped `S_PUDDING` C-identifier from prose.
- Dropped filler sentence "Among the hardest conducts in the game."
- Trimmed slow-digestion ring parenthetical from a wordy "the ring
  itself still costs a tiny amount, but it's effectively a free pass"
  to "slows hunger almost to a halt."
- Dropped the orphan "Polymorphing breaks the polyself conduct, not
  foodless" clarification — no source of confusion in the surrounding
  text.

### Close calls
- Verified V2.1 "dairy" hypothesis against `mondata.h` (no comment),
  `dat/data.base:570-576` (describes puddings as amoeboid slimes,
  no dairy reference), and `doc/fixes5-0-0.txt` (no relevant entry).
  The "in-world reason" for puddings breaking vegan is **not** lore-
  supported, so the spoiler now states the rule without a fabricated
  reason: "Vegan also excludes puddings."

---

## 2026-05-18 — v2 audit #3: Bestiary Tables — Quadrupeds `q`

Source: `spoilers/companion.md` line 8241. No factual corrections,
one voice tightening.

### Verified
All 56 cells across 7 rows verified against `include/monsters.h:831-885`:
rothe, mumak, leocrotta, wumpus, titanothere, baluchitherium,
mastodon. Every Lvl, Spd, AC, MR%, color, and attack mode/dice/side-
effect matches. All attacks are AD_PHYS; no side-effect notes needed.

### Voice tightenings
- Mumakil lead-in tightened from "slow but extremely sturdy" to
  "slow but hit for 4d12 and shrug off blows." Cross-references the
  damage figure already given at L1779 ("solo two-attack bruisers").

### Notes
- M1_THICK_HIDE on mumak/titanothere/baluchitherium/mastodon is not
  tagged in the Notes column. Consistent with the spoiler's pattern
  of not surfacing "thick-hide" anywhere else.
- Rothe G_SGROUP (pack) is mentioned in the prose lead-ins at L1679
  and L1777-1778 rather than in the table. Consistent.

---

## 2026-05-18 — v2 audit #4: Armor Tables (appendix)

Source: `spoilers/companion.md` line 7597. 3 factual corrections,
2 wisdom adjustments, 4 voice tightenings.

### Wrong → fixed
- **Levitation boots note** ("can't be removed while floating, so
  you're stuck above pickup..."): `Boots_off()` at `do_wear.c:300-310`
  handles in-air removal and calls `float_down()`. The actual trap
  is the 9/10 curse, not floating itself. Reworded to "Levitation.
  Generated cursed 9 times in 10. Cursed boots can't be taken off,
  so this is a trap item."
- **Blue dragon scale mail / scales** "intrinsic speed (Fast)":
  blue dragon armor grants extrinsic Fast via `EFast`
  (`do_wear.c:817-828`), putting you in `Very_fast` — the same
  speed-boots tier, not the slower intrinsic-Fast tier. Reworded
  to "Shock resistance + speed, same tier as speed boots."
- **Speed boots** "+1 speed": opaque shorthand that wrongly suggests
  parity with intrinsic Fast. Replaced with the actual mechanic:
  "Very fast. Free extra action on 2/3 of turns."

### Verified
- 100% spot-check of every AC/MC/Wt/Cost/Material cell against
  `include/objects.h:445-727` (HELM / CLOAK / SHIELD / GLOVES /
  BOOTS / ARMOR / DRGN_ARMR macros). All numbers match.
- 9/10-cursed-on-generation armors at `mkobj.c:1086-1090` are
  FUMBLE_BOOTS, LEVITATION_BOOTS, HELM_OF_OPPOSITE_ALIGNMENT,
  GAUNTLETS_OF_FUMBLING — flagged correctly in each row.
- Dunce cap auto-curses on wear at `do_wear.c:475-491`.
- Helm of brilliance / gauntlets of dexterity linear-in-spe via
  `adj_abon` (`do_wear.c:3319-3336`).
- Cornuthaum CHA effect and CLAIRVOYANT block for non-Wizards at
  `do_wear.c:454-461`, `worn.c:40-44`.
- Mummy wrapping blocks INVIS while worn at `worn.c:38-39`.
- Mithril is metallic (`objclass.h:194-196`), so spell casting
  penalty applies (`spell.c:2191-2193`).
- All ten dragon-scale-mail dual-property effects match
  `do_wear.c:806-883`.
- 5.0 additions (helm of caution, shield of drain resistance, shield
  of shock resistance) present and correct per
  `doc/fixes5-0-0.txt:2694, 2927`.
- Shimmering DSM/scales correctly absent (deferred in C via `#if 0`).

### Wisdom adjustments
- Chain mail note "Dwarves drop these" dropped — all iron mails are
  Mines dwarf drops, so singling out chain mail misleads.
- Robe note "+1 spellcasting effectiveness" replaced with the actual
  mechanic: "Casting bonus. Cancels most of the metal-armor penalty."
  The `spell.c:2192-2195` subtraction of `spelarmr` is a much larger
  shift than "+1."

### Voice tightenings
- Intro "alongside any tactical caveats" → "and tactical caveats"
  (meta-language about document structure).
- Cloak of magic resistance: "Magic resistance. Lightest source of
  magic resistance." de-duplicated to "Magic resistance. The lightest
  source."
- Dunce cap note trimmed: "Auto-curses itself when worn (regardless
  of starting BUC), so you can't un-wear it without remove curse." →
  "Auto-curses on wear. Needs remove curse to take off."
- Helm of opposite alignment trimmed: "Generated cursed 9 times in
  10 — and cursed means you can't take it off." → "Generated cursed
  9 times in 10. Trap item."

### Notes / follow-ups
- `spoilers/build_armor_appendix.py` appears to be out of sync with
  the committed table (hand-edits added the second hidden property
  to every dragon scale mail row). Consider syncing the generator's
  NOTES dict or marking it manually maintained.
- "yellow dragon scale mail | Rare." annotation may not reflect 5.0
  generation rules. Not chased in this audit.

---

## 2026-05-18 — v2 audit #5: Branches and Landmarks — The Quest

Source: `spoilers/companion.md` line 984. 3 factual corrections
(the auditor proposed a 4th — DL 11-17 — that was applied and then
reverted; see Close calls below), 3 wisdom additions, 4 voice
tightenings.

### Wrong → fixed
- **"Only the Tourist's Platinum Yendorian Express Card gives magic
  resistance just by being carried"**: three carried-MR quest
  artifacts exist. Orb of Detection at `artilist.h:221` has
  `CARY(AD_MAGM)`; Magic Mirror of Merlin at `artilist.h:257` has
  `CARY(AD_MAGM)`; PYEC at `artilist.h:293` has `CARY(AD_MAGM)`.
  Reworded.
- **"A few others (Sceptre of Might, Eye of the Aethiopica) block
  magic attacks only when wielded or worn"**: three not two —
  `DFNS(AD_MAGM)` at `artilist.h:233` (Sceptre of Might),
  `artilist.h:261` (Eyes of the Overworld — Monk), and
  `artilist.h:304` (Eye of the Aethiopica). Reworded.
- **"The nemesis drops two things, on the floor."**: misleading.
  Only the Bell of Opening drops from the nemesis's inventory on
  kill (placed at spawn via `src/makemon.c:1378-1379` —
  `MS_NEMESIS` gets BELL_OF_OPENING). The quest artifact is placed
  on the floor under the nemesis at level generation (e.g.
  `dat/Val-goal.lua:49,76` puts both the Orb of Fate and Lord
  Surtur at (17,8); `dat/Wiz-goal.lua:73,96` same for Eye and Dark
  One). Reworded.

### Verified
- Prerequisite XL 14 (fixed for all roles) at `include/quest.h:45`
  (`MIN_QUEST_LEVEL 14`).
- Minimum alignment record 20 to start at `include/quest.h:43`
  (`MIN_QUEST_ALIGN 20`); enforcement at `src/quest.c:164-176`.
- Magic-portal trap delivers you to qstart at `src/quest.c:91-103,
  188-216`.
- Leader appears on the first Quest level (qstart). E.g., Valkyrie's
  Norn at `dat/Val-strt.lua:63`.
- Role/artifact/nemesis pairings confirmed in
  `include/artilist.h:225-307` and `src/role.c:252,334,431,471,
  511,551`.

### Wisdom additions
- Most quest nemeses carry an amulet of life saving; added "expect
  to kill them twice."
- Added note that the portal back is on the first Quest level only,
  so descending underprepared can mean a long climb home.

### Voice tightenings
- Three short sentences on portal entry trimmed to two; "But you
  can't enter it immediately" filler dropped.
- "Milestone that marks the transition from 'surviving' to
  'preparing for the endgame'" replaced with "major power spike.
  The late game starts here."
- "The nemesis drops two things, on the floor." bold sentence
  rewritten as "Two prizes wait on the nemesis's square."
- Em-dash parenthetical "(from attacking peacefuls, for instance)"
  replaced with periods per the punctuation-ladder rule.

### Close calls
- **Reverted in-flight: "DL 11-16" → "DL 11-17" → "DL 11-16".**
  The sub-agent's reading of `level_range()` (`src/dungeon.c:380-411`)
  was off by one. The function returns a *count*: with `randc = 2`
  the picked level is `base..base+1`, not `base..base+2`. For the
  Quest portal that gives max `6 + 9 + 1 = 16`, not 17. The wiki
  (consulted via WebSearch after the initial commit) showed 11-16
  and prompted the closer reread. The companion text was reverted
  to "11 through 16" within the same session; the badge notes the
  transient mis-edit. Lesson for the autonomous phase: when C math
  involves arithmetic on a count vs. a range, cross-check against
  the wiki via WebSearch before committing.
- Wiki direct fetch (WebFetch on `nethackwiki.com`) is blocked by
  Cloudflare. WebSearch returns Google-summarized wiki content and
  is the working workaround. alt.org game logs are accessible by
  WebFetch directly.
- Some roles quest much earlier than the XL-14 minimum suggests
  (Valkyrie, Samurai), while others quest much later (Healer,
  Tourist). Section makes no per-role timing claim, so the
  softening is consistent.

---

## 2026-05-18 — v2 audit #6: Sokoban Solutions — Level 2, Version A

Source: `spoilers/companion.md` line 6248. No corrections (re-audit).

### Verified
- Map walls and floor match `dat/soko3-1.lua:10-21` exactly (lua col,row → spoiler col+1,row+1).
- All 20 boulders A-T mapped to lua placements at `soko3-1.lua:31-53`.
- Upstair `<` at (24,5), locked door `+` at (28,10), player arrival `@` at (12,3), rolling-boulder trap at (12,11), 15 holes at (13,11)-(27,11): all match `soko3-1.lua:23-25, 58-73`.
- Steps 1-3 confirmed by the pass-1 audit. v2 extended through steps 4-9.
- "Push F up to (3,4)" in step 8 is not gratuitous: F at (3,7) seals the only N-S corridor through (3,6), so the only way to access the upper chamber for finishing F and A is to push F upward through the opening, simultaneously moving the player up.
- Final tally "Five boulders (B, C, D, I, and Q) remain" exact: 20 boulders minus 15 holes filled.

### Notes
- The pass-1 audit explicitly stated it had only walked steps 1-3. v2 re-audit fills the gap with no corrections found.

---

## 2026-05-18 — v2 audit #7: Weapons Tables — Broadsword

Source: `spoilers/companion.md` line 7302. 2 artifact additions, 1 voice replacement.

### Wrong → fixed
- **Broadsword row Notes**: previously "+d4 small, +1 large" — formula notation that duplicated the Damage column. No mention of **Dragonbane** (BROADSWORD artifact at `artilist.h:157-160`, SPFX_REFLECT, +d5 vs S_DRAGON). Replaced with "Dragonbane is the artifact form. +d5 vs dragons, grants reflection."
- **Elven broadsword row Notes**: previously empty. No mention of **Orcrist** (ELVEN_BROADSWORD artifact at `artilist.h:134-136`, A_CHAOTIC, warns of orcs, +d5 damage). Added "Orcrist is the chaotic artifact form. Warns of orcs, +d5 damage."
- **Runesword row Notes**: previously "Stormbringer is the chaotic-aligned artifact form." Expanded slightly: "Stormbringer is the chaotic artifact form. Drains life on hit." Parallel to peer rows that list the artifact's effect.

### Verified
- Broadsword stats 1d4+1d4 / 1d6+1, wt 70, cost 10, iron, P_BROAD_SWORD at `include/objects.h:262-265`; +d4/+1 bonus applied at `src/weapon.c:235,285`.
- Elven broadsword stats 1d6+1d4 / 1d6+1, wt 70, cost 10, wood, prob 4 at `include/objects.h:266-269`.
- Runesword stats 1d4+1d4 / 1d6+1, wt 40, cost 300, iron, color CLR_BLACK, prob 0 (not randomly generated) at `include/objects.h:287-290`. Stormbringer A_CHAOTIC at `artilist.h:93-96`.

### Notes
- Strike type for all three (slash via `S` flag at `objects.h:137`) was verified — spoiler doesn't claim a strike type, no issue.

---

## 2026-05-18 — v2 audit #8: Bestiary Tables — Vampires `V`

Source: `spoilers/companion.md` line 8804. 2 factual corrections, 1 voice tightening.

### Wrong → fixed
- **"All vampires fly, regenerate, have poisonous corpses, are undead..."**: all three V-class monsters carry `G_NOCORPSE` (`include/monsters.h:2282, 2292, 2314`; `include/monflag.h:201`), so they never leave any corpse. "Poisonous corpses" is nonsense. Dropped.
- **"Shapeshifts to bat or cloud."**: incomplete. Base `PM_VAMPIRE` shifts to fog cloud or vampire bat per `src/mon.c:4956-4967`; `PM_VAMPIRE_LEADER` and Vlad (`PM_VLAD_THE_IMPALER`) can additionally become a wolf. Reworded: "Shapeshifts to bat or fog cloud. Lords and Vlad can also become wolves."

### Verified
- vampire row Lvl 10, Spd 12, AC 1, MR 25, claw 1d6 + bite 1d6 drain-XL at `include/monsters.h:2281-2290`.
- vampire lord row Lvl 12, Spd 14, AC 0, MR 50, claw 1d8 + bite 1d8 drain-XL at `include/monsters.h:2291-2300`.
- Vlad the Impaler Lvl 28, Spd 26, AC -6, MR 80, weapon 2d10 + bite 1d12 drain-XL at `include/monsters.h:2313-2322`. G_UNIQ; `M3_WANTSCAND` → CANDELABRUM_OF_INVOCATION at `src/wizard.c:149-150`.
- Vampire mage correctly omitted (`#if 0 DEFERRED` at `monsters.h:2301-2312`).
- Vlad's Tower location verified at `dat/dungeon.lua:98, 262` and `dat/tower1.lua:6, 29`.

### Voice
- Lead-in "Vlad the Impaler is the vampire boss in his Tower." reworded to "Vlad the Impaler is the boss of Vlad's Tower." — uses the proper noun, avoids the "vampire" repetition from the prior sentence.

---

## 2026-05-18 — v2 audit #9: Spellcasting

Source: `spoilers/companion.md` line 5077. 3 factual corrections, 1 wisdom softening, 2 voice tightenings.

### Wrong → fixed
- **"Each **successful** read counts toward a fixed total (about five)"**: `MAX_SPELL_STUDY = 3` with the `> MAX_SPELL_STUDY` check at `spell.c:401` caps at **4** successful reads, not "about five." The comment at `spell.c:400` explicitly says "a normal book can be read and re-read a total of 4 times." Reworded to "a fixed total of four."
- **Charm monster row "Tame nearby creatures (3×3, 5×5 confused)"**: two issues. (1) Confused casting fails outright at `spell.c:1372`, so a "confused area" is unreachable. (2) The scroll-of-taming confused area is 11×11 (`bd = confused ? 5 : 1`, `-bd..bd` inclusive at `read.c:1689,1695`), not 5×5. Reworded to "Tame nearby creatures in a 3×3 area; Skilled+ acts like a blessed scroll."
- **"Power regenerates over time (faster with higher Wisdom and with a regeneration source)"**: incomplete. Regen amount is `(Wis + Int)/15 + 1` at `allmain.c:607` — Intelligence matters too — and Wizards tick on factor 3 vs the standard 4 at `allmain.c:605`. Reworded.

### Wisdom
- **"A Valkyrie might manage identify (level 3) but will struggle with anything above level 4."**: Valkyries have *divination restricted* (no entry in `Skill_V` at `u_init.c:525-546`), so even identify is occasional-at-best for them. Softened to "A Valkyrie can occasionally read identify (level 3) if her Intelligence is boosted by gain-ability potions, but non-spellcasters are usually better off with scrolls."

### Voice
- Full-paragraph parenthetical "(The 'Minimum Int + XL' column means...)" promoted to plain prose.
- "Each failure also has a 1-in-3 chance of destroying the book on the spot." was duplicated (once in the Learning Spells paragraph, once in the spellbook-fade paragraph). Consolidated to the fade paragraph.

### Close calls / notes
- Read-success table "Min Int + XL" is approximate. Int 18 + XL 14 = 32 gives a level-6 read score of ~17, an 85% chance — not "always." Acceptable rule-of-thumb but the word "reliably" is loose; not changed.
- "1-in-3 destruction on failed read" wording could be tightened further but the current phrasing is clear enough.

---

## 2026-05-18 — v2 audit #10: Weapons Tables — Long sword

Source: `spoilers/companion.md` line 7315. 1 factual completion, 1 voice tightening.

### Wrong → fixed
- **"Artifact forms: Excalibur, Vorpal Blade, Frost Brand, Fire Brand."**: incomplete. `include/artilist.h` defines six LONG_SWORD artifacts: Excalibur (l.85), Frost Brand (l.149), Fire Brand (l.153), Giantslayer (l.174), Vorpal Blade (l.191), Sunsword (l.209). Added Giantslayer and Sunsword.

### Verified
- long sword stats 1d8/1d12, wt 40, cost 15, iron, P_LONG_SWORD at `include/objects.h:270-272`.
- katana stats 1d10/1d12, wt 40, cost 80, +1 to-hit, iron, P_LONG_SWORD at `include/objects.h:278-280`.
- Excalibur dipping: `obj->otyp == LONG_SWORD`, `u.ulevel >= 5`, single non-artifact sword, Excalibur not already extant; rolls `!rn2(Role_if(PM_KNIGHT) ? 6 : 30)`; Lawful gets blessed Excalibur, non-Lawful gets curse plus rustproof strip at `src/fountain.c:404-440`.
- Snickersnee is a KATANA artifact at `include/artilist.h:203-205`, A_LAWFUL, Samurai-only.
- Demonbane is now SILVER_MACE (not a long sword) at `include/artilist.h:162-164`. Correctly absent from the list.

### Voice
- Excalibur dipping line reworked from a semicolon-and-parenthetical chain ("rolls 1-in-30 (1-in-6 for Knights); Lawfuls who roll get Excalibur, others get the sword cursed") into four periods per the punctuation ladder.

### Notes
- Non-Lawfuls on a successful roll also lose rustproofing and possibly an enchantment point, not just a curse. "Cursed" is shorthand. Not expanded — keeping the table cell concise.
- The pass-1 audit badge text says "ANY alignment rolls 1-in-30 at XL 5+" — slightly sloppy since Knights are 1-in-6 regardless. Cosmetic only; left.

---

## 2026-05-18 — v2 audit #11: Branches and Landmarks — The Gnomish Mines

Source: `spoilers/companion.md` line 876. **All v2 edits reverted same session — see Reverted below.** Net effect: 0 corrections.

### Verified
- Mines branch DL 2-4 at `dat/dungeon.lua:14-19`.
- Seven Minetown variants at `dat/dungeon.lua:178-185`, including the Orcish Town variant at `dat/minetn-1.lua` with no shops, no priest, iron bars, unaligned shrine.
- All three Mine's End variants seed a not-cursed achievement-flagged luckstone at `dat/minend-{1,2,3}.lua`.
- Fake-luckstone mimic placement at `dat/minend-1.lua:59` (plus mimics for loadstone, flint, touchstone, and a real loadstone).
- Race-peaceful gnomes/dwarves for gnomish PCs via `src/role.c:654` lovemask.
- `dat/minefill.lua:36-44` places 6-8 gnomes plus exactly one guaranteed gnome lord, two dwarves, two random gnome-class slots, and a 50/50 humanoid slot that can rarely roll a mind flayer.

### Reverted (do not re-apply)
- An attempt to add a mind-flayer warning to the prose used the community jargon term ("minesflayer") and turned the intro into a stat dump. User reaction: *"old introduction was much better"*, *"too much inside baseball and a madeup word 'minesflayer'"*, *"please do not make the text worse!"* The prose was restored verbatim to the pre-v2 wording. **Lesson:** voice fixes should preserve existing rhythm; never introduce community jargon. The Brainlessness section in Part Three already covers mind flayers; the Mines section doesn't need to reiterate.
- Six "voice tightenings" that sub-agent flagged ("modest but steady stream", "Usually it's a small settlement", "the clean answer", "wherever you arrive", parenthetical-on-mimic promotion, "you've found a safe place to identify items by dropping them on it" → "BUC-tests"): all reverted. The original phrasing has rhythm and flavor that the auditor's terser proposals lack.

### Close calls / notes
- Mine's End depth (DL ~10-13) is not stated in the section; left as-is.

---

## 2026-05-18 — v2 audit #12: Weapons Tables — Mace

Source: `spoilers/companion.md` line 7386. 2 factual corrections.

### Wrong → fixed
- **Demonbane row "+d5/+0 silver mace"**: `PHYS(5, 0)` doesn't mean "+5 to-hit, +0 damage." `damn=5` provides `rnd(5)` to-hit via `spec_abon` (`src/artifact.c:1083-1085`), and `damd=0` returns `max(tmp, 1)` in `spec_dbon` (`src/artifact.c:1106-1107`) — which doubles base damage versus demons. Demonbane also has a banish invoke. Reworded to "+1d5 to-hit and double damage versus demons, plus a banish invoke."
- **Silver mace row "Bonus damage to demons, undead, and shape-changers"**: the silver +1d20 bonus at `src/uhitm.c:1376-1377` fires only on `hates_silver` targets — demons, weres, vampires, shades, and most imps (`src/mondata.c:524-528`). "Undead" is too broad (mummies, zombies, ghosts, liches don't qualify); "shape-changers" is too broad (chameleons don't). Magnitude (+1d20) was unstated. Reworded.

### Verified
- mace stats 1d6+1 / 1d6, wt 30, cost 5, iron at `include/objects.h:355-358`.
- silver mace stats 1d6+1 / 1d6, wt 36, cost 60, silver at `include/objects.h:359-361`.
- Demonbane SILVER_MACE, A_LAWFUL, `role=PM_PRIEST`, banish invoke at `include/artilist.h:162-164`.
- Sceptre of Might is also a MACE artifact at `include/artilist.h:232-235`. Added to the row notes.
- Mjollnir is a WAR_HAMMER (correctly excluded from this section).
- Role caps for P_MACE: Caveman / Priest Expert; Archeologist / Knight / Samurai Skilled; Healer / Tourist / Valkyrie Basic; Wizard not listed.

### Notes
- The section was missing an audit badge before this pass. Added one.

---

## 2026-05-18 — v2 audit #13: Enhancing Skills

Source: `spoilers/companion.md` line 4810. 3 factual corrections, 2 wisdom adjustments, 5 voice tightenings.

### Wrong → fixed
- **"Non-weapon skills — spell schools, two-weapon, riding, bare hands, martial arts — cost roughly half as many slots as melee weapons"**: two-weapon is treated as a weapon for slot cost per `src/weapon.c:1141` (`if (skill <= P_LAST_WEAPON || skill == P_TWO_WEAPON_COMBAT)`). The spoiler was repeating pre-3.7 lore. Reworded to drop two-weapon from the non-weapon list, with a parenthetical noting "two-weapon uses the weapon column despite the name."
- **"A Valkyrie aiming for Expert long sword, Expert two-weapon, and Skilled riding is eleven slots deep"**: with correct two-weapon costs that's 6 + 6 + 2 = **fourteen**, not eleven. The 11 figure assumed two-weapon at non-weapon cost (4) and Basic riding (1). Reworded.
- **"Bare hands and martial arts bonuses still only apply to 50% and 75% of hits respectively"**: conflates *training rate* with *bonus application*. The bonuses apply on **every** hit per `src/weapon.c:1611-1613`; the 50%/75% is the chance a hit *also trains the skill counter*. The earlier paragraph already says this correctly ("The rank still applies on every hit"); this later contradiction was dropped.

### Verified
- Skill tiers and the `level²×20` cumulative practice (20/80/180/320/500) match `include/skills.h:90-106`.
- Weapon slot costs 1/2/3 and unarmed/martial 1/1/2/2/3 at `src/weapon.c:1130-1152`.
- 2 starting slots, +1 per XL, +1 from crowning, ceiling 32 at `src/u_init.c:884`, `src/attrib.c:1068-1073`, `src/pray.c:992-994`.
- Skill-bonus tables for weapon (−4/−2 … +3/+2) and two-weapon (−9/−3 … −3/+1) match `src/weapon.c:1559-1600`.
- Riding -2/-1/0/0 to-hit and +1/+2 damage at Skilled/Expert at `src/weapon.c:1617-1633, 1712-1725`.
- Practice award gate `train_weapon_skill = (hmd->dmg > 1)` at `src/uhitm.c:849, 946`.
- Riding-skill training every 100 successful moves at `src/steed.c:393`.
- Pre-credit of 20 practice at starting Basic at `src/weapon.c:1801`.

### Wisdom adjustments
- "Knights should advance it on the first opportunity even though Basic still leaves a −1 to-hit penalty in the saddle" was based on a wrong premise (Knights start at Basic riding per `src/weapon.c:1787-1789`; first opportunity is to push to Skilled). Reworded.
- "Cone of cold and fireball stop being beams and become room-clearing **explosions**" oversells the footprint — at Skilled the cast becomes a cluster of 2-9 sequential 3×3 explosions clustered near a target square. Reworded to "a cluster of 3×3 explosions you can place at range" in both mentions.

### Voice tightenings (kept)
- "restricted from long swords entirely. Restricted skills don't appear on the `#enhance` menu and can never leave Unskilled" → "restricted from long swords. Restricted skills don't appear on `#enhance` and stay Unskilled." (Minor trim, no flavor lost.)
- "shouldn't expect anything past level 3" clarified as "spell-level 3" (was ambiguous between game-level and spell-level).
- Em-dashes in the two-weapon penalty sentence replaced with periods (punctuation ladder).

### Reverted (do not re-apply)
- "the dungeon's quiet subsidy for magic" was dropped on grounds of "invented in-world reason." Restored. It's a metaphor / editorial gloss, not a factual claim. Voice features like this should stay.
- "the difference between landing the killing blow and watching the monster shrug" was replaced with "+3 to hit, +2 damage. That's why dedicating to a single weapon matters." Restored. The vivid framing was earning its keep, and the auditor's bare-numbers proposal lost the voice without gaining clarity.
- "Specialization by decree." was dropped as "meta." Restored. Light editorial flourishes at the end of bullet points are part of the book's register.

---

## 2026-05-18 — v2 audit #14: Branches and Landmarks — Fort Ludios

Source: `spoilers/companion.md` line 1055. 4 factual corrections, 2 wisdom adjustments, 3 voice tightenings.

### Wrong → fixed
- **"roughly twenty soldiers and a lieutenant"**: `dat/knox.lua:126-142` hard-codes exactly sixteen soldiers and one lieutenant. Reinforcements migrate in via the barracks zoo, so "roughly twenty" is defensible for the live count after a few turns, but the static garrison is sixteen plus one. Reworded.
- **"a magic portal somewhere around Dlvl 18-22"**: off in two ways. (a) `dat/dungeon.lua:34-38` defines base 18 range 4, so the dungeon.lua hint is DL 18-21 not 18-22. (b) The actual placement code at `src/mklev.c:2647-2651` only requires depth > 10 and above Medusa, so the portal can land as shallow as DL 11. Wiki confirms. Reworded.
- **"often inside a small vault that requires digging to reach"**: the portal is *always* inside a vault per `src/mklev.c:1331, 2624-2658`. Reworded.
- **"the only way out is back through the portal or through the walls"**: the level is flagged non-diggable at `dat/knox.lua:35`, so wall-escape doesn't work. `noteleport` only blocks intra-level teleport, so level-teleport (scroll, wand, trap) still works. Reworded.

### Verified
- Treasury gold: 60 squares at 600-900 zorkmids each, 36000-54000 total at `dat/knox.lua:57-70`.
- Trap ratio: roughly one in three tiles trapped, mix of land mines and spiked pits at `dat/knox.lua:59-65`.
- Corner gem caches (diamonds, emeralds, rubies, amethysts) at `dat/knox.lua:155-167`.
- Four giant eels in the moat, four dragons, stone giant, one lieutenant at `dat/knox.lua:142-154`.
- Alarm quiets once Croesus dies at `src/do.c:1894-1903`.
- Croesus G_UNIQ | G_NOGEN, MS_GUARD, hostile, level 20 at `include/monsters.h:2859-2869`.

### Wisdom adjustments
- "plan to engage him rather than tip-toe around" inverted by community advice: Croesus is covetous and dangerous in melee. Reworded to "shoot or zap him from across the moat."
- "money for protection rackets or shop purchases" softened — at DL 11-21, protection has gotten very expensive, so Ludios gold is more often spent on identification scrolls or shop stock.

### Voice tightenings
- "the unique fortress warden and vault guardian" → "Croesus on the throne, the vault guardian himself" (dropped meta "unique").
- "(a 15×4 treasury holds 36k-54k pieces, though most of the tiles are spiked-pit or land-mine trapped)" promoted to plain prose, with the trapped fraction corrected from "most" to "roughly a third."
- "decent weapons" → "serviceable weapons."

---

## 2026-05-18 — v2 audit #15: The Apothecary

Source: `spoilers/companion.md` line 3331. 1 factual fix; voice changes mostly reverted (see below).

### Wrong → fixed
- **"One blessed quaff and you're permanently faster for the rest of the game"**: the intrinsic-Fast grant requires only `!otmp->cursed` per `src/potion.c:1066` — an **uncursed** potion of speed also grants permanent intrinsic speed. Blessing only extends the temporary timer that overlays the intrinsic grant. Reworded inline as a semicolon clause on the same sentence.

### Verified
- Price table at L3346-3354 matches every entry in `include/objects.h:1125-1177` (healing 20; booze/fruit juice/see invisible/sickness 50; etc.).
- Water has fixed "clear" appearance per `include/objects.h:1175-1177`.
- Holy water altar-prayer mechanic at `src/pray.c:1386-1412`.
- Gain ability blessed-raises-all vs uncursed-raises-one at `src/potion.c:1029-1048`.
- Extra healing always cures blindness (`cureblind=TRUE`) and non-cursed cures sickness at `src/potion.c:1131-1133`.
- Maxhp boost on non-cursed extra (2/5) and full healing (4/8) at `src/potion.c:1132, 1147`.
- Wand of speed monster self-zap grants 50-74 turns of timed speed only at `src/zap.c:2845-2848` (`speed_up(rn1(25, 50))`).
- All alchemy recipes match `mixtype()` at `src/potion.c:2122-2208`.
- Explosion rate 1/10 base, 1/30 with alchemy smock at `src/potion.c:2421`.
- Cursed dipping target always explodes at `src/potion.c:2419`.
- Diluted-stack cap of 2 per operation at `src/potion.c:2521-2522`.
- Unicorn horn purification mappings at `src/potion.c:2151-2159`.

### Wisdom adjustments
- "never use a cursed potion as a dipping target" reworded to "never let the receiving potion (the one you're dipping into) be cursed" — target/source language can confuse readers.
- "Drop uncursed water on a co-aligned altar" left as the standard play pattern, but the mechanism also blesses cursed water on the altar (water_prayer at `src/pray.c:1395-1402`). Not changed; the standard pattern is what readers should do.
- "Treat every gain energy potion like the catalyst it is" left as written. Note: gain level is just as good a catalyst and slightly more common per `include/objects.h` (prob 20 vs 40), but this is a soft point.

### Reverted (do not re-apply)
- Lead-in colon ("Ruby liquids, milky fluids, smoky concoctions: each one a small gamble..."): restored. The colon does rhythmic work that the period flattened.
- "Water is the oddity in the $100 group: it always appears as 'clear potion'": restored. Same reason.
- Speed paragraph short-sentence rewrite: restored to the original semicolon-joined "trading blows / hitting twice" phrasing. The factual fix on uncursed speed is now folded in as a semicolon clause on the lead sentence.
- "Think of it as artisanal alchemy rather than industrial production." restored. The gag earns its keep.
- "never use a cursed potion as a dipping target" was reworded to "never let the receiving potion (the one you're dipping into) be cursed" on auditor concerns about source/target language. Restored to original wording — clearer and shorter.

### Notes
- Extra healing also cures hallucination per `src/potion.c:1134`. Not claimed, not wrong, just an omission worth flagging if the chapter expands.
- Section makes no mention of sink-dip ID, bag-of-holding scatter on explosion, or Gehennom hot-ground potion shatter — those 5.0 changes are absent here. Not wrong, but the chapter could be enriched in a future pass.

---

## 2026-05-18 — v2 audit #16: Weapons Tables — Short sword

Source: `spoilers/companion.md` line 7283. No corrections (re-audit clean).

### Verified
- short sword 1d6/1d8, wt 30, cost 10, iron at `include/objects.h:244-246`.
- elven short sword 1d8/1d8, wt 30, cost 10, wood at `include/objects.h:247-249`.
- orcish short sword 1d5/1d8 (verified the unusual 1d5 die), wt 30, cost 10, iron at `include/objects.h:250-252`.
- dwarvish short sword 1d7/1d8, wt 30, cost 10, iron at `include/objects.h:253-255`.
- All four share P_SHORT_SWORD.
- Rogue starter at `src/u_init.c:134`. Samurai wakizashi alias at `src/u_init.c:144` + `src/objnam.c:106`.
- No SHORT_SWORD-base artifact exists.

### Notes
- Auditor flagged "The Rogue's starter" as slightly misleading (the dagger stack is the Rogue's defining weapon), but the short sword is in the starting inventory and the framing is fine. Per preserve-voice, left as-is.

---

## 2026-05-18 — v2 audit #17: Dangerous Encounters — Seduction

Source: `spoilers/companion.md` line 2175. 2 factual fixes, 2 wisdom additions.

### Wrong → fixed
- **"Depending on its randomly assigned gender"**: incomplete. `could_seduce` at `mhitu.c:1980` requires opposite-sex `genagr`/`gendef`. A same-sex foocubus never seduces and just claws. Reworded.
- **"Items aren't dropped on floor (just unequipped to inventory)"** was correct from pass 1. v2 verified.

### Verified
- Random gender assignment at `makemon.c:1279`.
- Strip order (cloak/suit/boots/gloves/shield/helm/shirt) at `mhitu.c:2119-2128`.
- Items unequipped to inventory only at `mhitu.c:2351` via `remove_worn_item(obj, TRUE)` at `steal.c:213`.
- Encounter aborts if cloak or suit still worn at `mhitu.c:2139`.
- Cha/20 prompt at `mhitu.c:2325`.
- Cap-32 attribute roll at `mhitu.c:2177-2178` (`rn2(35) > min(attr_tot, 32)`).
- 6-15 HP damage as `rn1(10,6)` at `mhitu.c:2219`.
- XL drain blocked by drain resistance at `mhitu.c:2204`.
- Peaceful demons charge 1/5 at `mhitu.c:2280`. 500+ zm cost at `mhitu.c:2276-2278`.
- Defense via hard-to-remove suit/cloak; free action is irrelevant (not a paralysis attack).

### Wisdom additions
- XL 1 farming warning: at experience level 1, the level-drain outcome is fatal. Added.
- Ring of adornment interactions at `mhitu.c:2019-2110`: succubus pockets a worn ring; incubus slips one from your pack onto your finger. Added a brief note.

### Notes
- "Defers" wording on the asleep/unresponsive case is slightly loose (the demon abandons the attempt without setting `mspec_used`, so it may retry next turn). Left as-is; the practical effect is similar.
- The "5 bad vs 5 good outcomes" framing reads like a 10-way die when it's actually a Cha+Int roll for *side* then `rn2(5)` for *which*. Acceptable simplification.

---

## 2026-05-18 — v2 audit #18: Appendices — Spell Tables

Source: `spoilers/companion.md` line 7779. 4 factual corrections.

### Wrong → fixed
- **flame sphere and freeze sphere rows**: both spells are inside `#if 0 /* DEFERRED */` at `include/objects.h:1413-1422` with no implementation anywhere in 5.0 `src/`. They are SLASH'EM leftovers. Dropped both rows. 41 spells, not 43.
- **charm monster row (triple error)**:
  - Type "aimed" → "untargeted": `seffect_taming` at `read.c:1679-1708` is an area centered on the caster, no direction prompt.
  - Effect "Tames one target" → "Tames monsters in a 3×3 area (11×11 if confused)": the area is `(2·bd+1)²` with `bd = confused ? 5 : 1`, so 3×3 normal and 11×11 confused, not "5×5 confused" — and *all* monsters in the area are tamed, not just one.
  - Upgrade "3×3 normal, 5×5 confused" → "Blessed-scroll behavior": the P_SKILLED upgrade is more reliable taming, not a radius bump.
- **cause fear row**: "Blessed: wider radius" was wrong. `seffect_scare_monster` at `read.c:1454-1486` ignores `sobj->blessed` entirely; blessed and uncursed are identical. The loop also hits *every visible monster* on the level, not just "nearby." Dropped the blessed-upgrade, reworded Effect to "Visible monsters flee."
- **remove curse row**: "Blessed: all worn/wielded" was wrong. `read.c:1514-1577` uncurses every (non-coin) carried item when blessed. Reworded to "all carried items."

### Verified
- Pw cost = 5 × spell level at `include/spell.h:36`.
- Fireball / cone of cold P_SKILLED aimed-explosion at `src/spell.c:1419-1452`.
- Protection P_EXPERT doubles uspmtime at `src/spell.c:1169`.
- Jumping range scales with `role_skill` at `src/spell.c:1584-1586`.
- Clairvoyance P_SKILLED extra monster-detect at `src/spell.c:1572-1576`.
- Restore ability / detect monsters / detect food / detect treasure / haste self / levitation: blessed-potion behavior at P_SKILLED at `src/spell.c:1533-1545`.
- Confuse monster / identify: blessed-scroll at P_SKILLED at `src/spell.c:1517-1525`.

### Notes
- Healing's P_SKILLED upgrade (also cures blindness per `src/spell.c:1480-1485` + `src/zap.c:447-448`) is not flagged in the table; minor inconsistency with how other small upgrades are tagged. Left for follow-up.
- Cross-references: chain lightning's level is correctly 2 in this appendix and in the Spellcasting "Key Spells" table (audited in #9). The audit-1 badge's note about a body-text mismatch is stale.

---

## 2026-05-18 — v2 audit #19: Bestiary Tables — Sea monsters `;`

Source: `spoilers/companion.md` line 9064. 2 factual corrections.

### Wrong → fixed
- **"Lives in water. Wraps around you and drags you under to drown."**: the intro applied wrap-and-drown to all 6 rows, but only giant eel, electric eel, and kraken have `AT_TUCH`/`AT_HUGS` + `AD_WRAP` per `monsters.h:3230-3256`. Jellyfish, piranha, and shark just bite/sting. The drown mechanic is gated on `AD_WRAP` at `src/uhitm.c:3389-3401`. Reworded.
- **"sting 3d3 poison"** (jellyfish row): `AD_DRST` drains strength rather than dealing generic poison damage (`src/uhitm.c:3149, 3157`). Changed to "sting 3d3 drain-Str", matching the spoiler's own drain-stat notation.

### Verified
- jellyfish Lvl 3, Spd 3, AC 6, MR 0, AD_DRST 3d3 + MR_POISON at `monsters.h:3205-3212`.
- piranha Lvl 5, Spd 18, AC 4, MR 0, bite 2d6 × 2, G_SGROUP at `monsters.h:3213-3220`.
- shark Lvl 7, Spd 12, AC 2, MR 0, bite 5d6 at `monsters.h:3221-3229`.
- giant eel Lvl 5, Spd 9, AC -1, MR 0, bite 3d6 + AT_TUCH AD_WRAP at `monsters.h:3230-3238`.
- electric eel Lvl 7, Spd 10, AC -3, MR 0, bite AD_ELEC 4d6 + AT_TUCH AD_WRAP + MR_ELEC at `monsters.h:3239-3247`.
- kraken Lvl 20, Spd 3, AC 6, MR 0, claw 2d4 × 2 + AT_HUGS AD_WRAP 2d6 + bite 5d4 at `monsters.h:3248-3256`.
- All six carry M1_SWIM | M1_AMPHIBIOUS.

### Notes
- Wand of cold and wand of fire freeze/cook water tiles and strand sea monsters — a standard tactic absent from the section. Could add in a follow-up.
- Greased outer armor or oilskin cloak blocks the grab. Also absent.

---

## 2026-05-18 — v2 audit #20: Voluntary Challenges — Polymorph Restrictions

Source: `spoilers/companion.md` line 6855. 2 narrow factual fixes. Other proposed edits reverted as scope-creep.

### Wrong → fixed
- **"surviving a stoning attack (auto-transforms to stone golem)"**: misreads `poly_when_stoned()` at `mondata.c:80-86`, which returns true only for non-stone golems. A normal character petrifies and dies; only a player already polymorphed into a flesh/clay/etc. golem reverts to stone golem. Dropped from the less-obvious list.
- **"sandestin … corpse"**: sandestins are G_NOCORPSE (`eat.c:1246` comment), so eating one is unreachable. Dropped from the corpse list.

### Reverted (do not re-apply)
- "The Amulet of Unchanging blocks every path" → reworded into a longer Antimagic-vs-Unchanging blocking chart. **Reverted.** The section is about the conduct, not an encyclopedia of polymorph mechanics. The original sentence is technically loose about Antimagic but is the right level of detail for a beginner deciding whether to attempt the conduct.
- Lycanthropy added as a less-obvious source. **Reverted.** Real but trivia at this section's level; were-attacks are covered elsewhere.
- Ring of polymorph clarified as "1/100 per turn random shifts". **Reverted.** The practical advice ("don't wear one") is the same regardless of mechanism.
- Reality-check sentence ("polyselfless is easy, polypileless is harder"). **Reverted.** Meta-commentary that adds length without changing play.
- User reaction to the original v2 edit: *"the point of covering the no-polymorph conduct is to talk about that conduct, not to give an exhaustive ways of doing polymorph."*

### Verified
- `polyselfs++` lives only in `polymon()` at `polyself.c:751` and the eat-a-mimic path at `eat.c:1199`.
- `polypiles++` ticks at `zap.c:2198` (wand/spell of polymorph) and `potion.c:2476` (dipping into potion of polymorph). Only those two paths.
- Polymorph trap: blocked by `Antimagic || Unchanging` at `trap.c:2486-2495`.
- Genetic engineer AD_POLY: blocked by `Antimagic` OR `Unchanging` at `mhitm.c:1127-1144`.
- Chameleon/doppelganger/genetic engineer corpse eat: only `Unchanging` blocks (`eat.c:1244-1263`).
- Self-zap of WAN_POLYMORPH/SPE_POLYMORPH: blocked only by `Unchanging` (`zap.c:2804-2809`).
- Fountain "toxic wastes" calls `polyself()`, blocked only by `Unchanging` (`fountain.c:680-685`).
- System shock returns early in `polyself()` at `polyself.c:488-495`, so a failed shock does NOT tick the conduct.

---

## 2026-05-18 — v2 audit #21: A Practical Identification Strategy — The Engrave Test (Wands)

Source: `spoilers/companion.md` line 2934. No corrections (re-audit clean).

### Verified
- "A lit field surrounds you" (light) at `src/zap.c:2549`.
- "The floor is riddled by bullet holes" (magic missile) at `src/engrave.c:646`.
- "Gravel flies up from the floor" (digging) at `src/engrave.c:704`.
- "A few ice cubes drop from the wand" (cold) at `src/engrave.c:660-661`.
- "Flames fly from the wand" (fire) at `src/engrave.c:716`.
- "Lightning arcs from the wand" + blind branch (lightning) at `src/engrave.c:727-728`, blind gated at `engrave.c:1248`.
- "The bugs on the floor stop moving!" — both sleep and death share this message at `src/engrave.c:651-656`.
- "The wand unsuccessfully fights your attempt to write!" — unique to striking at `src/engrave.c:604`.
- "The bugs on the floor slow down/speed up!" at `src/engrave.c:608-615`.
- Polymorph randomizes prior engraving at `src/engrave.c:618-633`.
- Cancellation / make-invisible / teleportation share "engraving … vanishes" at `src/engrave.c:666-682`.
- Wand of wishing engrave grants the wish at `src/zap.c:2575-2585`.
- DUST-class wands (nothing, undead turning, opening, locking, probing) produce no special message at `src/engrave.c:635-640`.
- Cursed wands explode at 1% per engrave per `WAND_BACKFIRE_CHANCE = 100` (`include/hack.h:1410`, `src/engrave.c:794`).

### Notes
- Auditor flagged "Apply a wand by engraving" (use of "Apply" vs. the `a` command) as a mild voice ambiguity. Left as-is per preserve-voice; section reads fluently and the surrounding "command: `E`" makes the intent clear.

---

## 2026-05-18 — v2 audit #22: Bestiary Tables — Imps and minor demons `i`

Source: `spoilers/companion.md` line 8116. 2 factual fixes.

### Wrong → fixed
- **manes "poisonous-corpse"** and **lemure "poisonous-corpse"** tags: both monsters carry `G_NOCORPSE` (`include/monsters.h:545` and `:567`), so M1_POIS is dormant and no corpse ever drops. Replaced "poisonous-corpse" with "No corpse" in both rows.
- **lemure missing Gehennom-only tag**: lemure has `G_HELL` (`monsters.h:567`), generating only in Gehennom — same shape as the disenchanter row's "Gehennom-only" tag. Added.

### Verified
- All six rows match `include/monsters.h:544-587` exactly (manes / homunculus / imp / lemure / quasit / tengu).
- "All except imp are poison-resistant" — confirmed (all carry MR_POISON except imp).
- "Follow you up and down stairs" — all six carry M2_STALK.

### Notes
- Tengu corpse confers teleport / teleport-control intrinsic. Worth flagging if/when the bestiary's corpse-intrinsic notation gets a consistency pass. Not added in this pass.

---

## 2026-05-18 — v2 audit #23: Weapons Tables — Morning star

Source: `spoilers/companion.md` line 7406. 0 user-facing corrections. 1 badge correction.

### Verified
- Damage 1d4+1d4 / 1d6+1, weight 120, cost 10, hit 0, iron, one-handed at `include/objects.h:363-365` plus bonus dice from `src/weapon.c:225-289`.
- P_MORNING_STAR is a distinct skill class (id 12) at `include/skills.h:35`.
- Role caps (not shown in section but consistent): Bar/Pri Skilled; Cav Expert; Val/Wiz/Sam/Mon Basic.

### Badge correction
- The pass-1 badge stated "No artifact morning star exists." That's wrong: **Trollsbane** is a MORNING_STAR artifact at `include/artilist.h:182-184` (regenerates while wielded, +d5 vs S_TROLL, cost 200). Documented in the Artifacts chapter; the user-facing row prose is fine as-is, so no prose change applied — just badge updated.

---

## 2026-05-18 — v2 audit #24: Branches and Landmarks — Sokoban

Source: `spoilers/companion.md` line 926. 2 factual fixes.

### Wrong → fixed
- **"you can't dig through the floors"**: too broad. The `hardfloor` flag is set only on the entrance level (soko4-{1,2}.lua:38,7); interior soko levels don't carry it. `Can_dig_down` checks the flag (`src/dungeon.c:1648-1654`). In practice digging on interior levels would just drop you onto another soko level (Sokoban is an upward-only branch), so escape is futile either way, but the rule as stated is inaccurate. Narrowed to "you can't dig down off the entrance level (its floor is reinforced)."
- **"Levitation or flying over unfinished pits is free of penalty"**: technically true (no `sokoban_guilt()` for floating past pits), but misleading. While levitating you cannot push boulders at all — `src/hack.c:415-425` rejects pushes with "you don't have enough leverage." Flying (not levitating) still allows pushing. Split into: "Flying lets you skip unfinished pits without penalty. Levitation avoids pits too, but it also prevents you from pushing boulders at all, so it's useless for solving."

### Verified
- Entrance DL 6-10, one above Oracle (Oracle DL 5-9 + Sokoban base=1 chainlevel=oracle, direction=up at `dat/dungeon.lua:21-25`, `60-66`).
- Four puzzle levels, two variants each at `dat/soko*.lua`; branch `nlevels = 2` per layer at `dat/dungeon.lua:225-244`.
- `noteleport` on every soko file (`dat/soko*.lua:7,38`); teleport blocked via `In_sokoban` at `src/teleport.c:1185-1189`.
- Prize on soko1 (top): 75% bag of holding / 25% amulet of reflection in soko1-1; 25/75 reversed in soko1-2.
- Cursed scroll of scare monster under the prize.
- Conduct triggers: squeeze, polymorph boulder, fracture by striking, scroll of earth — all call `sokoban_guilt()` which does `u.uconduct.sokocheat++; change_luck(-1)` (`src/trap.c:7039-7054`).

---

## 2026-05-18 — v2 audit #25: Bestiary Tables — Nagas `N`

Source: `spoilers/companion.md` line 8669. 4 fixes (3 factual + 1 voice de-duplication).

### Wrong → fixed
- **guardian naga row Notes: "Friendly to the Healer. Hostile otherwise."**: wrong. The pass-1 badge claimed this line was removed, but it was not. Guardian naga is MS_MUMBLE with maligntyp = +7 (lawful) per `monsters.h:2040`. `peace_minded()` has no special-case path for Healer/Rogue; only `sgn(mal)==sgn(ual)` applies, which means *lawful* PCs may find them peaceful (Knight, Samurai, lawful Valkyrie/Priest/Monk/Archeologist/Caveman). Replaced with "Lawful PCs may find them peaceful."
- **Intro "varied breath weapons (acid / fire / poison)"**: wrong. Only the red naga has `AT_BREA` (fire) at `monsters.h:2008`. Black naga and guardian naga use `AT_SPIT` (acid and venom respectively). Golden naga has no breath/spit — its second attack is `AT_MAGC AD_SPEL` (`monsters.h:2027`). Narrowed to "with ranged attacks" without enumerating per-color details, per the no-trivia rule.
- **golden naga row "spell 4d6 spell"**: duplicated word. The attack is `ATTK(AT_MAGC, AD_SPEL, 4, 6)`. Changed to "cast spell 4d6" matching the spoiler's notation elsewhere for AT_MAGC.

### Voice (de-duplication)
- Intro had "All nagas are poison-resistant" both at the end of the first sentence and again as a standalone one-line paragraph. Dropped the standalone duplicate.

### Verified
- All 8 rows match `include/monsters.h:1972-2048` exactly. All carry MR_POISON.
- Black naga corpse confers poison + acid + stoning resistance per `monsters.h:2020` MR_POISON|MR_ACID|MR_STONE — section correctly surfaces this.

---

## 2026-05-18 — v2 rollback: trivia additions from batches 1-4

User feedback during batch 5: *"so instead of making the book more brief and to the point, we are filling it with more rare trivia that isn't actually helpful."*

Six trivia additions from batches 1-4 reverted. Each was technically correct but added completeness rather than saving a beginner's life or changing a strategic decision.

### Reverted

- **v2 audit #5 (The Quest)**: named-artifact lists for carried-MR and wielded/worn-MR collapsed back to "a few grant... a few others block..." with a pointer to the Artifacts chapter. The pass-1 framing was wrong ("only the Tourist's PYEC"); the v2 expansion to three named artifacts on each side was the wrong correction — a generic statement plus a chapter pointer is the right level.
- **v2 audit #7 (Broadsword)**: dropped the Dragonbane and Orcrist row notes added in v2. Restored Stormbringer to the original short form ("the chaotic artifact form"). The broadsword row's redundant "+d4 small, +1 large" formula note (already encoded in the Damage column) is now empty rather than replaced with an artifact mention.
- **v2 audit #8 (Vampires)**: dropped "Lords and Vlad can also become wolves" from the intro. The "bat or cloud" gloss is sufficient at the bestiary-row level. (The G_NOCORPSE fix on the "poisonous corpses" claim is kept.)
- **v2 audit #10 (Long sword)**: artifact list rolled back from 6 names to 4 (Excalibur, Vorpal Blade, Frost Brand, Fire Brand — the pass-1 state). Giantslayer and Sunsword are documented in the Artifacts chapter.
- **v2 audit #12 (Mace)**: dropped the "Sceptre of Might is the other MACE artifact" addition. Demonbane is the famous one and is already named. (The PHYS(5,0) interpretation fix and the silver-mace `hates_silver` fix are kept.)
- **v2 audit #17 (Seduction)**: dropped the ring-of-adornment paragraph (succubus pockets / incubus puts on). The XL-1 safety note for the farm strategy is kept — that's a real lifesaver for a beginner attempting the strategy and not trivia.

### Voice fix

- Sea monsters intro em-dash → colon ("drag you under to drown — instadeath" → "drag you under to drown: instadeath") per the punctuation ladder.

### Lesson

Audit additions need a "would a beginner make a different decision with this fact?" test. The Artifacts chapter is the canonical home for artifact details; bestiary and weapon rows should not duplicate it. Saved as a memory rule [feedback-no-trivia] for the autonomous run going forward.

---

## 2026-05-18 — v2 audit #26: Dangerous Encounters — Enchantment Drain

Source: `spoilers/companion.md` line 2106. No corrections (re-audit clean).

### Verified
- G_HELL gates generation (`monsters.h:2156`; `makemon.c:1935,1998`).
- Active-claw target via `some_armor()` at `do_wear.c:2629-2653` (cloak > body armor > shirt; 1/4 chance each for helm/gloves/boots/shield). Weapons never targeted by the active attack.
- If naked, `rn2(5)` may chew ring/ring/amulet/blindfold or nothing at `uhitm.c:3621-3640`. (Note: `drain_item` actually only drains charged objects; the amulet/blindfold branches no-op. The book's wording "It can instead chew a ring, amulet, or blindfold" overstates what actually happens, but the strategic message — "if you're naked, expect to lose enchantment elsewhere" — is right. Skippable trivia.)
- Passive weapon drain when YOU melee them at `mhitu.c:2508-2515` (silent).
- Active-claw "less effective" message at `uhitm.c:3642`.
- MC defense via `mhitm_mgc_atk_negated` at `uhitm.c:3613`; MC3 ~ 90% negation. MC does NOT apply to the passive counter-drain.
- Artifact / Invocation-item / Rider-corpse resistance at `zap.c:1392-1394, 1462-1467`.
- Corpse strips one intrinsic via `attrcurse()` at `eat.c:1270-1275`.

### Close calls / notes
- "Three or four melee strikes will take a +7 sword to +3" is slightly optimistic (90% drain probability, so ~4.4 strikes expected on average). The strategic message ("don't melee them") is right either way. Left as-is.

---

## 2026-05-18 — v2 audit #27: Bestiary Tables — Jabberwocks `J`

Source: `spoilers/companion.md` line 8595. No corrections (re-audit clean).

### Verified
- jabberwock row LVL(15, 12, -2, 50, 0), bite 2d10 × 2 + claw 2d10 × 2, color orange, M1_FLY, G_GENO|1 — all match `include/monsters.h:1806-1814`.
- Vorpal Blade auto-behead vs `PM_JABBERWOCK` at `src/artifact.c:1595-1596` confirmed: `dieroll == 1 || mdef->data == &mons[PM_JABBERWOCK]` short-circuits the 1/20 trigger.
- "Vorpal jabberwock" entry at `monsters.h:1816-1824` is `#if 0 /* DEFERRED */` and correctly excluded.
- "Player baseline speed" claim correct: `NORMAL_SPEED 12` at `permonst.h:80`.

---

## 2026-05-18 — v2 audit #28: Dangerous Encounters — Drowning

Source: `spoilers/companion.md` line 1979. No corrections (re-audit clean).

### Verified
- Drown check uses monster's tile (`is_pool(magr->mx, magr->my)`) gated by `!Swimming && !Amphibious && !Breathless` at `src/uhitm.c:3389-3390`. No encumbrance test in the grab-drown path.
- Three flags that prevent it: Swimming, Amphibious, Breathless (`youprop.h:264-277`). Magical breathing grants both Amphibious and Breathless.
- Eels use AT_TUCH+AD_WRAP; kraken uses AT_HUGS+AD_WRAP (`monsters.h:3230-3256`). Both route via `mhitm_ad_wrap()`.
- Castle moat eels at `dat/castle.lua:186-189`. Medusa-4 has eels+kraken; medusa-1/3 only eels. Water plane has both.
- Swamp room generation: eels + piranha only, no krakens by design (`mkroom.c:557-565`).
- Pool entry gated by `!Levitation && !Flying` at `hack.c:3272`. The drown/grab path does NOT check Levitation — "doesn't save you from an eel's grab" is right.
- `emergency_disrobe()` gated by Stressed+ at `trap.c:4897-4941`.

### Close calls / notes
- "An amulet (or spell) of magical breathing gives you Breathless" — also gives Amphibious; either flag alone defeats the grab-drown. Harmless shorthand.
- "Eels and krakens at moats around the Castle, in swamp rooms, and on the Water Plane" — krakens are only on Medusa-4 and the Water Plane, not in swamp rooms or castle moats. Defensible as a union ("eels [in some places] and krakens [in others]"), but a careful reader could misread. Borderline; left.

---

## 2026-05-18 — v2 audit #29: A Practical Identification Strategy — The Price Is Right

Source: `spoilers/companion.md` line 2636. 1 factual fix.

### Wrong → fixed
- **Angry-shopkeeper paragraph "+33% buy surcharge ... until you pay your bill in full"**: backwards. `pacify_shk(shkp, FALSE)` at `shk.c:2663` (the bill-payment path) does NOT clear the `surcharge` flag. The flag is only cleared by `pacify_shk(shkp, TRUE)`, called at `shk.c:302` (bones-load) and `shk.c:793` (new-customer transition). So in a single hero's playthrough, paying the bill never lifts the surcharge — it's effectively permanent for that hero in that shop. The pass-1 close-call note had it right but the body text was never corrected. Reworded.

### Verified
- Cha multipliers exactly match `shk.c:2953-2964` (Cha ≤5 ×2, 6-7 ×3/2, 8-10 ×4/3, 11-15 ×1, 16-17 ×3/4, 18 ×2/3, ≥19 ×1/2).
- Tourist / dunce / Hawaiian-shirt cues at `shk.c:2947-2951`: shared ×4/3 markup, mutually exclusive (`if`/`else if`), XL threshold `u.ulevel < MAXULEV/2` = below XL 15.
- Tourist sell drops to base/3 at `shk.c:3154-3160`.
- Unfamiliar-shop sell penalty 3/4 (`!(shkp->m_id % 4)`) at `shk.c:3173-3174`.
- UnID buy surcharge 4/3 (`(oid % 4) == 0`) at `shk.c:2864-2873`.
- Angry surcharge formula `tmp += (tmp+2)/3` at `shk.c:2985-2986`; JS widget matches.
- JS `computeBuy`/`computeSell` faithfully replicate the C math including the `(*10/d + 5)/10` rounding step.
- Sell-offer 1/2 base, 3/8 on unID from unfamiliar shop. Correct.
- All four price tables (scrolls 22 entries, potions 26, rings 28, wands 22) match `include/objects.h` exactly. Group-size claims ($300 ring group = 4 rings; $500 wand group = 2) verified.
- Amulets all $150 except the $0 fake Amulet of Yendor (`objects.h:865-869`).

### Close calls / notes
- "If a scroll is in the $20 group, it's identify. Period." True at base price but the unID 4/3 surcharge plus Cha multipliers can move that to $27 / $30 / etc. The print-only conversion table handles this, but the "Period." is slightly absolute.

---

## 2026-05-18 — v2 audit #30: Bestiary Tables — Piercers `p`

Source: `spoilers/companion.md` line 8238. No corrections (re-audit clean).

### Verified
- rock piercer Lvl 3, Spd 1, AC 3, MR 0, bite 2d6 at `include/monsters.h:800-808`.
- iron piercer Lvl 5, Spd 1, AC 0, MR 0, bite 3d6 at `include/monsters.h:809-817`.
- glass piercer Lvl 7, Spd 1, AC 0, MR 0, bite 4d6, MR_ACID at `include/monsters.h:818-826`.
- All three carry M1_CLING | M1_HIDE.

---

## 2026-05-18 — v2 audit #31: Bestiary Tables — Vortices `v`

Source: `spoilers/companion.md` line 8346. No corrections (re-audit clean).

### Verified
- All six rows match `include/monsters.h:1053-1110`: fog cloud (gray, Lvl 3, Spd 1, AC 0, engulf 1d6 AD_PHYS); dust vortex (brown, Lvl 4, Spd 20, MR 30, engulf 2d8 AD_BLND); ice vortex (cyan, Lvl 5, Spd 20, MR 30, engulf 1d6 AD_COLD); energy vortex (HI_ZAP / bright-blue, Lvl 6, Spd 20, MR 30, engulf 1d6 AD_ELEC + 2d6 AD_DREN + AT_NONE 0d4 passive); steam vortex (blue, Lvl 7, Spd 22, MR 30, engulf 1d8 AD_FIRE); fire vortex (yellow, Lvl 8, Spd 22, MR 30, engulf 1d10 AD_FIRE + AT_NONE 0d4 passive).
- All six carry M1_FLY|M1_MINDLESS|G_NOCORPSE.
- Intro damage-type list (blinding/cold/shock+drain/fire) accurate; fog cloud's plain physical engulf is implicit.

---

## 2026-05-18 — v2 audit #32: The Castle

Source: `spoilers/companion.md` line 5435. 3 factual corrections.

### Wrong → fixed
- **"A throne room with a throne and guards"**: the throne room (region 27,05-37,11) is filled with random court monsters from the L/N/E/H/M/O/R/T/X/Z classes per `dat/castle.lua:54, 195-221`. Soldiers and the lieutenant guard the entry hall and tower corners (`castle.lua:162-179`), not the throne room. Reworded to "a random court of high-letter monsters."
- **"A central hallway with five trap doors at evenly-spaced squares"**: `castle.lua:156-160` places them at columns 40/44/48/52/55 — gaps of 4/4/4/3, not strictly even. Dropped "evenly-spaced."
- **"Stepping on one drops you to a random Gehennom level"**: wrong. `src/trap.c:669-670` checks `Is_stronghold(&u.uz)` and calls `find_hell()`; `src/dungeon.c:1949-1953` always sets `dlevel = 1` — i.e., the **Valley of the Dead** specifically. Reworded.

### Verified
- Wand-of-wishing chest mechanics at `dat/castle.lua:142-149` — exactly one chest, locked, in one of four corner alcoves (`place:rndcoord(1)`), containing `wishing` and `potion of gain level`.
- Elbereth + cursed scroll wards explained by the lua author's own comment at `castle.lua:150` ("Prevent monsters from eating it").
- Castle chest now locked in 5.0 per `doc/fixes5-0-0.txt:102`.
- 5.0 no-arch-lich (and master-lich) change at `doc/fixes5-0-0.txt:232-234`.
- Wand of wishing yields ~2 wishes reliably: `mkobj.c:1116-1117` (spe=1 at creation) + `read.c:738-787` (cap on recharge; second always explodes).
- Monsters cannot unlock chests in 5.0 per `muse.c:2273`.
- Castle DL math: `dat/dungeon.lua:7-11, 82-85` — DoD base=25 range=5, Castle base=-1 → DL 25-29.

---

## 2026-05-18 — v2 audit #33: Weapons Tables — Saber

Source: `spoilers/companion.md` line 7298. 1 factual fix.

### Wrong → fixed
- **Silver saber row "Grayswandir (Lawful, +5 hit, hallucination resistance)"**: PHYS(5, 0) at `artilist.h:172` gives +1d5 to-hit (`artifact.c:1083-1086 spec_abon`) AND doubles damage (`artifact.c:1106-1107 spec_dbon`), same shape as Demonbane (corrected in v2 #12). "+5 hit" is wrong; the full effect set is documented in the Artifacts chapter at line 4219. Per no-trivia, replaced the inline parenthetical with "(see Artifacts)" rather than duplicating the canonical entry.

### Verified
- scimitar 1d8/1d8, wt 40, cost 15, iron, P_SABER at `include/objects.h:256-258`.
- silver saber 1d8/1d8, wt 40, cost 75, silver, P_SABER at `include/objects.h:259-261`.
- P_SCIMITAR-into-P_SABER merge confirmed.
- Werebane SILVER_SABER artifact at `artilist.h:166-168`.
- Grayswandir SILVER_SABER artifact at `artilist.h:170-172`.

---

## 2026-05-18 — v2 audit #34: A Practical Identification Strategy — The Sink Test (Rings)

Source: `spoilers/companion.md` line 2966. No corrections (badge added).

### Verified
- `dosinkring()` at `src/do.c:498-650` — 28 distinct ring-type messages, plus the searching/slow-digestion "goto giveback" branch at `src/do.c:507-516`.
- 1/20 backup chance and 1/5 buried chance for the consumed branch at `src/do.c:649-660`.
- Section correctly defers detail to the Sinks subsection.

### Notes
- "Every other ring is consumed" is a slight simplification (most consumed, but 1/20 back up); section's defer-to-Sinks framing handles the nuance.
- Section had no audit badge before this pass; one was added.

---

## 2026-05-18 — v2 audit #35: Weapons Tables — Flail

Source: `spoilers/companion.md` line 7415. No corrections (re-audit clean).

### Verified
- flail 1d6/1d4 + small +1 (`weapon.c:272-275`) + large +1d4 (`weapon.c:239-243`), wt 15, cost 4, iron, P_FLAIL at `include/objects.h:384-386`.
- grappling hook 1d2/1d6, wt 30, cost 50, iron, P_FLAIL (WEPTOOL) at `include/objects.h:1010-1012`.
- `use_grapple()` pull mechanic at `src/apply.c:3728-3886`; range 4/4/5/8 by skill at `apply.c:3686-3698`.
- No FLAIL or GRAPPLING_HOOK artifact in `include/artilist.h`.

---

## 2026-05-18 — v2 audit #36: What to Pack

Source: `spoilers/companion.md` line 327. No corrections (re-audit clean).

### Verified
- Per-role inventory from `src/u_init.c`.
- Pet step-around at `src/dogmove.c:145` + 991-1077.
- Floating-eye paralysis at `src/uhitm.c:6022`.
- Touchstone gem-ID at `src/apply.c:2742-2750`.
- Burdened status label at `src/botl.c:12`.
- Food ration 800 nut / wt 20 at `include/objects.h:1110`.

---

## 2026-05-18 — v2 audit #37: Bestiary Tables — Bats and birds `B`

Source: `spoilers/companion.md` line 8449. 1 voice/factual tightening.

### Wrong → fixed
- **"Vampire bats drain Strength on the second bite"**: misleading framing. The AD_DRST is the second *attack slot* (not a sequential second bite); both slots roll independently each turn (`!rn2(8)` at `src/uhitm.c:3154`). Reworded to "Vampire bats drain Strength with a poisoned bite (poison resistance blocks it)."

### Verified
- All four rows (bat / giant bat / raven / vampire bat) match `include/monsters.h:1269-1297` exactly.
- All carry M1_FLY.
- Erratic-fly behavior from S_BAT class branch at `src/monmove.c:1870-1871` (1/3 chance to wander).
- Poison resistance blocks the drain via `poisoned()` at `src/attrib.c:338-343`.

### Notes
- The auditor flagged that `poisoned()` can also instakill or do HP damage in rare branches; per no-trivia, not added — the practical advice ("get poison resistance") is unchanged.

---

## 2026-05-18 — v2 audit #38: Provisions and Dining

Source: `spoilers/companion.md` line 3190. 3 factual corrections + 1 wisdom adjustment.

### Wrong → fixed
- **"1–50 | Weak | Movement slowed."**: wrong effect. Weak imposes a -1 Strength penalty via ATEMP (`attrib.c:471` via `eat.c:3455`), not movement slowing. Reworded.
- **"Blessed tins open instantly."**: incomplete. Only a *blessed tin opener* guarantees instant; with an ordinary tin opener a blessed tin still rolls `rn2(2)` (50/50 between instant and one turn) at `eat.c:1740-1745`. Reworded.
- **"about 25 turns to vanish"** (globs): misread. 25 turns is the shrink *interval* per `mkobj.c:1487-1490`; a fresh weight-20 glob lasts ~500 turns total (the source comment says "twice as long as the average corpse"). Reworded.

### Wisdom adjustment
- **"Eat corpses within a few turns of the kill"**: understates the safe window. The rotted check at `eat.c:1887-1895, 1939` uses `(moves - age) / (10 + rn2(20)) > 5` — corpses are safe roughly 50 turns before tainting becomes a real risk. "A few turns" makes beginners discard usable food. Expanded to "30 to 50 turns."

### Verified
- Hunger thresholds (Satiated >1000, Hungry 51-150, Weak 1-50, Fainting ≤0) at `eat.c:3369-3372`.
- Base hunger -1/turn, sleep cuts to ~10% at `eat.c:3174-3179`.
- Encumbrance hunger fires only past Stressed at `eat.c:3197`.
- Food ration 800/20, lembas 800/5 at `objects.h:1106-1111`.
- Elven starting inventory swaps cram for lembas at `u_init.c:234`.
- Cannibalism `-rn1(4,2)` luck + aggravate, Caveman/Orc exempt at `eat.c:51, 770-786`.
- Prayer cures starvation at Weak or below at `pray.c:216`.
- Corpse intrinsic table verified against `include/monsters.h` mconveys masks.
- Vegan/vegetarian macros at `include/mondata.h:232-241`.

### Notes
- "Never eat cockatrice corpse" is strictly true for unprepared characters; the auditor flagged that stone-resistant + gloved players can sometimes eat cockatrice tins, but per no-trivia this edge case is omitted.

---

## 2026-05-18 — v2 audit #39: Bestiary Tables — Kobolds `k`

Source: `spoilers/companion.md` line 8151. 1 voice/factual fix plus a drive-by on Gnomes.

### Wrong → fixed
- **kobold shaman row "spell spell"**: implies two attacks. The C source has only one AT_MAGC/AD_SPEL attack at `include/monsters.h:651`. Changed to "cast spell" matching the AT_MAGC convention used elsewhere (Naga golden, etc.).
- **gnomish wizard row "spell spell"** (line 8569, in the Gnomes section): same bug — single AT_MAGC/AD_SPEL at `monsters.h:1697`. Changed to "cast spell" in a drive-by fix; Gnomes badge updated to note this.

### Verified
- All four kobold rows match `include/monsters.h:624-656`.
- All carry M1_POIS|MR_POISON.

---

## 2026-05-18 — v2 audit #40: Bestiary Tables — Felines `f`

Source: `spoilers/companion.md` line 8055. No corrections (re-audit clean).

### Verified
- All 8 rows match `include/monsters.h:381-444`: kitten, housecat, jaguar, lynx, panther, large cat, tiger, displacer beast.
- M2_DOMESTIC on kitten/housecat/large cat (tameable); M2_HOSTILE on the wild rows.
- Displacer beast carries M3_DISPLACES.
- Wizard always gets kitten via `urole.petnum=PM_KITTEN` (`role.c:548`).

### Notes
- Intro lists Valkyrie and Tourist as 50/50 kitten/dog, but Archeologist, Healer, Priest, Monk, Rogue, and Ranger also default to 50/50 when `urole.petnum` is `NON_PM` (`dog.c:93-100`). Only Wizard is guaranteed. Phrasing isn't wrong, just slightly partial; left as-is per preserve-voice.

---

## 2026-05-18 — v2 audit #41: Bestiary Tables — Mummies `M`

Source: `spoilers/companion.md` line 8644. 1 factual fix.

### Wrong → fixed
- **"All mummies have poisonous corpses and are mindless and undead."**: every mummy row carries `G_NOCORPSE` (`monsters.h:1902, 1910, 1918, 1927, 1936, 1944, 1953, 1961`; flag at `monflag.h:201`). Mummies never leave a corpse, so the M1_POIS flag is dormant. Reworded to "All mummies are mindless undead and leave no corpse."

### Verified
- All 8 rows (kobold/gnome/orc/dwarf/elf/human/ettin/giant mummy) match `include/monsters.h:1901-1968`.
- All carry MR_COLD | MR_SLEEP | MR_POISON, M1_MINDLESS | M2_UNDEAD.
- All attacks AD_PHYS only; no AD_DISE / "withering" mechanic (pass-1's removal stayed).

---

## 2026-05-18 — v2 audit #42: Traps and Hazards — Dangerous Traps

Source: `spoilers/companion.md` line 1262. 1 wisdom addition.

### Wisdom addition
- Sleeping-gas paragraph didn't mention sleep resistance. `trap.c:2772-2773` returns early on Sleep_resistance, so elves and ring-of-sleep-resistance wearers sidestep the trap entirely. Added one short sentence: "Sleep resistance (elven blood, the right ring) sidesteps it." Real strategic info for an elf player wondering if they need to fear sleep traps.

### Verified
- Anti-magic implosion formula at `trap.c:2351-2370` (rnd(4) base + Half_physical||Half_spell + Magicbane + first carried magic-resistance artifact, max 4d4; quartered for Passes_walls).
- Polymorph trap blocked by `Antimagic || Unchanging` at `trap.c:2486-2489`. Iron shoes checked first and convert into kicking boots (or vice versa) at `trap.c:2478-2486`.
- Fire trap damage `d(2,4)`; items still take `destroy_items` regardless of Fire_resistance per `trap.c:4233-4309`.
- Cancellation on magical trap: `20 + d(3,6)` explosion at `zap.c:3593-3621`.

### Notes
- Auditor flagged the iron-footwear polymorph-trap conversion as a potential addition; section already covers it ("your shoes shift instead"). Skipped.
- Auditor flagged "if you carry magic resistance" vs "if you're magic-resistant" wording difference between table cell and body paragraph; minor and not strategic. Left.

---

## 2026-05-18 — v2 audit #43: The Art of Combat

Source: `spoilers/companion.md` line 4685. 2 factual fixes.

### Wrong → fixed
- **To-hit list "Your Strength bonus (muscles still matter underground)"**: incomplete. `abon()` at `src/weapon.c:950-988` includes BOTH Strength AND Dexterity. Dex 25 yields +11, often the dominant contributor at high levels. Pass-1 missed this. Reworded to "Your Strength and Dexterity bonuses (muscles plus agility, both matter)" — preserves voice without expanding into a list.
- **"Monster spellcasters no longer get a free extra step after casting"** (full bullet): fabricated 5.0 change. The pass-1 audit flagged this as "plausible but unverified"; the v2 auditor confirmed no such fix exists in git history. Monsters still move via `m_move()` (PHASE THREE) then attack/cast via `mattacku()`/`castmu()` (PHASE FOUR) on the same turn (`monmove.c:911, 943-944, 971`). Bullet dropped entirely.

### Verified
- d20 + abon + AC + uhitinc + Luck + level formula at `src/uhitm.c:376-378`.
- Luck contribution cap `(|Luck|+2)/3` (so ±5 at Luck 13).
- Str damage +6 cap at STR ≥ 18/100.
- Two-handed Str-damage 50% bonus at `src/uhitm.c:1465-1468`.
- Two-weapon -9/-7/-5/-3 to-hit and -3/-1/0/+1 damage by skill at `src/weapon.c:1559-1600`.
- Conflict requires mutual sight at `src/mon.c:1306`; resist formula `rnd(20) > min(19, Cha - m_lev + u.ulevel)` at `src/mondata.c:1607-1612`.
- Ranged-monster keep-distance behavior new in 5.0/3.7 at `src/monmove.c:1180-1224`.
- Cornered scared monsters fight via `panicattk` at `src/monmove.c:918-920, 968`.

---

## 2026-05-18 — v2 audit #44: Dangerous Encounters — Level Drain

Source: `spoilers/companion.md` line 2079. 1 factual fix + 1 wisdom addition.

### Wrong → fixed
- **"the bite of a hostile incubus or succubus (see Seduction below)"**: under default `sysopt.seduce = 1` at `sys.c:100`, the demon's bite is `AD_SSEX`, not `AD_DRLI`. The `AD_SSEX → AD_DRLI` substitution at `mhitu.c:327-334` only fires when SEDUCE is disabled. So under stock options hostile foocubi do not drain levels. Dropped the clause.

### Wisdom addition
- Existing text said "you have to kill enough monsters to re-earn them" — implies that's the only path. Added: potion of restore ability restores one lost level per quaff, and a blessed one restores all at once (`potion.c:687-691`). Wraith corpse already listed; this rounds out the recovery options for a beginner who just got drained.

### Verified
- AD_DRLI carriers (wraith, barrow wight, Nazgul, vampire, vampire leader, Vlad) at `monsters.h:2281-2348`.
- Drain mechanic at `uhitm.c:2479-2488`: 1-in-3 chance, blocked by `Drain_resistance` or `mhitm_mgc_atk_negated`.
- HP/power loss per `u.uhpinc[u.ulevel]` / `u.ueninc[u.ulevel]` at `exper.c:251-273`.
- Drain resistance carriers (all wielded only): Excalibur, Stormbringer, Aesculapius at `artilist.h`.
- Black DSM grants both disintegration and drain resistance at `do_wear.c:809-815`.
- Shield of drain resistance has DRAIN_RES as its sole `oc_oprop` at `objects.h:656-658`.
- Wraith corpse +1 level via `pluslvl(FALSE)` at `eat.c:1141-1142`; weight 0 / cnutrit 0 makes it untinnable.

### Notes
- Synced the vampire-bat parenthetical to match the v2 #37 reword ("poisoned bite" not "second bite").

---

## 2026-05-18 — v2 audit #45: A Practical Identification Strategy — A Practical Strategy

Source: `spoilers/companion.md` line 3152. No corrections (re-audit clean).

### Verified
- Altar BUC flash at `do.c:379-389`.
- Engrave-test costs one charge at `engrave.c:792` + `zap.c:2520`.
- Wand of digging auto-IDs via "Gravel flies up" at `engrave.c:684-704`.
- WAN_COLD engrave message "A few ice cubes drop from the wand" at `engrave.c:658-661`.
- All amulets fixed 150gp at `objects.h:834`.

---

## 2026-05-18 — v2 audit #46: Choosing Your Expedition

Source: `spoilers/companion.md` line 132. 2 factual fixes + 2 wisdom adjustments.

### Wrong → fixed
- **Healer "convert them to fruit juice with an amethyst"**: wrong gemstone. The amethyst converts POT_BOOZE to fruit juice (`potion.c:2161-2163`), not POT_SICKNESS. Sickness → fruit juice is via unicorn horn (`potion.c:2151-2154`). Reworded.
- **Knight "+0 lance"**: the starting lance is +1, not +0 (`u_init.c:91-92`, `{ LANCE, 1, ... }`). Fixed to "+1 lance."

### Wisdom adjustments
- **Cave Dweller "You gain speed early"**: misleading. Cave Dweller intrinsic Fast is at XL 7 (`attrib.c:37`), while Samurai and Monk both get speed at XL 1. A beginner reading the section sequentially would reasonably expect "early" to mean what it means in the Samurai paragraph. Softened to "by mid-game."
- **"Mjollnir waiting at the first altar you can sacrifice on"** (closing recommendation): cross-aligned altars don't deliver sacrifice gifts. Clarified to "first co-aligned altar" — a real beginner gotcha when a new Valkyrie sacrifices at the first altar they find and gets nothing back.

### Verified
- All 13 role alignments and race availabilities against `src/role.c:55-558`.
- All 5 race stat caps against `role.c:597-678`.
- Race hostility / `lovemask` per `role.c` and `include/you.h:273`.
- Knight code: `-1` align for fleeing-or-helpless (`uhitm.c:336-339`); Samurai's giri at `uhitm.c:342-345`.
- Knight Excalibur 1/6, others Lawful 1/30 at XL ≥ 5 (`fountain.c:404-405`).
- Knight intrinsic jumping at char-gen (`u_init.c:691`).
- Intrinsic-by-XL tables in `attrib.c:27-88`.
- Elf sleep-res XL 4 (`attrib.c:94-95`); elf Priest/Wizard random instrument (`u_init.c:799-813`).
- Healer sickness immunity (`potion.c:977`).
- Priest BUC sense (`invent.c:3553-3555, 3593-3595`).
- Rogue backstab `+rnd(u.ulevel)` (`uhitm.c:920-964`).
- Monk veg-conduct alignment penalty (`eat.c:1379-1381`).
- Mjollnir ELEC(5,24) returns at Str 25, Valkyrie-only; role-gift alignment rewritten to match PC at char-gen (`artifact.c:92-95`), so "regardless of alignment" is correct.
- Demonbane Priest role-gift, silver mace (`artilist.h:162-164`); Priest mace Expert (`u_init.c:392`).
- Wizard skill-based spellbook ID is Wizard-only (`spell.c:861-867`).

### Notes
- Rogue "six daggers for throwing": actual range is 6-15 (`u_init.c:135`). Not corrected per no-trivia — "six" is the minimum and beginner doesn't need the range.
- Knight "lance is largely useless on foot" is true for melee but the lance can be `#applied` at reach distance. Not corrected per preserve-voice; the absoluteness reads fine for a first-time-player chapter.

---

## 2026-05-18 — v2 audit #47: Bestiary Tables — Jellies `j`

Source: `spoilers/companion.md` line 8131. No corrections (re-audit clean).

### Verified
- All three rows match `include/monsters.h:591-620`: blue jelly LVL(4,0,8,10) passive 0d6 cold; spotted LVL(5,0,8,10) passive 0d6 acid; ochre LVL(6,3,8,20) engulf 3d6 + passive 3d6 acid.
- All carry M1_AMORPHOUS | M1_MINDLESS.
- Blue jelly's MR_COLD|MR_POISON conveys permanently via `should_givit` at `eat.c:983-988`.
- Spotted/ochre's MR_ACID|MR_STONE conveys TIMED via `temp_givit` at `eat.c:991-997` (chance=3 for acid, chance=6 for stone).

---

## 2026-05-18 — v2 audit #48: Voluntary Challenges — Bonesless

Source: `spoilers/companion.md` line 6988. No corrections (re-audit clean).

### Verified
- "bonesless" xlogfile achievement set only when `!flags.bones` at `src/topten.c:605`.
- `bones` is `set_in_config` per `include/optlist.h:213-215` — config file / command line only, not the in-game `O` menu.
- `!flags.bones` blocks both save (`bones.c:360`) and load (`bones.c:642`).
- The "didn't encounter any bones levels" enlightenment is distinct (`insight.c:439-441` requires `flags.bones` true + `numbones==0`).
- 5.0 addition per `doc/fixes5-0-0.txt:2742`.

---

## 2026-05-18 — v2 audit #49: Traps and Hazards — Nuisance Traps

Source: `spoilers/companion.md` line 1226. No corrections (re-audit clean).

### Verified
- Arrow trap at `trap.c:1190-1248`; 1/15 trap-empty chance once seen.
- Dart trap with 1-in-6 poisoned dart at `trap.c:1273`.
- Squeaky board at `trap.c:1402-1476`; wake_nearby/wake_nearto, skipped by Levitation OR Flying.
- Rust trap default branch (40%) hits cloak/suit/shirt in order and douses lit lamps at `trap.c:1632-1643`.
- Missed arrows/darts land on the floor via `place_object + stackobj`, confirming "Veterans sometimes trigger them deliberately to stock up."

---

## 2026-05-18 — v2 audit #50: Dangerous Encounters — Petrification (Stoning)

Source: `spoilers/companion.md` line 1949. 1 timing fix + 1 wisdom softening.

### Wrong → fixed
- **"after that you're paralyzed for three turns and the next message kills you"**: off by two. The dialogue at counter 3 is "Your limbs have turned to stone" (paralysis); two MORE messages appear before death — "You have turned to stone" (counter 2) and "You are a statue" (counter 1) — and `done(STONING)` fires when the counter reaches 0 (`timeout.c:674-684`). Reworded to "the final messages kill you."

### Wisdom adjustment
- **Unchanging-during-stoning warning**: was over-strong. `poly_when_stoned` (`mondata.c:80-85`) only fires when the player is already polymorphed into a non-stone golem. For an unpolymorphed hero (the typical case), Unchanging doesn't actually block any rescue because there was no rescue to block. Reworded to scope the warning: "If you happen to be polymorphed into a non-stone golem, wearing it during the countdown is actively harmful..."

### Verified
- 5-turn countdown started by `make_stoned(5L,...)` at `uhitm.c:3937`; dialogue strings at `timeout.c:128-148`.
- "Your limbs have turned to stone" triggers `nomul(-3)` at `timeout.c:163-165`.
- Kicking a cockatrice corpse barefoot calls `instapetrify` at `dokick.c:542-554`.
- Tripping over a cockatrice corpse from Fumbling at `timeout.c:1256-1261`.
- Acid blob corpse grants `d(3,6)` turns of HStone_resistance at `eat.c:1089-1094`.
- Yellow dragon scale mail/scales grants EStone_resistance at `do_wear.c:860-872`.
- Wielded cockatrice corpse: hits call `munstone`/`minstapetrify` at `uhitm.c:1152-1167`; wielding without gloves is fatal at `wield.c:142-150`.
- Cures: lizard/acidic flesh (`eat.c:3941-3944`); potion of acid (`potion.c:1312`); stone-to-flesh (`zap.c:2974`); prayer (`pray.c:382`).

---

## 2026-05-18 — v2 audit #51: Weapons Tables — Whip

Source: `spoilers/companion.md` line 7526. No corrections (re-audit clean).

### Verified
- rubber hose 1d4/1d3, wt 20, cost 3, plastic, P_WHIP, prob 0 (never random) at `include/objects.h:374-376`.
- bullwhip 1d2/1, wt 20, cost 4, leather, P_WHIP at `include/objects.h:390-392`.
- Archeologist starter +1 proficient at `src/apply.c:2992-2993`.
- Disarm only when target wielding a weapon at `src/apply.c:3148-3153`.
- Pit yank anchors at `src/apply.c:3089-3099`.
- No whip artifacts in `include/artilist.h`.

---

## 2026-05-18 — v2 audit #52: Dangerous Encounters — The Touch of Death

Source: `spoilers/companion.md` line 2016. No corrections (re-audit clean).

### Verified
- Death the Rider's two AT_TUCH AD_DETH attacks (8d8 each) at `include/monsters.h:3144-3153`.
- `rn2(20)` roll: 17-19 = full touch (15%), 5-16 = permdrain=1 life drain (60%), 0-4 = miss (25%) at `src/uhitm.c:3858-3882`.
- Full touch `dmg = 50 + d(8,6)`, permadrain half at `src/mcastu.c:323-353`.
- `if (!Antimagic)` guard on the 17-19 branch with FALLTHROUGH to default drain at `src/uhitm.c:3862-3868`.
- Wand/spell self-zap checks only `nonliving || is_demon` (no Antimagic check) at `src/zap.c:2885-2902`; ray-hits-hero path checks both at `src/zap.c:4493-4502`.
- `nonliving` covers undead/manes/golems/S_VORTEX per `include/mondata.h:219-220`.

---

## 2026-05-18 — v2 audit #53: Traps and Hazards — Engravings

Source: `spoilers/companion.md` line 1419. No corrections (re-audit clean).

### Verified
- Engraving rate default 10 (instant); slow methods (dulling_wep / RING / GEM) set rate=1 at `engrave.c:1275, 1320-1325`.
- Uncursed athame skips slow branch and doesn't dull at `engrave.c:1306-1307`.
- Edged weapon dulling -1 enchantment per ~2 chars at `engrave.c:1357-1382`.
- Impairment garble (Blind 1/11, Confused 1/7, Stunned 1/4, Hallucinating 1/2) applies universally at `engrave.c:1218-1228`.
- Wand types: WAN_DIGGING → ENGRAVE, WAN_FIRE/LIGHTNING → BURN at `engrave.c:684-732`.
- DUST monster-step erodes 1 char per turn at `monmove.c:734` + `engrave.c:271-289`.
- BURN damage on ice or magical fire @ 50% at `engrave.c:278`.
- Strict-match Elbereth at `engrave.c:256`.
- "ad aerarium" niche placement at `mklev.c:728-737`.

---

## 2026-05-18 — v2 audit #54: Voluntary Challenges — Illiterate

Source: `spoilers/companion.md` line 6814. 1 wisdom softening.

### Wisdom softening
- **"Without spellbooks, you have no spells"**: overstates. Wizards, Priests, Healers, Monks, and Knights start with one pre-learned spell that lasts until `KEEN = 20000` turns expire (`spell.h:17`, `spell.c:2340`). For a casting role attempting Illiterate, the starting spell is a real (if temporary) asset. Reworded to "Without spellbooks, you can't learn new spells or refresh old ones, so any starting spell you have will eventually fade."

### Verified
- "x"/"X" engraving exemption at `engrave.c:1213` (length-1 with x/X).
- Blank scrolls/spellbooks exempt at `read.c:600-601`.
- Book of the Dead exempt at `read.c:600`.
- Hawaiian shirts exempt at `read.c:392-395` (returns before literate increment).
- Floor engraving redraw at `engrave.c:1724` (no conduct logic).
- Scrolls/spellbooks at `read.c:602`; fortune cookies at `eat.c:2525`; T-shirts at `read.c:397`; marker writing at `write.c:245`.
- Novel-only-on-read at `spell.c:519`.

### Notes
- Forbidden-reads list is technically incomplete (coins, credit cards, candy bars, magic markers, dunce caps, Orb of Fate signature, naming artifacts, Archeologist scroll auto-decipher), but per no-trivia the headline cases suffice. Tourists attempting Illiterate need to ditch their starting dunce cap; Archeologists must not pick up unknown scrolls — both are role-specific traps that an Illiterate player will discover.

---

## 2026-05-18 — v2 audit #55: Weapons Tables — Shuriken

Source: `spoilers/companion.md` line 7591. No corrections (re-audit clean).

### Verified
- 1d8/1d6, wt 1, cost 5, +2 hit, iron, PIERCE, missile, P_SHURIKEN at `include/objects.h:163-165`.
- `is_poisonable` per `include/obj.h:264-268`.
- Samurai trains to Expert per `src/u_init.c:481`.

---

## 2026-05-18 — v2 audit #56: Sokoban Solutions — Level 2, Version B

Source: `spoilers/companion.md` line 6290. No spoiler-text corrections; 1 badge correction.

### Wrong → fixed (badge only)
- The pass-1 badge cited "soko2-2.lua" as the source file. The actual source is `dat/soko3-2.lua` (NetHack Sokoban .lua files are numbered from the bottom up, so spoiler "Level 2" = second-from-top = soko3-X). Badge corrected.

### Verified
- All 16 boulder start coords (A-P) match `dat/soko3-2.lua:33-48` under spoiler = lua+1.
- Downstair @=(4,2)/lua(3,1), upstair <=(21,5)/lua(20,4), locked door +=(25,10)/lua(24,9), rolling-boulder →=(12,11)/lua(11,10), twelve hole traps at spoiler (13-24,11).
- All 22 push steps geometrically legal.
- Both intermediate diagrams (after step 9, after step 16) match simulated boulder positions.
- Step 17 (H left one) is necessary to clear the pushing position for steps 18 and 22.
- Final tally "Four boulders (A, D, G, and H) remain" — checks.

### Notes
- Step 21 ("Push G right one square. Push D up one square.") is gratuitous (the pass-1 badge already flagged this as "harmless"). Left as-is.

---

## 2026-05-18 — v2 audit #57: Weapons Tables — Spear

Source: `spoilers/companion.md` line 7476. 1 factual correction.

### Wrong → fixed
- **"The Valkyrie ... gets +1 multishot on any thrown spear"**: wrong. Per `src/dothrow.c:47-52` the P_SPEAR class multishot bonus goes to `PM_CAVE_DWELLER` (Caveman), not Valkyrie. Valkyrie has no class-specific spear multishot — she gets only the generic Expert-tier multishot that any Expert spear-user gets. The pass-1 audit asserted this incorrectly. Reworded the strategic framing: Valkyrie still starts with a spear and trains to Expert, but the Caveman is the actual multishot specialist. Updated the javelin Notes cell from "Valkyries can ranged-spam them" to "Cavemen can ranged-spam them."

### Verified
- All damage/weight/cost stats match `include/objects.h:174-191`.
- Valkyrie starts with a spear and caps at Expert (`u_init.c:160-161, 537`).
- Kebab +2 to-hit list (xorn, dragon, jabberwock, naga, giant) at `src/weapon.c:71-73, 167-168`.
- No spear artifacts in `include/artilist.h`.
- Stiletto is P_KNIFE, correctly excluded.

---

## 2026-05-18 — v2 audit #58: Voluntary Challenges — Wishing Restrictions

Source: `spoilers/companion.md` line 6874. No corrections (re-audit clean).

### Verified
- Two separate counters: `u.uconduct.wishes` and `u.uconduct.wisharti` at `include/you.h:157-158`.
- Two xlogfile achievements: `wishless` / `artiwishless` at `topten.c:596-597`.
- Wish sources: wand of wishing, smoky-potion djinni, fountain water demon, Vlad's throne, Amulet of Yendor pickup. All routes converge on `makewish()`.
- Wishing for literal "nothing" returns early without ticking the counter (`zap.c:6369-6373`).
- `wisharti` ticks even for *denied* artifact wishes (`objnam.c:5362-5365` runs BEFORE the deny branch at 5371-5381).

---

## 2026-05-18 — v2 audit #59: Voluntary Challenges — Petless

Source: `spoilers/companion.md` line 6945. 1 factual correction (fabrication removed).

### Wrong → fixed
- **"dairy products to foocubi"**: not a NetHack mechanic. Food-throw taming gates on `is_domestic(ptr)` (or monkey/ape + banana) per `include/mondata.h:255-261 befriend_with_obj()`. Foocubi aren't domestic and cannot be tamed by thrown food of any kind. The wiki-known foocubus trick is throwing a ring of adornment (pacification, not taming). Fabricated mechanism. Replaced with the actual food-throw taming path that was missing from the list: "food thrown at hostile dogs and cats."

### Verified
- `u.uconduct.pets` counter at `include/you.h:161`, incremented in `dog.c:87`.
- `OPTIONS=pettype:none` short-circuits `makedog()` at `dog.c:225-229`, overriding per-role mandatory pets.
- 5.0 addition per `doc/fixes5-0-0.txt:2843`.
- Real taming paths: scrolls of taming (`read.c:1057, 3325`), charm-monster spell (`spell.c:1522`), magic trap (`trap.c:4429`), food-throw at domestic monsters (covered by the fix above), magic flute (`music.c:214`), figurines.
- `petless` xlogfile achievement at `topten.c:606`.

### Notes
- The list is still exemplary rather than exhaustive (figurines, magic flute, werecreatures, demon-summoning prayer rewards all missing) — but per no-trivia the four examples in the spoiler suffice.

---

## 2026-05-18 — v2 audit #60: Sokoban Solutions — Level 3, Version B

Source: `spoilers/companion.md` line 6427. No corrections (re-audit clean).

### Verified
- All 16 boulders A-P map to `dat/soko2-2.lua` coords under spoiler = lua+1.
- Upstair `<` at (16,7) per pass-1 fix; downstair/start `@` at (7,12); rolling-boulder trap at (8,12); eleven holes at cols 9-19; two locked doors at (20,10) and (20,12).
- 15 numbered steps faithfully compress Boudewijn Waijers's original 22 steps (the spoiler merges adjacent Push+Finish pairs).
- Each push geometrically reachable.
- Intermediate map state after step 7 matches expected boulder positions.
- Final tally "Five boulders (A, B, D, E, and J) remain" exact (16 − 11 finished).

---

## 2026-05-18 — v2 audit #61: Bestiary Tables — Elementals `E`

Source: `spoilers/companion.md` line 8521. No corrections (re-audit clean).

### Verified
- All five rows match `include/monsters.h:1566-1610`: stalker (no mindless, sees-invis, M2_STALK); air (AT_ENGL AD_PHYS 1d10); fire (claw 3d6 AD_FIRE + passive 0d4); earth (claw 4d6 + MR_FIRE|MR_COLD|MR_POISON|MR_STONE); water (claw 5d6 + M1_SWIM|M1_AMPHIBIOUS + MR_POISON|MR_STONE).
- Lead-in "all except stalker also are mindless" matches the M1_MINDLESS flags.

### Notes
- "Water drowns if you're adjacent in water" is defensible flavor — water elementals don't have a drown attack but spawn only on water tiles, so encountering one already places you near the water-tile drowning risk.
- "Air engulfs and suffocates" — engulf is AD_PHYS, not AD_DRST; "suffocates" reads as engulf-flavor and is defensible.
- Air and fire rows could enrich Notes with their resistances (MR_POISON|MR_STONE on air, MR_FIRE|MR_POISON|MR_STONE on fire) to match earth/water rows. Pass-1 already flagged this as a close call; left for now.

---

## 2026-05-18 — v2 audit #64: Bestiary Tables — Xans and fantastic insects `x`

Source: `spoilers/companion.md` line 8387. 1 factual fix.

### Wrong → fixed
- **"sting your legs and slow you down"**: xan's AD_LEGS / Wounded_legs reduces carrying capacity (`hack.c:4331-4336`) and abuses Dex (`attrib.c:472, 581`) but does NOT reduce movement speed. Reworded to "sting your legs and cut your carrying capacity."

### Verified
- Grid bug Lvl 0, Spd 12, AC 9, bite 1d1 shock at `monsters.h:1149-1156`.
- Xan Lvl 7, Spd 18, AC -4, sting 1d4 AD_LEGS, M1_FLY|M1_POIS at `monsters.h:1157-1164`.
- Both carry MR_POISON.

---

## 2026-05-18 — v2 audit #65: Bestiary Tables — Trolls `T`

Source: `spoilers/companion.md` line 8782. No corrections (re-audit clean).

### Verified
- All five rows match `include/monsters.h:2225-2266`: troll, ice troll, rock troll, water troll, Olog-hai.
- All carry M1_REGEN | M2_STALK.
- S_TROLL class is `is_reviver` per `mondata.h:170`.
- Revival via `revive_corpse` at `mon.c:1560, 1679`.
- Trollsbane disables revive via `mkcorpstat_norevive` flag at `monst.h:247-248`, applied at `uhitm.c:1906, 4867` and `mhitm.c:1082`.
- Stoning leaves a statue (`mon.c:671 mkcorpstat(STATUE,...)`), so no corpse to revive from.

---

## 2026-05-18 — v2 audit #62: Tools of the Trade

Source: `spoilers/companion.md` line 3912. 4 corrections.

### Wrong → fixed
- **"Bell of Opening ... granted by your quest leader on Quest completion"**: wrong. The Bell is carried by the quest *nemesis* (`makemon.c:1378-1379` — `MS_NEMESIS` gets BELL_OF_OPENING at spawn) and looted from their corpse. The quest leader chides you if you finish without it (`quest.c:267-268 quest_complete_no_bell`) but doesn't grant it. Reworded the Other Notable Tools cell.
- **"One blessed scroll of charging restores it to at least 50"**: misleading. Uncursed charging also reaches 50 (`read.c:880-883`); blessing pushes the floor to 75. Reworded to "non-cursed scroll of charging restores it to at least 50 (more if blessed)."
- **Magic lamp "rub it while blessed and there's a 1-in-3 chance the djinni emerges"**: implies blessing affects emergence. The 1/3 emergence is independent of bless (`apply.c:1817`); bless only affects the wish-grant probability (80% blessed, lower otherwise). Reworded.
- **"~16 charges very well spent"** for writing scroll of charging: that's the basecost. Actual write cost is `rn1(8,8)` = 8-15 charges. Updated to "8-15 charges."

### Wisdom additions
- Added the G_UNIQ-skip caveat to class genocide: "uniquely-named demon lords survive any class genocide" (`read.c:2998`). Real beginner protection — a player who genocides `&` thinking it'll remove Demogorgon will be unpleasantly surprised.

### Verified
- Container weights and locked-on-creation rates at `objects.h:899-912`, `mkobj.c:311-336`.
- BoH scatter-not-destroy per `fixes5-0-0.txt:183`.
- Intelligent monsters loot containers per `fixes5-0-0.txt:2668`.
- Skeleton key floors `75 + Dex` boxes / `70 + Dex` doors at `lock.c:528, 640`.
- Magic marker 30-99 charges at `mkobj.c:1026 rn1(70,30)`.
- Write costs match per-scroll basecost / 2 to basecost at `write.c:13-57, 256-265`.
- Mid-write failure (scroll disappears, spellbook paper survives) at `write.c:269-282`.
- Second marker recharge always fails at `read.c:854-865`.
- Wand of wishing 2nd charging always explodes at `read.c:761-764`.
- Unicorn horn 7-status cure list at `apply.c:2312-2327`; no longer restores attribute drain per `fixes5-0-0.txt:190`.
- Magic flute sleep / harp tame at `music.c:589-669`.
- Drum of earthquake at `music.c:688-698`.
- Crystal ball one-glyph-class-per-gaze at `detect.c:1300-1311`.

---

## 2026-05-18 — v2 audit #63: Traps and Hazards — Searching and Detection

Source: `spoilers/companion.md` line 1319. 1 factual fix.

### Wrong → fixed
- **"Wand of secret door detection reveals everything hidden in a square radius around you"**: wrong shape. The wand uses `do_clear_area` at `vision.c:2107-2148` with `circle_data` at `vision.c:27-45` — a *circular* area of radius `BOLT_LIM = 8` (`hack.h:49`), further gated by `couldsee()` line-of-sight checks at `vision.c:2144`. Walls block detection. Reworded to "a roughly circular area around you (radius about eight, blocked by line of sight)."

### Verified
- `dosearch0` independent rolls per square at `detect.c:2033-2090`.
- `rnl` Luck bias at `rnd.c:112-140`; trap roll `!rnl(8)` at `detect.c:2079`.
- Excalibur is the only SPFX_SEARCH artifact at `artilist.h:85-86`; bonus only on rnl(7-fund) at `detect.c:2043, 2053`, not on trap roll.
- Wand reveals SDOOR/SCORR/traps/trapped chests/hidden mimics via `findone` at `detect.c:1639-1726`.
- Crystal ball trap detection scans the level-wide `gf.ftrap` list at `detect.c:1011-1075`.
- `trap_is_unavoidable` ground-trap list at `trap.c:2810-2898`.

---

## 2026-05-18 — v2 audit #66: Weapons Tables — Club

Source: `spoilers/companion.md` line 7383. 1 voice/factual tightening.

### Wrong → fixed
- **Club row Notes "What a Caveman starts with — basic but free of curses early"**: wrong. Starting inventory uses `blessorcurse(otmp, 10)` at `mkobj.c:876-885`, so about a 10% chance the starting club is cursed. Trimmed to "Caveman starter." matching the short-sword row's convention.

### Verified
- Club 1d6/1d3, wt 30, cost 3, wood, P_CLUB at `objects.h:371-373`.
- Aklys 1d6/1d3, wt 15, cost 4, iron, P_CLUB at `objects.h:381-383`.
- Caveman starts with club at `u_init.c:68-70`.
- Aklys return mechanic requires W_WEP per `dothrow.c:30-34 AutoReturn` macro; ~1% misfire at `dothrow.c:1711`.
- No P_CLUB artifacts in `include/artilist.h`.

---

## 2026-05-18 — v2 audit #67: Bestiary Tables — Nymphs `n`

Source: `spoilers/companion.md` line 8204. No corrections (re-audit clean).

### Verified
- All three rows (wood / water / mountain) Lvl 3, Spd 12, AC 9, MR 20%, AT_CLAW AD_SITM + AT_CLAW AD_SEDU at `monsters.h:702-723`.
- Water nymph M1_SWIM at `monsters.h:714`.
- All three M1_TPORT.
- AD_SITM steal-and-teleport handled at `uhitm.c:4724, 4798`; AD_SEDU at `uhitm.c:4642`.

---

## 2026-05-18 — v2 audit #68: A Practical Identification Strategy — Blessed, Uncursed, Cursed

Source: `spoilers/companion.md` line 2582. No corrections (re-audit clean).

### Verified
- Altar flash colors at `do.c:379-388` (amber=blessed, black=cursed).
- Pet step-around-cursed at `dogmove.c:535-538` (with starvation exception not surfaced in prose).
- Cursed armor stays welded at `do_wear.c:1900, 2199`.
- Cursed gain-level "rises through ceiling" at `potion.c:1083-1109`.
- Cursed scroll of teleportation = level teleport at `read.c:2015-2025`.
- Holy water making at `pray.c:1387-1411, 2336-2339`.
- Priests sense BUC naturally at `invent.c:2763, 3545`.
- Blessed scroll of identify "at least 2 items + 1-in-5 chance whole pack" at `read.c:2086-2092`.
- Cursed scroll of identify only IDs itself on first cursed read at `read.c:2074-2081`.

### Notes
- "Uncursed scroll IDs one or two items" is a typical-case simplification — the C code at `read.c:2086` has a 1-in-5 chance to roll `rn2(5)`, so uncursed *can* occasionally identify more, but the modal outcome is 1. Defensible as written.

---

## 2026-05-18 — v2 audit #69: A Practical Identification Strategy — Naming What You've Learned

Source: `spoilers/companion.md` line 3142. No corrections (re-audit clean).

### Verified
- `#name` / `#call` aliases at `src/cmd.c:1773-1774`.
- Class-naming via `docall` (sets `objects[otyp].oc_uname`) at `src/do_name.c:571-588`.
- Renaming-by-overwrite at `src/do_name.c:660-672` (frees old `*uname_p`, assigns new).

---

## 2026-05-18 — v2 audit #70: Bestiary Tables — Leprechauns `l`

Source: `spoilers/companion.md` line 8176. No corrections (re-audit clean).

### Verified
- Stats (Lvl 5, Spd 15, AC 8, MR 20, green, claw 1d2 AD_SGLD, M1_TPORT) at `monsters.h:660-666`.
- Stealgold + teleport at `src/steal.c:58-115`.

### Notes
- Auditor flagged that unseen leprechauns can bury gold (`monmove.c:1152-1171 leppie_stash`), so the corpse doesn't always drop the stolen gold back. Common case still drops gold; per no-trivia, left.

---

## 2026-05-18 — v2 audit #71: Dangerous Encounters — Genocide

Source: `spoilers/companion.md` line 2308. 1 word fix.

### Wrong → fixed
- **"genocide your own race"**: imprecise. The PLAYER branch at `read.c:2839` uses `mndx = u.umonster` = `gu.urole.mnum` (`u_init.c:991`), the **role's** monster (PM_VALKYRIE, PM_ARCHEOLOGIST, etc.), not the race (PM_HUMAN/PM_ELF/...). Changed "race" to "species."

### Verified
- Confused-uncursed-scroll path at `read.c:1737 do_genocide((!scursed) | (2 * !!Confusion))`; flags = 3 → killplayer at `read.c:2838-2842` + REALLY branch at `read.c:2968-2972` with killer "genocidal confusion."

---

## 2026-05-18 — v2 audit #72: Voluntary Challenges — Weaponless

Source: `spoilers/companion.md` line 6785. 2 misclassification fixes.

### Wrong → fixed
- **"iron chain"** in the weapon-tool list: wrong. Iron chain is CHAIN_CLASS (`objects.h:101, 1631`), not TOOL_CLASS. `is_weptool` requires `oclass == TOOL_CLASS`, so swinging a wielded iron chain does NOT break the conduct. Removed from the list.
- **"aklys"** framed as a weapon-tool: wrong. Aklys is WEAPON_CLASS via the `WEAPON()` macro at `objects.h:381-383`, not a weptool. Still breaks the conduct (via the WEAPON_CLASS branch), just kept in the list reordered to flow with the other weapons.

### Verified
- Core check at `src/uhitm.c:616-617` requires `weapon && (weapon->oclass == WEAPON_CLASS || is_weptool(weapon))`.
- Miss revert at `uhitm.c:636-639` (Vorpal hit-converted-to-miss rolls back weaphit).
- Polearm-via-`#apply` exception at `dothrow.c:2199-2203` is the only weaphit++ outside uhitm.c.
- Thrown/fired ammo does NOT break (no weaphit++ in those paths).
- Pick-axe and unicorn horn are weptools (`objects.h:1007-1016` via WEPTOOL macro).
- Wielded cockatrice corpse (FOOD_CLASS) and wands (WAND_CLASS) don't match the check — correctly listed as safe.

---

## 2026-05-18 — v2 audit #73: Bestiary Tables — Cockatrices `c`

Source: `spoilers/companion.md` line 7997. No corrections (re-audit clean).

### Verified
- All three rows match `monsters.h:167-195`: chickatrice Lvl 4, cockatrice Lvl 5, pyrolisk Lvl 6.
- chickatrice/cockatrice carry MR_POISON|MR_STONE; pyrolisk carries MR_POISON|MR_FIRE (no stoning).
- Wield-corpse rule: bare-handed cockatrice corpse calls `instapetrify` regardless of role at `wield.c:146-152`.

---

## 2026-05-18 — v2 audit #74: Bestiary Tables — Fungi and molds `F`

Source: `spoilers/companion.md` line 8543. No corrections (re-audit clean).

### Verified
- All 7 rows (lichen, brown/yellow/green/red mold, shrieker, violet fungus) match `monsters.h:1614-1676`.
- Lichen corpse never rots per `mkobj.c:1402`, `eat.c:59`.
- Yellow mold has M1_POIS (poisonous-corpse tag correct); other molds have MR_POISON resistance but no M1_POIS (their corpses aren't poisonous).

---

## 2026-05-18 — v2 audit #75: Your First Descent

Source: `spoilers/companion.md` line 378. 2 number fixes.

### Wrong → fixed
- **Prayer cooldown "about once every 300-500 turns"**: too low. `pray.c:780, 1356, 1819` use `rnz(300)` / `rnz(350)` scaled via `rne(4)` to ~75-2400 turns. Community wisdom is ~1000 turns. New players following 300-500 hit "too soon" rejections. Updated to "about a thousand turns or so."
- **Corpse rot "guaranteed-safe within 50 turns ... past ~150 turns certainly tainted"**: off in both directions per the `(moves - age) / (10 + rn2(20))` formula at `eat.c:1887, 1939`. Guaranteed-safe-from-HP-loss needs age ≤ 30 (rotted ≤ 3 at all divisors); guaranteed-taint needs age > 174. Updated to 30 / 175.

### Verified
- Lizard/lichen nonrotting at `eat.c:58-61`. Lizard corpse cures petrification at `eat.c:3941-3944`.
- Pet step-around-cursed at `dogmove.c:535`.
- Floating-eye paralysis-on-melee at `mhitu.c:2536-2557`.
- Stair-falling 1-3 HP at `do.c:1780-1795 losehp(rnd(3),...)`.
- Killer bee speed 18, G_LGROUP, poisoned at `monsters.h:96-102`.
- Supply chest mechanics (2/3 above Oracle, 2/3 chest vs 1/3 large box, 5/6 locked, 50% healing potion, Mines-branch food bias) at `mklev.c:1010-1119`.
- `#force` with dagger at `lock.c:658-670`.

---

## 2026-05-18 — v2 audit #76: Dangerous Encounters — The Displacer Beast

Source: `spoilers/companion.md` line 2366. 1 fabricated-mechanic removal.

### Wrong → fixed
- **"hostiles meleeing your pet displacer beast trigger the same 50% place-swap, so the attacker often ends up next to *you* instead of biting the pet"**: not supported by source. M3_DISPLACES is only consulted at `hack.c:1972` (hero attacks displacer) and `mon.c:2462` via `mfndpos` (the displacer moves through another monster's square via `ALLOW_MDISP`). There is NO `mhitm.c` path for hostile-attacks-pet-displacer triggering a swap. Fabricated. Removed; the pet is still excellent (AC -10, three attacks, 0% MR for taming) but not for a swap trick.

### Verified
- Stats AC -10, 4d4/4d4/2d10, speed 12, level 12, MR 0 at `monsters.h:437-444`.
- 50% melee swap at `hack.c:1972` (`!rn2(2)` for PM_DISPLACER_BEAST, gated by `goodpos`).
- Ranged bypasses swap (only fires in `domove_attackmon_at` melee path).
- MR 0 → sleep/paralysis/charm/taming all land.
- Corpse confers cloak-style Displacement intrinsic at `eat.c:1265-1268` (sets HDisplaced, distinct from the swap mechanic).

---

## 2026-05-18 — v2 audit #77: Bestiary Tables — Unicorns and horses `u`

Source: `spoilers/companion.md` line 8334. 1 factual fix.

### Wrong → fixed
- **"Horses (pony, horse, warhorse) are usually peaceful in the wild"**: wrong. `makemon.c:1339-1342` sets `mpeaceful` only for `is_unicorn()`, which excludes ponies/horses/warhorses. Wild ponies/horses/warhorses spawn hostile. The 1-in-100 saddled-spawn at `makemon.c:1447-1452` isn't peaceful either. Reworded to "spawn hostile in the wild but can be tamed, saddled, and ridden."

### Verified
- All 6 rows match `monsters.h:1002-1049`.
- Alignment-to-color mapping (white/L +7, gray/N 0, black/C -7).
- Co-aligned unicorns peaceful at `makemon.c:1339-1342`.
- Killing co-aligned: -5 Luck + "feel guilty" at `mon.c:3666-3669`. Cross-aligned: no Luck change.
- Gem-throw placation at `dothrow.c:2087-2098, 2309-2382` (unconditional `mpeaceful=1` + teleport).
- Knight's saddled pony at `dog.c:262-268`.
- Killed unicorn drops horn at `mon.c:604-613`.

---

## 2026-05-18 — v2 audit #78: Branches and Landmarks — Medusa's Island

Source: `spoilers/companion.md` line 1082. 2 small corrections; badge backfilled (none existed before).

### Wrong → fixed
- **"downward staircase (or ladder)"**: no medusa-*.lua uses a ladder; all four use `des.stair("down", ...)`. Dropped "(or ladder)."
- **"Giant eels"** as the only water threat: `dat/medusa-2.lua:99-104` has electric eels (six of them), not giant eels. Same grab-and-drown threat (both carry AT_TUCH+AD_WRAP) plus AD_ELEC bite. Added a one-clause clarifier "(electric eels on one layout)."

### Verified
- Level placement DL ~20-29 (DoD base 25 range 5, Medusa base -5 range 4) at `dat/dungeon.lua:75-81`.
- Four layouts at `dat/medusa-{1,2,3,4}.lua`.
- Perseus loot percentages (75% shield of reflection cursed / 25% levitation boots / 50% blessed +2 scimitar / 50% sack) match all four layouts.
- Other statues forced empty (`contents = 0`).
- Gaze stones Medusa via reflection at `src/mhitu.c:1721-1745`.
- Eel grab uses eel's tile for drown at `src/uhitm.c:3389-3401` — so levitation/water-walking on adjacent dry land does NOT save you. Section correctly captures this.
- Kraken only on `dat/medusa-4.lua:122`.
- Oilskin/grease protects against AT_TUCH+AD_WRAP grabs (only excluded for AT_ENGL).

### Notes
- Stone resistance also blocks the gaze per `mhitu.c:1747-1748` but is rarely attainable pre-Medusa. Omitted per no-trivia.

---

## 2026-05-18 — v2 audit #79: Weapons Tables — Knife

Source: `spoilers/companion.md` line 7277. No corrections (re-audit clean).

### Verified
- All 5 rows match `include/objects.h:215-233`: scalpel, knife, stiletto, worm tooth, crysknife. P_KNIFE on all.
- Healer scalpel starter at `u_init.c:77`.
- Crysknife revert mechanic at `do.c:903-918` (`!obj->oerodeproof || !rn2(10)`).
- Athame correctly NOT in this table — it's P_DAGGER (`objects.h:212-214`).

---

## 2026-05-18 — v2 audit #80: Voluntary Challenges — Pacifist

Source: `spoilers/companion.md` line 6803. No corrections (re-audit clean).

### Verified
- `u.uconduct.killer` referenced at `insight.c:2144-2145` and `topten.c:592`.
- Counter increments only at `mon.c:3500` (xkilled) and `hack.c:2201` (pet pushed into fatal trap).
- Monster-on-monster kills via `monkilled` (`mon.c:3377`) don't increment — conflict and pet kills are safe.
- Charm monster spell at `spell.c:1522` exists for the strategy mention.

---

## 2026-05-18 — v2 audit #81: Sokoban Solutions — Level 1, Version B

Source: `spoilers/companion.md` line 6201. No corrections (re-audit clean).

### Verified
- Map walls, floors, upstair (2,2), branch portal (4,2), all 12 boulders A-L geometry matches `dat/soko4-2.lua:9-21, 29-42`.
- Pits col 2 rows 3-7 and row 9 cols 2-6, both rolling-boulder traps, both scrolls of earth at (2,10)/(3,10) per `soko4-2.lua:48-64`.
- All 16 solution steps land on lua floor tiles with reachable cardinal approach squares.
- Final tally "D and E remain" exact: 10 boulders finished into 10 pits.
- Intermediate map at line 6231-6245 matches simulated post-step-7 state.

---

## 2026-05-18 — v2 audit #82: Dangerous Encounters — Starvation

Source: `spoilers/companion.md` line 2047. No corrections (re-audit clean).

### Verified
- Faint at `u.uhunger ≤ 0` per `eat.c:3369-3372`; faint handler at `eat.c:3410-3432`.
- STARVED death at `u.uhunger < -(100 + 10*Con)` per `eat.c:3437-3447`.
- Prayer cures hunger via TROUBLE_HUNGRY at `pray.c:216-217` (covers Weak/Fainting).

---

## 2026-05-18 — v2 audit #83: Use-Testing (The Careful Way)

Source: `spoilers/companion.md` line 2982. 4 factual corrections.

### Wrong → fixed
- **"Dipping a poisonable weapon (dagger, arrow, spear) into a potion of sickness"**: daggers and spears are NOT poisonable. `is_poisonable` at `include/obj.h:264-268` requires `oc_skill` in `[-P_SHURIKEN, -P_BOW]` = `[-24, -20]`, i.e., ranged ammunition only (arrows, crossbow bolts, darts, shurikens, sling stones). Daggers (skill +1) and spears (skill +17) fail. Reworded to list the actual poisonable ammunition.
- **Confused remove-curse "about half end up blessed, half cursed"**: wrong ratio. `blessorcurse(obj, 2)` at `mkobj.c:1841-1853` gives 1/4 blessed, 1/4 cursed, 1/2 unchanged. Reworded.
- **Confused remove-curse scope**: a *non-blessed* confused scroll only touches worn/wielded items (plus loadstones, active leashes) per `read.c:1549-1552`. The all-inventory branch only fires when the scroll is blessed. Added the distinction.
- **Helm of opposite alignment missing from auto-curse warning**: HELM_OF_OPPOSITE_ALIGNMENT is in the same 90% auto-curse branch at `mkobj.c:1087-1090` and shares the etched/crested/visored/plumed helm appearance pool with helm of caution and helm of telepathy. Added to the list of auto-cursed shop traps.

### Verified
- Unicorn horn dip table at `potion.c:2151-2160`.
- Throwing potions effects at `potion.c:1625-1820`.
- Scroll of destroy armor with no armor worn produces "strange feeling" at `read.c:1324-1339`.
- Armor shuffle pools at `o_init.c:280-287`.
- Helm of brilliance always "crystal helmet"; dunce cap and cornuthaum both "conical hat" — fixed appearances.
- All armor price tiers verified vs `objects.h:686-727, 637-650`.

---

## 2026-05-18 — v2 audit batch 18: Humans/elves (#84), Trappers/lurkers (#85), Iron Bars (#86), What Actually Kills (#87), Bow (#88)

### Humans and elves `@` (#84) — `spoilers/companion.md:8920` — 3 corrections

- **Master of Thieves was "Rogue quest nemesis"** — wrong. Per `dat/Rog-strt.lua:106` he is the Rogue quest *leader* (consistent with monsters.h:3559-3568 placing him in the quest-leaders section), and per `dat/Tou-goal.lua:117` plus the `monsters.h:3564` comment "Master of Thieves is also the Tourist's nemesis," he is the Tourist quest *nemesis*. Updated to "Rogue quest leader; also Tourist quest nemesis."
- **Master Assassin was "Rogue quest nemesis backup"** — wrong. `dat/Rog-goal.lua:72` names him as the *primary* Rogue quest nemesis. Dropped "backup."
- **Wizard of Yendor row missing** — promised in the section intro and flagged in audit #17's close calls, never added. Inserted between Medusa and Croesus per source order at `monsters.h:2847-2858`: bright-magenta, L30 Spd12 AC-8 MR100, claw 2d12 steal-amulet + spell, flies/regenerates/sees-invis/fire-res/poison-res, covetous, the final boss.

### Trappers and lurkers `t` (#85) — `spoilers/companion.md:8325` — 0 corrections, badge added

Stats verified vs `monsters.h:981-998`. AD_WRAP + AD_PHYS (not AD_DGST, per the 5.0 retcon at `monsters.h:973-980`). Both have M1_HIDE; lurker above has M1_FLY so it's a ceiling hider, trapper is a floor hider (`mondata.h:43-45`). Both M2_STALK = follow you up and down stairs (`monflag.h:146`). Engulf escape and farlook tip are accurate.

### Iron Bars (#86) — `spoilers/companion.md:1346` — 3 corrections

- **"Wand of lightning *will* melt bars"** overstated. `zap.c:5349` has `if (damgtype == ZT_LIGHTNING && rn2(10)) break;`, so each beam-tile only dissolves on a 1-in-10 roll (acid has no such gate). Softened to "can melt them too — though only about one zap in ten actually dissolves the bars."
- **"Ordinary stone on the flanks"** geometry wrong. Niche bars sit in a room wall with stone *behind* them, but the flanking tiles are room-wall (not stone). The trivial "pick-axe through the adjacent wall tunnels into the niche from the side" framing didn't match the layout — digging the flank reaches stone, not the niche. Reworded to digging diagonally past the bars, or through the wall to the stone behind and back into the niche.
- **"Scroll of teleportation guaranteed"** overstated. `mklev.c:790-792` skips the scroll on noteleport levels. Reworded to "unless the level is non-teleport, in which case the niche skips it."

### What Actually Kills Adventurers (#87) — `spoilers/companion.md:1737` — 1 correction + 1 agent error caught

- **Scale mails "AC 1 worn"** used the raw `objects.h` `ac` field, inconsistent with the body-armor equipment table (line 7650+) which uses the `+9` AC-bonus convention. Reworded to "+9 AC worn (the best in the body slot)" — matches both the equipment table and the NetHack Wiki convention ("9 base AC" / "+9 base AC", positive integers).
- **Agent flagged confused-genocide line as wrong** ("Valkyrie, Wizard" examples allegedly impossible because `u.umonster` is supposedly the race). FALSE. `u_init.c:991` sets `u.umonster = gu.urole.mnum` (the role's monster index, per the `Role_if(X)` macro at `role.h:247`). Confused genocide kills your role's species — exactly as the original text said. Original kept; audit comment now documents the agent's error so future passes don't repeat it.

Re-verified all DSM dual-property claims against `do_wear.c:810-880`, mount slip 10-14 (`steed.c:354` `rn1(5, 10)`), water demon 1/30 fountain (`fountain.c:247`), bones items cursed 4/5 (`bones.c:290`), mimic stick MC-gated (`uhitm.c:3310, 3324`), rope golem AT_HUGS, all standard top-killer lore.

### Bow (#88) — `spoilers/companion.md:7549` — 0 corrections, badge updated

All 9 rows (arrow/elven/orcish/silver/ya + bow/elven/orcish/yumi) verified clean vs `objects.h:141-154, 395-402`. Yumi `prob=0` correct (Samurai-only via `u_init.c:142-146`; Rangers get plain BOW). Agent flagged gaps — multishot Str/Ranger/Samurai-yumi bonuses at `dothrow.c:58-77`, Longbow of Diana, role skill caps — but per the no-trivia rule these are additions, not corrections, and intentionally not applied.

### Pass-2 queue
88/183 done.

---

## 2026-05-18 — v2 audit batch 19: Dart (#89), The Lay of the Land (#90), Sokoban L4B (#91), Gnomes (#92), Engulfment from Hiding (#93)

### Dart (#89) — `spoilers/companion.md:7598` — 1 correction

Tourist starting dart stack was "~25–60 at +2" — wrong. `u_init.c:150-151` reads `{ DART, 2, WEAPON_CLASS, 21, 40, UNDEF_BLESS }`, so `trquan()` at `u_init.c:1109-1114` yields `21 + rn2(20)` = 21–40. Corrected. Wiki confirms 21–40.

### The Lay of the Land (#90) — `spoilers/companion.md:521` — 5 corrections

- **Sink glyph change (`#` → `{`)**. NetHack 5.0 changed the default sink symbol per `defsym.h:133` and `doc/fixes5-0-0.txt:827` ("change kitchen sink glyph to a white {"). Sink and fountain now share the `{` glyph (white vs. bright blue). The travel/farlook getpos cycle at `getpos.c:1046-1062` matches on the *displayed* symbol, so typing `#` no longer reaches sinks; typing `{` cycles through sinks and fountains together. Map-symbols table at line 564 had `# Sink` row — removed, and merged the fountain row to "Fountain (bright blue) or sink (white)." Sinks section header at line 812 also updated from `#### Sinks \`#\`` to `#### Sinks \`{\``. Confirmed this is the default symset behavior — the IBMgraphics, DECgraphics, RogueLevel symsets either inherit the default `{` or use their own override. Only the legacy IBM symset shows sinks as the same character as fountains (`\xf4`).
- **Trap room vs. teleportation hub conflation**. Companion lumped them into "a teleportation hub of stacked traps." Source has two distinct themed rooms: `themerms.lua:102-114` (Trap room) places one randomly chosen trap type (arrow / dart / falling rock / bear / land mine / sleep gas / rust / anti-magic) across ~30% of the floor; `themerms.lua:265-279` (Teleportation hub) places 2–4 fixed-destination teleporters. Separated in the prose and in the bullet list.
- **Fake Delphi fiction**. Companion described it as a room with "a non-Oracle pretending to be one" and a "don't pay for advice" warning. `themerms.lua:291-305` contains **zero monsters** — it's purely a geometric joke: an outer ordinary room with an inner empty 3×3 room laid out like the Oracle's chamber. Rewrote.
- **Light source room narrowed**. "Lit candle, lantern, or lamp. Free torches." Source at `themerms.lua:205-210` places exactly **a lit oil lamp**, nothing else. Reworded to "a lit oil lamp. Free torch."
- **Wraith corpse misattribution**. The Massacre/Mausoleum bullet read "Old corpses sometimes carry surprises (a wraith corpse for the level boost is the famous one)." Neither room generates wraith corpses. `themerms.lua:173-188` (Massacre) lists only player-role corpses (apprentice, ninja, valkyrie, etc., from a 27-element role table); `themerms.lua:420-443` (Mausoleum) places an M/V/L/Z monster (mummy, vampire, lich, or zombie) or a human `@` corpse, with a 20% chance of a secret door. Dropped the wraith claim and split Massacre and Mausoleum into separate bullets with accurate contents.

### Sokoban L4B (#91) — `spoilers/companion.md:6579` — 0 corrections

Full 28-step solution simulated against `dat/soko1-2.lua` (note: lua "soko1" = player's Level 4; lua "soko4" = player's Level 1). All three intermediate map states reproduce exactly; final remainder of {O at (13,7), S at (13,8)} matches the closing sentence. Geometry, boulder/hole positions, prize odds (25% BoH / 75% AoR at lua:104-111), hardfloor, noteleport, and no-diagonal-push (`hack.c:441-448`) all verified.

### Gnomes `G` (#92) — `spoilers/companion.md:8575` — 0 corrections

All 22 cells / 4 rows verified vs `monsters.h:1681-1709`. S_GNOME has exactly four entries; no "deep gnome" in 5.0 (correctly omitted). Race peacefulness via `race_peaceful` at `makemon.c:2283` with `MH_GNOME` lovemask confirmed. Gnome lord is the most common Mines gnome (frequency 2 vs. 1 for the others). Drive-by fix from v1 audit (`spell spell` → `cast spell` for gnomish wizard) still correct.

### Engulfment from Hiding (#93) — `spoilers/companion.md:2149` — 0 corrections

Section consistent with the v2 #85 bestiary audit of trappers/lurkers. AD_WRAP+AD_PHYS, M1_HIDE+M1_FLY ceiling-hider lurker / floor-hider trapper, search/telepathy/warning defenses, weapons-still-work-while-swallowed (`uhitm.c:781,805` `mhit = (tmp > dieroll || u.uswallow)`) all verified. 0 corrections.

### Pass-2 queue
93/183 done.

---

## 2026-05-18 — v2 audit batch 20: The Armory (#94), Mimics (#95), Making Friends (#96), Ogres (#97), Rust monsters/disenchanters (#98)

### The Armory (#94) — `spoilers/companion.md:4074` — 3 corrections

- **Drain resistance "only non-artifact source"** wrong. The shield of drain resistance (`objects.h:656-658`, new in 5.0) is the second non-artifact source. Reworded to "one of two non-artifact sources, alongside the shield of drain resistance." The drain-life chapter already names both sources; this section was the outlier.
- **Warning glyph colors** wrong. Companion said "yellow for moderate, red for deadly." Actual color table at `drawing.c:39-52` has six warning levels: white, red, red, red, magenta, bright-magenta. There is no yellow. Reworded to "white for the least threat, through red, with magenta for the worst."
- **Column labels misleading**. "Best mundane options / Best magical options" — most "mundane" picks (cloak of protection, helm of caution, gauntlets of power, speed boots, shield of reflection) are actually magical (oc_magic=1 in objects.h); the "magical" column's small shield is mundane. Relabeled to "Primary pick / Specialty pick" which honestly describes the use-intent split.

Re-verified: MC formula at `uhitm.c:87` (`negated = !(rn2(10) >= 3 * armpro)` → MC3 = 90% block), helm of caution warning intrinsic at `do_wear.c:448-450`, DSM dual-property pattern across `do_wear.c:806-883` (gray and silver intentionally single-property), DSM scroll transformation at `read.c:1225` (`s >= 0`), small shield as only no-penalty shield at `spell.c:2269`. Base AC 10 from `mons[PM_HUMAN].ac`.

### Mimics `m` (#95) — `spoilers/companion.md:8199` — 0 corrections, badge updated

All 3 rows (small/large/giant) verified clean against `monsters.h:670-698`. AD_STCK on large and giant only (correct in the table); MC-block at `uhitm.c:3310, 3324` consistent with batch 18 v2 #87. M1_AMORPHOUS | M1_HIDE | MR_ACID class trait verified.

### Making Friends (#96) — `spoilers/companion.md:2437` — 2 corrections

- **"You have a sad feeling for a moment" misattributed**. Companion claimed the message fires when you change levels without your pet adjacent ("Your pet is still alive on the previous level"). Actually that case produces **no message** — the pet just isn't with you on the new level, and loyalty decays at 1 per 150 moves apart (`dog.c:689-697`). The sad-feeling message at `mon.c:952` (`mtmp->mtame && !canseemon`, printed at `mon.c:3101` / `mon.c:3495`) fires when a tame pet **dies offscreen**. This was a real beginner trap — a reader hearing the message and thinking the pet was still alive would go back for a corpse. Separated the two cases in the prose. Note: the "What Actually Kills" message table at line 1606 already had this right.
- **Confused taming radius "5×5"** wrong. `read.c:1689` sets `bd = confused ? 5 : 1`, with the loop spanning `[-bd..bd]` so the area is `(2*bd+1)²`. Normal = 3×3 (correct in the prose), confused = 11×11 (not 5×5). Corrected.

Re-verified pet-curse-avoidance (`dogmove.c:535-538, 1235-1238`), tameness-loss exclusivity to player-initiated abuse, starvation-feral at `dog.c:706-708`, scroll-of-taming and charm-monster routing through the same `seffect_taming` (`read.c:2236-2238`), taming exclusion list at `dog.c:1163-1166, 1244-1247, 1250`, pet revival prayer at `pray.c:2335-2337` calling `pray_revive` at `pray.c:2176`, pet corpse intrinsic absorption at `mon.c:1763-1777`.

### Ogres `O` (#97) — `spoilers/companion.md:8703` — 0 corrections, badge updated

All 3 rows verified clean against `monsters.h:2052-2075`. M2_COLLECT (weapon pickup) verified on all three; MZ_LARGE confirmed. Prior v1 fix (removing "ogre kings throw boulders" — ogres lack M2_ROCKTHROW) holds.

### Rust monsters and disenchanters `R` (#98) — `spoilers/companion.md:8762` — 0 corrections, badge updated

Both rows verified clean against `monsters.h:2147-2161`. AD_RUST erodes iron armor via `uhitm.c:2311 erode_armor`; non-iron weapons (silver, mithril, copper, wood) immune per `is_rustprone` = `oc_material == IRON` at `objclass.h:200`. Disenchanter G_HELL (Gehennom-only generation), AC -10 hard to hit, active claw drains armor at `uhitm.c:3611-3644`, passive drains weapon at `uhitm.c:5992-6011`. Note: disenchanter uses AD_ENCH, not AD_DREN (which is level-drain on vampires etc.) — the prompt-author confused these but the spoiler correctly uses neither.

### Pass-2 queue
98/183 done.

---

## 2026-05-18 — v2 audit batch 21: Orcs (#99), Rodents (#100), Snakes (#101), Blobs (#102), Zombies (#103)

### Rodents `r` (#100) — `spoilers/companion.md:8299` — 1 correction

Rock mole row had only "tunnels." in Notes. Added "eats metal. Will chew through your bag of gold or unattended weapons." Rock mole is `M1_METALLIVORE` per `mondata.c:561`, and `hack.c:769-784` is the swallow-metal-object branch. The other places in the book that mention metallivores (Iron Bars in v2 #86, niche-cracker tactics) reference rock moles, but the bestiary row itself was the one place a beginner would look it up and learn nothing. Clears the no-trivia bar (real beginner risk to inventory).

### Orcs `o` (#99) — `spoilers/companion.md:8242` — 0 corrections, badge updated

All 8 rows verified clean against `monsters.h:727-796`. Mordor orc speed 5 is correct for 5.0. Agent flagged plain "orc" having `G_NOGEN | M2_NOPOLY` (corpse-only) as a "why don't I see red `o`s" puzzle, but per the no-trivia rule it doesn't change a beginner's strategic decisions — not noted.

### Snakes `S` (#101) — `spoilers/companion.md:8784` — 0 corrections, badge updated

All 6 rows verified against `monsters.h:2167-2221`. M1_SWIM universal; M1_CONCEAL on all except python; python's AT_HUGS pair (WRAP + PHYS) renders correctly.

### Blobs `b` (#102) — `spoilers/companion.md:7997` — 0 corrections, badge updated

All 3 rows verified against `monsters.h:137-166`. Acid blob passive at `uhitm.c:5906-5933` (50% splash + 1/30 corrode armor + 1/6 weapon/glove erode via `passive_obj`); gelatinous cube paralysis at `uhitm.c:6019-6064` (2/3 rate, free-action blocks). Note: 5.0 gelatinous cube is AT_TUCH only (no AT_ENGL — older versions had engulf, 5.0 doesn't).

### Zombies `Z` (#103) — `spoilers/companion.md:8902` — 0 corrections, badge updated

All 10 rows verified against `monsters.h:2421-2504`. All carry `G_NOCORPSE` (the prior audit's intro rewrite remains correct). Class flag is `M2_UNDEAD` (not "M3_UNDEAD"). `M2_STALK` is universal. Agent flagged that elf and human zombie rows omit cold/sleep/poison-res in Notes despite the MR masks at `monsters.h:2457, 2466` — per no-trivia this is a stat-detail inconsistency that doesn't affect beginner decisions (slow undead die fast enough that resistances rarely matter).

### Pass-2 queue
103/183 done.

---

## 2026-05-18 — v2 audit batch 22: Pick-axe (#104), Shopping (#105), Curses (#106), Arachnids (#107), Dagger (#108)

### Shopping and Shopkeeper Pricing (#105) — `spoilers/companion.md:7030` — 3 corrections

- **"Shop walls are non-diggable from inside"** wrong. `dig.c:488-501` converts shop walls to doors normally; the shopkeeper bills you for `SHOP_WALL_DMG` and the chase continues (`shk.c:5061-5078 shopdig` grabs your pack). Reworded to "Digging through a shop wall or floor doesn't escape the bill."
- **Touchstone identification** had two errors. (1) Full-name identification requires a **blessed** touchstone (or non-cursed for Archeologist/Gnome) per `apply.c:2744-2751`; an uncursed touchstone only gives a streak color (line 2759). (2) Hardness is irrelevant — touchstones work on all gems. Reworded accordingly.
- **Glass row sells for "0–8 zm"** wrong. The unidentified-gem formula at `shk.c:3168-3172` is `(tmp + 3) * quan` with `tmp = 0..(divisor-1)`, so the minimum is 3 zm, not 0. Corrected to "3–8 zm."

Re-verified: credit/debit/loan ordering (`shk.c:3884-3909`), shop door blocked iff `debit || billct || robbed` (`shk.c:5791-5815`), shopkeeper-ignores-Elbereth (`monmove.c:251-268`), shopkeeper-sees-invisible (`shk.c:5302-5303`), bones-shop reset (`bones.c:51-99`), all 22 gem prices and Mohs hardness against `objects.h:1526-1571`.

### Dagger (#108) — `spoilers/companion.md:7280` — 1 correction

Silver dagger row said "Silver damage to demons, undead, lycanthropes, and shades" — "undead" is too broad. `mon_hates_silver()` at `mondata.c:524-528` covers weres, `S_VAMPIRE`, demons, shades, and imps (except tengu). Other undead — liches, zombies, mummies, wraiths, ghouls, ghosts — are NOT silver-vulnerable. Reworded to "demons, vampires, lycanthropes, shades, and imps."

Re-verified all 5 rows against `objects.h:200-214`. Daggers correctly NOT claimed poisonable (`oc_skill = +1`, outside `is_poisonable` range). Sting at `artilist.h:138`. Rogue Expert multishot to 4 at `dothrow.c:65-66, 178-190`. Athame no-dull engraving at `engrave.c:1306-1307`.

### Pick-axe (#104) — `spoilers/companion.md:7395` — 0 corrections, badge updated

Stats verified against `objects.h:1007-1009` (pick-axe) and `:345-347` (mattock). Mattock bimanual 3/2 Str damage bonus at `uhitm.c:1467-1468`. Dig-down creates pit first then deepens to hole at `dig.c:432-433, 372-374`.

### Curses and How to Break Them (#106) — `spoilers/companion.md:5227` — 0 corrections, badge updated

Re-verified: bones 80% cursed (`bones.c:290`), rings of teleportation/polymorph and amulet of strangulation 90% cursed (`mkobj.c:1063-1066, 1143-1147`), cursed BoH weight doubling (`mkobj.c:1950-1953`), holy water uncursing by dipping (`potion.c:1514-1518`), confused remove-curse 25/25/50 split (consistent with batch 17 v2 #83), blessed-vs-uncursed remove-curse scope (`read.c:1524, 1549`), prayer top-tier reward uncursing all inventory (`pray.c:1283-1308`).

### Arachnids and centipedes `s` (#107) — `spoilers/companion.md:8320` — 0 corrections, badge updated

All 5 rows verified against `monsters.h:940-972, 3713-3722`. Webmaker via `mondata.h:147-148` on cave spider + giant spider only. M1_CONCEAL on all except giant spider. Cave spider/centipede corpses safe (no M1_POIS); giant spider/scorpion poisonous. Scorpius `MR_STONE` confers ston-res.

### Pass-2 queue
108/183 done.

---

## 2026-05-18 — v2 audit batch 23: Golems (#109), Attack Wands (#110), Atheist (#111), Zruties (#112), Angelic beings (#113)

### Golems `'` (#109) — `spoilers/companion.md:9063` — 1 correction

Iron golem row had "poisonous-corpse" — wrong. Iron golem carries `G_NOCORPSE` at `monsters.h:2587`, so the M1_POIS flag never produces an eatable corpse. Same v2 pattern as the manes/lemure catch in earlier batches. Changed to "no corpse." Cross-section consistency check: agent flagged that `poly_when_stoned` at `mondata.c:80-85` covers ALL golems except stone (broader than the batch-17 paraphrase suggested), but the spoiler's stoning chapter (audit #172 v2 #50) and polymorph-conduct section (audit #161 v2 #20) both already describe the mechanic correctly — no cross-section fix needed.

Re-verified all 11 rows against `monsters.h:2509-2594`. Clay golem dies on cancellation (`zap.c:3201-3212`); iron golem one-shotted by rust (`uhitm.c:2289, 2316 completelyrusts`). Both interesting but skipped per no-trivia rule.

### Attack Wands and the Warning Shot (#110) — `spoilers/companion.md:2011` — 0 corrections, badge updated

Re-verified `mwandexp` mechanic at `muse.c:1830-1860`: `buzz_force_miss` on first wand zap, flag set TRUE after. Six wands (death/sleep/fire/cold/lightning/magic missile) in the buzzfn dispatch at `muse.c:1842-1847` match the spoiler list. Late-game zone list at `makemon.c:1291-1293` (Stronghold || Knox || endgame || hell || V_tower || quest) matches exactly. The wand-identifies-on-visibility claim correct (`muse.c:1839, 1849-1850 canseemon`).

### Atheist (#111) — `spoilers/companion.md:6785` — 0 corrections, badge updated

All 5 conduct-breaking sites in source verified: `#pray` (`pray.c:2221`), `#offer` corpse (`pray.c:1977`), `#turn` undead (`pray.c:2426`, Knights/Priests only), `#chat` with priest (`priest.c:572`), altar-drop (`do.c:370`). Final Amulet offering exempt (`pray.c:1529-1588` `offer_real_amulet` has no gnostic write).

### Zruties `z` (#112) — `spoilers/companion.md:8445` — 0 corrections, badge updated

Single-row table re-verified vs `monsters.h:1192-1202`. M1_HUMANOID + M2_STRONG, no special abilities beyond raw 3-attack damage.

### Angelic beings `A` (#113) — `spoilers/companion.md:8457` — 0 corrections, badge updated

All 5 rows re-verified vs `monsters.h:1206-1265`. M1_FLY on all except Aleax, M1_SEE_INVIS on all except couatl (correctly reflected in prose), M2_STALK universal. AD_MAGM ("magic", Angel) vs AD_SPEL ("spell", ki-rin/Archon) labels correctly distinguished.

### Pass-2 queue
113/183 done.

---

## 2026-05-18 — v2 audit batch 24: Combining Conducts (#114), Acknowledgements (#115), Gremlins (#116), Ascension Kit (#117), Sokoban-conduct (#118)

### Combining Conducts (#114) — `spoilers/companion.md:6917` — 1 correction

Summary line misclassified two of the five new-in-5.0 conducts. The corrected split is:
- **Pauper, Permadeaf, Bonesless**: start-of-game options (`optlist.h:213-215` for `bones`, `:268` for `permadeaf`, `:559` for `pauper`).
- **Sokoban**: tracked from in-game actions.
- **Petless**: not a settable option at all. `u.uconduct.pets++` at `dog.c:87` is unconditional, and the comment at `dog.c:77-79` notes the starting pet is created before `in_moveloop` but still bumps the counter. The only way to have `!u.uconduct.pets` is to start without a pet, which requires Pauper (`u_init.c:1308-1309` early-return suppresses the starting pet). So Petless is effectively a Pauper sub-conduct.

The book had Pauper/Petless/Permadeaf as "start-of-game options" and Sokoban/Bonesless as "tracked automatically" — the right partition flips both Petless and Bonesless.

### Acknowledgements (#115) — `spoilers/companion.md:9334` — 2 corrections

- **WCST "(originally the 'World's Encyclopaedia of NetHack')"** parenthetical was never verifiable. The WCST source file at pdwaterman.com doesn't expand the acronym, and Waterman's Wheaton, Illinois distribution address strongly suggests "WC" stands for Wheaton College. User confirmed; replaced with "(distributed from Wheaton, Illinois starting in 1991)" which matches the verifiable WCST v7.00 contact line.
- **Kevin Hugo missing from current-team list** at line 9478. `dat/history:314` lists him on the 5.0 core team, and the book already credits him above as a 3.2.2 spoiler author. Added between Collet and Kallinen.

Re-verified: 1987 NetHack origin via Stephenson's 1.4 (`dat/history:25-26`), Fenlason→Brouwer→Stephenson lineage, 3.4.3 December 2003 (`dat/history:193`), twelve-year hiatus to 3.6.0 in December 2015, Izchak Miller "founding member" who died between 3.1.3 and 3.2.0 (1994 by community consensus, not in bundled docs), Rogue 1980 by Toy/Wichman, NAO operators Streib + Kallinen (`dat/history:344-346`).

### Ascension Kit (#117) — `spoilers/companion.md:5783` — 2 corrections

- **Mitre of Holiness "fire resistance + see invisible"** wrong. Per `artilist.h:265-269`, Mitre is a `HELM_OF_BRILLIANCE` base with `CARY(AD_FIRE)` (fire resistance), `SPFX_PROTECT` (+1 protection), `M2_UNDEAD` bonus (×2 vs undead), `ENERGY_BOOST` invoke. No see invisible. The artifact-table line at 4386 already had this right. Reworded to "a helm of brilliance that adds fire resistance, +1 protection, and an energy-boost invoke."
- **"An ascended Monk wore the Eye of the Aethiopica"** wrong. Eye of the Aethiopica is `PM_WIZARD`-restricted with `SPFX_RESTR` at `artilist.h:303-307`. A Monk picking it up triggers the badclass blast at `artifact.c:920-948`. Reworded to "Wizards who survive to their quest can wear the Eye of the Aethiopica instead."

Re-verified: Gray DSM = MR, Silver = reflection, Blue = shock (`objects.h:502, 507, 521`); speed boots = FAST; gauntlets of power lock Str 25 (`attrib.c:1214, 1278`); choking-through-slow-digestion at SATIATED (`eat.c:248`). Wand of death on the High Priest verified clean (`zap.c:4314` sets `type = -1` to skip saving throws; High Priest has no antimagic gear or covered intrinsic).

### Gremlins `g` (#116) — `spoilers/companion.md:8109` — 0 corrections, badge updated

All 3 rows re-verified vs `monsters.h:448-473`. Water/fountain split (`mon.c:987-992`, 2/3) vs. night AD_CURS (`uhitm.c:3037-3058`) correctly distinguished by v2 #152.

### Sokoban-conduct (#118) — `spoilers/companion.md:7002` — 0 corrections, badge updated

All five guilt-triggering sites verified: squeeze (`hack.c:299, 307`), wand-of-striking fracture (`zap.c:5556`), polymorph boulder (`zap.c:1711`), scroll of earth (`read.c:1951`), dismount onto boulder (`steed.c:767`). Conduct reported only if branch was entered (`insight.c:2216 sokoban_in_play`).

### Pass-2 queue
118/183 done.

---

## 2026-05-19 — v2 audit batch 25: No Genocide (#119), Wishes (#120), The Castle (#121), Permadeaf (#122), Apelike (#123)

### No Genocide (#119) — `spoilers/companion.md:6848` — 1 correction (real)

The book said: "sitting on **Vlad's throne**, which has one outcome that prompts you to genocide a **class**." Both halves wrong:
- Not Vlad's throne. Genocide is case 8 of `throne_sit_effect` at `sit.c:125-132`, the **regular** throne switch. Vlad's tower thrones take the early-return at `sit.c:63-66` into `special_throne_effect`, which has no genocide case.
- Not a class. The throne calls `do_genocide(5)` (REALLY|ONTHRONE) — a single-**species** prompt. Class genocide only comes from a blessed scroll via `do_class_genocide()`.

Reworded to "sitting on a throne" + "single species" + "case 8 of 13." Also updated the "ascend without genociding" line that mentioned "never sit Vlad's throne" to "never roll case 8 on a throne."

### Wishes and Wishing (#120) — `spoilers/companion.md:5005, 5081` — 0 prose corrections, badge updated

Re-verified all wish sources: Vlad's throne 4/13 wish rate (`sit.c:241-256`); Amulet pickup wish (`allmain.c:446-451`, `u.uhave.amulet && !u.uevent.amulet_wish`); magic lamp 1/3 emergence × 80% wish-blessed ≈ 27% (`apply.c:1817 !rn2(3)` × `potion.c:2833-2845` blessed=case 0); smoky potion `POTION_OCCUPANT_CHANCE` base 1-in-13 (`hack.h:1409`); fountain ~1/30 demon × 15/100 shallow-floor wish ≈ 1/200 (`fountain.c:78, 314`); Orcus Town magic lamp OR marker guaranteed (`dat/orcus.lua:107-111`). Bare-wish BUC random (`mkobj.c:1846-1851 blessorcurse(otmp,10)` = 1/10 × 1/2 each direction = ~5%/5%/90%); the v1 audit comment had this as ~10%/10%/80% — corrected the statistic in the comment. Artifact denial probabilistic (`objnam.c:5374`), quest artifacts absolutely blocked, `wisharti` counter increments either way. Five mundane substitutions exact (`objnam.c:5003-5018`).

### The Castle (#121) — `spoilers/companion.md:1183` — 1 correction

Brief Castle entry had "A maze section to each side may contain minotaurs" — fabricated. `castle.lua` has no minotaurs and no internal maze rooms; the `des.mazewalk` calls at lines 223-224 fill entry-approach corridors *outside* the walls. Same error already corrected in the full Castle section at line 5454 (v1 #109). Dropped from the brief entry too.

### Permadeaf (#122) — `spoilers/companion.md:6981` — 1 correction + 1 beginner-relevant addition

- **`-Dpermadeaf` command-line claim** wrong. `-D` is the debug/wizard-mode flag (`sys/unix/unixmain.c:359-365`: `wizard = TRUE, discover = FALSE`). It does not accept option names. There is no `-Dpermadeaf` syntax. Dropped the command-line clause; rcfile (`OPTIONS=permadeaf`) is the path.
- **Added shrieker note** (per agent's "saves a beginner's life" framing under the no-trivia rule). When Deaf, only the *messages* are suppressed. A shrieker still calls `makemon` and `aggravate()` even when Deaf (`mon.c:4089-4106 m_respond_shrieker`: only the `pline` shriek-message is gated on `!Deaf`; the spawn-and-aggravate run unconditionally). A Permadeaf player who steps next to a shrieker gets the consequences without the warning. Added a paragraph naming this trap.

### Apelike creatures `Y` (#123) — `spoilers/companion.md:8893` — 0 corrections, badge updated

All 6 rows re-verified vs `monsters.h:2372-2417`. monkey AD_SITM, ape AT_BITE third attack (no AT_HUGS), owlbear AT_HUGS 2d8, yeti MR_COLD, carnivorous ape AT_HUGS, sasquatch AT_KICK + M1_SEE_INVIS. All match.

### Pass-2 queue
123/183 done.

---

## 2026-05-19 — v2 audit batch 26: Wraiths (#124), Worms (#125), Hammer (#126), Ascension Run (#127), Humanoids (#128)

### Ascension Run (#127) — `spoilers/companion.md:5838` — 1 correction

Mysterious Force paragraph had two related errors:
- **"dropped back down one to three levels"** overstates the per-alignment max. Per `do.c:1544` `odds = 3 + ualign.type` and `diff = rn2(odds)`: Chaotics (`odds=2`) max -1; Neutrals (`odds=3`) max -2; only Lawfuls (`odds=4`) reach -3.
- **"A smaller chance just teleports you elsewhere on the same level"** inverts the distribution. Same-level (diff==0) is the *majority* outcome among triggers — 50% for Lawful/Chaotic, 33% for Neutral; only Lawfuls have the -3 tail.

Reworded to: "Often it just shuffles you elsewhere on the same level; sometimes it drops you down a level (Chaotic max), two (Neutral max), or even three (Lawfuls only)." Also dropped the backtick around `Inhell` — was a C-identifier leak; now reads "a hard Gehennom gate."

Re-verified all other claims: Amulet pickup wish (`allmain.c:446-451`), Wizard respawn (`wizard.c:721-757`), Amulet blocks level teleport (`teleport.c:1185-1189`), covetous warp (`wizard.c:274+`), bottom-four-levels exclusion (`do.c:1541` `dunlev < dunlevs_in_dungeon - 3`), Elbereth dead in Gehennom and endgame (`teleport.c:68-70`).

### Wraiths `W` (#124) — `spoilers/companion.md:8865` — 0 corrections, badge updated

All 3 rows re-verified vs `monsters.h:2326-2353`. Only plain wraith leaves an eatable corpse (barrow wight + Nazgul both G_NOCORPSE). Wraith corpse pluslvl at `eat.c:1141-1142`.

### Worms `w` (#125) — `spoilers/companion.md:8405` — 0 corrections, badge updated

All 4 rows re-verified vs `monsters.h:1114-1145`. Worm tooth drop only fires for `PM_LONG_WORM` (not baby long worm) per `mon.c:619` — spoiler row placement correct.

### Hammer (#126) — `spoilers/companion.md:7463` — 0 corrections, badge updated

War hammer 1d4+1/1d4 verified against `objects.h:367-369` ("`+1 small`" comment). Mjollnir Valkyrie role-lock + alignment-fixup verified at `artilist.h:109-112` + `artifact.c:86-95`. Aklys correctly excluded (uses P_CLUB, not P_HAMMER).

### Humanoids `h` (#128) — `spoilers/companion.md:8131` — 0 corrections, badge updated

All 7 rows re-verified vs `monsters.h:477-540`. Helmet-blocks-7/8 of mind flayer tentacles confirmed at `uhitm.c:3235` (`uarmh && rn2(8)`). Bugbear is AT_WEAP only (no bite — spoiler correctly omits).

### Pass-2 queue
128/183 done.

---

## 2026-05-19 — v2 audit batch 27: Pauper (#129), Umber hulks (#130), Dogs (#131), Brainlessness (#132), Luck and Fortune (#133)

### Pauper (#129) — `spoilers/companion.md:6949` — 1 correction (+ Bonesless drive-by)

"Rcfile or command line only" was wrong. `pauper` is `set_in_config` at `optlist.h:559`, which means rcfile or `NETHACKOPTIONS` env. Unix command-line option parsing in `unixmain.c:343-426` has no generic `-pauper` handler (same mistake the Permadeaf v2 #122 audit caught for `-Dpermadeaf`). Reworded both Pauper and Bonesless sections — same wording appeared in both.

### Umber hulks `U` (#130) — `spoilers/companion.md:8836` — 1 correction

"The confusion stacks and makes spellcasting impossible" was wrong. Per `spell.c:687-708` `rejectcasting()`, only **Stunned** blocks casting, not Confused. Confusion garbles spellbook study (`spell.c:368, 620`) and worsens spell forgetting when zapped (`spell.c:1778-1782`), but you can still cast confused. Reworded to "wrecks navigation, and confused spellbook study garbles the spell."

### Luck and Fortune (#133) — `spoilers/companion.md:5305` — 4 corrections

- **Killing your quest leader** row said "-4 to baseline luck" but missed the immediate `change_luck(-20)` (floored at LUCKMIN=-10) and `u.ugangr += 7` from `mon.c:3680`. Expanded the row.
- **"Attacking your pet -1"** mislabeled. `mon.c:3664` fires on *killing* a tame monster, not each attack. Also -15 alignment via `adjalign` at `mon.c:3704`. Changed to "Killing your pet."
- **"Breaking a mirror or crystal -2"** — only mirror has the luck hook (`uhitm.c:1133`, `dothrow.c:2496`, `dokick.c:445, 1724`). Crystal balls and crystal armor have no luck penalty for breaking. Dropped "or crystal."
- **"Archeologists begin with all gems identified, which is why their class description mentions 'unicorn negotiation'"** was fabricated. `u_init.c:903` sets TOUCHSTONE knowledge only; the touchstone tool (`u_init.c:50`) lets Archeologists *verify* a gem is real before throwing, but gems themselves aren't pre-identified. The "unicorn negotiation" class-description quote doesn't exist anywhere in source or wiki. Reworded to the actual touchstone mechanic.

Re-verified: Luck range ±10 base / ±13 with luckstone, 600-turn drift (300 with Amulet/u.ugangr>0), full-moon/Friday baselines, set_moreluck ±3 to non-cursed luckstones, identified-gem +5 / +2 / +1 / -3..+3 / -1..+1 unicorn matrix, Sokoban cheat -1 each, prayer fails on any negative Luck, sacrifice cap at corpse difficulty, Heart of Ahriman / Tsurugi / Orb of Fate luck conferral.

### Dogs and canines `d` (#131) — `spoilers/companion.md:8044` — 0 corrections, badge updated

All 16 rows + intro re-verified vs `monsters.h:199-320`. werejackal/werewolf S_DOG vs S_HUMAN are intentionally separate (shape-change machinery, per the source comment at monsters.h:264-266).

### Brainlessness (#132) — `spoilers/companion.md:2062` — 0 corrections, badge updated

Re-verified all mind-flayer mechanics: 3 vs 5 tentacles, 2d1 drain-Int per tentacle (max 10/turn on master), 1-in-5 `losespells()` per hit, brainlessness death at `eat.c:698-715`, restore ability/prayer recovery, unicorn horn no longer restoring stats.

### Pass-2 queue
133/183 done.

---

## 2026-05-19 — v2 audit batch 28: Gehennom (#134), Lance (#135), Gray Stones (#136), Keystone Kops (#137), Rings/Amulets (#138)

### Gehennom (#134) — `spoilers/companion.md:5540` — 4 corrections

- **Asmodeus "carries a wand of cold"** — actually wands of cold AND fire (`makemon.c:804-807`).
- **Asmodeus "cold- and poison-resistant"** — also fire-resistant (`MR_FIRE | MR_COLD | MR_POISON` at `monsters.h:3124`). Updated to "fire-, cold-, and poison-resistant."
- **Baalzebub "surrounded by a poison-gas cloud, summons swarms of flies"** was fabricated. Per `monsters.h:3110-3119`, his attacks are AT_BITE/AD_DRST (poisonous bite, drains Str) and AT_GAZE/AD_STUN. No gas cloud, no fly summons. The "Lord of the Flies" name + beetle-shaped lair are real (`mkmaze.c:471 baalz_fixup`). Reworded.
- **Vlad's throne arithmetic** was wrong. Book said "4/13 chance per sit of the wish ending it, so on average you sit ~3 times before the wish (and absorb two of the bad effects)." Per `sit.c:45`, only `rnd(6) > 4` (1/3 of sits) triggers any effect at all; of those, 4/13 are the wish. Unconditional rate is `(1/3) × (4/13) = 4/39 ≈ 10%`, so average ~10 sits with ~7 bad effects absorbed. Reworded.

### Keystone Kops `K` (#137) — `spoilers/companion.md:8651` — 2 corrections

- **Respawn "near up-stairs"** wrong. `mon.c:3148` calls `stairway_find_type_dir(FALSE, FALSE)`; the second `FALSE` is the `up` flag, so it finds **down-stairs** (`stairs.c:89-95`, `mklev.c:2193`).
- **Respawn odds "1-in-5 stairs / 2-in-5 random / 2-in-5 dead"** wrong arithmetic. `mon.c:3151-3164` rolls `rnd(5)` (1..5 uniform): case 1 → stairs (1/5), case 2 → random (1/5), default 3/4/5 → dead (3/5).

### Gray Stones (#136) — `spoilers/companion.md:3104` — 1 correction

"A loadstone auto-curses itself the moment you pick it up" — wrong. Loadstones are cursed at object creation (`mkobj.c:978-979`); the curse is intrinsic from generation, not an event-triggered curse on pickup. Reworded to "Loadstones are cursed when they generate, and a cursed loadstone refuses to be dropped at all."

### Lance (#135) — `spoilers/companion.md:7552` — 0 corrections, badge updated

Joust bonus and shatter chance re-verified vs `objects.h:351-352`, `uhitm.c:1546, 2123-2125`.

### Rings and Amulets (#138) — `spoilers/companion.md:3779` — 0 prose corrections, badge updated

Re-verified all ring prices, auto-curse list, hunger costs, restful-sleep mechanics. The v1 close call about restful sleep being "always cursed per mkobj.c:1065" was itself wrong (90% per `rn2(10)` at `mkobj.c:1063-1066`); the body text "usually cursed" was correct.

### Pass-2 queue
138/183 done.

---

## 2026-05-19 — v2 audit batch 29: Puddings (#139), Sling (#140), Dragons (#141), Scroll Rack (#142), Crossbow (#143)

### The Scroll Rack (#142) — `spoilers/companion.md:3478` — 2 corrections (beginner-saving)

- **Enchant weapon at +6+** was wrong. Companion said "Past +9 the scroll usually does nothing but never destroys the weapon" — but per `wield.c:999-1009 chwepon`, when `uwep->spe > 5` (i.e., +6 or higher) and `amount >= 0`, `rn2(3)` evaluates true 2/3 of the time and destroys the weapon outright. So +6 and above is at 2/3 destruction risk per read. Reworded with "**Safe ceiling: +5**." Real beginner trap.
- **Charging probability table** was off by one. Source formula `n³/7³` at `read.c:746-758`: 1st 0%, 2nd 0.29%, 3rd 2.33%, 4th 7.87%, 5th 18.66%, 6th 36.44%, 7th 62.97%, 8th 100%. Companion wrote "36% on sixth — and on the seventh, always" — missing the 63% seventh-charge step and labeling the always-explode as 7th instead of 8th. Corrected.

### Puddings and oozes (#139) — `spoilers/companion.md:8744` — 1 correction

"Splits when you hit them with an iron or metal melee weapon" implied all four split. Per `uhitm.c:1609-1610`, only `PM_BLACK_PUDDING || PM_BROWN_PUDDING` split. Gray ooze and green slime don't. Reworded the intro to scope the split to brown/black puddings.

### Sling (#140) — `spoilers/companion.md:7615` — 1 correction (long-overdue)

The Notes cell still read "Trains sling skill from any rock you pick up." The v1 audit comment claimed this was corrected, but the prose wasn't actually updated. Picking up rocks doesn't train any skill (training fires on hit while wielding the launcher, `weapon.c:1750-1761`). Replaced with "Launches rocks, flint stones, and gems. Caveman starting weapon."

### Dragons (#141) — `spoilers/companion.md:8524` — 1 correction

Baby blue dragon Notes cell read "Lightning breath, ditto." — wrong. Baby blue dragon has only bite 2d6 (`monsters.h:1408-1415`, no AT_BREA), and the section intro explicitly states "Babies don't breathe." Appears to be a stray editorial placeholder. Cleared the cell.

### Crossbow (#143) — `spoilers/companion.md:7604` — 1 correction

"Valkyries Skilled" was wrong. `u_init.c:525-547` (Skill_V) has no P_CROSSBOW entry; Valkyries cap at Unskilled. The Skilled role is **Knight** (`u_init.c:366`). Corrected.

### Pass-2 queue
143/183 done.

---

## 2026-05-19 — v2 audit batch 30: Genetic Engineer (#144), Two-handed sword (#145), Quantum mechanics (#146), Feelings and Sounds (#147), The Oracle (#148)

All five sections re-audit clean — 0 prose corrections.

- **Genetic Engineer (#144)**: claw + corpse polymorph mechanics, defenses (kill, Antimagic, Unchanging) verified vs mhitm.c:1128-1136, eat.c:1244-1263.
- **Two-handed sword (#145)**: stats vs objects.h:273-285, 3/2 Str bonus formula at uhitm.c:1467-1468 (technically `(3*|dbon|+1)/2` ceiling, but "1.5x" reads correctly for beginner voice).
- **Quantum mechanics (#146)**: both rows speed 12 (not 24 as prompt hint had suggested); AD_TLPT vs AD_POLY correctly distinguished.
- **Feelings and Sounds (#147)**: vault/fountain/oracle/shop sounds, bugle reveille, sad-feeling (a feeling, not gated by Deaf) all verified vs sounds.c.
- **The Oracle (#148)**: DL 5-9, 4 fountains, minor=50, major=500+50×XL, minor consult always rumors.tru, Sokoban entrance upstairs, 8 centaur statues.

### Pass-2 queue
148/183 done.

---

## 2026-05-19 — v2 audit batch 31: Eyes/spheres (#149), Lights (#150), Sokoban L1A (#151), Sokoban L4A (#152), Boomerang (#153)

### Sokoban Level 1, Version A (#151) — `spoilers/companion.md:6172` — 1 correction (v1 regression)

The v1 audit (#30) "corrected" scroll coordinates from (3,12)/(4,12) to (2,12)/(3,12), claiming "column 4 is the ┌ wall character." That was based on a column miscount. Row 12 character-by-character (with the 4-char `12  ` label and col 1 = pos 4 of the line): col 1 = space, col 2 = │ (wall), cols 3-4 = `··` (the two floor squares where scrolls land), col 5 = ┌ (corner), cols 6-13 = `─` (bottom corridor), col 14 = ┘. So scrolls are at companion (3,12) and (4,12), matching `soko4-1.lua:94-95` `des.object("scroll of earth", 02, 11)` and `(03, 11)` under the standard `lua_xy + 1 = spoiler_col,row` mapping. Restored the original v1-incorrect/v0-correct coordinates.

### Eyes and spheres (#149) — `spoilers/companion.md:8077` — 1 correction

Floating eye Notes mentioned "Use ranged, blind yourself, or close eyes first." There's no close-eyes command in NetHack 5.0; the only way to break sight is being Blind (status, or worn blindfold/towel). A beginner could hunt for a non-existent command. Reworded to "Use ranged, or wear a blindfold or towel to break sight."

### Boomerang (#153) — `spoilers/companion.md:7642` — 1 correction (long-overdue)

The Notes cell still read "Returns when thrown. Always." The v1 audit flagged this as false but didn't actually update the prose — same pattern as the Sling fix in batch 29 v2 #140. Per `zap.c:boomhit`, the boomerang flies a 10-step curved path that stops on the first monster, wall, closed door, or sink; catching on return requires a Dex check (auto-fails if Fumbling) and a failed catch hits the thrower. Reworded to "Curves back on a clear path; stops on a monster, wall, door, or sink. Low Dex or Fumbling means you catch it in the face."

### Lights (#150) — `spoilers/companion.md:8443` — 0 corrections, badge updated

Both rows verified vs `monsters.h:1168-1191`. AT_EXPL means the monster dies on attack ("bursts on contact" in prose).

### Sokoban Level 4, Version A (#152) — `spoilers/companion.md:6516` — 0 corrections, badge added

All 19 push steps re-simulated geometrically against `dat/soko1-1.lua`. Intermediate map after step 13 shows exactly 8 holes filled (F, G, H, I, K, L, M, N). Final remainder of 2 boulders (A and E) exact. Prize odds 75% bag of holding / 25% amulet of reflection at lua:102-111. Chamber coordinates (17,12)/(17,14)/(17,16) map to lua (16,11)/(16,13)/(16,15), adjacent to zoo region (18,10,22,16) — "next to the treasure zoo" correct.

### Pass-2 queue
153/183 done.

---

## 2026-05-19 — v2 audit batch 32: Rogue Level (#154), Divine Relations (#155), Centaurs (#156), Wands and Staves (#157), Elemental Planes (#158)

### Divine Relations (#155) — `spoilers/companion.md:4495` — 2 corrections

- **Trouble priority list item 10** ("Blindness, confusion, stunning, hallucination") was misclassified as a major trouble. Per `pray.c:95, 99-101`: `TROUBLE_BLIND=-5`, `STUNNED=-9`, `CONFUSED=-10`, `HALLUCINATION=-11` are all MINOR troubles, addressed by `in_trouble()` only after positive-valued troubles. Same parallel mistake as the v1-demoted Punishment, never applied to this row. Moved these afflictions to the "additional blessings" tier and renumbered the list.
- **Same-race sacrifice "exception"** said it "can convert an altar to your alignment" — wrong. Per `pray.c:1717-1720`, same-race blood always converts a lawful or neutral altar to **chaotic**, not to co-aligned. Only chaotic heroes benefit. On a chaotic altar it summons a demon. Reworded.

### Wands and Staves (#157) — `spoilers/companion.md:3585` — 4 corrections (engrave-test paragraph)

- **Magic missile and death "just write in dust"** — wrong on both. Magic missile prints "The <surface> is riddled by bullet holes!" (`engrave.c:642-648`), a distinctive message. Sleep and death share the same "the bugs on the <surface> stop moving!" message (`engrave.c:651-656`). The price-distinguish hint should be for sleep vs death, not magic missile vs death.
- **"Striking scatters dust around"** — wrong. Actual message is "The wand unsuccessfully fights your attempt to write!" (`engrave.c:602-605`).
- **Slow monster and speed monster** were in the "needs zap testing" group — but they produce distinctive engrave messages ("the bugs on the <surface> slow down" / "speed up" at `engrave.c:606-616`). They belong in step 1.
- Rewrote the engrave-test paragraph to reflect all three.

### The Elemental Planes (#158) — `spoilers/companion.md:5931` — 1 correction

"Wand of teleport on yourself silently fails" was the wrong word. Per `teleport.c:854-855`, scrolltele prints "A mysterious force prevents you from teleporting!" — audible feedback, not silent. Self-zap WAN_TELEPORTATION reaches scrolltele() at line 844 from `zap.c:2876-2878`. Reworded both occurrences to name the actual message in one place and drop "silently" in the other.

### Centaurs (#156) — `spoilers/companion.md:8510` — 2 voice fixes

- "Mounted archers" was wrong — centaurs are half-horse, not riders. Reworded to "Half-horse archers."
- "They wield bows" was too narrow. Per `makemon.c:474-484`, forest centaurs get BOW+arrows but plains and mountain centaurs get CROSSBOW+bolts. Reworded.

### The Rogue Level (#154) — `spoilers/companion.md:1033` — 0 corrections, badge updated

All claims re-verified vs source. Tile mode off across all 4 GUI ports.

### Pass-2 queue
158/183 done.

---

## 2026-05-19 — v2 audit batch 33: Choking (#159), Artifacts (#160), Disintegration (#161), Ants (#162), Light Bursts (#163)

### Artifacts (#160) — `spoilers/companion.md:4210` — 4 corrections

- **Frost Brand / Fire Brand resistance swap.** The book said Frost Brand grants "fire resistance + cold defense" and Fire Brand "cold resistance + fire defense." Per `artilist.h:149-155` and `set_artifact_intrinsic` at `artifact.c:730-736`: Frost Brand `DFNS=COLD` grants COLD resistance; Fire Brand `DFNS=FIRE` grants FIRE resistance. Each defends against its OWN element. Swapped.
- **Grimtooth ×2-vs-elves.** Wrong. `spec_dbon` at `artifact.c:1099-1102` explicitly bypasses `spec_applies` for Grimtooth so the +d6 damage applies to all targets, not just elves. The warning is elf-specific but the damage is universal.
- **Mitre of Holiness "×2 vs undead"** is fictional. Mitre's ATTK is NO_ATTK, so `spec_dbon` at `artifact.c:1095-1098` sets `spec_dbon_applies=FALSE` and no damage bonus is ever applied. The M2_UNDEAD flag only enables `shade_glare` on weapons (`artifact.c:554-571`), not on worn helms. Dropped from the table row and rewrote the prose to name the real benefits.
- **Eye of the Aethiopica "worn or carried" MR.** Wrong. `DFNS(AD_MAGM)` + `NO_CARY` at `artilist.h:303-305` means the MR fires only when worn (an amulet is worn in practice, so this rarely matters strategically — but the prose was inaccurate). The cspfx flags (EREGEN, HSPDAM) work when carried. Reworded.

### Disintegration (#161) — `spoilers/companion.md:2295` — 2 corrections

- **"Reflection ... the bounce often kills it outright"** wrong. Black dragons have MR_DISINT in both attack and defense slots (`monsters.h:1523`); per `resists_disint` at `zap.c:4318` the reflected beam does no damage to them. Reflection protects you but doesn't kill the dragon.
- **"shield of reflection that fails to reflect"** misleading. Shields of reflection don't have a failure mode. The shield-eats-one-breath behavior applies to *ordinary* shields. Reworded.

### Choking (#159) — `spoilers/companion.md:2259` — 2 corrections

- **"Take it off"** was misleading. The amulet of strangulation is 90% cursed at gen (`mkobj.c:1063`), so a beginner trying to remove it usually can't. Replaced with the real escape: pray, or uncurse with holy water / remove curse.
- **"Magic resistance doesn't help (it's a physical attack)"** had a wrong rationale. Strangulation isn't an attack — it's a timer death via `done_timeout(DIED, STRANGLED)`. MR-doesn't-help is true, but the reason is "no attack to resist." Reworded.

### Ants and insects (#162) — `spoilers/companion.md:8007` — 0 corrections, badge updated

All 6 rows re-verified vs `monsters.h:89-133`.

### Light Bursts (#163) — `spoilers/companion.md:2165` — 0 corrections, badge updated

All claims re-verified vs `monsters.h:1169-1191` and `mhitu.c:1623-1650`. Note: warning detects yellow/black lights only at adjacent range, which is also their explosion range — so warning is less helpful in practice than the prose implies, but the prose doesn't overstate.

### Pass-2 queue
163/183 done.

---

## 2026-05-19 — v2 audit batch 34: Quarterstaff (#164), Deadly Poison (#165), Giant humanoids (#166), Riders (#167), Advanced Controls (#168)

### Giant humanoids `H` (#166) — `spoilers/companion.md:8627` — 3 fixes

- **Cyclops "Caveman quest nemesis"** wrong. Per `role.c:154-172`, Cyclops is the **Healer** quest nemesis; Caveman's is the Chromatic Dragon (`role.c:113-131`).
- **Lord Surtur "Has Mjollnir if you don't"** unsupported. `M3_WANTSARTI` targets the player's quest artifact (Orb of Fate for Valkyrie per `role.c:516`), and Mjollnir is a sacrifice gift artifact (`artilist.h:109-112`); no code in makemon/mkobj puts Mjollnir on Surtur. Dropped.
- **Fire giant "Surprisingly poor offensively if you have fire res"** misleading. Fire giant attacks are AD_PHYS (weapon damage), so fire resistance doesn't reduce its melee. Dropped.

### The Riders (#167) — `spoilers/companion.md:2230` — 1 voice fix

"Each hits twice per turn with AT_TUCH 8d8" used a C identifier in beginner-voice prose. Reworded to "a touch attack dealing 8d8 damage."

### Quarterstaff (#164) — `spoilers/companion.md:7490` — 0 corrections, badge updated

Stats vs `objects.h:377-378`, Wizard starter at `u_init.c:168`, bimanual 3/2 Str bonus at `uhitm.c:1467`.

### Deadly Poison (#165) — `spoilers/companion.md:2280` — 0 corrections, badge updated

AD_DRST 1/240 frequency (`rn2(8) × rn2(30)` at `uhitm.c:3154` + `attrib.c:362`); poison resistance grants full immunity; Famine corpse fatal at `eat.c:831-838`.

### Advanced Controls (#168) — `spoilers/companion.md:6034` — 0 corrections, badge updated

All keystrokes, options, and the `verbose`/`autopickup`/`pickup_types` semantics re-verified.

### Pass-2 queue
168/183 done.

---

## 2026-05-19 — v2 audit batch 35: Movement Traps (#169), Elbereth (#170), Major demons (#171), Delayed Deaths (#172), What Changed (#173)

### Major demons `&` (#171) — `spoilers/companion.md:9046` — 3 corrections

Three stings mislabeled as "poison" when the C source has AD_DRST (strength-drain, not generic poison): bone devil (`monsters.h:2999`), Orcus (`:3082`), and Geryon (`:3093`) all have `ATTK(AT_STNG, AD_DRST, 2, 4)`. Same drain-Str pattern as the jellyfish fix in batch 30. Beginner trap: a player armored against poison would NOT be protected against these stings — they'd watch Strength drop during combat. Changed all three to "sting 2d4 drain-Str."

### Delayed Deaths (#172) — `spoilers/companion.md:2322` — 3 corrections

- **Sliming "~9-turn transformation"** off by one. Initial timer is 10 (`make_slimed(10L,...)` at `uhitm.c:3199`, `eat.c:854`); the 9-turn impression came from the t/2 message cadence at `timeout.c:391`. Now consistent with the Puddings section (v2 #139).
- **"polymorph into a flame-bodied or slime-immune form"** overbroad. Per `polyself.c:842-849` the cure requires `flaming()` or `PM_GREEN_SLIME`. Noncorporeal forms (ghost, shade) prevent new infection but don't cure an active timer.
- **"cancellation negates the touch attack"** wrongly listed under Cures. Cancelling at `uhitm.c:3556-3560` prevents future hits but doesn't clear a running timer.

### What Changed Since Last Time (#173) — `spoilers/companion.md:9156` — 3 corrections

- **Touch of death "Magic resistance reduces but no longer fully prevents it"** wrong. Per `mcastu.c:391-407`, the spell is binary — `!Antimagic && rn2(m_lev) > 12` gates the kill; Antimagic in the else branch triggers `shieldeff()` and "Lucky for you, it didn't work!" Antimagic still fully blocks the spell in 5.0; the 5.0 change is the unprotected outcome (instakill → drain+damage per `fixes5-0-0.txt:538`), not the MR semantics. Reworded.
- **Iron bars "since 3.6"** wrong date. Iron bars were added in 3.3.0 per `fixes3-3-0.txt:349`. Corrected to "since 3.3."
- **Gold dragon scale mail "in addition to its two resistances"** wrong. Gold DSM grants only hallucination resistance + innate light (`do_wear.c:846-851`); the DRGN_ARMR slot for gold is 0 (`objects.h:505`). Reworded.

### Movement Traps (#169) — `spoilers/companion.md:1246` — 0 corrections, badge updated

All trapdoor/hole/pit mechanics re-verified.

### Elbereth (#170) — `spoilers/companion.md:1497` — 0 corrections, badge updated

Defile rule, exact-word requirement, S_HUMAN/Rider/Angel/minotaur exclusions, blind/peaceful pass-through, cornered ALLOW_SSM step-through all re-verified.

### Pass-2 queue
173/183 done.

---

## 2026-05-19 — v2 audit batch 36: Points of Interest (#174), Axe (#175), Polearms (#176), Field Guide (#177), Xorns (#178)

### Points of Interest (#174) — `spoilers/companion.md:700` — 4 corrections

- **"Occasionally bless" the dipped fountain item** wrong. Per `fountain.c:464-475`, cases 17-20 = uncurse, not bless. No fountain bless outcome exists.
- **Quaff table treated "Wish granted" and "Water demon" as independent rows** — they're the same case 23 of `rnd(30)` at `fountain.c:314`. Shallow wish odds also overstated: 1/30 is the demon-spawn rate; the wish then requires `rnd(100) > 80 + level_difficulty()` (`fountain.c:78`), so actual shallow wish odds are ~1/150 and zero past DL 20. Merged the rows.
- **Potion-poly sink transform missing "grave"** — `do.c:416-446` case 3 generates a grave. The ring-drop table at line 873 already lists it; the potion-dip row was inconsistent. Added.

### Polearms (#176) — `spoilers/companion.md:7500` — 1 correction

"the attack is treated as bashing (no strength bonus, no weapon-skill bonus)" — wrong on the Strength half. Adjacent polearm at `uhitm.c:1075-1086` clamps damage to rnd(2), but the strength-bonus branch at `uhitm.c:1447-1469` runs regardless; only `use_weapon_skill` is FALSE. Reworded to: "damage clamps to 1d2 base, weapon-skill bonus doesn't apply (Strength still does)."

### A Field Guide to Dungeon Fauna (#177) — `spoilers/companion.md:1636` — 2 corrections

- **`w` Worms "grow tail segments after each hit"** wrong. Per `worm.c:218-237`, long worms grow on a movement-driven timer (`wgrowtime`), not per hit. Reworded to "grow tail segments as they move."
- **`P` Puddings "Use silver, dragonhide, or spells"** misleading. No dragonhide weapons exist in 5.0 (DRAGON_HIDE is body-armor-only). Split gate at `uhitm.c:1616-1618` admits IRON|METAL only, so wooden and silver weapons are the actual non-splitters. Reworded to "Use a silver or wooden weapon, or spells."

### Axe (#175) — `spoilers/companion.md:7407` — 0 corrections, badge added

Stats vs `objects.h:236-241`; battle-axe bimanual 3/2 Str at `uhitm.c:1467-1468`; Cleaver = BATTLE_AXE artifact.

### Xorns (#178) — `spoilers/companion.md:8897` — 0 corrections, badge updated

All claims re-verified. Speed 9, M1_WALLWALK (not M1_TUNNEL), AD_PHYS attacks only (worn gear safe).

### Pass-2 queue
178/183 done.

---

## 2026-05-19 — v2 audit batch 37 (FINAL): Skill Caps (#179), Lizards (#180), Trident (#181), Secret Doors (#182), Liches (#183)

### Trident (#181) — `spoilers/companion.md:7552` — 1 correction

Swimmer bonus labeled "+4 damage / +2" — wrong type. Per `weapon.c:170-176`, the bonus path is inside `hitval()`, not `dmgval()` — it's a **to-hit** bonus, not damage. Reworded.

### Finding Secret Doors (#182) — `spoilers/companion.md:1375` — 1 correction

Excalibur enchantment and lenses don't stack independently. Per `detect.c:2026-2032`, both feed a single `fund` variable that is then capped at +5. So lenses + a +5 Excalibur still gives `fund=5`; lenses only add value if Excalibur's enchantment is below +3. Reworded to make the shared cap explicit.

### Liches `L` (#183) — `spoilers/companion.md:8679` — 1 correction

"The higher tiers can cast touch of death" — wrong; only the arch-lich can. Per `mcastu.c:111`, monster spell selection rolls `rn2(m_lev)` and matches against spell-level thresholds; DEATH_TOUCH is at spell-level 20. Master lich `m_lev=17` means `rn2(17) ≤ 16` — can never reach 20. Only arch-lich (`m_lev=25`) can. The v1 audit caught this and corrected it once; the prose drifted back. Re-corrected.

### Skill Caps (#179) — `spoilers/companion.md:7833` — 0 corrections

All 494 cells exact-match verified: 27 weapon rows + 4 fighting-style rows + 7 spell-school rows × 13 role columns. Cross-section consistent with every other v2 audit that touched skill rows.

### Lizards `:` (#180) — `spoilers/companion.md:9133` — 0 corrections, badge updated

All 8 entries verified vs `monsters.h:3260-3324`. Lizard corpse stoning cure, newt Pw boost, chameleon shape-shifter eat-poly all confirmed.

### Pass-2 queue
**183/183 done — v2 pass complete.**

---
