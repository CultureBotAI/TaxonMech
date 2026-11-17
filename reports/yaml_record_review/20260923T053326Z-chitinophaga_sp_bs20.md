# YAML Record Review: Chitinophaga sp. BS20

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/chitinophaga_sp_bs20.yaml
- Started UTC: 2026-09-23T05:32:40Z
- Finished UTC: 2026-09-23T05:33:26Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007088`
- Label: `Chitinophaga sp. BS20`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2619133` (`unclassified Chitinophaga`)
- Maintained path: generated `data/taxa/bacteria/chitinophaga_sp_bs20.yaml`; fixes belong in `data/raw/`, `data/atb/`, `data/straininfo/`, `curation/seed_scope.tsv`, or `src/taxonmech/seed.py`, depending on source.

The record is a generated NCBI-only placeholder for an unclassified Chitinophaga species-level taxon.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/archaea/candidatus_nitrosarchaeum_limnium.yaml data/taxa/bacteria/micrococcus_sp_kc5.yaml data/taxa/bacteria/brevibacterium_hankyongi.yaml data/taxa/bacteria/chitinophaga_sp_bs20.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/chitinophaga_sp_bs20.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML agrees with the pinned NCBI inventory row in `data/raw/ncbitaxon_taxa.tsv:210798`: `NCBITaxon:1007088`, label `Chitinophaga sp. BS20`, rank `SPECIES`, parent `NCBITaxon:2619133`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.

The lineage is carried from NCBI and is internally consistent from `root` through `Bacteria`, `Pseudomonadati`, `FCB group`, `Bacteroidota/Chlorobiota group`, `Bacteroidota`, `Chitinophagia`, `Chitinophagales`, `Chitinophagaceae`, `Chitinophaga`, and `unclassified Chitinophaga`. `grounding_status: EXACT` is appropriate because the record is seeded directly from the same NCBI identifier.

## Evidence

- `source_attestations[0]` correctly cites `NCBITAXON` / `NCBITaxon:1007088` with source label `Chitinophaga sp. BS20`, `assertion_count: 1`, and `assertion_unit: NAME`.
- `mapping_status: SEEDED` matches a record generated from committed seed inputs.
- The source row has empty LPSN, GTDB, BacDive, GOLD, ATB, and StrainInfo columns, so the absence of `nomenclature`, `taxonomy_mappings`, strain listings, genome records, ATB evidence, and StrainInfo evidence is supported.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-chitinophaga_sp_bs20.md'` included ignored reports and found no prior review for this stem.
- An anchored exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found only the PATHS entry for `NCBITaxon:1007088` and the single `data/raw/ncbitaxon_taxa.tsv` source row.
- `strain_count: 0` is complete for the inspected rows: no BacDive, ATB, or StrainInfo rows were found for this taxon.
- No optional synonym, nomenclature, GTDB mapping, strain, genome, sample, causal-graph, or quality sections are required by the local sources currently attached to this record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this passing NCBI-only record. If a future refresh links this taxon to GTDB, LPSN, BacDive, ATB, or StrainInfo, rerun `just validate-strict data/taxa/bacteria/chitinophaga_sp_bs20.yaml`, `just validate data/taxa/bacteria/chitinophaga_sp_bs20.yaml`, and a focused exact `rg --no-ignore --hidden` over the maintained source rows before reviewing the newly projected sections.

## Additional Notes

The live NCBI browser and source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 NCBI snapshot row is the authority evidence used for this report.
