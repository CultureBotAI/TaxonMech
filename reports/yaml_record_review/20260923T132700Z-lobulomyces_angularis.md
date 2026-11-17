# YAML Record Review: Lobulomyces angularis

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lobulomyces_angularis.yaml
- Started UTC: 2026-09-23T13:27:00Z
- Finished UTC: 2026-09-23T13:27:00Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lobulomyces_angularis.yaml` denotes the exact NCBI species `Lobulomyces angularis` as `NCBITaxon:109889`, rank `SPECIES`, under genus `NCBITaxon:642604` (`Lobulomyces`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lobulomyces_angularis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lizonia_empirigonia.yaml data/taxa/eukaryota/lobaria_pulmonaria.yaml data/taxa/eukaryota/lobosporangium_transversale.yaml data/taxa/eukaryota/lobulomyces_angularis.yaml` reported 0 total ERROR rows while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:19731` carries `NCBITaxon:109889`, label `Lobulomyces angularis`, rank `SPECIES`, parent `NCBITaxon:642604`, genetic code `1`, one exact synonym, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Lobulomyces` genus.
- The record preserves `Chytriomyces angularis` as an exact synonym and both authorship-bearing names as related synonyms from NCBI.
- `curation/seed_scope.tsv:53748` contains this identifier with reason `attested rule: Lobulomyces angularis, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:109889`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:1835`, whose aggregate count is `1` for `NCBITaxon:109889`.
- The native GOLD scan found one exact organism for this NCBI ID, `Go0389722`, for strain `JEL45`.
- The native GOLD projects scan found two linked projects for `Go0389722` and no analyses linked through their project IDs.
- Exact BacDive and StrainInfo scans found no rows for this NCBI ID.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:6281` through `6284` contain four reference-material spellings for `Chytriomyces angularis`: `AFTOL-ID 630`, `AFTOL-ID:630`, `JEL 45`, and `JEL:45`. The current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:109889`, `just validate data/taxa/eukaryota/lobulomyces_angularis.yaml`, and `just validate-strict data/taxa/eukaryota/lobulomyces_angularis.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lobulomyces_angularis` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
