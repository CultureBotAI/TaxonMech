# YAML Record Review: Kregervanrija fluxuum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kregervanrija_fluxuum.yaml
- Started UTC: 2026-09-23T10:08:08Z
- Finished UTC: 2026-09-23T10:08:08Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kregervanrija_fluxuum.yaml` denotes the exact NCBI species `Kregervanrija fluxuum` as `NCBITaxon:324740`, rank `SPECIES`, under genus `NCBITaxon:324738` (`Kregervanrija`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kregervanrija_fluxuum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kregervanrija_delftensis.yaml data/taxa/eukaryota/kregervanrija_fluxuum.yaml data/taxa/eukaryota/kregervanrija_pseudodelftensis.yaml data/taxa/eukaryota/kretzschmaria_clavus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:66300` carries `NCBITaxon:324740`, label `Kregervanrija fluxuum`, rank `SPECIES`, parent `NCBITaxon:324738`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kregervanrija`.
- `curation/seed_scope.tsv:55207` contains this identifier with reason `attested rule: Kregervanrija fluxuum, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:51936` and `NCBITaxon:53651` into this current taxon, but no retained raw NCBI taxon rows exist for those old IDs, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:32126`, whose aggregate count is `1` for `NCBITaxon:324740`.
- The current native GOLD scan found exact organism `Go0517046` for `Kregervanrija fluxuum NRRL YB-4273`.
- Expanding that exact GOLD organism found project `Gp0441084` and the native linked analysis `Kregervanrija fluxuum NRRL YB-4273` through `AP PROJECT GOLD IDS`.
- StrainInfo has 53 exact direct rows and 109 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 37 rows for `NCBITaxon:324740` at lines 177323-177359, covering `ATCC 18823`, `ATCC 9888`, `BCRC 21650`, `CBS 639`, `CCRC 21650`, `IFO 1247`, `JCM 1456`, `NRRL Y-1615`, and `NRRL Y-94` variants under `Candida vini`, plus `CBS 2287`, `NRRL YB4273`, `ATCC 24239`, `BCRC 21530`, `BCRC 22205`, `CCRC 21530`, `CCRC 22205`, `JCM 3646`, `NCYC 544`, and `NRRL YB-4273` variants under `Debaryomyces fluxuum`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:324740`, `just validate data/taxa/eukaryota/kregervanrija_fluxuum.yaml`, and `just validate-strict data/taxa/eukaryota/kregervanrija_fluxuum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kregervanrija_fluxuum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
