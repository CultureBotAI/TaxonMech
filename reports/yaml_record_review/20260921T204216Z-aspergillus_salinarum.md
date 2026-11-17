# YAML Record Review: Aspergillus salinarum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_salinarum.yaml
- Started UTC: 2026-09-21T20:41:00Z
- Finished UTC: 2026-09-21T20:42:16Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1470016 |
| label | Aspergillus salinarum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720783 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_salinarum.yaml`. It carries two NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_salinarum.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_salinarum.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_salinarum.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 375397 has `NCBITaxon:1470016`, label `Aspergillus salinarum`, rank `SPECIES`, direct parent `NCBITaxon:2720783`, genetic code `1`, two exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 60240 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Polypaecilum`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:1470016`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 375397 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 60240 | Supported exactly: `attested rule: Aspergillus salinarum, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 11323 | Supported exactly with two aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1470016`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 34156-34160 | Supported exactly with culture-from-holotype and holotype designations for the exact synonym `Phialosimplex salinarum`. |
| Native GOLD evidence | Exact native GOLD organism and sequencing-project scans | Supported exactly with two exact organism rows and no linked sequencing projects under NCBI taxon `1470016`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1470016`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1470016`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1470016`. |

The native GOLD snapshot has exact organism rows for `Phialosimplex salinarum DSM 27530` on line 447494 and `Phialosimplex salinarum AGR KA 34` on line 447495. No native GOLD sequencing projects or genome analyses join to those organism IDs.

Native StrainInfo has eight direct strain rows and eight deposit-taxonomy hits under taxon `1470016`; the generated StrainInfo overlay files contain no rows for `NCBITaxon:1470016` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, two exact synonyms, two related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of two.
- The local native GOLD snapshot has two exact organisms, no linked sequencing projects, and no matched BacDive-derived local strain identifier to join through.
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
