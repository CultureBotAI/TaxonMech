# YAML Record Review: Klebsiella sp. GQr7

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/klebsiella_sp_gqr7.yaml
- Started UTC: 2026-09-23T13:22:54Z
- Finished UTC: 2026-09-23T13:24:12Z
- Verdict: pass

## Target

`data/taxa/bacteria/klebsiella_sp_gqr7.yaml` is the generated `TaxonRecord` for `NCBITaxon:1009027`, label `Klebsiella sp. GQr7`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:2608929` `unclassified Klebsiella`.

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*klebsiella_sp_gqr7.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/klebsiella_sp_gqr7.yaml data/taxa/bacteria/morganella_sp_ivcfp4.yaml data/taxa/bacteria/proteus_sp_iicaz2.yaml data/taxa/bacteria/proteus_sp_viitmp5.yaml` | Passed for the 4-file batch |
| `just validate data/taxa/bacteria/klebsiella_sp_gqr7.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:211450` supports the identifier, label, `SPECIES` rank, `NCBITaxon:2608929` parent, genetic code `11`, and the NCBI-only source flag. `curation/seed_scope.tsv:312076` carries the matching one-source inclusion row, and `data/taxa/PATHS.tsv:2840` resolves the identifier to this YAML path.

## Evidence

The only `source_attestations` entry is a one-count `NCBITAXON` `NAME` assertion from the pinned 2026-09-13 NCBI snapshot.

## Completeness

Exact gitignore-independent searches over the full `data/raw/`, `data/atb/`, and `data/straininfo/` auxiliary source trees found no same-taxon rows for `NCBITaxon:1009027`. The absence of LPSN, GTDB, BacDive, GOLD, MediaDive, Madin, BactoTraits, AllTheBacteria, StrainInfo, and curator-added blocks is expected for this NCBI-only record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. After any source refresh that adds non-NCBI support for `NCBITaxon:1009027`, rerun `just seed-canary NCBITaxon:1009027`, `just validate`, `just validate-strict`, and `just verify-corpus`.

## Additional Notes

Live NCBI pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
