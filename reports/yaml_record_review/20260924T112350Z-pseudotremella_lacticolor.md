# YAML Record Review: Pseudotremella lacticolor

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudotremella_lacticolor.yaml`
- Identifier: `NCBITaxon:1336424`

## Target

Reviewed the complete 75-line YAML record for Pseudotremella lacticolor. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudotremella_lacticolor`.

## Validation

- `just validate data/taxa/eukaryota/pseudotremella_lacticolor.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudotaeniolina_sp.yaml data/taxa/eukaryota/pseudotremella_lacticolor.yaml data/taxa/eukaryota/pseudotulostoma_volvatum.yaml data/taxa/eukaryota/pseudovirgaria_hyperparasitica.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:320235` retains `NCBITaxon:1336424` as `Pseudotremella lacticolor`, rank `SPECIES`, parent `NCBITaxon:1909752`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:59524`, with reason `attested rule: Pseudotremella lacticolor, 2 sources incl. NCBI`.
- NCBI lists 1 exact synonym, 2 related synonyms, and 0 broad synonyms for the taxon: `Cryptococcus lacticolor` as exact, plus `Pseudotremella lacticolor Satoh & Makimura ex Yurkov, 2020` and `Tremella sp. yayoi-2008` as related.
- All 12 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- `data/raw/ncbi_merged_ids.tsv:82105` retires `NCBITaxon:498027` into `NCBITaxon:1336424`, but that old ID is absent from retained NCBI taxon rows and does not require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:8160` reports `organism_count: 5` for `NCBITaxon:1336424`, matching the YAML source count.
- The native GOLD tables contain 5 organism rows, 0 project rows, and 0 analysis rows for this taxon.
- NCBI has 9 type-material rows at `data/raw/ncbi_type_material.tsv:23728` through `data/raw/ncbi_type_material.tsv:23736`: culture-from-holotype designations `CBS 10915`, `CBS:10915`, `DSM 21093`, `DSM:21093`, `JCM 15449`, and `JCM:15449`; holotype designations `TIMM 10013` and `TIMM:10013`; and type-material designation `yayoi`.
- Local StrainInfo records have 1 direct exact taxon row, `siID 405725`, DOI `10.60712/SI-ID405725.2`, and 1 exact type-strain deposit row for `DSM 21093`.
- BacDive has 0 exact local rows for `NCBITaxon:1336424`.

## Completeness

- Generated raw strain tables contain 0 target rows across `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary generated sources contain 0 target rows across BactoTraits, GTDB mappings, GTDB species, LPSN, Madin, and MediaDive.
- Generated StrainInfo overlays contain 0 rows across `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- The StrainInfo evidence is represented only in the local exact-record cache, so the YAML correctly carries `strain_count: 0`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The raw type-material and StrainInfo evidence is limited to type-strain designations that have not produced a generated strain overlay row, so the reviewed record remains GOLD-only.
