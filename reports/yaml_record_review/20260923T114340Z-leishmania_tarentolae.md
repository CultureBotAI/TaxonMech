# YAML Record Review: Leishmania tarentolae

- Repository: TaxonMech
- Record: data/taxa/eukaryota/leishmania_tarentolae.yaml
- Started UTC: 2026-09-23T11:43:40Z
- Finished UTC: 2026-09-23T11:43:40Z
- Verdict: pass

## Target

Generated eukaryote species record `data/taxa/eukaryota/leishmania_tarentolae.yaml` denotes the exact NCBI species `Leishmania tarentolae` as `NCBITaxon:5689`, rank `SPECIES`, under `NCBITaxon:5688` (`lizard Leishmania`). It is an exactly grounded, seeded record attested by NCBI Taxonomy and GOLD.

## Validation

- `just validate data/taxa/eukaryota/leishmania_tarentolae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/leishmania_tarentolae.yaml data/taxa/eukaryota/leishmania_tropica.yaml data/taxa/eukaryota/leishmania_turanica.yaml data/taxa/eukaryota/lentamyces_parricida.yaml` exited successfully.
- Full `just validate-history` and `just verify-corpus` had already passed for this checkout; they were not rerun for this generated record.
- `just validate-products` is not applicable because this generated record has no `causal_graphs`.

## Identity and Grounding

- `data/raw/ncbitaxon_taxa.tsv:2535` carries `NCBITaxon:5689`, label `Leishmania tarentolae`, rank `SPECIES`, parent `NCBITaxon:5688`, genetic code `1`, exact synonym `Sauroleishmania tarentolae`, and snapshot `2026-09-13`.
- The 12 ancestor rows in `lineage` matched the local NCBI inventory with no missing or mismatched labels or ranks, terminating in the expected `lizard Leishmania` clade.
- `curation/seed_scope.tsv:52068` contains this identifier with reason `attested rule: Leishmania tarentolae, 2 sources incl. NCBI`.
- The exact NCBI merge scan found no rows for `NCBITaxon:5689`, matching the absence of `replaces`.

## Evidence

- The NCBI source attestation is supported by the exact target row in `data/raw/ncbitaxon_taxa.tsv`, including snapshot `2026-09-13`.
- The GOLD source attestation is supported by `data/raw/gold_organisms.tsv:39079`, whose aggregate count is `2` for `NCBITaxon:5689`.
- The current native GOLD scan found exact organisms `Go0573437` for `Leishmania tarentolae Parrot Tar II` and `Go0574423` for `Leishmania tarentolae Parrot-TarII`, linked projects `Gp0548089` and `Gp0549118`, and two native analysis rows.
- Exact StrainInfo scans found two direct strains and two deposit rows for this NCBI ID, but exact BacDive scans found no rows and the generated StrainInfo overlay tables have no rows for this taxon.

## Completeness

- Exact scans of the generated raw strain tables found 0 rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Exact scans of the generated StrainInfo overlays found 0 rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.
- Exact scans of the auxiliary taxon tables found no LPSN, GTDB, Madin, MediaDive, or BactoTraits rows for this NCBI ID, matching the absence of `nomenclature` and `taxonomy_mappings`.
- Exact scans found no `NCBITaxon:5689` rows in `data/raw/ncbi_type_material.tsv`, matching the absence of type-material assertions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If the GOLD or NCBI inventories are refreshed, rerun `just seed-canary NCBITaxon:5689`, `just validate data/taxa/eukaryota/leishmania_tarentolae.yaml`, and `just validate-strict data/taxa/eukaryota/leishmania_tarentolae.yaml` on the regenerated record.

## Additional Notes

- No prior exact report for `leishmania_tarentolae` was present under `reports/yaml_record_review/`; the check used `find`, so ignored `reports/` files were included.
- Review source reads, validators, and bounded scans were run in `/private/tmp/taxonmech-codex-review` to avoid interfering with the primary checkout.
