# B2 language revision (2026-10-11)

Scope: language only, before Stage 2.5. No claims, numbers, or citations were added, removed, or changed.
Pre-revision copy: `main-before-b2.tex` (this folder).

## Template changes
- `\documentclass[journal,onecolumn]{IEEEtran}`, journal author block with `\thanks`, `\markboth` running heads (previous turn).
- Tables: `\scriptsize` -> `\footnotesize`; first-column widths widened to use the single-column page.
- Caption wording simplified; "Critical-System Properties" section renamed "Properties for Critical Systems".

## Language changes (target: CEFR B2)
- Long multi-clause sentences split; one idea per sentence where possible.
- Idioms and C1/C2 vocabulary replaced (e.g., "reality check", "temper", "elides", "entails",
  "sharpen", "flagship", "contested middle ground", "first-order concern", "gradient", "binding constraint",
  "lineage", "frame").
- Long paragraphs split (DSA static pipelines, streaming DSAs, hybrids, security, conclusion).
- Spelling normalized to American English (IEEE style): neighbor, favor, behavior, analyzed, defense, toward.
- Acronyms now defined at first body use: DSA, DRAM, DIMM, ALU, SerDes, ASIC.

## Checks (scripted, see cmp.py logic in session)
| Metric | Before | After |
|---|---|---|
| \cite keys and per-key use counts | — | identical |
| Numeric tokens in prose and tables | — | identical set |
| Sentences | 390 | 480 |
| Mean / median sentence length (words) | 18.4 / 17 | 16.6 / 16 |
| Sentences > 30 words | 33 | 11 (mostly lists) |
| Words (abstract to conclusion, no tables) | 7,191 | 7,960 |

Build: `make` succeeds, 12 pages, no overfull boxes or undefined references.

## Shortening pass (2026-10-11, author request)
Pre-shortening copy: `main-before-shorten.tex`.
- Cut repeated summaries: abstract, roadmap paragraph, contribution (iii), section wrap-ups, throughput and
  evidence-comparability recaps, Piccolo's repeat of the burst-waste numbers, open challenges 1-3 and 5-6.
- Conclusion rewritten from 3 paragraphs (~480 words) to 2 (~300 words); same claims and citations.
- Small details dropped as redundant: "designs range from DIMM-level broadcast to point-to-point links"
  (challenge 2); "including preprocessing and data transfer" (challenge 3); "Without these, cross-camp claims
  cannot be checked" (challenge 3).
- Affiliation: Instituto Superior de Engenharia do Porto (ISEP), Porto, Portugal.
- Checks vs. pre-B2 version: \cite keys and per-key counts identical; numeric tokens identical.
  Words 7,960 -> 7,380 (same counter; pre-B2 was 7,191). Sentences >30 words: 10. 11 pages, clean build.
