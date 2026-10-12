# YAML Record Review: Enterobacter sp. Wr1A11

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/enterobacter_sp_wr1a11.yaml
- Started UTC: 2026-09-23T06:35:09Z
- Finished UTC: 2026-09-23T06:35:09Z
- Verdict: pass

## Target

Read the whole generated species record `NCBITaxon:1007185`, `Enterobacter sp. Wr1A11`, at `data/taxa/bacteria/enterobacter_sp_wr1a11.yaml`. It is a seeded NCBITaxon-only bacterial placeholder under `unclassified Enterobacter`, with `strain_count: 0`.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1h11.yaml data/taxa/bacteria/stenotrophomonas_sp_wr1c11.yaml data/taxa/bacteria/enterobacter_sp_wr1a11.yaml data/taxa/bacteria/enterobacter_sp_wr1g06.yaml` | Passed; 4 files scanned and 0 files had errors. |
| `just validate data/taxa/bacteria/enterobacter_sp_wr1a11.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-enterobacter_sp_wr1a11.md'` | No existing report found, including ignored report files. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found the PATHS row and pinned NCBI taxonomy row, with no same-taxon ATB or StrainInfo rows. |
| `just verify-corpus` | Skipped because no generated YAML was edited and earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped because no history record was written. |
| `just validate-products` | Not applicable because no `causal_graphs` are present. |

## Identity and Grounding

The NCBI identity is internally consistent: PATHS maps `NCBITaxon:1007185` to `enterobacter_sp_wr1a11`, and `data/raw/ncbitaxon_taxa.tsv` carries label `Enterobacter sp. Wr1A11`, rank `SPECIES`, parent `NCBITaxon:2608935`, and genetic code `11`. No LPSN, GTDB, or strain overlay alters that seeded identity.

Live NCBI lookup was unavailable, so the pinned local row is the reviewed source of truth.

## Evidence

The NCBITAXON attestation is supported by the exact 2026-09-13 NCBI row and has the correct `NAME` unit/count. No other claim-bearing blocks are present.

## Completeness

The ignored-inclusive exact source search found no auxiliary rows; empty synonyms, nomenclature, mappings, strains, genomes, ATB, StrainInfo, and causal graph sections are appropriate.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- `just validate-strict data/taxa/bacteria/enterobacter_sp_wr1a11.yaml`
- `just verify-corpus`

## Additional Notes

None.
