# YAML Record Review: Streptomyces sp. O2VM

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/streptomyces_sp_o2vm.yaml
- Started UTC: 2026-09-22T16:29:34Z
- Finished UTC: 2026-09-22T16:29:34Z
- Verdict: pass

## Target

Reviewed `data/taxa/bacteria/streptomyces_sp_o2vm.yaml`, the generated `TaxonRecord` for `NCBITaxon:1003113` / `Streptomyces sp. O2VM`.

- Class: `TaxonRecord`
- Identifier: `NCBITaxon:1003113`
- Label: `Streptomyces sp. O2VM`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2593676` / `unclassified Streptomyces`
- Maintained owner: source rows under `data/raw/`; do not patch `data/taxa/bacteria/streptomyces_sp_o2vm.yaml` directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/streptomyces_sp_o2vm.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/taxa/bacteria/streptomyces_sp_o2vm.yaml data/taxa/bacteria/lysobacter_yananisis.yaml data/taxa/bacteria/acinetobacter_sp_aq_1.yaml data/taxa/bacteria/acinetobacter_sp_aq_2.yaml` | Passed for the four-file batch with 4 files scanned, 0 files with errors, and 0 total error rows. |
| `just validate-history` | Not run; this is a read-only generated record review and no `history/` decision was added. |
| `just validate-products` | Not applicable; the record has no `causal_graphs` to validate. |

## Identity and Grounding

- The identity row in `data/raw/ncbitaxon_taxa.tsv` maps `NCBITaxon:1003113` to label `Streptomyces sp. O2VM`, rank `SPECIES`, parent `NCBITaxon:2593676`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`; the YAML carries those same identity fields.
- The root-first lineage is internally consistent and reaches `NCBITaxon:2593676` through `Bacteria`, `Bacillati`, `Actinomycetota`, `Actinomycetes`, `Kitasatosporales`, `Streptomycetaceae`, and `Streptomyces`. Each checked ancestor had an exact local NCBI source row.
- No synonyms, nomenclature block, GTDB mappings, xrefs, strains, assemblies, or causal graph are asserted, matching the absence of non-NCBI rows for this exact taxon in the reviewed source inventories.

## Evidence

- The single `NCBITAXON` source attestation with `assertion_count: 1` and `assertion_unit: NAME` is supported by the exact NCBI row for `NCBITaxon:1003113`.
- No evidence object points at a sibling or broader taxon.

## Completeness

- A gitignore-independent exact search with `rg --no-ignore --hidden` over `data/raw`, `data/atb`, and `data/straininfo` plus `data/taxa/PATHS.tsv` found only the `NCBITaxon:1003113` NCBI row and its `PATHS.tsv` entry for `Streptomyces sp. O2VM`; no LPSN, GTDB, BacDive, StrainInfo, trait, medium, GOLD organism, or genome evidence was locally available.
- The empty optional slots are therefore appropriate for a generated NCBI-only record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- If future source snapshots add non-NCBI attestations for `NCBITaxon:1003113`, rerun the taxon generation step that owns `data/taxa/bacteria/streptomyces_sp_o2vm.yaml`, then rerun `just validate data/taxa/bacteria/streptomyces_sp_o2vm.yaml` and a strict validation over the regenerated file.
- For a live authority audit beyond the pinned `2026-09-13` snapshot, manually compare current NCBI Taxonomy for `NCBITaxon:1003113` against the local row before changing maintained inputs.

## Additional Notes

- Exact prior-report collision checks used `find reports/yaml_record_review -maxdepth 1` and therefore included ignored report files.
