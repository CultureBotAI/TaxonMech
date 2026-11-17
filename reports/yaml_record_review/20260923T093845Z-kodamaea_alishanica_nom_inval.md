# YAML Record Review: Kodamaea alishanica (nom. inval.)

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kodamaea_alishanica_nom_inval.yaml
- Started UTC: 2026-09-23T09:38:45Z
- Finished UTC: 2026-09-23T09:38:45Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kodamaea_alishanica_nom_inval.yaml` denotes the exact NCBI species `Kodamaea alishanica (nom. inval.)` as `NCBITaxon:1072094`, rank `SPECIES`, under `NCBITaxon:2641443` (`unclassified Kodamaea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kodamaea_alishanica_nom_inval.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kockovaella_lichenicola.yaml data/taxa/eukaryota/kockovaella_prillingeri.yaml data/taxa/eukaryota/kockovaella_sichuanensis.yaml data/taxa/eukaryota/kodamaea_alishanica_nom_inval.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:229711` carries `NCBITaxon:1072094`, label `Kodamaea alishanica (nom. inval.)`, rank `SPECIES`, parent `NCBITaxon:2641443`, genetic code `12`, and the NCBI synonym set retained in the generated record.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in `unclassified Kodamaea` under genus `Kodamaea`.
- `curation/seed_scope.tsv:57475` contains this identifier with reason `attested rule: Kodamaea alishanica (nom. inval.), 2 sources incl. NCBI`.
- Side `ncbi_merged` rows list old IDs `NCBITaxon:599725` and `NCBITaxon:599727`, but neither old ID is present in the retained retired taxa inventory, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:1232`, whose aggregate count is `1` for `NCBITaxon:1072094`.
- The current native GOLD scan found exact organism `Go0704997` for `Kodamaea alishanica CBS 11429`.
- Expanding that exact GOLD organism found project `Gp0831014`, with no native linked analysis rows.
- StrainInfo has no exact direct, deposit, assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found no rows for `NCBITaxon:1072094`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1072094`, `just validate data/taxa/eukaryota/kodamaea_alishanica_nom_inval.yaml`, and `just validate-strict data/taxa/eukaryota/kodamaea_alishanica_nom_inval.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kodamaea_alishanica_nom_inval` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
