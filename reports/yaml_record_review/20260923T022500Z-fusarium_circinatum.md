# YAML Record Review: Fusarium circinatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_circinatum.yaml
- Started UTC: 2026-09-23T02:25:00Z
- Finished UTC: 2026-09-23T02:25:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:48490` |
| Label | `Fusarium circinatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171627` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_circinatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_camptoceras.yaml data/taxa/eukaryota/fusarium_cicatricum.yaml data/taxa/eukaryota/fusarium_circinatum.yaml data/taxa/eukaryota/fusarium_clavum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with four organism assertions, four current native GOLD organism rows with four linked projects, three native GOLD analysis rows linked by project ID, one NCBI merged-ID side row, six exact direct StrainInfo rows, ten StrainInfo deposit rows, seventeen NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:48490`, `label: Fusarium circinatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171627`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:6174`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium fujikuroi species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36858`, which records four retained direct organisms for `NCBITaxon:48490`; this agrees with `source_attestations[1].assertion_count: 4` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:48490`. The YAML preserves NCBI's exact synonym `Gibberella circinata` and three related synonyms: `Fusarium circinatum Nirenberg & O'Donnell, 1998`, `Fusarium lateritium f. sp. pini`, and `Fusarium subglutinans f. sp. pini`.

The `data/raw/ncbi_merged_ids.tsv` side inventory has old ID `NCBITaxon:116833` merged into `NCBITaxon:48490`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv` for generated replacement provenance; the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies four organism assertions; the current native GOLD catalogs still contain four exact organism rows, four linked project rows, and three linked analysis rows for the target NCBI taxon.

StrainInfo contains six exact direct rows and ten exact deposit rows for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has seventeen type-material aliases for the target in `typematerial.dmp`: `BBA 69720`, `BBA:69720`, `CBS 405.97`, `CBS 405.97; BBA 69720`, `CBS:405.97`, `DAOM 225113`, `DAOM:225113`, `IMI 375321`, `IMI:375321`, `MRC 7541`, `MRC:7541`, `MRC<ZAF> 7541`, `MRC<ZAF>-7541`, `MRC<ZAF>7541`, `MRC<ZAF>:7541`, `NRRL 25331`, and `NRRL:25331`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI related and exact synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_circinatum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_circinatum.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
