# YAML Record Review: Komagataella phaffii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/komagataella_phaffii.yaml
- Started UTC: 2026-09-23T10:02:48Z
- Finished UTC: 2026-09-23T10:02:48Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/komagataella_phaffii.yaml` denotes the exact NCBI species `Komagataella phaffii` as `NCBITaxon:460519`, rank `SPECIES`, under genus `NCBITaxon:460517` (`Komagataella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/komagataella_phaffii.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/komagataella_phaffii.yaml data/taxa/eukaryota/komagataella_phaffii_cbs_7435.yaml data/taxa/eukaryota/komagataella_phaffii_gs115.yaml data/taxa/eukaryota/komagataella_populi.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:103339` carries `NCBITaxon:460519`, label `Komagataella phaffii`, rank `SPECIES`, parent `NCBITaxon:460517`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Komagataella`.
- `curation/seed_scope.tsv:55736` contains this identifier with reason `attested rule: Komagataella phaffii, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:90808` maps side-inventory old ID `NCBITaxon:65813` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:36211`, whose aggregate count is `5` for `NCBITaxon:460519`.
- The current native GOLD scan found exact organisms for `NRRL Y-11430`, `ATCC 76273`, `NRRL 64867`, `UWOPS03-328y3`, and `NRRL Y-7556`.
- Expanding those exact GOLD organisms found 6 projects, including two for `NRRL 64867`, and 2 native linked analysis rows through `AP PROJECT GOLD IDS`.
- StrainInfo has 62 exact direct rows and 64 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 5 rows for `NCBITaxon:460519` at lines 216473-216477, covering `CBS 2612` and `NRRL Y-7556` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:460519`, `just validate data/taxa/eukaryota/komagataella_phaffii.yaml`, and `just validate-strict data/taxa/eukaryota/komagataella_phaffii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `komagataella_phaffii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
