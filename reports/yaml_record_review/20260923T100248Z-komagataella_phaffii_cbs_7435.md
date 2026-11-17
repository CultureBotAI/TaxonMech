# YAML Record Review: Komagataella phaffii CBS 7435

- Repository: TaxonMech
- Record: data/taxa/eukaryota/komagataella_phaffii_cbs_7435.yaml
- Started UTC: 2026-09-23T10:02:48Z
- Finished UTC: 2026-09-23T10:02:48Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/komagataella_phaffii_cbs_7435.yaml` denotes the exact NCBI strain `Komagataella phaffii CBS 7435` as `NCBITaxon:981350`, rank `STRAIN`, under species `NCBITaxon:460519` (`Komagataella phaffii`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/komagataella_phaffii_cbs_7435.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/komagataella_phaffii.yaml data/taxa/eukaryota/komagataella_phaffii_cbs_7435.yaml data/taxa/eukaryota/komagataella_phaffii_gs115.yaml data/taxa/eukaryota/komagataella_populi.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:204630` carries `NCBITaxon:981350`, label `Komagataella phaffii CBS 7435`, rank `STRAIN`, parent `NCBITaxon:460519`, and genetic code `1`; the raw NCBI row carries no synonyms for this strain.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected species `Komagataella phaffii`.
- `curation/seed_scope.tsv:57069` contains this identifier with reason `attested rule: Komagataella phaffii CBS 7435, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:45238`, whose aggregate count is `1` for `NCBITaxon:981350`.
- The current native GOLD scan found exact organisms `Go0010215` for `Komagataella phaffii CBS 7435` and `Go0415714` for `Komagataella phaffii CBS 7435 ERS1987891`.
- Expanding those exact GOLD organisms found projects `Gp0010215` and `Gp0308807`, with 2 native linked analysis rows through `AP PROJECT GOLD IDS`.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:981350`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:981350`, `just validate data/taxa/eukaryota/komagataella_phaffii_cbs_7435.yaml`, and `just validate-strict data/taxa/eukaryota/komagataella_phaffii_cbs_7435.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `komagataella_phaffii_cbs_7435` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The generated assertion count follows `data/raw/gold_organisms.tsv`; the current native exact scan contains one additional exact GOLD organism row for `CBS 7435 ERS1987891`.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
