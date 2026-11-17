# YAML Record Review: Rhizophagus irregularis DAOM 181602=DAOM 197198

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizophagus_irregularis_daom_181602_daom_197198.yaml`
- Identifier: `NCBITaxon:747089`

## Target

Reviewed the complete 90-line YAML record for Rhizophagus irregularis DAOM 181602=DAOM 197198. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizophagus_irregularis_daom_181602_daom_197198.

## Validation

- `just validate data/taxa/eukaryota/rhizophagus_irregularis_daom_181602_daom_197198.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizophagus_irregularis.yaml data/taxa/eukaryota/rhizophagus_irregularis_daom_181602_daom_197198.yaml data/taxa/eukaryota/rhizophlyctis_rosea.yaml data/taxa/eukaryota/rhizophydium_sp.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:172165`: `taxon_id` `NCBITaxon:747089`, label `Rhizophagus irregularis DAOM 181602=DAOM 197198`, rank `STRAIN`, parent `NCBITaxon:588596`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 7 exact synonyms, no related or broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 56607, added `2026-09-12` with reason `attested rule: Rhizophagus irregularis DAOM 181602=DAOM 197198, 2 sources incl. NCBI`.
- Checked all 13 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found three exact rows in `data/raw/ncbi_merged_ids.tsv` mapping old IDs `NCBITaxon:1097011`, `NCBITaxon:619289`, and `NCBITaxon:946008` to current `NCBITaxon:747089`; exact grep found no retained old rows in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:42234` for `NCBITaxon:747089` with `organism_count` `3`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 2 exact analysis rows, 2 exact organism rows, and 3 exact project rows for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 0 direct StrainInfo JSONL records, and 0 StrainInfo deposit records carrying `NCBITaxon:747089`.

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
