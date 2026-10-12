# YAML Record Review: Yueomyces sinensis

- Verdict: pass
- Target: `data/taxa/eukaryota/yueomyces_sinensis.yaml`
- Identifier: `NCBITaxon:58632`

## Target

Reviewed the complete 79-line YAML record for Yueomyces sinensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yueomyces_sinensis.

## Validation

- `just validate data/taxa/eukaryota/yueomyces_sinensis.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/yarrowia_yakushimensis.yaml data/taxa/eukaryota/yueomyces_sinensis.yaml data/taxa/eukaryota/yunzhangia_sonckii.yaml data/taxa/eukaryota/yurkovia_mendeliana.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:7425` is `NCBITaxon:58632`, `Yueomyces sinensis`, rank `SPECIES`, parent `NCBITaxon:1723649`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Yueomyces sinensis` entry, at `data/curated/seed_scope.tsv:52991`.
- NCBI synonym counts are 1 exact synonym, 0 broad synonyms, and 2 related synonyms; the YAML preserves all 3 synonym entries from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:58632`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:39515` reports `organism_count` 1 for `NCBITaxon:58632`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 2 project rows, and 2 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 17 exact rows for `NCBITaxon:58632`: 15 `culture from type material` variants for `BCRC 22324`, `CBS 7075`, `CCRC 22324`, `CGMCC 2.01395`, `CGMCC 2.1395`, `IFO 10111`, `NBRC 10111`, and `NRRL Y-17406`, plus two `holotype` variants for `AS 2.1395`.
- BacDive has 0 exact local rows for `NCBITaxon:58632`.
- StrainInfo has 0 exact direct strain rows and 1 exact deposit match for `NCBITaxon:58632`, on a `Nadsonia fulvescens var. elongata` record at siID 122363.

## Completeness

- Generated raw strain tables all have 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables all have 0 rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlay tables all have 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
