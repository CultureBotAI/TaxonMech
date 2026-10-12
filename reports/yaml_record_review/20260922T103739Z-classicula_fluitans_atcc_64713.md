# YAML Record Review: Classicula fluitans ATCC 64713

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/classicula_fluitans_atcc_64713.yaml`
- Started UTC: 2026-09-22T10:34:00Z
- Finished UTC: 2026-09-22T10:37:39Z
- Verdict: pass

## Target

Reviewed `data/taxa/eukaryota/classicula_fluitans_atcc_64713.yaml` for
`NCBITaxon:1397326`. The record is a generated `TaxonRecord` for the strain
`Classicula fluitans ATCC 64713` under species `NCBITaxon:203533`
`Classicula fluitans`; future changes belong in the maintained raw
inventories, `curation/seed_scope.tsv`, or the seeder rather than in this YAML
file.

## Validation

- `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*classicula_fluitans_atcc_64713.md' -print`
  returned no prior matching review report; the check used `find` on the
  ignored report directory, so ignored files were included.
- `sed -n '1,300p' data/taxa/eukaryota/classicula_fluitans_atcc_64713.yaml`
  read the whole target YAML before judgement.
- `just validate data/taxa/eukaryota/classicula_fluitans_atcc_64713.yaml`
  reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/classicula_fluitans_atcc_64713.yaml`
  scanned one record, found 0 errors, and wrote
  `reports/instance_validation_failures.tsv`.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/classicula_fluitans_atcc_64713.yaml`
  regenerated a bounded raw-source scan at
  `/private/tmp/classicula_fluitans_atcc_64713_scan.json`.
- `just validate-history` and `just verify-corpus` had already passed for this
  worktree snapshot. `just validate-products` was not applicable because this
  generated record has no `causal_graphs`.

## Identity and Grounding

- `identifier`, `label`, `rank`, `parent_taxon`, and `genetic_code` agree with
  `data/raw/ncbitaxon_taxa.tsv:343832`: `NCBITaxon:1397326`,
  `Classicula fluitans ATCC 64713`, `STRAIN`, parent `NCBITaxon:203533`, and
  genetic code `1`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a
  seeded NCBI strain record.
- The 13-entry root-to-species lineage was checked against retained
  `data/raw/ncbitaxon_taxa.tsv` rows; all ancestor IDs, labels, and ranks were
  present and no mismatches were found.
- `curation/seed_scope.tsv:59849` keeps this taxon in scope with the reason
  `attested rule: Classicula fluitans ATCC 64713, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the retained
  `data/raw/ncbitaxon_taxa.tsv` row and the recorded 2026-09-13 taxonomy
  snapshot.
- The GOLD source attestation with `assertion_count: 1` is supported by
  `data/raw/gold_organisms.tsv:9370` and by exact native GOLD rows: organism
  `Go0036615`, project `Gp0036615`, and one analysis project named
  `Classicula fluitans ATCC 64713 (P35)`.
- The only emitted synonym, `Naiadella fluitans ATCC 64713`, is the exact
  synonym from the retained NCBI row.

## Completeness

- Empty `nomenclature`, `taxonomy_mappings`, `strains`, `genome_assemblies`,
  `genome_records`, `replaces`, and `causal_graphs` slots are appropriate for
  this generated record: the bounded scan found no exact rows for this strain
  ID in the raw BacDive, strain assembly, strain genome, strain related-record,
  culture-collection, GTDB, LPSN, MediaDive, Madin, BactoTraits, StrainInfo,
  NCBI type-material, or NCBI merged-ID inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If a future BacDive, GOLD, LPSN, GTDB, or StrainInfo refresh
adds rows for `NCBITaxon:1397326`, rerun the focused seed canary for this ID,
then rerun
`just validate data/taxa/eukaryota/classicula_fluitans_atcc_64713.yaml`,
`just validate-strict data/taxa/eukaryota/classicula_fluitans_atcc_64713.yaml`,
and `just verify-corpus`.

## Additional Notes

- No source rows suggested a homonym, merged current identifier, or broader
  taxon accidentally standing in for `Classicula fluitans ATCC 64713`.
- This review was read-only. It did not edit the generated YAML, generated
  pages, history records, or GitHub state.
