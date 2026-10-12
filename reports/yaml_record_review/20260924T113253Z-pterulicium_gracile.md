# YAML Record Review: Pterulicium gracile

- Verdict: pass
- Target: `data/taxa/eukaryota/pterulicium_gracile.yaml`
- Identifier: `NCBITaxon:1884261`

## Target

Reviewed the complete 100-line YAML record for Pterulicium gracile. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pterulicium_gracile`.

## Validation

- `just validate data/taxa/eukaryota/pterulicium_gracile.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pterulicium_gracile.yaml data/taxa/eukaryota/puccinia_arachidis.yaml data/taxa/eukaryota/puccinia_coronata_f_sp_avenae.yaml data/taxa/eukaryota/puccinia_graminis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:490365` retains `NCBITaxon:1884261` as `Pterulicium gracile`, rank `SPECIES`, parent `NCBITaxon:604075`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:61441`, with reason `attested rule: Pterulicium gracile, 2 sources incl. NCBI`.
- NCBI lists 4 exact synonyms, 5 related synonyms, and 0 broad synonyms for the taxon, matching the 9 synonym assertions in the YAML.
- All 14 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:1884261`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:16936` reports `organism_count: 1` for `NCBITaxon:1884261`, matching the YAML source count.
- The native GOLD tables contain 1 organism row, 2 project rows, and 0 analysis rows for this taxon.
- NCBI has 0 type-material rows for `NCBITaxon:1884261`.
- Local StrainInfo records have 6 direct exact taxon rows and 6 exact deposit entries for `NCBITaxon:1884261`; an exact numeric-boundary scan of `data/straininfo/records.jsonl.gz` found the same 6 direct records.
- BacDive has 0 exact local rows for `NCBITaxon:1884261`.

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

The exact StrainInfo rows remain local cache evidence only; no generated raw strain or overlay table currently contributes a missing strain assertion.
