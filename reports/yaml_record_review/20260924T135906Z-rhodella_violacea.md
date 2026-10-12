# YAML Record Review: Rhodella violacea

- Verdict: pass
- Target: `data/taxa/eukaryota/rhodella_violacea.yaml`
- Identifier: `NCBITaxon:2801`

## Target

Reviewed the complete 69-line YAML record for Rhodella violacea. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhodella_violacea.

## Validation

- `just validate data/taxa/eukaryota/rhodella_violacea.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizopus_sp.yaml data/taxa/eukaryota/rhizopus_sp_acetoinus.yaml data/taxa/eukaryota/rhizopus_stolonifer.yaml data/taxa/eukaryota/rhodella_violacea.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:1948`: `taxon_id` `NCBITaxon:2801`, label `Rhodella violacea`, rank `SPECIES`, parent `NCBITaxon:2800`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 2 exact synonyms, 3 related synonyms, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 51808, added `2026-09-12` with reason `attested rule: Rhodella violacea, 2 sources incl. NCBI`.
- Checked all 8 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found one exact merged-ID row at `data/raw/ncbi_merged_ids.tsv:74489`, mapping `NCBITaxon:38298` into `NCBITaxon:2801`; the exact anchored search found no retained `NCBITaxon:38298` row in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:26793` for `NCBITaxon:2801` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 1 exact organism row, and 0 exact project rows for this identifier.
- Confirmed 2 exact rows in `data/raw/ncbi_type_material.tsv`, with type-material designations `SAG 115.79` and `SAG:115.79`.
- Confirmed 0 exact local BacDive rows, 7 direct StrainInfo JSONL records, and 12 StrainInfo deposit records carrying `NCBITaxon:2801`.

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
