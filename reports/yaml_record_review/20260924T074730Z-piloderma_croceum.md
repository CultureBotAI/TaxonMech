# YAML Record Review: Piloderma croceum

- Verdict: pass
- Target: `data/taxa/eukaryota/piloderma_croceum.yaml`
- Identifier: `NCBITaxon:80663`

## Target

Reviewed the complete 72-line YAML record for `Piloderma croceum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `piloderma_croceum`.

## Validation

- `just validate data/taxa/eukaryota/piloderma_croceum.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/piloderma_byssinum.yaml data/taxa/eukaryota/piloderma_croceum.yaml data/taxa/eukaryota/piloderma_sphaerosporum.yaml data/taxa/eukaryota/pinguiococcus_pyrenoidosus.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:12074` is the exact retained NCBITaxon row for `NCBITaxon:80663`: label `Piloderma croceum`, rank `SPECIES`, parent `NCBITaxon:80662`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:53358` contains the seeded in-scope row for `NCBITaxon:80663` with the reason `attested rule: Piloderma croceum, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:80663`.

## Evidence

- `data/raw/gold_organisms.tsv:42884` is the aggregate GOLD row for `NCBITaxon:80663` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:833`, seven linked project rows starting at `data/gold/projects.jsonl.gz:854`, and one linked analysis row at `data/gold/analyses.jsonl.gz:138951`.
- The NCBI type-material inventory has no exact rows for `NCBITaxon:80663`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:80663`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:80663`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
