# YAML Record Review: [Haemophilus] ducreyi 025
- Repository: TaxonMech
- Record: `data/taxa/bacteria/haemophilus_ducreyi_025.yaml`
- Started UTC: 2026-09-22T20:38:22Z
- Finished UTC: 2026-09-22T20:39:27Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1005044` / `haemophilus_ducreyi_025`.
- The record is a generated `STRAIN`-rank `BACTERIA` record for `[Haemophilus] ducreyi 025` under species parent `NCBITaxon:730` (`[Haemophilus] ducreyi`).
- The record is seeded from the pinned NCBITAXON inventory only.

## Validation
- `just validate data/taxa/bacteria/haemophilus_ducreyi_025.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/candidatus_regiella_insecticola_5_15.yaml data/taxa/bacteria/haemophilus_ducreyi_025.yaml data/taxa/bacteria/haemophilus_ducreyi_511.yaml data/taxa/bacteria/haemophilus_ducreyi_atcc_33921.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005044`, `label: [Haemophilus] ducreyi 025`, `rank: STRAIN`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:730`, and `genetic_code: 11` match the exact NCBI row in `data/raw/ncbitaxon_taxa.tsv`.
- The bracketed genus in the label and parent species is NCBI's spelling in the local snapshot and is preserved verbatim.
- The three exact synonyms are the bracketless NCBI strain aliases from the same NCBI source row.

## Evidence
- The exact-ID gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, and `data/straininfo` found only the NCBITAXON source row for `NCBITaxon:1005044`.
- No exact-ID GTDB, GOLD, MADIN, LPSN, BacDive, MediaDive, ATB, StrainInfo, or culture-collection rows were present in the pinned local source rows.
- The generated `source_attestations` entry is therefore correctly limited to the NCBITAXON name attestation.

## Completeness
- The record carries the available identity, parent, lineage, NCBI synonym, genetic-code, and source-attestation evidence.
- `strain_count: 0`, empty genome sections, and absent nomenclature, GTDB mapping, and xref sections are expected for an NCBI-only strain record with no exact same-taxon strain inventory rows.

## Findings
- No findings.

## Recommended Edits
- None.

## Follow-up Checks
- None required for this record.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-haemophilus_ducreyi_025.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI lookup was not used; the pinned local NCBI Taxon row dated `2026-09-13` was treated as the source of truth.
