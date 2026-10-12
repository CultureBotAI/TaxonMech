# YAML Record Review: Aurantiochytrium sp. KH105

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aurantiochytrium_sp_kh105.yaml
- Started UTC: 2026-09-21T22:45:20Z
- Finished UTC: 2026-09-21T22:46:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:2010233 |
| label | Aurantiochytrium sp. KH105 |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:1547518 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target record is a generated eukaryotic stramenopile species-level placeholder at `data/taxa/eukaryota/aurantiochytrium_sp_kh105.yaml`. It carries one exact NCBI synonym, no related NCBI synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive-derived local strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aurantiochytrium_sp_kh105.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aurantiochytrium_sp_kh105.yaml` exited successfully with `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aurantiochytrium_sp_kh105.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 509521 has `NCBITaxon:2010233`, label `Aurantiochytrium sp. KH105`, rank `SPECIES`, direct parent `NCBITaxon:1547518`, genetic code `1`, one exact synonym, no related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61844 keeps this taxon in scope through the attested-source rule.

The YAML lineage matches the NCBI inventory parent chain exactly, including the immediate parent `unclassified Aurantiochytrium` under `Aurantiochytrium`.

`data/raw/ncbi_merged_ids.tsv` line 16634 maps old ID `NCBITaxon:145925` into `NCBITaxon:2010233`, but there is no retained retired row for that old ID in `data/raw/ncbitaxon_taxa.tsv`; the generated record correctly omits `replaces`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 509521 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61844 | Supported exactly: `attested rule: Aurantiochytrium sp. KH105, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 18555 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:2010233`. |
| Historical NCBI merge | `data/raw/ncbi_merged_ids.tsv` line 16634 plus exact retained-old-ID scan | Supported; one old ID merges into this target but does not generate `replaces` without a retained retired NCBI inventory row. |
| Native GOLD organism evidence | Exact native GOLD organism scan | Supported exactly with `Go0593688` on line 425465. |
| Native GOLD project evidence | Exact native GOLD sequencing-project scan | Supported exactly with project `Gp0607633` on line 452372. |
| Native GOLD analysis evidence | Exact native GOLD analysis scan by organism and project IDs | Supported exactly with one analysis row joining through project `Gp0607633`. |
| Empty NCBI type-material inventory | Exact scan of `data/raw/ncbi_type_material.tsv` | Supported; no type-material rows mention `NCBITaxon:2010233`. |
| Empty BacDive-derived local strain surface | Exact taxon scans of `data/bacdive/records.jsonl.gz` and `data/raw/bacdive_strains.tsv` | Supported; no BacDive record or raw BacDive-derived strain row was filed under taxon ID `2010233`. |
| Empty native StrainInfo surface | Exact native StrainInfo taxon scans | Supported; the native StrainInfo snapshot has no direct records or deposit-taxonomy hits under `2010233`. |
| Empty generated StrainInfo overlay surface | Exact scans of `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` | Supported; no generated StrainInfo assembly, exclusion, or related-record rows mention `NCBITaxon:2010233`. |
| Empty auxiliary source surfaces | Exact scans of the LPSN, GTDB, MediaDive, Madin et al., and BactoTraits raw TSVs | Supported; no auxiliary source row mentions `NCBITaxon:2010233`. |

The local native GOLD organism is named `Aurantiochytrium sp. KH105 missing` and has no strain token, but it has one joined sequencing project and one joined analysis row in the local snapshot. None of those GOLD source rows create a local `strains` entry in this generated eukaryotic taxon record.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, the direct `unclassified Aurantiochytrium` parent, one exact synonym, and the visible merged-ID context.
- NCBI does not supply type-material rows for this taxon.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot supplies one exact organism with one joined project and one joined analysis row.
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
- NCBI ranks `Aurantiochytrium sp. KH105` as `SPECIES`, and the generated record follows the source rank exactly.
