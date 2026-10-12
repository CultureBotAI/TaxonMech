# YAML Record Review: Pseudomonas sp. MOIL14HWK12:I1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_moil14hwk12_i1.yaml`
- Started UTC: 2026-10-05T00:02:28Z
- Finished UTC: 2026-10-05T00:05:13Z
- Verdict: needs curation

## Target

Read the complete generated `TaxonRecord`, `NCBITaxon:1033993`,
Pseudomonas sp. MOIL14HWK12:I1. It has SPECIES rank, BACTERIA domain,
parent 196821, ten ancestors, EXACT grounding, SEEDED status, one GTDB
mapping, one exact synonym and xref, genetic code 11, zero BacDive
strains, three source attestations and one seed event. The species rank
is NCBI's, despite the isolate-specific name. No YAML, input, code,
status or history was changed.

## Validation

- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudomonas_sp_moil14hwk12_i1.yaml`; no issues.
- Passed, exit 0: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/pseudomonas_sp_moil14hwk12_i1.yaml`; one file, zero errors; emits `reports/instance_validation_failures.tsv`.
- Bounded complete backbone/lineage, mapped inventories, children, scope, filename and inline-event comparisons passed; counts were checked separately below.
- Not run: full-corpus `just verify-corpus`, QC, tests and rendering. Its `--max-diffs` option is not a target selector. Bounded source comparisons do not prove corpus reproduction or biological correctness.
- Not applicable: `just validate-products`; no curator graph nodes. Authority identifiers were checked directly.
- Not run: `just validate-history`; ignored-inclusive filename and compressed-content searches found no target history artifact. Inline seed provenance was inspected.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:221415`, the full native scientific
name at `data/catalog/ncbi_names-0005.jsonl.gz:30759`,
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033993&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033993)
agree on the identifier, label, SPECIES rank, parent and code. All ten
ancestor IDs match: root, cellular organisms, Bacteria, Pseudomonadati,
Pseudomonadota, Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae,
Pseudomonas and unclassified Pseudomonas. Expanded labels and ranks agree
where supplied. NCBI supplies no alternate name here. Complete exact-ID
type-material, merged-ID and dropped-taxon scans found no rows.

Keep I1 distinct from the unsuffixed taxon 1033992 and I2 taxon 1033994.
Each has a separate source assembly and BioSample. This is a source-record
distinction, not proof about their laboratory derivation. In particular,
the unsuffixed strain's equivalent name, ANI warning and literature
observations must not be transferred to I1 merely from the name prefix.

## Evidence

NCBITAXON's one NAME and September 13 snapshot match the backbone.
`data/raw/madin_taxa.tsv:642` supplies six TRAIT_ASSERTION entries;
the count does not establish six individually verified phenotypes.
Direct mapped BacDive, LPSN, GOLD, MediaDive and BactoTraits inventories
were empty. A complete child scan was empty, consistent with zero
descendant-inclusive BacDive strains. Native GOLD records described below
do not retroactively create an attestation in the separate KGX inventory.

`data/raw/gtdb_mappings.tsv:1388` and `data/raw/gtdb_species.tsv:42707`
support the carried mapping and 61-genome cluster count. A full scan of
all 19 native GTDB shards examined 901341 rows, matching the RS232
manifest, and found 61 unique assembly accessions across 15 NCBI taxon
IDs in Chryseomonas oryzihabitans. The representative is NBRC 102199,
RS_GCF_000730625.1. The target is nonrepresentative RS_GCF_000510705.1,
whose full object at `data/catalog/gtdb_genomes-0013.jsonl.gz:6483`
was read. Other members include RIT_BL1, L19, AG1002, RIT411, unnamed
genome bins and both other MOIL taxa. The mapping table also carries
multiple closeMatches and broadMatches from this cluster to distinct NCBI
concepts. Sixty-one is a cluster assembly count, not 61 I1 genomes or
61 physical culture deposits. The live GTDB tree was inaccessible; the
finding rests on the inspected pinned metadata, not a search snippet.

Full native GenBank and RefSeq objects at
`data/catalog/ncbi_genbank-0000.jsonl.gz:16672` and
`data/catalog/ncbi_refseq-0000.jsonl.gz:13839` agree with
[live assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000510705.1/dataset_report).
Exact-taxonomy Assembly search returned one assembly. GCF_000510705.1
and GCA_000510705.1 are both current, explicitly identical, and have no
reported RefSeq exclusion. The scaffold assembly contains 5005518 total
bases and 5005052 ungapped bases, with 12 scaffolds. NCBI separately
reports 17 contigs and 16 component sequences; those fields must not be
silently conflated. SAMN02597178 is the exact BioSample and PRJNA79067
the sequencing project; PRJNA224116 is RefSeq's umbrella.

The BioSample names MOIL14HWK12:I1 and rhizosphere/soil. Geographic
location, collection date, reference biomaterial and growth conditions
are missing. NCBI's taxonomy check is OK at genus level, with no submitted
type assembly; the best ANI match is P. oryzihabitans at 98.44%.
This differs from the unsuffixed taxon's inconclusive result. A best
genomic match supports classification, not a formal nomenclatural synonym
or a change to TaxonMech's NCBI-carried lineage.

All 34 exact-taxonomy nuccore summary records were inspected: one GenBank
master, 16 component accessions, four scaffold accessions, and 13 RefSeq
records comprising a master and 12 scaffolds. They are not 34 genomes.
The complete metadata, source feature, references and comments of
[AZNY00000000.1](https://www.ncbi.nlm.nih.gov/nuccore/AZNY00000000.1)
confirm the exact taxon, strain, sample, project and JGI project 404623.
It is a direct JGI submission, not an inspected experimental paper.
Its master length 16 denotes the component inventory, not a 16-base
genome. Raw bases and all component gene features were not reviewed.

The full native BV-BRC object at `data/bvbrc/bvbrc-0000.jsonl.gz:3260`
links PATRIC 1033993.3, GCA_000510705.1, SAMN02597178 and PRJNA79067.
Its culture-collection value is blank. Its lineage-name array drops the
suffix at the terminal label, while the genome name, strain and terminal
taxon ID explicitly retain I1; that display discrepancy is not a merge.
Full native GOLD objects at `data/gold/organisms.jsonl.gz:11320`,
`data/gold/projects.jsonl.gz:11183` and `data/gold/analyses.jsonl.gz:16267`
establish Go0012840 -> Gp0012840 -> Ga0025412 -> IMG 2510065053 /
GCA_000510705.1. The analysis has an explicit project bridge but no direct
organism ID. The organism's culture-collection field is empty. These
source records support genome provenance, not an eligible deposit join.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden -n -z -i` searched ID, slug
and I1 name separator variants across `data/raw`, `data/catalog`,
`data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`,
`data/straininfo`, `data/atb`, `curation` and `history`, excluding only
`SOURCE.json`. All 34 matching contexts were inspected. Incidental
genome lengths, IMG numbers and longer sample IDs were not target matches;
SAMEA1033993 is an unrelated Streptococcus sample.

An assembly/sample/project/WGS/IMG search returned 19 contexts, all
inspected. Longer WGS prefixes containing AZNY were unrelated. The exact
sample occurs at `data/catalog/allthebacteria.tsv.xz:1033173`, with
SRR3944178, META_FAIL and SYLPH_RESULTS_FAIL, and no ENA analysis.
The full TSV row was read. Its supplied FASTA URL does not override the
metadata exclusion. No eligible BacDive/StrainInfo deposit bridge was
found within these searches. Zero BacDive strains is not absence of a
genome and must not be repaired by inventing a culture identifier.

Bounded web searches did not yield an inspected primary paper specific
to I1 or a JGI portal page. Gene-index, patent and supplementary-table
search leads were not used as organism-phenotype evidence. No literature
claim is required by the YAML. Optional nomenclature, phenotype and graph
fields are not mandatory merely because genome metadata exist.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. Major: an isolate-specific, species-ranked NCBI placeholder inherits
   the entire GTDB species as an exact name without evidence of equivalent
   circumscription. Lines 43 and 64 carry closeMatch, line 46 introduces
   the EXACT_SYNONYM and line 51 adds the identity xref. The native data
   establish membership of I1's assembly in a multi-taxon cluster, not that
   this unresolved placeholder denotes the entire named species. NCBI
   supplies no such synonym. Upstream kg-microbe mapping semantics are
   imported at `src/taxonmech/extract.py:501`; TaxonMech's
   `src/taxonmech/seed.py:451` treats every closeMatch as identity and
   line 466 promotes synonym/xref. Those maintained owners must change,
   not the generated YAML. A rank-only guard would miss this SPECIES case.

## Recommended Edits

1. Require supported concept equivalence before exact synonym/xref
   promotion, including isolate-specific species placeholders. Preserve
   genome membership and classification separately. Correct the maintained
   mapping/seeder rule, then regenerate away the unsupported identity
   assertions. Do not blindly replace closeMatch with broadMatch; confirm
   the source predicate contract and direction first.
2. Add a regression in `tests/test_seed.py` explicitly covering a SPECIES
   placeholder in a multi-NCBI-taxon GTDB cluster, alongside strain-ranked
   cases and valid same-concept mappings. Preserve the 61-genome source
   count, six MADIN assertions, source units, lineage and SEEDED status.

## Follow-up Checks

After an authorized maintained-input correction, rerun cluster membership
and concept-scope checks, focused tests, regeneration, schema/strict
validation and full `just verify-corpus` plus relevant QC gates. Future
strain enrichment requires an eligible whole deposit identifier and must
retain ATB exclusion. Do not transfer unsuffixed or I2 source claims to I1.
No blocker prevents further independent record reviews.

## Additional Notes

`data/taxa/PATHS.tsv:13870` fixes the slug;
`curation/seed_scope.tsv:36156` adds the target on September 12, 2026.
The September 13 seed event and three-source reason agree. No prior
target report or history artifact was found by ignored-inclusive searches.
iModulonDB is not applicable: no gene, regulator or expression module is
asserted. No paid research, outside contact, GitHub mutation, generator
run, human REVIEWED promotion or curation-history change occurred.
