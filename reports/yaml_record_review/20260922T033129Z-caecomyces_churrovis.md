# YAML Record Review: Caecomyces churrovis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/caecomyces_churrovis.yaml
- Started UTC: 2026-09-22T03:31:29Z
- Finished UTC: 2026-09-22T03:31:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2019372 |
| label | Caecomyces churrovis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:4823 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/caecomyces_churrovis.yaml`. It carries two NCBI related synonyms, no exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*caecomyces_churrovis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/caecomyces_churrovis.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/caecomyces_churrovis.yaml` exited successfully and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 511077 has `NCBITaxon:2019372`, label `Caecomyces churrovis`, rank `SPECIES`, direct parent `NCBITaxon:4823`, genetic code `1`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61944 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Caecomyces` under family `Neocallimastigaceae`.

No committed NCBI merged-ID row or retained retired row points at `NCBITaxon:2019372`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 511077 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61944 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 18798 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2019372`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0125801` for `Caecomyces churrovis A` at line 74725. |
| Native GOLD project evidence | Complete exact native GOLD project scan joined from exact organism IDs | Supported exactly by 26 project rows for `Go0125801`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly by one analysis row joined through project `Gp0134099`. |
| Empty NCBI merged-ID inventories | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired rows | Supported; neither side old-ID inventory nor retained retired-row evidence points at `NCBITaxon:2019372`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with one holotype row, `JMRC SF012539`, for `Caecomyces churrovis`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2019372`. |
| Empty StrainInfo taxon surface | Exact native StrainInfo taxon scans plus generated overlay scans | Supported; no native direct/deposit hit or generated StrainInfo overlay row mentions `NCBITaxon:2019372`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2019372`. |

The committed aggregate GOLD row is mirrored by an exact native GOLD organism, 26 native project rows for that organism, and one analysis row joined through project `Gp0134099`.

The NCBI type-material inventory contributes one holotype row for `Caecomyces churrovis`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Caecomyces` parent, two related synonyms, and one holotype row.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, 26 project rows, and one joined analysis row.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- NCBI merged-ID, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The native GOLD project count exceeded the bounded scan sample, so this review also scanned `data/gold/projects.jsonl.gz` exactly for `Go0125801` to recover all 26 rows.
- Exact local native GOLD scans recovered one organism row, 26 project rows, and one analysis row for `NCBITaxon:2019372`.
- GOLD analysis evidence joins through `AP PROJECT GOLD IDS`, not `AP ORGANISM GOLD ID`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Caecomyces churrovis` as `SPECIES`, and the generated record follows the source rank exactly.
