# YAML Record Review: Fusarium euwallaceae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_euwallaceae.yaml
- Started UTC: 2026-09-23T02:36:42Z
- Finished UTC: 2026-09-23T02:36:42Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1147111` |
| Label | `Fusarium euwallaceae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:232080` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_euwallaceae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_equiseti.yaml data/taxa/eukaryota/fusarium_euwallaceae.yaml data/taxa/eukaryota/fusarium_falciforme.yaml data/taxa/eukaryota/fusarium_flagelliforme.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, two current native GOLD organism rows with two linked projects, two native GOLD analysis rows linked by project ID, twelve NCBI merged-ID side rows, eight NCBI type-material rows, no StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1147111`, `label: Fusarium euwallaceae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:232080`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:250679`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium solani species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:2997`, which records two retained direct organisms for `NCBITaxon:1147111`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1147111`. The YAML preserves exact synonym `Neocosmospora euwallaceae` and fifteen related NCBI synonyms, including the AF-2, FD31, NRRL, and UCR provisional names.

The `data/raw/ncbi_merged_ids.tsv` side inventory has twelve old IDs merged into `NCBITaxon:1147111`. None are retained in `data/raw/ncbitaxon_taxa.tsv` for generated replacement provenance, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies two organism assertions; the current native GOLD catalogs still contain two exact organism rows, two linked project rows, and two linked analysis rows for the target NCBI taxon.

No exact StrainInfo or BacDive rows are present for the target. NCBI has eight type-material aliases for the target in `typematerial.dmp`: `CBS 135854`, `CBS-135854`, `CBS135854`, `CBS:135854`, `NRRL 54722`, `NRRL:54722`, `BPI 884203`, and `BPI:884203`. No maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI related and exact synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact direct SI-ID or deposit rows; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_euwallaceae.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_euwallaceae.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
