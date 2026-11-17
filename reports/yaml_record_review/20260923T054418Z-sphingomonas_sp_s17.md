# YAML Record Review: Sphingomonas sp. S17

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/sphingomonas_sp_s17.yaml
- Started UTC: 2026-09-23T05:42:45Z
- Finished UTC: 2026-09-23T05:44:18Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007104`
- Label: `Sphingomonas sp. S17`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:196159` (`unclassified Sphingomonas`)
- Maintained path: generated `data/taxa/bacteria/sphingomonas_sp_s17.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB synonym/xref projection in `src/taxonmech/seed.py`.

The record is a compact generated NCBI placeholder species attested by NCBI, GTDB, and Madin rows.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/sphingomonas_sp_s17.yaml data/taxa/bacteria/pusillimonas_sp_t7_7.yaml data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_c03.yaml data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_e06.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/sphingomonas_sp_s17.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI side is grounded to the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv:210811`: `NCBITaxon:1007104`, label `Sphingomonas sp. S17`, rank `SPECIES`, parent `NCBITaxon:196159`, genetic code `11`, sources `ncbitaxon|gtdb|madin_etal`, and snapshot date `2026-09-13`.

The GTDB projection is over-scoped. `data/raw/gtdb_mappings.tsv:1073` maps the 24-genome species cluster `GTDB:s__Sphingomonas_paucimobilis` to the placeholder S17 NCBI species as `skos:closeMatch`, then `src/taxonmech/seed.py` emits `Sphingomonas paucimobilis` as a GTDB `EXACT_SYNONYM`. The local LPSN row in `data/raw/lpsn_names.tsv:19895` instead grounds `Sphingomonas paucimobilis` as a legitimate, validly published, correct ICNP species linked to `NCBITaxon:13689`.

## Evidence

- `source_attestations` correctly reflects one NCBI name row, one GTDB mapping row with 24 genomes, and five Madin trait assertions.
- No NCBI synonym column, LPSN row, BacDive strain row, ATB assembly, StrainInfo row, GOLD row, MediaDive row, or BactoTraits row was found for `NCBITaxon:1007104` by the exact ignored-file source search, matching the compact generated YAML.
- The `GTDB:s__Sphingomonas_paucimobilis` row supports a broad relationship to the S17 placeholder at most; it does not support using an ICNP species name as an exact synonym for an unclassified isolate placeholder.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-sphingomonas_sp_s17.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, GTDB, Madin, and distinct `Sphingomonas paucimobilis` LPSN rows needed to review the generated fields.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1073` and `src/taxonmech/seed.py` project the 24-genome `GTDB:s__Sphingomonas_paucimobilis` species cluster onto the placeholder `Sphingomonas sp. S17` NCBI species and emit `Sphingomonas paucimobilis` as an `EXACT_SYNONYM`, even though the same name is grounded locally as the separate LPSN/NCBI species `NCBITaxon:13689`.

## Recommended Edits

- Fix the maintained GTDB mapping input so `GTDB:s__Sphingomonas_paucimobilis` is not emitted as a close match for `NCBITaxon:1007104`.
- Keep GTDB projection in `src/taxonmech/seed.py` from turning GTDB species labels into exact synonyms when the target is an NCBI unclassified placeholder or when the name is grounded to a distinct LPSN/NCBI species.
- Regenerate `data/taxa/bacteria/sphingomonas_sp_s17.yaml` after the mapping or generator fix.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/sphingomonas_sp_s17.yaml` and `just validate data/taxa/bacteria/sphingomonas_sp_s17.yaml`.
- Re-run an exact `rg --no-ignore --hidden` for `NCBITaxon:1007104`, `GTDB:s__Sphingomonas_paucimobilis`, and `sphingomonas_sp_s17` across `data/raw`, `data/atb`, and `data/straininfo`.
- Verify that the regenerated YAML retains the NCBI and Madin evidence but no longer emits `Sphingomonas paucimobilis` as a GTDB exact synonym.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
