# YAML Record Review: Lipomyces mesembrius

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_mesembrius.yaml
- Started UTC: 2026-09-23T13:13:04Z
- Finished UTC: 2026-09-23T13:13:04Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_mesembrius.yaml` denotes the exact NCBI species `Lipomyces mesembrius` as `NCBITaxon:56874`, rank `SPECIES`, under genus `NCBITaxon:29828` (`Lipomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_mesembrius.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lipomyces_lipofer.yaml data/taxa/eukaryota/lipomyces_mesembrius.yaml data/taxa/eukaryota/lipomyces_oligophaga.yaml data/taxa/eukaryota/lipomyces_orientalis.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7208` carries `NCBITaxon:56874`, label `Lipomyces mesembrius`, rank `SPECIES`, parent `NCBITaxon:29828`, genetic code `1`, one exact synonym, one related synonym, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces` genus.
- The record preserves `Lipomyces starkeyi a` as an exact synonym and the authorship-bearing `Lipomyces mesembrius` name as a related synonym from NCBI.
- `curation/seed_scope.tsv:52973` contains this identifier with reason `attested rule: Lipomyces mesembrius, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:56874`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39062`, whose aggregate count is `2` for `NCBITaxon:56874`.
- The native GOLD scan found two exact organisms for this NCBI ID: `Go0517144` for strain `NRRL Y-27506` and `Go0583978` for strain `CBS 7600`.
- The native GOLD projects scan found three linked projects across those two exact GOLD organisms. The native GOLD analyses scan found one row linked through project `Gp0441182`.
- Exact StrainInfo scans found two direct strain rows and eight deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:236646` through `236652` contain seven type-material spellings for `Lipomyces mesembrius`, covering `CBS 7661` as culture from holotype and `MUCL 39419` plus `NRRL Y-27506` as type material. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:56874`, `just validate data/taxa/eukaryota/lipomyces_mesembrius.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_mesembrius.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_mesembrius` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
