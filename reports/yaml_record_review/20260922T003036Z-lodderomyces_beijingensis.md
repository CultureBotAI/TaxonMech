# YAML Record Review: Lodderomyces beijingensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/lodderomyces_beijingensis.yaml
- Started UTC: 2026-09-22T00:29:05Z
- Finished UTC: 2026-09-22T00:30:36Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1775926 |
| label | Lodderomyces beijingensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:36913 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/lodderomyces_beijingensis.yaml`. It carries three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*lodderomyces_beijingensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/lodderomyces_beijingensis.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/lodderomyces_beijingensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 463189 has `NCBITaxon:1775926`, label `Lodderomyces beijingensis`, rank `SPECIES`, direct parent `NCBITaxon:36913`, genetic code `12`, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61247 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Lodderomyces` under family `Debaryomycetaceae`.

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:2866346` to this taxon, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at it with `retired_into`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 463189 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61247 | Supported exactly: `attested rule: Lodderomyces beijingensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15495 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1775926`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0705093`, strain CBS 14171. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with one project, `Gp0831114`, for `Go0705093`. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no local native GOLD analysis row joins to this taxon. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with six rows on lines 58618-58623. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1775926`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1775926`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1775926`. |

The NCBI type-material inventory contributes four `culture from holotype` rows for CICC 33087 and NYNU 15764 plus two `holotype` rows for CBS 14171. The local native GOLD snapshot has one exact organism, CBS 14171, with one joined project and no joined analysis rows.

No exact native StrainInfo rows were filed under `NCBITaxon:1775926`, and the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `12`, the direct `Lodderomyces` parent, three related synonyms, and six type-material rows.
- NCBI supplies one raw merged-ID row, but does not supply a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one project and no joined analyses.
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
- NCBI ranks `Lodderomyces beijingensis` as `SPECIES`, and the generated record follows the source rank exactly.
