# YAML Record Review: Acaryochloridopsis arrabidensis LEGE 18583

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acaryochloridopsis_arrabidensis_lege_18583.yaml
- Started UTC: 2026-09-22T06:50:03Z
- Finished UTC: 2026-09-22T06:50:55Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:3133075 |
| label | Acaryochloridopsis arrabidensis LEGE 18583 |
| rank | STRAIN |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:3366351 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a compact generated bacterial strain record at `data/taxa/bacteria/acaryochloridopsis_arrabidensis_lege_18583.yaml`. It is seeded from NCBITaxon only, carries one NCBI exact synonym, no GTDB mappings, no xrefs, no LPSN nomenclature, no generated local strain entries, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 427281 maps `NCBITaxon:3133075` to slug `acaryochloridopsis_arrabidensis_lege_18583`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -type f -name "*acaryochloridopsis_arrabidensis_lege_18583.md" -print` returned no prior report. `find` includes ignored files, and the probe was scoped to `reports/yaml_record_review/`. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acaryochloridopsis_arrabidensis_lege_18583.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acaryochloridopsis_arrabidensis.yaml data/taxa/bacteria/acaryochloridopsis_arrabidensis_lege_12582.yaml data/taxa/bacteria/acaryochloridopsis_arrabidensis_lege_16640.yaml data/taxa/bacteria/acaryochloridopsis_arrabidensis_lege_18583.yaml` scanned this file with zero ERROR rows in a four-file batch and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 605002 has `NCBITaxon:3133075`, label `Acaryochloridopsis arrabidensis LEGE 18583`, rank `STRAIN`, direct parent `NCBITaxon:3366351`, genetic code `11`, exact synonym `Acaryochloridales cyanobacterium LEGE 18583`, source set `ncbitaxon`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:1783272` Bacillati, `KINGDOM` | line 464835 |
| `NCBITaxon:1798711` Cyanobacteriota/Melainabacteria group, `CLADE` | line 469139 |
| `NCBITaxon:1117` Cyanobacteriota, `PHYLUM` | line 870 |
| `NCBITaxon:3028117` Cyanophyceae, `CLASS` | line 587019 |
| `NCBITaxon:3079744` Acaryochloridales, `ORDER` | line 595536 |
| `NCBITaxon:2881378` Thermosynechococcaceae, `FAMILY` | line 567237 |
| `NCBITaxon:3366350` Acaryochloridopsis, `GENUS` | line 621106 |
| `NCBITaxon:3366351` Acaryochloridopsis arrabidensis, `SPECIES` | line 621107 |

`curation/seed_scope.tsv` line 596474 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, exact synonym, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 605002 | Supported exactly. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 427281 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 596474 | Supported exactly by a single seed-scope row. |
| Empty GTDB, NCBI type-material, LPSN, MediaDive, GOLD, Madin et al., BactoTraits, BacDive-derived strain, ATB, and StrainInfo surfaces | Exact gitignore-independent scans for `NCBITaxon:3133075` across `data/raw/`, `data/atb/`, and `data/straininfo/` TSV inventories | Supported; no same-taxon auxiliary row names this NCBI taxon outside `data/raw/ncbitaxon_taxa.tsv`. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the strain identity, direct Acaryochloridopsis arrabidensis parent, root-first bacterial lineage, genetic code `11`, one exact synonym, and the NCBITAXON source attestation.
- The committed seed scope includes the taxon through the attested-source rule with one source including NCBI.
- No exact same-taxon auxiliary source row in the committed TSV inventories supplies GTDB mappings, NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:3133075`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` row is the pinned primary NCBI dump snapshot that seeded the record.
