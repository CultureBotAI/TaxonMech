# YAML Record Review: Ascogregarina taiwanensis

## Target

- File: `data/taxa/eukaryota/ascogregarina_taiwanensis.yaml`
- Identifier: `NCBITaxon:158379`
- Label: `Ascogregarina taiwanensis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:158378` / `Ascogregarina`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Sar` -> `Alveolata` -> `Apicomplexa` -> `Conoidasida` -> `Gregarinasina` -> `Eugregarinorida` -> `Lecudinidae` -> `Ascogregarina`
- Existing review report: none found for `*ascogregarina_taiwanensis.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/ascogregarina_taiwanensis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/ascogregarina_taiwanensis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:158379`, labelled `Ascogregarina taiwanensis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:158379` is a `SPECIES` child of `NCBITaxon:158378` / `Ascogregarina`.
- The generated NCBI synonym block matches the raw NCBI row: it has related synonym `Ascogregarina taiwanensis Lien & Levine, 1980`, with no exact synonyms in the snapshot.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Ascogregarina taiwanensis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:158379`, so the generated current identifier is not represented as merged away in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:158379`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and the legacy page path. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:158379`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:158379` with count `1`.
- Exact native GOLD inspection found two organism rows for the same taxon: `Go0003431`, `Ascogregarina taiwanensis Taoyuan-1`, with strain `Taoyuan-1`, and `Go0038954`, `Ascogregarina taiwanensis`, with no strain or culture collection ID.
- Native GOLD organism `Go0003431` has one project, `Gp0003431`, with BioProject `PRJNA27765` and BioSample `SAMN02953717`; organism `Go0038954` has two projects, `Gp0038954` and `Gp0090214`, with BioProjects `PRJNA170545` and `PRJNA170719`.
- GOLD project `Gp0003431` is linked to genome analysis `Ga0039261` with GenBank ID `ABJQ00000000` and no assembly accession.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct strain rows and 0 deposit-only rows for `158379`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `158379`.
- Exact `Taoyuan-1` token lookups found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:158379`.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the source checks: BacDive and StrainInfo have no exact NCBI match, and the native GOLD `Taoyuan-1` token does not add an eligible local BacDive or StrainInfo strain.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/ascogregarina_taiwanensis.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonym, count-consistent aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- Rerun `just validate data/taxa/eukaryota/ascogregarina_taiwanensis.yaml` and `just validate-strict data/taxa/eukaryota/ascogregarina_taiwanensis.yaml` after regenerating the taxon record.

## Additional Notes

- The aggregate GOLD source count of 1 comes from `data/raw/gold_organisms.tsv`; the local native `data/gold/organisms.jsonl.gz` snapshot has two inspectable same-taxon organism rows for `158379`. This source-count mismatch is not itself a YAML defect when the aggregate file supports the generated count.
