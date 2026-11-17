# YAML Record Review: Piloderma byssinum

- Verdict: pass
- Target: `data/taxa/eukaryota/piloderma_byssinum.yaml`
- Identifier: `NCBITaxon:146056`

## Target

Reviewed the complete 78-line YAML record for `Piloderma byssinum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `piloderma_byssinum`.

## Validation

- `just validate data/taxa/eukaryota/piloderma_byssinum.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/piloderma_byssinum.yaml data/taxa/eukaryota/piloderma_croceum.yaml data/taxa/eukaryota/piloderma_sphaerosporum.yaml data/taxa/eukaryota/pinguiococcus_pyrenoidosus.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:29579` is the exact retained NCBITaxon row for `NCBITaxon:146056`: label `Piloderma byssinum`, rank `SPECIES`, parent `NCBITaxon:80662`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54032` contains the seeded in-scope row for `NCBITaxon:146056` with the reason `attested rule: Piloderma byssinum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:146056`.

## Evidence

- `data/raw/gold_organisms.tsv:11169` is the aggregate GOLD row for `NCBITaxon:146056` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:346134`, two linked project rows starting at `data/gold/projects.jsonl.gz:283826`, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:32851` through `data/raw/ncbi_type_material.tsv:32858` contain the 8 exact NCBI type-material rows for `NCBITaxon:146056`.
- StrainInfo has 1 direct exact JSONL row and 1 exact deposit hit for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:146056`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:146056`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
