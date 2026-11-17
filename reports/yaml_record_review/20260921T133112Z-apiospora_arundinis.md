# YAML Record Review: Apiospora arundinis

## Target

- File: `data/taxa/eukaryota/apiospora_arundinis.yaml`
- Identifier: `NCBITaxon:335852`
- Label: `Apiospora arundinis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:1811811` / `Apiospora`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Xylariomycetidae` -> `Amphisphaeriales` -> `Apiosporaceae` -> `Apiospora`
- Existing review report: none found for `*apiospora_arundinis.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apiospora_arundinis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apiospora_arundinis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:335852`, labelled `Apiospora arundinis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:335852` is a `SPECIES` child of `NCBITaxon:1811811` / `Apiospora`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonyms `Arthrinium arundinis` and `Gymnosporium arundinis`, plus related synonyms `Apiospora arundinis (Corda) Pintos & P. Alvarado, 2021`, `Arthrinium arundinis (Corda) Dyko & B. Sutton, 1979`, `Arthrinium sp. MUT 4777`, and `Gymnosporium arundinis Corda, 1838`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apiospora arundinis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:1671125` to the current identifier `NCBITaxon:335852`.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:335852` and exact label `Apiospora arundinis` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/merged-ID rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:335852`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:335852` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0019297`, `Arthrinium arundinis NRRL 25634`, strain and culture collection ID `NRRL 25634`.
- GOLD organism `Go0019297` has one project, `Gp0019297`, with BioProject `PRJNA346435` and BioSample `SAMN05920551`; no native GOLD analysis rows currently link to the organism or project.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 19 direct strain rows for `335852`, 0 deposit-only rows, and 0 missing exclusions; all 19 source IDs are excluded locally as `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `335852`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:335852`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and all exact StrainInfo matches are explicitly excluded.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apiospora_arundinis.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, old-ID merge context, count-consistent one-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If GOLD adds a native analysis row for `Gp0019297`, re-run the native GOLD project-link traversal and check whether downstream assembly metadata should be recorded elsewhere.
- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate the 19 excluded StrainInfo rows for `NCBITaxon:335852` and check whether any should contribute to `strain_count`.
- Rerun `just validate data/taxa/eukaryota/apiospora_arundinis.yaml` and `just validate-strict data/taxa/eukaryota/apiospora_arundinis.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD row still uses the older `Arthrinium arundinis` label from an exact NCBI synonym, but its `ORGANISM NCBI TAX ID` points at the current `Apiospora arundinis` identifier.
- This record has a native GOLD organism with one project but currently no linked rows in `data/gold/analyses.jsonl.gz`; that is an inspectable absence rather than an AP project-link parser miss.
