# YAML Record Review: Retiboletus ornatipes

- Verdict: pass
- Target: `data/taxa/eukaryota/retiboletus_ornatipes.yaml`
- Identifier: `NCBITaxon:1282276`

## Target

Reviewed the complete 87-line YAML record for Retiboletus ornatipes. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for retiboletus_ornatipes.

## Validation

- `just validate data/taxa/eukaryota/retiboletus_ornatipes.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/remersonia_thermophila.yaml data/taxa/eukaryota/reniforma_strues.yaml data/taxa/eukaryota/resinicium_bicolor.yaml data/taxa/eukaryota/retiboletus_ornatipes.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:299722`: `taxon_id` `NCBITaxon:1282276`, label `Retiboletus ornatipes`, rank `SPECIES`, parent `NCBITaxon:889442`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, exact synonym `Boletus ornatipes`, 3 related synonyms, no broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 58900, added `2026-09-12` with reason `attested rule: Retiboletus ornatipes, 2 sources incl. NCBI`.
- Checked all 15 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found one exact row in `data/raw/ncbi_merged_ids.tsv` mapping old `NCBITaxon:182631` to current `NCBITaxon:1282276`; exact grep found no retained old row in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:6570` for `NCBITaxon:1282276` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 1 exact analysis row, 1 exact organism row, and 1 exact project row for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 2 direct StrainInfo JSONL records, and 2 StrainInfo deposit entries carrying `NCBITaxon:1282276`.

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
