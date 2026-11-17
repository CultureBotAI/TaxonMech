# YAML Record Review: Haladaptatus pallidirubidus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/archaea/haladaptatus_pallidirubidus.yaml
- Started UTC: 2026-09-23T10:42:10Z
- Finished UTC: 2026-09-23T10:44:32Z
- Verdict: pass

## Target

Reviewed `data/taxa/archaea/haladaptatus_pallidirubidus.yaml`.

| Field | Value |
|---|---|
| identifier | `NCBITaxon:1008152` |
| label | `Haladaptatus pallidirubidus` |
| rank | `SPECIES` |
| domain | `ARCHAEA` |
| parent | `NCBITaxon:367188` / `Haladaptatus` |
| generated status | Seeded from pinned source inventories in `data/raw/`, `data/atb/`, and `data/straininfo/` |

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-haladaptatus_pallidirubidus.md'` | Passed: no prior report for this stem; `find` inspected ignored report files. |
| `just validate-strict data/taxa/archaea/haloterrigena_sp_yim_93684.yaml data/taxa/archaea/haladaptatus_pallidirubidus.yaml data/taxa/archaea/halalkalicoccus_paucihalophilus.yaml data/taxa/archaea/haloterrigena_sp_yim_93792.yaml` | Passed: 4 files scanned, 0 files with errors, 0 total error rows. |
| `just validate data/taxa/archaea/haladaptatus_pallidirubidus.yaml` | Passed: LinkML validation exited 0. |

`just validate-products` was skipped because this taxon has no `causal_graphs`. `just validate-history` was skipped because this read-only review did not add a history decision. The full-corpus `just verify-corpus` gate was skipped for this individual review batch because these reports do not edit generated taxon YAML.

## Identity and Grounding

The record consistently denotes the archaeal species `NCBITaxon:1008152`, `Haladaptatus pallidirubidus`.

- The curated identifier, label, rank, parent `NCBITaxon:367188`, genetic code `11`, exact synonym `Haladaptatus sp. YIM 90917`, related NCBI synonyms, and source list agree with `data/raw/ncbitaxon_taxa.tsv`.
- `data/raw/lpsn_names.tsv` links `lpsn:792656` to `NCBITaxon:1008152`, marks `Haladaptatus pallidirubidus` as a legitimate, validly published ICNP correct name, and supplies the `Liu et al. 2015` authority, two type-strain designations, two DOI references, `PMID:25190334`, and `INSDC:JF449425`.
- `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Haladaptatus_pallidirubidus` to this NCBI species with `skos:closeMatch`; `data/raw/gtdb_species.tsv` reports 3 genomes for the same GTDB species, matching the record's GTDB attestation count.
- The single generated strain, `kgmicrobe.strain:bacdive_162029`, is backed by `data/raw/bacdive_strains.tsv` for BacDive ID `162029`, NCBI taxon `1008152`, LPSN name `lpsn:792656`, and culture collection IDs `CCTCC-AB%202010454` and `JCM-17504`.

## Evidence

The source projection is internally supported.

- NCBI supplies the canonical label, parent, exact synonym, related synonyms, genetic code, and 2026-09-13 snapshot provenance.
- LPSN supplies the nomenclature block and the `lpsn:792656` xref.
- GTDB supplies the species-level taxonomy mapping and the JCM 17504 genome rows, including `gtdb.genome:RS_GCF_039544045.1` and `gtdb.genome:RS_GCF_042429455.1`.
- BacDive, BV-BRC, GOLD, GTDB, and NCBI Assembly rows in `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` support the listed assemblies, genomes, BioProjects, BioSamples, and GOLD related records for JCM 17504.

No live NCBI, LPSN, GTDB, BacDive, or GOLD pages were used; the pinned local source rows are the reviewed source of truth for this generated record.

## Completeness

No consequential gaps were found.

- `strain_count: 1` matches the single BacDive strain row for `NCBITaxon:1008152`.
- `source_attestations` matches the same-taxon inventory counts: 1 NCBI name, 1 LPSN name, 3 GTDB genomes, 1 BacDive strain, and 2 GOLD organisms.
- Exact `rg --no-ignore --hidden` searches over `data/raw/`, `data/atb/`, and `data/straininfo/` for `NCBITaxon:1008152`, the canonical label, and the projected NCBI synonyms found the expected raw rows and no same-taxon ATB or StrainInfo rows that the record failed to project.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No record-specific follow-up is needed. If LPSN, BacDive, GOLD, GTDB, or NCBI Assembly snapshots change, rerun source seeding and validate the regenerated strain and related-record blocks.

## Additional Notes

This review was read-only. Future fixes for nomenclature, GTDB mappings, strain rows, or source attestation counts belong in the upstream source transforms and `src/taxonmech/seed.py`, not in the generated YAML.
