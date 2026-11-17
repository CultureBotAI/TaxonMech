# YAML Record Review: Rhizomucor pusillus

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizomucor_pusillus.yaml`
- Identifier: `NCBITaxon:4840`

## Target

Reviewed the complete 75-line YAML record for Rhizomucor pusillus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizomucor_pusillus.

## Validation

- `just validate data/taxa/eukaryota/rhizomucor_pusillus.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizomucor_miehei.yaml data/taxa/eukaryota/rhizomucor_pusillus.yaml data/taxa/eukaryota/rhizophagus_clarus.yaml data/taxa/eukaryota/rhizophagus_intraradices.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:2089`: `taxon_id` `NCBITaxon:4840`, label `Rhizomucor pusillus`, rank `SPECIES`, parent `NCBITaxon:4838`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, exact synonym `Mucor pusillus`, 2 related synonyms, no broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 51856, added `2026-09-12` with reason `attested rule: Rhizomucor pusillus, 2 sources incl. NCBI`.
- Checked all 12 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:4840` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:36835` for `NCBITaxon:4840` with `organism_count` `12`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 12 exact organism rows, and 12 exact project rows for this identifier.
- Confirmed 6 exact culture-from-type-material rows in `data/raw/ncbi_type_material.tsv`, spanning ATCC 46342, CBS 354.68, and NRRL 3639 designation variants.
- Confirmed 0 exact local BacDive rows, 91 direct StrainInfo JSONL records, and 137 StrainInfo deposit entries carrying `NCBITaxon:4840`.
- The numeric-boundary StrainInfo scan found 93 JSONL rows with exact `NCBITaxon:4840`: 91 direct rows plus 2 non-direct rows carrying exact deposits for ATCC 46033, NRRL 3638, CBS 253.53, and IMI 226172.

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
