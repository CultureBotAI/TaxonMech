# YAML Record Review: 2,4-D-degrading bacterium 524

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/2_4_d_degrading_bacterium_524.yaml
- Started UTC: 2026-09-22T04:13:27Z
- Finished UTC: 2026-09-22T04:14:07Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:103496 |
| label | 2,4-D-degrading bacterium 524 |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:122612 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/2_4_d_degrading_bacterium_524.yaml`. It carries no synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated AllTheBacteria or StrainInfo overlay rows, no causal graphs, and one source attestation from NCBITAXON.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 14242 maps `NCBITaxon:103496` to slug `2_4_d_degrading_bacterium_524`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*2_4_d_degrading_bacterium_524.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/2_4_d_degrading_bacterium_524.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/2_4_d_degrading_bacterium_524.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; the latest neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 18479 has `NCBITaxon:103496`, label `2,4-D-degrading bacterium 524`, rank `SPECIES`, direct parent `NCBITaxon:122612`, genetic code `11`, no exact synonyms, no related synonyms, source `ncbitaxon`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:1224` Pseudomonadota, `PHYLUM` | line 945 |
| `NCBITaxon:28211` Alphaproteobacteria, `CLASS` | line 2912 |
| `NCBITaxon:204457` Sphingomonadales, `ORDER` | line 40379 |
| `NCBITaxon:41297` Sphingomonadaceae, `FAMILY` | line 4800 |
| `NCBITaxon:122612` unclassified Sphingomonadaceae, `NO_RANK` | line 23177 |

`curation/seed_scope.tsv` line 144125 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, source, empty synonym slots, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 18479 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 14242 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 144125 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| Empty LPSN, GTDB, BacDive-derived raw, MediaDive, GOLD, Madin et al., BactoTraits, ATB, and StrainInfo TSV surfaces | Exact gitignore-independent scans for `NCBITaxon:103496` and `2,4-D-degrading bacterium 524` across the auxiliary raw/source TSV families | Supported; no auxiliary TSV row names this NCBI taxon. |
| Empty StrainInfo generated overlay | Exact generated overlay TSV scans | Supported; no `data/straininfo/*.tsv` row names `NCBITaxon:103496`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identity, direct parent, root-first bacterial lineage, genetic code `11`, and the sole source attestation.
- The committed seed scope includes the taxon through the attested-source rule.
- No exact auxiliary source row in the committed TSV inventories supplies LPSN nomenclature, GTDB mappings, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:103496`.
- With `strain_count: 0`, no source-specific attestation beyond NCBITAXON, and no curator-added `causal_graphs`, the optional strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
