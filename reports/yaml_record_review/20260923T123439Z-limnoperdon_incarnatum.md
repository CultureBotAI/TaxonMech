# YAML Record Review: Limnoperdon incarnatum

- Repository: TaxonMech
- Record: data/taxa/eukaryota/limnoperdon_incarnatum.yaml
- Started UTC: 2026-09-23T12:34:39Z
- Finished UTC: 2026-09-23T12:34:39Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/limnoperdon_incarnatum.yaml` denotes the exact NCBI species `Limnoperdon incarnatum` as `NCBITaxon:175175`, rank `SPECIES`, under genus `NCBITaxon:175174` (`Limnoperdon`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/limnoperdon_incarnatum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/licmophora_paradoxa.yaml data/taxa/eukaryota/licmophora_sp.yaml data/taxa/eukaryota/liebetanzomyces_polymorphus.yaml data/taxa/eukaryota/limnoperdon_incarnatum.yaml` exited successfully while scanning this 4-record batch.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:35536` carries `NCBITaxon:175175`, label `Limnoperdon incarnatum`, rank `SPECIES`, parent `NCBITaxon:175174`, genetic code `1`, one related synonym, `attested_by` value `gold`, and snapshot `2026-09-13`.
- The 14 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Limnoperdon` genus.
- `curation/seed_scope.tsv:54284` contains this identifier with reason `attested rule: Limnoperdon incarnatum, 2 sources incl. NCBI`.
- The side NCBI merge scan found no retired IDs for `NCBITaxon:175175`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:15231`, whose aggregate count is `4` for `NCBITaxon:175175`.
- The current native GOLD scan found four exact organism rows, with no linked project or analysis rows in the compressed GOLD files.
- Exact StrainInfo scans found 9 direct strains and 18 deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no NCBI type-material rows for `NCBITaxon:175175`, matching the absence of embedded type-material evidence.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:175175`, `just validate data/taxa/eukaryota/limnoperdon_incarnatum.yaml`, and `just validate-strict data/taxa/eukaryota/limnoperdon_incarnatum.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `limnoperdon_incarnatum` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
