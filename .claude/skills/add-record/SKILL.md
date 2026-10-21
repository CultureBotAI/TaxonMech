---
name: add-record
description: "Propose, review, and add new species-or-below microbial taxon records to TaxonMech via curation/seed_scope.tsv and the validated seeder pipeline"
argument-hint: "[--rule <rule> | <NCBITaxon:ID> ...]"
---

# Add TaxonRecord to TaxonMech

You are adding one or more microbial taxon records (`TaxonRecord` at `SPECIES` rank or below) to the TaxonMech knowledge base (`data/taxa/<domain>/<slug>.yaml`).

## Overview

TaxonMech records are **never hand-written**. Every `data/taxa/<domain>/<slug>.yaml` file is deterministically generated from the committed source inventories (`data/raw/`, `data/atb/`, `data/straininfo/`) and the explicit scope file `curation/seed_scope.tsv` through the closed-schema validation gate (`src/taxonmech/validation/write_validated.py`).

Adding a taxon record therefore consists of:
1. Identifying and reviewing candidate species-or-below microbial taxa in `data/raw/ncbitaxon_taxa.tsv` that are not yet in `curation/seed_scope.tsv`.
2. Appending reviewed identifiers and provenance reasons to `curation/seed_scope.tsv`.
3. Running the single-record canary (`just seed-canary <NCBITaxon:ID> --force`) and inspecting the generated YAML before bulk seeding.
4. Running `just seed-apply`, `just render`, and `just docs-stats`.
5. Recording a curation history entry (`just new-history`) and structured review coverage (`reviews/structured/` and `docs/structured-review-inventory/`).
6. Passing `just qc` and `just review-check`.

---

## Step 1: Discover and Review Unscoped Microbial Taxa

1. Query unscoped candidate taxa using `scripts/propose_scope.py`:
   ```bash
   just propose-scope --rule attested --rank '' --all --append
   ```
   Or check the supported selection rules in `scripts/propose_scope.py` (`core`, `attested`).
2. For each candidate `NCBITaxon:<id>`:
   - **Rank gate**: Verify `inv.is_species_or_below(tid)` is true (`SPECIES`, an infraspecific rank such as `SUBSPECIES`, `STRAIN`, `VARIETAS`, `FORMA_SPECIALIS`, `SEROTYPE`, etc., or an unranked/`CLADE` node beneath a `SPECIES` ancestor). Genera and higher ranks are never records; they appear only in `lineage`.
   - **Microbial scope**: Verify the taxon is a prokaryote (`BACTERIA`, `ARCHAEA`), microbial eukaryote (`EUKARYOTA` fungi/yeasts, microsporidia, oomycetes, protists, microalgae attested directly or via microbial strain descendants in `GOLD`, `MEDIADIVE`, or `BACDIVE`), or other microbial entry in the pinned inventory.
   - **Duplicate & retirement check**: Confirm the identifier is not already in `curation/seed_scope.tsv` or `data/taxa/PATHS.tsv`, and check `retired_into` in `data/raw/ncbitaxon_taxa.tsv`.
   - **Source evidence check**: Inspect the row in `data/raw/ncbitaxon_taxa.tsv` (and any linked rows in `gtdb_mappings.tsv`, `lpsn_names.tsv`, `bacdive_strains.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, `bactotraits_taxa.tsv`, or descendant strain rows).

---

## Step 2: Update `curation/seed_scope.tsv`

Append the reviewed candidate rows (`identifier`, `added`, `reason`) to `curation/seed_scope.tsv`:

```bash
uv run python scripts/propose_scope.py --rule attested --rank '' --all --append --date YYYY-MM-DD >> curation/seed_scope.tsv
```

Re-run `just propose-scope --rule attested --rank '' --all --append` to confirm `0 of 0 candidates proposed` when expanding to completion.

---

## Step 3: Canary First, Then Seed Corpus

1. Dry-run the seeder to verify scope counts and path assignments:
   ```bash
   just seed
   ```
2. Run a one-record canary and inspect the resulting YAML file:
   ```bash
   just seed-canary <NCBITaxon:ID> --force
   just validate data/taxa/<domain>/<slug>.yaml
   just validate-strict data/taxa/<domain>/<slug>.yaml
   ```
3. Seed all newly scoped records and update `data/taxa/PATHS.tsv`:
   ```bash
   just seed-apply
   ```

---

## Step 4: Refresh Derived Site, Docs, History, and Structured Reviews

1. Re-render `pages/` and refresh `README.md` statistics:
   ```bash
   just render
   just docs-stats
   ```
2. Record an append-only curation history entry for the scope expansion:
   ```bash
   just new-history --kind other --path curation/seed_scope.tsv --slug <slug> \
     --event EDIT --outcome changed --sections scope,identifiers \
     --summary "<concise summary>" \
     --model <model> --agent-tool <tool> \
     --details "<what was added, how it was verified>"
   just validate-history
   ```
3. Review every newly added `data/taxa/<domain>/<slug>.yaml` record under the structured review contract (`docs/record-review-profile.md`) and update `docs/structured-review-inventory/`, `docs/structured-review-batches.tsv`, and `reviews/structured/` so full-corpus review coverage (`uv run python scripts/corpus_review_inventory.py --check`) remains at 100%.

---

## Step 5: Quality Gate Verification

Run the full repository quality gates before finishing:

```bash
uv run python scripts/corpus_review_inventory.py --check --verify-target-sha256
just review-check
just qc
```

## Important Rules

1. **Never hand-edit `data/taxa/<domain>/<slug>.yaml` or `pages/`**: Always update `curation/seed_scope.tsv` (or `src/taxonmech/seed.py`) and run `just seed-apply` and `just render`.
2. **Species and below only**: Never add a genus, family, order, class, phylum, or domain to `curation/seed_scope.tsv`.
3. **Preserve existing slugs**: Never alter existing identifier-to-slug mappings in `data/taxa/PATHS.tsv`.
4. **Canary before bulk write**: Always inspect one generated record with `just seed-canary` before running `just seed-apply`.
