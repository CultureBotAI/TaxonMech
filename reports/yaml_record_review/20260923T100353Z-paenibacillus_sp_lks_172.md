# YAML Record Review: Paenibacillus sp. LKS-172

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/paenibacillus_sp_lks_172.yaml
- Started UTC: 2026-09-23T10:02:55Z
- Finished UTC: 2026-09-23T10:03:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | Taxon |
| Identifier | NCBITaxon:1008078 |
| Label | Paenibacillus sp. LKS-172 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:185978, `unclassified Paenibacillus` |
| Maintained record | `data/taxa/bacteria/paenibacillus_sp_lks_172.yaml` |
| Source provenance | Seeded from `data/raw/`, `data/atb/`, and `data/straininfo/` inventories |

The record denotes the NCBI species-level Paenibacillus placeholder `NCBITaxon:1008078`.

## Validation

| Check | Result |
| --- | --- |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-paenibacillus_sp_lks_172.md' -print` | Passed before this report was written; `find` includes ignored report files and found no prior report for this stem. |
| `just validate-strict data/taxa/bacteria/paenibacillus_sp_lks_128.yaml data/taxa/bacteria/paenibacillus_sp_lks_167.yaml data/taxa/bacteria/paenibacillus_sp_lks_172.yaml data/taxa/bacteria/paenibacillus_sp_lks_44.yaml` | Passed. |
| `just validate data/taxa/bacteria/paenibacillus_sp_lks_172.yaml` | Passed; reported `No issues found`. |
| `just validate-history` | Skipped; this read-only review did not add a curation decision to `history/`. |
| `just validate-products` | Not applicable; this record has no causal graphs or generated products. |
| `just verify-corpus` | Skipped for this read-only per-record review; an earlier full-corpus verification over 625,960 records was clean. |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv` contains the sole local source row for `NCBITaxon:1008078`, with label `Paenibacillus sp. LKS-172`, species rank, parent `NCBITaxon:185978`, genetic code `11`, source `ncbitaxon`, and 2026-09-13 snapshot date. The YAML identifier, label, rank, bacterial domain, parent, NCBITaxon source attestation, and `EXACT` grounding status all agree with that source row.

The lineage is internally coherent for a Paenibacillus placeholder under `unclassified Paenibacillus`, and the record does not project any synonym, mapping, strain, nomenclature, or cross-reference that would require non-NCBI support.

## Evidence

| Claim | Nearest evidence | Review |
| --- | --- | --- |
| `NCBITaxon:1008078` is labeled `Paenibacillus sp. LKS-172` | `data/raw/ncbitaxon_taxa.tsv` | Supported exactly by the pinned NCBITaxon row. |
| The only source attestation is NCBITAXON | Exact, gitignore-independent searches for `NCBITaxon:1008078` and the tab-anchored label `Paenibacillus sp. LKS-172` across `data/raw`, `data/atb`, and `data/straininfo` found only the NCBITaxon row. | Supported; no auxiliary same-taxon ATB, StrainInfo, GTDB, BacDive, GOLD, or LPSN evidence is present locally. |
| `strain_count: 0` | Absence of same-taxon strain rows in local pinned inventories | Supported; no StrainInfo or ATB strain material was found for this placeholder. |

## Completeness

No consequential source-backed slots are missing. Synonyms, mappings, strain objects, nomenclature, and external database attestations are correctly absent because exact local source searches found only the NCBITaxon placeholder row. The pre-write `find` check also included ignored files and found no pre-existing review report for `paenibacillus_sp_lks_172`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No follow-up is required for this record. If upstream source inventories change, rerun `just validate-strict data/taxa/bacteria/paenibacillus_sp_lks_172.yaml` and `just validate data/taxa/bacteria/paenibacillus_sp_lks_172.yaml` after reseeding.

## Additional Notes

Live source lookups were unavailable during this run, so the pinned local 2026-09-13 NCBITaxon row was treated as the source of truth.
