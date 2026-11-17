# YAML Record Review: Knufia marmoricola

- Repository: TaxonMech
- Record: data/taxa/eukaryota/knufia_marmoricola.yaml
- Started UTC: 2026-09-23T09:32:54Z
- Finished UTC: 2026-09-23T09:32:54Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/knufia_marmoricola.yaml` denotes the exact NCBI species `Knufia marmoricola` as `NCBITaxon:1690601`, rank `SPECIES`, under genus `NCBITaxon:430999` (`Knufia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/knufia_marmoricola.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/knufia_marmoricola.yaml data/taxa/eukaryota/knufia_petricola.yaml data/taxa/eukaryota/knufia_petricola_cbs_123872.yaml data/taxa/eukaryota/knufia_separata.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:441159` carries `NCBITaxon:1690601`, label `Knufia marmoricola`, rank `SPECIES`, parent `NCBITaxon:430999`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Knufia`.
- `curation/seed_scope.tsv:61025` contains this identifier with reason `attested rule: Knufia marmoricola, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:14597`, whose aggregate count is `1` for `NCBITaxon:1690601`.
- The current native GOLD scan found exact organism `Go0583378` for `Knufia marmoricola CCFEE 5895`.
- Expanding that exact GOLD organism found projects `Gp0587341` and `Gp0891530`, with no native linked analysis rows.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 4 rows for `NCBITaxon:1690601` at lines 52612-52615, covering `CBS 139726` and `CCFEE 5895` culture-from-holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1690601`, `just validate data/taxa/eukaryota/knufia_marmoricola.yaml`, and `just validate-strict data/taxa/eukaryota/knufia_marmoricola.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `knufia_marmoricola` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
