# YAML Record Review: Yurkovia mendeliana

- Verdict: pass
- Target: `data/taxa/eukaryota/yurkovia_mendeliana.yaml`
- Identifier: `NCBITaxon:1882489`

## Target

Reviewed the complete 72-line YAML record for Yurkovia mendeliana. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yurkovia_mendeliana.

## Validation

- `just validate data/taxa/eukaryota/yurkovia_mendeliana.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/yarrowia_yakushimensis.yaml data/taxa/eukaryota/yueomyces_sinensis.yaml data/taxa/eukaryota/yunzhangia_sonckii.yaml data/taxa/eukaryota/yurkovia_mendeliana.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:490199` is `NCBITaxon:1882489`, `Yurkovia mendeliana`, rank `SPECIES`, parent `NCBITaxon:1927869`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Yurkovia mendeliana` entry, at `data/curated/seed_scope.tsv:61428`.
- NCBI synonym counts are 0 exact synonyms, 0 broad synonyms, and 2 related synonyms; the YAML preserves all 2 synonym entries from that row.
- All 12 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` has 0 redirects into `NCBITaxon:1882489`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:16912` reports `organism_count` 3 for `NCBITaxon:1882489`, matching the YAML GOLD assertion count of 3.
- Native GOLD evidence has 3 organism rows, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 8 exact rows for `NCBITaxon:1882489`: six `culture from holotype` variants for `CBS 14273`, `DSM 101889`, and `KT152`, plus two `holotype` variants for `PYCC 6884`.
- BacDive has 0 exact local rows for `NCBITaxon:1882489`.
- StrainInfo has 1 exact direct strain row and 1 exact deposit match for `NCBITaxon:1882489`, both at siID 401449.

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
