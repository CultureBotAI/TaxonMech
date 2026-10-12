# YAML Record Review: Escherichia coli EC4402
- Repository: TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_ec4402.yaml
- Started UTC: 2026-09-23T00:56:28Z
- Finished UTC: 2026-09-23T00:56:28Z
- Verdict: needs curation

## Target

- YAML record: `data/taxa/bacteria/escherichia_coli_ec4402.yaml`
- Identifier: `NCBITaxon:1005530`
- Label: `Escherichia coli EC4402`
- Rank: `STRAIN`
- Parent: `NCBITaxon:562`
- Registry row: `data/taxa/PATHS.tsv:1763`
- Scope row: `curation/seed_scope.tsv:36012`
- A pre-write `find reports/yaml_record_review ... -name '*-escherichia_coli_ec4402.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/escherichia_coli_ec4422.yaml data/taxa/bacteria/escherichia_coli_ec4013.yaml data/taxa/bacteria/escherichia_coli_ec4402.yaml data/taxa/bacteria/escherichia_coli_ec4439.yaml` passed for this four-record batch with zero error rows.
- `just validate data/taxa/bacteria/escherichia_coli_ec4402.yaml` exited successfully with no LinkML validation failure.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:210425` attests the same `NCBITaxon:1005530` identifier, `Escherichia coli EC4402` label, `STRAIN` rank, `NCBITaxon:562` parent, and genetic code `11` present in the YAML.
- The lineage places this node below the expected `Escherichia coli` species parent.
- The NCBI grounding is exact for the EC4402 strain taxon.

## Evidence

- `data/raw/madin_taxa.tsv:297` contributes one Madin trait assertion for `NCBITaxon:1005530`.
- `data/raw/gtdb_mappings.tsv:969` maps `GTDB:s__Escherichia_coli` to this strain with `skos:closeMatch` and genome count `36408`.
- `data/raw/gtdb_species.tsv:59219` shows `GTDB:s__Escherichia_coli` is a GTDB species cluster under `GTDB:g__Escherichia`, not an EC4402 strain.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no rows for `NCBITaxon:1005530`, `Escherichia coli EC4402`, or `escherichia_coli_ec4402`.

## Completeness

- The record includes NCBI, GTDB, and Madin attestations from the three-source seed.
- The GTDB mapping, xref, and exact synonym are generated but semantically inappropriate for a strain-level record.

## Findings

- **Major:** `GTDB:s__Escherichia_coli` denotes the GTDB E. coli species cluster, yet the YAML projects it onto `Escherichia coli EC4402` as a close match, xref, exact synonym, and GTDB source attestation. That makes a single NCBI strain look equivalent to a 36408-genome GTDB species cluster.

## Recommended Edits

- Update the GTDB mapping generation or `src/taxonmech/seed.py` projection path to keep species-cluster mappings off NCBI strain YAMLs.
- Regenerate this record so `GTDB:s__Escherichia_coli` is removed unless a strain-specific GTDB source ID can be cited.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/escherichia_coli_ec4402.yaml` after regeneration.
- Confirm the regenerated YAML has no GTDB exact synonym text equating `Escherichia coli EC4402` with `Escherichia coli`.

## Additional Notes

- Pinned rows in `data/raw/`, `data/atb/`, and `data/straininfo/` were used as source of truth; live NCBI and GTDB lookup was not used.
- `just validate-history` was skipped because no `history/` curation decision was created.
- `just validate-products` was not applicable because there are no `causal_graphs`.

