# YAML Record Review: Aurantiochytrium limacinum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aurantiochytrium_limacinum.yaml
- Started UTC: 2026-09-21T22:44:10Z
- Finished UTC: 2026-09-21T22:45:12Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:87102 |
| label | Aurantiochytrium limacinum |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:420535 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic stramenopile species at `data/taxa/eukaryota/aurantiochytrium_limacinum.yaml`. It carries one exact NCBI synonym, two related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aurantiochytrium_limacinum.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aurantiochytrium_limacinum.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aurantiochytrium_limacinum.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 13514 has `NCBITaxon:87102`, label `Aurantiochytrium limacinum`, rank `SPECIES`, direct parent `NCBITaxon:420535`, genetic code `1`, one exact synonym, two related synonyms, and source `gold`. `curation/seed_scope.tsv` line 53452 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `Aurantiochytrium` under `Thraustochytriidae`.

No committed NCBI merged-id or retained retired-row evidence points at this taxon, so the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 13514 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 53452 | Supported exactly: `attested rule: Aurantiochytrium limacinum, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 43614 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:87102`. |
| NCBI type-material inventory | `data/raw/ncbi_type_material.tsv` lines 269914-269916 | Supported exactly with three `typematerial.dmp` type-material designations under the homotypic synonym `Schizochytrium limacinum`. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0368580` for strain `ATCCMYA-1381` on line 273304. |
| Empty native GOLD project and analysis evidence | Exact native GOLD sequencing-project and analysis scans | Supported; no native GOLD project or analysis row joins back to this organism in the local snapshot. |
| Native StrainInfo evidence | Exact native StrainInfo direct and deposit-taxonomy scans | Supported exactly with one direct row under taxon ID `87102`, carrying deposits `ATCC MYA-1381` and `IFO 32693`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:87102`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `87102`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:87102`. |

NCBI records `ATCC MYA-1381`, `ATCC:MYA-1381`, and `ATCC:MYA:1381` as type-material spellings for `Schizochytrium limacinum`. StrainInfo and GOLD both reference the same culture token through their own punctuation variants, but no BacDive-derived strain or generated StrainInfo overlay row is filed under this target.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `Aurantiochytrium` parent, one exact synonym, two related synonyms, and the type-material designations reviewed above.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with no joined project or analysis rows.
- The local native StrainInfo snapshot supplies one exact row with two deposits, but the generated StrainInfo overlay surface is empty for this target.
- BacDive does not supply exact local strain evidence for this taxon.
- LPSN, GTDB, MediaDive, Madin et al., BactoTraits, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The BacDive, StrainInfo, raw strain-table, auxiliary source, type-material, and native GOLD checks used exact scans of the relevant committed TSV and gzip JSONL snapshots.
- NCBI ranks `Aurantiochytrium limacinum` as `SPECIES`, and the generated record follows the source rank exactly.
