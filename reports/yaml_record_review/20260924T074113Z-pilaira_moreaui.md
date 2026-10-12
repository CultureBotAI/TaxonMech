# YAML Record Review: Pilaira moreaui

- Verdict: pass
- Target: `data/taxa/eukaryota/pilaira_moreaui.yaml`
- Identifier: `NCBITaxon:443155`

## Target

Reviewed the complete 73-line YAML record for `Pilaira moreaui`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pilaira_moreaui`.

## Validation

- `just validate data/taxa/eukaryota/pilaira_moreaui.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pichiaceae_sp_jcm_15000.yaml data/taxa/eukaryota/piedraia_hortae.yaml data/taxa/eukaryota/pilaira_anomala.yaml data/taxa/eukaryota/pilaira_moreaui.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:98492` is the exact retained NCBITaxon row for `NCBITaxon:443155`: label `Pilaira moreaui`, rank `SPECIES`, parent `NCBITaxon:64640`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:55667` contains the seeded in-scope row for `NCBITaxon:443155` with the reason `attested rule: Pilaira moreaui, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- The NCBI merged-ID inventory has no old IDs for `NCBITaxon:443155`.

## Evidence

- `data/raw/gold_organisms.tsv:35639` is the aggregate GOLD row for `NCBITaxon:443155` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:291320`, one linked project row at `data/gold/projects.jsonl.gz:193668`, and no linked analysis rows for this target.
- The NCBI type-material inventory has no exact rows for `NCBITaxon:443155`.
- StrainInfo has 2 direct exact JSONL rows and 7 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:443155`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:443155`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The YAML GOLD attestation correctly notes that records are filed directly under `Pilaira moreaui` and descendant taxa are not gathered for this generated record.
