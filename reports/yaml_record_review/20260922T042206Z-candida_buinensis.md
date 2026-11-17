# YAML Record Review: Yamadazyma buinensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/candida_buinensis.yaml
- Started UTC: 2026-09-22T04:22:06Z
- Finished UTC: 2026-09-22T04:22:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:45529 |
| label | Yamadazyma buinensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:766765 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/candida_buinensis.yaml`. It carries one NCBI exact synonym, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*candida_buinensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/candida_buinensis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/candida_buinensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 5592 has `NCBITaxon:45529`, label `Yamadazyma buinensis`, rank `SPECIES`, direct parent `NCBITaxon:766765`, genetic code `12`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52638 keeps this taxon in scope through the attested-source rule for `[Candida] buinensis`.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent genus `Yamadazyma` under family `Debaryomycetaceae`.

No committed NCBI merged-ID row or retained retired row points at `NCBITaxon:45529`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 5592 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52638 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 36038 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:45529`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0705208` for `Candida buinensis NRRL Y-11706` at line 525654. |
| Native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported exactly by project `Gp0831233` for `Go0705208`. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no analysis row joins through the exact organism or project IDs for `NCBITaxon:45529`. |
| Empty NCBI merged-ID inventories | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired rows | Supported; neither side old-ID inventory nor retained retired-row evidence points at `NCBITaxon:45529`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 14 type-material rows for `Yamadazyma buinensis` under the `Candida buinensis` name. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `45529`. |
| Native StrainInfo exact taxon evidence | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 11 deposit-taxonomy hits and one direct record under `45529`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:45529`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:45529`. |

The committed aggregate GOLD row is mirrored by one exact native GOLD organism and one native project row. The local native GOLD analysis snapshot has no row joined through that exact project ID.

Native StrainInfo has exact taxon rows under `45529`, but the generated StrainInfo overlay correctly remains empty because no BacDive-derived local strain inventory entry joins those rows.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `12`, the direct `Yamadazyma` genus parent, one exact synonym, two related synonyms, and 14 type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism and one project row, but no joined analysis row.
- Native StrainInfo has exact rows under this taxon, but no BacDive-derived local strain inventory entry turns them into generated `data/straininfo/` overlay rows.
- BacDive does not supply exact local strain evidence for this taxon.
- NCBI merged-ID, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The NCBI type-material count exceeded the bounded scan sample, so this review also used an exact `rg -n '^NCBITaxon:45529\t' data/raw/ncbi_type_material.tsv` scan to recover all 14 rows.
- Exact local native GOLD scans recovered one organism row, one project row, and zero analysis rows for `NCBITaxon:45529`.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- StrainInfo exact taxon rows do not generate overlay rows unless they join to the BacDive-derived local strain inventory.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Yamadazyma buinensis` as `SPECIES`, and the generated record follows the source rank exactly.
