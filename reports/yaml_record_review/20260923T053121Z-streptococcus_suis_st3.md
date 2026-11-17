# YAML Record Review: Streptococcus suis ST3

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/streptococcus_suis_st3.yaml
- Started UTC: 2026-09-23T05:30:40Z
- Finished UTC: 2026-09-23T05:31:21Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007064`
- Label: `Streptococcus suis ST3`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1307` (`Streptococcus suis`)
- Maintained path: generated `data/taxa/bacteria/streptococcus_suis_st3.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB projection logic in `src/taxonmech/seed.py`.

The record is a generated NCBI strain for `Streptococcus suis ST3` with NCBI, GTDB, GOLD, and Madin attestations.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/streptomyces_sp_x3014.yaml data/taxa/bacteria/streptococcus_suis_st3.yaml data/taxa/bacteria/escherichia_coli_m15.yaml data/taxa/bacteria/bacillus_sp_w2_2.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/streptococcus_suis_st3.yaml` | Passed; `linkml-validate` exited successfully. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI identity agrees with the pinned NCBI inventory row in `data/raw/ncbitaxon_taxa.tsv:210791`: `NCBITaxon:1007064`, label `Streptococcus suis ST3`, rank `STRAIN`, parent `NCBITaxon:1307`, genetic code `11`, NCBI exact synonyms `Streptococcus suis str. ST3` and `Streptococcus suis strain ST3`, source set `ncbitaxon|gtdb|gold|madin_etal`, and snapshot date `2026-09-13`.

The lineage correctly places the strain under the species `Streptococcus suis`. `grounding_status: EXACT` is appropriate for the NCBI side of the record because the record is seeded from the same NCBI strain identifier.

The GTDB projection is over-scoped: `data/raw/gtdb_mappings.tsv:1064` maps `GTDB:s__Streptococcus_suis` to the strain `NCBITaxon:1007064` with `skos:closeMatch` and `genome_count: 2003`. That GTDB species cluster is broader than the single NCBI ST3 strain.

## Evidence

- `source_attestations` correctly reflects the local row counts: one NCBI name row, one GOLD organism row in `data/raw/gold_organisms.tsv:169`, one GTDB mapping row, and five Madin trait assertions in `data/raw/madin_taxa.tsv:365`.
- The two NCBI strain-name synonyms are supported by the synonym column in `data/raw/ncbitaxon_taxa.tsv:210791`.
- The GTDB species cluster supports, at most, a broad or species-level relationship; it does not support projecting `Streptococcus suis` as an `EXACT_SYNONYM` of the ST3 strain or adding `GTDB:s__Streptococcus_suis` as an exact-looking strain xref.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-streptococcus_suis_st3.md'` included ignored reports and found no prior review for this stem.
- An anchored exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS entry, the NCBI row, the GTDB species-cluster row, the GOLD organism count, and the Madin count.
- No ATB or StrainInfo rows were found for this strain, so the absence of ATB and StrainInfo evidence is supported.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1064` and `src/taxonmech/seed.py` project the GTDB `s__Streptococcus_suis` species cluster onto the `Streptococcus suis ST3` NCBI strain. The generated YAML consequently gives a 2,003-genome species cluster an exact synonym and xref on a single strain record, which inflates the identity scope.

## Recommended Edits

- Adjust the maintained GTDB mapping generation in `data/raw/gtdb_mappings.tsv` and the GTDB synonym/xref projection in `src/taxonmech/seed.py` so GTDB species clusters are not emitted as exact synonyms or exact-looking xrefs on NCBI strain records. Regenerate `data/taxa/bacteria/streptococcus_suis_st3.yaml` after the maintained input or generator fix.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/streptococcus_suis_st3.yaml` and `just validate data/taxa/bacteria/streptococcus_suis_st3.yaml`.
- Re-run an anchored `rg --no-ignore --hidden` for `NCBITaxon:1007064`, `Streptococcus suis ST3`, and `streptococcus_suis_st3` across `data/raw`, `data/atb`, and `data/straininfo`.
- Manually verify that regenerated strain YAML retains the NCBI, GOLD, and Madin attestations but no longer emits `Streptococcus suis` as a GTDB exact synonym or `GTDB:s__Streptococcus_suis` as a strain xref.

## Additional Notes

The live NCBI browser and source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 NCBI, GTDB, GOLD, and Madin rows are the authority evidence used for this report.
