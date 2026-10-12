# YAML Record Review: Athelia psychrophila

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/athelia_psychrophila.yaml
- Started UTC: 2026-09-21T22:36:30Z
- Finished UTC: 2026-09-21T22:37:37Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1759441 |
| label | Athelia psychrophila |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:5309 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/athelia_psychrophila.yaml`. It carries one exact NCBI synonym, three related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*athelia_psychrophila.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/athelia_psychrophila.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/athelia_psychrophila.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 459652 has `NCBITaxon:1759441`, label `Athelia psychrophila`, rank `SPECIES`, direct parent `NCBITaxon:5309`, genetic code `1`, one exact synonym, three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61228 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Athelia` under `Atheliaceae`.

`data/raw/ncbi_merged_ids.tsv` line 77710 maps old ID `NCBITaxon:436010` into `NCBITaxon:1759441`, but there is no retained retired row for that old ID in `data/raw/ncbitaxon_taxa.tsv`; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 459652 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61228 | Supported exactly: `attested rule: Athelia psychrophila, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 15315 | Supported exactly with one aggregate KG-Microbe GOLD row asserting three organisms for `NCBITaxon:1759441`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 57297-57300 | Supported exactly with four `typematerial.dmp` holotype designations. |
| Historical NCBI merge | `data/raw/ncbi_merged_ids.tsv` line 77710 plus exact retained-old-ID scan | Supported; one old ID merges into this target but does not generate `replaces` without a retained retired NCBI inventory row. |
| Empty native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported; no local native GOLD organism, project, or analysis row joins to this taxon in the local snapshot. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `1759441`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `1759441`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:1759441`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:1759441`. |

NCBI records four holotype designations for the homotypic synonym `Fibularhizoctonia psychrophila`: `CBS 109695`, `CBS-109695`, `CBS109695`, and `CBS:109695`. These are source inventory evidence and do not by themselves imply a generated local strain, because TaxonMech builds eukaryotic local strain entries from BacDive-derived and StrainInfo overlay rows rather than from NCBI `typematerial.dmp`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Athelia` parent, one exact synonym, three related synonyms, the visible merged-ID context, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of three.
- The local native GOLD snapshot does not supply an exact organism for this target.
- BacDive and StrainInfo do not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Athelia psychrophila` as `SPECIES`, and the generated record follows the source rank exactly.
