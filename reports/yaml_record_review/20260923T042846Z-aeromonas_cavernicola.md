# YAML Record Review: Aeromonas cavernicola

- Repository: TaxonMech
- Record: `data/taxa/bacteria/aeromonas_cavernicola.yaml`
- Started UTC: 2026-09-23T04:28:46Z
- Finished UTC: 2026-09-23T04:28:46Z
- Verdict: pass with minor issues

## Target

- Identifier: `NCBITaxon:1006623`
- Label: `Aeromonas cavernicola`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:642` / `Aeromonas`
- PATHS row: `data/taxa/PATHS.tsv:2056` maps the identifier to `aeromonas_cavernicola`.

## Validation

- `just validate-strict data/taxa/bacteria/uncultured_bacterium_a42.yaml data/taxa/bacteria/uncultured_bacterium_a49.yaml data/taxa/bacteria/uncultured_bacterium_pm3.yaml data/taxa/bacteria/aeromonas_cavernicola.yaml` scanned all four files with zero errors.
- `just validate data/taxa/bacteria/aeromonas_cavernicola.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded exactly to species-level `NCBITaxon:1006623` and preserves the seeded NCBI label, species rank, bacterial domain, genetic code `11`, and direct parent genus `NCBITaxon:642`.

The YAML lineage follows the expected `Aeromonas` branch: root -> cellular organisms -> Bacteria -> Pseudomonadati -> Pseudomonadota -> Gammaproteobacteria -> Aeromonadales -> Aeromonadaceae -> Aeromonas.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210713` is the local pinned NCBI row for `NCBITaxon:1006623`, with three NCBI related synonyms, sources `ncbitaxon|gtdb|bacdive|gold`, and snapshot date `2026-09-13`.
- `data/raw/gtdb_mappings.tsv:1063` links `GTDB:s__Aeromonas_cavernicola` to this species as `skos:closeMatch`, and `data/raw/gtdb_species.tsv:5634` carries the same one-genome species cluster.
- `data/raw/bacdive_strains.tsv:23297` contributes the single BacDive strain, `bacdive:23545`, with the `CCM-7641`, `CECT-7862`, `DSM-24474`, and `MDC 2508` culture-collection IDs also indexed in `data/raw/culture_collection_strains.tsv`.
- `data/raw/strain_assemblies.tsv:110198` through `data/raw/strain_assemblies.tsv:110202`, `data/raw/strain_genome_records.tsv:88593` through `data/raw/strain_genome_records.tsv:88595`, and `data/raw/strain_related_records.tsv:318874` through `data/raw/strain_related_records.tsv:318885` back the BacDive, GTDB, NCBI Assembly, GOLD organism, BioProject, and BioSample links projected under the BacDive strain.
- `data/straininfo/strain_links.tsv:81338` through `data/straininfo/strain_links.tsv:81340` provide exact culture-identifier matches from `CECT 7862`, `CCM 7641`, and `DSM 24474` to `bacdive:23545`; their source-side NCBI taxon is the genus `NCBITaxon:642`, which is correctly retained only as source metadata.

## Completeness

The YAML captures the NCBI identity, related synonyms, one-genome GTDB species mapping, one BacDive strain, strain assemblies, GTDB/IMG/PATRIC genome records, GOLD organism links, and three StrainInfo deposit links. The extra NCBI type-material aliases at `data/raw/ncbi_type_material.tsv:513` through `data/raw/ncbi_type_material.tsv:522` overlap the same CCM, CECT, DSM, and MDC deposits; TaxonMech currently derives `is_type_strain` from LPSN, not from NCBI `typematerial.dmp`, and no local LPSN row is present for this taxon.

## Findings

### Minor: Seed history undercounts the listed source families

The structured `source_attestations` list correctly has four families: `NCBITAXON`, `GTDB`, `BACDIVE`, and `GOLD`. The generated `curation_history` prose lists all four but ends with `3 sources incl. NCBI`, so the count in that human-readable seed note is stale by one.

## Recommended Edits

- Fix the seed-history source-count string so it counts the same source families emitted in `source_attestations`.
- Regenerate this record after that text-only count is corrected.

## Follow-up Checks

- Re-run strict validation after regeneration and confirm the `source_attestations` set still contains `NCBITAXON`, `GTDB`, `BACDIVE`, and `GOLD`.

## Additional Notes

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `aeromonas_cavernicola`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
