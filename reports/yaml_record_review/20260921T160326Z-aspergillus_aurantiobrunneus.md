# YAML Record Review: Aspergillus aurantiobrunneus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/aspergillus_aurantiobrunneus.yaml
- Started UTC: 2026-09-21T16:02:30Z
- Finished UTC: 2026-09-21T16:03:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:41725 |
| label | Aspergillus aurantiobrunneus |
| rank | SPECIES |
| taxon_domain | EUKARYOTA |
| parent_taxon | NCBITaxon:2720870 |
| grounding_status | EXACT |
| mapping_status | SEEDED |
| generated status | Generated in `data/taxa/` from committed inventories plus `curation/seed_scope.tsv`; future corrections belong in source extraction, seeding, the scope, or upstream source mappings. |

The target resolves to exactly one generated eukaryotic species record at `data/taxa/eukaryota/aspergillus_aurantiobrunneus.yaml`. It carries NCBI synonyms for the older `Emericella` names, no LPSN nomenclature, no GTDB taxonomy mappings, no BacDive strain entries, no causal graphs, and source attestations from NCBITAXON and GOLD.

## Validation

| Check | Result |
|---|---|
| Prior report check | Pass; `find reports/yaml_record_review -maxdepth 1 -name '*aspergillus_aurantiobrunneus.md' -print` returned no prior report. This search was scoped to the ignored `reports/yaml_record_review/` directory and included ignored report files. |
| Open LinkML validation | Pass; `just validate data/taxa/eukaryota/aspergillus_aurantiobrunneus.yaml` reported `No issues found`. |
| Strict closed-schema validation | Pass; `just validate-strict data/taxa/eukaryota/aspergillus_aurantiobrunneus.yaml` scanned one file with zero ERROR rows and refreshed `reports/instance_validation_failures.tsv`. |
| History validation | Not rerun for this compact generated record; `just validate-history` is a full-history gate and had already passed on the current checkout. |
| Corpus reproduction | Not rerun for this compact generated record; `just verify-corpus` is a full-corpus gate and had already reproduced 625,960 expected records on the current checkout with zero missing, extra, or differing files. |
| Product id-label validation | Not applicable; `just validate-products` only walks curator-added `causal_graphs` nodes, and this generated record has no `causal_graphs`. |

## Identity and Grounding

The YAML identity agrees with `data/raw/ncbitaxon_taxa.tsv`: line 4866 has `NCBITaxon:41725`, label `Aspergillus aurantiobrunneus`, rank `SPECIES`, parent `NCBITaxon:2720870`, genetic code `1`, the two exact synonyms, the three related synonyms, and source `gold`. `curation/seed_scope.tsv` line 52478 keeps this identifier in scope through the attested-source rule, consistent with the generated `SEEDED` status and the `seed_from_sources` history event.

The YAML lineage matches the NCBI inventory parent chain exactly, from `root` through `Eukaryota`, `Fungi`, `Ascomycota`, `Eurotiales`, `Aspergillaceae`, `Aspergillus`, and `Aspergillus subgen. Nidulantes` to `Aspergillus aurantiobrunneus`.

No replacement row was found in `data/raw/ncbi_merged_ids.tsv`, so the record does not need a `replaces` entry.

## Evidence

| Claim | Source check | Assessment |
|---|---|---|
| NCBITaxon identity, rank, parent, genetic code, and synonyms | `data/raw/ncbitaxon_taxa.tsv` line 4866 | Supported exactly. |
| Scope rationale and seeded history | `curation/seed_scope.tsv` line 52478 | Supported exactly: `attested rule: Aspergillus aurantiobrunneus, 2 sources incl. NCBI`. |
| NCBITAXON attestation | NCBI inventory row above | Supported exactly with one name assertion from the 2026-09-13 snapshot. |
| GOLD attestation | `data/raw/gold_organisms.tsv` line 34921 and native `data/gold/organisms.jsonl.gz` row 59797 | Supported exactly with one GOLD organism, `Go0108099`. |
| Empty BacDive strain surface | Exact scan of `data/bacdive/records.jsonl.gz` for taxon IDs `41725` and `NCBITaxon:41725` | Supported; no exact BacDive records were found. |
| Empty StrainInfo overlay | Exact scan of `data/straininfo/records.jsonl.gz` and `data/straininfo/exclusions.tsv` | Supported; six direct NCBI-taxonomy StrainInfo rows exist, and every one is excluded with `no_eligible_own_deposit_match`. |

`data/raw/ncbi_type_material.tsv` has sixteen NCBI type-material rows for designations including `NRRL 4545`, `ATCC 16821`, `CBS 465.65`, `IMI 074897`, `IMI 074897ii`, `IMI 139281`, `LCP 84.2554`, `WB 4545`, and their colon-separated variants. Exact quoted-token scans for those values found no BacDive hits and found only excluded `straininfo.strain:123559`.

## Completeness

The record is complete for the committed source evidence:

- NCBI supplies identity, lineage, genetic code, two exact synonyms, and three related synonyms.
- The aggregate GOLD transform and native GOLD snapshot both support a single organism row for `Aspergillus aurantiobrunneus CBS 465.65`.
- Native GOLD has two sequencing projects for `Go0108099`, but no analysis rows; without a BacDive strain join, these projects do not create TaxonMech strain related records or genome links.
- BacDive has no exact records for the taxon or the checked type-material tokens.
- StrainInfo rows for this NCBI taxon are intentionally excluded before seeding.
- LPSN, GTDB, causal-graph, and curated-evidence sections are correctly empty for the current inventories.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this record.

## Additional Notes

- The empty BacDive and StrainInfo checks used exact scans of the committed gzip JSONL snapshots by NCBI taxon ID and quoted type-material tokens.
- The absence of `nomenclature` is expected for this eukaryotic record because TaxonMech generates nomenclature from LPSN only.
