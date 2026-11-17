# YAML Record Review: Apiospora esporlensis

## Target

- File: `data/taxa/eukaryota/apiospora_esporlensis.yaml`
- Identifier: `NCBITaxon:2421358`
- Label: `Apiospora esporlensis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:1811811` / `Apiospora`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Xylariomycetidae` -> `Amphisphaeriales` -> `Apiosporaceae` -> `Apiospora`
- Existing review report: none found for `*apiospora_esporlensis.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apiospora_esporlensis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apiospora_esporlensis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:2421358`, labelled `Apiospora esporlensis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:2421358` is a `SPECIES` child of `NCBITaxon:1811811` / `Apiospora`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonym `Arthirnium esporlense`, plus related synonyms `Apiospora esporlensis (Pintos & P. Alvarado) Pintos & P. Alvarado, 2021`, `Arthirnium esporlense Pintos & P. Alvarado, 2019`, and `Arthrinium sp. PA-2018b`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apiospora esporlensis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:2421358`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:2421358` and exact label `Apiospora esporlensis` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/type-material rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:2421358`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:2421358` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0570874`, `Apiospora esporlensis UNIPAMPA010`, strain `UNIPAMPA010`.
- GOLD organism `Go0570874` has two projects, `Gp0543301` with BioProject `PRJNA1080818` and BioSample `SAMN40207477`, and `Gp0543302` with BioProject `PRJNA1305019` and BioSample `SAMN50584310`; no native GOLD analysis rows currently link to either project.
- Exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `2421358`; there were therefore 0 local StrainInfo exclusions to account for.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `2421358`.
- `data/raw/ncbi_type_material.tsv` has six type-material rows for `NCBITaxon:2421358`: duplicate punctuation variants of culture from holotype `CBS 145136` / `CBS:145136`, holotype `MA-Fungi 91727` / `MA:Fungi:91727`, and isotype `AP16717` / `AP:16717`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apiospora_esporlensis.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, type-material evidence, and count-consistent one-organism GOLD source attestation when regenerating the record.

## Follow-up Checks

- If GOLD adds a native analysis row for `Gp0543301` or `Gp0543302`, re-run the native GOLD project-link traversal and check whether downstream assembly metadata should be recorded elsewhere.
- Rerun `just validate data/taxa/eukaryota/apiospora_esporlensis.yaml` and `just validate-strict data/taxa/eukaryota/apiospora_esporlensis.yaml` after regenerating the taxon record.

## Additional Notes

- This record has a native GOLD organism with two projects but currently no linked rows in `data/gold/analyses.jsonl.gz`; that is an inspectable absence rather than an AP project-link parser miss.
