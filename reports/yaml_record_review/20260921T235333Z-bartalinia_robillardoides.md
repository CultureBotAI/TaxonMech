# YAML Record Review: Bartalinia robillardoides

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/bartalinia_robillardoides.yaml
- Started UTC: 2026-09-21T23:52:16Z
- Finished UTC: 2026-09-21T23:53:33Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:162409 |
| label | Bartalinia robillardoides |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:162405 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/bartalinia_robillardoides.yaml`. It carries one NCBI exact synonym, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*bartalinia_robillardoides.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/bartalinia_robillardoides.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/bartalinia_robillardoides.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 33421 has `NCBITaxon:162409`, label `Bartalinia robillardoides`, rank `SPECIES`, direct parent `NCBITaxon:162405`, genetic code `1`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 54198 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Bartalinia` under family `Sporocadaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 33421 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54198 | Supported exactly: `attested rule: Bartalinia robillardoides, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 13906 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:162409`. |
| Empty native GOLD organism evidence | Exact native GOLD organism scan | Supported; no native GOLD organism row in the local JSONL snapshot has `ORGANISM NCBI TAX ID` `162409`. |
| Empty native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; with no matching local organism IDs, no native GOLD project row joins to this taxon. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no local native GOLD analysis row joins to this taxon. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with six rows on lines 47831-47836. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `162409`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:162409`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:162409`. |

The NCBI type-material inventory contributes two `culture from epitype` rows for CBS 122705, two `epitype` rows for CBS H-21728, and two `lectotype` rows for IMI 93089. The native GOLD JSONL snapshot has no exact organism, project, or analysis rows for this taxon even though the aggregate GOLD transform contributes a taxon-level assertion count of one.

The native StrainInfo snapshot has seven exact direct rows and nine exact deposit rows under `NCBITaxon:162409`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Bartalinia` parent, one exact synonym, two related synonyms, and six type-material rows.
- NCBI does not supply merged-ID rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies no exact organisms, projects, or analyses for this taxon.
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
- NCBI ranks `Bartalinia robillardoides` as `SPECIES`, and the generated record follows the source rank exactly.
