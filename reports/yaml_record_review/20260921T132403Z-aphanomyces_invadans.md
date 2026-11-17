# YAML Record Review: Aphanomyces invadans

## Target

- File: `data/taxa/eukaryota/aphanomyces_invadans.yaml`
- Identifier: `NCBITaxon:157072`
- Label: `Aphanomyces invadans`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:100860` / `Aphanomyces`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Sar` -> `Stramenopiles` -> `Oomycota` -> `Saprolegniomycetes` -> `Saprolegniales` -> `Verrucalvaceae` -> `Aphanomyces`
- Existing review report: none found for `*aphanomyces_invadans.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/aphanomyces_invadans.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aphanomyces_invadans.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:157072`, labelled `Aphanomyces invadans` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:157072` is a `SPECIES` child of `NCBITaxon:100860` / `Aphanomyces`.
- The raw NCBI row has no local synonym or equivalent-name payload for this identifier, matching the absence of a generated `synonyms` block.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aphanomyces invadans, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:157072`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:157072` and exact label `Aphanomyces invadans` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:157072`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:157072` with count `2`.
- Exact native GOLD inspection found both organism rows for the same taxon: `Go0037780` / `Aphanomyces invadans NJM9701` and `Go0572326` / `Aphanomyces invadans NJM0002`.
- GOLD organism `Go0037780` has project `Gp0037780` with BioProject `PRJNA188082` and BioSample `SAMN01907307`; GOLD organism `Go0572326` has project `Gp0546908` with BioProject `PRJNA484796` and BioSample `SAMN09769773`.
- GOLD projects `Gp0037780` and `Gp0546908` are linked to genome analyses `Ga0129518` and `Ga0487925` with GenBank assembly accessions `GCA_000520115.1` and `GCA_003546525.1`.
- Exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `157072`; there were therefore 0 local StrainInfo exclusions to account for.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `157072`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:157072`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, genetic code, `strain_count`, two source attestations, and generation history.
- There are no synonyms, taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks.
- The native GOLD organism rows expose only native strain tokens `NJM9701` and `NJM0002` and no `ORGANISM CULTURE COLLECTION ID`, so there is no inspectable local culture-collection token that would be expected to join through the BacDive-derived strain inventory.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aphanomyces_invadans.yaml`; it is generated and validates strictly.
- Preserve the count-consistent two-organism GOLD source attestation when regenerating the record.

## Follow-up Checks

- If a future GOLD refresh adds culture collection identifiers for `Go0037780` or `Go0572326`, check whether any tokens join against BacDive-derived local strain inventory and whether `strain_count` should become nonzero.
- Rerun `just validate data/taxa/eukaryota/aphanomyces_invadans.yaml` and `just validate-strict data/taxa/eukaryota/aphanomyces_invadans.yaml` after regenerating the taxon record.

## Additional Notes

- Both native GOLD analyses for `Aphanomyces invadans` are project-linked through `AP PROJECT GOLD IDS`; neither uses `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
