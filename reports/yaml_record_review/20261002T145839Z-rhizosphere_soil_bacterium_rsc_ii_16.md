# YAML Record Review: rhizosphere soil bacterium RSC-II-16

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_16.yaml
- Started UTC: 2026-10-02T14:58:39Z
- Finished UTC: 2026-10-02T14:58:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102473` |
| Label | `rhizosphere soil bacterium RSC-II-16` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:150475` |
| Parent label | `rhizosphere soil bacteria ensemble` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_16.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_11.yaml data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_13.yaml data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_16.yaml data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_17.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 39 lines, 5 lineage entries, 0 synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| `taxonmech_bounded_scan.py` for this YAML | Pass: found one seed row and one NCBI Taxonomy row; confirmed all 5 lineage rows; and found no native GOLD organism, project, or analysis rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:102473` trace only to PATHS, the seed row, the NCBI Taxonomy row, and the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10703 maps `NCBITaxon:102473` to `rhizosphere_soil_bacterium_rsc_ii_16`.
- `curation/seed_scope.tsv` row 143677 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 18003 names `NCBITaxon:102473` as `rhizosphere soil bacterium RSC-II-16`.
- The generated YAML line 1 preserves the NCBI identifier and line 26 preserves the sole NCBI source attestation.

## Evidence

- The YAML identifier, species rank, label, parent taxon, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:150475` / `rhizosphere soil bacteria ensemble`.
- No external xrefs, taxonomy mappings, strain rows, genome assemblies, genome records, or causal graphs are expected for the current source set.

## Completeness

- The record is complete for the exact NCBI row currently present for this taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102473`.
- This review does not infer a deeper placement below the rhizosphere soil bacteria ensemble parent.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_16.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_16.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10703 |
| `curation/seed_scope.tsv` | 143677 |
| `data/raw/ncbitaxon_taxa.tsv` | 18003 |
| `data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_16.yaml` | 1 and 26 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_16.yaml`.
- The generated record has no top-level `synonyms`, `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/rhizosphere_soil_bacterium_rsc_ii_16.yaml` directly.
