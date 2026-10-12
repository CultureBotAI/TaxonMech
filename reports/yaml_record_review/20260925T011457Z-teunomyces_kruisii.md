# YAML Record Review: Teunomyces kruisii

- Verdict: pass
- Target: `data/taxa/eukaryota/teunomyces_kruisii.yaml`
- Identifier: `NCBITaxon:45561`

## Target

Reviewed the complete 88-line YAML record for Teunomyces kruisii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for teunomyces_kruisii.

## Validation

- `just validate data/taxa/eukaryota/teunomyces_kruisii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/teunomyces_gatunensis.yaml data/taxa/eukaryota/teunomyces_kruisii.yaml data/taxa/eukaryota/teunomyces_lycoperdinae.yaml data/taxa/eukaryota/teunomyces_pallodes.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:5613` is `NCBITaxon:45561`, label `Teunomyces kruisii`, rank `SPECIES`, parent `NCBITaxon:1539665`, genetic code `12`, taxonomy snapshot `2026-09-13`, with 2 exact synonyms, 0 broad synonyms, and 4 related synonyms.
- The seed-scope table has exactly one row for `NCBITaxon:45561` at line 52659.
- All 13 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- The NCBI merged-ID table maps obsolete `NCBITaxon:348311` and `NCBITaxon:348315` to current `NCBITaxon:45561`; the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:45561` at line 36068 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 1 analysis row for this taxon.
- `data/raw/ncbi_type_material.tsv` has 16 exact `NCBITaxon:45561` Torulopsis kruisii type-material rows at lines 215330-215345 for ATCC 24408, BCRC/CCRC 21573, CBS 6451, CCY 29-19-7, IFO 10256, JCM 1779, and NRRL Y-17087 designation variants.
- The local BacDive exact table has no row for `NCBITaxon:45561`.
- The local StrainInfo exact scan found 12 direct rows and 32 exact deposit rows for `NCBITaxon:45561`; the parsed JSONL follow-up found five non-direct `Pichia kudriavzevii` strain rows carrying one exact `NCBITaxon:45561` deposit each.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:45561`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:45561`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:45561`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, type-material evidence, StrainInfo exact matches, and zero generated-strain coverage internally consistent with the local generated evidence.
