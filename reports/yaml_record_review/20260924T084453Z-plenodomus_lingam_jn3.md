# YAML Record Review: Plenodomus lingam JN3

- Verdict: pass
- Target: `data/taxa/eukaryota/plenodomus_lingam_jn3.yaml`
- Identifier: `NCBITaxon:985895`

## Target

Reviewed the complete 90-line YAML record for `Plenodomus lingam JN3`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plenodomus_lingam_jn3`.

## Validation

- `just validate data/taxa/eukaryota/plenodomus_lingam_jn3.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plectosphaerella_plurivora.yaml data/taxa/eukaryota/plenodomus_lingam.yaml data/taxa/eukaryota/plenodomus_lingam_jn3.yaml data/taxa/eukaryota/plenodomus_tracheiphilus_ipt5.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:205542` is the exact retained NCBITaxon row for `NCBITaxon:985895`: label `Plenodomus lingam JN3`, rank `STRAIN`, parent `NCBITaxon:5022`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:57081` contains the seeded in-scope row for `NCBITaxon:985895` with the reason `attested rule: Plenodomus lingam JN3, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 0 related synonyms, and 0 broad synonyms.
- All 19 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:985895`.

## Evidence

- `data/raw/gold_organisms.tsv:45337` is the aggregate GOLD row for `NCBITaxon:985895` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD organism, project, and analysis files each have one exact row for this target.
- `data/raw/ncbi_type_material.tsv` has no exact type-material rows for `NCBITaxon:985895`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:985895`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:985895`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No additional notes.
