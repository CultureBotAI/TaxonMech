# YAML Record Review: Bigelowiella natans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/bigelowiella_natans.yaml
- Started UTC: 2026-09-22T00:56:35Z
- Finished UTC: 2026-09-22T00:56:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:227086 |
| label | Bigelowiella natans |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:227085 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic rhizarian species at `data/taxa/eukaryota/bigelowiella_natans.yaml`. It carries four NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*bigelowiella_natans.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/bigelowiella_natans.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/bigelowiella_natans.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 44526 has `NCBITaxon:227086`, label `Bigelowiella natans`, rank `SPECIES`, direct parent `NCBITaxon:227085`, genetic code `1`, four exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 54627 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Bigelowiella` under class `Chlorarachniophyceae`.

`data/raw/ncbi_merged_ids.tsv` maps three old IDs to this taxon: `NCBITaxon:467051`, `NCBITaxon:77303`, and `NCBITaxon:91327`. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at this taxon with `retired_into`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 44526 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 54627 | Supported exactly: `attested rule: Bigelowiella natans, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 21357 | Supported exactly with 23 aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:227086`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with 23 native organisms filed directly under `NCBITaxon:227086`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with 20 projects joined through those exact organism IDs. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no local native GOLD analysis row joins to this taxon. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no exact type-material row was filed under `NCBITaxon:227086`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `227086`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:227086`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:227086`. |

The exact native GOLD organism scan found one bare `Bigelowiella natans` row, four CCMP 1242/1258.1/1259/623 organism rows, and 18 CCMP621/RCC623 resequencing organism rows filed directly under `NCBITaxon:227086`. The native GOLD project scan found two projects for the bare `Go0039037` organism plus 18 projects for the CCMP621/RCC623 resequencing organisms; the four CCMP 1242/1258.1/1259/623 organisms had no joined project rows.

The native StrainInfo snapshot has one exact direct row and two exact deposit rows under `NCBITaxon:227086`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Bigelowiella` parent, four exact synonyms, and two related synonyms.
- NCBI supplies three raw merged-ID rows, but does not supply a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of 23.
- The local native GOLD snapshot supplies 23 exact organisms with 20 joined projects and no joined analyses.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD source attestation explicitly counts records filed directly under this taxon, not descendant taxa, and the exact native GOLD scan used direct `ORGANISM NCBI TAX ID` matches for `227086`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Bigelowiella natans` as `SPECIES`, and the generated record follows the source rank exactly.
