# YAML Record Review: Hyphomicrobium nitrativorans NL23

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/hyphomicrobium_nitrativorans_nl23.yaml
- Started UTC: 2026-10-03T02:17:45Z
- Finished UTC: 2026-10-03T02:18:03Z
- Verdict: needs-curation

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1029756` |
| Label | `Hyphomicrobium nitrativorans NL23` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:1427356` |
| Parent label | `Hyphomicrobium nitrativorans` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/hyphomicrobium_nitrativorans_nl23.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/psychrilyobacter_sp_stab704.yaml ... data/taxa/bacteria/pedobacter_sp_fg_18a.yaml` | Pass: the strict mixed ten-file batch scanned 10 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 81 lines, 10 lineage entries, 2 synonyms, 1 xref, 1 taxonomy mapping, 0 declared strains, 0 genome assemblies, and 3 source attestations. |
| Direct bounded-source fallback | Needs curation: exact scans found the expected seed, NCBI, GTDB, and MADIN rows, but also found BacDive/GOLD genome and related-record rows that are absent from the YAML. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Needs curation: ignored-file-inclusive source scans found exact `strain_assemblies.tsv`, `strain_genome_records.tsv`, and `strain_related_records.tsv` rows for `NCBITaxon:1029756`. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 12285 maps `NCBITaxon:1029756` to `hyphomicrobium_nitrativorans_nl23`.
- `curation/seed_scope.tsv` row 36106 keeps this taxon in scope with NCBI, GTDB, and MADIN evidence.
- `data/raw/ncbitaxon_taxa.tsv` row 220052 names `NCBITaxon:1029756` as `Hyphomicrobium nitrativorans NL23`, under `NCBITaxon:1427356` / `Hyphomicrobium nitrativorans`.
- The generated YAML line 1 preserves the NCBI identifier; lines 59, 65, and 71 preserve the NCBI, GTDB, and MADIN source IDs.

## Evidence

- The YAML identifier, strain rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The NCBI row supplies `Hyphomicrobium sp. NL23`, and the GTDB row supplies `Hyphomicrobium C nitrativorans`, matching the two-entry `synonyms` block.
- The GTDB `skos:closeMatch` is represented as both `taxonomy_mappings` and `xrefs`.
- The MADIN row at `data/raw/madin_taxa.tsv` row 544 supports the retained MADIN source attestation with 6 trait assertions.

## Completeness

- The NCBI, GTDB, and MADIN evidence currently present for this strain-level record is represented.
- Exact raw scans also found two strain assembly rows, three strain genome-record rows, and four strain related-record rows for `NCBITaxon:1029756`.
- The generated YAML has no `genome_assemblies`, `genome_records`, or `related_records`, so the BacDive/GOLD genome evidence is currently dropped.
- Exact BacDive and StrainInfo rows for the same local strain are filed under the parent species taxon, so the strain evidence needs a seeder-side decision rather than a manual YAML-only edit.

## Findings

- Major: exact BacDive/GOLD genome and related-record rows for `NCBITaxon:1029756` are absent from the generated YAML even though the record retains NCBI, GTDB, and MADIN evidence.

## Recommended Edits

- Investigate why `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` rows keyed to `NCBITaxon:1029756` do not generate genome or related-record entries for this strain.
- Either emit the BacDive/GOLD genome evidence into `data/taxa/bacteria/hyphomicrobium_nitrativorans_nl23.yaml` or document why the rows should remain side evidence.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/hyphomicrobium_nitrativorans_nl23.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/hyphomicrobium_nitrativorans_nl23.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 12285, `curation/seed_scope.tsv` row 36106, `data/raw/ncbitaxon_taxa.tsv` row 220052, and YAML lines 1, 59, 65, and 71.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/hyphomicrobium_nitrativorans_nl23.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/hyphomicrobium_nitrativorans_nl23.yaml` directly.
