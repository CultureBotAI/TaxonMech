# YAML Record Review: Kellermania agaves

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kellermania_agaves.yaml
- Started UTC: 2026-09-23T09:16:39Z
- Finished UTC: 2026-09-23T09:16:39Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kellermania_agaves.yaml` denotes the exact NCBI species `Kellermania agaves` as `NCBITaxon:1414626`, rank `SPECIES`, under genus `NCBITaxon:1248177` (`Kellermania`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kellermania_agaves.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kazachstania_viticola.yaml data/taxa/eukaryota/kellermania_agaves.yaml data/taxa/eukaryota/keqinozyma_nonsorbophila.yaml data/taxa/eukaryota/khoyollomyces_ramosus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:350754` carries `NCBITaxon:1414626`, label `Kellermania agaves`, rank `SPECIES`, parent `NCBITaxon:1248177`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 16 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kellermania`.
- `curation/seed_scope.tsv:60053` contains this identifier with reason `attested rule: Kellermania agaves, 2 sources incl. NCBI`.
- No exact retained retired rows or side `ncbi_merged` rows were found for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:10030`, whose aggregate count is `1` for `NCBITaxon:1414626`.
- The current native GOLD scan found no exact organism, project, or analysis rows for `NCBITaxon:1414626`.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 6 rows for `NCBITaxon:1414626` at lines 29505-29510: `CBS 136430` and `CPC 21713` cultures from holotype plus `CBS H-21439` holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1414626`, `just validate data/taxa/eukaryota/kellermania_agaves.yaml`, and `just validate-strict data/taxa/eukaryota/kellermania_agaves.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kellermania_agaves` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
