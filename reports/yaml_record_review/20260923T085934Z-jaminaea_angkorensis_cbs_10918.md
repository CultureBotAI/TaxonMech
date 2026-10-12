# YAML Record Review: Jaminaea angkorensis CBS 10918

- Repository: TaxonMech
- Record: data/taxa/eukaryota/jaminaea_angkorensis_cbs_10918.yaml
- Started UTC: 2026-09-23T08:59:34Z
- Finished UTC: 2026-09-23T08:59:34Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/jaminaea_angkorensis_cbs_10918.yaml` denotes the exact NCBI strain `Jaminaea angkorensis CBS 10918` as `NCBITaxon:1294688`, rank `STRAIN`, under species `NCBITaxon:542766` (`Jaminaea angkorensis`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/jaminaea_angkorensis_cbs_10918.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/jamesozyma_rosinii.yaml data/taxa/eukaryota/jamesozyma_spencerorum.yaml data/taxa/eukaryota/jaminaea_angkorensis_cbs_10918.yaml data/taxa/eukaryota/jaminaea_lanaiensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:304459` carries `NCBITaxon:1294688`, label `Jaminaea angkorensis CBS 10918`, rank `STRAIN`, parent `NCBITaxon:542766`, genetic code `1`, and no synonyms.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, including species `Jaminaea angkorensis` and the no-rank `Microstromatales incertae sedis` parent above genus `Jaminaea`.
- `curation/seed_scope.tsv:58965` contains this identifier with reason `attested rule: Jaminaea angkorensis CBS 10918, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:6937`, whose aggregate count is `1` for `NCBITaxon:1294688`.
- The current native GOLD scan found exact organisms `Go0037759` for `Jaminaea angkorensis CBS 10918` and `Go0618526` for `Jaminaea angkorensis DSM 29587`.
- Expanding those exact GOLD organisms found project `Gp0037759`, with no native linked analysis rows.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no type-material rows for `NCBITaxon:1294688`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1294688`, `just validate data/taxa/eukaryota/jaminaea_angkorensis_cbs_10918.yaml`, and `just validate-strict data/taxa/eukaryota/jaminaea_angkorensis_cbs_10918.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `jaminaea_angkorensis_cbs_10918` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
