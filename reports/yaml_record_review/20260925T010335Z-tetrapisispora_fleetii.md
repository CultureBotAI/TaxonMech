# YAML Record Review: Tetrapisispora fleetii

- Verdict: pass
- Target: `data/taxa/eukaryota/tetrapisispora_fleetii.yaml`
- Identifier: `NCBITaxon:300277`

## Target

Reviewed the complete 72-line YAML record for Tetrapisispora fleetii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tetrapisispora_fleetii.

## Validation

- `just validate data/taxa/eukaryota/tetrapisispora_fleetii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tetrapisispora_arboricola.yaml data/taxa/eukaryota/tetrapisispora_fleetii.yaml data/taxa/eukaryota/tetrapisispora_iriomotensis.yaml data/taxa/eukaryota/tetrapisispora_namnaoensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:61162` is `NCBITaxon:300277`, label `Tetrapisispora fleetii`, rank `SPECIES`, parent `NCBITaxon:113604`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 0 exact synonyms, 0 broad synonyms, and 1 related synonym.
- The seed-scope table has exactly one row for `NCBITaxon:300277` at line 55069.
- All 13 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:300277`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:300277` at line 30101 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has four exact `NCBITaxon:300277` culture-from-holotype rows at lines 154640-154643 for CBS 8957 and NRRL Y-27350 designation variants.
- The local BacDive exact table has no row for `NCBITaxon:300277`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:300277`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:300277`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:300277`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:300277`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material evidence, and zero-strain coverage internally consistent with the local generated evidence.
