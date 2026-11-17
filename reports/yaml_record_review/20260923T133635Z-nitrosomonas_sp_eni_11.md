# YAML Record Review: Nitrosomonas sp. ENI-11

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/nitrosomonas_sp_eni_11.yaml
- Started UTC: 2026-09-23T13:35:02Z
- Finished UTC: 2026-09-23T13:36:37Z
- Verdict: pass

## Target

`data/taxa/bacteria/nitrosomonas_sp_eni_11.yaml` is the generated `TaxonRecord` for `NCBITaxon:100906`, label `Nitrosomonas sp. ENI-11`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:2609265` `unclassified Nitrosomonas`.

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*nitrosomonas_sp_eni_11.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/vibrio_sp_06071e4.yaml data/taxa/bacteria/vibrio_sp_06071h4.yaml data/taxa/bacteria/nitrosomonas_sp_eni_11.yaml data/taxa/bacteria/vibrio_sp_06071sb4.yaml` | Passed for the 4-file batch |
| `just validate data/taxa/bacteria/nitrosomonas_sp_eni_11.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:17343` supports the identifier, label, `SPECIES` rank, `NCBITaxon:2609265` parent, genetic code `11`, and the NCBI-only source flag. `curation/seed_scope.tsv:143119` carries the matching one-source inclusion row, and `data/taxa/PATHS.tsv:2862` resolves the identifier to this YAML path.

## Evidence

The only `source_attestations` entry is a one-count `NCBITAXON` `NAME` assertion from the pinned 2026-09-13 NCBI snapshot.

## Completeness

The `NCBITaxon:100906` identifier was searched with a tab-anchored gitignore-independent pattern so nearby IDs such as `NCBITaxon:1009060` could not satisfy the check. Exact searches over the full `data/raw/`, `data/atb/`, and `data/straininfo/` auxiliary source trees found no same-taxon rows beyond the pinned NCBI and seed-scope rows, so the absence of LPSN, GTDB, BacDive, GOLD, MediaDive, Madin, BactoTraits, AllTheBacteria, StrainInfo, and curator-added blocks is expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. After any source refresh that adds non-NCBI support for `NCBITaxon:100906`, rerun `just seed-canary NCBITaxon:100906`, `just validate`, `just validate-strict`, and `just verify-corpus`.

## Additional Notes

Live NCBI pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
