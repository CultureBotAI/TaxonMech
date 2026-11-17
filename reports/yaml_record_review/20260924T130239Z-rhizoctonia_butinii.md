# YAML Record Review: Rhizoctonia butinii

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizoctonia_butinii.yaml`
- Identifier: `NCBITaxon:1414673`

## Target

Reviewed the complete 72-line YAML record for Rhizoctonia butinii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizoctonia_butinii.

## Validation

- `just validate data/taxa/eukaryota/rhizoctonia_butinii.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizoclosmatium_sp.yaml data/taxa/eukaryota/rhizoctonia_butinii.yaml data/taxa/eukaryota/rhizoctonia_endophytica.yaml data/taxa/eukaryota/rhizoctonia_rubi.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:350766`: `taxon_id` `NCBITaxon:1414673`, label `Rhizoctonia butinii`, rank `SPECIES`, parent `NCBITaxon:1322061`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, related synonym `Rhizoctonia butinii Oberw., R. Bauer, Garnica & R. Kirschner, 2013`, no exact or broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 60055, added `2026-09-12` with reason `attested rule: Rhizoctonia butinii, 2 sources incl. NCBI`.
- Checked all 13 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:1414673` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:10035` for `NCBITaxon:1414673` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 0 exact organism rows, and 0 exact project rows for this identifier.
- Confirmed one exact type-material row in `data/raw/ncbi_type_material.tsv` for `M:H Butin 11026`.
- Confirmed 0 exact local BacDive rows, 2 direct StrainInfo JSONL records, and 2 StrainInfo deposit entries carrying `NCBITaxon:1414673`.

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
