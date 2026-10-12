# YAML Record Review: [Haemophilus] ducreyi HMC112
- Repository: TaxonMech
- Record: `data/taxa/bacteria/haemophilus_ducreyi_hmc112.yaml`
- Started UTC: 2026-09-22T20:40:28Z
- Finished UTC: 2026-09-22T20:41:32Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1005047` / `haemophilus_ducreyi_hmc112`.
- The record is a generated `STRAIN`-rank `BACTERIA` record for `[Haemophilus] ducreyi HMC112` under species parent `NCBITaxon:730` (`[Haemophilus] ducreyi`).
- The record is seeded from the pinned NCBITAXON inventory only.

## Validation
- `just validate data/taxa/bacteria/haemophilus_ducreyi_hmc112.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/haemophilus_ducreyi_hmc112.yaml data/taxa/bacteria/collimonas_fungivorans_ter331.yaml data/taxa/bacteria/buchnera_aphidicola_str_ua_uroleucon_ambrosiae.yaml data/taxa/bacteria/gallibacterium_anatis_umn179.yaml` completed successfully for the four-file batch.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005047`, `label: [Haemophilus] ducreyi HMC112`, `rank: STRAIN`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:730`, and `genetic_code: 11` match the exact NCBI row in `data/raw/ncbitaxon_taxa.tsv`.
- The bracketed genus in the label and parent species is NCBI's spelling in the local snapshot and is preserved verbatim.
- The three exact synonyms are the bracketless NCBI strain aliases from the same NCBI source row.

## Evidence
- The exact-ID gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, and `data/straininfo` found only the NCBITAXON source row for `NCBITaxon:1005047`.
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
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-haemophilus_ducreyi_hmc112.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI lookup was not used; the pinned local NCBI Taxon row dated `2026-09-13` was treated as the source of truth.
