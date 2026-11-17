# YAML Record Review: Bipolaris maydis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/bipolaris_maydis.yaml
- Started UTC: 2026-09-22T01:01:55Z
- Finished UTC: 2026-09-22T01:01:55Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5016 |
| label | Bipolaris maydis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:33194 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/bipolaris_maydis.yaml`. It carries five NCBI exact synonyms, three NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*bipolaris_maydis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/bipolaris_maydis.yaml` exited successfully. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/bipolaris_maydis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2187 has `NCBITaxon:5016`, label `Bipolaris maydis`, rank `SPECIES`, direct parent `NCBITaxon:33194`, genetic code `1`, five exact synonyms, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 51907 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Bipolaris` under family `Pleosporaceae`.

`data/raw/ncbi_merged_ids.tsv` maps one old ID to this taxon: `NCBITaxon:509226`. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at this taxon with `retired_into`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2187 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51907 | Supported exactly: `attested rule: Bipolaris maydis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37327 | Supported exactly with 16 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:5016`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with 16 native organisms filed directly under `NCBITaxon:5016`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with 18 projects joined through those exact organism IDs. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with four analysis rows joined through projects `Gp0098693`, `Gp0010041`, `Gp0645259`, and `Gp0779658`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with eight rows on lines 224775-224782. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5016`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5016`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:5016`. |

The exact native GOLD organism scan found two ATCC 48331 / C4 organism rows, three Hm338/Hm540/PR1x412 organism rows near the start of the snapshot, nine `Cochliobolus heterostrophus` organism rows in the Go0515324-Go0516968 blocks, and two later BM1/KET7 organism rows. Those rows join to 18 projects, including three ATCC 48331 projects and one project for each of the other 15 exact organism rows; four of the 18 projects have local native analysis rows.

The NCBI type-material inventory contributes two `holotype` rows for BPI 626700, two `culture from neotype` rows for CBS 137271, two `culture from paratype` rows for CBS 136.29, and two `neotype` rows for ATCC 48332. The native StrainInfo snapshot has 126 exact direct rows and 133 exact deposit rows under `NCBITaxon:5016`; none overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Bipolaris` parent, five exact synonyms, three related synonyms, and eight type-material rows.
- NCBI supplies one raw merged-ID row, but does not supply a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of 16.
- The local native GOLD snapshot supplies 16 exact organisms with 18 joined projects and four joined analyses.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD source attestation explicitly counts records filed directly under this taxon, not descendant taxa, and the exact native GOLD scan used direct `ORGANISM NCBI TAX ID` matches for `5016`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Bipolaris maydis` as `SPECIES`, and the generated record follows the source rank exactly.
