# YAML Record Review: Cladobotryum asterophorum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cladobotryum_asterophorum.yaml
- Started UTC: 2026-09-22T09:46:29Z
- Finished UTC: 2026-09-22T09:46:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:76881 |
| label | Cladobotryum asterophorum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:73504 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cladobotryum_asterophorum.yaml`. It carries one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cladobotryum_asterophorum.md' -print` returned no prior report for this record. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cladobotryum_asterophorum.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cladobotryum_asterophorum.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already passed on the current checkout. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 11068 has `NCBITaxon:76881`, label `Cladobotryum asterophorum`, rank `SPECIES`, direct parent `NCBITaxon:73504`, genetic code `1`, the NCBI related synonym, and source `gold`. `curation/seed_scope.tsv` line 53304 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cladobotryum` under family `Hypocreaceae`.

Exact scans found no retained retired row or exact `data/raw/ncbi_merged_ids.tsv` old ID for this current taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 11068 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53304 | Supported exactly: `attested rule: Cladobotryum asterophorum, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 42653 | Supported exactly with one aggregate GOLD organism assertion for `NCBITaxon:76881`. |
| Empty exact native GOLD surface | Exact native GOLD scans by NCBI taxon ID, organism IDs, and project IDs | Supported; the local native GOLD snapshot has no exact organism, project, or analysis rows for `76881`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with four `CBS 676.77` and `MFC 1743` type-material spelling variants on lines 263902-263905. |
| Native StrainInfo exact evidence | Exact native StrainInfo taxon scans | Supported with one exact direct StrainInfo record and one exact deposit-taxonomy match under taxon ID `76881`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz`, `data/raw/bacdive_strains.tsv`, and raw generated-strain inputs | Supported; no BacDive record, raw BacDive-derived strain row, or raw generated-strain row was filed under taxon ID `76881`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:76881`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:76881`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; no retained retired row or exact merged-ID row points into this taxon. |

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cladobotryum` parent, one related synonym, and four type-material rows.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies no exact organism, joined project, or joined analysis rows for this taxon.
- Native StrainInfo has an exact row for this taxon, but there are no local BacDive-derived strain records or generated StrainInfo overlay rows under `NCBITaxon:76881`.
- BacDive, LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- An `rg --no-ignore --hidden` check over `data/raw`, `data/straininfo`, and `curation/seed_scope.tsv` included ignored files while confirming there were no additional maintained rows for this taxon beyond the expected NCBI, GOLD aggregate, seed-scope, NCBI type-material, and native StrainInfo evidence.
- NCBI ranks `Cladobotryum asterophorum` as `SPECIES`, and the generated record follows the source rank exactly.
