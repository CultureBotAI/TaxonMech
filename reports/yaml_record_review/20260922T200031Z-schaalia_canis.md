# YAML Record Review: Schaalia canis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/schaalia_canis.yaml`
- Started UTC: 2026-09-22T19:57:28Z
- Finished UTC: 2026-09-22T20:00:31Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:100469` |
| Label | `Schaalia canis` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2529408` |
| LPSN name | `lpsn:798104` |
| GTDB mapping | `GTDB:s__Pauljensenia_canis` |
| Strain count | `3` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated NCBI species record with one typed GTDB species mapping, three BacDive strains, and no curator-authored causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/schaalia_canis.yaml` | Pass; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/taxa/bacteria/bifidobacterium_sp_pg2.yaml data/taxa/bacteria/bifidobacterium_sp_pg9.yaml data/taxa/bacteria/schleiferilactobacillus_perolens.yaml data/taxa/bacteria/schaalia_canis.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

`NCBITaxon:100469` is the pinned NCBI row for `Schaalia canis`, rank `SPECIES`, parent `NCBITaxon:2529408`, and genetic code `11`. The lineage follows NCBI through `Actinomycetota`, `Actinomycetes`, `Actinomycetales`, `Actinomycetaceae`, and `Schaalia`. The GTDB mapping to `GTDB:s__Pauljensenia_canis` is close, not equivalent, which matches the retained `Pauljensenia canis` GTDB synonym.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI identity, exact synonym, and related synonyms | `data/raw/ncbitaxon_taxa.tsv` has the species row, exact synonym `Actinomyces canis`, and related names `Actinomyces canis Hoyles et al. 2000`, `Actinomyces sp. CCUG 34479`, `Actinomyces sp. CCUG 41706`, and `Schaalia canis (Hoyles et al. 2000) Nouioui et al. 2018`. |
| LPSN nomenclature and synonym | `data/raw/lpsn_names.tsv` maps `lpsn:798104` to `NCBITaxon:100469`, marks `Schaalia canis` legitimate, validly published, and correct, lists type strains `CCUG 41706`, `CIP 106351`, and `DSM 15536`, and links the synonym `lpsn:772767` for `Actinomyces canis`. |
| GTDB mapping | `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Pauljensenia_canis` to `NCBITaxon:100469` with `skos:closeMatch` and 1 genome. |
| Strains and related identifiers | `data/raw/bacdive_strains.tsv` has `bacdive:180`, `bacdive:147912`, and `bacdive:155403`; `data/raw/strain_related_records.tsv` has the GOLD organism rows for the type strain, and `data/straininfo/strain_links.tsv` plus `data/straininfo/related_records.tsv.gz` have the StrainInfo strain, deposit, and nucleotide rows embedded under all three BacDive strains. |
| Source attestations and scope | `data/raw/mediadive_taxa.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` contain the asserted source counts, and `curation/seed_scope.tsv` lists `NCBITaxon:100469` as in scope by an `attested rule` with 8 sources including NCBI. |

## Completeness

The record includes the NCBI, LPSN, and GTDB synonyms, the one GTDB species mapping, all three BacDive rows, six GOLD organism rows for the type strain deposits, and StrainInfo deposit/sequence rows for the matched CCUG, CIP, and DSM deposits. The omitted `genome_assemblies`, `genome_records`, record-level `evidence`, `causal_graphs`, and discussion sections are complete for the inspected rows.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Re-run the focused `just validate` and `just validate-strict` checks after any future refresh that changes `NCBITaxon:100469`, `GTDB:s__Pauljensenia_canis`, `lpsn:798104`, or BacDive strains `180`, `147912`, and `155403`.

## Additional Notes

An exact `find reports/yaml_record_review -maxdepth 1 -type f -name '*-schaalia_canis.md'` check, which includes ignored report files, found no prior local report before this one was written. Live source lookups were unavailable during this run, so identity was checked against pinned `data/raw` and `data/straininfo` rows.
