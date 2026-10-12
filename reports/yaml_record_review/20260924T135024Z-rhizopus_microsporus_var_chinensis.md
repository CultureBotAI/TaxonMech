# YAML Record Review: Rhizopus microsporus var. chinensis

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizopus_microsporus_var_chinensis.yaml`
- Identifier: `NCBITaxon:4843`

## Target

Reviewed the complete 87-line YAML record for Rhizopus microsporus var. chinensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizopus_microsporus_var_chinensis.

## Validation

- `just validate data/taxa/eukaryota/rhizopus_microsporus_var_chinensis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizopus_lyococcus.yaml data/taxa/eukaryota/rhizopus_microsporus.yaml data/taxa/eukaryota/rhizopus_microsporus_var_chinensis.yaml data/taxa/eukaryota/rhizopus_microsporus_var_microsporus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:2092`: `taxon_id` `NCBITaxon:4843`, label `Rhizopus microsporus var. chinensis`, rank `VARIETAS`, parent `NCBITaxon:58291`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 3 exact synonyms, 2 related synonyms, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 51858, added `2026-09-12` with reason `attested rule: Rhizopus microsporus var. chinensis, 2 sources incl. NCBI`.
- Checked all 14 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:4843` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:36844` for `NCBITaxon:4843` with `organism_count` `6`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 6 exact organism rows, and 6 exact project rows for this identifier.
- Confirmed all 6 exact rows in `data/raw/ncbi_type_material.tsv`, at lines 221347-221352, carrying type-material designations for `ATCC 52807`, `CBS 631.82`, and `IMI 130842` variants under `Rhizopus chinensis`.
- Confirmed 0 exact local BacDive rows, 40 direct StrainInfo JSONL records, and 71 StrainInfo deposit records carrying `NCBITaxon:4843`; the numeric-boundary JSONL count found 42 exact lines, comprising 40 direct rows plus 2 non-direct rows with 2 exact deposits.

## Completeness

- Generated strain raw tables have no rows for this target: `data/raw/bacdive_strains.tsv` 0, `data/raw/culture_collection_strains.tsv` 0, `data/raw/strain_assemblies.tsv` 0, `data/raw/strain_genome_records.tsv` 0, and `data/raw/strain_related_records.tsv` 0.
- Auxiliary source scans all returned 0 rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlays have no rows for this target in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

Review completed in the detached worktree `/private/tmp/taxonmech-codex-review`; only this ignored report was added to the primary checkout.
