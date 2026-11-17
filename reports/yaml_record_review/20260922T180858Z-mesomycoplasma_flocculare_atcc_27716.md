# YAML Record Review: Mesomycoplasma flocculare ATCC 27716

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/mesomycoplasma_flocculare_atcc_27716.yaml`
- Started UTC: 2026-09-22T18:06:02Z
- Finished UTC: 2026-09-22T18:08:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `NCBITaxon:1004152` |
| Label | `Mesomycoplasma flocculare ATCC 27716` |
| Rank | `STRAIN` |
| Domain | `BACTERIA` |
| Parent | `NCBITaxon:2128` |
| Grounding | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated strain-level NCBI taxon record. Seeded taxonomy fields are owned by source inventory generation and `src/taxonmech/seed.py`.

## Validation

| Check | Result |
|---|---|
| `just validate data/taxa/bacteria/mesomycoplasma_flocculare_atcc_27716.yaml` | Pass; LinkML reported no issues. |
| `just validate-strict data/taxa/bacteria/mesoflavibacter_zeaxanthinifaciens_s86.yaml data/taxa/bacteria/photorhabdus_khanii.yaml data/taxa/bacteria/photorhabdus_khanii_nc19.yaml data/taxa/bacteria/mesomycoplasma_flocculare_atcc_27716.yaml` | Pass; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-history` | Skipped for this read-only review because no `history/` decision row was created. |
| `just validate-products` | Skipped because this record has no curator-authored `causal_graphs` nodes needing OAK id/label checks. |
| `just verify-corpus` | Skipped for this per-record report; full-corpus reproduction had already passed earlier in this run, and this review added only ignored Markdown under `reports/`. |

## Identity and Grounding

The NCBI-derived identity is coherent: `NCBITaxon:1004152` is the pinned NCBI strain row for `Mesomycoplasma flocculare ATCC 27716`, parented by the species `NCBITaxon:2128`, with bacterial domain placement and genetic code `4`. The exact synonyms `Mycoplasma flocculare ATCC 27716`, `Mycoplasma flocculare str. ATCC 27716`, and `Mycoplasma flocculare strain ATCC 27716` are NCBI exact synonyms on that row.

The `GTDB:s__Mesomycoplasma_flocculare` mapping is over-scoped in the same way as the NC19 strain record: it is a GTDB species cluster for `Mesomycoplasma flocculare`, but the YAML imports it as an exact GTDB mapping, species-level synonym, xref, and 9-genome attestation on the `ATCC 27716` strain taxon.

## Evidence

| Claim | Local support checked |
|---|---|
| NCBI strain identity and exact synonyms | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:1004152`, label `Mesomycoplasma flocculare ATCC 27716`, rank `STRAIN`, parent `NCBITaxon:2128`, genetic code `4`, and the three NCBI exact synonyms in the record. |
| Parent species identity | `data/raw/ncbitaxon_taxa.tsv` has `NCBITaxon:2128`, label `Mesomycoplasma flocculare`, rank `SPECIES`, and genus parent `NCBITaxon:2923352`. |
| Madin attestation | `data/raw/madin_taxa.tsv` has `NCBITaxon:1004152` with count `1`, matching the `MADIN` `TRAIT_ASSERTION` attestation. |
| Erroneous GTDB projection | `data/raw/gtdb_mappings.tsv` maps `GTDB:s__Mesomycoplasma_flocculare` to `NCBITaxon:1004152` as `skos:closeMatch` with count `9`, even though that GTDB identifier is the species cluster for the parent species name. |

The local GTDB mapping row is the immediate source of the generated GTDB fields, but it does not support treating the 9-genome GTDB species cluster as exact to this one NCBI strain.

## Completeness

The record has no BacDive strain entries, LPSN nomenclature, record-level evidence, or causal graphs, and none are required by the schema for a seeded strain. A gitignore-independent exact search over `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa/PATHS.tsv` found only the NCBI, Madin, and over-scoped GTDB rows for `NCBITaxon:1004152`; no exact same-taxon BacDive, LPSN, MediaDive, GOLD, BactoTraits, StrainInfo, or AllTheBacteria row was found for the strain itself.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record imports `GTDB:s__Mesomycoplasma_flocculare` as an exact mapping, exact synonym, xref, and 9-genome attestation on an NCBI strain taxon. | `data/raw/gtdb_mappings.tsv` maps the GTDB species cluster directly to `NCBITaxon:1004152` with `skos:closeMatch`; the target's pinned NCBI parent is the actual `Mesomycoplasma flocculare` species. | Upstream `data/raw/gtdb_mappings.tsv` generation / kg-microbe taxonomy mapping, plus `src/taxonmech/seed.py` if the seeder needs to suppress GTDB species xrefs and synonyms on strain-level records. |

## Recommended Edits

1. Correct the source taxonomy mapping so `GTDB:s__Mesomycoplasma_flocculare` no longer projects as `skos:closeMatch` to strain `NCBITaxon:1004152` in `data/raw/gtdb_mappings.tsv`.
2. Add a regression guard around `src/taxonmech/seed.py` so GTDB species-cluster rows cannot create `taxonomy_mappings`, exact synonyms, `xrefs`, or GTDB genome attestations on NCBI strain records when the mapping belongs at species scope.

## Follow-up Checks

After the mapping/projection fix, re-run `just seed-canary NCBITaxon:1004152`, `just validate-strict data/taxa/bacteria/mesomycoplasma_flocculare_atcc_27716.yaml`, and `just verify-corpus`. Also run an exact `rg --no-ignore --hidden` search for `GTDB:s__Mesomycoplasma_flocculare` with `NCBITaxon:1004152` across `data/raw`, `data/atb`, `data/straininfo`, and `data/taxa` to prove no strain-level GTDB species-cluster projection remains.

## Additional Notes

The live NCBI lookup was unavailable during this run, so NCBI identity was checked against the pinned `data/raw/ncbitaxon_taxa.tsv` snapshot. The GTDB finding should be fixed at the source-mapping or seed-projection layer; directly patching this generated YAML would only create corpus drift.
