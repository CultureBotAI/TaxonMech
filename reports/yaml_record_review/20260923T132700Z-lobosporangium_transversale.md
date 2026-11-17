# YAML Record Review: Lobosporangium transversale

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lobosporangium_transversale.yaml
- Started UTC: 2026-09-23T13:27:00Z
- Finished UTC: 2026-09-23T13:27:00Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lobosporangium_transversale.yaml` denotes the exact NCBI species `Lobosporangium transversale` as `NCBITaxon:64571`, rank `SPECIES`, under genus `NCBITaxon:299330` (`Lobosporangium`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lobosporangium_transversale.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lizonia_empirigonia.yaml data/taxa/eukaryota/lobaria_pulmonaria.yaml data/taxa/eukaryota/lobosporangium_transversale.yaml data/taxa/eukaryota/lobulomyces_angularis.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:8192` carries `NCBITaxon:64571`, label `Lobosporangium transversale`, rank `SPECIES`, parent `NCBITaxon:299330`, genetic code `1`, one exact synonym, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lobosporangium` genus.
- The record preserves `Echinosporangium transversale` as an exact synonym and both authorship-bearing names as related synonyms from NCBI.
- `curation/seed_scope.tsv:53098` contains this identifier with reason `attested rule: Lobosporangium transversale, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:64571`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:40342`, whose aggregate count is `2` for `NCBITaxon:64571`.
- The native GOLD scan found two exact organisms for this NCBI ID: `Go0115750` for strain `NRRL 3116` and `Go0302657` for strain `NRRL 5525`.
- The native GOLD projects scan found four linked projects across those two exact GOLD organisms, and the native GOLD analyses scan found two rows linked through project `Gp0120030`.
- Exact StrainInfo scans found two direct strain rows and seven deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:244470` through `244482` contain 13 type-material spellings for `Echinosporangium transversale`, spanning `ATCC 16960`, `CBS 357.67`, `FSU806; CBS357.67`, `IMI 130776ii`, `NRRL 3116`, and `VKM F-1384` variants. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:64571`, `just validate data/taxa/eukaryota/lobosporangium_transversale.yaml`, and `just validate-strict data/taxa/eukaryota/lobosporangium_transversale.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lobosporangium_transversale` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
