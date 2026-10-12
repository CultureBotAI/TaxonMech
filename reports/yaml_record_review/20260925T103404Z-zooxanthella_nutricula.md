# YAML Record Review: Zooxanthella nutricula

- Verdict: pass
- Target: `data/taxa/eukaryota/zooxanthella_nutricula.yaml`
- Identifier: `NCBITaxon:1333877`

## Target

Reviewed the complete 82-line YAML record for Zooxanthella nutricula. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zooxanthella_nutricula.

## Validation

- `just validate data/taxa/eukaryota/zooxanthella_nutricula.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zoophthora_radicans.yaml data/taxa/eukaryota/zoophthora_radicans_arsef_4784.yaml data/taxa/eukaryota/zooxanthella_nutricula.yaml data/taxa/eukaryota/zopfia_rhizophila.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:319680` is `NCBITaxon:1333877`, `Zooxanthella nutricula`, rank `SPECIES`, parent `NCBITaxon:1333873`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zooxanthella nutricula` entry, at `data/curated/seed_scope.tsv:59521`.
- NCBI synonym counts are 3 exact synonyms, 0 broad synonyms, and 5 related synonyms; the YAML preserves all 8 synonym entries from that row.
- All 9 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` retains 3 redirects into `NCBITaxon:1333877`: `NCBITaxon:1333874`, `NCBITaxon:1426914`, and `NCBITaxon:47176`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:8107` reports `organism_count` 1 for `NCBITaxon:1333877`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 0 exact rows for `NCBITaxon:1333877`.
- BacDive has 0 exact local rows for `NCBITaxon:1333877`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:1333877`.

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
