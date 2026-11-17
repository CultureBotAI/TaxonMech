# YAML Record Review: Pseudocosmospora vilior

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudocosmospora_vilior.yaml`
- Identifier: `NCBITaxon:45281`

## Target
Reviewed the complete 90-line YAML record for `Pseudocosmospora vilior`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudocosmospora_vilior`.

## Validation
- `just validate data/taxa/eukaryota/pseudocosmospora_vilior.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudocercospora_vitis.yaml data/taxa/eukaryota/pseudocohnilembus_persalinus.yaml data/taxa/eukaryota/pseudocosmospora_vilior.yaml data/taxa/eukaryota/pseudoechria_curvicolla.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 5523 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:45281` as species `Pseudocosmospora vilior`, with parent `NCBITaxon:1406987`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 2 exact synonyms, 2 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 52609: `attested rule: Pseudocosmospora vilior, 2 sources incl. NCBI`.
- Sixteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had two exact current-ID rows: line 18986 maps old ID `NCBITaxon:152773` into `NCBITaxon:45281`, and line 99943 maps old ID `NCBITaxon:94994` into `NCBITaxon:45281`; exact two-file greps matched only `data/raw/ncbi_merged_ids.tsv`, so neither old ID is retained as a current NCBI row and the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:45281` at line 35909 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 0 exact projects, 0 exact organism rows, and 0 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 6 exact rows for `NCBITaxon:45281`, lines 213819-213824: 3 culture-from-epitype designations, 2 epitype designations, and holotype `S F46424`.
- `data/straininfo/records.jsonl.gz` had 29 direct JSONL rows and 31 exact deposits for `NCBITaxon:45281`; the exact numeric-boundary JSONL check counted 30 rows, including non-direct siID 73217 carrying exact deposit `MUCL 4137` as `Nectria vilior`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:45281`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:45281`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:45281`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
