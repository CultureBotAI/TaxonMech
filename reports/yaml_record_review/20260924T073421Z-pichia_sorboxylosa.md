# YAML Record Review: Pichia sorboxylosa

- Verdict: pass
- Target: `data/taxa/eukaryota/pichia_sorboxylosa.yaml`
- Identifier: `NCBITaxon:49334`

## Target

Reviewed the complete 79-line YAML record for `Pichia sorboxylosa`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pichia_sorboxylosa`.

## Validation

- `just validate data/taxa/eukaryota/pichia_sorboxylosa.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pichia_rugopelliculosa.yaml data/taxa/eukaryota/pichia_scutulata.yaml data/taxa/eukaryota/pichia_sorboxylosa.yaml data/taxa/eukaryota/pichia_sp.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:6284` is the exact retained NCBITaxon row for `NCBITaxon:49334`: label `Pichia sorboxylosa`, rank `SPECIES`, parent `NCBITaxon:4919`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:52808` contains the seeded in-scope row for `NCBITaxon:49334` with the reason `attested rule: Pichia sorboxylosa, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:49334`.

## Evidence

- `data/raw/gold_organisms.tsv:37177` is the aggregate GOLD row for `NCBITaxon:49334` and reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD has two exact organism rows at `data/gold/organisms.jsonl.gz:78906` and `data/gold/organisms.jsonl.gz:525774`, two linked project rows at `data/gold/projects.jsonl.gz:90151` and `data/gold/projects.jsonl.gz:609919`, and one analysis row at `data/gold/analyses.jsonl.gz:75589`.
- `data/raw/ncbi_type_material.tsv:223629` through `data/raw/ncbi_type_material.tsv:223650` contain the 22 exact NCBI type-material rows for `NCBITaxon:49334`.
- StrainInfo has 16 direct exact JSONL rows and 32 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:49334`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:49334`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
