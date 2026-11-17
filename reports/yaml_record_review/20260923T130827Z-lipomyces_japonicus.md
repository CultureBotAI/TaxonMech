# YAML Record Review: Lipomyces japonicus

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lipomyces_japonicus.yaml
- Started UTC: 2026-09-23T13:08:27Z
- Finished UTC: 2026-09-23T13:08:27Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lipomyces_japonicus.yaml` denotes the exact NCBI species `Lipomyces japonicus` as `NCBITaxon:56871`, rank `SPECIES`, under genus `NCBITaxon:29828` (`Lipomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lipomyces_japonicus.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/lipomyces_doorenjongii.yaml data/taxa/eukaryota/lipomyces_japonicus.yaml data/taxa/eukaryota/lipomyces_kockii.yaml data/taxa/eukaryota/lipomyces_kononenkoae.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:7206` carries `NCBITaxon:56871`, label `Lipomyces japonicus`, rank `SPECIES`, parent `NCBITaxon:29828`, genetic code `1`, one exact synonym, one related synonym, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lipomyces` genus.
- The record preserves the authorship-bearing `Lipomyces japonicus` related synonym from NCBI.
- `curation/seed_scope.tsv:52971` contains this identifier with reason `attested rule: Lipomyces japonicus, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:56871`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39060`, whose aggregate count is `3` for `NCBITaxon:56871`.
- The native GOLD scan found three exact organisms for this NCBI ID: `Go0517141` for strain `NRRL Y-17848`, `Go0583977` for strain `CBS 7319`, and `Go0584005` for strain `NRRL Y-11784`.
- The native GOLD projects scan found five linked projects across those three exact GOLD organisms. The native GOLD analyses scan found one row linked through project `Gp0441179`.
- Exact StrainInfo scans found three direct strain rows and 15 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:236627` through `236637` contain 11 type-material spellings for `Lipomyces japonicus`, covering `CBS 7319`, `JCM 7254`, `MUCL 39413`, `NRRL Y-17357`, and `NRRL Y-17848`. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:56871`, `just validate data/taxa/eukaryota/lipomyces_japonicus.yaml`, and `just validate-strict data/taxa/eukaryota/lipomyces_japonicus.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lipomyces_japonicus` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
