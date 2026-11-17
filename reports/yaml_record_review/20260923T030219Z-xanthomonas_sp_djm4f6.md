# YAML Record Review: Xanthomonas sp. DJM4F6

- Repository: TaxonMech
- Record: data/taxa/bacteria/xanthomonas_sp_djm4f6.yaml
- Started UTC: 2026-09-23T03:02:19Z
- Finished UTC: 2026-09-23T03:02:19Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005857`
- Label: `Xanthomonas sp. DJM4F6`
- Rank: `SPECIES`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:2643310` (`unclassified Xanthomonas`)
- Path registry row: `data/taxa/PATHS.tsv:1946`

## Validation

- `just validate-strict data/taxa/bacteria/xanthomonas_sp_djm4f1.yaml data/taxa/bacteria/xanthomonas_sp_djm4f6.yaml data/taxa/bacteria/paenibacillus_sp_jg_tb1.yaml data/taxa/bacteria/bacillus_sp_jg_tb2.yaml` passed with 4 files scanned, 0 files with errors, and 0 total error rows.
- `just validate data/taxa/bacteria/xanthomonas_sp_djm4f6.yaml` passed with no LinkML issues.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-xanthomonas_sp_djm4f6.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, and bacterial genetic code match the pinned NCBI taxonomy row in `data/raw/ncbitaxon_taxa.tsv:210609`.
- `grounding_status: EXACT` is appropriate because the record is grounded directly to the same `NCBITaxon:1005857` identifier named in its sole source attestation.
- The lineage terminates at `Xanthomonas` and `unclassified Xanthomonas`, matching the placeholder identity of this `Xanthomonas sp.` record.

## Evidence

- `curation/seed_scope.tsv:311325` keeps this taxon in scope through the NCBI-only attested rule for `Xanthomonas sp. DJM4F6`.
- The sole `source_attestations` entry names `NCBITAXON`, `NCBITaxon:1005857`, and the 2026-09-13 NCBI taxonomy snapshot, matching the pinned row.
- A gitignore-independent `rg --no-ignore --hidden` scan found no same-ID rows in `data/raw/gtdb_mappings.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
- A gitignore-independent `rg --no-ignore --hidden` scan found no same-ID, same-label, or same-slug rows in `data/atb` or `data/straininfo`.

## Completeness

- The record has no `alternative_names`, `taxonomy_mappings`, traits, strain assemblies, or related strain records, which is complete for the available NCBI-only local evidence.
- `strain_count: 0` is consistent with the absence of local strain assembly or strain-related raw rows for `NCBITaxon:1005857`.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review this record if ATB, StrainInfo, GTDB, assembly, or related-strain evidence is later imported for `NCBITaxon:1005857` or `Xanthomonas sp. DJM4F6`.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
