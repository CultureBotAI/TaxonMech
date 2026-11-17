# YAML Record Review: Pseudomonas sp. Wr1C05

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_wr1c05.yaml
- Started UTC: 2026-09-23T06:12:00Z
- Finished UTC: 2026-09-23T06:12:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | NCBITaxon:1007157 |
| Label | Pseudomonas sp. Wr1C05 |
| Rank | SPECIES |
| Domain | BACTERIA |
| Parent | NCBITaxon:196821, unclassified Pseudomonas |
| Maintained path | data/taxa/bacteria/pseudomonas_sp_wr1c05.yaml |
| Generation status | Generated from the committed inventories by `seed_from_sources` |

The whole target YAML was read. It is a generated NCBITaxon-only species placeholder in the bacterial corpus, with no synonyms, no LPSN nomenclature, no GTDB taxonomy mappings, no strain or genome entries, `strain_count: 0`, one NCBITAXON source attestation, and one `SEEDED_FROM_SOURCES` curation-history entry dated 2026-09-13.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1b12.yaml data/taxa/bacteria/pseudomonas_sp_wr1c02.yaml data/taxa/bacteria/pseudomonas_sp_wr1c04.yaml data/taxa/bacteria/pseudomonas_sp_wr1c05.yaml` | Passed; strict validation scanned 4 files and reported 0 files with errors. |
| `just validate data/taxa/bacteria/pseudomonas_sp_wr1c05.yaml` | Passed; LinkML reported `No issues found`. |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudomonas_sp_wr1c05.md'` | No prior report found. The `find` search included ignored files under the report directory. |
| `rg --no-ignore --hidden ... data/taxa/PATHS.tsv data/raw data/atb data/straininfo` | Found the PATHS row and the `data/raw/ncbitaxon_taxa.tsv` source row; found no same-taxon ATB or StrainInfo rows. |
| `just verify-corpus` | Skipped for this read-only review because earlier full-corpus verification over 625,960 records was clean and this review did not edit generated YAML. |
| `just validate-history` | Skipped because no `history/` decision is created by a read-only review. |
| `just validate-products` | Not applicable; the record has no `causal_graphs`. |

## Identity and Grounding

`data/taxa/PATHS.tsv` maps `NCBITaxon:1007157` to `pseudomonas_sp_wr1c05`, and the pinned NCBI inventory row identifies the same CURIE as `Pseudomonas sp. Wr1C05`, rank `SPECIES`, parent `NCBITaxon:196821`, and genetic code `11`.

The generated lineage is internally consistent for a bacterial `Pseudomonas` placeholder below the no-rank `unclassified Pseudomonas` parent. There are no LPSN names or GTDB mappings to reconcile against NCBI.

Live NCBI lookup was unavailable, so `data/raw/ncbitaxon_taxa.tsv` is the pinned local source of truth for this review.

## Evidence

- The NCBITAXON attestation matches the exact row for `NCBITaxon:1007157` and label `Pseudomonas sp. Wr1C05` in `data/raw/ncbitaxon_taxa.tsv`.
- `assertion_count: 1` / `assertion_unit: NAME` matches the single NCBI source assertion present for the taxon.
- No optional synonyms, nomenclature, mapping, strain, genome, ATB, StrainInfo, or causal-graph assertions are present without evidence.

## Completeness

The sparse representation is complete for the committed evidence inspected. A gitignore-independent `rg --no-ignore --hidden` search across `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` for `NCBITaxon:1007157`, `Pseudomonas sp. Wr1C05`, and `pseudomonas_sp_wr1c05` found only the PATHS and NCBI taxonomy rows.

The empty auxiliary sections and `strain_count: 0` are therefore appropriate.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Run `just validate-strict data/taxa/bacteria/pseudomonas_sp_wr1c05.yaml` after any future seed refresh that touches this taxon.
- Run `just verify-corpus` after any future change to `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, or the seed logic.

## Additional Notes

The no-rank parent is carried lineage context from NCBI, not an out-of-scope TaxonMech record for a higher taxon.
