# YAML Record Review: Pseudomonas sp. Wr1G04

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_wr1g04.yaml
- Started UTC: 2026-09-23T06:30:18Z
- Finished UTC: 2026-09-23T06:30:18Z
- Verdict: pass

## Target

Reviewed the complete generated record for `NCBITaxon:1007177`, `Pseudomonas sp. Wr1G04`, a bacterial species placeholder under `NCBITaxon:196821` at `data/taxa/bacteria/pseudomonas_sp_wr1g04.yaml`.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1g03.yaml data/taxa/bacteria/pseudomonas_sp_wr1g04.yaml data/taxa/bacteria/pseudomonas_sp_wr1g05.yaml data/taxa/bacteria/pseudomonas_sp_wr1g10.yaml` | Passed; strict validation scanned 4 files and reported 0 errors. |
| `just validate data/taxa/bacteria/pseudomonas_sp_wr1g04.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_wr1g04.md'` | No existing report found, including ignored files. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found only this taxon's PATHS row and NCBI taxonomy row. |
| `just verify-corpus` | Skipped for this read-only review because earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped because no history record was written. |
| `just validate-products` | Not applicable; no `causal_graphs` are present. |

## Identity and Grounding

`data/taxa/PATHS.tsv` maps `NCBITaxon:1007177` to `pseudomonas_sp_wr1g04`; `data/raw/ncbitaxon_taxa.tsv` gives the same ID label `Pseudomonas sp. Wr1G04`, rank `SPECIES`, parent `NCBITaxon:196821`, and genetic code `11`. With no GTDB or LPSN projection on this record, the NCBI identity is unambiguous.

Live NCBI lookup was unavailable, so the local pinned NCBI row is the reviewed source of truth.

## Evidence

The NCBITAXON source attestation is directly supported by the pinned NCBI row. The record has no synonyms, nomenclature, mappings, strains, genome links, or causal-graph claims that would need additional evidence.

## Completeness

The gitignore-independent source search covered `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` and found no same-taxon auxiliary source rows. The absent optional sections and `strain_count: 0` are correct for the committed inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1g04.yaml`
- `just verify-corpus`

## Additional Notes

None.
