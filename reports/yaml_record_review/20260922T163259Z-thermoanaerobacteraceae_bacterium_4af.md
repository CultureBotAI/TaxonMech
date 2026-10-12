# YAML Record Review: Thermoanaerobacteraceae bacterium 4AF

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/thermoanaerobacteraceae_bacterium_4af.yaml
- Started UTC: 2026-09-22T16:32:59Z
- Finished UTC: 2026-09-22T16:32:59Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/thermoanaerobacteraceae_bacterium_4af.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003141` / `Thermoanaerobacteraceae bacterium 4AF`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003141`
- Label: `Thermoanaerobacteraceae bacterium 4AF`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:520763` / `unclassified Thermoanaerobacteraceae`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/thermoanaerobacteraceae_bacterium_4af.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/thermoanaerobacteraceae_bacterium_4af.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/bacillus_sp_um96.yaml data/taxa/bacteria/thermoanaerobacteraceae_bacterium_47af.yaml data/taxa/bacteria/thermoanaerobacteraceae_bacterium_4af.yaml data/taxa/bacteria/thermoanaerobacter_sp_18af.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The identity row in `data/raw/ncbitaxon_taxa.tsv` maps `NCBITaxon:1003141` to label `Thermoanaerobacteraceae bacterium 4AF`, rank `SPECIES`, parent `NCBITaxon:520763`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those same identity fields.
- The root-first lineage is internally consistent and reaches `NCBITaxon:520763` through `Bacteria`, `Bacillati`, `Bacillota`, `Clostridia`, `Thermoanaerobacterales`, and `Thermoanaerobacteraceae`. Each checked ancestor had an exact local NCBI source row.
- No synonyms, nomenclature block, GTDB mappings, xrefs, strains, assemblies, or causal graph are asserted, matching the absence of non-NCBI rows for this exact taxon in the reviewed source inventories.

## Evidence

- The single `NCBITAXON` source attestation with `assertion_count: 1` and `assertion_unit: NAME` is supported by the exact NCBI row for `NCBITaxon:1003141`.
- No evidence object points at a sibling or broader taxon.

## Completeness

- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found only the `NCBITaxon:1003141` NCBI row and its `PATHS.tsv` entry for `Thermoanaerobacteraceae bacterium 4AF`; no LPSN, GTDB, BacDive, StrainInfo, trait, medium, GOLD organism, or genome evidence was locally available.
- The empty optional slots are therefore appropriate for a generated NCBI-only record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- If future source snapshots add non-NCBI attestations for `NCBITaxon:1003141`, rerun the taxon generation step that owns `data/taxa/bacteria/thermoanaerobacteraceae_bacterium_4af.yaml`, then rerun `just validate data/taxa/bacteria/thermoanaerobacteraceae_bacterium_4af.yaml` and a strict validation over the regenerated file.
- For a live authority audit beyond the pinned `2026-09-13` snapshot, manually compare current NCBI Taxonomy for `NCBITaxon:1003141` against the local row before changing maintained inputs.

## Additional Notes

- Exact prior-report collision checks used `find reports/yaml_record_review -maxdepth 1` and therefore included ignored report files.
