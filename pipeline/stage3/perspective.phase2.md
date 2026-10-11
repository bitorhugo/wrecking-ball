contract_role: perspective
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: warn
trigger: "a missing or informal threat model, loose use of predictability language"

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

I reviewed this as a dependable and secure systems researcher with a real-time systems background. I read the manuscript mainly for Section 7 (Properties for Critical Systems) and the open challenges in Section 8 that follow from it, and checked whether an adjacent-field reader can follow the framing and trust the claims that reach beyond computer architecture. Performance-modelling detail is outside my competence, and I have not judged it.

Overall, the critical-systems section is more than a gap list. It gives an architectural reason for the security asymmetry, raises a real dependability point for analog PIM (a faulty cell changes the topology, not just a value), and turns these into concrete research directions. It also marks the authors' own inference as inference. The weaknesses are in rigour as a DSN or real-time reader would see it. The security comparison has no stated threat model and sets protections against different adversaries side by side. The predictability paragraph uses worst-case and bounded-latency language loosely enough that a real-time reader would object. The dependability paragraph overstates what ECC buys a DSA and misses an asymmetry that would strengthen the paper's own argument. None of these overturns the section's main conclusion that security, dependability and predictability have barely been studied for either camp; the absence claims are scoped and look sound. That is why I score D4 `warn` and not `block`.

### S1: Workload model and acronyms are accessible to adjacent-field readers
**Evidence Anchor**: text: §2.1 "Graphs are usually stored in compressed sparse row (CSR) or compressed sparse column form."
Section 2 introduces the vertex-centric model, the storage formats, the synchronous/asynchronous and push/pull choices, and the three kinds of irregularity in plain language, and expands every acronym. A reader from dependable systems can follow Sections 3 to 7 without outside reading.

### S2: Own inference is explicitly separated from surveyed evidence
**Evidence Anchor**: text: §7 Security "This is our own inference: IMPACT's side channel targets other applications, and no surveyed paper has evaluated leakage of graph structure."
The step from row-buffer timing channels to graph-structure leakage is clearly labelled as the authors' extrapolation rather than attributed to IMPACT. This is the correct practice for a cross-field claim.

### S3: The dependability argument is specific to graph semantics
**Evidence Anchor**: text: §7 Dependability "If a crossbar cell that stores the adjacency matrix is faulty, the topology of the graph itself changes."
The paper explains why the usual tolerance argument for analog error (convergent numerical kernels) does not carry over to reachability-type kernels. This is the right distinction for a dependability reader, and it is backed by a stated full-text check of GraphR, Spara and GaaS-X.

### S4: Open challenges give actionable, domain-appropriate detection ideas
**Evidence Anchor**: text: §8 item 5 "checking that SSSP distance labels only decrease"
Directions 4 and 5 go beyond "more work is needed". They propose traversal-correctness metrics (reachability errors), structure-aware fault detection (replicating high-degree vertices, and checking that SSSP labels only decrease, which holds for relaxation-based SSSP), and a comparative threat model covering both confidentiality and integrity.

### S5: Scratchpad predictability point is correct
**Evidence Anchor**: text: §7 Predictability "A scratchpad, such as the one in Graphicionado, has a fixed access latency, unlike a cache whose hit rate depends on the graph"
This matches the standard real-time argument for scratchpads over caches when analysing timing. It is one of the few places where the DSA camp's predictability is reasoned about rather than marked "not studied".

### W1: Predictability reasoning misuses worst-case and bounded-latency concepts
**Severity**: Major
**Evidence Anchor**: text: §7 Predictability "This is good on average, but it has no upper bound in the worst case, because one update can affect the whole graph."
**Confidence**: 4 — real-time systems background, familiar with WCET and timing-analysis terminology
To a real-time reader, "no upper bound" means unbounded. But an update that affects the whole graph still has a bound for monotonic kernels: roughly the cost of recomputing from scratch on a finite graph. The bound is loose and unanalysed, which is not the same as having none. The point the paper seems to want is that no design gives an analysable, tight bound, as opposed to a bound on average. In the same paragraph, the Spara evidence (GraphR's performance changes by more than 5x as the edge count doubles) shows scaling with input size, not timing variability for a fixed input. It is offered as evidence of unpredictability without saying so. The paper never names WCET, never separates timing variability from timing analysability, and never states what "bounded latency" would require (for example, a bound on the affected region or on iteration count). As a result, the conclusion "No surveyed design therefore offers bounded latency" is right in substance but supported by reasoning a real-time reviewer would reject. The minimum remedy is to define the predictability notion used (worst-case bound versus variability, and analysable versus measured), rephrase "no upper bound" as "no tight or analysed bound", and either drop the Spara example or recast it as a scaling result.

### W2: The security comparison has no threat model and contrasts protections against different adversaries
**Severity**: Major
**Evidence Anchor**: text: §7 Security "A DSA keeps the trust boundary at the memory controller, where conventional encryption can be used."
**Confidence**: 4 — secure-systems background, familiar with memory-encryption and microarchitectural side-channel threat models
Section 7 sets MGX (memory encryption and integrity, normally against an attacker on the off-chip memory side) against IMPACT (row-buffer covert and side channels exploited by co-located software). These are different adversaries with different capabilities and assets, but the section states neither, and Table tab:critical places them in the same row as if they measured the same property. The trust-boundary argument also stops halfway. Encryption and integrity protection at the controller do not hide the address trace. So the observation that "the access pattern itself encodes the graph" applies equally to a DSA whose off-chip accesses can be observed, unless the DSA uses access-pattern obfuscation, which the paper does not discuss. As written, an adjacent-field reader would conclude that graph-structure leakage is mainly a PIM problem. That does not follow from the evidence. The core conclusion, that the two camps' security has not been compared, survives. But the section needs, at minimum, an explicit adversary model per property (who the attacker is, what they observe or control, and what is protected), with each surveyed defence or attack placed in it. It also needs a sentence acknowledging access-pattern leakage on the DSA side. Open challenge 4 asks for exactly this; the paper should apply its own recommendation to its own Section 7.

### W3: The ECC argument for DSAs is overstated and misses a PIM/ECC asymmetry
**Severity**: Minor
**Evidence Anchor**: text: §7 Dependability "DSAs read and write conventional DRAM and on-chip SRAM, so standard memory protection, such as error-correcting codes (ECC), applies without change."
**Confidence**: 3 — dependability background; detail of commercial PIM ECC handling is at the edge of my expertise
ECC protects stored data. It does not protect the accelerator's datapath, pipeline registers or control logic from transient faults, and large on-chip scratchpads are not automatically ECC-protected. The claim should be limited to storage. There is also a sharper contrast the paper misses: compute inside the DRAM changes data below the point where rank-level ECC is usually computed by the memory controller, so standard ECC may not apply to PIM without redesign. Making this explicit would strengthen the Dependability row of Table tab:critical.

### W4: The network-security use case is thin and not linked to the paper's own mutability finding
**Severity**: Minor
**Evidence Anchor**: text: §7 opening "Graph analytics supports applications such as network-security analysis [@asquini2025tc], where results must be trustworthy and delivered on time."
**Confidence**: 3 — familiar with security-analytics deployments, not with the cited workshop paper
The practical motivation for the whole critical-systems section rests on one workshop citation and one sentence. The paper does not say what "delivered on time" means for this use case (for example, a per-batch latency budget for flow or alert graphs). It also does not draw the obvious link: such workloads are inherently streaming, so the paper's central mutability finding (DSAs support dynamic graphs and PIM does not) bears directly on them, as does JetStream's small-batch advantage. One or two sentences making this link would turn the use case from a citation into an argument.

### W5: Security, dependability and predictability are never defined
**Severity**: Minor
**Evidence Anchor**: absence: §7 Properties for Critical Systems — expected working definitions of the three assessed properties, such as the dependability attributes considered, the adversary class for security, and the timing notion for predictability; checked §1 sub-question SQ4, §2 Background and Survey Method, §7 opening paragraph and all three property paragraphs, Table tab:critical, §8 items 4 and 5
**Confidence**: 4 — dependable-systems background
"Dependability" is used to cover both designed-in analog imprecision and hardware faults (stuck-at, endurance, read disturbance), which the dependability literature treats as different things. Neither "security" nor "predictability" is scoped. A short definitional paragraph at the start of Section 7 would make the section easier to use for DSN and real-time readers and would anchor W1 and W2.
