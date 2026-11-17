# YAML Record Review: Metallosphaera cuprina

- Repository: TaxonMech
- Record: data/taxa/archaea/metallosphaera_cuprina.yaml
- Started UTC: 2026-09-23T03:47:32Z
- Finished UTC: 2026-09-23T03:47:32Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1006005`
- Label: `Metallosphaera cuprina`
- Rank: `SPECIES`
- Domain: `ARCHAEA`
- Parent: `NCBITaxon:41980` (`Metallosphaera`)
- Path registry row: `data/taxa/PATHS.tsv:2006`

## Validation

- `just validate-strict data/taxa/bacteria/buttiauxella_agrestis_atcc_33320.yaml data/taxa/archaea/metallosphaera_cuprina.yaml data/taxa/archaea/metallosphaera_cuprina_ar_4.yaml data/taxa/bacteria/priestia_megaterium_wsh_002.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/archaea/metallosphaera_cuprina.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-metallosphaera_cuprina.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, archaeal genetic code, and NCBI authority string match `data/raw/ncbitaxon_taxa.tsv:210668`.
- `data/raw/lpsn_names.tsv:26550` confirms `Metallosphaera cuprina` as a legitimate, validly published, correct species name with LPSN ID `lpsn:789502`.
- `data/raw/ncbi_type_material.tsv:484` through `data/raw/ncbi_type_material.tsv:489` list the type-strain designations represented on the LPSN-backed species record.

## Evidence

- `data/raw/bacdive_strains.tsv:83867` supplies BacDive strain `161630`, the JCM/CGMCC culture-collection IDs, and the type-strain flag.
- `data/raw/strain_assemblies.tsv:72188` and `data/raw/strain_assemblies.tsv:72189` supply the BacDive and GOLD assembly rows for the `Ar-4` type strain rolled up into the species payload.
- `data/raw/strain_genome_records.tsv:56403` through `data/raw/strain_genome_records.tsv:56405` supply the BacDive, GOLD/IMG, and BacDive/PATRIC genome records.
- `data/raw/strain_related_records.tsv:222982` through `data/raw/strain_related_records.tsv:222985` supply the GOLD BioProject, analysis, organism, and project related records.
- `data/raw/madin_taxa.tsv:354` supplies the one Madin trait assertion summarized by the `MADIN` source attestation.

## Completeness

- The species record has the expected LPSN nomenclature block, NCBI related synonym, LPSN xref, type strain, BacDive/GOLD child strain rollup, and NCBI/BacDive/LPSN/Madin source attestations.
- No GTDB taxonomy mapping is projected directly onto the species record; the only GTDB xref comes through the LPSN same-species row and does not create a species-cluster exact synonym.

## Findings

- No curation findings.

## Recommended Edits

- None.

## Follow-up Checks

- If child-strain payload generation is changed, keep `kgmicrobe.strain:bacdive_161630` attached to the parent species or add an explicit cross-link so the type-strain evidence remains visible from this record.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
