# YAML Record Review: Hasegawazyma lactosa

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hasegawazyma_lactosa.yaml
- Started UTC: 2026-09-23T06:09:39Z
- Finished UTC: 2026-09-23T06:09:39Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:57693` |
| Label | `Hasegawazyma lactosa` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1798825` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hasegawazyma_lactosa.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/harpochytrium_sp.yaml data/taxa/eukaryota/harringtonia_lauricola.yaml data/taxa/eukaryota/hasegawazyma_lactosa.yaml data/taxa/eukaryota/haslea_ostrearia.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, no current exact native GOLD organisms, 24 exact NCBI type-material rows, no side NCBI merged-ID rows, five direct exact StrainInfo rows with 22 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:57693`, `label: Hasegawazyma lactosa`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1798825`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:7328`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hasegawazyma`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39302`, which records one retained direct organism for `NCBITaxon:57693`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:57693`. `Rhodotorula lactosa` is present in `data/raw/ncbitaxon_taxa.tsv:7328` as an exact synonym, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs do not have an exact organism row for `NCBITaxon:57693`, so the record is relying on the retained aggregate source rather than a current native side row.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:237909` through `data/raw/ncbi_type_material.tsv:237932` as 24 spellings for `CBS 5826`, `ATCC 18176`, `BCRC 22480`, `CCRC 22480`, `DBVPG 7022`, `IAM 12230`, `IFO 1423`, `IGC 4843`, `JCM 1546`, `MUCL 30445`, `NRRL Y-17377`, and `UCD 67-62`. StrainInfo also has five direct exact rows with 22 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hasegawazyma_lactosa.yaml` plus `just validate-strict data/taxa/eukaryota/hasegawazyma_lactosa.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hasegawazyma_lactosa` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; current native GOLD rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
