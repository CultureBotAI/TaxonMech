# YAML Record Review: Aspergillus oryzae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_oryzae.yaml
- Started UTC: 2026-09-21T19:39:30Z
- Finished UTC: 2026-09-21T19:43:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:5062 |
| label | Aspergillus oryzae |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_oryzae.yaml`. It carries three NCBI exact synonyms, two NCBI related synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_oryzae.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_oryzae.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_oryzae.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 2211 has `NCBITaxon:5062`, label `Aspergillus oryzae`, rank `SPECIES`, direct parent `NCBITaxon:2720871`, genetic code `1`, three exact synonyms, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 51921 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` line 94339 redirects old ID `NCBITaxon:748371` into `NCBITaxon:5062`, but that old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`; the record therefore has no retired predecessor record to list in `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 2211 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 51921 | Supported exactly: `attested rule: Aspergillus oryzae, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 37426 | Supported exactly with eight aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:5062`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 225420-225433 | Supported exactly with `CBS 100925` and `NRRL 447` culture-from-neotype variants plus `CBS 466.91`, `IFO 6215`, and `WB 5032` type-material variants for `Eurotium oryzae`. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported; the local snapshot has ten exact organism rows, 38 linked projects, and nine linked analyses under NCBI taxon `5062`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `5062`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:5062`. |

The native GOLD snapshot contains ten exact organism rows for NCBI taxon `5062`, including `Go0038491` for `Aspergillus oryzae RIB40` on line 32546 and several unstrained `Aspergillus oryzae` organism rows. Those organisms join to 38 sequencing projects and nine genome analyses through either `ORGANISM GOLD ID` or `AP PROJECT GOLD IDS`.

Native StrainInfo has 249 direct strain rows and 578 deposit-taxonomy hits under taxon `5062`, but the generated StrainInfo overlay files contain no rows for `NCBITaxon:5062` because the overlay is limited to BacDive-derived local strains.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, exact and related synonyms, the merged old ID, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of eight.
- The local native GOLD snapshot has exact rows for this taxon, but no matched BacDive-derived local strain identifier to join through.
- BacDive does not supply exact local strain records for this taxon, and the native StrainInfo records do not produce generated overlay rows.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- The GOLD aggregate in `data/raw/gold_organisms.tsv` can differ from the count of exact rows in the native GOLD projection; the YAML assertion count correctly follows the aggregate raw inventory.
- The NCBI type-material rows do not create `nomenclature` entries in generated eukaryotic records because TaxonMech generates nomenclature from LPSN only.
