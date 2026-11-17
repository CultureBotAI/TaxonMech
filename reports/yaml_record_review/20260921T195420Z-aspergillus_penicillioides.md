# YAML Record Review: Aspergillus penicillioides

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_penicillioides.yaml
- Started UTC: 2026-09-21T19:53:10Z
- Finished UTC: 2026-09-21T19:54:20Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41959 |
| label | Aspergillus penicillioides |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720874 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_penicillioides.yaml`. It carries one NCBI exact synonym, no NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_penicillioides.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_penicillioides.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_penicillioides.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4901 has `NCBITaxon:41959`, label `Aspergillus penicillioides`, rank `SPECIES`, direct parent `NCBITaxon:2720874`, genetic code `1`, one exact synonym, and source `gold`. `curation/seed_scope.tsv` line 52505 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` line 35807 redirects old ID `NCBITaxon:2041220` into `NCBITaxon:41959`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4901 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52505 | Supported exactly: `attested rule: Aspergillus penicillioides, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 35019 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:41959`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 207605-207618 | Supported exactly with `ATCC 16910`, `CBS 540.65`, and `NRRL 4548` culture-from-neotype variants plus `IMI 211392` neotype variants for `Aspergillus penicillioides`. |
| Native GOLD evidence | Exact native GOLD organism and sequencing-project scans | Supported exactly with one exact organism row and two linked sequencing projects under NCBI taxon `41959`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41959`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:41959`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:41959`. |

The native GOLD snapshot has one exact organism row, `Go0108083` for `Aspergillus penicilloides CBS 540.65` on line 59789. It joins to standard-draft project `Gp0108083` and transcriptome project `Gp0108084` on lines 61463-61464, with no linked genome-analysis rows.

Native StrainInfo has 40 direct strain rows and 100 deposit-taxonomy hits under taxon `41959`; the generated StrainInfo overlay files contain no rows for `NCBITaxon:41959` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one exact synonym, the merged old ID, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism with two linked sequencing projects, no genome analyses, and no matched BacDive-derived local strain identifier to join through.
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
- Native GOLD spells its organism/project names as `Aspergillus penicilloides`, but the row still has the exact numeric NCBI taxon ID `41959` and the aggregate attestation follows `NCBITaxon:41959`.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
