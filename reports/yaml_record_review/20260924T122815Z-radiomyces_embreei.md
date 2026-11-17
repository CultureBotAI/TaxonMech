# YAML Record Review: Radiomyces embreei

- Verdict: pass
- Target: `data/taxa/eukaryota/radiomyces_embreei.yaml`
- Identifier: `NCBITaxon:64573`

## Target

Reviewed the complete 69-line YAML record for Radiomyces embreei. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for radiomyces_embreei.

## Validation

- `just validate data/taxa/eukaryota/radiomyces_embreei.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/quintaria_lignatilis.yaml data/taxa/eukaryota/radiomyces_embreei.yaml data/taxa/eukaryota/radiomyces_mexicanus.yaml data/taxa/eukaryota/radiomyces_spectabilis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:8193`: `taxon_id` `NCBITaxon:64573`, label `Radiomyces embreei`, rank `SPECIES`, parent `NCBITaxon:64560`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, related synonym `Radiomyces embreei R.K. Benj., 1960`, no exact or broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 53099, added `2026-09-12` with reason `attested rule: Radiomyces embreei, 2 sources incl. NCBI`.
- Checked all 12 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:64573` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:40343` for `NCBITaxon:64573` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 1 exact organism row, and 2 exact project rows for this identifier.
- Confirmed 13 exact type-material rows in `data/raw/ncbi_type_material.tsv`, spanning ATCC 13845, CBS 254.60, IMI 081586, NRRL 2839, RSA 914, and VKM F-1352 designation variants.
- Confirmed 0 exact local BacDive rows, 10 direct StrainInfo JSONL records, and 17 StrainInfo deposit entries carrying `NCBITaxon:64573`; the numeric-boundary StrainInfo scan found 10 JSONL rows total, matching the direct record count.

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
