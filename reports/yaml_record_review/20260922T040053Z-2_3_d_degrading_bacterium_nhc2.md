# YAML Record Review: 2,3-D degrading bacterium NHC2

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/2_3_d_degrading_bacterium_nhc2.yaml
- Started UTC: 2026-09-22T03:59:38Z
- Finished UTC: 2026-09-22T04:00:53Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:119160 |
| label | 2,3-D degrading bacterium NHC2 |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:90141 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/2_3_d_degrading_bacterium_nhc2.yaml`. It carries no synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated AllTheBacteria or StrainInfo overlay rows, no causal graphs, and one source attestation from NCBITAXON.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 63106 maps `NCBITaxon:119160` to slug `2_3_d_degrading_bacterium_nhc2`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*2_3_d_degrading_bacterium_nhc2.md' -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/2_3_d_degrading_bacterium_nhc2.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/2_3_d_degrading_bacterium_nhc2.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; the latest neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 22335 has `NCBITaxon:119160`, label `2,3-D degrading bacterium NHC2`, rank `SPECIES`, direct parent `NCBITaxon:90141`, genetic code `11`, no exact synonyms, no related synonyms, source `ncbitaxon`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:1224` Pseudomonadota, `PHYLUM` | line 945 |
| `NCBITaxon:28211` Alphaproteobacteria, `CLASS` | line 2912 |
| `NCBITaxon:356` Hyphomicrobiales, `ORDER` | line 274 |
| `NCBITaxon:82115` Rhizobiaceae, `FAMILY` | line 12340 |
| `NCBITaxon:90141` unclassified Rhizobiaceae, `NO_RANK` | line 14480 |

`curation/seed_scope.tsv` line 147257 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, source, empty synonym slots, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 22335 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 63106 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 147257 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| Empty LPSN, GTDB, BacDive-derived raw, MediaDive, GOLD, Madin et al., BactoTraits, ATB, and StrainInfo TSV surfaces | Exact gitignore-independent scans for `NCBITaxon:119160` across the auxiliary raw/source TSV families | Supported; no auxiliary TSV row names this NCBI taxon. |
| Empty StrainInfo generated overlay | Exact generated overlay TSV scans | Supported; no `data/straininfo/*.tsv` row names `NCBITaxon:119160`. |

One broad exploratory search for bare `119160` recovered unrelated native BacDive and StrainInfo integer identifiers; those were false positives because they were not `NCBITaxon:119160`. The verdict above uses only exact CURIE and full-label checks.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identity, direct parent, root-first bacterial lineage, genetic code `11`, and the sole source attestation.
- The committed seed scope includes the taxon through the attested-source rule.
- No exact auxiliary source row in the committed TSV inventories supplies LPSN nomenclature, GTDB mappings, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:119160`.
- With `strain_count: 0`, no source-specific attestation beyond NCBITAXON, and no curator-added `causal_graphs`, the optional strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- `data/taxa/PATHS.tsv` has 625,960 record rows, and 856 unique report stems existed before this report was written; after this pass, 625,103 records still need an individual `review-yaml-record` report.
- An external NCBI Taxonomy Browser/E-utilities fetch for `NCBITaxon:119160` was attempted but returned no usable page through the available web fetcher. The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
