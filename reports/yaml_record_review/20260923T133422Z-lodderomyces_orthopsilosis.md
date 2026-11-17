# YAML Record Review: Lodderomyces orthopsilosis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lodderomyces_orthopsilosis.yaml
- Started UTC: 2026-09-23T13:34:22Z
- Finished UTC: 2026-09-23T13:34:22Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lodderomyces_orthopsilosis.yaml` denotes the exact NCBI species `Lodderomyces orthopsilosis` as `NCBITaxon:273371`, rank `SPECIES`, under genus `NCBITaxon:36913` (`Lodderomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD records filed directly under this taxon.

## Validation

- `just validate data/taxa/eukaryota/lodderomyces_orthopsilosis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lodderomyces_orthopsilosis.yaml data/taxa/eukaryota/lodderomyces_orthopsilosis_ay2.yaml data/taxa/eukaryota/lodderomyces_orthopsilosis_co_90_125.yaml data/taxa/eukaryota/lodderomyces_oxycetoniae.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:56420` carries `NCBITaxon:273371`, label `Lodderomyces orthopsilosis`, rank `SPECIES`, parent `NCBITaxon:36913`, genetic code `12`, two exact synonyms, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lodderomyces` genus.
- The record preserves `Candida orthopsilosis` and `Candida parapsilosis group II` as exact synonyms and both authorship-bearing names as related synonyms from NCBI.
- `curation/seed_scope.tsv:54928` contains this identifier with reason `attested rule: Lodderomyces orthopsilosis, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:273371`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:25489`, whose aggregate count is `4` for direct `NCBITaxon:273371` organism rows; descendant strain taxa are not gathered.
- The native GOLD scan found four exact organisms for this NCBI ID: `Go0454334`, `Go0516654`, `Go0657828`, and `Go0705541`.
- The native GOLD projects scan found one linked project for each exact GOLD organism, and the native GOLD analyses scan found two rows linked through projects `Gp0702096` and `Gp0322641`.
- Exact StrainInfo scans found 15 direct strain rows and 17 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:115339` through `115347` contain nine type-material spellings for `Candida orthopsilosis`, covering `CBS 10906` and `NRRL Y-48468` as cultures from holotype plus `ATCC 96139` as holotype. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:273371`, `just validate data/taxa/eukaryota/lodderomyces_orthopsilosis.yaml`, and `just validate-strict data/taxa/eukaryota/lodderomyces_orthopsilosis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lodderomyces_orthopsilosis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
