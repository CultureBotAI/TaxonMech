# YAML Record Review: Sphingomonas sp. KC8

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/sphingomonas_sp_kc8.yaml
- Started UTC: 2026-10-03T04:19:00Z
- Finished UTC: 2026-10-03T04:19:00Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/sphingomonas_sp_kc8.yaml` |
| Identifier | `NCBITaxon:1030157` |
| Label | `Sphingomonas sp. KC8` |
| Class | `TaxonRecord` |
| Rank | `SPECIES` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:196159` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated Sphingomonas species record with NCBITaxon, GTDB, and
MADIN attestations, with path pinned by `data/taxa/PATHS.tsv:12528`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/sphingomonas_sp_kc8.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12528-12537` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 78 YAML lines, 10 lineage entries, 3 source attestations, 1 GTDB taxonomy mapping, 1 GTDB synonym, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Exact source scans | Found the expected NCBI row, GTDB species row, GTDB closeMatch row targeting `NCBITaxon:1030157`, MADIN row, seed row, and legacy page path; found no exact GOLD, StrainInfo, ATB, or ignored prior report for this stem. |
| First-column lineage scan | Found the 10 expected committed NCBI lineage rows, ending at `NCBITaxon:196159`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030157` resolves to label `Sphingomonas sp. KC8`, rank `SPECIES`,
direct parent `NCBITaxon:196159`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`unclassified Sphingomonas`. The YAML retains one GTDB-derived exact synonym
and one GTDB xref from `GTDB:s__Sphingomonas_E_sp002151445`.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220294` supports the species
identity, direct unclassified-Sphingomonas parent, genetic code, merged
NCBITaxon/GTDB/MADIN source set, empty NCBI synonym columns, and 2026-09-13
snapshot date. The seed event is supported by `curation/seed_scope.tsv:36128`.

`data/raw/gtdb_species.tsv:166689` and `data/raw/gtdb_mappings.tsv:1292`
support the `GTDB:s__Sphingomonas_E_sp002151445` xref, synonym,
`skos:closeMatch` mapping, and GTDB source attestation with 2 genomes.
`data/raw/madin_taxa.tsv:569` supports the MADIN trait attestation with 6
trait assertions for `NCBITaxon:1030157`.

The legacy page path at `curation/legacy_page_paths.tsv:728` is retained for
the target identifier. Exact source scans found no exact GOLD organism row,
StrainInfo row, or ATB row for `NCBITaxon:1030157`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, GTDB, MADIN, seed, and target
YAML inputs, and found no extra retained source rows or strain evidence for
this identifier.

The record has no local strain inventory, genome assembly, genome record, or
causal graph section; none is expected from the scanned inputs.

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
The direct parent is `NCBITaxon:196159`, unclassified Sphingomonas.
The GTDB mapping to `GTDB:s__Sphingomonas_E_sp002151445` is a close match.
The GTDB source attestation represents 2 genomes.
The MADIN source attestation represents 6 trait assertions.
No local strain inventory row is filed on this target.
No genome assembly or genome record section is expected.
No causal graph is expected.
The ignored report probe included gitignored files.
