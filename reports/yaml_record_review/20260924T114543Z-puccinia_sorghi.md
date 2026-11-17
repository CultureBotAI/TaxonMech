# YAML Record Review: Puccinia sorghi

- Verdict: pass
- Target: `data/taxa/eukaryota/puccinia_sorghi.yaml`
- Identifier: `NCBITaxon:27349`

## Target

Reviewed the complete 69-line YAML record for Puccinia sorghi. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `puccinia_sorghi`.

## Validation

- `just validate data/taxa/eukaryota/puccinia_sorghi.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/puccinia_graminis_f_sp_tritici_uvpgt59.yaml data/taxa/eukaryota/puccinia_horiana.yaml data/taxa/eukaryota/puccinia_sorghi.yaml data/taxa/eukaryota/puccinia_striiformis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:2747` retains `NCBITaxon:27349` as `Puccinia sorghi`, rank `SPECIES`, parent `NCBITaxon:5296`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:52161`, with reason `attested rule: Puccinia sorghi, 2 sources incl. NCBI`.
- NCBI lists 0 exact synonyms, 1 related synonym, and 0 broad synonyms for the taxon: `Puccinia sorghi Schwein., 1832` as related.
- All 12 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:27349`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:25497` reports `organism_count: 1` for `NCBITaxon:27349`, matching the YAML source count.
- The native GOLD tables contain 1 organism row, 1 project row, and 1 analysis row for this taxon.
- NCBI has 0 type-material rows for `NCBITaxon:27349`.
- Local StrainInfo records have 0 direct exact taxon rows and 0 exact deposit rows for `NCBITaxon:27349`.
- BacDive has 0 exact local rows for `NCBITaxon:27349`.

## Completeness

- Generated raw strain tables contain 0 target rows across `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary generated sources contain 0 target rows across BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive.
- Generated StrainInfo overlays contain 0 rows across `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- The YAML correctly carries `strain_count: 0`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

No auxiliary, type-material, BacDive, StrainInfo, or merged-ID evidence surfaced beyond the direct NCBI and GOLD rows.
