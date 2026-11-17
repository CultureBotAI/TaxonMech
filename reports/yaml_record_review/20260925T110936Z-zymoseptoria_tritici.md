# YAML Record Review: Zymoseptoria tritici

- Verdict: pass
- Target: `data/taxa/eukaryota/zymoseptoria_tritici.yaml`
- Identifier: `NCBITaxon:1047171`

## Target

Reviewed the complete 100-line YAML record for Zymoseptoria tritici. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zymoseptoria_tritici.

## Validation

- `just validate data/taxa/eukaryota/zymoseptoria_tritici.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zymoseptoria_passerinii_sp63.yaml data/taxa/eukaryota/zymoseptoria_pseudotritici.yaml data/taxa/eukaryota/zymoseptoria_pseudotritici_stir04_3_11_1.yaml data/taxa/eukaryota/zymoseptoria_tritici.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:224867` is `NCBITaxon:1047171`, `Zymoseptoria tritici`, rank `SPECIES`, parent `NCBITaxon:1047167`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zymoseptoria tritici` entry, at `data/curated/seed_scope.tsv:57375`.
- NCBI synonym counts are 3 exact synonyms, 0 broad synonyms, and 4 related synonyms; the YAML preserves the exact and related synonyms from that row.
- All 16 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 1 redirect into `NCBITaxon:1047171`, from old ID `NCBITaxon:54734`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:791` reports `organism_count` 205 for `NCBITaxon:1047171`, matching the YAML GOLD assertion count of 205.
- Native GOLD evidence has 203 organism rows, 236 project rows, and 18 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 4 exact culture-from-epitype rows for `NCBITaxon:1047171`.
- BacDive has 0 exact local rows for `NCBITaxon:1047171`.
- StrainInfo has 137 exact direct strain rows and 146 exact deposit matches for `NCBITaxon:1047171`, all attached to direct StrainInfo rows.

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
