# YAML Record Review: Pseudomonas sp. Wr1B10

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_wr1b10.yaml
- Started UTC: 2026-09-23T06:09:27Z
- Finished UTC: 2026-09-23T06:09:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | NCBITaxon:1007153 |
| Label | Pseudomonas sp. Wr1B10 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:196821, unclassified Pseudomonas |
| Maintained path | data/taxa/bacteria/pseudomonas_sp_wr1b10.yaml |
| Generation status | Generated from the committed inventories by `seed_from_sources` |

The whole YAML record was read. It is a seeded NCBI species-level placeholder under `unclassified Pseudomonas`, with `grounding_status: EXACT`, `mapping_status: SEEDED`, bacterial genetic code `11`, no synonym or auxiliary source blocks, `strain_count: 0`, one NCBITAXON source attestation, and a single 2026-09-13 `SEEDED_FROM_SOURCES` event.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1b04.yaml data/taxa/bacteria/pseudomonas_sp_wr1b06.yaml data/taxa/bacteria/pseudomonas_sp_wr1b09.yaml data/taxa/bacteria/pseudomonas_sp_wr1b10.yaml` | Passed; the strict closed-schema validator scanned 4 files and reported 0 files with errors. |
| `just validate data/taxa/bacteria/pseudomonas_sp_wr1b10.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_wr1b10.md'` | No prior report found. The `find` search covered ignored files under the report directory. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found only this taxon's PATHS row and pinned `data/raw/ncbitaxon_taxa.tsv` row among those inventories. |
| `just verify-corpus` | Skipped for this read-only review batch because an earlier full-corpus verification over 625,960 records was clean and no generated YAML was edited. |
| `just validate-history` | Skipped because read-only reviews do not add `history/` decisions. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The record identity is internally consistent. `data/taxa/PATHS.tsv` maps `NCBITaxon:1007153` to `pseudomonas_sp_wr1b10`, and `data/raw/ncbitaxon_taxa.tsv` carries `NCBITaxon:1007153`, label `Pseudomonas sp. Wr1B10`, rank `SPECIES`, parent `NCBITaxon:196821`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.

The lineage places the placeholder below `Bacteria`, `Pseudomonadota`, `Gammaproteobacteria`, `Pseudomonadales`, `Pseudomonadaceae`, `Pseudomonas`, and the no-rank `unclassified Pseudomonas` parent. No GTDB, LPSN, BacDive, ATB, or StrainInfo projection is present.

Live NCBI lookup was unavailable in this run, so the local pinned NCBI row is the reviewed source of truth.

## Evidence

- The NCBITAXON attestation is supported by the exact row for `NCBITaxon:1007153` in `data/raw/ncbitaxon_taxa.tsv`.
- `assertion_count: 1` and `assertion_unit: NAME` accurately describe the single NCBI source assertion.
- There are no synonyms, nomenclature entries, taxonomy mappings, strain records, genome links, ATB sample links, StrainInfo deposits, or causal-graph claims requiring extra evidence.

## Completeness

The record is complete for the pinned inputs inspected. A gitignore-independent `rg --no-ignore --hidden` search over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` for `NCBITaxon:1007153`, `Pseudomonas sp. Wr1B10`, and `pseudomonas_sp_wr1b10` found only PATHS plus NCBI taxonomy evidence; it found no same-taxon ATB or StrainInfo rows.

Given that absence, `strain_count: 0` and the absent optional auxiliary sections are appropriate.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1b10.yaml` after any future seed refresh touching this taxon.
- Re-run `just verify-corpus` after any future change to `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, or `src/taxonmech/seed.py` that could affect this generated record.

## Additional Notes

The no-rank parent is lineage context only; the reviewed record itself remains a species-level NCBI placeholder and therefore stays inside TaxonMech's species-and-below scope.
