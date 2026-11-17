# YAML Record Review: Podosphaera macularis

- Verdict: pass
- Target: `data/taxa/eukaryota/podosphaera_macularis.yaml`
- Identifier: `NCBITaxon:683375`

## Target

Reviewed the complete 96-line YAML record for `Podosphaera macularis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podosphaera_macularis`.

## Validation

- `just validate data/taxa/eukaryota/podosphaera_macularis.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podila_verticillata.yaml data/taxa/eukaryota/podosira_stelligera.yaml data/taxa/eukaryota/podosordaria_jugoyasan.yaml data/taxa/eukaryota/podosphaera_macularis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:160581` is the exact retained NCBITaxon row for `NCBITaxon:683375`: label `Podosphaera macularis`, rank `SPECIES`, parent `NCBITaxon:62701`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56384` contains the seeded in-scope row for `NCBITaxon:683375` with the reason `attested rule: Podosphaera macularis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 3 exact synonyms, 4 related synonyms, and 0 broad synonyms.
- All 15 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old ID `NCBITaxon:180121` to `NCBITaxon:683375`, and exact retained NCBITaxon scans found no retained row for the old ID.

## Evidence

- `data/raw/gold_organisms.tsv:41292` is the aggregate GOLD row for `NCBITaxon:683375` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, one linked project row, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:683375`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:683375`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:683375`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The generated GOLD source attestation is consistent with both the aggregate GOLD row and the native GOLD row for `Podosphaera macularis HPM-609`. No exact BacDive, StrainInfo, or type-material evidence needed to be materialized into the zero-strain YAML.
