# YAML Record Review: Pseudomonas sp. Wr1F03

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_wr1f03.yaml
- Started UTC: 2026-09-23T06:25:12Z
- Finished UTC: 2026-09-23T06:25:12Z
- Verdict: pass

## Target

`NCBITaxon:1007169` / `Pseudomonas sp. Wr1F03` is a generated `BACTERIA` `SPECIES` record at `data/taxa/bacteria/pseudomonas_sp_wr1f03.yaml`. The whole YAML was read; it contains NCBI identity and lineage under `unclassified Pseudomonas`, `grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code `11`, `strain_count: 0`, one NCBITAXON source attestation, and one seed-history entry.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1f03.yaml data/taxa/bacteria/uncultured_bacterium_sha_28.yaml data/taxa/bacteria/pseudomonas_sp_wr1f04.yaml data/taxa/bacteria/pseudomonas_sp_wr1f06.yaml` | Passed; 4 files scanned and 0 files had errors. |
| `just validate data/taxa/bacteria/pseudomonas_sp_wr1f03.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_wr1f03.md'` | No prior report found, including ignored files under the report directory. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found only the expected PATHS and NCBI rows after tightening the short-ID search to CURIEs, exact labels, and slugs. |
| `just verify-corpus` | Skipped for this read-only review; earlier full-corpus verification over 625,960 records was clean and no generated YAML was edited. |
| `just validate-history` | Skipped because no `history/` decision was written. |
| `just validate-products` | Not applicable because the record has no `causal_graphs`. |

## Identity and Grounding

`data/taxa/PATHS.tsv` maps `NCBITaxon:1007169` to `pseudomonas_sp_wr1f03`, and `data/raw/ncbitaxon_taxa.tsv` carries the same NCBI CURIE, label `Pseudomonas sp. Wr1F03`, rank `SPECIES`, parent `NCBITaxon:196821`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`. No LPSN, GTDB, BacDive, ATB, or StrainInfo assertion changes that identity.

Live NCBI lookup was unavailable; the pinned local NCBI row is the reviewed source of truth.

## Evidence

The sole NCBITAXON attestation is supported by the exact pinned source row and correctly has `assertion_count: 1` / `assertion_unit: NAME`. No optional evidence-bearing blocks are present.

## Completeness

The gitignore-independent `rg --no-ignore --hidden` search over PATHS, raw, ATB, and StrainInfo inputs found no same-taxon auxiliary source rows. `strain_count: 0` and the absence of synonyms, nomenclature, taxonomy mappings, strain records, genome records, and ATB/StrainInfo blocks are therefore appropriate.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Run `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1f03.yaml` after seed refreshes touching this taxon.
- Run `just verify-corpus` after future changes to NCBI source rows, scope, or seed logic.

## Additional Notes

None.
