# YAML Record Review: Ascobolus immersus

## Target

- File: `data/taxa/eukaryota/ascobolus_immersus.yaml`
- Identifier: `NCBITaxon:5191`
- Label: `Ascobolus immersus`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:5190` / `Ascobolus`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `Pezizomycetes` -> `Pezizales` -> `Ascobolaceae` -> `Ascobolus`
- Existing review report: none found for `*ascobolus_immersus.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascobolus_immersus.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascobolus_immersus.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:5191`, labelled `Ascobolus immersus` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:5191` is a `SPECIES` child of `NCBITaxon:5190` / `Ascobolus`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and one related synonym, `Ascobolus immersus Persoon, 1796`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascobolus immersus, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps old identifier `NCBITaxon:1160508` into `NCBITaxon:5191`; it has no row mapping `NCBITaxon:5191` to another target, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:5191`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merged-ID rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:5191`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:5191` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0017640`, `Ascobolus immersus RN42`, with culture collection ID `CBS 140666`.
- GOLD organism `Go0017640` has two projects: `Gp0017640`, with BioProject `PRJNA346638` and BioSample `SAMN05920622`, and `Gp0018270`, with BioProject `PRJNA250965` and BioSample `SAMN03003147`.
- GOLD project `Gp0017640` is linked to genome analysis `Ga0226788`, which has IMG taxon ID `2761201883` and an empty `AP_GENBANK` list.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 22 direct strain rows for `5191`, all already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `5191`.
- `data/raw/ncbi_type_material.tsv` has no rows for `NCBITaxon:5191`.
- Exact `CBS 140666` token lookups found 0 BacDive rows and 0 StrainInfo rows.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, all exact StrainInfo rows are already excluded, and the native GOLD `CBS 140666` token does not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascobolus_immersus.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, current NCBI identifier, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascobolus_immersus.yaml` and `just validate-strict data/taxa/eukaryota/ascobolus_immersus.yaml` after regenerating the taxon record.

## Additional Notes

- The visible native GOLD analysis for `Ascobolus immersus RN42` is project-linked through `AP PROJECT GOLD IDS = Gp0017640`; it does not use `AP ORGANISM GOLD ID`.
- The native GOLD analysis has an empty `AP_GENBANK` list, so there is no native GenBank assembly accession to reconcile for this record.
