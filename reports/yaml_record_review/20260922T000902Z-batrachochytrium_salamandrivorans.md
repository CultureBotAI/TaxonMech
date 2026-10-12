# YAML Record Review: Batrachochytrium salamandrivorans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/batrachochytrium_salamandrivorans.yaml
- Started UTC: 2026-09-22T00:07:09Z
- Finished UTC: 2026-09-22T00:09:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1357716 |
| label | Batrachochytrium salamandrivorans |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:100474 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/batrachochytrium_salamandrivorans.yaml`. It carries three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*batrachochytrium_salamandrivorans.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/batrachochytrium_salamandrivorans.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/batrachochytrium_salamandrivorans.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 328853 has `NCBITaxon:1357716`, label `Batrachochytrium salamandrivorans`, rank `SPECIES`, direct parent `NCBITaxon:100474`, genetic code `1`, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 59654 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Batrachochytrium` under `Rhizophydiales incertae sedis`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 328853 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 59654 | Supported exactly: `attested rule: Batrachochytrium salamandrivorans, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 8678 | Supported exactly with seven aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1357716`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with seven native organisms: `Go0373181`, `Go0631172`, `Go0631173`, `Go0631174`, `Go0631175`, `Go0678464`, and `Go0678465`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with seven projects: `Gp0219982`, `Gp0644475`, `Gp0644476`, `Gp0644477`, `Gp0644478`, `Gp0780423`, and `Gp0780424`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with seven analysis rows joining through those exact project IDs. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with four rows on lines 25700-25703. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1357716`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1357716`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1357716`. |

The NCBI type-material inventory contributes two `culture from holotype` rows for CBS 135744 and two `type material` rows for AMFP13/1. The local native GOLD snapshot has seven exact organisms, seven joined projects, and seven joined analysis rows.

No exact native StrainInfo rows were filed under `NCBITaxon:1357716`, and the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Batrachochytrium` parent, three related synonyms, and four type-material rows.
- NCBI does not supply merged-ID rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of seven.
- The local native GOLD snapshot supplies seven exact organisms with seven projects and seven joined analyses.
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
- NCBI ranks `Batrachochytrium salamandrivorans` as `SPECIES`, and the generated record follows the source rank exactly.
