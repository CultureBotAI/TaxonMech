# YAML Record Review: Laccaria trichodermophora

- Repository: TaxonMech
- Record: data/taxa/eukaryota/laccaria_trichodermophora.yaml
- Started UTC: 2026-09-23T10:35:46Z
- Finished UTC: 2026-09-23T10:35:46Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/laccaria_trichodermophora.yaml` denotes the exact NCBI species `Laccaria trichodermophora` as `NCBITaxon:344589`, rank `SPECIES`, under genus `NCBITaxon:29882` (`Laccaria`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/laccaria_trichodermophora.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/laccaria_trichodermophora.yaml data/taxa/eukaryota/lachancea_cidri.yaml data/taxa/eukaryota/lachancea_dasiensis.yaml data/taxa/eukaryota/lachancea_fermentati.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:71029` carries `NCBITaxon:344589`, label `Laccaria trichodermophora`, rank `SPECIES`, parent `NCBITaxon:29882`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Laccaria`.
- `curation/seed_scope.tsv:55292` contains this identifier with reason `attested rule: Laccaria trichodermophora, 2 sources incl. NCBI`.
- The local NCBI merge side inventory has no old IDs for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:32874`, whose aggregate count is `1` for `NCBITaxon:344589`.
- The current native GOLD scan found no exact organism, project, or analysis rows for `NCBITaxon:344589`.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:344589`, matching the absence of type-material derived strain assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:344589`, `just validate data/taxa/eukaryota/laccaria_trichodermophora.yaml`, and `just validate-strict data/taxa/eukaryota/laccaria_trichodermophora.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `laccaria_trichodermophora` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD exact catalogs are side evidence only and can differ from the retained aggregate used to generate source attestations.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
