# YAML Record Review: Rhodotorula mucilaginosa

- Verdict: pass
- Target: `data/taxa/eukaryota/rhodotorula_mucilaginosa.yaml`
- Identifier: `NCBITaxon:5537`

## Target

Reviewed the complete 99-line YAML record for Rhodotorula mucilaginosa. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhodotorula_mucilaginosa.

## Validation

- `just validate data/taxa/eukaryota/rhodotorula_mucilaginosa.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhodotorula_glutinis.yaml data/taxa/eukaryota/rhodotorula_kratochvilovae.yaml data/taxa/eukaryota/rhodotorula_mucilaginosa.yaml data/taxa/eukaryota/rhodotorula_paludigena.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:2459`: `taxon_id` `NCBITaxon:5537`, label `Rhodotorula mucilaginosa`, rank `SPECIES`, parent `NCBITaxon:5533`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 7 exact synonyms, 4 related synonyms, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 52028, added `2026-09-12` with reason `attested rule: Rhodotorula mucilaginosa, 2 sources incl. NCBI`.
- Checked all 12 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 3 exact merged-ID rows mapping `NCBITaxon:1353776`, `NCBITaxon:5431`, and `NCBITaxon:5534` into `NCBITaxon:5537`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:38665` for `NCBITaxon:5537` with `organism_count` `17`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 13 exact analysis rows, 15 exact organism rows, and 24 exact project rows for this identifier.
- Confirmed 69 exact rows in `data/raw/ncbi_type_material.tsv`, spanning lines 234113-234181.
- Confirmed 0 exact local BacDive rows, 260 direct StrainInfo JSONL records, and 472 StrainInfo deposit records carrying `NCBITaxon:5537`; the numeric-boundary JSONL count found 261 exact lines, comprising 260 direct rows plus 1 non-direct row with 1 exact deposit.

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
