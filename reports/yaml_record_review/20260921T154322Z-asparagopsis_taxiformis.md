# YAML Record Review: Asparagopsis taxiformis

## Target

- File: `data/taxa/eukaryota/asparagopsis_taxiformis.yaml`
- Identifier: `NCBITaxon:260499`
- Label: `Asparagopsis taxiformis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:31366` / `Asparagopsis`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Rhodophyta` -> `Florideophyceae` -> `Rhodymeniophycidae` -> `Bonnemaisoniales` -> `Bonnemaisoniaceae` -> `Asparagopsis`
- Existing review report: none found for `*asparagopsis_taxiformis.md` under the ignored `reports/yaml_record_review/` tree. A no-ignore, hidden-file search over `reports/yaml_record_review/` for `asparagopsis_taxiformis` also found no existing report body that mentioned this slug; ignored files were included.

## Validation

- `just validate data/taxa/eukaryota/asparagopsis_taxiformis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/asparagopsis_taxiformis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:260499`, labelled `Asparagopsis taxiformis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:260499` is a `SPECIES` child of `NCBITaxon:31366` / `Asparagopsis`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonym `Fucus taxiformis`, plus related synonyms `Asparagopsis taxiformis (Delile) Trevisan de Saint-Leon, 1845` and `Fucus taxiformis Delile, 1813`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Asparagopsis taxiformis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:260499`, so the generated current identifier is not represented as merged away in the local raw snapshot.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:260499`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:260499` with count `1`.
- Exact native GOLD inspection found 0 organism rows, 0 project rows, and 0 analysis rows for `260499` in the local `data/gold/*.jsonl.gz` snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `260499`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `260499`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:260499`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, NCBITaxon and GOLD source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact local match, and the local native GOLD snapshot has no visible strain or culture collection tokens for this taxon.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/asparagopsis_taxiformis.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/asparagopsis_taxiformis.yaml` and `just validate-strict data/taxa/eukaryota/asparagopsis_taxiformis.yaml` after regenerating the taxon record.

## Additional Notes

- The local native GOLD snapshot has no inspectable organism row for `NCBITaxon:260499`; the generated record only attests the aggregate GOLD organism count already present in `data/raw/gold_organisms.tsv`.
