# YAML Record Review: Plectosphaerella plurivora

- Verdict: pass
- Target: `data/taxa/eukaryota/plectosphaerella_plurivora.yaml`
- Identifier: `NCBITaxon:936078`

## Target

Reviewed the complete 85-line YAML record for `Plectosphaerella plurivora`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plectosphaerella_plurivora`.

## Validation

- `just validate data/taxa/eukaryota/plectosphaerella_plurivora.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plectosphaerella_plurivora.yaml data/taxa/eukaryota/plenodomus_lingam.yaml data/taxa/eukaryota/plenodomus_lingam_jn3.yaml data/taxa/eukaryota/plenodomus_tracheiphilus_ipt5.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:198178` is the exact retained NCBITaxon row for `NCBITaxon:936078`: label `Plectosphaerella plurivora`, rank `SPECIES`, parent `NCBITaxon:40657`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:56955` contains the seeded in-scope row for `NCBITaxon:936078` with the reason `attested rule: Plectosphaerella plurivora, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:936078`.

## Evidence

- `data/raw/gold_organisms.tsv:44810` is the aggregate GOLD row for `NCBITaxon:936078` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row, two linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has five exact rows for `NCBITaxon:936078`: `CBS 131742`, `CBS:131742`, and `Plect365` as cultures from holotype, plus `CBS H-20899` and `CBS:H-20899` as holotypes.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 14 exact local JSONL records covering 14 deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:936078`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:936078`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows, so the generated YAML correctly remains a zero-strain record. The aggregate GOLD inventory reports 1 organism, while the local native GOLD project JSONL has 2 linked native project rows for this NCBI taxon; generated GOLD source attestations use the aggregate row.
