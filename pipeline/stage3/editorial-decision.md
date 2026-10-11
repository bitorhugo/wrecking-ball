# Editorial Decision Package

## Calibration Resolution

`calibration_status: NOT_CALIBRATED`

Current runtime boundary: this package is not upgraded from any candidate or prose-named profile. `PROFILE_MEASURED` is unavailable until a closed profile artifact and replay validator bind the target fields to the completed panel's `execution_topology_sha256`.

## Manuscript Information

- **Title**: Wrecking (Memory) Ball: Processing-in-Memory versus Domain-Specific Accelerators for Irregular Graph Workloads---A Survey
- **Field**: Computer architecture (memory systems, accelerators); comparative literature survey
- **Manuscript ID**: not provided
- **Decision Date**: 2026-10-11
- **Review Round**: Round 1 (panel `wrecking-ball-stage3-round1`)
- **Contract**: `reviewer/reviewer_full/v2` (`pipeline/stage3/contract.json`), mode `reviewer_full`, panel size 5
- **Criteria binding**: unbound run. All five cards disclose `criteria_binding_unavailable`. This letter makes no venue-alignment claim. The only target requirements are the author's course rubric (brief.org), which the Journal-Fit (EIC) seat used for D5/D6 as configured in Card #1.

---

## Part 1: Editorial Decision Letter

Dear Author,

Thank you for submitting "Wrecking (Memory) Ball: Processing-in-Memory versus Domain-Specific Accelerators for Irregular Graph Workloads---A Survey". Five role-separated review seats assessed the manuscript: a Journal-Fit Reviewer (EIC), three peer reviewers (R1 methodology, R2 domain, R3 cross-disciplinary), and a fixed Devil's Advocate (DA). The provenance section below reports how they were executed. It does not amount to a claim that the seats are independent.

### Review Panel Provenance (#540/#740)

- **Typed artifact**: `pipeline/stage3/review-panel-provenance.json` (validated by the orchestrator)
- **Artifact SHA-256**: `c95060c40521b13f881f99b412bac25e9dcfcd1ad185a98d9cdf456937dee7f2`
- **Panel ID**: `wrecking-ball-stage3-round1`
- **Contract SHA-256**: `e9712090d2469fea15a37b8e22d4e137afbcb2bf38d5789939c5df56738ef7af`
- **Normalized manifest SHA-256**: `de4160665cd627eb35e556c59d43fbdcc495976837539559c707033e9897cd4b`
- **Execution topology SHA-256**: `c259b3f71e07a5edf63a2840650cfafb0d9380f68f5533b18fdd78f82f6e2603`
- **Fresh-context scope**: `within_panel_attempt_only`. This does not compare retries or prior rounds.

| Seat | Role ID | Actor type | Context ID | Peer outputs visible | Model family | Provider | Human reviewer ID |
|---|---|---|---|---|---|---|---|
| EIC | eic | model | a0483e7f9a5dccf1c | false | claude-opus-5-5 | anthropic | unknown (null) |
| R1 | methodology | model | a939abf9e69203646 | false | claude-opus-5-5 | anthropic | unknown (null) |
| R2 | domain | model | a74802494d5b52a63 | false | claude-opus-5-5 | anthropic | unknown (null) |
| R3 | perspective | model | ae9cfdfee9905f64f | false | claude-opus-5-5 | anthropic | unknown (null) |
| DA | da | model | a7320e669e97807d5 | false | claude-opus-5-5 | anthropic | unknown (null) |

| Provenance axis | Status |
|---|---|
| Role-separated | true |
| Within-panel invocation-context separation | true |
| Blind to peer outputs | true |
| Model-family distinct | false |
| Provider distinct | false |
| Human-reviewer distinct | false |

- **Binary independence claim**: not computed (`independence_claim: not_computed_from_personas`). Persona or role diversity shows only `role_separated`. The panel is not described as independent.
- **Correlated-error disclosure** (required, reason `same_model_family`): All model-executed review seats used one model family; role separation does not remove correlated-error risk.
- **Orchestrator note (data)**: the DA seat's Read tool returned the full `cards.md` file. That file contains the other seats' configured identities but none of their outputs. The artifact's `blind_to_peer_outputs: true` stands as validated.
- **Cross-model decision check**: not configured (`ARS_CROSS_MODEL` unset). This is a single-model decision, and no `[CROSS-MODEL-HANDOFF v1]` envelope was emitted.

### Decision: Major Revision

### Mechanical Audit (v3.6.2 Sprint Contract Synthesizer Protocol)

The run completed in unbound mode: all five cards (EIC, R1, R2, R3, DA) disclose `criteria_binding_unavailable`.

**Step 1: role-scoped scoring matrix.** Only assessed scores from eligible seats are counted.

| Dim | Name | Priority | Eligible roles | Assessed eligible scores | Verdict (worst) |
|---|---|---|---|---|---|
| D1 | methodology_rigor | mandatory | methodology | R1 warn | warn |
| D2 | domain_accuracy | mandatory | domain | R2 block (repairable) | block |
| D3 | argumentative_coherence | mandatory | da, methodology | DA block (repairable); R1 warn | block |
| D4 | cross_disciplinary_relevance | high | perspective | R3 warn | warn |
| D5 | writing_and_structure | normal | eic | EIC warn | warn |
| D6 | venue_fit_and_contribution | mandatory | eic | EIC pass | pass |

No seat declared a fatal block.

**Step 2: failure conditions.**

| Condition | Severity | Quantifier | Expression | Evaluation | Fired |
|---|---|---|---|---|---|
| F1 | 95 | any | any mandatory dimension has a fatal block | no fatal block on D1/D2/D3/D6 | false |
| F2 | 90 | any | any mandatory dimension scores 'block' | D2 (R2 block, 1/1) and D3 (DA block, 1/2 ≥ 1) | true |
| F3 | 70 | majority | two or more mandatory dimensions score 'warn' or worse | D1: 1/1 (owner seat); D2: 1/1; D3: 2/2 (n=2 needs both); D6: 0/1. Three dimensions true, which meets "two or more" | true |
| F4 | 60 | any | any high-priority dimension scores 'block' | D4 = warn | false |
| F5 | 40 | any | any dimension scores 'warn' or worse | D1, D2, D3, D4, D5 | true |
| F0 | 10 | all | every dimension scores 'pass' | D1–D5 not pass | false |

**Step 3: precedence.** The fired conditions are F2 (90), F3 (70), and F5 (40). The highest severity is F2, whose action is `major_revision`. No DA CRITICAL IDs exist: the DA card's `#### CRITICAL` table has no rows. No adjudication is required, and the DA-vs-Accept marker does not apply.

dimension_verdicts: [D1=warn, D2=block, D3=block, D4=warn, D5=warn, D6=pass]
fired_conditions: [F2, F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision

### Blocking Issues (0–3, immutable source order)

Both block verdicts are repairable. The rows below are the findings that the two blocking seats named as their block triggers: R2's D2 trigger is "omission of several landmark or directly competing works", and the DA's D3 trigger is "a load-bearing claim that the cited evidence does not support". They are listed in roadmap source order.

| Transport ref | Blocking issue | Source reviewer(s) | Evidence anchor | Resolving roadmap item |
|---|---|---|---|---|
| R1 | The conclusion states which camp is "better" per regime, but the paper itself says no matched PIM-vs-DSA comparison exists (D3 block trigger) | DA M1; corroborated by R1 W5, EIC W4 | text: §6.1 and §9 "No study in our corpus compares a PIM design and a DSA under matched conditions." / "DSAs are better for evolving graphs, and for frontier-heavy traversals on today's PIM hardware" | REV-04 |
| R8 | Hybrid host/PIM cooperation is presented as a new class; the PEI/GraphPIM lineage is omitted (D2 block basis) | R2 W1 | text: §1 and §5 "A new class of hybrid designs has also appeared" and "It is evaluated against Piccolo, PEI, and GraphPIM" | REV-15 |
| R9 | Graph DSAs within the stated venues and window are missing, so "DSA, static" coverage for 2021–2026 is materially incomplete (D2 block basis) | R2 W2 | text: §2.3 "since 2021, graph PIM has been the more active design space at the target venues, while many graph DSAs are older" | REV-16 |

### Reviewer Summary

The sprint-contract cards record dimension scores, not narrative recommendations. Confidence is recorded per finding only; no card gives a report-level number.

| Seat | Role (Card) | Recommendation | Scores (owned/eligible) | Confidence |
|---|---|---|---|---|
| EIC | Journal-Fit: course instructor / ISCA-MICRO PC member grading against brief.org | not stated (sprint card) | D5 warn, D6 pass | per-finding (3–4) |
| R1 | Methodology: systematic-review methodology for computer systems | not stated (sprint card) | D1 warn, D3 warn | per-finding (3–5) |
| R2 | Domain: PIM/near-data architect (HMC, UPMEM, HBM-PIM, graph accelerators) | not stated (sprint card) | D2 block (repairable) | per-finding (3–5) |
| R3 | Cross-disciplinary: dependable/secure and real-time systems (DSN) | not stated (sprint card) | D4 warn | per-finding (3–4) |
| DA | Fixed adversarial seat | N/A, findings only | D3 block (repairable); 0 CRITICAL, 6 MAJOR | per-finding (4–5) |

### Consensus Analysis

Consensus is counted per sub-claim over the four non-DA seats (EIC, R1, R2, R3). A seat that did not mention a sub-claim is counted as silent, not as agreeing. DA corroboration is reported separately and is not part of the count. The full inventory (SC-1 to SC-34) is in Part 3.

#### Points of Agreement (Consensus)

- **[CONSENSUS-4]**: none. No sub-claim was raised by all four non-DA seats.
- **[CONSENSUS-3]**: none. No sub-claim was raised by three non-DA seats.

#### Corroborated findings (2 of 4 non-DA seats, no conflict)

- **SC-3: the simulation-versus-silicon gap confounds architecture with evaluation substrate.** Raised by R1 W4 (Major) and R2 W3 (Major); EIC and R3 are silent. The DA also raised it in M5 (Major), so 3 of 5 seats in total. All three seats make the same point: simulated HMC logic-layer designs with inter-cube links are being compared with UPMEM DIMM DPUs that have no inter-DPU path, so the Abstract's "mainly because communication … goes through the host" and §6.4's "gap between simulation and silicon" overstate what the comparison of evidence tiers can show.
- **SC-9a: the low-cross-partition-traffic row of the axes table gives "+" ratings that its Basis column does not support.** Raised by EIC W2 (Minor) and R1 W6 (Minor); R2 and R3 are silent. Both seats observe that the Basis column for this row cites only PIM sources (PrIM, PimPam). The DA raised a related point about a different row (SC-9c, high-traffic DSA "+", M3), so 3 of 5 seats in total flag unsupported cells in this table.
- **SC-25: the critical-systems motivation rests on a single workshop citation.** Raised by EIC W6 (Minor) and R3 W4 (Minor); R1 and R2 are silent. 2 of 5 seats in total.

#### DA-corroborated single-seat findings

Each of these was raised by one non-DA seat and corroborated by the DA, so 2 of 5 seats in total:

- SC-2, the Energy synthesis breaks the paper's own comparison rule: R1 W3 and DA M6.
- SC-4, real-hardware evidence was searched asymmetrically, so only PIM is held to silicon evidence: R1 W2 and DA M5.
- SC-11, the physical explanation of mutability is preferred over the convenience explanation without adequate support: R2 W4 and DA M4.

#### Points of Disagreement

**Disagreement 1: severity of the conclusion's comparative verdicts (SC-1) [SPLIT]**
- **R1 W5 (Major)**: "the concluding 'better' claims go further than the paper's own statement that no matched comparison exists". The verdicts should be restated as hypotheses supported by indirect evidence. DA M1 (Major) agrees.
- **EIC W4 (Minor)**: the same overreach, but banded Minor "only for its effect on how the contribution reads to a grader". The EIC states that "the substantive call belongs to the D3 seat".
- **Disagreement type**: severity disagreement. The remedies are compatible: EIC proposes "the evidence favours" or "only DSAs currently support", R1 proposes restating the verdicts as hypotheses, and DA proposes restating them as evidence-coverage findings.
- **Editor's Resolution**: the transported severities stay as they are on each source row, and the item is must_fix.
- **Resolution Rationale**: expertise first. D3 is owned by the DA and also eligible to methodology, and both of those seats band this Major. The EIC explicitly deferred to them. No seat disputes that the problem exists.

**Disagreement 2: severity of the "graph PIM more active since 2021" claim (SC-7) [SPLIT]**
- **R1 W8 (Minor)**: the venue and year counts do not support the claim (three pure-PIM designs versus four DSAs at the named venues from 2021). The remedy is to drop the claim or support it with counts.
- **R2 W2 (Major)**: the claim rests on a sample that omits in-window graph DSAs. The remedy is to add those works or narrow and justify the claim.
- **Disagreement type**: severity disagreement. The remedies are compatible.
- **Editor's Resolution**: transported severities are kept per row. The item is must_fix because R2 cites it as part of its D2 block basis.
- **Resolution Rationale**: evidence first. Both seats independently show from the corpus that the claim is unsupported. The difference in severity comes from R2's parent weakness (the coverage omission, SC-14), which falls within R2's domain competence.

**Disagreement 3: whether the venue-scoped absence claim is a strength or a weakness of the mutability axis (SC-12; DA vs R2, outside the 4-seat count)**
- **R2 S4**: "Absence claims are scoped, and near-miss counterexamples are disclosed … This is the right epistemic stance." R2 also says the empirical part of the mutability claim holds (W4).
- **DA M4**: the mutability axis is inferred from an absence inside a venue-restricted corpus that excludes two named counterexamples, and an absence of designs "shows a research gap. It does not show that DSAs are better."
- **Disagreement type**: perspective difference. R2 assesses the absence statement, and the DA assesses the inference drawn from it.
- **Editor's Resolution**: both positions are kept. The scoped absence statement may remain as written (R2). Its use as a separating axis and as a "better" verdict must be restated as a coverage gap (DA M4, consistent with R1 W5 and DA M1). Whether to assess the two out-of-corpus works is left to the author, who must explain the choice.
- **Resolution Rationale**: evidence first. The two seats' claims concern different steps of the argument and do not conflict once those steps are separated.

**Disagreement 4: whether the three-assumption reframing holds (EIC S3 vs DA M2; perspective difference)**
- **EIC S3**: reframing the question around mutability, granularity, and communication topology "is a contribution of the author's own" (D6 pass).
- **DA M2**: the paper itself describes access granularity as affecting both camps, so that axis separates fine-grained from coarse-grained designs, not PIM from DSA.
- **Editor's Resolution**: the D6 pass stands, since the DA does not score D6 and states that "the descriptive core … survives". The claim that "Three of them separate the camps" must still be revised or justified under REV-30.
- **Resolution Rationale**: expertise first. Each seat speaks to its own dimension, and the two findings are compatible.

### DA CRITICAL adjudications

None. The DA card's CRITICAL table is empty. All six DA findings (M1–M6) are banded MAJOR and are carried in the roadmap with their sources.

### Decision Rationale

The decision follows mechanically from the contract. F2 fires because two mandatory dimensions carry repairable blocks: D2 from R2 and D3 from the DA. F3 also fires, because D1, D2, and D3 are each warn or worse under the majority quantifier. F2 has the highest severity (90), so the action is Major Revision. No seat declared a fatal block, so F1 does not fire and Reject is not available. Both blocking seats explicitly declined the fatal class: R2 wrote "No single defect invalidates the core thesis", and the DA wrote that "the descriptive core … survives".

The panel's findings agree in substance with the mechanical outcome. The most widely shared concerns all ask the same thing: that the synthesis observe the paper's own comparison rule. The conclusion ranks camps that, by the paper's own account, have never been compared under matched conditions (EIC W4, R1 W5, DA M1). The simulation-versus-silicon gap mixes architecture with substrate (R1 W4, R2 W3, DA M5). The energy claim compares figures across baselines, which the rule forbids (R1 W3, DA M6). Separately, R2 finds coverage gaps in both camps (W1, W2) that change the history the paper tells. R1 finds that the search cannot be reproduced and was applied asymmetrically to real-hardware evidence (W1, W2). R3 finds that the security and predictability reasoning in §7 would not satisfy readers from those fields (W1, W2).

A Minor Revision would ignore two blocks on mandatory dimensions. Every seat credited the paper's strengths: baseline-annotated numbers (R1 S1, R2 S1, EIC S2), its correction of the GraphQ figure (R1 S4, R2 S2, DA), inference that is labelled as inference (R2 S5, R3 S2), and full coverage of the brief (EIC S1, S5; D6 pass). All of the defects are repairable by rewording, restructuring, added coverage, or a documented search.

### Closing

Please revise the manuscript against the reviewers' comments and submit it with a point-by-point response. The revised manuscript will be reviewed again. The roadmap in Part 2 lists every item in source order. It does not set a work order: you decide which items to address and in what sequence, and any item you decline should be recorded with your reasoning.

---

## Part 2: Revision Roadmap

The roadmap is kept in immutable source-traceability order. Items are sorted by their first source finding, in dispatch order EIC → R1 → R2 → R3 → DA, then by finding ID. Neither the order nor the obligation class is a ranking or a work order. `R<n>` and `S<n>` are transport references only. Author triage (`will_address` / `wont_address` / `not_on_point`) belongs in the separate author sidecar and is not included here.

**Obligation rule (stated once):**
- `must_fix` (required for the mechanical decision): every item whose source finding has a transported Major severity.
- `should_fix` (optional): a Minor finding on a mandatory dimension, a factual correction, or a Minor finding corroborated by two or more seats.
- `consider` (optional): a single-seat Minor finding on D4, D5, or the passed D6.

**Mechanical link column.** This column shows which dimension, and therefore which fired condition, each source finding bears on: D1 → F3; D2 → F2 and F3; D3 → F2 and F3; D4 and D5 → F5 only. Clearing every must_fix item tied to D1–D3 is necessary, but not sufficient, to move below Major Revision on re-review. While any dimension stays at warn, F5 still fires.

**Missing-reference rule.** Several items add papers that reviewers named from memory: PEI, GraphPIM, PolyGraph, Dalorex, ScalaGraph, GraphPulse, Samsung HBM-PIM/FIMDRAM, SK hynix AiM, Ambit, the Mutlu et al. primer, Ghose et al., and any stronger critical-systems citations. The orchestrator has not verified these. **Every such reference must be verified against a primary record (publisher, dblp, or the paper itself) before it is cited.** R2 itself flagged uncertainty about the ScalaGraph author list, the AiM title, and the year of the primer chapter.

**Machine artifact boundary.** No block manifest is bound for this run, so `proposed_targets[]` block IDs are not emitted. Locators below are manuscript sections, tables, and figures. The closed `revision-roadmap/1.0` JSON core and the author sidecar are built later by `scripts/revision_roadmap.py`. Item IDs REV-01 to REV-32 are stable.

### Required Revisions (Must Fix): 14 items

| Transport ref | Item | Revision Item | Sub-Claim(s) | Severity (transported) | Evidence Anchor | Confidence (transported) | Source | Obligation class | Mechanical link | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | REV-04 | Restate the §9 (and §6.5) comparative "better" verdicts as evidence-coverage findings or hypotheses supported by indirect evidence | SC-1 | EIC W4 minor; R1 W5 major; DA M1 major | text: §9 "PIM is better for stable graphs with little traffic between partitions. DSAs are better for evolving graphs"; text: §6.1 "No study in our corpus compares a PIM design and a DSA under matched conditions." | EIC 3; R1 4; DA 5 | EIC W4, R1 W5, DA M1 | must_fix | D3 → F2/F3 | sentence: §9 Conclusion, §6.5 summary sentence | claim_scope_unsupported → claim: §9 verdicts |
| R2 | REV-07 | Make the search reproducible: query strings, execution dates, and an identification/screening flow with counts | SC-5 | major | absence: §2.3 Survey method; expected queries, dates, and screening counts; checked §2.3, Table tab:corpus, Declarations, Introduction | 4 | R1 W1 | must_fix | D1 → F3 | section: §2.3 Survey method (+ Table tab:corpus) | method_reproducibility_unresolved → section: §2.3 |
| R3 | REV-08 | Run and report a search for real-hardware DSA graph evaluations (FPGA, silicon) as broad as the out-of-frame UPMEM search, or restrict the "DSAs lack silicon validation" and "unbalanced" claims to the searched frame | SC-4 | R1 W2 major; DA M5 major | text: §6.4 "On the DSA side, only ReGraph runs on real hardware" | R1 4; DA 4 | R1 W2, DA M5 | must_fix | D1, D3 → F2/F3 | new_data: additional search (§2.3, §6.4); or sentence: §6.4 | evidence_gap_remains → claim: §6.4 real-hardware asymmetry |
| R4 | REV-09 | Compare energy only within baseline classes, or downgrade "Energy is where the advantage of PIM is most consistent" to a qualitative mechanism argument; remove the cross-baseline PIM energy advantage from the conclusion | SC-2 | R1 W3 major; DA M6 major | text: §6.2 "Energy is where the advantage of PIM is most consistent"; text: §2.3 "we never place two numbers side by side unless they use the same class of baseline and the same substrate" | R1 4; DA 4 | R1 W3, DA M6 | must_fix | D1, D3 → F2/F3 | section: §6.2 Energy (+ §9) | claim_scope_unsupported → claim: §6.2 energy advantage |
| R5 | REV-10 | Reframe the sim-versus-silicon gap as an architectural difference observed on one commercial platform, with architecture class and fidelity confounded (Abstract, §6.4), unless a validation study of a simulated UPMEM model is cited; drop "mainly" | SC-3 | R1 W4 major; R2 W3 major; DA M5 major | text: Abstract "Real PIM hardware performs worse than simulated PIM, mainly because communication between PIM cores goes through the host." | R1 4; R2 4; DA 4 | R1 W4, R2 W3, DA M5 | must_fix | D1, D2, D3 → F2/F3 | sentence: Abstract; section: §6.4 | claim_scope_unsupported → claim: Abstract sim-vs-silicon sentence |
| R6 | REV-12 | Drop the claim that "graph PIM has been the more active design space since 2021", or support it with venue/year counts over a corpus that includes the in-window DSAs (see REV-16) | SC-7 | R1 W8 minor; R2 W2 major | text: §2.3 "This is partly a finding: since 2021, graph PIM has been the more active design space at the target venues" | R1 4; R2 4 | R1 W8, R2 W2 | must_fix | D1, D2 → F2/F3 | sentence: §2.3 | claim_scope_unsupported → claim: §2.3 activity claim |
| R7 | REV-15 | Add an instruction-offload / host-cooperative PIM class to the taxonomy and Table I; review PEI and GraphPIM; present Piccolo, FALA, and CoGraf as refinements of that line rather than "a new class" (verify references before citing) | SC-13 | major | text: §1 and §5 "A new class of hybrid designs has also appeared" and "It is evaluated against Piccolo, PEI, and GraphPIM" | 5 | R2 W1 | must_fix | D2 → F2/F3 | section: §2.2, §5, Table tab:corpus, §1 | evidence_gap_remains → section: §5 Hybrid designs |
| R8 | REV-16 | Add the in-window graph DSAs named by R2 (PolyGraph, Dalorex, ScalaGraph; GraphPulse as JetStream's base), after verifying each, or narrow and justify the static-DSA coverage claim | SC-14 | major | text: §2.3 "since 2021, graph PIM has been the more active design space at the target venues, while many graph DSAs are older" | 4 | R2 W2 | must_fix | D2 → F2/F3 | section: §4.1, Table tab:corpus, Table tab:designs | evidence_gap_remains → table: tab:corpus DSA-static rows |
| R9 | REV-17 | Limit the physical explanation of "static-only PIM" to partitioned PnM; acknowledge that for host-managed fine-grained or instruction-offload PIM the convenience explanation is not excluded; replace the "predicts the pattern we observe" test with one that distinguishes the two explanations, or present both as open | SC-11 | R2 W4 major; DA M4 major | text: §6.6 "The benefit of PIM depends on placing the data of each partition in the memory unit that computes on it"; text: §6.6 "We think the second explanation is stronger, because it predicts the pattern we observe." | R2 4; DA 4 | R2 W4, DA M4 | must_fix | D2, D3 → F2/F3 | section: §6.6 Mutability paragraph (+ §8 item 1) | claim_scope_unsupported → claim: §6.6 physical explanation |
| R10 | REV-25 | Define the predictability notion used (worst-case bound versus variability; analysable versus measured); rephrase "no upper bound" as "no tight or analysed bound"; drop the Spara example or recast it as a scaling result; state what bounded latency would require | SC-27 | major | text: §7 Predictability "This is good on average, but it has no upper bound in the worst case, because one update can affect the whole graph." | 4 | R3 W1 | must_fix | D4 → F5 | section: §7 Predictability | interpretive_ambiguity_remains → section: §7 Predictability |
| R11 | REV-26 | State an explicit adversary model per security property (attacker, observation/control, protected asset); place MGX and IMPACT within it; acknowledge address-trace leakage for DSAs without access-pattern obfuscation; align Table tab:critical | SC-28 | major | text: §7 Security "A DSA keeps the trust boundary at the memory controller, where conventional encryption can be used." | 4 | R3 W2 | must_fix | D4 → F5 | section: §7 Security, Table tab:critical | claim_scope_unsupported → claim: §7 security asymmetry |
| R12 | REV-30 | Revise or justify "Three of them separate the camps": the text says access granularity affects both camps, so either reclassify granularity (fine- versus coarse-grained, cutting across PIM/DSA) or show how it separates PIM from DSA | SC-33 | major | text: §6.6 "Three of them separate the camps." / "When each access brings little useful data, both conventional DSAs and coarse-grained PIM waste bandwidth" / "Fine-grained PIM mechanisms help both camps" | 4 | DA M2 | must_fix | D3 → F2/F3 | section: §6.6, Table tab:axes, Abstract, §9 | claim_scope_unsupported → claim: three separating axes |
| R13 | REV-31 | Treat graph size and communication symmetrically (both are conditional), or justify the asymmetry; reconcile with the axes-table size row (PIM + vs DSA ±); give a DSA basis for the high-traffic DSA "+" or change it to "?" | SC-34, SC-9c | major | table: Table tab:axes, rows Graph size >> on-chip (PIM +, DSA ±, Hyb. +) and High cross-partition traffic (DSA + with PIM-only basis citations) | 4 | DA M3 | must_fix | D3 → F2/F3 | section: §6.6 "other axes" paragraph; table: tab:axes | claim_scope_unsupported → table: tab:axes size and high-traffic rows |
| R14 | REV-32 | Present the mutability axis as a coverage gap within the venue-restricted corpus rather than as evidence that separates the camps; address the two named out-of-corpus counterexamples (assess them, or explain why exclusion does not affect the axis) | SC-12 | major | text: §6.6 "These two works are outside our corpus, so we do not assess them." | 4 | DA M4 | must_fix | D3 → F2/F3 | section: §6.6 Mutability, Table tab:axes Dynamic row | claim_scope_unsupported → claim: mutability axis |

### Required Item Details

**R1 (REV-04): Comparative verdicts exceed the paper's comparison rule**
- **Problem**: §9 says which camp is "better" per regime. §6.1 says no matched comparison exists. For evolving graphs, "DSAs are better" follows from the absence of a PIM competitor.
- **Source**: DA M1; R1 W5; EIC W4 (see Disagreement 1).
- **Requirement**: Restate the verdicts as evidence-coverage findings or hypotheses, for example "only DSAs currently support" or "the evidence favours".
- **Acceptance criteria**: No sentence in §9, §6.5, or the Abstract asserts a cross-camp "better" verdict without stating that it rests on indirect, unmatched evidence.

**R2 (REV-07): Search protocol not reproducible**
- **Problem**: The method describes "targeted web searches" with no query strings, execution dates, or screening counts, yet several conclusions are absence claims.
- **Source**: R1 W1.
- **Requirement**: Report the queries and their run dates, and add an identification and screening flow with counts.
- **Acceptance criteria**: §2.3 (or an appendix) lists every query with its date and source, plus identified, screened, excluded, and included counts that reconcile to the 30-entry corpus.

**R3 (REV-08): Asymmetric search for real-hardware evidence**
- **Problem**: All four UPMEM silicon studies come from outside the named venues, but no matching search for DSA FPGA or silicon evaluations is described. The "only ReGraph" and "unbalanced" statements may therefore be produced by the search itself.
- **Source**: R1 W2; DA M5 (second clause: "only PIM is held to silicon evidence").
- **Requirement**: Run and report an equally broad real-hardware DSA search, or restrict the claim to the searched frame.
- **Acceptance criteria**: §2.3 documents a real-hardware search that covers both camps, or §6.4 explicitly limits the DSA real-hardware claim to the searched frame.

**R4 (REV-09): Energy synthesis violates the comparison rule**
- **Problem**: Tesseract (versus host), GraphP (versus Tesseract), and CoGraf (DRAM-only, versus non-PIM) are combined into "most consistent" and contrasted with DSA savings measured against software and GPU baselines.
- **Source**: R1 W3; DA M6.
- **Requirement**: Make within-baseline-class comparisons only, or downgrade the claim to a qualitative mechanism argument, and update the conclusion to match.
- **Acceptance criteria**: §6.2 makes no cross-camp energy-advantage claim that relies on figures with different baseline classes, and §9 no longer lists a PIM energy advantage as measured.

**R5 (REV-10): Sim-versus-silicon gap confounded with architecture**
- **Problem**: The simulated HMC designs (GHz-class cores, inter-cube links) and UPMEM (DIMM DPUs, no inter-DPU path) are different architectures, so "mainly because" is unsupported.
- **Source**: R1 W4; R2 W3; DA M5.
- **Requirement**: State that the gap is observed on one commercial platform and that architecture class and fidelity are confounded. Alternatively, cite a validation study of a simulated UPMEM model.
- **Acceptance criteria**: The Abstract and §6.4 no longer attribute the gap "mainly" to host-mediated communication or to simulation optimism, and they name the confound.

**R6 (REV-12): "PIM more active since 2021" claim unsupported**
- **Problem**: R1's count at the named venues (three pure-PIM designs versus four DSAs since 2021) and R2's in-window DSA omissions both contradict the claim.
- **Source**: R1 W8; R2 W2 (see Disagreement 2).
- **Requirement**: Drop the claim, or support it with explicit counts over a corpus that includes the in-window DSAs.
- **Acceptance criteria**: §2.3 either no longer asserts relative activity, or gives venue/year counts by camp from which the stated conclusion follows.

**R7 (REV-15): PEI/GraphPIM lineage missing; hybrids presented as new**
- **Problem**: PEI (2015) and GraphPIM (2017) already used locality-aware host/PIM cooperation. The manuscript cites them only as FALA's baselines.
- **Source**: R2 W1.
- **Requirement**: Add a host-cooperative or instruction-offload PIM class, review PEI and GraphPIM after verifying the references, and recast the 2025–2026 hybrids as refinements.
- **Acceptance criteria**: The taxonomy (§2.2, Fig. 1, Table I) includes the class, PEI and GraphPIM are reviewed with verified citations, and the "new class" wording in §1 and §5 is removed or qualified.

**R8 (REV-16): In-window graph DSAs missing**
- **Problem**: R2 names PolyGraph, Dalorex, ScalaGraph, and GraphPulse, from memory, as relevant graph DSAs. Without them, the static-DSA camp has no ASIC design after 2019 except GraphWave.
- **Source**: R2 W2.
- **Requirement**: Verify each named work and add those that meet the inclusion criteria. Otherwise, narrow and justify the coverage claim.
- **Acceptance criteria**: Each named work is verified against a primary record and then either added to Table tab:corpus or listed with its exclusion reason. The coverage statement matches the resulting corpus.

**R9 (REV-17): Physical explanation of mutability over-generalised**
- **Problem**: The repartitioning argument holds for partitioned PnM but not for PIM on host-managed, interleaved data. The test "predicts the pattern we observe" does not discriminate, because both explanations predict that pattern.
- **Source**: R2 W4; DA M4 (rival-explanation clause).
- **Requirement**: Restrict the physical explanation to partitioned PnM and treat the convenience explanation as live for fine-grained and instruction-offload PIM. Optionally, link this to open challenge 1, as R2 suggests.
- **Acceptance criteria**: §6.6 scopes the physical explanation to partitioned PnM and no longer selects between explanations on a test both pass.

**R10 (REV-25): Predictability terminology**
- **Problem**: "No upper bound" is used where the bound is loose and unanalysed. Spara's scaling result is offered as timing variability. WCET and bounded latency are not defined.
- **Source**: R3 W1.
- **Requirement**: Define the timing notion, rephrase the claim, recast or drop the Spara example, and state what bounded latency would require.
- **Acceptance criteria**: §7 Predictability defines its timing notion, contains no "no upper bound" claim for finite-graph monotonic kernels, and presents the Spara evidence as a scaling result or omits it.

**R11 (REV-26): Security comparison lacks a threat model**
- **Problem**: MGX (off-chip memory attacker) and IMPACT (co-located software exploiting row-buffer channels) defend against or exploit different adversaries, yet the paper and Table tab:critical treat them as comparable. DSA address-trace leakage is not acknowledged.
- **Source**: R3 W2.
- **Requirement**: Give an adversary model per property, place each surveyed defence or attack within it, and add a sentence on DSA access-pattern leakage.
- **Acceptance criteria**: §7 Security names the attacker, the observation or control capability, and the protected asset for each comparison, and states that controller-side encryption does not hide the address trace.

**R12 (REV-30): Granularity axis does not separate the camps**
- **Problem**: The text says granularity affects both camps and that fine-grained mechanisms help both.
- **Source**: DA M2.
- **Requirement**: Reclassify the axis, or justify how it separates PIM from DSA, and revise the "three assumptions" thesis wherever it appears.
- **Acceptance criteria**: The Abstract, §6.6, Table tab:axes, and §9 state consistently which axes separate PIM from DSA, and the granularity axis is either justified as separating them or relabelled as cutting across the camps.

**R13 (REV-31): Asymmetric treatment of graph size; unsupported high-traffic DSA rating**
- **Problem**: Size is dismissed as conditional on communication, while communication, which is also conditional, is treated as decisive. The size row rates PIM and DSA differently. The high-traffic DSA "+" has only PIM sources in its Basis column.
- **Source**: DA M3.
- **Requirement**: Treat the two axes symmetrically or justify the asymmetry, and either add DSA evidence for the high-traffic cell or change it to "?".
- **Acceptance criteria**: The §6.6 "other axes" paragraph applies the same conditionality standard to size and communication, and every DSA-column cell in tab:axes cites at least one DSA source or reads "?".

**R14 (REV-32): Mutability axis inferred from absence**
- **Problem**: The axis rests on finding no PIM design for dynamic graphs within the chosen venues and years, while two works outside that frame are named and then excluded.
- **Source**: DA M4 (see Disagreement 3; R2 S4 supports keeping the scoped absence statement itself).
- **Requirement**: Present the axis as a coverage gap and address the two counterexamples.
- **Acceptance criteria**: §6.6 and Table tab:axes describe the dynamic-graph row as "no PIM design found in the searched frame", and the treatment of the two out-of-corpus works is justified explicitly.

### Suggested Revisions (Optional): 18 items

| Transport ref | Item | Revision Item | Sub-Claim(s) | Severity (transported) | Evidence Anchor | Confidence (transported) | Source | Obligation class | Mechanical link | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | REV-01 | Make Fig. 1 consistent with Table 1 / §5 on the hybrids (mark them as spanning levels or explain the bank-level placement); add SynCron, GraphWave, and ReGraph or explain their omission | SC-22 | minor | figure: Fig. 1 (fig:placement), row "DRAM bank / column (UPMEM, FGPIM)" lists Piccolo, FALA, CoGraf | 4 | EIC W1 | consider | D5 → F5 | other: Fig. 1 | editorial_conformance_unmet → figure: fig:placement |
| S2 | REV-02 | Give every tab:axes cell a supporting basis or change it to "?" (low-traffic row DSA/Hybrid "+"; graph-size row Hybrid "+"); state the coding rule for +, –, ±, ? | SC-9a, SC-9b, SC-10 | EIC W2 minor; R1 W6 minor | table: Table 4 (tab:axes), rows "Low cross-partition traffic" and "Graph size ≫ on-chip"; table: Table tab:axes, row "Low cross-partition traffic", DSA column | EIC 4; R1 3 | EIC W2, R1 W6 | should_fix | D1/D3, D5 → F2/F3/F5 | other: Table tab:axes (+ legend) | reader_traceability_reduced → table: tab:axes |
| S3 | REV-03 | Make the GraphDynS substrate label in Table 3 as specific as the other rows | SC-23 | minor | text: §4.1 Pipelines for static graphs "The design is implemented in RTL and evaluated with five algorithms on six real-world and five synthetic graphs" | 3 | EIC W3 | consider | D5 → F5 | sentence: Table tab:designs GraphDynS row | editorial_conformance_unmet → table: tab:designs |
| S4 | REV-05 | Name the research questions the surveyed literature addresses (brief requirement 3) in one short paragraph or table row | SC-24 | minor | absence: §1 Introduction and §2 Background; expected an explicit list of the key research questions the surveyed literature addresses (brief requirement 3); checked §1 sub-questions, §2.1–§2.3, §6 subsection headings, §8 open questions | 3 | EIC W5 | consider | D6 (pass) | sentence: §1 or §2 | acceptance_criterion_unmet → section: §1 |
| S5 | REV-06 | Add one or two stronger citations for safety- or security-critical uses of graph analytics to support §7's motivation (verify before citing) | SC-25 | EIC W6 minor; R3 W4 minor | text: §7 Properties for Critical Systems "Graph analytics supports applications such as network-security analysis [@asquini2025tc], where results must be trustworthy and delivered on time." | EIC 3; R3 3 | EIC W6, R3 W4 | should_fix | D4, D6 → F5 | sentence: §7 opening | evidence_gap_remains → claim: §7 motivation |
| S6 | REV-11 | Qualify "single-digit factor" as average-case, or drop "single-digit" (GraphQ 13.9x max; TDGraph 4.6–12.7x) | SC-31 | minor | text: §6.1 "Recent designs in both camps therefore improve on the best earlier design of their own camp by a single-digit factor." | 5 | R1 W7 | should_fix | D3 → F2/F3 | sentence: §6.1 | claim_scope_unsupported → claim: §6.1 single-digit |
| S7 | REV-13 | Add a threats-to-validity paragraph covering self-reported results, single-extractor AI-assisted coding, and availability of the extraction form | SC-32 | minor | absence: Survey method and Conclusion; expected a threats-to-validity statement covering author self-reported results, single-extractor AI-assisted coding, and access to the extraction form; checked §2.3, §6.4, §9, and Declarations | 4 | R1 W9 | should_fix | D1 → F3 | section: §2.3 or §9 | reporting_requirement_unmet → section: §2.3 |
| S8 | REV-14 | State one venue frame and apply it to every absence claim (§6.6 names four venues; §2.3 names five, including DSN) | SC-6 | minor | text: §6.6 "In our search of ISCA, MICRO, HPCA, and ASPLOS for 2021--2026, we found no PIM hardware design for streaming or evolving graphs." | 4 | R1 W10 | should_fix | D1 → F3 | sentence: §6.6, §2.3 | method_reproducibility_unresolved → claim: §6.6 absence scope |
| S9 | REV-18 | Name commercial bank-level PIM silicon (Samsung HBM-PIM/FIMDRAM; SK hynix AiM), state that no graph evaluation on it was found, and qualify "only UPMEM" (verify titles before citing) | SC-15 | minor | absence: §2.2 taxonomy and Table I; expected Samsung HBM-PIM and SK hynix AiM as the commercial bank-level PIM instances; checked §2.2, §3.4, §6.5, Table I, refs.bib | 4 | R2 W5 | should_fix | D2 → F2/F3 | section: §2.2, §6.5 | evidence_gap_remains → section: §2.2 |
| S10 | REV-19 | Add a digital DRAM processing-using-memory class (Ambit-style) to the taxonomy, since SISA uses in-DRAM bulk bitwise operations (verify reference before citing) | SC-16 | minor | text: §2.2 "with resistive crossbars performs analog sparse matrix--vector multiplication inside the memory array itself" | 4 | R2 W6 | should_fix | D2 → F2/F3 | section: §2.2, Fig. 1 | reader_traceability_reduced → section: §2.2 |
| S11 | REV-20 | Give the UPMEM DPU clock per system and describe the DPU as a fine-grained multithreaded core | SC-17 | minor | text: §3.4 "Each DRAM processing unit (DPU) is a 350 MHz in-order core" | 4 | R2 W7 | should_fix | D2 → F2/F3 | sentence: §3.4 | interpretive_ambiguity_remains → claim: §3.4 DPU description |
| S12 | REV-21 | Name SISA's baseline as an implementation and platform, not as the Bron–Kerbosch algorithm (check against the SISA paper) | SC-18 | minor | text: §3.3 "speedup over the Bron--Kerbosch maximal-clique algorithm" | 3 | R2 W8 | should_fix | D2 → F2/F3 | sentence: §3.3, Table tab:designs SISA row | reporting_requirement_unmet → claim: §3.3 SISA baseline |
| S13 | REV-22 | Justify classifying GraphWave as a static DSA, or move it to its own (compute-at-memory) class; check its use as DSA evidence in §6.4 and tab:axes | SC-19 | minor | text: §4.1 "GraphWave targets edge devices. It assigns one functional unit to every vertex" | 4 | R2 W9 | should_fix | D2 → F2/F3 | section: §4.1, Table tab:corpus | interpretive_ambiguity_remains → claim: GraphWave classification |
| S14 | REV-23 | Widen "discrete DSAs" in the RQ, or split core-attached units (HATS, TDGraph) into their own class, so that the camp boundary in §6 matches the RQ | SC-20 | minor | text: §1 "how do PIM architectures and discrete DSAs trade off throughput" | 4 | R2 W10 | should_fix | D2 → F2/F3 | sentence: §1 RQ (+ §2.2) | interpretive_ambiguity_remains → claim: RQ camp boundary |
| S15 | REV-24 | Position the survey against existing PIM surveys and primers (e.g., Mutlu et al.; Ghose et al.) as well as Gui et al. 2019 (verify references before citing) | SC-21 | minor | absence: §1 and §2.3 positioning; expected comparison with existing PIM surveys and primers (e.g., Mutlu et al., A Modern Primer on Processing in Memory) as well as the 2019 graph-accelerator survey; checked §1, §2.3, refs.bib | 4 | R2 W11 | should_fix | D2 → F2/F3 | sentence: §1 | evidence_gap_remains → section: §1 positioning |
| S16 | REV-27 | Limit the ECC claim for DSAs to stored data (not datapath or control; scratchpads not automatically protected); note the PIM/ECC asymmetry (in-DRAM compute below rank-level ECC) | SC-29 | minor | text: §7 Dependability "DSAs read and write conventional DRAM and on-chip SRAM, so standard memory protection, such as error-correcting codes (ECC), applies without change." | 3 | R3 W3 | consider | D4 → F5 | sentence: §7 Dependability, Table tab:critical | claim_scope_unsupported → claim: §7 ECC |
| S17 | REV-28 | Say what "delivered on time" means for the network-security use case and link it to the paper's mutability finding (such workloads are streaming; JetStream's small-batch advantage) | SC-26 | minor | text: §7 opening "Graph analytics supports applications such as network-security analysis [@asquini2025tc], where results must be trustworthy and delivered on time." | 3 | R3 W4 | consider | D4 → F5 | sentence: §7 opening | interpretive_ambiguity_remains → claim: §7 use case |
| S18 | REV-29 | Add working definitions of security (adversary class), dependability (attributes; designed-in imprecision versus faults), and predictability (timing notion) at the start of §7 | SC-30 | minor | absence: §7 Properties for Critical Systems; expected working definitions of the three assessed properties; checked §1 SQ4, §2, §7 opening and all three property paragraphs, Table tab:critical, §8 items 4 and 5 | 4 | R3 W5 | consider | D4 → F5 | section: §7 opening | interpretive_ambiguity_remains → section: §7 |

**Accuracy note on S11 (REV-20)**, from orchestrator verification notes (data). PrIM's system table lists the 2,556-DPU system at 350 MHz and the 640-DPU system at 267 MHz. R2's parenthetical in W7 has the two systems reversed. R2's underlying point stands: the manuscript gives one 350 MHz figure for both systems. Use the PrIM table, not the reviewer's parenthetical, when revising.

### Source-Traceability Checklist (immutable source order; no work order implied)

- [ ] REV-01 / S1: obligation `consider`. Fig. 1 hybrid placement and missing entries (EIC W1).
- [ ] REV-02 / S2: obligation `should_fix`. tab:axes cell basis and coding rule (EIC W2, R1 W6).
- [ ] REV-03 / S3: obligation `consider`. GraphDynS substrate label (EIC W3).
- [ ] REV-04 / R1: obligation `must_fix`. Restate the comparative verdicts (EIC W4, R1 W5, DA M1).
- [ ] REV-05 / S4: obligation `consider`. State the literature's own research questions (EIC W5).
- [ ] REV-06 / S5: obligation `should_fix`. Strengthen critical-systems motivation citations (EIC W6, R3 W4).
- [ ] REV-07 / R2: obligation `must_fix`. Reproducible search protocol (R1 W1).
- [ ] REV-08 / R3: obligation `must_fix`. Symmetric real-hardware search, or a scoped claim (R1 W2, DA M5).
- [ ] REV-09 / R4: obligation `must_fix`. Energy comparison within baseline classes (R1 W3, DA M6).
- [ ] REV-10 / R5: obligation `must_fix`. Sim-versus-silicon confound (R1 W4, R2 W3, DA M5).
- [ ] REV-11 / S6: obligation `should_fix`. "Single-digit factor" (R1 W7).
- [ ] REV-12 / R6: obligation `must_fix`. "PIM more active since 2021" claim (R1 W8, R2 W2).
- [ ] REV-13 / S7: obligation `should_fix`. Threats to validity (R1 W9).
- [ ] REV-14 / S8: obligation `should_fix`. One venue frame for absence claims (R1 W10).
- [ ] REV-15 / R7: obligation `must_fix`. PEI/GraphPIM lineage; hybrids not "new" (R2 W1). Verify references.
- [ ] REV-16 / R8: obligation `must_fix`. In-window graph DSAs (R2 W2). Verify references.
- [ ] REV-17 / R9: obligation `must_fix`. Scope of the physical mutability explanation (R2 W4, DA M4).
- [ ] REV-18 / S9: obligation `should_fix`. Commercial bank-level PIM silicon (R2 W5). Verify references.
- [ ] REV-19 / S10: obligation `should_fix`. DRAM processing-using-memory class (R2 W6). Verify reference.
- [ ] REV-20 / S11: obligation `should_fix`. UPMEM DPU clock per system (R2 W7; see accuracy note).
- [ ] REV-21 / S12: obligation `should_fix`. SISA baseline as an implementation (R2 W8).
- [ ] REV-22 / S13: obligation `should_fix`. GraphWave classification (R2 W9).
- [ ] REV-23 / S14: obligation `should_fix`. "Discrete DSAs" wording (R2 W10).
- [ ] REV-24 / S15: obligation `should_fix`. Positioning against PIM surveys (R2 W11). Verify references.
- [ ] REV-25 / R10: obligation `must_fix`. Predictability terminology (R3 W1).
- [ ] REV-26 / R11: obligation `must_fix`. Security threat model (R3 W2).
- [ ] REV-27 / S16: obligation `consider`. ECC scope and PIM/ECC asymmetry (R3 W3).
- [ ] REV-28 / S17: obligation `consider`. Network-security use case linked to mutability (R3 W4).
- [ ] REV-29 / S18: obligation `consider`. Define the three critical-systems properties (R3 W5).
- [ ] REV-30 / R12: obligation `must_fix`. Granularity axis and the "three separate" thesis (DA M2).
- [ ] REV-31 / R13: obligation `must_fix`. Size/communication asymmetry; high-traffic DSA cell (DA M3).
- [ ] REV-32 / R14: obligation `must_fix`. Mutability axis as a coverage gap; out-of-corpus works (DA M4).

**Count: 32 items. 14 are required (`must_fix`) and 18 are optional (12 `should_fix`, 6 `consider`).**

### Journal-Supplied Deadline (Optional Transport)

- **Exact deadline from source letter**: NOT PROVIDED. No deadline, duration, or work estimate is inferred.

### Response Letter Instructions

Please respond to every roadmap item (REV-01 to REV-32) using `templates/revision_response_template.md`. For each required item, describe the revision. For each optional item, say whether you adopted it or why not. Mark all changes in the revised manuscript, and include a cross-reference table of new section, table, and figure locations. Record any item you decline, with your reasoning. It will stay visible at re-review.

---

## Part 3: Appendix

### A. Reviewer report summaries

**Journal-Fit Reviewer (EIC)**. D5 warn ("inconsistent terminology or formatting"); D6 pass. Recommendation: not stated (sprint card). Key point: the manuscript meets every brief requirement (33 references, 22 from 2021–2026, about 10 pages, four comparative tables, a dedicated critical-systems section) and goes beyond summary by organising the evidence around deciding assumptions (S1–S5). Presentation is inconsistent in Fig. 1, tab:axes, and Table 3 (W1–W3). Rubric and motivation gaps are minor (W5, W6). The conclusion's verdicts are firmer than the comparison rule allows (W4, deferred to D3).

**Reviewer 1 (Methodology)**. D1 warn ("The protocol is stated but has gaps"); D3 warn ("Some secondary claims overgeneralize…"). Recommendation: not stated. Key point: the survey is more auditable than most (S1–S4), but its search cannot be reproduced (W1), was asymmetric for real hardware (W2), breaks its own rule in the energy section (W3), and confounds sim-versus-silicon with architecture (W4). Its "better" verdicts go too far (W5). Minor items: W6–W10. No recomputable statistics were found (arithmetic receipt: `no_recomputable_statistics`).

**Reviewer 2 (Domain)**. D2 block, repairable ("omission of several landmark or directly competing works…"). Recommendation: not stated. Key point: the per-paper numbers are accurate, with their baselines (S1–S5). Coverage omits the PEI/GraphPIM lineage (W1) and in-window graph DSAs (W2). Two headline technical claims are too broad (W3, W4). Minor accuracy and taxonomy items: W5–W11. Missing papers were named from memory, and R2 asked for verification.

**Reviewer 3 (Cross-disciplinary)**. D4 warn ("a missing or informal threat model, loose use of predictability language"). Recommendation: not stated. Key point: §7 is more than a gap list (S1–S5), but the predictability reasoning misuses worst-case terms (W1), the security comparison has no threat model (W2), and ECC, the use case, and the definitions need tightening (W3–W5). Performance-modelling detail is outside R3's stated competence.

**Devil's Advocate**. D3 block, repairable ("A load-bearing claim that the cited evidence does not support"). Recommendation: N/A, findings only. Key challenge: the evidence base can say which assumptions each camp has tested, but not which camp is better under them (M1). Two of the three axes do not cleanly separate the camps (M2, M3). The mutability axis rests on an absence (M4). The sim/silicon (M5) and energy (M6) claims break the paper's own rule. There are no CRITICAL findings. The DA's untabled minor remarks (workload-class summary mixing baselines; the three dynamic-DSA generations being simulation-only) have no finding ID. They are recorded here for transparency and are not itemised in the roadmap. The rival-explanation remark is part of M4 (REV-17, REV-32).

### B. Weakness sub-claim inventory (Step 1b)

Severity and confidence are transported from the cards. No `[SEVERITY-SOURCE: letter-fallback]` or `[CONFIDENCE-SOURCE: report-level]` tags were needed: every card weakness carries its own Severity and Confidence, and the DA carries them by table band. "Non-DA agree" counts EIC, R1, R2, and R3 only.

| sub_claim_id | Parent weakness | Positions (seat: position, severity, confidence) | Non-DA agree / conflict | DA | Disposition | Roadmap |
|---|---|---|---|---|---|---|
| SC-1 | Conclusion verdicts exceed the comparison rule | EIC W4: raised, minor, 3; R1 W5: raised, major, 4; R2/R3: not-mentioned | 2 / severity conflict | M1 major, 5 | SPLIT (severity) → arbitrated, Disagreement 1 | REV-04 |
| SC-2 | Energy synthesis breaks the comparison rule | R1 W3: raised, major, 4; others not-mentioned | 1 / 0 | M6 major, 4 | single-reviewer, DA-corroborated | REV-09 |
| SC-3 | Sim-vs-silicon gap confounded with architecture | R1 W4: raised, major, 4; R2 W3: corroborated, major, 4; EIC/R3: not-mentioned | 2 / 0 | M5 major, 4 | corroborated finding | REV-10 |
| SC-4 | Real-hardware search asymmetric (only PIM held to silicon) | R1 W2: raised, major, 4 | 1 / 0 | M5 major, 4 | single-reviewer, DA-corroborated | REV-08 |
| SC-5 | Search protocol not reproducible | R1 W1: raised, major, 4 | 1 / 0 | n/m | single-reviewer | REV-07 |
| SC-6 | Venue frame inconsistent across absence claims | R1 W10: raised, minor, 4 | 1 / 0 | n/m | single-reviewer | REV-14 |
| SC-7 | "PIM more active since 2021" unsupported | R1 W8: raised, minor, 4; R2 W2: corroborated, major, 4 | 2 / severity conflict | n/m | SPLIT (severity) → arbitrated, Disagreement 2 | REV-12 |
| SC-9a | tab:axes low-traffic row "+" lacks basis | EIC W2: raised, minor, 4; R1 W6: corroborated, minor, 3 | 2 / 0 | n/m | corroborated finding | REV-02 |
| SC-9b | tab:axes graph-size Hybrid "+" lacks basis | EIC W2: raised, minor, 4 | 1 / 0 | n/m | single-reviewer | REV-02 |
| SC-9c | tab:axes high-traffic DSA "+" has PIM-only basis | none | 0 non-DA | M3 major, 4 | DA finding | REV-31 |
| SC-10 | tab:axes has no coding rule | R1 W6: raised, minor, 3 | 1 / 0 | n/m | single-reviewer | REV-02 |
| SC-11 | Physical explanation of mutability over-generalised / non-discriminating test | R2 W4: raised, major, 4 | 1 / 0 | M4 major, 4 | single-reviewer, DA-corroborated | REV-17 |
| SC-12 | Mutability axis inferred from absence; counterexamples excluded | (R2 S4 supports the scoped absence statement itself; see Disagreement 3) | 0 non-DA | M4 major, 4 | DA finding | REV-32 |
| SC-13 | Hybrids presented as new; PEI/GraphPIM omitted | R2 W1: raised, major, 5 | 1 / 0 | n/m | single-reviewer | REV-15 |
| SC-14 | In-window graph DSAs missing | R2 W2: raised, major, 4 | 1 / 0 | n/m | single-reviewer | REV-16 |
| SC-15 | Commercial bank-level PIM silicon absent | R2 W5: raised, minor, 4 | 1 / 0 | n/m | single-reviewer | REV-18 |
| SC-16 | DRAM processing-using-memory class missing | R2 W6: raised, minor, 4 | 1 / 0 | n/m | single-reviewer | REV-19 |
| SC-17 | UPMEM DPU clock as a single value | R2 W7: raised, minor, 4 | 1 / 0 | n/m | single-reviewer (orchestrator accuracy note) | REV-20 |
| SC-18 | SISA baseline stated as an algorithm | R2 W8: raised, minor, 3 | 1 / 0 | n/m | single-reviewer | REV-21 |
| SC-19 | GraphWave classed as a static DSA | R2 W9: raised, minor, 4 | 1 / 0 | n/m | single-reviewer | REV-22 |
| SC-20 | "Discrete DSAs" versus core-attached units | R2 W10: raised, minor, 4 | 1 / 0 | n/m | single-reviewer | REV-23 |
| SC-21 | No positioning against PIM surveys | R2 W11: raised, minor, 4 | 1 / 0 | n/m | single-reviewer | REV-24 |
| SC-22 | Fig. 1 hybrid placement / missing entries | EIC W1: raised, minor, 4 | 1 / 0 | n/m | single-reviewer | REV-01 |
| SC-23 | GraphDynS substrate label | EIC W3: raised, minor, 3 | 1 / 0 | n/m | single-reviewer | REV-03 |
| SC-24 | Literature's own RQs not stated | EIC W5: raised, minor, 3 | 1 / 0 | n/m | single-reviewer | REV-05 |
| SC-25 | Critical-systems motivation rests on one workshop citation | EIC W6: raised, minor, 3; R3 W4: corroborated, minor, 3 | 2 / 0 | n/m | corroborated finding | REV-06 |
| SC-26 | Use case not linked to the mutability finding; "on time" undefined | R3 W4: raised, minor, 3 | 1 / 0 | n/m | single-reviewer | REV-28 |
| SC-27 | Predictability terminology misused | R3 W1: raised, major, 4 | 1 / 0 | n/m | single-reviewer | REV-25 |
| SC-28 | No threat model in the security comparison | R3 W2: raised, major, 4 | 1 / 0 | n/m | single-reviewer | REV-26 |
| SC-29 | ECC argument overstated; PIM/ECC asymmetry | R3 W3: raised, minor, 3 | 1 / 0 | n/m | single-reviewer | REV-27 |
| SC-30 | Critical-systems properties undefined | R3 W5: raised, minor, 4 | 1 / 0 | n/m | single-reviewer | REV-29 |
| SC-31 | "Single-digit factor" conflicts with reported numbers | R1 W7: raised, minor, 5 | 1 / 0 | n/m | single-reviewer | REV-11 |
| SC-32 | No threats-to-validity statement | R1 W9: raised, minor, 4 | 1 / 0 | n/m | single-reviewer | REV-13 |
| SC-33 | Granularity axis does not separate the camps | none | 0 non-DA | M2 major, 4 | DA finding (EIC S3 perspective; Disagreement 4) | REV-30 |
| SC-34 | Graph-size dismissal asymmetric | none | 0 non-DA | M3 major, 4 | DA finding | REV-31 |

(SC-8 is not used. The coverage half of R2 W2 is SC-14.)

### C. Corroboration summary (all five seats)

| Issue | Seats | Count (of 5) | Roadmap |
|---|---|---|---|
| Conclusion's "better" verdicts exceed the no-matched-comparison statement (SC-1) | EIC W4, R1 W5, DA M1 | 3 | REV-04 |
| Sim-vs-silicon gap confounds architecture with substrate (SC-3) | R1 W4, R2 W3, DA M5 | 3 | REV-10 |
| tab:axes cells unsupported by their Basis column (SC-9a/b/c, SC-10) | EIC W2, R1 W6, DA M3 | 3 | REV-02, REV-31 |
| Energy synthesis breaks the comparison rule (SC-2) | R1 W3, DA M6 | 2 | REV-09 |
| Real-hardware evidence asymmetry (SC-4) | R1 W2, DA M5 | 2 | REV-08 |
| "PIM more active since 2021" unsupported (SC-7) | R1 W8, R2 W2 | 2 | REV-12 |
| Physical mutability explanation over-generalised (SC-11) | R2 W4, DA M4 | 2 | REV-17 |
| Critical-systems motivation rests on one citation (SC-25) | EIC W6, R3 W4 | 2 | REV-06 |

Shared strengths (not roadmap items): baseline and substrate annotation of every headline number (EIC S2, R1 S1, R2 S1, DA body); correct contextualisation of GraphQ's 98.34x (R1 S4, R2 S2, DA body); inference labelled as inference in §7 (EIC body, R2 S5, R3 S2, DA body); scoped absence claims (R1 body, R2 S4, DA body).

### D. Quality-gate self-check

- All five committed cards were read and cited (EIC, R1, R2, R3, DA), together with their Phase 1 triggers.
- Consensus and disagreement are labelled. No CONSENSUS-4 or CONSENSUS-3 exists. There are two SPLITs and two DA-involved disagreements, each arbitrated with a rationale.
- The decision matches the mechanical contract output, and no fired action was softened.
- Every roadmap item traces to a seat finding ID. No issue was introduced that a seat did not raise. The orchestrator note was used only to correct a reviewer's parenthetical figure.
- Severity and confidence are transported unchanged.
- Manuscript text was treated as data. No instruction-like or reviewer-directed text was found (consistent with EIC body). The manuscript was not edited.

## Attachment: Acronym Check (advisory, #849)

### Acronym check (advisory; no reply needed)
Coverage: body (partial)
Not in this input: English abstract, Chinese abstract.
Not checked:
- Body, line 19: BFS (the initials before its parentheses do not spell it)
- Body, line 19: SSSP (the initials before its parentheses do not spell it)
- Body, line 21: DRAM (the initials before its parentheses do not spell it)
- Body, line 21: DSA (the initials before its parentheses do not spell it)
- Body, line 21: PIM (the initials before its parentheses do not spell it)
- Body, line 21: UPMEM (the initials before its parentheses do not spell it)
- Body, line 33: COO (the initials before its parentheses do not spell it)
- Body, line 39: PnM (the initials before its parentheses do not spell it)
- Body, line 43: ASIC (the initials before its parentheses do not spell it)
- Body, line 69: SpMV (the initials before its parentheses do not spell it)
- Body, line 73: ISA (the initials before its parentheses do not spell it)
- Body, line 79: CSR (the initials before its parentheses do not spell it)
- Body, line 85: RTL (the initials before its parentheses do not spell it)
- Body, line 87: BDFS (the initials before its parentheses do not spell it)
- Body, line 109: FGPIM (the initials before its parentheses do not spell it)
- Body, line 144: CPU (the initials before its parentheses do not spell it)
- Body, line 152: HATS (the initials before its parentheses do not spell it)
- Body, line 194: ECC (the initials before its parentheses do not spell it)
- Body, line 227: CRediT (the initials before its parentheses do not spell it)

| Scope | Line | Rule | Acronym | Uses |
|---|---|---|---|---|
| Body | 19 | Not defined | GB | 5 |
| Body | 25 | Not defined | GPU | 9 |
| Body | 25 | Not defined | SQ1 | 1 |
| Body | 25 | Not defined | SQ2 | 1 |
| Body | 25 | Not defined | SQ3 | 1 |
| Body | 25 | Not defined | SQ4 | 1 |
| Body | 43 | Not defined | ACM | 1 |
| Body | 43 | Not defined | ASPLOS | 2 |
| Body | 43 | Not defined | DSN | 1 |
| Body | 43 | Not defined | FPGA | 12 |
| Body | 43 | Not defined | HPCA | 2 |
| Body | 43 | Not defined | IEEE | 1 |
| Body | 43 | Not defined | ISCA | 2 |
| Body | 43 | Not defined | MGX | 4 |
| Body | 43 | Not defined | MICRO | 2 |
| Body | 49 | Not defined | SISA | 5 |
| Body | 50 | Not defined | GaaS | 5 |
| Body | 50 | Not defined | ReRAM | 9 |
| Body | 50 | Not defined | SPICE | 1 |
| Body | 51 | Not defined | ALPHA | 4 |
| Body | 51 | Not defined | PrIM | 3 |
| Body | 51 | Not defined | TC | 1 |
| Body | 53 | Not defined | MEGA | 5 |
| Body | 54 | Not defined | FALA | 6 |
| Body | 55 | Not defined | IMPACT | 5 |
| Body | 55 | Not defined | PiD | 1 |
| Body | 63 | Not defined | TB | 2 |
| Body | 69 | Not defined | GRAM | 1 |
| Body | 77 | Not defined | KB | 1 |
| Body | 77 | Not defined | MB | 3 |
| Body | 87 | Not defined | VO | 1 |
| Body | 89 | Not defined | GPGPU | 1 |
| Body | 89 | Not defined | GTEPS | 2 |
| Body | 105 | Not defined | DDR | 3 |
| Body | 107 | Not defined | HBM2 | 4 |
| Body | 107 | Not defined | PEI | 2 |
| Body | 109 | Not defined | DDR4 | 2 |
| Body | 145 | Not defined | CAM | 1 |
| Body | 145 | Not defined | MAC | 1 |
| Body | 194 | Not defined | SRAM | 1 |
| Body | 229 | Not defined | AI | 2 |
