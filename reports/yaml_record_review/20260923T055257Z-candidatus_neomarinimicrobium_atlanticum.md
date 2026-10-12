# YAML Record Review: Candidatus Neomarinimicrobium atlanticum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/candidatus_neomarinimicrobium_atlanticum.yaml
- Started UTC: 2026-09-23T05:51:31Z
- Finished UTC: 2026-09-23T05:52:57Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007123`
- Label: `Candidatus Neomarinimicrobium atlanticum`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:3453327` (`Candidatus Neomarinimicrobium`)
- Maintained path: generated `data/taxa/bacteria/candidatus_neomarinimicrobium_atlanticum.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB synonym/xref projection in `src/taxonmech/seed.py`.

The record is a generated NCBI `Candidatus` species with NCBI synonyms, one GOLD organism attestation, two Madin trait assertions, and an over-broad GTDB species-cluster mapping.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/candidatus_neomarinimicrobium_atlanticum.yaml data/taxa/bacteria/fidelibacterota_bacterium_scgc_aaa076_m08.yaml data/taxa/bacteria/magnetospirillum_sp_pmbn1.yaml data/taxa/bacteria/acinetobacter_sp_wr1b02.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/candidatus_neomarinimicrobium_atlanticum.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI side is grounded to the pinned NCBI row in `data/raw/ncbitaxon_taxa.tsv:210827`: `NCBITaxon:1007123`, label `Candidatus Neomarinimicrobium atlanticum`, rank `SPECIES`, parent `NCBITaxon:3453327`, genetic code `11`, two exact NCBI synonyms, two related NCBI synonyms, sources `ncbitaxon|gtdb|gold|madin_etal`, and snapshot date `2026-09-13`.

The GTDB projection is over-scoped. `data/raw/gtdb_mappings.tsv:1082` maps the 15-genome `GTDB:s__Marinisoma_atlantica` species cluster to this NCBI `Candidatus` species as `skos:closeMatch`. The same GTDB species cluster is mapped to `NCBITaxon:1007122` and `NCBITaxon:1379406` as close matches and to broader SAR406/Fidelibacterota taxa as broad matches, so the generated `Marinisoma atlantica` exact synonym and exact-looking xref are not justified by the local pinned mappings.

## Evidence

- `source_attestations` correctly reflects one NCBI name row, one GTDB mapping row with 15 genomes, one GOLD organism assertion, and two Madin trait assertions.
- The NCBI exact and related synonyms in the YAML are supported by the two synonym columns in `data/raw/ncbitaxon_taxa.tsv:210827`.
- No LPSN, BacDive, ATB, StrainInfo, MediaDive, or BactoTraits rows were found for `NCBITaxon:1007123` by the exact ignored-file source search.
- The 15-genome GTDB species cluster may be related to this species, but it should not be emitted as the exact identity of `Candidatus Neomarinimicrobium atlanticum` without a curated resolution of the neighboring close mappings.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-candidatus_neomarinimicrobium_atlanticum.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, GOLD, Madin, GTDB species, and GTDB mapping rows needed to review the generated fields.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1082` and `src/taxonmech/seed.py` project the shared 15-genome `GTDB:s__Marinisoma_atlantica` species cluster onto `NCBITaxon:1007123` and emit `Marinisoma atlantica` as an exact synonym. The same GTDB cluster is close-mapped to other NCBI species placeholders, so this should be downgraded or curated before appearing as exact identity.

## Recommended Edits

- Downgrade or remove the maintained `GTDB:s__Marinisoma_atlantica` to `NCBITaxon:1007123` close mapping unless curation confirms exact identity.
- Keep GTDB species-cluster labels from becoming exact synonyms on `Candidatus`/single-cell placeholders in `src/taxonmech/seed.py` unless the GTDB mapping is curated as exact.
- Regenerate `data/taxa/bacteria/candidatus_neomarinimicrobium_atlanticum.yaml` after the mapping or generator fix.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/candidatus_neomarinimicrobium_atlanticum.yaml` and `just validate data/taxa/bacteria/candidatus_neomarinimicrobium_atlanticum.yaml`.
- Re-run an exact `rg --no-ignore --hidden` for `NCBITaxon:1007123`, `GTDB:s__Marinisoma_atlantica`, and `candidatus_neomarinimicrobium_atlanticum` across `data/raw`, `data/atb`, and `data/straininfo`.
- Manually verify that regenerated YAML retains the NCBI, GOLD, and Madin evidence but no longer emits `Marinisoma atlantica` as an exact synonym of the `Candidatus` species.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
