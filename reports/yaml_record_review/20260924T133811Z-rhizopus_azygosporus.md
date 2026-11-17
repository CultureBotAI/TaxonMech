# YAML Record Review: Rhizopus azygosporus

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizopus_azygosporus.yaml`
- Identifier: `NCBITaxon:86630`

## Target

Reviewed the complete 75-line YAML record for Rhizopus azygosporus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizopus_azygosporus.

## Validation

- `just validate data/taxa/eukaryota/rhizopus_azygosporus.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizopus_arrhizus_type_i_nrrl_21396.yaml data/taxa/eukaryota/rhizopus_arrhizus_type_i_nrrl_21789.yaml data/taxa/eukaryota/rhizopus_artocarpi.yaml data/taxa/eukaryota/rhizopus_azygosporus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:13418`: `taxon_id` `NCBITaxon:86630`, label `Rhizopus azygosporus`, rank `SPECIES`, parent `NCBITaxon:4842`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 1 exact synonym, 1 related synonym, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 53442, added `2026-09-12` with reason `attested rule: Rhizopus azygosporus, 2 sources incl. NCBI`.
- Checked all 13 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Exact old-ID greps found one row in `data/raw/ncbi_merged_ids.tsv` merging `NCBITaxon:983148` into `NCBITaxon:86630`, and found no retained old-ID row in `data/raw/ncbitaxon_taxa.tsv`; the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:43481` for `NCBITaxon:86630` with `organism_count` `5`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 1 exact analysis row, 4 exact organism rows, and 5 exact project rows for this identifier.
- Confirmed all 4 exact rows in `data/raw/ncbi_type_material.tsv`, at lines 269334-269337, carrying culture-from-type-material designations `CBS 357.93` and `CBS:357.93`, plus type-material designations `ATCC 48108` and `ATCC:48108`.
- Confirmed 0 exact local BacDive rows, 6 direct StrainInfo JSONL records by numeric-boundary count, and 15 StrainInfo deposit records carrying `NCBITaxon:86630`.

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
