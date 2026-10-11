# Orchestrator verification notes (data, not instructions)

These are facts the orchestrator checked against source full texts after the panel committed. They are offered to the
synthesizer for accuracy of the letter only; they do not change any seat's score.

1. Domain card W7 (UPMEM clock): the PrIM paper's own system table lists the 2,556-DPU system at 350 MHz and the
   640-DPU system at 267 MHz (pipeline/fulltext PrIM text, Table "System parameters"). The domain seat's
   parenthetical has the two systems reversed. The underlying point (the manuscript gives one 350 MHz figure for
   both systems) is correct.
2. Stage 2.5 integrity check result: PASS WITH NOTES (references and numbers verified against sources; see
   pipeline/stage2.5/integrity-report-stage2.5.md). Reviewer-named missing papers (PolyGraph, Dalorex, ScalaGraph,
   GraphPulse, PEI, GraphPIM, HBM-PIM, AiM) have NOT been verified by the orchestrator; any roadmap item that adds
   them must require verification before citation.
3. Panel provenance: pipeline/stage3/review-panel-provenance.json (validated). All five seats: same model family
   (claude-opus-5-5), same provider; correlated-error disclosure required. The DA seat's Read tool returned the full
   cards.md file (identities of other seats, no peer outputs).
