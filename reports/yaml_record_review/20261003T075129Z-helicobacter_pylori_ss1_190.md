# YAML Record Review: Helicobacter pylori SS1_190

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/helicobacter_pylori_ss1_190.yaml
- Started UTC: 2026-10-03T07:51:29Z
- Finished UTC: 2026-10-03T07:51:29Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/helicobacter_pylori_ss1_190.yaml` |
| Identifier | `NCBITaxon:1031535` |
| Label | `Helicobacter pylori SS1_190` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:210` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated seeded `Helicobacter pylori` strain record with NCBI,
GTDB, and MADIN support, with path pinned by `data/taxa/PATHS.tsv:13066`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/helicobacter_pylori_ss1_190.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 9-file covered `data/taxa/PATHS.tsv:13058-13066` subset | Passed strict validation with 9 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 84 YAML lines, 10 lineage entries, 3 source attestations, 1 GTDB mapping, 3 synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1031535` in the expected seed, NCBI, GTDB, MADIN, and legacy page rows; found no exact GOLD, StrainInfo, ATB, BacDive, strain assembly, strain genome, or strain related-record row for this identifier. |
| Exact prior-report probe | Found no `*-helicobacter_pylori_ss1_190.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:210`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1031535` resolves to label `Helicobacter pylori SS1_190`, rank
`STRAIN`, direct parent `NCBITaxon:210`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, and taxonomy snapshot `2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`Helicobacter pylori`. The generated YAML retains the two NCBI exact synonyms
and the GTDB `s__Helicobacter_pylori` closeMatch synonym and xref.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220740` supports the strain
identity, direct `Helicobacter pylori` parent, genetic code, and two NCBI
synonyms. `data/raw/gtdb_mappings.tsv:1301` supports the GTDB mapping and xref,
and `data/raw/madin_taxa.tsv:576` supports the MADIN trait attestation.

The 2026-09-12 seed event is supported by `curation/seed_scope.tsv:36133`, and
the legacy path is supported by `curation/legacy_page_paths.tsv:736`.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for the expected NCBI, seed, GTDB, MADIN, and legacy
inputs, and found no extra retained strain, genome, GOLD, BacDive, StrainInfo,
or ATB source rows for this identifier.

The 84-line YAML shape is expected for this GTDB/MADIN-backed strain record; no
strain, genome assembly, genome record, related-record, or causal graph section
is expected.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.
