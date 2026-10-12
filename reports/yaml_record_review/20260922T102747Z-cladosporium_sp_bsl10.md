# YAML Record Review: Cladosporium sp. BSL10

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/cladosporium_sp_bsl10.yaml`
- Started UTC: 2026-09-22T10:23:00Z
- Finished UTC: 2026-09-22T10:27:47Z
- Verdict: pass

## Target

Reviewed `data/taxa/eukaryota/cladosporium_sp_bsl10.yaml` for
`NCBITaxon:1712568`. The record is a generated `TaxonRecord` for the NCBI
species-rank placeholder `Cladosporium sp. BSL10` under
`NCBITaxon:2614628` `unclassified Cladosporium`; future changes belong in the
maintained raw inventories, `curation/seed_scope.tsv`, or the seeder rather
than in this YAML file.

## Validation

- `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cladosporium_sp_bsl10.md' -print`
  returned no prior matching review report; the check used `find` on the
  ignored report directory, so ignored files were included.
- `sed -n '1,260p' data/taxa/eukaryota/cladosporium_sp_bsl10.yaml` read the
  whole target YAML before judgement.
- `just validate data/taxa/eukaryota/cladosporium_sp_bsl10.yaml` reported
  `No issues found`.
- `just validate-strict data/taxa/eukaryota/cladosporium_sp_bsl10.yaml`
  scanned one record, found 0 errors, and wrote
  `reports/instance_validation_failures.tsv`.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/cladosporium_sp_bsl10.yaml`
  regenerated a bounded raw-source scan at
  `/private/tmp/cladosporium_sp_bsl10_scan.json`.
- `just validate-history` and `just verify-corpus` had already passed for this
  worktree snapshot. `just validate-products` was not applicable because this
  generated record has no `causal_graphs`.

## Identity and Grounding

- `identifier`, `label`, `rank`, `parent_taxon`, and `genetic_code` agree with
  `data/raw/ncbitaxon_taxa.tsv:446385`: `NCBITaxon:1712568`,
  `Cladosporium sp. BSL10`, `SPECIES`, parent `NCBITaxon:2614628`, and genetic
  code `1`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a
  seeded NCBI species-rank placeholder.
- The 17-entry root-to-`unclassified Cladosporium` lineage was checked against
  retained `data/raw/ncbitaxon_taxa.tsv` rows; all ancestor IDs, labels, and
  ranks were present and no mismatches were found.
- `curation/seed_scope.tsv:61143` keeps this taxon in scope with the reason
  `attested rule: Cladosporium sp. BSL10, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the retained
  `data/raw/ncbitaxon_taxa.tsv` row and the recorded 2026-09-13 taxonomy
  snapshot.
- The GOLD source attestation with `assertion_count: 1` is supported by
  `data/raw/gold_organisms.tsv:14833` and by exact native GOLD rows: organism
  `Go0384501`, project `Gp0235608`, and one analysis project named
  `Preussia sp. BSL10`.
- The NCBI row has no exact, broad, or related synonyms, so the generated YAML
  correctly omits `synonyms`.

## Completeness

- Empty `nomenclature`, `taxonomy_mappings`, `strains`, `genome_assemblies`,
  `genome_records`, `replaces`, and `causal_graphs` slots are appropriate for
  this generated record: the bounded scan found no exact rows for this taxon in
  the raw BacDive, strain assembly, strain genome, strain related-record,
  culture-collection, GTDB, LPSN, MediaDive, Madin, BactoTraits, StrainInfo,
  NCBI type-material, or NCBI merged-ID inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If a future BacDive, GOLD, LPSN, GTDB, or StrainInfo refresh
adds rows for `NCBITaxon:1712568`, rerun the focused seed canary for this ID,
then rerun `just validate data/taxa/eukaryota/cladosporium_sp_bsl10.yaml`,
`just validate-strict data/taxa/eukaryota/cladosporium_sp_bsl10.yaml`, and
`just verify-corpus`.

## Additional Notes

- The native GOLD organism, project, and analysis names still use
  `Preussia sp. BSL10`; the TaxonMech record is nevertheless grounded to the
  current NCBI row for the same taxon ID.
- This review was read-only. It did not edit the generated YAML, generated
  pages, history records, or GitHub state.
