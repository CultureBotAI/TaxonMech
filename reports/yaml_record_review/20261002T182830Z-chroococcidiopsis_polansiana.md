# YAML Record Review: Chroococcidiopsis polansiana

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/chroococcidiopsis_polansiana.yaml
- Started UTC: 2026-10-02T18:28:30Z
- Finished UTC: 2026-10-02T18:28:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1027909` |
| Label | `Chroococcidiopsis polansiana` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:54298` |
| Parent label | `Chroococcidiopsis` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Synonyms | `1` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/chroococcidiopsis_polansiana.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/desulfovibrio_sp_enrichment_culture_clone_83.yaml data/taxa/bacteria/chroococcidiopsis_polansiana.yaml data/taxa/bacteria/micromonospora_sp_scsio_n160.yaml data/taxa/bacteria/agrobacterium_sp_wr57.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 58 lines, 10 lineage entries, 1 synonym, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| Direct bounded-source fallback | Pass: found one seed row, one first-column NCBI Taxonomy species row, one NCBI child strain row parented to this identifier, all 10 first-column lineage rows, and no GOLD aggregate or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation target-ID scan | Pass: source rows for `NCBITaxon:1027909` trace to PATHS, the seed row, the exact NCBI species row, one NCBI child-strain parent reference, and the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 11122 maps `NCBITaxon:1027909` to `chroococcidiopsis_polansiana`.
- `curation/seed_scope.tsv` row 319465 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 218953 names `NCBITaxon:1027909` as `Chroococcidiopsis polansiana`, under `NCBITaxon:54298` / `Chroococcidiopsis`.
- The generated YAML line 1 preserves the NCBI identifier, lines 38-41 preserve the single NCBI related synonym, and line 47 preserves the sole NCBI source ID.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The single NCBI related synonym matches the synonym in `data/raw/ncbitaxon_taxa.tsv`.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:54298` / `Chroococcidiopsis`.

## Completeness

- The record is complete for the exact NCBI row currently present for this species taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, exact GOLD, and exact strain-related source rows.
- `data/raw/ncbitaxon_taxa.tsv` row 34969 records a child strain taxon parented to `NCBITaxon:1027909`; that child is not an exact attestation for this species YAML.
- `taxonomy_mappings` is absent because no external taxonomy mapping is currently present for `NCBITaxon:1027909`.
- No external xrefs, genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/chroococcidiopsis_polansiana.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/chroococcidiopsis_polansiana.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 11122, `curation/seed_scope.tsv` row 319465, `data/raw/ncbitaxon_taxa.tsv` rows 34969 and 218953, YAML line 1, YAML lines 38-41, and YAML line 47.
- Direct lineage checks covered every lineage id in `data/taxa/bacteria/chroococcidiopsis_polansiana.yaml`.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/chroococcidiopsis_polansiana.yaml` directly.
