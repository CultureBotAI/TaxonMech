# YAML Record Review: Linnemannia schmuckeri

- Repository: TaxonMech
- Record: data/taxa/eukaryota/linnemannia_schmuckeri.yaml
- Started UTC: 2026-09-23T12:58:56Z
- Finished UTC: 2026-09-23T12:58:56Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/linnemannia_schmuckeri.yaml` denotes the exact NCBI species `Linnemannia schmuckeri` as `NCBITaxon:64567`, rank `SPECIES`, under genus `NCBITaxon:2779861` (`Linnemannia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/linnemannia_schmuckeri.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/linnemannia_hyalina.yaml data/taxa/eukaryota/linnemannia_nantahalensis.yaml data/taxa/eukaryota/linnemannia_schmuckeri.yaml data/taxa/eukaryota/linnemannia_sclerotiella.yaml` exited successfully while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:8189` carries `NCBITaxon:64567`, label `Linnemannia schmuckeri`, rank `SPECIES`, parent `NCBITaxon:2779861`, genetic code `1`, one exact synonym, two related synonyms, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Linnemannia` genus.
- `curation/seed_scope.tsv:53095` contains this identifier with reason `attested rule: Linnemannia schmuckeri, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:64567`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:40339`, whose aggregate count is `2` for `NCBITaxon:64567`.
- The current native GOLD scan found two exact organism rows, two exact projects, and no native analysis rows for this NCBI ID.
- Exact StrainInfo scans found 5 direct strains and 7 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:244464` through `244467` contain four culture-from-syntype spellings for `Mortierella schmuckeri`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:64567`, `just validate data/taxa/eukaryota/linnemannia_schmuckeri.yaml`, and `just validate-strict data/taxa/eukaryota/linnemannia_schmuckeri.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `linnemannia_schmuckeri` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
