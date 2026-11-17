# YAML Record Review: Leyanella arenaria

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leyanella_arenaria.yaml
- Started UTC: 2026-09-23T12:19:37Z
- Finished UTC: 2026-09-23T12:19:37Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leyanella_arenaria.yaml` denotes the exact NCBI species `Leyanella arenaria` as `NCBITaxon:555756`, rank `SPECIES`, under genus `NCBITaxon:555755` (`Leyanella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leyanella_arenaria.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/leucosporidium_scottii.yaml data/taxa/eukaryota/leucosporidium_yakuticum.yaml data/taxa/eukaryota/leyanella_arenaria.yaml data/taxa/eukaryota/liangdongia_berthetii.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:130355` carries `NCBITaxon:555756`, label `Leyanella arenaria`, rank `SPECIES`, parent `NCBITaxon:555755`, genetic code `1`, related synonym `Leyanella arenaria Hasle, von Stosch & Syvertsen, 1983`, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leyanella` genus.
- `curation/seed_scope.tsv:56024` contains this identifier with reason `attested rule: Leyanella arenaria, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38722`, whose aggregate count is `1` for `NCBITaxon:555756`.
- The current native GOLD scan found no exact organism, project, or analysis rows for this NCBI ID.
- Exact StrainInfo scans found 2 direct strains and 2 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

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

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:555756`, `just validate data/taxa/eukaryota/leyanella_arenaria.yaml`, and `just validate-strict data/taxa/eukaryota/leyanella_arenaria.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leyanella_arenaria` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
