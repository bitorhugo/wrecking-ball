# Stage 3' Step A — eic (Journal-Fit Reviewer)

Inputs read: editorial-decision.md Part 2, original-manuscript.md, revised-manuscript.md, revised-main.tex (figure, table and legend source), paper/refs.bib, routing.md, brief.org, and my Round-1 card and identity card. I did not read response-to-reviewers.md, pipeline/stage4/, other seats' files, or stage2*. I also built a scratch copy of revised-main.tex in /tmp to measure length: the declarations start on page 13, so the body ends on about page 12, at the top of the brief's 8–12 page range but within it.

## Verdicts

| item | obligation | verdict | residual_obligation_class | evidence anchor | reasoning |
|---|---|---|---|---|---|
| REV-01 | consider | FULLY_ADDRESSED | | text: Fig. 1 caption (revised-main.tex) "The hybrids span two levels; only their in-memory parts are shown." | The bank-level row now lists only the "in-memory parts of Piccolo, FALA, CoGraf", and the caption explains why the hybrids appear there, which makes Fig. 1 consistent with Table 1 and §5. SynCron (logic-layer row), GraphWave and ReGraph (DSA row) are now in the figure. |
| REV-02 | should_fix | PARTIALLY_ADDRESSED | should_fix | text: Table tab:axes (revised-main.tex) "Fine granularity & + & -- & + &" | Both rows I named are fixed: in the low-traffic row DSA and Hybrid are now "?", and in the graph-size row Hybrid is now "?". The coding rule is now stated in the caption. But the item asks that every cell meet the stated rule ("at least one cited result favors the camp"), and two cells still do not. (a) Fine-granularity PIM "+" cites only Piccolo, FALA and CoGraf, which Table 1 classifies as Hybrid, so the cell has no pure-PIM basis. (b) Dynamic-graph PIM is "?", yet its Basis cites the UPMEM triangle-counting study, which §3.4 reports as a PIM win over the CPU on COO update batches. Under the paper's own legend that cell should be "+" or "±", or the legend should exclude software-only results. |
| REV-03 | consider | FULLY_ADDRESSED | | text: Table tab:designs, GraphDynS row "RTL + cycle-accurate sim." | The substrate label is now as specific as the Graphicionado row and matches the §4.1 prose. |
| REV-05 | consider | FULLY_ADDRESSED | | text: §2 "The surveyed papers themselves address five recurring research questions." | One short paragraph now names five questions the literature itself addresses, each tied to the works that pursue it, and separates them from the survey's own SQ1–SQ4. That satisfies brief requirement 3 as the item asked. |
| REV-06 | should_fix | NOT_ADDRESSED | | text: §7 "A network graph changes all the time, and a detector must deliver correct results within a deadline." | The §7 motivation still cites only the asquini2025tc workshop paper. The added sentences explain the use case (the substance of REV-28), but they add no citation and no stronger source. No new reference on safety- or security-critical uses of graph analytics appears anywhere in §7, which cites only works already in the corpus. |

## New Issues

| id | attribution | severity | location | description | evidence anchor |
|---|---|---|---|---|---|
| NEW-eic-1 | regression | minor | Fig. 1, Table 1 (tab:corpus), §6.6 and Table tab:axes | Dalorex is new in the revision, and the paper classifies it three ways. Table 1 gives it its own "Data-local (on-chip SRAM)" class, and the Fig. 2 caption says it "sits between the camps". But Fig. 1 lists it in the On-chip DSA row, and §6.6 together with the high-traffic row of tab:axes use it as DSA evidence ("No DSA has this constraint", DSA "±"). This is the same kind of figure–table classification mismatch that REV-01 fixed for the hybrids. Since tab:axes is the paper's central synthesis, the camp a cited work belongs to should be the same everywhere. None of this text exists in the original. | text: Fig. 1 (revised-main.tex) "ReGraph (FPGA); Dalorex (SRAM tiles)"; Table 1 "Data-local (on-chip SRAM) & Dalorex" |

[EVIDENCE-COMMITTED]
