# YAML Record Review: Pseudoechria curvicolla

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudoechria_curvicolla.yaml`
- Identifier: `NCBITaxon:48157`

## Target
Reviewed the complete 94-line YAML record for `Pseudoechria curvicolla`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudoechria_curvicolla`.

## Validation
- `just validate data/taxa/eukaryota/pseudoechria_curvicolla.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudocercospora_vitis.yaml data/taxa/eukaryota/pseudocohnilembus_persalinus.yaml data/taxa/eukaryota/pseudocosmospora_vilior.yaml data/taxa/eukaryota/pseudoechria_curvicolla.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 6136 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:48157` as species `Pseudoechria curvicolla`, with parent `NCBITaxon:2905961`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 2 exact synonyms, 3 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 52746: `attested rule: Pseudoechria curvicolla, 2 sources incl. NCBI`.
- Sixteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had one exact current-ID row: line 92103 maps old ID `NCBITaxon:683399` into `NCBITaxon:48157`; the exact two-file grep matched only `data/raw/ncbi_merged_ids.tsv`, so `NCBITaxon:683399` is not retained as a current NCBI row and the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:48157` at line 36774 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 2 exact projects, 1 exact organism row, and 0 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 0 exact rows for `NCBITaxon:48157`.
- `data/straininfo/records.jsonl.gz` had 4 direct JSONL rows and 6 exact deposits for `NCBITaxon:48157`; the exact numeric-boundary JSONL check also counted 4 rows.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:48157`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:48157`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:48157`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
