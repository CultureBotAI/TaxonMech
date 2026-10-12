# YAML Record Review: Lysobacter yananisis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/lysobacter_yananisis.yaml
- Started UTC: 2026-09-22T16:29:34Z
- Finished UTC: 2026-09-22T16:29:34Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/lysobacter_yananisis.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003114` / `Lysobacter yananisis`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003114`
- Label: `Lysobacter yananisis`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:68` / `Lysobacter`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/lysobacter_yananisis.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/lysobacter_yananisis.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/streptomyces_sp_o2vm.yaml data/taxa/bacteria/lysobacter_yananisis.yaml data/taxa/bacteria/acinetobacter_sp_aq_1.yaml data/taxa/bacteria/acinetobacter_sp_aq_2.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The identity row in `data/raw/ncbitaxon_taxa.tsv` maps `NCBITaxon:1003114` to label `Lysobacter yananisis`, rank `SPECIES`, parent `NCBITaxon:68`, genetic code `11`, NCBI related synonyms `"Lysobacter yananisis" Cui et al. 2013` and `Lysobacter sp. SNNU513`, source bundle `ncbitaxon|gtdb|gold`, and snapshot date `2026-09-13`; the YAML carries those same identity fields.
- The root-first lineage is internally consistent and reaches `NCBITaxon:68` through `Bacteria`, `Pseudomonadati`, `Pseudomonadota`, `Gammaproteobacteria`, `Lysobacterales`, and `Lysobacteraceae`. Each checked ancestor had an exact local NCBI source row.
- The GTDB mapping to `GTDB:s__Lysobacter_yananisis` with predicate `skos:closeMatch` and genome count `7` is supported by `data/raw/gtdb_mappings.tsv`; `data/raw/gtdb_species.tsv` also carries genome count `7` for that GTDB species.

## Evidence

- The single GOLD organism attestation is supported by `data/raw/gold_organisms.tsv`.
- Source attestations match the inspected inventory rows: NCBI `1 NAME`, GTDB `7 GENOME`, and GOLD `1 ORGANISM`.
- No unsupported evidence placement, over-scoped source, or mismatched source identifier was found.

## Completeness

- The record correctly leaves causal-graph slots absent; no causal graph was attested in the reviewed raw rows.
- Optional GTDB and GOLD surfaces that have same-taxon evidence are represented.
- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found no LPSN, BacDive, StrainInfo, trait, medium, or genome rows that would require additional blocks for this record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- If upstream `Lysobacter` source inventories are refreshed, rerun the taxon generation step that owns `data/taxa/bacteria/lysobacter_yananisis.yaml`, then rerun `just validate data/taxa/bacteria/lysobacter_yananisis.yaml` and a strict validation over the regenerated file.
- For a live authority audit beyond the pinned `2026-09-13` snapshot, manually compare current NCBI Taxonomy, GTDB, and GOLD pages against the local rows before changing maintained inputs.

## Additional Notes

- `data/raw/gtdb_mappings.tsv` also maps `GTDB:s__Lysobacter_yananisis` broadly to genus `NCBITaxon:69`; the reviewed YAML uses the species-level close match to `NCBITaxon:1003114`.
