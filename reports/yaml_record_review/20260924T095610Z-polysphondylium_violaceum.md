# YAML Record Review: Polysphondylium violaceum

- Verdict: pass
- Target: `data/taxa/eukaryota/polysphondylium_violaceum.yaml`
- Identifier: `NCBITaxon:133409`

## Target

Reviewed the complete 63-line YAML record for `Polysphondylium violaceum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `polysphondylium_violaceum`.

## Validation

- `just validate data/taxa/eukaryota/polysphondylium_violaceum.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/polyplosphaeria_fusca.yaml data/taxa/eukaryota/polyporus_arcularius.yaml data/taxa/eukaryota/polysphondylium_violaceum.yaml data/taxa/eukaryota/polytolypa_hystricis_uamh7299.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:25938` is the exact retained NCBITaxon row for `NCBITaxon:133409`: label `Polysphondylium violaceum`, rank `SPECIES`, parent `NCBITaxon:13641`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53953` contains the seeded in-scope row for `NCBITaxon:133409` with the reason `attested rule: Polysphondylium violaceum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 10 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:8113` is the aggregate GOLD row for `NCBITaxon:133409` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:133409`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 13 direct local JSONL records covering 19 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:133409`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:133409`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows. The generated GOLD source attestation is consistent with both the aggregate GOLD row and the native GOLD row for `Polysphondylium violaceum P6`.
