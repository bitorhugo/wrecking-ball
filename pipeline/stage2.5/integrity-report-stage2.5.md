# Academic Integrity Verification Report — Stage 2.5 (Mode 1, pre-review)

- Paper: *Wrecking (Memory) Ball: PIM versus DSAs for Irregular Graph Workloads — A Survey* (`paper/main.tex`)
- Run date: 2026-10-11
- Verifier: integrity_verification_agent protocol, executed in-session by the same model that drafted and revised
  the paper. **This is not an independent check** (same-source risk). Stage 3 review and Stage 4.5 re-run it from scratch.
- Input draft: `pipeline/stage2.5/main-before-integrity-fixes.tex` (+ `refs-before-integrity-fixes.bib`)
- Output draft: `paper/main.tex` sha256 `328b7b3a49a4a5db…`, `paper/refs.bib` sha256 `911557289764bf4f…`

## Verdict

| Round | Verdict | Reason |
|---|---|---|
| 1 | **FAIL** | 1 SERIOUS (MAJOR_DISTORTION, IL-SERIOUS-1), 1 MEDIUM (IL-MEDIUM-1) |
| 2 (corrected items re-verified) | **PASS WITH NOTES** | 0 SERIOUS, 0 MEDIUM, 0 MAJOR_DISTORTION, 0 UNVERIFIABLE; 2 UNVERIFIABLE_ACCESS notes; advisory rows open |

AI Research Failure Mode Checklist: no mode SUSPECTED; Modes 1, 3, 5, 6 not INSUFFICIENT EVIDENCE → **no block**.

## Verification Summary

| Phase | Population | Checked | Result |
|---|---|---|---|
| A — references | 31 registered bib entries | 31 (100%) | 31 VERIFIED (exist; title, all author surnames in order, year, venue match Crossref). 1 page error (MEDIUM), 1 newer published version, 9 confirmed DOIs missing, 17 entries missing pages (MINOR). 0 orphans, 0 dangling |
| B — citation context | 228 citation/number-bearing sentences | 100% of numeric claims + ~35 mechanism/attribution claims (well above 30%) | see Phase E |
| C — data | 245 numeric tokens in prose and tables | 100% | Every source-attributed number found in the cited full text; 22 untraced tokens are layout widths, SQ labels, or survey metadata. Table 2 values identical to prose values (same token set) |
| D — originality | 58 paragraphs | 58 (100%) vs. 29 local full texts | All ORIGINAL; 6 paragraphs share 8–10-word runs that are number-reporting phrases ("4.4× speedup and 11.6× less energy") |
| E — claims | 228 registered sentences | 119 targeted window checks (all numerical/headline claims) + ~35 mechanism claims + 3 absence claims (grep over full texts) | 1 MAJOR_DISTORTION (fixed), 4 MINOR_DISTORTION (fixed), 2 UNVERIFIABLE_ACCESS (published version not obtainable) |

### Phase A audit trail (method)
- Tier 1: Crossref REST API — DOI resolution for 21 entries with a DOI; bibliographic title search for the 10 without
  (raw results: `phaseA-crossref.json`). All author surnames compared position-by-position.
- Tier 2: Semantic Scholar Graph API for the 5 entries whose PDF is absent or a preprint (PrIM, IMPACT, MGX,
  NDMiner, PiD): titles, venues, and published abstracts retrieved.
- Low title-similarity scores (GraphQ, GraphDynS, TDGraph, MGX, NDMiner) are Crossref storing only the short title;
  the full titles match the PDFs.

### Phase E — claim verdicts after round 1

| Verdict | Count | Items |
|---|---|---|
| VERIFIED | all other checked claims | — |
| MAJOR_DISTORTION | 1 → fixed | IL-SERIOUS-1 |
| MINOR_DISTORTION | 4 → fixed | IL-MINOR-1…4 |
| UNVERIFIABLE_ACCESS | 2 (open notes) | N-1 PrIM, N-2 MGX |
| UNVERIFIABLE | 0 | — |

Absence claims checked by full-text search:
- "None of [Piccolo, FALA, CoGraf] mentions dynamic, streaming, or evolving graphs": VERIFIED (the only hits for
  "streaming"/"insertion" are titles in their reference lists; CoGraf's "graph updates" are vertex updates).
- "None of [GraphR, Spara, GaaS-X] evaluates device variation, stuck-at faults, or endurance": VERIFIED (GraphR cites
  ReRAM endurance of up to 10^12 cycles as a device property; nothing is evaluated).
- MGX and NDMiner claims: VERIFIED against their published abstracts (33% → 5% graph overhead; buffer-chip set
  units, load elision for symmetry breaking, 6.4× / 2.5×).

## Issue List (Sorted by Severity)

### SERIOUS (Must Fix)
| ID | # | Category | Location | Issue | Correct information | Source | Status |
|---|---|---|---|---|---|---|---|
| IL-SERIOUS-1 | 1 | Claim (MAJOR_DISTORTION) | §VI "Mutability" | Said the UPMEM triangle-counting study "recounts all triangles each time" and that its advantage is "not from incremental computation". The paper says the PIM (and GPU) versions "quickly begin counting the triangles formed by the newly updated set of edges". The error came from the Stage 1 extraction sheet, which misread the Fig. 7 caption ("counting the exact triangle number") | Rewritten: a software study on existing PIM hardware (not a dynamic-graph PIM design) that appends COO batches and counts the triangles each batch forms; its advantage over the CPU comes from avoiding a full CSR conversion after every update. Extraction sheet rows corrected and marked | asquini2025tc full text, §4.6 and Fig. 7 | **Fixed, re-verified** |

### MEDIUM (Must Fix)
| ID | # | Category | Location | Issue | Correct information | Source | Status |
|---|---|---|---|---|---|---|---|
| IL-MEDIUM-1 | 1 | Reference (page error) | refs.bib `giannoula2021syncron` | pages 263–273 | 263–276 | Crossref, DOI 10.1109/HPCA51647.2021.00031 | **Fixed** |

### MINOR (Recommended Fix) — all applied
| ID | # | Category | Location | Issue | Applied fix |
|---|---|---|---|---|---|
| IL-MINOR-1 | 1 | Claim | §III-D UPMEM; §VII Predictability | "adding DPUs hardly reduces the synchronization time" / "does not decrease": the source says BFS inter-DPU sync cost *increases linearly* with DPUs | "grows with the number of DPUs" / "grows as DPUs are added" |
| IL-MINOR-2 | 2 | Claim | §III-C SynCron | "1.35× (real applications)": the source says low-contention real applications | "(low-contention real applications)" |
| IL-MINOR-3 | 3 | Claim | §III-D PrIM; §VI Communication topology | the 13 benchmarks avoid intensive inter-DPU sync *or floating-point ops*; "benchmarks without synchronization" overstates | added "or intensive floating-point operations"; "without heavy synchronization" |
| IL-MINOR-4 | 4 | Claim | §III-D triangle counting | "UPMEM is slower than CPU and GPU on static graphs": the source says "generally", with one exception (Human-Jung); "faster only when…" was relative to the CPU | "generally slower"; "faster than the CPU only when…" |
| IL-MINOR-5 | 5 | Internal consistency | Abstract | "30 hardware designs, real-hardware studies, and position papers": the 30 include the two software systems that §II-C says are not counted as hardware | "30 works … and two software systems used as context" |
| IL-MINOR-6 | 6 | Method wording | §II-C | Stage 1 searches were targeted, not proceedings scans (brief §6) | "targeted web searches" |
| IL-MINOR-7 | 7 | Reference | refs.bib `yuksel2026pid` | cited as arXiv preprint; now published | ICS 2026 Workshops, pp. 6–11, DOI 10.1145/3774895.3819989 (158× confirmed in the published abstract) |
| IL-MINOR-8 | 8 | Reference | refs.bib `asquini2025tc` | cited as @misc/arXiv | IPDPSW 2025 (GrAPL), pp. 805–814, DOI 10.1109/IPDPSW66978.2025.00126 |
| IL-MINOR-9 | 9 | Reference | refs.bib, 7 entries | DOIs missing but now confirmed (GraphP, HATS, Graphicionado, ReGraph, GraphWave, Piccolo, IMPACT) | added |
| IL-MINOR-10 | 10 | Reference | refs.bib, 17 entries | page ranges missing | added from Crossref |

### Notes (UNVERIFIABLE_ACCESS — non-blocking)
| ID | Item | Detail |
|---|---|---|
| N-1 | PrIM (`gomezluna2022prim`) | Cited version is IEEE Access 2022; numbers (93.0×, 27.9×, 13 benchmarks, BFS sync behavior, DPU specs) were verified in the authors' arXiv long version. The Access abstract confirms the 640/2,556-DPU systems. The open-access Access PDF could not be downloaded here (IEEE and ETH repository block scripted access). **Action for you:** download it (it is open access) and confirm the numbers, or I can cite both versions |
| N-2 | MGX, NDMiner | No full text; claims limited to their abstracts, as stated in §II-C. Abstract claims verified. Adding the PDFs would allow full-text checks at Stage 4.5 |
| N-3 | IMPACT | Text is arXiv v4; the 8.2/14.8 Mb/s and 3.6×/6.5× values are confirmed in the DSN 2025 record's abstract. The GraphBIG defense evaluation is verified only in v4 |

## Advisory rows (not issues; never gate)

**ADV-E5 — novelty/absence claims with absolute wording** (`claim_verification_protocol.md` §E5). Default: proceed open.

| ID | Location | Claim wording | Classification | Recommended bounded rewording |
|---|---|---|---|---|
| ADV-E5-1 | Conclusion; Open challenge 1 | "Such a combination for dynamic graphs … does not exist yet"; "The clearest gap is a PIM design that supports incremental updates" | UNRESOLVED — **Stage 1 found counter-evidence outside the searched venues** (J. Supercomputing 2026 dynamic-graph CIM mapping; Moctopus preprint), and the paper does not mention it | Add one sentence: "Outside these venues, a 2026 journal paper and a preprint address dynamic graphs on PIM [refs]"; and/or bound the wording to "in the surveyed venues". Needs the journal paper's bibliographic details verified first |
| ADV-E5-2 | §VI-A Throughput | "No study compares a PIM design and a DSA under matched conditions" | UNRESOLVED (absolute) | "No study in our corpus…" |
| ADV-E5-3 | §VI-D Evidence | "the same gap for ASIC-class graph DSAs has never been measured" | UNRESOLVED (absolute) | "has not been measured in the surveyed work" |
| ADV-E5-4 | §VI other axes | "Concurrency … has been addressed in software but not in either hardware camp" | UNRESOLVED (absolute) | "…but not by any surveyed hardware design" |
| ADV-E5-5 | §VII Predictability | "Neither camp addresses worst-case timing"; "Neither camp therefore offers bounded latency today" | UNRESOLVED (absolute) | "No surveyed design addresses…" |

E4 scope-conformance: no claim broadened beyond the RQ scope (2015–2026, ISCA/MICRO/HPCA/ASPLOS/DSN focus).
E6 claim-strength drift: `[E6-SKIPPED: no revision evidence]` (first-pass audit). A script confirmed that the B2
rewrite and shortening kept every number and citation unchanged.

## AI Research Failure Mode Checklist (7 modes)

| Mode | Status | Evidence |
|---|---|---|
| 1 Implementation bug | CLEAR | Survey: no experiments or analysis code. Reported numbers are extracted values, each traced to its source text |
| 2 Hallucinated citation | CLEAR | 31/31 references exist and match Crossref; the one page error is fixed |
| 3 Hallucinated result | CLEAR | 245/245 source-attributed numeric tokens traced; 119 context-window checks pass. One interpretation error (IL-SERIOUS-1) found and fixed |
| 4 Shortcut reliance | CLEAR (N/A) | No trained models or ablations |
| 5 Bug reframed as insight | CLEAR | No "surprising/unexpected" framing; the headline findings are literature syntheses with cited support |
| 6 Methodology fabrication | CLEAR | §II-C matches the Stage 1 brief and citation audit: venues and window, two abstract-only works, full texts in `pipeline/fulltext/`. "targeted" added (IL-MINOR-6). Note: the brief records dblp's API as unreachable in Stage 1; dblp web pages were still used |
| 7 Frame-lock | CLEAR, with advisory | The red-team confound from Stage 1 (tooling vs. physics) is discussed in §VI. Known out-of-venue counter-evidence is not disclosed → ADV-E5-1 |

## Tool Limitation Disclaimer

> The originality check (Phase D) compared the paper with the 29 local full texts using 8-word n-grams; no web-wide
> search or professional plagiarism tool (Turnitin/iThenticate) was used. Phase A used Crossref and Semantic Scholar,
> not a WebSearch sweep. Claim checks are model-mediated and were run by the model that wrote the draft. Run a
> professional similarity check before formal submission.

## Files
- `phaseA-crossref.json`: raw Crossref records per reference
- `claim-registry.json`: 228 registered sentences with numeric-token traces
- `main-before-integrity-fixes.tex`, `refs-before-integrity-fixes.bib`: pre-correction inputs
- `../extraction-sheet.org`: two rows corrected (marked "Corrected at Stage 2.5")

## Checkpoint disposition (2026-10-11): user chose option (a)

ADV-E5-1 to ADV-E5-5 were applied as bounded rewordings:
- ADV-E5-1: §VI "Mutability" now names the two out-of-venue works as outside the corpus and not assessed;
  Open challenge 1 is bounded to "In the surveyed venues". The conclusion's "does not exist yet" had already been
  removed in the shortening pass.
- ADV-E5-2…5: "No study in our corpus…", "the surveyed work has not measured…", "not by any surveyed hardware
  design", "No surveyed design in either camp addresses…", "No surveyed design therefore offers…".

Registered additions (Phase A, verified):
| Key | Verified via | Claim scope in paper |
|---|---|---|
| ghasemi2026dynamic | Crossref DOI 10.1007/s11227-026-08883-x (J. Supercomputing 82(15), art. 739, 2026; authors Ghasemi, Farbeh); Semantic Scholar record. Abstract withheld by the publisher | Title-level only: "proposes a mapping approach for dynamic graph computation in computing-in-memory systems" |
| ma2024moctopus | arXiv API, 2403.10051 (7 authors, 2024-03-15); abstract read | "a PIM-based graph database that supports graph updates through dynamic partitioning" (matches the abstract) |

Numbers and the existing 31 citations unchanged (script check). Words 7,488. Build clean.
Post-checkpoint verdict: PASS WITH NOTES (unchanged).
