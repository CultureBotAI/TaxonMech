# YAML Record Review: [Candida] ipomoeae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/candida_ipomoeae.yaml
- Started UTC: 2026-09-22T06:39:17Z
- Finished UTC: 2026-09-22T06:39:17Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1807681 |
| label | [Candida] ipomoeae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:1904948 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/candida_ipomoeae.yaml`. It carries two NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*candida_ipomoeae.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/candida_ipomoeae.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/candida_ipomoeae.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 472450 has `NCBITaxon:1807681`, label `[Candida] ipomoeae`, rank `SPECIES`, direct parent `NCBITaxon:1904948`, genetic code `12`, two exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61291 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate `Metschnikowia/Candida clade` under genus `Metschnikowia`.

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:75991` into this taxon, but the retained retired rows are empty; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 472450 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61291 | Supported exactly: `attested rule: [Candida] ipomoeae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15916 | Supported exactly with four aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1807681`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with four native organisms: `Go0455140`, `Go0455164`, `Go0455177`, and `Go0705429`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with four projects, `Gp0323466`, `Gp0323490`, `Gp0323503`, and `Gp0831472`, for the four organism rows. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported exactly with three analysis rows for UWOPS 01-141c3, UWOPS 10-104.1, and UWOPS 99-324.1. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 13 rows on lines 61200-61212. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1807681`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1807681`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1807681`. |
| Omitted `replaces` | Exact scan of retained retired rows plus side inventory for merged NCBI IDs | Supported; only the side inventory maps `NCBITaxon:75991` into `NCBITaxon:1807681`, so no retained retired row is available for generated `replaces`. |

The NCBI type-material inventory contributes nine `culture from holotype` rows for CBS 8466 and NRRL Y-27455 spelling variants plus four `holotype` rows for UWO(PS) 91-672.1 spelling variants under `Candida ipomoeae`. The local native GOLD snapshot has four exact organisms, four joined projects, and three joined analysis rows.

The native StrainInfo snapshot has two exact direct rows and three exact deposit rows under `NCBITaxon:1807681`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `12`, the direct `Metschnikowia/Candida clade` parent, two exact synonyms, two related synonyms, and 13 type-material rows.
- NCBI has one side-inventory old ID for this taxon, but no retained retired rows to generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of four.
- The local native GOLD snapshot supplies four exact organisms with four projects and three joined analyses.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `[Candida] ipomoeae` as `SPECIES`, and the generated record follows the source rank exactly.
