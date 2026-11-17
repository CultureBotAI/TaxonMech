# YAML Record Review: Coriobacterium sp. H818

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/coriobacterium_sp_h818.yaml
- Started UTC: 2026-10-02T13:07:32Z
- Finished UTC: 2026-10-02T13:07:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102229` |
| Label | `Coriobacterium sp. H818` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:2629388` |
| Parent label | `unclassified Coriobacterium` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/coriobacterium_sp_h818.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/coriobacterium_sp_g118.yaml data/taxa/bacteria/coriobacterium_sp_h818.yaml data/taxa/bacteria/coriobacterium_sp_ekso3.yaml data/taxa/bacteria/gloeocapsa_sp_pcc_73106.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 54 lines, 10 lineage entries, 0 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| `taxonmech_bounded_scan.py` for this YAML | Not checked: this helper was stopped after producing no prompt output for this 54-line NCBI-only record; the exact raw-source and lineage scans passed instead. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| `rg --no-ignore --hidden -n 'NCBITaxon:102229' data/raw curation data/taxa/bacteria/coriobacterium_sp_h818.yaml` | Pass: all checked occurrences trace to the seed, NCBI Taxonomy source, and generated YAML rows. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10552 maps `NCBITaxon:102229` to `coriobacterium_sp_h818`.
- `curation/seed_scope.tsv` row 143528 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17848 names `NCBITaxon:102229` as `Coriobacterium sp. H818`.
- The generated YAML line 1 preserves the NCBI identifier and line 43 preserves the sole NCBI source attestation.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:2629388` / `unclassified Coriobacterium`.
- No source synonyms, external xrefs, strain rows, genome assemblies, genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI row currently present for this taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102229`.
- This review did not infer a deeper placement below the unclassified Coriobacterium parent.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/coriobacterium_sp_h818.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/coriobacterium_sp_h818.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10552 |
| `curation/seed_scope.tsv` | 143528 |
| `data/raw/ncbitaxon_taxa.tsv` | 17848 |
| `data/taxa/bacteria/coriobacterium_sp_h818.yaml` | 1 and 43 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/coriobacterium_sp_h818.yaml`.
- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `synonyms`, `xrefs`, `strains`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/coriobacterium_sp_h818.yaml` directly.
