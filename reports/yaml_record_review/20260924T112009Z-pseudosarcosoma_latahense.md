# YAML Record Review: Pseudosarcosoma latahense

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudosarcosoma_latahense.yaml`
- Identifier: `NCBITaxon:1281308`

## Target
Reviewed the complete 85-line YAML record for `Pseudosarcosoma latahense`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudosarcosoma_latahense`.

## Validation
- `just validate data/taxa/eukaryota/pseudosarcosoma_latahense.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudorhypophila_sp.yaml data/taxa/eukaryota/pseudosarcosoma_latahense.yaml data/taxa/eukaryota/pseudosperma_rimosum.yaml data/taxa/eukaryota/pseudotaeniolina_globosa.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 299468 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:1281308` as species `Pseudosarcosoma latahense`, with parent `NCBITaxon:1281307`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 2 exact synonyms, 3 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 58899: `attested rule: Pseudosarcosoma latahense, 2 sources incl. NCBI`.
- Thirteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had two exact current-ID rows: line 10685 maps old ID `NCBITaxon:1280928` into `NCBITaxon:1281308`, and line 34995 maps old ID `NCBITaxon:201885` into `NCBITaxon:1281308`; exact two-file greps matched only `data/raw/ncbi_merged_ids.tsv`, so neither old ID is retained as a current NCBI row and the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:1281308` at line 6558 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 2 exact projects, 1 exact organism row, and 0 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 2 exact type-material rows for `NCBITaxon:1281308`, lines 18960-18961, covering designations `CBS 733.68` and `CBS:733.68`.
- `data/straininfo/records.jsonl.gz` had 1 direct JSONL row and 1 exact deposit for `NCBITaxon:1281308`: siID 167794 at line 120238 with deposit `CBS 733.68`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:1281308`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:1281308`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:1281308`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
