# YAML Record Review: Kodamaea hsintzibuensis (nom. inval.)

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kodamaea_hsintzibuensis_nom_inval.yaml
- Started UTC: 2026-09-23T09:44:22Z
- Finished UTC: 2026-09-23T09:44:22Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kodamaea_hsintzibuensis_nom_inval.yaml` denotes the exact NCBI species `Kodamaea hsintzibuensis (nom. inval.)` as `NCBITaxon:1072096`, rank `SPECIES`, under `NCBITaxon:2641443` (`unclassified Kodamaea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kodamaea_hsintzibuensis_nom_inval.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/kodamaea_fungicola.yaml data/taxa/eukaryota/kodamaea_hsintzibuensis_nom_inval.yaml data/taxa/eukaryota/kodamaea_jinghongensis.yaml data/taxa/eukaryota/kodamaea_kakaduensis.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:229713` carries `NCBITaxon:1072096`, label `Kodamaea hsintzibuensis (nom. inval.)`, rank `SPECIES`, parent `NCBITaxon:2641443`, genetic code `12`, and the NCBI synonym set retained in the generated record.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in `unclassified Kodamaea` under genus `Kodamaea`.
- `curation/seed_scope.tsv:57477` contains this identifier with reason `attested rule: Kodamaea hsintzibuensis (nom. inval.), 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old IDs `NCBITaxon:452175` and `NCBITaxon:639325`, but neither old ID is present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:1234`, whose aggregate count is `1` for `NCBITaxon:1072096`.
- The current native GOLD scan found exact organism `Go0704996` for `Kodamaea hsintzibuensis CBS 11427`.
- Expanding that exact GOLD organism found project `Gp0831013`, with no native linked analysis rows.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no rows for `NCBITaxon:1072096`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1072096`, `just validate data/taxa/eukaryota/kodamaea_hsintzibuensis_nom_inval.yaml`, and `just validate-strict data/taxa/eukaryota/kodamaea_hsintzibuensis_nom_inval.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kodamaea_hsintzibuensis_nom_inval` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
