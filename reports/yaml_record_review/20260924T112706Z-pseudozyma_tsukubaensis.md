# YAML Record Review: Pseudozyma tsukubaensis

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudozyma_tsukubaensis.yaml`
- Identifier: `NCBITaxon:5483`

## Target

Reviewed the complete 78-line YAML record for Pseudozyma tsukubaensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudozyma_tsukubaensis`.

## Validation

- `just validate data/taxa/eukaryota/pseudozyma_tsukubaensis.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudozyma_flocculosa.yaml data/taxa/eukaryota/pseudozyma_hubeiensis.yaml data/taxa/eukaryota/pseudozyma_tsukubaensis.yaml data/taxa/eukaryota/psilocybe_cf_subviscida.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:2433` retains `NCBITaxon:5483` as `Pseudozyma tsukubaensis`, rank `SPECIES`, parent `NCBITaxon:63298`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:52010`, with reason `attested rule: Pseudozyma tsukubaensis, 2 sources incl. NCBI`.
- NCBI lists 3 exact synonyms, 1 related synonym, and 0 broad synonyms for the taxon, matching the 4 synonym assertions in the YAML.
- All 12 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:5483`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:38495` reports `organism_count: 1` for `NCBITaxon:5483`, matching the YAML source count.
- The native GOLD tables contain 1 organism row, 1 project row, and 1 analysis row for this taxon.
- NCBI has 19 type-material rows at `data/raw/ncbi_type_material.tsv:232950` through `data/raw/ncbi_type_material.tsv:232968`, all for `Candida tsukubaensis`, covering paired ATCC, CBS, DBVPG, IFO, IGC, JCM, MUCL, NCYC, and NRRL designations plus `NRRL:Y:7792`.
- Local StrainInfo records have 2 direct exact taxon rows and 12 exact deposit entries for `NCBITaxon:5483`; an exact numeric-boundary scan of `data/straininfo/records.jsonl.gz` found the same 2 direct records.
- BacDive has 0 exact local rows for `NCBITaxon:5483`.

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

The local exact strain evidence has not generated any strain overlay rows, leaving the YAML consistent with the generated source inventories.
