import sys
p=sys.argv[1]; t=open(p).read()
def rep(a,b):
    global t
    assert a in t, a[:70]; t=t.replace(a,b,1)
# DSA
rep("GraphDynS identifies data-dependent behaviour as the root of the irregularity. It decouples the datapath so that dependencies are visible at runtime and schedules work, accesses, and computation dynamically.",
"GraphDynS identifies data-dependent behaviour as the root of the irregularity. Its Dispatching/Processing programming model decouples the datapath so that data dependencies can be extracted at runtime. A data-aware scheduler then balances work across lanes, issues edge accesses in an order that exploits the extracted dependencies, and skips vertices that were not updated, which targets all three irregularities at once. The design is implemented in RTL and evaluated with five algorithms on six real-world and five synthetic graphs~\\cite{yan2019graphdyns}.")
rep("TDGraph attaches a topology-driven accelerator to each core of a many-core processor.",
"TDGraph couples a topology-driven engine to each core of a many-core processor. The engine sits between the core and its private L2 cache and operates on virtual addresses through the core's TLB, so it shares the conventional memory hierarchy instead of replacing it~\\cite{zhao2022tdgraph}.")
rep("The lesson for our comparison is that once external bandwidth is plentiful,",
"ReGraph is also the one design in our DSA set that runs on real hardware end to end, so its numbers include effects, such as routing and resource limits, that simulation typically omits. The lesson for our comparison is that once external bandwidth is plentiful,")
# Hybrid
rep("Second, all three keep the static-graph assumption:",
"The hybrids also inherit a limitation from each camp. From the DSA side, they inherit dependence on tiling and cache reuse, which is strongest when the working set is stable. From the PIM side, they inherit the need for modified memory parts, even if the modification is small. Second, all three keep the static-graph assumption:")
# Analysis: workload-class synthesis before "Which assumptions decide?"
rep("\\subsection{Which assumptions decide?}",
"""\\subsection{A workload-class view}
Organizing the evidence by workload class, rather than by camp, gives a more useful answer to the research question. For \\emph{whole-graph iterative kernels} such as PageRank, every vertex is active and the access pattern is regular at the level of an iteration. This is where analog ReRAM and 3D-stacked PIM report their largest gains~\\cite{song2018graphr,challapalle2020gaasx,ahn2015tesseract}, and where hybrids profit from tiling~\\cite{shin2025piccolo}. For \\emph{frontier-driven traversals} such as BFS and SSSP, the active set is small and changes every iteration. Here the burst-waste problem is worst for DSAs~\\cite{shin2025piccolo}, and the synchronization problem is worst for real PIM~\\cite{gomezluna2022prim,barkhordar2025alphapim}. Fine-grained hybrids target exactly this case~\\cite{shin2025fala,yenimol2026cograf}. For \\emph{graph mining}, work is dominated by set operations over neighbour lists, partitions communicate little once the data is distributed, and PIM shows strong results on both simulated and real hardware~\\cite{besta2021sisa,talati2022ndminer,cai2024pimpam}. For \\emph{streaming and evolving} workloads, only DSAs offer hardware support~\\cite{rahman2021jetstream,zhao2022tdgraph,gao2023mega}. In short, PIM's case is strongest for mining and whole-graph kernels, the DSA case is strongest for dynamic workloads, and traversal, the flagship workload of the research question, is the contested middle ground that the hybrids are designed for.

\\subsection{Which assumptions decide?}""")
# Open challenges 5,6
rep("are needed before such designs can be used in critical systems~\\cite{song2018graphr,zheng2020spara}.",
"are needed before such designs can be used in critical systems~\\cite{song2018graphr,zheng2020spara}. Useful starting points are protection schemes that exploit graph structure, such as replicating high-degree vertices, whose corruption propagates furthest, or checking invariants like monotone distance labels in SSSP. These could detect faults at lower cost than general-purpose ECC on analog arrays.")
rep("would reduce the effort of adopting any of them.",
"would reduce the effort of adopting any of them. The vertex-programming model already serves as a common front end for DSAs~\\cite{ham2016graphicionado}, and linear-algebraic formulations serve the same role for PIM~\\cite{barkhordar2025alphapim}. A compiler that lowers one into placement-specific code, deciding per phase whether to run on the host, in a DSA pipeline, or in memory, would turn the hybrid design space into something programmers can use.")
# Conclusion
rep("PIM's strength is energy efficiency and bandwidth that grows with capacity,",
"We surveyed 30 works spanning simulated 3D-stacked and analog PIM, real UPMEM hardware, static and dynamic DSAs, and the 2025--2026 hybrids, and compared them under an explicit rule for comparability. PIM's strength is energy efficiency and bandwidth that grows with capacity,")
rep("Their weakness is the external bandwidth ceiling and the burst waste it entails~\\cite{shin2025piccolo,chen2022regraph}.",
"Their weakness is the external bandwidth ceiling and the burst waste it entails~\\cite{shin2025piccolo,chen2022regraph}. They also lack real-silicon validation, which leaves the size of their own simulation-to-silicon gap unknown.")
rep("Achieving that combination for dynamic graphs, with security, dependability, and timing guarantees suited to critical systems, remains open.",
"Achieving that combination for dynamic graphs, with security, dependability, and timing guarantees suited to critical systems, remains open. It is also where we expect the next decisive results. A PIM-capable hybrid that handles updates without repartitioning, evaluated end to end on real hardware against a DSA baseline, would resolve the question this survey can only frame.")
open(p,'w').write(t); print('applied')
