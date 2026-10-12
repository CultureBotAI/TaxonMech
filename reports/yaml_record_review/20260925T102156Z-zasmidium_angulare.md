# YAML Record Review: Zasmidium angulare

- Verdict: pass
- Target: `data/taxa/eukaryota/zasmidium_angulare.yaml`
- Identifier: `NCBITaxon:1194242`

## Target

Reviewed the complete 81-line YAML record for Zasmidium angulare. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zasmidium_angulare.

## Validation

- `just validate data/taxa/eukaryota/zasmidium_angulare.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zalerion_sp.yaml data/taxa/eukaryota/zancudomyces_culisetae.yaml data/taxa/eukaryota/zarea_fungicola.yaml data/taxa/eukaryota/zasmidium_angulare.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:268606` is `NCBITaxon:1194242`, `Zasmidium angulare`, rank `SPECIES`, parent `NCBITaxon:395590`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zasmidium angulare` entry, at `data/curated/seed_scope.tsv:58261`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML preserves the related synonym from that row.
- All 16 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:1194242`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:4617` reports `organism_count` 1 for `NCBITaxon:1194242`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 6 exact `culture from holotype` rows for `NCBITaxon:1194242`, covering `CBS 132094`, `CPC 19042`, and `GA2 27B1a` designation variants.
- BacDive has 0 exact local rows for `NCBITaxon:1194242`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:1194242`.

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
