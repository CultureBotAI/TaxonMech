# YAML Record Review: Australozyma touchengensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/australozyma_touchengensis.yaml
- Started UTC: 2026-09-21T23:17:25Z
- Finished UTC: 2026-09-21T23:18:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:432114 |
| label | Australozyma touchengensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:3300567 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic yeast species at `data/taxa/eukaryota/australozyma_touchengensis.yaml`. It carries one exact NCBI synonym, three related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*australozyma_touchengensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/australozyma_touchengensis.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/australozyma_touchengensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 95503 has `NCBITaxon:432114`, label `Australozyma touchengensis`, rank `SPECIES`, direct parent `NCBITaxon:3300567`, genetic code `12`, one exact synonym, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 55638 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Australozyma` under family `Metschnikowiaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 95503 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55638 | Supported exactly: `attested rule: Australozyma touchengensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 35332 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:432114`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0704957` for strain `CBS 10585` on line 525403. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with project `Gp0830973` on line 609528. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis row joins to organism `Go0704957` or project `Gp0830973` in the local snapshot. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with ten rows on lines 209727-209736, all under synonym name `Candida touchengensis`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `432114`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:432114`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:432114`. |

The NCBI type-material inventory contributes four `culture from holotype` rows for CBS 10585, four `culture from holotype` rows for SY 4S03, and two `holotype` rows for BCRC 23097. The local native GOLD snapshot has the matching CBS 10585 organism and one project, without a joined analysis row.

The native StrainInfo snapshot has one exact direct row under `NCBITaxon:432114` with BCRC 23097 and CCRC 23097 deposits. It does not overlay onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Australozyma` parent, one exact synonym, three related synonyms, and ten type-material rows.
- NCBI does not supply merged-ID rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one project and no joined analysis row.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Australozyma touchengensis` as `SPECIES`, and the generated record follows the source rank exactly.
