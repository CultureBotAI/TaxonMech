# YAML Record Review: Tetrapisispora namnaoensis

- Verdict: pass
- Target: `data/taxa/eukaryota/tetrapisispora_namnaoensis.yaml`
- Identifier: `NCBITaxon:279732`

## Target

Reviewed the complete 76-line YAML record for Tetrapisispora namnaoensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tetrapisispora_namnaoensis.

## Validation

- `just validate data/taxa/eukaryota/tetrapisispora_namnaoensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tetrapisispora_arboricola.yaml data/taxa/eukaryota/tetrapisispora_fleetii.yaml data/taxa/eukaryota/tetrapisispora_iriomotensis.yaml data/taxa/eukaryota/tetrapisispora_namnaoensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:56860` is `NCBITaxon:279732`, label `Tetrapisispora namnaoensis`, rank `SPECIES`, parent `NCBITaxon:113604`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 1 exact synonym, 0 broad synonyms, and 1 related synonym.
- The seed-scope table has exactly one row for `NCBITaxon:279732` at line 54952.
- All 13 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:279732`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:279732` at line 26730 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has ten exact `NCBITaxon:279732` culture-from-type-material rows at lines 123017-123026 for CBS 10093, JCM 12664, NRRL Y-27982, TISTR 5828, and TN101 designation variants.
- The local BacDive exact table has no row for `NCBITaxon:279732`.
- The local StrainInfo exact scan found 1 direct row carrying 4 exact deposit rows for `NCBITaxon:279732`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:279732`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:279732`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:279732`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material evidence, StrainInfo exact matches, and zero generated-strain coverage internally consistent with the local generated evidence.
