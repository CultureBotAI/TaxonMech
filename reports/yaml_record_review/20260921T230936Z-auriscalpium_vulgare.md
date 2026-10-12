# YAML Record Review: Auriscalpium vulgare

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/auriscalpium_vulgare.yaml
- Started UTC: 2026-09-21T23:08:33Z
- Finished UTC: 2026-09-21T23:09:36Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:40419 |
| label | Auriscalpium vulgare |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:40418 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/auriscalpium_vulgare.yaml`. It carries two related NCBI synonyms, no exact NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*auriscalpium_vulgare.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/auriscalpium_vulgare.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/auriscalpium_vulgare.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4598 has `NCBITaxon:40419`, label `Auriscalpium vulgare`, rank `SPECIES`, direct parent `NCBITaxon:40418`, genetic code `1`, two related synonyms, no exact synonyms, and source `gold`. `curation/seed_scope.tsv` line 52431 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Auriscalpium` under family `Auriscalpiaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4598 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52431 | Supported exactly: `attested rule: Auriscalpium vulgare, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34530 | Supported exactly with three aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:40419`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0072261` for strain `FP105234-sp` on line 45935 and `Go0682010` for strain `CBS 236.39` on line 506641. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with projects `Gp0072261`, `Gp0072262`, and `Gp0784077` on lines 44868, 44869, and 583113. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with two analysis rows joining through projects `Gp0072261` and `Gp0784077`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows mention `NCBITaxon:40419`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `40419`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:40419`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:40419`. |

The local native GOLD snapshot has two exact organisms with three joined projects and two joined analysis rows. Project `Gp0072262` is present for `Go0072261` without a matching analysis row in the local snapshot, and none of the GOLD rows create a local `strains` entry in this generated eukaryotic taxon record.

The native StrainInfo snapshot has 11 exact direct rows and 12 exact deposit-taxonomy rows under `NCBITaxon:40419`, including a `CBS 236.39` deposit that also appears in native GOLD. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Auriscalpium` parent, and two related synonyms.
- NCBI does not supply type-material or merged-ID rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of three.
- The local native GOLD snapshot supplies two exact organisms with three projects and two joined analysis rows.
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
- NCBI ranks `Auriscalpium vulgare` as `SPECIES`, and the generated record follows the source rank exactly.
