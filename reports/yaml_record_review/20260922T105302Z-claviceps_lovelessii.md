# YAML Record Review: Claviceps lovelessii

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/claviceps_lovelessii.yaml`
- Started UTC: 2026-09-22T10:49:00Z
- Finished UTC: 2026-09-22T10:53:02Z
- Verdict: pass

## Target

Reviewed `data/taxa/eukaryota/claviceps_lovelessii.yaml` for
`NCBITaxon:1806559`. The record is a generated `TaxonRecord` for the species
`Claviceps lovelessii` under `NCBITaxon:5110` `Claviceps`; future changes
belong in the maintained raw inventories, `curation/seed_scope.tsv`, or the
seeder rather than in this YAML file.

## Validation

- `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*claviceps_lovelessii.md' -print`
  returned no prior matching review report; the check used `find` on the
  ignored report directory, so ignored files were included.
- `sed -n '1,260p' data/taxa/eukaryota/claviceps_lovelessii.yaml` read the
  whole target YAML before judgement.
- `just validate data/taxa/eukaryota/claviceps_lovelessii.yaml` reported
  `No issues found`.
- `just validate-strict data/taxa/eukaryota/claviceps_lovelessii.yaml`
  scanned one record, found 0 errors, and wrote
  `reports/instance_validation_failures.tsv`.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/claviceps_lovelessii.yaml`
  regenerated a bounded raw-source scan at
  `/private/tmp/claviceps_lovelessii_scan.json`.
- `just validate-history` and `just verify-corpus` had already passed for this
  worktree snapshot. `just validate-products` was not applicable because this
  generated record has no `causal_graphs`.

## Identity and Grounding

- `identifier`, `label`, `rank`, `parent_taxon`, and `genetic_code` agree with
  `data/raw/ncbitaxon_taxa.tsv:472250`: `NCBITaxon:1806559`,
  `Claviceps lovelessii`, `SPECIES`, parent `NCBITaxon:5110`, and genetic code
  `1`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a
  seeded NCBI species record.
- The 16-entry root-to-genus lineage was checked against retained
  `data/raw/ncbitaxon_taxa.tsv` rows; all ancestor IDs, labels, and ranks were
  present and no mismatches were found.
- `curation/seed_scope.tsv:61289` keeps this taxon in scope with the reason
  `attested rule: Claviceps lovelessii, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the retained
  `data/raw/ncbitaxon_taxa.tsv` row and the recorded 2026-09-13 taxonomy
  snapshot.
- The GOLD source attestation with `assertion_count: 1` is supported by
  `data/raw/gold_organisms.tsv:15903` and by exact native GOLD rows: organism
  `Go0631391`, project `Gp0644819`, and one analysis project named
  `Claviceps lovelessii CCC 647`.
- All six emitted NCBI synonyms match the retained NCBI row: exact synonym
  `Sphacelia lovelessii` plus five related synonyms.

## Completeness

- Empty `nomenclature`, `taxonomy_mappings`, `strains`, `genome_assemblies`,
  `genome_records`, and `causal_graphs` slots are appropriate for this
  generated record: the bounded scan found no exact rows for this taxon in the
  raw BacDive, strain assembly, strain genome, strain related-record,
  culture-collection, GTDB, LPSN, MediaDive, Madin, BactoTraits, StrainInfo,
  or NCBI type-material inputs.
- The side inventory `data/raw/ncbi_merged_ids.tsv` maps three retired IDs to
  `NCBITaxon:1806559`, but none are retained rows in
  `data/raw/ncbitaxon_taxa.tsv`; the absence of `replaces` entries is
  therefore consistent with the generated record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If a future BacDive, GOLD, LPSN, GTDB, or StrainInfo refresh
adds rows for `NCBITaxon:1806559`, rerun the focused seed canary for this ID,
then rerun `just validate data/taxa/eukaryota/claviceps_lovelessii.yaml`,
`just validate-strict data/taxa/eukaryota/claviceps_lovelessii.yaml`, and
`just verify-corpus`.

## Additional Notes

- No source rows suggested a homonym, merged current identifier, or broader
  taxon accidentally standing in for `Claviceps lovelessii`.
- This review was read-only. It did not edit the generated YAML, generated
  pages, history records, or GitHub state.
