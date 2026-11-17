# YAML Record Review: Microbacterium sp. ADAT-G

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_adat_g.yaml`
- Started UTC: 2026-10-07T14:15:13Z
- Finished UTC: 2026-10-07T14:17:26Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` for `NCBITaxon:1035919`,
Microbacterium sp. ADAT-G, was read. It is species-rank BACTERIA,
with `EXACT` grounding, `SEEDED` lifecycle, genetic code 11,
10 root-first ancestors, zero inventoried BacDive strains, one
NCBITAXON name attestation, and one inline seed event.
It asserts no synonyms, nomenclature, mappings, strain/genome
objects, literature citations, phenotypes, or causal graph.
Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/microbacterium_sp_adat_g.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/microbacterium_sp_adat_g.yaml --out /private/tmp/micro-adat-g-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source checks passed for identity, all ancestor labels/ranks/links, synonyms, attestation, unique path/scope rows, and seed-event wording. These checks do not replace corpus reproduction.
- Live NCBI taxonomy EFetch/Datasets and complete metadata/features/references for the sole exact-taxid Nuccore hit were inspected.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxon identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite. No corpus-wide acceptance claim is made.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035919&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035919)
agree on active ID, exact label, species rank, bacterial placement,
parent `NCBITaxon:2609290` (unclassified Microbacterium),
genetic code 11, and lineage. EFetch lists no additional names.

All 10 ancestors match the pinned backbone, including Bacillati,
Actinomycetota, Actinomycetes, Micrococcales, Microbacteriaceae,
and Microbacterium. Datasets supplies root and EFetch the
remaining labeled chain. A strain-like suffix does not change
the species rank assigned to this NCBI node.

The complete source rows agree at
`data/raw/ncbitaxon_taxa.tsv:222218`,
`data/catalog/ncbi_names-0005.jsonl.gz:31726`,
`data/taxa/PATHS.tsv:14717`, and
`curation/seed_scope.tsv:322477`.
Synonym columns and `retired_into` are blank, and the snapshot
is 2026-09-13. Parsed backbone/status inventories contain no
target child, type-material, merged-ID, or dropped row.

## Evidence

The attestation counts one `NAME`, not one culture or genome.
Exact-target raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin,
and BactoTraits scans found no applicable rows. With no
backbone descendants, zero inventoried BacDive strains agrees
with the inputs.

Seed wording matches the scope/inventories.
The event timestamp `2026-09-13T17:54:04Z` equals the newest
extraction timestamp among the inspected raw, ATB, and StrainInfo
YAML manifests, following `src/taxonmech/seed.py::_seed_timestamp`.

Exact Assembly search `txid1035919[Organism:noexp]` returned
zero with phrase-not-found/no-items warnings. This is a bounded
index result, not proof of global genome absence.
Exact Nuccore search returned only UID 334192518.
All metadata, features, and references were read, excluding
nucleotide payloads.

[JF834172.1](https://www.ncbi.nlm.nih.gov/nuccore/JF834172.1)
is a 1,490-nt partial 16S rRNA gene, annotated with strain ADAT-G,
`taxon:1035919`, soil, and India. These are isolate-scoped
submission metadata, not a whole-genome assembly, culture
deposit, or taxon-wide ecological assertion.
The entry cites an unpublished Ghosal/Dutta/Chakraborty/Basu/Dutta
study and a 13-April-2011 direct submission from Bose Institute.
An unpublished study title about acenaphthene degradation is
not itself a verified assay or pathway dataset.

An exact-label/accession search led to a
[primary study of Microbacterium SL10](https://repository.elizadeuniversity.edu.ng/bitstream/20.500.12398/1226/1/ContentServer.pdf),
DOI `10.1007/s11274-013-1437-7`, visible on the retrieved paper.
Its title, abstract, sampling/isolation methods, and initial
identification methods were inspected. Those experiments concern
SL10 isolated in Lagos, Nigeria, not the Indian ADAT-G submission.
Subsequent PDF context and figure requests timed out, so the
search-indexed ADAT-G comparison and its figure were not independently
verified in full source context. No reported SL10 phenotype is
transferred to ADAT-G. The YAML asserts no literature or
phenotype claim that depends on that optional lead.

## Completeness

Complete enough for a generated NCBI-only identity record.
Optional slots are correctly left empty without applicable
supported objects. `strain_count: 0` counts inventoried
BacDive strains, not all isolates ever sequenced.

Initial and accession-expanded searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Ignored, hidden, and compressed content was included.
Patterns covered taxid, label/slug, ADAT-G, and JF834172.
Both searches returned the same 35 rows, all read completely,
including nested native source objects.

Three rows describe the target backbone, scope, and scientific
name. Excluded matches are:

- Twenty Campylobacter jejuni rows across GOLD, BV-BRC, GenBank, and AllTheBacteria match BioSample digits in `SAMN10359190`, `SAMN10359191`, `SAMN10359192`, `SAMN10359193`, or `SAMN10359199`.
- Three GOLD expression projects describe Neurospora crassa XL-ADAT, organism `Go0498738`; the substring spanning ADAT and Gene matches the search pattern. They are not Microbacterium transcriptomics, and no Eukaryota YAML was re-reviewed.
- Four GOLD/BV-BRC/GenBank/GTDB rows describe RUG13609, `GCA_902790775.1`, taxid 172733; the WGS prefix `CADATG` is a substring collision.
- Three Acinetobacter baumannii rows describe ARLG_6375 (`GCA_014880655.1` and suppressed historical `GCF_014880655.1`, prefix `JADATG`) or AC11 (`GCA_016497665.1`, prefix `DADATG`).
- Salmonella enterica PNUSAS070500 (`GCA_005497825.1`) matches WGS prefix `AADATG`.
- Streptococcus oralis `GCA_963456725.1`, taxid 1303, matches genome length 1035919.

Five native `SOURCE.json` files were parsed completely,
and history filenames were independently searched.
No additional applicable source assertion, deposit, strain-genome
link, or standalone history artifact was found in these bounded
local sources. No global absence claim is made.

iModulonDB is not applicable to this identity-only YAML.
The optional ribosomal marker and unrelated fungal expression
projects do not identify an applicable expression-module dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, count units, optional omissions,
and seed provenance are supported.

## Recommended Edits

None required. Keep the generated YAML and `mapping_status: SEEDED`
unchanged; do not add a review event or promote human-review status.

Future corrections belong to maintained source inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope changes belong to `curation/seed_scope.tsv`.
Any optional phenotype enrichment needs direct ADAT-G evidence,
not a related isolate's measurements or an unpublished title.

## Follow-up Checks

No corrective follow-up is required. Before optional literature
enrichment, retrieve the full original evidence, resolve exact
strain/accession links, and retain assay-level scope.
Do not infer strain equivalence from 16S relatedness.

After future authorized input changes, rerun appropriate
extraction/seeding, schema, strict, reproduction, provenance,
and QC gates; validate products/history if introduced.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- The complete YAML was reread byte-identical before report creation.
- Only this new report is written; no source, YAML, history, generated product, GitHub object, branch, or worktree is changed.
- Eukaryota is already fully covered and its YAML records were not re-reviewed.
