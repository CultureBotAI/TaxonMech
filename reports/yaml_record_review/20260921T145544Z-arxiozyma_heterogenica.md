# YAML Record Review: Arxiozyma heterogenica

## Target

- File: `data/taxa/eukaryota/arxiozyma_heterogenica.yaml`
- Identifier: `NCBITaxon:278026`
- Label: `Arxiozyma heterogenica`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:36906` / `Arxiozyma`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Saccharomycotina` -> `Saccharomycetes` -> `Saccharomycetales` -> `Saccharomycetaceae` -> `Arxiozyma`
- Existing review report: none found for `*arxiozyma_heterogenica.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arxiozyma_heterogenica.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arxiozyma_heterogenica.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:278026`, labelled `Arxiozyma heterogenica` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:278026` is a `SPECIES` child of `NCBITaxon:36906` / `Arxiozyma`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Kazachstania heterogenica` and related synonyms `Arxiozyma heterogenica (Kurtzman & Robnett) Q.M. Wang, Yurkov & Boekhout, 2024`, `Kazachstania heterogenica Kurtzman & Robnett, 2005`, and `Kazachstania sp. SB-2023a`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arxiozyma heterogenica, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old identifier `NCBITaxon:3029323` into `NCBITaxon:278026`; it has no row mapping `NCBITaxon:278026` to another target, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:278026`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:278026`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:278026` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0705434`, `Arxiozyma heterogenica NRRL Y-27499`, with strain and culture collection ID `NRRL Y-27499`.
- GOLD organism `Go0705434` has one project, `Gp0831477`, with BioProject `PRJNA736342` and BioSample `SAMN20341720`; the local native GOLD snapshot has no analysis rows attached directly through `AP ORGANISM GOLD ID` or indirectly through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 2 direct strain rows for `278026` and 2 deposit-only rows, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `278026`.
- `data/raw/ncbi_type_material.tsv` has 15 type-material rows for `NCBITaxon:278026`, covering BCRC/CCRC `22002`, CBS `2675`, DBVPG `7981`, IFO `1897`, NRRL `Y-11611`, and NRRL `Y-27499` spellings.
- Exact BCRC/CCRC/CBS/DBVPG/IFO/NRRL token lookups found 0 BacDive rows and only `straininfo.strain:119221`, one of the same excluded deposit-only StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact and deposit-only StrainInfo rows are already excluded, and the native GOLD `NRRL Y-27499` token does not add an eligible local BacDive or StrainInfo strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arxiozyma_heterogenica.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, type-material evidence, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/arxiozyma_heterogenica.yaml` and `just validate-strict data/taxa/eukaryota/arxiozyma_heterogenica.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD project for `Arxiozyma heterogenica NRRL Y-27499` currently has no matching analysis row in `data/gold/analyses.jsonl.gz`, so there are no GOLD genome accessions to reconcile for this record.
