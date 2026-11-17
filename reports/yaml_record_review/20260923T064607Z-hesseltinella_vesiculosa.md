# YAML Record Review: Hesseltinella vesiculosa

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hesseltinella_vesiculosa.yaml
- Started UTC: 2026-09-23T06:46:07Z
- Finished UTC: 2026-09-23T06:46:07Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:101127` |
| Label | `Hesseltinella vesiculosa` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:101126` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hesseltinella_vesiculosa.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hermanozyma_aechmeae.yaml data/taxa/eukaryota/hermanssonia_centrifuga.yaml data/taxa/eukaryota/herpomyces_periplanetae.yaml data/taxa/eukaryota/hesseltinella_vesiculosa.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, one exact current native GOLD organism with three linked native GOLD projects and two linked native GOLD analyses, no exact NCBI type-material rows, no side NCBI merged-ID rows, one direct exact StrainInfo row with five deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:101127`, `label: Hesseltinella vesiculosa`, `rank: SPECIES`, `parent_taxon: NCBITaxon:101126`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:17441`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hesseltinella`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:257`, which records two retained direct organisms for `NCBITaxon:101127`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain one exact organism, three linked projects, and two linked analyses.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:101127`. `Hesseltinella vesiculosa H.P. Upadhyay, 1970` is present in `data/raw/ncbitaxon_taxa.tsv:17441` as a related synonym, and the source row has no exact synonyms to omit.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact organism `Go0046760` for `NRRL 3301`; linked projects `Gp0046759`, `Gp0046760`, and `Gp0455850`; and two native analyses linked by `Gp0046759`.

StrainInfo has one direct exact row for this taxon, with five deposits: `CBS 197.68`, `IMI 132188`, `VKM F-1523`, `ATCC 42645`, and `NRRL 3301`. That side-inventory row is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No NCBI type-material row, side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hesseltinella_vesiculosa.yaml` plus `just validate-strict data/taxa/eukaryota/hesseltinella_vesiculosa.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hesseltinella_vesiculosa` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
