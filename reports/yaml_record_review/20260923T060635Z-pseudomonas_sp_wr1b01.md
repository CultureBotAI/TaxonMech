# YAML Record Review: Pseudomonas sp. Wr1B01

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_wr1b01.yaml
- Started UTC: 2026-09-23T06:06:35Z
- Finished UTC: 2026-09-23T06:06:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | NCBITaxon:1007148 |
| Label | Pseudomonas sp. Wr1B01 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:196821, unclassified Pseudomonas |
| Maintained path | data/taxa/bacteria/pseudomonas_sp_wr1b01.yaml |
| Generation status | Generated from the committed inventories by `seed_from_sources` |

The whole YAML record was read. It contains a seeded NCBI species-level placeholder under `unclassified Pseudomonas`, no synonyms, no `nomenclature`, no `taxonomy_mappings`, no strain records, `strain_count: 0`, one NCBITAXON source attestation, and one `SEEDED_FROM_SOURCES` curation-history event from 2026-09-13.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1a10.yaml data/taxa/bacteria/pseudomonas_sp_wr1a12.yaml data/taxa/bacteria/pseudomonas_sp_wr1b01.yaml data/taxa/bacteria/pseudomonas_sp_wr1b03.yaml` | Passed for this four-record batch; the strict closed-schema validator accepted all 4 files. |
| `just validate data/taxa/bacteria/pseudomonas_sp_wr1b01.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_wr1b01.md'` | No prior report found. The `find` search covered ignored files under the report directory. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found only the PATHS row and the pinned `data/raw/ncbitaxon_taxa.tsv` row for this taxon among those inventories. |
| `just verify-corpus` | Skipped for this read-only review batch because an earlier full-corpus verification over 625,960 records was clean and no generated YAML was edited. |
| `just validate-history` | Skipped because read-only reviews do not add `history/` decisions. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The record identity is internally consistent. `data/taxa/PATHS.tsv` maps `NCBITaxon:1007148` to `pseudomonas_sp_wr1b01`, and `data/raw/ncbitaxon_taxa.tsv` carries `NCBITaxon:1007148`, label `Pseudomonas sp. Wr1B01`, rank `SPECIES`, parent `NCBITaxon:196821`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.

The `BACTERIA` domain and `Pseudomonas` lineage are consistent with the pinned NCBI parentage in the generated record. There are no GTDB, LPSN, BacDive, ATB, or StrainInfo projections whose identity would need reconciliation with the NCBI placeholder.

Live NCBI lookup was unavailable in this run, so the local pinned NCBI row is the reviewed source of truth.

## Evidence

- The NCBITAXON source attestation is supported by `data/raw/ncbitaxon_taxa.tsv`, which has exactly the asserted source ID and label.
- The attestation uses `assertion_count: 1` and `assertion_unit: NAME`, matching a single pinned NCBI name row for this record.
- No synonyms, nomenclature assertions, taxonomy mappings, strain deposits, genome records, ATB sample links, or StrainInfo sequence links are present, so there is no over-scoped auxiliary evidence to flag.

## Completeness

The sparse record is complete for the committed inventories inspected. The gitignore-independent `rg --no-ignore --hidden` search over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found only the PATHS row and the NCBI taxonomy row for `NCBITaxon:1007148` / `Pseudomonas sp. Wr1B01` / `pseudomonas_sp_wr1b01`; it found no same-taxon ATB or StrainInfo rows to project.

`strain_count: 0` is therefore consistent with the absence of pinned BacDive, ATB, or StrainInfo strain evidence. Empty optional sections for synonyms, nomenclature, mappings, strains, genomes, and causal graphs are correctly absent.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1b01.yaml` after any future seed refresh touching this record.
- Re-run `just verify-corpus` after any future change to `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, or `src/taxonmech/seed.py` that could affect this generated YAML.

## Additional Notes

The parent `NCBITaxon:196821` is a no-rank NCBI bucket, `unclassified Pseudomonas`, retained only as lineage context. TaxonMech's scope rule is still satisfied because the target record itself is species level.
