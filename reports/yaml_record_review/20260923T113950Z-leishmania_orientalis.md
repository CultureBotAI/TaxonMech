# YAML Record Review: Leishmania orientalis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leishmania_orientalis.yaml
- Started UTC: 2026-09-23T11:39:50Z
- Finished UTC: 2026-09-23T11:39:50Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leishmania_orientalis.yaml` denotes the exact NCBI species `Leishmania orientalis` as `NCBITaxon:2249476`, rank `SPECIES`, under subgenus `NCBITaxon:2249475` (`Mundinia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leishmania_orientalis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/leishmania_orientalis.yaml data/taxa/eukaryota/leishmania_peruviana.yaml data/taxa/eukaryota/leishmania_sp_ghana_2012_lv757.yaml data/taxa/eukaryota/leishmania_sp_namibia.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:522151` carries `NCBITaxon:2249476`, label `Leishmania orientalis`, rank `SPECIES`, parent `NCBITaxon:2249475`, genetic code `1`, exact synonym `Leishmania (Mundinia) orientalis`, related synonym `Leishmania orientalis Bates & Jariyapan, 2018`, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Mundinia` subgenus.
- `curation/seed_scope.tsv:62499` contains this identifier with reason `attested rule: Leishmania orientalis, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:2249476`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:21198`, whose aggregate count is `1` for `NCBITaxon:2249476`.
- The current native GOLD scan found exact organism `Go0598297` for `Leishmania orientalis LSCM4`, project `Gp0616726`, and one native analysis row.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:89542` contains hapantotype material `MHOM/TH/2014/LSCM4` for `NCBITaxon:2249476`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:2249476`, `just validate data/taxa/eukaryota/leishmania_orientalis.yaml`, and `just validate-strict data/taxa/eukaryota/leishmania_orientalis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leishmania_orientalis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
