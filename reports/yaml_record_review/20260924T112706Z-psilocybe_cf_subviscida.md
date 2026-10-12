# YAML Record Review: Psilocybe cf. subviscida

- Verdict: pass
- Target: `data/taxa/eukaryota/psilocybe_cf_subviscida.yaml`
- Identifier: `NCBITaxon:2480587`

## Target

Reviewed the complete 71-line YAML record for Psilocybe cf. subviscida. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `psilocybe_cf_subviscida`.

## Validation

- `just validate data/taxa/eukaryota/psilocybe_cf_subviscida.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudozyma_flocculosa.yaml data/taxa/eukaryota/pseudozyma_hubeiensis.yaml data/taxa/eukaryota/pseudozyma_tsukubaensis.yaml data/taxa/eukaryota/psilocybe_cf_subviscida.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:525828` retains `NCBITaxon:2480587` as `Psilocybe cf. subviscida`, rank `SPECIES`, parent `NCBITaxon:71950`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:62583`, with reason `attested rule: Psilocybe cf. subviscida, 2 sources incl. NCBI`.
- NCBI lists 0 exact synonyms, 0 related synonyms, and 0 broad synonyms for the taxon, matching the absence of a synonym block in the YAML.
- All 14 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:2480587`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:22227` reports `organism_count: 1` for `NCBITaxon:2480587`, matching the YAML source count.
- The native GOLD tables contain 1 organism row, 1 project row, and 1 analysis row for this taxon.
- NCBI has 0 type-material rows for `NCBITaxon:2480587`.
- Local StrainInfo records have 0 direct exact taxon rows and 0 exact deposit rows for `NCBITaxon:2480587`.
- BacDive has 0 exact local rows for `NCBITaxon:2480587`.

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

The record is a straightforward GOLD-attested, no-strain Psilocybe placeholder with no auxiliary evidence or merged-ID residue requiring additional YAML assertions.
