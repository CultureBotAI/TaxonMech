# YAML Record Review: Polytolypa hystricis UAMH7299

- Verdict: pass
- Target: `data/taxa/eukaryota/polytolypa_hystricis_uamh7299.yaml`
- Identifier: `NCBITaxon:1447883`

## Target

Reviewed the complete 81-line YAML record for `Polytolypa hystricis UAMH7299`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `polytolypa_hystricis_uamh7299`.

## Validation

- `just validate data/taxa/eukaryota/polytolypa_hystricis_uamh7299.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/polyplosphaeria_fusca.yaml data/taxa/eukaryota/polyporus_arcularius.yaml data/taxa/eukaryota/polysphondylium_violaceum.yaml data/taxa/eukaryota/polytolypa_hystricis_uamh7299.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:364877` is the exact retained NCBITaxon row for `NCBITaxon:1447883`: label `Polytolypa hystricis UAMH7299`, rank `STRAIN`, parent `NCBITaxon:221428`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:60158` contains the seeded in-scope row for `NCBITaxon:1447883` with the reason `attested rule: Polytolypa hystricis UAMH7299, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:10883` is the aggregate GOLD row for `NCBITaxon:1447883` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:1447883`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1447883`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1447883`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

This is a retained strain-level NCBITaxon record, and the YAML lineage correctly includes `Polytolypa hystricis` as the immediate species-level ancestor. No exact BacDive, StrainInfo, or type-material evidence needed to be materialized into the zero-strain YAML.
