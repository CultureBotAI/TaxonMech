# YAML Record Review: Buckleyzyma aurantiaca

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/buckleyzyma_aurantiaca.yaml
- Started UTC: 2026-09-22T03:19:26Z
- Finished UTC: 2026-09-22T03:19:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:91979 |
| label | Buckleyzyma aurantiaca |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:1798813 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/buckleyzyma_aurantiaca.yaml`. It carries two NCBI exact synonyms, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*buckleyzyma_aurantiaca.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/buckleyzyma_aurantiaca.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/buckleyzyma_aurantiaca.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 14874 has `NCBITaxon:91979`, label `Buckleyzyma aurantiaca`, rank `SPECIES`, direct parent `NCBITaxon:1798813`, genetic code `1`, two exact synonyms, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53531 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Buckleyzyma` under family `Buckleyzymaceae`.

No committed NCBI merged-ID row or retained retired row points at `NCBITaxon:91979`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 14874 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53531 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 44492 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:91979`. |
| Empty native GOLD organism evidence | Exact native GOLD organism scan | Supported; no native GOLD organism row currently carries NCBI taxon `91979`. |
| Empty native GOLD project evidence | Exact native GOLD project scan joined from exact organism IDs | Supported; with no exact organism IDs, no native GOLD project joins to this taxon. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis joins to this taxon by exact organism ID or project ID. |
| Empty NCBI merged-ID inventories | Exact scans of `data/raw/ncbi_merged_ids.tsv` and retained retired rows | Supported; neither side old-ID inventory nor retained retired-row evidence points at `NCBITaxon:91979`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with two culture-from-type-material rows and 16 type-material rows for `Rhodotorula aurantiaca`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `91979`. |
| Native StrainInfo exact taxon evidence | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 34 deposit-taxonomy hits and 11 direct records under `91979`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:91979`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:91979`. |

The committed aggregate GOLD row gives this yeast its second source attestation, but the local native GOLD organism/project/analysis snapshots do not contain an exact row for taxon ID `91979`.

The NCBI type-material inventory contributes 18 rows for the `Rhodotorula aurantiaca` synonym.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Buckleyzyma` parent, two exact synonyms, three related synonyms, and 18 type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies no exact organism, project, or analysis rows for this taxon.
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

- The NCBI type-material count exceeded the bounded scan sample, so this review also used an exact `rg -n '^NCBITaxon:91979\t' data/raw/ncbi_type_material.tsv` scan to recover all 18 rows.
- The GOLD aggregate row is present even though no exact local native GOLD row remains for `NCBITaxon:91979`; this review treats both committed surfaces separately.
- StrainInfo exact taxon rows do not generate overlay rows unless they join to the BacDive-derived local strain inventory.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Buckleyzyma aurantiaca` as `SPECIES`, and the generated record follows the source rank exactly.
