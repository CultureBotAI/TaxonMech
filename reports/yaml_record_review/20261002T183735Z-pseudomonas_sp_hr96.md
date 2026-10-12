# YAML Record Review: Pseudomonas sp. HR96

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_hr96.yaml
- Started UTC: 2026-10-02T18:37:35Z
- Finished UTC: 2026-10-02T18:37:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1027966` |
| Label | `Pseudomonas sp. HR96` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:196821` |
| Parent label | `unclassified Pseudomonas` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Taxonomy mappings | `1` |
| Synonyms | `1` |
| Xrefs | `1` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/pseudomonas_sp_hr96.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_hr94.yaml data/taxa/bacteria/pseudomonas_sp_hr96.yaml data/taxa/bacteria/pseudomonas_sp_hr97.yaml data/taxa/bacteria/pseudomonas_sp_hr99.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 73 lines, 10 lineage entries, 1 GTDB taxonomy mapping, 1 GTDB synonym, 1 GTDB xref, 0 declared strains, 0 genome assemblies, and 2 source attestations. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy row, one GTDB species row, one GTDB mapping row, all 10 first-column lineage rows, and no GOLD aggregate or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID and GTDB scan | Pass: source rows for `NCBITaxon:1027966` and `GTDB:s__Aquipseudomonas_sp034059295` trace to PATHS, seed, NCBI Taxonomy, GTDB species, GTDB mapping, and the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11142 maps `NCBITaxon:1027966` to `pseudomonas_sp_hr96`.
- `curation/seed_scope.tsv` row 65993 keeps this taxon in scope with an attested two-source NCBI plus GTDB rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218973 names `NCBITaxon:1027966` as `Pseudomonas sp. HR96`, under `NCBITaxon:196821` / `unclassified Pseudomonas`, with sources `ncbitaxon|gtdb`.
- `data/raw/gtdb_species.tsv` row 11700 records `GTDB:s__Aquipseudomonas_sp034059295` as `s__Aquipseudomonas_sp034059295` under `GTDB:g__Aquipseudomonas` with 1 genome.
- `data/raw/gtdb_mappings.tsv` row 1219 maps that GTDB species to `NCBITaxon:1027966` by `skos:closeMatch` with genome count 1.
- The generated YAML line 1 preserves the NCBI identifier, lines 37-41 preserve the GTDB closeMatch, lines 45-52 preserve the GTDB synonym and xref, and lines 56 and 62 preserve the NCBI and GTDB source IDs.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded from NCBI Taxonomy snapshot 2026-09-13 and GTDB support for `s__Aquipseudomonas_sp034059295`.
- The GTDB closeMatch, exact synonym, xref, and genome-count attestation agree with `data/raw/gtdb_species.tsv` and `data/raw/gtdb_mappings.tsv`.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:196821` / `unclassified Pseudomonas`.

## Completeness

- The record is complete for the exact NCBI and GTDB rows currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, exact GOLD, and exact strain-related source rows.
- No genome assemblies, genome records, related records, or causal graphs are expected for the current NCBI plus GTDB source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/pseudomonas_sp_hr96.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/pseudomonas_sp_hr96.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID and GTDB source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11142, `curation/seed_scope.tsv` row 65993, `data/raw/ncbitaxon_taxa.tsv` row 218973, `data/raw/gtdb_species.tsv` row 11700, `data/raw/gtdb_mappings.tsv` row 1219, YAML line 1, YAML lines 37-41, YAML lines 45-52, and YAML lines 56 and 62.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/pseudomonas_sp_hr96.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/pseudomonas_sp_hr96.yaml` directly.
