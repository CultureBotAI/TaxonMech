---
name: curate-yaml-record
description: Review one TaxonMech taxon YAML record for identity, lineage, nomenclature, taxonomy mappings, strains, attestations and resolvable gaps. Use for a named record audit; seeded fields are generated and read-only, so improvements go into the seeder, the scope, or kg-microbe, never into the YAML directly. Do not use for bulk ingestion, generated page edits, or as permission to spend credits, contact anyone, or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 2.0.0
---

# Curate one TaxonMech YAML record

Produce a defensible account of one `TaxonRecord`: what is supported, what is
wrong, what is unresolved, and where the fix belongs. Search results are
leads; only inspected sources can support a claim.

## The contract

<!-- canonical:begin the-contract -->
Produce a defensible record and an explicit account of four things: what is
**supported**, what was **corrected**, what is **still unresolved**, and what is
**genuinely unknown**. The last two are different — a gap you searched for and
could not close is a finding; a gap you did not look at is not.

**One target.** Resolve exactly one record before touching anything. If a label
matches several, or a request names a family rather than a member, stop and
disambiguate. Silently substituting a similar record is the error that no later
check catches, because everything downstream is then correct about the wrong
thing.

**Audit preserves scientific inputs. Curation authorises edits to the named
record only.** A review or audit request changes no scientific record, status,
or curation history. It does save a new timestamped structured review through
`docs/record-reviews.md` and the native rubric in `docs/record-review-profile.md`.
A curate, improve, complete, correct or add-evidence request authorises local edits to that record and the smallest
maintained path its provenance requires — not to neighbours, not to whatever
else looked wrong on the way.

**Search results are leads. Only an inspected source supports a claim.** A
search hit, a deep-research report, a rendered page, and a generated artifact are
each somewhere to look, and none is evidence. Evidence is text you read in the
source, attached to the narrowest assertion it actually supports.
<!-- canonical:end the-contract -->

## Structured audit output

For a review, audit, or assessment request, apply the scientific checklist below
without taking the curation write steps. Follow [docs/record-reviews.md](../../../docs/record-reviews.md)
and [the local profile](../../../docs/record-review-profile.md): capture target
and maintained-input hashes before judging, then save the assessed result with
`uv run python scripts/record_review.py validate <completed-review.yaml>` and
`uv run python scripts/record_review.py save --content <completed-review.yaml>`.
The output is `reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/review.yaml` plus its
derived `review.md`; link both in the final response. Preserve actual check
results, evidence, scope, unresolved findings, and unavailable checks. Use a
partial/blocked review when required checks are unavailable after assessment.
Do not append curation/history events or promote native status from an audit.

Worklists, sampling output, source searches, and raw provider drafts are inputs
to review, not completed scientific reviews. Keep their selection rules and
population denominators when assessing a sample; deterministic-only inspection
uses `scientific_review: false`. A queue checkpoint never substitutes for the
validated saved bundle. Existing curation write and scientific sign-off gates
below still apply when curation is explicitly requested.

## Boundaries

- Resolve one target under `data/taxa/<domain>/`. Stop and disambiguate when a
  name could denote several NCBI taxa (homonyms, subspecies, strains).
- **Every seeded field is generated.** `just verify-corpus` fails on a hand
  edit. A correction to identity, lineage, nomenclature, mappings, strains or
  attestations is a change to the seeder (with a test), to
  `curation/seed_scope.tsv`, or to kg-microbe: identify that owner in the
  saved finding and proposed action; issue creation needs separate authorization.
- Never edit generated `pages/`; edit templates and regenerate.
- Never launch paid research, contact anyone, or create/edit a GitHub item or
  outbound message without explicit authorization.
- Preserve unrelated work and use a dedicated branch/worktree.

## Read before judging the record

Read the full target plus `CLAUDE.md`, `docs/CURATION.md`,
`docs/HARMONIZATION.md`, `docs/SCHEMA.md`, the relevant classes in
`src/taxonmech/schema/taxonmech.yaml`, `history/README.md`, and
[references/review-checklist.md](references/review-checklist.md).

Inspect the record's rows in `data/raw/` (the inventories are the evidence
the seeder had), the source-native pages (NCBI Taxonomy browser, LPSN name
page, GTDB taxon page, BacDive strain page) and any cited literature.

## Workflow

### 1. Establish the baseline

Read the whole YAML. Note identifier, rank, domain, lineage, synonyms,
nomenclature, mappings, strain count and listing, attestations, status and
history. Run:

```bash
just validate-strict <record-path>
just verify-corpus
```

A green gate proves shape and reproducibility, not biological correctness.

### 2. Verify identity and lineage

Confirm the NCBI id resolves to the label and rank the record carries, and
that the lineage matches NCBI's. Confirm the `taxon_domain` bucket.

### 3. Verify nomenclature and mappings

For each `nomenclature` entry, open the LPSN page: is this name really mapped
to this NCBI taxon, is the status line current, are the type strain
designations LPSN's? For each `taxonomy_mappings` entry, open the GTDB page:
is the predicate defensible (closeMatch for the same species, broadMatch when
NCBI is broader)? A wrong mapping is a kg-microbe finding.

### 4. Verify strains

Spot-check the listed type strain against LPSN and BacDive. Check that
`strain_count` matches the inventory. Note strains BacDive files here that
LPSN would place elsewhere.

### 5. Report, and route the fixes

Report corrections and their evidence, retained claims checked, unresolved
gaps, and for each finding **where the fix belongs**: seeder, scope,
kg-microbe, or a curator overlay whose availability must first be checked
with an ignored/hidden-inclusive search. Save the structured review using the
contract above; do not append a history event or edit the generated record.
History events remain part of separately authorized curation changes.
