# YAML Record Review: Aspergillus assulatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_assulatus.yaml
- Started UTC: 2026-09-21T15:59:20Z
- Finished UTC: 2026-09-21T16:00:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1245746 |
| label | Aspergillus assulatus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720872 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_assulatus.yaml`. It carries NCBI synonyms for the `Neosartorya assulata` naming history, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and NCBITAXON plus GOLD source attestations.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_assulatus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_assulatus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_assulatus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 286463 has `NCBITaxon:1245746`, label `Aspergillus assulatus`, rank `SPECIES`, parent `NCBITaxon:2720872`, genetic code `1`, exact synonym `Neosartorya assulata`, the four generated related synonyms, and source `gold`. `curation/seed_scope.tsv` line 58657 keeps this identifier in scope through the attested-source rule, consistent with the generated `SEEDED` status.

The root-first lineage in the YAML matches the NCBI inventory parent chain exactly and places the record under `Aspergillus subgen. Fumigati`, not under the `Aspergillus subgen. Nidulantes` parent shared by the preceding records in this review pass.

`data/raw/ncbi_merged_ids.tsv` line 72166 maps old `NCBITaxon:356361` to `NCBITaxon:1245746`. A literal, gitignore-independent search for `NCBITaxon:356361` across `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, `curation/seed_scope.tsv`, and `data/taxa/` found no retained retired taxon row or generated record for that old ID. Because `src/taxonmech/seed.py` emits `replaces` from retired rows retained in `data/raw/ncbitaxon_taxa.tsv`, the merged-ID row by itself does not require `replaces` on this YAML.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 286463 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 58657 | Supported exactly: `attested rule: Aspergillus assulatus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 5916 | Supported exactly with one aggregate KG-Microbe GOLD organism assertion for `NCBITaxon:1245746`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `1245746` and `NCBITaxon:1245746` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` for strain and deposit taxon IDs `1245746` and `NCBITaxon:1245746` | Supported; no direct or deposit-only StrainInfo rows were found. |

`data/raw/ncbi_type_material.tsv` has six NCBI type-material rows for `IBT 27911`, `IBT-27911`, `IBT27911`, `IBT:27911`, `KACC 41691`, and `KACC:41691`. Exact quoted-token scans for those values found no matching BacDive or StrainInfo snapshot records.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, one exact synonym, and four related synonyms.
- The aggregate GOLD transform supplies a taxon-level organism count of one.
- The local native GOLD snapshot has no organism, sequencing-project, or analysis-project row for taxon ID `1245746`; this is not a YAML defect because the generated taxon-level GOLD count is sourced from `data/raw/gold_organisms.tsv`.
- BacDive and StrainInfo do not supply exact taxon or type-material token matches.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The checks that found no BacDive, StrainInfo, native GOLD, scoped-retired-ID, or generated-record evidence used source-specific exact scans. The `NCBITaxon:356361` absence check included ignored files in the scoped `data/taxa/` search.
- The absence of `nomenclature` is expected for this eukaryotic record because TaxonMech generates nomenclature from LPSN only.
