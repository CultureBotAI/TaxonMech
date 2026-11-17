# YAML Record Review: Xerocomellus chrysenteron

- Verdict: pass
- Target: `data/taxa/eukaryota/xerocomellus_chrysenteron.yaml`
- Identifier: `NCBITaxon:1354920`

## Target

Reviewed the complete 120-line YAML record for Xerocomellus chrysenteron. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for xerocomellus_chrysenteron.

## Validation

- `just validate data/taxa/eukaryota/xerocomellus_chrysenteron.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/xanthoria_parietina_46_1_sa22.yaml data/taxa/eukaryota/xerocomellus_chrysenteron.yaml data/taxa/eukaryota/xerocomellus_pruinatus.yaml data/taxa/eukaryota/xerocomus_subtomentosus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 327343 retains `NCBITaxon:1354920` as `Xerocomellus chrysenteron`, rank `SPECIES`, parent `NCBITaxon:1348651`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1354920` at line 59637, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 7 exact, 0 broad, and 8 related synonyms, matching the YAML synonym entries. All 15 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps four old identifiers, `NCBITaxon:279507`, `NCBITaxon:455634`, `NCBITaxon:5386`, and `NCBITaxon:545495`, into this retained target, and the YAML keeps only `NCBITaxon:1354920`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1354920` at line 8622 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 1 exact direct row and 1 exact deposit row for `NCBITaxon:1354920`, with all target deposits carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a retained NCBITaxon and GOLD seed with exact StrainInfo support, and the four old NCBI identifiers correctly remain out of the YAML identifier set.
