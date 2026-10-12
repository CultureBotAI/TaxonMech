# YAML Record Review: Rhodomonas salina

- Verdict: pass
- Target: `data/taxa/eukaryota/rhodomonas_salina.yaml`
- Identifier: `NCBITaxon:3034`

## Target

Reviewed the complete 75-line YAML record for Rhodomonas salina. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhodomonas_salina.

## Validation

- `just validate data/taxa/eukaryota/rhodomonas_salina.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhodomonas_salina.yaml data/taxa/eukaryota/rhodomonas_sp_rcc2513.yaml data/taxa/eukaryota/rhodonia_placenta.yaml data/taxa/eukaryota/rhodosorus_marinus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:2032`: `taxon_id` `NCBITaxon:3034`, label `Rhodomonas salina`, rank `SPECIES`, parent `NCBITaxon:37096`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 3 exact synonyms, 5 related synonyms, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 51835, added `2026-09-12` with reason `attested rule: Rhodomonas salina, 2 sources incl. NCBI`.
- Checked all 7 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 2 exact merged-ID rows mapping `NCBITaxon:402395` and `NCBITaxon:52970` into `NCBITaxon:3034`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:30371` for `NCBITaxon:3034` with `organism_count` `2`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 0 exact organism rows, and 0 exact project rows for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 0 direct StrainInfo JSONL records, and 1 StrainInfo deposit record carrying `NCBITaxon:3034`; the numeric-boundary JSONL count found 1 exact line, comprising 0 direct rows plus 1 non-direct row with 1 exact deposit.

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
