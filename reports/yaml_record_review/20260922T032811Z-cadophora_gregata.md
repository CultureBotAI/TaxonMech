# YAML Record Review: Cadophora gregata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cadophora_gregata.yaml
- Started UTC: 2026-09-22T03:28:11Z
- Finished UTC: 2026-09-22T03:28:11Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:51156 |
| label | Cadophora gregata |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:210567 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cadophora_gregata.yaml`. It carries two NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*cadophora_gregata.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cadophora_gregata.yaml` found no issues. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cadophora_gregata.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 6433 has `NCBITaxon:51156`, label `Cadophora gregata`, rank `SPECIES`, direct parent `NCBITaxon:210567`, genetic code `1`, exact synonyms `Cephalosporium gregatum` and `Phialophora gregata`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52826 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cadophora` under family `Ploettnerulaceae`.

No committed NCBI merged-ID row or retained retired row points at `NCBITaxon:51156`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 6433 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52826 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37510 | Supported exactly with three aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:51156`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly by `Go0618169`, `Go0618170`, and `Go0618171` for three `Phialophora gregata` strains. |
| Empty native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported; no native GOLD project joins to the three exact organism IDs for this taxon. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis joins to this taxon by exact organism ID or project ID. |
| Empty NCBI merged-ID inventories | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired rows | Supported; neither side old-ID inventory nor retained retired-row evidence points at `NCBITaxon:51156`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with eight type-material rows for `Cephalosporium gregatum`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `51156`. |
| Native StrainInfo exact taxon evidence | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 19 deposit-taxonomy hits and 15 direct records under `51156`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:51156`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:51156`. |

The committed aggregate GOLD row is mirrored by three exact native GOLD organisms named under the exact NCBI synonym `Phialophora gregata`; no native GOLD project or analysis row joins to those organisms.

The NCBI type-material inventory contributes eight rows for the exact synonym `Cephalosporium gregatum`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cadophora` parent, two exact synonyms, two related synonyms, and eight type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of three.
- The local native GOLD snapshot supplies three exact organisms, with no joined project or analysis rows.
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

- The NCBI type-material count exceeded the bounded scan sample, so this review also used an exact `rg -n '^NCBITaxon:51156\t' data/raw/ncbi_type_material.tsv` scan to recover all eight rows.
- Exact local native GOLD scans recovered three organism rows, no project rows, and no analysis rows for `NCBITaxon:51156`.
- StrainInfo exact taxon rows do not generate overlay rows unless they join to the BacDive-derived local strain inventory.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Cadophora gregata` as `SPECIES`, and the generated record follows the source rank exactly.
