# YAML Record Review: Rhizopus arrhizus Type I NRRL 21789

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizopus_arrhizus_type_i_nrrl_21789.yaml`
- Identifier: `NCBITaxon:1279479`

## Target

Reviewed the complete 71-line YAML record for Rhizopus arrhizus Type I NRRL 21789. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizopus_arrhizus_type_i_nrrl_21789.

## Validation

- `just validate data/taxa/eukaryota/rhizopus_arrhizus_type_i_nrrl_21789.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizopus_arrhizus_type_i_nrrl_21396.yaml data/taxa/eukaryota/rhizopus_arrhizus_type_i_nrrl_21789.yaml data/taxa/eukaryota/rhizopus_artocarpi.yaml data/taxa/eukaryota/rhizopus_azygosporus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:298846`: `taxon_id` `NCBITaxon:1279479`, label `Rhizopus arrhizus Type I NRRL 21789`, rank `STRAIN`, parent `NCBITaxon:64495`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 0 exact synonyms, 0 related synonyms, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 58882, added `2026-09-12` with reason `attested rule: Rhizopus arrhizus Type I NRRL 21789, 2 sources incl. NCBI`.
- Checked all 14 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:1279479` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:6518` for `NCBITaxon:1279479` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 1 exact analysis row, 1 exact organism row, and 1 exact project row for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 0 direct StrainInfo JSONL records, and 0 StrainInfo deposit records carrying `NCBITaxon:1279479`.

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
