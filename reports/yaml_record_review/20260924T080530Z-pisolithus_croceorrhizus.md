# YAML Record Review: Pisolithus croceorrhizus

- Verdict: pass
- Target: `data/taxa/eukaryota/pisolithus_croceorrhizus.yaml`
- Identifier: `NCBITaxon:2060934`

## Target

Reviewed the complete 78-line YAML record for `Pisolithus croceorrhizus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pisolithus_croceorrhizus`.

## Validation

- `just validate data/taxa/eukaryota/pisolithus_croceorrhizus.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pisolithus_capsulifer.yaml data/taxa/eukaryota/pisolithus_croceorrhizus.yaml data/taxa/eukaryota/pisolithus_marmoratus.yaml data/taxa/eukaryota/pisolithus_microcarpus.yaml` exited successfully over the four-file batch.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:515058` is the exact retained NCBITaxon row for `NCBITaxon:2060934`: label `Pisolithus croceorrhizus`, rank `SPECIES`, parent `NCBITaxon:37467`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:62239` contains the seeded in-scope row for `NCBITaxon:2060934` with the reason `attested rule: Pisolithus croceorrhizus, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 1 related synonym, and 0 broad synonyms.
- All 14 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:8225` and `data/raw/ncbi_merged_ids.tsv:37950` map old IDs `NCBITaxon:1217551` and `NCBITaxon:2136025` into `NCBITaxon:2060934`; exact anchored checks of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:19707` is the aggregate GOLD row for `NCBITaxon:2060934` and reports `organism_count=16`, matching the YAML GOLD source attestation.
- Native GOLD has 16 exact organism rows, 25 linked project rows, and two linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:82150` through `data/raw/ncbi_type_material.tsv:82154` contain the 5 exact NCBI type-material rows for `NCBITaxon:2060934`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:2060934`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:2060934`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The two merged old IDs are merge metadata only for this generated record. Because neither old ID is present in the retained NCBITaxon table, the absence of generated `replaces` edges is expected.
