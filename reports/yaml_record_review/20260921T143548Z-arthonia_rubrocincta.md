# YAML Record Review: Arthonia rubrocincta

## Target

- File: `data/taxa/eukaryota/arthonia_rubrocincta.yaml`
- Identifier: `NCBITaxon:714574`
- Label: `Arthonia rubrocincta`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:39679` / `Arthonia`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `dothideomyceta` -> `Arthoniomycetes` -> `Arthoniales` -> `Arthoniaceae` -> `Arthonia`
- Existing review report: none found for `*arthonia_rubrocincta.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arthonia_rubrocincta.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arthonia_rubrocincta.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:714574`, labelled `Arthonia rubrocincta` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:714574` is a `SPECIES` child of `NCBITaxon:39679` / `Arthonia`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and one related synonym, `Arthonia rubrocincta G. Merr. ex Grube & Lendemer, 2009`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arthonia rubrocincta, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:714574`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:714574`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:714574`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:714574`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:714574` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0102211`, `Arthonia rubrocincta Arru_GBP0182`, strain `Arru_GBP0182`, and no culture collection ID.
- GOLD organism `Go0102211` has one project, `Gp0102211`, with BioProject `PRJNA256244`; the native project row has no BioSample accession.
- No native GOLD analysis rows link to organism `Go0102211` or to project `Gp0102211` through `AP PROJECT GOLD IDS`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct or deposit-only strain rows for `714574`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `714574`.
- An exact `Arru_GBP0182` token lookup found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI matches, and the native GOLD `Arru_GBP0182` token does not add an eligible local strain.
- The absence of `nomenclature` is consistent with the local source inventory: `data/raw/ncbi_type_material.tsv` has no row for this identifier, and generated `nomenclature` entries currently come from LPSN only.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arthonia_rubrocincta.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/arthonia_rubrocincta.yaml` and `just validate-strict data/taxa/eukaryota/arthonia_rubrocincta.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD snapshot has one project for `Arthonia rubrocincta Arru_GBP0182` but no matching genome analysis rows through either `AP ORGANISM GOLD ID` or `AP PROJECT GOLD IDS`.
