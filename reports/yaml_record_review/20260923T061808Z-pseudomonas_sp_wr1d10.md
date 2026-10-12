# YAML Record Review: Pseudomonas sp. Wr1D10

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_wr1d10.yaml
- Started UTC: 2026-09-23T06:18:08Z
- Finished UTC: 2026-09-23T06:18:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | NCBITaxon:1007163 |
| Label | Pseudomonas sp. Wr1D10 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:196821, unclassified Pseudomonas |
| Maintained path | data/taxa/bacteria/pseudomonas_sp_wr1d10.yaml |
| Generation status | Generated from the committed inventories by `seed_from_sources` |

The whole YAML record was read. It has one NCBITAXON attestation and no synonyms, nomenclature, taxonomy mappings, strains, genomes, ATB links, StrainInfo links, or causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1d07.yaml data/taxa/bacteria/pseudomonas_sp_wr1d08.yaml data/taxa/bacteria/pseudomonas_sp_wr1d10.yaml data/taxa/bacteria/pseudomonas_sp_wr1d11.yaml` | Passed; strict validation scanned 4 files and reported 0 files with errors. |
| `just validate data/taxa/bacteria/pseudomonas_sp_wr1d10.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_wr1d10.md'` | No prior report found. The `find` search included ignored report files. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found only this record's PATHS and NCBI taxonomy rows for the exact ID, label, and slug. |
| `just verify-corpus` | Skipped for this read-only review because earlier full-corpus verification over 625,960 records was clean and no generated YAML was edited. |
| `just validate-history` | Skipped because read-only reviews do not write history decisions. |
| `just validate-products` | Not applicable because the record has no `causal_graphs`. |

## Identity and Grounding

The identity is internally consistent: `NCBITaxon:1007163` maps to `pseudomonas_sp_wr1d10` in `data/taxa/PATHS.tsv`, and the pinned `data/raw/ncbitaxon_taxa.tsv` row names it `Pseudomonas sp. Wr1D10` with rank `SPECIES`, parent `NCBITaxon:196821`, and genetic code `11`.

The generated bacterial lineage places the taxon under `Pseudomonas` and no LPSN, GTDB, or strain-level projection conflicts with that NCBI identity. Live NCBI lookup was unavailable, so the local pinned NCBI row is the reviewed source of truth.

## Evidence

- The NCBITAXON source attestation is supported by `data/raw/ncbitaxon_taxa.tsv`.
- `assertion_count: 1` and `assertion_unit: NAME` match the single source assertion.
- No auxiliary evidence blocks are present without source rows.

## Completeness

The gitignore-independent source search covered `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo`; ignored files were included. It found no same-taxon ATB or StrainInfo rows, so `strain_count: 0` and the absent optional sections are appropriate.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Run `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1d10.yaml` after future seed refreshes touching this taxon.
- Run `just verify-corpus` after future changes to source rows, seed scope, or seed logic.

## Additional Notes

None.
