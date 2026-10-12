# YAML Record Review: Lagenidium giganteum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lagenidium_giganteum.yaml
- Started UTC: 2026-09-23T11:09:43Z
- Finished UTC: 2026-09-23T11:09:43Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lagenidium_giganteum.yaml` denotes the exact NCBI species `Lagenidium giganteum` as `NCBITaxon:4803`, rank `SPECIES`, under genus `NCBITaxon:4802` (`Lagenidium`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lagenidium_giganteum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lactifluus_subvellereus.yaml data/taxa/eukaryota/lactifluus_volemus.yaml data/taxa/eukaryota/laetiporus_sulphureus.yaml data/taxa/eukaryota/lagenidium_giganteum.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2067` carries `NCBITaxon:4803`, label `Lagenidium giganteum`, rank `SPECIES`, parent `NCBITaxon:4802`, genetic code `1`, and the related synonym retained in the generated record.
- The 10 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lagenidium`.
- `curation/seed_scope.tsv:51849` contains this identifier with reason `attested rule: Lagenidium giganteum, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:4803`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:36738`, whose aggregate count is `2` for `NCBITaxon:4803`.
- The current native GOLD scan found exact organisms `Go0390094` for `Lagenidium giganteum ARSEF 373` and `Go0572062` for `Lagenidium giganteum MTLA-03`.
- Expanding those exact GOLD organisms found projects `Gp0252491` and `Gp0546564`, each with a native analysis row.
- Exact StrainInfo scans found 6 direct strains and 12 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.
- Exact scans found two type-material rows in `data/raw/ncbi_type_material.tsv:220776-220777`, matching the type-material assertions for the recorded `ATCC 36492` variants.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found all two `NCBITaxon:4803` type-material rows in `data/raw/ncbi_type_material.tsv`, matching the generated type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:4803`, `just validate data/taxa/eukaryota/lagenidium_giganteum.yaml`, and `just validate-strict data/taxa/eukaryota/lagenidium_giganteum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lagenidium_giganteum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
