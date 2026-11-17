# YAML Record Review: Nocardioides sp. CGMCC 1.09653

- Repository: TaxonMech
- Record: data/taxa/bacteria/nocardioides_sp_cgmcc_1_09653.yaml
- Started UTC: 2026-09-23T03:36:01Z
- Finished UTC: 2026-09-23T03:36:01Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005943`
- Label: `Nocardioides sp. CGMCC 1.09653`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2615069` (`unclassified Nocardioides`)
- Path registry row: `data/taxa/PATHS.tsv:1993`

## Validation

- `just validate-strict data/taxa/bacteria/nocardioides_sp_cgmcc_1_09653.yaml data/taxa/bacteria/nocardioides_szechwanensis.yaml data/taxa/bacteria/nocardioides_psychrotolerans.yaml data/taxa/bacteria/iranian_hemp_witches_broom_phytoplasma.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/nocardioides_sp_cgmcc_1_09653.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-nocardioides_sp_cgmcc_1_09653.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, and bacterial genetic code match the pinned NCBI taxonomy row in `data/raw/ncbitaxon_taxa.tsv:210656`.
- `grounding_status: EXACT` is appropriate because the record is grounded directly to the same `NCBITaxon:1005943` identifier named in its only source attestation.
- The lineage terminates at `Nocardioides` and `unclassified Nocardioides`, matching the placeholder identity of this `Nocardioides sp.` record.

## Evidence

- `curation/seed_scope.tsv:311367` keeps this taxon in scope through the NCBI-only attested rule for `Nocardioides sp. CGMCC 1.09653`.
- The sole `source_attestations` entry names `NCBITAXON`, `NCBITaxon:1005943`, and the 2026-09-13 NCBI taxonomy snapshot, matching the pinned row.
- A gitignore-independent `rg --no-ignore --hidden` scan found no same-ID rows in `data/raw/gtdb_mappings.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
- A gitignore-independent `rg --no-ignore --hidden` scan found no same-ID, same-label, or same-slug rows in `data/atb` or `data/straininfo`.

## Completeness

- The record has no `alternative_names`, `taxonomy_mappings`, traits, strain assemblies, or related strain records, which is complete for the available NCBI-only local evidence.
- `strain_count: 0` is consistent with the absence of local strain assembly or strain-related raw rows for `NCBITaxon:1005943`.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review this record if ATB, StrainInfo, GTDB, assembly, or related-strain evidence is later imported for `NCBITaxon:1005943` or `Nocardioides sp. CGMCC 1.09653`.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
