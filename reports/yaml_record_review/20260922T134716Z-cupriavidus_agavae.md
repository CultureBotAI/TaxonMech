# YAML Record Review: Cupriavidus agavae

## Target

- Record: `data/taxa/bacteria/cupriavidus_agavae.yaml`
- Identifier: `NCBITaxon:1001822`
- Slug: `cupriavidus_agavae`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:106589` (`Cupriavidus`)

## Validation

- `just validate data/taxa/bacteria/cupriavidus_agavae.yaml`: passed.
- `just validate-strict data/taxa/bacteria/ochrobactrum_sp_relman_1999.yaml data/taxa/bacteria/cupriavidus_agavae.yaml data/taxa/bacteria/variovorax_sp_fr1.yaml data/taxa/bacteria/clostridium_sp_fgh.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The core NCBI identity is exact for `NCBITaxon:1001822` / `Cupriavidus agavae`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label` matches the pinned `data/raw/ncbitaxon_taxa.tsv` label.
- `parent_taxon: NCBITaxon:106589` matches the pinned NCBI parent, `Cupriavidus`.
- The lineage stays within Bacteria through `Pseudomonadota`, `Betaproteobacteria`, `Burkholderiales`, `Burkholderiaceae`, then `Cupriavidus`.
- `grounding_status: EXACT` is correct for the NCBI species seed itself.

## Evidence

The NCBI, LPSN, GTDB, BacDive, and GOLD attestations are keyed directly to `NCBITaxon:1001822`; their labels and assertion counts match the reviewed raw rows. The LPSN row `lpsn:8175` preserves the expected species name, authority, valid-publication flags, type-strain designations, publications, and `INSDC:HQ914245` sequence accession, and its linked `GTDB:s__Cupriavidus_agavae` species cluster accounts for the one-genome GTDB close match.

The one BacDive-derived strain `bacdive:167276` preserves the `ASC-9842` designation, the `CIP-110327` and `LMG-26414` culture collection identifiers, the BacDive and GOLD genome/assembly records, the AllTheBacteria assembly linked through `biosample:SAMN10872460`, the GOLD BioProject, BioSample, analysis, organism, and project records, and the StrainInfo strain/deposit rows for both culture-collection identifiers.

Exact `rg --no-ignore --hidden` searches over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, `data/straininfo`, and `data/atb` found the expected NCBI, LPSN, GTDB, BacDive, GOLD, culture-collection, StrainInfo, ATB, NCBI merged-ID, NCBI type-material, assembly, genome, and strain-related rows keyed to `NCBITaxon:1001822`.

## Completeness

`strain_count: 1` matches the single BacDive strain row, and the `Cupriavidus sp. ASC-9842` and `Cupriavidus sp. ASC-993` related synonyms preserve NCBI synonym evidence for alternate strain-associated names.

The record has no `equivalent_identifiers`, `comments`, or product-level sections. None are required by the reviewed local evidence.

## Findings

No findings.

## Recommended Edits

- None.

## Follow-up Checks

- None.

## Additional Notes

- The review used pinned local `data/raw/*.tsv`, `data/straininfo/*.tsv`, and `data/atb/*.tsv` snapshots rather than live source lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `cupriavidus_agavae` review.
