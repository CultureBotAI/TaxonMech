# YAML Record Review: Ehrlichia sp. CASC

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/ehrlichia_sp_casc.yaml
- Started UTC: 2026-10-02T11:26:42Z
- Finished UTC: 2026-10-02T11:26:42Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:101948` |
| Label | `Ehrlichia sp. CASC` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:106181` |
| Parent label | `unclassified Ehrlichia` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/ehrlichia_sp_casc.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/capnocytophaga_sputigena.yaml data/taxa/bacteria/ehrlichia_sp_casc.yaml` | Pass: the strict two-file batch scanned 2 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 53 lines, 10 lineage entries, 0 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| `taxonmech_bounded_scan.py` for this YAML | Pass: found one seed row and one NCBI Taxonomy row; confirmed all 10 lineage rows; and found no native GOLD organism, project, or analysis rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:101948\|Ehrlichia sp. CASC' data curation` | Pass: found the expected source and generated YAML rows for this NCBI-only species. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10410 maps `NCBITaxon:101948` to `ehrlichia_sp_casc`.
- `curation/seed_scope.tsv` row 143400 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17706 names `NCBITaxon:101948` as `Ehrlichia sp. CASC`.
- The generated YAML line 1 preserves the NCBI identifier and line 43 preserves the sole NCBI source attestation.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:106181` / `unclassified Ehrlichia`.
- No source synonyms, external xrefs, strain rows, genome assemblies, genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI row currently present for this taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:101948`.
- This review does not infer a deeper placement below the unclassified Ehrlichia parent.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/ehrlichia_sp_casc.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/ehrlichia_sp_casc.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10410 |
| `curation/seed_scope.tsv` | 143400 |
| `data/raw/ncbitaxon_taxa.tsv` | 17706 |
| `data/taxa/bacteria/ehrlichia_sp_casc.yaml` | 1 and 43 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/ehrlichia_sp_casc.yaml`.
- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/ehrlichia_sp_casc.yaml` directly.
