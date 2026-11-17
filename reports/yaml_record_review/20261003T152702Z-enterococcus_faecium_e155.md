# YAML Record Review: Enterococcus faecium E155

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterococcus_faecium_e155.yaml`
- Started UTC: 2026-10-03T15:25:19Z
- Finished UTC: 2026-10-03T15:27:02Z
- Verdict: needs curation

## Target

Read the entire 78-line generated `TaxonRecord` before judgement.
Identity is `NCBITaxon:1303769`, rank `STRAIN`, domain `BACTERIA`,
parent species `NCBITaxon:1352`, genetic code 11. Grounding is `EXACT`
and mapping status `SEEDED`. One GTDB mapping, one GTDB exact synonym,
one equivalence xref, three attestations and one seed event are present.
Strain count is zero; no strains, genome links, nomenclature,
experimental evidence or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterococcus_faecium_e155.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterococcus_faecium_e155.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison confirms identity, rank,
  parent, genetic code and all ten lineage entries. No target children
  occur in the pinned backbone.
- Full exact-field inventory scans reproduce the GTDB mapping and Madin
  count 4. No direct BacDive, LPSN, GOLD, MediaDive or BactoTraits taxon
  inventory membership was found.
- Complete native GTDB census confirms 4,800 distinct species-cluster
  accessions spanning 353 source taxon IDs; exactly one row has 1303769.
  This reproduces the count, not a strain/species equivalence.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, generated products,
  exports and genome sequences were not audited.
- Ignored-inclusive history searches found no target entry. Standalone
  history validation had no target; strict validation covered the embedded
  event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308133` and the complete scientific-name
object at `data/catalog/ncbi_names-0007.jsonl.gz:30680` support the
exact E155 identity. The raw NCBI synonym fields are empty. The PATHS
index resolves this ID to one record slug.

The browser URL was inaccessible through the web tool. Current
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303769&retmode=xml)
confirms the exact name, strain rank, Bacteria division, parent 1352,
code 11 and complete non-root lineage with no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303769)
also confirms strain rank and all ten ancestor IDs including root.
Read-only API access used network escalation after sandbox DNS failed
earlier in this review session. The NCBI grounding is supported.

E155 is not E1552, which appears as an exact synonym of EnGen0021 in
the raw taxonomy inventory, nor the unrelated E155-designated genomes
from other genera found in the broader name search. None was merged.

## Evidence

| Assertion | Inspected inventory | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308133` | Exact ID and label; snapshot 2026-09-13 |
| GTDB 4800 GENOME | `data/raw/gtdb_species.tsv:58284`; `gtdb_mappings.tsv:17465` | Correct for species cluster, not E155 |
| MADIN 4 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11830` | Count reproduced; no particular trait asserted |

The scope row at `curation/seed_scope.tsv:42155` admits the target on
2026-09-12 with three sources. The 2026-09-13T17:54:04Z seed event
preserves that reason and the actual attesting sources. It does not
claim human review, and units must not be summed across sources.

The GTDB census parsed every `gtdb_genomes-*.jsonl.gz` file, selecting
the terminal species exactly `s__Enterococcus_B faecium`. Its 4,800
accessions include many other strain designations. The representative,
RS_GCF_029023785.1, is DSM 20477, source taxon 1352, not E155; its
complete object is at `gtdb_genomes-0004.jsonl.gz:21353`. The sole
target-classified member is RS_GCF_000442045.1 at
`gtdb_genomes-0008.jsonl.gz:43469`, with strain field E155, sample
SAMN02471500 and GenBank accession GCA_000442045.1. The taxon web page
was inaccessible; pinned primary metadata, not snippets, support M1.

Complete NCBI objects at `ncbi_genbank-0000.jsonl.gz:13608` and
`ncbi_refseq-0000.jsonl.gz:11420` preserve GCA/GCF_000442045.1,
assembly EfmE155_v1.0, strain E155, taxon 1303769 and sample
SAMN02471500. They explicitly describe an identical GenBank/RefSeq pair,
contig level, 495 contigs and 3,066,426 bp. GenBank project PRJNA192879
and RefSeq umbrella project PRJNA224116 remain distinct source values.
The complete BV-BRC object at `data/bvbrc/bvbrc-0001.jsonl.gz:23823`
retains genome 1303769.3, GCA_000442045.1 and the same strain/sample.

Native GOLD preserves Go0036860 -> Gp0036860 -> Ga0021353 with
GCA_000442045.1, IMG 2551306684, PRJNA192879 and SAMN02471500.
The objects are at `data/gold/organisms.jsonl.gz:31198`,
`projects.jsonl.gz:25044` and `analyses.jsonl.gz:13349`. Its culture
field is empty and its strain field is the bare designation E155.
The absence of a KGX-derived GOLD taxon count is not contradicted by
this separate primary catalog: the existing model keeps those sources
and derivations separate. Do not manufacture an attestation count.

The assembly metadata cite PMID 23882129. Its inspected
[PubMed entry](https://pubmed.ncbi.nlm.nih.gov/23882129/)
resolves to DOI 10.1093/gbe/evt111, a comparative recombination study,
and lists AUWX00000000 among the associated sequence accessions.
The PMC full-text link returned a browser challenge. No experimental
claim or curator-added citation was inferred from the abstract or title.

## Completeness

Ignored-inclusive native searches covered all `*.jsonl.gz` files in
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/straininfo/` and `data/seqcode/`, using taxon ID, E155 and slug.
Unrelated E. coli E155, Acinetobacter DETAB-E155 and Streptomyces E155
objects were inspected and excluded, demonstrating why a bare name is
not a culture-join key. No target BacDive or StrainInfo native object
was found in that bounded search.

The complete BacDive membership scan and singleton subtree support
strain count zero. Native genome data exist, but the current model
attaches genome links to source-supported BacDive strains through
direct assertions or eligible culture identifiers. E155 is not such
a registered culture key. Missing native taxon-genome representation
is a separate modeling question, not permission to invent a strain row.

Ignored-inclusive searches of the raw strain assembly/genome/related
inventories and StrainInfo link/assembly/exclusion tables found no target
ID, E155 designation or slug. Compressed searches of `data/atb/` and
the full `data/catalog/allthebacteria.tsv.xz`, additionally using
SAMN02471500, found no target/sample result. These are bounded pinned
source misses, not proof that no biological sequence exists.

There is no same-taxon LPSN inventory mapping. Optional nomenclature and
type flags need not be copied from the parent species. The YAML names
no gene, locus, regulator, pathway, specific trait or transcriptomic
dataset, so iModulonDB is not applicable. Four unspecified Madin
assertions do not establish a particular phenotype or mechanism.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. YAML lines 46-51 treat
  `GTDB:s__Enterococcus_B_faecium` as an exact synonym and equivalence
  xref for strain E155. The native species cluster has 4,800 genomes,
  only one classified as this strain. Membership does not establish
  identity. `src/taxonmech/seed.py:451` treats a source `skos:closeMatch`
  as identity without rank/scope checks; lines 466-469 emit the xref
  and exact synonym, contrary to the true-equivalence contract at
  `src/taxonmech/schema/taxonmech.yaml:180`. The maintained fix belongs
  in `src/taxonmech/seed.py` with `tests/test_seed.py`; review the
  upstream kg-microbe predicate separately. The count is correct for
  the species cluster but must not imply 4,800 E155 genomes.
- Minor: None found.

## Recommended Edits

1. Make equivalence generation in `src/taxonmech/seed.py` rank/scope-aware.
   Retain GTDB classification and source provenance, but do not generate
   the species exact synonym or equivalence xref for E155 without actual
   identity evidence. Explicitly scope the 4,800 count to its cluster;
   do not replace it with 1 while retaining species-count semantics.
2. Add a strain/species regression to `tests/test_seed.py` while preserving
   supported same-scope mappings. Review kg-microbe's source predicate;
   do not hand-patch extracted TSVs or guess a predicate direction.
3. Follow the authorized dry-run/canary/regeneration workflow after the
   maintained fix. Do not hand-edit YAML, invent culture joins or promote
   human review status. Preserve source-specific project and genome IDs.

## Follow-up Checks

Run the new regression and `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, rerun both focused validators and inspect
the written YAML: classification retained, unsupported exact synonym and
xref absent, cluster count clearly scoped, NCBI identity unchanged.
Repeat the exact-terminal GTDB census and distinguish its single target
member from species scope and culture identity. Run `just verify-corpus`
and full QC for the regeneration. M1 is unresolved; no fix was made here.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find`, or `rg --no-ignore --hidden`, with `-z` for compressed sources.
The only manual write is this new report; strict validation wrote its
standard diagnostic. No YAML, prior report, source, history or status
was edited. No generator, refresh, paid research, GitHub mutation or
cross-repository write occurred. Eukaryota was not re-reviewed.
