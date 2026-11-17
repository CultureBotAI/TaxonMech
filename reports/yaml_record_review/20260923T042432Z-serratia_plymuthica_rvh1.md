# YAML Record Review: Serratia plymuthica RVH1

- Repository: TaxonMech
- Record: `data/taxa/bacteria/serratia_plymuthica_rvh1.yaml`
- Started UTC: 2026-09-23T04:24:32Z
- Finished UTC: 2026-09-23T04:24:32Z
- Verdict: needs curation

## Target

- Identifier: `NCBITaxon:1006598`
- Label: `Serratia plymuthica RVH1`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:82996` / `Serratia plymuthica`
- PATHS row: `data/taxa/PATHS.tsv:2052` maps the identifier to `serratia_plymuthica_rvh1`.

## Validation

- `just validate-strict data/taxa/bacteria/uncultured_bacterium_a36.yaml data/taxa/bacteria/bacterium_6a_5.yaml data/taxa/bacteria/bacterium_8d_7.yaml data/taxa/bacteria/serratia_plymuthica_rvh1.yaml` completed successfully for this batch.
- `just validate data/taxa/bacteria/serratia_plymuthica_rvh1.yaml` returned `No issues found`.

## Identity and Grounding

The NCBI side is grounded exactly to strain-level `NCBITaxon:1006598` and preserves the NCBI strain label, rank, bacterial domain, genetic code `11`, and direct parent species `NCBITaxon:82996`.

The YAML lineage follows the expected `Serratia plymuthica` branch: root -> cellular organisms -> Bacteria -> Pseudomonadati -> Pseudomonadota -> Gammaproteobacteria -> Enterobacterales -> Yersiniaceae -> Serratia -> Serratia plymuthica.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210712` is the local pinned NCBI row for `NCBITaxon:1006598`, with label `Serratia plymuthica RVH1`, rank `STRAIN`, parent `NCBITaxon:82996`, two NCBI exact synonyms, sources `ncbitaxon|gtdb|madin_etal`, and snapshot date `2026-09-13`.
- `data/raw/madin_taxa.tsv:364` contributes one Madin trait assertion for this strain.
- `data/raw/gtdb_mappings.tsv:1062` maps `GTDB:s__Serratia_plymuthica` to this NCBI strain as `skos:closeMatch` with `40` genomes. `data/raw/gtdb_species.tsv:164682` confirms that `s__Serratia_plymuthica` is a GTDB species cluster with the same `40`-genome count.
- Exact same-taxon searches over `data/raw`, `data/atb`, and `data/straininfo` found no ATB, StrainInfo, BacDive, LPSN, GOLD, or other auxiliary rows for this identifier, label, or slug beyond the NCBI, GTDB, and Madin rows listed above.

## Completeness

The direct NCBI synonyms and Madin count are projected. There are no local BacDive, LPSN, ATB, StrainInfo, or GOLD rows that would justify adding strain inventory entries, nomenclature entries, genome links, GOLD organism links, or deprecation metadata.

## Findings

### Major: GTDB species cluster is projected as an exact synonym and xref on an NCBI strain

`GTDB:s__Serratia_plymuthica` represents a 40-genome GTDB species cluster in `data/raw/gtdb_species.tsv:164682`, but the YAML attaches it to the single strain `NCBITaxon:1006598` via `skos:closeMatch`, an `xrefs` entry, and the exact synonym `Serratia plymuthica`. The GTDB concept is broader than `Serratia plymuthica RVH1`, so projecting its label as an exact synonym of the strain overstates the match.

## Recommended Edits

- Update `data/raw/gtdb_mappings.tsv` generation and taxonomy-mapping/synonym projection in `src/taxonmech/seed.py` so a GTDB species cluster that lands on an NCBI strain is not emitted as a strain-level exact synonym or exact-looking xref.
- Regenerate this record after that projection logic is corrected so the valid NCBI and Madin evidence stays in place but the broad GTDB species assertion is no longer exact on the strain.

## Follow-up Checks

- Re-run strict validation after regeneration and confirm `GTDB:s__Serratia_plymuthica` no longer contributes the exact synonym `Serratia plymuthica` on this strain record.
- Check nearby Serratia strain records mapped to the same GTDB species cluster for the same projection error.

## Additional Notes

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `serratia_plymuthica_rvh1`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
