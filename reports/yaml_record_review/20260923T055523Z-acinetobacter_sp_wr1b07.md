# YAML Record Review: Acinetobacter sp. Wr1B07

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acinetobacter_sp_wr1b07.yaml
- Started UTC: 2026-09-23T05:54:16Z
- Finished UTC: 2026-09-23T05:55:23Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007131`
- Label: `Acinetobacter sp. Wr1B07`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:196816` (`unclassified Acinetobacter`)
- Maintained path: generated `data/taxa/bacteria/acinetobacter_sp_wr1b07.yaml`; fixes, if any, would belong in the source inventories or generator, not by hand in the generated YAML.

The record is a generated NCBI-only Acinetobacter placeholder with no auxiliary source evidence.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/acinetobacter_sp_wr1b05.yaml data/taxa/bacteria/acinetobacter_sp_wr1b07.yaml data/taxa/bacteria/acinetobacter_sp_wr1d12.yaml data/taxa/bacteria/acinetobacter_sp_wr1f05.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/acinetobacter_sp_wr1b07.yaml` | Passed. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI identity agrees with the pinned NCBI inventory row in `data/raw/ncbitaxon_taxa.tsv:210832`: `NCBITaxon:1007131`, label `Acinetobacter sp. Wr1B07`, rank `SPECIES`, parent `NCBITaxon:196816`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.

The lineage correctly places the placeholder under `Acinetobacter` and `unclassified Acinetobacter`, with no NCBI synonym, GTDB, LPSN, strain, genome, or trait fields projected into the YAML.

## Evidence

- `source_attestations` correctly contains only the single NCBI name assertion.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a generated record seeded directly from the same pinned NCBI taxon row.
- The absence of `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, `genome_records`, and trait/database attestations is supported by the exact ignored-file source search.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-acinetobacter_sp_wr1b07.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found only the PATHS row and the pinned NCBI row for `NCBITaxon:1007131`, so the missing auxiliary sections were checked against ignored and non-ignored local source files.

## Findings

No curation findings.

## Recommended Edits

No edits recommended.

## Follow-up Checks

- No follow-up is required for this record beyond normal regeneration QA.
- If the source inventories or generator change, rerun `just validate-strict data/taxa/bacteria/acinetobacter_sp_wr1b07.yaml` and `just validate data/taxa/bacteria/acinetobacter_sp_wr1b07.yaml`.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
