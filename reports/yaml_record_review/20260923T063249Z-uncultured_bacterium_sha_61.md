# YAML Record Review: uncultured bacterium SHA-61

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_bacterium_sha_61.yaml
- Started UTC: 2026-09-23T06:32:49Z
- Finished UTC: 2026-09-23T06:32:49Z
- Verdict: pass

## Target

The complete generated YAML for `NCBITaxon:100718`, `uncultured bacterium SHA-61`, was read at `data/taxa/bacteria/uncultured_bacterium_sha_61.yaml`. It is a bacterial species-level placeholder under NCBI's no-rank `environmental samples` lineage bucket, with one NCBITAXON attestation and no auxiliary sections.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/uncultured_bacterium_sha_61.yaml data/taxa/bacteria/pseudomonas_sp_wr1h05.yaml data/taxa/bacteria/pseudomonas_sp_wr1h07.yaml data/taxa/bacteria/pseudomonas_sp_wr1h08.yaml` | Passed for the batch. |
| `just validate data/taxa/bacteria/uncultured_bacterium_sha_61.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uncultured_bacterium_sha_61.md'` | No prior report found; ignored report files were included. |
| CURIE-bounded `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found only PATHS and NCBI rows for this taxon. |
| `just verify-corpus` | Skipped; no generated YAML was edited and earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped; no review history event was created. |
| `just validate-products` | Not applicable; the record has no `causal_graphs`. |

## Identity and Grounding

`data/taxa/PATHS.tsv` maps `NCBITaxon:100718` to `uncultured_bacterium_sha_61`, and `data/raw/ncbitaxon_taxa.tsv` identifies the same CURIE as `uncultured bacterium SHA-61` with rank `SPECIES`, parent `NCBITaxon:48479`, and genetic code `11`. Live NCBI lookup was unavailable, so the pinned NCBI row is the reviewed source of truth.

## Evidence

The NCBITAXON source attestation is supported by the exact pinned row. The record has no synonym, nomenclature, mapping, strain, genome, ATB, StrainInfo, or causal-graph claims needing additional evidence.

## Completeness

The gitignore-independent source search found no same-taxon rows in ATB or StrainInfo. `strain_count: 0` and the absent optional sections are complete for the committed local inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- `just validate-strict data/taxa/bacteria/uncultured_bacterium_sha_61.yaml`
- `just verify-corpus`

## Additional Notes

The no-rank `environmental samples` parent is lineage context, not a maintained higher-rank TaxonMech record.
