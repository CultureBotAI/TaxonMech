# YAML Record Review: Ascoidea asiatica

## Target

- File: `data/taxa/eukaryota/ascoidea_asiatica.yaml`
- Identifier: `NCBITaxon:1301101`
- Label: `Ascoidea asiatica`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:27308` / `Ascoidea`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Saccharomycotina` -> `Saccharomycetes` -> `Ascoideales` -> `Ascoideaceae` -> `Ascoidea`
- Existing review report: none found for `*ascoidea_asiatica.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascoidea_asiatica.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascoidea_asiatica.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1301101`, labelled `Ascoidea asiatica` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1301101` is a `SPECIES` child of `NCBITaxon:27308` / `Ascoidea`.
- The generated `genetic_code: 12` matches the raw NCBI genetic-code column for this yeast species.
- The generated NCBI synonym block matches the raw NCBI row: it has related synonym `Ascoidea asiatica L.R. Batra & Francke-Grosm. 1964`, with no exact synonyms in the snapshot.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascoidea asiatica, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1301101`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:1301101`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope/type-material rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1301101`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1301101` with count `2`.
- Exact native GOLD inspection found two organism rows for the same taxon: `Go0145223`, `Ascoidea asiatica JCM 7603`, with strain and culture collection ID `JCM 7603`, and `Go0705310`, `Ascoidea asiatica NRRL Y-17632`, with strain and culture collection ID `NRRL Y-17632`.
- Native GOLD organism `Go0145223` has one project, `Gp0150862`, with BioProject `PRJDB3724` and BioSample `SAMD00031916`; organism `Go0705310` has one project, `Gp0831346`, with BioProject `PRJNA736342` and BioSample `SAMN20341566`.
- GOLD project `Gp0150862` is linked to genome analysis `Ga0133624` with GenBank assembly accession `GCA_001600695.1`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `1301101`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1301101`.
- `data/raw/ncbi_type_material.tsv` has ten rows for `NCBITaxon:1301101`, covering type material `377.68`, `ATCC 22852`, `ATCC:22852`, `Batra 1925`, `personal:Batra:1925`, `DSM 1365`, `DSM:1365`, `NRRL Y-17632`, `NRRL:Y-17632`, and `NRRL:Y:17632`.
- Exact JCM and type-material token lookups found no same-taxon BacDive or StrainInfo rows. The matched `DSM 1365` BacDive/StrainInfo rows belong to `Brevibacterium paucivorans` or `Thermobrachium celere`, and the matched fuller yeast token set belongs to StrainInfo taxon `Alloascoidea africana` / `NCBITaxon:27309`, so none are eligible own-taxon strain evidence for `NCBITaxon:1301101`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, yeast mitochondrial genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI match, and the native GOLD `JCM 7603` and `NRRL Y-17632` tokens do not add an eligible local BacDive or StrainInfo strain.
- The NCBI type-material rows do not imply a missing `nomenclature` block: generated `nomenclature` entries currently come from LPSN only, while this is a eukaryotic fungal species.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascoidea_asiatica.yaml`; it is generated and validates strictly.
- Preserve the yeast mitochondrial genetic code, NCBI synonym, type-material evidence, count-consistent aggregate/native GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascoidea_asiatica.yaml` and `just validate-strict data/taxa/eukaryota/ascoidea_asiatica.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD analysis for `Ascoidea asiatica JCM 7603` is project-linked through `AP PROJECT GOLD IDS = Gp0150862`; it does not use `AP ORGANISM GOLD ID`, so any future GOLD inspection for this record needs to keep the project-link traversal.
