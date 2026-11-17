# YAML Record Review: Teunia tronadorensis

- Verdict: pass
- Target: `data/taxa/eukaryota/teunia_tronadorensis.yaml`
- Identifier: `NCBITaxon:3393985`

## Target

Reviewed the complete 89-line YAML record for Teunia tronadorensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for teunia_tronadorensis.

## Validation

- `just validate data/taxa/eukaryota/teunia_tronadorensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tetrapisispora_taiwanensis_nom_inval.yaml data/taxa/eukaryota/tetrapyrgos_nigripes.yaml data/taxa/eukaryota/teunia_tronadorensis.yaml data/taxa/eukaryota/teunomyces_aglyptinius.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:626111` is `NCBITaxon:3393985`, label `Teunia tronadorensis`, rank `SPECIES`, parent `NCBITaxon:2724800`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 2 exact synonyms, 0 broad synonyms, and 5 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:3393985` at line 63615.
- All 12 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps obsolete `NCBITaxon:743940` and `NCBITaxon:743942` to current `NCBITaxon:3393985`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:3393985` at line 32633 with `organism_count` 5, matching the YAML GOLD source assertion count of 5.
- Native GOLD source tables include 0 organism rows, 0 project rows, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has four exact `NCBITaxon:3393985` holotype rows at lines 184142-184145 for CRUB 1299 designation variants.
- The local BacDive exact table has no row for `NCBITaxon:3393985`.
- The local StrainInfo exact scan found 1 direct row carrying 1 exact deposit row for `NCBITaxon:3393985`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:3393985`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:3393985`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:3393985`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material evidence, StrainInfo exact matches, and zero generated-strain coverage internally consistent with the local generated evidence.
