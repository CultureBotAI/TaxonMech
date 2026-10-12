# YAML Record Review: Defluviitoga tunisiensis

- Repository: TaxonMech
- Record: `data/taxa/bacteria/defluviitoga_tunisiensis.yaml`
- Started UTC: 2026-09-23T04:16:57Z
- Finished UTC: 2026-09-23T04:16:57Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1006576`
- Label: `Defluviitoga tunisiensis`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1511648` / `Defluviitoga`
- PATHS row: `data/taxa/PATHS.tsv:2042` maps the identifier to `defluviitoga_tunisiensis`.

## Validation

- `just validate-strict data/taxa/bacteria/uncultured_bacterium_pm5.yaml data/taxa/bacteria/defluviitoga_tunisiensis.yaml data/taxa/bacteria/uncultured_bacterium_pm8_1.yaml data/taxa/bacteria/corynebacterium_ulcerans_05149.yaml` scanned all four files with zero errors.
- `just validate data/taxa/bacteria/defluviitoga_tunisiensis.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded exactly to the species `NCBITaxon:1006576` and preserves the seeded NCBI label, bacterial domain, genetic code `11`, and direct parent genus `NCBITaxon:1511648`.

The YAML lineage follows the expected `Defluviitoga` branch: root -> cellular organisms -> Bacteria -> Thermotogati -> Thermotogota -> Thermotogae -> Petrotogales -> Petrotogaceae -> Defluviitoga.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210704` is the local pinned NCBI row for `NCBITaxon:1006576`, with two NCBI related synonyms and sources `ncbitaxon|gtdb|bacdive|lpsn|mediadive|gold|madin_etal|bactotraits`.
- `data/raw/lpsn_names.tsv:26932` confirms `Defluviitoga tunisiensis` as a legitimate, validly published, correct LPSN species name with type-strain deposits `DSM 23805` and `JCM 17210`, publications, and sequence accession `INSDC:FR850164`.
- `data/raw/gtdb_mappings.tsv:1060` links `GTDB:s__Defluviitoga_tunisiensis` to this species as `skos:closeMatch`, and `data/raw/gtdb_species.tsv:54541` carries the same 28-genome species cluster.
- `data/raw/bacdive_strains.tsv:16888` and `data/raw/bacdive_strains.tsv:53140` provide the two BacDive strains projected into `strains`; the type strain has `DSM-23805` and `JCM-17210`, and the second strain has `DSM-29926`.
- The source counts line up with the raw inventory: `data/raw/mediadive_taxa.tsv:46` has two media, `data/raw/gold_organisms.tsv:167` has five GOLD organism assertions, `data/raw/madin_taxa.tsv:361` has seven Madin trait assertions, and `data/raw/bactotraits_taxa.tsv:32` has nineteen BactoTraits assertions.
- The sequence and related-record projections are backed by `data/raw/strain_assemblies.tsv:17161`, `data/raw/strain_assemblies.tsv:93639`, `data/raw/strain_assemblies.tsv:93640`, `data/raw/strain_genome_records.tsv:13371`, `data/raw/strain_genome_records.tsv:13372`, `data/raw/strain_related_records.tsv:273100` through `data/raw/strain_related_records.tsv:273107`, and exact StrainInfo deposit matches in `data/straininfo/strain_links.tsv:10557` and `data/straininfo/strain_links.tsv:72846`.

## Completeness

The YAML captures the correct LPSN name, type-strain designations, GTDB species-level mapping, two BacDive strains, strain genome links, GOLD organism links, StrainInfo deposit evidence, and the direct source counts. The extra NCBI `typematerial.dmp` rows at `data/raw/ncbi_type_material.tsv:507` through `data/raw/ncbi_type_material.tsv:512` repeat DSM/JCM/SulfLac type-material aliases already grounded by the LPSN/BacDive evidence and do not expose a missing projected field.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

No follow-up required for this record.

## Additional Notes

- Exact `find` checks against `reports/yaml_record_review` found no prior report for `defluviitoga_tunisiensis`; `find` includes ignored report files.
- Live NCBI/source lookups were not required; this review treats the pinned local source inventories as the source of truth.
