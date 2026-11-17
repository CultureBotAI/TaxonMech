# YAML Record Review: gamma proteobacterium SCGC AAA076-D13

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_d13.yaml
- Started UTC: 2026-09-23T05:47:19Z
- Finished UTC: 2026-09-23T05:48:19Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007115`
- Label: `gamma proteobacterium SCGC AAA076-D13`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:33811` (`unclassified Gammaproteobacteria`)
- Maintained path: generated `data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_d13.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB synonym/xref projection in `src/taxonmech/seed.py`.

The record is a generated NCBI single-cell gamma-proteobacterium placeholder with one GTDB species-cluster mapping.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_d13.yaml data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_e13.yaml data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_f14.yaml data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_p09.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_d13.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI side is grounded to the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv:210819`: `NCBITaxon:1007115`, label `gamma proteobacterium SCGC AAA076-D13`, rank `SPECIES`, parent `NCBITaxon:33811`, genetic code `11`, sources `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The GTDB projection is over-scoped. `data/raw/gtdb_mappings.tsv:1077` maps the 22-genome `GTDB:s__Pseudothioglobus_singularis` species cluster to this single-cell NCBI placeholder as `skos:closeMatch`; the adjacent rows also map the same cluster to `NCBITaxon:1007114` and the split `s__Pseudothioglobus_singularis_B` cluster to `NCBITaxon:1007117`, so this record should not treat the canonical cluster label as its exact identity.

## Evidence

- `source_attestations` correctly reflects one NCBI name row and one GTDB mapping row with 22 genomes.
- No NCBI synonym column, LPSN row, BacDive strain row, ATB assembly, StrainInfo row, GOLD row, MediaDive row, Madin row, or BactoTraits row was found for `NCBITaxon:1007115` by the exact ignored-file source search, matching the compact generated YAML.
- The `GTDB:s__Pseudothioglobus_singularis` cluster supports a broad species-cluster relationship; it does not justify emitting `Pseudothioglobus singularis` as an `EXACT_SYNONYM` of an unclassified single-cell Gammaproteobacteria placeholder.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-gamma_proteobacterium_scgc_aaa076_d13.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, GTDB species, and GTDB mapping rows needed to review the generated fields.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1077` and `src/taxonmech/seed.py` project the 22-genome `GTDB:s__Pseudothioglobus_singularis` species cluster onto the single-cell placeholder `NCBITaxon:1007115` and emit `Pseudothioglobus singularis` as an exact synonym. This turns a broad GTDB species-cluster label into the exact identity of one environmental record.

## Recommended Edits

- Downgrade or remove the maintained `GTDB:s__Pseudothioglobus_singularis` to `NCBITaxon:1007115` close mapping unless curation confirms exact identity.
- Keep GTDB species-cluster labels from becoming exact synonyms on unclassified environmental or single-cell placeholders in `src/taxonmech/seed.py`.
- Regenerate `data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_d13.yaml` after the mapping or generator fix.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_d13.yaml` and `just validate data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_d13.yaml`.
- Re-run an exact `rg --no-ignore --hidden` for `NCBITaxon:1007115`, `GTDB:s__Pseudothioglobus_singularis`, and `gamma_proteobacterium_scgc_aaa076_d13` across `data/raw`, `data/atb`, and `data/straininfo`.
- Manually verify that regenerated YAML retains the NCBI seed identity and no longer emits `Pseudothioglobus singularis` as an exact synonym of the SCGC AAA076-D13 placeholder.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
