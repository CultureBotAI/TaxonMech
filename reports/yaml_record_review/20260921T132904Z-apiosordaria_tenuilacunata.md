# YAML Record Review: Apiosordaria tenuilacunata

## Target

- File: `data/taxa/eukaryota/apiosordaria_tenuilacunata.yaml`
- Identifier: `NCBITaxon:2074768`
- Label: `Apiosordaria tenuilacunata`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:192815` / `Apiosordaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Sordariomycetidae` -> `Sordariales` -> `Lasiosphaeriaceae` -> `Apiosordaria`
- Existing review report: none found for `*apiosordaria_tenuilacunata.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apiosordaria_tenuilacunata.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apiosordaria_tenuilacunata.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:2074768`, labelled `Apiosordaria tenuilacunata` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:2074768` is a `SPECIES` child of `NCBITaxon:192815` / `Apiosordaria`.
- The generated synonym block matches the raw NCBI row's equivalent-name payload, `Apiosordaria tenuilacunata Guarro, A.T. Martinez & Arx, 1984`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apiosordaria tenuilacunata, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:2074768`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:2074768` and exact label `Apiosordaria tenuilacunata` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:2074768`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:2074768` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0651432`, `Apiosordaria tenuilacunata CBS 629.82`, strain and culture collection ID `CBS 629.82`.
- GOLD organism `Go0651432` has two projects, `Gp0688336` with BioProject `PRJNA1081062` and BioSample `SAMN40290127`, and `Gp0699258` with BioProject `PRJNA1360364` and BioSample `SAMN53188599`; no native GOLD analysis rows currently link to either project.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 3 direct strain rows for `2074768`, 0 deposit-only rows, and 0 missing exclusions; all three source IDs, `straininfo.strain:171134`, `straininfo.strain:171135`, and `straininfo.strain:187466`, are excluded locally as `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `2074768`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:2074768`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and all exact StrainInfo matches are explicitly excluded.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apiosordaria_tenuilacunata.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym, count-consistent one-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If GOLD adds a native analysis row for `Gp0688336` or `Gp0699258`, re-run the native GOLD project-link traversal and check whether downstream assembly metadata should be recorded elsewhere.
- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate the three excluded StrainInfo rows for `NCBITaxon:2074768` and check whether any should contribute to `strain_count`.
- Rerun `just validate data/taxa/eukaryota/apiosordaria_tenuilacunata.yaml` and `just validate-strict data/taxa/eukaryota/apiosordaria_tenuilacunata.yaml` after regenerating the taxon record.

## Additional Notes

- This record has a native GOLD organism with projects but currently no linked rows in `data/gold/analyses.jsonl.gz`; that is an inspectable absence rather than an AP project-link parser miss.
