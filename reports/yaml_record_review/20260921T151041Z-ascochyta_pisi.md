# YAML Record Review: Ascochyta pisi

## Target

- File: `data/taxa/eukaryota/ascochyta_pisi.yaml`
- Identifier: `NCBITaxon:749586`
- Label: `Ascochyta pisi`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:5453` / `Ascochyta`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `dothideomyceta` -> `Dothideomycetes` -> `Pleosporomycetidae` -> `Pleosporales` -> `Pleosporineae` -> `Didymellaceae` -> `Ascochyta`
- Existing review report: none found for `*ascochyta_pisi.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascochyta_pisi.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascochyta_pisi.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:749586`, labelled `Ascochyta pisi` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:749586` is a `SPECIES` child of `NCBITaxon:5453` / `Ascochyta`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonyms `Ascochyta pisi var. pisi` and `Didymella pisi`, plus related synonyms `Ascochyta pisi Libert, 1830` and `Didymella pisi M.I. Chilvers, J.D. Rogers & T.L. Peever 2009`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascochyta pisi, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old identifiers `NCBITaxon:47971` and `NCBITaxon:487625` into `NCBITaxon:749586`; it has no row mapping `NCBITaxon:749586` to another target, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:749586`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:749586`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:749586` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0676799`, `Ascochyta pisi CBS 122785`, with strain `CBS 122785` and culture collection ID `CBS:122785`.
- GOLD organism `Go0676799` has one project, `Gp0778604`, with BioProject `PRJNA827019` and BioSample `SAMN27594410`.
- GOLD project `Gp0778604` is linked to genome analysis `Ga0664202` with GenBank assembly accession `GCA_026119825.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 25 direct strain rows for `749586`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `749586`.
- `data/raw/ncbi_type_material.tsv` has seven rows for `NCBITaxon:749586`, covering culture-from-epitype `CBS 122785`, `CBS:122785`, `ICMP:6893`, `PD 78/517`, `PD:78/517`, and epitype `HMAS 246705` / `HMAS:246705`.
- Exact CBS/ICMP/PD/HMAS epitype-token lookups found 0 BacDive rows and only the same excluded StrainInfo row, `straininfo.strain:223431`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the native GOLD `CBS 122785` token does not add an eligible local BacDive or StrainInfo strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascochyta_pisi.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym split, type-material evidence, current NCBI identifier, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascochyta_pisi.yaml` and `just validate-strict data/taxa/eukaryota/ascochyta_pisi.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Ascochyta pisi CBS 122785` is project-linked through `AP PROJECT GOLD IDS = Gp0778604`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
