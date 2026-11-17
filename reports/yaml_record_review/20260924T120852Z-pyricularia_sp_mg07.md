# YAML Record Review: Pyricularia sp. MG07

- Verdict: pass
- Target: `data/taxa/eukaryota/pyricularia_sp_mg07.yaml`
- Identifier: `NCBITaxon:1758318`

## Target

Reviewed the complete 80-line YAML record for Pyricularia sp. MG07. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for pyricularia_sp_mg07.

## Validation

- `just validate data/taxa/eukaryota/pyricularia_sp_mg07.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pyricularia_sp_mg07.yaml data/taxa/eukaryota/pyricularia_sp_mg08.yaml data/taxa/eukaryota/pyricularia_sp_mg12.yaml data/taxa/eukaryota/pyrocystis_lunula.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:458922`: `taxon_id` `NCBITaxon:1758318`, label `Pyricularia sp. MG07`, rank `SPECIES`, parent `NCBITaxon:2638110`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, no exact, broad, or related synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 61221, added `2026-09-12` with reason `attested rule: Pyricularia sp. MG07, 2 sources incl. NCBI`.
- Checked all 17 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:1758318` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:15304` for `NCBITaxon:1758318` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 1 exact analysis row, 1 exact organism row, and 1 exact project row for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 0 direct StrainInfo JSONL records, and 0 StrainInfo deposit records carrying `NCBITaxon:1758318`.

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
