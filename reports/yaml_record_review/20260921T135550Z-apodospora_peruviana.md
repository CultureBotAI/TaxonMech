# YAML Record Review: Apodospora peruviana

## Target

- File: `data/taxa/eukaryota/apodospora_peruviana.yaml`
- Identifier: `NCBITaxon:516989`
- Label: `Apodospora peruviana`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:516988` / `Apodospora`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Sordariomycetidae` -> `Sordariales` -> `Lasiosphaeriaceae` -> `Apodospora`
- Existing review report: none found for `*apodospora_peruviana.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apodospora_peruviana.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apodospora_peruviana.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:516989`, labelled `Apodospora peruviana` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:516989` is a `SPECIES` child of `NCBITaxon:516988` / `Apodospora`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and one related synonym, `Apodospora peruviana T. Muroi, Udagawa & Y. Otani, 1987`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apodospora peruviana, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:516989`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:516989`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:516989`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:516989` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0358439`, `Apodospora peruviana CBS 118394`, strain and culture collection ID `CBS 118394`.
- GOLD organism `Go0358439` has two projects: `Gp0197116` with BioProject `PRJNA370049` and BioSample `SAMN06296149`, and `Gp0251462` with BioProject `PRJNA442600` and BioSample `SAMN08775307`.
- GOLD project `Gp0197116` is linked to genome analysis `Ga0221526`, whose `AP GENBANK` list is empty in the local native GOLD snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct or deposit-only strain rows for `516989`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `516989`.
- A `CBS 118394` / `CBS118394` token lookup found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:516989` in the local NCBI type-material snapshot.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: neither source has an exact NCBI match, and the GOLD `CBS 118394` token does not join to either local strain source.
- The absence of `nomenclature` is expected for this eukaryotic species because generated `nomenclature` entries currently come from LPSN only, and NCBI has no type-material rows for this taxon in the local raw snapshot.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apodospora_peruviana.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- If GOLD analysis linking changes, recheck whether project `Gp0251462` acquires an analysis and whether `Ga0221526` acquires a GenBank assembly accession.
- Rerun `just validate data/taxa/eukaryota/apodospora_peruviana.yaml` and `just validate-strict data/taxa/eukaryota/apodospora_peruviana.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Apodospora peruviana CBS 118394` is project-linked through `AP PROJECT GOLD IDS = Gp0197116`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
