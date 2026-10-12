# YAML Record Review: Acholeplasma laidlawii PG-8A

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/acholeplasma_laidlawii_pg_8a.yaml
- Started UTC: 2026-09-26T19:08:00Z
- Finished UTC: 2026-09-26T19:08:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/acholeplasma_laidlawii_pg_8a.yaml` |
| Identifier | `NCBITaxon:441768` |
| Label | `Acholeplasma laidlawii PG-8A` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2148` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded record from the NCBI Taxonomy snapshot dated
2026-09-13. Its path is pinned by `data/taxa/PATHS.tsv:505745`, and all seeded
fields are owned by the seeder, `curation/seed_scope.tsv`, or upstream
kg-microbe inputs rather than the YAML file itself.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/acholeplasma_laidlawii_pg_8a.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict data/taxa/bacteria/acholeplasma_hippikon_atcc_29725.yaml data/taxa/bacteria/acholeplasma_laidlawii.yaml data/taxa/bacteria/acholeplasma_laidlawii_pg_8a.yaml data/taxa/bacteria/acholeplasma_oculi.yaml` | Passed the four-file strict batch with 0 files in error and 0 total error rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected compact generated shape: 84 YAML lines, 10 lineage entries, 3 source attestations, 0 nomenclature entries, 1 GTDB `skos:closeMatch` mapping, 3 exact synonyms, 1 xref, 0 BacDive strains, 0 genome assemblies, 0 genome records, 0 related records, and 0 causal graphs. |
| Exact `rg --no-ignore --hidden` source scan | Found this identifier in the expected `curation/seed_scope.tsv`, `data/raw/ncbitaxon_taxa.tsv`, `data/taxa/PATHS.tsv`, GTDB, Madin, and generated YAML rows; found no prior ignored report for this stem. |
| Bounded source scan | Found 1 matching `seed_scope.tsv` row, the NCBI row at `data/raw/ncbitaxon_taxa.tsv:97985`, 10 checked lineage entries with no missing rows or mismatches, 1 GTDB mapping row, 1 Madin row, 1 native GOLD organism/project/analysis set, 0 NCBI merge rows, and 0 direct LPSN, StrainInfo, BacDive, BactoTraits, MediaDive, normalized assembly, normalized genome, or normalized related-record rows. |

Not run: full-corpus gates such as `just verify-corpus`, `just validate-all`,
`just validate-history`, and `just validate-products`. This review did not edit
generated YAML or history and used the narrow per-record schema and source
checks above.

## Identity and Grounding

`NCBITaxon:441768` resolves in the committed NCBI inventory to label
`Acholeplasma laidlawii PG-8A`, rank `STRAIN`, parent `NCBITaxon:2148`,
genetic code `11`, and taxonomy snapshot `2026-09-13`. The record carries
those same identity fields and correctly lands in the `bacteria` path bucket
through `taxon_domain: BACTERIA`.

The lineage is root-first and matches the committed NCBI rows for all 10 stored
taxa, from `NCBITaxon:1` root through `NCBITaxon:2148` Acholeplasma laidlawii.
There are no retained old identifiers for this target in the NCBI merge input.

## Evidence

The `NCBITAXON` source attestation is supported by the raw NCBI row: source ID
`NCBITaxon:441768`, source label `Acholeplasma laidlawii PG-8A`,
`assertion_count: 1`, `assertion_unit: NAME`, and the 2026-09-13 snapshot note
all match.

The GTDB mapping is the committed `skos:closeMatch` row to
`GTDB:s__Acholeplasma_laidlawii` with `genome_count: 16`. The GTDB exact
synonym, 2 NCBI exact synonyms, 1 GTDB xref, and `MADIN` source attestation are
all direct rows for `NCBITaxon:441768`.

The bounded scan also found a native GOLD organism/project/analysis set for
the same NCBI taxon. It has no corresponding normalized
`data/raw/strain_*.tsv` rows, which matches the YAML's compact shape with
`strain_count: 0`.

The seed event is supported by `curation/seed_scope.tsv:32755`, which records
`NCBITaxon:441768` as added on `2026-09-12` with reason `attested rule:
Acholeplasma laidlawii PG-8A, 3 sources incl. NCBI`.

## Completeness

No consequential required claim is absent for this generated compact record.
The exact and bounded scans account for the expected NCBI, GTDB, Madin, and
generated YAML inputs, and found no NCBI merge, LPSN, BacDive, StrainInfo,
MediaDive, BactoTraits, AllTheBacteria, normalized assembly, normalized genome,
or normalized related-record row that would require an enriched YAML section.

An ignored-file-inclusive `find` under `reports/yaml_record_review` returned no
existing Markdown report for this stem before this report was written.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

This was a read-only generated-record review. It did not append a curation
event, promote `mapping_status`, write a history record, or touch the seeded
YAML.
