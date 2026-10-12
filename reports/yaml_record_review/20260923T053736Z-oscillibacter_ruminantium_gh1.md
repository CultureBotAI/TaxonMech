# YAML Record Review: Oscillibacter ruminantium GH1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/oscillibacter_ruminantium_gh1.yaml
- Started UTC: 2026-09-23T05:36:45Z
- Finished UTC: 2026-09-23T05:37:36Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1007096`
- Label: `Oscillibacter ruminantium GH1`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1263547` (`Oscillibacter ruminantium`)
- Maintained path: generated `data/taxa/bacteria/oscillibacter_ruminantium_gh1.yaml`; fixes belong in `data/raw/gtdb_mappings.tsv` generation and GTDB projection logic in `src/taxonmech/seed.py`.

The record is a generated NCBI strain for `Oscillibacter ruminantium GH1` with NCBI, GTDB, BacDive, Madin, and StrainInfo support.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/microlunatus_sp_bs15.yaml data/taxa/bacteria/pedobacter_sp_bs03.yaml data/taxa/bacteria/pigmentiphaga_soli.yaml data/taxa/bacteria/oscillibacter_ruminantium_gh1.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/oscillibacter_ruminantium_gh1.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The NCBI identity agrees with the pinned NCBI inventory row in `data/raw/ncbitaxon_taxa.tsv:210806`: `NCBITaxon:1007096`, label `Oscillibacter ruminantium GH1`, rank `STRAIN`, parent `NCBITaxon:1263547`, genetic code `11`, five NCBI exact synonyms, source set `ncbitaxon|gtdb|bacdive|madin_etal`, and snapshot date `2026-09-13`.

The lineage correctly places the strain under the species `Oscillibacter ruminantium`. `grounding_status: EXACT` is appropriate for the NCBI side of the record because the record is seeded from the same NCBI strain identifier.

The GTDB projection is over-scoped: `data/raw/gtdb_mappings.tsv:1068` maps `GTDB:s__Oscillibacter_ruminantium` to the strain `NCBITaxon:1007096` with `skos:closeMatch` and `genome_count: 14`. The same GTDB species cluster is also mapped to the NCBI species in `data/raw/gtdb_mappings.tsv:15259`, so the strain-level mapping adds a broader species identity to one GH1 strain.

## Evidence

- `source_attestations` correctly reflects the local row counts: one NCBI name row, one GTDB mapping row, one BacDive strain row in `data/raw/bacdive_strains.tsv:56161`, and one Madin trait assertion in `data/raw/madin_taxa.tsv:368`.
- The five NCBI strain-name synonyms are supported by the synonym column in `data/raw/ncbitaxon_taxa.tsv:210806`.
- The BacDive row supports designation `GH1`, four culture-collection IDs, and two medium entries; `data/straininfo/strain_links.tsv:15364` links BacDive strain `133851` to StrainInfo strain `406617` and deposit `913927`.
- The GTDB species cluster supports, at most, a species-level relationship; it does not support projecting `Oscillibacter ruminantium` as an `EXACT_SYNONYM` of the GH1 strain or adding `GTDB:s__Oscillibacter_ruminantium` as an exact-looking strain xref.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-oscillibacter_ruminantium_gh1.md'` included ignored reports and found no prior review for this stem.
- An anchored exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS, NCBI, GTDB, LPSN species, BacDive, culture-collection, strain assembly, strain genome, Madin, and StrainInfo rows supporting the generated fields and the GTDB over-scope finding.
- No ATB, GOLD, or sample rows were found for the GH1 strain, so the absence of those evidence sections is supported.

## Findings

### Major

- `data/raw/gtdb_mappings.tsv:1068` and `src/taxonmech/seed.py` project the GTDB `s__Oscillibacter_ruminantium` species cluster onto the `Oscillibacter ruminantium GH1` NCBI strain. The generated YAML consequently gives a 14-genome species cluster an exact synonym and xref on a single strain record, which inflates the identity scope.

## Recommended Edits

- Adjust the maintained GTDB mapping generation in `data/raw/gtdb_mappings.tsv` and the GTDB synonym/xref projection in `src/taxonmech/seed.py` so GTDB species clusters are not emitted as exact synonyms or exact-looking xrefs on NCBI strain records. Regenerate `data/taxa/bacteria/oscillibacter_ruminantium_gh1.yaml` after the maintained input or generator fix.

## Follow-up Checks

- Rerun `just validate-strict data/taxa/bacteria/oscillibacter_ruminantium_gh1.yaml` and `just validate data/taxa/bacteria/oscillibacter_ruminantium_gh1.yaml`.
- Re-run an anchored `rg --no-ignore --hidden` for `NCBITaxon:1007096`, `Oscillibacter ruminantium GH1`, and `oscillibacter_ruminantium_gh1` across `data/raw`, `data/atb`, and `data/straininfo`.
- Manually verify that regenerated strain YAML retains the NCBI, BacDive, Madin, and StrainInfo evidence but no longer emits `Oscillibacter ruminantium` as a GTDB exact synonym or `GTDB:s__Oscillibacter_ruminantium` as a strain xref.

## Additional Notes

The live source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 local source rows are the authority evidence used for this report.
