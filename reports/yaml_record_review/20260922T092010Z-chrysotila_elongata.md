# YAML Record Review: Chrysotila elongata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chrysotila_elongata.yaml
- Started UTC: 2026-09-22T09:20:10Z
- Finished UTC: 2026-09-22T09:20:10Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:97483 |
| label | Chrysotila elongata |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:424538 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic haptophyte species at `data/taxa/eukaryota/chrysotila_elongata.yaml`. It carries two NCBI exact synonyms, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*chrysotila_elongata.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chrysotila_elongata.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chrysotila_elongata.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 16455 has `NCBITaxon:97483`, label `Chrysotila elongata`, rank `SPECIES`, direct parent `NCBITaxon:424538`, genetic code `1`, two exact synonyms, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53586 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Chrysotila` under family `Isochrysidaceae`.

The merged-ID scan found no old IDs pointing into this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 16455 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53586 | Supported exactly: `attested rule: Chrysotila elongata, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 45157 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:97483`. |
| Empty native GOLD surface | Exact native GOLD organism, project, and analysis scans | Supported; the local native GOLD snapshot has no exact organism, joined project, or joined analysis rows for `NCBITaxon:97483`. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported with no exact direct StrainInfo records and one exact deposit-taxonomy match under taxon ID `97483`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or raw generated-strain row was filed under taxon ID `97483`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:97483`. |
| Empty type-material and auxiliary source surfaces | Exact scans of `data/raw/ncbi_type_material.tsv` plus the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no type-material or auxiliary source row mentions `NCBITaxon:97483`. |
| Omitted `replaces` | Exact scan of merged NCBI IDs | Supported; no old ID maps into this current taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Chrysotila` parent, two exact synonyms, and three related synonyms.
- The NCBI merged-ID side inventory has no old ID for this taxon, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of one; the local native GOLD JSONL snapshot has no exact organism, project, or analysis rows under `NCBITaxon:97483`.
- Native StrainInfo has an exact deposit-taxonomy hit for this taxon, but there are no local BacDive-derived strain records or generated StrainInfo overlay rows under `NCBITaxon:97483`.
- BacDive, type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Chrysotila elongata` as `SPECIES`, and the generated record follows the source rank exactly.
- Native StrainInfo has a deposit-only exact hit, `RCC 1430`, under `siID` 346785; no local generated StrainInfo assembly, exclusion, or related-record row is derived from it in the current maintained overlay tables.
