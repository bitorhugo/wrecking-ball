contract_role: eic
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: warn
trigger: "inconsistent terminology or formatting"

### D6: venue_fit_and_contribution
score: pass

## Review Body

I read this as an instructor grading against the course brief (brief.org), as my Phase 1 plan committed. Venue fit therefore means: does the survey cover the brief's required elements, meet the reference and length expectations, use comparative tables, discuss critical-system properties, and go beyond summary? On all of these the manuscript does well. It sets a stated research question and four sub-questions. It reviews PIM, DSA, and hybrid designs as competing approaches. It applies an explicit comparability rule. It uses four comparative tables and two figures. It gives a full section to security, dependability, and predictability, lists six open directions, and ends with a synthesis that takes a position. By my count the reference list has 33 entries. Of these, 22 date from 2021 to 2026, and all but one (an arXiv preprint cited only for context) are peer-reviewed venues, which meets requirement 8 of the brief. The coordinator reports a rendered body of about 10 pages, which is within the 8 to 12 page range of requirement 9. D6 therefore passes.

The contribution goes beyond summary. The paper reorganises the evidence by deciding assumption (mutability, access granularity, communication topology) instead of by camp. That reframing is the paper's own, and it is argued from the cited evidence. The paper also reports every headline number with its baseline and substrate, which a grader would credit under critical analysis. The critical-systems section offers original inferences, for example about graph-structure leakage through row-buffer timing and about reachability errors from faulty crossbar cells. It labels them correctly as inference, not as surveyed findings.

D5 gets a warn. The problems are local presentation inconsistencies that a reader can work around but should not have to. The figures and tables do not always classify the hybrid designs the same way. The assumption-axes table gives some cells a verdict that its Basis column does not support. One substrate label in the main comparison table differs from the prose. None of these stops a reader from following the comparison, so the score is warn, not block. Each is a minor revision.

I also note, for the owning seats rather than as a score: the conclusion's ranking of the camps per workload is stated more firmly than the paper's own comparability rule allows. That belongs to D3 and is recorded below as a Minor finding only for its effect on how the contribution reads to a grader. I found no instruction-like or reviewer-directed text in the manuscript.

### S1: Full coverage of the brief's required elements
**Evidence Anchor**: text: §1 Introduction "We divide this question into four sub-questions."
The introduction sets a research question with four sub-questions, maps them to sections, and lists contributions. Together with Sections 6 to 8 and the conclusion, every numbered requirement of the brief has a dedicated home.

### S2: Explicit comparability rule applied throughout
**Evidence Anchor**: text: §2.3 Survey method "we never place two numbers side by side unless they use the same class of baseline and the same substrate"
This is the main reason the survey reads as critical analysis rather than a catalogue of speedups. The main comparison table states that its numbers cannot be compared across rows.

### S3: Original synthesis by deciding assumption
**Evidence Anchor**: text: §6 Which assumptions decide? "maps the evidence onto six assumptions. Three of them separate the camps."
Reframing the PIM-versus-DSA question around mutability, granularity, and communication topology is a contribution of the author's own. It is the kind of added value the brief asks for.

### S4: Critical-systems discussion with a dedicated table
**Evidence Anchor**: table: Table 5 (tab:critical), rows Security, Dependability, Predictability
The brief requires an explicit discussion of system properties for critical-systems topics. Section 7 covers three such properties per camp and says honestly where nothing has been studied.

### S5: Reference base meets the brief
**Evidence Anchor**: dataset: paper/refs.bib, 33 entries, 22 dated 2021 to 2026, 32 conference or journal entries
The base exceeds the minimum of 20, is mostly recent, and draws mainly on ISCA, MICRO, HPCA, ASPLOS, and DSN, which are the brief's suggested venues.

### W1: Hybrid designs classified inconsistently between the taxonomy figure and the corpus table
**Severity**: Minor
**Evidence Anchor**: figure: Fig. 1 (fig:placement), row "DRAM bank / column (UPMEM, FGPIM)" lists Piccolo, FALA, CoGraf
**Confidence**: 4 — direct comparison of figure source against Table 1 and Section 5
Fig. 1 puts the three hybrids in the same bank-level PIM row as PrIM and the UPMEM studies. Table 1 and Section 5 treat them as a separate Hybrid camp that keeps control and reuse on the processor side. The taxonomy figure should either mark the hybrids as spanning levels or say why they are placed at bank level. Fig. 1 also leaves out SynCron, GraphWave, and ReGraph, which appear in Table 1.

### W2: Assumption-axes table gives verdicts its Basis column does not support
**Severity**: Minor
**Evidence Anchor**: table: Table 4 (tab:axes), rows "Low cross-partition traffic" and "Graph size ≫ on-chip"
**Confidence**: 4 — cell-by-cell check of verdicts against cited basis
The low-traffic row marks all three camps "+", but its Basis column cites only PIM sources (PrIM, PimPam), so the row neither separates the camps nor is supported for DSA or Hybrid. The graph-size row gives Hybrid "+", but no hybrid work is cited in its Basis. Either add the supporting citations or change those cells to "?". Since the paper presents this table as its central synthesis, its cells should match the stated legend exactly.

### W3: Substrate label for GraphDynS differs between table and prose
**Severity**: Minor
**Evidence Anchor**: text: §4.1 Pipelines for static graphs "The design is implemented in RTL and evaluated with five algorithms on six real-world and five synthetic graphs"
**Confidence**: 3 — prose versus Table 3 label; did not check the primary source
Table 3 lists the GraphDynS substrate only as "simulation", while Graphicionado gets "RTL + DRAMSim2". Since the paper's comparison rule depends on substrate labels, the labels in Table 3 should be equally specific for every row.

### W4: Conclusion ranks the camps more firmly than the comparability rule allows
**Severity**: Minor
**Evidence Anchor**: text: §9 Conclusion "PIM is better for stable graphs with little traffic between partitions. DSAs are better for evolving graphs"
**Confidence**: 3 — editorial reading; the substantive call belongs to the D3 seat
Section 6 states that no study in the corpus compares PIM and DSA under matched conditions. The "better for evolving graphs" verdict also rests on PIM designs being absent from the search, not on a measured comparison. Phrasing the conclusion as "the evidence favours" or "only DSAs currently support" would keep the synthesis consistent with the paper's own rule, at no cost to the contribution.

### W5: The literature's own research questions are not stated separately from the survey's questions
**Severity**: Minor
**Evidence Anchor**: absence: §1 Introduction and §2 Background — expected an explicit list of the key research questions the surveyed literature addresses (brief requirement 3); checked §1 sub-questions, §2.1 to §2.3, §6 subsection headings, §8 open questions
**Confidence**: 3 — rubric interpretation; the material exists implicitly
The paper states its own RQ and SQ1 to SQ4, and Section 8 asks forward-looking questions. The questions the surveyed designs themselves set out to answer (for example, how to scale PIM communication, how to recover locality online, how to support incremental updates) are only implicit in the section narratives. One short paragraph or table row naming them would make the rubric item clearly satisfied.

### W6: Critical-systems relevance of graph analytics rests on a single workshop citation
**Severity**: Minor
**Evidence Anchor**: text: §7 Properties for Critical Systems "Graph analytics supports applications such as network-security analysis [@asquini2025tc], where results must be trustworthy and delivered on time."
**Confidence**: 3 — check of the citation supporting the section's motivation
The brief's critical-systems clause applies only to critical-systems topics. The paper's case that graph analytics is one cites a single workshop paper about triangle counting. One or two stronger citations for safety- or security-critical uses of graph analytics would better justify the section, which is otherwise one of the paper's strengths.
