# YAML Record Review: alpha proteobacterium SCGC AAA076-C03

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_c03.yaml
- Started UTC: 2026-09-23T05:42:45Z
- Finished UTC: 2026-09-23T05:44:20Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007109`
- Label: `alpha proteobacterium SCGC AAA076-C03`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:33807` (`unclassified Alphaproteobacteria`)
- Maintained path: generated `data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_c03.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB synonym/xref projection in `src/taxonmech/seed.py`.

The record is a generated NCBI single-cell alpha-proteobacterium placeholder with one GTDB mapping.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/sphingomonas_sp_s17.yaml data/taxa/bacteria/pusillimonas_sp_t7_7.yaml data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_c03.yaml data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_e06.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_c03.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI side is grounded to the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv:210813`: `NCBITaxon:1007109`, label `alpha proteobacterium SCGC AAA076-C03`, rank `SPECIES`, parent `NCBITaxon:33807`, genetic code `11`, sources `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The GTDB projection is over-scoped. `data/raw/gtdb_mappings.tsv:1075` maps the 30-genome `GTDB:s__Amylibacter_sp000153745` cluster to this single-cell NCBI placeholder as `skos:closeMatch`; that same GTDB species cluster is mapped to several other NCBI taxa elsewhere as broad or close matches, so it should not be represented as the exact identity of `SCGC AAA076-C03`.

## Evidence

- `source_attestations` correctly reflects one NCBI name row and one GTDB mapping row with 30 genomes.
- No NCBI synonym column, LPSN row, BacDive strain row, ATB assembly, StrainInfo row, GOLD row, MediaDive row, Madin row, or BactoTraits row was found for `NCBITaxon:1007109` by the exact ignored-file source search, matching the compact generated YAML.
- The GTDB cluster supports an `Amylibacter` species cluster relationship but does not justify emitting `Amylibacter sp000153745` as an `EXACT_SYNONYM` of an unclassified alpha-proteobacterium single-cell placeholder.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-alpha_proteobacterium_scgc_aaa076_c03.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, GTDB species, and GTDB mapping rows needed to review the generated fields.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1075` and `src/taxonmech/seed.py` project the 30-genome `GTDB:s__Amylibacter_sp000153745` species cluster onto the single-cell placeholder `NCBITaxon:1007109` and emit `Amylibacter sp000153745` as an exact synonym. This makes a broad GTDB species-cluster label look like the exact identity of a single environmental record.

## Recommended Edits

- Downgrade or remove the maintained `GTDB:s__Amylibacter_sp000153745` to `NCBITaxon:1007109` close mapping unless curation confirms exact identity.
- Keep GTDB species-cluster labels from becoming exact synonyms on unclassified environmental or single-cell placeholders in `src/taxonmech/seed.py`.
- Regenerate `data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_c03.yaml` after the mapping or generator fix.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_c03.yaml` and `just validate data/taxa/bacteria/alpha_proteobacterium_scgc_aaa076_c03.yaml`.
- Re-run an exact `rg --no-ignore --hidden` for `NCBITaxon:1007109`, `GTDB:s__Amylibacter_sp000153745`, and `alpha_proteobacterium_scgc_aaa076_c03` across `data/raw`, `data/atb`, and `data/straininfo`.
- Manually verify that regenerated YAML retains the NCBI seed identity and no longer emits `Amylibacter sp000153745` as an exact synonym of the SCGC AAA076-C03 placeholder.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
