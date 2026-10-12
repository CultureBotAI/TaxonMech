# YAML Record Review: gamma proteobacterium SCGC AAA076-F14

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_f14.yaml
- Started UTC: 2026-09-23T05:47:19Z
- Finished UTC: 2026-09-23T05:48:21Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007117`
- Label: `gamma proteobacterium SCGC AAA076-F14`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:33811` (`unclassified Gammaproteobacteria`)
- Maintained path: generated `data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_f14.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB synonym/xref projection in `src/taxonmech/seed.py`.

The record is a generated NCBI single-cell gamma-proteobacterium placeholder with one GTDB species-cluster mapping.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_d13.yaml data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_e13.yaml data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_f14.yaml data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_p09.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_f14.yaml` | Passed. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI side is grounded to the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv:210821`: `NCBITaxon:1007117`, label `gamma proteobacterium SCGC AAA076-F14`, rank `SPECIES`, parent `NCBITaxon:33811`, genetic code `11`, sources `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The GTDB projection is over-scoped. `data/raw/gtdb_mappings.tsv:1078` maps the five-genome `GTDB:s__Pseudothioglobus_singularis_B` species cluster to this single-cell NCBI placeholder as `skos:closeMatch`; the same split cluster is also broad-mapped to `NCBITaxon:1427364`, and its unsuffixed sibling cluster is being projected to neighboring SCGC placeholders.

## Evidence

- `source_attestations` correctly reflects one NCBI name row and one GTDB mapping row with five genomes.
- No NCBI synonym column, LPSN row, BacDive strain row, ATB assembly, StrainInfo row, GOLD row, MediaDive row, Madin row, or BactoTraits row was found for `NCBITaxon:1007117` by the exact ignored-file source search, matching the compact generated YAML.
- The `GTDB:s__Pseudothioglobus_singularis_B` cluster supports a broad species-cluster relationship; it does not justify emitting `Pseudothioglobus singularis B` as an `EXACT_SYNONYM` of an unclassified single-cell Gammaproteobacteria placeholder.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-gamma_proteobacterium_scgc_aaa076_f14.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, GTDB species, and GTDB mapping rows needed to review the generated fields.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1078` and `src/taxonmech/seed.py` project the five-genome `GTDB:s__Pseudothioglobus_singularis_B` species cluster onto the single-cell placeholder `NCBITaxon:1007117` and emit `Pseudothioglobus singularis B` as an exact synonym. This turns a GTDB split-species cluster label into the exact identity of one environmental record.

## Recommended Edits

- Downgrade or remove the maintained `GTDB:s__Pseudothioglobus_singularis_B` to `NCBITaxon:1007117` close mapping unless curation confirms exact identity.
- Keep GTDB species-cluster labels from becoming exact synonyms on unclassified environmental or single-cell placeholders in `src/taxonmech/seed.py`.
- Regenerate `data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_f14.yaml` after the mapping or generator fix.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_f14.yaml` and `just validate data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_f14.yaml`.
- Re-run an exact `rg --no-ignore --hidden` for `NCBITaxon:1007117`, `GTDB:s__Pseudothioglobus_singularis_B`, and `gamma_proteobacterium_scgc_aaa076_f14` across `data/raw`, `data/atb`, and `data/straininfo`.
- Manually verify that regenerated YAML retains the NCBI seed identity and no longer emits `Pseudothioglobus singularis B` as an exact synonym of the SCGC AAA076-F14 placeholder.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
