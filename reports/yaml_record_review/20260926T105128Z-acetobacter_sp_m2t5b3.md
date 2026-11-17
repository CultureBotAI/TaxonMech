# YAML Record Review: Acetobacter sp. M2T5B3

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetobacter_sp_m2t5b3.yaml
- Started UTC: 2026-09-26T10:51:28Z
- Finished UTC: 2026-09-26T10:51:28Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | TaxonRecord |
| Identifier | NCBITaxon:682984 |
| Label | Acetobacter sp. M2T5B3 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent taxon | NCBITaxon:2628570 |
| Path | data/taxa/bacteria/acetobacter_sp_m2t5b3.yaml |
| Status | Generated from committed source inventories; generated YAML remains read-only |

The record contains ten lineage entries, one NCBITAXON name attestation, `grounding_status: EXACT`, `mapping_status: SEEDED`, `genetic_code: 11`, and `strain_count: 0`.

## Validation

| Command | Result |
|---|---|
| `just validate data/taxa/bacteria/acetobacter_sp_m2t5b3.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/acetobacter_sp_m2c2.yaml data/taxa/bacteria/acetobacter_sp_m2f_r2a_18.yaml data/taxa/bacteria/acetobacter_sp_m2t5b3.yaml data/taxa/bacteria/acetobacter_sp_m3t1b3.yaml` | Pass; scanned four files with zero files with ERROR and zero total ERROR rows. |

No product-term validator was needed: this record has no curator-added causal-graph nodes. No separate history validator was needed: this review did not add a sidecar history record.

## Identity and Grounding

- The target resolved uniquely through `data/taxa/PATHS.tsv`: `NCBITaxon:682984` maps to `acetobacter_sp_m2t5b3`.
- `data/raw/ncbitaxon_taxa.tsv:160356` carries `NCBITaxon:682984`, label `Acetobacter sp. M2T5B3`, rank `SPECIES`, parent `NCBITaxon:2628570`, genetic code `11`, attested source `ncbitaxon`, and taxonomy snapshot `2026-09-13`.
- The bounded raw scan found all ten lineage IDs in `data/raw/ncbitaxon_taxa.tsv` and found no lineage label or rank mismatches.
- The record's `EXACT` grounding is defensible because the record identifier is the source NCBI identifier and the label/rank/parent/genetic-code fields are copied from the matching NCBI inventory row.
- `curation/seed_scope.tsv:267373` keeps this identifier in scope with the reason `attested rule: Acetobacter sp. M2T5B3, 1 sources incl. NCBI`, matching the record's single NCBITAXON attestation.

## Evidence

- Supported: the NCBI identity, species rank, parent taxon, Bacteria domain through the NCBI lineage, and genetic code are backed by the exact `data/raw/ncbitaxon_taxa.tsv` row.
- Supported: the single `source_attestations` entry is backed by the same raw row's `attested_by: ncbitaxon`, and its count of one reflects one upstream NCBI name assertion for the target.
- Supported absence: a gitignore-independent exact scan for the full NCBI identifier and label across `data/raw`, `data/catalog`, `data/bacdive`, `data/gold`, `data/atb`, `data/straininfo`, `curation`, and `history` found only the NCBI inventory row and the scope row. The bounded scan also found zero target rows in BacDive strains, culture-collection strains, strain assemblies, strain genome records, strain related records, StrainInfo direct/deposit/assembly/exclusion/related-record sources, LPSN names, GTDB species, GTDB mappings, Madin, BactoTraits, MediaDive, GOLD aggregates, and native GOLD organism/project/analysis snapshots.
- No unsupported or over-scoped claims were found.
- No citation or quoted-snippet mismatches were present; the record has no literature citations.

## Completeness

- Complete for seeded NCBI support: identity, rank, parent, lineage, genetic code, grounding status, mapping status, source attestation, and seed history are present.
- Correctly empty: `synonyms`, `nomenclature`, `taxonomy_mappings`, `xrefs`, `strains`, `definitions`, and `causal_graphs` are absent because no inspected source row or compressed native-source scan exposed matching evidence for this NCBI identifier.
- The record's `strain_count: 0` agrees with the absence of BacDive, StrainInfo, culture-collection, genome, and related-record rows for the target.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

None required for this record. Re-run `just validate`, `just validate-strict`, the exact ignored-inclusive source search, and the bounded compressed-source scan after any source inventory refresh that mentions `NCBITaxon:682984`.

## Additional Notes

- Duplicate-report preflight used `find reports/yaml_record_review -maxdepth 1 -name '*-acetobacter_sp_m2t5b3.md' -print`, which includes the ignored `reports/` tree and found no existing report for this exact record stem before this file was written.
- The generated YAML is not the maintained owner for future biological corrections. A future fix would belong in the source inventories, the seeder, or `curation/seed_scope.tsv`, depending on the failing evidence.
