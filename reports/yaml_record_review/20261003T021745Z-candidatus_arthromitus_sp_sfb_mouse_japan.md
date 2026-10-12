# YAML Record Review: Candidatus Arthromitus sp. SFB-mouse-Japan

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/candidatus_arthromitus_sp_sfb_mouse_japan.yaml
- Started UTC: 2026-10-03T02:17:45Z
- Finished UTC: 2026-10-03T02:18:03Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1029718` |
| Label | `Candidatus Arthromitus sp. SFB-mouse-Japan` |
| Rank | `ISOLATE` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:49118` |
| Parent label | `Candidatus Arthromitus sp. SFB-mouse` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_arthromitus_sp_sfb_mouse_japan.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/psychrilyobacter_sp_stab704.yaml ... data/taxa/bacteria/pedobacter_sp_fg_18a.yaml` | Pass: the strict mixed ten-file batch scanned 10 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 76 lines, 11 lineage entries, 1 GTDB synonym, 1 xref, 1 taxonomy mapping, 0 declared strains, 0 genome assemblies, and 2 source attestations. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, all 11 first-column lineage rows, one GTDB closeMatch, and no GOLD aggregate or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: ignored-file-inclusive source scans found the expected `ncbitaxon_taxa.tsv`, `gtdb_mappings.tsv`, and `seed_scope.tsv` rows for `NCBITaxon:1029718`, with no exact auxiliary source rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 12282 maps `NCBITaxon:1029718` to `candidatus_arthromitus_sp_sfb_mouse_japan`.
- `curation/seed_scope.tsv` row 65998 keeps this taxon in scope with NCBI and GTDB evidence.
- `data/raw/ncbitaxon_taxa.tsv` row 220049 names `NCBITaxon:1029718` as `Candidatus Arthromitus sp. SFB-mouse-Japan`, under `NCBITaxon:49118` / `Candidatus Arthromitus sp. SFB-mouse`.
- The generated YAML line 1 preserves the NCBI identifier; lines 59 and 65 preserve the NCBI and GTDB source IDs.

## Evidence

- The YAML identifier, isolate rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13 and a GTDB `skos:closeMatch` with 29 genomes.
- The GTDB row maps `GTDB:s__Dwaynesavagella_sp000270205` to this NCBI identifier, matching the taxonomy mapping, GTDB synonym, xref, and GTDB source attestation.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:49118` / `Candidatus Arthromitus sp. SFB-mouse`.

## Completeness

- The record is complete for the exact NCBI and GTDB rows currently present for this SFB mouse isolate.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- The external GTDB taxonomy mapping is represented as both `taxonomy_mappings` and `xrefs`.
- No genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/candidatus_arthromitus_sp_sfb_mouse_japan.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/candidatus_arthromitus_sp_sfb_mouse_japan.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 12282, `curation/seed_scope.tsv` row 65998, `data/raw/ncbitaxon_taxa.tsv` row 220049, `data/raw/gtdb_mappings.tsv` row 1249, and YAML lines 1, 59, and 65.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/candidatus_arthromitus_sp_sfb_mouse_japan.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/candidatus_arthromitus_sp_sfb_mouse_japan.yaml` directly.
