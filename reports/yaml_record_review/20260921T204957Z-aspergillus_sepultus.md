# YAML Record Review: Aspergillus sepultus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_sepultus.yaml
- Started UTC: 2026-09-21T20:48:55Z
- Finished UTC: 2026-09-21T20:49:57Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:138283 |
| label | Aspergillus sepultus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5052 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_sepultus.yaml`. It carries no NCBI exact synonyms, one NCBI related synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_sepultus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_sepultus.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_sepultus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 27768 has `NCBITaxon:138283`, label `Aspergillus sepultus`, rank `SPECIES`, direct parent `NCBITaxon:5052`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 53986 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate genus parent `Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:138283`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 27768 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53986 | Supported exactly: `attested rule: Aspergillus sepultus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 8990 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:138283`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 27211-27216 | Supported exactly with CBS, ATCC, and IMI culture-from-holotype and type-material designations for `Aspergillus sepultus`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism, three sequencing projects, and no native GOLD analysis rows for `Aspergillus sepultus CBS 257.85`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `138283`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:138283`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:138283`. |

The native GOLD snapshot has one exact organism row on line 304891 for `Aspergillus sepultus CBS 257.85`. That organism joins to sequencing projects `Gp0312189`, `Gp0348437`, and `Gp0397211`; no genome-analysis rows join to the exact GOLD organism.

Native StrainInfo has six direct strain rows and eight deposit-taxonomy hits under taxon `138283`; the generated StrainInfo overlay files contain no rows for `NCBITaxon:138283` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one related synonym, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism, three linked sequencing projects, no linked genome analyses, and no matched BacDive-derived local strain identifier to join through.
- BacDive does not supply exact local strain records for this taxon, and the native StrainInfo records do not produce generated overlay rows.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, native GOLD, and complete NCBI type-material checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
