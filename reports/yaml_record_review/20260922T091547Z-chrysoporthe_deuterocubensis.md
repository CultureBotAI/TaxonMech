# YAML Record Review: Chrysoporthe deuterocubensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/chrysoporthe_deuterocubensis.yaml
- Started UTC: 2026-09-22T09:15:47Z
- Finished UTC: 2026-09-22T09:15:47Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:764597 |
| label | Chrysoporthe deuterocubensis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:305399 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/chrysoporthe_deuterocubensis.yaml`. It carries two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*chrysoporthe_deuterocubensis.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/chrysoporthe_deuterocubensis.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/chrysoporthe_deuterocubensis.yaml` exited successfully. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 177532 has `NCBITaxon:764597`, label `Chrysoporthe deuterocubensis`, rank `SPECIES`, direct parent `NCBITaxon:305399`, genetic code `1`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 56680 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Chrysoporthe` nested through the no-rank `Cryphonectria-Endothia species complex`.

The merged-ID scan found no old IDs pointing into this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 177532 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 56680 | Supported exactly: `attested rule: Chrysoporthe deuterocubensis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 42525 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:764597`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0113894` for `Chrysoporthe deuterocubensis CMW 8650`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact project `Gp0117565` joins to `Go0113894`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; exact analysis `Chrysoporthe deuterocubensis CMW 8650` joins to project `Gp0117565`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with four `CBS 118651` and `CMW 18515` type-material spelling variants on lines 263185-263188. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or raw generated-strain row was filed under taxon ID `764597`. |
| Empty native and generated StrainInfo surfaces | Exact scans of native StrainInfo plus `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no native direct row, native deposit-taxonomy hit, generated assembly, exclusion, or related-record row mentions `NCBITaxon:764597`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:764597`. |
| Omitted `replaces` | Exact scan of merged NCBI IDs | Supported; no old ID maps into this current taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Chrysoporthe` parent, two related synonyms, and four type-material rows.
- The NCBI merged-ID side inventory has no old ID for this taxon, so no `replaces` entry is generated.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, one joined project, and one joined analysis for this taxon.
- BacDive, StrainInfo, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Chrysoporthe deuterocubensis` as `SPECIES`, and the generated record follows the source rank exactly.
