# YAML Record Review: gamma proteobacterium SCGC AAA160-D02

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/gamma_proteobacterium_scgc_aaa160_d02.yaml
- Started UTC: 2026-09-23T05:49:18Z
- Finished UTC: 2026-09-23T05:50:28Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007120`
- Label: `gamma proteobacterium SCGC AAA160-D02`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:33811` (`unclassified Gammaproteobacteria`)
- Maintained path: generated `data/taxa/bacteria/gamma_proteobacterium_scgc_aaa160_d02.yaml`; fixes, if any, would belong in the source inventories or generator, not by hand in the generated YAML.

The record is a generated NCBI-only single-cell gamma-proteobacterium placeholder with no auxiliary source evidence.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_p13.yaml data/taxa/bacteria/gamma_proteobacterium_scgc_aaa160_d02.yaml data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_b08.yaml data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_c11.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/gamma_proteobacterium_scgc_aaa160_d02.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI identity agrees with the pinned NCBI inventory row in `data/raw/ncbitaxon_taxa.tsv:210824`: `NCBITaxon:1007120`, label `gamma proteobacterium SCGC AAA160-D02`, rank `SPECIES`, parent `NCBITaxon:33811`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.

The lineage correctly places the placeholder under `Gammaproteobacteria` and `unclassified Gammaproteobacteria`, with no NCBI synonym, GTDB, LPSN, strain, genome, or trait fields projected into the YAML.

## Evidence

- `source_attestations` correctly contains only the single NCBI name assertion.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a generated record seeded directly from the same pinned NCBI taxon row.
- The absence of `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, `genome_records`, and trait/database attestations is supported by the exact ignored-file source search.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-gamma_proteobacterium_scgc_aaa160_d02.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found only the PATHS row and the pinned NCBI row for `NCBITaxon:1007120`, so the missing auxiliary sections were checked against ignored and non-ignored local source files.

## Findings

No curation findings.

## Recommended Edits

No edits recommended.

## Follow-up Checks

- No follow-up is required for this record beyond normal regeneration QA.
- If the source inventories or generator change, rerun `just validate-strict data/taxa/bacteria/gamma_proteobacterium_scgc_aaa160_d02.yaml` and `just validate data/taxa/bacteria/gamma_proteobacterium_scgc_aaa160_d02.yaml`.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
