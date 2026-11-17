# YAML Record Review: Asordaria goundaensis

## Target

- File: `data/taxa/eukaryota/asordaria_goundaensis.yaml`
- Identifier: `NCBITaxon:2082102`
- Label: `Asordaria goundaensis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:266095` / `Asordaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Sordariomycetidae` -> `Sordariales` -> `Sordariaceae` -> `Asordaria`
- Existing review report: none found for `*asordaria_goundaensis.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/asordaria_goundaensis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/asordaria_goundaensis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:2082102`, labelled `Asordaria goundaensis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:2082102` is a `SPECIES` child of `NCBITaxon:266095` / `Asordaria`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonyms `Asordaria goundaensis var. goundaensis` and `Sordaria goundaensis`, plus related synonyms `Asordaria goundaensis (Cailleux) Arx & Guarro, 1987` and `Sordaria goundaensis Cailleux, 1972`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Asordaria goundaensis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has two historical IDs, `NCBITaxon:2082594` and `NCBITaxon:2082595`, both merged into the current `NCBITaxon:2082102` identifier.
- A no-ignore, hidden-file search over the repository for `NCBITaxon:2082102`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merge rows, and the generated page/index rows. Ignored files were included.
- A second no-ignore, hidden-file search over `data/raw`, `data/taxa`, `curation`, and `reports` for the historical merged IDs found only the two local merge rows. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:2082102`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:2082102` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0651466`, `Sordaria goundaensis MNHN RF-02343`, with strain and culture collection ID `MNHN RF-02343`.
- GOLD organism `Go0651466` has two projects, `Gp0688370` and `Gp0699314`; the first carries BioProject `PRJNA1081093` and BioSample `SAMN40290162`, and the transcriptome project has no BioProject or BioSample in the local snapshot.
- No native GOLD genome analysis rows were linked to `Go0651466` or to either of its projects.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 2 direct strain rows for `2082102`, both already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `2082102`.
- Exact `MNHN RF-02343`, `MNHN RF 02343`, `RF-02343`, and `RF 02343` token lookups found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:2082102`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the native GOLD `MNHN RF-02343` token does not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/asordaria_goundaensis.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, count-consistent aggregate/native GOLD source attestation, merge handling, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/asordaria_goundaensis.yaml` and `just validate-strict data/taxa/eukaryota/asordaria_goundaensis.yaml` after regenerating the taxon record.

## Additional Notes

- The two exact StrainInfo rows are independently real source observations for `Asordaria goundaensis`: `straininfo.strain:168466` has available `CBS 564.72` deposited under `Asordaria goundaensis var. goundaensis`, and `straininfo.strain:184388` has available `IMI 337023` deposited under `Sordaria goundaensis`. Their exclusion rows are consistent with the generated `strain_count: 0` because neither has an eligible matched local BacDive own deposit.
- The local native GOLD snapshot has no genome-analysis rows for either `Sordaria goundaensis MNHN RF-02343` project; the generated record only attests the same aggregate GOLD organism count already present in `data/raw/gold_organisms.tsv`.
