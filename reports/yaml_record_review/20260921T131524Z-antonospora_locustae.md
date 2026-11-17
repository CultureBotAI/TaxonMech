# YAML Record Review: Antonospora locustae

## Target

- File: `data/taxa/eukaryota/antonospora_locustae.yaml`
- Identifier: `NCBITaxon:278021`
- Label: `Antonospora locustae`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:67677` / `Antonospora`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Fungi incertae sedis` -> `Microsporidia` -> `Microsporidia incertae sedis` -> `Antonospora`
- Existing review report: none found for `*antonospora_locustae.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/antonospora_locustae.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/antonospora_locustae.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:278021`, labelled `Antonospora locustae` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:278021` is a `SPECIES` child of `NCBITaxon:67677` / `Antonospora`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonyms `Nosema locustae` and `Paranosema locustae`, plus three authority-bearing related synonyms from the raw equivalent-name column.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Antonospora locustae, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old `NCBITaxon:235221` and `NCBITaxon:33696` to the current identifier `NCBITaxon:278021`.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:278021` and exact label `Antonospora locustae` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope/merged-ID rows, and page index rows for this record. No duplicate review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:278021`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:278021` with count `3`.
- Exact native GOLD inspection found all three organism rows for the same taxon: `Go0002413` / `Nosema (Antonospora) locustae`, `Go0002414` / `Nosema locustae.`, and `Go0591372` / `Antonospora locustae CLX`.
- The native GOLD projects are `Gp0002414` for organism `Go0002414` and `Gp0605318` for organism `Go0591372`; `Gp0605318` carries BioProject `PRJNA353563` and BioSample `SAMN06016424`.
- The current CLX project is linked to genome analysis `Ga0661126`, whose GenBank accessions all use assembly accession `GCA_007674295.1`.
- Exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `278021`; there were therefore 0 local StrainInfo exclusions to account for.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `278021`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:278021`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks.
- None of the three native GOLD organism rows carries an `ORGANISM CULTURE COLLECTION ID`; only `Go0591372` has an `ORGANISM STRAIN` token, `CLX`, so there is no inspectable local culture-collection token that would be expected to join through the BacDive-derived strain inventory.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/antonospora_locustae.yaml`; it is generated and validates strictly.
- Preserve the current NCBI synonyms, old-ID merge context, and count-consistent three-organism GOLD source attestation when regenerating the record.

## Follow-up Checks

- If a future GOLD refresh adds culture collection identifiers for `Go0002413`, `Go0002414`, or `Go0591372`, check whether the tokens join against BacDive-derived local strain inventory and whether `strain_count` should become nonzero.
- Rerun `just validate data/taxa/eukaryota/antonospora_locustae.yaml` and `just validate-strict data/taxa/eukaryota/antonospora_locustae.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Antonospora locustae CLX` is project-linked through `AP PROJECT GOLD IDS = Gp0605318`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
