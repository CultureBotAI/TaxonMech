# YAML Record Review: Torulaspora franciscae

- Verdict: pass
- Target: `data/taxa/eukaryota/torulaspora_franciscae.yaml`
- Identifier: `NCBITaxon:53488`

## Target
Reviewed the complete 72-line YAML record for Torulaspora franciscae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `torulaspora_franciscae`.

## Validation
- `just validate data/taxa/eukaryota/torulaspora_franciscae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/torulaspora_delbrueckii.yaml data/taxa/eukaryota/torulaspora_franciscae.yaml data/taxa/eukaryota/torulaspora_gathmanii.yaml data/taxa/eukaryota/torulaspora_globosa.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 6762 retained `NCBITaxon:53488` as `Torulaspora franciscae` at rank `SPECIES`, with parent `NCBITaxon:4948`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:53488` on line 52869.
- The NCBI synonym columns supplied 0 exact synonyms, 0 broad synonyms, and 1 related synonym.
- All 13 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:53488`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:53488` on line 38138, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 1 analysis row, 1 organism row, and 1 project row for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 9 exact rows for `NCBITaxon:53488` across `CBS 2926`, `CBS:2926`, `IFO 1360`, `IFO:1360`, `JCM 3662`, `JCM:3662`, `NRRL Y-6686`, `NRRL:Y-6686`, and `NRRL:Y:6686`.
- BacDive found 0 exact rows. StrainInfo found 0 direct strain rows and 1 deposit row under `NCBITaxon:53488`; that deposit was carried by non-target strain record 64110 for `Torulaspora pretoriensis`.

## Completeness
- Generated strain tables had 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables had 0 target rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlays had 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
No YAML edits were made; this report records the read-only evidence review.
