# YAML Record Review: Karenia brevis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/karenia_brevis.yaml
- Started UTC: 2026-09-23T09:07:36Z
- Finished UTC: 2026-09-23T09:07:36Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/karenia_brevis.yaml` denotes the exact NCBI species `Karenia brevis` as `NCBITaxon:156230`, rank `SPECIES`, under genus `NCBITaxon:156229` (`Karenia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/karenia_brevis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kalmanozyma_brasiliensis.yaml data/taxa/eukaryota/kappamyces_sp.yaml data/taxa/eukaryota/kappaphycus_alvarezii.yaml data/taxa/eukaryota/karenia_brevis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:32466` carries `NCBITaxon:156230`, label `Karenia brevis`, rank `SPECIES`, parent `NCBITaxon:156229`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 9 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Karenia`.
- `curation/seed_scope.tsv:54122` contains this identifier with reason `attested rule: Karenia brevis, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old ID `NCBITaxon:58157`, but that old ID is not present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:12514`, whose aggregate count is `4` for `NCBITaxon:156230`.
- The current native GOLD scan found exact organisms `Go0002364`, `Go0368710`, `Go0368711`, `Go0368712`, and `Go0368713`.
- Expanding those exact GOLD organisms found project `Gp0002364`, with no native linked analysis rows.
- StrainInfo has 9 exact direct rows and 9 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no type-material rows for `NCBITaxon:156230`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:156230`, `just validate data/taxa/eukaryota/karenia_brevis.yaml`, and `just validate-strict data/taxa/eukaryota/karenia_brevis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `karenia_brevis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
