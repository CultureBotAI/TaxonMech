# YAML Record Review: Zancudomyces culisetae

- Verdict: pass
- Target: `data/taxa/eukaryota/zancudomyces_culisetae.yaml`
- Identifier: `NCBITaxon:1213189`

## Target

Reviewed the complete 76-line YAML record for Zancudomyces culisetae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for zancudomyces_culisetae.

## Validation

- `just validate data/taxa/eukaryota/zancudomyces_culisetae.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/zalerion_sp.yaml data/taxa/eukaryota/zancudomyces_culisetae.yaml data/taxa/eukaryota/zarea_fungicola.yaml data/taxa/eukaryota/zasmidium_angulare.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:274432` is `NCBITaxon:1213189`, `Zancudomyces culisetae`, rank `SPECIES`, parent `NCBITaxon:1213188`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Zancudomyces culisetae` entry, at `data/curated/seed_scope.tsv:58422`.
- NCBI synonym counts are 1 exact synonym, 0 broad synonyms, and 2 related synonyms; the YAML preserves all 3 synonym entries from that row.
- All 12 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` retains 1 redirect into `NCBITaxon:1213189`: `NCBITaxon:4889`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:5074` reports `organism_count` 1 for `NCBITaxon:1213189`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 9 exact `type material` rows for `NCBITaxon:1213189`, covering `AFTOL-ID 29`, `ARSEF 9012`, `ATCC 16244`, and `COL-18-3` designation variants.
- BacDive has 0 exact local rows for `NCBITaxon:1213189`.
- StrainInfo has 4 exact direct strain rows and 5 exact deposit matches for `NCBITaxon:1213189`, covering siIDs 251878, 254124, 254125, and 256868.

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
