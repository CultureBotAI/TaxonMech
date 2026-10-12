# YAML Record Review: Rhizopogon vinicolor

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizopogon_vinicolor.yaml`
- Identifier: `NCBITaxon:80600`

## Target

Reviewed the complete 75-line YAML record for Rhizopogon vinicolor. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizopogon_vinicolor.

## Validation

- `just validate data/taxa/eukaryota/rhizopogon_vinicolor.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizopogon_vesiculosus.yaml data/taxa/eukaryota/rhizopogon_villosulus.yaml data/taxa/eukaryota/rhizopogon_vinicolor.yaml data/taxa/eukaryota/rhizopogon_vulgaris.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:12051`: `taxon_id` `NCBITaxon:80600`, label `Rhizopogon vinicolor`, rank `SPECIES`, parent `NCBITaxon:5375`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 0 exact synonyms, 1 related synonym, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 53350, added `2026-09-12` with reason `attested rule: Rhizopogon vinicolor, 2 sources incl. NCBI`.
- Checked all 14 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:80600` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:42876` for `NCBITaxon:80600` with `organism_count` `6`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 6 exact analysis rows, 6 exact organism rows, and 6 exact project rows for this identifier.
- Confirmed all 5 exact rows in `data/raw/ncbi_type_material.tsv`, at lines 265266-265270, carrying holotype designations `MICH, leg E. Trueblood 2195`, `VINRHI2195`, and `VINRHI:2195`, plus type-material designations `MICH Trueblood 2195` and `MICH:collector:Trueblood:2195`.
- Confirmed 0 exact local BacDive rows, 3 direct StrainInfo JSONL records, and 3 StrainInfo deposit records carrying `NCBITaxon:80600`.

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
