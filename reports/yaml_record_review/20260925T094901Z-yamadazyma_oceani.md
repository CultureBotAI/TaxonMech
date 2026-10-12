# YAML Record Review: Yamadazyma oceani

- Verdict: pass
- Target: `data/taxa/eukaryota/yamadazyma_oceani.yaml`
- Identifier: `NCBITaxon:1186037`

## Target

Reviewed the complete 88-line YAML record for Yamadazyma oceani. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yamadazyma_oceani.

## Validation

- `just validate data/taxa/eukaryota/yamadazyma_oceani.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/yamadazyma_laniorum.yaml data/taxa/eukaryota/yamadazyma_mexicana.yaml data/taxa/eukaryota/yamadazyma_nakazawae.yaml data/taxa/eukaryota/yamadazyma_oceani.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 265360 retains `NCBITaxon:1186037` as `Yamadazyma oceani`, rank `SPECIES`, parent `NCBITaxon:766765`, genetic code `12`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1186037` at line 58240, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 5 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps old `NCBITaxon:310034`, `NCBITaxon:526732`, and `NCBITaxon:866852` to this target at lines 63432, 84679, and 97091; an ignored-file-inclusive exact scan found no retained current NCBITaxon rows for those old identifiers.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1186037` at line 4163 with `organism_count` 3, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 2 organism rows, and 1 project for this identifier. `data/raw/ncbi_type_material.tsv` contained 6 rows, covering 2 culture-from-holotype aliases for `DSM 23777` plus 4 holotype aliases for `CBS 11857`. BacDive contributed 0 exact rows, and StrainInfo contributed 1 exact direct row and 1 exact deposit row for `NCBITaxon:1186037`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with no generated raw strain-table rows pending YAML incorporation.
