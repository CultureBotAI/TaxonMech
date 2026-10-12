# YAML Record Review: [Haemophilus] ducreyi ATCC 33921
- Repository: TaxonMech
- Record: `data/taxa/bacteria/haemophilus_ducreyi_atcc_33921.yaml`
- Started UTC: 2026-09-22T20:38:22Z
- Finished UTC: 2026-09-22T20:39:27Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1005046` / `haemophilus_ducreyi_atcc_33921`.
- The record is a generated `STRAIN`-rank `BACTERIA` record for `[Haemophilus] ducreyi ATCC 33921` under species parent `NCBITaxon:730` (`[Haemophilus] ducreyi`).
- The record is seeded from the pinned NCBITAXON and MADIN inventories.

## Validation
- `just validate data/taxa/bacteria/haemophilus_ducreyi_atcc_33921.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/candidatus_regiella_insecticola_5_15.yaml data/taxa/bacteria/haemophilus_ducreyi_025.yaml data/taxa/bacteria/haemophilus_ducreyi_511.yaml data/taxa/bacteria/haemophilus_ducreyi_atcc_33921.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005046`, `label: [Haemophilus] ducreyi ATCC 33921`, `rank: STRAIN`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:730`, and `genetic_code: 11` match the exact NCBI row in `data/raw/ncbitaxon_taxa.tsv`.
- The bracketed genus in the label and parent species is NCBI's spelling in the local snapshot and is preserved verbatim.
- The three exact synonyms are the bracketless NCBI strain aliases from the same NCBI source row.

## Evidence
- Exact-ID gitignore-independent `rg --no-ignore --hidden` searches across `data/raw`, `data/atb`, and `data/straininfo` found one NCBITAXON source row and one MADIN trait-assertion row for `NCBITaxon:1005046`.
- No exact-ID GTDB, GOLD, LPSN, BacDive, MediaDive, ATB, StrainInfo, or culture-collection rows were present in the pinned local source rows.
- The generated `source_attestations` entries therefore correctly summarize the NCBITAXON name and one MADIN trait assertion.

## Completeness
- The record carries the available identity, parent, lineage, NCBI synonym, genetic-code, and source-attestation evidence.
- `strain_count: 0`, empty genome sections, and absent nomenclature, GTDB mapping, and xref sections are expected for a strain record with no exact same-taxon BacDive row.

## Findings
- No findings.

## Recommended Edits
- None.

## Follow-up Checks
- None required for this record.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-haemophilus_ducreyi_atcc_33921.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI and Madin lookups were not used; the pinned local rows in `data/raw/` were treated as the source of truth.
