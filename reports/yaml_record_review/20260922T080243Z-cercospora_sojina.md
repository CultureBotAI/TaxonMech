# YAML Record Review: Cercospora sojina

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cercospora_sojina.yaml
- Started UTC: 2026-09-22T08:02:43Z
- Finished UTC: 2026-09-22T08:02:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:438356 |
| label | Cercospora sojina |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:29002 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cercospora_sojina.yaml`. It carries one NCBI exact synonym, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, four NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cercospora_sojina.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cercospora_sojina.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cercospora_cf_sigesbeckiae.yaml data/taxa/eukaryota/cercospora_sojina.yaml data/taxa/eukaryota/cercospora_zeae_maydis.yaml data/taxa/eukaryota/cercospora_zeae_maydis_scoh1_5.yaml` scanned four files with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 97141 has `NCBITaxon:438356`, label `Cercospora sojina`, rank `SPECIES`, direct parent `NCBITaxon:29002`, genetic code `1`, exact synonym `Passalora sojina`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 55651 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cercospora` under family `Mycosphaerellaceae`.

`data/raw/ncbi_merged_ids.tsv` maps old ID `NCBITaxon:227735` into this taxon, but the retained retired rows are empty; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 97141 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55651 | Supported exactly: `attested rule: Cercospora sojina, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 35482 | Supported exactly with three aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:438356`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported; the local native GOLD snapshot has four exact organisms for `NCBITaxon:438356`: `Go0011038`, `Go0384738`, `Go0519857`, and `Go0589981`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported; exact projects `Gp0011038`, `Gp0235858`, `Gp0444021`, and `Gp0603926` join to those four native organism IDs. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by project IDs | Supported; exact analysis rows join to all four exact project IDs. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly by four culture-from-neotype rows for `CBS 132615` and `CPC 11353` designations at lines 211148 through 211151. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `438356`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:438356`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:438356`. |
| Omitted `replaces` | Exact scan of retained retired rows plus side inventory for merged NCBI IDs | Supported; only the side inventory maps `NCBITaxon:227735` into `NCBITaxon:438356`, so no retained retired row is available for generated `replaces`. |

The aggregate GOLD row used for generation contributes three organism assertions. The local native GOLD snapshot currently has four exact organism rows under `NCBITaxon:438356`; all four have `Cercospora sojina` names and join to exact native GOLD projects and analysis rows.

The native StrainInfo snapshot has 12 exact direct rows and 13 exact deposit links under `NCBITaxon:438356`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cercospora` parent, one exact synonym, one related synonym, and four type-material rows.
- NCBI has one side-inventory old ID for this taxon, but no retained retired rows to generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of three.
- The local native GOLD snapshot supplies four exact organisms, four joined projects, and four joined analysis rows for this taxon.
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
- NCBI ranks `Cercospora sojina` as `SPECIES`, and the generated record follows the source rank exactly.
- The aggregate KG-Microbe GOLD count and native exact GOLD organism rows differ in the current committed inventories, but this review did not find a label or taxon-ID mismatch in the exact native GOLD rows.
