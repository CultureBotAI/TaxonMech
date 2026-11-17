# YAML Record Review: Tetrapisispora iriomotensis

- Verdict: pass
- Target: `data/taxa/eukaryota/tetrapisispora_iriomotensis.yaml`
- Identifier: `NCBITaxon:113606`

## Target

Reviewed the complete 75-line YAML record for Tetrapisispora iriomotensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tetrapisispora_iriomotensis.

## Validation

- `just validate data/taxa/eukaryota/tetrapisispora_iriomotensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tetrapisispora_arboricola.yaml data/taxa/eukaryota/tetrapisispora_fleetii.yaml data/taxa/eukaryota/tetrapisispora_iriomotensis.yaml data/taxa/eukaryota/tetrapisispora_namnaoensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:20666` is `NCBITaxon:113606`, label `Tetrapisispora iriomotensis`, rank `SPECIES`, parent `NCBITaxon:113604`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 0 exact synonyms, 0 broad synonyms, and 2 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:113606` at line 53793.
- All 13 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps obsolete `NCBITaxon:80766` to current `NCBITaxon:113606`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:113606` at line 2786 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has eight exact `NCBITaxon:113606` culture-from-type-material rows at lines 8908-8915 for CBS 8762, IFO 10929, JCM 10810, and NRRL Y-27309 designation variants.
- The local BacDive exact table has no row for `NCBITaxon:113606`.
- The local StrainInfo exact scan found 1 direct row carrying 8 exact deposit rows for `NCBITaxon:113606`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:113606`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:113606`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:113606`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material evidence, StrainInfo exact matches, and zero generated-strain coverage internally consistent with the local generated evidence.
