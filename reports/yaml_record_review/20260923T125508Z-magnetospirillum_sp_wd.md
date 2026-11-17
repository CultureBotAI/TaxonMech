# YAML Record Review: Magnetospirillum sp. WD

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/magnetospirillum_sp_wd.yaml
- Started UTC: 2026-09-23T12:53:26Z
- Finished UTC: 2026-09-23T12:55:08Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:100868` |
| Label | `Magnetospirillum sp. WD` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2617991` `unclassified Magnetospirillum` |
| Status | `grounding_status: EXACT`; `mapping_status: SEEDED` |
| Maintained? | Generated under `data/taxa/`; no direct YAML edit is recommended |

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*magnetospirillum_sp_wd.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/shinella_sp_agr14.yaml data/taxa/bacteria/streptomyces_sp_jau4234.yaml data/taxa/bacteria/magnetospirillum_sp_wd.yaml data/taxa/eukaryota/phytophthora_litchii.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/bacteria/magnetospirillum_sp_wd.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: this record has no `causal_graphs`, and the product id/label gate is only for curator-added graph nodes |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

The NCBI row in `data/raw/ncbitaxon_taxa.tsv:17332` supports the record identifier, label, `SPECIES` rank, `NCBITaxon:2617991` parent, genetic code `11`, the `Dechlorospirillum sp. WD` exact synonym, the `ncbitaxon|madin_etal` source flags, and the `2026-09-13` NCBI snapshot note. `curation/seed_scope.tsv:53619` carries the matching attested-scope row for this exact taxon.

The lineage at `data/taxa/bacteria/magnetospirillum_sp_wd.yaml:6` ends at `NCBITaxon:2617991` `unclassified Magnetospirillum`, agreeing with the NCBI row, and `taxon_domain: BACTERIA` agrees with the `NCBITaxon:2` ancestor.

## Evidence

The NCBI synonym block at `data/taxa/bacteria/magnetospirillum_sp_wd.yaml:39` is exactly the synonym from `data/raw/ncbitaxon_taxa.tsv:17332`. `data/raw/madin_taxa.tsv:397` supports the `MADIN` source attestation count of five trait assertions.

The exact gitignore-independent source search also found `kgmicrobe.strain:bacdive_139937`: `data/raw/bacdive_strains.tsv:62231` names a BacDive strain `WD` with `DSM-21661` but no NCBI classification, `data/raw/strain_genome_records.tsv:34249` stores its IMG genome with `taxon_id: NCBITaxon:100868`, and `data/straininfo/strain_links.tsv:26747` links the deposit to StrainInfo under genus-level `NCBITaxon:13134`. Those rows do not contradict this record and do not establish a missing `strains` entry because TaxonMech keeps strain identity, BacDive classification, and genome-record taxon metadata separate.

## Completeness

The target record is complete for the exact NCBI and MADIN rows currently attached to `NCBITaxon:100868`. The absence of `nomenclature`, `taxonomy_mappings`, BacDive `strains`, ATB genome records, and StrainInfo genome records matches the pinned source rows that have an explicit same-taxon classification.

No curator-added `evidence`, `definition`, `discussions`, or `causal_graphs` are present or required for the seeded identity.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. If BacDive or StrainInfo later gains a direct `NCBITaxon:100868` classification for the `WD` strain, rerun `just seed-canary NCBITaxon:100868`, `just validate data/taxa/bacteria/magnetospirillum_sp_wd.yaml`, `just validate-strict data/taxa/bacteria/magnetospirillum_sp_wd.yaml`, and `just verify-corpus`.

## Additional Notes

Live NCBI, BacDive, and StrainInfo pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
