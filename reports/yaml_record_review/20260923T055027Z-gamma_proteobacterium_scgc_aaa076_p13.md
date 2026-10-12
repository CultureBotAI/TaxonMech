# YAML Record Review: gamma proteobacterium SCGC AAA076-P13

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_p13.yaml
- Started UTC: 2026-09-23T05:49:18Z
- Finished UTC: 2026-09-23T05:50:27Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007119`
- Label: `gamma proteobacterium SCGC AAA076-P13`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:33811` (`unclassified Gammaproteobacteria`)
- Maintained path: generated `data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_p13.yaml`; fixes, if any, would belong in the source inventories or generator, not by hand in the generated YAML.

The record is a generated NCBI single-cell gamma-proteobacterium placeholder with a one-genome GTDB species cluster and two Madin trait assertions.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_p13.yaml data/taxa/bacteria/gamma_proteobacterium_scgc_aaa160_d02.yaml data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_b08.yaml data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_c11.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_p13.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI side is grounded to the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv:210823`: `NCBITaxon:1007119`, label `gamma proteobacterium SCGC AAA076-P13`, rank `SPECIES`, parent `NCBITaxon:33811`, genetic code `11`, sources `ncbitaxon|gtdb|madin_etal`, and snapshot date `2026-09-13`.

The GTDB mapping is at the same placeholder-cell granularity. `data/raw/gtdb_mappings.tsv:1079` maps the one-genome `GTDB:s__SCGC-AAA076-P13_sp000384935` cluster to `NCBITaxon:1007119`, and the GTDB genus label preserves the same `SCGC AAA076-P13` cell name as the NCBI label.

## Evidence

- `source_attestations` correctly reflects one NCBI name row, one GTDB mapping row with one genome, and two Madin trait assertions.
- No LPSN, BacDive, ATB, StrainInfo, GOLD, MediaDive, or BactoTraits rows were found for `NCBITaxon:1007119` by the exact ignored-file source search.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a generated record seeded directly from the same pinned NCBI taxon row.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-gamma_proteobacterium_scgc_aaa076_p13.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, GTDB, and Madin rows supporting the generated fields.

## Findings

No curation findings.

## Recommended Edits

No edits recommended.

## Follow-up Checks

- No follow-up is required for this record beyond normal regeneration QA.
- If the source inventories or generator change, rerun `just validate-strict data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_p13.yaml` and `just validate data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_p13.yaml`.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
