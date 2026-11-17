# YAML Record Review: Phormidium laetevirens LEGE 06103

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/phormidium_laetevirens_lege_06103.yaml
- Started UTC: 2026-10-02T19:47:13Z
- Finished UTC: 2026-10-02T19:47:13Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1028306` |
| Label | `Phormidium laetevirens LEGE 06103` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1028305` |
| Parent label | `Phormidium laetevirens` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/phormidium_laetevirens_lege_06103.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/streptomyces_sp_61348.yaml data/taxa/bacteria/leptolyngbya_mycoidea_lege_06009.yaml data/taxa/bacteria/phormidium_laetevirens.yaml data/taxa/bacteria/phormidium_laetevirens_lege_06103.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 60 lines, 12 lineage entries, 0 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, all 12 first-column lineage rows, and no GOLD aggregate or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: ignored-file-inclusive source scans found only `ncbitaxon_taxa.tsv` and `seed_scope.tsv` rows for `NCBITaxon:1028306`, with no exact `data/straininfo` or `data/atb` rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11288 maps `NCBITaxon:1028306` to `phormidium_laetevirens_lege_06103`.
- `curation/seed_scope.tsv` row 319626 keeps this taxon in scope with an NCBI rule.
- `data/raw/ncbitaxon_taxa.tsv` row 219118 names `NCBITaxon:1028306` as `Phormidium laetevirens LEGE 06103`, under `NCBITaxon:1028305` / `Phormidium laetevirens`.
- The generated YAML line 1 preserves the NCBI identifier, and line 49 preserves the NCBI source ID.

## Evidence

- The YAML identifier, strain rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The NCBI row supplies no synonyms, matching the absence of a `synonyms` block.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:1028305` / `Phormidium laetevirens`.

## Completeness

- The record is complete for the exact NCBI row currently present for this strain taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no external taxonomy mapping is currently present for `NCBITaxon:1028306`.
- No external xrefs, genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/phormidium_laetevirens_lege_06103.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/phormidium_laetevirens_lege_06103.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11288, `curation/seed_scope.tsv` row 319626, `data/raw/ncbitaxon_taxa.tsv` row 219118, and YAML lines 1 and 49.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/phormidium_laetevirens_lege_06103.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/phormidium_laetevirens_lege_06103.yaml` directly.
