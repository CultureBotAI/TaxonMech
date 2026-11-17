# YAML Record Review: Clostridium sp. NAN076

- Repository: TaxonMech
- Record: data/taxa/bacteria/clostridium_sp_nan076.yaml
- Started UTC: 2026-09-23T03:23:19Z
- Finished UTC: 2026-09-23T03:23:19Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005894`
- Label: `Clostridium sp. NAN076`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2614128` (`unclassified Clostridium`)
- Path registry row: `data/taxa/PATHS.tsv:1977`

## Validation

- `just validate-strict data/taxa/bacteria/clostridium_sp_nan076.yaml data/taxa/bacteria/clostridium_sp_nan123.yaml data/taxa/bacteria/bacillus_sp_3_10.yaml data/taxa/bacteria/kordiimonas_aestuarii.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/clostridium_sp_nan076.yaml` passed with no LinkML issues.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-clostridium_sp_nan076.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, and bacterial genetic code match the pinned NCBI taxonomy row in `data/raw/ncbitaxon_taxa.tsv:210640`.
- `grounding_status: EXACT` is appropriate because the record is grounded directly to the same `NCBITaxon:1005894` identifier named in its sole source attestation.
- The lineage terminates at `Clostridium` and `unclassified Clostridium`, matching the placeholder identity of this `Clostridium sp.` record.

## Evidence

- `curation/seed_scope.tsv:311356` keeps this taxon in scope through the NCBI-only attested rule for `Clostridium sp. NAN076`.
- The sole `source_attestations` entry names `NCBITAXON`, `NCBITaxon:1005894`, and the 2026-09-13 NCBI taxonomy snapshot, matching the pinned row.
- A gitignore-independent `rg --no-ignore --hidden` scan found no same-ID rows in `data/raw/gtdb_mappings.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
- A gitignore-independent `rg --no-ignore --hidden` scan found no same-ID, same-label, or same-slug rows in `data/atb` or `data/straininfo`.

## Completeness

- The record has no `alternative_names`, `taxonomy_mappings`, traits, strain assemblies, or related strain records, which is complete for the available NCBI-only local evidence.
- `strain_count: 0` is consistent with the absence of local strain assembly or strain-related raw rows for `NCBITaxon:1005894`.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review this record if ATB, StrainInfo, GTDB, assembly, or related-strain evidence is later imported for `NCBITaxon:1005894` or `Clostridium sp. NAN076`.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
