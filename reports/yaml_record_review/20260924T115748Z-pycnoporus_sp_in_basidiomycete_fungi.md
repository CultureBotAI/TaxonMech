# YAML Record Review: Pycnoporus sp. (in: basidiomycete fungi)

- Verdict: pass
- Target: `data/taxa/eukaryota/pycnoporus_sp_in_basidiomycete_fungi.yaml`
- Identifier: `NCBITaxon:2047320`

## Target

Reviewed the complete 71-line YAML record for Pycnoporus sp. (in: basidiomycete fungi). The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for pycnoporus_sp_in_basidiomycete_fungi.

## Validation

- `just validate data/taxa/eukaryota/pycnoporus_sp_in_basidiomycete_fungi.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pycnoporus_sp_in_basidiomycete_fungi.yaml data/taxa/eukaryota/pyrenochaeta_sp.yaml data/taxa/eukaryota/pyrenophora_seminiperda_ccb06.yaml data/taxa/eukaryota/pyrenophora_teres_f_maculata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:513624`: `taxon_id` `NCBITaxon:2047320`, label `Pycnoporus sp. (in: basidiomycete fungi)`, rank `SPECIES`, parent `NCBITaxon:2676587`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, no exact, broad, or related synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 62177, added `2026-09-12` with reason `attested rule: Pycnoporus sp. (in: basidiomycete fungi), 2 sources incl. NCBI`.
- Checked all 14 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:2047320` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:19459` for `NCBITaxon:2047320` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 0 exact organism rows, and 0 exact project rows for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 0 direct StrainInfo JSONL records, and 0 StrainInfo deposit records carrying `NCBITaxon:2047320`.

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
