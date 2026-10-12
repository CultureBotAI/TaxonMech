# YAML Record Review: Cenococcum geophilum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cenococcum_geophilum.yaml
- Started UTC: 2026-09-22T07:30:26Z
- Finished UTC: 2026-09-22T07:30:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5570 |
| label | Cenococcum geophilum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5569 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/cenococcum_geophilum.yaml`. It carries one NCBI related synonym, no exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no NCBI type-material rows, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cenococcum_geophilum.md' -print` returned no prior report. This search was scoped to the ignored primary `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/cenococcum_geophilum.yaml` printed `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/cenococcum_geophilum.yaml` scanned one file with zero ERROR rows and refreshed the temp worktree's `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2474 has `NCBITaxon:5570`, label `Cenococcum geophilum`, rank `SPECIES`, direct parent `NCBITaxon:5569`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 52037 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Cenococcum` under family `Gloniaceae`.

The bounded merged-ID scan found no old NCBI IDs that point into this taxon and no retained retired rows, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2474 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52037 | Supported exactly: `attested rule: Cenococcum geophilum, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 38759 | Supported exactly with 39 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:5570`; the generated note correctly says descendant taxa are not gathered. |
| Native GOLD organism evidence | Complete exact native GOLD organism scan | Supported exactly with 25 native organisms filed directly under NCBI taxon ID `5570`. |
| Native GOLD project evidence | Complete exact native GOLD sequencing-project scan | Supported exactly with 205 joined projects for the 25 exact native GOLD organism IDs. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by all 205 project IDs | Supported exactly with two analysis rows for `Cenococcum geophilum 1.58`, both linked by `AP PROJECT GOLD IDS` to `Gp0006117`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no NCBI type-material rows mention `NCBITaxon:5570`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5570`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5570`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:5570`. |
| Omitted `replaces` | Exact scans of retained retired rows and merged NCBI IDs | Supported; no retained retired row or side-inventory merged ID points into `NCBITaxon:5570`. |

The aggregate GOLD row used for generation contributes 39 direct organism assertions, while the local native GOLD snapshot currently has 25 exact organism rows for taxon ID `5570`; both are direct-to-taxon surfaces rather than descendant rollups. The 25 native organisms have 205 joined projects and two joined analyses.

The native StrainInfo snapshot has 21 exact direct rows and 23 exact deposit links under `NCBITaxon:5570`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code `1`, the direct `Cenococcum` parent, one related synonym, no exact synonyms, and no type-material rows.
- NCBI has no side-inventory old IDs or retained retired rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of 39 and the generated descendant-note.
- The local native GOLD snapshot supplies 25 exact organisms, 205 projects, and two joined analyses.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, retained-old-ID, merged-ID, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Cenococcum geophilum` as `SPECIES`, and the generated record follows the source rank exactly.
