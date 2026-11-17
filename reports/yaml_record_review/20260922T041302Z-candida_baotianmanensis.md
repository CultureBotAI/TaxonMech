# YAML Record Review: Candida baotianmanensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/candida_baotianmanensis.yaml
- Started UTC: 2026-09-22T04:13:02Z
- Finished UTC: 2026-09-22T04:13:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1284353 |
| label | Candida baotianmanensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5475 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/candida_baotianmanensis.yaml`. It carries one NCBI exact synonym, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*candida_baotianmanensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/candida_baotianmanensis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/candida_baotianmanensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 300599 has `NCBITaxon:1284353`, label `Candida baotianmanensis`, rank `SPECIES`, direct parent `NCBITaxon:5475`, genetic code `12`, one exact synonym, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 58913 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent genus `Candida` under family `Debaryomycetaceae`.

The NCBI merged-ID side inventory maps old ID `NCBITaxon:871938` to `NCBITaxon:1284353`, but the retained retired-row inventory is empty for this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 300599 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58913 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 6602 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1284353`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0705018` for `Helenozyma baotianmanensis CBS 11898` at line 525464. |
| Native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported exactly by project `Gp0831038` for `Go0705018`. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no analysis row joins through the exact organism or project IDs for `NCBITaxon:1284353`. |
| NCBI merged-ID side inventory | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported exactly with old ID `NCBITaxon:871938` pointing at `NCBITaxon:1284353`. |
| Empty retained retired-row inventory | Exact retained retired-row scan | Supported; no retained retired row points at `NCBITaxon:1284353`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with four type-material rows for `Candida baotianmanensis`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1284353`. |
| Empty StrainInfo taxon surface | Exact native StrainInfo taxon scans plus generated overlay scans | Supported; no native direct/deposit hit or generated StrainInfo overlay row mentions `NCBITaxon:1284353`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1284353`. |

The committed aggregate GOLD row is mirrored by one exact native GOLD organism and one native project row. The local native GOLD analysis snapshot has no row joined through that exact project ID.

The NCBI merged-ID side inventory has one old ID, but the generated `replaces` list remains empty because retained retired-row evidence is empty.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `12`, the direct `Candida` genus parent, one exact synonym, three related synonyms, and four type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism and one project row, but no joined analysis row.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- The NCBI merged-ID side inventory has one old ID, but no retained retired row contributes a generated `replaces` value.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- Exact local native GOLD scans recovered one organism row, one project row, and zero analysis rows for `NCBITaxon:1284353`.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Candida baotianmanensis` as `SPECIES`, and the generated record follows the source rank exactly.
