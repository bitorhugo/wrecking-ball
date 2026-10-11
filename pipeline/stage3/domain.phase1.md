## Contract Paraphrase

D1 (methodology_rigor, mandatory, owned by the methodology seat): From a domain-accuracy standpoint, this dimension asks whether the way the work was assembled is sound enough for the community's review bar. For a survey that means how the corpus was chosen, how searching was documented, what rules govern comparisons across systems, and how evidence of differing strength is weighted. I do not score it, but corpus gaps I find in the domain literature are relevant evidence for that seat.

D2 (domain_accuracy, mandatory, owned by me): This is my dimension. Every technical claim should match what the memory-systems and accelerator literature actually reports; cited prior designs and products must be described faithfully (their mechanisms, evaluation settings, and reported results); terminology for memory technologies, near-data and in-memory processing variants, and accelerator classes must be used correctly; and no seminal or directly competing work that a specialist would expect should be silently absent.

D3 (argumentative_coherence, mandatory, owned by the devil's advocate and also scored by methodology): The central thesis must hang together, with each claim backed by the evidence presented and no reasoning flaws that would collapse the main argument. From my side, a technically wrong premise can make an otherwise tidy argument incoherent, so domain errors feed into this dimension even though I do not score it.

D4 (cross_disciplinary_relevance, high, owned by the perspective seat): Readers from neighbouring fields should be able to follow the framing, definitions, and implications, and any claims reaching beyond architecture must be supported. Domain-wise, definitions that are accessible must still be technically correct; simplification must not become inaccuracy.

D5 (writing_and_structure, normal, owned by the editor-in-chief): Organisation, clarity, figure and table quality, and adherence to venue conventions. My interest is limited to whether comparison tables and figures present technical parameters correctly and with consistent units and baselines.

D6 (venue_fit_and_contribution, mandatory, owned by the editor-in-chief): The work must fit its configured target (here, the author's supplied rubric) and offer an original, meaningful contribution to its audience. From a domain view, a survey contributes only if its synthesis adds insight beyond existing surveys in the area, which depends on accurate and complete coverage.

## Scoring Plan

### D2: domain_accuracy
dimension_id: D2
what_to_look_for: Faithful description of cited PIM, near-data, and accelerator designs (mechanism, memory technology, evaluation methodology, reported speedups and their baselines); correct use of memory-system and accelerator terminology; coverage of the landmark and directly competing works a specialist would expect; claims about commercial devices consistent with their published specifications; technical generalisations that hold across the cited systems rather than a selected subset.
what_triggers_block: One or more material misrepresentations of prior work or factual technical errors that a domain expert would flag and that affect a comparison or conclusion, or omission of several landmark or directly competing works such that the coverage of either compared camp is materially incomplete; correctable in revision without rethinking the thesis.
what_triggers_warn: Minor inaccuracies, imprecise or inconsistent terminology, reported numbers quoted without their baseline or evaluation context, isolated missing references, or generalisations stated more broadly than the cited evidence supports, none of which change a main conclusion.
what_triggers_fatal: The central thesis or primary comparative claim rests on a technically false premise or systematically misrepresented prior work, so that correcting the domain facts would invalidate the main conclusion rather than merely revise it.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
