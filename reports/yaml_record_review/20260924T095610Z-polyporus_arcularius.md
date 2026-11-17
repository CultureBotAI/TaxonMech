# YAML Record Review: Polyporus arcularius

- Verdict: pass
- Target: `data/taxa/eukaryota/polyporus_arcularius.yaml`
- Identifier: `NCBITaxon:5639`

## Target

Reviewed the complete 96-line YAML record for `Polyporus arcularius`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `polyporus_arcularius`.

## Validation

- `just validate data/taxa/eukaryota/polyporus_arcularius.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/polyplosphaeria_fusca.yaml data/taxa/eukaryota/polyporus_arcularius.yaml data/taxa/eukaryota/polysphondylium_violaceum.yaml data/taxa/eukaryota/polytolypa_hystricis_uamh7299.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2509` is the exact retained NCBITaxon row for `NCBITaxon:5639`: label `Polyporus arcularius`, rank `SPECIES`, parent `NCBITaxon:5637`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52051` contains the seeded in-scope row for `NCBITaxon:5639` with the reason `attested rule: Polyporus arcularius, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 6 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:1969916` to `NCBITaxon:5639`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:38906` is the aggregate GOLD row for `NCBITaxon:5639` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:5639`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 36 direct local JSONL records covering 45 exact deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5639`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5639`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows. The generated GOLD source attestation is consistent with both the aggregate GOLD row and the native GOLD row for `Polyporus arcularius HHB13444 ss-1`.
