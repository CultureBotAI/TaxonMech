# YAML Record Review: Podila verticillata

- Verdict: pass
- Target: `data/taxa/eukaryota/podila_verticillata.yaml`
- Identifier: `NCBITaxon:78898`

## Target

Reviewed the complete 87-line YAML record for `Podila verticillata`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `podila_verticillata`.

## Validation

- `just validate data/taxa/eukaryota/podila_verticillata.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/podila_verticillata.yaml data/taxa/eukaryota/podosira_stelligera.yaml data/taxa/eukaryota/podosordaria_jugoyasan.yaml data/taxa/eukaryota/podosphaera_macularis.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:11540` is the exact retained NCBITaxon row for `NCBITaxon:78898`: label `Podila verticillata`, rank `SPECIES`, parent `NCBITaxon:2779937`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53330` contains the seeded in-scope row for `NCBITaxon:78898` with the reason `attested rule: Podila verticillata, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 3 exact synonyms, 4 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory maps old IDs `NCBITaxon:979651` and `NCBITaxon:979652` to `NCBITaxon:78898`, and exact retained NCBITaxon scans found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:42757` is the aggregate GOLD row for `NCBITaxon:78898` and reports `organism_count=5`, matching the YAML GOLD source attestation.
- Native GOLD has four exact organism rows, four linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has eight exact type-material rows for `NCBITaxon:78898`, filed under `Haplosporangium attenuatissimum` and `Haplosporangium fasciculatum`.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 25 exact local JSONL records covering 34 deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:78898`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:78898`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material rows are NCBI designations that do not appear as generated strain rows, and the exact StrainInfo JSONL hits likewise have no corresponding BacDive or generated StrainInfo overlay rows. The generated GOLD source attestation uses the aggregate GOLD row rather than the smaller local native GOLD organism row count.
