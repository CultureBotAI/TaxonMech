# YAML Record Review: Piedraia hortae

- Verdict: pass
- Target: `data/taxa/eukaryota/piedraia_hortae.yaml`
- Identifier: `NCBITaxon:147573`

## Target

Reviewed the complete 84-line YAML record for `Piedraia hortae`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `piedraia_hortae`.

## Validation

- `just validate data/taxa/eukaryota/piedraia_hortae.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pichiaceae_sp_jcm_15000.yaml data/taxa/eukaryota/piedraia_hortae.yaml data/taxa/eukaryota/pilaira_anomala.yaml data/taxa/eukaryota/pilaira_moreaui.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:30123` is the exact retained NCBITaxon row for `NCBITaxon:147573`: label `Piedraia hortae`, rank `SPECIES`, parent `NCBITaxon:147572`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:54051` contains the seeded in-scope row for `NCBITaxon:147573` with the reason `attested rule: Piedraia hortae, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 1 related synonym, and 0 broad synonyms.
- All 16 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:147573`.

## Evidence

- `data/raw/gold_organisms.tsv:11408` is the aggregate GOLD row for `NCBITaxon:147573` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:20734`, two linked project rows starting at `data/gold/projects.jsonl.gz:20224`, and one linked analysis row at `data/gold/analyses.jsonl.gz:137474`.
- The NCBI type-material inventory has no exact rows for `NCBITaxon:147573`.
- StrainInfo has 1 direct exact JSONL row and 1 exact deposit hit for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:147573`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:147573`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The source and generated inventories support the current record as a GOLD plus NCBITaxon seed with no generated strain assertions.
