# YAML Record Review: Coprobacillus cateniformis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/coprobacillus_cateniformis.yaml
- Started UTC: 2026-09-23T12:58:54Z
- Finished UTC: 2026-09-23T13:01:00Z
- Verdict: pass

## Target

`data/taxa/bacteria/coprobacillus_cateniformis.yaml` is the generated `TaxonRecord` for `NCBITaxon:100884`, label `Coprobacillus cateniformis`, rank `SPECIES`, `taxon_domain: BACTERIA`, and parent `NCBITaxon:100883` `Coprobacillus`.

The full 1,158-line target file was read before judging. An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*coprobacillus_cateniformis.md' -print` check, which includes ignored review reports, returned no prior report for this stem before this file was written.

## Validation

| Check | Result |
|---|---|
| `just validate-strict data/taxa/bacteria/coprobacillus_cateniformis.yaml data/taxa/bacteria/catenibacterium_mitsuokai.yaml data/taxa/bacteria/uncultured_aestuariimicrobium_sp.yaml data/taxa/bacteria/uncultured_telmatospirillum_sp.yaml` | Passed: 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate data/taxa/bacteria/coprobacillus_cateniformis.yaml` | Passed: LinkML found no issues for this `TaxonRecord` |
| `just validate-products` | Skipped: no `causal_graphs` are present |
| `just validate-history` | Skipped: this read-only review did not create a `history/` event |
| `just verify-corpus` | Skipped for this report because no YAML was edited; an earlier full-corpus reproduction check over 625,960 records was clean |

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:17339` supports the NCBI identifier, label, `SPECIES` rank, `NCBITaxon:100883` parent, genetic code `11`, the NCBI synonym strings, and the `ncbitaxon|gtdb|bacdive|lpsn|gold|madin_etal` source flags. `curation/seed_scope.tsv:8899` carries the matching six-source inclusion row.

`data/raw/lpsn_names.tsv:16424` supports the LPSN name `lpsn:775119`, authority `Kageyama and Benno 2000`, correct-name status, the type-strain designations `CIP-106690`, `DSM-15921`, and `JCM-10604`, the DOI / PMID set, `INSDC:AB030219`, and the LPSN-side xref to `GTDB:s__Coprobacillus_cateniformis`.

## Evidence

The GTDB mappings at `data/raw/gtdb_mappings.tsv:1106-1108` account for the three `taxonomy_mappings` entries. The LPSN-linked `GTDB:s__Coprobacillus_cateniformis` cluster is kept as the primary GTDB attestation with 42 genomes, and the `Bacteroides_uniformis` and `Longibaculum_muris` entries are retained as pooled `skos:broadMatch` context.

The BacDive strain count is supported by three BacDive rows: two filed directly under `NCBITaxon:100884` at `data/raw/bacdive_strains.tsv:83232-83233`, plus `kgmicrobe.strain:bacdive_23017` filed under the descendant type-strain taxon `NCBITaxon:1297794`. The type strain has the expected `classified_as: NCBITaxon:1297794` and gathers its BacDive, NCBI Assembly, BV-BRC, GOLD, GTDB, AllTheBacteria, and StrainInfo genome evidence through the same culture-deposit identifiers.

`data/raw/gold_organisms.tsv:203` supports the `GOLD` attestation count of 27 organisms filed directly under the species, and `data/raw/madin_taxa.tsv:398` supports the single `MADIN` trait-assertion count. Exact gitignore-independent searches of `data/raw/mediadive_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, `data/raw/ncbi_merged_ids.tsv`, and `data/raw/dropped.tsv` found no direct same-taxon rows, so no direct MediaDive, BactoTraits, merged-id, or dropped-source block is missing.

## Completeness

The record reports `strain_count: 3`, lists all three BacDive strains represented by the pinned BacDive rows, and preserves uncapped genome and related-record evidence on the type strain rather than truncating at page-display boundaries. There are no curator-added `evidence`, `definition`, `discussions`, or `causal_graphs`, which is expected for a generated seeded record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No curation follow-up is required. If a future source refresh changes `lpsn:775119`, the `GTDB:s__Coprobacillus_cateniformis` mapping, or the `bacdive:23017` type-strain links, rerun `just seed-canary NCBITaxon:100884`, `just validate data/taxa/bacteria/coprobacillus_cateniformis.yaml`, `just validate-strict data/taxa/bacteria/coprobacillus_cateniformis.yaml`, and `just verify-corpus`.

## Additional Notes

Live NCBI, LPSN, GTDB, BacDive, and StrainInfo pages were unavailable for this batch; the pinned rows under `data/raw/`, `data/atb/`, and `data/straininfo/` were treated as the source of truth.
