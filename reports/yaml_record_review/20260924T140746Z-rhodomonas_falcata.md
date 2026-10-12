# YAML Record Review: Rhodomonas falcata

- Verdict: pass
- Target: `data/taxa/eukaryota/rhodomonas_falcata.yaml`
- Identifier: `NCBITaxon:356655`

## Target

Reviewed the complete 60-line YAML record for Rhodomonas falcata. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhodomonas_falcata.

## Validation

- `just validate data/taxa/eukaryota/rhodomonas_falcata.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhodomonas_falcata.yaml data/taxa/eukaryota/rhodomonas_irregularis.yaml data/taxa/eukaryota/rhodomonas_lens.yaml data/taxa/eukaryota/rhodomonas_marina.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:73550`: `taxon_id` `NCBITaxon:356655`, label `Rhodomonas falcata`, rank `SPECIES`, parent `NCBITaxon:37096`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 1 exact synonym, 2 related synonyms, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 55335, added `2026-09-12` with reason `attested rule: Rhodomonas falcata, 2 sources incl. NCBI`.
- Checked all 7 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:356655` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:33098` for `NCBITaxon:356655` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 1 exact organism row, and 1 exact project row for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 1 direct StrainInfo JSONL record, and 1 StrainInfo deposit record carrying `NCBITaxon:356655`.

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
