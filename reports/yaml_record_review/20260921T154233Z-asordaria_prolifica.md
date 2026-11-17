# YAML Record Review: Asordaria prolifica

## Target

- File: `data/taxa/eukaryota/asordaria_prolifica.yaml`
- Identifier: `NCBITaxon:303331`
- Label: `Asordaria prolifica`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:266095` / `Asordaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Sordariomycetidae` -> `Sordariales` -> `Sordariaceae` -> `Asordaria`
- Existing review report: none found for `*asordaria_prolifica.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/asordaria_prolifica.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/asordaria_prolifica.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:303331`, labelled `Asordaria prolifica` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:303331` is a `SPECIES` child of `NCBITaxon:266095` / `Asordaria`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Sordaria prolifica`, plus related synonyms `Asordaria prolifica (Cailleux) Arx & Guarro, 1987` and `Sordaria prolifica Cailleux, 1972`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Asordaria prolifica, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:303331`, so the generated current identifier is not represented as merged away in the local raw snapshot.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:303331`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:303331` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0651464`, `Sordaria prolifica MNHN RF-02352`, with strain and culture collection ID `MNHN RF-02352`.
- GOLD organism `Go0651464` has two projects, `Gp0688368` and `Gp0699316`; the first carries BioProject `PRJNA1081091` and BioSample `SAMN40290111`, and the transcriptome project has no BioProject or BioSample in the local snapshot.
- No native GOLD genome analysis rows were linked to `Go0651464` or to either of its projects.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 1 direct strain row for `303331`, already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `303331`.
- Exact `MNHN RF-02352`, `MNHN RF 02352`, `RF-02352`, and `RF 02352` token lookups found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:303331`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the exact StrainInfo row is already excluded, and the native GOLD `MNHN RF-02352` token does not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/asordaria_prolifica.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, count-consistent aggregate/native GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/asordaria_prolifica.yaml` and `just validate-strict data/taxa/eukaryota/asordaria_prolifica.yaml` after regenerating the taxon record.

## Additional Notes

- The exact StrainInfo row is a real source observation for `Asordaria prolifica`: `straininfo.strain:168469` has available `CBS 567.72` deposited under the same taxon. Its exclusion row is consistent with the generated `strain_count: 0` because it has no eligible matched local BacDive own deposit.
- The local native GOLD snapshot has no genome-analysis rows for either `Sordaria prolifica MNHN RF-02352` project; the generated record only attests the same aggregate GOLD organism count already present in `data/raw/gold_organisms.tsv`.
