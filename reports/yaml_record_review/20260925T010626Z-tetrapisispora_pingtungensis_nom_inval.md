# YAML Record Review: Tetrapisispora pingtungensis (nom. inval.)

- Verdict: pass
- Target: `data/taxa/eukaryota/tetrapisispora_pingtungensis_nom_inval.yaml`
- Identifier: `NCBITaxon:1321244`

## Target

Reviewed the complete 75-line YAML record for Tetrapisispora pingtungensis (nom. inval.). The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tetrapisispora_pingtungensis_nom_inval.

## Validation

- `just validate data/taxa/eukaryota/tetrapisispora_pingtungensis_nom_inval.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tetrapisispora_nanseiensis.yaml data/taxa/eukaryota/tetrapisispora_phaffii.yaml data/taxa/eukaryota/tetrapisispora_phaffii_cbs_4417.yaml data/taxa/eukaryota/tetrapisispora_pingtungensis_nom_inval.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The retained NCBI taxonomy row at `data/raw/ncbitaxon_taxa.tsv:314803` is `NCBITaxon:1321244`, label `Tetrapisispora pingtungensis (nom. inval.)`, rank `SPECIES`, parent `NCBITaxon:2633500`, genetic code `1`, taxonomy snapshot `2026-09-13`, with 0 exact synonyms, 0 broad synonyms, and 1 related synonym.
- The seed-scope table has exactly one row for `NCBITaxon:1321244` at line 59453.
- All 14 lineage links in the YAML were present in the retained NCBI taxonomy table with no missing IDs and no parent or label mismatches.
- No NCBI merged-ID row targeted `NCBITaxon:1321244`, and the YAML retained no obsolete IDs.

## Evidence

- The GOLD aggregate table has exactly one row for `NCBITaxon:1321244` at line 7808 with `organism_count` 1, matching the YAML GOLD source assertion count of 1.
- Native GOLD source tables include 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- `data/raw/ncbi_type_material.tsv` has no exact `NCBITaxon:1321244` rows.
- The local BacDive exact table has no row for `NCBITaxon:1321244`.
- The local StrainInfo exact scan found 0 direct rows and 0 deposit rows for `NCBITaxon:1321244`.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all have 0 rows for `NCBITaxon:1321244`, matching `strain_count: 0`.
- Auxiliary local source tables for BacTobase/BactoTraits, GTDB mappings, GTDB species, LPSN, Madin traits, and MediaDive all have 0 exact rows for `NCBITaxon:1321244`.
- Generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all have 0 rows for `NCBITaxon:1321244`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The bounded review found the record's NCBI identity, NCBI lineage, GOLD assertion count, and zero-strain coverage internally consistent with the local generated evidence.
