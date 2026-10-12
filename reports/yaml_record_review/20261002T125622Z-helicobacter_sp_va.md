# YAML Record Review: Helicobacter sp. VA

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/helicobacter_sp_va.yaml
- Started UTC: 2026-10-02T12:56:22Z
- Finished UTC: 2026-10-02T12:56:22Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102212` |
| Label | `Helicobacter sp. VA` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2593540` |
| Parent label | `unclassified Helicobacter` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/helicobacter_sp_va.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/beggiatoa_alba.yaml data/taxa/bacteria/helicobacter_sp_va.yaml data/taxa/bacteria/bacterium_i1.yaml data/taxa/bacteria/thermus_sp_env_os_ac7.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 53 lines, 10 lineage entries, 0 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| `taxonmech_bounded_scan.py` for this YAML | Pass: found one seed row and one NCBI Taxonomy row; confirmed all 10 lineage rows; and found no native GOLD organism, project, or analysis rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:102212' data/raw curation data/taxa/bacteria/helicobacter_sp_va.yaml` | Pass: all checked occurrences trace to the seed, NCBI Taxonomy source, and generated YAML rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10536 maps `NCBITaxon:102212` to `helicobacter_sp_va`.
- `curation/seed_scope.tsv` row 143514 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17832 names `NCBITaxon:102212` as `Helicobacter sp. VA`.
- The generated YAML line 1 preserves the NCBI identifier and line 43 preserves the sole NCBI source attestation.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:2593540` / `unclassified Helicobacter`.
- No source synonyms, external xrefs, strain rows, genome assemblies, genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI row currently present for this taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102212`.
- This review did not infer a deeper placement below the unclassified Helicobacter parent.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/helicobacter_sp_va.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/helicobacter_sp_va.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10536 |
| `curation/seed_scope.tsv` | 143514 |
| `data/raw/ncbitaxon_taxa.tsv` | 17832 |
| `data/taxa/bacteria/helicobacter_sp_va.yaml` | 1 and 43 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/helicobacter_sp_va.yaml`.
- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/helicobacter_sp_va.yaml` directly.
