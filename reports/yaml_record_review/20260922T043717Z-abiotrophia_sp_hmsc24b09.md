# YAML Record Review: Abiotrophia sp. HMSC24B09

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abiotrophia_sp_hmsc24b09.yaml
- Started UTC: 2026-09-22T04:35:30Z
- Finished UTC: 2026-09-22T04:37:17Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1581061 |
| label | Abiotrophia sp. HMSC24B09 |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2608917 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a compact generated bacterial species record at `data/taxa/bacteria/abiotrophia_sp_hmsc24b09.yaml`. It carries a 21-genome GTDB `skos:closeMatch`, a GTDB-derived exact synonym and xref, no LPSN nomenclature, no generated local strain entries, no causal graphs, and source attestations from NCBITAXON and GTDB.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 212420 maps `NCBITaxon:1581061` to slug `abiotrophia_sp_hmsc24b09`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*-abiotrophia_sp_hmsc24b09.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abiotrophia_sp_hmsc24b09.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abiotrophia_sp_hmsc24b09.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 407606 has `NCBITaxon:1581061`, label `Abiotrophia sp. HMSC24B09`, rank `SPECIES`, direct parent `NCBITaxon:2608917`, genetic code `11`, empty NCBI synonym slots, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

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
| `NCBITaxon:2608917` unclassified Abiotrophia, `NO_RANK` | line 536727 |

`data/raw/gtdb_mappings.tsv` line 38371 maps `GTDB:s__Abiotrophia_sp001815865` to `NCBITaxon:1581061` with `skos:closeMatch`; `data/raw/gtdb_species.tsv` line 2809 records the GTDB species with 21 genomes. `curation/seed_scope.tsv` line 74173 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, empty synonym slots, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 407606 | Supported exactly. |
| One GTDB close mapping | `data/raw/gtdb_mappings.tsv` line 38371 and `data/raw/gtdb_species.tsv` line 2809 | Supported exactly with a 21-genome GTDB species. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 212420 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 74173 | Supported exactly by a single seed-scope row. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct unclassified parent, root-first bacterial lineage, genetic code `11`, and the NCBITAXON source attestation.
- GTDB supplies `s__Abiotrophia_sp001815865` as a close match and therefore the generated xref and exact synonym `Abiotrophia sp001815865`.
- The same GTDB species is deliberately broad for other NCBI taxa; this record only carries the close NCBITaxon-to-GTDB mapping filed for `NCBITaxon:1581061`.
- No same-taxon auxiliary source row in the checked source TSVs supplies LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:1581061`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
