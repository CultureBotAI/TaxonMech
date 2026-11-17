# YAML Record Review: Nocardioides sp. LS1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/nocardioides_sp_ls1.yaml
- Started UTC: 2026-10-02T18:01:37Z
- Finished UTC: 2026-10-02T18:01:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1027620` |
| Label | `Nocardioides sp. LS1` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2615069` |
| Parent label | `unclassified Nocardioides` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Taxonomy mappings | `1` |
| Synonyms | `1` |
| Xrefs | `1` |
| Source attestations | `NCBITAXON`, `GTDB` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/nocardioides_sp_ls1.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/nocardioides_sp_ss4.yaml data/taxa/bacteria/devosia_sp_ss5.yaml data/taxa/bacteria/devosia_sp_rs1.yaml data/taxa/bacteria/nocardioides_sp_ls1.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 73 lines, 10 lineage entries, 1 synonym, 1 xref, 1 taxonomy mapping, 0 declared strains, 0 genome assemblies, and 2 source attestations. |
| Direct exact NCBI/GTDB source scan | Pass: found one seed row, one first-column NCBI Taxonomy row, the exact GTDB mapping row for this identifier, and no auxiliary exact rows for this identifier. |
| Exact GTDB-source scan | Pass: found the GTDB species row with genome count 2 and the `skos:closeMatch` row to `NCBITaxon:1027620` with genome count 2. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11071 maps `NCBITaxon:1027620` to `nocardioides_sp_ls1`.
- `curation/seed_scope.tsv` row 65991 keeps this taxon in scope with a two-source rule covering NCBI Taxonomy and GTDB.
- `data/raw/ncbitaxon_taxa.tsv` row 218902 names `NCBITaxon:1027620` as `Nocardioides sp. LS1`, under `NCBITaxon:2615069` / `unclassified Nocardioides`, with sources `ncbitaxon|gtdb`.
- `data/raw/gtdb_mappings.tsv` row 1216 maps `GTDB:s__Nocardioides_ginsengisegetis` to `NCBITaxon:1027620` with `skos:closeMatch` and 2 genomes.
- `data/raw/gtdb_species.tsv` row 127762 records the same GTDB species under `GTDB:g__Nocardioides` with 2 genomes.
- The generated YAML line 1 preserves the NCBI identifier, lines 39-51 preserve the GTDB mapping, synonym, and xref, and lines 55-66 preserve the two source attestations.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The GTDB `taxonomy_mappings` item preserves the exact GTDB source ID, label, `skos:closeMatch` predicate, and genome count from `data/raw/gtdb_mappings.tsv`.
- The GTDB synonym and xref are the normalized companion assertions for `GTDB:s__Nocardioides_ginsengisegetis`.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:2615069` / `unclassified Nocardioides`.

## Completeness

- The record is complete for the exact NCBI and GTDB rows currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, exact GOLD, and exact strain-related source rows.
- The exact GTDB species scan found an LPSN row for `NCBITaxon:661491`, not for `NCBITaxon:1027620`, so it does not create an additional LPSN attestation on this record.
- No genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/nocardioides_sp_ls1.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/nocardioides_sp_ls1.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11071, `curation/seed_scope.tsv` row 65991, `data/raw/ncbitaxon_taxa.tsv` row 218902, `data/raw/gtdb_mappings.tsv` row 1216, `data/raw/gtdb_species.tsv` row 127762, YAML line 1, YAML lines 39-51, and YAML lines 55-66.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/nocardioides_sp_ls1.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/nocardioides_sp_ls1.yaml` directly.
