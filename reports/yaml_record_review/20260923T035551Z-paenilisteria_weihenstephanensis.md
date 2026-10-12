# YAML Record Review: Paenilisteria weihenstephanensis

- Repository: TaxonMech
- Record: data/taxa/bacteria/paenilisteria_weihenstephanensis.yaml
- Started UTC: 2026-09-23T03:55:51Z
- Finished UTC: 2026-09-23T03:55:51Z
- Verdict: pass with minor issues

## Target

- Identifier: `NCBITaxon:1006155`
- Label: `Paenilisteria weihenstephanensis`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:3373705` (`Paenilisteria`)
- Path registry row: `data/taxa/PATHS.tsv:2017`

## Validation

- `just validate-strict data/taxa/bacteria/paenilisteria_weihenstephanensis.yaml data/taxa/bacteria/dysgonomonas_sp_a1_2011.yaml data/taxa/bacteria/delftia_sp_a2_2011.yaml data/taxa/bacteria/delftia_sp_a3_2011.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/paenilisteria_weihenstephanensis.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-paenilisteria_weihenstephanensis.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, bacterial genetic code, exact NCBI synonym `Listeria weihenstephanensis`, and NCBI related synonyms match `data/raw/ncbitaxon_taxa.tsv:210679`.
- The record is grounded to the NCBI species `NCBITaxon:1006155`.
- `data/raw/lpsn_names.tsv:8714` confirms `Paenilisteria weihenstephanensis` is legitimate and validly published, but marks it as a synonym that is not recommended for medical use. The YAML preserves this with `validly_published: true`, `legitimate: true`, `is_correct_name: false`, and an explicit deprecation note.
- `data/raw/lpsn_names.tsv:27447` gives `Listeria weihenstephanensis` as the LPSN correct name, and the YAML keeps that as an LPSN-related synonym.
- `data/raw/gtdb_mappings.tsv:1056` maps the 3-genome GTDB species cluster `GTDB:s__Listeria_A_weihenstephanensis` to this same NCBI species as `skos:closeMatch`.

## Evidence

- `data/raw/bacdive_strains.tsv:22883` and `data/raw/bacdive_strains.tsv:22884` supply the two BacDive strains `WS 4560` and `WS 4615`.
- `data/raw/strain_assemblies.tsv:108318` through `data/raw/strain_assemblies.tsv:108326` and `data/raw/strain_genome_records.tsv:87130` through `data/raw/strain_genome_records.tsv:87144` account for the BacDive, BV-BRC, and GOLD assembly/genome evidence retained under `WS 4560`.
- `data/atb/strain_links.tsv:3509` and `data/atb/genome_links.tsv:15218` through `data/atb/genome_links.tsv:15225` supply the AllTheBacteria assembly linkage for BioSample `SAMN03349274`.
- `data/straininfo/strain_links.tsv:80485` through `data/straininfo/strain_links.tsv:80488` support the StrainInfo deposits for both BacDive strains.
- `data/raw/mediadive_taxa.tsv:45`, `data/raw/gold_organisms.tsv:162`, `data/raw/madin_taxa.tsv:357`, and `data/raw/bactotraits_taxa.tsv:31` supply the MediaDive, GOLD, Madin, and BactoTraits source-attestation counts.

## Completeness

- The record includes the expected NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD, Madin, and BactoTraits attestations for a source-rich species.
- The type strain and additional WS 4615 BacDive strain are represented, with genome assemblies, genome records, AllTheBacteria evidence, StrainInfo records, and GOLD related records where present locally.

## Findings

- Minor: the current NCBI label is an LPSN non-correct synonym of `Listeria weihenstephanensis`, which is explicitly recommended for medical use in `data/raw/lpsn_names.tsv:27447`. The YAML captures the deprecation, but downstream consumers need the LPSN nomenclature block to understand that `Paenilisteria weihenstephanensis` is not the preferred ICNP/medical display name.

## Recommended Edits

- None for this record if TaxonMech is intentionally preserving NCBI's current label while surfacing LPSN deprecation metadata.

## Follow-up Checks

- If display-name policy changes to prefer LPSN correct names for deprecated NCBI labels, regenerate and verify that `Listeria weihenstephanensis` becomes the preferred label while the NCBI taxon and Paenilisteria synonym remain reachable.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
