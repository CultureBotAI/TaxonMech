# YAML Record Review: Penicillium turbatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/penicillium_turbatum.yaml
- Started UTC: 2026-09-22T00:32:09Z
- Finished UTC: 2026-09-22T00:33:52Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:70105 |
| label | Penicillium turbatum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5073 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/penicillium_turbatum.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*penicillium_turbatum.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/penicillium_turbatum.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/penicillium_turbatum.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 9775 has `NCBITaxon:70105`, label `Penicillium turbatum`, rank `SPECIES`, direct parent `NCBITaxon:5073`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 53205 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Penicillium` under family `Aspergillaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 9775 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53205 | Supported exactly: `attested rule: Penicillium turbatum, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 41625 | Supported exactly with 12 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:70105`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with 11 native organisms, from `Go0607911` through `Go0607922`. |
| Empty native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; no native GOLD project row joins to the 11 exact local organism IDs. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no local native GOLD analysis row joins to this taxon. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 22 rows on lines 258727-258748. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `70105`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:70105`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:70105`. |

The NCBI type-material inventory contributes 22 `type material` rows for ATCC 9782, CBS 237.60, CBS 383.48, DSM 2426, FRR 757, IFO 7767, IMI 039738, MUCL 29115, NRRL 757, NRRL 758, and QM 1941 variants. The local native GOLD snapshot has 11 exact organisms and no joined project or analysis rows; that exact native organism count is one lower than the aggregate GOLD taxon-level organism count of 12.

The native StrainInfo snapshot has seven exact direct rows and 23 exact deposit rows under `NCBITaxon:70105`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Penicillium` parent, one related synonym, and 22 type-material rows.
- NCBI does not supply merged-ID rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of 12.
- The local native GOLD snapshot supplies 11 exact organisms with no projects or joined analyses.
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
- NCBI ranks `Penicillium turbatum` as `SPECIES`, and the generated record follows the source rank exactly.
