# YAML Record Review: Apiosordaria backusii

## Target

- File: `data/taxa/eukaryota/apiosordaria_backusii.yaml`
- Identifier: `NCBITaxon:314023`
- Label: `Apiosordaria backusii`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:192815` / `Apiosordaria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Sordariomycetidae` -> `Sordariales` -> `Lasiosphaeriaceae` -> `Apiosordaria`
- Existing review report: none found for `*apiosordaria_backusii.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apiosordaria_backusii.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apiosordaria_backusii.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:314023`, labelled `Apiosordaria backusii` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:314023` is a `SPECIES` child of `NCBITaxon:192815` / `Apiosordaria`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonym `Triangularia backusii` and related synonyms `Apiosordaria backusii (L.H. Huang) Guarro, in Guarro & Cano, 1988` and `Triangularia backusii L.H. Huang, 1975`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apiosordaria backusii, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:2587413` to the current identifier `NCBITaxon:314023`.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:314023` and exact label `Apiosordaria backusii` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/type-material/merged-ID rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:314023`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:314023` with count `2`.
- Exact native GOLD inspection found both organism rows for the same taxon: `Go0358430` / `Apiosordaria backusii CBS 540.89` and `Go0651429` / `Apiosordaria backusii PSN 263`.
- GOLD organism `Go0358430` has projects `Gp0197098` and `Gp0251471`; GOLD organism `Go0651429` has projects `Gp0688333` and `Gp0699289`.
- GOLD project `Gp0197098` is linked to genome analysis `Ga0221888`; that analysis has an empty `AP GENBANK` list in the native snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 3 direct strain rows and 1 deposit-only row for `314023`, with 0 missing exclusions; all four source IDs, `straininfo.strain:122088`, `straininfo.strain:172630`, `straininfo.strain:172631`, and `straininfo.strain:261355`, are excluded locally as `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `314023`.
- `data/raw/ncbi_type_material.tsv` has four type-material rows for `NCBITaxon:314023`: duplicate punctuation variants of `ATCC 28796` / `ATCC:28796` and `CBS 539.89` / `CBS:539.89` under the synonym label `Triangularia backusii`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and all exact StrainInfo matches are explicitly excluded.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apiosordaria_backusii.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym, old-ID merge context, type-material evidence, count-consistent two-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate the four excluded StrainInfo rows for `NCBITaxon:314023` and check whether any should contribute to `strain_count`.
- Rerun `just validate data/taxa/eukaryota/apiosordaria_backusii.yaml` and `just validate-strict data/taxa/eukaryota/apiosordaria_backusii.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `CBS 540.89` is project-linked through `AP PROJECT GOLD IDS = Gp0197098`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
