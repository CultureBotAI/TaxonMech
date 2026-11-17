# YAML Record Review: 2,4-D-degrading bacterium 017

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/2_4_d_degrading_bacterium_017.yaml
- Started UTC: 2026-09-22T04:05:16Z
- Finished UTC: 2026-09-22T04:05:49Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:103500 |
| label | 2,4-D-degrading bacterium 017 |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:80841 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/2_4_d_degrading_bacterium_017.yaml`. It carries no synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated AllTheBacteria or StrainInfo overlay rows, no causal graphs, and one source attestation from NCBITAXON.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 14287 maps `NCBITaxon:103500` to slug `2_4_d_degrading_bacterium_017`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*2_4_d_degrading_bacterium_017.md' -print` returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/2_4_d_degrading_bacterium_017.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/2_4_d_degrading_bacterium_017.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; the latest neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 18483 has `NCBITaxon:103500`, label `2,4-D-degrading bacterium 017`, rank `SPECIES`, direct parent `NCBITaxon:80841`, genetic code `11`, no exact synonyms, no related synonyms, source `ncbitaxon`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:1224` Pseudomonadota, `PHYLUM` | line 945 |
| `NCBITaxon:28216` Betaproteobacteria, `CLASS` | line 2916 |
| `NCBITaxon:80840` Burkholderiales, `ORDER` | line 12115 |
| `NCBITaxon:80841` unclassified Burkholderiales, `NO_RANK` | line 12116 |

`curation/seed_scope.tsv` line 144129 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, source, empty synonym slots, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 18483 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 14287 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 144129 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| Empty LPSN, GTDB, BacDive-derived raw, MediaDive, GOLD, Madin et al., BactoTraits, ATB, and StrainInfo TSV surfaces | Exact gitignore-independent scans for `NCBITaxon:103500` across the auxiliary raw/source TSV families | Supported; no auxiliary TSV row names this NCBI taxon. |
| Empty StrainInfo generated overlay | Exact generated overlay TSV scans | Supported; no `data/straininfo/*.tsv` row names `NCBITaxon:103500`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identity, direct parent, root-first bacterial lineage, genetic code `11`, and the sole source attestation.
- The committed seed scope includes the taxon through the attested-source rule.
- No exact auxiliary source row in the committed TSV inventories supplies LPSN nomenclature, GTDB mappings, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:103500`.
- With `strain_count: 0`, no source-specific attestation beyond NCBITAXON, and no curator-added `causal_graphs`, the optional strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.

