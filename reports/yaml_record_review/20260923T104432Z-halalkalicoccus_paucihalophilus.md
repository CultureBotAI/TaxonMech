# YAML Record Review: Halalkalicoccus paucihalophilus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/halalkalicoccus_paucihalophilus.yaml
- Started UTC: 2026-09-23T10:42:10Z
- Finished UTC: 2026-09-23T10:44:32Z
- Verdict: pass

## Target

Reviewed `data/taxa/archaea/halalkalicoccus_paucihalophilus.yaml`.

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1008153` |
| label | `Halalkalicoccus paucihalophilus` |
| rank | `SPECIES` |
| domain | `ARCHAEA` |
| parent | `NCBITaxon:332246` / `Halalkalicoccus` |
| generated status | Seeded from pinned source inventories in `data/raw/`, `data/atb/`, and `data/straininfo/` |

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-halalkalicoccus_paucihalophilus.md'` | Passed: no prior report for this stem; `find` inspected ignored report files. |
| `just validate-strict data/taxa/archaea/haloterrigena_sp_yim_93684.yaml data/taxa/archaea/haladaptatus_pallidirubidus.yaml data/taxa/archaea/halalkalicoccus_paucihalophilus.yaml data/taxa/archaea/haloterrigena_sp_yim_93792.yaml` | Passed: 4 files scanned, 0 files with errors, 0 total error rows. |
| `just validate data/taxa/archaea/halalkalicoccus_paucihalophilus.yaml` | Passed: LinkML validation reported no issues. |

`just validate-products` was skipped because this taxon has no `causal_graphs`. `just validate-history` was skipped because this read-only review did not add a history decision. The full-corpus `just verify-corpus` gate was skipped for this individual review batch because these reports do not edit generated taxon YAML.

## Identity and Grounding

The record consistently denotes the archaeal species `NCBITaxon:1008153`, `Halalkalicoccus paucihalophilus`.

- The curated identifier, label, rank, parent `NCBITaxon:332246`, genetic code `11`, related NCBI synonyms, and source list agree with `data/raw/ncbitaxon_taxa.tsv`.
- `data/raw/lpsn_names.tsv` links `lpsn:790810` to `NCBITaxon:1008153`, marks `Halalkalicoccus paucihalophilus` as a legitimate, validly published ICNP correct name, and supplies the `Liu et al. 2013` authority, two type-strain designations, two DOI references, `PMID:23338603`, and `INSDC:JF449426`.
- `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Halalkalicoccus_paucihalophilus` to this NCBI species with `skos:closeMatch`; `data/raw/gtdb_species.tsv` reports 1 genome for the same GTDB species, matching the record's GTDB attestation count.
- The single generated strain, `kgmicrobe.strain:bacdive_24084`, is backed by `data/raw/bacdive_strains.tsv` for BacDive ID `24084`, NCBI taxon `1008153`, LPSN name `lpsn:790810`, and the CCTCC, DSM, JCM, and YIM culture collection IDs listed in the record.

## Evidence

The source projection is internally supported.

- NCBI supplies the canonical label, parent, related synonyms, genetic code, and 2026-09-13 snapshot provenance.
- LPSN supplies the nomenclature block and the `lpsn:790810` xref.
- GTDB supplies the species-level taxonomy mapping and the DSM 24557 genome row `gtdb.genome:RS_GCF_001593955.1`.
- BacDive, BV-BRC, GOLD, GTDB, NCBI Assembly, and StrainInfo rows in `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, and `data/straininfo/` support the listed DSM 24557 assemblies, genome rows, BioProjects, BioSamples, GOLD records, and StrainInfo deposit records.
- `data/raw/mediadive_taxa.tsv` reports two MediaDive media for `NCBITaxon:1008153`, matching the MediaDive source attestation.

No live NCBI, LPSN, GTDB, BacDive, MediaDive, StrainInfo, or GOLD pages were used; the pinned local source rows are the reviewed source of truth for this generated record.

## Completeness

No consequential gaps were found.

- `strain_count: 1` matches the single BacDive strain row for `NCBITaxon:1008153`.
- `source_attestations` matches the same-taxon inventory counts: 1 NCBI name, 1 LPSN name, 1 GTDB genome, 1 BacDive strain, 2 MediaDive media, and 4 GOLD organisms.
- The exact `rg --no-ignore --hidden` searches over `data/raw/`, `data/atb/`, and `data/straininfo/` for `NCBITaxon:1008153`, the canonical label, and the projected NCBI synonyms found the expected raw and StrainInfo rows and no same-taxon ATB rows that the record failed to project.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No record-specific follow-up is needed. If LPSN, BacDive, GOLD, GTDB, NCBI Assembly, MediaDive, or StrainInfo snapshots change, rerun source seeding and validate the regenerated strain, related-record, and attestation blocks.

## Additional Notes

This review was read-only. Future fixes for nomenclature, GTDB mappings, strain rows, or source attestation counts belong in the upstream source transforms and `src/taxonmech/seed.py`, not in the generated YAML.
