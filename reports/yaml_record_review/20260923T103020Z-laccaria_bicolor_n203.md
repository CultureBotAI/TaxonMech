# YAML Record Review: Laccaria bicolor N203

- Repository: TaxonMech
- Record: data/taxa/eukaryota/laccaria_bicolor_n203.yaml
- Started UTC: 2026-09-23T10:30:20Z
- Finished UTC: 2026-09-23T10:30:20Z
- Verdict: pass

## Target

Generated eukaryote strain record `data/taxa/eukaryota/laccaria_bicolor_n203.yaml` denotes the exact NCBI strain `Laccaria bicolor N203` as `NCBITaxon:980499`, rank `STRAIN`, under species `NCBITaxon:29883` (`Laccaria bicolor`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/laccaria_bicolor_n203.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/laccaria_amethystina.yaml data/taxa/eukaryota/laccaria_bicolor.yaml data/taxa/eukaryota/laccaria_bicolor_n203.yaml data/taxa/eukaryota/laccaria_laccata.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:204448` carries `NCBITaxon:980499`, label `Laccaria bicolor N203`, rank `STRAIN`, parent `NCBITaxon:29883`, genetic code `1`, and no extra synonyms, matching the generated record.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected species `Laccaria bicolor`.
- `curation/seed_scope.tsv:57068` contains this identifier with reason `attested rule: Laccaria bicolor N203, 2 sources incl. NCBI`.
- The local NCBI merge side inventory has no old IDs for this target, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:45221`, whose aggregate count is `1` for `NCBITaxon:980499`.
- The current native GOLD scan found exact organism `Go0072797` carrying `ORGANISM NCBI TAX ID` `980499`.
- Expanding that exact GOLD organism found projects `Gp0332673`, `Gp0332674`, `Gp0332675`, and `Gp0332676`, with no native linked analysis rows.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 0 rows for `NCBITaxon:980499`, matching the absence of type-material derived strain assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:980499`, `just validate data/taxa/eukaryota/laccaria_bicolor_n203.yaml`, and `just validate-strict data/taxa/eukaryota/laccaria_bicolor_n203.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `laccaria_bicolor_n203` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Native GOLD currently names the exact NCBI-keyed organism only as `Laccaria bicolor`; the generated record follows the explicit NCBI Taxonomy row and GOLD aggregate keyed to `NCBITaxon:980499`.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
