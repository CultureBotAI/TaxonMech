# YAML Record Review: Pseudogymnoascus pannorum

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudogymnoascus_pannorum.yaml`
- Identifier: `NCBITaxon:79858`

## Target
Reviewed the complete 106-line YAML record for `Pseudogymnoascus pannorum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudogymnoascus_pannorum`.

## Validation
- `just validate data/taxa/eukaryota/pseudogymnoascus_pannorum.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudogymnoascus_pannorum.yaml data/taxa/eukaryota/pseudogymnoascus_pannorum_m1372.yaml data/taxa/eukaryota/pseudogymnoascus_verrucosus.yaml data/taxa/eukaryota/pseudohalonectria_lignicola.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 11701 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:79858` as species `Pseudogymnoascus pannorum`, with parent `NCBITaxon:78156`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 6 exact synonyms, 4 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 53342: `attested rule: Pseudogymnoascus pannorum, 2 sources incl. NCBI`.
- Fifteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had one exact current-ID row: line 95928 maps old ID `NCBITaxon:79859` into `NCBITaxon:79858`; the exact two-file grep matched only `data/raw/ncbi_merged_ids.tsv`, so `NCBITaxon:79859` is not retained as a current NCBI row and the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:79858` at line 42855 with `organism_count=2`, matching the YAML GOLD source attestation.
- The native GOLD exports had 1 exact project, 1 exact organism row, and 0 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:79858`.
- `data/straininfo/records.jsonl.gz` had 223 direct JSONL rows and 271 exact deposits for `NCBITaxon:79858`; the exact numeric-boundary JSONL check counted 224 rows, including non-direct siID 121546 carrying exact deposit `UAMH 3089` as `Geomyces pannorum`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:79858`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:79858`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:79858`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
