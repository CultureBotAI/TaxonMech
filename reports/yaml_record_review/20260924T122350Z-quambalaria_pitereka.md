# YAML Record Review: Quambalaria pitereka

- Verdict: pass
- Target: `data/taxa/eukaryota/quambalaria_pitereka.yaml`
- Identifier: `NCBITaxon:363178`

## Target

Reviewed the complete 75-line YAML record for Quambalaria pitereka. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for quambalaria_pitereka.

## Validation

- `just validate data/taxa/eukaryota/quambalaria_pitereka.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pythium_periplocum.yaml data/taxa/eukaryota/pyxidiophora_arvernensis.yaml data/taxa/eukaryota/pyxidiophora_hyalina.yaml data/taxa/eukaryota/quambalaria_pitereka.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:75810`: `taxon_id` `NCBITaxon:363178`, label `Quambalaria pitereka`, rank `SPECIES`, parent `NCBITaxon:218126`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, exact synonym `Ramularia pitereka`, 2 related synonyms, no broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 55360, added `2026-09-12` with reason `attested rule: Quambalaria pitereka, 2 sources incl. NCBI`.
- Checked all 12 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:363178` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:33325` for `NCBITaxon:363178` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 1 exact organism row, and 1 exact project row for this identifier.
- Confirmed 3 exact holotype rows in `data/raw/ncbi_type_material.tsv`: `DAR 19773`, `DAR19773`, and `DAR:19773`.
- Confirmed 0 exact local BacDive rows, 0 direct StrainInfo JSONL records, and 0 StrainInfo deposit records carrying `NCBITaxon:363178`.

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
