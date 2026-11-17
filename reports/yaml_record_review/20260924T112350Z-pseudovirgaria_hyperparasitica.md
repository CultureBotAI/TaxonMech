# YAML Record Review: Pseudovirgaria hyperparasitica

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudovirgaria_hyperparasitica.yaml`
- Identifier: `NCBITaxon:470096`

## Target

Reviewed the complete 82-line YAML record for Pseudovirgaria hyperparasitica. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudovirgaria_hyperparasitica`.

## Validation

- `just validate data/taxa/eukaryota/pseudovirgaria_hyperparasitica.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudotaeniolina_sp.yaml data/taxa/eukaryota/pseudotremella_lacticolor.yaml data/taxa/eukaryota/pseudotulostoma_volvatum.yaml data/taxa/eukaryota/pseudovirgaria_hyperparasitica.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:104943` retains `NCBITaxon:470096` as `Pseudovirgaria hyperparasitica`, rank `SPECIES`, parent `NCBITaxon:470095`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:55764`, with reason `attested rule: Pseudovirgaria hyperparasitica, 2 sources incl. NCBI`.
- NCBI lists 0 exact synonyms, 1 related synonym, and 0 broad synonyms for the taxon: `Pseudovirgaria hyperparasitica H.D. Shin, U. Braun, Arzanlou & Crous, 2007` as related.
- All 16 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:470096`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:36414` reports `organism_count: 2` for `NCBITaxon:470096`, matching the YAML source count.
- The native GOLD tables contain 1 organism row, 2 project rows, and 1 analysis row for this taxon.
- NCBI has 6 holotype rows at `data/raw/ncbi_type_material.tsv:218247` through `data/raw/ncbi_type_material.tsv:218252`: `CBS 121739`, `CBS 121740`, `CBS 121741`, `CBS:121739`, `CBS:121740`, and `CBS:121741`.
- Local StrainInfo records have 0 direct exact taxon rows and 0 exact deposit rows for `NCBITaxon:470096`.
- BacDive has 0 exact local rows for `NCBITaxon:470096`.

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

The local raw evidence does not surface any generated strain, auxiliary, BacDive, StrainInfo overlay, or merged-ID assertion that is missing from the YAML.
