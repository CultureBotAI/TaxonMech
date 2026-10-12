# YAML Record Review: Trichoderma aureoviride

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_aureoviride.yaml`
- Identifier: `NCBITaxon:64502`

## Target
Reviewed the complete 93-line YAML record for Trichoderma aureoviride. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trichoderma_aureoviride`.

## Validation
- `just validate data/taxa/eukaryota/trichoderma_aureoviride.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_atrobrunneum.yaml data/taxa/eukaryota/trichoderma_atroviride.yaml data/taxa/eukaryota/trichoderma_attinorum.yaml data/taxa/eukaryota/trichoderma_aureoviride.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 8171 retained `NCBITaxon:64502` as `Trichoderma aureoviride` at rank `SPECIES`, with parent `NCBITaxon:5543`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:64502` on line 53082.
- The NCBI synonym columns supplied 2 exact synonyms, 0 broad synonyms, and 3 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:65469` occurred only as an old identifier merged into `NCBITaxon:64502` in `data/raw/ncbi_merged_ids.tsv`, and it was not retained as a live YAML identifier.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:64502` on line 40310, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 0 analysis rows, 0 organism rows, and 0 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 6 exact rows for `NCBITaxon:64502` across `CBS 120536`, `K(M) 162235`, `SHD-M 2663`, and `K(M) 161792` spellings.
- BacDive found 0 exact rows. StrainInfo found 39 direct strain rows and 56 deposit rows under `NCBITaxon:64502`; 39 of 42 compressed JSONL rows were assigned directly to the target, and the remaining exact deposits occurred on SI 90906, SI 147101, and SI 156105 under non-target taxa.

## Completeness
- Generated strain tables had 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables had 0 target rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlays had 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
No YAML edits were made; this report records the read-only evidence review.
