# YAML Record Review: Clostridium sp. LKS-AN-9

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/clostridium_sp_lks_an_9.yaml
- Started UTC: 2026-09-23T10:00:40Z
- Finished UTC: 2026-09-23T10:01:37Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | Taxon |
| Identifier | NCBITaxon:1008072 |
| Label | Clostridium sp. LKS-AN-9 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:2614128, `unclassified Clostridium` |
| Maintained record | `data/taxa/bacteria/clostridium_sp_lks_an_9.yaml` |
| Source provenance | Seeded from `data/raw/`, `data/atb/`, and `data/straininfo/` inventories |

The record denotes the NCBI species-level Clostridium placeholder `NCBITaxon:1008072`.

## Validation

| Check | Result |
| --- | --- |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-clostridium_sp_lks_an_9.md' -print` | Passed before this report was written; `find` includes ignored report files and found no prior report for this stem. |
| `just validate-strict data/taxa/bacteria/clostridium_sp_lks_an_9.yaml data/taxa/bacteria/lysinibacillus_sp_lks_151.yaml data/taxa/bacteria/micrococcus_sp_lks_91a.yaml data/taxa/bacteria/paenibacillus_sp_lks_110.yaml` | Passed; scanned 4 files with 0 errors. |
| `just validate data/taxa/bacteria/clostridium_sp_lks_an_9.yaml` | Passed; reported `No issues found`. |
| `just validate-history` | Skipped; this read-only review did not add a curation decision to `history/`. |
| `just validate-products` | Not applicable; this record has no causal graphs or generated products. |
| `just verify-corpus` | Skipped for this read-only per-record review; an earlier full-corpus verification over 625,960 records was clean. |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv` contains the sole local source row for `NCBITaxon:1008072`, with label `Clostridium sp. LKS-AN-9`, species rank, parent `NCBITaxon:2614128`, genetic code `11`, source `ncbitaxon`, and 2026-09-13 snapshot date. The YAML identifier, label, rank, bacterial domain, parent, NCBITaxon source attestation, and `EXACT` grounding status all agree with that source row.

The lineage is internally coherent for a Clostridium placeholder under `unclassified Clostridium`, and the record does not project any synonym, mapping, strain, nomenclature, or cross-reference that would require non-NCBI support.

## Evidence

| Claim | Nearest evidence | Review |
| --- | --- | --- |
| `NCBITaxon:1008072` is labeled `Clostridium sp. LKS-AN-9` | `data/raw/ncbitaxon_taxa.tsv` | Supported exactly by the pinned NCBITaxon row. |
| The only source attestation is NCBITAXON | Exact, gitignore-independent searches for `NCBITaxon:1008072` and the tab-anchored label `Clostridium sp. LKS-AN-9` across `data/raw`, `data/atb`, and `data/straininfo` found only the NCBITaxon row. | Supported; no auxiliary same-taxon ATB, StrainInfo, GTDB, BacDive, GOLD, or LPSN evidence is present locally. |
| `strain_count: 0` | Absence of same-taxon strain rows in local pinned inventories | Supported; no StrainInfo or ATB strain material was found for this placeholder. |

## Completeness

No consequential source-backed slots are missing. Synonyms, mappings, strain objects, nomenclature, and external database attestations are correctly absent because exact local source searches found only the NCBITaxon placeholder row. The pre-write `find` check also included ignored files and found no pre-existing review report for `clostridium_sp_lks_an_9`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No follow-up is required for this record. If upstream source inventories change, rerun `just validate-strict data/taxa/bacteria/clostridium_sp_lks_an_9.yaml` and `just validate data/taxa/bacteria/clostridium_sp_lks_an_9.yaml` after reseeding.

## Additional Notes

Live source lookups were unavailable during this run, so the pinned local 2026-09-13 NCBITaxon row was treated as the source of truth.
