# YAML Record Review: Komagataella phaffii GS115

- Repository: TaxonMech
- Record: data/taxa/eukaryota/komagataella_phaffii_gs115.yaml
- Started UTC: 2026-09-23T10:02:48Z
- Finished UTC: 2026-09-23T10:02:48Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/komagataella_phaffii_gs115.yaml` denotes the exact NCBI strain `Komagataella phaffii GS115` as `NCBITaxon:644223`, rank `STRAIN`, under species `NCBITaxon:460519` (`Komagataella phaffii`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/komagataella_phaffii_gs115.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/komagataella_phaffii.yaml data/taxa/eukaryota/komagataella_phaffii_cbs_7435.yaml data/taxa/eukaryota/komagataella_phaffii_gs115.yaml data/taxa/eukaryota/komagataella_populi.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:148653` carries `NCBITaxon:644223`, label `Komagataella phaffii GS115`, rank `STRAIN`, parent `NCBITaxon:460519`, and genetic code `1`; the raw NCBI row carries no synonyms for this strain.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected species `Komagataella phaffii`.
- `curation/seed_scope.tsv:56213` contains this identifier with reason `attested rule: Komagataella phaffii GS115, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:40272`, whose aggregate count is `1` for `NCBITaxon:644223`.
- The current native GOLD scan found exact organism `Go0004868` for `Komagataella pastoris GS115`.
- Expanding that exact GOLD organism found projects `Gp0004868` and `Gp0219964`, with 2 native linked analysis rows through `AP PROJECT GOLD IDS`.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:644223`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:644223`, `just validate data/taxa/eukaryota/komagataella_phaffii_gs115.yaml`, and `just validate-strict data/taxa/eukaryota/komagataella_phaffii_gs115.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `komagataella_phaffii_gs115` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Native GOLD still names the exact organism `Komagataella pastoris GS115`; the NCBI row and generated record use the current parentage under `Komagataella phaffii`.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
