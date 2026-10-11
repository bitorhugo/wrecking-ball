contract_role: domain

## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: block
trigger: "omission of several landmark or directly competing works such that the coverage of either compared camp is materially incomplete"
block_class: repairable

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

I read this as a PIM and near-data processing architect who knows the HMC, UPMEM, and HBM-PIM lines and the graph-accelerator literature. The per-paper numbers I could check from memory are reported accurately and with their baselines. This is uncommon in surveys of this area and it is the paper's main domain strength. The problems are in coverage and in how the field's history is told. The survey leaves out the instruction-offload PIM line (PEI, GraphPIM). It cites both as FALA baselines, but does not review them. Leaving them out makes the 2025--2026 hybrids look like a new class, when locality-aware host/PIM cooperation dates to 2015. The survey also leaves out graph DSAs inside its own venue and time window (for example PolyGraph at ISCA 2021). That weakens the statement that graph PIM has been the more active design space since 2021. Two headline technical claims are stated more broadly than the evidence allows. The first is that real PIM hardware is worse than simulated PIM because of host-mediated communication. The second is the physical explanation for why PIM has not handled mutability. Both can be fixed in revision without rethinking the thesis. Taken together, they reach my Phase 1 block threshold for D2 (repairable). No single defect invalidates the core thesis, so I do not apply the fatal class.

Where I name missing papers below, I give authors, venue, and year from memory and flag any detail I am unsure of. The author should check each one before citing it.

### W1: Hybrid host/PIM cooperation is presented as new; PEI and GraphPIM lineage omitted
**Severity**: Major
**Evidence Anchor**: text: §1 and §5 "A new class of hybrid designs has also appeared" and "It is evaluated against Piccolo, PEI, and GraphPIM"
**Confidence**: 5 — direct familiarity with the PEI/GraphPIM/FALA line

The manuscript names PEI and GraphPIM only as FALA's baselines. It never reviews them. PEI (J. Ahn, S. Yoo, O. Mutlu, K. Choi, "PIM-Enabled Instructions: A Low-Overhead, Locality-Aware Processing-in-Memory Architecture," ISCA 2015) already proposed what §5 credits to FALA: a locality monitor that sends each operation either to host caches or to memory-side PIM. GraphPIM (L. Nai, R. Hadidi, J. Sim, H. Kim, P. Kumar, H. Kim, "GraphPIM: Enabling Instruction-Level PIM Offloading in Graph Computing Frameworks," HPCA 2017) offloads graph atomics from host cores to HMC atomic units. It keeps the host in control and the data layout conventional. That is the hybrid recipe that §5 says the 2025--2026 designs introduced ("minimum function in memory ... control and data reuse on the processor side"). The convergence narrative and the claim of a "new class" therefore misrepresent the history. Minimum fix: add an instruction-offload or host-cooperative PIM class to the taxonomy and Table I, review PEI and GraphPIM, and present Piccolo, FALA, and CoGraf as refinements of that line (fine-grained column access, coalescing, burst-granularity scatter-gather), not as its start.

### W2: In-window graph DSAs are missing, which weakens the "PIM more active since 2021" claim
**Severity**: Major
**Evidence Anchor**: text: §2.3 "since 2021, graph PIM has been the more active design space at the target venues, while many graph DSAs are older"
**Confidence**: 4 — confident in the main omissions; venue/year details for the secondary ones flagged below

Several graph DSAs published at the stated venues within 2021--2026 are missing. The clearest is PolyGraph (V. Dadu, S. Liu, T. Nowatzki, "PolyGraph: Exposing the Value of Flexibility for Graph Processing Accelerators," ISCA 2021). It is directly relevant because it studies the sync/async and push/pull choices that §2.1 treats as design axes. Dalorex (M. Orenes-Vera, E. Tureci, D. Wentzlaff, M. Martonosi, HPCA 2023) is a data-local, task-based architecture for memory-bound graph and sparse workloads. It sits right on the PnM/DSA boundary this survey is about. ScalaGraph (P. Yao et al., HPCA 2022; I am fairly but not fully certain of the author list) is a scalable spatial graph accelerator. GraphPulse (S. Rahman, N. Abu-Ghazaleh, R. Gupta, MICRO 2020) is mentioned only indirectly as JetStream's base, even though the 6x asynchronous advantage cited in §2.1 comes from it. Because these are missing, the static-DSA camp in Table I has no ASIC design after 2019 except GraphWave. The statement about relative activity rests on an incomplete sample, and the "DSA, static" coverage is materially incomplete for 2021--2026. Fix: add these works, or narrow and justify the activity claim.

### W3: The silicon-versus-simulation gap mixes architecture class with evaluation fidelity
**Severity**: Major
**Evidence Anchor**: text: Abstract "Real PIM hardware performs worse than simulated PIM, mainly because communication between PIM cores goes through the host."
**Confidence**: 4 — working knowledge of UPMEM and HMC-PIM design points

All of the "real PIM hardware" evidence comes from one platform, UPMEM. UPMEM is a DIMM-based PnM design with slow multithreaded in-order DPUs and modest per-DPU MRAM bandwidth (roughly hundreds of MB/s per DPU in PrIM's measurements; the author should check the exact figure). The simulated designs it is compared with (Tesseract, GraphQ) are HMC logic-layer designs with GHz-class cores, a vault-level bandwidth budget, and inter-cube links by design. The gap therefore reflects a different architecture as well as the difference between simulation and silicon. Host-mediated communication is one cause, and the manuscript makes that case well (§3.4). But "mainly" is not supported unless the comparison controls for core capability and per-unit bandwidth. No surveyed study isolates these factors. The abstract and §6.4 should say that the gap is observed on one commercial platform and that architecture class and fidelity are confounded. Alternatively, they should bring in silicon PIM evidence from other platforms (see W5). Graph workloads have, to my knowledge, not been run on those platforms, and the survey should say so.

### W4: The physical explanation for "static-only PIM" does not cover instruction-offload and fine-grained PIM
**Severity**: Major
**Evidence Anchor**: text: §6.6 "The benefit of PIM depends on placing the data of each partition in the memory unit that computes on it"
**Confidence**: 4 — the mechanism argument follows from how the cited designs map data

The mutability argument (repartitioning moves data through the narrow path PIM is meant to avoid) is technically sound for partitioned PnM: Tesseract/GraphQ vaults and UPMEM banks. It does not cover PIM that operates on host-managed, address-interleaved data. That includes GraphPIM-style atomic offload, FALA's per-bank reduce units, and CoGraf's bank-parallel FGPIM. In those designs the host owns the layout, and an edge insertion does not force any repartitioning beyond what a conventional system or a DSA would do. For that subclass, the observation that no dynamic-graph design exists is better explained by research focus (the "convenience" explanation, which the paper rejects) than by physics. Within the stated venues and window, I know of no PIM hardware design for streaming graphs, so the empirical part of the mutability claim holds. The explanation should be limited to partitioned PnM. The paper should also say that fine-grained and instruction-offload PIM are the most plausible route to dynamic graphs. This strengthens open challenge 1 rather than weakening it.

### W5: Commercial bank-level PIM silicon is absent from the taxonomy
**Severity**: Minor
**Evidence Anchor**: absence: §2.2 taxonomy and Table I — expected Samsung HBM-PIM and SK hynix AiM as the commercial bank-level PIM instances; checked §2.2, §3.4, §6.5, Table I, refs.bib
**Confidence**: 4 — confident these exist; exact paper titles flagged

The "fine-grained / bank-level PIM" class is illustrated only by simulated designs (CoGraf, FALA), yet commercial silicon exists. One example is Samsung HBM-PIM / FIMDRAM: S. Lee et al., "Hardware Architecture and Software Stack for PIM Based on Commercial DRAM Technology," ISCA 2021, and Y.-C. Kwon et al., ISSCC 2021. Another is SK hynix AiM (S. Lee et al., GDDR6-based Accelerator-in-Memory, ISSCC 2022; I am less certain of the exact title). FALA's "up to 50% area overhead" claim (§5) refers to exactly these products. The survey should name them, state that no graph evaluation on them was found, and qualify "only UPMEM" (§6.5) accordingly. They also lack direct inter-bank communication, which would make the host-communication argument more general.

### W6: The taxonomy leaves out DRAM-based processing-using-memory, which SISA itself uses
**Severity**: Minor
**Evidence Anchor**: text: §2.2 "with resistive crossbars performs analog sparse matrix--vector multiplication inside the memory array itself"
**Confidence**: 4 — standard PnM/PuM terminology

The taxonomy limits processing-using-memory to analog ReRAM. §3.3, however, describes SISA's use of in-DRAM bulk bitwise operations. These are Ambit-style DRAM processing-using-memory (V. Seshadri et al., MICRO 2017) and do not fit any listed class. Adding a digital DRAM processing-using-memory class would also make the read-disturbance discussion in §7 easier to place.

### W7: The UPMEM DPU clock is stated as a single value
**Severity**: Minor
**Evidence Anchor**: text: §3.4 "Each DRAM processing unit (DPU) is a 350 MHz in-order core"
**Confidence**: 4 — recollection of PrIM's system table

As I recall, PrIM's two systems run at different DPU frequencies: about 267 MHz for the 2,556-DPU system and 350 MHz for the 640-DPU system. Since §3.4 compares the two systems' speedups, the clock should be given per system ("up to 350 MHz"). Describing the DPU as a fine-grained multithreaded core (up to 24 hardware threads) would also be more accurate than "in-order core".

### W8: The SISA baseline is described as an algorithm rather than an implementation
**Severity**: Minor
**Evidence Anchor**: text: §3.3 "speedup over the Bron--Kerbosch maximal-clique algorithm"
**Confidence**: 3 — recollection of SISA's evaluation framing

Bron--Kerbosch is the algorithm that both SISA and its baseline run. As I recall, SISA's >10x is measured against tuned non-PIM (set-based) implementations, not against the algorithm. The baseline should be named as an implementation and platform, as the paper's own comparison rule requires.

### W9: GraphWave, a compute-at-memory design, is classed as a static DSA
**Severity**: Minor
**Evidence Anchor**: text: §4.1 "GraphWave targets edge devices. It assigns one functional unit to every vertex"
**Confidence**: 4 — GraphWave's own title describes it as compute-at-memory

GraphWave's title calls it "A Highly-Parallel Compute-at-Memory Graph Processing Accelerator". It places a functional unit with each vertex's on-chip storage, which is closer to near-SRAM computing than to a Graphicionado-style pipeline. It is used as DSA evidence in §6.4 and Table VI ("graph size"). Either justify the classification or move it into its own class.

### W10: The research question names "discrete DSAs", but the DSA set includes core-attached units
**Severity**: Minor
**Evidence Anchor**: text: §1 "how do PIM architectures and discrete DSAs trade off throughput"
**Confidence**: 4 — from HATS and TDGraph's stated integration points

HATS and TDGraph are engines attached to each core and sitting in front of the private cache hierarchy (§4.1, §4.3 say so). They are not discrete accelerators. TDGraph is one of the three dynamic-graph "DSAs" behind the mutability conclusion. The wording of the research question should be widened, or the class should be split, so that the camp boundary used in §6 matches the research question.

### W11: The survey does not position itself against existing PIM surveys
**Severity**: Minor
**Evidence Anchor**: absence: §1 and §2.3 positioning — expected comparison with existing PIM surveys and primers (e.g., Mutlu et al., A Modern Primer on Processing in Memory) as well as the 2019 graph-accelerator survey; checked §1, §2.3, refs.bib
**Confidence**: 4 — well-known reference works in the area

The only prior survey cited is Gui et al. (2019, graph accelerators). PIM-side overviews are not cited. Examples are O. Mutlu, S. Ghose, J. Gómez-Luna, R. Ausavarungnirun, "A Modern Primer on Processing in Memory" (arXiv 2020; later a Springer book chapter, year uncertain) and S. Ghose et al., "Processing-in-memory: A workload-driven perspective" (IBM J. Res. Dev., 2019). Citing them would show what this survey's head-to-head framing adds.

### S1: Every headline number is given with its baseline and substrate
**Evidence Anchor**: text: §2.3 "we never place two numbers side by side unless they use the same class of baseline and the same substrate"

The figures I could check (Tesseract 8 TB/s and 87% energy, GraphR 16.01x/33.82x and 1.16--4.12x over PIM, GraphQ 3.3x/13.9x/81%, PrIM 93.0x/27.9x, MGX 33%->5%) match the original papers as I remember them. Table II's baseline column is accurate.

### S2: GraphQ's 98.34x figure is correctly put in context
**Evidence Anchor**: text: §3.1 "It is not a gain over earlier PIM"

This figure is often misquoted as a gain over Tesseract. The manuscript correctly identifies it as a capacity-scaling result against a single conventional node.

### S3: The UPMEM host-communication bottleneck is described accurately and mechanistically
**Evidence Anchor**: text: §3.4 "After every BFS iteration, the host merges the frontiers of all DPUs one after another and sends them back."

The description of serialized frontier merging, and of PimPam's optimizations as workarounds for platform limits, matches the PrIM, PimPam, and ALPHA-PIM findings.

### S4: Absence claims are scoped, and near-miss counterexamples are disclosed
**Evidence Anchor**: text: §6.6 "These two works are outside our corpus, so we do not assess them."

The mutability claim is limited to named venues and years, and the out-of-corpus dynamic-graph CIM and PIM works are disclosed. This is the right epistemic stance. I know of no in-window PIM hardware design for streaming graphs that contradicts it.

### S5: The PIM security discussion is technically accurate and separates evidence from inference
**Evidence Anchor**: text: §7 "This is our own inference: IMPACT's side channel targets other applications"

The trust-boundary argument (PIM computes inside the boundary where data must be plaintext) is correct. The paper labels its graph-structure leakage hypothesis as inference rather than as a reported result.
