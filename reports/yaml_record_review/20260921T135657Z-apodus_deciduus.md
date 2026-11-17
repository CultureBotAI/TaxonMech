# YAML Record Review: Apodus deciduus

## Target

- File: `data/taxa/eukaryota/apodus_deciduus.yaml`
- Identifier: `NCBITaxon:303344`
- Label: `Apodus deciduus`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:303323` / `Apodus`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Sordariomycetidae` -> `Sordariales` -> `Lasiosphaeriaceae` -> `Apodus`
- Existing review report: none found for `*apodus_deciduus.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apodus_deciduus.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apodus_deciduus.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:303344`, labelled `Apodus deciduus` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:303344` is a `SPECIES` child of `NCBITaxon:303323` / `Apodus`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonyms `Thielavia decidua` and `Thielavia deciduus`, plus related synonym `Apodus deciduus Malloch & Cain, 1971`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apodus deciduus, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:303344`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:303344`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:303344`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:303344` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0651470`, `Apodus deciduus CBS 506.70`, strain and culture collection ID `CBS 506.70`.
- GOLD organism `Go0651470` has two projects: `Gp0688374` with BioProject `PRJNA1081097` and BioSample `SAMN40290116`, and transcriptome project `Gp0699238`, whose BioProject and BioSample fields are blank in the local native GOLD snapshot.
- No native GOLD genome analysis rows linked to organism `Go0651470`, `Gp0688374`, or `Gp0699238` were present in the local `data/gold/analyses.jsonl.gz` snapshot.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 1 direct strain row for `303344`, 0 deposit-only rows, and 0 missing exclusions; `straininfo.strain:167722` is excluded locally as `no_eligible_own_deposit_match`.
- A `CBS 506.70` token lookup found no BacDive rows and one StrainInfo row, `straininfo.strain:167722`, already included in the excluded exact StrainInfo set.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `303344`.
- `data/raw/ncbi_type_material.tsv` has six type-material rows for `NCBITaxon:303344`: duplicate punctuation variants for type material `ATCC 22100`, `CBS 506.70`, and `TRTC 45705`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and the only exact StrainInfo match is explicitly excluded.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apodus_deciduus.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, type-material evidence, count-consistent one-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate `straininfo.strain:167722` for `NCBITaxon:303344` and check whether it should contribute to `strain_count`.
- If GOLD analysis linking changes, recheck whether projects `Gp0688374` or `Gp0699238` acquire analysis rows and whether those rows remain source evidence only or can join into strain-related records.
- Rerun `just validate data/taxa/eukaryota/apodus_deciduus.yaml` and `just validate-strict data/taxa/eukaryota/apodus_deciduus.yaml` after regenerating the taxon record.

## Additional Notes

- The GOLD transcriptome project `Gp0699238` is tied to the same native organism but currently has no BioProject, BioSample, or analysis row in the inspected local GOLD snapshot.
