# YAML Record Review: Acetobacteraceae bacterium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacteraceae_bacterium.yaml
- Reviewed UTC: 2026-09-26T12:14:31Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | TaxonRecord |
| Identifier | NCBITaxon:1909293 |
| Label | Acetobacteraceae bacterium |
| Rank / domain | SPECIES / BACTERIA |
| Parent | NCBITaxon:41293, unclassified Acetobacteraceae |
| PATHS row | data/taxa/PATHS.tsv:301149 |
| Record status | Generated YAML; seeded from maintained inventories and curation/seed_scope.tsv |
| Scope row | curation/seed_scope.tsv:61570 |

## Validation

| Check | Result |
| --- | --- |
| Duplicate report preflight | Pass; ignored-file `find` over `reports/yaml_record_review` found no existing `*-acetobacteraceae_bacterium.md` report |
| `just validate data/taxa/bacteria/acetobacteraceae_bacterium.yaml` | Pass; no issues found |
| `just validate-strict data/taxa/bacteria/acetobacteraceae_bacterium.yaml data/taxa/bacteria/acetobacteraceae_bacterium_184_22.yaml data/taxa/bacteria/acetobacteraceae_bacterium_3279o2.yaml data/taxa/bacteria/acetobacteraceae_bacterium_3292o2.yaml` | Pass; 4 files scanned, 0 files with ERROR, 0 total ERROR rows |
| YAML summary helper | Pass; 1471 lines, 9 lineage entries, 201 GTDB mappings, 0 synonyms, 0 xrefs, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records |
| Bounded source scan | Pass; exact NCBI, seed-scope, GTDB, GOLD, native GOLD, and BacDive genome-side rows checked with no lineage mismatches |
| Exact ignored-aware source scan | Pass; `rg --no-ignore --hidden` covered curation, raw, BacDive, StrainInfo, AllTheBacteria, and history paths and found the expected exact rows for this target |

## Identity and Grounding

- `NCBITaxon:1909293`, label `Acetobacteraceae bacterium`, rank `SPECIES`, parent `NCBITaxon:41293`, genetic code `11`, and snapshot `2026-09-13` match `data/raw/ncbitaxon_taxa.tsv:493237`.
- `grounding_status: EXACT` is appropriate because the record identifier is the exact NCBI taxon ID used as the source identity.
- `mapping_status: SEEDED` is consistent with `curation/seed_scope.tsv:61570`.
- The bounded NCBI scan resolved all 9 root-first lineage entries and found no missing ancestors or label, rank, or parent mismatches.

## Evidence

- `data/raw/gtdb_mappings.tsv:89023` through `data/raw/gtdb_mappings.tsv:89223` contain exactly 201 `skos:broadMatch` rows for `NCBITaxon:1909293`, matching the YAML mapping list. The genome counts across those broad matches sum to 389, and all 201 are correctly retained as pooled non-equivalence mappings.
- The primary GTDB source attestation names `GTDB:s__Roseomonas_mucosa`; `data/raw/gtdb_mappings.tsv:89220` supports its `genome_count: 29`.
- `data/raw/gold_organisms.tsv:17340` supports the direct `GOLD` / `ORGANISM` source attestation count of 10.
- Native GOLD has 10 exact organisms, 10 projects, and 6 analyses for `NCBITaxon:1909293`; those source-side project and analysis rows are not strain-genome links without a represented strain.
- The two BacDive-derived genome crosswalk rows with `NCBITaxon:1909293` belong to `kgmicrobe.strain:bacdive_164609`, but `data/raw/bacdive_strains.tsv:86845` classifies that BacDive strain as `NCBITaxon:1484109`, so those rows do not require a strain entry on this record.

## Completeness

- The generated NCBI identity, 201 pooled GTDB broad matches, NCBI, GTDB, and GOLD source attestations, and absence of xrefs are complete for the pinned local source rows.
- `strain_count: 0` is complete for this NCBI taxon: there is no exact compact BacDive strain row, no exact culture-collection row, no final StrainInfo overlay, and no strain classified here even though BacDive 164609 has two genome-side rows whose assembly metadata mention `NCBITaxon:1909293`.
- The exact ignored-aware source scans found no LPSN nomenclature, NCBI synonym, BactoTraits row, Madin et al. row, MediaDive row, NCBI merged-ID row, NCBI type-material row, generated definition, or curator-added causal graph for this identifier.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record. Future changes should rerun the same exact source checks plus open and strict validation after any NCBI, GTDB, GOLD, BacDive, or StrainInfo refresh.

## Additional Notes

- `GTDB:s__Roseomonas_mucosa` has the largest broad-match genome count and is therefore the source used in the record-level GTDB attestation; the other 200 GTDB mappings are retained without promoting them to xrefs or synonyms.
- The generated YAML was left read-only; any future correction would belong in a maintained source inventory, seeder logic, or `curation/seed_scope.tsv`.
