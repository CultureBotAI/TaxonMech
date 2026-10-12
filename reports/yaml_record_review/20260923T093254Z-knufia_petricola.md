# YAML Record Review: Knufia petricola

- Repository: TaxonMech
- Record: data/taxa/eukaryota/knufia_petricola.yaml
- Started UTC: 2026-09-23T09:32:54Z
- Finished UTC: 2026-09-23T09:32:54Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/knufia_petricola.yaml` denotes the exact NCBI species `Knufia petricola` as `NCBITaxon:206542`, rank `SPECIES`, under genus `NCBITaxon:430999` (`Knufia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and direct GOLD records for this taxon.

## Validation

- `just validate data/taxa/eukaryota/knufia_petricola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/knufia_marmoricola.yaml data/taxa/eukaryota/knufia_petricola.yaml data/taxa/eukaryota/knufia_petricola_cbs_123872.yaml data/taxa/eukaryota/knufia_separata.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:40741` carries `NCBITaxon:206542`, label `Knufia petricola`, rank `SPECIES`, parent `NCBITaxon:430999`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 15 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Knufia`.
- `curation/seed_scope.tsv:54498` contains this identifier with reason `attested rule: Knufia petricola, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old IDs `NCBITaxon:1671130` and `NCBITaxon:93477`, but neither old ID is present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:19731`, whose aggregate count is `1` for `NCBITaxon:206542`.
- The current native GOLD scan found exact organism `Go0384306` for `Knufia petricola MA5790`.
- Expanding that exact GOLD organism found project `Gp0235398` and a native linked analysis row for `Knufia petricola MA5790`.
- StrainInfo has 6 exact direct rows and 6 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 5 rows for `NCBITaxon:206542` at lines 82317-82321, covering `CBS 726.95`, `Ch49`, and `IMI 389175` culture-from-type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:206542`, `just validate data/taxa/eukaryota/knufia_petricola.yaml`, and `just validate-strict data/taxa/eukaryota/knufia_petricola.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `knufia_petricola` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
