# YAML Record Review: Gardnerella vaginalis HMP9231

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/gardnerella_vaginalis_hmp9231.yaml
- Started UTC: 2026-09-27T16:18:41Z
- Finished UTC: 2026-09-27T16:18:41Z
- Verdict: fail

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/gardnerella_vaginalis_hmp9231.yaml` |
| Identifier | `NCBITaxon:1009464` |
| Label | `Gardnerella vaginalis HMP9231` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2702` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated GTDB- and MADIN-backed Gardnerella strain record, with
path pinned by `data/taxa/PATHS.tsv:3172`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/gardnerella_vaginalis_hmp9231.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/gardnerella_vaginalis_hmp9231.yaml data/taxa/bacteria/bacterium_kkc2.yaml data/taxa/bacteria/bacterium_kkc8.yaml data/taxa/bacteria/ochrobactrum_sp_kkc4.yaml` | Passed strict validation with 4 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found 84 YAML lines, 10 lineage entries, 1 GTDB closeMatch taxonomy mapping, 3 exact synonyms, 1 GTDB xref, 1 NCBITAXON, 1 GTDB, and 1 MADIN source attestation, 0 nomenclature entries, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1009464` in the expected seed, NCBI, GTDB mapping, `data/taxa/PATHS.tsv`, and generated target YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:211776`, 1 GTDB mapping row at `data/raw/gtdb_mappings.tsv:1125`, 1 MADIN row at `data/raw/madin_taxa.tsv:403`, 10 checked lineage entries, 2 raw assembly rows, 3 raw genome rows, 2 exact raw related-record rows, 1 native GOLD organism, project, and analysis row, and no exact BacDive, type-material, or NCBI merge row. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1009464` resolves to `Gardnerella vaginalis HMP9231`, rank
`STRAIN`, parent `NCBITaxon:2702`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches all 10 committed NCBI rows, ending at
`NCBITaxon:2702` Gardnerella vaginalis. The bounded scan found no NCBI merge
row and no retained old-id row.

## Evidence

The NCBI row supports the strain-rank HMP9231 identity, direct Gardnerella
vaginalis parent, two NCBI exact synonyms, and snapshot date. The seed event is
supported by `curation/seed_scope.tsv:36076`.

GTDB line 1125 supports the `skos:closeMatch` to
`GTDB:s__Bifidobacterium_vaginale` and its 115-genome attestation; MADIN line
403 supports the 3 trait assertions.

## Completeness

Native GOLD rows for `Go0005891` / `Gp0005891` are side evidence only: no GOLD
aggregate or normalized genome/strain row was retained.

The exception is raw HMP9231 genome evidence: exact target rows in
`strain_assemblies.tsv`, `strain_genome_records.tsv`, and
`strain_related_records.tsv` are keyed to `kgmicrobe.strain:bacdive_155873`,
whose BacDive and culture-collection strain rows are filed under
`NCBITaxon:309120` Dialister micraerophilus.

## Findings

- Blocker: 0
- Major: 1
- Minor: 0

Major: exact raw assembly, genome, and BV-BRC related-record rows for
`NCBITaxon:1009464` are emitted under the Dialister `kgmicrobe.strain`
`bacdive_155873`; the Gardnerella HMP9231 YAML has `strain_count: 0`, while
`data/taxa/bacteria/dialister_micraerophilus.yaml` now carries HMP9231 genome
rows at lines 918, 937, 946, 963, and 972.

## Recommended Edits

1. Fix the upstream strain linkage so Gardnerella HMP9231 assembly, genome,
   and BV-BRC related-record rows are not keyed to a Dialister BacDive strain.
2. Add a seeder guard that refuses strain child rows whose `taxon_id` is
   outside the filed BacDive strain's NCBI subtree.
3. Regenerate Gardnerella and Dialister records and rerun strict validation.

## Follow-up Checks

Re-check `data/taxa/bacteria/gardnerella_vaginalis_hmp9231.yaml` and
`data/taxa/bacteria/dialister_micraerophilus.yaml` after the source-link fix.

## Additional Notes

This was a read-only generated-record review; it did not append history or touch YAML.
GTDB and MADIN attestations are retained independently of the strain-link issue.
Native GOLD rows remain side evidence only.
The ignored report probe included gitignored files.
