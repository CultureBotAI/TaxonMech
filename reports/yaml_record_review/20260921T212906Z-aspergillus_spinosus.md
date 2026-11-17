# YAML Record Review: Aspergillus spinosus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_spinosus.yaml
- Started UTC: 2026-09-21T21:27:53Z
- Finished UTC: 2026-09-21T21:29:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:36631 |
| label | Aspergillus spinosus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic species at `data/taxa/eukaryota/aspergillus_spinosus.yaml`. It carries four exact NCBI synonyms, one related NCBI synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_spinosus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_spinosus.yaml` exited successfully with no validation issue output. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_spinosus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4078 has `NCBITaxon:36631`, label `Aspergillus spinosus`, rank `SPECIES`, direct parent `NCBITaxon:2720872`, genetic code `1`, four exact synonyms, one related authorship synonym, and source `gold`. `curation/seed_scope.tsv` line 52336 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aspergillus subgen. Fumigati`.

`data/raw/ncbi_merged_ids.tsv` has no old IDs redirected into `NCBITaxon:36631`, and `data/raw/ncbitaxon_taxa.tsv` has no retained retired rows that point at this species; the record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4078 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52336 | Supported exactly: `attested rule: Aspergillus spinosus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 33420 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:36631`. |
| NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported exactly with 10 rows on lines 194815-194824 for NRRL 5034, NRRL MOLD 5034, ATCC 16898, CBS 483.65, and a comma-delimited IFO/IFM/CBS/ATCC/NRRL designation, with colonized variants where present. |
| Native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported exactly with one organism, one sequencing project, and no matching native GOLD analysis row. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `36631`. |
| Native StrainInfo exact hits | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has 51 direct records and 76 deposit-taxonomy hits under `36631`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:36631`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:36631`. |

The native GOLD snapshot has one exact organism row on line 74716 for `Aspergillus spinosus CBS 483.65` under NCBI taxon `36631`, strain `CBS 483.65`, and GOLD organism `Go0125788`. That organism joins to sequencing project `Gp0134086` on line 81907; the bounded native GOLD analysis scan found no analysis row linked to that organism or project.

Native StrainInfo has 51 direct strain rows under taxon `36631`. Those native StrainInfo hits do not create generated overlay rows because StrainInfo overlays only BacDive-derived local strain entries, and there is no exact BacDive-derived local strain for this NCBI taxon.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aspergillus subgen. Fumigati` parent, and all five synonyms.
- NCBI has 10 type-material rows for this taxon; these rows are inventory evidence and do not by themselves imply a generated local strain entry.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has one exact organism, one linked sequencing project, and no linked genome analysis.
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
- NCBI ranks `Aspergillus spinosus` as `SPECIES`, and the generated record follows the source rank exactly.
