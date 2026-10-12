# YAML Record Review: Arthrobotrys entomopaga

## Target

- File: `data/taxa/eukaryota/arthrobotrys_entomopaga.yaml`
- Identifier: `NCBITaxon:321852`
- Label: `Arthrobotrys entomopaga`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:13348` / `Arthrobotrys`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `Orbiliomycetes` -> `Orbiliales` -> `Orbiliaceae` -> `Arthrobotrys`
- Existing review report: none found for `*arthrobotrys_entomopaga.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arthrobotrys_entomopaga.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arthrobotrys_entomopaga.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:321852`, labelled `Arthrobotrys entomopaga` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:321852` is a `SPECIES` child of `NCBITaxon:13348` / `Arthrobotrys`.
- The generated NCBI synonym block matches the raw NCBI row: it has one exact synonym, `Dactylellina entomopaga`, and one related synonym, `Arthrobotrys entomopaga Drechsler, 1944`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arthrobotrys entomopaga, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:321852`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:321852`.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:321852`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:321852`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:321852` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0632088`, `Arthrobotrys entomopaga CBS642.8`, strain `CBS642.8`, and no culture collection ID.
- GOLD organism `Go0632088` has one project, `Gp0645909`, with BioProject `PRJNA283584` and BioSample `SAMN03653092`.
- GOLD project `Gp0645909` is linked to genome analysis `Ga0553220` with GenBank assembly accession `GCA_012184315.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 1 direct strain row for `321852`, already excluded in `data/straininfo/exclusions.tsv` with `no_eligible_own_deposit_match`, and 0 deposit-only rows.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `321852`.
- A `CBS642.8` token lookup found 0 BacDive rows and found the same excluded exact-NCBI StrainInfo row, `straininfo.strain:169376`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive has no exact NCBI match, and the one exact StrainInfo row that matches both the target taxon and native GOLD token is already excluded.
- The absence of `nomenclature` is consistent with the local source inventory: `data/raw/ncbi_type_material.tsv` has no row for this identifier, and generated `nomenclature` entries currently come from LPSN only.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arthrobotrys_entomopaga.yaml`; it is generated and validates strictly.
- Preserve the NCBI exact and related synonyms, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/arthrobotrys_entomopaga.yaml` and `just validate-strict data/taxa/eukaryota/arthrobotrys_entomopaga.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Arthrobotrys entomopaga CBS642.8` is project-linked through `AP PROJECT GOLD IDS = Gp0645909`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
