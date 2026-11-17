# YAML Record Review: Aspergillus luchuensis IFO 4308

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_luchuensis_ifo_4308.yaml
- Started UTC: 2026-09-21T18:39:44Z
- Finished UTC: 2026-09-21T18:40:40Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1033177 |
| label | Aspergillus luchuensis IFO 4308 |
| rank | STRAIN |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:1069201 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic strain record at `data/taxa/eukaryota/aspergillus_luchuensis_ifo_4308.yaml`. It carries one NCBI exact synonym, no NCBI type-material entries, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_luchuensis_ifo_4308.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_luchuensis_ifo_4308.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_luchuensis_ifo_4308.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 220936 has `NCBITaxon:1033177`, label `Aspergillus luchuensis IFO 4308`, rank `STRAIN`, direct parent `NCBITaxon:1069201`, genetic code `1`, exact synonym `Aspergillus kawachii IFO 4308`, and source `gold`. `curation/seed_scope.tsv` line 57236 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent species `Aspergillus luchuensis`.

`data/raw/ncbi_merged_ids.tsv` has no row that redirects an old NCBI taxon ID into `NCBITaxon:1033177`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonym | `data/raw/ncbitaxon_taxa.tsv` line 220936 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 57236 | Supported exactly: `attested rule: Aspergillus luchuensis IFO 4308, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 434 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1033177`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no `typematerial.dmp` designation is filed under `NCBITaxon:1033177`. |
| Empty BacDive strain surface | Exact taxon scan of `data/bacdive/records.jsonl.gz`; exact scan of `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1033177`. |
| Empty StrainInfo overlay | Exact scans of `data/straininfo/records.jsonl.gz`, `data/straininfo/assemblies.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; StrainInfo has no direct strain record, deposit-taxonomy record, assembly overlay, or related-record overlay for `NCBITaxon:1033177`. |

Native GOLD contains one exact organism row for `Aspergillus kawachii IFO 4308`, one linked sequencing-project row, and one linked analysis row through `AP PROJECT GOLD IDS`. The organism row has no `ORGANISM CULTURE COLLECTION ID` or `ORGANISM STRAIN` value to join through, and no matching row exists in the BacDive-derived local strain inventory; this native GOLD evidence is therefore correctly absent from generated strain, assembly, genome, and related-record sections.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies the strain identity, lineage, genetic code, and exact synonym.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one organism, one sequencing project, and one analysis for this strain; they correctly do not generate record-level assertions because the GOLD adapter only emits through culture identifiers already present in `data/raw/bacdive_strains.tsv`.
- StrainInfo and BacDive do not supply exact records for this taxon.
- NCBI type-material, LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The native GOLD analysis lookup checked both `AP ORGANISM GOLD ID` and exact IDs in `AP PROJECT GOLD IDS`.
