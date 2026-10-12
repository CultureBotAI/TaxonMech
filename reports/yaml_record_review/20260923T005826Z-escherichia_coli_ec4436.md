# YAML Record Review: Escherichia coli EC4436
- Repository: TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_ec4436.yaml
- Started UTC: 2026-09-23T00:58:26Z
- Finished UTC: 2026-09-23T00:58:26Z
- Verdict: needs curation

## Target

- YAML record: `data/taxa/bacteria/escherichia_coli_ec4436.yaml`
- Identifier: `NCBITaxon:1005532`
- Label: `Escherichia coli EC4436`
- Rank: `STRAIN`
- Parent: `NCBITaxon:562`
- Registry row: `data/taxa/PATHS.tsv:1765`
- Scope row: `curation/seed_scope.tsv:36014`
- A pre-write `find reports/yaml_record_review ... -name '*-escherichia_coli_ec4436.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/escherichia_coli_ec4436.yaml data/taxa/bacteria/escherichia_coli_ec4437.yaml data/taxa/bacteria/escherichia_coli_ec4448.yaml data/taxa/bacteria/escherichia_coli_ec1738.yaml` passed for this four-record batch with 0 total error rows.
- `just validate data/taxa/bacteria/escherichia_coli_ec4436.yaml` passed with no LinkML issues.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:210427` matches the YAML's `NCBITaxon:1005532` identifier, `Escherichia coli EC4436` label, `STRAIN` rank, `NCBITaxon:562` parent, and genetic code `11`.
- The YAML lineage terminates at `NCBITaxon:562` / `Escherichia coli`, which is coherent for this strain.
- The NCBI grounding is exact for the target taxon.

## Evidence

- `data/raw/madin_taxa.tsv:299` contributes one Madin trait assertion for `NCBITaxon:1005532`.
- `data/raw/gtdb_mappings.tsv:971` maps `GTDB:s__Escherichia_coli` to `NCBITaxon:1005532` with `skos:closeMatch` and genome count `36408`.
- `data/raw/gtdb_species.tsv:59219` shows that `GTDB:s__Escherichia_coli` is a species-cluster source with `36408` genomes.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` for `NCBITaxon:1005532`, `Escherichia coli EC4436`, and `escherichia_coli_ec4436` found no same-taxon auxiliary rows.

## Completeness

- The record includes the expected generated NCBI identity, lineage, Madin attestation, GTDB mapping, xref, synonym, source attestations, and curation history for a three-source seed row.
- The record is over-complete because the GTDB species cluster is attached to a narrower NCBI strain node.

## Findings

- **Major:** `GTDB:s__Escherichia_coli` is a GTDB species cluster, but this record promotes it to a close match, xref, exact synonym source, and genome attestation for strain `Escherichia coli EC4436`. That makes the strain semantically equivalent to a broad species cluster.

## Recommended Edits

- Fix `data/raw/gtdb_mappings.tsv` generation and `src/taxonmech/seed.py` projection so GTDB species-cluster rows are not emitted as NCBI strain equivalences.
- Regenerate this record after the shared mapping fix so the GTDB species cluster is absent from the strain-level YAML.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/escherichia_coli_ec4436.yaml` after regeneration.
- Confirm that no regenerated `synonyms` entry says `Escherichia coli` is an `EXACT_SYNONYM` for `Escherichia coli EC4436`.

## Additional Notes

- Pinned local source rows were treated as authoritative; live NCBI and GTDB lookups were not used.
- `just validate-history` was skipped because this review added no `history/` file.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

