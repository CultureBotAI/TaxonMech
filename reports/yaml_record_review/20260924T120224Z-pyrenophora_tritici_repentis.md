# YAML Record Review: Pyrenophora tritici-repentis

- Verdict: pass
- Target: `data/taxa/eukaryota/pyrenophora_tritici_repentis.yaml`
- Identifier: `NCBITaxon:45151`

## Target

Reviewed the complete 105-line YAML record for Pyrenophora tritici-repentis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for pyrenophora_tritici_repentis.

## Validation

- `just validate data/taxa/eukaryota/pyrenophora_tritici_repentis.yaml` exited with `No issues found`.
- `just validate-strict data/taxa/eukaryota/pyrenophora_teres_f_teres.yaml data/taxa/eukaryota/pyrenophora_tritici_repentis.yaml data/taxa/eukaryota/pyricularia_grisea.yaml data/taxa/eukaryota/pyricularia_oryzae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- Retained the exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:5496`: `taxon_id` `NCBITaxon:45151`, label `Pyrenophora tritici-repentis`, rank `SPECIES`, parent `NCBITaxon:5027`, genetic code `1`, taxonomy snapshot `2026-09-13`, `attested_by` `gold`, 3 exact synonyms, 5 related synonyms, and no `retired_into` value.
- Confirmed the identifier remains in seed scope through one `data/seed/scope.tsv` row at line 52606, added `2026-09-12` with reason `attested rule: Pyrenophora tritici-repentis, 2 sources incl. NCBI`.
- Checked all 17 lineage assertions against local NCBI rows and found 0 missing ancestors and 0 parent mismatches.
- Found three exact rows in `data/raw/ncbi_merged_ids.tsv` mapping old IDs `NCBITaxon:132100`, `NCBITaxon:469969`, and `NCBITaxon:475175` to current `NCBITaxon:45151`; exact greps found no retained old rows in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly omits `replaces`.

## Evidence

- Confirmed one GOLD aggregate row at `data/raw/gold_organisms.tsv:35869` for `NCBITaxon:45151` with `organism_count` `51`, matching the YAML GOLD source assertion count.
- Native GOLD files contain 48 exact analysis rows, 51 exact organism rows, and 51 exact project rows for this identifier.
- Confirmed 0 exact rows in `data/raw/ncbi_type_material.tsv`.
- Confirmed 0 exact local BacDive rows, 21 direct StrainInfo JSONL records, and 22 StrainInfo deposit entries carrying `NCBITaxon:45151`. The numeric-boundary StrainInfo scan found 22 JSONL rows total; the extra deposit-only row is line 62573, where direct taxon `Pyrenophora`/`NCBITaxon:5027` carries deposit `CBS 259.59` as `Drechslera tritici-repentis`/`NCBITaxon:45151`.

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
