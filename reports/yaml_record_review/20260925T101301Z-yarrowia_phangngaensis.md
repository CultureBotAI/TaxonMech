# YAML Record Review: Yarrowia phangngaensis

- Verdict: pass
- Target: `data/taxa/eukaryota/yarrowia_phangngaensis.yaml`
- Identifier: `NCBITaxon:444778`

## Target

Reviewed the complete 85-line YAML record for Yarrowia phangngaensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yarrowia_phangngaensis.

## Validation

- `just validate data/taxa/eukaryota/yarrowia_phangngaensis.yaml` ran LinkML validation and printed `No issues found`.
- `just validate-strict data/taxa/eukaryota/yarrowia_lipolytica.yaml data/taxa/eukaryota/yarrowia_osloensis.yaml data/taxa/eukaryota/yarrowia_phangngaensis.yaml data/taxa/eukaryota/yarrowia_porcina.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:98954` is `NCBITaxon:444778`, `Yarrowia phangngaensis`, rank `SPECIES`, parent `NCBITaxon:4951`, genetic code `1`, taxonomy snapshot `2026-09-13`.
- The seed-scope table has exactly one `Yarrowia phangngaensis` entry, at `data/curated/seed_scope.tsv:55672`.
- NCBI synonym counts are 1 exact synonym, 0 broad synonyms, and 4 related synonyms; the YAML preserves all 5 synonym entries from that row.
- All 13 lineage entries were checked against the retained NCBI rows with no missing IDs and no label, rank, or parent mismatches.
- `data/raw/ncbi_merged_ids.tsv` retains 2 redirects into `NCBITaxon:444778`: `NCBITaxon:1527288` and `NCBITaxon:444777`.

## Evidence

- The generated GOLD aggregate row at `data/generated/gold_organism_counts.tsv:35694` reports `organism_count` 1 for `NCBITaxon:444778`, matching the YAML GOLD assertion count of 1.
- Native GOLD evidence has 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has 14 exact rows for `NCBITaxon:444778`: four `culture from holotype` variants for `CBS 10407`, four for `NBRC 101970`, four for `NRRL Y-63743`, and two `holotype` variants for `PT1-17`.
- BacDive has 0 exact local rows for `NCBITaxon:444778`.
- StrainInfo has 0 exact direct strain rows and 0 exact deposit matches for `NCBITaxon:444778`.

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
