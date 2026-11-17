# YAML Record Review: Pseudomonas fluorescens Wayne1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_fluorescens_wayne1.yaml
- Started UTC: 2026-09-23T08:53:55Z
- Finished UTC: 2026-09-23T08:55:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1007656 |
| label | Pseudomonas fluorescens Wayne1 |
| rank | STRAIN |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:294 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/` and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: all 87 lines of `data/taxa/bacteria/pseudomonas_fluorescens_wayne1.yaml` were read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_fluorescens_wayne1.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact `rg --no-ignore --hidden` checks found the expected NCBI, GTDB, and Madin rows for `NCBITaxon:1007656` across `data/raw/`, `data/atb/`, and `data/straininfo/`. No same-taxon LPSN, BacDive, AllTheBacteria, StrainInfo, or NCBI type-material row was found. |
| `just validate data/taxa/bacteria/pseudomonas_fluorescens_wayne1.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/dechloromonas_sp_nm.yaml data/taxa/bacteria/bacillus_sp_916.yaml data/taxa/bacteria/sphingomonas_sp_sj_1.yaml data/taxa/bacteria/pseudomonas_fluorescens_wayne1.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes pinned NCBI Taxonomy strain `NCBITaxon:1007656`. Its label, `STRAIN` rank, parent `NCBITaxon:294`, NCBI exact strain synonyms, and bacterial genetic code `11` match `data/raw/ncbitaxon_taxa.tsv:211056`.

The root-first lineage through `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Pseudomonadales`, `Pseudomonadaceae`, `Pseudomonas`, `Pseudomonas fluorescens group`, and `Pseudomonas fluorescens` is consistent with the corresponding pinned NCBI inventory rows.

The GTDB overlay is not identity-preserving: `data/raw/gtdb_mappings.tsv:1087` maps the 123-genome species cluster `GTDB:s__Aquipseudomonas_protegens` to this one NCBI strain with `skos:closeMatch`. The same local mapping inventory contains `GTDB:s__Aquipseudomonas_protegens` as a `skos:broadMatch` to parent species `NCBITaxon:294` at `data/raw/gtdb_mappings.tsv:236735`, so projecting the GTDB species label as this strain's exact synonym makes the strain look like an entire species cluster.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:211056` supports the NCBI identifier, label, strain rank, parent, bacterial genetic code, the two NCBI exact synonyms, and raw source list `ncbitaxon|gtdb|madin_etal`.
- `data/raw/madin_taxa.tsv:382` supports the Madin source attestation with one `TRAIT_ASSERTION`.
- `data/raw/gtdb_mappings.tsv:1087` is the maintained input for the currently emitted GTDB taxonomy mapping, exact synonym, xref, and GTDB source attestation.
- The generated `Aquipseudomonas protegens` exact synonym and `GTDB:s__Aquipseudomonas_protegens` xref are over-scoped for a single NCBI strain record.

## Completeness

The NCBI and Madin portions of the record are complete for the pinned local evidence. The only consequential gap is representational: the GTDB species cluster should not be exposed as an exact equivalent of `Pseudomonas fluorescens Wayne1`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | `GTDB:s__Aquipseudomonas_protegens` is projected as a `skos:closeMatch`, exact synonym, xref, and exact-looking source attestation on a single NCBI strain. | `data/raw/gtdb_mappings.tsv:1087` assigns the 123-genome GTDB species cluster to `NCBITaxon:1007656`; the same cluster is broader than parent species `Pseudomonas fluorescens` in `data/raw/gtdb_mappings.tsv:236735`. | `data/raw/gtdb_mappings.tsv` generation and the taxonomy-mapping/synonym projection in `src/taxonmech/seed.py` |

## Recommended Edits

1. Correct the GTDB mapping input so `GTDB:s__Aquipseudomonas_protegens` is not emitted as a close/exact match for strain `NCBITaxon:1007656`, or change the seeder so multi-genome GTDB species clusters mapped to NCBI strains are retained only as non-exact taxonomy evidence.
2. Regenerate `data/taxa/bacteria/pseudomonas_fluorescens_wayne1.yaml` so it drops the `Aquipseudomonas protegens` exact synonym, the `GTDB:s__Aquipseudomonas_protegens` xref, and the GTDB source attestation unless a corrected non-exact mapping remains.

## Follow-up Checks

After the mapping fix, rerun `just seed-canary NCBITaxon:1007656`, inspect `data/taxa/bacteria/pseudomonas_fluorescens_wayne1.yaml`, and rerun `just validate-strict data/taxa/bacteria/pseudomonas_fluorescens_wayne1.yaml`. Also search `data/raw/gtdb_mappings.tsv` for `GTDB:s__Aquipseudomonas_protegens` to verify that close/exact projections are no longer being attached to NCBI strain records.

## Additional Notes

- External live NCBI, GTDB, and Madin lookups were not used in this environment; the pinned `2026-09-13` local inventories are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
