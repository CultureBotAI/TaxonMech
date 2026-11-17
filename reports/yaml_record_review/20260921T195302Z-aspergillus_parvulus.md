# YAML Record Review: Aspergillus parvulus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_parvulus.yaml
- Started UTC: 2026-09-21T19:51:55Z
- Finished UTC: 2026-09-21T19:53:02Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41750 |
| label | Aspergillus parvulus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_parvulus.yaml`. It carries one NCBI related synonym, no NCBI exact synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_parvulus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_parvulus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_parvulus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4879 has `NCBITaxon:41750`, label `Aspergillus parvulus`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 52491 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:41750`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4879 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52491 | Supported exactly: `attested rule: Aspergillus parvulus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34942 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:41750`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 207065-207083 | Supported exactly with `NRRL 4753` culture-from-holotype variants and `ATCC 16911`, `CBS 136.61`, `IMI 086558`, `LSHB BB405`, `NRRL 1846`, `QM 7955`, `UC 4613`, and `WB 4753` type-material variants for `Aspergillus parvulus`. |
| Native GOLD evidence | Exact native GOLD organism and sequencing-project scans | Supported exactly with one exact organism row and two linked sequencing projects under NCBI taxon `41750`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `41750`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:41750`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:41750`. |

The native GOLD snapshot has one exact organism row, `Go0108075` for `Aspergillus parvulus CBS 136.61` on line 59785. It joins to standard-draft project `Gp0108075` and transcriptome project `Gp0108076` on lines 61455-61456, with no linked genome-analysis rows.

Native StrainInfo has 12 direct strain rows and 21 deposit-taxonomy hits under taxon `41750`, including the `ATCC 16911` type-strain deposit and the GOLD strain `CBS 136.61`; the generated StrainInfo overlay files contain no rows for `NCBITaxon:41750` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one related synonym, and the type-material designations reviewed above.
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
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
