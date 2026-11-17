# YAML Record Review: Fidelibacterota bacterium SCGC AAA076-M08

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa076_m08.yaml
- Started UTC: 2026-09-23T05:51:31Z
- Finished UTC: 2026-09-23T05:52:58Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007124`
- Label: `Fidelibacterota bacterium SCGC AAA076-M08`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:3106486` (`unclassified Fidelibacterota`)
- Maintained path: generated `data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa076_m08.yaml`; fixes, if any, would belong in the source inventories or generator, not by hand in the generated YAML.

The record is a generated NCBI single-cell Fidelibacterota placeholder with one NCBI exact synonym and one GOLD organism attestation.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/candidatus_neomarinimicrobium_atlanticum.yaml data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa076_m08.yaml data/taxa/bacteria/magnetospirillum_sp_pmbn1.yaml data/taxa/bacteria/acinetobacter_sp_wr1b02.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa076_m08.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI side is grounded to the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv:210828`: `NCBITaxon:1007124`, label `Fidelibacterota bacterium SCGC AAA076-M08`, rank `SPECIES`, parent `NCBITaxon:3106486`, genetic code `11`, exact synonym `SAR406 cluster bacterium SCGC AAA076-M08`, sources `ncbitaxon|gold`, and snapshot date `2026-09-13`.

The lineage correctly places the placeholder under `Fidelibacterota` and `unclassified Fidelibacterota`, and no GTDB, LPSN, strain, genome, or trait fields are projected into the YAML.

## Evidence

- `source_attestations` correctly contains one NCBI name assertion and one GOLD organism assertion.
- The `SAR406 cluster bacterium SCGC AAA076-M08` exact synonym is supported by the NCBI synonym column.
- No GTDB, LPSN, BacDive, ATB, StrainInfo, MediaDive, Madin, or BactoTraits rows were found for `NCBITaxon:1007124` by the exact ignored-file source search.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-fidelibacterota_bacterium_scgc_aaa076_m08.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found only the PATHS, NCBI, and GOLD rows for `NCBITaxon:1007124`, so the missing auxiliary sections were checked against ignored and non-ignored local source files.

## Findings

No curation findings.

## Recommended Edits

No edits recommended.

## Follow-up Checks

- No follow-up is required for this record beyond normal regeneration QA.
- If the source inventories or generator change, rerun `just validate-strict data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa076_m08.yaml` and `just validate data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa076_m08.yaml`.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
