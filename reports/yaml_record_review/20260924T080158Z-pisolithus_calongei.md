# YAML Record Review: Pisolithus calongei

- Verdict: pass
- Target: `data/taxa/eukaryota/pisolithus_calongei.yaml`
- Identifier: `NCBITaxon:1073420`

## Target

Reviewed the complete 90-line YAML record for `Pisolithus calongei`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pisolithus_calongei`.

## Validation

- `just validate data/taxa/eukaryota/pisolithus_calongei.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/piskurozyma_tuonelana.yaml data/taxa/eukaryota/piskurozyma_yama.yaml data/taxa/eukaryota/pisolithus_albus.yaml data/taxa/eukaryota/pisolithus_calongei.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:230051` is the exact retained NCBITaxon row for `NCBITaxon:1073420`: label `Pisolithus calongei`, rank `SPECIES`, parent `NCBITaxon:37467`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:57508` contains the seeded in-scope row for `NCBITaxon:1073420` with the reason `attested rule: Pisolithus calongei, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 0 exact synonyms, 6 related synonyms, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:2444`, `data/raw/ncbi_merged_ids.tsv:99421`, `data/raw/ncbi_merged_ids.tsv:99422`, and `data/raw/ncbi_merged_ids.tsv:99424` map old IDs `NCBITaxon:1073419`, `NCBITaxon:935958`, `NCBITaxon:935959`, and `NCBITaxon:935960` into `NCBITaxon:1073420`; exact anchored checks of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:1285` is the aggregate GOLD row for `NCBITaxon:1073420` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:291269`, one linked project row at `data/gold/projects.jsonl.gz:193616`, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:4717` through `data/raw/ncbi_type_material.tsv:4718` contain the 2 exact NCBI type-material rows for `NCBITaxon:1073420`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1073420`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1073420`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The four merged old IDs are merge metadata only for this generated record. Because none of those old IDs are present in the retained NCBITaxon table, the absence of generated `replaces` edges is expected.
