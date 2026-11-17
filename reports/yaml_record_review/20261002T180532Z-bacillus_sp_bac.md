# YAML Record Review: Bacillus sp. BAC

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/bacillus_sp_bac.yaml
- Started UTC: 2026-10-02T18:05:32Z
- Finished UTC: 2026-10-02T18:05:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1027627` |
| Label | `Bacillus sp. BAC` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:185979` |
| Parent label | `unclassified Bacillus (in: firmicutes)` |
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
| `just validate data/taxa/bacteria/bacillus_sp_bac.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/nocardioides_sp_ymn1.yaml data/taxa/bacteria/nocardioides_sp_pfs1.yaml data/taxa/bacteria/bacillus_sp_bac.yaml data/taxa/bacteria/bacillus_sp_ce2.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 73 lines, 10 lineage entries, 1 synonym, 1 xref, 1 taxonomy mapping, 0 declared strains, 0 genome assemblies, and 2 source attestations. |
| Direct exact NCBI/GTDB source scan | Pass: found one seed row, one first-column NCBI Taxonomy row, the exact GTDB mapping row for this identifier, and no auxiliary exact rows for this identifier. |
| Exact GTDB-source scan | Pass: found the GTDB species row with genome count 479 and the `skos:closeMatch` row to `NCBITaxon:1027627` with genome count 479. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11078 maps `NCBITaxon:1027627` to `bacillus_sp_bac`.
- `curation/seed_scope.tsv` row 65992 keeps this taxon in scope with a two-source rule covering NCBI Taxonomy and GTDB.
- `data/raw/ncbitaxon_taxa.tsv` row 218909 names `NCBITaxon:1027627` as `Bacillus sp. BAC`, under `NCBITaxon:185979` / `unclassified Bacillus (in: firmicutes)`, with sources `ncbitaxon|gtdb`.
- `data/raw/gtdb_mappings.tsv` row 1217 maps `GTDB:s__Bacillus_licheniformis` to `NCBITaxon:1027627` with `skos:closeMatch` and 479 genomes.
- `data/raw/gtdb_species.tsv` row 16173 records the same GTDB species under `GTDB:g__Bacillus` with 479 genomes.
- The generated YAML line 1 preserves the NCBI identifier, lines 39-51 preserve the GTDB mapping, synonym, and xref, and lines 55-66 preserve the two source attestations.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The GTDB `taxonomy_mappings` item preserves the exact GTDB source ID, label, `skos:closeMatch` predicate, and genome count from `data/raw/gtdb_mappings.tsv`.
- The GTDB synonym and xref are the normalized companion assertions for `GTDB:s__Bacillus_licheniformis`.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:185979` / `unclassified Bacillus (in: firmicutes)`.

## Completeness

- The record is complete for the exact NCBI and GTDB rows currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, exact GOLD, and exact strain-related source rows.
- The exact GTDB species scan found other NCBI mappings, including an LPSN-backed `NCBITaxon:1402` row, but they do not create additional attestations on `NCBITaxon:1027627`.
- No genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/bacillus_sp_bac.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/bacillus_sp_bac.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11078, `curation/seed_scope.tsv` row 65992, `data/raw/ncbitaxon_taxa.tsv` row 218909, `data/raw/gtdb_mappings.tsv` row 1217, `data/raw/gtdb_species.tsv` row 16173, YAML line 1, YAML lines 39-51, and YAML lines 55-66.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/bacillus_sp_bac.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/bacillus_sp_bac.yaml` directly.
