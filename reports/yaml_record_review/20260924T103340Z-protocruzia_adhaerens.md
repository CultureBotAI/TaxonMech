# YAML Record Review: Protocruzia adhaerens

- Verdict: pass
- Target: `data/taxa/eukaryota/protocruzia_adhaerens.yaml`
- Identifier: `NCBITaxon:223996`

## Target

Reviewed the complete 75-line YAML record for `Protocruzia adhaerens`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `protocruzia_adhaerens`.

## Validation

- `just validate data/taxa/eukaryota/protocruzia_adhaerens.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/protocruzia_adhaerens.yaml data/taxa/eukaryota/protomyces_lactucae_debilis.yaml data/taxa/eukaryota/protomycocladus_faisalabadensis.yaml data/taxa/eukaryota/protostelium_mycophagum.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:43948` is the exact retained NCBITaxon row for `NCBITaxon:223996`: label `Protocruzia adhaerens`, rank `SPECIES`, parent `NCBITaxon:49977`, genetic code `6`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54612` contains the seeded in-scope row for `NCBITaxon:223996` with the reason `attested rule: Protocruzia adhaerens, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 2 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- All 10 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory returned no old IDs for this retained target.

## Evidence

- `data/raw/gold_organisms.tsv:21159` is the aggregate GOLD row for `NCBITaxon:223996` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, no linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:223996`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:223996`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:223996`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The native GOLD organism row uses the retained exact NCBI taxon ID with the synonym spelling `Protocruzia adherens`. No exact BacDive, StrainInfo, or type-material evidence needed to be materialized into the zero-strain YAML.
