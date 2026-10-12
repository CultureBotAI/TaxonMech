# YAML Record Review: Aspergillus aureoterreus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_aureoterreus.yaml
- Started UTC: 2026-09-21T16:04:59Z
- Finished UTC: 2026-09-21T16:05:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41288 |
| label | Aspergillus aureoterreus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720871 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_aureoterreus.yaml`. It carries NCBI synonyms for `Aspergillus auroterreus` and `Aspergillus terreus var. aureus`, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_aureoterreus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_aureoterreus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_aureoterreus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4791 has `NCBITaxon:41288`, label `Aspergillus aureoterreus`, rank `SPECIES`, parent `NCBITaxon:2720871`, genetic code `1`, exact synonyms `Aspergillus auroterreus` and `Aspergillus terreus var. aureus`, related synonym `Aspergillus aureoterreus Samson, S.W. Peterson, Frisvad & Varga, 2014`, and source `gold`. `curation/seed_scope.tsv` line 52470 keeps the identifier in scope through the attested-source rule, matching the generated `SEEDED` status.

The YAML lineage matches the NCBI inventory parent chain exactly and places this species under `Aspergillus subgen. Circumdati`.

`data/raw/ncbi_merged_ids.tsv` line 31053 maps old `NCBITaxon:1883085` to `NCBITaxon:41288`. A scoped `rg --no-ignore --hidden` search for `NCBITaxon:1883085` across `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and `curation/seed_scope.tsv` found no retained retired taxon row or scoped/generated path, so the raw redirect alone does not require a generated `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4791 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52470 | Supported exactly: `attested rule: Aspergillus aureoterreus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34784 and native `data/gold/organisms.jsonl.gz` row 59864 | Supported exactly with one GOLD organism, `Go0108237`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `41288` and `NCBITaxon:41288` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` and `data/straininfo/exclusions.tsv` | Supported; sixteen direct rows and one deposit-only row involving this NCBI taxon are all excluded with `no_eligible_own_deposit_match`. |

`data/raw/ncbi_type_material.tsv` has seventeen NCBI type-material rows for `CBS 503.65`, `ATCC 16793`, `IFO 30536`, `IMI 082431`, `NRRL 1923`, `QM 7472`, `VKM F-2035`, `WB 1923`, and colon-separated variants. Exact quoted-token scans for those values found no BacDive hits and found only excluded `straininfo.strain:79522`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, two exact synonyms, and one related synonym.
- The aggregate GOLD transform and native GOLD snapshot both support a single organism row for `Aspergillus aureoterreus CBS 503.65`.
- Native GOLD has two sequencing projects for `Go0108237`, but no analysis rows; without a BacDive strain join, these projects do not create TaxonMech strain related records or genome links.
- BacDive has no exact records for the taxon or the checked type-material tokens.
- StrainInfo rows for this taxon are intentionally excluded before seeding.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive and StrainInfo checks used exact scans of the committed gzip JSONL snapshots by NCBI taxon ID and quoted type-material tokens.
- The absence check for old `NCBITaxon:1883085` included ignored files in the scoped seeding and path files.
