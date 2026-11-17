# YAML Record Review: Entophlyctis luteolus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/entophlyctis_luteolus.yaml
- Started UTC: 2026-09-23T00:27:28Z
- Finished UTC: 2026-09-23T00:27:28Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:109932` |
| Label | `Entophlyctis luteolus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:64501` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/entophlyctis_luteolus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/entophlyctis_helioformis.yaml data/taxa/eukaryota/entophlyctis_luteolus.yaml data/taxa/eukaryota/entrophospora_candida.yaml data/taxa/eukaryota/entrophospora_etunicata.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three organism assertions, three exact native GOLD organism rows, four exact native GOLD project rows, no native GOLD analyses, six NCBI type-material rows, one exact StrainInfo row with one deposit, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:109932`, `label: Entophlyctis luteolus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:64501`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:19739`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Entophlyctis` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:1841`, which records three retained direct organisms for `NCBITaxon:109932`; this agrees with `source_attestations[1].assertion_count: 3` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:109932`. The YAML preserves NCBI's one related synonym, `Entophlyctis luteolus Longcore, 1995`; NCBI supplies no exact or broad synonyms and no old-ID side rows.

The six NCBI type-material rows preserve aliases for `ATCC 90967`, `JEL0129`, and `L-129` under `Entophlyctis luteolus`. The native GOLD catalogs contain three exact organism rows, `Go0389719`, `Go0515098`, and `Go0515099`, with four matching projects and no matching native GOLD analysis rows.

StrainInfo contains one exact target row, `siID 250256`, with one deposit designation, `ATCC 90967`; that side row does not produce a BacDive-derived local strain child for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/entophlyctis_luteolus.yaml` plus `just validate-strict data/taxa/eukaryota/entophlyctis_luteolus.yaml`.

## Additional Notes

The NCBI type-material sample was expanded with an exact `NCBITaxon:109932` lookup in `data/raw/ncbi_type_material.tsv` to account for all 6 designations. The retained GOLD aggregate count matches the three current native GOLD organism rows.
