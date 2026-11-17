# YAML Record Review: Aphanobasidium pseudotsugae

## Target

- File: `data/taxa/eukaryota/aphanobasidium_pseudotsugae.yaml`
- Identifier: `NCBITaxon:693291`
- Label: `Aphanobasidium pseudotsugae`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:693290` / `Aphanobasidium`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Agaricomycetes` -> `Agaricomycetidae` -> `Agaricales` -> `Pleurotineae` -> `Radulomycetaceae` -> `Aphanobasidium`
- Existing review report: none found for `*aphanobasidium_pseudotsugae.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/aphanobasidium_pseudotsugae.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aphanobasidium_pseudotsugae.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:693291`, labelled `Aphanobasidium pseudotsugae` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:693291` is a `SPECIES` child of `NCBITaxon:693290` / `Aphanobasidium`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonyms `Corticium pseudotsugae`, `Phlebiella pseudotsugae`, and `Xenasma pseudotsugae`, plus related synonyms `Aphanobasidium pseudotsugae (Burt) Boidin & Gilles, 1989` and `Corticium pseudotsugae Burt, 1926`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aphanobasidium pseudotsugae, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:264108` to the current identifier `NCBITaxon:693291`.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:693291` and exact label `Aphanobasidium pseudotsugae` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/merged-ID rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:693291`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:693291` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0411995`, `Aphanobasidium pseudotsugae OMC1630`, strain `OMC1630`, culture collection ID `FBCC 2405`.
- GOLD organism `Go0411995` has two projects: `Gp0306849` with BioProject `PRJNA519428` and BioSample `SAMN10865530`, and `Gp0306850` with BioProject `PRJNA519429` and BioSample `SAMN10865529`.
- GOLD project `Gp0306850` is linked to genome analysis `Ga0265607`; that analysis has an empty `AP GENBANK` list in the native snapshot.
- Exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `693291`; there were therefore 0 local StrainInfo exclusions to account for.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `693291`.
- Exact source-string checks found no `FBCC 2405` or `OMC1630` string in either the local BacDive or StrainInfo JSONL snapshots.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:693291`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks.
- Although GOLD organism `Go0411995` exposes culture collection token `FBCC 2405`, that token is absent from the local BacDive-derived and StrainInfo inventories, so it would not currently be expected to produce a joined strain row.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aphanobasidium_pseudotsugae.yaml`; it is generated and validates strictly.
- Preserve the current NCBI synonyms, old-ID merge context, and count-consistent one-organism GOLD source attestation when regenerating the record.

## Follow-up Checks

- If a future BacDive or StrainInfo refresh adds `FBCC 2405`, check whether GOLD organism `Go0411995` joins against BacDive-derived local strain inventory and whether `strain_count` should become nonzero.
- Rerun `just validate data/taxa/eukaryota/aphanobasidium_pseudotsugae.yaml` and `just validate-strict data/taxa/eukaryota/aphanobasidium_pseudotsugae.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `OMC1630` is project-linked through `AP PROJECT GOLD IDS = Gp0306850`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
