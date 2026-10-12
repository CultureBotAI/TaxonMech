# YAML Record Review: Zygoascus hellenicus

- Verdict: pass
- Target: `data/taxa/eukaryota/zygoascus_hellenicus.yaml`
- Identifier: `NCBITaxon:5621`

## Target

Reviewed the complete 78-line YAML record for Zygoascus hellenicus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zygoascus_hellenicus.

## Validation

- `just validate data/taxa/eukaryota/zygoascus_hellenicus.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zygoascus_bituminiphila.yaml data/taxa/eukaryota/zygoascus_flipseniorum.yaml data/taxa/eukaryota/zygoascus_hellenicus.yaml data/taxa/eukaryota/zygoascus_meyerae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:2498` is `NCBITaxon:5621`, `Zygoascus hellenicus`, rank `SPECIES`, parent `NCBITaxon:5620`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zygoascus hellenicus` entry, at `data/curated/seed_scope.tsv:52046`.
- NCBI synonym counts are 2 exact synonyms, 0 broad synonyms, and 1 related synonym; the YAML preserves the exact and related synonyms from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 4 redirects into `NCBITaxon:5621`, from old IDs `NCBITaxon:262089`, `NCBITaxon:262090`, `NCBITaxon:262093`, and `NCBITaxon:314313`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:38871` reports `organism_count` 1 for `NCBITaxon:5621`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 3 project rows, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 22 exact rows for `NCBITaxon:5621`: 7 culture-from-type-material rows and 15 type-material rows.
- BacDive has 0 exact local rows for `NCBITaxon:5621`.
- StrainInfo has 24 exact direct strain rows and 73 exact deposit matches for `NCBITaxon:5621`, all attached to direct StrainInfo rows.

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
