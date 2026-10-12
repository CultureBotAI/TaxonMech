# YAML Record Review: Pseudohyphozyma bogoriensis

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudohyphozyma_bogoriensis.yaml`
- Identifier: `NCBITaxon:106002`

## Target
Reviewed the complete 85-line YAML record for `Pseudohyphozyma bogoriensis`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudohyphozyma_bogoriensis`.

## Validation
- `just validate data/taxa/eukaryota/pseudohyphozyma_bogoriensis.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudohansfordia_irregularis.yaml data/taxa/eukaryota/pseudohaptolina_sorokinii.yaml data/taxa/eukaryota/pseudohyphozyma_bogoriensis.yaml data/taxa/eukaryota/pseudohyphozyma_pustula.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 19039 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:106002` as species `Pseudohyphozyma bogoriensis`, with parent `NCBITaxon:1801563`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 3 exact synonyms, 3 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 53709: `attested rule: Pseudohyphozyma bogoriensis, 2 sources incl. NCBI`.
- Twelve lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:106002`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:106002` at line 1092 with `organism_count=10`, matching the YAML GOLD source attestation.
- The native GOLD exports had 0 exact projects, 10 exact organism rows, and 0 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 20 exact rows for `NCBITaxon:106002`, lines 3839-3858: 2 culture-from-type-material rows and 18 type-material rows under `Candida bogoriensis`.
- `data/straininfo/records.jsonl.gz` had 3 direct JSONL rows and 14 exact deposits for `NCBITaxon:106002`; the exact numeric-boundary JSONL check also counted 3 rows.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:106002`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:106002`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:106002`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
