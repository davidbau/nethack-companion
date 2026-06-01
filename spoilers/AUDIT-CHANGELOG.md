# Audit Changelog

Systematic audit of `companion.md` for accuracy (vs NetHack 5.0 source),
community wisdom (NetHackWiki + r/nethack), beginner-friendly language
(in-game voice, no code jargon), and helpful cross-references.

Order is shuffled with seed 42 for reproducibility (`.audit-sections.txt`).
Each batch is committed individually.

## Progress

- Total sections: 272
- Audited: 1
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

**Changes**: rewrote the paragraph (companion.md:8183).
</content>
