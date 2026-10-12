# YAML Record Review: Pycnoporellus fulgens

- Verdict: pass
- Target: `data/taxa/eukaryota/pycnoporellus_fulgens.yaml`
- Identifier: `NCBITaxon:202718`

## Target

Reviewed the complete 78-line YAML record for Pycnoporellus fulgens. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `pycnoporellus_fulgens`.

## Validation

- `just validate data/taxa/eukaryota/pycnoporellus_fulgens.yaml` exited 0 and reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/pucciniomycotina_sp.yaml data/taxa/eukaryota/pulveroboletus_ravenelii.yaml data/taxa/eukaryota/purpureocillium_lilacinum.yaml data/taxa/eukaryota/pycnoporellus_fulgens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

- The NCBI source row at `data/raw/ncbitaxon_taxa.tsv:39994` retains `NCBITaxon:202718` as `Pycnoporellus fulgens`, rank `SPECIES`, parent `NCBITaxon:202717`, genetic code `1`, taxonomy snapshot `2026-09-13`, and `attested_by: gold`.
- The seeded scope contains exactly one exact identifier row, `data/seeds.tsv:54468`, with reason `attested rule: Pycnoporellus fulgens, 2 sources incl. NCBI`.
- NCBI lists 1 exact synonym, 2 related synonyms, and 0 broad synonyms for the taxon, matching the 3 synonym assertions in the YAML.
- All 13 YAML lineage assertions were checked against the NCBI dump, with 0 missing source rows and 0 parent mismatches.
- The NCBI merged-ID table has no rows that retire an old identifier into `NCBITaxon:202718`, and no retained old IDs require a `replaces` assertion.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:19079` reports `organism_count: 1` for `NCBITaxon:202718`, matching the YAML source count.
- The native GOLD tables contain 1 organism row, 2 project rows, and 0 analysis rows for this taxon.
- NCBI has 2 reference-material rows for `Hydnum fulgens`: `CFMR:CA-20` and `CFMR:CA:20`.
- Local StrainInfo records have 4 direct exact taxon rows and 5 exact deposit entries for `NCBITaxon:202718`.
- BacDive has 0 exact local rows for `NCBITaxon:202718`.

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

The small NCBI reference-material and StrainInfo exact-cache sets do not produce generated overlay rows, leaving the no-strain YAML assertions consistent.
