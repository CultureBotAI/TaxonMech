# YAML Record Review: Abiotrophia para-adiacens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abiotrophia_para_adiacens.yaml
- Started UTC: 2026-09-22T04:33:40Z
- Finished UTC: 2026-09-22T04:35:13Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:191553 |
| label | Abiotrophia para-adiacens |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:46123 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a compact generated bacterial species record at `data/taxa/bacteria/abiotrophia_para_adiacens.yaml`. It carries one NCBI related synonym, no GTDB mappings, no xrefs, no LPSN nomenclature, no generated local strain entries, no causal graphs, and source attestations from NCBITAXON and MADIN.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 302132 maps `NCBITaxon:191553` to slug `abiotrophia_para_adiacens`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abiotrophia_para_adiacens.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abiotrophia_para_adiacens.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abiotrophia_para_adiacens.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 38005 has `NCBITaxon:191553`, label `Abiotrophia para-adiacens`, rank `SPECIES`, direct parent `NCBITaxon:46123`, genetic code `11`, related synonym `"Abiotrophia para-adiacens" Kanamoto et al. 2000`, source set `ncbitaxon|madin_etal`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:1239` Bacillota, `PHYLUM` | line 955 |
| `NCBITaxon:91061` Bacilli, `CLASS` | line 14761 |
| `NCBITaxon:186826` Lactobacillales, `ORDER` | line 37043 |
| `NCBITaxon:186827` Aerococcaceae, `FAMILY` | line 37044 |
| `NCBITaxon:46123` Abiotrophia, `GENUS` | line 5771 |

`data/raw/madin_taxa.tsv` line 18854 supplies the one direct Madin et al. trait assertion, and `curation/seed_scope.tsv` line 54409 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, related synonym, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 38005 | Supported exactly. |
| Madin source attestation | `data/raw/madin_taxa.tsv` line 18854 | Supported exactly with one direct trait assertion. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 302132 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 54409 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct genus parent, root-first bacterial lineage, genetic code `11`, the only synonym, and the NCBITAXON source attestation.
- Madin et al. supplies the one directly filed trait assertion represented in `source_attestations`.
- No same-taxon auxiliary source row in the checked source TSVs supplies GTDB mappings, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:191553`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
