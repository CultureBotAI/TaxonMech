# YAML Record Review: Utharomyces epallocaulus

- Verdict: pass
- Target: `data/taxa/eukaryota/utharomyces_epallocaulus.yaml`
- Identifier: `NCBITaxon:101125`

## Target

Reviewed the complete 78-line YAML record for Utharomyces epallocaulus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for utharomyces_epallocaulus.

## Validation

- `just validate data/taxa/eukaryota/utharomyces_epallocaulus.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ustulina_deusta.yaml data/taxa/eukaryota/utharomyces_epallocaulus.yaml data/taxa/eukaryota/vairimorpha_apis_brl_01.yaml data/taxa/eukaryota/vairimorpha_ceranae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 17439 retains `NCBITaxon:101125` as `Utharomyces epallocaulus`, rank `SPECIES`, parent `NCBITaxon:101124`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:101125` at line 53645, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps 2 old identifiers into this target at lines 78196 and 83674, with no old identifiers retained as current NCBITaxon rows.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:101125` at line 256 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 4 type-material rows for the target at lines 879 through 882. BacDive contributed 0 exact rows; StrainInfo contributed 11 exact direct rows and 15 exact deposit rows for `NCBITaxon:101125`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support plus two retired NCBI identifiers resolved into the current target, so the YAML accurately reflects the evidence available for the target identifier.
