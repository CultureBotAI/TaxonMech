# YAML Record Review: Komagataella ulmi

- Repository: TaxonMech
- Record: data/taxa/eukaryota/komagataella_ulmi.yaml
- Started UTC: 2026-09-23T10:05:23Z
- Finished UTC: 2026-09-23T10:05:23Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/komagataella_ulmi.yaml` denotes the exact NCBI species `Komagataella ulmi` as `NCBITaxon:1099807`, rank `SPECIES`, under genus `NCBITaxon:460517` (`Komagataella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/komagataella_ulmi.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/komagataella_pseudopastoris.yaml data/taxa/eukaryota/komagataella_ulmi.yaml data/taxa/eukaryota/kondoa_malvinella.yaml data/taxa/eukaryota/kondoa_phyllada.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:236530` carries `NCBITaxon:1099807`, label `Komagataella ulmi`, rank `SPECIES`, parent `NCBITaxon:460517`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Komagataella`.
- `curation/seed_scope.tsv:57620` contains this identifier with reason `attested rule: Komagataella ulmi, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:1847`, whose aggregate count is `2` for `NCBITaxon:1099807`.
- The current native GOLD scan found exact organisms `Go0681685` for `Komagataella ulmi CBS 12361` and `Go0705702` for `Komagataella ulmi NRRL YB-407`.
- Expanding those exact GOLD organisms found projects `Gp0783735` and `Gp0831756`, with one native linked analysis for `Komagataella ulmi CBS 12361` through `AP PROJECT GOLD IDS`.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 9 rows for `NCBITaxon:1099807` at lines 6325-6333, covering `CBS 12361`, `NRRL YB-407`, and `YB-407` holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1099807`, `just validate data/taxa/eukaryota/komagataella_ulmi.yaml`, and `just validate-strict data/taxa/eukaryota/komagataella_ulmi.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `komagataella_ulmi` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
