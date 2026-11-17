# YAML Record Review: Aspergillus japonicus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_japonicus.yaml
- Started UTC: 2026-09-21T18:26:20Z
- Finished UTC: 2026-09-21T18:27:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:34381 |
| label | Aspergillus japonicus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_japonicus.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_japonicus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_japonicus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_japonicus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 3840 has `NCBITaxon:34381`, label `Aspergillus japonicus`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 52274 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:34381`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 3840 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52274 | Supported exactly: `attested rule: Aspergillus japonicus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 32855 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:34381`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 188590-188591 | Supported exactly with two `typematerial.dmp` culture-from-neotype designations for `CBS 114.51` and its colon-normalized variant under taxon name `Aspergillus japonicus`. |
| Empty BacDive strain surface | Exact taxon and exact quoted-designation scans of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `34381` or the reviewed NCBI type-material and GOLD culture designations. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/assemblies.tsv` and `data/straininfo/related_records.tsv.gz` | Supported; `data/straininfo/records.jsonl.gz` has eighty-seven direct strain records, ninety matching deposit-taxonomy records, and 136 matching deposits for taxon ID `34381`, including one entry with the exact `CBS 114.51` type-material and GOLD culture string, but none produce StrainInfo assembly or related-record overlay rows for `NCBITaxon:34381`. |

Native GOLD contains two exact organism rows for this taxon, three linked sequencing-project rows, and one linked analysis row through `AP PROJECT GOLD IDS`. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one related synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot has two organisms, three sequencing projects, and one analysis for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo has exact taxon records, but no assembly or related-record exports for them and no BacDive-derived strains to overlay.
- BacDive does not supply exact records for this taxon.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The native GOLD analysis lookup checked both `AP ORGANISM GOLD ID` and exact IDs in `AP PROJECT GOLD IDS`.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
