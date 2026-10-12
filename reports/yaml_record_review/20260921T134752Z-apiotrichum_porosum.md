# YAML Record Review: Apiotrichum porosum

## Target

- File: `data/taxa/eukaryota/apiotrichum_porosum.yaml`
- Identifier: `NCBITaxon:105984`
- Label: `Apiotrichum porosum`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:105983` / `Apiotrichum`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Basidiomycota` -> `Agaricomycotina` -> `Tremellomycetes` -> `Trichosporonales` -> `Trichosporonaceae` -> `Apiotrichum`
- Existing review report: none found for `*apiotrichum_porosum.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apiotrichum_porosum.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apiotrichum_porosum.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:105984`, labelled `Apiotrichum porosum` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:105984` is a `SPECIES` child of `NCBITaxon:105983` / `Apiotrichum`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonym `Trichosporon porosum`, plus related synonyms `Apiotrichum porosum Stautz, 1931`, `Trichosporon sp. Af113-1-1`, `Trichosporon sp. ICMP 16990`, `Trichosporon sp. ICMP 16991`, `Trichosporon sp. SJ13S15`, and `Trichosporon sp. SJ15S11`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apiotrichum porosum, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` maps five old identifiers into this active target: `NCBITaxon:2898193`, `NCBITaxon:432118`, `NCBITaxon:432119`, `NCBITaxon:565609`, and `NCBITaxon:565610`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:105984`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material/merge rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:105984`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:105984` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0138947`, `Apiotrichum porosum JCM 1458`, strain and culture collection ID `JCM 1458`.
- GOLD organism `Go0138947` has one project, `Gp0144004`, with BioProject `PRJDB3693` and BioSample `SAMD00028414`.
- GOLD project `Gp0144004` is linked to genome analysis `Ga0131597` with GenBank assembly accession `GCA_001600255.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 8 direct strain rows for `105984`, 0 deposit-only rows, and 0 missing exclusions; all 8 direct IDs are excluded locally as `no_eligible_own_deposit_match`.
- A boundary-aware `JCM 1458` token lookup found no BacDive rows and one StrainInfo row, `straininfo.strain:63182`, already included in the excluded exact StrainInfo set.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `105984`.
- `data/raw/ncbi_type_material.tsv` has 10 type-material rows for `NCBITaxon:105984`: duplicate punctuation variants of culture from type material `CBS 2040`, duplicate variants for type material `JCM 1458`, and three punctuation variants each for type material `NRRL Y-17198` and `VKM Y-3`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and all exact StrainInfo matches are explicitly excluded.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apiotrichum_porosum.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, retired-ID merge evidence, type-material evidence, count-consistent one-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate the 8 excluded StrainInfo rows for `NCBITaxon:105984` and check whether any should contribute to `strain_count`.
- Rerun `just validate data/taxa/eukaryota/apiotrichum_porosum.yaml` and `just validate-strict data/taxa/eukaryota/apiotrichum_porosum.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Apiotrichum porosum JCM 1458` is project-linked through `AP PROJECT GOLD IDS = Gp0144004`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
