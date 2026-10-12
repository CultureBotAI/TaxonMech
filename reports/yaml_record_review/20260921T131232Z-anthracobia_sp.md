# YAML Record Review: Anthracobia sp.

## Target

- File: `data/taxa/eukaryota/anthracobia_sp.yaml`
- Identifier: `NCBITaxon:2709752`
- Label: `Anthracobia sp.`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2647567` / `unclassified Anthracobia`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Opisthokonta` -> `Fungi` -> `Dikarya` -> `Ascomycota` -> `saccharomyceta` -> `Pezizomycotina` -> `Pezizomycetes` -> `Pezizales` -> `Pyronemataceae` -> `Anthracobia` -> `unclassified Anthracobia`
- Existing review report: none found for `*anthracobia_sp.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/anthracobia_sp.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/anthracobia_sp.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species-level placeholder `NCBITaxon:2709752`, labelled `Anthracobia sp.` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:2709752` is a `SPECIES` child of the no-rank node `NCBITaxon:2647567` / `unclassified Anthracobia`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Anthracobia sp., 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:2709752`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A no-ignore, hidden-file search for the bounded identifier `NCBITaxon:2709752` and exact label `Anthracobia sp.` found only the generated taxon/page/path rows, the raw NCBI/GOLD/scope rows, and label mentions in the neighboring `Anthracobia macrocystis` synonym/report content. No duplicate `anthracobia_sp` review report was present; ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:2709752`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:2709752` with count `1`.
- The current native GOLD snapshot is not count-consistent with that transformed aggregate: exact inspection of `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, and `data/gold/analyses.jsonl.gz` found 0 organisms, 0 projects, and 0 analyses linked to NCBI taxon `2709752`.
- Exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `2709752`; there were therefore 0 local StrainInfo exclusions to account for.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `2709752`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:2709752`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, genetic code, `strain_count`, two source attestations, and generation history.
- There are no synonyms, nomenclature rows, taxonomy mappings, strains, evidence rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks.
- No type-material row is available in `data/raw/ncbi_type_material.tsv`, so there is no local NCBI type-material evidence to propagate.

## Findings

- **Low - GOLD aggregate count is not reproducible from the native snapshot.** The record's `GOLD` source attestation mirrors `data/raw/gold_organisms.tsv`, but exact native GOLD inspection found no organism row with `ORGANISM NCBI TAX ID = 2709752` and no downstream project or analysis rows for this taxon. This mirrors the known distinction that `data/raw/gold_organisms.tsv` is an aggregate KG-Microbe GOLD count, whereas the inspectable native snapshot lives under `data/gold/*.jsonl.gz`.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/anthracobia_sp.yaml`; it is generated and validates strictly.
- Reconcile the transformed GOLD aggregate with the native GOLD snapshot for `NCBITaxon:2709752` so the single `GOLD` count can be traced to a current GOLD organism row, or intentionally allow the generated source attestation to remain aggregate-only when native rows are absent.

## Follow-up Checks

- After refreshing KG-Microbe GOLD transforms or local GOLD JSONL snapshots, rerun an exact native GOLD lookup for NCBI taxon `2709752` and confirm whether an organism row reappears.
- Rerun `just validate data/taxa/eukaryota/anthracobia_sp.yaml` and `just validate-strict data/taxa/eukaryota/anthracobia_sp.yaml` after regenerating the taxon record.

## Additional Notes

- Because this is a eukaryotic, GOLD-seeded placeholder taxon with no BacDive or StrainInfo evidence in the local exact searches, the record follows the same compact generated pattern as nearby `Anthracobia` records rather than the strain-rich bacterial/archaeal path.
