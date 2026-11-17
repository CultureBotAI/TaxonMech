# YAML Record Review: Arachnopeziza araneosa

## Target

- File: `data/taxa/eukaryota/arachnopeziza_araneosa.yaml`
- Identifier: `NCBITaxon:2259763`
- Label: `Arachnopeziza araneosa`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:47751` / `Arachnopeziza`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `leotiomyceta` -> `sordariomyceta` -> `Leotiomycetes` -> `Helotiales` -> `Arachnopezizaceae` -> `Arachnopeziza`
- Existing review report: none found for `*arachnopeziza_araneosa.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arachnopeziza_araneosa.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arachnopeziza_araneosa.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:2259763`, labelled `Arachnopeziza araneosa` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:2259763` is a `SPECIES` child of `NCBITaxon:47751` / `Arachnopeziza`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonyms `Belonidium araneosum` and `Pyronema araneosum Sacc., 1878`, plus related synonyms `Arachnopeziza araneosa (Sacc.) Korf, 1952` and `Belonidium araneosum Sacc., 1889`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arachnopeziza araneosa, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:2259763`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:2259763`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:2259763`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:2259763` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0517608`, `Arachnopeziza araneosa D781`, strain `D781`, and culture collection ID `ICMP 21731`.
- GOLD organism `Go0517608` has one project, `Gp0441661`, with BioProject `PRJNA487672` and BioSample `SAMN09907757`.
- GOLD project `Gp0441661` is linked to genome analysis `Ga0657352` with GenBank assembly accession `GCA_003988855.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 5 direct strain rows for `2259763`, 0 deposit-only rows, and 0 missing exclusions; all 5 direct IDs are excluded locally as `no_eligible_own_deposit_match`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `2259763`.
- An `ICMP 21731` token lookup found 0 BacDive rows and one StrainInfo row, `straininfo.strain:266897`, already included in the excluded exact StrainInfo set.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:2259763` in the local NCBI type-material snapshot.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: BacDive has no exact NCBI match, and all exact StrainInfo matches are explicitly excluded.
- The absence of `nomenclature` is expected for this eukaryotic species because generated `nomenclature` entries currently come from LPSN only, and NCBI has no type-material rows for this taxon in the local raw snapshot.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arachnopeziza_araneosa.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, count-consistent one-organism GOLD source attestation, and StrainInfo exclusion behavior when regenerating the record.

## Follow-up Checks

- If the StrainInfo exclusion policy for `no_eligible_own_deposit_match` changes, re-evaluate the 5 excluded StrainInfo rows for `NCBITaxon:2259763` and check whether any should contribute to `strain_count`.
- Rerun `just validate data/taxa/eukaryota/arachnopeziza_araneosa.yaml` and `just validate-strict data/taxa/eukaryota/arachnopeziza_araneosa.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Arachnopeziza araneosa D781` is project-linked through `AP PROJECT GOLD IDS = Gp0441661`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
- The bare `D781` GOLD strain token is too short for broad local strain-source text search because it appears in unrelated StrainInfo deposit text; `ICMP 21731` is the specific GOLD culture token for follow-up lookups.
