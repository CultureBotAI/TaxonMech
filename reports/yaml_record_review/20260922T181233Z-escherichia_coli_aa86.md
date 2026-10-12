# YAML Record Review: Escherichia coli AA86

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/escherichia_coli_aa86.yaml`
- Started UTC: 2026-09-22T18:10:48Z
- Finished UTC: 2026-09-22T18:12:33Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004153` |
| Label | `Escherichia coli AA86` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:562` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated strain-level NCBI taxon record. Its seeded identity, lineage, GTDB projection, source attestations, and curation history are regenerated from the maintained inventories and `src/taxonmech/seed.py`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/escherichia_coli_aa86.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/escherichia_coli_aa86.yaml data/taxa/bacteria/candidatus_brocadia_carolinensis.yaml data/taxa/bacteria/photorhabdus_tasmaniensis.yaml data/taxa/bacteria/photorhabdus_caribbeanensis.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

The NCBI identity is coherent: `NCBITaxon:1004153` is the pinned NCBI strain row for `Escherichia coli AA86`, parented by species `NCBITaxon:562`, and the YAML carries the expected `Bacteria` to `Escherichia coli` lineage. The exact synonyms `Escherichia coli str. AA86` and `Escherichia coli strain AA86` are exact NCBI synonyms on the local taxonomy row.

The GTDB projection is too broad for this target. `GTDB:s__Escherichia_coli` is a species cluster with 36,408 genomes, but the generated strain record imports it as a `skos:closeMatch`, an exact synonym `Escherichia coli`, an `xref`, and a 36,408-genome source attestation on one AA86 strain taxon.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI strain identity and exact synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004153`, label `Escherichia coli AA86`, rank `STRAIN`, parent `NCBITaxon:562`, genetic code `11`, and the two NCBI exact synonyms. |
| Parent species identity | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:562`, label `Escherichia coli`, rank `SPECIES`, parent `NCBITaxon:561`, and the expected species-level source coverage. |
| Madin attestation | `data/raw/madin_taxa.tsv` has `NCBITaxon:1004153` with count `5`, matching the `MADIN` `TRAIT_ASSERTION` attestation. |
| Erroneous GTDB projection | `data/raw/gtdb_mappings.tsv` row 822 maps `GTDB:s__Escherichia_coli` to `NCBITaxon:1004153` as `skos:closeMatch` with count `36408`. |

The GTDB row is the immediate source of the generated mapping, synonym, xref, and genome attestation, but it does not support treating the whole GTDB `Escherichia coli` species cluster as exact to the AA86 strain.

## Completeness

The absence of `strains`, `nomenclature`, record-level `evidence`, and `causal_graphs` is not a schema defect for this seeded NCBI strain record. A gitignore-independent `rg --no-ignore --hidden` scan over `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa/PATHS.tsv` for the target ID and slug found NCBI, GTDB, and Madin rows for `NCBITaxon:1004153`, with no same-taxon BacDive, LPSN, MediaDive, GOLD, BactoTraits, StrainInfo, or AllTheBacteria rows.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record imports a GTDB species cluster as an exact mapping, exact synonym, xref, and 36,408-genome attestation on an NCBI strain taxon. | `data/raw/gtdb_mappings.tsv` emits `GTDB:s__Escherichia_coli` -> `NCBITaxon:1004153` with `skos:closeMatch`, while `NCBITaxon:1004153` is a strain under the species `NCBITaxon:562`. | Upstream `data/raw/gtdb_mappings.tsv` generation / kg-microbe taxonomy mapping, plus `src/taxonmech/seed.py` if the seeder needs to suppress GTDB species xrefs and synonyms on strain-level records. |

## Recommended Edits

1. Correct the source taxonomy mapping so `GTDB:s__Escherichia_coli` no longer projects as a `skos:closeMatch` to strain `NCBITaxon:1004153` in `data/raw/gtdb_mappings.tsv`.
2. Add a regression guard around `src/taxonmech/seed.py` so GTDB species-cluster rows cannot create `taxonomy_mappings`, exact species synonyms, `xrefs`, or GTDB genome attestations on NCBI strain records.

## Follow-up Checks

After the mapping/projection fix, re-run `just seed-canary NCBITaxon:1004153`, `just validate-strict data/taxa/bacteria/escherichia_coli_aa86.yaml`, and `just verify-corpus`. Also run an exact `rg --no-ignore --hidden` search for `GTDB:s__Escherichia_coli` with `NCBITaxon:1004153` across `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa` to prove the stale strain-level projection is gone.

## Additional Notes

The local `GTDB:s__Escherichia_coli` mapping search returns many strain-level NCBI rows with the same 36,408-genome count, so this record is one instance of the same systemic GTDB species-cluster projection issue seen in other strain records.
