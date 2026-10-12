# YAML Record Review: Aphanomyces cochlioides

## Target

- File: `data/taxa/eukaryota/aphanomyces_cochlioides.yaml`
- Identifier: `NCBITaxon:112091`
- Label: `Aphanomyces cochlioides`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:100860` / `Aphanomyces`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Sar` -> `Stramenopiles` -> `Oomycota` -> `Saprolegniomycetes` -> `Saprolegniales` -> `Verrucalvaceae` -> `Aphanomyces`
- Existing review report: none found for `*aphanomyces_cochlioides.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/aphanomyces_cochlioides.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aphanomyces_cochlioides.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:112091`, labelled `Aphanomyces cochlioides` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:112091` is a `SPECIES` child of `NCBITaxon:100860` / `Aphanomyces`.
- The raw NCBI row has no local synonym or equivalent-name payload for this identifier, matching the absence of a generated `synonyms` block.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aphanomyces cochlioides, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:112091`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:112091` and exact label `Aphanomyces cochlioides` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:112091`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:112091` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0598247`, `Aphanomyces cochlioides 103-1`, strain `103-1`.
- GOLD organism `Go0598247` has one project, `Gp0616673`, with BioProject `PRJNA719397` and BioSample `SAMN18617838`.
- GOLD project `Gp0616673` is linked to genome analysis `Ga0531392` with GenBank assembly accession `GCA_019828595.1`.
- Exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `112091`; there were therefore 0 local StrainInfo exclusions to account for.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `112091`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:112091`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, genetic code, `strain_count`, two source attestations, and generation history.
- There are no synonyms, taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks.
- The native GOLD organism row exposes only strain token `103-1` and no `ORGANISM CULTURE COLLECTION ID`, so there is no inspectable local culture-collection token that would be expected to join through the BacDive-derived strain inventory.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aphanomyces_cochlioides.yaml`; it is generated and validates strictly.
- Preserve the count-consistent one-organism GOLD source attestation when regenerating the record.

## Follow-up Checks

- If a future GOLD refresh adds a culture collection identifier for `Go0598247`, check whether the token joins against BacDive-derived local strain inventory and whether `strain_count` should become nonzero.
- Rerun `just validate data/taxa/eukaryota/aphanomyces_cochlioides.yaml` and `just validate-strict data/taxa/eukaryota/aphanomyces_cochlioides.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Aphanomyces cochlioides 103-1` is project-linked through `AP PROJECT GOLD IDS = Gp0616673`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
