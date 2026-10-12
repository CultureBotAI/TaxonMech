# YAML Record Review: Lentamyces zychae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lentamyces_zychae.yaml
- Started UTC: 2026-09-23T11:46:19Z
- Finished UTC: 2026-09-23T11:46:19Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lentamyces_zychae.yaml` denotes the exact NCBI species `Lentamyces zychae` as `NCBITaxon:36079`, rank `SPECIES`, under genus `NCBITaxon:565135` (`Lentamyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lentamyces_zychae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lentamyces_zychae.yaml data/taxa/eukaryota/lentinellus_vulpinus.yaml data/taxa/eukaryota/lentinula_aciculospora.yaml data/taxa/eukaryota/lentinula_aff_boryana.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:4065` carries `NCBITaxon:36079`, label `Lentamyces zychae`, rank `SPECIES`, parent `NCBITaxon:565135`, genetic code `1`, exact synonym `Absidia zychae`, two related synonyms, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lentamyces` genus.
- `curation/seed_scope.tsv:52328` contains this identifier with reason `attested rule: Lentamyces zychae, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:36079`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33277`, whose aggregate count is `2` for `NCBITaxon:36079`.
- The current native GOLD scan found exact organisms `Go0452973` for `Absidia zychae NRRL A-23515` and `Go0512870` for `Lentamyces zychae NRRL 2806`, three linked projects, and no linked native GOLD analysis rows.
- Exact StrainInfo scans found two direct strains and seven deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:193905` through `193910` contain six exact type-material rows for `NCBITaxon:36079`, covering `CBS 104.35` culture-from-type spellings and `ATCC 24266` / `NRRL 2806` type-material spellings. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:36079`, `just validate data/taxa/eukaryota/lentamyces_zychae.yaml`, and `just validate-strict data/taxa/eukaryota/lentamyces_zychae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lentamyces_zychae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
