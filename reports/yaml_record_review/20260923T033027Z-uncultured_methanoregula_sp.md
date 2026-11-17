# YAML Record Review: uncultured Methanoregula sp.

- Repository: TaxonMech
- Record: data/taxa/archaea/uncultured_methanoregula_sp.yaml
- Started UTC: 2026-09-23T03:30:27Z
- Finished UTC: 2026-09-23T03:30:27Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005933`
- Label: `uncultured Methanoregula sp.`
- Rank: `SPECIES`
- Domain: `ARCHAEA`
- Parent: `NCBITaxon:511148` (`environmental samples`)
- Path registry row: `data/taxa/PATHS.tsv:1985`

## Validation

- `just validate-strict data/taxa/archaea/uncultured_methanoregula_sp.yaml data/taxa/bacteria/rickettsia_sp_cyrtu4s.yaml data/taxa/bacteria/rickettsia_sp_cyrtu57h.yaml data/taxa/bacteria/rickettsia_sp_cyha22s.yaml` passed across the four target files.
- `just validate data/taxa/archaea/uncultured_methanoregula_sp.yaml` passed.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-uncultured_methanoregula_sp.md'` found no prior report for this exact slug; `find` included ignored report files.

## Identity and Grounding

- The YAML `identifier`, `label`, `rank`, `parent_taxon`, archaeal domain, and bacterial genetic code match the pinned NCBI taxonomy row in `data/raw/ncbitaxon_taxa.tsv:210648`.
- The lineage places the taxon under `Methanoregula` and its environmental-samples placeholder node, matching the NCBI environmental identity.
- The YAML projects the 23 GTDB rows in `data/raw/gtdb_mappings.tsv:1017` through `data/raw/gtdb_mappings.tsv:1039`.
- All GTDB projections use `skos:broadMatch`, and every note marks the relationship as a pooled GTDB species placed under this broader NCBI environmental taxon.
- `grounding_status: EXACT` is appropriate because the record is grounded directly to `NCBITaxon:1005933`; the GTDB species clusters are explicitly weaker broad mappings rather than asserted synonyms.

## Evidence

- `curation/seed_scope.tsv:65972` keeps this taxon in scope through two attesting sources, NCBI and GTDB.
- The sole NCBI `source_attestations` entry names `NCBITAXON`, `NCBITaxon:1005933`, and the 2026-09-13 NCBI taxonomy snapshot, matching the pinned NCBI row.
- The GTDB `source_attestations` entry is anchored on the largest pooled mapping, `GTDB:s__Methanoregula_sp964409915` with four genomes, and its note points to the 22 further GTDB species in `taxonomy_mappings`.
- A gitignore-independent `rg --no-ignore --hidden` scan found no same-ID, same-label, or same-slug rows in `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, `data/raw/strain_related_records.tsv`, `data/atb`, or `data/straininfo`.

## Completeness

- The record has no strain assemblies, strain genome records, related strain records, culture-collection rows, ATB rows, or StrainInfo rows, which matches the local evidence found for `NCBITaxon:1005933` outside the GTDB taxonomy mappings.
- All 23 GTDB taxonomy mappings for `NCBITaxon:1005933` are present with their local genome counts: one four-genome species, one three-genome species, one two-genome species, and twenty one-genome species.
- `strain_count: 0` is consistent with the absence of local strain-level rows for this environmental-sample placeholder.

## Findings

- None.

## Recommended Edits

- None.

## Follow-up Checks

- Re-review the record if GTDB-to-NCBI mapping generation starts promoting pooled environmental mappings above `skos:broadMatch`.
- Re-review the record if local strain, ATB, or StrainInfo imports add rows for `NCBITaxon:1005933` or `uncultured Methanoregula sp.`.

## Additional Notes

- Live taxonomy services were not used; this review treats the pinned TaxonMech local source rows as the source of truth.
