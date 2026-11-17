# YAML Record Review: Yunzhangia sonckii

- Verdict: pass
- Target: `data/taxa/eukaryota/yunzhangia_sonckii.yaml`
- Identifier: `NCBITaxon:106019`

## Target

Reviewed the complete 89-line YAML record for Yunzhangia sonckii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yunzhangia_sonckii.

## Validation

- `just validate data/taxa/eukaryota/yunzhangia_sonckii.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/yarrowia_yakushimensis.yaml data/taxa/eukaryota/yueomyces_sinensis.yaml data/taxa/eukaryota/yunzhangia_sonckii.yaml data/taxa/eukaryota/yurkovia_mendeliana.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:19049` is `NCBITaxon:106019`, `Yunzhangia sonckii`, rank `SPECIES`, parent `NCBITaxon:1803523`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Yunzhangia sonckii` entry, at `data/curated/seed_scope.tsv:53719`.
- NCBI synonym counts are 4 exact synonyms, 0 broad synonyms, and 3 related synonyms; the YAML preserves all 7 synonym entries from that row.
- All 12 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:106019`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:1102` reports `organism_count` 1 for `NCBITaxon:106019`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 0 organism rows, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 18 exact rows for `NCBITaxon:106019`: two `culture from type material` variants for `CBS 6713` and 16 `type material` variants for `ATCC 28322`, `IFO 10420`, `IGC 4848`, `JCM 3935`, `MUCL 30044`, `NRRL Y-17172`, and `VKM Y-2708`.
- BacDive has 0 exact local rows for `NCBITaxon:106019`.
- StrainInfo has 2 exact direct strain rows and 11 exact deposit matches for `NCBITaxon:106019`, distributed across siIDs 64272 and 77048.

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
