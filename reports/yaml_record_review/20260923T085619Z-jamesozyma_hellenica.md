# YAML Record Review: Jamesozyma hellenica

- Repository: TaxonMech
- Record: data/taxa/eukaryota/jamesozyma_hellenica.yaml
- Started UTC: 2026-09-23T08:56:19Z
- Finished UTC: 2026-09-23T08:56:19Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/jamesozyma_hellenica.yaml` denotes the exact NCBI species `Jamesozyma hellenica` as `NCBITaxon:473794`, rank `SPECIES`, under genus `NCBITaxon:3162961` (`Jamesozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/jamesozyma_hellenica.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/jamesozyma_hellenica.yaml data/taxa/eukaryota/jamesozyma_jinghongensis.yaml data/taxa/eukaryota/jamesozyma_lodderae.yaml data/taxa/eukaryota/jamesozyma_piceae.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:105775` carries `NCBITaxon:473794`, label `Jamesozyma hellenica`, rank `SPECIES`, parent `NCBITaxon:3162961`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Jamesozyma`.
- `curation/seed_scope.tsv:55772` contains this identifier with reason `attested rule: Jamesozyma hellenica, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old IDs `NCBITaxon:467810`, `NCBITaxon:473795`, and `NCBITaxon:473796`, but none are present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:36508`, whose aggregate count is `1` for `NCBITaxon:473794`.
- The current native GOLD scan found exact organism `Go0705571` for `Jamesozyma hellenica NRRL Y-48844`.
- Expanding that exact GOLD organism found project `Gp0831614`, with no native linked analysis rows.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 12 culture-from-type-material rows for `NCBITaxon:473794` at lines 218776-218787, covering `ATCC MYA-4559`, `CBS 10706`, `D9W17`, `NBRC 103637`, and `NRRL Y-48844` spelling variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:473794`, `just validate data/taxa/eukaryota/jamesozyma_hellenica.yaml`, and `just validate-strict data/taxa/eukaryota/jamesozyma_hellenica.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `jamesozyma_hellenica` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
