# YAML Record Review: Photorhabdus khanii NC19

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/photorhabdus_khanii_nc19.yaml`
- Started UTC: 2026-09-22T18:06:02Z
- Finished UTC: 2026-09-22T18:08:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004151` |
| Label | `Photorhabdus khanii NC19` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:1004150` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated strain-level NCBI taxon record. The review was read-only; the YAML should not be edited directly.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/photorhabdus_khanii_nc19.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/mesoflavibacter_zeaxanthinifaciens_s86.yaml data/taxa/bacteria/photorhabdus_khanii.yaml data/taxa/bacteria/photorhabdus_khanii_nc19.yaml data/taxa/bacteria/mesomycoplasma_flocculare_atcc_27716.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

The NCBI portion is internally consistent: the pinned `data/raw/ncbitaxon_taxa.tsv` row identifies `NCBITaxon:1004151` as strain `Photorhabdus khanii NC19`, parented by species `NCBITaxon:1004150`, with genetic code `11` and the NCBI exact synonyms that appear in the YAML.

The GTDB portion is over-scoped. `GTDB:s__Photorhabdus_khanii` is a species cluster and is already the proper GTDB mapping on parent species `NCBITaxon:1004150`; it should not make this NCBI strain record claim `Photorhabdus khanii` as an exact GTDB synonym, add the species GTDB CURIE as an `xref`, or credit the strain taxon with all 11 genomes in the GTDB species cluster.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI strain identity and exact synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004151`, label `Photorhabdus khanii NC19`, rank `STRAIN`, parent `NCBITaxon:1004150`, genetic code `11`, and exact synonyms `Photorhabdus khaniii C1`, `Photorhabdus temperata subsp. khanii C1`, and `Photorhabdus temperata subsp. khanii NC19`. |
| Madin attestation | `data/raw/madin_taxa.tsv` has `NCBITaxon:1004151` with count `5`, matching the `MADIN` `TRAIT_ASSERTION` attestation. |
| Erroneous GTDB projection | `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Photorhabdus_khanii` to `NCBITaxon:1004151` as `skos:closeMatch` with count `11`; the same GTDB species also maps to the parent species `NCBITaxon:1004150`. |

The GTDB row explains how the generated fields arose but does not make the species cluster exact to the NC19 strain. The GTDB mapping, GTDB-derived exact synonym, GTDB `xref`, and GTDB genome-count attestation are therefore unsupported at this strain scope.

## Completeness

`strain_count: 0` is consistent with the exact local BacDive input for this target: the `bacdive:5051` row for NC19 is filed under the parent species record, and the `strain_assemblies.tsv` / `strain_genome_records.tsv` rows retain `NCBITaxon:1004151` only as source genome taxonomy on that BacDive strain.

No record-level evidence, nomenclature, strains, or causal graphs are required for this seeded strain record. The consequential gap is the need to remove the over-scoped GTDB species projection rather than to add a missing local source row.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record imports a GTDB species cluster as an exact mapping, exact synonym, xref, and 11-genome attestation on an NCBI strain taxon. | `data/raw/gtdb_mappings.tsv` emits `GTDB:s__Photorhabdus_khanii` -> `NCBITaxon:1004151` with `skos:closeMatch`, while the same GTDB species is the parent species mapping for `NCBITaxon:1004150`. | Upstream `data/raw/gtdb_mappings.tsv` generation / kg-microbe taxonomy mapping, plus `src/taxonmech/seed.py` if the seeder needs to suppress GTDB species xrefs and synonyms on strain-level records. |

## Recommended Edits

1. Correct the source taxonomy mapping so `GTDB:s__Photorhabdus_khanii` no longer projects as `skos:closeMatch` to strain `NCBITaxon:1004151` in `data/raw/gtdb_mappings.tsv`.
2. Add a regression guard around `src/taxonmech/seed.py` so a GTDB species-cluster row cannot create `taxonomy_mappings`, exact synonyms, `xrefs`, or GTDB genome attestations on NCBI strain records when the mapping belongs at the species level.

## Follow-up Checks

After the mapping/projection fix, re-run `just seed-canary NCBITaxon:1004151`, `just validate-strict data/taxa/bacteria/photorhabdus_khanii_nc19.yaml`, and `just verify-corpus`. Also run an exact `rg --no-ignore --hidden` search for `GTDB:s__Photorhabdus_khanii` with `NCBITaxon:1004151` across `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa` to prove the stale strain-level projection is gone while the parent `NCBITaxon:1004150` species mapping remains.

## Additional Notes

This is a systemic GTDB mapping/projection defect, not a hand-curation issue in `data/taxa/bacteria/photorhabdus_khanii_nc19.yaml`; generated YAML remains read-only.
