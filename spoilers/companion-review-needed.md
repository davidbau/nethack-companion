# Companion-audit close calls — needs human review

Items found during the systematic chapter-by-chapter audit that the
auditor (AI) was unable to resolve confidently against C source alone.
Reasons usually fall into one of:

- C says one thing, but community/wiki/lore consensus says another.
  Worth a human judgment about which to spoil.
- Claim depends on a subjective threshold ("often", "rare", "most")
  that has no numeric source code to verify against.
- Multiple readings of the C code are defensible; need a person who
  has played the relevant scenario.
- Sentence is true today but might be a 5.0 change with no commit
  trail (e.g., behaviour adjusted between RC and Release).

Format per entry:

```
## YYYY-MM-DD — audit unit #N (Chapter Name)
### Open question
**Claim** — exact wording from spoiler
**Spoiler line** — companion.md line at audit time
**Source ref** — C file:line or other reference
**What I found** — short summary of the evidence on each side
**Question for human** — the specific judgment needed
```

---

(no entries yet)
