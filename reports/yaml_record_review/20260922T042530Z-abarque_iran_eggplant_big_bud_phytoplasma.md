# YAML Record Review: Abarque(Iran) eggplant big bud phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/abarque_iran_eggplant_big_bud_phytoplasma.yaml
- Started UTC: 2026-09-22T04:24:51Z
- Finished UTC: 2026-09-22T04:25:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:358730 |
| label | Abarque(Iran) eggplant big bud phytoplasma |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:85621 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated bacterial species record at `data/taxa/bacteria/abarque_iran_eggplant_big_bud_phytoplasma.yaml`. It carries no synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated AllTheBacteria or StrainInfo overlay rows, no causal graphs, and one source attestation from NCBITAXON.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 471146 maps `NCBITaxon:358730` to slug `abarque_iran_eggplant_big_bud_phytoplasma`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; a `find reports/yaml_record_review -maxdepth 1 ... -name '*abarque_iran_eggplant_big_bud_phytoplasma.md' ... -print` probe returned no prior report. `find` includes ignored files, and this search was scoped to the report directory. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/abarque_iran_eggplant_big_bud_phytoplasma.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/abarque_iran_eggplant_big_bud_phytoplasma.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; the latest neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 74353 has `NCBITaxon:358730`, label `Abarque(Iran) eggplant big bud phytoplasma`, rank `SPECIES`, direct parent `NCBITaxon:85621`, genetic code `11`, no exact synonyms, no related synonyms, source `ncbitaxon`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:544448` Mycoplasmatota, `PHYLUM` | line 126468 |
| `NCBITaxon:31969` Mollicutes, `CLASS` | line 3369 |
| `NCBITaxon:186329` Acholeplasmatales, `ORDER` | line 36985 |
| `NCBITaxon:2146` Acholeplasmataceae, `FAMILY` | line 1689 |
| `NCBITaxon:33926` Candidatus Phytoplasma, `GENUS` | line 3660 |
| `NCBITaxon:85621` 16SrII (Peanut WB group), `SPECIES_GROUP` | line 13216 |

`curation/seed_scope.tsv` line 190598 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, source, empty synonym slots, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 74353 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 471146 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 190598 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| Empty NCBI type-material, LPSN, GTDB, BacDive-derived raw, MediaDive, GOLD, Madin et al., BactoTraits, ATB, and StrainInfo TSV surfaces | Exact gitignore-independent scans for `NCBITaxon:358730` across the auxiliary raw/source TSV families | Supported; no auxiliary TSV row names this NCBI taxon. |
| Empty StrainInfo generated overlay | Exact generated overlay TSV scans | Supported; no `data/straininfo/*.tsv` row names `NCBITaxon:358730`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the identity, direct parent, root-first bacterial lineage, genetic code `11`, and the sole source attestation.
- The committed seed scope includes the taxon through the attested-source rule.
- No exact auxiliary source row in the committed TSV inventories supplies NCBI type material, LPSN nomenclature, GTDB mappings, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:358730`.
- With `strain_count: 0`, no source-specific attestation beyond NCBITAXON, and no curator-added `causal_graphs`, the optional strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
