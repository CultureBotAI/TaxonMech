# YAML Record Review: Claviceps purpurea

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/claviceps_purpurea.yaml`
- Started UTC: 2026-09-22T11:00:00Z
- Finished UTC: 2026-09-22T11:04:20Z
- Verdict: pass

## Target

Reviewed `data/taxa/eukaryota/claviceps_purpurea.yaml` for
`NCBITaxon:5111`. The record is a generated `TaxonRecord` for the species
`Claviceps purpurea` under `NCBITaxon:5110` `Claviceps`; future changes belong
in the maintained raw inventories, `curation/seed_scope.tsv`, or the seeder
rather than in this YAML file.

## Validation

- `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*claviceps_purpurea.md' -print`
  returned no prior matching review report; the check used `find` on the
  ignored report directory, so ignored files were included.
- `sed -n '1,320p' data/taxa/eukaryota/claviceps_purpurea.yaml` read the whole
  target YAML before judgement.
- `just validate data/taxa/eukaryota/claviceps_purpurea.yaml` reported
  `No issues found`.
- `just validate-strict data/taxa/eukaryota/claviceps_purpurea.yaml` scanned
  one record and exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/claviceps_purpurea.yaml`
  regenerated a bounded raw-source scan at
  `/private/tmp/claviceps_purpurea_scan.json`.
- `just validate-history` and `just verify-corpus` had already passed for this
  worktree snapshot. `just validate-products` was not applicable because this
  generated record has no `causal_graphs`.

## Identity and Grounding

- `identifier`, `label`, `rank`, `parent_taxon`, and `genetic_code` agree with
  `data/raw/ncbitaxon_taxa.tsv:2237`: `NCBITaxon:5111`,
  `Claviceps purpurea`, `SPECIES`, parent `NCBITaxon:5110`, and genetic code
  `1`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a
  seeded NCBI species record.
- The 16-entry root-to-genus lineage was checked against retained
  `data/raw/ncbitaxon_taxa.tsv` rows; all ancestor IDs, labels, and ranks were
  present and no mismatches were found.
- `curation/seed_scope.tsv:51938` keeps this taxon in scope with the reason
  `attested rule: Claviceps purpurea, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the retained
  `data/raw/ncbitaxon_taxa.tsv` row and the recorded 2026-09-13 taxonomy
  snapshot.
- The GOLD source attestation with `assertion_count: 23` is supported by
  `data/raw/gold_organisms.tsv:37502` and by complete exact native scans of
  `data/gold/organisms.jsonl.gz`, `data/gold/projects.jsonl.gz`, and
  `data/gold/analyses.jsonl.gz`, which found 23 organism rows, 23 project
  rows, and 23 downstream analysis-project rows for `NCBITaxon:5111`.
- All five emitted NCBI synonyms match the retained NCBI row: exact synonyms
  `Sphacelia segetum` and `Sphaeria purpurea`, plus three related synonyms.

## Completeness

- Empty `nomenclature`, `taxonomy_mappings`, `strains`, `genome_assemblies`,
  `genome_records`, `replaces`, and `causal_graphs` slots are appropriate for
  this generated record: the bounded scan found no exact rows for this taxon in
  the raw BacDive, strain assembly, strain genome, strain related-record,
  culture-collection, GTDB, LPSN, MediaDive, Madin, BactoTraits, NCBI
  type-material, or NCBI merged-ID inputs.
- The bounded scan found 33 exact StrainInfo strain records and 54 exact
  deposit rows under this NCBI ID, but no final raw strain rows. That is
  consistent with the current StrainInfo overlay, which only augments local
  BacDive-derived strains.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If a future BacDive, GOLD, LPSN, GTDB, or StrainInfo refresh
adds rows for `NCBITaxon:5111`, rerun the focused seed canary for this ID,
then rerun `just validate data/taxa/eukaryota/claviceps_purpurea.yaml`,
`just validate-strict data/taxa/eukaryota/claviceps_purpurea.yaml`, and
`just verify-corpus`.

## Additional Notes

- No source rows suggested a homonym, merged current identifier, or broader
  taxon accidentally standing in for `Claviceps purpurea`.
- This review was read-only. It did not edit the generated YAML, generated
  pages, history records, or GitHub state.
