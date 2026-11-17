# YAML Record Review: Butyriboletus roseoflavus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/butyriboletus_roseoflavus.yaml
- Started UTC: 2026-09-22T03:24:12Z
- Finished UTC: 2026-09-22T03:24:12Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1325616 |
| label | Butyriboletus roseoflavus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:1524449 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/butyriboletus_roseoflavus.yaml`. It carries one NCBI exact synonym, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*butyriboletus_roseoflavus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/butyriboletus_roseoflavus.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/butyriboletus_roseoflavus.yaml` exited successfully and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 316253 has `NCBITaxon:1325616`, label `Butyriboletus roseoflavus`, rank `SPECIES`, direct parent `NCBITaxon:1524449`, genetic code `1`, exact synonym `Boletus roseoflavus`, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 59475 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Butyriboletus` under subfamily `Boletoideae`.

`data/raw/ncbi_merged_ids.tsv` line 11237 records side-inventory old ID `NCBITaxon:1297047` merged into `NCBITaxon:1325616`, but the retained NCBI row for this generated record is current and has no `retired_into` value. The record correctly omits `replaces`, which is generated only from retained retired rows.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 316253 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 59475 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 7933 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1325616`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0518050` for `Butyriboletus roseoflavus MG29` and `Go0631681` for `Butyriboletus roseoflavus LA02`. |
| Native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported exactly by projects `Gp0442119` and `Gp0645229`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly by two analysis rows joined through projects `Gp0645229` and `Gp0442119`. |
| NCBI merged-ID side inventory | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported exactly with old ID `NCBITaxon:1297047` pointing to the current taxon. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with one type-material row, `Baqy1`, for `Butyriboletus roseoflavus`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1325616`. |
| Empty StrainInfo taxon surface | Exact native StrainInfo taxon scans plus generated overlay scans | Supported; no native direct/deposit hit or generated StrainInfo overlay row mentions `NCBITaxon:1325616`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1325616`. |

The committed aggregate GOLD row is mirrored by two exact native GOLD organism rows, two native project rows, and two analysis rows joined through those projects.

The NCBI type-material inventory contributes one row for `Butyriboletus roseoflavus`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Butyriboletus` parent, one exact synonym, three related synonyms, and one type-material row.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies two exact organisms, two project rows, and two joined analysis rows.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The side-inventory NCBI merge row for `NCBITaxon:1297047` does not require a YAML `replaces` entry without a retained retired source row.
- Exact local native GOLD scans recovered two organism rows, two project rows, and two analysis rows for `NCBITaxon:1325616`.
- GOLD analysis rows for both `MG29` and `LA02` join through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Butyriboletus roseoflavus` as `SPECIES`, and the generated record follows the source rank exactly.
