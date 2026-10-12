# YAML Record Review: Pichia phayaonensis

- Verdict: pass
- Target: `data/taxa/eukaryota/pichia_phayaonensis.yaml`
- Identifier: `NCBITaxon:1258690`

## Target

Reviewed the complete 90-line YAML record for `Pichia phayaonensis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pichia_phayaonensis`.

## Validation

- `just validate data/taxa/eukaryota/pichia_phayaonensis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pichia_paraexigua.yaml data/taxa/eukaryota/pichia_phayaonensis.yaml data/taxa/eukaryota/pichia_pseudocactophila.yaml data/taxa/eukaryota/pichia_pseudolambica.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:290315` is the exact retained NCBITaxon row for `NCBITaxon:1258690`: label `Pichia phayaonensis`, rank `SPECIES`, parent `NCBITaxon:4919`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:58784` contains the seeded in-scope row for `NCBITaxon:1258690` with the reason `attested rule: Pichia phayaonensis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 5 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:5921` and `data/raw/ncbi_merged_ids.tsv:94702` map old IDs `NCBITaxon:1165303` and `NCBITaxon:756821` into `NCBITaxon:1258690`; exact anchored checks of `data/raw/ncbitaxon_taxa.tsv` found no retained rows for those old IDs.

## Evidence

- `data/raw/gold_organisms.tsv:6115` is the aggregate GOLD row for `NCBITaxon:1258690` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:525638`, one linked project row at `data/gold/projects.jsonl.gz:609770`, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:17201` through `data/raw/ncbi_type_material.tsv:17215` contain the 15 exact NCBI type-material rows for `NCBITaxon:1258690`.
- BacDive and StrainInfo have no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:1258690`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:1258690`, consistent with the absence of exact StrainInfo JSONL rows.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The two merged old IDs are merge metadata only for this generated record. Because neither old ID is present in the retained NCBITaxon table, the absence of generated `replaces` edges is expected.
