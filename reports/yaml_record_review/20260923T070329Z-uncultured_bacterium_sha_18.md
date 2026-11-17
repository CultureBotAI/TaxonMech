# YAML Record Review: uncultured bacterium SHA-18

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_bacterium_sha_18.yaml
- Started UTC: 2026-09-23T07:03:32Z
- Finished UTC: 2026-09-23T07:03:32Z
- Verdict: pass

## Target

Read the whole generated species record `NCBITaxon:100722`, `uncultured bacterium SHA-18`, at `data/taxa/bacteria/uncultured_bacterium_sha_18.yaml`. It is a seeded NCBITaxon-only bacterial placeholder under the no-rank `environmental samples` lineage bucket, with `strain_count: 0`.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/uncultured_bacterium_sha_18.yaml data/taxa/bacteria/bacterium_yct68.yaml data/taxa/bacteria/bacterium_yct69.yaml data/taxa/bacteria/bacterium_yct7.yaml` | Passed; 4 files scanned and 0 files had errors. |
| `just validate data/taxa/bacteria/uncultured_bacterium_sha_18.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uncultured_bacterium_sha_18.md'` | No prior report found; ignored report files were included. |
| CURIE-bounded `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found the PATHS row and pinned NCBI taxonomy row, with no same-taxon ATB or StrainInfo rows. |
| `just verify-corpus` | Skipped; no generated YAML was edited and earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped; no review history event was created. |
| `just validate-products` | Not applicable; the record has no `causal_graphs`. |

## Identity and Grounding

The NCBI identity is internally consistent: `data/taxa/PATHS.tsv` maps `NCBITaxon:100722` to `uncultured_bacterium_sha_18`, and `data/raw/ncbitaxon_taxa.tsv` carries label `uncultured bacterium SHA-18`, rank `SPECIES`, parent `NCBITaxon:48479`, and genetic code `11`. No LPSN, GTDB, ATB, or StrainInfo overlay alters that seeded identity.

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

- `just validate-strict data/taxa/bacteria/uncultured_bacterium_sha_18.yaml`
- `just verify-corpus`

## Additional Notes

The no-rank `environmental samples` parent is lineage context, not a maintained higher-rank TaxonMech record.
