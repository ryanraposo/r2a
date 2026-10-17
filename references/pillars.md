# Five-pillar field manual

## Scope record

Inputs: user outcome; subject and eligibility boundary; jurisdiction and dates when material; evidence quality; research effort; future tool environment; execution-hours parameter; permitted actions and human gates. The target can be anything that can be researched and acted upon. Define downstream success in observable terms before searching.

## P1: Meta-discovery as measured exploration

1. Build taxonomy, terms, alternate spellings, official registries, primary providers, databases, independent communities and archives.
2. Trial at least two differing source strategies on overlapping representative slices and record `(method, query_or_procedure, source_class, tested, new_relevant_count, duplicate_count, blindspots, checked_at)`.
3. Evaluate precision/relevance, category yield, authority for *specific claims*, cross-source duplication, indexing/access limitations and overlooked categories.
4. Document repeatable searches and where/why specific source types are authoritative. Refine the search plan based on observed results.

## P2: Field coverage and evidence-aware prioritization

- State eligibility predicate and explicit exclusions before ranking. Maintain canonical identity, aliases, status and source links for every lead.
- Sample independent categories and source strata. Record `(category, checked, stop_reason, known_gaps)`. Use marginal novel discoveries, saturation, source balance, external denominator if available, and deadline/cost tradeoffs to decide when broad exploration stops.
- Distinguish relevant-but-unverified from vetted/eligible; never boost a candidate purely because it has abundant publicity. Prefer understandable ranking rationale over made-up precision. Candidate desirability is not the same as proven chance of success.
- If a category yields few candidates, assess retrieval quality before inferring scarcity.

## P3: Path dossier per candidate x outcome x execution environment

For each priority object capture: target outcome, eligibility and proof, authentic first step, exact interface/endpoint or physical starting point, prerequisites, time/cost, step-by-step action status and citation, branches, permissions/approval requirements, anticipated error modes, recoveries, termination criteria, expected proof, and recheck triggers. Assign evidence IDs to the exact steps supported. A step is `verified` only when supported by an independently inspectable credible record or direct interface observation. A brand's general FAQ alone may leave the exact button flow inferred. If the entry cannot be verified, record the blocking condition and move on.

**Domain adaptations:** Websites require exact current interaction flow; APIs require auth/endpoints/schemas/idempotency; code tasks require repository/runtime and commands; purchases require restrictions, totals and human consent; scientific work requires protocols, instruments and reproducibility; institutions require rules, deadlines and applicant eligibility; physical tasks require location and safe human execution details.

## P4: Independent corroboration

Form a concrete question for each shortlisted candidate: "What actually happens when an eligible person tries this path in this context?" Search for positive and failed outcomes, independently attributable users, specific dated reports, comparative tests and relevant scientific findings. Capture the direct source, age, incentives, representativeness and disagreements. Avoid translating single anecdotes into population-level probabilities. Distinguish independent testimony from affiliated promotions, syndicated copies and unverified claims. When no independent evidence exists after targeted searches, write `Searched: ...` with source types, queries and dates rather than manufacturing support.

## P5: Research the next agent's best route to actual results

Build execution capability matrix `(action, tool, availability [exercised/documented/unknown/unavailable], permissions, preflight, proof, fallback)`. Document specific priority order, dependency graph, concurrency conflicts, approval points and first-action sequence. Convert estimated action effort into a budget-aware queue under `{execution_hours}`. Prioritize realizable outcomes before marginal research. The executor should make time-sensitive rechecks at the relevant action point and move through blockers while preserving state. Set aside enough time to verify outcomes and provide truthful receipts.

### Iteration and stop

P4 failure may demote a candidate and reopen P2; P3 may expose an unsearched source type and reopen P1. Stop when extra information has lower expected value than executing the best supported paths, or when research tools/budget constrain further work. Name unknowns instead of treating a stop as proof of exhaustive coverage.
