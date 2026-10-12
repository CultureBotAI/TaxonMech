# YAML Record Review: Zarea fungicola

- Verdict: pass
- Target: `data/taxa/eukaryota/zarea_fungicola.yaml`
- Identifier: `NCBITaxon:93591`

## Target

Reviewed the complete 111-line YAML record for Zarea fungicola. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zarea_fungicola.

## Validation

- `just validate data/taxa/eukaryota/zarea_fungicola.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zalerion_sp.yaml data/taxa/eukaryota/zancudomyces_culisetae.yaml data/taxa/eukaryota/zarea_fungicola.yaml data/taxa/eukaryota/zasmidium_angulare.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:15412` is `NCBITaxon:93591`, `Zarea fungicola`, rank `SPECIES`, parent `NCBITaxon:3412474`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zarea fungicola` entry, at `data/curated/seed_scope.tsv:53544`.
- NCBI synonym counts are 5 exact synonyms, 0 broad synonyms, and 6 related synonyms; the YAML preserves all 11 synonym entries from that row.
- All 16 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` retains 2 redirects into `NCBITaxon:93591`: `NCBITaxon:1294127` and `NCBITaxon:170721`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:44804` reports `organism_count` 3 for `NCBITaxon:93591`, matching the YAML GOLD assertion count of 3.
- Native GOLD evidence has 0 organism rows, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 2 exact `culture from type material` rows for `NCBITaxon:93591`: `CBS 992.69` and `CBS:992.69`.
- BacDive has 0 exact local rows for `NCBITaxon:93591`.
- StrainInfo has 52 exact direct strain rows and 60 exact deposit matches for `NCBITaxon:93591`; seven non-direct StrainInfo records contribute 8 of those deposit matches.

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
