# YAML Record Review: Zoophthora radicans ARSEF 4784

- Verdict: pass
- Target: `data/taxa/eukaryota/zoophthora_radicans_arsef_4784.yaml`
- Identifier: `NCBITaxon:1314797`

## Target

Reviewed the complete 68-line YAML record for Zoophthora radicans ARSEF 4784. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zoophthora_radicans_arsef_4784.

## Validation

- `just validate data/taxa/eukaryota/zoophthora_radicans_arsef_4784.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zoophthora_radicans.yaml data/taxa/eukaryota/zoophthora_radicans_arsef_4784.yaml data/taxa/eukaryota/zooxanthella_nutricula.yaml data/taxa/eukaryota/zopfia_rhizophila.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:312647` is `NCBITaxon:1314797`, `Zoophthora radicans ARSEF 4784`, rank `STRAIN`, parent `NCBITaxon:42210`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zoophthora radicans ARSEF 4784` entry, at `data/curated/seed_scope.tsv:59387`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 0 related synonyms; the YAML correctly has no synonym entries.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:1314797`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:7698` reports `organism_count` 1 for `NCBITaxon:1314797`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 0 organism rows, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 0 exact rows for `NCBITaxon:1314797`.
- BacDive has 0 exact local rows for `NCBITaxon:1314797`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:1314797`.

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
