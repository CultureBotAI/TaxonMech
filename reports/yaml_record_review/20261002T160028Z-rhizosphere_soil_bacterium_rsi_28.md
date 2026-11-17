# YAML Record Review: rhizosphere soil bacterium RSI-28

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/rhizosphere_soil_bacterium_rsi_28.yaml
- Started UTC: 2026-10-02T16:00:28Z
- Finished UTC: 2026-10-02T16:00:28Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102563` |
| Label | `rhizosphere soil bacterium RSI-28` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:49928` |
| Parent label | `unclassified Bacteria` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/rhizosphere_soil_bacterium_rsi_28.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/rhizosphere_soil_bacterium_rsi_28.yaml data/taxa/bacteria/rhizosphere_soil_bacterium_rsi_29.yaml data/taxa/bacteria/rhizosphere_soil_bacterium_rsi_30.yaml data/taxa/bacteria/rhizosphere_soil_bacterium_rsi_31.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 36 lines, 4 lineage entries, 0 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| Direct bounded-source fallback | Pass: found one seed row and one first-column NCBI Taxonomy row; confirmed all 4 first-column lineage rows; and found no GOLD aggregate row or auxiliary exact rows for this identifier. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:102563` trace only to PATHS, the seed row, the NCBI Taxonomy row, and the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10794 maps `NCBITaxon:102563` to `rhizosphere_soil_bacterium_rsi_28`.
- `curation/seed_scope.tsv` row 143767 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 18093 names `NCBITaxon:102563` as `rhizosphere soil bacterium RSI-28`.
- The generated YAML line 1 preserves the NCBI identifier and line 23 preserves the sole NCBI source attestation.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:49928` / `unclassified Bacteria`.
- No external xrefs, taxonomy mappings, strain rows, genome assemblies, genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI row currently present for this taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102563`.
- This review does not infer a deeper placement below the unclassified Bacteria parent.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/rhizosphere_soil_bacterium_rsi_28.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/rhizosphere_soil_bacterium_rsi_28.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10794 |
| `curation/seed_scope.tsv` | 143767 |
| `data/raw/ncbitaxon_taxa.tsv` | 18093 |
| `data/taxa/bacteria/rhizosphere_soil_bacterium_rsi_28.yaml` | 1 and 23 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/rhizosphere_soil_bacterium_rsi_28.yaml`.
- The generated record has no top-level `synonyms`, `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/rhizosphere_soil_bacterium_rsi_28.yaml` directly.
