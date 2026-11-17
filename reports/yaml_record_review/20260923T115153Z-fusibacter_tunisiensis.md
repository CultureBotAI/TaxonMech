# YAML Record Review: Fusibacter tunisiensis
- Repository: TaxonMech
- Record: data/taxa/bacteria/fusibacter_tunisiensis.yaml
- Started UTC: 2026-09-23T11:51:53Z
- Finished UTC: 2026-09-23T11:51:53Z
- Verdict: pass

## Target

Reviewed `NCBITaxon:1008308`, the species record for `Fusibacter tunisiensis`, encoded at `data/taxa/bacteria/fusibacter_tunisiensis.yaml`.

## Validation

`just validate-strict data/taxa/bacteria/fusibacter_tunisiensis.yaml data/taxa/bacteria/bacterium_enrichment_culture_clone_d907_1.yaml data/taxa/bacteria/bacterium_enrichment_culture_clone_d907_10.yaml data/taxa/bacteria/bacterium_enrichment_culture_clone_d907_11.yaml` scanned the batch and returned 0 errors.

`just validate data/taxa/bacteria/fusibacter_tunisiensis.yaml` returned `No issues found`.

## Identity and Grounding

The accepted taxon is grounded to `NCBITaxon:1008308`, label `Fusibacter tunisiensis`, as an exact named species under genus `Fusibacter`.

The record carries the expected cross-source identity for the same species: LPSN `lpsn:789943`, GTDB `GTDB:s__Fusibacter_D_tunisiensis`, BacDive `bacdive:18033`, BV-BRC/PATRIC `patric:1008308.3`, IMG `img.taxon:2901118534`, type strain `BELH1`, culture collection accessions `DSM-24436` and `JCM-17481`, StrainInfo `straininfo.strain:402839`, ATB assembly `atb.assembly:202505.SAMN17619925`, and GOLD organism, analysis, and project identifiers for `DSM 24436` and `JCM 17481`.

## Evidence

Local pinned source rows support the species in `data/raw/ncbitaxon_taxa.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/ncbi_type_material.tsv`, `data/raw/bacdive_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/mediadive_taxa.tsv`, `data/raw/madin_taxa.tsv`, `data/raw/bactotraits_taxa.tsv`, `data/straininfo/strain_links.tsv`, `data/straininfo/assemblies.tsv`, `data/atb/assemblies.tsv`, and `data/atb/genome_links.tsv`.

An exact gitignore-independent ID search over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS row for `fusibacter_tunisiensis` and the expected same-taxon local source rows for `NCBITaxon:1008308`. A tab-bounded label search likewise resolved `Fusibacter tunisiensis` to the same local source set and ATB sample assembly.

## Completeness

The record includes the expected LPSN nomenclature, publication and sequence accessions, NCBI synonyms, type-strain material, culture collection mappings, GTDB species-cluster mapping, BacDive/BV-BRC/GOLD/NCBI/StrainInfo/ATB assemblies, GTDB/IMG/PATRIC/ATB genome records, and the BioProject, BioSample, GOLD, and StrainInfo related records visible in the pinned tables.

The MEDIADIVE, MADIN, and BACTOTRAITS rows for this taxon are represented at the source-attestation level as intended by the current TaxonMech projection.

## Findings

No curation findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

A gitignore-independent `find` of `reports/yaml_record_review` found no pre-existing report for `fusibacter_tunisiensis` before this report was written. Live external lookups were unavailable during this review; the local pinned NCBI, LPSN, GTDB, BacDive, GOLD, BV-BRC, ATB, StrainInfo, MediaDive, MADIN, and BacToTraits inputs were treated as authoritative.
