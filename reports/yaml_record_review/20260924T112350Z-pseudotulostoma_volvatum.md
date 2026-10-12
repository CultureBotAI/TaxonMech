# YAML Record Review: Pseudotulostoma volvatum

- Verdict: pass
- Target: `data/taxa/eukaryota/pseudotulostoma_volvatum.yaml`
- Identifier: `NCBITaxon:144541`

## Target

Reviewed the complete 78-line YAML record for Pseudotulostoma volvatum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pseudotulostoma_volvatum`.

## Validation

- `just validate data/taxa/eukaryota/pseudotulostoma_volvatum.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pseudotaeniolina_sp.yaml data/taxa/eukaryota/pseudotremella_lacticolor.yaml data/taxa/eukaryota/pseudotulostoma_volvatum.yaml data/taxa/eukaryota/pseudovirgaria_hyperparasitica.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:29170` retains `NCBITaxon:144541` as `Pseudotulostoma volvatum`, rank `SPECIES`, parent `NCBITaxon:144540`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:54026`, with reason `attested rule: Pseudotulostoma volvatum, 2 sources incl. NCBI`.
- NCBI lists 1 exact synonym, 0 related synonyms, and 0 broad synonyms for the taxon: `Pseudotulostoma volvatum O.K. Mill. & T.W. Henkel, 2001` as exact.
- All 15 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- `data/raw/ncbi_merged_ids.tsv:31545` retires `NCBITaxon:1899303` into `NCBITaxon:144541`, but that old ID is absent from retained NCBI taxon rows and does not require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:10600` reports `organism_count: 1` for `NCBITaxon:144541`, matching the YAML source count.
- The native GOLD tables contain 1 organism row, 1 project row, and 1 analysis row for this taxon.
- NCBI has 2 type-material rows for `NCBITaxon:144541`: `Henkel 7022` and `personal:Henkel:7022` as type-material designations.
- Local StrainInfo records have 0 direct exact taxon rows and 0 exact deposit rows for `NCBITaxon:144541`.
- BacDive has 0 exact local rows for `NCBITaxon:144541`.

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

The only extra local evidence is NCBI type-material metadata and one non-retained retired NCBI ID; neither changes the GOLD-only YAML assertions.
