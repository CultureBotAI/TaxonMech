# YAML Record Review: Jamesozyma rosinii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/jamesozyma_rosinii.yaml
- Started UTC: 2026-09-23T08:59:34Z
- Finished UTC: 2026-09-23T08:59:34Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/jamesozyma_rosinii.yaml` denotes the exact NCBI species `Jamesozyma rosinii` as `NCBITaxon:56413`, rank `SPECIES`, under genus `NCBITaxon:3162961` (`Jamesozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/jamesozyma_rosinii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/jamesozyma_rosinii.yaml data/taxa/eukaryota/jamesozyma_spencerorum.yaml data/taxa/eukaryota/jaminaea_angkorensis_cbs_10918.yaml data/taxa/eukaryota/jaminaea_lanaiensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7089` carries `NCBITaxon:56413`, label `Jamesozyma rosinii`, rank `SPECIES`, parent `NCBITaxon:3162961`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Jamesozyma`.
- `curation/seed_scope.tsv:52958` contains this identifier with reason `attested rule: Jamesozyma rosinii, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:38917`, whose aggregate count is `1` for `NCBITaxon:56413`.
- The current native GOLD scan found exact organism `Go0517029` for `Kazachstania rosinii NRRL Y-17919` and project `Gp0441067`.
- The native GOLD analysis scan found one exact linked analysis, `Kazachstania rosinii NRRL Y-17919`, through project `Gp0441067`.
- StrainInfo has 3 exact direct rows and 21 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 20 type-material rows for `NCBITaxon:56413` at lines 235955-235974, covering `BCRC 21424`, `CBS 7127`, `CCRC 21424`, `DBVP 6747`, `DBVPG 6747`, `IFO 10008`, `NRRL Y-17919`, and `UCD-FST 01-154` spelling variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:56413`, `just validate data/taxa/eukaryota/jamesozyma_rosinii.yaml`, and `just validate-strict data/taxa/eukaryota/jamesozyma_rosinii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `jamesozyma_rosinii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
