# YAML Record Review: Cladorrhinum coprophilum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cladorrhinum_coprophilum.yaml
- Started UTC: 2026-09-22T10:05:05Z
- Finished UTC: 2026-09-22T10:05:05Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:314027 |
| label | Cladorrhinum coprophilum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:223374 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cladorrhinum_coprophilum.yaml`. It carries two NCBI exact synonyms, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cladorrhinum_coprophilum.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cladorrhinum_coprophilum.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cladorrhinum_coprophilum.yaml` exited successfully after scanning one file and refreshing the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already passed on the current checkout. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 64226 has `NCBITaxon:314027`, label `Cladorrhinum coprophilum`, rank `SPECIES`, direct parent `NCBITaxon:223374`, genetic code `1`, two exact synonyms, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 55147 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cladorrhinum` under family `Podosporaceae`.

Exact scans found no retained retired row or exact `data/raw/ncbi_merged_ids.tsv` old ID for this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 64226 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55147 | Supported exactly: `attested rule: Cladorrhinum coprophilum, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 31711 | Supported exactly with one aggregate GOLD organism assertion for `NCBITaxon:314027`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has one exact organism row, `Go0651397`, for `Cercophora coprophila NBRC 32091`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact projects `Gp0688301` and `Gp0699292` join to `Go0651397`. |
| Empty native GOLD analysis surface | Exact native GOLD analysis scan by joined project IDs | Supported; no native GOLD analysis rows join to exact projects `Gp0688301` or `Gp0699292`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material row exists for `NCBITaxon:314027`. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported with one exact direct StrainInfo record and two exact deposit-taxonomy matches under taxon ID `314027`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or raw generated-strain row was filed under taxon ID `314027`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:314027`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:314027`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; no retained retired row or exact merged-ID row points into this taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cladorrhinum` parent, two exact synonyms, and three related synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism, two joined projects, and no joined analysis rows for this taxon.
- Native StrainInfo has an exact row for this taxon, but there are no local BacDive-derived strain records or generated StrainInfo overlay rows under `NCBITaxon:314027`.
- BacDive, NCBI type-material, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- An `rg --no-ignore --hidden` check over `data/raw`, `data/straininfo`, and `curation/seed_scope.tsv` included ignored files while confirming there were no additional maintained rows for this taxon beyond the expected NCBI, GOLD aggregate, seed-scope, native GOLD, and native StrainInfo evidence.
- NCBI ranks `Cladorrhinum coprophilum` as `SPECIES`, and the generated record follows the source rank exactly.
