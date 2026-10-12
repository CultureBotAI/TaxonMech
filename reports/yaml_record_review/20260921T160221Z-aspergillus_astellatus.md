# YAML Record Review: Aspergillus astellatus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_astellatus.yaml
- Started UTC: 2026-09-21T16:00:50Z
- Finished UTC: 2026-09-21T16:02:21Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1810904 |
| label | Aspergillus astellatus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_astellatus.yaml`. It carries NCBI synonyms for older `Aspergillus variecolor var. astellatus` and `Emericella astellata` combinations, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_astellatus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_astellatus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_astellatus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 473461 has `NCBITaxon:1810904`, label `Aspergillus astellatus`, rank `SPECIES`, parent `NCBITaxon:2720870`, genetic code `1`, exact synonyms `Aspergillus variecolor var. astellatus` and `Emericella astellata`, the three generated related synonyms, and source `gold`. `curation/seed_scope.tsv` line 61305 keeps this taxon in scope through the attested-source rule, matching the generated `SEEDED` status.

The YAML lineage matches the NCBI inventory parent chain exactly, from `root` through `Eukaryota`, `Fungi`, `Ascomycota`, `Eurotiales`, `Aspergillaceae`, `Aspergillus`, and `Aspergillus subgen. Nidulantes` to `Aspergillus astellatus`.

`data/raw/ncbi_merged_ids.tsv` line 76709 maps old `NCBITaxon:41733` to `NCBITaxon:1810904`. A literal, gitignore-independent search for `NCBITaxon:41733` across `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, and `curation/seed_scope.tsv` found no retained retired taxon row or scoped/generated path for that old ID. The missing `replaces` field is therefore consistent with `src/taxonmech/seed.py`, which emits replacements from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 473461 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 61305 | Supported exactly: `attested rule: Aspergillus astellatus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 16008 and native `data/gold/organisms.jsonl.gz` row 59796 | Supported exactly with one GOLD organism, `Go0108097`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `1810904` and `NCBITaxon:1810904` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` and `data/straininfo/exclusions.tsv` | Supported; the one direct row and one deposit-only row involving this NCBI taxon are both excluded with `no_eligible_own_deposit_match`. |

`data/raw/ncbi_type_material.tsv` has ten type-material rows for syntype and type-material designations including `NRRL 2396`, `CBS 134.55`, `CBS 261.93`, and composite `WB 2396 = CBS 134.55 = IBT 22589` tokens. Exact quoted-token scans for the component designations found no BacDive hits and found only excluded `straininfo.strain:208590`, whose own strain taxonomy is `Phycomyces blakesleeanus`, not `Aspergillus astellatus`.

## Completeness

The record is complete for the current committed source evidence:

- NCBI supplies identity, lineage, genetic code, two exact synonyms, and three related synonyms.
- The aggregate GOLD transform and native GOLD snapshot both support a single organism row for `Aspergillus astellatus CBS 261.93`.
- Native GOLD has two sequencing projects for `Go0108097`, but no analysis rows; without a BacDive strain join, these project rows do not generate TaxonMech strain related records.
- BacDive has no exact records for the taxon or the checked type-material tokens.
- The StrainInfo rows involving this taxon are excluded before seeding, so no StrainInfo strain, deposit, or sequence links should appear.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive and StrainInfo checks used exact scans of the committed gzip JSONL snapshots by NCBI taxon ID and quoted type-material tokens.
- The absence check for old `NCBITaxon:41733` used `rg --no-ignore --hidden` over the scoped seeding and path files, so ignored files were included.
