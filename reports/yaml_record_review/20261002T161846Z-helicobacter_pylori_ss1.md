# YAML Record Review: Helicobacter pylori SS1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/helicobacter_pylori_ss1.yaml
- Started UTC: 2026-10-02T16:18:46Z
- Finished UTC: 2026-10-02T16:18:46Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:102617` |
| Label | `Helicobacter pylori SS1` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:210` |
| Parent label | `Helicobacter pylori` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `0` |
| Source attestations | `NCBITAXON`, `GTDB`, `MADIN` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/helicobacter_pylori_ss1.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/helicobacter_pylori_n6.yaml data/taxa/bacteria/helicobacter_pylori_ss1.yaml` | Pass: the strict two-file batch scanned 2 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 81 lines, 10 lineage entries, 2 synonyms, 1 xref, 0 declared strains, 0 genome assemblies, and 3 source attestations. |
| Direct raw/curation exact-ID scan | Pass: source rows for `NCBITaxon:102617` trace to PATHS, legacy page paths, seed scope, MADIN, NCBI Taxonomy, GTDB mapping, and the generated YAML. |
| Direct GTDB source scan | Pass: first-column `GTDB:s__Helicobacter_pylori` rows confirm the GTDB species source and the exact mapping to `NCBITaxon:102617`. |
| Direct auxiliary exact-ID scan | Pass: no `data/atb/` or `data/straininfo/` rows mention `NCBITaxon:102617`. |
| Direct lineage source scan | Pass: all 10 lineage identifiers resolve as first-column rows in `data/raw/ncbitaxon_taxa.tsv`. |
| Exact ignored-file-inclusive report preflight | Pass: no prior report existed for this stem. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10829 maps `NCBITaxon:102617` to `helicobacter_pylori_ss1`.
- `curation/seed_scope.tsv` row 31672 keeps this taxon in scope with an attested three-source rule including NCBI.
- `data/raw/ncbitaxon_taxa.tsv` row 18127 names `NCBITaxon:102617` as the strain `Helicobacter pylori SS1`.
- `data/raw/gtdb_mappings.tsv` row 1199 maps `GTDB:s__Helicobacter_pylori` to `NCBITaxon:102617` with `skos:closeMatch` and a genome count of 633.
- `data/raw/madin_taxa.tsv` row 499 backs the MADIN `TRAIT_ASSERTION` count of 5 for `NCBITaxon:102617`.

## Evidence

- The YAML identifier, strain rank, label, parent species, and genetic code agree with the exact NCBI Taxonomy row.
- The record preserves the NCBI synonym `Helicobacter pylori (strain SS1)` from `data/raw/ncbitaxon_taxa.tsv` row 18127.
- The GTDB taxonomy mapping, xref, stripped exact synonym text, `skos:closeMatch` predicate, and 633-genome attestation are backed by `data/raw/gtdb_species.tsv` row 73699 and `data/raw/gtdb_mappings.tsv` row 1199.
- The `lineage` block is a root-first NCBI chain ending at `NCBITaxon:210` / `Helicobacter pylori`.
- The generated YAML keeps the NCBI, GTDB, and MADIN attestations in separate units instead of summing names, genomes, and trait assertions.

## Completeness

- The record is complete for the exact NCBI, GTDB, and MADIN source rows currently present for this strain taxon.
- `strain_count: 0` is consistent with the absence of BacDive, culture-collection, StrainInfo, ATB, exact GOLD aggregate, and other exact strain-related source rows.
- No genome assemblies, genome records, related records, or causal graphs are expected for the current source set.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/helicobacter_pylori_ss1.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/helicobacter_pylori_ss1.yaml`.
- Re-run `just verify-corpus`.
- Re-run the direct exact-ID source scan after any refresh of `data/raw/`, `data/straininfo/`, `data/atb/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors: `data/taxa/PATHS.tsv` row 10829, `curation/seed_scope.tsv` row 31672, `data/raw/madin_taxa.tsv` row 499, `data/raw/gtdb_mappings.tsv` row 1199, `data/raw/gtdb_species.tsv` row 73699, and `data/raw/ncbitaxon_taxa.tsv` row 18127.
- YAML lines 1, 57, 59, 65, and 71 preserve the identifier, source-attestation block, and three source IDs.
- Future corrections belong in the upstream source extraction, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/helicobacter_pylori_ss1.yaml` directly.
