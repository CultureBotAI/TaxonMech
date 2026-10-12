# YAML Record Review: Abyssicoccaceae bacterium KTH-63

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abyssicoccaceae_bacterium_kth_63.yaml
- Started UTC: 2026-09-22T06:25:30Z
- Finished UTC: 2026-09-22T06:27:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:3417167 |
| label | Abyssicoccaceae bacterium KTH-63 |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:3106228 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a compact generated bacterial species record at `data/taxa/bacteria/abyssicoccaceae_bacterium_kth_63.yaml`. It is seeded from NCBITaxon only, carries one NCBI exact synonym, and has no GTDB mappings, xrefs, LPSN nomenclature, generated local strain entries, or causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 458199 maps `NCBITaxon:3417167` to slug `abyssicoccaceae_bacterium_kth_63`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abyssicoccaceae_bacterium_kth_63.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abyssicoccaceae_bacterium_kth_63.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abyssicoccaceae_bacterium_kth_63.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 630279 has `NCBITaxon:3417167`, label `Abyssicoccaceae bacterium KTH-63`, rank `SPECIES`, direct parent `NCBITaxon:3106228`, genetic code `11`, exact synonym `Staphylococcaceae bacterium KTH-63`, source set `ncbitaxon`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:1239` Bacillota, `PHYLUM` | line 955 |
| `NCBITaxon:91061` Bacilli, `CLASS` | line 14761 |
| `NCBITaxon:1385` Caryophanales, `ORDER` | line 1076 |
| `NCBITaxon:3076164` Abyssicoccaceae, `FAMILY` | line 594994 |
| `NCBITaxon:3106228` unclassified Abyssicoccaceae, `NO_RANK` | line 599031 |

`curation/seed_scope.tsv` line 608546 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, exact synonym, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 630279 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 458199 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 608546 | Supported exactly by a single seed-scope row. |
| Empty GTDB, NCBI type-material, LPSN, MediaDive, GOLD, Madin et al., BactoTraits, BacDive-derived strain, ATB, and StrainInfo surfaces | Exact gitignore-independent scans for `NCBITaxon:3417167` across the auxiliary raw/source TSV families | Supported; no same-taxon auxiliary row names this NCBI taxon outside NCBI. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct unclassified Abyssicoccaceae parent, root-first bacterial lineage, genetic code `11`, one exact synonym, and the NCBITAXON source attestation.
- The committed seed scope includes the taxon through the attested-source rule with one source including NCBI.
- No exact same-taxon auxiliary source row in the committed TSV inventories supplies GTDB mappings, NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:3417167`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
