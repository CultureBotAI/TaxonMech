# YAML Record Review: Ascoidea rubescens

## Target

- File: `data/taxa/eukaryota/ascoidea_rubescens.yaml`
- Identifier: `NCBITaxon:54195`
- Label: `Ascoidea rubescens`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:27308` / `Ascoidea`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Saccharomycotina` -> `Saccharomycetes` -> `Ascoideales` -> `Ascoideaceae` -> `Ascoidea`
- Existing review report: none found for `*ascoidea_rubescens.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascoidea_rubescens.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascoidea_rubescens.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:54195`, labelled `Ascoidea rubescens` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:54195` is a `SPECIES` child of `NCBITaxon:27308` / `Ascoidea`.
- The generated `genetic_code: 12` matches the raw NCBI genetic-code column for this yeast species.
- The generated NCBI synonym block matches the raw NCBI row: it has related synonym `Ascoidea rubescens Bref., 1891`, with no exact synonyms in the snapshot.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascoidea rubescens, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:54195`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:54195`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:54195`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:54195` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0705338`, `Ascoidea rubescens NRRL Y-17699`, with strain and culture collection ID `NRRL Y-17699`.
- GOLD organism `Go0705338` has one project, `Gp0831374`, with BioProject `PRJNA736342` and BioSample `SAMN20341597`.
- No native GOLD genome analysis rows were linked to `Go0705338` or to its project.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 4 direct strain rows for `54195`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `54195`.
- `data/raw/ncbi_type_material.tsv` has five rows for `NCBITaxon:54195`, covering type material `CBS 116.35`, `CBS:116.35`, `NRRL Y-17699`, `NRRL:Y-17699`, and `NRRL:Y:17699`.
- Exact CBS/NRRL token lookups found 0 BacDive rows and only the same excluded StrainInfo row, `straininfo.strain:152348`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, yeast mitochondrial genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the native GOLD `NRRL Y-17699` token does not add an eligible local BacDive or StrainInfo strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascoidea_rubescens.yaml`; it is generated and validates strictly.
- Preserve the yeast mitochondrial genetic code, NCBI synonym, type-material evidence, count-consistent aggregate/native GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascoidea_rubescens.yaml` and `just validate-strict data/taxa/eukaryota/ascoidea_rubescens.yaml` after regenerating the taxon record.

## Additional Notes

- The local native GOLD snapshot has no genome-analysis row for `Ascoidea rubescens NRRL Y-17699`; the generated record only attests the same aggregate GOLD organism count already present in `data/raw/gold_organisms.tsv`.
