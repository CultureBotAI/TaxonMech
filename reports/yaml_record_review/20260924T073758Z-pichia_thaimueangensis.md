# YAML Record Review: Pichia thaimueangensis

- Verdict: pass
- Target: `data/taxa/eukaryota/pichia_thaimueangensis.yaml`
- Identifier: `NCBITaxon:392265`

## Target

Reviewed the complete 89-line YAML record for `Pichia thaimueangensis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pichia_thaimueangensis`.

## Validation

- `just validate data/taxa/eukaryota/pichia_thaimueangensis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pichia_sp_pb3310.yaml data/taxa/eukaryota/pichia_sporocuriosa.yaml data/taxa/eukaryota/pichia_terricola.yaml data/taxa/eukaryota/pichia_thaimueangensis.yaml` scanned the four-file batch with 0 files containing ERROR rows and 0 total ERROR rows.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:83186` is the exact retained NCBITaxon row for `NCBITaxon:392265`: label `Pichia thaimueangensis`, rank `SPECIES`, parent `NCBITaxon:4919`, genetic code `1`, `attested_by` GOLD, and no `retired_into` value.
- `curation/seed_scope.tsv:55488` contains the seeded in-scope row for `NCBITaxon:392265` with the reason `attested rule: Pichia thaimueangensis, 2 sources incl. NCBI`.
- The YAML synonym block matches the NCBITaxon source fields: 1 exact synonym, 5 related synonyms, and 0 broad synonyms.
- All 13 YAML lineage ancestors were checked against exact retained NCBITaxon rows with no missing ancestors and no label, rank, or identifier mismatches.
- `data/raw/ncbi_merged_ids.tsv:62745` maps old ID `NCBITaxon:3082069` into `NCBITaxon:392265`; an exact anchored check of `data/raw/ncbitaxon_taxa.tsv` found no retained row for that old ID.

## Evidence

- `data/raw/gold_organisms.tsv:34146` is the aggregate GOLD row for `NCBITaxon:392265` and reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD has one exact organism row at `data/gold/organisms.jsonl.gz:525625`, one linked project row at `data/gold/projects.jsonl.gz:609757`, and no linked analysis rows for this target.
- `data/raw/ncbi_type_material.tsv:201755` through `data/raw/ncbi_type_material.tsv:201774` contain the 20 exact NCBI type-material rows for `NCBITaxon:392265`.
- StrainInfo has 1 direct exact JSONL row and 3 exact deposit hits for this taxon; BacDive has no exact local JSONL records for this NCBI taxon.

## Completeness

- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` have no rows for `NCBITaxon:392265`.
- The auxiliary exact-source scans of BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive all returned 0 rows.
- The generated StrainInfo overlay tables `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` have no rows for `NCBITaxon:392265`; exact StrainInfo evidence is present only in the local source JSONL and did not pass through the BacDive-derived local-strain overlay.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The single merged old ID is merge metadata only for this generated record. Because `NCBITaxon:3082069` is absent from the retained NCBITaxon table, the absence of a generated `replaces` edge is expected.
