# YAML Record Review: Kondoa phyllada

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kondoa_phyllada.yaml
- Started UTC: 2026-09-23T10:05:23Z
- Finished UTC: 2026-09-23T10:05:23Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kondoa_phyllada.yaml` denotes the exact NCBI species `Kondoa phyllada` as `NCBITaxon:105982`, rank `SPECIES`, under genus `NCBITaxon:36054` (`Kondoa`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kondoa_phyllada.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/komagataella_pseudopastoris.yaml data/taxa/eukaryota/komagataella_ulmi.yaml data/taxa/eukaryota/kondoa_malvinella.yaml data/taxa/eukaryota/kondoa_phyllada.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:19028` carries `NCBITaxon:105982`, label `Kondoa phyllada`, rank `SPECIES`, parent `NCBITaxon:36054`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kondoa`.
- `curation/seed_scope.tsv:53703` contains this identifier with reason `attested rule: Kondoa phyllada, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:82189` maps side-inventory old ID `NCBITaxon:4994` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:1084`, whose aggregate count is `1` for `NCBITaxon:105982`.
- The current native GOLD JSONL exact scan found no organism, project, or analysis rows for this NCBI ID.
- StrainInfo has 5 exact direct rows and 12 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.
- Exact BacDive scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 11 rows for `NCBITaxon:105982` at lines 3789-3799, covering `CBS 7169` culture-from-type-material variants plus `IFO 10581`, `IGC 5344`, `JCM 7476`, and `NRRL Y-17309` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:105982`, `just validate data/taxa/eukaryota/kondoa_phyllada.yaml`, and `just validate-strict data/taxa/eukaryota/kondoa_phyllada.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kondoa_phyllada` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The generated assertion count follows `data/raw/gold_organisms.tsv`; the current native exact GOLD JSONL scan does not contain rows for this NCBI ID.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
