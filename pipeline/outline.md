# Paper Outline + Evidence Map (Phase 2)

**Working title:** *Wrecking (Memory) Ball: Processing-in-Memory versus Domain-Specific Accelerators for Irregular Graph Workloads — A Critical Survey*
(Alternative, plainer title: *Moving Compute or Moving Data? A Comparative Survey of Processing-in-Memory and Domain-Specific Accelerators for Graph Analytics*)

**Thesis (one sentence):** PIM and DSAs attack different parts of the same memory wall: PIM removes data movement, while DSAs reshape computation around locality and time. The deciding factors are graph mutability, access granularity, and host-mediated communication, not graph size. The 2025–26 hybrids show that each camp's best ideas are being absorbed into one design.

**Budget:** about 7,000 words of body text + 4 tables + 2 figures, which fits roughly 10 IEEEtran pages. Rubric weights are shown in brackets.

| § | Section | Words | Purpose / SQ | Key evidence (corpus keys) |
|---|---------|------:|--------------|----------------------------|
| I | Introduction | 650 | Memory wall for graphs; the two philosophies; RQ + SQ1–4; contributions; scope (GNNs, GPUs, near-storage out) | tesseract, graphicionado, gui2019survey, prim |
| II | Background and Survey Method | 750 | Graph workload traits (CSR/COO, vertex programs, push/pull, traversal vs. mining); taxonomy of *where compute sits* (host → on-chip DSA → logic layer → bank/column → crossbar); method: venues, years, inclusion, **comparison rule**, corpus balance. **Table I**: corpus by camp/substrate/year. **Fig. 1**: compute-placement diagram | gui2019survey, kim2020dynamic, prim, all |
| III | PIM for Graphs | 1,350 | SQ1/SQ2. (A) 3D-stacked lineage: Tesseract → GraphP → GraphQ, framed as a fight against inter-cube communication; (B) analog ReRAM: GraphR → Spara → GaaS-X, trading precision and flexibility for energy (SpMV-only); (C) set-centric mining: SISA, NDMiner; (D) infrastructure: SynCron; (E) **real-hardware reality check**: PrIM (BFS limited by host-mediated sync), PimPam, ALPHA-PIM (utilization, partition sensitivity), GrAPL TC | tesseract, graphp, graphq, graphr, spara, gaasx, sisa, ndminer, syncron, prim, pimpam, alphapim, asquini2025tc |
| IV | Domain-Specific Accelerators | 1,150 | SQ1/SQ2. (A) static-graph pipelines: Graphicionado, HATS (online locality scheduling), GraphDynS (data-aware dynamic scheduling), GraphWave (edge, compute-at-memory on chip); (B) FPGA+HBM reference point: ReGraph; (C) **temporal lineage**: JetStream → TDGraph → MEGA (CommonGraph as software basis); concurrency (Glign, software) | graphicionado, hats, graphdyns, graphwave, regraph, jetstream, tdgraph, mega, commongraph, glign |
| V | Convergence: Hybrid Designs | 550 | Piccolo (built on a DSA baseline, adds in-memory scatter-gather; granularity mismatch with DDR), FALA (fine-grained column access + locality-aware PIM; beats Piccolo/PEI), CoGraf (FGPIM + tuple LLC coalescing; ROI-only results) | piccolo, fala, cograf |
| VI | Comparative Analysis [30%] | 1,450 | SQ2/SQ3. (A) Throughput; (B) energy; (C) bandwidth (internal vs. external; why the DSA bound is the pin bandwidth and the PIM bound is inter-unit links/host); (D) **evidence comparability** (simulation vs. silicon; baseline classes; ROI vs. end-to-end); (E) **assumption axes**: mutability, access granularity, partitionability/skew, capacity vs. graph size, concurrency, precision/programmability. **Table II**: per-design summary (substrate, baseline, headline *with baseline*, assumption). **Table III**: assumption-axis matrix (evidence for / against / untested) | extraction sheet rows; graphq C4, graphr C5 |
| VII | Critical-System Properties | 700 | Required by brief. Security (MGX for DSAs; IMPACT timing channels incl. GraphBIG defense eval; read-disturb amplification); dependability (ReRAM faults on stored adjacency, GraphR's error-tolerance claim vs. exact BFS/SSSP; read disturbance); predictability (data-dependent traversal timing, host-mediated sync, multi-tenant interference; Glign as nearest). **Table IV**: camp × property engagement | mgx, impact, yuksel2026pid, graphr, prim, glign |
| VIII | Open Challenges and Future Directions | 650 | (1) dynamic-graph PIM (static-partition assumption; MEMSYS'20 → no top-venue design; TC result as hint); (2) inter-PIM-core interconnect and host bypass; (3) evaluation methodology standards (real-hardware, end-to-end, common baselines); (4) cross-camp security/threat models; (5) fault tolerance for analog graph PIM; (6) programmability across the hybrid design space | kim2020dynamic, asquini2025tc, alphapim, prim, impact |
| IX | Conclusion | 400 | Critical synthesis: strengths/weaknesses/trade-offs per camp; answer to the RQ | — |
| — | References | — | about 30 entries (IEEE) | — |

**Figures**
- **Fig. 1** (§II): "Where does compute sit?", a TikZ stack (host CPU → on-chip DSA → memory controller → logic layer / buffer chip → DRAM bank/column → ReRAM crossbar) with representative designs at each level.
- **Fig. 2** (§V or §VI): lineage timeline 2015–2026, two tracks (PIM, DSA) converging into the hybrid track (Piccolo 2025, FALA 2025, CoGraf 2026), with the dynamic-graph branch only on the DSA track.

**Argument guards (from devil's-advocate notes)**
- Never place numbers with different baselines in the same comparison. Table II states the baseline in every cell.
- Present two explanations for "no dynamic PIM": tooling/simulator convenience vs. the physical cost of re-partitioning bank-local data. Argue for the second, but keep the first.
- Absence claims are written as "not found in {ISCA, MICRO, HPCA, ASPLOS} 2021–2026 in our search".
- Labels: CommonGraph and Glign = software; GrAPL TC and the ICS'26 paper = workshop; IMPACT cited as its DSN'25 version.
- Corpus imbalance (more PIM than DSA) is disclosed in §II as a finding.

**Files to produce (Phase 4)**: `paper/main.tex`, `paper/refs.bib`, `paper/declarations.tex` (separate, as requested), `paper/main.md` (review copy).
