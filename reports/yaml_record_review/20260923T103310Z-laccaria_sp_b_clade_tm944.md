# YAML Record Review: Laccaria sp. B clade TM944

- Repository: TaxonMech
- Record: data/taxa/eukaryota/laccaria_sp_b_clade_tm944.yaml
- Started UTC: 2026-09-23T10:33:10Z
- Finished UTC: 2026-09-23T10:33:10Z
- Verdict: pass

## Target

Generated eukaryote species-level placeholder record `data/taxa/eukaryota/laccaria_sp_b_clade_tm944.yaml` denotes the exact NCBI placeholder `Laccaria sp. B clade TM944` as `NCBITaxon:934781`, rank `SPECIES`, under `NCBITaxon:2620704` (`unclassified Laccaria`) within genus `NCBITaxon:29882` (`Laccaria`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/laccaria_sp_b_clade_tm944.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/laccaria_proxima.yaml data/taxa/eukaryota/laccaria_sp.yaml data/taxa/eukaryota/laccaria_sp_b_clade_tm944.yaml data/taxa/eukaryota/laccaria_tortilis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:197777` carries `NCBITaxon:934781`, label `Laccaria sp. B clade TM944`, rank `SPECIES`, parent `NCBITaxon:2620704`, genetic code `1`, and no extra synonyms, matching the generated record.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected no-rank `unclassified Laccaria` node.
- `curation/seed_scope.tsv:56948` contains this identifier with reason `attested rule: Laccaria sp. B clade TM944, 2 sources incl. NCBI`.
- The local NCBI merge side inventory has no old IDs for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:44776`, whose retained aggregate count is `1` for `NCBITaxon:934781`.
- The current native GOLD scan found exact organisms `Go0009678` and `Go0010139` keyed to this NCBI taxon.
- Expanding those exact GOLD organisms found project `Gp0010139`, with no native linked analysis rows.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:934781`, matching the absence of type-material derived strain assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:934781`, `just validate data/taxa/eukaryota/laccaria_sp_b_clade_tm944.yaml`, and `just validate-strict data/taxa/eukaryota/laccaria_sp_b_clade_tm944.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `laccaria_sp_b_clade_tm944` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD exact rows are side evidence only and can differ from the retained aggregate used to generate source attestations.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
