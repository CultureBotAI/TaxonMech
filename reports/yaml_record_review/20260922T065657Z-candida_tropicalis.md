# YAML Record Review: Candida tropicalis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/candida_tropicalis.yaml
- Started UTC: 2026-09-22T06:56:57Z
- Finished UTC: 2026-09-22T06:56:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5482 |
| label | Candida tropicalis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5475 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/candida_tropicalis.yaml`. It carries nine NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*candida_tropicalis.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/candida_tropicalis.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/candida_tropicalis.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2432 has `NCBITaxon:5482`, label `Candida tropicalis`, rank `SPECIES`, direct parent `NCBITaxon:5475`, genetic code `12`, nine exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52009 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Candida` under family `Debaryomycetaceae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2432 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52009 | Supported exactly: `attested rule: Candida tropicalis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 38494 | Supported exactly with 27 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:5482`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with 21 native organisms, spanning strains 121, E0-E5, ES5, yHKB116, yHKB300, yHKB468, yHKB469, yHKB84, yHMH234, yHMH254, yHMH255, yHMH281, yHQL347, yHQL385, Y3313, and Y1033A. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with 26 projects for the 21 exact organism rows. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported exactly with three analysis rows for Candida tropicalis 121, Y3313, and Y1033A. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 29 rows on lines 232921-232949. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5482`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5482`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:5482`. |

The NCBI type-material inventory contributes three `culture from holotype` rows for NRRL Y-12968 spelling variants and 26 `type material` rows under the source taxon name `Oidium tropicale` for ATCC 4563, ATCC 7349, ATCC 750, BCRC 20520, CBS 94, CCRC 20520, DBVPG 3982, IFO 1070, IFO 1400, JCM 1541, NRRL Y-12699, NRRL Y-607, and CBS 94 spelling variants. The local native GOLD snapshot has 21 exact organisms, 26 joined projects, and three joined analysis rows.

The native StrainInfo snapshot has 383 exact direct rows and 510 exact deposit links under `NCBITaxon:5482`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `12`, the direct `Candida` parent, nine exact synonyms, two related synonyms, and 29 type-material rows.
- NCBI does not supply merged-ID rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of 27.
- The local native GOLD snapshot supplies 21 exact organisms with 26 projects and three joined analyses.
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
- NCBI ranks `Candida tropicalis` as `SPECIES`, and the generated record follows the source rank exactly.
