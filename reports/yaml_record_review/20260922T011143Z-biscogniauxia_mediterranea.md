# YAML Record Review: Biscogniauxia mediterranea

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/biscogniauxia_mediterranea.yaml
- Started UTC: 2026-09-22T01:11:43Z
- Finished UTC: 2026-09-22T01:11:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:97377 |
| label | Biscogniauxia mediterranea |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:97376 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/biscogniauxia_mediterranea.yaml`. It carries two NCBI exact synonyms, 99 NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*biscogniauxia_mediterranea.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/biscogniauxia_mediterranea.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/biscogniauxia_mediterranea.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 16430 has `NCBITaxon:97377`, label `Biscogniauxia mediterranea`, rank `SPECIES`, direct parent `NCBITaxon:97376`, genetic code `1`, two exact synonyms, 99 related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53580 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Biscogniauxia` under family `Xylariaceae`.

`data/raw/ncbi_merged_ids.tsv` maps 97 old IDs to this taxon, mostly former `fungal sp. ARIZ` isolate IDs now folded into `NCBITaxon:97377`. No retained retired row in `data/raw/ncbitaxon_taxa.tsv` points at this taxon with `retired_into`, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 16430 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53580 | Supported exactly: `attested rule: Biscogniauxia mediterranea, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 45146 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:97377`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with two native organisms filed directly under `NCBITaxon:97377`. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with 24 projects joined through those exact organism IDs. |
| Empty native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported; no native GOLD analysis row joins through exact `NCBITaxon:97377` organism or project IDs. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no exact type-material row was filed under `NCBITaxon:97377`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `97377`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:97377`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:97377`. |

The local native GOLD snapshot has one exact AZ0048 organism and one exact CBS 129072 organism. Those rows join to 24 projects: minimal-draft and transcriptome projects for each strain, plus 20 AZ0048 gene-expression projects on lines 417009-417028 of `data/gold/projects.jsonl.gz`.

The native StrainInfo snapshot has eight exact direct rows and ten exact deposit rows under `NCBITaxon:97377`. None overlays onto a BacDive-derived local strain inventory entry, so the generated StrainInfo assembly, exclusion, and related-record surfaces are correctly empty for this record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Biscogniauxia` parent, two exact synonyms, 99 related synonyms, and 97 raw merged-ID rows.
- NCBI does not supply a retained retired row that would generate `replaces`, and it does not supply type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot supplies two exact organisms with 24 joined projects and no joined analyses.
- BacDive does not supply exact local strain evidence for this taxon, and exact StrainInfo rows correctly have no generated overlay rows without a BacDive-derived local strain.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The GOLD source attestation explicitly counts records filed directly under this taxon, not descendant taxa, and the exact native GOLD scan used direct `ORGANISM NCBI TAX ID` matches for `97377`.
- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Biscogniauxia mediterranea` as `SPECIES`, and the generated record follows the source rank exactly.
