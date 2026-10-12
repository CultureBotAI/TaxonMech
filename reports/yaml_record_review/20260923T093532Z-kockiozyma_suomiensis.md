# YAML Record Review: Kockiozyma suomiensis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kockiozyma_suomiensis.yaml
- Started UTC: 2026-09-23T09:35:32Z
- Finished UTC: 2026-09-23T09:35:32Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kockiozyma_suomiensis.yaml` denotes the exact NCBI species `Kockiozyma suomiensis` as `NCBITaxon:1337062`, rank `SPECIES`, under genus `NCBITaxon:2861358` (`Kockiozyma`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kockiozyma_suomiensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/knufia_sp.yaml data/taxa/eukaryota/kockiozyma_suomiensis.yaml data/taxa/eukaryota/kockovaella_chinensis.yaml data/taxa/eukaryota/kockovaella_imperatae.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:320405` carries `NCBITaxon:1337062`, label `Kockiozyma suomiensis`, rank `SPECIES`, parent `NCBITaxon:2861358`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kockiozyma`.
- `curation/seed_scope.tsv:59535` contains this identifier with reason `attested rule: Kockiozyma suomiensis, 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old ID `NCBITaxon:56420`, but that old ID is not present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:8175`, whose aggregate count is `1` for `NCBITaxon:1337062`.
- The current native GOLD scan found exact organism `Go0517146` for `Kockiozyma suomiensis NRRL Y-17356`.
- Expanding that exact GOLD organism found projects `Gp0588862` and `Gp0595913`, with no native linked analysis rows.
- StrainInfo has 1 exact direct row and 10 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 14 rows for `NCBITaxon:1337062` at lines 23865-23878, covering `ATCC 66546`, `BCRC 22226`, `CBS 7251`, `CCRC 22226`, `IFO 10920`, `NCYC 2392`, and `NRRL Y-17356` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1337062`, `just validate data/taxa/eukaryota/kockiozyma_suomiensis.yaml`, and `just validate-strict data/taxa/eukaryota/kockiozyma_suomiensis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kockiozyma_suomiensis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
