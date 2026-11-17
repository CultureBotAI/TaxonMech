# YAML Record Review: Baffinella frigidus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/baffinella_frigidus.yaml
- Started UTC: 2026-09-21T23:42:28Z
- Finished UTC: 2026-09-21T23:43:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2571260 |
| label | Baffinella frigidus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2571259 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic cryptophyte species at `data/taxa/eukaryota/baffinella_frigidus.yaml`. It carries four related NCBI synonyms, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*baffinella_frigidus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/baffinella_frigidus.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/baffinella_frigidus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 532140 has `NCBITaxon:2571260`, label `Baffinella frigidus`, rank `SPECIES`, direct parent `NCBITaxon:2571259`, genetic code `1`, four related synonyms, no exact synonyms, and source `gold`. `curation/seed_scope.tsv` line 62834 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Baffinella` under family `Baffinellaceae`.

`data/raw/ncbi_merged_ids.tsv` lines 92784-92785 map old identifiers `NCBITaxon:697907` and `NCBITaxon:697909` to the current target. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` has `retired_into` pointing at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 532140 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 62834 | Supported exactly: `attested rule: Baffinella frigidus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 23453 | Supported exactly with three aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:2571260`. |
| Empty native GOLD organism evidence | Exact native GOLD organism scan | Supported; no native GOLD organism row in the local JSONL snapshot has `ORGANISM NCBI TAX ID` `2571260`. |
| Empty native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; with no matching local organism IDs, no native GOLD project row joins to this taxon. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no local native GOLD analysis row joins to this taxon. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with eight rows on lines 102194-102201. |
| NCBI merged IDs | `data/raw/ncbi_merged_ids.tsv` lines 92784-92785 plus retained retired-row scan | Supported exactly; the raw merges exist but do not produce `replaces` without retained retired taxon rows. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2571260`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:2571260`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2571260`. |

The NCBI type-material inventory contributes four `culture from holotype` rows for CCMP 2045 designation variants and four `holotype` rows for C A92087 designation variants. The native GOLD JSONL snapshot has no exact organism, project, or analysis rows for this taxon even though the aggregate GOLD transform contributes a taxon-level assertion count of three.

No exact native StrainInfo rows were filed under `NCBITaxon:2571260`, and the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Baffinella` parent, four related synonyms, eight type-material rows, and two raw merged-ID rows.
- The raw NCBI merged-ID rows have no corresponding retained retired taxon rows, so no `replaces` values should be generated.
- The aggregate GOLD transform supplies a taxon-level organism count of three.
- The local native GOLD snapshot supplies no exact organisms, projects, or analyses for this taxon.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Baffinella frigidus` as `SPECIES`, and the generated record follows the source rank exactly.
