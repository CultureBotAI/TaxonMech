# YAML Record Review: Classicula fluitans

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/classicula_fluitans.yaml`
- Started UTC: 2026-09-22T10:29:00Z
- Finished UTC: 2026-09-22T10:32:56Z
- Verdict: pass

## Target

Reviewed `data/taxa/eukaryota/classicula_fluitans.yaml` for
`NCBITaxon:203533`. The record is a generated `TaxonRecord` for the species
`Classicula fluitans` under `NCBITaxon:203532` `Classicula`; future changes
belong in the maintained raw inventories, `curation/seed_scope.tsv`, or the
seeder rather than in this YAML file.

## Validation

- `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*classicula_fluitans.md' -print`
  returned no prior matching review report; the check used `find` on the
  ignored report directory, so ignored files were included.
- `sed -n '1,260p' data/taxa/eukaryota/classicula_fluitans.yaml` read the
  whole target YAML before judgement.
- `just validate data/taxa/eukaryota/classicula_fluitans.yaml` reported
  `No issues found`.
- `just validate-strict data/taxa/eukaryota/classicula_fluitans.yaml` scanned
  one record, found 0 errors, and wrote `reports/instance_validation_failures.tsv`.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/classicula_fluitans.yaml`
  regenerated a bounded raw-source scan at
  `/private/tmp/classicula_fluitans_scan.json`.
- `just validate-history` and `just verify-corpus` had already passed for this
  worktree snapshot. `just validate-products` was not applicable because this
  generated record has no `causal_graphs`.

## Identity and Grounding

- `identifier`, `label`, `rank`, `parent_taxon`, and `genetic_code` agree with
  `data/raw/ncbitaxon_taxa.tsv:40196`: `NCBITaxon:203533`,
  `Classicula fluitans`, `SPECIES`, parent `NCBITaxon:203532`, and genetic
  code `1`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a
  seeded NCBI species record.
- The 12-entry root-to-genus lineage was checked against retained
  `data/raw/ncbitaxon_taxa.tsv` rows; all ancestor IDs, labels, and ranks were
  present and no mismatches were found.
- `curation/seed_scope.tsv:54479` keeps this taxon in scope with the reason
  `attested rule: Classicula fluitans, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the retained
  `data/raw/ncbitaxon_taxa.tsv` row and the recorded 2026-09-13 taxonomy
  snapshot.
- The GOLD source attestation with `assertion_count: 1` is supported by
  `data/raw/gold_organisms.tsv:19233`, which reports one directly filed GOLD
  organism for `NCBITaxon:203533`. The bounded scan found no exact organism,
  project, or analysis rows for this taxon in the native local
  `data/gold/*.jsonl.gz` files.
- Both emitted NCBI synonyms match the retained NCBI row: exact synonym
  `Naiadella fluitans` and related synonym
  `Classicula fluitans R. Bauer, Begerow, Oberw. & Marvanova, 2003`.

## Completeness

- Empty `nomenclature`, `taxonomy_mappings`, `strains`, `genome_assemblies`,
  `genome_records`, `replaces`, and `causal_graphs` slots are appropriate for
  this generated record: the bounded scan found no exact rows for this taxon in
  the raw BacDive, strain assembly, strain genome, strain related-record,
  culture-collection, GTDB, LPSN, MediaDive, Madin, BactoTraits, NCBI
  type-material, or NCBI merged-ID inputs.
- The bounded scan found one exact StrainInfo strain record and one exact
  deposit row under this NCBI ID, but no final raw strain rows. That is
  consistent with the current StrainInfo overlay, which only augments local
  BacDive-derived strains.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If a future BacDive, GOLD, LPSN, GTDB, or StrainInfo refresh
adds rows for `NCBITaxon:203533`, rerun the focused seed canary for this ID,
then rerun `just validate data/taxa/eukaryota/classicula_fluitans.yaml`,
`just validate-strict data/taxa/eukaryota/classicula_fluitans.yaml`, and
`just verify-corpus`.

## Additional Notes

- No source rows suggested a homonym, merged current identifier, or broader
  taxon accidentally standing in for `Classicula fluitans`.
- This review was read-only. It did not edit the generated YAML, generated
  pages, history records, or GitHub state.
