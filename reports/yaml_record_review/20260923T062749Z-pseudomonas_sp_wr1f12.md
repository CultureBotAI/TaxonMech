# YAML Record Review: Pseudomonas sp. Wr1F12

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_wr1f12.yaml
- Started UTC: 2026-09-23T06:27:49Z
- Finished UTC: 2026-09-23T06:27:49Z
- Verdict: pass

## Target

The whole generated record for `NCBITaxon:1007174` / `Pseudomonas sp. Wr1F12` was read at `data/taxa/bacteria/pseudomonas_sp_wr1f12.yaml`. It is a `BACTERIA` `SPECIES` record under `NCBITaxon:196821` with one NCBITAXON name attestation and no auxiliary evidence sections.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1f08.yaml data/taxa/bacteria/pseudomonas_sp_wr1f10.yaml data/taxa/bacteria/pseudomonas_sp_wr1f12.yaml data/taxa/bacteria/pseudomonas_sp_wr1g02.yaml` | Passed for the batch. |
| `just validate data/taxa/bacteria/pseudomonas_sp_wr1f12.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_wr1f12.md'` | No previous report found; ignored reports were included. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found only the PATHS and pinned NCBI rows for this taxon. |
| `just verify-corpus` | Skipped because this review was read-only and earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped because no history record was written. |
| `just validate-products` | Not applicable because no `causal_graphs` are present. |

## Identity and Grounding

`data/taxa/PATHS.tsv` maps `NCBITaxon:1007174` to `pseudomonas_sp_wr1f12`; `data/raw/ncbitaxon_taxa.tsv` has label `Pseudomonas sp. Wr1F12`, rank `SPECIES`, parent `NCBITaxon:196821`, and genetic code `11` for the same ID. The record has a bacterial `Pseudomonas` lineage, and the pinned NCBI row is the source of truth because live NCBI lookup was unavailable.

## Evidence

The single NCBITAXON attestation is exactly supported by `data/raw/ncbitaxon_taxa.tsv`, with `assertion_count: 1` and `assertion_unit: NAME`. No unsupported synonyms, nomenclature, mappings, strain links, or genome links are present.

## Completeness

The gitignore-independent exact search found no same-taxon rows in `data/atb` or `data/straininfo`; the empty optional slots and `strain_count: 0` are complete for the committed sources.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1f12.yaml`
- `just verify-corpus`

## Additional Notes

None.
