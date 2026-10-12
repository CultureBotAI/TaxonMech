# YAML Record Review: Pseudonocardia sp. HBUC20201

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudonocardia_sp_hbuc20201.yaml
- Started UTC: 2026-09-23T05:07:40Z
- Finished UTC: 2026-09-23T05:09:00Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1006890`
- Label: `Pseudonocardia sp. HBUC20201`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2619320` (`unclassified Pseudonocardia`)
- Maintained path: generated `data/taxa/bacteria/pseudonocardia_sp_hbuc20201.yaml`; fixes belong in `data/raw/`, `data/atb/`, `data/straininfo/`, `curation/seed_scope.tsv`, or `src/taxonmech/seed.py`, depending on source.

The record is a generated NCBI-only placeholder for an unclassified Pseudonocardia species-level taxon.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/planotetraspora_sp_hbuc10404.yaml data/taxa/bacteria/promicromonospora_sp_hbud10206.yaml data/taxa/bacteria/promicromonospora_sp_hbud30218.yaml data/taxa/bacteria/pseudonocardia_sp_hbuc20201.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/pseudonocardia_sp_hbuc20201.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML agrees with the pinned NCBI inventory row in `data/raw/ncbitaxon_taxa.tsv:210757`: `NCBITaxon:1006890`, label `Pseudonocardia sp. HBUC20201`, rank `SPECIES`, parent `NCBITaxon:2619320`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.

The lineage is carried from NCBI and is internally consistent from `root` through `Bacillati`, `Actinomycetota`, `Actinomycetes`, `Pseudonocardiales`, `Pseudonocardiaceae`, `Pseudonocardia`, and `unclassified Pseudonocardia`. `grounding_status: EXACT` is appropriate because the record is seeded directly from the same NCBI identifier.

## Evidence

- `source_attestations[0]` correctly cites `NCBITAXON` / `NCBITaxon:1006890` with source label `Pseudonocardia sp. HBUC20201`, `assertion_count: 1`, and `assertion_unit: NAME`.
- `mapping_status: SEEDED` matches a record generated from committed seed inputs.
- The source row has empty LPSN, GTDB, BacDive, GOLD, ATB, and StrainInfo columns, so the absence of `nomenclature`, `taxonomy_mappings`, strain listings, genome records, ATB evidence, and StrainInfo evidence is supported.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-pseudonocardia_sp_hbuc20201.md'` included ignored reports and found no prior review for this stem.
- Exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found only the PATHS entry for `NCBITaxon:1006890` and the single `data/raw/ncbitaxon_taxa.tsv` source row.
- `strain_count: 0` is complete for the inspected rows: no BacDive, ATB, or StrainInfo rows were found for this taxon.
- No optional synonym, nomenclature, GTDB mapping, strain, genome, sample, causal-graph, or quality sections are required by the local sources currently attached to this record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this passing NCBI-only record. If a future refresh links this taxon to GTDB, LPSN, BacDive, ATB, or StrainInfo, rerun `just validate-strict data/taxa/bacteria/pseudonocardia_sp_hbuc20201.yaml`, `just validate data/taxa/bacteria/pseudonocardia_sp_hbuc20201.yaml`, and a focused exact `rg --no-ignore --hidden` over the maintained source rows before reviewing the newly projected sections.

## Additional Notes

The live NCBI browser and source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 NCBI snapshot row is the authority evidence used for this report.
