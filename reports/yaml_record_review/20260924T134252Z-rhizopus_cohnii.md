# YAML Record Review: Rhizopus cohnii

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizopus_cohnii.yaml`
- Identifier: `NCBITaxon:2572697`

## Target

Reviewed the complete 72-line YAML record for Rhizopus cohnii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizopus_cohnii.

## Validation

- `just validate data/taxa/eukaryota/rhizopus_cohnii.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizopus_chungkuoensis.yaml data/taxa/eukaryota/rhizopus_circinans.yaml data/taxa/eukaryota/rhizopus_cohnii.yaml data/taxa/eukaryota/rhizopus_delemar.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:532257`: `taxon_id` `NCBITaxon:2572697`, label `Rhizopus cohnii`, rank `SPECIES`, parent `NCBITaxon:4842`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 0 exact synonyms, 1 related synonym, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 62847, added `2026-09-12` with reason `attested rule: Rhizopus cohnii, 2 sources incl. NCBI`.
- Checked all 13 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:2572697` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:23484` for `NCBITaxon:2572697` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 1 exact organism row, and 1 exact project row for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 10 direct StrainInfo JSONL records, and 13 StrainInfo deposit records carrying `NCBITaxon:2572697`; the numeric-boundary JSONL count found 13 exact lines, comprising 10 direct rows plus 3 non-direct rows with 3 exact deposits.

## Completeness

- Generated strain raw tables have no direct rows for this target in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, or `data/raw/strain_genome_records.tsv`.
- `data/raw/strain_related_records.tsv` has 8 exact GOLD related-record rows at lines 196040-196047 for `kgmicrobe.strain:bacdive_15464` and `Rhizopus cohnii NRRL 1517`; the anchored BacDive lookup showed that `kgmicrobe.strain:bacdive_15464` is filed under `NCBITaxon:1923`, not `NCBITaxon:2572697`.
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
