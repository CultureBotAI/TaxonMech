# YAML Record Review: Neisseria wadsworthii 9715

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/neisseria_wadsworthii_9715.yaml
- Started UTC: 2026-10-03T06:28:09Z
- Finished UTC: 2026-10-03T06:28:09Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/taxa/bacteria/neisseria_wadsworthii_9715.yaml` |
| Identifier | `NCBITaxon:1030841` |
| Label | `Neisseria wadsworthii 9715` |
| Class | `TaxonRecord` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:607711` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

The file is a generated bacterial strain record with NCBITaxon identity, one
GTDB close match, and Madin et al. trait assertions. Its path is pinned by
`data/taxa/PATHS.tsv:12862`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/neisseria_wadsworthii_9715.yaml` | Passed LinkML validation with no issues. |
| `just validate-strict` on the 10-file `data/taxa/PATHS.tsv:12858-12867` batch | Passed strict validation with 10 files scanned and 0 total ERROR rows. |
| `/private/tmp/taxonmech_yaml_summary.py` | Confirmed the expected generated shape: 90 YAML lines, 10 lineage entries, 3 source attestations, 1 taxonomy mapping, 5 synonyms, 1 xref, 0 strains, 0 genome assemblies, 0 genome records, and 0 causal graphs. |
| Boundary-guarded exact `NCBITaxon:` scan | Found `NCBITaxon:1030841` in NCBI, GTDB, MADIN, legacy-path, BacDive/GOLD genome, and seed rows; the scan included ignored files. |
| Exact prior-report probe | Found no `*-neisseria_wadsworthii_9715.md` report under `reports/yaml_record_review`, with ignored files included. |
| First-column lineage scan | Found all expected committed NCBI lineage rows, ending at `NCBITaxon:607711`. |

Not run: `just verify-corpus`, `just validate-all`, `just validate-history`,
and `just validate-products`. This review did not edit YAML or history.

## Identity and Grounding

`NCBITaxon:1030841` resolves to label `Neisseria wadsworthii 9715`, rank
`STRAIN`, direct parent `NCBITaxon:607711`, genetic code `11`, source set
`ncbitaxon|gtdb|madin_etal`, four NCBI exact synonyms, and taxonomy snapshot
`2026-09-13`.

The lineage is root-first and matches the committed NCBI rows from root through
`Neisseria wadsworthii`. The generated `GTDB:s__Neisseria_wadsworthii`
close-match mapping, xref, GTDB synonym, and count of 3 genomes are supported
by `data/raw/gtdb_mappings.tsv:1295`.

## Evidence

The NCBI row at `data/raw/ncbitaxon_taxa.tsv:220603` supports the strain
identity, direct species parent, genetic code, four NCBI synonyms, NCBITAXON
source attestation, and 2026-09-13 snapshot date. `data/raw/madin_taxa.tsv:570`
supports the MADIN source attestation with 5 trait assertions, and
`curation/seed_scope.tsv:36130` supports the seeded scope reason.

The exact BacDive/GOLD assembly rows at `data/raw/strain_assemblies.tsv:931-932`,
genome rows at `data/raw/strain_genome_records.tsv:764-766`, and GOLD related
rows at `data/raw/strain_related_records.tsv:2906-2909` and `:2912` are tied to
`kgmicrobe.strain:bacdive_10498`. The owning BacDive row is filed under parent
species `NCBITaxon:607711`, not the child strain taxon, so those rows do not
seed a nested `strains` block on this child record.

## Completeness

No consequential required generated claim is absent for this record. Exact
source scans accounted for NCBI, GTDB, MADIN, seed, legacy routing, and the
BacDive/GOLD genome rows linked through the parent-filed BacDive strain.

The 90-line YAML shape is expected for this child strain: there is one GTDB
mapping, one GTDB xref, and no local `strains`, genome, nomenclature, GOLD
organism, MediaDive, BactoTraits, StrainInfo, ATB, or causal graph section to
seed directly under `NCBITaxon:1030841`.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.
