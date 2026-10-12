# YAML Record Review: Neoscardovia arbecensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/neoscardovia_arbecensis.yaml`
- Started UTC: 2026-09-22T19:50:04Z
- Finished UTC: 2026-09-22T19:53:19Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004583` |
| Label | `Neoscardovia arbecensis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1730861` |
| LPSN name | `lpsn:790159` |
| Strain count | `1` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated NCBI species record under the genus `Neoscardovia`, with one BacDive strain row and no curator-authored causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/neoscardovia_arbecensis.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/bifidobacterium_sp_hmsh1.yaml data/taxa/bacteria/bifidobacterium_sp_hmsh2.yaml data/taxa/bacteria/bifidobacterium_sp_hmsh5.yaml data/taxa/bacteria/neoscardovia_arbecensis.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:1004583` is the pinned NCBI row for `Neoscardovia arbecensis`, rank `SPECIES`, parent `NCBITaxon:1730861`, genetic code `11`, and source set `ncbitaxon|bacdive|lpsn|mediadive|gold|bactotraits`. The root-first lineage agrees with the local NCBI parentage through `Actinomycetota`, `Actinomycetes`, `Bifidobacteriales`, `Bifidobacteriaceae`, and `Neoscardovia`.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity, lineage, and synonyms | `data/raw/ncbitaxon_taxa.tsv` carries the `NCBITaxon:1004583` species row with parent `NCBITaxon:1730861`, genetic code `11`, and the six seeded NCBI related synonyms: `Bifidobacterium sp. PG10`, `Bifidobacterium sp. PG18`, `Bifidobacterium sp. PG19`, `Bifidobacterium sp. PG22`, `Bifidobacterium sp. PG30`, and `Neoscardovia arbecensis Garcia-Aljaro et al. 2015`. |
| LPSN nomenclature | `data/raw/lpsn_names.tsv` maps `lpsn:790159` to `NCBITaxon:1004583`, marks `Neoscardovia arbecensis` as legitimate, validly published, and the correct name, lists authority `García-Aljaro et al. 2015`, type strain `kgmicrobe.strain:DSM-25737`, publication IDs `PMID:22824582`, `doi:10.1016/j.syapm.2012.06.007`, `doi:10.1099/ijsem.0.000464`, and accession `INSDC:JF519691`. |
| BacDive strain | `data/raw/bacdive_strains.tsv` has `kgmicrobe.strain:bacdive_1769`, BacDive ID `1769`, designation `PG10`, taxon `NCBITaxon:1004583`, LPSN `lpsn:790159`, and culture collection deposits `kgmicrobe.strain:CECT-8111` and `kgmicrobe.strain:DSM-25737`. |
| GOLD genome and related records | `data/raw/strain_genome_records.tsv` contains two IMG rows for `gold:Ga0679509` and `img.taxon:8131085032` matched through `DSM 25737`; `data/raw/strain_related_records.tsv` contains the paired GOLD analysis, organism, and project rows for `gold:Ga0679509`, `gold:Go0411417`, `gold:Go0614938`, and `gold:Gp0304986` that are embedded under the BacDive strain. |
| StrainInfo related records | `data/straininfo/strain_links.tsv` and `data/straininfo/related_records.tsv.gz` both carry the matched `DSM 25737` path through `straininfo.deposit:898774`; the related-record inventory also carries the source strain and deposit rows for `CECT 8111`/`straininfo.deposit:898773` with source taxon `NCBITaxon:240233`, which the generated YAML preserves explicitly on those rows. |
| Source attestations and scope | `data/raw/mediadive_taxa.tsv`, `data/raw/gold_organisms.tsv`, and `data/raw/bactotraits_taxa.tsv` contain the asserted source counts, and `curation/seed_scope.tsv` lists `NCBITaxon:1004583` as in scope by an `attested rule` with 6 sources including NCBI. |

## Completeness

The record includes the expected NCBI synonyms, the LPSN name, one BacDive strain, two GOLD IMG genome-record rows, eight GOLD related rows, and four StrainInfo strain/deposit related rows for the one listed BacDive strain. An exact, gitignore-independent `rg --no-ignore --hidden` scan over `data/raw/strain_assemblies.tsv`, `data/atb`, `data/straininfo/assemblies.tsv`, and `data/raw/gtdb_mappings.tsv` found no NCBI assembly, AllTheBacteria, StrainInfo assembly, or GTDB mapping rows for `kgmicrobe.strain:bacdive_1769`, `NCBITaxon:1004583`, or `Neoscardovia arbecensis`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:1004583`, `bacdive:1769`, `lpsn:790159`, `gold:Ga0679509`, or `straininfo.strain:394941`.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-neoscardovia_arbecensis.md'` check, which includes ignored report files, found no prior local report before this one was written. Live source lookups were unavailable during this run, so identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/bacdive_strains.tsv`, GOLD inventories, and `data/straininfo` snapshot.

The embedded `CECT 8111` StrainInfo related rows retain StrainInfo's own source taxon `NCBITaxon:240233`, which the pinned NCBI table identifies as the `Aeriscardovia` genus. Those rows are source-related identifiers under the BacDive strain and do not alter the target record's `NCBITaxon:1004583` identity or strain count.
