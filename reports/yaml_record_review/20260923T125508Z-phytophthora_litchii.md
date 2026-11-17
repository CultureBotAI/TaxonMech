# YAML Record Review: Phytophthora litchii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/phytophthora_litchii.yaml
- Started UTC: 2026-09-23T12:53:26Z
- Finished UTC: 2026-09-23T12:55:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:100870` |
| Label | `Phytophthora litchii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4783` `Phytophthora` |
| Status | `grounding_status: EXACT`; `mapping_status: SEEDED` |
| Maintained? | Generated under `data/taxa/`; no direct YAML edit is recommended |

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*phytophthora_litchii.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/shinella_sp_agr14.yaml data/taxa/bacteria/streptomyces_sp_jau4234.yaml data/taxa/bacteria/magnetospirillum_sp_wd.yaml data/taxa/eukaryota/phytophthora_litchii.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/eukaryota/phytophthora_litchii.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: this record has no `causal_graphs`, and the product id/label gate is only for curator-added graph nodes |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

The NCBI row in `data/raw/ncbitaxon_taxa.tsv:17333` supports the record identifier, label, `SPECIES` rank, `NCBITaxon:4783` parent, nuclear genetic code `1`, the exact synonym `Peronophythora litchii`, the two authority-bearing related synonyms, the GOLD source flag, and the `2026-09-13` NCBI snapshot note. `curation/seed_scope.tsv:53620` carries the matching attested-scope row.

The lineage at `data/taxa/eukaryota/phytophthora_litchii.yaml:6` runs through `Eukaryota`, `Stramenopiles`, `Oomycota`, and `Phytophthora`, so `taxon_domain: EUKARYOTA` and the parent agree with the NCBI identity.

## Evidence

The three NCBI synonyms at `data/taxa/eukaryota/phytophthora_litchii.yaml:39` are exactly the exact-synonym and related-synonym pipes from `data/raw/ncbitaxon_taxa.tsv:17333`. `data/raw/gold_organisms.tsv:201` supports the `GOLD` source attestation with one organism filed under `NCBITaxon:100870`.

The neotype and culture-from-neotype values in `data/raw/ncbi_type_material.tsv:681-700` are NCBI type-material rows, not BacDive or LPSN strain rows, so it is expected that they do not appear as `StrainEntry` records.

## Completeness

The record is complete for the NCBI and GOLD rows currently attached to `NCBITaxon:100870`. Exact gitignore-independent searches across `data/atb/`, `data/straininfo/`, and the auxiliary `data/raw/` source files found no same-taxon BacDive, LPSN, GTDB, MediaDive, Madin, BactoTraits, AllTheBacteria, StrainInfo, merged-id, or dropped-source rows.

No curator-added `evidence`, `definition`, `discussions`, or `causal_graphs` are present or required for the seeded identity.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. If a future GOLD, BacDive, or StrainInfo refresh changes support for `NCBITaxon:100870`, rerun `just seed-canary NCBITaxon:100870`, `just validate data/taxa/eukaryota/phytophthora_litchii.yaml`, `just validate-strict data/taxa/eukaryota/phytophthora_litchii.yaml`, and `just verify-corpus`.

## Additional Notes

Live NCBI and GOLD pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
