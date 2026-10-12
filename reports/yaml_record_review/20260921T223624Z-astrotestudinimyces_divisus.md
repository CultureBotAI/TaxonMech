# YAML Record Review: Astrotestudinimyces divisus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/astrotestudinimyces_divisus.yaml
- Started UTC: 2026-09-21T22:35:00Z
- Finished UTC: 2026-09-21T22:36:24Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:3079314 |
| label | Astrotestudinimyces divisus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:3079313 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic fungal species at `data/taxa/eukaryota/astrotestudinimyces_divisus.yaml`. It carries one exact NCBI synonym, one related NCBI synonym, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*astrotestudinimyces_divisus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/astrotestudinimyces_divisus.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/astrotestudinimyces_divisus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 595473 has `NCBITaxon:3079314`, label `Astrotestudinimyces divisus`, rank `SPECIES`, direct parent `NCBITaxon:3079313`, genetic code `1`, one exact synonym, one related synonym, and source `gold`. `curation/seed_scope.tsv` line 63543 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Astrotestudinimyces` under `Neocallimastigomycetes incertae sedis`.

`data/raw/ncbi_merged_ids.tsv` line 60765 maps old ID `NCBITaxon:3025777` into `NCBITaxon:3079314`, but there is no retained retired row for that old ID in `data/raw/ncbitaxon_taxa.tsv`; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 595473 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 63543 | Supported exactly: `attested rule: Astrotestudinimyces divisus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 31196 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:3079314`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 164813-164817 | Supported exactly with five `typematerial.dmp` culture-from-holotype designations. |
| Historical NCBI merge | `data/raw/ncbi_merged_ids.tsv` line 60765 plus exact retained-old-ID scan | Supported; one old ID merges into this target but does not generate `replaces` without a retained retired NCBI inventory row. |
| Empty native GOLD evidence | Exact native GOLD organism, sequencing-project, and analysis scans | Supported; no local native GOLD organism, project, or analysis row joins to this taxon in the local snapshot. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `3079314`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `3079314`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:3079314`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:3079314`. |

NCBI records five culture-from-holotype designations for this species: `BClone21`, `OKLA B1.1`, `OKLA-B1.1`, `OKLA:B1.1`, and `OKLAB1.1`. These are source inventory evidence and do not by themselves imply a generated local strain, because TaxonMech builds eukaryotic local strain entries from BacDive-derived and StrainInfo overlay rows rather than from NCBI `typematerial.dmp`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Astrotestudinimyces` parent, one exact synonym, one related synonym, the visible merged-ID context, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
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
- NCBI ranks `Astrotestudinimyces divisus` as `SPECIES`, and the generated record follows the source rank exactly.
