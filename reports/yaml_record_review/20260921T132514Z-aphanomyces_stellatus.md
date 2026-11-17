# YAML Record Review: Aphanomyces stellatus

## Target

- File: `data/taxa/eukaryota/aphanomyces_stellatus.yaml`
- Identifier: `NCBITaxon:120398`
- Label: `Aphanomyces stellatus`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:100860` / `Aphanomyces`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Sar` -> `Stramenopiles` -> `Oomycota` -> `Saprolegniomycetes` -> `Saprolegniales` -> `Verrucalvaceae` -> `Aphanomyces`
- Existing review report: none found for `*aphanomyces_stellatus.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/aphanomyces_stellatus.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aphanomyces_stellatus.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:120398`, labelled `Aphanomyces stellatus` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:120398` is a `SPECIES` child of `NCBITaxon:100860` / `Aphanomyces`.
- The raw NCBI row has no local synonym or equivalent-name payload for this identifier, matching the absence of a generated `synonyms` block.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aphanomyces stellatus, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:120398`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:120398` and exact label `Aphanomyces stellatus` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:120398`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:120398` with count `2`.
- Exact native GOLD inspection found both organism rows for the same taxon: `Go0572070` / `Aphanomyces stellatus CBS 578.67` and `Go0572535` / `Aphanomyces stellatus CBS 568.67`.
- GOLD organism `Go0572070` has project `Gp0546572` with BioProject `PRJNA551386` and BioSample `SAMN12145847`; GOLD organism `Go0572535` has project `Gp0547147` with BioProject `PRJEB24018` and BioSample `SAMEA104444324`.
- GOLD projects `Gp0546572` and `Gp0547147` are linked to genome analyses `Ga0487936` and `Ga0487902` with GenBank assembly accessions `GCA_009835185.1` and `GCA_900708865.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 2 direct strain rows for `120398`, 0 deposit-only rows, and 0 missing exclusions; both direct IDs, `straininfo.strain:307830` and `straininfo.strain:307848`, are excluded locally as `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `120398`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:120398`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, genetic code, `strain_count`, two source attestations, and generation history.
- There are no synonyms, taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and both exact StrainInfo matches are explicitly excluded.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aphanomyces_stellatus.yaml`; it is generated and validates strictly.
- Preserve the count-consistent two-organism GOLD source attestation and the StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate `straininfo.strain:307830` and `straininfo.strain:307848` and check whether either should contribute to `strain_count`.
- Rerun `just validate data/taxa/eukaryota/aphanomyces_stellatus.yaml` and `just validate-strict data/taxa/eukaryota/aphanomyces_stellatus.yaml` after regenerating the taxon record.

## Additional Notes

- Both native GOLD analyses for `Aphanomyces stellatus` are project-linked through `AP PROJECT GOLD IDS`; neither uses `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
