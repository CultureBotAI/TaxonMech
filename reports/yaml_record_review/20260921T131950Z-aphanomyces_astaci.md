# YAML Record Review: Aphanomyces astaci

## Target

- File: `data/taxa/eukaryota/aphanomyces_astaci.yaml`
- Identifier: `NCBITaxon:112090`
- Label: `Aphanomyces astaci`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:100860` / `Aphanomyces`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Sar` -> `Stramenopiles` -> `Oomycota` -> `Saprolegniomycetes` -> `Saprolegniales` -> `Verrucalvaceae` -> `Aphanomyces`
- Existing review report: none found for `*aphanomyces_astaci.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/aphanomyces_astaci.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aphanomyces_astaci.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:112090`, labelled `Aphanomyces astaci` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:112090` is a `SPECIES` child of `NCBITaxon:100860` / `Aphanomyces`.
- The raw NCBI row has no local synonym or equivalent-name payload for this identifier, matching the absence of a generated `synonyms` block.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aphanomyces astaci, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:112090`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:112090` and exact label `Aphanomyces astaci` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:112090`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:112090` with count `14`.
- Exact native GOLD inspection found all 14 organism rows for the same taxon: `Go0037777` / `APO3`, `Go0384172` / `Pc`, `Go0572327` / `SA`, `Go0572328` / `Kv`, `Go0572329` / `KB13`, `Go0572330` / `FDL457`, `Go0572331` / `197901`, `Go0572332` / `Da`, `Go0572333` / `Si`, `Go0572334` / `Sv`, `Go0572335` / `Yx`, `Go0572336` / `D2`, `Go0572412` / `E`, and `Go0572663` / `Evira4806`.
- The same native GOLD inspection found 14 linked projects and 14 linked genome analyses, including project `Gp0037777` / analysis `Ga0129517` for `APO3`, `Gp0235262` / `Ga0213397` for `Pc`, 10 `PRJNA484796` projects for strains `SA`, `Kv`, `KB13`, `FDL457`, `197901`, `Da`, `Si`, `Sv`, `Yx`, and `D2`, `Gp0547003` / `Ga0487934` for `E`, and `Gp0547293` / `Ga0664762` for `Evira4806`.
- The native GOLD analyses expose GenBank assembly accessions `GCA_000520075.1`, `GCA_002197585.2`, `GCA_003546625.1`, `GCA_003546585.1`, `GCA_003546565.1`, `GCA_003546545.1`, `GCA_003546805.1`, `GCA_003666305.1`, `GCA_003546785.1`, `GCA_003546765.1`, `GCA_009835205.1`, `GCA_003546825.1`, `GCA_003546605.1`, and `GCA_900243735.1`.
- Exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `112090`; there were therefore 0 local StrainInfo exclusions to account for.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `112090`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:112090`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, genetic code, `strain_count`, two source attestations, and generation history.
- There are no synonyms, taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks.
- The 14 native GOLD organism rows expose only native strain tokens and no `ORGANISM CULTURE COLLECTION ID`, so there is no inspectable local culture-collection token that would be expected to join through the BacDive-derived strain inventory.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aphanomyces_astaci.yaml`; it is generated and validates strictly.
- Preserve the count-consistent 14-organism GOLD source attestation when regenerating the record.

## Follow-up Checks

- If a future GOLD refresh adds culture collection identifiers for these 14 organism rows, check whether any tokens join against BacDive-derived local strain inventory and whether `strain_count` should become nonzero.
- Rerun `just validate data/taxa/eukaryota/aphanomyces_astaci.yaml` and `just validate-strict data/taxa/eukaryota/aphanomyces_astaci.yaml` after regenerating the taxon record.

## Additional Notes

- All 14 native GOLD analyses are project-linked through `AP PROJECT GOLD IDS`; none use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
