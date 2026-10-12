# YAML Record Review: Pseudomonas sp. Wr1E04

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_wr1e04.yaml
- Started UTC: 2026-09-23T06:20:16Z
- Finished UTC: 2026-09-23T06:20:16Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007166`
- Label: `Pseudomonas sp. Wr1E04`
- Rank/domain: `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:196821`, `unclassified Pseudomonas`
- Maintained path: `data/taxa/bacteria/pseudomonas_sp_wr1e04.yaml`
- Generation status: generated from the committed inventories by `seed_from_sources`

The whole record was read. It contains only seeded NCBI identity, lineage, grounding/status fields, bacterial genetic code `11`, `strain_count: 0`, one NCBITAXON source attestation, and one 2026-09-13 seed event.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1e02.yaml data/taxa/bacteria/pseudomonas_sp_wr1e04.yaml data/taxa/bacteria/pseudomonas_sp_wr1e09.yaml data/taxa/bacteria/pseudomonas_sp_wr1f01.yaml` | Passed; 4 files scanned and 0 files had errors. |
| `just validate data/taxa/bacteria/pseudomonas_sp_wr1e04.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_wr1e04.md'` | No previous report found, including ignored report files. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found only the PATHS and `data/raw/ncbitaxon_taxa.tsv` rows for this exact ID/label/slug. |
| `just verify-corpus` | Skipped; this was a read-only review, no generated YAML was edited, and an earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped; no history record was written. |
| `just validate-products` | Not applicable; no `causal_graphs` are present. |

## Identity and Grounding

`data/taxa/PATHS.tsv` maps `NCBITaxon:1007166` to `pseudomonas_sp_wr1e04`; `data/raw/ncbitaxon_taxa.tsv` carries the same ID and label with rank `SPECIES`, parent `NCBITaxon:196821`, and genetic code `11`. The lineage is a bacterial `Pseudomonas` lineage ending at the no-rank unclassified bucket. Live NCBI lookup was unavailable, so the pinned local row was the identity source of truth.

## Evidence

The NCBITAXON source attestation is supported exactly by the 2026-09-13 NCBI snapshot row. There are no synonyms, LPSN names, GTDB mappings, strains, genomes, ATB evidence, StrainInfo records, or graph claims requiring additional evidence.

## Completeness

A gitignore-independent `rg --no-ignore --hidden` search covered `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` and found no same-taxon auxiliary source rows. The sparse NCBI-only representation and `strain_count: 0` are complete for the committed evidence inspected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Run `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1e04.yaml` after any future seed refresh touching this taxon.
- Run `just verify-corpus` after any future source-row, seed-scope, or seed-logic change that could alter this generated record.

## Additional Notes

None.
