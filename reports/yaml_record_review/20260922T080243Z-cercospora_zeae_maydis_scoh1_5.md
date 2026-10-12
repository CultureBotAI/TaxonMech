# YAML Record Review: Cercospora zeae-maydis SCOH1-5

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cercospora_zeae_maydis_scoh1_5.yaml
- Started UTC: 2026-09-22T08:02:43Z
- Finished UTC: 2026-09-22T08:02:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:717836 |
| label | Cercospora zeae-maydis SCOH1-5 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:135779 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal strain at `data/taxa/eukaryota/cercospora_zeae_maydis_scoh1_5.yaml`. It carries no synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows directly under this strain taxon, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cercospora_zeae_maydis_scoh1_5.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cercospora_zeae_maydis_scoh1_5.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cercospora_cf_sigesbeckiae.yaml data/taxa/eukaryota/cercospora_sojina.yaml data/taxa/eukaryota/cercospora_zeae_maydis.yaml data/taxa/eukaryota/cercospora_zeae_maydis_scoh1_5.yaml` scanned four files with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 169247 has `NCBITaxon:717836`, label `Cercospora zeae-maydis SCOH1-5`, rank `STRAIN`, direct parent `NCBITaxon:135779`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 56551 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent species `Cercospora zeae-maydis` under genus `Cercospora`.

The bounded merged-ID scan found no old NCBI IDs that point into this taxon and no retained retired rows, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and empty synonym set | `data/raw/ncbitaxon_taxa.tsv` line 169247 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 56551 | Supported exactly: `attested rule: Cercospora zeae-maydis SCOH1-5, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 41930 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:717836`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has two exact organism rows under strain taxon ID `717836`: `Go0009719` for `SCOH1-5` and `Go0046924` with the broader organism name `Cercospora zeae-maydis`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact project `Gp0009719` joins to `Go0009719`, and expression-profiling projects `Gp0332700` and `Gp0332701` join to `Go0046924`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; exact analysis `Cercospora zeae-maydis SCOH1-5` joins to project `Gp0009719`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material rows mention strain taxon `NCBITaxon:717836`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `717836`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:717836`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:717836`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; no retained retired row or side-inventory merged ID points into `NCBITaxon:717836`. |

The aggregate GOLD row used for generation contributes one organism assertion. The local native GOLD snapshot currently has two exact organism rows under `NCBITaxon:717836`; both carry the exact NCBI taxon ID, and one carries the source label plus strain while the other carries the species name with an empty strain.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cercospora zeae-maydis` parent, no synonyms, and no type-material rows directly under this strain taxon.
- NCBI has no side-inventory old IDs or retained retired rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies two exact organisms, three joined projects, and one joined analysis for this taxon.
- BacDive and StrainInfo do not supply exact local strain or overlay evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Cercospora zeae-maydis SCOH1-5` as `STRAIN`, and the generated record follows the source rank exactly.
- The aggregate KG-Microbe GOLD count and native exact GOLD organism rows differ in the current committed inventories, but this review did not find an ID mismatch in the exact native GOLD rows.
