# YAML Record Review: Pichia terricola

- Verdict: pass
- Target: `data/taxa/eukaryota/pichia_terricola.yaml`
- Identifier: `NCBITaxon:54551`

## Target

Reviewed the complete 75-line YAML record for `Pichia terricola`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pichia_terricola`.

## Validation

- `just validate data/taxa/eukaryota/pichia_terricola.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pichia_sp_pb3310.yaml data/taxa/eukaryota/pichia_sporocuriosa.yaml data/taxa/eukaryota/pichia_terricola.yaml data/taxa/eukaryota/pichia_thaimueangensis.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:6937` is the exact retained NCBITaxon row for `NCBITaxon:54551`: label `Pichia terricola`, rank `SPECIES`, parent `NCBITaxon:4919`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52931` contains the seeded in-scope row for `NCBITaxon:54551` with the reason `attested rule: Pichia terricola, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 1 related synonym, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:54551`.

## Evidence

- `data/raw/gold_organisms.tsv:38405` is the aggregate GOLD row for `NCBITaxon:54551` and reports `organism_count=5`, matching the YAML GOLD source attestation.
- Native GOLD has five exact organism rows, six linked project rows, and six linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:232231` through `data/raw/ncbi_type_material.tsv:232249` contain the 19 exact NCBI type-material rows for `NCBITaxon:54551`.
- StrainInfo has 22 direct exact JSONL rows and 47 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:54551`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:54551`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact type-material row set for `NCBITaxon:54551` was confirmed by reading the 19-line interval reported by the bounded scanner after an anomalous empty exact grep.
