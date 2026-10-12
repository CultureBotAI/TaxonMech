# YAML Record Review: Capnocytophaga gingivalis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/capnocytophaga_gingivalis.yaml
- Started UTC: 2026-10-02T08:45:06Z
- Finished UTC: 2026-10-02T08:45:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017` |
| Label | `Capnocytophaga gingivalis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1016` |
| Parent label | `Capnocytophaga` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `5` |
| Source attestations | `NCBITAXON`, `LPSN`, `GTDB`, `BACDIVE`, `GOLD`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/capnocytophaga_gingivalis.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/capnocytophaga_gingivalis.yaml data/taxa/bacteria/enterobacter_sp_jdm_19.yaml data/taxa/bacteria/paenimyroides_anatoliense.yaml data/taxa/bacteria/escherichia_coli_c54_58_1b.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 1,875 lines, 11 lineage entries, 1 nomenclature record, 2 taxonomy mappings, 2 synonyms, 2 xrefs, 5 BacDive strains, and 6 source attestations. |
| `taxonmech_bounded_scan.py data/taxa/bacteria/capnocytophaga_gingivalis.yaml` | Not applicable: the NCBI-only helper exited with `NCBI source mismatch` because the record intentionally combines NCBITaxon, LPSN, GTDB, BacDive, GOLD, and MADIN evidence. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*capnocytophaga_gingivalis.md'` | Pass: no prior report existed for this stem. |
| Exact NCBI, LPSN, GTDB, BacDive, GOLD, MADIN, type-material, strain-link, and strain-genome scans | Pass: all inspected source rows agree with the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10181 maps `NCBITaxon:1017` to `capnocytophaga_gingivalis`.
- `curation/seed_scope.tsv` row 8660 keeps this species in scope with an attested six-source rule.
- `data/raw/ncbitaxon_taxa.tsv` row 790 names the same species, parent genus, rank, genetic code, two NCBI synonyms, and source set `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal`.
- `data/raw/lpsn_names.tsv` row 16021 backs the correct-name LPSN block and links `GTDB:s__Capnocytophaga_gingivalis`, seven type-strain designations, two DOI citations, PMID `518239`, and `INSDC:AB638448`.
- The generated `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the directly attested NCBI species.

## Evidence

- `source_attestations` accurately summarize NCBITaxon name, LPSN name, GTDB genome, BacDive strain, GOLD organism, and MADIN trait-assertion evidence.
- `data/raw/gtdb_species.tsv` rows 40622 and 40641 plus `data/raw/gtdb_mappings.tsv` rows 1173 and 1174 support the two GTDB broad species mappings with genome counts 28 and 12.
- `data/raw/gold_organisms.tsv` row 291 supports the direct GOLD assertion count of 27; `data/raw/madin_taxa.tsv` row 458 supports the direct MADIN assertion count of 3.
- Four BacDive strains are filed directly under `NCBITaxon:1017` in `data/raw/bacdive_strains.tsv` rows 64856, 64857, 64870, and 68244.
- `kgmicrobe.strain:bacdive_5487` is filed under descendant `NCBITaxon:553178` in `data/raw/bacdive_strains.tsv` row 5377 and is correctly gathered with `classified_as: NCBITaxon:553178`.
- StrainInfo, GTDB, BV-BRC, GOLD, BacDive, and NCBI Assembly genome and related-record rows are preserved under their matching BacDive strain blocks.

## Completeness

- The five `strains` blocks start at YAML lines 98, 942, 1257, 1511, and 1765 and match the five BacDive strain IDs expected for this species-level record.
- The first strain is the ATCC 33624 type strain from the child NCBI strain record; its eight culture-collection identifiers agree with the BacDive row and the NCBI type-material rows.
- The LPSN xref appears both in `nomenclature` and top-level `xrefs`; the primary GTDB species appears in `taxonomy_mappings`, `xrefs`, and `source_attestations`.
- GOLD and MADIN are represented as direct count-style attestations, matching the seeder rule that descendants are not gathered for those sources.
- No causal graph is expected for this generated taxon identity record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/capnocytophaga_gingivalis.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/capnocytophaga_gingivalis.yaml`.
- Re-run the BacDive, StrainInfo, GTDB, GOLD, and MADIN source scans after any source refresh.

## Additional Notes

- The source scans used `--no-ignore --hidden`, so ignored files were included.
- `bacdive_142751` has GOLD rows that mention `NCBITaxon:1017`, but its own BacDive row is filed under `NCBITaxon:45242`; it is therefore not one of this record's five asserted BacDive strains.
- The source attestation lines in the YAML are 1833 for NCBITAXON, 1839 for LPSN, 1845 for GTDB, 1852 for BACDIVE, 1858 for GOLD, and 1864 for MADIN.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10181 |
| `curation/seed_scope.tsv` | 8660 |
| `data/raw/ncbitaxon_taxa.tsv` | 790 and 129513 |
| `data/raw/lpsn_names.tsv` | 16021 |
| `data/raw/gtdb_species.tsv` | 40622 and 40641 |
| `data/raw/gtdb_mappings.tsv` | 1173 and 1174 |
| `data/raw/gold_organisms.tsv` | 291 |
| `data/raw/madin_taxa.tsv` | 458 |
| `data/raw/bacdive_strains.tsv` | 5377, 64856, 64857, 64870, 68244 |
| `data/raw/ncbi_type_material.tsv` | 1082-1098 |
