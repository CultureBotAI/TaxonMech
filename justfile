# TaxonMech — microbial taxon and strain knowledge base harmonized from kg-microbe

set positional-arguments := true

schema := "src/taxonmech/schema/taxonmech.yaml"
taxa := "data/taxa"

default:
    @just --list --unsorted

# Install package + dev tools
install:
    uv sync --extra dev

# Generate Pydantic classes from the LinkML schema
gen-schema:
    uv run gen-pydantic {{schema}} > src/taxonmech/schema/taxonmech_dataclasses.py

# Re-extract the data/raw/ inventories from a local kg-microbe checkout.
# Only needed when kg-microbe's sources change — the inventories are committed,
# so seeding, validation and tests all run without kg-microbe present.
# Set KG_MICROBE_ROOT or edit conf/sources.yaml to point at the checkout.
extract-inventory *args:
    uv run python scripts/extract_source_inventory.py {{args}}

# Show what extraction would produce, without writing (free check before the real run)
extract-inventory-dry:
    uv run python scripts/extract_source_inventory.py --dry-run --skip-input-hashes

# Download and verify only the pinned AllTheBacteria metadata, not genome FASTAs.
atb-fetch *args:
    uv run python scripts/atb.py fetch {{args}}

# Build a full local SQLite catalogue and compact source-evidenced crosswalks.
# Dry-run by default; --apply publishes the index and data/atb inventories.
atb-index *args:
    uv run python scripts/atb.py index {{args}}

# Indexed lookup by sample, ENA analysis, strain, exact genome identifier or source species.
atb-query *args:
    uv run python scripts/query_atb.py {{args}}

# Capture public StrainInfo search and rich deposit/sequence evidence.
straininfo-fetch *args:
    uv run python scripts/fetch_straininfo.py {{args}}

# Build the committed StrainInfo overlay; dry-run unless --apply is supplied.
straininfo-index *args:
    uv run python scripts/straininfo.py {{args}}

# Resolve StrainInfo strains/deposits to supported genome identifiers.
straininfo-query *args:
    uv run python scripts/query_straininfo.py {{args}}

# Complete source catalogs: native identifier lookup without inferred identity.
source-query *args:
    uv run python scripts/query_sources.py "$@"

# Project pinned primary inputs (--project) or rebuild the source census manifest.
source-catalog *args:
    uv run python scripts/build_source_catalog.py "$@"

# Rank candidate taxa for curation/seed_scope.tsv. Prints; never writes the file.
propose-scope *args:
    uv run python scripts/propose_scope.py "$@"

# Dry-run the seed: report the scope and what WOULD be written. No files touched.
seed *args:
    uv run python scripts/seed_from_sources.py {{args}}

# Seed exactly one record end to end and validate it — the canary to run
# before any bulk write. `just seed-canary NCBITaxon:562`
seed-canary *args:
    uv run python scripts/seed_from_sources.py --apply --only "$@"

# Write every in-scope taxon record under data/taxa/<domain>/<slug>.yaml.
# Run `just seed` and `just seed-canary` first.
seed-apply *args:
    uv run python scripts/seed_from_sources.py --apply {{args}}

# Validate a single taxon YAML against the schema (open mode, quick check)
validate file:
    uv run linkml-validate -s {{schema}} --target-class TaxonRecord {{file}}

# Validate every record. Delegates to validate-strict (closed mode: unknown
# fields are errors, not silently accepted as they are in linkml-validate's
# default open mode).
validate-all *args:
    @just validate-strict {{args}}

# Strict in-process validation in closed mode. Emits
# reports/instance_validation_failures.tsv and exits 1 on any ERROR.
validate-strict *args:
    uv run python scripts/validate_strict.py {{args}}

# Verify data/taxa/ is exactly what data/raw/ + curation/seed_scope.tsv produce.
verify-corpus *args:
    uv run python scripts/verify_corpus.py {{args}}

# Render the browsable site under pages/ from the corpus. Committed; `--check`
# fails when it has gone stale.
render *args:
    uv run python scripts/render_pages.py {{args}}

# Fail if pages/ is out of step with the corpus
render-check:
    uv run python scripts/render_pages.py --check

# Corpus report: records per domain, rank and status; source coverage; strains.
report *args:
    uv run python scripts/corpus_report.py {{args}}

# Refresh the generated current-corpus block in README.md.
docs-stats:
    uv run python scripts/check_docs.py --write

# Fail if README.md's current-corpus block is out of step with the corpus.
docs-check:
    uv run python scripts/check_docs.py --check

# Verify raw inventories and the ATB crosswalk against their source manifests.
provenance-check:
    uv run python scripts/check_provenance.py

# Run the test suite
test *args:
    uv run pytest {{args}}

# Lint
lint *args:
    uv run ruff check {{args}} .

# Auto-fix lint findings
lint-fix:
    uv run ruff check --fix .

# The authoritative quality gate used both locally and in CI.
qc:
    uv run python scripts/run_qc.py

# Verify every claw-governed vendored file matches the pinned canonical
# revision in scripts/.vendored_canon_ref (the same check CI runs).
vendored-check:
    bash scripts/check_vendored_sync.sh

# id<->label correspondence gate (vendored): every (grounding, label) pair a
# curator adds to a causal graph must match the ontology through OAK.
# Downloads OAK sqlite ontologies on first run.
validate-products:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml

# The same check written to reports/label_drift.tsv without failing.
report-label-drift:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml --report reports/label_drift.tsv || true

# Scaffold an append-only curation-history record (history/<kind>/<slug>/...).
# See history/README.md. "$@" not {{args}}: see `set positional-arguments`.
new-history *args:
    uv run python scripts/new_history_record.py "$@"

# Validate history records or directories of them against the vendored schema.
validate-history *args:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ "$#" -eq 0 ]; then set -- history; fi
    for target in "$@"; do
      uv run python scripts/validate_history.py "$target"
    done

# Preview full semantic map inputs; --limit/--record select an explicit canary.
# Add --output build/text-map/inputs.jsonl to atomically export the JSONL.
text-map-inputs *args:
    uv run python scripts/text_map_inputs.py "$@"
