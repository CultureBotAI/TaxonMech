# YAML Record Review: Pteridomonas danica

- Verdict: pass
- Target: `data/taxa/eukaryota/pteridomonas_danica.yaml`
- Identifier: `NCBITaxon:38822`

## Target

Reviewed the complete 60-line YAML record for Pteridomonas danica. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pteridomonas_danica`.

## Validation

- `just validate data/taxa/eukaryota/pteridomonas_danica.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/psilocybe_cubensis.yaml data/taxa/eukaryota/psilocybe_cyanescens.yaml data/taxa/eukaryota/psilocybe_subaeruginosa.yaml data/taxa/eukaryota/pteridomonas_danica.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:4419` retains `NCBITaxon:38822` as `Pteridomonas danica`, rank `SPECIES`, parent `NCBITaxon:38821`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:52398`, with reason `attested rule: Pteridomonas danica, 2 sources incl. NCBI`.
- NCBI lists 0 exact synonyms, 1 related synonym, and 0 broad synonyms for the taxon: `Pteridomonas danica Patterson & Fenchel` as related.
- All 9 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:38822`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:34046` reports `organism_count: 1` for `NCBITaxon:38822`, matching the YAML source count.
- The native GOLD tables contain 1 organism row, 0 project rows, and 0 analysis rows for this taxon.
- NCBI has 0 type-material rows for `NCBITaxon:38822`.
- Local StrainInfo records have 2 direct exact taxon rows and 2 exact deposit entries for `NCBITaxon:38822`.
- BacDive has 0 exact local rows for `NCBITaxon:38822`.

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

The Stramenopiles lineage and local exact evidence are internally consistent, and no generated source contributes a missing strain or auxiliary assertion.
