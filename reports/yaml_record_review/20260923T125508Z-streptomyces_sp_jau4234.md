# YAML Record Review: Streptomyces sp. JAU4234

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/streptomyces_sp_jau4234.yaml
- Started UTC: 2026-09-23T12:53:26Z
- Finished UTC: 2026-09-23T12:55:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1008500` |
| Label | `Streptomyces sp. JAU4234` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2593676` `unclassified Streptomyces` |
| Status | `grounding_status: EXACT`; `mapping_status: SEEDED` |
| Maintained? | Generated under `data/taxa/`; no direct YAML edit is recommended |

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*streptomyces_sp_jau4234.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/shinella_sp_agr14.yaml data/taxa/bacteria/streptomyces_sp_jau4234.yaml data/taxa/bacteria/magnetospirillum_sp_wd.yaml data/taxa/eukaryota/phytophthora_litchii.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/bacteria/streptomyces_sp_jau4234.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: this record has no `causal_graphs`, and the product id/label gate is only for curator-added graph nodes |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

The NCBI row in `data/raw/ncbitaxon_taxa.tsv:211411` supports the record identifier, label, `SPECIES` rank, `NCBITaxon:2593676` parent, genetic code `11`, the NCBI-only source flag, and the `2026-09-13` NCBI snapshot note. `curation/seed_scope.tsv:312044` carries the matching attested-scope row.

The lineage at `data/taxa/bacteria/streptomyces_sp_jau4234.yaml:6` ends at `NCBITaxon:2593676` `unclassified Streptomyces`, agreeing with the raw NCBI parent, and `taxon_domain: BACTERIA` agrees with the `NCBITaxon:2` ancestor.

## Evidence

The only source attestation at `data/taxa/bacteria/streptomyces_sp_jau4234.yaml:42` mirrors the exact NCBI row: one name assertion from the `2026-09-13` snapshot.

An exact gitignore-independent search across the auxiliary source rows in `data/raw/`, `data/atb/`, and `data/straininfo/` found no same-taxon LPSN, GTDB, BacDive, GOLD, MediaDive, Madin, BactoTraits, AllTheBacteria, StrainInfo, merged-id, or dropped-source rows for `NCBITaxon:1008500` or `Streptomyces sp. JAU4234`.

## Completeness

The record is complete for an NCBI-only seeded placeholder. `strain_count: 0` is expected, and the absence of `synonyms`, `nomenclature`, `taxonomy_mappings`, `strains`, `evidence`, `definition`, `discussions`, and `causal_graphs` matches the pinned inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. If a future source refresh adds LPSN, GTDB, BacDive, GOLD, ATB, or StrainInfo support for `NCBITaxon:1008500`, rerun `just seed-canary NCBITaxon:1008500`, `just validate data/taxa/bacteria/streptomyces_sp_jau4234.yaml`, `just validate-strict data/taxa/bacteria/streptomyces_sp_jau4234.yaml`, and `just verify-corpus`.

## Additional Notes

Live NCBI pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
