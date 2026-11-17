# YAML Record Review: Flavobacterium sp. TE15

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/flavobacterium_sp_te15.yaml
- Started UTC: 2026-09-23T13:10:52Z
- Finished UTC: 2026-09-23T13:11:58Z
- Verdict: pass

## Target

`data/taxa/bacteria/flavobacterium_sp_te15.yaml` is the generated `TaxonRecord` for `NCBITaxon:1009009`, label `Flavobacterium sp. TE15`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:196869` `unclassified Flavobacterium`.

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*flavobacterium_sp_te15.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/brevundimonas_sp_te4.yaml data/taxa/bacteria/flavobacterium_sp_te15.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_onchocerca_ochengi.yaml data/taxa/bacteria/beta_proteobacterium_in3.yaml` | Passed for the 4-file batch |
| `just validate data/taxa/bacteria/flavobacterium_sp_te15.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:211432` supports the identifier, label, `SPECIES` rank, `NCBITaxon:196869` parent, genetic code `11`, and the NCBI-only source flag. `curation/seed_scope.tsv:312058` carries the matching one-source inclusion row, and `data/taxa/PATHS.tsv:2820` resolves the identifier to this YAML path.

## Evidence

The only `source_attestations` entry is a one-count `NCBITAXON` `NAME` assertion from the pinned 2026-09-13 NCBI snapshot.

## Completeness

Exact gitignore-independent searches over the full `data/raw/`, `data/atb/`, and `data/straininfo/` auxiliary source trees found no same-taxon rows for `NCBITaxon:1009009`. The absence of LPSN, GTDB, BacDive, GOLD, MediaDive, Madin, BactoTraits, AllTheBacteria, StrainInfo, and curator-added blocks is expected for this NCBI-only record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. After any source refresh that adds non-NCBI support for `NCBITaxon:1009009`, rerun `just seed-canary NCBITaxon:1009009`, `just validate`, `just validate-strict`, and `just verify-corpus`.

## Additional Notes

Live NCBI pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
