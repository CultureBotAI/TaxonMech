# YAML Record Review: Archaeorhizomyces borealis

## Target

- File: `data/taxa/eukaryota/archaeorhizomyces_borealis.yaml`
- Identifier: `NCBITaxon:1472423`
- Label: `Archaeorhizomyces borealis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:1075815` / `Archaeorhizomyces`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `Taphrinomycotina` -> `Archaeorhizomycetes` -> `Archaeorhizomycetales` -> `Archaeorhizomycetaceae` -> `Archaeorhizomyces`
- Existing review report: none found for `*archaeorhizomyces_borealis.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/archaeorhizomyces_borealis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/archaeorhizomyces_borealis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1472423`, labelled `Archaeorhizomyces borealis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1472423` is a `SPECIES` child of `NCBITaxon:1075815` / `Archaeorhizomyces`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and three related synonyms, `Archaeorhizomyces borealis Menkis, T. James & Rosling, 2014`, `Archaeorhizomyces sp. AM-2014`, and `Archaeorhizomyces sp. FG15P2b`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Archaeorhizomyces borealis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps one old identifier, `NCBITaxon:1075839`, into this active target.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:1472423`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material/merge rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1472423`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1472423` with count `1`.
- Exact native GOLD inspection of `data/gold/organisms.jsonl.gz` found 0 organism rows with `ORGANISM NCBI TAX ID = 1472423`; broader searches for `Archaeorhizomyces`, the target NCBI number, and the NCBI holotype tokens also found no matching organism, project, or analysis rows in local `data/gold/*.jsonl.gz`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct or deposit-only strain rows for `1472423`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1472423`.
- Token lookup for the NCBI holotype tokens `CBS 138755`, `NS99-600`, and `UPS F-665323` found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has six type-material rows for `NCBITaxon:1472423`: duplicate punctuation variants of culture from holotype `CBS 138755`, duplicate variants for holotype `NS99-600`, and duplicate variants for holotype `UPS F-665323`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive, StrainInfo, and native GOLD checks: neither strain source has an exact NCBI match, the NCBI holotype tokens do not join to either local strain source, and the aggregate GOLD count has no matching native organism row in the local `data/gold` snapshot.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/archaeorhizomyces_borealis.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonyms, retired-ID merge evidence, type-material evidence, count-consistent aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- If the local native GOLD snapshot is refreshed, recheck whether the aggregate GOLD count for `NCBITaxon:1472423` resolves to a `data/gold/organisms.jsonl.gz` row and whether that row acquires projects or analysis rows.
- Rerun `just validate data/taxa/eukaryota/archaeorhizomyces_borealis.yaml` and `just validate-strict data/taxa/eukaryota/archaeorhizomyces_borealis.yaml` after regenerating the taxon record.

## Additional Notes

- The GOLD source attestation for this generated taxon is supported by the aggregate `data/raw/gold_organisms.tsv` row; the local native GOLD snapshot does not currently contain an inspectable organism row for the same NCBI taxon.
