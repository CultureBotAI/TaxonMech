# YAML Record Review: uncultured Candidatus Neoarthromitus sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_candidatus_neoarthromitus_sp.yaml
- Started UTC: 2026-09-23T13:02:12Z
- Finished UTC: 2026-09-23T13:03:39Z
- Verdict: pass

## Target

`data/taxa/bacteria/uncultured_candidatus_neoarthromitus_sp.yaml` is the generated `TaxonRecord` for `NCBITaxon:1008890`, label `uncultured Candidatus Neoarthromitus sp.`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:1008889` `environmental samples`.

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*uncultured_candidatus_neoarthromitus_sp.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/uncultured_propionispora_sp.yaml data/taxa/bacteria/uncultured_candidatus_neoarthromitus_sp.yaml data/taxa/bacteria/burkholderia_sp_8b.yaml data/taxa/bacteria/clostridium_sp_mh18.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/bacteria/uncultured_candidatus_neoarthromitus_sp.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:211419` supports the identifier, label, `SPECIES` rank, `NCBITaxon:1008889` parent, genetic code `11`, and the `ncbitaxon|gtdb` source flags. `curation/seed_scope.tsv:65979` carries the matching two-source inclusion row.

## Evidence

`data/raw/gtdb_mappings.tsv:1114-1117` supports all four GTDB mapping entries. They are all `skos:broadMatch` rows and are correctly retained as pooled context; the largest, `GTDB:s__Dwaynesavagella_sp000270205`, has 29 genomes and supplies the `GTDB` source attestation while the other three are counted in the attestation note.

## Completeness

Exact gitignore-independent searches over `data/atb/`, `data/straininfo/`, and the auxiliary `data/raw/` source files found no same-taxon LPSN, BacDive, GOLD, MediaDive, Madin, BactoTraits, AllTheBacteria, StrainInfo, merged-id, or dropped-source rows for `NCBITaxon:1008890`. The record's empty `strains`, `evidence`, `definition`, `discussions`, and `causal_graphs` slots are expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. After any source refresh that changes the Dwaynesavagella GTDB pooling set, rerun `just seed-canary NCBITaxon:1008890`, `just validate`, `just validate-strict`, and `just verify-corpus`.

## Additional Notes

Live NCBI and GTDB pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
