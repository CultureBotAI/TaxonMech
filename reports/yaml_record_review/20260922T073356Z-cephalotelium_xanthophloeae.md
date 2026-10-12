# YAML Record Review: Cephalotelium xanthophloeae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cephalotelium_xanthophloeae.yaml
- Started UTC: 2026-09-22T07:33:56Z
- Finished UTC: 2026-09-22T07:33:56Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2086370 |
| label | Cephalotelium xanthophloeae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:3019582 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cephalotelium_xanthophloeae.yaml`. It carries one NCBI exact synonym, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, two NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cephalotelium_xanthophloeae.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cephalotelium_xanthophloeae.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cephalotelium_xanthophloeae.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 517823 has `NCBITaxon:2086370`, label `Cephalotelium xanthophloeae`, rank `SPECIES`, direct parent `NCBITaxon:3019582`, genetic code `1`, exact synonym `Ravenelia xanthophloeae`, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 62291 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cephalotelium` under family `Raveneliaceae`.

The bounded merged-ID scan found no old NCBI IDs that point into this taxon and no retained retired rows, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 517823 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 62291 | Supported exactly: `attested rule: Cephalotelium xanthophloeae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 19966 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2086370`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0529076`, strain BRIP 64502 under the source name `Ravenelia xanthophloeae BRIP 64502`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with projects `Gp0457377` and `Gp0457379` for `Go0529076`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; no native analysis rows join to those project IDs in the local snapshot. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with two holotype rows for PREM 61213 spelling variants under `Ravenelia xanthophloeae`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2086370`. |
| Empty StrainInfo surface | Exact scans of native StrainInfo rows plus generated StrainInfo TSVs | Supported; no native or generated StrainInfo rows mention `NCBITaxon:2086370`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2086370`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; no retained retired row or side-inventory merged ID points into `NCBITaxon:2086370`. |

The local native GOLD snapshot has one exact organism, BRIP 64502, with two joined projects and no joined analysis rows. The exact BacDive, StrainInfo, raw strain, and auxiliary-source scans are all empty for this taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cephalotelium` parent, one exact synonym, three related synonyms, and two type-material rows.
- NCBI has no side-inventory old IDs or retained retired rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with two projects and no joined analyses.
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
- NCBI ranks `Cephalotelium xanthophloeae` as `SPECIES`, and the generated record follows the source rank exactly.
