# YAML Record Review: Kockovaella imperatae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kockovaella_imperatae.yaml
- Started UTC: 2026-09-23T09:35:32Z
- Finished UTC: 2026-09-23T09:35:32Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kockovaella_imperatae.yaml` denotes the exact NCBI species `Kockovaella imperatae` as `NCBITaxon:4999`, rank `SPECIES`, under genus `NCBITaxon:4998` (`Kockovaella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kockovaella_imperatae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/knufia_sp.yaml data/taxa/eukaryota/kockiozyma_suomiensis.yaml data/taxa/eukaryota/kockovaella_chinensis.yaml data/taxa/eukaryota/kockovaella_imperatae.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2178` carries `NCBITaxon:4999`, label `Kockovaella imperatae`, rank `SPECIES`, parent `NCBITaxon:4998`, genetic code `1`, and the NCBI synonym retained in the generated record.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kockovaella`.
- `curation/seed_scope.tsv:51902` contains this identifier with reason `attested rule: Kockovaella imperatae, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:37294`, whose aggregate count is `1` for `NCBITaxon:4999`.
- The current native GOLD scan found exact organism `Go0115733` for `Kockovaella imperatae NRRL Y-17943`.
- Expanding that exact GOLD organism found projects `Gp0120011` and `Gp0120012`; native linked analysis expansion found two rows for `Kockovaella imperatae NRRL Y-17943 Standard Draft` through `Gp0120011`.
- StrainInfo has 1 exact direct row and 12 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 8 rows for `NCBITaxon:4999` at lines 224510-224517, covering `CBS 7554` culture-from-type-material variants plus `IFO 10522`, `IGC 5360`, and `JCM 7826` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:4999`, `just validate data/taxa/eukaryota/kockovaella_imperatae.yaml`, and `just validate-strict data/taxa/eukaryota/kockovaella_imperatae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kockovaella_imperatae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
