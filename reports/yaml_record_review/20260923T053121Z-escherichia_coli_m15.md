# YAML Record Review: Escherichia coli M15

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/escherichia_coli_m15.yaml
- Started UTC: 2026-09-23T05:30:40Z
- Finished UTC: 2026-09-23T05:31:21Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007065`
- Label: `Escherichia coli M15`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:562` (`Escherichia coli`)
- Maintained path: generated `data/taxa/bacteria/escherichia_coli_m15.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB projection logic in `src/taxonmech/seed.py`.

The record is a generated NCBI strain for `Escherichia coli M15` with NCBI, GTDB, and Madin attestations.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/streptomyces_sp_x3014.yaml data/taxa/bacteria/streptococcus_suis_st3.yaml data/taxa/bacteria/escherichia_coli_m15.yaml data/taxa/bacteria/bacillus_sp_w2_2.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/escherichia_coli_m15.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI identity agrees with the pinned NCBI inventory row in `data/raw/ncbitaxon_taxa.tsv:210792`: `NCBITaxon:1007065`, label `Escherichia coli M15`, rank `STRAIN`, parent `NCBITaxon:562`, genetic code `11`, NCBI exact synonyms `Escherichia coli str. M15` and `Escherichia coli strain M15`, source set `ncbitaxon|gtdb|madin_etal`, and snapshot date `2026-09-13`.

The lineage correctly places the strain under the species `Escherichia coli`. `grounding_status: EXACT` is appropriate for the NCBI side of the record because the record is seeded from the same NCBI strain identifier.

The GTDB projection is over-scoped: `data/raw/gtdb_mappings.tsv:1065` maps `GTDB:s__Escherichia_coli` to the strain `NCBITaxon:1007065` with `skos:closeMatch` and `genome_count: 36408`. That GTDB species cluster is far broader than the single NCBI M15 strain.

## Evidence

- `source_attestations` correctly reflects the local row counts: one NCBI name row, one GTDB mapping row, and one Madin trait assertion in `data/raw/madin_taxa.tsv:366`.
- The two NCBI strain-name synonyms are supported by the synonym column in `data/raw/ncbitaxon_taxa.tsv:210792`.
- The GTDB species cluster supports, at most, a broad or species-level relationship; it does not support projecting `Escherichia coli` as an `EXACT_SYNONYM` of the M15 strain or adding `GTDB:s__Escherichia_coli` as an exact-looking strain xref.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-escherichia_coli_m15.md'` included ignored reports and found no prior review for this stem.
- An anchored exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS entry, the NCBI row, the GTDB species-cluster row, and the Madin count.
- No ATB, BacDive, GOLD, or StrainInfo rows were found for this strain, so the absence of those evidence sections is supported.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1065` and `src/taxonmech/seed.py` project the GTDB `s__Escherichia_coli` species cluster onto the `Escherichia coli M15` NCBI strain. The generated YAML consequently gives a 36,408-genome species cluster an exact synonym and xref on a single strain record, which inflates the identity scope.

## Recommended Edits

- Adjust the maintained GTDB mapping generation in `data/raw/gtdb_mappings.tsv` and the GTDB synonym/xref projection in `src/taxonmech/seed.py` so GTDB species clusters are not emitted as exact synonyms or exact-looking xrefs on NCBI strain records. Regenerate `data/taxa/bacteria/escherichia_coli_m15.yaml` after the maintained input or generator fix.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/escherichia_coli_m15.yaml` and `just validate data/taxa/bacteria/escherichia_coli_m15.yaml`.
- Re-run an anchored `rg --no-ignore --hidden` for `NCBITaxon:1007065`, `Escherichia coli M15`, and `escherichia_coli_m15` across `data/raw`, `data/atb`, and `data/straininfo`.
- Manually verify that regenerated strain YAML retains the NCBI and Madin attestations but no longer emits `Escherichia coli` as a GTDB exact synonym or `GTDB:s__Escherichia_coli` as a strain xref.

## Additional Notes

The live NCBI browser and source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 NCBI, GTDB, and Madin rows are the authority evidence used for this report.
