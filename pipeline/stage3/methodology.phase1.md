## Contract Paraphrase

D1 (methodology_rigor): For a survey, rigor means the way the evidence was gathered and handled rather than statistics. A reader should be able to rerun the corpus construction: search sources, query strings or seed lists, dates, inclusion and exclusion rules, and screening counts should all be stated. Comparisons between works need an explicit, consistently applied rule for when results count as comparable (baselines, workloads, datasets, metrics). Evidence must be weighted by how it was produced, with simulation, FPGA prototypes, and fabricated silicon kept apart. The extraction artifacts should be available or described well enough for an independent reviewer to check them.

D2 (domain_accuracy): Domain claims must match the current evidence base, and the prior work being summarized must be represented faithfully. From the methodology side, my concern is whether the stated extraction procedure would expose any misreporting. Judging the domain facts themselves belongs to the domain seat.

D3 (argumentative_coherence): The central thesis has to follow from the evidence the survey actually assembled. From a methodology view, generalizations must stay within what the corpus size, its composition, and the evidence tiers can support. Conclusions that rely on cherry-picked or non-comparable results, or that go beyond the stated scope, break coherence even when the prose reads smoothly.

D4 (cross_disciplinary_relevance): Definitions, framing, and implications should make sense to readers in neighbouring fields, and any claim that crosses fields needs substantiation. For methodology this means that terms such as speedup, energy efficiency, and irregularity are defined well enough that adjacent readers can tell how comparisons were built.

D5 (writing_and_structure): Organisation, clarity, figures and tables, and venue conventions. The methodology-relevant part is whether the method, the comparison tables, and the limitations are easy to find and laid out so a reader can audit them.

D6 (venue_fit_and_contribution): The manuscript should fit the configured target, here a course rubric, and add something original and significant. For a survey, the contribution partly depends on whether the synthesis method adds value beyond a list of papers, for example a reusable comparison framework or a weighting of evidence.

## Scoring Plan

### D1: methodology_rigor
dimension_id: D1
what_to_look_for: A reproducible corpus protocol (sources, queries or seed lists, date window, inclusion and exclusion criteria, screening counts); an explicit comparison rule that is applied the same way to every included work; evidence tiers that separate simulation, FPGA, and silicon results and weight them differently; acknowledged threats to validity such as publication bias, baseline heterogeneity, and single-reviewer extraction; extraction artifacts that are available or fully described.
what_triggers_block: The corpus selection cannot be reproduced (no stated sources, queries, or inclusion criteria), or the comparison rule is missing or visibly applied inconsistently across works, so the headline comparisons cannot be audited.
what_triggers_warn: The protocol is stated but has gaps, such as missing screening counts, unstated date bounds, or partial evidence-tier labeling, or the threats-to-validity discussion leaves out a material bias, while the core comparisons can still be traced.
what_triggers_fatal: Headline quantitative comparisons are presented as like-for-like even though they combine incompatible baselines, metrics, or evidence tiers without disclosure, or the described selection process contradicts the corpus actually reported, which invalidates the survey's central findings.

### D3: argumentative_coherence
dimension_id: D3
what_to_look_for: Whether each general conclusion is backed by enough included works across the relevant evidence tiers; whether the strength of a claim is scaled to corpus size and evidence quality; whether counter-evidence in the corpus is acknowledged; whether the scope limits stated in the method are respected in the conclusions.
what_triggers_block: A central conclusion depends on a handful of non-comparable or simulation-only results while being stated as a general finding, and nothing in the paper qualifies it.
what_triggers_warn: Some secondary claims overgeneralize beyond the corpus or underweight contrary evidence, but the main thesis remains supported once the language is hedged.
what_triggers_fatal: The main thesis contradicts the survey's own extracted evidence, or rests on circular or selectively chosen evidence, so that no amount of rewording could make the conclusion follow.

criteria_binding_unavailable

[CONTRACT-ACKNOWLEDGED]
