# YAML Record Review: Cladosporium sphaerospermum

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/cladosporium_sphaerospermum.yaml`
- Started UTC: 2026-09-22T10:29:00Z
- Finished UTC: 2026-09-22T10:32:56Z
- Verdict: pass

## Target

Reviewed `data/taxa/eukaryota/cladosporium_sphaerospermum.yaml` for
`NCBITaxon:92950`. The record is a generated `TaxonRecord` for the species
`Cladosporium sphaerospermum` under `NCBITaxon:5498` `Cladosporium`; future
changes belong in the maintained raw inventories, `curation/seed_scope.tsv`,
or the seeder rather than in this YAML file.

## Validation

- `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cladosporium_sphaerospermum.md' -print`
  returned no prior matching review report; the check used `find` on the
  ignored report directory, so ignored files were included.
- `sed -n '1,260p' data/taxa/eukaryota/cladosporium_sphaerospermum.yaml` read
  the whole target YAML before judgement.
- `just validate data/taxa/eukaryota/cladosporium_sphaerospermum.yaml`
  reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/cladosporium_sphaerospermum.yaml`
  scanned one record, found 0 errors, and wrote
  `reports/instance_validation_failures.tsv`.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/cladosporium_sphaerospermum.yaml`
  regenerated a bounded raw-source scan at
  `/private/tmp/cladosporium_sphaerospermum_scan.json`.
- `just validate-history` and `just verify-corpus` had already passed for this
  worktree snapshot. `just validate-products` was not applicable because this
  generated record has no `causal_graphs`.

## Identity and Grounding

- `identifier`, `label`, `rank`, `parent_taxon`, and `genetic_code` agree with
  `data/raw/ncbitaxon_taxa.tsv:15257`: `NCBITaxon:92950`,
  `Cladosporium sphaerospermum`, `SPECIES`, parent `NCBITaxon:5498`, and
  genetic code `1`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a
  seeded NCBI species record.
- The 16-entry root-to-genus lineage was checked against retained
  `data/raw/ncbitaxon_taxa.tsv` rows; all ancestor IDs, labels, and ranks were
  present and no mismatches were found.
- `curation/seed_scope.tsv:53541` keeps this taxon in scope with the reason
  `attested rule: Cladosporium sphaerospermum, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the retained
  `data/raw/ncbitaxon_taxa.tsv` row and the recorded 2026-09-13 taxonomy
  snapshot.
- The GOLD source attestation with `assertion_count: 2` is supported by
  `data/raw/gold_organisms.tsv:44615` and by exact native GOLD rows for
  organisms `Go0384346` and `Go0657851`, their two projects, and their two
  analysis-project rows.
- All four emitted NCBI related synonyms match the retained NCBI row:
  `Cladosporium sp. EXF732`, `Cladosporium sp. HKB21`,
  `Cladosporium sphaerospermum Penz.`, and
  `Cladosporium sphaerospermum Penzig, 1882`.
- `data/raw/ncbi_type_material.tsv:273580-273587` lists eight neotype or type
  material designations for this NCBI taxon. The current generated taxon YAML
  does not expose NCBI type-material side-table rows as fields.

## Completeness

- Empty `nomenclature`, `taxonomy_mappings`, `strains`, `genome_assemblies`,
  `genome_records`, and `causal_graphs` slots are appropriate for this
  generated record: the bounded scan found no exact rows for this taxon in the
  raw BacDive, strain assembly, strain genome, strain related-record,
  culture-collection, GTDB, LPSN, MediaDive, Madin, or BactoTraits inputs.
- The bounded scan found 112 exact StrainInfo strain records and 148 exact
  deposit rows under this NCBI ID, but no final raw strain rows. That is
  consistent with the current StrainInfo overlay, which only augments local
  BacDive-derived strains.
- The side inventory `data/raw/ncbi_merged_ids.tsv` maps three retired IDs to
  `NCBITaxon:92950`, but none are retained rows in `data/raw/ncbitaxon_taxa.tsv`;
  the absence of `replaces` entries is therefore consistent with the generated
  record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If a future BacDive, GOLD, LPSN, GTDB, or StrainInfo refresh
adds rows for `NCBITaxon:92950`, rerun the focused seed canary for this ID,
then rerun `just validate data/taxa/eukaryota/cladosporium_sphaerospermum.yaml`,
`just validate-strict data/taxa/eukaryota/cladosporium_sphaerospermum.yaml`,
and `just verify-corpus`.

## Additional Notes

- No source rows suggested a homonym, merged current identifier, or broader
  taxon accidentally standing in for `Cladosporium sphaerospermum`.
- This review was read-only. It did not edit the generated YAML, generated
  pages, history records, or GitHub state.
