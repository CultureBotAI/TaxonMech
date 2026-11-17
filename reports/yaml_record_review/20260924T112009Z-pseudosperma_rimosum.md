# YAML Record Review: Pseudosperma rimosum

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudosperma_rimosum.yaml`
- Identifier: `NCBITaxon:217425`

## Target
Reviewed the complete 105-line YAML record for `Pseudosperma rimosum`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudosperma_rimosum`.

## Validation
- `just validate data/taxa/eukaryota/pseudosperma_rimosum.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudorhypophila_sp.yaml data/taxa/eukaryota/pseudosarcosoma_latahense.yaml data/taxa/eukaryota/pseudosperma_rimosum.yaml data/taxa/eukaryota/pseudotaeniolina_globosa.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 42859 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:217425` as species `Pseudosperma rimosum`, with parent `NCBITaxon:2709788`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 4 exact synonyms, 7 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 54569: `attested rule: Pseudosperma rimosum, 2 sources incl. NCBI`.
- Fourteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had one exact current-ID row: line 99398 maps old ID `NCBITaxon:935575` into `NCBITaxon:217425`; the exact two-file grep matched only `data/raw/ncbi_merged_ids.tsv`, so `NCBITaxon:935575` is not retained as a current NCBI row and the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:217425` at line 20757 with `organism_count=2`, matching the YAML GOLD source attestation.
- The native GOLD exports had 0 exact projects, 0 exact organism rows, and 0 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 1 exact lectotype row for `NCBITaxon:217425` at line 86849: `L:L0054128`.
- `data/straininfo/records.jsonl.gz` had 1 direct JSONL row and 1 exact deposit for `NCBITaxon:217425`: siID 161015 at line 113790 with deposit `CBS 210.55`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:217425`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:217425`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:217425`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
