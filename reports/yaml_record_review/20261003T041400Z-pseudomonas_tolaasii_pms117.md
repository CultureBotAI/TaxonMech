# YAML Record Review: Pseudomonas tolaasii PMS117

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/pseudomonas_tolaasii_pms117.yaml
- Started UTC: 2026-10-03T04:14:00Z
- Finished UTC: 2026-10-03T04:14:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/pseudomonas_tolaasii_pms117.yaml` |
| Identifier | `NCBITaxon:1030145` |
| Label | `Pseudomonas tolaasii PMS117` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:29442` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated NCBITaxon strain record with NCBITaxon, GTDB, and MADIN
attestations, with path pinned by `data/taxa/PATHS.tsv:12526`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/pseudomonas_tolaasii_pms117.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12518-12527` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 87 YAML lines, 11 lineage entries, 3 source attestations, 1 GTDB taxonomy mapping, 3 synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Exact source scans | Found the expected NCBI row, GTDB species row, GTDB closeMatch row targeting `NCBITaxon:1030145`, MADIN row, seed row, and legacy page path; found no exact GOLD, StrainInfo, ATB, or ignored prior report for this stem. |
| First-column lineage scan | Found the 11 expected committed NCBI lineage rows, ending at `NCBITaxon:29442`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030145` resolves to label `Pseudomonas tolaasii PMS117`, rank
`STRAIN`, direct parent `NCBITaxon:29442`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`Pseudomonas tolaasii`. The YAML retains both NCBI strain-name synonyms from
the NCBI row and one GTDB-derived exact synonym from
`GTDB:s__Aquipseudomonas_tolaasii`.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220292` supports the strain
identity, Pseudomonas tolaasii parent, two NCBI synonyms, genetic code, merged
NCBITaxon/GTDB/MADIN source set, and 2026-09-13 snapshot date. The seed event
is supported by `curation/seed_scope.tsv:36127`.

`data/raw/gtdb_species.tsv:11939` and
`data/raw/gtdb_mappings.tsv:1291` support the
`GTDB:s__Aquipseudomonas_tolaasii` xref, synonym, `skos:closeMatch` mapping,
and GTDB source attestation with 20 genomes. `data/raw/madin_taxa.tsv:568`
supports the MADIN trait attestation for `NCBITaxon:1030145`.

The legacy page path at `curation/legacy_page_paths.tsv:727` is retained for
the target identifier. Exact source scans found no exact GOLD organism row,
StrainInfo row, or ATB row for `NCBITaxon:1030145`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, GTDB, MADIN, seed, and target
YAML inputs, and found no extra retained source rows or strain evidence for
this identifier.

The record is a strain-rank seeded taxon but has no local strain inventory,
genome assembly, genome record, or causal graph section; none is expected from
the scanned inputs.

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

This was a read-only generated-record review.
The direct parent is `NCBITaxon:29442`, Pseudomonas tolaasii.
The GTDB mapping to `GTDB:s__Aquipseudomonas_tolaasii` is a close match.
The GTDB source attestation represents 20 genomes.
The MADIN source attestation represents 1 trait assertion.
No local strain inventory row is filed on this target.
No genome assembly or genome record section is expected.
No causal graph is expected.
The ignored report probe included gitignored files.
