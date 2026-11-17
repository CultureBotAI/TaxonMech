# YAML Record Review: Leratiomyces ceres

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leratiomyces_ceres.yaml
- Started UTC: 2026-09-23T12:11:08Z
- Finished UTC: 2026-09-23T12:11:08Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leratiomyces_ceres.yaml` denotes the exact NCBI species `Leratiomyces ceres` as `NCBITaxon:935580`, rank `SPECIES`, under genus `NCBITaxon:75498` (`Leratiomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leratiomyces_ceres.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leratiomyces_ceres.yaml data/taxa/eukaryota/leratiomyces_erythrocephalus.yaml data/taxa/eukaryota/lessardia_elongata.yaml data/taxa/eukaryota/leucangium_carthusianum.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:198000` carries `NCBITaxon:935580`, label `Leratiomyces ceres`, rank `SPECIES`, parent `NCBITaxon:75498`, genetic code `1`, exact synonyms `Agaricus ceres` and `Psilocybe ceres`, two related synonyms, and snapshot `2026-09-13`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leratiomyces` genus.
- `curation/seed_scope.tsv:56950` contains this identifier with reason `attested rule: Leratiomyces ceres, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:44790`, whose aggregate count is `1` for `NCBITaxon:935580`.
- The current native GOLD scan found exact organism `Go0530008` for `Leratiomyces ceres mycota028`, 8 exact projects from `Gp0460685` through `Gp0460691` plus `Gp0467504`, and no exact native analysis rows for the complete project-ID set.
- Exact StrainInfo scans found 5 direct strains and 5 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

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

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:935580`, `just validate data/taxa/eukaryota/leratiomyces_ceres.yaml`, and `just validate-strict data/taxa/eukaryota/leratiomyces_ceres.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leratiomyces_ceres` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
