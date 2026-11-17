# YAML Record Review: Clostridium sp. MH18

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/clostridium_sp_mh18.yaml
- Started UTC: 2026-09-23T13:02:12Z
- Finished UTC: 2026-09-23T13:03:39Z
- Verdict: pass

## Target

`data/taxa/bacteria/clostridium_sp_mh18.yaml` is the generated `TaxonRecord` for `NCBITaxon:1008895`, label `Clostridium sp. MH18`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:2614128` `unclassified Clostridium`.

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*clostridium_sp_mh18.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/uncultured_propionispora_sp.yaml data/taxa/bacteria/uncultured_candidatus_neoarthromitus_sp.yaml data/taxa/bacteria/burkholderia_sp_8b.yaml data/taxa/bacteria/clostridium_sp_mh18.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/bacteria/clostridium_sp_mh18.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:211421` supports the identifier, label, `SPECIES` rank, `NCBITaxon:2614128` parent, genetic code `11`, and the NCBI-only source flag. `curation/seed_scope.tsv:312048` carries the matching one-source inclusion row, and the generated lineage reaches `Clostridium` under bacterial Clostridiaceae.

## Evidence

The only `source_attestations` entry is a one-count `NCBITAXON` `NAME` assertion from the pinned 2026-09-13 NCBI snapshot.

## Completeness

Exact gitignore-independent searches over the full `data/raw/`, `data/atb/`, and `data/straininfo/` auxiliary source trees found no same-taxon LPSN, GTDB, BacDive, GOLD, MediaDive, Madin, BactoTraits, AllTheBacteria, StrainInfo, merged-id, or dropped-source rows for `NCBITaxon:1008895`. The absence of optional seeded and curator-added sections is expected for this NCBI-only record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. After any source refresh that adds non-NCBI support for `NCBITaxon:1008895`, rerun `just seed-canary NCBITaxon:1008895`, `just validate`, `just validate-strict`, and `just verify-corpus`.

## Additional Notes

Live NCBI pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
