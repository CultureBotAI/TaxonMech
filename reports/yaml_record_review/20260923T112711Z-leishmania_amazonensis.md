# YAML Record Review: Leishmania amazonensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leishmania_amazonensis.yaml
- Started UTC: 2026-09-23T11:27:11Z
- Finished UTC: 2026-09-23T11:27:11Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leishmania_amazonensis.yaml` denotes the exact NCBI species `Leishmania amazonensis` as `NCBITaxon:5659`, rank `SPECIES`, under `NCBITaxon:38582` (`Leishmania mexicana species complex`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leishmania_amazonensis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/leishmania_aethiopica.yaml data/taxa/eukaryota/leishmania_amazonensis.yaml data/taxa/eukaryota/leishmania_braziliensis.yaml data/taxa/eukaryota/leishmania_braziliensis_mhom_br_75_m2904.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2519` carries `NCBITaxon:5659`, label `Leishmania amazonensis`, rank `SPECIES`, parent `NCBITaxon:38582`, genetic code `1`, and exact synonyms `Leishmania (Leishmania) amazonensis` and `Leishmania mexicana amazonensis`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leishmania mexicana species complex`.
- `curation/seed_scope.tsv:52055` contains this identifier with reason `attested rule: Leishmania amazonensis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:64433` maps side-inventory old ID `NCBITaxon:31284` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38991`, whose aggregate count is `3` for `NCBITaxon:5659`.
- The current native GOLD scan found exact organisms `Go0038909`, `Go0098599`, `Go0519943`, and `Go0572623`, five linked projects, and four native analysis rows.
- Exact StrainInfo scans found 2 direct strains and 2 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:5659` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:5659`, `just validate data/taxa/eukaryota/leishmania_amazonensis.yaml`, and `just validate-strict data/taxa/eukaryota/leishmania_amazonensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leishmania_amazonensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
