# YAML Record Review: Cellulosimicrobium sp. K2029

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/cellulosimicrobium_sp_k2029.yaml
- Started UTC: 2026-09-23T05:24:18Z
- Finished UTC: 2026-09-23T05:25:08Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1007054`
- Label: `Cellulosimicrobium sp. K2029`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2624466` (`unclassified Cellulosimicrobium`)
- Maintained path: generated `data/taxa/bacteria/cellulosimicrobium_sp_k2029.yaml`; fixes belong in `data/raw/`, `data/atb/`, `data/straininfo/`, `curation/seed_scope.tsv`, or `src/taxonmech/seed.py`, depending on source.

The record is a generated NCBI-only placeholder for an unclassified Cellulosimicrobium species-level taxon.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/veillonella_sp_c546.yaml data/taxa/bacteria/paracoccus_sp_gsm2.yaml data/taxa/bacteria/sphingobacterium_sp_gsm1.yaml data/taxa/bacteria/cellulosimicrobium_sp_k2029.yaml` | Passed; closed-schema validation accepted all 4 files. |
| `just validate data/taxa/bacteria/cellulosimicrobium_sp_k2029.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-history` | Deliberately skipped for this read-only review because it did not create a `history/` decision record. |
| `just verify-corpus` | Deliberately skipped in this focused batch; earlier full-corpus verification over 625,960 generated records was clean, and this review did not edit `data/taxa/`. |
| `just validate-products` | Not applicable; this record has no `causal_graphs`. |

## Identity and Grounding

The YAML agrees with the pinned NCBI inventory row in `data/raw/ncbitaxon_taxa.tsv:210781`: `NCBITaxon:1007054`, label `Cellulosimicrobium sp. K2029`, rank `SPECIES`, parent `NCBITaxon:2624466`, genetic code `11`, source `ncbitaxon`, and snapshot date `2026-09-13`.

The lineage is carried from NCBI and is internally consistent from `root` through `Bacteria`, `Bacillati`, `Actinomycetota`, `Actinomycetes`, `Micrococcales`, `Promicromonosporaceae`, `Cellulosimicrobium`, and `unclassified Cellulosimicrobium`. `grounding_status: EXACT` is appropriate because the record is seeded directly from the same NCBI identifier.

## Evidence

- `source_attestations[0]` correctly cites `NCBITAXON` / `NCBITaxon:1007054` with source label `Cellulosimicrobium sp. K2029`, `assertion_count: 1`, and `assertion_unit: NAME`.
- `mapping_status: SEEDED` matches a record generated from committed seed inputs.
- The source row has empty LPSN, GTDB, BacDive, GOLD, ATB, and StrainInfo columns, so the absence of `nomenclature`, `taxonomy_mappings`, strain listings, genome records, ATB evidence, and StrainInfo evidence is supported.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-cellulosimicrobium_sp_k2029.md'` included ignored reports and found no prior review for this stem.
- Exact `rg --no-ignore --hidden` over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found only the PATHS entry for `NCBITaxon:1007054` and the single `data/raw/ncbitaxon_taxa.tsv` source row.
- `strain_count: 0` is complete for the inspected rows: no BacDive, ATB, or StrainInfo rows were found for this taxon.
- No optional synonym, nomenclature, GTDB mapping, strain, genome, sample, causal-graph, or quality sections are required by the local sources currently attached to this record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for this passing NCBI-only record. If a future refresh links this taxon to GTDB, LPSN, BacDive, ATB, or StrainInfo, rerun `just validate-strict data/taxa/bacteria/cellulosimicrobium_sp_k2029.yaml`, `just validate data/taxa/bacteria/cellulosimicrobium_sp_k2029.yaml`, and a focused exact `rg --no-ignore --hidden` over the maintained source rows before reviewing the newly projected sections.

## Additional Notes

The live NCBI browser and source-provider lookups were unavailable earlier in this run, so the committed 2026-09-13 NCBI snapshot row is the authority evidence used for this report.
