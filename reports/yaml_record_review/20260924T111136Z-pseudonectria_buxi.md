# YAML Record Review: Pseudonectria buxi

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudonectria_buxi.yaml`
- Identifier: `NCBITaxon:1053252`

## Target
Reviewed the complete 93-line YAML record for `Pseudonectria buxi`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudonectria_buxi`.

## Validation
- `just validate data/taxa/eukaryota/pseudonectria_buxi.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudomassariella_vexata.yaml data/taxa/eukaryota/pseudomerulius_curtisii.yaml data/taxa/eukaryota/pseudonectria_buxi.yaml data/taxa/eukaryota/pseudonectria_foliicola.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 227442 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:1053252` as species `Pseudonectria buxi`, with parent `NCBITaxon:40628`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 3 exact synonyms, 2 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 57436: `attested rule: Pseudonectria buxi, 2 sources incl. NCBI`.
- Sixteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had one exact current-ID row: line 87920 maps old ID `NCBITaxon:589686` into `NCBITaxon:1053252`; the exact two-file grep matched only `data/raw/ncbi_merged_ids.tsv`, so `NCBITaxon:589686` is not retained as a current NCBI row and the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:1053252` at line 996 with `organism_count=2`, matching the YAML GOLD source attestation.
- The native GOLD exports had 2 exact projects, 2 exact organism rows, and 2 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:1053252`.
- `data/straininfo/records.jsonl.gz` had 7 direct JSONL rows and 8 exact deposits for `NCBITaxon:1053252`; the exact numeric-boundary JSONL check also counted 7 rows.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:1053252`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:1053252`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:1053252`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
