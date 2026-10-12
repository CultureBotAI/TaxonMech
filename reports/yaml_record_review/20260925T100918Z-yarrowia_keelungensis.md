# YAML Record Review: Yarrowia keelungensis

- Verdict: pass
- Target: `data/taxa/eukaryota/yarrowia_keelungensis.yaml`
- Identifier: `NCBITaxon:1635098`

## Target

Reviewed the complete 75-line YAML record for Yarrowia keelungensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yarrowia_keelungensis.

## Validation

- `just validate data/taxa/eukaryota/yarrowia_keelungensis.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/yarrowia_divulgata.yaml data/taxa/eukaryota/yarrowia_galli.yaml data/taxa/eukaryota/yarrowia_hollandica.yaml data/taxa/eukaryota/yarrowia_keelungensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:425638` is `NCBITaxon:1635098`, `Yarrowia keelungensis`, rank `SPECIES`, parent `NCBITaxon:4951`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Yarrowia keelungensis` entry, at `data/curated/seed_scope.tsv:60942`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 2 related synonyms; the YAML preserves all 2 synonym entries from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` retains 1 redirect into `NCBITaxon:1635098`: `NCBITaxon:445418`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:14005` reports `organism_count` 2 for `NCBITaxon:1635098`, matching the YAML GOLD assertion count of 2.
- Native GOLD evidence has 2 organism rows, 2 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 13 exact rows for `NCBITaxon:1635098`: `culture from holotype` variants for `BCRC 23110`, `CBS 11062`, `JCM 14894`, and `NRRL Y-63742`, plus two `holotype` variants for `SM-22`.
- BacDive has 0 exact local rows for `NCBITaxon:1635098`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:1635098`.

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
