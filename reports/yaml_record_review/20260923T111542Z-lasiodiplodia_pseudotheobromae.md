# YAML Record Review: Lasiodiplodia pseudotheobromae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lasiodiplodia_pseudotheobromae.yaml
- Started UTC: 2026-09-23T11:15:42Z
- Finished UTC: 2026-09-23T11:15:42Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lasiodiplodia_pseudotheobromae.yaml` denotes the exact NCBI species `Lasiodiplodia pseudotheobromae` as `NCBITaxon:466954`, rank `SPECIES`, under genus `NCBITaxon:66739` (`Lasiodiplodia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lasiodiplodia_pseudotheobromae.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lasiodiplodia_citricola.yaml data/taxa/eukaryota/lasiodiplodia_pseudotheobromae.yaml data/taxa/eukaryota/lasiodiplodia_theobromae.yaml data/taxa/eukaryota/lasiosphaeria_deviata.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:104363` carries `NCBITaxon:466954`, label `Lasiodiplodia pseudotheobromae`, rank `SPECIES`, parent `NCBITaxon:66739`, genetic code `1`, the exact synonym retained in the generated record, and the related synonyms retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lasiodiplodia`.
- `curation/seed_scope.tsv:55750` contains this identifier with reason `attested rule: Lasiodiplodia pseudotheobromae, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:31506`, `data/raw/ncbi_merged_ids.tsv:80994`, and `data/raw/ncbi_merged_ids.tsv:80995` map side-inventory old IDs `NCBITaxon:1898625`, `NCBITaxon:481272`, and `NCBITaxon:481273` into this current taxon, but no retained raw NCBI taxon rows exist for those old IDs, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:36348`, whose aggregate count is `1` for `NCBITaxon:466954`.
- The current native GOLD scan found exact organism `Go0677850` for `Lasiodiplodia pseudotheobromae KET9`, project `Gp0779691`, and one native analysis row linked through `Gp0779691`.
- Exact scans found two culture-from-type-material rows in `data/raw/ncbi_type_material.tsv:217936-217937` for `CBS 116459` variants.
- Exact StrainInfo scans found 2 direct strains and 2 deposits for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found all two `NCBITaxon:466954` type-material rows in `data/raw/ncbi_type_material.tsv`, matching the generated culture-from-type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:466954`, `just validate data/taxa/eukaryota/lasiodiplodia_pseudotheobromae.yaml`, and `just validate-strict data/taxa/eukaryota/lasiodiplodia_pseudotheobromae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lasiodiplodia_pseudotheobromae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
