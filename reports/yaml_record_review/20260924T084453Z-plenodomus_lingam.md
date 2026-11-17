# YAML Record Review: Plenodomus lingam

- Verdict: pass
- Target: `data/taxa/eukaryota/plenodomus_lingam.yaml`
- Identifier: `NCBITaxon:5022`

## Target

Reviewed the complete 124-line YAML record for `Plenodomus lingam`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `plenodomus_lingam`.

## Validation

- `just validate data/taxa/eukaryota/plenodomus_lingam.yaml` passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/plectosphaerella_plurivora.yaml data/taxa/eukaryota/plenodomus_lingam.yaml data/taxa/eukaryota/plenodomus_lingam_jn3.yaml data/taxa/eukaryota/plenodomus_tracheiphilus_ipt5.yaml` scanned the four-file batch and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2191` is the exact retained NCBITaxon row for `NCBITaxon:5022`: label `Plenodomus lingam`, rank `SPECIES`, parent `NCBITaxon:220671`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:51909` contains the seeded in-scope row for `NCBITaxon:5022` with the reason `attested rule: Plenodomus lingam, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 4 exact synonyms, 9 related synonyms, and 0 broad synonyms.
- All 18 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:2633` maps old ID `NCBITaxon:1077373` into `NCBITaxon:5022`; an exact anchored check of `data/raw/ncbitaxon_taxa.tsv` found no retained row for that old ID.

## Evidence

- `data/raw/gold_organisms.tsv:37337` is the aggregate GOLD row for `NCBITaxon:5022` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has three exact organism rows, three linked project rows, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv` has four exact rows for `NCBITaxon:5022`: `CBS 260.94` and `CBS:260.94` as cultures from epitype, plus `CBS H-24655,` and `CBS:H-24655` as epitypes.
- BacDive has no exact local JSONL records for this NCBI taxon; an exact anchored scan of StrainInfo found 50 exact local JSONL records covering 54 deposits.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:5022`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:5022`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The merged old ID is merge metadata only for this generated record. Because that old ID is not present in the retained NCBITaxon table, the absence of a generated `replaces` edge is expected. The exact StrainInfo JSONL hits have no corresponding BacDive or generated StrainInfo overlay rows, so the generated YAML correctly remains a zero-strain record. The aggregate GOLD inventory reports 2 organisms, while the local native GOLD organism JSONL has 3 exact rows for this NCBI taxon; generated GOLD source attestations use the aggregate row.
