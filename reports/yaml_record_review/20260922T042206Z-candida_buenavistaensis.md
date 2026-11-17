# YAML Record Review: Candida buenavistaensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/candida_buenavistaensis.yaml
- Started UTC: 2026-09-22T04:22:06Z
- Finished UTC: 2026-09-22T04:22:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:434039 |
| label | Candida buenavistaensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5475 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/candida_buenavistaensis.yaml`. It carries no NCBI exact synonyms, four NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*candida_buenavistaensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/candida_buenavistaensis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/candida_buenavistaensis.yaml` exited successfully and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 95735 has `NCBITaxon:434039`, label `Candida buenavistaensis`, rank `SPECIES`, direct parent `NCBITaxon:5475`, genetic code `12`, four related synonyms, and source `gold`. `curation/seed_scope.tsv` line 55639 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent genus `Candida` under family `Debaryomycetaceae`.

The NCBI merged-ID side inventory maps old ID `NCBITaxon:234511` to `NCBITaxon:434039`, but the retained retired-row inventory is empty for this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 95735 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55639 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 35381 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:434039`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0705487` for `Candida buenavistaensis NRRL Y-27734` at line 525933. |
| Native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported exactly by project `Gp0831530` for `Go0705487`. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no analysis row joins through the exact organism or project IDs for `NCBITaxon:434039`. |
| NCBI merged-ID side inventory | Exact scan of `data/raw/ncbi_merged_ids.tsv` | Supported exactly with old ID `NCBITaxon:234511` pointing at `NCBITaxon:434039`. |
| Empty retained retired-row inventory | Exact retained retired-row scan | Supported; no retained retired row points at `NCBITaxon:434039`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with six type-material rows for `Candida buenavistaensis`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `434039`. |
| Empty StrainInfo taxon surface | Exact native StrainInfo taxon scans plus generated overlay scans | Supported; no native direct/deposit hit or generated StrainInfo overlay row mentions `NCBITaxon:434039`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:434039`. |

The committed aggregate GOLD row is mirrored by one exact native GOLD organism and one native project row. The local native GOLD analysis snapshot has no row joined through that exact project ID.

The NCBI merged-ID side inventory has one old ID, but the generated `replaces` list remains empty because retained retired-row evidence is empty.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `12`, the direct `Candida` genus parent, four related synonyms, and six type-material rows.
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

- The NCBI type-material count exceeded the bounded scan sample, so this review also used an exact `rg -n '^NCBITaxon:434039\t' data/raw/ncbi_type_material.tsv` scan to recover all six rows.
- Exact local native GOLD scans recovered one organism row, one project row, and zero analysis rows for `NCBITaxon:434039`.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Candida buenavistaensis` as `SPECIES`, and the generated record follows the source rank exactly.
