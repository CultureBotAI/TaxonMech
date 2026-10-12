# YAML Record Review: Helicobacter pylori J166

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/helicobacter_pylori_j166.yaml
- Started UTC: 2026-10-02T16:15:27Z
- Finished UTC: 2026-10-02T16:15:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102611` |
| Label | `Helicobacter pylori J166` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:210` |
| Parent label | `Helicobacter pylori` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/helicobacter_pylori_j166.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/helicobacter_pylori_f32.yaml data/taxa/bacteria/helicobacter_pylori_hp1.yaml data/taxa/bacteria/helicobacter_pylori_12.yaml data/taxa/bacteria/helicobacter_pylori_j166.yaml` | Pass: the strict four-file batch scanned 4 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 76 lines, 10 lineage entries, 2 synonyms, 1 xref, 0 declared strains, 0 genome assemblies, and 2 source attestations. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:102611` trace to PATHS, seed scope, NCBI Taxonomy, GTDB mapping, and the generated YAML. |
| Direct GTDB source scan | Pass: first-column `GTDB:s__Helicobacter_pylori` rows confirm the GTDB species source and the exact mapping to `NCBITaxon:102611`. |
| Direct auxiliary exact-ID scan | Pass: no `data/atb/` or `data/straininfo/` rows mention `NCBITaxon:102611`. |
| Direct lineage source scan | Pass: all 10 lineage identifiers resolve as first-column rows in `data/raw/ncbitaxon_taxa.tsv`. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10823 maps `NCBITaxon:102611` to `helicobacter_pylori_j166`.
- `curation/seed_scope.tsv` row 64048 keeps this taxon in scope with an attested two-source rule including NCBI.
- `data/raw/ncbitaxon_taxa.tsv` row 18121 names `NCBITaxon:102611` as the strain `Helicobacter pylori J166`.
- `data/raw/gtdb_mappings.tsv` row 1197 maps `GTDB:s__Helicobacter_pylori` to `NCBITaxon:102611` with `skos:closeMatch` and a genome count of 633.

## Evidence

- The YAML identifier, strain rank, label, parent species, and genetic code agree with the exact NCBI Taxonomy row.
- The record preserves the NCBI synonym `Helicobacter pylori (strain J166)` from `data/raw/ncbitaxon_taxa.tsv` row 18121.
- The GTDB taxonomy mapping, xref, stripped exact synonym text, `skos:closeMatch` predicate, and 633-genome attestation are backed by `data/raw/gtdb_species.tsv` row 73699 and `data/raw/gtdb_mappings.tsv` row 1197.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:210` / `Helicobacter pylori`.
- The generated YAML keeps the NCBI and GTDB attestations in separate `NAME` and `GENOME` units.

## Completeness

- The record is complete for the exact NCBI and GTDB source rows currently present for this strain taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, exact GOLD aggregate, and other exact strain-related source rows.
- No genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/helicobacter_pylori_j166.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/helicobacter_pylori_j166.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 10823, `curation/seed_scope.tsv` row 64048, `data/raw/gtdb_mappings.tsv` row 1197, `data/raw/gtdb_species.tsv` row 73699, and `data/raw/ncbitaxon_taxa.tsv` row 18121.
- YAML lines 1, 57, 59, and 65 preserve the identifier, source-attestation block, and two source IDs.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/helicobacter_pylori_j166.yaml` directly.
