# YAML Record Review: Pyrenophora teres f. maculata

- Verdict: pass
- Target: `data/taxa/eukaryota/pyrenophora_teres_f_maculata.yaml`
- Identifier: `NCBITaxon:97480`

## Target

Reviewed the complete 87-line YAML record for Pyrenophora teres f. maculata. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for pyrenophora_teres_f_maculata.

## Validation

- `just validate data/taxa/eukaryota/pyrenophora_teres_f_maculata.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pycnoporus_sp_in_basidiomycete_fungi.yaml data/taxa/eukaryota/pyrenochaeta_sp.yaml data/taxa/eukaryota/pyrenophora_seminiperda_ccb06.yaml data/taxa/eukaryota/pyrenophora_teres_f_maculata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:16453`: `taxon_id` `NCBITaxon:97480`, label `Pyrenophora teres f. maculata`, rank `FORMA`, parent `NCBITaxon:53485`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, related synonym `Pyrenophora teres f. maculata Smed.-Pet., 1971`, no exact or broad synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 53585, added `2026-09-12` with reason `attested rule: Pyrenophora teres f. maculata, 2 sources incl. NCBI`.
- Checked all 18 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found 0 exact rows for `NCBITaxon:97480` in `data/raw/ncbi_merged_ids.tsv`; no old IDs are retained in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:45155` for `NCBITaxon:97480` with `organism_count` `1`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 1 exact analysis row, 1 exact organism row, and 1 exact project row for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 1 direct StrainInfo JSONL record carrying `NCBITaxon:97480` (`siID` 226864, DOI `10.60712/SI-ID226864.2`, line 169317), and 0 exact StrainInfo deposit records.

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
