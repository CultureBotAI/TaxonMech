# YAML Record Review: Aspergillus sp. Z5

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_sp_z5.yaml
- Started UTC: 2026-09-21T21:24:35Z
- Finished UTC: 2026-09-21T21:25:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1662659 |
| label | Aspergillus sp. Z5 |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2606521 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_sp_z5.yaml`. It carries no NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_sp_z5.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_sp_z5.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_sp_z5.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 434215 has `NCBITaxon:1662659`, label `Aspergillus sp. Z5`, rank `SPECIES`, direct parent `NCBITaxon:2606521`, genetic code `1`, no synonyms, and source `gold`. `curation/seed_scope.tsv` line 60999 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `unclassified Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:1662659`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 434215 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60999 | Supported exactly: `attested rule: Aspergillus sp. Z5, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 14317 | Supported exactly with the aggregate KG-Microbe `organism_count` of two for `NCBITaxon:1662659`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows are filed under taxon ID `1662659`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with three organisms, three sequencing projects, and three genome analyses for exact taxon `1662659`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1662659`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1662659`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1662659`. |

The aggregate GOLD transform supplies the YAML's GOLD assertion count of two on line 14317. The local native GOLD snapshot has three exact organism rows under NCBI taxon `1662659`: `Go0116516` on line 66112 for `Aspergillus sp. Z5`, `Go0657587` on line 484108 for `Aspergillus sp. Z5 PG40-03`, and `Go0657625` on line 484146 for `Aspergillus sp. Z5 S4102`. Those organisms join to sequencing projects `Gp0120939`, `Gp0701855`, and `Gp0701893`, and the native GOLD analysis rows on lines 77759, 445610, and 445613 join through `AP PROJECT GOLD IDS` to the same projects.

Native StrainInfo has no direct strain rows or deposit-taxonomy hits under taxon `1662659`, and the generated StrainInfo overlay files contain no rows for `NCBITaxon:1662659`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, and the direct unclassified-Aspergillus parent.
- The aggregate GOLD transform supplies a taxon-level organism count of two; the local native GOLD snapshot currently has three exact organisms, three linked sequencing projects, and three linked genome analyses.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, type-material, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks this `Aspergillus sp.` entry as `SPECIES`, and the generated record follows the source rank exactly.
