# YAML Record Review: Rickettsia sp. CyRtu43S

- Repository: TaxonMech
- Record: data/taxa/bacteria/rickettsia_sp_cyrtu43s.yaml
- Started UTC: 2026-09-23T03:32:53Z
- Finished UTC: 2026-09-23T03:32:53Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005939`
- Label: `Rickettsia sp. CyRtu43S`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2750824` (`unclassified spotted fever group`)
- Path registry row: `data/taxa/PATHS.tsv:1990`

## Validation

- `just validate-strict data/taxa/bacteria/rickettsia_sp_cyrtu43d.yaml data/taxa/bacteria/rickettsia_sp_cyrtu43s.yaml data/taxa/bacteria/rickettsia_sp_cyrtu43g.yaml data/taxa/bacteria/planococcus_halocryophilus_or1.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/rickettsia_sp_cyrtu43s.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-rickettsia_sp_cyrtu43s.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, and bacterial genetic code match the pinned NCBI taxonomy row in `data/raw/ncbitaxon_taxa.tsv:210653`.
- `grounding_status: EXACT` is appropriate because the record is grounded directly to the same `NCBITaxon:1005939` identifier named in its only source attestation.
- The lineage terminates at `Rickettsia`, `spotted fever group`, and `unclassified spotted fever group`, matching the placeholder identity of this `Rickettsia sp.` record.

## Evidence

- `curation/seed_scope.tsv:311365` keeps this taxon in scope through the NCBI-only attested rule for `Rickettsia sp. CyRtu43S`.
- The sole `source_attestations` entry names `NCBITAXON`, `NCBITaxon:1005939`, and the 2026-09-13 NCBI taxonomy snapshot, matching the pinned row.
- A gitignore-independent `rg --no-ignore --hidden` scan found no same-ID rows in `data/raw/gtdb_mappings.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
- A gitignore-independent `rg --no-ignore --hidden` scan found no same-ID, same-label, or same-slug rows in `data/atb` or `data/straininfo`.

## Completeness

- The record has no `alternative_names`, `taxonomy_mappings`, traits, strain assemblies, or related strain records, which is complete for the available NCBI-only local evidence.
- `strain_count: 0` is consistent with the absence of local strain assembly or strain-related raw rows for `NCBITaxon:1005939`.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review this record if ATB, StrainInfo, GTDB, assembly, or related-strain evidence is later imported for `NCBITaxon:1005939` or `Rickettsia sp. CyRtu43S`.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
