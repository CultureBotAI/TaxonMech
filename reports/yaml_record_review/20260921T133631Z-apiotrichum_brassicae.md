# YAML Record Review: Apiotrichum brassicae

## Target

- File: `data/taxa/eukaryota/apiotrichum_brassicae.yaml`
- Identifier: `NCBITaxon:82513`
- Label: `Apiotrichum brassicae`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:105983` / `Apiotrichum`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Tremellomycetes` -> `Trichosporonales` -> `Trichosporonaceae` -> `Apiotrichum`
- Existing review report: none found for `*apiotrichum_brassicae.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apiotrichum_brassicae.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apiotrichum_brassicae.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:82513`, labelled `Apiotrichum brassicae` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:82513` is a `SPECIES` child of `NCBITaxon:105983` / `Apiotrichum`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonym `Trichosporon brassicae` and related synonyms `Apiotrichum brassicae (Nakase) A.M. Yurkov & Boekhout, 2015` and `Trichosporon brassicae Nakase, 1971`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apiotrichum brassicae, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:82513`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:82513` and exact label `Apiotrichum brassicae` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/type-material rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:82513`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:82513` with count `2`.
- Exact native GOLD inspection found both organism rows for the same taxon: `Go0138927` / `Apiotrichum brassicae JCM 1599` and `Go0657699` / `Apiotrichum brassicae M2204`.
- GOLD organism `Go0138927` has project `Gp0143984` with BioProject `PRJDB3695` and BioSample `SAMD00028416`; GOLD organism `Go0657699` has project `Gp0701967` with BioProject `PRJNA833221` and BioSample `SAMN27964161`.
- GOLD projects `Gp0143984` and `Gp0701967` are linked to genome analyses `Ga0131312` and `Ga0663788` with GenBank assembly accessions `GCA_001600295.1` and `GCA_023628095.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 4 direct strain rows for `82513`, 0 deposit-only rows, and 0 missing exclusions; all four source IDs, `straininfo.strain:63267`, `straininfo.strain:236773`, `straininfo.strain:313251`, and `straininfo.strain:340522`, are excluded locally as `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `82513`.
- `data/raw/ncbi_type_material.tsv` has 17 type-material rows for `NCBITaxon:82513` under the synonym label `Trichosporon brassicae`, including duplicate punctuation variants for `CBS 6382`, `AJ 4833`, `ATCC 24124`, `CCRC 21783`, `IFO 1584`, `JCM 1599`, `NCYC 2562`, and `UAMH 7657`, plus a `BCRC:21783` row.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and all exact StrainInfo matches are explicitly excluded.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apiotrichum_brassicae.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, type-material evidence, count-consistent two-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate the four excluded StrainInfo rows for `NCBITaxon:82513` and check whether any should contribute to `strain_count`.
- Rerun `just validate data/taxa/eukaryota/apiotrichum_brassicae.yaml` and `just validate-strict data/taxa/eukaryota/apiotrichum_brassicae.yaml` after regenerating the taxon record.

## Additional Notes

- Both native GOLD analyses for `Apiotrichum brassicae` are project-linked through `AP PROJECT GOLD IDS`; neither uses `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
