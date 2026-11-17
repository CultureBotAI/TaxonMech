# YAML Record Review: Cladosporium colombiae

- Repository: TaxonMech
- Record: `data/taxa/eukaryota/cladosporium_colombiae.yaml`
- Started UTC: 2026-09-22T10:12:00Z
- Finished UTC: 2026-09-22T10:16:53Z
- Verdict: pass

## Target

Reviewed `data/taxa/eukaryota/cladosporium_colombiae.yaml` for
`NCBITaxon:643907`. The record is a generated `TaxonRecord` for the species
`Cladosporium colombiae` under `NCBITaxon:5498` `Cladosporium`; future changes
belong in the maintained raw inventories, `curation/seed_scope.tsv`, or the
seeder rather than in this YAML file.

## Validation

- `find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TaxonMech/reports/yaml_record_review -maxdepth 1 -name '*cladosporium_colombiae.md' -print`
  returned no prior matching review report; the check used `find` on the
  ignored report directory, so ignored files were included.
- `sed -n '1,220p' data/taxa/eukaryota/cladosporium_colombiae.yaml` read the
  whole target YAML before judgement.
- `just validate data/taxa/eukaryota/cladosporium_colombiae.yaml` reported
  `No issues found`.
- `just validate-strict data/taxa/eukaryota/cladosporium_colombiae.yaml`
  scanned one record and exited successfully.
- `.venv/bin/python /private/tmp/taxonmech_bounded_scan.py data/taxa/eukaryota/cladosporium_colombiae.yaml`
  regenerated a bounded raw-source scan at
  `/private/tmp/cladosporium_colombiae_scan.json`.
- `just validate-history` and `just verify-corpus` had already passed for this
  worktree snapshot. `just validate-products` was not applicable because this
  generated record has no `causal_graphs`.

## Identity and Grounding

- `identifier`, `label`, `rank`, `parent_taxon`, and `genetic_code` agree with
  `data/raw/ncbitaxon_taxa.tsv` for `NCBITaxon:643907`:
  `Cladosporium colombiae`, `SPECIES`, parent `NCBITaxon:5498`, and genetic
  code `1`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a
  seeded NCBI species record.
- The 16-entry root-to-genus lineage was checked against retained
  `data/raw/ncbitaxon_taxa.tsv` rows; all ancestor IDs, labels, and ranks were
  present and no mismatches were found.
- `curation/seed_scope.tsv:56208` keeps this taxon in scope with the reason
  `attested rule: Cladosporium colombiae, 2 sources incl. NCBI`.

## Evidence

- The NCBI source attestation is supported by the retained
  `data/raw/ncbitaxon_taxa.tsv` row and the recorded 2026-09-13 taxonomy
  snapshot.
- The GOLD source attestation with `assertion_count: 1` is supported by
  `data/raw/gold_organisms.tsv:40261` and by exact native GOLD rows:
  organism `Go0647359`, project `Gp0683426`, and one analysis project named
  `Cladosporium colombiae VS AB III KN 4`.
- Both emitted NCBI related synonyms,
  `Cladosporium colombiae K. Schub. & Crous, 2009` and
  `Cladosporium sp. JZG-2009b`, match the retained NCBI row.
- `data/raw/ncbi_type_material.tsv:244149` and `:244150` list culture-from-
  holotype designations for this NCBI taxon. The current generated taxon YAML
  does not expose NCBI type-material side-table rows as fields.

## Completeness

- Empty `nomenclature`, `taxonomy_mappings`, `strains`, `genome_assemblies`,
  `genome_records`, `replaces`, and `causal_graphs` slots are appropriate for
  this generated record: the bounded scan found no exact rows for this taxon in
  the raw BacDive, strain assembly, strain genome, strain related-record,
  culture-collection, GTDB, LPSN, MediaDive, Madin, BactoTraits, StrainInfo,
  or NCBI merged-ID inputs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If a future BacDive, GOLD, LPSN, GTDB, or StrainInfo refresh
adds rows for `NCBITaxon:643907`, rerun the focused seed canary for this ID,
then rerun `just validate data/taxa/eukaryota/cladosporium_colombiae.yaml`,
`just validate-strict data/taxa/eukaryota/cladosporium_colombiae.yaml`, and
`just verify-corpus`.

## Additional Notes

- No source rows suggested a homonym, merged current identifier, or broader
  taxon accidentally standing in for `Cladosporium colombiae`.
- This review was read-only. It did not edit the generated YAML, generated
  pages, history records, or GitHub state.
