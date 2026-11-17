# YAML Record Review: Pyricularia grisea

- Verdict: pass
- Target: `data/taxa/eukaryota/pyricularia_grisea.yaml`
- Identifier: `NCBITaxon:148305`

## Target

Reviewed the complete 87-line YAML record for Pyricularia grisea. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for pyricularia_grisea.

## Validation

- `just validate data/taxa/eukaryota/pyricularia_grisea.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pyrenophora_teres_f_teres.yaml data/taxa/eukaryota/pyrenophora_tritici_repentis.yaml data/taxa/eukaryota/pyricularia_grisea.yaml data/taxa/eukaryota/pyricularia_oryzae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:30358`: `taxon_id` `NCBITaxon:148305`, label `Pyricularia grisea`, rank `SPECIES`, parent `NCBITaxon:48558`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 2 exact synonyms, 1 related synonym, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 54055, added `2026-09-12` with reason `attested rule: Pyricularia grisea, 2 sources incl. NCBI`.
- Checked all 16 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found four exact rows in `data/raw/ncbi_merged_ids.tsv` mapping old IDs `NCBITaxon:29878`, `NCBITaxon:41252`, `NCBITaxon:5138`, and `NCBITaxon:89476` to current `NCBITaxon:148305`; exact greps found no retained old rows in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:11481` for `NCBITaxon:148305` with `organism_count` `5`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 5 exact analysis rows, 6 exact organism rows, and 6 exact project rows for this identifier.
- Confirmed 6 exact type-material rows in `data/raw/ncbi_type_material.tsv`: holotype designations `BPI 625033` and `BPI:625033`, culture-from-epitype designations `CBS 138707` and `CBS:138707`, and epitype designations `CBS H-22280` and `CBS:H-22280`.
- Confirmed 0 exact local BacDive rows, 206 direct StrainInfo JSONL records, and 222 StrainInfo deposit entries carrying `NCBITaxon:148305`. The numeric-boundary StrainInfo scan found 207 JSONL rows total; the extra deposit-only row is line 63913, where direct taxon `Pyricularia oryzae`/`NCBITaxon:318829` carries deposit `ICMP 14699` as `Magnaporthe grisea`/`NCBITaxon:148305`.

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
