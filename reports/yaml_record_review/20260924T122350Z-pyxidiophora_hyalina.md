# YAML Record Review: Pyxidiophora hyalina

- Verdict: pass
- Target: `data/taxa/eukaryota/pyxidiophora_hyalina.yaml`
- Identifier: `NCBITaxon:112121`

## Target

Reviewed the complete 84-line YAML record for Pyxidiophora hyalina. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for pyxidiophora_hyalina.

## Validation

- `just validate data/taxa/eukaryota/pyxidiophora_hyalina.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pythium_periplocum.yaml data/taxa/eukaryota/pyxidiophora_arvernensis.yaml data/taxa/eukaryota/pyxidiophora_hyalina.yaml data/taxa/eukaryota/quambalaria_pitereka.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:20400`: `taxon_id` `NCBITaxon:112121`, label `Pyxidiophora hyalina`, rank `SPECIES`, parent `NCBITaxon:45040`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, exact synonym `Chalara hyalina`, 2 related synonyms, no broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 53783, added `2026-09-12` with reason `attested rule: Pyxidiophora hyalina, 2 sources incl. NCBI`.
- Checked all 15 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:112121` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:2200` for `NCBITaxon:112121` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 1 exact organism row, and 2 exact project rows for this identifier.
- Confirmed 4 exact type-material rows in `data/raw/ncbi_type_material.tsv`: `ATCC 52296`, `ATCC:52296`, `CBS 558.92`, and `CBS:558.92`.
- Confirmed 0 exact local BacDive rows, 1 direct StrainInfo JSONL record, and 2 StrainInfo deposit entries carrying `NCBITaxon:112121`.

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
