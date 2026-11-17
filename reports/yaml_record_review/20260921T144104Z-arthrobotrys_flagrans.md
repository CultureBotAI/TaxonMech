# YAML Record Review: Arthrobotrys flagrans

## Target

- File: `data/taxa/eukaryota/arthrobotrys_flagrans.yaml`
- Identifier: `NCBITaxon:97331`
- Label: `Arthrobotrys flagrans`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:13348` / `Arthrobotrys`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `Orbiliomycetes` -> `Orbiliales` -> `Orbiliaceae` -> `Arthrobotrys`
- Existing review report: none found for `*arthrobotrys_flagrans.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arthrobotrys_flagrans.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arthrobotrys_flagrans.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:97331`, labelled `Arthrobotrys flagrans` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:97331` is a `SPECIES` child of `NCBITaxon:13348` / `Arthrobotrys`.
- The generated NCBI synonym block matches the raw NCBI row: it has exact synonyms `Duddingtonia flagrans` and `Trichothecium flagrans`, plus three related synonyms with authorship.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arthrobotrys flagrans, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has one retired identifier that now merges into `NCBITaxon:97331`: `NCBITaxon:47257`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:97331`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:97331`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:97331`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:97331` with count `2`.
- Exact native GOLD inspection found one organism row for the same taxon, using an exact synonym in the organism name: `Go0565846`, `Duddingtonia flagrans CBS H-5679`, strain and culture collection ID `CBS H-5679`.
- GOLD organism `Go0565846` has one project, `Gp0536206`, with BioProject `PRJNA494930` and BioSample `SAMN10185917`.
- GOLD project `Gp0536206` is linked to genome analysis `Ga0486033` with GenBank assembly accession `GCA_004000055.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 9 direct strain rows for `97331`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `97331`.
- An exact `CBS H-5679` token lookup found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, the nine exact StrainInfo rows are already excluded, and the native GOLD `CBS H-5679` token does not add an eligible local strain.
- The absence of `nomenclature` is consistent with the local source inventory: `data/raw/ncbi_type_material.tsv` has no row for this identifier, and generated `nomenclature` entries currently come from LPSN only.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arthrobotrys_flagrans.yaml`; it is generated and validates strictly.
- Preserve the NCBI exact and related synonyms, retained merged-ID context, count-consistent aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/arthrobotrys_flagrans.yaml` and `just validate-strict data/taxa/eukaryota/arthrobotrys_flagrans.yaml` after regenerating the taxon record.

## Additional Notes

- The generated GOLD assertion count is backed by `data/raw/gold_organisms.tsv`, which is an aggregate transformed KG-Microbe GOLD count. The local native GOLD snapshot currently has one inspectable organism for `NCBITaxon:97331`, one project, and one project-linked genome analysis.
- The native GOLD analysis for `Duddingtonia flagrans CBS H-5679` is project-linked through `AP PROJECT GOLD IDS = Gp0536206`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
