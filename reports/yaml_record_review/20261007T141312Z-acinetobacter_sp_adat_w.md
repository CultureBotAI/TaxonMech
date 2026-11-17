# YAML Record Review: Acinetobacter sp. ADAT-W

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_adat_w.yaml`
- Started UTC: 2026-10-07T14:10:38Z
- Finished UTC: 2026-10-07T14:13:12Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035918`,
Acinetobacter sp. ADAT-W: species rank, BACTERIA, `EXACT` grounding,
`SEEDED` lifecycle, code 11, 10 root-first ancestors, zero inventoried
BacDive strains, one NCBITAXON name attestation, and one inline
seed event. It contains no synonym, nomenclature, taxonomy mapping,
strain/genome, literature, phenotype, or graph objects.
Seeded fields are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/acinetobacter_sp_adat_w.yaml`: passed, no LinkML issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/acinetobacter_sp_adat_w.yaml --out /private/tmp/acin-adat-w-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source comparisons passed for identity, all ancestor labels/ranks/links, synonyms, attestation, unique path/scope rows, and seed-event wording. These bounded checks do not replace corpus reproduction.
- NCBI taxonomy EFetch/Datasets, complete metadata/features/references for the exact-taxid Nuccore hit, and the linked PubMed abstract/metadata were inspected.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxon identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target history artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite. No corpus-wide acceptance claim is made.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035918&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035918)
confirm the active taxid, exact ADAT-W label, species rank,
bacterial placement, parent `NCBITaxon:196816` (unclassified
Acinetobacter), genetic code 11, and lineage. EFetch lists no
additional names. The strain-like suffix does not alter NCBI's rank.

All 10 ancestors match the pinned backbone, including Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Moraxellales, Moraxellaceae,
and Acinetobacter. Datasets supplies root; EFetch supplies the
remaining labeled lineage.

Complete rows agree at `data/raw/ncbitaxon_taxa.tsv:222217`,
`data/catalog/ncbi_names-0005.jsonl.gz:31725`,
`data/taxa/PATHS.tsv:14716`, and
`curation/seed_scope.tsv:322476`. Synonym columns and
`retired_into` are blank; the snapshot is 2026-09-13.
Parsed backbone/status inventories contain no target child,
type-material, merged-ID, or dropped row.

## Evidence

The NCBITAXON attestation correctly counts one `NAME`, not
a culture deposit or genome. Exact-target scans of raw BacDive,
LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories
found no applicable rows. There are no backbone descendants;
zero inventoried BacDive strains is consistent.

The event wording agrees with the inputs and scope.
Its timestamp `2026-09-13T17:54:04Z` matches the newest extraction
timestamp among the inspected raw, ATB, and StrainInfo YAML
manifests, as specified by `src/taxonmech/seed.py::_seed_timestamp`.

Exact Assembly search `txid1035918[Organism:noexp]` returned zero
with phrase-not-found/no-items warnings. This is a bounded index
result, not proof of global genome absence. Exact Nuccore search
returned only UID 334192519; all metadata, features, and references
were inspected, excluding nucleotide payloads.

[JF834173.1](https://www.ncbi.nlm.nih.gov/nuccore/JF834173.1)
is a 1,504-nt partial 16S rRNA gene, explicitly annotated with
strain ADAT-W, `taxon:1035918`, soil, and India.
These are isolate-scoped submission metadata, not a genome assembly,
deposit accession, or taxon-wide ecological claim.
References include a 13-April-2011 Bose Institute submission,
an unpublished study, and PMID 23178176.

The [linked primary publication](https://pubmed.ncbi.nlm.nih.gov/23178176/)
has DOI `10.1016/j.resmic.2012.11.003`; its bibliographic metadata
and full abstract were inspected. It calls the strain AGAT-W,
not ADAT-W, and describes acenaphthene assimilation by an isolate
from waste-contaminated soil, supported by metabolite and
cell-free enzyme analyses. GenBank explicitly links this paper
to JF834173.1, but taxonomy and source qualifiers retain ADAT-W.

This spelling discrepancy is preserved, not silently normalized.
The abstract does not establish whether ADAT-W is a typographic
variant, a former designation, or an annotation error.
A DOI open failed and publisher full-text access returned HTTP 403,
so full methods/accession context was not verified.
The current YAML makes no alias or metabolic-pathway assertion;
there is no unsupported phenotype transfer to correct in it.

## Completeness

Complete enough as an NCBI-only identity record. Optional slots
are appropriately empty without applicable supported objects.
`strain_count: 0` counts inventoried BacDive strains, not all
isolates or marker sequences ever associated with this taxon.

Ignored-independent searches used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Ignored, hidden, and compressed content was included.
Initial ID/label/slug/ADAT-W patterns returned 58 candidate rows;
expansion with JF834173 and AGAT-W returned 63.
All initial rows and all five additional rows were read fully,
including nested native source objects.

Three rows describe the target backbone, scope, and scientific
name. Excluded candidates are:

- Forty Campylobacter jejuni rows in GOLD projects, BV-BRC, GenBank, and AllTheBacteria match BioSample substrings `SAMN10359180` through `SAMN10359189`; they do not establish ADAT-W genomes.
- One additional Campylobacter jejuni row matches assembly digits `GCA_010359185.1`, strain PNUSAC014820.
- Four GOLD rows describe Neurospora crassa `XL-ADAT-W_GCN4`, taxid 5141, organism `Go0498735` and three expression projects. They are a partial-label collision, not Acinetobacter transcriptomics. Inspecting source candidates did not re-review a Eukaryota YAML.
- Four rows describe uncultured Lachnospiraceae bacterium RUG13619, `GCA_902790925.1`, taxid 297314; the matching WGS prefix is `CADATW`.
- Two rows describe uncultured Clostridiaceae bacterium `GCA_905203225.1`, taxid 195049; genome length 1035918 causes the numeric match.
- Three rows describe Acinetobacter baumannii: ARLG_6359 with `GCA_014881595.1` and suppressed historical `GCF_014881595.1` (`JADATW`), and MyJU802 with `GCA_016498125.1` (`DADATW`). Shared genus and WGS-prefix substrings are not strain identity.
- Salmonella enterica `GCA_005498485.1`, strain PNUSAS070697, matches WGS prefix `AADATW`.
- Five accession-expanded rows describe Clostridia bacterium RGIG8769 (`JAGATW`, `GCA_017621085.1`, three sources), Klebsiella pneumoniae T7-366 (`DAGATW`, `GCA_021975375.1`), and Salmonella enterica PNUSAS042855 (`AAGATW`, `GCA_006710125.1`). None denotes AGAT-W or ADAT-W.

Five native `SOURCE.json` files were parsed completely;
history filenames were searched independently.
No additional applicable local source assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within those bounded roots. Global absence is not claimed.

iModulonDB is not applicable to this identity-only record.
The unrelated fungal expression projects are not target matches;
a linked enzyme-assay paper is not itself a covered expression dataset.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current YAML assertions. The ADAT-W/AGAT-W
source discrepancy is an unresolved optional-enrichment question,
not evidence that the YAML's NCBI identity is wrong.

## Recommended Edits

None required. Leave generated YAML and `mapping_status: SEEDED`
unchanged; do not append a review event from this read-only audit.

Before adding AGAT-W as an alias or importing a pathway claim,
resolve the spelling discrepancy through full primary source
context and authoritative accession annotations.
Future identity/source corrections belong to maintained inputs
and `src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
scope changes belong to `curation/seed_scope.tsv`.
Do not patch generated YAML or pages directly.

## Follow-up Checks

No corrective gate is outstanding for current assertions.
Optional alias or phenotype enrichment requires inspection of the
full paper's strain/accession linkage and appropriately scoped
evidence. A linked citation alone does not settle every spelling
or make a partial marker into an assembly.

After authorized maintained-input changes, rerun extraction/seeding,
schema, strict, reproduction, provenance, and QC checks.
Validate graph products and standalone history if introduced.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- The complete YAML was reread byte-identical before report creation.
- Only this new review report is created; no YAML, history, source, generated product, GitHub object, branch, or worktree is changed.
- Eukaryota is already fully covered and its YAML records were not re-reviewed.
