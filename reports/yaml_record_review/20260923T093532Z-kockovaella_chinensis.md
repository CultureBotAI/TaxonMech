# YAML Record Review: Kockovaella chinensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kockovaella_chinensis.yaml
- Started UTC: 2026-09-23T09:35:32Z
- Finished UTC: 2026-09-23T09:35:32Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kockovaella_chinensis.yaml` denotes the exact NCBI species `Kockovaella chinensis` as `NCBITaxon:104677`, rank `SPECIES`, under genus `NCBITaxon:4998` (`Kockovaella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kockovaella_chinensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/knufia_sp.yaml data/taxa/eukaryota/kockiozyma_suomiensis.yaml data/taxa/eukaryota/kockovaella_chinensis.yaml data/taxa/eukaryota/kockovaella_imperatae.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:18708` carries `NCBITaxon:104677`, label `Kockovaella chinensis`, rank `SPECIES`, parent `NCBITaxon:4998`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kockovaella`.
- `curation/seed_scope.tsv:53689` contains this identifier with reason `attested rule: Kockovaella chinensis, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:687`, whose aggregate count is `6` for `NCBITaxon:104677`.
- Complete exact native GOLD expansion found 6 organisms for `Kockovaella chinensis`: `Go0624909`, `Go0624910`, `Go0624911`, `Go0624912`, `Go0624913`, and `Go0624914`.
- Expanding those exact GOLD organisms found no native linked project or analysis rows.
- StrainInfo has 7 exact direct rows and 10 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 4 rows for `NCBITaxon:104677` at lines 3028-3031, covering `CBS 8278` culture-from-type-material variants and `HB 28` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:104677`, `just validate data/taxa/eukaryota/kockovaella_chinensis.yaml`, and `just validate-strict data/taxa/eukaryota/kockovaella_chinensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kockovaella_chinensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
