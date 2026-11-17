# YAML Record Review: Brachybacterium sp. LKS-186

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/brachybacterium_sp_lks_186.yaml
- Started UTC: 2026-09-23T09:53:49Z
- Finished UTC: 2026-09-23T09:54:55Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | Taxon |
| Identifier | NCBITaxon:1008063 |
| Label | Brachybacterium sp. LKS-186 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:2623841, `unclassified Brachybacterium` |
| Maintained record | `data/taxa/bacteria/brachybacterium_sp_lks_186.yaml` |
| Source provenance | Seeded from `data/raw/`, `data/atb/`, and `data/straininfo/` inventories |

The record denotes the NCBI species-level Brachybacterium placeholder `NCBITaxon:1008063`.

## Validation

| Check | Result |
| --- | --- |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-brachybacterium_sp_lks_186.md' -print` | Passed before this report was written; `find` includes ignored report files and found no prior report for this stem. |
| `just validate-strict data/taxa/bacteria/bacillus_sp_lks_b.yaml data/taxa/bacteria/bacillus_sp_lks_c.yaml data/taxa/bacteria/bacillus_sp_lks_d.yaml data/taxa/bacteria/brachybacterium_sp_lks_186.yaml` | Passed. |
| `just validate data/taxa/bacteria/brachybacterium_sp_lks_186.yaml` | Passed; reported `No issues found`. |
| `just validate-history` | Skipped; this read-only review did not add a curation decision to `history/`. |
| `just validate-products` | Not applicable; this record has no causal graphs or generated products. |
| `just verify-corpus` | Skipped for this read-only per-record review; an earlier full-corpus verification over 625,960 records was clean. |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv` contains the sole local source row for `NCBITaxon:1008063`, with label `Brachybacterium sp. LKS-186`, species rank, parent `NCBITaxon:2623841`, genetic code `11`, source `ncbitaxon`, and 2026-09-13 snapshot date. The YAML identifier, label, rank, bacterial domain, parent, NCBITaxon source attestation, and `EXACT` grounding status all agree with that source row.

The lineage is internally coherent for a Brachybacterium placeholder under `unclassified Brachybacterium`, and the record does not project any synonym, mapping, strain, nomenclature, or cross-reference that would require non-NCBI support.

## Evidence

| Claim | Nearest evidence | Review |
| --- | --- | --- |
| `NCBITaxon:1008063` is labeled `Brachybacterium sp. LKS-186` | `data/raw/ncbitaxon_taxa.tsv` | Supported exactly by the pinned NCBITaxon row. |
| The only source attestation is NCBITAXON | Exact, gitignore-independent searches for `NCBITaxon:1008063` and the tab-anchored label `Brachybacterium sp. LKS-186` across `data/raw`, `data/atb`, and `data/straininfo` found only the NCBITaxon row. | Supported; no auxiliary same-taxon ATB, StrainInfo, GTDB, BacDive, GOLD, or LPSN evidence is present locally. |
| `strain_count: 0` | Absence of same-taxon strain rows in local pinned inventories | Supported; no StrainInfo or ATB strain material was found for this placeholder. |

## Completeness

No consequential source-backed slots are missing. Synonyms, mappings, strain objects, nomenclature, and external database attestations are correctly absent because exact local source searches found only the NCBITaxon placeholder row. The pre-write `find` check also included ignored files and found no pre-existing review report for `brachybacterium_sp_lks_186`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No follow-up is required for this record. If upstream source inventories change, rerun `just validate-strict data/taxa/bacteria/brachybacterium_sp_lks_186.yaml` and `just validate data/taxa/bacteria/brachybacterium_sp_lks_186.yaml` after reseeding.

## Additional Notes

Live source lookups were unavailable during this run, so the pinned local 2026-09-13 NCBITaxon row was treated as the source of truth.
