# YAML Record Review: Pyrrhoderma lamaoense

- Verdict: pass
- Target: `data/taxa/eukaryota/pyrrhoderma_lamaoense.yaml`
- Identifier: `NCBITaxon:2282106`

## Target

Reviewed the complete 108-line YAML record for Pyrrhoderma lamaoense. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for pyrrhoderma_lamaoense.

## Validation

- `just validate data/taxa/eukaryota/pyrrhoderma_lamaoense.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pyropia_haitanensis.yaml data/taxa/eukaryota/pyropia_yezoensis.yaml data/taxa/eukaryota/pyrrhoderma_lamaoense.yaml data/taxa/eukaryota/pyrrhoderma_noxium.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:522810`: `taxon_id` `NCBITaxon:2282106`, label `Pyrrhoderma lamaoense`, rank `SPECIES`, parent `NCBITaxon:175660`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 8 exact synonyms, 5 related synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 62529, added `2026-09-12` with reason `attested rule: Pyrrhoderma lamaoense, 2 sources incl. NCBI`.
- Checked all 13 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found one exact row in `data/raw/ncbi_merged_ids.tsv` mapping old `NCBITaxon:1156444` to current `NCBITaxon:2282106`; exact grep found no retained old row in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:21392` for `NCBITaxon:2282106` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 0 exact organism rows, and 0 exact project rows for this identifier.
- Confirmed 2 exact type-material rows in `data/raw/ncbi_type_material.tsv`: `NY:collector:R.S.Williams:` for `Pyropolyporus lamaensis` and `NY:collector:R.S.Williams:` for `Pyropolyporus lamaoensis`.
- Confirmed 0 exact local BacDive rows, 3 direct StrainInfo JSONL records, and 3 StrainInfo deposit entries carrying `NCBITaxon:2282106`.

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
