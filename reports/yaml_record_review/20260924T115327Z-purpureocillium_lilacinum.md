# YAML Record Review: Purpureocillium lilacinum

- Verdict: pass
- Target: `data/taxa/eukaryota/purpureocillium_lilacinum.yaml`
- Identifier: `NCBITaxon:33203`

## Target

Reviewed the complete 94-line YAML record for Purpureocillium lilacinum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `purpureocillium_lilacinum`.

## Validation

- `just validate data/taxa/eukaryota/purpureocillium_lilacinum.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pucciniomycotina_sp.yaml data/taxa/eukaryota/pulveroboletus_ravenelii.yaml data/taxa/eukaryota/purpureocillium_lilacinum.yaml data/taxa/eukaryota/pycnoporellus_fulgens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:3557` retains `NCBITaxon:33203` as `Purpureocillium lilacinum`, rank `SPECIES`, parent `NCBITaxon:1052105`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:52256`, with reason `attested rule: Purpureocillium lilacinum, 2 sources incl. NCBI`.
- NCBI lists 3 exact synonyms, 2 related synonyms, and 0 broad synonyms for the taxon, matching the 5 synonym assertions in the YAML.
- All 16 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:33203`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:32336` reports `organism_count: 18` for `NCBITaxon:33203`, matching the YAML source count.
- The native GOLD tables contain 16 organism rows, 57 project rows, and 5 analysis rows for this taxon.
- NCBI has 22 type-material rows at `data/raw/ncbi_type_material.tsv:179016` through `data/raw/ncbi_type_material.tsv:179037`, including 2 culture-from-type-material `CBS 284.36` designations and 20 `Penicillium lilacinum` type-material designations.
- Local StrainInfo records have 184 direct exact taxon rows and 224 exact deposit entries for `NCBITaxon:33203`; the exact numeric-boundary text scan found 185 records because `siID 187729` is a non-direct `Talaromyces rugulosus` record with a deposit labeled `IMI 028811` for `Paecilomyces lilacinus`.
- BacDive has 0 exact local rows for `NCBITaxon:33203`.

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

The abundant local type-material and StrainInfo cache evidence does not materialize into generated strain overlay rows, so the generated YAML remains a GOLD/NCBI no-strain record.
