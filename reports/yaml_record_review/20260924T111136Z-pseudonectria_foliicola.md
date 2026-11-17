# YAML Record Review: Pseudonectria foliicola

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudonectria_foliicola.yaml`
- Identifier: `NCBITaxon:1634538`

## Target
Reviewed the complete 81-line YAML record for `Pseudonectria foliicola`. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudonectria_foliicola`.

## Validation
- `just validate data/taxa/eukaryota/pseudonectria_foliicola.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudomassariella_vexata.yaml data/taxa/eukaryota/pseudomerulius_curtisii.yaml data/taxa/eukaryota/pseudonectria_buxi.yaml data/taxa/eukaryota/pseudonectria_foliicola.yaml` exited 0, scanned all four files, and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- Line 425226 of `data/raw/ncbitaxon_taxa.tsv` retained `NCBITaxon:1634538` as species `Pseudonectria foliicola`, with parent `NCBITaxon:40628`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by=gold`, and no `retired_into` value.
- The NCBI synonym columns supplied 0 exact synonyms, 1 related synonym, and 0 broad synonyms, matching the YAML synonym blocks.
- The seed-scope table had exactly one target row at line 60938: `attested rule: Pseudonectria foliicola, 2 sources incl. NCBI`.
- Sixteen lineage taxa from the YAML were checked against the raw NCBI table with 0 missing identifiers and 0 label mismatches.
- The NCBI merged-ID table had 0 exact rows for current ID `NCBITaxon:1634538`, so the empty `replaces` block is consistent.

## Evidence
- `data/raw/gold_organisms.tsv` had one aggregate row for `NCBITaxon:1634538` at line 13997 with `organism_count=2`, matching the YAML GOLD source attestation.
- The native GOLD exports had 2 exact projects, 2 exact organism rows, and 2 exact analyses for this taxon ID.
- `data/raw/ncbi_type_material.tsv` had 5 exact rows for `NCBITaxon:1634538`, lines 48514-48518: 4 culture-from-holotype rows and 1 culture-from-type-material row.
- `data/straininfo/records.jsonl.gz` had 2 direct JSONL rows and 2 exact deposits for `NCBITaxon:1634538`.
- The BacDive exact-target scan had 0 rows.

## Completeness
- The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` all had 0 exact rows for `NCBITaxon:1634538`.
- Auxiliary sources `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` all had 0 exact rows for `NCBITaxon:1634538`.
- The generated StrainInfo overlays `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` all had 0 exact rows for `NCBITaxon:1634538`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
Validation and source scans ran in the detached `/private/tmp/taxonmech-codex-review` worktree; this ignored report was the only primary-checkout write.
