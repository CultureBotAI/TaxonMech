# YAML Record Review: Ceratobasidium cereale

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ceratobasidium_cereale.yaml
- Started UTC: 2026-09-22T07:41:22Z
- Finished UTC: 2026-09-22T07:41:22Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:76351 |
| label | Ceratobasidium cereale |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5251 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/ceratobasidium_cereale.yaml`. It carries two NCBI exact synonyms, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*ceratobasidium_cereale.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/ceratobasidium_cereale.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/ceratobasidium_cereale.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 10952 has `NCBITaxon:76351`, label `Ceratobasidium cereale`, rank `SPECIES`, direct parent `NCBITaxon:5251`, genetic code `1`, exact synonyms `Ceratorhiza cerealis` and `Rhizoctonia cerealis`, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53293 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Ceratobasidium` under family `Ceratobasidiaceae`.

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:2074828` into this taxon, but the retained retired rows are empty; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 10952 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53293 | Supported exactly: `attested rule: Ceratobasidium cereale, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 42511 | Supported exactly with six aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:76351`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the current local native GOLD snapshot has no exact organism rows under NCBI taxon ID `76351`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; with no exact native organism IDs, no native projects join to this taxon in the local snapshot. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; with no joined native projects, no native analyses join to this taxon in the local snapshot. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material rows mention `NCBITaxon:76351`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `76351`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:76351`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:76351`. |
| Omitted `replaces` | Exact scan of retained retired rows plus side inventory for merged NCBI IDs | Supported; only the side inventory maps `NCBITaxon:2074828` into `NCBITaxon:76351`, so no retained retired row is available for generated `replaces`. |

The aggregate GOLD row used for generation contributes six organism assertions. The local native GOLD snapshot currently has no exact organism rows for `NCBITaxon:76351`; the generated record is still faithful to the committed aggregate row that drives `source_attestations`.

The native StrainInfo snapshot has 14 exact direct rows and 16 exact deposit links under `NCBITaxon:76351`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Ceratobasidium` parent, two exact synonyms, three related synonyms, and no type-material rows.
- NCBI has one side-inventory old ID for this taxon, but no retained retired rows to generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of six.
- The local native GOLD snapshot supplies no exact organisms, projects, or analyses for this taxon.
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
- NCBI ranks `Ceratobasidium cereale` as `SPECIES`, and the generated record follows the source rank exactly.
