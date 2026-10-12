# YAML Record Review: Knufia epidermidis CBS 120353

- Repository: TaxonMech
- Record: data/taxa/eukaryota/knufia_epidermidis_cbs_120353.yaml
- Started UTC: 2026-09-23T09:30:05Z
- Finished UTC: 2026-09-23T09:30:05Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/knufia_epidermidis_cbs_120353.yaml` denotes the exact NCBI strain `Knufia epidermidis CBS 120353` as `NCBITaxon:1220923`, rank `STRAIN`, under species `NCBITaxon:535988` (`Knufia epidermidis`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/knufia_epidermidis_cbs_120353.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kluyveromyces_wickerhamii.yaml data/taxa/eukaryota/knoxdaviesia_capensis.yaml data/taxa/eukaryota/knoxdaviesia_proteae.yaml data/taxa/eukaryota/knufia_epidermidis_cbs_120353.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:276952` carries `NCBITaxon:1220923`, label `Knufia epidermidis CBS 120353`, rank `STRAIN`, parent `NCBITaxon:535988`, genetic code `1`, and the exact synonym retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected parent species `Knufia epidermidis`.
- `curation/seed_scope.tsv:58477` contains this identifier with reason `attested rule: Knufia epidermidis CBS 120353, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:5311`, whose aggregate count is `1` for `NCBITaxon:1220923`.
- The current native GOLD scan found exact organism `Go0023046` for `Coniosporium epidermidis CBS 120353`.
- Expanding that exact GOLD organism found project `Gp0023046`, with no native linked analysis rows.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no rows for `NCBITaxon:1220923`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1220923`, `just validate data/taxa/eukaryota/knufia_epidermidis_cbs_120353.yaml`, and `just validate-strict data/taxa/eukaryota/knufia_epidermidis_cbs_120353.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `knufia_epidermidis_cbs_120353` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
