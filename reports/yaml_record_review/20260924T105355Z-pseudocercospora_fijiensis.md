# YAML Record Review: Pseudocercospora fijiensis

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudocercospora_fijiensis.yaml`
- Identifier: `NCBITaxon:1873960`

## Target
Reviewed the complete 100-line YAML record for `Pseudocercospora fijiensis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudocercospora_fijiensis`.

## Validation
- `just validate data/taxa/eukaryota/pseudocercospora_fijiensis.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudocercospora_cruenta.yaml data/taxa/eukaryota/pseudocercospora_crystallina.yaml data/taxa/eukaryota/pseudocercospora_eumusae.yaml data/taxa/eukaryota/pseudocercospora_fijiensis.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 489659 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:1873960` as species `Pseudocercospora fijiensis`, with parent `NCBITaxon:131324`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 5 exact synonyms, 2 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 61419: `attested rule: Pseudocercospora fijiensis, 2 sources incl. NCBI`.
- Sixteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had two exact current-ID rows: line 83031 maps old ID `NCBITaxon:513417` into `NCBITaxon:1873960`, and line 96323 maps old ID `NCBITaxon:83344` into `NCBITaxon:1873960`; exact two-file greps matched only `data/raw/ncbi_merged_ids.tsv`, so neither old ID is retained as a current NCBI row and the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:1873960` at line 16849 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 2 exact projects, 1 exact organism row, and 2 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:1873960`.
- `data/straininfo/records.jsonl.gz` had 25 direct JSONL rows and 25 exact deposits for `NCBITaxon:1873960`; the exact numeric-boundary JSONL check also counted 25 rows.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:1873960`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:1873960`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:1873960`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
