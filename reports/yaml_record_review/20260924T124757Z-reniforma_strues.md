# YAML Record Review: Reniforma strues

- Verdict: pass
- Target: `data/taxa/eukaryota/reniforma_strues.yaml`
- Identifier: `NCBITaxon:106000`

## Target

Reviewed the complete 66-line YAML record for Reniforma strues. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for reniforma_strues.

## Validation

- `just validate data/taxa/eukaryota/reniforma_strues.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/remersonia_thermophila.yaml data/taxa/eukaryota/reniforma_strues.yaml data/taxa/eukaryota/resinicium_bicolor.yaml data/taxa/eukaryota/retiboletus_ornatipes.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:19038`: `taxon_id` `NCBITaxon:106000`, label `Reniforma strues`, rank `SPECIES`, parent `NCBITaxon:105999`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, related synonym `Reniforma strues Pore & Sorenson, 1990`, no exact or broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 53708, added `2026-09-12` with reason `attested rule: Reniforma strues, 2 sources incl. NCBI`.
- Checked all 11 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:106000` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:1091` for `NCBITaxon:106000` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 0 exact organism rows, and 0 exact project rows for this identifier.
- Confirmed 7 exact type-material rows in `data/raw/ncbi_type_material.tsv`, spanning CBS 8263, ATCC 66374, and NRRL Y-17275 designation variants.
- Confirmed 0 exact local BacDive rows, 1 direct StrainInfo JSONL record, and 5 StrainInfo deposit entries carrying `NCBITaxon:106000`.

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
