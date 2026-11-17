# YAML Record Review: Pseudozyma hubeiensis

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudozyma_hubeiensis.yaml`
- Identifier: `NCBITaxon:327079`

## Target

Reviewed the complete 69-line YAML record for Pseudozyma hubeiensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudozyma_hubeiensis`.

## Validation

- `just validate data/taxa/eukaryota/pseudozyma_hubeiensis.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudozyma_flocculosa.yaml data/taxa/eukaryota/pseudozyma_hubeiensis.yaml data/taxa/eukaryota/pseudozyma_tsukubaensis.yaml data/taxa/eukaryota/psilocybe_cf_subviscida.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:66862` retains `NCBITaxon:327079` as `Pseudozyma hubeiensis`, rank `SPECIES`, parent `NCBITaxon:63298`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:55229`, with reason `attested rule: Pseudozyma hubeiensis, 2 sources incl. NCBI`.
- NCBI lists 0 exact synonyms, 1 related synonym, and 0 broad synonyms for the taxon: `Pseudozyma hubeiensis F.Y. Bai & Q.M. Wang, 2006` as related.
- All 12 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:327079`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:32182` reports `organism_count: 2` for `NCBITaxon:327079`, matching the YAML source count.
- The native GOLD tables contain 2 organism rows, 2 project rows, and 2 analysis rows for this taxon.
- NCBI has 8 type-material rows at `data/raw/ncbi_type_material.tsv:177664` through `data/raw/ncbi_type_material.tsv:177671`: culture-from-holotype designations `AS 2.2493`, `AS 2.2493 (ex-type)`, `AS:2.2493`, `AS:2.2493 (ex-type)`, `CGMCC 2.2493`, and `CGMCC:2.2493`, plus type-material designations `CBS 10077` and `CBS:10077`.
- Local StrainInfo records have 4 direct exact taxon rows and 9 exact deposit entries for `NCBITaxon:327079`; an exact numeric-boundary scan of `data/straininfo/records.jsonl.gz` found the same 4 direct records.
- BacDive has 0 exact local rows for `NCBITaxon:327079`.

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

The StrainInfo exact rows and NCBI type-material designations are present only in local raw/cache sources and do not indicate any missing generated strain assertion.
