# YAML Record Review: Calonectria fujianensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/calonectria_fujianensis.yaml
- Started UTC: 2026-09-22T03:43:11Z
- Finished UTC: 2026-09-22T03:43:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1026983 |
| label | Calonectria fujianensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2779500 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/calonectria_fujianensis.yaml`. It carries one NCBI exact synonym, five NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*calonectria_fujianensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/calonectria_fujianensis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/calonectria_fujianensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 218771 has `NCBITaxon:1026983`, label `Calonectria fujianensis`, rank `SPECIES`, direct parent `NCBITaxon:2779500`, genetic code `1`, exact synonym `Calonectria nymphaeae`, five related synonyms, and source `gold`. `curation/seed_scope.tsv` line 57217 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Calonectria colhounii species complex` under genus `Calonectria`.

`data/raw/ncbi_merged_ids.tsv` lines 5465, 5466, and 49611 record side-inventory old IDs `NCBITaxon:1150968`, `NCBITaxon:1150969`, and `NCBITaxon:2728092` merged into `NCBITaxon:1026983`, but the retained NCBI row for this generated record is current and has no `retired_into` value. The record correctly omits `replaces`, which is generated only from retained retired rows.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 218771 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 57217 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 327 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1026983`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0677162` for `Calonectria fujianensis CMW 27257` at line 501793. |
| Native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported exactly by project `Gp0778971` for `Go0677162`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly by one analysis row joined through project `Gp0778971`. |
| NCBI merged-ID side inventory | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported exactly with old IDs `NCBITaxon:1150968`, `NCBITaxon:1150969`, and `NCBITaxon:2728092` pointing to the current taxon. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 13 type-material rows for the current name and exact synonym `Calonectria nymphaeae`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1026983`. |
| Empty StrainInfo taxon surface | Exact native StrainInfo taxon scans plus generated overlay scans | Supported; no native direct/deposit hit or generated StrainInfo overlay row mentions `NCBITaxon:1026983`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1026983`. |

The committed aggregate GOLD row is mirrored by one exact native GOLD organism, one native project row, and one analysis row joined through that project.

The NCBI type-material inventory contributes 11 rows for the current name `Calonectria fujianensis` and two holotype rows for the exact synonym `Calonectria nymphaeae`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Calonectria colhounii species complex` parent, one exact synonym, five related synonyms, and 13 type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, one project row, and one joined analysis row.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The NCBI type-material count exceeded the bounded scan sample, so this review also used an exact `rg -n '^NCBITaxon:1026983\t' data/raw/ncbi_type_material.tsv` scan to recover all 13 rows.
- The side-inventory NCBI merge rows for `NCBITaxon:1150968`, `NCBITaxon:1150969`, and `NCBITaxon:2728092` do not require YAML `replaces` entries without retained retired source rows.
- Exact local native GOLD scans recovered one organism row, one project row, and one analysis row for `NCBITaxon:1026983`.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Calonectria fujianensis` as `SPECIES`, and the generated record follows the source rank exactly.
