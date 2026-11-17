# YAML Record Review: Maricurvus nonylphenolicus
- Repository: TaxonMech
- Record: data/taxa/bacteria/maricurvus_nonylphenolicus.yaml
- Started UTC: 2026-09-23T11:49:13Z
- Finished UTC: 2026-09-23T11:49:13Z
- Verdict: pass

## Target

Reviewed `NCBITaxon:1008307`, the species record for `Maricurvus nonylphenolicus`, encoded at `data/taxa/bacteria/maricurvus_nonylphenolicus.yaml`.

## Validation

`just validate-strict data/taxa/bacteria/pseudomonas_sp_dac9.yaml data/taxa/bacteria/fervidobacterium_thailandense.yaml data/taxa/bacteria/thermotoga_sp_fc1002.yaml data/taxa/bacteria/maricurvus_nonylphenolicus.yaml` scanned the batch and returned 0 errors.

`just validate data/taxa/bacteria/maricurvus_nonylphenolicus.yaml` returned `No issues found`.

## Identity and Grounding

The accepted taxon is grounded to `NCBITaxon:1008307`, label `Maricurvus nonylphenolicus`, as an exact named species in genus `Maricurvus`.

The YAML carries the expected cross-source identity for the same species: LPSN `lpsn:789784`, GTDB `GTDB:s__Maricurvus_nonylphenolicus`, BacDive `bacdive:162113`, BV-BRC/PATRIC `patric:1008307.3`, GOLD genome and project identifiers, IMG `img.taxon:8140692193`, type-strain material, culture collection accessions `JCM-17778` and `KCTC-23758`, and ATB assembly `atb.assembly:202505.SAMD00769374`.

## Evidence

Local pinned source rows support the species in `data/raw/ncbitaxon_taxa.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/ncbi_type_material.tsv`, `data/raw/bacdive_strains.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/strain_related_records.tsv`, `data/atb/strain_links.tsv`, `data/atb/genome_links.tsv`, and `data/atb/assemblies.tsv`.

An exact gitignore-independent `rg --no-ignore --hidden` search over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS row for `maricurvus_nonylphenolicus` and the expected same-taxon source rows for `NCBITaxon:1008307` and `Maricurvus nonylphenolicus`.

## Completeness

The record includes the expected type-strain material, culture collection mappings, assembly and genome references, GTDB species-cluster mapping, NCBI related synonyms `Maricurvus nonylphenolicus Iwaki et al. 2012`, `Maricurvus nonylphenolicus Iwaki et al. 2012 emend. Seo et al. 2015`, and `gamma proteobacterium KU41E`, and the related BioProject, BioSample, GOLD organism, GOLD study, and GOLD project identifiers visible in the local source tables.

No same-taxon LPSN, BacDive, GOLD, GTDB, BV-BRC, ATB, or StrainInfo row was left unapplied in the pinned sources inspected for this review.

## Findings

No curation findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

A gitignore-independent `find` of `reports/yaml_record_review` found no pre-existing report for `maricurvus_nonylphenolicus` before this report was written. Live external lookups were unavailable during this review; local pinned NCBI, LPSN, GTDB, BacDive, GOLD, BV-BRC, ATB, and StrainInfo tables were treated as authoritative.
