# YAML Record Review: uncultured Telmatospirillum sp.

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/uncultured_telmatospirillum_sp.yaml
- Started UTC: 2026-09-23T12:58:54Z
- Finished UTC: 2026-09-23T13:01:00Z
- Verdict: pass

## Target

`data/taxa/bacteria/uncultured_telmatospirillum_sp.yaml` is the generated `TaxonRecord` for `NCBITaxon:1008884`, label `uncultured Telmatospirillum sp.`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:1008883` `environmental samples`.

The full target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*uncultured_telmatospirillum_sp.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/coprobacillus_cateniformis.yaml data/taxa/bacteria/catenibacterium_mitsuokai.yaml data/taxa/bacteria/uncultured_aestuariimicrobium_sp.yaml data/taxa/bacteria/uncultured_telmatospirillum_sp.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/bacteria/uncultured_telmatospirillum_sp.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:211415` supports the identifier, label, `SPECIES` rank, `NCBITaxon:1008883` parent, genetic code `11`, and the `ncbitaxon|gtdb` source flags. `curation/seed_scope.tsv:65978` carries the matching two-source inclusion row.

## Evidence

The GTDB mapping in `data/raw/gtdb_mappings.tsv:1113` maps `GTDB:s__DUZF01_sp903858635` to this NCBI placeholder as `skos:closeMatch` with three genomes, matching the record's `taxonomy_mappings`, `DUZF01 sp903858635` GTDB synonym, xref, and `GTDB` source attestation. `data/raw/gtdb_species.tsv:54015` supports the same three-genome GTDB source count.

## Completeness

Exact gitignore-independent searches over `data/atb/`, `data/straininfo/`, and the auxiliary `data/raw/` source files found no same-taxon LPSN, BacDive, GOLD, MediaDive, Madin, BactoTraits, AllTheBacteria, StrainInfo, merged-id, or dropped-source rows for `NCBITaxon:1008884`. The record's empty `strains`, `evidence`, `definition`, `discussions`, and `causal_graphs` slots are expected.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. After any source refresh that changes `GTDB:s__DUZF01_sp903858635`, rerun `just seed-canary NCBITaxon:1008884`, `just validate`, `just validate-strict`, and `just verify-corpus`.

## Additional Notes

Live NCBI and GTDB pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
