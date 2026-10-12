# YAML Record Review: Laccaria laccata

- Repository: TaxonMech
- Record: data/taxa/eukaryota/laccaria_laccata.yaml
- Started UTC: 2026-09-23T10:30:20Z
- Finished UTC: 2026-09-23T10:30:20Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/laccaria_laccata.yaml` denotes the exact NCBI species `Laccaria laccata` as `NCBITaxon:36061`, rank `SPECIES`, under genus `NCBITaxon:29882` (`Laccaria`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/laccaria_laccata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/laccaria_amethystina.yaml data/taxa/eukaryota/laccaria_bicolor.yaml data/taxa/eukaryota/laccaria_bicolor_n203.yaml data/taxa/eukaryota/laccaria_laccata.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4061` carries `NCBITaxon:36061`, label `Laccaria laccata`, rank `SPECIES`, parent `NCBITaxon:29882`, genetic code `1`, exact synonym `Agaricus laccatus`, and the NCBI synonym set retained in the generated record.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Laccaria`.
- `curation/seed_scope.tsv:52326` contains this identifier with reason `attested rule: Laccaria laccata, 2 sources incl. NCBI`.
- The local NCBI merge side inventory has no old IDs for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33273`, whose aggregate count is `1` for `NCBITaxon:36061`.
- The current native GOLD scan found no exact organism, project, or analysis rows for `NCBITaxon:36061`.
- Exact StrainInfo scans found 18 direct strains and 21 deposits for this taxon; exact BacDive and generated raw strain-table scans found no corresponding local BacDive-derived strain rows to overlay.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:36061`, matching the absence of type-material derived strain assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:36061`, `just validate data/taxa/eukaryota/laccaria_laccata.yaml`, and `just validate-strict data/taxa/eukaryota/laccaria_laccata.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `laccaria_laccata` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD exact catalogs are side evidence only and can differ from the retained aggregate used to generate source attestations.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
