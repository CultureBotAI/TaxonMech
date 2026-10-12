# YAML Record Review: uncultured marine picoplancton S1-005-F-E

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_marine_picoplancton_s1_005_f_e.yaml
- Started UTC: 2026-09-23T14:43:28Z
- Finished UTC: 2026-09-23T14:45:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | TaxonRecord |
| Identifier | NCBITaxon:100916 |
| Label | uncultured marine picoplancton S1-005-F-E |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:150626, marine picoplancton ensemble |
| Maintained input | data/raw/ncbitaxon_taxa.tsv |
| YAML status | Generated from the pinned NCBI inventory |

The target was resolved by the exact `PATHS.tsv` row `NCBITaxon:100916	uncultured_marine_picoplancton_s1_005_f_e` at line 2964. A `find` duplicate check over the ignored `reports/yaml_record_review` directory found no prior `*-uncultured_marine_picoplancton_s1_005_f_e.md` report before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/uncultured_marine_picoplancton_s1_005_f_e.yaml data/taxa/bacteria/exiguobacterium_sp_8_4m1.yaml data/taxa/bacteria/exiguobacterium_sp_8_7m1.yaml data/taxa/bacteria/exiguobacterium_sp_8_7m2.yaml` | Passed: 4 files scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate data/taxa/bacteria/uncultured_marine_picoplancton_s1_005_f_e.yaml` | Passed: `linkml-validate` reported `No issues found`. |
| `just verify-corpus` | Skipped: this read-only review did not change `data/taxa/`, and the earlier full-corpus reproduction check over all 625,960 records was clean. |
| `just validate-history` | Skipped: no append-only `history/` record is created during this read-only review. |
| `just validate-products` | Skipped: this NCBI-only taxon has no `causal_graphs` grounding to validate. |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:17345` exactly supports the generated identifier, label, rank, parent, bacterial genetic code, source, and 2026-09-13 snapshot:

```text
NCBITaxon:100916	uncultured marine picoplancton S1-005-F-E	SPECIES	NCBITaxon:150626	11				ncbitaxon		2026-09-13
```

The YAML record is therefore an exact seeded NCBI Taxonomy record for `NCBITaxon:100916`. Its `taxon_domain: BACTERIA`, `rank: SPECIES`, `grounding_status: EXACT`, and `mapping_status: SEEDED` agree with the local pinned row and with its root-first lineage under `environmental samples` and `marine picoplancton ensemble`.

Live NCBI Taxonomy browser lookup was unavailable in this environment; the committed NCBI snapshot row above was treated as the reproducible source of truth.

## Evidence

The only `source_attestations` entry is:

| Source | Source ID | Source label | Count | Unit |
|---|---|---|---:|---|
| NCBITAXON | NCBITaxon:100916 | uncultured marine picoplancton S1-005-F-E | 1 | NAME |

That attestation is supported by the single exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:17345`. A gitignore-independent source search over `data/raw`, `data/atb`, and `data/straininfo`, including gzip-compressed `.tsv.gz` and `.jsonl.gz` files, found no additional rows for the exact `NCBITaxon:100916` identifier or label, so the absence of ATB, StrainInfo, GTDB, LPSN, BacDive, MediaDive, GOLD, Madin, BactoTraits, genome, nomenclature, and strain attestations is supported by the local source corpus.

## Completeness

This is a minimal NCBI-only environmental-sample species placeholder under `marine picoplancton ensemble`. The empty optional areas are appropriate for the inspected inputs:

| Area | Assessment |
|---|---|
| Lineage | Complete root-first NCBI lineage is present through `NCBITaxon:150626`. |
| Synonyms | Correctly absent; no synonym-bearing source row matched this exact taxon. |
| Nomenclature | Correctly absent; no LPSN row matched this exact taxon. |
| Taxonomy mappings | Correctly absent; no GTDB mapping row matched this exact taxon. |
| Strains and genomes | Correctly absent with `strain_count: 0`; no ATB or StrainInfo row matched this exact taxon. |
| Causal graphs | Correctly absent; no curated mechanism overlay is present for this record. |

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate-strict data/taxa/bacteria/uncultured_marine_picoplancton_s1_005_f_e.yaml` after any source refresh or seeder change that touches this record.
- Re-run `just verify-corpus` after a future curation change to prove this generated YAML still reproduces from `data/raw/`, `data/atb`, `data/straininfo`, and `curation/seed_scope.tsv`.

## Additional Notes

- The no-prior-report check used `find` so ignored Markdown reports in `reports/yaml_record_review` were included.
- The no-auxiliary-source search used `Find.find` rather than a git-aware file list, so ignored files under `data/raw`, `data/atb`, and `data/straininfo` were included.
- `data/raw/bacdive_strains.tsv:25133` has a BacDive source-local ID of `100916`, but that row is for `NCBITaxon:1701`; it is a numeric near miss in a different source namespace and is not evidence for `NCBITaxon:100916`.
