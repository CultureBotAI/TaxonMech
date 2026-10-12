# YAML Record Review: Arachnomyces bostrychodes

## Target

- File: `data/taxa/eukaryota/arachnomyces_bostrychodes.yaml`
- Identifier: `NCBITaxon:2609445`
- Label: `Arachnomyces bostrychodes`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:130040` / `Arachnomyces`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `Eurotiomycetes` -> `Eurotiomycetidae` -> `Onygenales` -> `Arachnomycetaceae` -> `Arachnomyces`
- Existing review report: none found for `*arachnomyces_bostrychodes.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arachnomyces_bostrychodes.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arachnomyces_bostrychodes.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:2609445`, labelled `Arachnomyces bostrychodes` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:2609445` is a `SPECIES` child of `NCBITaxon:130040` / `Arachnomyces`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and two related synonyms, `Arachnomyces bostrychodes Rodr.-Andr., Cano & Stchigel, 2021` and `Arachnomyces sp. ERA-2019b`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arachnomyces bostrychodes, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:2609445`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:2609445`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:2609445`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:2609445` with count `1`.
- Exact native GOLD inspection of `data/gold/organisms.jsonl.gz` found 0 organism rows with `ORGANISM NCBI TAX ID = 2609445`; broader searches for `Arachnomyces`, the target NCBI number, and the NCBI type-material culture tokens also found no matching organism, project, or analysis rows in local `data/gold/*.jsonl.gz`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct or deposit-only strain rows for `2609445`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `2609445`.
- Token lookup for the NCBI holotype cultures `CBS 146926`, `FMR 17685`, and `UTHSCSA DI18-91` found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has 16 type-material rows for `NCBITaxon:2609445`: four punctuation variants each for culture from holotype `CBS 146926`, `FMR 17685`, and `UTHSCSA DI18-91`, plus four punctuation variants for holotype `CBS H-24452`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive, StrainInfo, and native GOLD checks: neither strain source has an exact NCBI match, the NCBI holotype culture tokens do not join to either local strain source, and the aggregate GOLD count has no matching native organism row in the local `data/gold` snapshot.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arachnomyces_bostrychodes.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonyms, type-material evidence, count-consistent aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- If the local native GOLD snapshot is refreshed, recheck whether the aggregate GOLD count for `NCBITaxon:2609445` resolves to a `data/gold/organisms.jsonl.gz` row and whether that row acquires projects or analysis rows.
- Rerun `just validate data/taxa/eukaryota/arachnomyces_bostrychodes.yaml` and `just validate-strict data/taxa/eukaryota/arachnomyces_bostrychodes.yaml` after regenerating the taxon record.

## Additional Notes

- The GOLD source attestation for this generated taxon is supported by the aggregate `data/raw/gold_organisms.tsv` row; the local native GOLD snapshot does not currently contain an inspectable organism row for the same NCBI taxon.
