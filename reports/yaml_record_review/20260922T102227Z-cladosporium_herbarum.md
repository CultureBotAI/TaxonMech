# YAML Record Review: Cladosporium herbarum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/cladosporium_herbarum.yaml`
- Started UTC: 2026-09-22T10:18:00Z
- Finished UTC: 2026-09-22T10:22:27Z
- Verdict: pass

## Target

Reviewed `data/taxa/eukaryota/cladosporium_herbarum.yaml` for
`NCBITaxon:29918`. The record is a generated `TaxonRecord` for the species
`Cladosporium herbarum` under `NCBITaxon:5498` `Cladosporium`; future changes
belong in the maintained raw inventories, `curation/seed_scope.tsv`, or the
seeder rather than in this YAML file.

## Validation

- `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cladosporium_herbarum.md' -print`
  returned no prior matching review report; the check used `find` on the
  ignored report directory, so ignored files were included.
- `sed -n '1,260p' data/taxa/eukaryota/cladosporium_herbarum.yaml` read the
  whole target YAML before judgement.
- `just validate data/taxa/eukaryota/cladosporium_herbarum.yaml` reported
  `No issues found`.
- `just validate-strict data/taxa/eukaryota/cladosporium_herbarum.yaml`
  scanned one record, found 0 errors, and wrote
  `reports/instance_validation_failures.tsv`.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/cladosporium_herbarum.yaml`
  regenerated a bounded raw-source scan at
  `/private/tmp/cladosporium_herbarum_scan.json`.
- `just validate-history` and `just verify-corpus` had already passed for this
  worktree snapshot. `just validate-products` was not applicable because this
  generated record has no `causal_graphs`.

## Identity and Grounding

- `identifier`, `label`, `rank`, `parent_taxon`, and `genetic_code` agree with
  `data/raw/ncbitaxon_taxa.tsv:3306`: `NCBITaxon:29918`,
  `Cladosporium herbarum`, `SPECIES`, parent `NCBITaxon:5498`, and genetic
  code `1`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a
  seeded NCBI species record.
- The 16-entry root-to-genus lineage was checked against retained
  `data/raw/ncbitaxon_taxa.tsv` rows; all ancestor IDs, labels, and ranks were
  present and no mismatches were found.
- `curation/seed_scope.tsv:52229` keeps this taxon in scope with the reason
  `attested rule: Cladosporium herbarum, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the retained
  `data/raw/ncbitaxon_taxa.tsv` row and the recorded 2026-09-13 taxonomy
  snapshot.
- The GOLD source attestation with `assertion_count: 3` is supported by
  `data/raw/gold_organisms.tsv:29966`, which reports three directly filed GOLD
  organisms for `NCBITaxon:29918`; exact native GOLD scanning found two local
  organism rows, `Go0115658` and `Go0367710`, and two linked project rows.
- All 19 emitted NCBI synonyms match the retained NCBI row: nine exact synonyms
  and ten related synonyms, including the authority-bearing
  `Cladosporium herbarum (Pers.) Link, 1816`.
- `data/raw/ncbi_type_material.tsv:153208-153211` lists four culture-from-
  epitype designations for this NCBI taxon. The current generated taxon YAML
  does not expose NCBI type-material side-table rows as fields.

## Completeness

- Empty `nomenclature`, `taxonomy_mappings`, `strains`, `genome_assemblies`,
  `genome_records`, and `causal_graphs` slots are appropriate for this
  generated record: the bounded scan found no exact rows for this taxon in the
  raw BacDive, strain assembly, strain genome, strain related-record,
  culture-collection, GTDB, LPSN, MediaDive, Madin, or BactoTraits inputs.
- The bounded scan found 140 exact StrainInfo strain records and 169 exact
  deposit rows under this NCBI ID, but no final raw strain rows. That is
  consistent with the current StrainInfo overlay, which only augments local
  BacDive-derived strains.
- The side inventory `data/raw/ncbi_merged_ids.tsv` maps four retired IDs to
  `NCBITaxon:29918`, but none are retained rows in `data/raw/ncbitaxon_taxa.tsv`;
  the absence of `replaces` entries is therefore consistent with the generated
  record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If a future BacDive, GOLD, LPSN, GTDB, or StrainInfo refresh
adds rows for `NCBITaxon:29918`, rerun the focused seed canary for this ID,
then rerun `just validate data/taxa/eukaryota/cladosporium_herbarum.yaml`,
`just validate-strict data/taxa/eukaryota/cladosporium_herbarum.yaml`, and
`just verify-corpus`.

## Additional Notes

- No source rows suggested a homonym, merged current identifier, or broader
  taxon accidentally standing in for `Cladosporium herbarum`.
- This review was read-only. It did not edit the generated YAML, generated
  pages, history records, or GitHub state.
