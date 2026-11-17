# YAML Record Review: Aspergillus sclerotialis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_sclerotialis.yaml
- Started UTC: 2026-09-21T20:43:00Z
- Finished UTC: 2026-09-21T20:44:22Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2070753 |
| label | Aspergillus sclerotialis |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720783 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_sclerotialis.yaml`. It carries two NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_sclerotialis.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_sclerotialis.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_sclerotialis.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 515545 has `NCBITaxon:2070753`, label `Aspergillus sclerotialis`, rank `SPECIES`, direct parent `NCBITaxon:2720783`, genetic code `1`, two exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 62246 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Polypaecilum`.

`data/raw/ncbi_merged_ids.tsv` has one old ID, `NCBITaxon:89794`, redirected into `NCBITaxon:2070753`; `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species, so the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 515545 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 62246 | Supported exactly: `attested rule: Aspergillus sclerotialis, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 19772 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2070753`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 82577-82580 | Supported exactly with CBS and IAM type-material designations for the exact synonym `Sagenomella sclerotialis`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism, one sequencing project, and one genome analysis for `Aspergillus sclerotialis CBS 366.77`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2070753`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:2070753`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2070753`. |

The native GOLD snapshot has one exact organism row on line 462152 for `Aspergillus sclerotialis CBS 366.77`; that organism joins to sequencing project `Gp0645214` on line 482215 and then to one genome analysis on line 362302 through `AP PROJECT GOLD IDS`.

Native StrainInfo has one direct strain row and two deposit-taxonomy hits under taxon `2070753`; the generated StrainInfo overlay files contain no rows for `NCBITaxon:2070753` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, two exact synonyms, two related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism, one linked sequencing project, one linked genome analysis, and no matched BacDive-derived local strain identifier to join through.
- BacDive does not supply exact local strain records for this taxon, and the native StrainInfo records do not produce generated overlay rows.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
