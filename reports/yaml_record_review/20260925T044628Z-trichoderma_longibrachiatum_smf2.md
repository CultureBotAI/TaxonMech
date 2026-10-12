# YAML Record Review: Trichoderma longibrachiatum SMF2

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_longibrachiatum_smf2.yaml`
- Identifier: `NCBITaxon:1234776`

## Target

Reviewed the complete 80-line YAML record for Trichoderma longibrachiatum SMF2. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_longibrachiatum_smf2.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_longibrachiatum_smf2.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_lentiforme.yaml data/taxa/eukaryota/trichoderma_lieckfeldtiae.yaml data/taxa/eukaryota/trichoderma_longibrachiatum.yaml data/taxa/eukaryota/trichoderma_longibrachiatum_smf2.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 282511 retains `NCBITaxon:1234776` as `Trichoderma longibrachiatum SMF2`, rank `STRAIN`, parent `NCBITaxon:5548`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1234776` at line 58611, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 0 related synonyms, matching the absence of a YAML synonyms block. All 17 YAML lineage entries, including the parent species `NCBITaxon:5548`, were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table reported no retired identifiers mapping to this taxon, and no retained old identifiers were present in the active NCBI row.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1234776` at line 5615 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. NCBI type material was absent for this strain-level row, as expected. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:1234776`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a direct strain-level GOLD and NCBITaxon seed under `NCBITaxon:5548`; its parent species evidence is intentionally reviewed on `trichoderma_longibrachiatum.yaml`, so the SMF2 YAML accurately reflects only direct evidence available for the strain identifier.
