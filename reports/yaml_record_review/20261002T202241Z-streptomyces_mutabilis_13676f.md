# YAML Record Review: Streptomyces mutabilis 13676F

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/streptomyces_mutabilis_13676f.yaml
- Started UTC: 2026-10-02T20:22:41Z
- Finished UTC: 2026-10-02T20:22:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1028809` |
| Label | `Streptomyces mutabilis 13676F` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:67332` |
| Parent label | `Streptomyces mutabilis` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/streptomyces_mutabilis_13676f.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/streptomyces_mutabilis_13676f.yaml` | Pass: the strict one-file batch scanned 1 file and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, all 10 first-column lineage rows, and no GOLD aggregate or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: ignored-file-inclusive source scans found only `ncbitaxon_taxa.tsv` and `seed_scope.tsv` rows for `NCBITaxon:1028809`, with no exact `data/straininfo` or `data/atb` rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11376 maps `NCBITaxon:1028809` to `streptomyces_mutabilis_13676f`.
- `curation/seed_scope.tsv` row 319686 keeps this taxon in scope with an NCBI rule.
- `data/raw/ncbitaxon_taxa.tsv` row 219212 names `NCBITaxon:1028809` as `Streptomyces mutabilis 13676F`, under `NCBITaxon:67332` / `Streptomyces mutabilis`.
- The generated YAML line 1 preserves the NCBI identifier, and line 50 preserves the NCBI source ID.

## Evidence

- The YAML identifier, strain rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The NCBI row supplies two exact synonyms, `Streptomyces mutabilis str. 13676F` and `Streptomyces mutabilis strain 13676F`; both are present with `source: NCBITaxon`.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:67332` / `Streptomyces mutabilis`.

## Completeness

- The record is complete for the exact NCBI row currently present for this strain taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no external taxonomy mapping is currently present for `NCBITaxon:1028809`.
- No external xrefs, genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/streptomyces_mutabilis_13676f.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/streptomyces_mutabilis_13676f.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11376, `curation/seed_scope.tsv` row 319686, `data/raw/ncbitaxon_taxa.tsv` row 219212, and YAML lines 1 and 50.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/streptomyces_mutabilis_13676f.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/streptomyces_mutabilis_13676f.yaml` directly.
