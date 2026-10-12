# YAML Record Review: Rhizoctonia solani

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizoctonia_solani.yaml`
- Identifier: `NCBITaxon:456999`

## Target

Reviewed the complete 76-line YAML record for Rhizoctonia solani. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizoctonia_solani.

## Validation

- `just validate data/taxa/eukaryota/rhizoctonia_solani.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizoctonia_solani.yaml data/taxa/eukaryota/rhizoctonia_solani_ag_1_ia.yaml data/taxa/eukaryota/rhizoctonia_solani_ag_3.yaml data/taxa/eukaryota/rhizodiscina_lignyota.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:102241`: `taxon_id` `NCBITaxon:456999`, label `Rhizoctonia solani`, rank `SPECIES`, parent `NCBITaxon:1322061`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, exact synonym `Rhizoctonia praticola`, related synonym `Rhizoctonia solani J.G. Kuhn, 1858`, no broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 55719, added `2026-09-12` with reason `attested rule: Rhizoctonia solani, 2 sources incl. NCBI`.
- Checked all 13 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:456999` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:36128` for `NCBITaxon:456999` with `organism_count` `55`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 17 exact analysis rows, 19 exact organism rows, and 20 exact project rows for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 453 direct StrainInfo JSONL records, and 523 StrainInfo deposit entries carrying `NCBITaxon:456999`.
- The numeric-boundary StrainInfo scan found 459 JSONL rows with exact `NCBITaxon:456999`: 453 direct rows plus 6 non-direct rows carrying exact deposits for CBS 590.66, CBS 337.34, MUCL 30267, CBS 329.84, DSM 903, and CBS 338.34.

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
