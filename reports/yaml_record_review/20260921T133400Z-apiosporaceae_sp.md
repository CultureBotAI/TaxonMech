# YAML Record Review: Apiosporaceae sp.

## Target

- File: `data/taxa/eukaryota/apiosporaceae_sp.yaml`
- Identifier: `NCBITaxon:1933422`
- Label: `Apiosporaceae sp.`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:338724` / `unclassified Apiosporaceae`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Xylariomycetidae` -> `Amphisphaeriales` -> `Apiosporaceae` -> `unclassified Apiosporaceae`
- Existing review report: none found for `*apiosporaceae_sp.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apiosporaceae_sp.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apiosporaceae_sp.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species-level placeholder `NCBITaxon:1933422`, labelled `Apiosporaceae sp.` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1933422` is a `SPECIES` child of the no-rank node `NCBITaxon:338724` / `unclassified Apiosporaceae`.
- The raw NCBI row has no local synonym or equivalent-name payload for this identifier, matching the absence of a generated `synonyms` block.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apiosporaceae sp., 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1933422`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:1933422` and exact label `Apiosporaceae sp.` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1933422`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1933422` with count `3`.
- Exact native GOLD inspection found 2 organism rows for the same taxon: `Go0705814` / `Apiosporaceae sp. Myco 0061` and `Go0705815` / `Apiosporaceae sp. UCDMyco 010 3.1`.
- GOLD organisms `Go0705814` and `Go0705815` have projects `Gp0832273` and `Gp0832274`; no native GOLD analysis rows currently link to either organism or project.
- Exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `1933422`; there were therefore 0 local StrainInfo exclusions to account for.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1933422`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:1933422`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, genetic code, `strain_count`, two source attestations, and generation history.
- There are no synonyms, taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks.
- The 2 native GOLD organism rows expose only native strain tokens and no `ORGANISM CULTURE COLLECTION ID`, so there is no inspectable local culture-collection token that would be expected to join through the BacDive-derived strain inventory.

## Findings

- **Low - Transformed GOLD count is higher than the native GOLD snapshot.** The generated `GOLD` source attestation mirrors `data/raw/gold_organisms.tsv` at count `3`, but exact native GOLD inspection found 2 organism rows for `ORGANISM NCBI TAX ID = 1933422`.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apiosporaceae_sp.yaml`; it is generated and validates strictly.
- Reconcile the transformed GOLD aggregate with the native GOLD snapshot for `NCBITaxon:1933422`, either by confirming why one native organism row is absent from the current local snapshot or by updating the transformed aggregate to match the 2 native organism rows.

## Follow-up Checks

- After any GOLD transform or snapshot refresh, rerun an exact native GOLD lookup for NCBI taxon `1933422` and confirm whether the generated `GOLD` `assertion_count` should stay at 3 or become 2.
- Rerun `just validate data/taxa/eukaryota/apiosporaceae_sp.yaml` and `just validate-strict data/taxa/eukaryota/apiosporaceae_sp.yaml` after regenerating the taxon record.

## Additional Notes

- This record has native GOLD organisms with projects but currently no linked rows in `data/gold/analyses.jsonl.gz`; that is an inspectable absence rather than an AP project-link parser miss.
