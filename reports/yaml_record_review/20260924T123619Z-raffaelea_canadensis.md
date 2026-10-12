# YAML Record Review: Raffaelea canadensis

- Verdict: pass
- Target: `data/taxa/eukaryota/raffaelea_canadensis.yaml`
- Identifier: `NCBITaxon:45347`

## Target

Reviewed the complete 87-line YAML record for Raffaelea canadensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for raffaelea_canadensis.

## Validation

- `just validate data/taxa/eukaryota/raffaelea_canadensis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/raffaelea_canadensis.yaml data/taxa/eukaryota/raffaelea_gnathotrichi.yaml data/taxa/eukaryota/raffaelea_tritirachium.yaml data/taxa/eukaryota/ramalina_intermedia.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:5540`: `taxon_id` `NCBITaxon:45347`, label `Raffaelea canadensis`, rank `SPECIES`, parent `NCBITaxon:45340`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, exact synonym `Ambrosiella sulcati`, 2 related synonyms, no broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 52615, added `2026-09-12` with reason `attested rule: Raffaelea canadensis, 2 sources incl. NCBI`.
- Checked all 16 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found one exact row in `data/raw/ncbi_merged_ids.tsv` mapping old `NCBITaxon:44381` to current `NCBITaxon:45347`; exact grep found no retained old row in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:35929` for `NCBITaxon:45347` with `organism_count` `4`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 4 exact organism rows, and 0 exact project rows for this identifier.
- Confirmed 6 exact type-material rows in `data/raw/ncbi_type_material.tsv`, spanning ATCC 22211, CBS 805.70, and DSM 1364 designation variants.
- Confirmed 0 exact local BacDive rows, 3 direct StrainInfo JSONL records, and 7 StrainInfo deposit entries carrying `NCBITaxon:45347`; the numeric-boundary StrainInfo scan found 3 JSONL rows total, matching the direct record count.

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
