# YAML Record Review: Aphanomyces euteiches

## Target

- File: `data/taxa/eukaryota/aphanomyces_euteiches.yaml`
- Identifier: `NCBITaxon:100861`
- Label: `Aphanomyces euteiches`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:100860` / `Aphanomyces`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Sar` -> `Stramenopiles` -> `Oomycota` -> `Saprolegniomycetes` -> `Saprolegniales` -> `Verrucalvaceae` -> `Aphanomyces`
- Existing review report: none found for `*aphanomyces_euteiches.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/aphanomyces_euteiches.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aphanomyces_euteiches.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:100861`, labelled `Aphanomyces euteiches` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:100861` is a `SPECIES` child of `NCBITaxon:100860` / `Aphanomyces`.
- The generated synonym block matches the raw NCBI row's equivalent-name payload, `Aphanomyces euteiches Drechsler, 1925`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aphanomyces euteiches, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:100861`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:100861` and exact label `Aphanomyces euteiches` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:100861`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:100861` with count `2`.
- Exact native GOLD inspection found 4 organism rows for the same taxon: `Go0004149`, `Go0022556`, `Go0572490` / `Aphanomyces euteiches ATCC 201684`, and `Go0573226` / `Aphanomyces euteiches pea`.
- The native GOLD snapshot has three linked projects: `Gp0004149`, `Gp0547096` with BioProject `PRJNA551439` and BioSample `SAMN12147934`, and `Gp0547868` with BioProject `PRJEB24016` and BioSample `SAMEA104443621`.
- GOLD projects `Gp0547096` and `Gp0547868` are linked to genome analyses `Ga0487890` and `Ga0664830` with GenBank assembly accessions `GCA_009835175.1` and `GCA_900312765.1`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `100861`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 32 direct strain rows for `100861`, 0 deposit-only rows, and 0 missing exclusions; all 32 direct IDs are excluded locally as `no_eligible_own_deposit_match`.
- Exact source-string inspection found no `ATCC 201684` string in BacDive and one in StrainInfo, at `straininfo.strain:300950`; that same source ID is present in `data/straininfo/exclusions.tsv`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:100861`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and all numeric-tolerant exact StrainInfo matches are explicitly excluded.

## Findings

- **Low - Transformed GOLD count is lower than the native GOLD snapshot.** The generated `GOLD` source attestation mirrors `data/raw/gold_organisms.tsv` at count `2`, but exact native GOLD inspection found 4 organism rows for `ORGANISM NCBI TAX ID = 100861`, including older rows `Go0004149` and `Go0022556`.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aphanomyces_euteiches.yaml`; it is generated and validates strictly.
- Reconcile the transformed GOLD aggregate with the native GOLD snapshot for `NCBITaxon:100861`, either by confirming why `Go0004149` and `Go0022556` are intentionally absent from the transform or by updating `data/raw/gold_organisms.tsv` to match all 4 native organism rows.

## Follow-up Checks

- After any GOLD transform change, rerun an exact native GOLD lookup for NCBI taxon `100861` and confirm whether the generated `GOLD` `assertion_count` should stay at 2 or become 4.
- Rerun `just validate data/taxa/eukaryota/aphanomyces_euteiches.yaml` and `just validate-strict data/taxa/eukaryota/aphanomyces_euteiches.yaml` after regenerating the taxon record.

## Additional Notes

- Both native GOLD analyses for `Aphanomyces euteiches` are project-linked through `AP PROJECT GOLD IDS`; neither uses `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
- StrainInfo stores the `taxon.ncbi` value numerically for `straininfo.strain:300950`, so exact source checks for this taxon should normalize NCBI IDs to strings before comparing them.
