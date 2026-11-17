# YAML Record Review: Ascodesmis nigricans

## Target

- File: `data/taxa/eukaryota/ascodesmis_nigricans.yaml`
- Identifier: `NCBITaxon:341454`
- Label: `Ascodesmis nigricans`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:47182` / `Ascodesmis`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `Pezizomycetes` -> `Pezizales` -> `Ascodesmidaceae` -> `Ascodesmis`
- Existing review report: none found for `*ascodesmis_nigricans.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascodesmis_nigricans.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascodesmis_nigricans.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:341454`, labelled `Ascodesmis nigricans` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:341454` is a `SPECIES` child of `NCBITaxon:47182` / `Ascodesmis`.
- The generated NCBI synonym block matches the raw NCBI row: it has related synonym `Ascodesmis nigricans Tieghem, 1876`, with no exact synonyms in the snapshot.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascodesmis nigricans, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:341454`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:341454`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:341454`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:341454` with count `2`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0090695`, `Ascodesmis nigricans CBS 389.68`, with strain and culture collection ID `CBS 389.68`.
- GOLD organism `Go0090695` has two projects, `Gp0090695` and `Gp0090696`, with BioProjects `PRJNA247594` and `PRJNA259029` and BioSamples `SAMN02787126` and `SAMN03003362`.
- No native GOLD genome analysis rows were linked to `Go0090695` or to either of its projects.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 10 direct strain rows for `341454`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `341454`.
- Exact `CBS 389.68` / `CBS:389.68` token lookups found 0 BacDive rows and only the same excluded StrainInfo row, `straininfo.strain:162804`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:341454`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the native GOLD `CBS 389.68` token does not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascodesmis_nigricans.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym, count-consistent aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascodesmis_nigricans.yaml` and `just validate-strict data/taxa/eukaryota/ascodesmis_nigricans.yaml` after regenerating the taxon record.

## Additional Notes

- The aggregate GOLD source count of 2 comes from `data/raw/gold_organisms.tsv`; the local native `data/gold/organisms.jsonl.gz` snapshot has one inspectable same-taxon organism row for `341454`. This source-count mismatch is not itself a YAML defect when the aggregate file supports the generated count.
