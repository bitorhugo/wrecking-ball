contract_role: methodology

## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "The protocol is stated but has gaps"

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: warn
trigger: "Some secondary claims overgeneralize beyond the corpus or underweight contrary evidence"

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

I reviewed this as a structured narrative survey. Following the contract hint, methodology rigor here means four things: how the corpus was selected, how transparent the search was, how consistently the comparison rule was applied, and how the evidence was weighted. Statistics are not the test. The manuscript does better than most surveys in its area. It states a comparison rule and labels every headline number in the design table with its baseline and substrate. It also says which works were read only as abstracts, and it scopes its absence claims to its own search. Those features make the review auditable. They also expose problems. The search protocol cannot be reproduced at the level of queries and screening counts. The search frame was applied asymmetrically to real-hardware evidence. The paper's own comparison rule is broken in the Energy subsection. The headline sim-versus-silicon claim mixes a substrate effect with an architecture effect. On D3, the concluding "better" statements go further than evidence the paper itself says is missing, although the paper does hedge elsewhere. That hedge is why I score D3 warn rather than block. None of the defects reaches the fatal triggers I committed to in Phase 1. Baselines are disclosed throughout, so nothing is presented as like-for-like without disclosure. I also found no contradiction between the stated selection process and the corpus actually reported. I counted the corpus table at 30 entries, which matches the abstract. Twenty-two entries come from the five named venues and eight from outside them, which the "focused on" wording allows. Each weakness below is banded by its own impact on the decision.

### S1: Every headline number carries baseline and substrate
**Evidence Anchor**: table: Table tab:designs, columns Substrate and Headline result (baseline)

The design table pairs each reported gain with its baseline class and its evaluation substrate (simulation, FPGA emulation, or UPMEM silicon). This is the main thing that makes the survey's synthesis auditable.

### S2: An explicit comparison rule is stated up front
**Evidence Anchor**: text: §2.3 Comparison rule "we never place two numbers side by side unless they use the same class of baseline and the same substrate"

Few architecture surveys state a rule like this. It gives reviewers a standard to check the synthesis against (see W3).

### S3: Abstract-only sources are disclosed and their use is limited
**Evidence Anchor**: text: §2.3 "The two exceptions, MGX and NDMiner, are cited only for claims that appear in their abstracts."

The paper is open about where its extraction stops.

### S4: Misleading baselines in the source papers are corrected
**Evidence Anchor**: text: §3.1 "It is not a gain over earlier PIM"

The paper sets GraphQ's 98.34x single-node comparison apart from its gain over Tesseract. It also flags CoGraf's region-of-interest reporting (§5). Together these show that baselines were actually read and not just copied.

### W1: The search protocol cannot be reproduced
**Severity**: Major
**Evidence Anchor**: absence: §2.3 Survey method — expected search query strings, search execution dates, and counts of records identified, screened, and excluded; checked §2.3 text, Table tab:corpus, Declarations, and the introduction
**Confidence**: 4 — systematic-review methodology is my core area

The method names databases, a set of venues, a time window, and an inclusion criterion. However, it describes the search only as "targeted web searches" and gives no query strings, no execution dates, and no screening counts. Without them a second team cannot rebuild the corpus or estimate what was missed. This matters because several conclusions are absence claims (no dynamic-graph PIM, no DSA silicon, no dependability evaluation). Remedy: report the queries and the date each was run, and add a short identification and screening flow with counts.

### W2: The search frame was applied asymmetrically to real-hardware evidence
**Severity**: Major
**Evidence Anchor**: text: §6.4 "On the DSA side, only ReGraph runs on real hardware"
**Confidence**: 4 — based on the venue fields in the reference list against the stated search frame

All four UPMEM silicon studies come from outside the five named venues (IEEE Access, SIGMOD, IISWC, an IPDPS workshop). So the search went out of frame to find PIM real-hardware evidence. The method describes no matching search for DSA FPGA or silicon evaluations, for example at FPGA- or VLSI-oriented venues. The conclusion that DSAs lack real-silicon validation, and the "unbalanced" comparison in §6.4, may therefore be partly created by the search itself. Remedy: run and report an equally broad search for real-hardware DSA graph evaluations, or restate the claim as limited to the searched frame.

### W3: The paper's own comparison rule is broken in the Energy synthesis
**Severity**: Major
**Evidence Anchor**: text: §6.2 "Energy is where the advantage of PIM is most consistent"
**Confidence**: 4 — the rule and its violation are both in the text

This claim rests on figures placed side by side whose baselines differ. Tesseract's 87% is against a host server, GraphP's 89% is against Tesseract, and CoGraf's 88–94% counts DRAM energy only and is measured against a non-PIM baseline. These are then compared with DSA savings against software and a GPU. §2.3 forbids exactly this combination. Each number keeps its baseline label, so the comparison can still be audited and the fatal trigger does not apply. But a cross-camp "most consistent" conclusion cannot rest on figures the paper's own rule says are not comparable. Remedy: compare energy only within baseline classes, or downgrade the claim to a qualitative mechanism argument.

### W4: The sim-versus-silicon gap is confounded with a change of architecture
**Severity**: Major
**Evidence Anchor**: text: Abstract "Real PIM hardware performs worse than simulated PIM, mainly because communication between PIM cores goes through the host."
**Confidence**: 4 — evidence-tier weighting is in my focus area

The simulated designs (HMC with inter-cube links) and the silicon platform (UPMEM DIMMs with no DPU interconnect) are different architectures. The paper's own explanation, host-mediated communication, is an architectural property, not an artefact of simulation. A true sim-to-silicon gap would compare a simulated model of the same platform with measurements on it. As written, §6.4's claim that silicon studies "show a gap between simulation and silicon" overstates what the evidence-tier comparison can support. Remedy: present this as an architectural difference between the simulated and the commercial design points, unless the paper can cite a validation study of a simulated UPMEM model.

### W5: The concluding "better" claims go further than the paper's own statement that no matched comparison exists
**Severity**: Major
**Evidence Anchor**: text: §9 "PIM is better for stable graphs with little traffic between partitions."
**Confidence**: 4 — generalisation limits of a roughly 30-work corpus

§6.1 states that "No study in our corpus compares a PIM design and a DSA under matched conditions." Yet the conclusion says which camp is "better" for each regime. For evolving graphs, "DSAs are better" follows from the absence of a PIM competitor, not from a comparison. The paper does hedge elsewhere ("this survey can only ask"), so the main contribution, the identification of deciding assumptions, survives. The verdicts need to be restated as hypotheses supported by indirect evidence.

### W6: The assumption-axes table has no coding rule, and one rating has no basis
**Severity**: Minor
**Evidence Anchor**: table: Table tab:axes, row "Low cross-partition traffic", DSA column
**Confidence**: 3 — the coding judgement involves some domain knowledge

The +, –, ±, and ? ratings are given without a stated rule for assigning them. The DSA "+" on low cross-partition traffic cites only two PIM papers. State the coding rule and give a basis for each cell.

### W7: The "single-digit factor" synthesis conflicts with numbers the paper reports
**Severity**: Minor
**Evidence Anchor**: text: §6.1 "Recent designs in both camps therefore improve on the best earlier design of their own camp by a single-digit factor."
**Confidence**: 5 — the conflict can be checked against numbers in the paper itself

GraphQ reaches 13.9x maximum over Tesseract, and TDGraph reaches 4.6–12.7x over HATS. Qualify the claim as average-case, or drop "single-digit".

### W8: The justification for the corpus imbalance does not match the corpus
**Severity**: Minor
**Evidence Anchor**: text: §2.3 "This is partly a finding: since 2021, graph PIM has been the more active design space at the target venues"
**Confidence**: 4 — based on a count of venue and year fields in the reference list

Among the corpus works from 2021 onward at the five named venues, I count three pure-PIM designs (SISA, SynCron, NDMiner) and four DSAs (JetStream, TDGraph, ReGraph, MEGA). The PIM surplus comes from the out-of-venue UPMEM studies and from counting the hybrids as PIM. A targeted search also cannot by itself support a claim about the relative activity of two fields. Either drop the claim or support it with counts.

### W9: No threats-to-validity statement covers self-reported results or single-extractor coding
**Severity**: Minor
**Evidence Anchor**: absence: Survey method and Conclusion — expected a threats-to-validity statement covering author self-reported results, single-extractor AI-assisted coding, and access to the extraction form; checked §2.3, §6.4, §9, and Declarations
**Confidence**: 4 — standard systematic-review practice

Every headline number is self-reported by the designing authors against baselines they chose, which creates a favourable-reporting bias. The Declarations say AI tools extracted the data and one author checked it, but no extraction form is made available. One paragraph on these threats would close the gap.

### W10: The scope of absence claims is inconsistent with the stated venue frame
**Severity**: Minor
**Evidence Anchor**: text: §6.6 "In our search of ISCA, MICRO, HPCA, and ASPLOS for 2021--2026, we found no PIM hardware design for streaming or evolving graphs."
**Confidence**: 4 — the inconsistency is between two statements in the text

§2.3 names five venues including DSN, but this claim names four. The corpus also takes evidence from outside the named venues. State one frame and apply it to every absence claim.

## Arithmetic Receipts

no_recomputable_statistics: Checked all sections, Tables tab:corpus, tab:designs, tab:axes and tab:critical; the survey reports only speedup ratios, percentages, bandwidths and counts taken from cited works, with no test statistics, p-values, degrees of freedom, or means with SD and N, so none of p_from_test_statistic, grim, grimmer or n_from_df applies.
