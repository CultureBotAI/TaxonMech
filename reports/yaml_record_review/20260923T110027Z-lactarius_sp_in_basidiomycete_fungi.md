# YAML Record Review: Lactarius sp. (in: basidiomycete fungi)

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lactarius_sp_in_basidiomycete_fungi.yaml
- Started UTC: 2026-09-23T11:00:27Z
- Finished UTC: 2026-09-23T11:00:27Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lactarius_sp_in_basidiomycete_fungi.yaml` denotes the exact NCBI species `Lactarius sp. (in: basidiomycete fungi)` as `NCBITaxon:1886493`, rank `SPECIES`, under `NCBITaxon:2676555` (`unclassified Lactarius (in: basidiomycete fungi)`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lactarius_sp_in_basidiomycete_fungi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lactarius_sanguifluus.yaml data/taxa/eukaryota/lactarius_sp_in_basidiomycete_fungi.yaml data/taxa/eukaryota/lactarius_stephensii.yaml data/taxa/eukaryota/lactarius_subdulcis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:490579` carries `NCBITaxon:1886493`, label `Lactarius sp. (in: basidiomycete fungi)`, rank `SPECIES`, parent `NCBITaxon:2676555`, genetic code `1`, and exact synonym `Lactarius sp.`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, passing through `unclassified Lactarius (in: basidiomycete fungi)` under genus `Lactarius`.
- `curation/seed_scope.tsv:61451` contains this identifier with reason `attested rule: Lactarius sp. (in: basidiomycete fungi), 2 sources incl. NCBI`.
- The side-inventory NCBI merged-ID scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:16971`, whose aggregate count is `2` for `NCBITaxon:1886493`.
- The current native GOLD scan found no exact organism, project, or analysis rows for `NCBITaxon:1886493`, so only the aggregate row currently supports the generated GOLD assertion count.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:1886493` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1886493`, `just validate data/taxa/eukaryota/lactarius_sp_in_basidiomycete_fungi.yaml`, and `just validate-strict data/taxa/eukaryota/lactarius_sp_in_basidiomycete_fungi.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lactarius_sp_in_basidiomycete_fungi` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
