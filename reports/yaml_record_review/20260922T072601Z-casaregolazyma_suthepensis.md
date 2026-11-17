# YAML Record Review: Casaregolazyma suthepensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/casaregolazyma_suthepensis.yaml
- Started UTC: 2026-09-22T07:26:01Z
- Finished UTC: 2026-09-22T07:26:01Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:795803 |
| label | Casaregolazyma suthepensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:3712543 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/casaregolazyma_suthepensis.yaml`. It carries one NCBI exact synonym, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, four NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*casaregolazyma_suthepensis.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/casaregolazyma_suthepensis.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/casaregolazyma_suthepensis.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 179553 has `NCBITaxon:795803`, label `Casaregolazyma suthepensis`, rank `SPECIES`, direct parent `NCBITaxon:3712543`, genetic code `1`, exact synonym `Candida suthepensis`, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 56704 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Casaregolazyma` under family `Trichomonascaceae`.

The bounded merged-ID scan found no old NCBI IDs that point into this taxon and no retained retired rows, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 179553 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 56704 | Supported exactly: `attested rule: Casaregolazyma suthepensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 42796 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:795803`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0705031`, strain CBS 12270 under the source name `Candida suthepensis CBS 12270`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with project `Gp0831051` for `Go0705031`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; no native analysis rows join to that project ID in the local snapshot. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with four type-material rows for CBS 12270 and JCM 16822 spelling variants. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `795803`. |
| Empty StrainInfo surface | Exact scans of native StrainInfo rows plus generated StrainInfo TSVs | Supported; no native or generated StrainInfo rows mention `NCBITaxon:795803`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:795803`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; no retained retired row or side-inventory merged ID points into `NCBITaxon:795803`. |

The local native GOLD snapshot has one exact organism, CBS 12270, with one joined project and no joined analysis rows. NCBI lists CBS 12270 and JCM 16822 as type-material culture-collection designations under the accepted synonym `Candida suthepensis`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Casaregolazyma` parent, one exact synonym, three related synonyms, and four type-material rows.
- NCBI has no side-inventory old IDs or retained retired rows for this taxon.
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

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Casaregolazyma suthepensis` as `SPECIES`, and the generated record follows the source rank exactly.
