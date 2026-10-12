# YAML Record Review: Komagataella kurtzmanii

- Repository: TaxonMech
- Record: data/taxa/eukaryota/komagataella_kurtzmanii.yaml
- Started UTC: 2026-09-23T09:59:38Z
- Finished UTC: 2026-09-23T09:59:38Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/komagataella_kurtzmanii.yaml` denotes the exact NCBI species `Komagataella kurtzmanii` as `NCBITaxon:1342318`, rank `SPECIES`, under genus `NCBITaxon:460517` (`Komagataella`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/komagataella_kurtzmanii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/komagataella_kurtzmanii.yaml data/taxa/eukaryota/komagataella_mondaviorum.yaml data/taxa/eukaryota/komagataella_pastoris.yaml data/taxa/eukaryota/komagataella_pastoris_dsmz_70382.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:322587` carries `NCBITaxon:1342318`, label `Komagataella kurtzmanii`, rank `SPECIES`, parent `NCBITaxon:460517`, genetic code `1`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Komagataella`.
- `curation/seed_scope.tsv:59572` contains this identifier with reason `attested rule: Komagataella kurtzmanii, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:8348`, whose aggregate count is `2` for `NCBITaxon:1342318`.
- The current native GOLD scan found exact organisms `Go0681687` for `Komagataella kurtzmanii CBS 12817` and `Go0705589` for `Komagataella kurtzmanii NRRL Y-63667`.
- Expanding those exact GOLD organisms found projects `Gp0783737` and `Gp0831633`, with one native linked analysis for `Komagataella kurtzmanii CBS 12817` through `AP PROJECT GOLD IDS`.
- Exact BacDive and StrainInfo scans found no native rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 14 rows for `NCBITaxon:1342318` at lines 24241-24254, covering `CBS 12817`, `KBP Y-2878`, `NRRL Y-63667`, `Starmer #75-208.2`, and `UCD-FST 76-20` culture-from-holotype variants plus `VKPM Y-727` holotype variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:1342318`, `just validate data/taxa/eukaryota/komagataella_kurtzmanii.yaml`, and `just validate-strict data/taxa/eukaryota/komagataella_kurtzmanii.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `komagataella_kurtzmanii` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
