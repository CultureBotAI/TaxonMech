# YAML Record Review: Rhizopus arrhizus

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizopus_arrhizus.yaml`
- Identifier: `NCBITaxon:64495`

## Target

Reviewed the complete 164-line YAML record for Rhizopus arrhizus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizopus_arrhizus.

## Validation

- `just validate data/taxa/eukaryota/rhizopus_arrhizus.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizopus_americanus.yaml data/taxa/eukaryota/rhizopus_arrhizus.yaml data/taxa/eukaryota/rhizopus_arrhizus_99_133.yaml data/taxa/eukaryota/rhizopus_arrhizus_99_892.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:8167`: `taxon_id` `NCBITaxon:64495`, label `Rhizopus arrhizus`, rank `SPECIES`, parent `NCBITaxon:4842`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 17 exact synonyms, 14 related synonyms, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 53080, added `2026-09-12` with reason `attested rule: Rhizopus arrhizus, 2 sources incl. NCBI`.
- Checked all 13 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Exact old-ID greps found 5 rows in `data/raw/ncbi_merged_ids.tsv` merging `NCBITaxon:126589`, `NCBITaxon:1810496`, `NCBITaxon:2072830`, `NCBITaxon:29925`, and `NCBITaxon:4845` into `NCBITaxon:64495`, and found no retained old-ID rows in `data/raw/ncbitaxon_taxa.tsv`; the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:40306` for `NCBITaxon:64495` with `organism_count` `152`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 36 exact analysis rows, 147 exact organism rows, and 148 exact project rows for this identifier.
- Confirmed all 16 exact rows in `data/raw/ncbi_type_material.tsv`, at lines 244328-244343, spanning 3 `Rhizopus arrhizus` culture-from-neotype rows and 13 `Rhizopus oryzae` culture-from-type-material or type-material rows.
- Confirmed 0 exact local BacDive rows, 485 direct StrainInfo JSONL records, and 982 StrainInfo deposit records carrying `NCBITaxon:64495`; the numeric-boundary JSONL count found 487 lines, explained by 485 direct rows plus 2 non-direct `Rhizopus microsporus` rows with exact `Rhizopus oryzae` deposits.

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
