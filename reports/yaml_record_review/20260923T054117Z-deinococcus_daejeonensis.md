# YAML Record Review: Deinococcus daejeonensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/deinococcus_daejeonensis.yaml
- Started UTC: 2026-09-23T05:38:43Z
- Finished UTC: 2026-09-23T05:41:17Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007098`
- Label: `Deinococcus daejeonensis`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1298` (`Deinococcus`)
- Maintained path: generated `data/taxa/bacteria/deinococcus_daejeonensis.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB synonym/xref projection in `src/taxonmech/seed.py`.

The record is a generated NCBI species for `Deinococcus daejeonensis` with a correct LPSN name row, a BacDive type strain, MediaDive/GOLD/Madin/BactoTraits/StrainInfo support, and one incorrect GTDB species projection.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/gordonia_caeni.yaml data/taxa/bacteria/deinococcus_daejeonensis.yaml data/taxa/bacteria/pseudomonas_kuykendallii.yaml data/taxa/bacteria/paenibacillus_elgii_b69.yaml` | Passed; closed-schema validation accepted all 4 files with zero errors. |
| `just validate data/taxa/bacteria/deinococcus_daejeonensis.yaml` | Passed. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI and LPSN identity of `NCBITaxon:1007098` is grounded: `data/raw/ncbitaxon_taxa.tsv` has the species as `Deinococcus daejeonensis` under `Deinococcus`, and `data/raw/lpsn_names.tsv:26933` has a legitimate, validly published, correct-name LPSN row for the same species with type-strain designations DSM 26465, JCM 16918, and KCTC 13751.

The GTDB identity is not grounded to this species. The YAML maps `GTDB:s__Deinococcus_grandis` to `NCBITaxon:1007098` with `skos:closeMatch` and then projects `Deinococcus grandis` as a GTDB `EXACT_SYNONYM`. The local LPSN inventory instead identifies `Deinococcus grandis` as a different correct-name species at `data/raw/lpsn_names.tsv:16608`, linked to `NCBITaxon:57498` and to `GTDB:s__Deinococcus_grandis`.

## Evidence

- `source_attestations` correctly reflects one NCBI name, one LPSN name, one BacDive strain, three MediaDive medium entries, three GOLD organisms, 14 Madin trait assertions, and 23 BactoTraits trait assertions for `NCBITaxon:1007098`.
- `data/raw/bacdive_strains.tsv` and `data/straininfo/strain_links.tsv:87890` support BacDive strain `3900`, JCM 16918/DSM 26465/KCTC 13751 type-strain identifiers, StrainInfo strain `400186`, and deposit `907033`.
- The strain assembly, genome, and related-record blocks are consistently for `D. daejeonensis` strain JCM 16918 and use BioSample `SAMD00245263`, BioProject `PRJDB10510`, GOLD project `Gp0548029`, and GTDB genome `RS_GCF_014647175.1`.
- The five-genome `GTDB:s__Deinococcus_grandis` cluster supports a separate `D. grandis` species; it does not support an exact synonym or exact-looking xref on the `D. daejeonensis` YAML.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-deinococcus_daejeonensis.md'` included ignored reports and found no prior review for this stem.
- An exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, LPSN, GTDB, BacDive, culture-collection, strain assembly, strain genome, GOLD, MediaDive, Madin, BactoTraits, and StrainInfo rows for `NCBITaxon:1007098`.
- The same exact ignored-file search also found the distinct `NCBITaxon:57498` / `Deinococcus grandis` local source rows that disprove using `GTDB:s__Deinococcus_grandis` as an exact synonym for `NCBITaxon:1007098`.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1070` and `src/taxonmech/seed.py` project `GTDB:s__Deinococcus_grandis` onto `Deinococcus daejeonensis`. The generated YAML therefore emits `Deinococcus grandis` as an `EXACT_SYNONYM` and `GTDB:s__Deinococcus_grandis` as an xref for the wrong LPSN/NCBI species, despite `data/raw/lpsn_names.tsv:16608` linking that GTDB species to the separate `Deinococcus grandis` taxon `NCBITaxon:57498`.

## Recommended Edits

- Fix the maintained GTDB mapping input so `GTDB:s__Deinococcus_grandis` is not emitted as a close match for `NCBITaxon:1007098`, and keep the GTDB synonym/xref projection in `src/taxonmech/seed.py` from turning untrusted GTDB labels into exact synonyms.
- Regenerate `data/taxa/bacteria/deinococcus_daejeonensis.yaml` after the mapping fix and verify that it retains the NCBI, LPSN, BacDive, MediaDive, GOLD, Madin, BactoTraits, and StrainInfo evidence while dropping the `Deinococcus grandis` synonym and GTDB xref.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/deinococcus_daejeonensis.yaml` and `just validate data/taxa/bacteria/deinococcus_daejeonensis.yaml`.
- Re-run an exact `rg --no-ignore --hidden` for `NCBITaxon:1007098`, `NCBITaxon:57498`, `GTDB:s__Deinococcus_grandis`, and `deinococcus_daejeonensis` across `data/raw`, `data/atb`, and `data/straininfo`.
- Manually verify that the regenerated `D. daejeonensis` record no longer contains `Deinococcus grandis` as a GTDB exact synonym.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
