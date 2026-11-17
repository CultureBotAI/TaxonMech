# YAML Record Review: Borrelia latyschewii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/borrelia_latyschewii.yaml
- Started UTC: 2026-10-02T18:15:38Z
- Finished UTC: 2026-10-02T18:15:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1027767` |
| Label | `Borrelia latyschewii` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:138` |
| Parent label | `Borrelia` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Nomenclature | `1` |
| Synonyms | `2` |
| Xrefs | `1` |
| Source attestations | `NCBITAXON`, `LPSN`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/borrelia_latyschewii.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/streptomyces_sp_sd_5.yaml data/taxa/bacteria/streptomyces_sp_sd_8.yaml data/taxa/bacteria/streptomyces_sp_sd_9.yaml data/taxa/bacteria/borrelia_latyschewii.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 87 lines, 9 lineage entries, 2 synonyms, 1 xref, 1 nomenclature item, 0 declared strains, 0 genome assemblies, and 3 source attestations. |
| Direct exact NCBI/LPSN/MADIN source scan | Pass: found one seed row, one first-column NCBI Taxonomy row, the exact LPSN name row, the exact MADIN row, and no auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct first-column lineage scan | Pass: every lineage id in the YAML was found as a first-column NCBI Taxonomy row. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11100 maps `NCBITaxon:1027767` to `borrelia_latyschewii`.
- `curation/seed_scope.tsv` row 36099 keeps this taxon in scope with a three-source rule covering NCBI Taxonomy, LPSN, and MADIN.
- `data/raw/ncbitaxon_taxa.tsv` row 218931 names `NCBITaxon:1027767` as `Borrelia latyschewii`, under `NCBITaxon:138` / `Borrelia`, with sources `ncbitaxon|lpsn|madin_etal`.
- `data/raw/lpsn_names.tsv` row 21609 records `lpsn:783529` as the correct, validly published, legitimate species name for `NCBITaxon:1027767`.
- `data/raw/madin_taxa.tsv` row 517 supplies 1 MADIN trait assertion for the same NCBI identifier.
- The generated YAML line 1 preserves the NCBI identifier, lines 36-60 preserve the LPSN nomenclature and xref plus the two NCBI synonyms, and lines 63-80 preserve the three source attestations.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The two NCBI exact synonyms match the two pipe-delimited synonyms in `data/raw/ncbitaxon_taxa.tsv`.
- The LPSN nomenclature block preserves the exact LPSN source ID, name, rank, authority, status flags, URL, and three publication references.
- The MADIN source attestation preserves the exact `NCBITaxon:1027767` support count from `data/raw/madin_taxa.tsv`.

## Completeness

- The record is complete for the exact NCBI, LPSN, and MADIN rows currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, exact GOLD, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:1027767`.
- No genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/borrelia_latyschewii.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/borrelia_latyschewii.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11100, `curation/seed_scope.tsv` row 36099, `data/raw/ncbitaxon_taxa.tsv` row 218931, `data/raw/lpsn_names.tsv` row 21609, `data/raw/madin_taxa.tsv` row 517, YAML line 1, YAML lines 36-60, and YAML lines 63-80.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/borrelia_latyschewii.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/borrelia_latyschewii.yaml` directly.
