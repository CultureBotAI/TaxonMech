# YAML Record Review: Yarrowia alimentaria

- Verdict: pass
- Target: `data/taxa/eukaryota/yarrowia_alimentaria.yaml`
- Identifier: `NCBITaxon:479092`

## Target

Reviewed the complete 88-line YAML record for Yarrowia alimentaria. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yarrowia_alimentaria.

## Validation

- `just validate data/taxa/eukaryota/yarrowia_alimentaria.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/yarrowia_alimentaria.yaml data/taxa/eukaryota/yarrowia_brassicae.yaml data/taxa/eukaryota/yarrowia_bubula.yaml data/taxa/eukaryota/yarrowia_deformans.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:107040` is `NCBITaxon:479092`, `Yarrowia alimentaria`, rank `SPECIES`, parent `NCBITaxon:4951`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Yarrowia alimentaria` entry, at `data/curated/seed_scope.tsv:55783`.
- NCBI synonym counts are 1 exact synonym, 0 broad synonyms, and 5 related synonyms; the YAML preserves all 6 synonym entries from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` retains 3 redirects into `NCBITaxon:479092`: `NCBITaxon:1527286`, `NCBITaxon:388560`, and `NCBITaxon:388561`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:36690` reports `organism_count` 1 for `NCBITaxon:479092`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 5 exact rows for `NCBITaxon:479092`: `CBS 10151`, `CBS:10151`, `NRRL Y-48253`, `NRRL:Y-48253`, and `NRRL:Y:48253`.
- BacDive has 0 exact local rows for `NCBITaxon:479092`.
- StrainInfo has 3 exact direct strain rows and 3 exact deposit matches for `NCBITaxon:479092`, covering siIDs 76658, 80519, and 273436.

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
