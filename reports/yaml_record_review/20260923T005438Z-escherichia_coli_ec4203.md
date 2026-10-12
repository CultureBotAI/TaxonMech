# YAML Record Review: Escherichia coli EC4203
- Repository: TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_ec4203.yaml
- Started UTC: 2026-09-23T00:54:38Z
- Finished UTC: 2026-09-23T00:54:38Z
- Verdict: needs curation

## Target

- YAML record: `data/taxa/bacteria/escherichia_coli_ec4203.yaml`
- Identifier: `NCBITaxon:1005523`
- Label: `Escherichia coli EC4203`
- Rank: `STRAIN`
- Parent: `NCBITaxon:562`
- Registry row: `data/taxa/PATHS.tsv:1757`
- Scope row: `curation/seed_scope.tsv:36006`
- A pre-write `find reports/yaml_record_review ... -name '*-escherichia_coli_ec4203.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/escherichia_coli_ec4203.yaml data/taxa/bacteria/escherichia_coli_ec4196.yaml data/taxa/bacteria/escherichia_coli_tw14301.yaml data/taxa/bacteria/escherichia_coli_ec4421.yaml` passed for this four-record batch with 4 scanned files and 0 total error rows.
- `just validate data/taxa/bacteria/escherichia_coli_ec4203.yaml` exited successfully with no LinkML validation failure.

## Identity and Grounding

- The YAML agrees with `data/raw/ncbitaxon_taxa.tsv:210419`: `NCBITaxon:1005523`, label `Escherichia coli EC4203`, rank `STRAIN`, parent `NCBITaxon:562`, genetic code `11`, and snapshot `2026-09-13`.
- The lineage is internally coherent for an E. coli strain under the `Escherichia coli` species.
- `grounding_status: EXACT` is appropriate for the NCBI strain identifier.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210419` provides the NCBI identity and lineage seed.
- `data/raw/madin_taxa.tsv:291` contributes one Madin trait assertion for `NCBITaxon:1005523`.
- `data/raw/gtdb_mappings.tsv:963` maps the GTDB species cluster `GTDB:s__Escherichia_coli` to `NCBITaxon:1005523` as `skos:closeMatch`.
- `data/raw/gtdb_species.tsv:59219` records `GTDB:s__Escherichia_coli` as `s__Escherichia_coli` under `GTDB:g__Escherichia`, with `36408` genomes.
- An exact, gitignore-independent scan found no `data/atb` or `data/straininfo` rows for `NCBITaxon:1005523`, `Escherichia coli EC4203`, or `escherichia_coli_ec4203`.

## Completeness

- The record contains the expected NCBI and Madin provenance for the generated strain.
- The GTDB-derived mapping, xref, source attestation, and exact synonym are present but should not be present on this strain node.

## Findings

- **Major:** `GTDB:s__Escherichia_coli` is a species-cluster identifier, not a strain-specific identifier for `Escherichia coli EC4203`. Emitting it as a `skos:closeMatch`, xref, GTDB source attestation, and exact synonym source makes this NCBI strain appear equivalent to the full GTDB species cluster.

## Recommended Edits

- Fix the GTDB mapping generator or `src/taxonmech/seed.py` so species-level GTDB clusters are not projected to every NCBI strain as close matches, exact synonyms, xrefs, or GTDB attestations.
- Regenerate this record after that shared projection fix.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/escherichia_coli_ec4203.yaml` after regeneration.
- Confirm that `GTDB:s__Escherichia_coli` and the GTDB exact synonym `Escherichia coli` no longer occur in this strain YAML.

## Additional Notes

- Local pinned source rows were the source of truth for this review; live NCBI and GTDB lookups were not used.
- `just validate-history` was skipped because this read-only review did not add a curation decision under `history/`.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

