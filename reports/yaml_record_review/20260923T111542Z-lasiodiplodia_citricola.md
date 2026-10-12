# YAML Record Review: Lasiodiplodia citricola

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lasiodiplodia_citricola.yaml
- Started UTC: 2026-09-23T11:15:42Z
- Finished UTC: 2026-09-23T11:15:42Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lasiodiplodia_citricola.yaml` denotes the exact NCBI species `Lasiodiplodia citricola` as `NCBITaxon:869388`, rank `SPECIES`, under genus `NCBITaxon:66739` (`Lasiodiplodia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lasiodiplodia_citricola.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lasiodiplodia_citricola.yaml data/taxa/eukaryota/lasiodiplodia_pseudotheobromae.yaml data/taxa/eukaryota/lasiodiplodia_theobromae.yaml data/taxa/eukaryota/lasiosphaeria_deviata.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:183946` carries `NCBITaxon:869388`, label `Lasiodiplodia citricola`, rank `SPECIES`, parent `NCBITaxon:66739`, genetic code `1`, and the related synonyms retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lasiodiplodia`.
- `curation/seed_scope.tsv:56805` contains this identifier with reason `attested rule: Lasiodiplodia citricola, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:869388`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:43543`, whose aggregate count is `1` for `NCBITaxon:869388`.
- The current native GOLD scan found exact organism `Go0677874` for `Lasiodiplodia citricola KE87127`, project `Gp0779715`, and one native analysis row linked through `Gp0779715`.
- Exact scans found four rows in `data/raw/ncbi_type_material.tsv:269666-269669`: two culture-from-holotype rows for `CBS 124707` variants and two type-material rows for `IRAN 1522C` variants.
- Exact StrainInfo and BacDive scans found no source rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found all four `NCBITaxon:869388` type-material rows in `data/raw/ncbi_type_material.tsv`, matching the generated culture-from-holotype and type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:869388`, `just validate data/taxa/eukaryota/lasiodiplodia_citricola.yaml`, and `just validate-strict data/taxa/eukaryota/lasiodiplodia_citricola.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lasiodiplodia_citricola` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
