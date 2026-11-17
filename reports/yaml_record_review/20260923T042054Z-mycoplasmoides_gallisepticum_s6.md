# YAML Record Review: Mycoplasmoides gallisepticum S6

- Repository: TaxonMech
- Record: `data/taxa/bacteria/mycoplasmoides_gallisepticum_s6.yaml`
- Started UTC: 2026-09-23T04:20:54Z
- Finished UTC: 2026-09-23T04:20:54Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1006581`
- Label: `Mycoplasmoides gallisepticum S6`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2096` / `Mycoplasmoides gallisepticum`
- PATHS row: `data/taxa/PATHS.tsv:2045` maps the identifier to `mycoplasmoides_gallisepticum_s6`.

## Validation

- `just validate-strict data/taxa/bacteria/mycoplasmoides_gallisepticum_s6.yaml data/taxa/bacteria/sporolactobacillus_sp_p3j.yaml data/taxa/bacteria/bacterium_5a_1.yaml data/taxa/bacteria/bacterium_60e.yaml` scanned all four files with zero errors.
- `just validate data/taxa/bacteria/mycoplasmoides_gallisepticum_s6.yaml` returned `No issues found`.

## Identity and Grounding

The NCBI side is grounded exactly to strain-level `NCBITaxon:1006581` and preserves the NCBI strain label, rank, bacterial domain, genetic code `4`, and direct parent species `NCBITaxon:2096`.

The YAML lineage follows the expected `Mycoplasmoides gallisepticum` branch: root -> cellular organisms -> Bacteria -> Bacillati -> Mycoplasmatota -> Mycoplasmoidales -> Mycoplasmoidaceae -> Mycoplasmoides -> Mycoplasmoides gallisepticum.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210706` is the local pinned NCBI row for `NCBITaxon:1006581`, with label `Mycoplasmoides gallisepticum S6`, rank `STRAIN`, parent `NCBITaxon:2096`, genetic code `4`, three NCBI exact synonyms, sources `ncbitaxon|gtdb|madin_etal`, and snapshot date `2026-09-13`.
- `data/raw/madin_taxa.tsv:363` contributes one Madin trait assertion for this strain.
- `data/raw/gtdb_mappings.tsv:1061` maps `GTDB:s__Mycoplasmoides_gallisepticum` to this NCBI strain as `skos:closeMatch` with `50` genomes. `data/raw/gtdb_species.tsv:123712` confirms that `s__Mycoplasmoides_gallisepticum` is a GTDB species cluster with the same `50`-genome count.
- Exact same-taxon searches over `data/raw`, `data/atb`, and `data/straininfo` found no ATB, StrainInfo, BacDive, LPSN, GOLD, or other auxiliary rows for this identifier, label, or slug beyond the NCBI, GTDB, and Madin rows listed above.

## Completeness

The direct NCBI synonyms and Madin count are projected. There are no local BacDive, LPSN, ATB, StrainInfo, or GOLD rows that would justify adding strain inventory entries, nomenclature entries, genome links, GOLD organism links, or deprecation metadata.

## Findings

### Major: GTDB species cluster is projected as an exact synonym and xref on an NCBI strain

`GTDB:s__Mycoplasmoides_gallisepticum` represents a 50-genome GTDB species cluster in `data/raw/gtdb_species.tsv:123712`, but the YAML attaches it to the single strain `NCBITaxon:1006581` via `skos:closeMatch`, an `xrefs` entry, and the exact synonym `Mycoplasmoides gallisepticum`. The GTDB concept is broader than `Mycoplasmoides gallisepticum S6`, so projecting its label as an exact synonym of the strain overstates the match.

## Recommended Edits

- Update `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py` so a GTDB species cluster that lands on an NCBI strain is not emitted as a strain-level exact synonym or exact-looking xref.
- Regenerate this record after that projection logic is corrected so the valid NCBI and Madin evidence stays in place but the broad GTDB species assertion is no longer exact on the strain.

## Follow-up Checks

- Re-run strict validation after regeneration and confirm `GTDB:s__Mycoplasmoides_gallisepticum` no longer contributes the exact synonym `Mycoplasmoides gallisepticum` on this strain record.
- Check nearby Mycoplasmoides strain records mapped to the same GTDB species cluster for the same projection error.

## Additional Notes

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `mycoplasmoides_gallisepticum_s6`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
