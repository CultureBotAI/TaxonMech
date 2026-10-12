# YAML Record Review: Rubrobacter bracarensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/rubrobacter_bracarensis.yaml
- Started UTC: 2026-10-02T10:50:06Z
- Finished UTC: 2026-10-02T10:50:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1017354` |
| Label | `Rubrobacter bracarensis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent taxon | `NCBITaxon:42255` |
| Parent label | `Rubrobacter` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Genetic code | `11` |
| Declared strains | `3` |
| Source attestations | `NCBITAXON`, `LPSN`, `BACDIVE`, `MEDIADIVE`, `GOLD`, `BACTOTRAITS` |

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/rubrobacter_bracarensis.yaml` | Pass: `No issues found`. |
| `just validate-strict data/taxa/bacteria/rubrobacter_bracarensis.yaml data/taxa/bacteria/pseudoalteromonas_sp_ws02.yaml data/taxa/bacteria/roseobacter_sp_ws3_3.yaml data/taxa/bacteria/ruegeria_sp_ws1_3.yaml data/taxa/bacteria/vibrio_sp_ws04.yaml` | Pass: the strict five-file batch scanned 5 files and reported 0 error rows. |
| `just verify-corpus` | Pass: the last full-corpus run in this checkout reproduced the generated corpus exactly: 625960 expected, 625960 found, 0 missing, 0 extra, and 0 differing. |
| `taxonmech_yaml_summary.py` for this YAML | Pass: 356 lines, 9 lineage entries, 4 NCBI synonyms, 1 LPSN nomenclature entry, 1 xref, 3 BacDive strains, 0 genome assemblies, 0 genome records, 0 causal graphs, and 6 source attestations. |
| Bounded simple-source scan | Not applicable: this multi-source NCBI row correctly fails the NCBITaxon-only helper with `NCBI source mismatch`; direct row checks covered the retained NCBI, LPSN, BacDive, MediaDive, GOLD, BactoTraits, StrainInfo, type-material, and lineage claims instead. |
| Direct raw-source, StrainInfo, GOLD, and lineage scans for this YAML | Pass: found the expected seed, NCBI, LPSN, BacDive, MediaDive, BactoTraits, GOLD aggregate, NCBI type-material, NCBI merge, culture-collection, StrainInfo, and GOLD organism rows; the exact first-column NCBI lineage scan matched all 9 YAML lineage rows. |
| `rg --no-ignore --hidden --files reports/yaml_record_review -g '*rubrobacter_bracarensis.md'` | Pass: no prior report existed for this stem. |
| Exact ignored-inclusive history search | Pass: no append-only `history/` entry referred to `NCBITaxon:1017354`, `Rubrobacter bracarensis`, or `rubrobacter_bracarensis`. |

## Identity and Grounding

- `data/taxa/PATHS.tsv` row 10342 maps `NCBITaxon:1017354` to `rubrobacter_bracarensis`.
- `curation/seed_scope.tsv` row 8797 keeps this taxon in scope with six source families including NCBI.
- `data/raw/ncbitaxon_taxa.tsv` row 218680 names `NCBITaxon:1017354` as `Rubrobacter bracarensis`.
- The NCBI row supplies the species rank, `Rubrobacter` parent, genetic code 11, four related synonyms, and the expected `ncbitaxon|bacdive|lpsn|mediadive|gold|bactotraits` source set.

## Evidence

- The YAML identity, species rank, parent taxon, NCBI synonyms, genetic code, source set, and 2026-09-13 NCBI snapshot agree with the exact NCBI Taxonomy row.
- `data/raw/lpsn_names.tsv` row 27566 supports `lpsn:790626`, the validly published legitimate correct-name status, the Jurado/Albuquerque authority string, the LPSN URL, `INSDC:FR852390`, two type-strain designations, two DOIs, and `PMID:22776713`.
- `data/raw/bacdive_strains.tsv` rows 24102-24104 support the three retained BacDive strains, including the type-strain flag on `bacdive:24537` / `VF70612_S1`.
- `data/straininfo/strain_links.tsv` rows 82967-82970 support the retained CECT 7924, DSM 24908, DSM 24909, and DSM 24910 StrainInfo related records.
- `data/raw/strain_related_records.tsv` rows 331096-331099 support the retained GOLD organism links for DSM 24908 and CECT 7924.
- The MediaDive, BactoTraits, GOLD aggregate, NCBI type-material, and NCBI merge side tables account for the remaining source-attestation counts or non-generated side facts.

## Completeness

- The generated record is complete for the Rubrobacter bracarensis source rows currently present.
- `strain_count: 3` matches the three exact BacDive rows for `NCBITaxon:1017354`.
- No genome assemblies, genome records, top-level taxonomy mappings, or causal graphs are expected from the current source rows.
- The excluded StrainInfo deposit `straininfo.deposit:898843` is not generated here because `data/straininfo/exclusions.tsv` marks it as a conflicting BacDive reference for a different deposit match.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/rubrobacter_bracarensis.yaml`.
- Re-run `just validate-strict data/taxa/bacteria/rubrobacter_bracarensis.yaml`.
- Re-run `just verify-corpus`.
- Re-run exact source-row probes after any refresh of `data/raw/`, `data/straininfo/`, or `curation/seed_scope.tsv`.

## Additional Notes

- Absence checks used `--no-ignore --hidden`, so ignored files were included.
- Reviewed row anchors:

| Artifact | Row or line |
|---|---|
| `data/taxa/PATHS.tsv` | 10342 |
| `curation/seed_scope.tsv` | 8797 |
| `data/raw/ncbitaxon_taxa.tsv` | 218680 |
| `data/raw/lpsn_names.tsv` | 27566 |
| `data/raw/bacdive_strains.tsv` | 24102-24104 |
| `data/taxa/bacteria/rubrobacter_bracarensis.yaml` | 1 and 319 |

- Future corrections belong in the upstream source extraction, `data/straininfo/`, `curation/seed_scope.tsv`, or the seeder, not in `data/taxa/bacteria/rubrobacter_bracarensis.yaml` directly.
