# YAML Record Review: uncultured Aestuariimicrobium sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_aestuariimicrobium_sp.yaml
- Started UTC: 2026-09-23T12:58:54Z
- Finished UTC: 2026-09-23T13:01:00Z
- Verdict: pass

## Target

`data/taxa/bacteria/uncultured_aestuariimicrobium_sp.yaml` is the generated `TaxonRecord` for `NCBITaxon:1008882`, label `uncultured Aestuariimicrobium sp.`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:1008876` `environmental samples`.

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*uncultured_aestuariimicrobium_sp.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/coprobacillus_cateniformis.yaml data/taxa/bacteria/catenibacterium_mitsuokai.yaml data/taxa/bacteria/uncultured_aestuariimicrobium_sp.yaml data/taxa/bacteria/uncultured_telmatospirillum_sp.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/bacteria/uncultured_aestuariimicrobium_sp.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:211413` supports the identifier, label, `SPECIES` rank, `NCBITaxon:1008876` parent, genetic code `11`, and the NCBI-only source flag. `curation/seed_scope.tsv:312045` carries the matching one-source inclusion row, and the generated lineage reaches `Aestuariimicrobium` under the bacterial Propionibacteriaceae.

## Evidence

The only `source_attestations` entry is the expected one-count `NCBITAXON` `NAME` assertion from the pinned 2026-09-13 snapshot.

## Completeness

Exact gitignore-independent searches over the full `data/raw/`, `data/atb/`, and `data/straininfo/` auxiliary source trees found no same-taxon LPSN, GTDB, BacDive, GOLD, MediaDive, Madin, BactoTraits, AllTheBacteria, StrainInfo, merged-id, or dropped-source rows for `NCBITaxon:1008882`. The absence of optional sections is therefore expected for this uncultured NCBI-only placeholder.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. After any source refresh that adds non-NCBI support for `NCBITaxon:1008882`, rerun `just seed-canary NCBITaxon:1008882`, `just validate`, `just validate-strict`, and `just verify-corpus`.

## Additional Notes

Live NCBI pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
