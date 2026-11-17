# YAML Record Review: Pucciniomycotina sp.

- Verdict: pass
- Target: `data/taxa/eukaryota/pucciniomycotina_sp.yaml`
- Identifier: `NCBITaxon:2011928`

## Target

Reviewed the complete 56-line YAML record for Pucciniomycotina sp. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pucciniomycotina_sp`.

## Validation

- `just validate data/taxa/eukaryota/pucciniomycotina_sp.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pucciniomycotina_sp.yaml data/taxa/eukaryota/pulveroboletus_ravenelii.yaml data/taxa/eukaryota/purpureocillium_lilacinum.yaml data/taxa/eukaryota/pycnoporellus_fulgens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:510008` retains `NCBITaxon:2011928` as `Pucciniomycotina sp.`, rank `SPECIES`, parent `NCBITaxon:205859`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:61850`, with reason `attested rule: Pucciniomycotina sp., 2 sources incl. NCBI`.
- NCBI lists 0 exact synonyms, 0 related synonyms, and 0 broad synonyms for the taxon, matching the absence of a synonym block in the YAML.
- All 9 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:2011928`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:18576` reports `organism_count: 1` for `NCBITaxon:2011928`, matching the YAML source count.
- The native GOLD tables contain 1 organism row, 1 project row, and 0 analysis rows for this taxon.
- NCBI has 0 type-material rows for `NCBITaxon:2011928`.
- Local StrainInfo records have 0 direct exact taxon rows and 0 exact deposit rows for `NCBITaxon:2011928`.
- BacDive has 0 exact local rows for `NCBITaxon:2011928`.

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

The record is a GOLD-attested unclassified placeholder with no synonym, strain, auxiliary, type-material, or merged-ID evidence requiring additional YAML assertions.
