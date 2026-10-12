# YAML Record Review: Hirsutella rhossiliensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hirsutella_rhossiliensis.yaml
- Started UTC: 2026-09-23T06:57:01Z
- Finished UTC: 2026-09-23T06:57:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:111463` |
| Label | `Hirsutella rhossiliensis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:42367` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hirsutella_rhossiliensis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hirsutella_rhossiliensis.yaml data/taxa/eukaryota/hirsutella_tunicata.yaml data/taxa/eukaryota/histomonas_meleagridis.yaml data/taxa/eukaryota/histoplasma_capsulatum.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with two linked native GOLD projects and no linked native GOLD analyses, four exact NCBI type-material rows, one side NCBI merged-ID row, 20 direct exact StrainInfo rows with 26 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:111463`, `label: Hirsutella rhossiliensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:42367`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:20227`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hirsutella`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:2031`, which records one retained direct organism for `NCBITaxon:111463`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism and two linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:111463`. `Hirsutella rhossiliensis Minter & B.L. Brady, 1980` and `Hirsutella sp. YA-2015` are present in `data/raw/ncbitaxon_taxa.tsv:20227` as related synonyms, and the source row has no exact synonyms to omit.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0583405` organism for `206A_T18_1`, linked projects `Gp0587368` and `Gp0749135`, and no linked native GOLD analysis rows.

NCBI carries four exact type-material aliases for `Hirsutella rhossiliensis` at `data/raw/ncbi_type_material.tsv:6909` through `data/raw/ncbi_type_material.tsv:6912`: `CBS 211.77`, `CBS:211.77`, `IMI 055839`, and `IMI:055839`. These aliases do not contradict the generated `strain_count: 0` because no exact BacDive, StrainInfo assembly, or maintained final strain rows are linked to `NCBITaxon:111463`.

NCBI merged-ID side data maps retired `NCBITaxon:1606761` into `NCBITaxon:111463`, but no retained retired source row exists for that old ID in `data/raw/ncbitaxon_taxa.tsv`, so the absence of a generated `replaces` value is consistent with the generator inputs.

StrainInfo has 20 direct exact rows with 26 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hirsutella_rhossiliensis.yaml` plus `just validate-strict data/taxa/eukaryota/hirsutella_rhossiliensis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hirsutella_rhossiliensis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
