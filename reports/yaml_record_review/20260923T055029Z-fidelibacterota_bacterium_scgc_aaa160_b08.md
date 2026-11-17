# YAML Record Review: Fidelibacterota bacterium SCGC AAA160-B08

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_b08.yaml
- Started UTC: 2026-09-23T05:49:18Z
- Finished UTC: 2026-09-23T05:50:29Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007121`
- Label: `Fidelibacterota bacterium SCGC AAA160-B08`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:3106486` (`unclassified Fidelibacterota`)
- Maintained path: generated `data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_b08.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB synonym/xref projection in `src/taxonmech/seed.py`.

The record is a generated NCBI single-cell Fidelibacterota placeholder with one NCBI exact synonym, one GOLD organism attestation, and an over-broad GTDB species-cluster mapping.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/gamma_proteobacterium_scgc_aaa076_p13.yaml data/taxa/bacteria/gamma_proteobacterium_scgc_aaa160_d02.yaml data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_b08.yaml data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_c11.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_b08.yaml` | Passed. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI side is grounded to the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv:210825`: `NCBITaxon:1007121`, label `Fidelibacterota bacterium SCGC AAA160-B08`, rank `SPECIES`, parent `NCBITaxon:3106486`, genetic code `11`, exact synonym `SAR406 cluster bacterium SCGC AAA160-B08`, sources `ncbitaxon|gtdb|gold`, and snapshot date `2026-09-13`.

The GTDB projection is over-scoped. `data/raw/gtdb_mappings.tsv:1080` maps the two-genome `GTDB:s__Marinisoma_sp000402755` species cluster to this single-cell NCBI placeholder as `skos:closeMatch`, while the same GTDB cluster is also broad-mapped to the broader SAR406 cluster in `data/raw/gtdb_mappings.tsv:310000`.

## Evidence

- `source_attestations` correctly reflects one NCBI name row, one GTDB mapping row with two genomes, and one GOLD organism assertion.
- The NCBI exact synonym in the YAML is supported by the synonym column in `data/raw/ncbitaxon_taxa.tsv:210825`.
- No LPSN, BacDive, ATB, StrainInfo, MediaDive, Madin, or BactoTraits rows were found for `NCBITaxon:1007121` by the exact ignored-file source search.
- The two-genome GTDB species cluster may be related to this single-cell taxon, but it does not justify emitting `Marinisoma sp000402755` as an exact synonym of the SCGC AAA160-B08 record.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-fidelibacterota_bacterium_scgc_aaa160_b08.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, GOLD, GTDB species, and GTDB mapping rows needed to review the generated fields.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1080` and `src/taxonmech/seed.py` project the two-genome `GTDB:s__Marinisoma_sp000402755` species cluster onto the single-cell placeholder `NCBITaxon:1007121` and emit `Marinisoma sp000402755` as an exact synonym. This treats a GTDB species-cluster label as the exact identity of a single SCGC cell.

## Recommended Edits

- Downgrade or remove the maintained `GTDB:s__Marinisoma_sp000402755` to `NCBITaxon:1007121` close mapping unless curation confirms exact identity.
- Keep GTDB species-cluster labels from becoming exact synonyms on unclassified environmental or single-cell placeholders in `src/taxonmech/seed.py`.
- Regenerate `data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_b08.yaml` after the mapping or generator fix.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_b08.yaml` and `just validate data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa160_b08.yaml`.
- Re-run an exact `rg --no-ignore --hidden` for `NCBITaxon:1007121`, `GTDB:s__Marinisoma_sp000402755`, and `fidelibacterota_bacterium_scgc_aaa160_b08` across `data/raw`, `data/atb`, and `data/straininfo`.
- Manually verify that regenerated YAML retains the NCBI synonym and GOLD evidence but no longer emits `Marinisoma sp000402755` as an exact synonym of the SCGC AAA160-B08 placeholder.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
