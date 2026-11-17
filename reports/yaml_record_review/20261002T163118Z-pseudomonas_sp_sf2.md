# YAML Record Review: Pseudomonas sp. SF2

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_sf2.yaml
- Started UTC: 2026-10-02T16:31:18Z
- Finished UTC: 2026-10-02T16:31:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1026793` |
| Label | `Pseudomonas sp. SF2` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:196821` |
| Parent label | `unclassified Pseudomonas` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Taxonomy mappings | `1` |
| External xrefs | `1` |
| Source attestations | `NCBITAXON`, `GTDB` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/pseudomonas_sp_sf2.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_rhf96.yaml data/taxa/bacteria/pseudomonas_sp_sf2.yaml data/taxa/bacteria/bacillus_sp_rhf98.yaml data/taxa/bacteria/bacillus_sp_rhf68.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 73 lines, 10 lineage entries, 1 GTDB synonym, 1 GTDB xref, 1 taxonomy mapping, 0 declared strains, 0 genome assemblies, and 2 source attestations. |
| `taxonmech_bounded_scan.py` | Not checked: the helper exited with `NCBI source mismatch` for this multi-source GTDB rollup; exact raw, StrainInfo, ATB, and curation source scans were used instead. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: `NCBITaxon:1026793` traces to PATHS, the seed row, the first-column NCBI Taxonomy row, and the generated YAML; the GTDB source CURIE traces to `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv`. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10853 maps `NCBITaxon:1026793` to `pseudomonas_sp_sf2`.
- `curation/seed_scope.tsv` row 65990 keeps this taxon in scope with an attested NCBI-plus-GTDB rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218702 names `NCBITaxon:1026793` as `Pseudomonas sp. SF2`, under `NCBITaxon:196821` / `unclassified Pseudomonas`, with `ncbitaxon|gtdb` provenance.
- `data/raw/gtdb_species.tsv` row 11470 names `GTDB:s__Aquipseudomonas_sp001642705` with `GTDB:g__Aquipseudomonas` as the parent and a genome count of 13.
- `data/raw/gtdb_mappings.tsv` row 1201 maps `GTDB:s__Aquipseudomonas_sp001642705` to `NCBITaxon:1026793` with `skos:closeMatch` and a genome count of 13.
- The generated YAML line 1 preserves the NCBI identifier, line 41 preserves the GTDB mapping source ID, line 49 preserves the GTDB synonym source ID, line 56 preserves the NCBI source ID, and line 62 preserves the GTDB source attestation ID.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The GTDB `taxonomy_mappings` block preserves the exact GTDB species ID, label, parent-independent mapping predicate, and 13-genome count from `gtdb_mappings.tsv` row 1201.
- The `Aquipseudomonas sp001642705` exact synonym is derived from the GTDB species label `s__Aquipseudomonas_sp001642705`, and the GTDB xref mirrors the same source CURIE.
- The NCBI source attestation matches the NCBI row's name assertion; the GTDB source attestation matches the 13-genome exact GTDB mapping.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:196821` / `unclassified Pseudomonas`.

## Completeness

- The record is complete for the exact NCBI row and exact `NCBITaxon:1026793` GTDB mapping currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- No genome assemblies, genome records, related records, or causal graphs are expected for the current source set.
- The same GTDB species appears in additional `gtdb_mappings.tsv` rows for other NCBI targets, but only row 1201 owns the `NCBITaxon:1026793` mapping reviewed here.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/pseudomonas_sp_sf2.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/pseudomonas_sp_sf2.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID and GTDB source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 10853, `curation/seed_scope.tsv` row 65990, `data/raw/ncbitaxon_taxa.tsv` row 218702, `data/raw/gtdb_species.tsv` row 11470, `data/raw/gtdb_mappings.tsv` row 1201, and YAML lines 1, 41, 49, 56, and 62.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/pseudomonas_sp_sf2.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/pseudomonas_sp_sf2.yaml` directly.
