# YAML Record Review: Ruminococcus flavefaciens 17

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/ruminococcus_flavefaciens_17.yaml
- Started UTC: 2026-10-03T06:28:09Z
- Finished UTC: 2026-10-03T06:28:09Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/ruminococcus_flavefaciens_17.yaml` |
| Identifier | `NCBITaxon:1030842` |
| Label | `Ruminococcus flavefaciens 17` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1265` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated bacterial strain record with NCBITaxon identity, one
GTDB close match, and one Madin et al. trait assertion. Its path is pinned by
`data/taxa/PATHS.tsv:12863`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/ruminococcus_flavefaciens_17.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12858-12867` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 84 YAML lines, 10 lineage entries, 3 source attestations, 1 taxonomy mapping, 3 synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030842` in NCBI, GTDB, MADIN, legacy-path, BacDive genome, and seed rows; the scan included ignored files. |
| Exact prior-report probe | Found no `*-ruminococcus_flavefaciens_17.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:1265`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030842` resolves to label `Ruminococcus flavefaciens 17`, rank
`STRAIN`, direct parent `NCBITaxon:1265`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, two NCBI exact synonyms, and taxonomy snapshot
`2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`Ruminococcus flavefaciens`. The generated
`GTDB:s__Ruminococcus_flavefaciens_F` close-match mapping, xref, GTDB synonym,
and count of 4 genomes are supported by `data/raw/gtdb_mappings.tsv:1296`.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220604` supports the strain
identity, direct species parent, genetic code, two NCBI synonyms, NCBITAXON
source attestation, and 2026-09-13 snapshot date. `data/raw/madin_taxa.tsv:571`
supports the MADIN source attestation with 1 trait assertion, and
`curation/seed_scope.tsv:36131` supports the seeded scope reason.

The exact BacDive assembly row at `data/raw/strain_assemblies.tsv:99987` and
genome rows at `data/raw/strain_genome_records.tsv:80536-80537` are tied to
`kgmicrobe.strain:bacdive_17683`. The owning BacDive row is filed under parent
species `NCBITaxon:1265`, not the child strain taxon, so those rows do not seed
a nested `strains` block on this child record.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for NCBI, GTDB, MADIN, seed, legacy routing, and the
BacDive genome rows linked through the parent-filed BacDive strain.

The 84-line YAML shape is expected for this child strain: there is one GTDB
mapping, one GTDB xref, and no local `strains`, genome, nomenclature, GOLD
organism, MediaDive, BactoTraits, StrainInfo, ATB, or causal graph section to
seed directly under `NCBITaxon:1030842`.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.
