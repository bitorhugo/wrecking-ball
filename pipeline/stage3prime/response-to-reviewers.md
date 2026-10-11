# Response to Reviewers — Stage 4 (Round 1 revision)

Manuscript: *Wrecking (Memory) Ball: PIM versus DSAs for Irregular Graph Workloads — A Survey*
Decision received: Major Revision (`dimension_verdicts: [D1=warn, D2=block, D3=block, D4=warn, D5=warn, D6=pass]`)
Revision mode: author chose "just fix it" (option b). Pre-revision copy: `main-before-revision.tex`, `refs-before-revision.bib`.

New sources used in this revision (all read in full text and verified in Crossref):
PEI (ISCA 2015, 10.1145/2749469.2750385), GraphPIM (HPCA 2017, 10.1109/HPCA.2017.54),
PolyGraph (ISCA 2021, 10.1109/ISCA52012.2021.00053), Dalorex (HPCA 2023, 10.1109/HPCA56546.2023.10071089).
ScalaGraph (HPCA 2022, 10.1109/HPCA53966.2022.00023) verified in Crossref only; cited solely as "not included,
full text unavailable".

Every new number was traced to the source text: PEI 47% / 20%; GraphPIM 2.4×, 37%, HMC 2.0 atomics, update
operations not offloadable; PolyGraph 1.93× over GraphPulse, 2.71×, up to 50%; Dalorex two orders of magnitude over
Tesseract at 256 cores, 4.2 MB per tile, PolyGraph plateau beyond 16 cores at 512 GB/s HBM, GraphQ non-reproduction
3.2× runtime / 4.6× energy; PrIM clocks 350 MHz (2,556 DPUs) / 267 MHz (640 DPUs), 24 hardware threads.

## Required items (must_fix)

| Item | Source | Response | Status |
|---|---|---|---|
| REV-04 | EIC W4, R1 W5, DA M1 | Abstract: "Almost no study compares the two camps under matched conditions, so we do not rank them." §VI-A now names the two closest comparisons (Piccolo; Dalorex vs Tesseract and PolyGraph) and says neither is a pure PIM-vs-DSA comparison. §VI workload view and §IX say the "favors" statements are "about coverage, not results of matched comparisons". | Addressed |
| REV-07 | R1 W1 | §II-C now gives the keyword set, the venues and years, the separate critical-systems queries, the end date of the main search (28 Sep 2026) and of the gap-closing searches (11 Oct 2026). **Screening counts were never logged**, so we state this as a limitation instead of reconstructing them. | Partly addressed (honest limitation) |
| REV-08 | R1 W2, DA M5 | Took the roadmap's second option: §II-C "Limitations of the search" and §VI-D state that we searched more widely for real-hardware PIM than for real-hardware DSAs, so the "only ReGraph" asymmetry "may partly come from our search, and it does not show that DSAs avoid silicon". No new search was run. | Addressed (scoped claim) |
| REV-09 | R1 W3, DA M6 | §VI-B rewritten: numbers grouped within baseline classes; "most consistent" removed; the camps share "a mechanism argument, not a measured ranking". §IX no longer claims a measured PIM energy advantage. | Addressed |
| REV-10 | R1 W4, R2 W3, DA M5 | Abstract drops "mainly"; it now says the silicon platform's architecture differs from the simulated designs. §VI-D: "Architecture and evaluation method change together, so we cannot say how much of the difference comes from each." Added Dalorex's failed reproduction of GraphQ as separate evidence about simulation. | Addressed |
| REV-12 | R1 W8, R2 W2 | "Graph PIM has been the more active design space" removed. §II-C explains the PIM-heavy corpus by our asymmetric search and says it "is therefore not evidence that one camp is more active". | Addressed |
| REV-15 | R2 W1 | New §III-B "3D-stacked PIM: offloading single instructions" reviews PEI and GraphPIM. Taxonomy (§II-B, Fig. 1, Table I) gains an instruction-offload class. §I and §V recast the 2025–2026 hybrids as refinements ("Convergence: Host–Memory Cooperation Revisited"). | Addressed |
| REV-16 | R2 W2 | PolyGraph added to §IV-A, Table I, Table III, Fig. 2. Dalorex added as a data-local design between the camps (§II-B, §V, Tables I and III, Fig. 2). ScalaGraph: verified, but excluded because the full text was unavailable, stated in §II-C. GraphPulse: already discussed as JetStream's base; not added as a separate corpus entry. | Addressed |
| REV-17 | R2 W4, DA M4 | §VI "Mutability" now gives three explanations: convenience; the physical argument, explicitly limited to PIM that partitions the graph (Tesseract, UPMEM); and, for instruction-level PIM, GraphPIM's own finding that updates need operations too complex for in-memory atomics. The "predicts the pattern" test is removed: "The current evidence cannot decide between these explanations, and more than one may hold." | Addressed |
| REV-25 | R3 W1 | §VII opens with working definitions (predictability = WCET/latency can be bounded and analysed). "No upper bound" replaced by "the only obvious bound is then the cost of a full recomputation, which is finite but loose, and no surveyed paper analyses it". Spara example removed. Added what bounded latency would require. | Addressed |
| REV-26 | R3 W2 | §VII Security names the adversary of each study (MGX: off-chip memory attacker; IMPACT: co-located software) and says the results "cannot be weighed against each other directly". Adds that controller-side encryption "does not hide the address trace", so access-pattern leakage affects both camps. Table V updated. | Addressed |
| REV-30 | DA M2 | The thesis is restated throughout (Abstract, §VI, §IX): only the communication path separates the camps on current hardware; access granularity "affects both camps" and explains convergence; mutability is "a gap in coverage". | Addressed |
| REV-31 | DA M3 | Graph size is no longer a separate axis: "Size and communication therefore act together, and we treat them as one condition." Table IV: high-traffic DSA cell changed from + to ± with DSA sources (PolyGraph, Dalorex); hybrid size cell changed to ?; coding rule added to the caption. | Addressed |
| REV-32 | DA M4 | §VI "Mutability (a gap in coverage)" says the axis "records what the top-venue literature covers, not what PIM can do", and explains why the two out-of-corpus works were not assessed (outside the venue frame with no full text; preprint). | Addressed |

## Optional items

| Item | Source | Response | Status |
|---|---|---|---|
| REV-01 | EIC W1 | Fig. 1: hybrids shown as "in-memory parts of Piccolo, FALA, CoGraf"; caption notes they span two levels; SynCron, GraphWave, ReGraph, PolyGraph, PEI, GraphPIM, Dalorex added. | Done |
| REV-02 | EIC W2, R1 W6 | Table IV: coding rule in caption; unsupported cells changed to ?. | Done |
| REV-03 | EIC W3 | Table III GraphDynS substrate: "RTL + cycle-accurate sim." | Done |
| REV-05 | EIC W5 | §II-A ends with the five research questions the literature itself addresses. | Done |
| REV-06 | EIC W6, R3 W4 | Stronger critical-use citations **not added**: we had no verified source at hand. The use case is now tied to the paper's own mutability finding (REV-28). | Not done |
| REV-11 | R1 W7 | "On average … single-digit factor. Maximum gains can be larger, such as 13.9× for GraphQ." | Done |
| REV-13 | R1 W9 | New "Threats to validity" paragraph in §II-C (self-reported numbers, no reproduction, single AI-assisted extractor with full-text checks, extraction sheet kept with the sources). | Done |
| REV-14 | R1 W10 | §II-C states one frame for absence claims (ISCA, MICRO, HPCA, ASPLOS 2021–2026; DSN only for critical properties). | Done |
| REV-18 | R2 W5 | HBM-PIM / AiM **not added**: no verified source and no graph evaluation to report. | Not done |
| REV-19 | R2 W6 | Taxonomy now includes digital bulk bitwise processing-using-memory, citing SISA (no Ambit citation added). | Done (partly) |
| REV-20 | R2 W7 | DPU clock per system from PrIM's table (350 MHz for 2,556 DPUs, 267 MHz for 640 DPUs); 24 hardware threads. The reviewer's reversed parenthetical was not used. | Done |
| REV-21 | R2 W8 | SISA baseline: "a non-SISA implementation of the established Bron–Kerbosch maximal-clique algorithm". | Done |
| REV-22 | R2 W9 | GraphWave: classification justified in §IV-A. | Done |
| REV-23 | R2 W10 | "discrete" removed from the RQ; §I says DSA includes per-core engines. | Done |
| REV-24 | R2 W11 | Positioning against PIM surveys and primers **not added** (no verified source at hand). | Not done |
| REV-27 | R3 W3 | ECC claim limited to stored data; scratchpads; in-DRAM compute "may" fall below ECC (hedged; no source). | Done |
| REV-28 | R3 W4 | §VII opening links network security to streaming graphs and the DSA-only hardware support. | Done |
| REV-29 | R3 W5 | Working definitions of security, dependability, and predictability added. | Done |

## Effects on the paper
- Corpus 30 → 34 works; references 33 → 38 (25 from 2021 or later).
- Words: 7,488 → about 9,090 (same counter). PDF: 13 pages, references from page 12, so the body is about 11 pages,
  inside the 8–12 page limit in brief.org. This is above the ~8,500 words proposed at the checkpoint.
- One numeric example removed on purpose (Spara's ">5× from 500 million to one billion edges", REV-25).
- Every pre-existing citation key and number is preserved, except the removed Spara example and its citation use.
- B2 style kept: mean sentence length 16.8 words.
