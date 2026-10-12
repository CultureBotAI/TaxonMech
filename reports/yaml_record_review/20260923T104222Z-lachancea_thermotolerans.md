# YAML Record Review: Lachancea thermotolerans

- Repository: TaxonMech
- Record: data/taxa/eukaryota/lachancea_thermotolerans.yaml
- Started UTC: 2026-09-23T10:42:22Z
- Finished UTC: 2026-09-23T10:42:22Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/lachancea_thermotolerans.yaml` denotes the exact NCBI species `Lachancea thermotolerans` as `NCBITaxon:381046`, rank `SPECIES`, under genus `NCBITaxon:300275` (`Lachancea`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/lachancea_thermotolerans.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/lachancea_nothofagi.yaml data/taxa/eukaryota/lachancea_quebecensis.yaml data/taxa/eukaryota/lachancea_sp_fantastica.yaml data/taxa/eukaryota/lachancea_thermotolerans.yaml` scanned 4 files with 0 ERROR rows.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:80118` carries `NCBITaxon:381046`, label `Lachancea thermotolerans`, rank `SPECIES`, parent `NCBITaxon:300275`, genetic code `1`, exact synonyms `Kluyveromyces thermotolerans` and `Zygosaccharomyces thermotolerans`, and the related synonyms retained in the generated record.
- The 13 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected genus `Lachancea`.
- `curation/seed_scope.tsv:55443` contains this identifier with reason `attested rule: Lachancea thermotolerans, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv:81780` maps side-inventory old ID `NCBITaxon:4916` into this current taxon, but no retained raw NCBI taxon row exists for that old ID, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:33900`, whose aggregate count is `1` for `NCBITaxon:381046`.
- The current native GOLD scan found exact organism `Go0705666` for `Lachancea thermotolerans NRRL Y-8284`.
- Expanding that exact GOLD organism found project `Gp0831718` and no native analysis rows linked through that project ID.
- Exact StrainInfo scans found 60 direct strains and 119 deposits for this taxon. The generated StrainInfo overlay scan found two related-record rows for `straininfo.strain:63233` / `straininfo.deposit:867846`, both matched through `kgmicrobe.strain:JCM-15486` to `kgmicrobe.strain:bacdive_4177`.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 2 rows in `data/straininfo/related_records.tsv.gz` at lines 214008-214009 and 0 rows in `data/straininfo/assemblies.tsv` or `data/straininfo/exclusions.tsv`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact `data/raw/ncbi_type_material.tsv` search found 17 rows for `NCBITaxon:381046` at lines 199676-199692, covering `CBS 6340`, `NRRL Y-8284`, `ATCC 56472`, `DBVPG 6232`, `IFO 1985`, `NRRL Y-12664`, and `VKM Y-894` type-material variants.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:381046`, `just validate data/taxa/eukaryota/lachancea_thermotolerans.yaml`, and `just validate-strict data/taxa/eukaryota/lachancea_thermotolerans.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `lachancea_thermotolerans` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
