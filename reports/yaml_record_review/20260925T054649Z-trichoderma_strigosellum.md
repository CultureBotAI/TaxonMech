# YAML Record Review: Trichoderma strigosellum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_strigosellum.yaml`
- Identifier: `NCBITaxon:1202974`

## Target

Reviewed the complete 106-line YAML record for Trichoderma strigosellum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_strigosellum.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_strigosellum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_stercorarium.yaml data/taxa/eukaryota/trichoderma_stilbohypoxyli.yaml data/taxa/eukaryota/trichoderma_strictipile.yaml data/taxa/eukaryota/trichoderma_strigosellum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 272099 retains `NCBITaxon:1202974` as `Trichoderma strigosellum`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1202974` at line 58333, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 9 related synonyms, matching the nine related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps six historical identifiers, `NCBITaxon:1265519`, `NCBITaxon:1265520`, `NCBITaxon:1265521`, `NCBITaxon:1265522`, `NCBITaxon:1265523`, and `NCBITaxon:1265524`, into this target; an exact ignored-file-inclusive scan found no retained current rows for those old identifiers in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1202974` at line 4861 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found nine type-material rows for the target: `CBS 102817`, `CBS:102817`, `C.P.K. 3604`, `CPK 3604`, `CPK:3604`, `HUA 179963`, `HUA:179963`, `CBS H-21054`, and `CBS:H:21054`. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:1202974`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material support and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
