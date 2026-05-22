# A Traveler's Companion to the Mazes of Menace

A commemorative spoiler book for **NetHack 5.0**, written to be a
beginner-friendly introduction to the secrets of the dungeon.

**Read it online:**
[https://davidbau.github.io/nethack-companion/](https://davidbau.github.io/nethack-companion/)

The book is `companion.md` — a single Markdown source that builds
to a long-form HTML page and a print-ready PDF. The cover under
`cover/` is also a self-contained vector + PDF set, designed to
(eventually) be printed and bound as a book.

This is a **commemorative edition**, prepared for the launch of
NetHack 5.0 (released in 2025 after the longest stretch of active
development since 3.4.3). Our goal is to make sure that every
claim, every number, and every piece of advice has been audited
against the new 5.0 code. The audit log lives in
`companion-audit.md`.

## In tribute to the WCST tradition

The deepest debt this book owes is to **Paul Waterman's WCST
NetHack Spoilers** (originally the "World's Encyclopaedia of
NetHack") — a single sprawling document that covered the entire
game in a conversational, opinionated voice. Where the
**Hugo/O'Donnell spoilers** (1995–2003, updated 2010) wrote
reference manuals, the WCST was a travel guide: it told you not
just what things did but what to *do* about them. The tone and
structure of this guide are a direct descendant.

Other works that informed specific sections, all credited in the
**Acknowledgements** chapter:

- **David Damerell's** Object Identification FAQ
- **Kieron Dunbar's** wand identification guide (the engrave-test)
- **Trevor Powell's** Instadeath Spoiler
- **Arien Malec's** Medusa guide
- **Matthew Lahut's** prayer guide
- **Boudewijn Waijers'** Sokoban solutions
- **Steven Bush's** spellbook reading tables
- **Gregory Bond's** shopkeeper pricing
- **Dion Nicolaas's** conducts catalog
- **David Goldfarb's** air elemental FAQ
- **Hojita Discordia's** experience-value calculations
- **Kate Nepveu's** steelypips.org archive of all of the above

And the entire **r/nethack**, **RGRN**, and **NetHackWiki**
communities — see the Acknowledgements for the longer list.

No text from any of these works has been copied. Where this book
restates a fact those authors documented, it has been re-verified
against the current 5.0 source. Where it disagrees with older
spoilers, the C code wins.

The effort to ensure the accuracy and wisdom of the advice in the
Companion is ongoing. Once it is good enough, we hope for it to be
worthy of printing as a physical open-source book, to celebrate the
5.0 release.

## Build

```bash
./setup.sh                       # one-time: pull NetHack 5.0 source submodule
spoilers/bootstrap-fonts.sh      # one-time: install EB Garamond + Source Code Pro
spoilers/build.sh                # builds index.html from companion.md (Pandoc)
spoilers/build-latex.sh          # builds book.pdf (XeLaTeX)
python3 spoilers/cover/build-cover.py    # builds the print cover PDF
```

The HTML build needs **Pandoc 3+** and **EB Garamond** installed
locally (the bootstrap script handles it on macOS via Homebrew).
The LaTeX build additionally needs **xelatex** and **luaotfload**.

The appendix builders
(`spoilers/build_armor_appendix.py`,
`spoilers/build_weapons_appendix.py`,
`spoilers/build_bestiary_appendix.py`) read directly from the
NetHack 5.0 C source in `nethack-c/upstream/`. That directory is
a git submodule pinned to the `NetHack-5.0.0_Released` tag;
`./setup.sh` initializes it. The plain HTML and LaTeX pipelines do
not require the submodule — they only need Pandoc (and xelatex
for the LaTeX path).

## Layout

```
README.md                   This file.
LICENSE                     CC BY-SA 4.0.
setup.sh                    Initializes nethack-c/upstream.
index.html                  Root-level Pages redirect → spoilers/.
nethack-c/upstream/         Submodule: NetHack 5.0 C source.

spoilers/
  companion.md              The book.
  index.html                Built HTML (the actual Pages target).
  template.html             Pandoc HTML template + sidebar TOC.
  template.tex              XeLaTeX template.
  style.css                 Web styling.
  latex-filter.lua          Pandoc filter for the LaTeX path.

  build.sh                  HTML build.
  build-latex.sh            PDF build.
  bootstrap-fonts.sh        One-shot font installer.

  build_armor_appendix.py   Data-table extractors that re-generate
  build_bestiary_appendix.py    appendix tables from C source.
  build_weapons_appendix.py
  dungeon_map.py

  fonts/                    Web font files (EB Garamond bold).
  images/                   Inline figures.
  cover/                    Print cover sources + final PDFs.

  companion-audit.md        Audit log — every fact-check, every fix.
  companion-audit-queue.md  Record of the 183-unit shuffled audit.
  companion-review-needed.md   Close calls left for human review.
```

## License

The book itself (`companion.md`), the cover art, and all built
outputs are released under
**[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)**
— the same license used in the book's colophon.

You are free to copy, distribute, remix, and adapt, including
commercially, provided you give credit and share derivative works
under the same license. See `LICENSE` for the full text.

Build scripts are dual-licensed CC BY-SA 4.0 or MIT at your option.

## A note on NetHack

NetHack itself is the work of the **NetHack DevTeam** since 1987,
founded by Mike Stephenson, Izchak Miller, and Janet Walz. The
current team — Michael Allison, Ken Arromdee, David Cohrs, Jessie
Collet, Pasi Kallinen, Ken Lorber, Dean Luick, Patric Mueller, Pat
Rankin, Derek S. Ray, Alex Smith, Mike Stephenson, Janet Walz,
Paul Winner, Bart House, and Warwick Allison — released 5.0 in
2025. Everything in this book is downstream of their work.

The game descends from Jay Fenlason's *Hack* (1982), itself
directly inspired by Toy and Wichman's *Rogue* (1980). The dungeon is
older than this guide, older than this repo, older than most of
its readers. May it outlast all of us.
