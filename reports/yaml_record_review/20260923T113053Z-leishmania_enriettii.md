# YAML Record Review: Leishmania enriettii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leishmania_enriettii.yaml
- Started UTC: 2026-09-23T11:30:53Z
- Finished UTC: 2026-09-23T11:30:53Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leishmania_enriettii.yaml` denotes the exact NCBI species `Leishmania enriettii` as `NCBITaxon:5663`, rank `SPECIES`, under `NCBITaxon:2249475` (`Mundinia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leishmania_enriettii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leishmania_chagasi.yaml data/taxa/eukaryota/leishmania_donovani.yaml data/taxa/eukaryota/leishmania_enriettii.yaml data/taxa/eukaryota/leishmania_guyanensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2522` carries `NCBITaxon:5663`, label `Leishmania enriettii`, rank `SPECIES`, parent `NCBITaxon:2249475`, genetic code `1`, exact synonyms `Leishmania (Leishmania) enriettii` and `Leishmania (Mundinia) enrietti`, and the related synonym retained in the generated record.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected subgenus `Mundinia`.
- `curation/seed_scope.tsv:52058` contains this identifier with reason `attested rule: Leishmania enriettii, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:5663`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39004`, whose aggregate count is `1` for `NCBITaxon:5663`.
- The current native GOLD scan found exact organisms `Go0038356` and `Go0598298`, projects `Gp0038356` and `Gp0616727`, and two native analysis rows.
- Exact StrainInfo scans found 2 direct strains and 2 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:5663` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:5663`, `just validate data/taxa/eukaryota/leishmania_enriettii.yaml`, and `just validate-strict data/taxa/eukaryota/leishmania_enriettii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leishmania_enriettii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
