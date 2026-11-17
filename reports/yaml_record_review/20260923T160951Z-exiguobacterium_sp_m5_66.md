# YAML Record Review: Exiguobacterium sp. m5_66

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/exiguobacterium_sp_m5_66.yaml
- Started UTC: 2026-09-23T16:09:28Z
- Finished UTC: 2026-09-23T16:09:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | TaxonRecord |
| Identifier | NCBITaxon:1009284 |
| Label | Exiguobacterium sp. m5_66 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:2644629, unclassified Exiguobacterium |
| Maintained input | data/raw/ncbitaxon_taxa.tsv |
| YAML status | Generated from the pinned NCBI inventory |

The target was resolved by the exact `PATHS.tsv` row `NCBITaxon:1009284	exiguobacterium_sp_m5_66` at line 3094. A `find` duplicate check over the ignored `reports/yaml_record_review` directory found no prior `*-exiguobacterium_sp_m5_66.md` report before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/exiguobacterium_sp_m5_64.yaml data/taxa/bacteria/exiguobacterium_sp_m5_65.yaml data/taxa/bacteria/exiguobacterium_sp_m5_66.yaml data/taxa/bacteria/exiguobacterium_sp_m5_67.yaml` | Passed: 4 files scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate data/taxa/bacteria/exiguobacterium_sp_m5_66.yaml` | Passed: `linkml-validate` reported `No issues found`. |
| `just verify-corpus` | Skipped: this read-only review did not change `data/taxa/`, and the earlier full-corpus reproduction check over all 625,960 records was clean. |
| `just validate-history` | Skipped: no append-only `history/` record is created during this read-only review. |
| `just validate-products` | Skipped: this NCBI-only taxon has no `causal_graphs` grounding to validate. |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:211696` exactly supports the generated identifier, label, rank, parent, bacterial genetic code, source, and 2026-09-13 snapshot:

```text
NCBITaxon:1009284	Exiguobacterium sp. m5_66	SPECIES	NCBITaxon:2644629	11				ncbitaxon		2026-09-13
```

The YAML record is therefore an exact seeded NCBI Taxonomy record for `NCBITaxon:1009284`. Its `taxon_domain: BACTERIA`, `rank: SPECIES`, `grounding_status: EXACT`, and `mapping_status: SEEDED` agree with the local pinned row and with its root-first bacterial lineage under `Exiguobacterium`.

Live NCBI Taxonomy browser lookup was unavailable in this environment; the committed NCBI snapshot row above was treated as the reproducible source of truth.

## Evidence

The only `source_attestations` entry is:

| Source | Source ID | Source label | Count | Unit |
|---|---|---|---:|---|
| NCBITAXON | NCBITaxon:1009284 | Exiguobacterium sp. m5_66 | 1 | NAME |

That attestation is supported by the single exact NCBI row at `data/raw/ncbitaxon_taxa.tsv:211696`. A gitignore-independent source search over `data/raw`, `data/atb`, and `data/straininfo`, including gzip-compressed inventories, found no additional rows for the exact NCBI identifier or tab-field anchored label and slug, so the absence of ATB, StrainInfo, GTDB, LPSN, BacDive, MediaDive, GOLD, Madin, BactoTraits, genome, nomenclature, and strain attestations is supported by the local source corpus.

## Completeness

This is a minimal NCBI-only species placeholder under `unclassified Exiguobacterium`. The empty optional areas are appropriate for the inspected inputs:

| Area | Assessment |
|---|---|
| Lineage | Complete root-first NCBI lineage is present through `NCBITaxon:2644629`. |
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

- Re-run `just validate-strict data/taxa/bacteria/exiguobacterium_sp_m5_66.yaml` after any source refresh or seeder change that touches this record.
- Re-run `just verify-corpus` after a future curation change to prove this generated YAML still reproduces from `data/raw/`, `data/atb`, `data/straininfo`, and `curation/seed_scope.tsv`.

## Additional Notes

- The no-prior-report check used `find` so ignored Markdown reports in `reports/yaml_record_review` were included.
- The no-auxiliary-source search used `rg --no-ignore --hidden` for plaintext source inventories and gzip-aware Ruby scans for compressed inventories, so ignored and compressed files under `data/raw`, `data/atb`, and `data/straininfo` were included.
