# YAML Record Review: Antrodiella citrinella

## Target

- File: `data/taxa/eukaryota/antrodiella_citrinella.yaml`
- Identifier: `NCBITaxon:2447956`
- Label: `Antrodiella citrinella`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:81041` / `Antrodiella`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetes incertae sedis` -> `Polyporales` -> `Steccherinaceae` -> `Antrodiella`
- Existing review report: none found for `*antrodiella_citrinella.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/antrodiella_citrinella.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/antrodiella_citrinella.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:2447956`, labelled `Antrodiella citrinella` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:2447956` is a `SPECIES` child of `NCBITaxon:81041` / `Antrodiella`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonym `Flaviporus citrinellus` and related synonyms `Antrodiella citrinella Niemela & Ryvarden, 1983` and `Flaviporus citrinellus (Niemel & Ryvarden) Ginns, 1984`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Antrodiella citrinella, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:92698` to the current identifier `NCBITaxon:2447956`.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:2447956` and exact label `Antrodiella citrinella` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/merged-ID rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:2447956`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:2447956` with count `3`.
- Exact native GOLD inspection found all three organism rows for the same taxon: `Go0515930` / `Antrodiella citrinella FBCC 969`, `Go0516829` / `Antrodiella citrinella OMC 1724`, and `Go0519078` / `Antrodiella citrinella sv. SBUG-M 1723 DSM 108506`.
- The three native GOLD projects are `Gp0436688`, `Gp0440429`, and `Gp0443213`; those rows carry BioProject accessions `PRJNA654235`, `PRJNA654101`, and `PRJNA517448`.
- GOLD project `Gp0443213` is linked to genome analysis `Ga0415495` with GenBank assembly accession `GCA_004802725.1`.
- Exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `2447956`; there were therefore 0 local StrainInfo exclusions to account for.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `2447956`.
- Exact source-string checks found no `DSM 108506` or `SBUG-M 1723` string in either the local BacDive or StrainInfo JSONL snapshots.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:2447956`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks.
- Although GOLD organism `Go0519078` exposes culture collection token `DSM 108506`, that token is absent from the local BacDive-derived and StrainInfo inventories, so it would not currently be expected to produce a joined strain row.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/antrodiella_citrinella.yaml`; it is generated and validates strictly.
- Preserve the current NCBI synonyms, old-ID merge context, and count-consistent three-organism GOLD source attestation when regenerating the record.

## Follow-up Checks

- If a future BacDive or StrainInfo refresh adds `DSM 108506`, check whether GOLD organism `Go0519078` joins against BacDive-derived local strain inventory and whether `strain_count` should become nonzero.
- Rerun `just validate data/taxa/eukaryota/antrodiella_citrinella.yaml` and `just validate-strict data/taxa/eukaryota/antrodiella_citrinella.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for the `SBUG-M 1723 DSM 108506` row is project-linked through `AP PROJECT GOLD IDS = Gp0443213`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
