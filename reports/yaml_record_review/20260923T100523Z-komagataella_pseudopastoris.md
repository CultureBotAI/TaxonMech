# YAML Record Review: Komagataella pseudopastoris

- Repository: TaxonMech
- Record: data/taxa/eukaryota/komagataella_pseudopastoris.yaml
- Started UTC: 2026-09-23T10:05:23Z
- Finished UTC: 2026-09-23T10:05:23Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/komagataella_pseudopastoris.yaml` denotes the exact NCBI species `Komagataella pseudopastoris` as `NCBITaxon:169507`, rank `SPECIES`, under genus `NCBITaxon:460517` (`Komagataella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/komagataella_pseudopastoris.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/komagataella_pseudopastoris.yaml data/taxa/eukaryota/komagataella_ulmi.yaml data/taxa/eukaryota/kondoa_malvinella.yaml data/taxa/eukaryota/kondoa_phyllada.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:34590` carries `NCBITaxon:169507`, label `Komagataella pseudopastoris`, rank `SPECIES`, parent `NCBITaxon:460517`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Komagataella`.
- `curation/seed_scope.tsv:54253` contains this identifier with reason `attested rule: Komagataella pseudopastoris, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:79246` maps side-inventory old ID `NCBITaxon:460520` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:14627`, whose aggregate count is `2` for `NCBITaxon:169507`.
- The current native GOLD scan found exact organisms `Go0517114` for `Komagataella pseudopastoris NRRL Y-27603` and `Go0681691` for `Komagataella pseudopastoris CBS 9187`.
- Expanding those exact GOLD organisms found projects `Gp0441152` and `Gp0783741`, with 2 native linked analysis rows through `AP PROJECT GOLD IDS`.
- StrainInfo has 8 exact direct rows and 20 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 6 rows for `NCBITaxon:169507` at lines 52944-52949, covering `CBS 9187`, `NCAIM Y 01541`, and `NRRL Y-27603` culture-from-type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:169507`, `just validate data/taxa/eukaryota/komagataella_pseudopastoris.yaml`, and `just validate-strict data/taxa/eukaryota/komagataella_pseudopastoris.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `komagataella_pseudopastoris` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
