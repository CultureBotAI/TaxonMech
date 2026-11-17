# YAML Record Review: Citeromyces matritensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/citeromyces_matritensis.yaml
- Started UTC: 2026-09-22T09:39:08Z
- Finished UTC: 2026-09-22T09:39:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:36909 |
| label | Citeromyces matritensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:36908 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic yeast species at `data/taxa/eukaryota/citeromyces_matritensis.yaml`. It carries two NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*citeromyces_matritensis.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/citeromyces_matritensis.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/citeromyces_matritensis.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4182 has `NCBITaxon:36909`, label `Citeromyces matritensis`, rank `SPECIES`, direct parent `NCBITaxon:36908`, genetic code `1`, two exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52358 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Citeromyces` under family `Pichiaceae`.

The merged-ID scan found no old IDs pointing into this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4182 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52358 | Supported exactly: `attested rule: Citeromyces matritensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 33539 | Supported exactly with seven aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:36909`. |
| Native GOLD organism evidence | Full exact native GOLD organism scan | Supported; the local native GOLD snapshot has seven exact organism rows under taxon ID `36909`, for ATCC 56468, CBS 2764, Ci-0101, DSM 70187, IFO 0954, NBRC 954, and NRRL Y-2407. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact project `Gp0831423` joins to `Go0608057` for `Citeromyces matritensis NRRL Y-2407`. |
| Empty native GOLD analysis surface | Exact native GOLD analysis scan by project IDs | Supported; no native GOLD analysis rows join to exact project `Gp0831423`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with sixteen `CBS 2764`, `NRRL Y-2407`, `ATCC 56468`, `BCRC/CCRC 22594`, `DBVPG 6779`, `IFO 0954`, and `JCM 2333` culture-from-type or type-material rows on lines 196179-196194. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported with thirty-four exact direct StrainInfo records and ninety exact deposit-taxonomy matches under taxon ID `36909`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or raw generated-strain row was filed under taxon ID `36909`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:36909`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:36909`. |
| Omitted `replaces` | Exact scan of merged NCBI IDs | Supported; no old ID maps into this current taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Citeromyces` parent, two exact synonyms, two related synonyms, and sixteen type-material rows.
- The NCBI merged-ID side inventory has no old ID for this taxon, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of seven.
- The local native GOLD snapshot supplies seven exact organisms, one joined project, and no joined analysis rows for this taxon.
- Native StrainInfo has exact rows for this taxon, but there are no local BacDive-derived strain records or generated StrainInfo overlay rows under `NCBITaxon:36909`.
- BacDive, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Citeromyces matritensis` as `SPECIES`, and the generated record follows the source rank exactly.
