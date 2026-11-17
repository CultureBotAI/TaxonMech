# YAML Record Review: Rhizophagus irregularis

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizophagus_irregularis.yaml`
- Identifier: `NCBITaxon:588596`

## Target

Reviewed the complete 95-line YAML record for Rhizophagus irregularis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizophagus_irregularis.

## Validation

- `just validate data/taxa/eukaryota/rhizophagus_irregularis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizophagus_irregularis.yaml data/taxa/eukaryota/rhizophagus_irregularis_daom_181602_daom_197198.yaml data/taxa/eukaryota/rhizophlyctis_rosea.yaml data/taxa/eukaryota/rhizophydium_sp.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:139284`: `taxon_id` `NCBITaxon:588596`, label `Rhizophagus irregularis`, rank `SPECIES`, parent `NCBITaxon:1129544`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 2 exact synonyms, 7 related synonyms, no broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 56113, added `2026-09-12` with reason `attested rule: Rhizophagus irregularis, 2 sources incl. NCBI`.
- Checked all 12 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found seven exact rows in `data/raw/ncbi_merged_ids.tsv` mapping old IDs `NCBITaxon:2358151`, `NCBITaxon:592166`, `NCBITaxon:658198`, `NCBITaxon:658199`, `NCBITaxon:658620`, `NCBITaxon:758872`, and `NCBITaxon:946009` to current `NCBITaxon:588596`; exact grep found no retained old rows in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:39551` for `NCBITaxon:588596` with `organism_count` `13`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 15 exact analysis rows, 13 exact organism rows, and 15 exact project rows for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 4 direct StrainInfo JSONL records, and 4 StrainInfo deposit entries carrying `NCBITaxon:588596`.

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
