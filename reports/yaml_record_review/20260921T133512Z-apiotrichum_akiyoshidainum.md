# YAML Record Review: Apiotrichum akiyoshidainum

## Target

- File: `data/taxa/eukaryota/apiotrichum_akiyoshidainum.yaml`
- Identifier: `NCBITaxon:279327`
- Label: `Apiotrichum akiyoshidainum`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:105983` / `Apiotrichum`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Tremellomycetes` -> `Trichosporonales` -> `Trichosporonaceae` -> `Apiotrichum`
- Existing review report: none found for `*apiotrichum_akiyoshidainum.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apiotrichum_akiyoshidainum.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apiotrichum_akiyoshidainum.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:279327`, labelled `Apiotrichum akiyoshidainum` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:279327` is a `SPECIES` child of `NCBITaxon:105983` / `Apiotrichum`.
- The generated synonym block matches the raw NCBI row's two equivalent-name payloads, `Apiotrichum akiyoshidainum M. Takash., Kurakado, O. Cho, K. Kikuchi, Sugiy. & Sugita, 2020` and `Trichosporon sp. His14`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apiotrichum akiyoshidainum, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:279327`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:279327` and exact label `Apiotrichum akiyoshidainum` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/type-material rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:279327`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:279327` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0455068`, `Apiotrichum akiyoshidainum HP2023`, strain `HP2023`, culture collection ID `ATCC MYA-4129`.
- GOLD organism `Go0455068` has one project, `Gp0323394`, with BioProject `PRJNA428315` and BioSample `SAMN08287212`.
- GOLD project `Gp0323394` is linked to genome analysis `Ga0655894` with GenBank assembly accession `GCA_002973495.1`.
- Exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `279327`; there were therefore 0 local StrainInfo exclusions to account for.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `279327`.
- Exact source-string checks found no `ATCC MYA-4129` or `HP2023` string in either the local BacDive or StrainInfo JSONL snapshots.
- `data/raw/ncbi_type_material.tsv` has four type-material rows for `NCBITaxon:279327`: duplicate punctuation variants of holotype `JCM 12595` / `JCM:12595` and isotype `CBS 9982` / `CBS:9982`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks.
- Although GOLD organism `Go0455068` exposes culture collection token `ATCC MYA-4129`, that token is absent from the local BacDive-derived and StrainInfo inventories, so it would not currently be expected to produce a joined strain row.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apiotrichum_akiyoshidainum.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, type-material evidence, and count-consistent one-organism GOLD source attestation when regenerating the record.

## Follow-up Checks

- If a future BacDive or StrainInfo refresh adds `ATCC MYA-4129`, check whether GOLD organism `Go0455068` joins against BacDive-derived local strain inventory and whether `strain_count` should become nonzero.
- Rerun `just validate data/taxa/eukaryota/apiotrichum_akiyoshidainum.yaml` and `just validate-strict data/taxa/eukaryota/apiotrichum_akiyoshidainum.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Apiotrichum akiyoshidainum HP2023` is project-linked through `AP PROJECT GOLD IDS = Gp0323394`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
