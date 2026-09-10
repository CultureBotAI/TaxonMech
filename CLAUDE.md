# CLAUDE.md

Operational guidance for Claude Code and other editing agents in this repository.

## Repository purpose

TaxonMech is a LinkML knowledge base of microbial taxa and strains, seeded
from kg-microbe's transforms of NCBI Taxonomy, GTDB, LPSN, BacDive, MediaDive,
GOLD, Madin et al. and BactoTraits. One generated YAML record lives under
`data/taxa/<domain>/<slug>.yaml` for each taxon in scope. The committed
inventories in `data/raw/` and the scope in `curation/seed_scope.tsv` are the
reproducible inputs.

Read these before changing domain behavior:

- [README.md](README.md) — public model and generated current statistics.
- [docs/HARMONIZATION.md](docs/HARMONIZATION.md) — identity, mapping and seeding design.
- [docs/CURATION.md](docs/CURATION.md) — what a record is and the evidence rules.
- [docs/SCHEMA.md](docs/SCHEMA.md) — field guide.
- [.claude/skills/curate-yaml-record/SKILL.md](.claude/skills/curate-yaml-record/SKILL.md)
  — audit one taxon record; generated YAML remains read-only.
- [.claude/skills/review-open-issues/SKILL.md](.claude/skills/review-open-issues/SKILL.md)
  — read-only, evidence-backed sweep of the open issue queue.

Sibling repositories use the same conventions: TraitMech, HabitatMech,
CultureMech, MediaIngredientMech, CommunityMech, CellStructureMech,
ProteinTraitsMech, AntibioticMech. The upstream pattern is
monarch-initiative/dismech.

## Authoritative commands

```bash
just qc                # every local and CI quality gate
just report            # current corpus statistics
just test              # unit and corpus-integrity tests
just validate-all      # closed-schema validation of every record
just verify-corpus     # prove data/taxa reproduces from data/raw + the scope
just render            # regenerate the committed site under pages/
just docs-stats        # refresh the generated README statistics block
just propose-scope ... # rank candidate taxa for curation/seed_scope.tsv (prints; never writes)
just new-history ...   # scaffold an append-only curation-history record
just validate-history  # validate history/ against the vendored schema
just vendored-check    # claw-governed files match canon at scripts/.vendored_canon_ref
just validate-products # id<->label gate via OAK, for curator-added graph nodes
```

`just qc` is authoritative: lint, README statistics, raw-data provenance,
tests, history records, closed-schema validation, corpus reproduction,
generated-site drift, corpus report. CI runs the same script.

For an upstream refresh:

```bash
just extract-inventory-dry
just extract-inventory
just seed
just seed-canary NCBITaxon:562
just seed-apply --force
just seed-apply --force --prune  # only when files that left the scope should be removed
```

## Fact-based answers only

Verify counts, statuses and identifiers with a live command (`just report`,
`grep`, `Read`) before stating them. Do not quote numbers from prose.

## Generated-file boundaries

**Never hand-edit a taxon record.** `data/taxa/` is generated from the
committed inventories plus the scope. Put harmonization changes in the
extractor or seeder and scope changes in `curation/seed_scope.tsv`.
`just verify-corpus` rejects drift.

**Never write a record except through `write_validated_taxon`.** It performs
closed-schema validation before writing. Every mutation must also append a
`CurationEvent` with `taxonmech.curate.curation_event.record_curation_event`.

**Re-emitting an unchanged record must be byte-identical.** Preserve the YAML
emission contract enforced by `tests/test_write_validated.py`.

**Edit site templates, not `pages/`.** Change `src/taxonmech/templates/`, run
`just render`, and commit the regenerated pages. `pages/` is published and
checked byte-for-byte.

**Do not edit any claw-governed vendored file here** —
`src/taxonmech/schema/mech_shared.yaml`, `src/taxonmech/schema/history.yaml`,
`scripts/check_vendored_sync.{py,sh}`, `scripts/validate_id_label_correspondence.py`,
`scripts/chem_formula.py`, `scripts/deep_research_contract.py`,
`prompts/backlog-loop-goal.md` and the five vendored `tests/test_*` contract
files. They are vendored byte-identically from culturebotai-claw at the commit
pinned in `scripts/.vendored_canon_ref`. Fix upstream in claw, then re-sync
and bump the pin.

## Safe corpus workflow

**Canary before a bulk write.** Run `just seed`, then `just seed-canary
<IDENTIFIER>`. Inspect the written file, not only the exit code, before a full
`seed-apply`.

**Never rename a record file directly.** Change the identifier-to-slug entry in
`data/taxa/PATHS.tsv` and re-seed.

**Never guess a CURIE.** Every identifier in a record came from an inventory;
a curator-added grounding must resolve at its authority.

**An LLM-drafted change is `PROPOSED`, never `REVIEWED`.** Promotion is a
human decision.

## Git workflow

Branch before the first edit. Open a PR for every change, including docs-only
changes. Review the diff as a separate adversarial pass and file findings as
issues. Do not merge without explicit approval. Delete branches after merge.
