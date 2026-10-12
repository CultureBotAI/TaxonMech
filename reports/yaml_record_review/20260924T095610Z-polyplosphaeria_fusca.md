# YAML Record Review: Polyplosphaeria fusca

- Verdict: pass
- Target: `data/taxa/eukaryota/polyplosphaeria_fusca.yaml`
- Identifier: `NCBITaxon:682080`

## Target

Reviewed the complete 96-line YAML record for `Polyplosphaeria fusca`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `polyplosphaeria_fusca`.

## Validation

- `just validate data/taxa/eukaryota/polyplosphaeria_fusca.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/polyplosphaeria_fusca.yaml data/taxa/eukaryota/polyporus_arcularius.yaml data/taxa/eukaryota/polysphondylium_violaceum.yaml data/taxa/eukaryota/polytolypa_hystricis_uamh7299.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:159993` is the exact retained NCBITaxon row for `NCBITaxon:682080`: label `Polyplosphaeria fusca`, rank `SPECIES`, parent `NCBITaxon:714959`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56379` contains the seeded in-scope row for `NCBITaxon:682080` with the reason `attested rule: Polyplosphaeria fusca, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 6 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old IDs `NCBITaxon:682081`, `NCBITaxon:682082`, `NCBITaxon:682083`, and `NCBITaxon:682084` to `NCBITaxon:682080`, and exact retained NCBITaxon scans found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:41194` is the aggregate GOLD row for `NCBITaxon:682080` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and one linked analysis row for this target.
- `data/raw/ncbi_type_material.tsv` has eight exact type-material rows for `NCBITaxon:682080`, filed under `Polyplosphaeria fusca`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:682080`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:682080`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material rows cover two `JCM 13175` culture-from-holotype designations, two `HHUF 29399` holotype designations, and four `KTC 1616` or `MAFF 239685` type-material designations. The generated GOLD source attestation uses the aggregate GOLD row rather than the smaller native GOLD organism row count.
