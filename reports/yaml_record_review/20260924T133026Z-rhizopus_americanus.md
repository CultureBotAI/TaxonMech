# YAML Record Review: Rhizopus americanus

- Verdict: pass
- Target: `data/taxa/eukaryota/rhizopus_americanus.yaml`
- Identifier: `NCBITaxon:235392`

## Target

Reviewed the complete 79-line YAML record for Rhizopus americanus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for rhizopus_americanus.

## Validation

- `just validate data/taxa/eukaryota/rhizopus_americanus.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/rhizopus_americanus.yaml data/taxa/eukaryota/rhizopus_arrhizus.yaml data/taxa/eukaryota/rhizopus_arrhizus_99_133.yaml data/taxa/eukaryota/rhizopus_arrhizus_99_892.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:46326`: `taxon_id` `NCBITaxon:235392`, label `Rhizopus americanus`, rank `SPECIES`, parent `NCBITaxon:4842`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 1 exact synonym, 2 related synonyms, 0 broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 54682, added `2026-09-12` with reason `attested rule: Rhizopus americanus, 2 sources incl. NCBI`.
- Checked all 13 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:235392` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:21874` for `NCBITaxon:235392` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 0 exact analysis rows, 1 exact organism row, and 1 exact project row for this identifier.
- Confirmed all 6 exact rows in `data/raw/ncbi_type_material.tsv`, at lines 93464-93469, carrying type-material designations for `CBS 340.62`, `IMI 209090`, and `NRRL 2626` variants under `Rhizopus sexualis var. americanus`.
- Confirmed 0 exact local BacDive rows, 1 direct StrainInfo JSONL record by numeric-boundary count, and 7 StrainInfo deposit records carrying `NCBITaxon:235392`.

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
