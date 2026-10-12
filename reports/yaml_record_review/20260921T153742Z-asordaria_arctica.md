# YAML Record Review: Asordaria arctica

## Target

- File: `data/taxa/eukaryota/asordaria_arctica.yaml`
- Identifier: `NCBITaxon:303332`
- Label: `Asordaria arctica`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:266095` / `Asordaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Sordariomycetidae` -> `Sordariales` -> `Sordariaceae` -> `Asordaria`
- Existing review report: none found for `*asordaria_arctica.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/asordaria_arctica.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/asordaria_arctica.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:303332`, labelled `Asordaria arctica` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:303332` is a `SPECIES` child of `NCBITaxon:266095` / `Asordaria`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Sordaria arctica`, plus related synonyms `Asordaria arctica (Cain) Arx & Guarro, 1987` and `Sordaria arctica Cain, 1957`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Asordaria arctica, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:303332`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:303332`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:303332`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:303332` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0583345`, `Asordaria arctica CBS 143.68`, with strain `CBS 143.68` and no culture collection ID.
- GOLD organism `Go0583345` has two projects, `Gp0587285` and `Gp0587286`, with BioProjects `PRJNA1080879` and `PRJNA1360484` and BioSamples `SAMN40207532` and `SAMN53188976`.
- No native GOLD genome analysis rows were linked to `Go0583345` or to either of its projects.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 4 direct strain rows for `303332`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `303332`.
- Exact `CBS 143.68` and `CBS:143.68` token lookups found 0 BacDive rows and only the same excluded StrainInfo row, `straininfo.strain:121557`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:303332`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the native GOLD `CBS 143.68` token does not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/asordaria_arctica.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, count-consistent aggregate/native GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/asordaria_arctica.yaml` and `just validate-strict data/taxa/eukaryota/asordaria_arctica.yaml` after regenerating the taxon record.

## Additional Notes

- The local native GOLD snapshot has no genome-analysis rows for either `Asordaria arctica CBS 143.68` project; the generated record only attests the same aggregate GOLD organism count already present in `data/raw/gold_organisms.tsv`.
