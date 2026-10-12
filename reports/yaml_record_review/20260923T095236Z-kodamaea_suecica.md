# YAML Record Review: Kodamaea suecica

- Repository: TaxonMech
- Record: data/taxa/eukaryota/kodamaea_suecica.yaml
- Started UTC: 2026-09-23T09:52:36Z
- Finished UTC: 2026-09-23T09:52:36Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/kodamaea_suecica.yaml` denotes the exact NCBI species `Kodamaea suecica` as `NCBITaxon:45595`, rank `SPECIES`, under genus `NCBITaxon:77850` (`Kodamaea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/kodamaea_suecica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/kodamaea_restingae.yaml data/taxa/eukaryota/kodamaea_sagamina.yaml data/taxa/eukaryota/kodamaea_suecica.yaml data/taxa/eukaryota/komagataea_norvegica.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:5632` carries `NCBITaxon:45595`, label `Kodamaea suecica`, rank `SPECIES`, parent `NCBITaxon:77850`, genetic code `12`, and the NCBI synonym set retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Kodamaea`.
- `curation/seed_scope.tsv:52678` contains this identifier with reason `attested rule: Kodamaea suecica, 2 sources incl. NCBI`.
- The exact side `ncbi_merged` scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:36087`, whose aggregate count is `1` for `NCBITaxon:45595`.
- The current native GOLD scan found exact organism `Go0705232` for `Kodamaea suecica NRRL Y-12943`.
- Expanding that exact GOLD organism found project `Gp0831260`, with no native linked analysis rows.
- StrainInfo has 1 exact direct row and 12 exact deposit rows but no exact assembly, exclusion, or related-record rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 14 rows for `NCBITaxon:45595` at lines 215646-215659, covering `ATCC 22292`, `BCRC 22619`, `CBS 5724`, `CCRC 22619`, `IFO 10313`, `JCM 7530`, and `NRRL Y-12943` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:45595`, `just validate data/taxa/eukaryota/kodamaea_suecica.yaml`, and `just validate-strict data/taxa/eukaryota/kodamaea_suecica.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `kodamaea_suecica` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
