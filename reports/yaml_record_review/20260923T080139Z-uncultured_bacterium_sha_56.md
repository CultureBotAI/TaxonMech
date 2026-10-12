# YAML Record Review: uncultured bacterium SHA-56

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_bacterium_sha_56.yaml
- Started UTC: 2026-09-23T08:01:39Z
- Finished UTC: 2026-09-23T08:01:39Z
- Verdict: pass

## Target

Read the whole generated species record `NCBITaxon:100731`, `uncultured bacterium SHA-56`, at `data/taxa/bacteria/uncultured_bacterium_sha_56.yaml`. It is a seeded NCBITaxon-only bacterial environmental-sample placeholder under `environmental samples`, with `strain_count: 0`.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/bacillus_sp_zk4806.yaml data/taxa/bacteria/bacillus_sp_zk4807.yaml data/taxa/bacteria/bacillus_sp_zk4808.yaml data/taxa/bacteria/uncultured_bacterium_sha_56.yaml` | Passed; 4 files scanned and 0 files had errors. |
| `just validate data/taxa/bacteria/uncultured_bacterium_sha_56.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uncultured_bacterium_sha_56.md'` | No prior report found; ignored report files were included. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo curation/seed_scope.tsv` | Found the exact PATHS row, pinned NCBI taxonomy row, and seed-scope row, with no same-taxon ATB or StrainInfo rows. |
| `just verify-corpus` | Skipped; no generated YAML was edited and earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped; no review history event was created. |
| `just validate-products` | Not applicable; the record has no `causal_graphs`. |

## Identity and Grounding

The NCBI identity is internally consistent: `data/taxa/PATHS.tsv` maps `NCBITaxon:100731` to `uncultured_bacterium_sha_56`, and `data/raw/ncbitaxon_taxa.tsv` carries label `uncultured bacterium SHA-56`, rank `SPECIES`, parent `NCBITaxon:48479`, and genetic code `11`. No LPSN, GTDB, ATB, or StrainInfo overlay alters that seeded identity.

Live NCBI lookup was unavailable, so the pinned 2026-09-13 NCBI row is the reviewed source of truth.

## Evidence

The NCBITAXON source attestation is supported by the exact pinned row and has the correct `NAME` unit/count. No synonym, nomenclature, mapping, strain, genome, ATB, StrainInfo, or causal-graph claims need additional evidence.

## Completeness

The ignored-inclusive exact source search found no same-taxon rows in ATB or StrainInfo. `strain_count: 0` and the absent optional sections are complete for the committed local inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- `just validate-strict data/taxa/bacteria/uncultured_bacterium_sha_56.yaml`
- `just verify-corpus`

## Additional Notes

The NCBI lineage label `environmental samples` is represented only as lineage context. The source search was refined with field boundaries because `NCBITaxon:100731` is a prefix of nearby `NCBITaxon:100731x` Bacillus records.
