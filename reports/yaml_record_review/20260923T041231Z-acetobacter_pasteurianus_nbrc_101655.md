# YAML Record Review: Acetobacter pasteurianus NBRC 101655

- Repository: TaxonMech
- Record: `data/taxa/bacteria/acetobacter_pasteurianus_nbrc_101655.yaml`
- Started UTC: 2026-09-23T04:12:31Z
- Finished UTC: 2026-09-23T04:12:31Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1006554`
- Label: `Acetobacter pasteurianus NBRC 101655`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:438` / `Acetobacter pasteurianus`
- PATHS row: `data/taxa/PATHS.tsv:2039` maps the identifier to `acetobacter_pasteurianus_nbrc_101655`.

## Validation

- `just validate-strict data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_t0131.yaml data/taxa/bacteria/klebsiella_michiganensis_kctc_1686.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_101655.yaml data/taxa/bacteria/uncultured_bacterium_pm4_2.yaml` completed successfully for this batch.
- `just validate data/taxa/bacteria/acetobacter_pasteurianus_nbrc_101655.yaml` returned `No issues found`.

## Identity and Grounding

The NCBI side is grounded exactly to strain-level `NCBITaxon:1006554` and preserves the NCBI strain label, rank, bacterial domain, genetic code `11`, and direct parent species `NCBITaxon:438`.

The YAML lineage follows the expected `Acetobacter pasteurianus` branch: root -> cellular organisms -> Bacteria -> Pseudomonadati -> Pseudomonadota -> Alphaproteobacteria -> Acetobacterales -> Acetobacteraceae -> Acetobacter -> Acetobacter pasteurianus.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210703` is the local pinned NCBI row for `NCBITaxon:1006554`, with label `Acetobacter pasteurianus NBRC 101655`, rank `STRAIN`, parent `NCBITaxon:438`, three NCBI exact synonyms, sources `ncbitaxon|gtdb|gold|madin_etal`, and snapshot date `2026-09-13`.
- `data/raw/gold_organisms.tsv:166` contributes three GOLD organism assertions for this strain.
- `data/raw/madin_taxa.tsv:360` contributes two Madin trait assertions for this strain.
- `data/raw/gtdb_mappings.tsv:1059` maps `GTDB:s__Acetobacter_pasteurianus` to this NCBI strain as `skos:closeMatch` with `31` genomes. `data/raw/gtdb_species.tsv:3318` confirms that `s__Acetobacter_pasteurianus` is a GTDB species cluster with the same `31`-genome count.
- Exact same-taxon searches over `data/raw`, `data/atb`, and `data/straininfo` found no ATB, StrainInfo, BacDive, LPSN, or other auxiliary rows for this identifier, label, or slug beyond the NCBI, GTDB, GOLD, and Madin rows listed above.

## Completeness

The direct NCBI synonyms, GOLD count, and Madin count are all projected. There are no local BacDive, LPSN, ATB, or StrainInfo rows that would justify strain inventory entries, nomenclature entries, genome links, or deprecation metadata.

## Findings

### Major: GTDB species cluster is projected as an exact synonym and xref on an NCBI strain

`GTDB:s__Acetobacter_pasteurianus` represents a `31`-genome GTDB species cluster in `data/raw/gtdb_species.tsv:3318`, but the YAML attaches it to the single strain `NCBITaxon:1006554` via `skos:closeMatch`, an `xrefs` entry, and the exact synonym `Acetobacter pasteurianus`. The GTDB concept is broader than `Acetobacter pasteurianus NBRC 101655`, so projecting its label as an exact synonym of the strain overstates the match.

## Recommended Edits

- Update `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py` so a GTDB species cluster that lands on an NCBI strain is not emitted as a strain-level exact synonym or exact-looking xref.
- Regenerate this record after that projection logic is corrected so the valid NCBI, GOLD, and Madin evidence stays in place but the broad GTDB species assertion is no longer exact on the strain.

## Follow-up Checks

- Re-run strict validation after regeneration and confirm `GTDB:s__Acetobacter_pasteurianus` no longer contributes the exact synonym `Acetobacter pasteurianus` on this strain record.
- Check nearby Acetobacter strain records mapped to the same GTDB species cluster for the same projection error.

## Additional Notes

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `acetobacter_pasteurianus_nbrc_101655`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
