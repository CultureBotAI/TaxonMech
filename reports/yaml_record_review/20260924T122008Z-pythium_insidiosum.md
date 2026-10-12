# YAML Record Review: Pythium insidiosum

- Verdict: pass
- Target: `data/taxa/eukaryota/pythium_insidiosum.yaml`
- Identifier: `NCBITaxon:114742`

## Target

Reviewed the complete 64-line YAML record for Pythium insidiosum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for pythium_insidiosum.

## Validation

- `just validate data/taxa/eukaryota/pythium_insidiosum.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pythium_brassicae_nom_inval.yaml data/taxa/eukaryota/pythium_guiyangense.yaml data/taxa/eukaryota/pythium_insidiosum.yaml data/taxa/eukaryota/pythium_oligandrum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:20862`: `taxon_id` `NCBITaxon:114742`, label `Pythium insidiosum`, rank `SPECIES`, parent `NCBITaxon:4797`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, related synonym `Pythium insidiosum De Cock, L. Mend., A.A. Padhye, Ajello & Kaufman, 1987`, no exact or broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 53803, added `2026-09-12` with reason `attested rule: Pythium insidiosum, 2 sources incl. NCBI`.
- Checked all 10 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:114742` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:3004` for `NCBITaxon:114742` with `organism_count` `13`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 11 exact analysis rows, 11 exact organism rows, and 11 exact project rows for this identifier.
- Confirmed 4 exact type-material rows in `data/raw/ncbi_type_material.tsv`: `ATCC 58643`, `ATCC:58643`, `CBS 574.85`, and `CBS:574.85`.
- Confirmed 0 exact local BacDive rows, 22 direct StrainInfo JSONL records, and 32 StrainInfo deposit entries carrying `NCBITaxon:114742`; the numeric-boundary StrainInfo scan found 22 JSONL rows total, matching the direct record count.

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
