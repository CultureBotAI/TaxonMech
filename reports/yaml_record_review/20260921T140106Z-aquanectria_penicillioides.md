# YAML Record Review: Aquanectria penicillioides

## Target

- File: `data/taxa/eukaryota/aquanectria_penicillioides.yaml`
- Identifier: `NCBITaxon:1634478`
- Label: `Aquanectria penicillioides`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:1634477` / `Aquanectria`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Sordariomycetes` -> `Hypocreomycetidae` -> `Hypocreales` -> `Nectriaceae` -> `Aquanectria`
- Existing review report: none found for `*aquanectria_penicillioides.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/aquanectria_penicillioides.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/aquanectria_penicillioides.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1634478`, labelled `Aquanectria penicillioides` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1634478` is a `SPECIES` child of `NCBITaxon:1634477` / `Aquanectria`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonyms `Flagellospora penicillioides` and `Nectria penicillioides`, plus related synonyms `Aquanectria penicillioides (Ingold) L. Lombard & Crous, 2015` and `Flagellospora penicillioides Ingold, 1942`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Aquanectria penicillioides, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps one old identifier, `NCBITaxon:57141`, into this active target.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:1634478`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/merge rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1634478`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1634478` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0520714`, `Aquanectria penicillioides NNIBRFG19`, strain `NNIBRFG19`, and no culture collection ID.
- GOLD organism `Go0520714` has one project, `Gp0444912`, with BioProject `PRJNA445064` and BioSample `SAMN08769082`.
- GOLD project `Gp0444912` is linked to genome analysis `Ga0656485` with GenBank assembly accession `GCA_003415625.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 2 direct strain rows for `1634478`, 0 deposit-only rows, and 0 missing exclusions; both direct IDs are excluded locally as `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1634478`.
- An `NNIBRFG19` token lookup found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:1634478` in the local NCBI type-material snapshot.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, all exact StrainInfo matches are explicitly excluded, and the GOLD `NNIBRFG19` token does not join to either local strain source.
- The absence of `nomenclature` is expected for this eukaryotic species because generated `nomenclature` entries currently come from LPSN only, and NCBI has no type-material rows for this taxon in the local raw snapshot.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/aquanectria_penicillioides.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, retired-ID merge evidence, count-consistent one-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate the 2 excluded StrainInfo rows for `NCBITaxon:1634478` and check whether either should contribute to `strain_count`.
- Rerun `just validate data/taxa/eukaryota/aquanectria_penicillioides.yaml` and `just validate-strict data/taxa/eukaryota/aquanectria_penicillioides.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Aquanectria penicillioides NNIBRFG19` is project-linked through `AP PROJECT GOLD IDS = Gp0444912`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
