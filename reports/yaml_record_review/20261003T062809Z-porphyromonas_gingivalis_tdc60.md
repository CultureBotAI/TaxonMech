# YAML Record Review: Porphyromonas gingivalis TDC60

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/porphyromonas_gingivalis_tdc60.yaml
- Started UTC: 2026-10-03T06:28:09Z
- Finished UTC: 2026-10-03T06:28:09Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/porphyromonas_gingivalis_tdc60.yaml` |
| Identifier | `NCBITaxon:1030843` |
| Label | `Porphyromonas gingivalis TDC60` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:837` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated bacterial strain record with NCBITaxon identity, one
GTDB close match, and Madin et al. trait assertions. Its path is pinned by
`data/taxa/PATHS.tsv:12864`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/porphyromonas_gingivalis_tdc60.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12858-12867` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 90 YAML lines, 12 lineage entries, 3 source attestations, 1 taxonomy mapping, 3 synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030843` in NCBI, GTDB, MADIN, legacy-path, BacDive genome, and seed rows; the scan included ignored files. |
| Exact prior-report probe | Found no `*-porphyromonas_gingivalis_tdc60.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:837`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030843` resolves to label `Porphyromonas gingivalis TDC60`, rank
`STRAIN`, direct parent `NCBITaxon:837`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, two NCBI exact synonyms, and taxonomy snapshot
`2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`Porphyromonas gingivalis`. The generated
`GTDB:s__Porphyromonas_gingivalis` close-match mapping, xref, GTDB synonym, and
count of 122 genomes are supported by `data/raw/gtdb_mappings.tsv:1297`.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220605` supports the strain
identity, direct species parent, genetic code, two NCBI synonyms, NCBITAXON
source attestation, and 2026-09-13 snapshot date. `data/raw/madin_taxa.tsv:572`
supports the MADIN source attestation with 5 trait assertions, and
`curation/seed_scope.tsv:36132` supports the seeded scope reason.

The exact BacDive assembly row at `data/raw/strain_assemblies.tsv:75019` and
genome rows at `data/raw/strain_genome_records.tsv:58446-58447` are tied to
`kgmicrobe.strain:bacdive_162568`. The owning BacDive row is filed under parent
species `NCBITaxon:837`, not the child strain taxon, so those rows do not seed
a nested `strains` block on this child record.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for NCBI, GTDB, MADIN, seed, legacy routing, and the
BacDive genome rows linked through the parent-filed BacDive strain.

The 90-line YAML shape is expected for this child strain: there is one GTDB
mapping, one GTDB xref, and no local `strains`, genome, nomenclature, GOLD
organism, MediaDive, BactoTraits, StrainInfo, ATB, or causal graph section to
seed directly under `NCBITaxon:1030843`.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.
