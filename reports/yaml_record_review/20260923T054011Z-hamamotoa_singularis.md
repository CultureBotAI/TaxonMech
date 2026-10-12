# YAML Record Review: Hamamotoa singularis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hamamotoa_singularis.yaml
- Started UTC: 2026-09-23T05:40:11Z
- Finished UTC: 2026-09-23T05:40:11Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5445` |
| Label | `Hamamotoa singularis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1801561` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hamamotoa_singularis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/halteria_grandinella.yaml data/taxa/eukaryota/halteromyces_radiatus.yaml data/taxa/eukaryota/hamamotoa_singularis.yaml data/taxa/eukaryota/hamiltosporidium_magnivora.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with eight organism assertions, eight exact current native GOLD organisms with no linked native GOLD projects or analyses, 17 exact NCBI type-material rows, no side NCBI merged-ID rows, two direct exact StrainInfo rows with 12 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5445`, `label: Hamamotoa singularis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1801561`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2412`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hamamotoa`; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38381`, which records eight retained direct organisms for `NCBITaxon:5445`; this agrees with `source_attestations[1].assertion_count: 8` and its organism assertion unit. The current native GOLD catalogs also contain eight exact organisms for `ATCC 24193`, `CBS 5109`, `DSM 70871`, `JCM 5356`, `NCYC 900`, `NRRL Y-5852`, `Sp-0601`, and `UCD 60-79`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5445`. `Bullera singularis` and `Sporobolomyces singularis` are present in `data/raw/ncbitaxon_taxa.tsv:2412` as exact synonyms, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies eight organism assertions. The current native GOLD catalogs have eight exact organism rows named under the synonym `Bullera singularis` and no linked native project or analysis rows.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:232026` through `data/raw/ncbi_type_material.tsv:232042` as 17 spellings for `ATCC 24193`, `CBS 5109`, `DBVPG 6620`, `JCM 5356`, `MUCL 27849`, `NCYC 900`, `NRRL Y-5852`, and `UCD 60-79`, all marked type material for `Sporobolomyces singularis`. StrainInfo also has two direct exact rows with 12 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

No side NCBI merged-ID row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hamamotoa_singularis.yaml` plus `just validate-strict data/taxa/eukaryota/hamamotoa_singularis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hamamotoa_singularis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
