# YAML Record Review: Bipolaris oryzae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/bipolaris_oryzae.yaml
- Started UTC: 2026-09-22T01:03:35Z
- Finished UTC: 2026-09-22T01:03:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:101162 |
| label | Bipolaris oryzae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:33194 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/bipolaris_oryzae.yaml`. It carries four NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*bipolaris_oryzae.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/bipolaris_oryzae.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/bipolaris_oryzae.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 17457 has `NCBITaxon:101162`, label `Bipolaris oryzae`, rank `SPECIES`, direct parent `NCBITaxon:33194`, genetic code `1`, four exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53656 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Bipolaris` under family `Pleosporaceae`.

`data/raw/ncbi_merged_ids.tsv` maps three old IDs to this taxon: `NCBITaxon:1484600`, `NCBITaxon:2081992`, and `NCBITaxon:33195`. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at this taxon with `retired_into`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 17457 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53656 | Supported exactly: `attested rule: Bipolaris oryzae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 267 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:101162`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with one native organism, `Go0384235`, for strain TG12bL2. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with project `Gp0235326` for `Go0384235`. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis row joining through project `Gp0235326`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no exact type-material row was filed under `NCBITaxon:101162`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `101162`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:101162`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:101162`. |

The local native GOLD snapshot has one exact TG12bL2 organism with one project and one joined analysis row.

The native StrainInfo snapshot has 51 exact direct rows and 65 exact deposit rows under `NCBITaxon:101162`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Bipolaris` parent, four exact synonyms, and two related synonyms.
- NCBI supplies three raw merged-ID rows, but does not supply a retained retired row that would generate `replaces`.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one project and one joined analysis.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD source attestation explicitly counts records filed directly under this taxon, not descendant taxa, and the exact native GOLD scan used direct `ORGANISM NCBI TAX ID` matches for `101162`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Bipolaris oryzae` as `SPECIES`, and the generated record follows the source rank exactly.
