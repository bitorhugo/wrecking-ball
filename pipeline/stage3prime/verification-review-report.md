[LEGACY-NO-CONTRACT]

# Verification Review Report — Stage 3' (Round 2)

## Judge Record (#539)

- **Verification judge**: claude-opus-5-5 (session model family), five seat agents.
- **Round-1 panel provenance**: `pipeline/stage3/review-panel-provenance.json` (validated by `review_panel_provenance.py validate`). Axes:
  role_separated true, fresh_context true (within the panel attempt), blind_to_peer_outputs true,
  model_family_distinct false, provider_distinct false, human_distinct false.
- **Blind cross-model pass**: not_configured (`ARS_CROSS_MODEL` unset). Single-family disclosure applies.
- **Pre-committed criteria**: none (legacy — no contract). Stand-in: each seat's Step A verdict file was frozen by sha256
  (`stepA-commit.sha256`) before the response letter was shown; all five hashes re-verified after Step B (OK).
- **Prompt/rubric surfaces**: `academic-paper-reviewer/references/re_review_mode_protocol.md` § Decision Derivation
  (B-rules applied by hand); item yardstick = Round-1 roadmap Requirement/Acceptance criteria
  (`pipeline/stage3/editorial-decision.md` Part 2).
- **Reviewer configuration**: round1_cards_reused (same five seat agents as Round 1, resumed with their Round-1 context).
- **Routing**: card_mapped — `routing.md` (one verifier per item, by Round-1 source seat).
- **Apply-report chain**: not applicable (legacy). The Stage 4 revision was made by direct edits; no patch/apply-report
  artifacts exist. This is why the author chose legacy mode.
- **Evidence seen by the judge**: original manuscript, revised manuscript (+ revised LaTeX source, refs.bib), roadmap;
  Response to Reviewers only in Step B. Input files hash-bound in `input-manifest.sha256` (re-verified OK).
- **Judging budget**: 10 seat calls (5 × Step A, 5 × Step B).

This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent
biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2).

## Decision
**Major Revision** (`reject_recommended: false`).

## Revision Response Checklist

### must_fix — Required Revisions

| Ref | Item | Verifier | Author's claim | Final status | Verified? | Cross-model | Note |
|---|---|---|---|---|---|---|---|
| R1 | REV-04 verdicts → coverage statements | DA | Addressed | FULLY_ADDRESSED | ✅ | not_configured | |
| R2 | REV-07 reproducible search | R1 | Partly addressed | PARTIALLY_ADDRESSED — residual **must_fix** | PARTIAL | not_configured | No per-query list with dates; no identification/screening counts (never logged) |
| R3 | REV-08 symmetric real-hardware search / scoped claim | R1 | Addressed (scoped) | PARTIALLY_ADDRESSED — residual should_fix | PARTIAL | not_configured | §IX still says DSAs "have almost no real-silicon validation" unscoped |
| R4 | REV-09 energy within baseline classes | R1 | Addressed | FULLY_ADDRESSED | ✅ | not_configured | |
| R5 | REV-10 sim-vs-silicon confound | R2 | Addressed | FULLY_ADDRESSED | ✅ | not_configured | |
| R6 | REV-12 "PIM more active" claim | R2 | Addressed | FULLY_ADDRESSED | ✅ | not_configured | |
| R7 | REV-15 PEI/GraphPIM lineage | R2 | Addressed | FULLY_ADDRESSED | ✅ | not_configured | |
| R8 | REV-16 in-window DSAs | R2 | Addressed | PARTIALLY_ADDRESSED — residual should_fix | PARTIAL | not_configured | GraphPulse neither cited as a corpus entry nor given an exclusion reason |
| R9 | REV-17 scope of physical explanation | R2 | Addressed | FULLY_ADDRESSED | ✅ | not_configured | |
| R10 | REV-25 predictability terminology | R3 | Addressed | FULLY_ADDRESSED | ✅ | not_configured | |
| R11 | REV-26 threat model | R3 | Addressed | FULLY_ADDRESSED | ✅ | not_configured | |
| R12 | REV-30 granularity axis | DA | Addressed | PARTIALLY_ADDRESSED — residual should_fix | PARTIAL | not_configured | Table IV fine-granularity row still PIM + / DSA – |
| R13 | REV-31 size/communication symmetry | DA | Addressed | PARTIALLY_ADDRESSED — residual should_fix | PARTIAL | not_configured | Table IV still has a separate size row with different PIM/DSA ratings |
| R14 | REV-32 mutability as coverage gap | DA | Addressed | FULLY_ADDRESSED | ✅ | not_configured | |

must_fix: 9 FULLY, 5 PARTIALLY (1 with must_fix residual), 0 NOT, 0 MADE_WORSE, 0 CANNOT_VERIFY.

### should_fix — Suggested Revisions

| # | Item | Status | Notes |
|---|---|---|---|
| S2 | REV-02 axes-table cells | PARTIALLY_ADDRESSED | Fine-granularity PIM "+" cites only hybrids; dynamic-graph PIM "?" though its basis reports a PIM win |
| S5 | REV-06 stronger critical-use citations | NOT_ADDRESSED | Author: no verified source at hand (recorded; does not count) |
| S6 | REV-11 single-digit qualifier | FULLY_ADDRESSED | |
| S7 | REV-13 threats to validity | PARTIALLY_ADDRESSED | Extraction-sheet availability unstated; Data availability statement unchanged |
| S8 | REV-14 one venue frame | FULLY_ADDRESSED | |
| S9 | REV-18 HBM-PIM / AiM | NOT_ADDRESSED | Author: no verified source |
| S10 | REV-19 digital processing-using-memory | PARTIALLY_ADDRESSED | Text added; Fig. 1 level and reference missing |
| S11 | REV-20 DPU clocks | FULLY_ADDRESSED | |
| S12 | REV-21 SISA baseline | PARTIALLY_ADDRESSED | Table III still "(Bron–Kerbosch)" |
| S13 | REV-22 GraphWave classification | FULLY_ADDRESSED | |
| S14 | REV-23 "discrete DSAs" | FULLY_ADDRESSED | |
| S15 | REV-24 PIM survey positioning | NOT_ADDRESSED | Author: no verified source |

`should_fix_addressed_rate` = 9 / 12 = **75%** (< 80%).

### consider — Nice to Fix

| # | Item | Status |
|---|---|---|
| N1 | REV-01 Fig. 1 | FULLY_ADDRESSED |
| N3 | REV-03 GraphDynS label | FULLY_ADDRESSED |
| N4 | REV-05 research questions | FULLY_ADDRESSED |
| N16 | REV-27 ECC scope | FULLY_ADDRESSED |
| N17 | REV-28 network-security use case | FULLY_ADDRESSED |
| N18 | REV-29 definitions | FULLY_ADDRESSED |

## New Issues (Discovered During Revision)

| # | Attribution | Severity | Location | Description (frozen at Step A) |
|---|---|---|---|---|
| NEW-DA-2 | regression (seat) — **contested by orchestrator, see note** | major | Abstract; §VI-G; §IX | The one remaining "separating" assumption (communication through a host) is a property of UPMEM, not of PIM as a camp; the simulated PIM designs assume interconnects |
| NEW-eic-1 / NEW-domain-1 / NEW-DA-3 | regression | minor | §II-B, Fig. 1, Table I, §VI | Dalorex classified three ways (DSA row in Fig. 1, own class in Table I, "between the camps"), yet used as DSA evidence ("No DSA has this constraint", Table IV); GraphWave/Dalorex classification inconsistent |
| NEW-domain-3 | regression | minor | §VI-G | "No DSA has this constraint" supported only by Dalorex |
| NEW-domain-2 | regression | minor | §VI-G Mutability | Third explanation over-reads GraphPIM (explains why updates stay on the host, not why no offload design for dynamic graphs exists) |
| NEW-DA-1 / NEW-methodology-1 | regression | minor | §VI-G, §II-C | Exclusion reasons for the two dynamic-graph PIM counterexamples are not stated inclusion rules, while the venue frame was widened for UPMEM |
| NEW-methodology-3 | regression | minor | §VI-D, §II-C, §VIII-3 | One unadjudicated failed reproduction (Dalorex/GraphQ) presented as a general simulation problem |
| NEW-domain-4 | previously_missed | minor | §VIII-2 | Open challenge 2 implies an interconnect alone would close the gap, contradicting the confound now stated in §VI-D |
| NEW-DA-4 | previously_missed | minor | §VI-G | "PIM wins when partitions rarely communicate" — wins against what? (DSA cell is "?") |
| NEW-methodology-2 | previously_missed | minor | §VI-B | PIM energy figures with different baselines still side by side within the camp |
| NEW-perspective-1 | previously_missed | minor | §VII Security | Under MGX's model, PIM moves computation to the untrusted side of the boundary, not "inside" it |

**Orchestrator note on NEW-DA-2 attribution.** The original manuscript's abstract already listed "whether communication
between units must pass through a host" as one of three separating assumptions. The revision narrowed the thesis to make
it the only one but did not create the underlying weakness. By the protocol's definition (regression = anchored in the
revised manuscript, not the original), the attribution is contestable; it may be `previously_missed`. It is recorded as
the seat filed it and flagged. **The decision does not depend on it** (B4 fires independently, see below).

## Decision Rationale

Gates: G0 n/a (legacy, inputs hash-verified); G1 none — no silent verdict changes (0 adjustments; Step A hashes
re-verified); G2 none.
Step 2, first match:
- B1, B2: no.
- **B3**: fires only if NEW-DA-2 is a `regression` of severity major (contested).
- **B4: fires** — REV-07 (must_fix) is PARTIALLY_ADDRESSED with `residual_obligation_class: must_fix`.
→ **Major Revision**. Also present (would have given Minor on their own): five PARTIALLY_ADDRESSED must_fix items with
should_fix residuals, `should_fix_addressed_rate` 75% < 80%, and minor regression-attributed new issues (B5).

## Residual Issues

Per the state machine, Major at Stage 3' → **Stage 4' (one re-revision round), then Stage 4.5 with no return to review**.
Items still open after Stage 4' become Acknowledged Limitations. The REV-07 residual (screening counts) cannot be met
without re-running a logged search; the honest options are (a) re-run a logged search, or (b) record it as an
acknowledged limitation in the paper and the response.
