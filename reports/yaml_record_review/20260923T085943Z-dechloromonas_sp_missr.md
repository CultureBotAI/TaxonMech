# YAML Record Review: Dechloromonas sp. MissR

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/dechloromonas_sp_missr.yaml
- Started UTC: 2026-09-23T08:57:43Z
- Finished UTC: 2026-09-23T08:59:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:100766 |
| label | Dechloromonas sp. MissR |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:2633351 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: the whole generated file at `data/taxa/bacteria/dechloromonas_sp_missr.yaml` was read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-dechloromonas_sp_missr.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact `rg --no-ignore --hidden` checks across `data/raw/`, `data/atb/`, and `data/straininfo/` found only the expected NCBI row for `NCBITaxon:100766` / `Dechloromonas sp. MissR`; no same-taxon GTDB, LPSN, BacDive, AllTheBacteria, StrainInfo, Madin, GOLD, MediaDive, BactoTraits, or NCBI type-material row was found. |
| `just validate data/taxa/bacteria/dechloromonas_sp_missr.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/dechloromonas_sp_missr.yaml data/taxa/bacteria/uncultured_hormoscilla_sp.yaml data/taxa/bacteria/pseudomonas_sp_pk.yaml data/taxa/bacteria/companilactobacillus_ginsenosidimutans.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes pinned NCBI Taxonomy species placeholder `NCBITaxon:100766`. Its label `Dechloromonas sp. MissR`, `SPECIES` rank, direct parent `NCBITaxon:2633351`, and bacterial genetic code `11` match `data/raw/ncbitaxon_taxa.tsv:17324`.

The root-first lineage is internally coherent. It runs through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Betaproteobacteria`, `Rhodocyclales`, `Azonexaceae`, `Dechloromonas`, and the no-rank `unclassified Dechloromonas` parent carried by the pinned NCBI inventory.

No GTDB, LPSN, BacDive, StrainInfo, AllTheBacteria, GOLD, MediaDive, or BactoTraits evidence overlays this NCBI-only identity.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:17324` supports the identifier, label, rank, parent, bacterial genetic code, raw `ncbitaxon` source set, and `2026-09-13` NCBI snapshot date.
- The only generated `source_attestations` item is the one expected `NCBITAXON` name assertion keyed to `NCBITaxon:100766`.
- `strain_count: 0` is consistent with the absence of same-taxon BacDive, StrainInfo, and generated local strain evidence.

## Completeness

The generated record is complete for the pinned local inventory. It needs no synonyms, nomenclature, GTDB mapping, xrefs, child strain entries, descriptions, or deprecation metadata.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- External live NCBI lookups were not used in this environment; the pinned `2026-09-13` local NCBI inventory is the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
