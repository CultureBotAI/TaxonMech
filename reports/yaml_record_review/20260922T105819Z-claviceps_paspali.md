# YAML Record Review: Claviceps paspali

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/claviceps_paspali.yaml`
- Started UTC: 2026-09-22T10:54:00Z
- Finished UTC: 2026-09-22T10:58:19Z
- Verdict: pass

## Target

Reviewed `data/taxa/eukaryota/claviceps_paspali.yaml` for `NCBITaxon:40601`.
The record is a generated `TaxonRecord` for the species `Claviceps paspali`
under `NCBITaxon:5110` `Claviceps`; future changes belong in the maintained
raw inventories, `curation/seed_scope.tsv`, or the seeder rather than in this
YAML file.

## Validation

- `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*claviceps_paspali.md' -print`
  returned no prior matching review report; the check used `find` on the
  ignored report directory, so ignored files were included.
- `sed -n '1,260p' data/taxa/eukaryota/claviceps_paspali.yaml` read the whole
  target YAML before judgement.
- `just validate data/taxa/eukaryota/claviceps_paspali.yaml` reported
  `No issues found`.
- `just validate-strict data/taxa/eukaryota/claviceps_paspali.yaml` scanned
  one record, found 0 errors, and wrote `reports/instance_validation_failures.tsv`.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/claviceps_paspali.yaml`
  regenerated a bounded raw-source scan at
  `/private/tmp/claviceps_paspali_scan.json`.
- `just validate-history` and `just verify-corpus` had already passed for this
  worktree snapshot. `just validate-products` was not applicable because this
  generated record has no `causal_graphs`.

## Identity and Grounding

- `identifier`, `label`, `rank`, `parent_taxon`, and `genetic_code` agree with
  `data/raw/ncbitaxon_taxa.tsv:4654`: `NCBITaxon:40601`,
  `Claviceps paspali`, `SPECIES`, parent `NCBITaxon:5110`, and genetic code
  `1`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a
  seeded NCBI species record.
- The 16-entry root-to-genus lineage was checked against retained
  `data/raw/ncbitaxon_taxa.tsv` rows; all ancestor IDs, labels, and ranks were
  present and no mismatches were found.
- `curation/seed_scope.tsv:52445` keeps this taxon in scope with the reason
  `attested rule: Claviceps paspali, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the retained
  `data/raw/ncbitaxon_taxa.tsv` row and the recorded 2026-09-13 taxonomy
  snapshot.
- The GOLD source attestation with `assertion_count: 3` is supported by
  `data/raw/gold_organisms.tsv:34614`, which counts GOLD organisms filed
  directly under `NCBITaxon:40601`; the native GOLD rows are `RRC-1481`,
  `ILB388`, and `ILB432`.
- Exact native GOLD scanning found three direct organism rows, three direct
  project rows, and two downstream analysis-project rows attached through
  `AP PROJECT GOLD IDS`.
- Both emitted NCBI related synonyms,
  `Claviceps paspali F. Stevens & J.G. Hall, 1910` and
  `paspalum staggers ergot`, match the retained NCBI row.

## Completeness

- Empty `nomenclature`, `taxonomy_mappings`, `strains`, `genome_assemblies`,
  `genome_records`, `replaces`, and `causal_graphs` slots are appropriate for
  this generated record: the bounded scan found no exact rows for this taxon in
  the raw BacDive, strain assembly, strain genome, strain related-record,
  culture-collection, GTDB, LPSN, MediaDive, Madin, BactoTraits, NCBI
  type-material, or NCBI merged-ID inputs.
- The bounded scan found 10 exact StrainInfo strain records and 23 exact
  deposit rows under this NCBI ID, but no final raw strain rows. That is
  consistent with the current StrainInfo overlay, which only augments local
  BacDive-derived strains.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If a future BacDive, GOLD, LPSN, GTDB, or StrainInfo refresh
adds rows for `NCBITaxon:40601`, rerun the focused seed canary for this ID,
then rerun `just validate data/taxa/eukaryota/claviceps_paspali.yaml`,
`just validate-strict data/taxa/eukaryota/claviceps_paspali.yaml`, and
`just verify-corpus`.

## Additional Notes

- GOLD evidence in this species record is direct for `NCBITaxon:40601`; the
  separate strain record `NCBITaxon:877506` is reviewed independently.
- This review was read-only. It did not edit the generated YAML, generated
  pages, history records, or GitHub state.
