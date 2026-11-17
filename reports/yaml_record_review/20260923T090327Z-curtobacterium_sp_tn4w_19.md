# YAML Record Review: Curtobacterium sp. TN4W-19

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/curtobacterium_sp_tn4w_19.yaml
- Started UTC: 2026-09-23T09:02:15Z
- Finished UTC: 2026-09-23T09:03:27Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:1007912 |
| label | Curtobacterium sp. TN4W-19 |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:257496 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: the whole generated file at `data/taxa/bacteria/curtobacterium_sp_tn4w_19.yaml` was read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-curtobacterium_sp_tn4w_19.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact anchored `rg --no-ignore --hidden` checks across `data/raw/`, `data/atb/`, and `data/straininfo/` found only the expected NCBI row for `NCBITaxon:1007912` / `Curtobacterium sp. TN4W-19`; no same-taxon GTDB, LPSN, BacDive, AllTheBacteria, StrainInfo, Madin, GOLD, MediaDive, BactoTraits, or NCBI type-material row was found. |
| `just validate data/taxa/bacteria/curtobacterium_sp_tn4w_19.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/verticillium_longisporum.yaml data/taxa/bacteria/chlamydia_trachomatis_rc_l2_55.yaml data/taxa/bacteria/chlamydia_trachomatis_rc_j_971.yaml data/taxa/bacteria/curtobacterium_sp_tn4w_19.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes pinned NCBI species placeholder `NCBITaxon:1007912`, with label `Curtobacterium sp. TN4W-19`, `SPECIES` rank, direct parent `NCBITaxon:257496`, and bacterial genetic code `11` matching `data/raw/ncbitaxon_taxa.tsv:211062`.

The lineage is root-first and reaches the NCBI parent through `Bacteria`, `Bacillati`, `Actinomycetota`, `Actinomycetes`, `Micrococcales`, `Microbacteriaceae`, `Curtobacterium`, and `unclassified Curtobacterium`.

No GTDB, LPSN, BacDive, StrainInfo, AllTheBacteria, GOLD, MediaDive, Madin, or BactoTraits evidence overlays this NCBI-only identity.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:211062` supports the NCBI identifier, label, rank, parent, genetic code, raw `ncbitaxon` source set, and `2026-09-13` snapshot date.
- The only generated `source_attestations` item is the expected one-assertion `NCBITAXON` name attestation.
- `strain_count: 0` is supported by the absence of same-taxon BacDive, StrainInfo, and generated local strain rows.

## Completeness

The generated record is complete for the pinned local source evidence. It needs no taxonomy mappings, synonyms, xrefs, nomenclature, child strains, descriptions, or deprecation metadata.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- External live NCBI lookups were not used in this environment; the pinned `2026-09-13` local NCBI inventory is the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
