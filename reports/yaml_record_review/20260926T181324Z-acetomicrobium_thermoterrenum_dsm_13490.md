# YAML Record Review: Acetomicrobium thermoterrenum DSM 13490

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acetomicrobium_thermoterrenum_dsm_13490.yaml
- Started UTC: 2026-09-26T18:13:24Z
- Finished UTC: 2026-09-26T18:13:24Z
- Verdict: fail

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acetomicrobium_thermoterrenum_dsm_13490.yaml` |
| Identifier | `NCBITaxon:1120987` |
| Label | `Acetomicrobium thermoterrenum DSM 13490` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1120986` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:36046`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acetomicrobium_thermoterrenum_dsm_13490.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acetomicrobium_sp_uba5826.yaml data/taxa/bacteria/acetomicrobium_thermoterrenum.yaml data/taxa/bacteria/acetomicrobium_thermoterrenum_dsm_13490.yaml data/taxa/bacteria/acetonema_longum.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Found a generated strain record: 714 YAML lines, 10 lineage entries, 1 `skos:closeMatch` GTDB taxonomy mapping, 1 BacDive strain, 11 genome assemblies, 9 genome records, 27 related records, 2 exact synonyms, 1 xref, and 6 source attestations. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in seed, legacy-path, NCBI, path, GTDB, BacDive, MediaDive, Madin, BactoTraits, culture-collection, strain assembly, genome, related-record, BV-BRC, GOLD, NCBI Assembly, StrainInfo, and AllTheBacteria rows. |
| Bounded source scan | Found 1 seed row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:241962`, 1 GTDB closeMatch row, 1 BacDive row, 2 culture-collection rows, 1 native GOLD organism with 1 project and 1 analysis, 1 MediaDive row, 1 Madin row, 1 BactoTraits row, 9 raw assembly rows, 7 raw genome rows, 20 raw related-record rows, and 10 checked lineage entries with no missing rows or mismatches. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:1120987` resolves in the committed NCBI inventory to label
`Acetomicrobium thermoterrenum DSM 13490`, rank `STRAIN`, parent
`NCBITaxon:1120986`, exact synonym `Anaerobaculum thermoterrenum DSM 13490`,
genetic code `11`, and taxonomy snapshot `2026-09-13`. The record carries
those same NCBI identity fields and correctly lands in the `bacteria` path
bucket through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10
stored taxa, from `NCBITaxon:1` root through `NCBITaxon:1120986`
Acetomicrobium thermoterrenum. There are no retained old identifiers for this
target in the NCBI merge input.

## Evidence

The BacDive strain block is supported by `data/raw/bacdive_strains.tsv:17589`
for BacDive 17778, designation `RWcit2`, taxon `NCBITaxon:1120987`, LPSN
parent name `lpsn:793978`, and the ACM 5076 / DSM 13490 collection
identifiers. The native strain and genome tables preserve matching DSM 13490
genomes through BacDive, BV-BRC, GOLD, GTDB genome, NCBI Assembly, and
AllTheBacteria rows.

The GTDB taxonomy mapping is present in `data/raw/gtdb_mappings.tsv:4456`,
which maps the 5-genome species cluster
`GTDB:s__Acetomicrobium_thermoterrenum` to this strain with predicate
`skos:closeMatch`.

The seed event is supported by `curation/seed_scope.tsv:10988`, which records
`NCBITaxon:1120987` as added on `2026-09-12` with reason `attested rule:
Acetomicrobium thermoterrenum DSM 13490, 6 sources incl. NCBI`.

## Completeness

Most generated slots are populated at the expected granularity for the DSM
13490 strain. The bounded scan found the expected BacDive, native GOLD,
MediaDive, Madin, BactoTraits, culture-collection, genome, related-record, and
ATB evidence and found no direct LPSN, StrainInfo, NCBI type-material, or NCBI
merge row for this strain taxon.

The exception is GTDB identity scope: the local GTDB genome rows support the
`RS_GCF_900107215.1` genome and assembly links inside the strain block, but
the GTDB species-cluster identifier should not be promoted into an exact
strain synonym or bare strain xref.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

## Findings

- Blocker: 0
- Major: 1
- Minor: 0

Major: `GTDB:s__Acetomicrobium_thermoterrenum` is emitted as a
`skos:closeMatch`, bare xref, GTDB source attestation, and exact synonym
`Acetomicrobium thermoterrenum` for the strain-level target
`NCBITaxon:1120987`. The GTDB source row is a species cluster with 5 genomes,
so it overstates this single DSM 13490 strain as equivalent to the broader
GTDB cluster.

## Recommended Edits

1. Prevent GTDB species clusters from being asserted as strain-level
   `skos:closeMatch` identities when `data/raw/gtdb_mappings.tsv` is generated.
2. In `src/taxonmech/seed.py`, gate GTDB-to-`xrefs` and
   GTDB-to-`EXACT_SYNONYM` projection by NCBI rank so species-cluster labels
   cannot become exact synonyms on `STRAIN` records.
3. Regenerate `data/taxa/bacteria/acetomicrobium_thermoterrenum_dsm_13490.yaml`
   and confirm its GTDB genome rows for `RS_GCF_900107215.1` remain while the
   species-cluster `taxonomy_mappings`, xref, source attestation, and exact
   synonym are removed or downgraded.

## Follow-up Checks

- Re-run `just validate-strict data/taxa/bacteria/acetomicrobium_thermoterrenum_dsm_13490.yaml`
  after the GTDB mapping/projection fix.
- Re-run `just validate data/taxa/bacteria/acetomicrobium_thermoterrenum_dsm_13490.yaml`
  to confirm LinkML still accepts the regenerated record.
- Re-run an exact `rg --no-ignore --hidden` scan for
  `GTDB:s__Acetomicrobium_thermoterrenum` and `NCBITaxon:1120987` to verify
  only the strain-level identity projection changed.

## Additional Notes

This was a read-only generated-record review. It did not append a curation
event, promote `mapping_status`, write a history record, or touch the seeded
YAML.
