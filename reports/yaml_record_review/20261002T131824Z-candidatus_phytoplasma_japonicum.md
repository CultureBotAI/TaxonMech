# YAML Record Review: Candidatus Phytoplasma japonicum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/candidatus_phytoplasma_japonicum.yaml
- Started UTC: 2026-10-02T13:18:24Z
- Finished UTC: 2026-10-02T13:18:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102262` |
| Label | `Candidatus Phytoplasma japonicum` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:3042590` |
| Parent label | `16SrI (Aster yellows group)` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/candidatus_phytoplasma_japonicum.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/uncultured_beta_proteobacterium_wekr_2.yaml data/taxa/bacteria/uncultured_beta_proteobacterium_wekr_3.yaml data/taxa/bacteria/candidatus_phytoplasma_brasiliense.yaml data/taxa/bacteria/candidatus_phytoplasma_japonicum.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 67 lines, 10 lineage entries, 4 NCBI synonyms, 0 xrefs, 0 declared strains, 0 genome assemblies, and 1 source attestation. |
| `taxonmech_bounded_scan.py` for this YAML | Pass: found one seed row and one NCBI Taxonomy row; confirmed all 10 lineage rows; and found no native GOLD organism, project, or analysis rows. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:102262` trace only to PATHS, the seed row, the NCBI Taxonomy row, and the generated YAML. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10566 maps `NCBITaxon:102262` to `candidatus_phytoplasma_japonicum`.
- `curation/seed_scope.tsv` row 143540 keeps this taxon in scope with an attested NCBI-only rule.
- `data/raw/ncbitaxon_taxa.tsv` row 17865 names `NCBITaxon:102262` as `Candidatus Phytoplasma japonicum`.
- The generated YAML line 1 preserves the NCBI identifier, lines 39-51 preserve all four NCBI synonyms, and line 54 preserves the sole NCBI source attestation.

## Evidence

- The YAML identifier, species rank, label, parent taxon, lineage, and genetic code agree with the exact NCBI Taxonomy row.
- The record is seeded exactly from NCBI Taxonomy snapshot 2026-09-13.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:3042590` / `16SrI (Aster yellows group)`.
- The authored-name and `JHP` related synonyms and both exact synonyms from NCBI Taxonomy are present and sourced from NCBI Taxonomy.

## Completeness

- The record is complete for the exact NCBI row currently present for this taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, and exact strain-related source rows.
- `taxonomy_mappings` is absent because no GTDB or other external taxonomy mapping is currently present for `NCBITaxon:102262`.
- No top-level `xrefs`, `genomes`, or `causal_graphs` blocks are expected for this generated species record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/candidatus_phytoplasma_japonicum.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/candidatus_phytoplasma_japonicum.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10566 |
| `curation/seed_scope.tsv` | 143540 |
| `data/raw/ncbitaxon_taxa.tsv` | 17865 |
| `data/taxa/bacteria/candidatus_phytoplasma_japonicum.yaml` | 1, 39, and 54 |

- Direct lineage checks covered every lineage id in `data/taxa/bacteria/candidatus_phytoplasma_japonicum.yaml`.
- The generated record has no top-level `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, `genomes`, or `causal_graphs` blocks.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/candidatus_phytoplasma_japonicum.yaml` directly.
