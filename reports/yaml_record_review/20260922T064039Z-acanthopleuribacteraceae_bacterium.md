# YAML Record Review: Acanthopleuribacteraceae bacterium

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acanthopleuribacteraceae_bacterium.yaml
- Started UTC: 2026-09-22T06:38:22Z
- Finished UTC: 2026-09-22T06:40:39Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2696471 |
| label | Acanthopleuribacteraceae bacterium |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2696470 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a compact generated bacterial species record at `data/taxa/bacteria/acanthopleuribacteraceae_bacterium.yaml`. It is seeded from NCBITaxon and GTDB, carries one GTDB close species mapping, one GTDB exact synonym, one GTDB xref, no LPSN nomenclature, no generated local strain entries, and no causal graphs.

## Validation

| Check | Result |
|---|---|
| Target resolution | Pass; `data/taxa/PATHS.tsv` line 364301 maps `NCBITaxon:2696471` to slug `acanthopleuribacteraceae_bacterium`, and the target file exists under `data/taxa/bacteria/`. |
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -type f -name "????????T??????Z-acanthopleuribacteraceae_bacterium.md" -print` returned no prior report. `find` includes ignored files, and the probe was scoped to `reports/yaml_record_review/`. |
| Open LinkML validation | Pass; `just validate data/taxa/bacteria/acanthopleuribacteraceae_bacterium.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/bacteria/acalypha_indica_phytoplasma.yaml data/taxa/bacteria/acanthopleuribacter_pedis.yaml data/taxa/bacteria/acanthopleuribacter_sp.yaml data/taxa/bacteria/acanthopleuribacteraceae_bacterium.yaml` scanned this file with zero ERROR rows in a four-file batch and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and this read-only report does not write a `history/` event. |
| Corpus reproduction | Not rerun for this compact generated record; a neighboring YAML review report had already recorded that `just verify-corpus` reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 544620 has `NCBITaxon:2696471`, label `Acanthopleuribacteraceae bacterium`, rank `SPECIES`, direct parent `NCBITaxon:2696470`, genetic code `11`, empty NCBI synonym slots, source set `ncbitaxon|gtdb`, and snapshot date `2026-09-13`.

The YAML lineage matches the pinned NCBI inventory parent chain exactly:

| YAML ancestor | Raw NCBI row |
|---|---|
| `NCBITaxon:1` root, `NO_RANK` | `data/raw/ncbitaxon_taxa.tsv` line 2 |
| `NCBITaxon:131567` cellular organisms, `CELLULAR_ROOT` | line 25334 |
| `NCBITaxon:2` Bacteria, `DOMAIN` | line 3 |
| `NCBITaxon:3379134` Pseudomonadati, `KINGDOM` | line 622851 |
| `NCBITaxon:57723` Acidobacteriota, `PHYLUM` | line 7341 |
| `NCBITaxon:533205` Holophagae, `CLASS` | line 122075 |
| `NCBITaxon:533206` Acanthopleuribacterales, `ORDER` | line 122076 |
| `NCBITaxon:533207` Acanthopleuribacteraceae, `FAMILY` | line 122077 |
| `NCBITaxon:2696470` unclassified Acanthopleuribacteraceae, `NO_RANK` | line 544619 |

`data/raw/gtdb_mappings.tsv` line 208200 maps `GTDB:s__JBGTRP01_sp041940685` to this NCBI species with `skos:closeMatch` and `genome_count` 1; `data/raw/gtdb_species.tsv` line 105632 carries the same native GTDB species and count. `curation/seed_scope.tsv` line 99201 keeps this taxon in scope through the attested-source rule.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, empty synonym slots, source set, and snapshot date | `data/raw/ncbitaxon_taxa.tsv` line 544620 | Supported exactly. |
| GTDB taxonomy mapping, `JBGTRP01 sp041940685` exact synonym, and `GTDB:s__JBGTRP01_sp041940685` xref | `data/raw/gtdb_mappings.tsv` line 208200 and `data/raw/gtdb_species.tsv` line 105632 | Supported exactly with `skos:closeMatch` and one GTDB genome. |
| Filesystem slug | `data/taxa/PATHS.tsv` line 364301 | Supported exactly. |
| Scope rationale and seeded history text | `curation/seed_scope.tsv` line 99201 | Supported exactly by a single seed-scope row. |
| Empty NCBI type-material, LPSN, MediaDive, GOLD, Madin et al., BactoTraits, BacDive-derived strain, ATB, and StrainInfo surfaces | Exact gitignore-independent scans for `NCBITaxon:2696471` across `data/raw/`, `data/atb/`, and `data/straininfo/` TSV inventories | Supported; no same-taxon auxiliary row names this NCBI taxon outside the NCBI and GTDB raw tables. |
| Empty retired-ID surface | Exact gitignore-independent scans of `data/raw/ncbi_merged_ids.tsv` and `data/raw/dropped.tsv` for `NCBITaxon:2696471` | Supported; no committed merged-ID or dropped-row evidence points at this taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the species identity, direct unclassified Acanthopleuribacteraceae parent, root-first bacterial lineage, genetic code `11`, and the NCBITAXON source attestation.
- GTDB supplies the one-genome `JBGTRP01_sp041940685` species mapping, exact synonym, xref, and GTDB source attestation.
- The committed seed scope includes the taxon through the attested-source rule with two sources including NCBI.
- No exact same-taxon auxiliary source row in the committed TSV inventories supplies NCBI type material, LPSN nomenclature, BacDive-derived strains, MediaDive counts, GOLD organisms, Madin et al. counts, BactoTraits counts, ATB overlap, or StrainInfo overlay assertions for `NCBITaxon:2696471`.
- With no same-taxon BacDive-derived or overlay strain rows and no curator-added `causal_graphs`, the optional local strain, genome, related-record, evidence, definition, and causal-graph sections are correctly empty.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

The local `data/raw/ncbitaxon_taxa.tsv` and GTDB rows are the committed source snapshots that seeded the record.
