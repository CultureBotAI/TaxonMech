# YAML Record Review: Libkindia masarykiana

- Repository: TaxonMech
- Record: data/taxa/eukaryota/libkindia_masarykiana.yaml
- Started UTC: 2026-09-23T12:23:01Z
- Finished UTC: 2026-09-23T12:23:01Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/libkindia_masarykiana.yaml` denotes the exact NCBI species `Libkindia masarykiana` as `NCBITaxon:1882490`, rank `SPECIES`, under genus `NCBITaxon:1927868` (`Libkindia`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/libkindia_masarykiana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/liangdongia_dendrica.yaml data/taxa/eukaryota/liangdongia_dryadoides.yaml data/taxa/eukaryota/liangdongia_quercuum.yaml data/taxa/eukaryota/libkindia_masarykiana.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:490200` carries `NCBITaxon:1882490`, label `Libkindia masarykiana`, rank `SPECIES`, parent `NCBITaxon:1927868`, genetic code `1`, two related synonyms, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `Libkindia` genus.
- `curation/seed_scope.tsv:61429` contains this identifier with reason `attested rule: Libkindia masarykiana, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:16913`, whose aggregate count is `3` for `NCBITaxon:1882490`.
- The current native GOLD scan found exact organisms `Go0619942`, `Go0619943`, and `Go0619944`, with no exact native projects or analysis rows for this NCBI ID.
- Exact StrainInfo scans found 1 direct strain and 1 deposit row for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- `data/raw/ncbi_type_material.tsv:66965` through `66972` contain eight holotype or culture-from-holotype spellings for `Libkindia masarykiana`; the current generated `TaxonRecord` does not embed NCBI type material directly.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD, NCBI, or StrainInfo inventories are refreshed, rerun `just seed-canary NCBITaxon:1882490`, `just validate data/taxa/eukaryota/libkindia_masarykiana.yaml`, and `just validate-strict data/taxa/eukaryota/libkindia_masarykiana.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `libkindia_masarykiana` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
