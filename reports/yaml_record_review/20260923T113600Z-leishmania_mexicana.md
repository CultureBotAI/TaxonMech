# YAML Record Review: Leishmania mexicana

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leishmania_mexicana.yaml
- Started UTC: 2026-09-23T11:36:00Z
- Finished UTC: 2026-09-23T11:36:00Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leishmania_mexicana.yaml` denotes the exact NCBI species `Leishmania mexicana` as `NCBITaxon:5665`, rank `SPECIES`, under `NCBITaxon:38582` (`Leishmania mexicana species complex`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leishmania_mexicana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leishmania_major_strain_lv39c5.yaml data/taxa/eukaryota/leishmania_major_strain_sd_75_1.yaml data/taxa/eukaryota/leishmania_martiniquensis.yaml data/taxa/eukaryota/leishmania_mexicana.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2524` carries `NCBITaxon:5665`, label `Leishmania mexicana`, rank `SPECIES`, parent `NCBITaxon:38582`, genetic code `1`, and exact synonym `Leishmania (Leishmania) mexicana`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Leishmania mexicana species complex`.
- `curation/seed_scope.tsv:52059` contains this identifier with reason `attested rule: Leishmania mexicana, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:5665`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39010`, whose aggregate count is `1` for `NCBITaxon:5665`.
- The current native GOLD scan found exact organism `Go0572624` for `Leishmania mexicana 215-49`, project `Gp0547247`, and one native analysis row.
- Exact StrainInfo scans found 3 direct strains and 3 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:5665` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:5665`, `just validate data/taxa/eukaryota/leishmania_mexicana.yaml`, and `just validate-strict data/taxa/eukaryota/leishmania_mexicana.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leishmania_mexicana` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
