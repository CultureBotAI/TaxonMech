---
name: curate-yaml-record
description: Review one TaxonMech taxon YAML record for identity, lineage, nomenclature, taxonomy mappings, strains, attestations and resolvable gaps. Use for a named record audit; seeded fields are generated and read-only, so improvements go into the seeder, the scope, or kg-microbe, never into the YAML directly. Do not use for bulk ingestion, generated page edits, or as permission to spend credits, contact anyone, or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Curate one TaxonMech YAML record

Produce a defensible account of one `TaxonRecord`: what is supported, what is
wrong, what is unresolved, and where the fix belongs. Search results are
leads; only inspected sources can support a claim.

## Boundaries

- Resolve one target under `data/taxa/<domain>/`. Stop and disambiguate when a
  name could denote several NCBI taxa (homonyms, subspecies, strains).
- **Every seeded field is generated.** `just verify-corpus` fails on a hand
  edit. A correction to identity, lineage, nomenclature, mappings, strains or
  attestations is a change to the seeder (with a test), to
  `curation/seed_scope.tsv`, or to kg-microbe — say which, and open the
  issue there.
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
kg-microbe, or a curator overlay that does not exist yet. Scaffold a history
record with `just new-history --event REVIEW` naming what was checked. Do not
edit the record YAML.
