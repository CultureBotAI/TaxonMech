# YAML Record Review: Staphylococcus aureus subsp. aureus T0131

- Repository: TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_t0131.yaml`
- Started UTC: 2026-09-23T04:12:31Z
- Finished UTC: 2026-09-23T04:12:31Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1006543`
- Label: `Staphylococcus aureus subsp. aureus T0131`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1280` / `Staphylococcus aureus`
- PATHS row: `data/taxa/PATHS.tsv:2037` maps the identifier to `staphylococcus_aureus_subsp_aureus_t0131`.

## Validation

- `just validate-strict data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_t0131.yaml data/taxa/bacteria/klebsiella_michiganensis_kctc_1686.yaml data/taxa/bacteria/acetobacter_pasteurianus_nbrc_101655.yaml data/taxa/bacteria/uncultured_bacterium_pm4_2.yaml` completed successfully for this batch.
- `just validate data/taxa/bacteria/staphylococcus_aureus_subsp_aureus_t0131.yaml` returned `No issues found`.

## Identity and Grounding

The NCBI side is grounded exactly to strain-level `NCBITaxon:1006543` and preserves the NCBI strain label, rank, bacterial domain, genetic code `11`, and direct parent species `NCBITaxon:1280`.

The YAML lineage follows the expected `Staphylococcus aureus` branch: root -> cellular organisms -> Bacteria -> Bacillati -> Bacillota -> Bacilli -> Caryophanales -> Staphylococcaceae -> Staphylococcus -> Staphylococcus aureus.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210701` is the local pinned NCBI row for `NCBITaxon:1006543`, with label `Staphylococcus aureus subsp. aureus T0131`, rank `STRAIN`, parent `NCBITaxon:1280`, three NCBI exact synonyms, sources `ncbitaxon|gtdb|gold|madin_etal`, and snapshot date `2026-09-13`.
- `data/raw/gold_organisms.tsv:164` contributes one GOLD organism assertion for this strain.
- `data/raw/madin_taxa.tsv:358` contributes five Madin trait assertions for this strain.
- `data/raw/gtdb_mappings.tsv:1057` maps `GTDB:s__Staphylococcus_aureus` to this NCBI strain as `skos:closeMatch` with `19502` genomes. `data/raw/gtdb_species.tsv:168198` confirms that `s__Staphylococcus_aureus` is a GTDB species cluster with the same `19502`-genome count.
- Exact same-taxon searches over `data/raw`, `data/atb`, and `data/straininfo` found no ATB, StrainInfo, BacDive, LPSN, or other auxiliary rows for this identifier, label, or slug beyond the NCBI, GTDB, GOLD, and Madin rows listed above.

## Completeness

The direct NCBI synonyms, GOLD count, and Madin count are all projected. There are no local BacDive, LPSN, ATB, or StrainInfo rows that would justify strain inventory entries, nomenclature entries, genome links, or deprecation metadata.

## Findings

### Major: GTDB species cluster is projected as an exact synonym and xref on an NCBI strain

`GTDB:s__Staphylococcus_aureus` represents a `19502`-genome GTDB species cluster in `data/raw/gtdb_species.tsv:168198`, but the YAML attaches it to the single strain `NCBITaxon:1006543` via `skos:closeMatch`, an `xrefs` entry, and the exact synonym `Staphylococcus aureus`. The GTDB concept is much broader than `Staphylococcus aureus subsp. aureus T0131`, so projecting its label as an exact synonym of the strain overstates the match.

## Recommended Edits

- Update `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py` so a GTDB species cluster that lands on an NCBI strain is not emitted as a strain-level exact synonym or exact-looking xref.
- Regenerate this record after that projection logic is corrected so the valid NCBI, GOLD, and Madin evidence stays in place but the broad GTDB species assertion is no longer exact on the strain.

## Follow-up Checks

- Re-run strict validation after regeneration and confirm `GTDB:s__Staphylococcus_aureus` no longer contributes the exact synonym `Staphylococcus aureus` on this strain record.
- Check nearby Staphylococcus strain records mapped to the same GTDB species cluster for the same projection error.

## Additional Notes

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `staphylococcus_aureus_subsp_aureus_t0131`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
