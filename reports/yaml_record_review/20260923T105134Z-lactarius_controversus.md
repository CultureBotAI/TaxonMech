# YAML Record Review: Lactarius controversus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lactarius_controversus.yaml
- Started UTC: 2026-09-23T10:51:34Z
- Finished UTC: 2026-09-23T10:51:34Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lactarius_controversus.yaml` denotes the exact NCBI species `Lactarius controversus` as `NCBITaxon:116075`, rank `SPECIES`, under genus `NCBITaxon:34444` (`Lactarius`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lactarius_controversus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lachnum_pygmaeum.yaml data/taxa/eukaryota/lactarius_akahatsu.yaml data/taxa/eukaryota/lactarius_controversus.yaml data/taxa/eukaryota/lactarius_deliciosus.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:21233` carries `NCBITaxon:116075`, label `Lactarius controversus`, rank `SPECIES`, parent `NCBITaxon:34444`, genetic code `1`, and related synonym `Lactarius controversus Pers., 1800`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lactarius`.
- `curation/seed_scope.tsv:53823` contains this identifier with reason `attested rule: Lactarius controversus, 2 sources incl. NCBI`.
- The side-inventory NCBI merged-ID scan found no old IDs for this current taxon, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:3449`, whose aggregate count is `1` for `NCBITaxon:116075`.
- The current native GOLD scan found exact organism `Go0570877` for `Lactarius controversus PMI44`.
- Expanding that exact GOLD organism found projects `Gp0543307` and `Gp0543308`, and no native analysis rows linked through those project IDs.
- Exact StrainInfo scans found 4 direct strains and 4 deposits for this taxon; exact BacDive and generated StrainInfo overlay scans found no corresponding local BacDive-derived rows to emit.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:116075` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:116075`, `just validate data/taxa/eukaryota/lactarius_controversus.yaml`, and `just validate-strict data/taxa/eukaryota/lactarius_controversus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lactarius_controversus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
