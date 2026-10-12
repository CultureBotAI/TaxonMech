# YAML Record Review: Pseudomonas sp. Wr1D06

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_wr1d06.yaml
- Started UTC: 2026-09-23T06:15:35Z
- Finished UTC: 2026-09-23T06:15:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | NCBITaxon:1007160 |
| Label | Pseudomonas sp. Wr1D06 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:196821, unclassified Pseudomonas |
| Maintained path | data/taxa/bacteria/pseudomonas_sp_wr1d06.yaml |
| Generation status | Generated from the committed inventories by `seed_from_sources` |

The whole YAML record was read. It is a seeded NCBI-only species placeholder with no synonym, nomenclature, taxonomy-mapping, strain, genome, ATB, StrainInfo, or causal-graph sections.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1c10.yaml data/taxa/bacteria/pseudomonas_sp_wr1d02.yaml data/taxa/bacteria/chloroherpeton_thalassium.yaml data/taxa/bacteria/pseudomonas_sp_wr1d06.yaml` | Passed for the four-record batch. |
| `just validate data/taxa/bacteria/pseudomonas_sp_wr1d06.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_wr1d06.md'` | No prior report found. The `find` search included ignored files under `reports/yaml_record_review`. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo data/bacdive data/gold data/bvbrc data/catalog` | Found only the PATHS row and the pinned NCBI row for this taxon. |
| `just verify-corpus` | Skipped for this read-only review; earlier full-corpus verification over 625,960 records was clean and no generated YAML was edited. |
| `just validate-history` | Skipped because this review does not create a `history/` decision. |
| `just validate-products` | Not applicable because this record has no `causal_graphs`. |

## Identity and Grounding

`data/taxa/PATHS.tsv` maps `NCBITaxon:1007160` to `pseudomonas_sp_wr1d06`, and `data/raw/ncbitaxon_taxa.tsv` carries `NCBITaxon:1007160`, `Pseudomonas sp. Wr1D06`, rank `SPECIES`, parent `NCBITaxon:196821`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.

The bacterial `Pseudomonas` lineage and no-rank `unclassified Pseudomonas` parent are internally consistent, and no external LPSN or GTDB identity claim is present. Live NCBI lookup was unavailable, so the pinned local NCBI row is the reviewed source of truth.

## Evidence

- The sole source attestation is supported by the exact `data/raw/ncbitaxon_taxa.tsv` row.
- `assertion_count: 1` / `assertion_unit: NAME` matches the single pinned NCBI name assertion.
- There are no auxiliary assertions lacking source rows.

## Completeness

A gitignore-independent, boundary-aware `rg --no-ignore --hidden` search for `NCBITaxon:1007160`, `Pseudomonas sp. Wr1D06`, and `pseudomonas_sp_wr1d06` across PATHS plus the raw, ATB, StrainInfo, BacDive, GOLD, BV-BRC, and catalog inventories found no same-taxon auxiliary source rows. `strain_count: 0` and the absent optional sections are appropriate.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Run `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1d06.yaml` after a seed refresh touching this taxon.
- Run `just verify-corpus` after edits to `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, or the seed logic.

## Additional Notes

The source search was boundary-aware for the short `NCBITaxon:100716` neighbor, so this record was not conflated with `Chloroherpeton thalassium`.
