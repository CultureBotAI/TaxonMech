# YAML Record Review: Ballistosporomyces xanthus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ballistosporomyces_xanthus.yaml
- Started UTC: 2026-09-21T23:44:32Z
- Finished UTC: 2026-09-21T23:45:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:4987 |
| label | Ballistosporomyces xanthus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:1798858 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/ballistosporomyces_xanthus.yaml`. It carries one NCBI exact synonym, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*ballistosporomyces_xanthus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/ballistosporomyces_xanthus.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/ballistosporomyces_xanthus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2174 has `NCBITaxon:4987`, label `Ballistosporomyces xanthus`, rank `SPECIES`, direct parent `NCBITaxon:1798858`, genetic code `1`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 51900 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Ballistosporomyces` under family `Chionosphaeraceae`.

`data/raw/ncbi_merged_ids.tsv` line 87201 maps old identifier `NCBITaxon:57689` to the current target. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` has `retired_into` pointing at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2174 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51900 | Supported exactly: `attested rule: Ballistosporomyces xanthus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37268 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:4987`. |
| Empty native GOLD organism evidence | Exact native GOLD organism scan | Supported; no native GOLD organism row in the local JSONL snapshot has `ORGANISM NCBI TAX ID` `4987`. |
| Empty native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; with no matching local organism IDs, no native GOLD project row joins to this taxon. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no local native GOLD analysis row joins to this taxon. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with six rows on lines 224383-224388. |
| NCBI merged IDs | `data/raw/ncbi_merged_ids.tsv` line 87201 plus retained retired-row scan | Supported exactly; the raw merge exists but does not produce `replaces` without a retained retired taxon row. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `4987`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:4987`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:4987`. |

The NCBI type-material inventory contributes six `type material` rows for CBS 7513, IGC 5356, and JCM 6885 designation variants. The native GOLD JSONL snapshot has no exact organism, project, or analysis rows for this taxon even though the aggregate GOLD transform contributes a taxon-level assertion count of one.

The native StrainInfo snapshot has two exact direct rows and 12 exact deposit rows under `NCBITaxon:4987`, including type deposits for JCM 6885 and IFO 10576. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Ballistosporomyces` parent, one exact synonym, two related synonyms, six type-material rows, and one raw merged-ID row.
- The raw NCBI merged-ID row has no corresponding retained retired taxon row, so no `replaces` value should be generated.
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
- NCBI ranks `Ballistosporomyces xanthus` as `SPECIES`, and the generated record follows the source rank exactly.
