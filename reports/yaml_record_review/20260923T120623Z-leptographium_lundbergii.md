# YAML Record Review: Leptographium lundbergii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leptographium_lundbergii.yaml
- Started UTC: 2026-09-23T12:06:23Z
- Finished UTC: 2026-09-23T12:06:23Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leptographium_lundbergii.yaml` denotes the exact NCBI species `Leptographium lundbergii` as `NCBITaxon:96373`, rank `SPECIES`, under genus `NCBITaxon:96312` (`Leptographium`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leptographium_lundbergii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leptographium_lundbergii.yaml data/taxa/eukaryota/leptomonas_pyrrhocoris.yaml data/taxa/eukaryota/leptomonas_seymouri.yaml data/taxa/eukaryota/leptomonas_seymouri_bhu1095.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:16262` carries `NCBITaxon:96373`, label `Leptographium lundbergii`, rank `SPECIES`, parent `NCBITaxon:96312`, genetic code `1`, related synonym `Leptographium lundbergii Lagerberg & Melin, 1927`, and snapshot `2026-09-13`.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leptographium` genus.
- `curation/seed_scope.tsv:53565` contains this identifier with reason `attested rule: Leptographium lundbergii, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:45104`, whose aggregate count is `1` for `NCBITaxon:96373`.
- The current native GOLD scan found exact organism `Go0140055` for `Leptographium lundbergii CBS 138716`, project `Gp0145151`, and one native analysis row linked through `AP PROJECT GOLD IDS` to `Gp0145151`.
- Exact StrainInfo scans found 26 direct strains and 29 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- The NCBI type-material scan found 0 rows for this taxon, matching the absence of type-material-specific output in the generated record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:96373`, `just validate data/taxa/eukaryota/leptographium_lundbergii.yaml`, and `just validate-strict data/taxa/eukaryota/leptographium_lundbergii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leptographium_lundbergii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
