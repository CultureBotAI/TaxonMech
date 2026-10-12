# YAML Record Review: Lobaria pulmonaria

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lobaria_pulmonaria.yaml
- Started UTC: 2026-09-23T13:27:00Z
- Finished UTC: 2026-09-23T13:27:00Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lobaria_pulmonaria.yaml` denotes the exact NCBI species `Lobaria pulmonaria` as `NCBITaxon:86794`, rank `SPECIES`, under genus `NCBITaxon:63752` (`Lobaria`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lobaria_pulmonaria.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lizonia_empirigonia.yaml data/taxa/eukaryota/lobaria_pulmonaria.yaml data/taxa/eukaryota/lobosporangium_transversale.yaml data/taxa/eukaryota/lobulomyces_angularis.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:13437` carries `NCBITaxon:86794`, label `Lobaria pulmonaria`, rank `SPECIES`, parent `NCBITaxon:63752`, genetic code `1`, one exact synonym, five related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 17 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lobaria` genus.
- The record preserves `Lichen pulmonarius` as an exact synonym and five related synonyms from NCBI, including three common-name synonyms.
- `curation/seed_scope.tsv:53445` contains this identifier with reason `attested rule: Lobaria pulmonaria, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:86794`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:43519`, whose aggregate count is `2` for `NCBITaxon:86794`.
- The native GOLD scan found two exact organisms for strain `Scotland`, `Go0016227` and `Go0018360`, and one linked project for each organism.
- The native GOLD analyses scan found no rows linked through those project IDs.
- Exact BacDive and StrainInfo scans found no rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- The exact NCBI type-material scan found no `data/raw/ncbi_type_material.tsv` rows for `NCBITaxon:86794`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:86794`, `just validate data/taxa/eukaryota/lobaria_pulmonaria.yaml`, and `just validate-strict data/taxa/eukaryota/lobaria_pulmonaria.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lobaria_pulmonaria` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
