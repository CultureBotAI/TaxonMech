# YAML Record Review: Ceratocystis fimbriata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ceratocystis_fimbriata.yaml
- Started UTC: 2026-09-22T07:51:03Z
- Finished UTC: 2026-09-22T07:51:03Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5158 |
| label | Ceratocystis fimbriata |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5157 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/ceratocystis_fimbriata.yaml`. It carries two NCBI related synonyms, no exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, seven NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*ceratocystis_fimbriata.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/ceratocystis_fimbriata.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/ceratocystis_eucalypticola.yaml data/taxa/eukaryota/ceratocystis_fimbriata.yaml data/taxa/eukaryota/ceratocystis_fimbriata_cbs_114723.yaml data/taxa/eukaryota/ceratocystis_harringtonii.yaml` scanned four files with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2269 has `NCBITaxon:5158`, label `Ceratocystis fimbriata`, rank `SPECIES`, direct parent `NCBITaxon:5157`, genetic code `1`, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 51948 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Ceratocystis` under family `Ceratocystidaceae`.

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:1608159` into this taxon, but the retained retired rows are empty; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2269 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51948 | Supported exactly: `attested rule: Ceratocystis fimbriata, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37602 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for direct records under `NCBITaxon:5158`; descendant taxa are intentionally not gathered. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has exact organism `Go0591005` for `Ceratocystis fimbriata LPF1912`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact project `Gp0604950` joins to `Go0591005`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; exact analysis `Ceratocystis fimbriata LPF1912` joins to project `Gp0604950`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly by seven rows at lines 226538 through 226544: five culture-from-epitype designations and two epitype designations. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5158`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5158`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:5158`. |
| Omitted `replaces` | Exact scan of retained retired rows plus side inventory for merged NCBI IDs | Supported; only the side inventory maps `NCBITaxon:1608159` into `NCBITaxon:5158`, so no retained retired row is available for generated `replaces`. |

The aggregate GOLD row used for generation contributes one direct organism assertion, matching the one exact organism row in the local native GOLD snapshot.

The native StrainInfo snapshot has 65 exact direct rows and 79 exact deposit links under `NCBITaxon:5158`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Ceratocystis` parent, two related synonyms, no exact synonyms, and seven type-material rows.
- NCBI has one side-inventory old ID for this taxon, but no retained retired rows to generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one for records filed directly under this species.
- The local native GOLD snapshot supplies one exact organism, one joined project, and one joined analysis for this taxon.
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
- NCBI ranks `Ceratocystis fimbriata` as `SPECIES`, and the generated record follows the source rank exactly.
