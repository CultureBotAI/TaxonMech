# YAML Record Review: Pseudomassariella vexata

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudomassariella_vexata.yaml`
- Identifier: `NCBITaxon:1141098`

## Target
Reviewed the complete 93-line YAML record for `Pseudomassariella vexata`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudomassariella_vexata`.

## Validation
- `just validate data/taxa/eukaryota/pseudomassariella_vexata.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudomassariella_vexata.yaml data/taxa/eukaryota/pseudomerulius_curtisii.yaml data/taxa/eukaryota/pseudonectria_buxi.yaml data/taxa/eukaryota/pseudonectria_foliicola.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 247834 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:1141098` as species `Pseudomassariella vexata`, with parent `NCBITaxon:1812772`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 3 exact synonyms, 2 related synonyms, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 57912: `attested rule: Pseudomassariella vexata, 2 sources incl. NCBI`.
- Sixteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:1141098`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:1141098` at line 2917 with `organism_count=1`, matching the YAML GOLD source attestation.
- The native GOLD exports had 2 exact projects, 1 exact organism row, and 2 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 4 exact rows for `NCBITaxon:1141098`, lines 9232-9235: culture-from-epitype designations `CBS 129021` and `CBS:129021`, plus epitype designations `WU 31333` and `WU:31333`.
- `data/straininfo/records.jsonl.gz` had 0 direct JSONL rows and 0 exact deposits for `NCBITaxon:1141098`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:1141098`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:1141098`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:1141098`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
