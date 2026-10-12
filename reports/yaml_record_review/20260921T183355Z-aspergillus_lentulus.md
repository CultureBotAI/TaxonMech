# YAML Record Review: Aspergillus lentulus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_lentulus.yaml
- Started UTC: 2026-09-21T18:32:42Z
- Finished UTC: 2026-09-21T18:33:55Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:293939 |
| label | Aspergillus lentulus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_lentulus.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_lentulus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_lentulus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_lentulus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 60054 has `NCBITaxon:293939`, label `Aspergillus lentulus`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 55044 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:293939`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 60054 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 55044 | Supported exactly: `attested rule: Aspergillus lentulus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 29034 | Supported exactly with fourteen aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:293939`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 144871-144893 | Supported exactly with twenty-three `typematerial.dmp` culture-from-holotype and holotype designations for `CBS 117885`, `IBT 27201`, `IFM 54703`, `KACC 41940`, `NRRL 35552`, `BPI 863540`, `FH5`, and their alternate variants under taxon name `Aspergillus lentulus`. |
| Empty BacDive strain surface | Exact taxon scan of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; BacDive has no exact record for taxon ID `293939` and no raw BacDive-derived strain row for `NCBITaxon:293939`. The exact quoted-token scan found `FH5`, but that BacDive record is `Draconibacterium orientale` under NCBI taxon `1168034`. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/assemblies.tsv` and `data/straininfo/related_records.tsv.gz` | Supported; `data/straininfo/records.jsonl.gz` has six direct strain records and six matching deposit-taxonomy records for taxon ID `293939`, including one entry with exact `FH5`, but none produce StrainInfo assembly or related-record overlay rows for `NCBITaxon:293939`. |

Native GOLD contains thirteen exact organism rows, thirteen linked sequencing-project rows, and thirteen linked analysis rows through `AP PROJECT GOLD IDS`. No matching row exists in the BacDive-derived local strain inventory, so this native GOLD evidence is correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one related synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of fourteen.
- The local native GOLD snapshot has thirteen organisms, thirteen sequencing projects, and thirteen analyses for this taxon; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
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
- The short `FH5` designation is shared by an `Aspergillus lentulus` StrainInfo record and an unrelated `Draconibacterium orientale` BacDive record; only the StrainInfo hit is taxonomically exact for `NCBITaxon:293939`.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
