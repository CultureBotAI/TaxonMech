# YAML Record Review: Rhodotorula glutinis

- Verdict: pass
- Target: `data/taxa/eukaryota/rhodotorula_glutinis.yaml`
- Identifier: `NCBITaxon:5535`

## Target

Reviewed the complete 87-line YAML record for Rhodotorula glutinis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhodotorula_glutinis.

## Validation

- `just validate data/taxa/eukaryota/rhodotorula_glutinis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhodotorula_glutinis.yaml data/taxa/eukaryota/rhodotorula_kratochvilovae.yaml data/taxa/eukaryota/rhodotorula_mucilaginosa.yaml data/taxa/eukaryota/rhodotorula_paludigena.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:2458`: `taxon_id` `NCBITaxon:5535`, label `Rhodotorula glutinis`, rank `SPECIES`, parent `NCBITaxon:5533`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 1 exact synonym, 6 related synonyms, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 52027, added `2026-09-12` with reason `attested rule: Rhodotorula glutinis, 2 sources incl. NCBI`.
- Checked all 12 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 4 exact merged-ID rows mapping `NCBITaxon:1038012`, `NCBITaxon:1186046`, `NCBITaxon:1211294`, and `NCBITaxon:86833` into `NCBITaxon:5535`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:38659` for `NCBITaxon:5535` with `organism_count` `3`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 2 exact analysis rows, 3 exact organism rows, and 8 exact project rows for this identifier.
- Confirmed 31 exact rows in `data/raw/ncbi_type_material.tsv`, spanning lines 234063-234093.
- Confirmed 0 exact local BacDive rows, 72 direct StrainInfo JSONL records, and 122 StrainInfo deposit records carrying `NCBITaxon:5535`; the numeric-boundary JSONL count found 86 exact lines, comprising 72 direct rows plus 14 non-direct rows with 16 exact deposits.

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
