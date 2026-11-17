# YAML Record Review: Aspergillus tonophilus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_tonophilus.yaml
- Started UTC: 2026-09-21T21:57:40Z
- Finished UTC: 2026-09-21T21:58:20Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1697446 |
| label | Aspergillus tonophilus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720874 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_tonophilus.yaml`. It carries one exact NCBI synonym, one related NCBI synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_tonophilus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_tonophilus.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_tonophilus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 441950 has `NCBITaxon:1697446`, label `Aspergillus tonophilus`, rank `SPECIES`, direct parent `NCBITaxon:2720874`, genetic code `1`, one exact synonym, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 61036 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Aspergillus`.

`data/raw/ncbi_merged_ids.tsv` redirects old ID `NCBITaxon:41423` into `NCBITaxon:1697446`. `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 441950 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61036 | Supported exactly: `attested rule: Aspergillus tonophilus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 14646 | Supported exactly with ten aggregate KG-Microbe GOLD organism assertions for `NCBITaxon:1697446`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with eight rows: four lectotype spellings for NRRL 5124 and four culture-from-type-material rows for ATCC 16440 and CBS 405.65 variants. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported; the local snapshot has nine exact organism rows, no linked sequencing projects, and no matching native GOLD analysis row under NCBI taxon `1697446`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1697446`. |
| Native StrainInfo exact hits | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has ten direct records and 32 deposit-taxonomy hits under `1697446`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1697446`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1697446`. |

The native GOLD snapshot has exact organism rows for nine `Eurotium tonophilum` strains under NCBI taxon `1697446`, including `Go0615584` on line 446288, `Go0615585` on line 446289, `Go0615586` on line 446290, `Go0615587` on line 446291, and `Go0615588` on line 446292. The bounded native GOLD project and analysis scans found no project or analysis row linked to those exact native GOLD organisms.

Native StrainInfo has ten direct strain rows and 32 deposit-taxonomy hits under taxon `1697446`. Those native StrainInfo hits do not create generated overlay rows because StrainInfo overlays only BacDive-derived local strain entries, and there is no exact BacDive-derived local strain for this NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus subgen. Aspergillus` parent, one exact synonym, and one related synonym.
- NCBI has eight type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of ten.
- The local native GOLD snapshot has nine exact organisms, no linked sequencing projects, and no linked genome analyses.
- BacDive does not supply exact local strain evidence for this taxon, and the native StrainInfo exact hits have no BacDive-derived local strain to overlay.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Aspergillus tonophilus` as `SPECIES`, and the generated record follows the source rank exactly.
