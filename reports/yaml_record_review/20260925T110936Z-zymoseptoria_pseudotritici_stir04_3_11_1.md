# YAML Record Review: Zymoseptoria pseudotritici STIR04_3.11.1

- Verdict: pass
- Target: `data/taxa/eukaryota/zymoseptoria_pseudotritici_stir04_3_11_1.yaml`
- Identifier: `NCBITaxon:744267`

## Target

Reviewed the complete 87-line YAML record for Zymoseptoria pseudotritici STIR04_3.11.1. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zymoseptoria_pseudotritici_stir04_3_11_1.

## Validation

- `just validate data/taxa/eukaryota/zymoseptoria_pseudotritici_stir04_3_11_1.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zymoseptoria_passerinii_sp63.yaml data/taxa/eukaryota/zymoseptoria_pseudotritici.yaml data/taxa/eukaryota/zymoseptoria_pseudotritici_stir04_3_11_1.yaml data/taxa/eukaryota/zymoseptoria_tritici.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:171500` is `NCBITaxon:744267`, `Zymoseptoria pseudotritici STIR04_3.11.1`, rank `STRAIN`, parent `NCBITaxon:1173715`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zymoseptoria pseudotritici STIR04_3.11.1` entry, at `data/curated/seed_scope.tsv:56590`.
- NCBI synonym counts are 2 exact synonyms, 0 broad synonyms, and 0 related synonyms; the YAML preserves the exact synonyms from that row.
- All 17 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:744267`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:42171` reports `organism_count` 1 for `NCBITaxon:744267`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 2 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 0 exact rows for `NCBITaxon:744267`.
- BacDive has 0 exact local rows for `NCBITaxon:744267`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:744267`.

## Completeness

- Generated raw strain tables all have 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables all have 0 rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlay tables all have 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
