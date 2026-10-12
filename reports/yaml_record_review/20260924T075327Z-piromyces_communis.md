# YAML Record Review: Piromyces communis

- Verdict: pass
- Target: `data/taxa/eukaryota/piromyces_communis.yaml`
- Identifier: `NCBITaxon:4822`

## Target

Reviewed the complete 75-line YAML record for `Piromyces communis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `piromyces_communis`.

## Validation

- `just validate data/taxa/eukaryota/piromyces_communis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pirella_circinans.yaml data/taxa/eukaryota/pirella_naumovii.yaml data/taxa/eukaryota/pirella_reniformis.yaml data/taxa/eukaryota/piromyces_communis.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2078` is the exact retained NCBITaxon row for `NCBITaxon:4822`: label `Piromyces communis`, rank `SPECIES`, parent `NCBITaxon:4821`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:51851` contains the seeded in-scope row for `NCBITaxon:4822` with the reason `attested rule: Piromyces communis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- All 12 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:13875` maps old ID `NCBITaxon:137782` into `NCBITaxon:4822`; an exact anchored check of `data/raw/ncbitaxon_taxa.tsv` found no retained row for that old ID.

## Evidence

- `data/raw/gold_organisms.tsv:36783` is the aggregate GOLD row for `NCBITaxon:4822` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:359562`, 62 linked project rows, and no linked analysis rows for this target.
- The NCBI type-material inventory has no exact rows for `NCBITaxon:4822`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:4822`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:4822`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The single merged old ID is merge metadata only for this generated record. Because `NCBITaxon:137782` is absent from the retained NCBITaxon table, the absence of a generated `replaces` edge is expected.
