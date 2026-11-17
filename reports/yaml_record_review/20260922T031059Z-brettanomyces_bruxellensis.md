# YAML Record Review: Brettanomyces bruxellensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/brettanomyces_bruxellensis.yaml
- Started UTC: 2026-09-22T03:10:59Z
- Finished UTC: 2026-09-22T03:10:59Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5007 |
| label | Brettanomyces bruxellensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:13366 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/brettanomyces_bruxellensis.yaml`. It carries three NCBI exact synonyms, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no generated StrainInfo overlay rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*brettanomyces_bruxellensis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/brettanomyces_bruxellensis.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/brettanomyces_bruxellensis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2182 has `NCBITaxon:5007`, label `Brettanomyces bruxellensis`, rank `SPECIES`, direct parent `NCBITaxon:13366`, genetic code `1`, three exact synonyms, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 51906 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Brettanomyces` under family `Pichiaceae`.

The side merged-ID inventory maps `NCBITaxon:13369`, `NCBITaxon:1641405`, and `NCBITaxon:37784` into this taxon, but no committed retained retired-row evidence points at it, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2182 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51906 | Supported exactly by a single seed-scope row. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37311 | Supported exactly with eight aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:5007`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with seven native organisms: `Go0005465`, `Go0095653`, `Go0357053`, `Go0390101`, `Go0631159`, `Go0631987`, and `Go0705233`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with eight joined projects, `Gp0095653`, `Gp0191336`, `Gp0252499`, `Gp0332576`, `Gp0332577`, `Gp0644448`, `Gp0645808`, and `Gp0831261`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with four project-joined analyses for CBS 2796, UMY321, AWRI1613, and Brbru1. |
| NCBI merged-ID side inventory | Exact `data/raw/ncbi_merged_ids.tsv` scan | Supported; old IDs `NCBITaxon:13369`, `NCBITaxon:1641405`, and `NCBITaxon:37784` merge into `NCBITaxon:5007`, but they are not retained retired rows and therefore do not generate `replaces`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 18 rows: five culture-from-type-material spellings for CBS 72 and NRRL Y-12961 plus 13 type-material rows. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5007`. |
| Native StrainInfo exact taxon evidence | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 199 deposit-taxonomy hits and 81 direct records under `5007`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5007`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:5007`. |

The local native GOLD snapshot has seven exact organisms, eight joined projects, and four analyses joined through project IDs.

The NCBI type-material inventory contributes 18 rows across `Brettanomyces bruxellensis` culture-from-type-material and type-material entries.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Brettanomyces` parent, three exact synonyms, three related synonyms, and 18 type-material rows.
- NCBI supplies three side-inventory old IDs in `data/raw/ncbi_merged_ids.tsv`, but no retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of eight.
- The local native GOLD snapshot supplies seven exact organisms, eight joined projects, and four project-joined analyses.
- Native StrainInfo has exact rows under this taxon, but no BacDive-derived local strain inventory entry turns them into generated `data/straininfo/` overlay rows.
- BacDive does not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The NCBI type-material count and native GOLD organism/project counts exceeded the bounded scan samples, so this review also used exact taxon scans of `data/raw/ncbi_type_material.tsv`, `data/gold/organisms.jsonl.gz`, and `data/gold/projects.jsonl.gz`.
- Native GOLD analysis rows can join by project ID as well as organism ID.
- StrainInfo exact taxon rows do not generate overlay rows unless they join to the BacDive-derived local strain inventory.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Brettanomyces bruxellensis` as `SPECIES`, and the generated record follows the source rank exactly.
