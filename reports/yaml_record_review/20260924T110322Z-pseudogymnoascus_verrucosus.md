# YAML Record Review: Pseudogymnoascus verrucosus

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudogymnoascus_verrucosus.yaml`
- Identifier: `NCBITaxon:342668`

## Target
Reviewed the complete 78-line YAML record for `Pseudogymnoascus verrucosus`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudogymnoascus_verrucosus`.

## Validation
- `just validate data/taxa/eukaryota/pseudogymnoascus_verrucosus.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudogymnoascus_pannorum.yaml data/taxa/eukaryota/pseudogymnoascus_pannorum_m1372.yaml data/taxa/eukaryota/pseudogymnoascus_verrucosus.yaml data/taxa/eukaryota/pseudohalonectria_lignicola.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 70595 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:342668` as species `Pseudogymnoascus verrucosus`, with parent `NCBITaxon:78156`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 0 exact synonyms, 1 related synonym, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 55284: `attested rule: Pseudogymnoascus verrucosus, 2 sources incl. NCBI`.
- Fifteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:342668`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:342668` at line 32830 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 2 exact projects, 1 exact organism row, and 1 exact analysis for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 2 exact culture-from-type-material rows for `NCBITaxon:342668`, lines 188150-188151, covering designations `UAMH 10579` and `UAMH:10579`.
- `data/straininfo/records.jsonl.gz` had 3 direct JSONL rows and 3 exact deposits for `NCBITaxon:342668`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:342668`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:342668`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:342668`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
