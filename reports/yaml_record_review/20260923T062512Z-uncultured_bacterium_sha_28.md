# YAML Record Review: uncultured bacterium SHA-28

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_bacterium_sha_28.yaml
- Started UTC: 2026-09-23T06:25:12Z
- Finished UTC: 2026-09-23T06:25:12Z
- Verdict: pass

## Target

`NCBITaxon:100717` / `uncultured bacterium SHA-28` is a generated `BACTERIA` `SPECIES` record at `data/taxa/bacteria/uncultured_bacterium_sha_28.yaml`. The whole YAML was read; it contains the NCBI environmental-samples lineage, `grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code `11`, `strain_count: 0`, one NCBITAXON source attestation, and one seed-history entry.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1f03.yaml data/taxa/bacteria/uncultured_bacterium_sha_28.yaml data/taxa/bacteria/pseudomonas_sp_wr1f04.yaml data/taxa/bacteria/pseudomonas_sp_wr1f06.yaml` | Passed; 4 files scanned and 0 files had errors. |
| `just validate data/taxa/bacteria/uncultured_bacterium_sha_28.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uncultured_bacterium_sha_28.md'` | No prior report found, including ignored files under the report directory. |
| `find data/taxa -name uncultured_bacterium_sha_28.yaml` | Located the generated YAML at `data/taxa/bacteria/uncultured_bacterium_sha_28.yaml`; `find` included ignored files. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found only the PATHS row, the exact YAML self-hits, and the pinned NCBI row for this ID/label/slug. |
| `just verify-corpus` | Skipped for this read-only review; earlier full-corpus verification over 625,960 records was clean and no generated YAML was edited. |
| `just validate-history` | Skipped because no `history/` decision was written. |
| `just validate-products` | Not applicable because the record has no `causal_graphs`. |

## Identity and Grounding

`data/taxa/PATHS.tsv` maps `NCBITaxon:100717` to `uncultured_bacterium_sha_28`, and `data/raw/ncbitaxon_taxa.tsv` carries label `uncultured bacterium SHA-28`, rank `SPECIES`, parent `NCBITaxon:48479`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`. The generated lineage terminates at NCBI's no-rank `environmental samples` bucket, which is lineage context rather than a maintained higher-taxon record.

Live NCBI lookup was unavailable; the pinned local NCBI row is the reviewed source of truth.

## Evidence

The NCBITAXON attestation is supported by the exact pinned row for `NCBITaxon:100717`; `assertion_count: 1` / `assertion_unit: NAME` matches that row. No LPSN, GTDB, BacDive, ATB, or StrainInfo claims are present.

## Completeness

The gitignore-independent source search used a CURIE-bounded pattern for short ID `NCBITaxon:100717`, avoiding neighboring `1007170` and unrelated label `100717` false positives. It found no same-taxon ATB or StrainInfo rows, so `strain_count: 0` and the absent auxiliary sections are appropriate.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Run `just validate-strict data/taxa/bacteria/uncultured_bacterium_sha_28.yaml` after seed refreshes touching this taxon.
- Run `just verify-corpus` after future changes to NCBI source rows, scope, or seed logic.

## Additional Notes

None.
