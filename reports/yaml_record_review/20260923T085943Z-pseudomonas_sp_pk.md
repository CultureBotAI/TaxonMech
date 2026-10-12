# YAML Record Review: Pseudomonas sp. PK

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_pk.yaml
- Started UTC: 2026-09-23T08:57:43Z
- Finished UTC: 2026-09-23T08:59:43Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| identifier | NCBITaxon:100767 |
| label | Pseudomonas sp. PK |
| rank | SPECIES |
| taxon_domain | BACTERIA |
| parent_taxon | NCBITaxon:196821 |
| mapping_status | SEEDED |
| grounding_status | EXACT |
| generated status | Generated from `data/raw/`, `data/atb/`, `data/straininfo/`, and `curation/seed_scope.tsv`; do not hand-edit under `data/taxa/` |

## Validation

| Check | Result |
|---|---|
| Full YAML read | Pass: the whole generated file at `data/taxa/bacteria/pseudomonas_sp_pk.yaml` was read end to end. |
| Prior report search | Pass: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_pk.md'` found no pre-existing report, including ignored report files. |
| Local source search | Pass: exact anchored `rg --no-ignore --hidden` checks across `data/raw/`, `data/atb/`, and `data/straininfo/` found the NCBI and Madin rows for `NCBITaxon:100767` / `Pseudomonas sp. PK`; no same-taxon GTDB, LPSN, BacDive, AllTheBacteria, StrainInfo, GOLD, MediaDive, BactoTraits, or NCBI type-material row was found. |
| `just validate data/taxa/bacteria/pseudomonas_sp_pk.yaml` | Pass: LinkML validation reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/dechloromonas_sp_missr.yaml data/taxa/bacteria/uncultured_hormoscilla_sp.yaml data/taxa/bacteria/pseudomonas_sp_pk.yaml data/taxa/bacteria/companilactobacillus_ginsenosidimutans.yaml` | Pass: closed-schema validation accepted all four records in this batch. |
| `just verify-corpus` | Skipped: this read-only review did not change generated records; earlier full-corpus verification over 625,960 records was clean. |
| `just validate-history` | Skipped: this read-only review did not add a `history/` decision. |
| `just validate-products` | Not applicable: the record has no curator-added `causal_graphs`. |

## Identity and Grounding

The record denotes pinned NCBI species placeholder `NCBITaxon:100767`, with label `Pseudomonas sp. PK`, direct parent `NCBITaxon:196821`, and bacterial genetic code `11` matching `data/raw/ncbitaxon_taxa.tsv:17325`.

The root-first lineage is consistent with the corresponding NCBI inventory chain through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Pseudomonadales`, `Pseudomonadaceae`, `Pseudomonas`, and the no-rank `unclassified Pseudomonas` parent.

No GTDB or nomenclatural overlay changes the seeded NCBI identity.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:17325` supports the identifier, label, rank, parent, bacterial genetic code, raw `ncbitaxon|madin_etal` source set, and `2026-09-13` NCBI snapshot date.
- `data/raw/madin_taxa.tsv:383` supports the Madin source attestation with five `TRAIT_ASSERTION` records.
- The generated `source_attestations` list contains exactly those two expected sources, `NCBITAXON` and `MADIN`.

## Completeness

The generated record is complete for the local evidence. It correctly leaves synonyms, taxonomy mappings, xrefs, nomenclature, strain records, GTDB attestations, AllTheBacteria rows, StrainInfo deposits, MediaDive assertions, GOLD organisms, and BactoTraits assertions absent.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

- External live NCBI and Madin lookups were not used in this environment; the pinned `2026-09-13` local inventories are the reviewed source of truth.
- The prior-report search used `find`, so ignored files under `reports/yaml_record_review/` were included.
