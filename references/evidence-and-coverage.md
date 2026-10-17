# Evidence, coverage and uncertainty contract

## Evidence ledger

Each relevant claim receives `{id, candidate_id, claim, url_or_locator, source_type, author_or_owner, publication_date, checked_at, access_method, evidence_grade, quote_or_summary, limitations, independent}`. Use `candidate_id: null` for method-wide or domain-wide evidence. A URL is one locator type; local file section, DOI, official record reference, page+paragraph, API response key, screenshot/observation, or operator transcript can be more appropriate. Do not record private tokens or unrelated personal data. Every operational `verified` step must reference evidence explicitly supporting that step, not just an adjacent official website.

- `verified`: directly observed interface or trustworthy source explicitly supporting the narrowly worded claim; evaluation still considers freshness/authoritativeness.
- `inferred`: derived from stated evidence; expose inference and possible alternative.
- `unconfirmed`: lead that still needs a source or observation.
- `contradicted`: dated counterclaim or evidence invalidates previous assertion, unresolved conflict explicitly noted.

**Important:** Local JSON validation only enforces presence, IDs and grade consistency. It cannot visit sources or establish that observations really occurred. Real evidence judgment remains a research obligation.

## Which kinds of evidence belong where?

| Claim being assessed | Better starting sources | Independent counterchecks |
|---|---|---|
| Current eligibility/terms | Official rulebook, current agency/provider page | Applicant experience, policy archive, support cases |
| Exact UX/API route | Observed interface, versioned official documentation | Dated user reports, issue trackers, test runs |
| Scientific effectiveness | Appropriate peer-reviewed/registered primary work | Replication, systematic review, conflicts and limitations |
| Reliability/performance | Reproducible tests, operational logs | Independent benchmarks, incident histories |
| Service interaction | Actual operator/customer reports | Negative cases, transparent sampling, contemporaneous traces |

Originality, independence, specificity, date/context fit and verifiability matter more than the number of repeated copies. Different sources can be authoritative for different claims. Absence of complaints is not an independent success rate.

## Retrieval and breadth ledger

Record each tested discovery method and each covered category with yield, duplication and blind spots. Assess search completeness relative to a declared boundary and the search/tool budget. Exhaustive language requires an enumerated universe or defensible systematic census; otherwise say **broad, bounded, sampled** or **coverage limited**. An empty search can mean a retrieval mismatch rather than an empty market.

For independent-evidence gaps, record an explicit targeted search note beginning `Searched:` including actual searches/source classes and date. Never write `Searched:` to imply work that was not performed. Recheck material information at execution when freshness can change (deadlines, signups, fee structures, URLs, legal requirements, tool access).

## Internal review questions

What original record supports this precise claim? Was it witnessed or inferred? How many supposedly independent sources are reposts? Is the dated evidence relevant to this jurisdiction/version? What counterexample would change the ranking? What gap should be carried to the executor as a required just-in-time check? Could the user safely act on the first step as written?
