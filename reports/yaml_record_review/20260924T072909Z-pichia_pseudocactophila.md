# YAML Record Review: Pichia pseudocactophila

- Verdict: pass
- Target: `data/taxa/eukaryota/pichia_pseudocactophila.yaml`
- Identifier: `NCBITaxon:53658`

## Target

Reviewed the complete 72-line YAML record for `Pichia pseudocactophila`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pichia_pseudocactophila`.

## Validation

- `just validate data/taxa/eukaryota/pichia_pseudocactophila.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pichia_paraexigua.yaml data/taxa/eukaryota/pichia_phayaonensis.yaml data/taxa/eukaryota/pichia_pseudocactophila.yaml data/taxa/eukaryota/pichia_pseudolambica.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:6794` is the exact retained NCBITaxon row for `NCBITaxon:53658`: label `Pichia pseudocactophila`, rank `SPECIES`, parent `NCBITaxon:4919`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52890` contains the seeded in-scope row for `NCBITaxon:53658` with the reason `attested rule: Pichia pseudocactophila, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:53658`.

## Evidence

- `data/raw/gold_organisms.tsv:38213` is the aggregate GOLD row for `NCBITaxon:53658` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:525720`, one linked project row at `data/gold/projects.jsonl.gz:609864`, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:230699` through `data/raw/ncbi_type_material.tsv:230717` contain the 19 exact NCBI type-material rows for `NCBITaxon:53658`.
- StrainInfo has 6 direct exact JSONL rows and 16 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:53658`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:53658`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
