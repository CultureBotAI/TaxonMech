# YAML Record Review: Fervidobacterium thailandense
- Repository: TaxonMech
- Record: data/taxa/bacteria/fervidobacterium_thailandense.yaml
- Started UTC: 2026-09-23T11:49:13Z
- Finished UTC: 2026-09-23T11:49:13Z
- Verdict: pass

## Target

Reviewed `NCBITaxon:1008305`, the species record for `Fervidobacterium thailandense`, encoded at `data/taxa/bacteria/fervidobacterium_thailandense.yaml`.

## Validation

`just validate-strict data/taxa/bacteria/pseudomonas_sp_dac9.yaml data/taxa/bacteria/fervidobacterium_thailandense.yaml data/taxa/bacteria/thermotoga_sp_fc1002.yaml data/taxa/bacteria/maricurvus_nonylphenolicus.yaml` scanned the batch and returned 0 errors.

`just validate data/taxa/bacteria/fervidobacterium_thailandense.yaml` returned `No issues found` on rerun.

## Identity and Grounding

The accepted taxon is grounded to `NCBITaxon:1008305`, label `Fervidobacterium thailandense`, as an exact named species in genus `Fervidobacterium`.

The YAML carries the expected cross-source identity for the same species: LPSN `lpsn:794921`, GTDB `GTDB:s__Fervidobacterium_A_thailandense`, BacDive `bacdive:133268`, BV-BRC/PATRIC `patric:1008305.3`, GOLD genome and project identifiers, IMG `img.taxon:2881251750`, type strain `FC2004`, and culture collection accessions `ATCC AA-2483`, `ATCC-BAA-2483`, and `JCM-18757`.

## Evidence

Local pinned source rows support the species in `data/raw/ncbitaxon_taxa.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/ncbi_type_material.tsv`, `data/raw/bacdive_strains.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/gtdb_mappings.tsv`, and `data/raw/strain_related_records.tsv`.

An exact gitignore-independent `rg --no-ignore --hidden` search over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS row for `fervidobacterium_thailandense` and the expected same-taxon source rows for `NCBITaxon:1008305` and `Fervidobacterium thailandense`.

## Completeness

The record includes the expected type-strain material, culture collection mappings, assembly and genome references, GTDB species-cluster mapping, NCBI exact synonym with authority, NCBI related synonym `Fervidobacterium sp. FC2004`, and related BioProject, BioSample, GOLD organism, GOLD study, and GOLD project identifiers visible in the local source tables.

No same-taxon LPSN, BacDive, GOLD, GTDB, BV-BRC, ATB, or StrainInfo row was left unapplied in the pinned sources inspected for this review.

## Findings

No curation findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

A gitignore-independent `find` of `reports/yaml_record_review` found no pre-existing report for `fervidobacterium_thailandense` before this report was written. Live external lookups were unavailable during this review; local pinned NCBI, LPSN, GTDB, BacDive, GOLD, BV-BRC, ATB, and StrainInfo tables were treated as authoritative.
