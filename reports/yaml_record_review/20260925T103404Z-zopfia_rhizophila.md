# YAML Record Review: Zopfia rhizophila

- Verdict: pass
- Target: `data/taxa/eukaryota/zopfia_rhizophila.yaml`
- Identifier: `NCBITaxon:160035`

## Target

Reviewed the complete 78-line YAML record for Zopfia rhizophila. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zopfia_rhizophila.

## Validation

- `just validate data/taxa/eukaryota/zopfia_rhizophila.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zoophthora_radicans.yaml data/taxa/eukaryota/zoophthora_radicans_arsef_4784.yaml data/taxa/eukaryota/zooxanthella_nutricula.yaml data/taxa/eukaryota/zopfia_rhizophila.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:33057` is `NCBITaxon:160035`, `Zopfia rhizophila`, rank `SPECIES`, parent `NCBITaxon:160034`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zopfia rhizophila` entry, at `data/curated/seed_scope.tsv:54159`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML preserves the related synonym from that row.
- All 15 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:160035`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:12921` reports `organism_count` 1 for `NCBITaxon:160035`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 2 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 0 exact rows for `NCBITaxon:160035`.
- BacDive has 0 exact local rows for `NCBITaxon:160035`.
- StrainInfo has 1 exact direct strain row and 1 exact deposit match for `NCBITaxon:160035`, both at siID 175217.

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
