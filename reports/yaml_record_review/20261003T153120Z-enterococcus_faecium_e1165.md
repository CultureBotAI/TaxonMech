# YAML Record Review: Enterococcus faecium E1165

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterococcus_faecium_e1165.yaml`
- Started UTC: 2026-10-03T15:30:07Z
- Finished UTC: 2026-10-03T15:31:20Z
- Verdict: needs curation

## Target

Read the complete generated `TaxonRecord` before judgement. The target
is `NCBITaxon:1303771`, rank `STRAIN`, domain `BACTERIA`, parent
`NCBITaxon:1352`, genetic code 11. Grounding is `EXACT` and mapping
status `SEEDED`. One GTDB mapping, one GTDB exact synonym, one
equivalence xref, three source attestations and one seed event are
present. Strain count is zero, with no strain list, genome links,
nomenclature, experimental claims or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterococcus_faecium_e1165.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterococcus_faecium_e1165.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone read confirms ID, label, rank, parent,
  genetic code and all ten lineage entries. The target has no children
  in the pinned backbone.
- Complete exact-field scans reproduce the GTDB mapping and Madin count
  4. No direct BacDive, LPSN, GOLD, MediaDive or BactoTraits taxon
  inventory membership was found.
- A fresh complete GTDB native census confirms 4,800 distinct accessions
  across 353 taxon IDs in the species cluster. One row has target ID
  1303771. The count reproduces; species/strain equivalence does not follow.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, generated products,
  exports and genome sequences were not audited.
- Ignored-inclusive history searches found no target entry. Standalone
  history validation had no target; strict validation checked the embedded
  event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308135` and the complete scientific-name
object at `data/catalog/ncbi_names-0007.jsonl.gz:30682` support the
exact E1165 identity. Raw NCBI synonym fields are empty. The PATHS
index resolves this identifier to one record slug.

The NCBI browser URL was inaccessible through the web tool. Inspected
current [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303771&retmode=xml)
confirms the exact label, strain rank, Bacteria division, parent 1352,
code 11 and complete non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303771)
also confirms strain rank and all ten ancestor IDs including root.
Read-only API access used network escalation after sandbox DNS failure
was established in this session. NCBI grounding is supported; the
additional GTDB species equivalence is not.

## Evidence

| Assertion | Inspected inventory | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308135` | Exact ID and label; snapshot 2026-09-13 |
| GTDB 4800 GENOME | `data/raw/gtdb_species.tsv:58284`; `gtdb_mappings.tsv:17467` | Species-cluster count, not E1165 count |
| MADIN 4 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11832` | Count reproduced; no particular trait asserted |

The scope row at `curation/seed_scope.tsv:42157` admits the target on
2026-09-12 with three sources. The embedded 2026-09-13T17:54:04Z seed
event preserves that reason and the actual attesting sources. It does
not claim human review. Counts with different units must not be added.

The GTDB census parsed all `gtdb_genomes-*.jsonl.gz` files, selecting
terminal taxonomy exactly `s__Enterococcus_B faecium`. The one
target-classified member is RS_GCF_000477595.1, with strain field
E1165, sample SAMN02471488 and GenBank GCA_000477595.1. Its complete
object is at `gtdb_genomes-0011.jsonl.gz:39138`. The representative
RS_GCF_029023785.1 is DSM 20477, source taxon 1352, not E1165
(`gtdb_genomes-0004.jsonl.gz:21353`). Other strains make up the broader
cluster. The shared GTDB taxon-page request in this session was
inaccessible; the pinned primary metadata, not web snippets, support M1.

The complete native objects at `ncbi_genbank-0000.jsonl.gz:15201` and
`ncbi_refseq-0000.jsonl.gz:12779` supply GCA/GCF_000477595.1,
assembly EfmE1165_v1.0, strain E1165, taxon 1303771 and sample
SAMN02471488. They explicitly describe an identical GenBank/RefSeq
pair, contig level, 355 contigs and 2,789,656 bp. GenBank project
PRJNA192894 and RefSeq umbrella PRJNA224116 retain distinct source
meanings. The complete BV-BRC object at
`data/bvbrc/bvbrc-0001.jsonl.gz:23825` supplies genome 1303771.3,
GCA_000477595.1, PRJNA192894 and the same strain/sample; its culture
field is blank.

Native GOLD retains Go0036859 -> Gp0036859 -> Ga0032122 with
GCA_000477595.1, IMG 2565956806, PRJNA192894 and SAMN02471488.
The complete objects are at `data/gold/organisms.jsonl.gz:31197`,
`projects.jsonl.gz:25043` and `analyses.jsonl.gz:22061`. Its culture
field is empty and its strain field is the bare designation E1165.
This primary catalog does not create a KGX-derived GOLD taxon count;
the existing model keeps the two derivations separate.

The native assembly metadata's PMID 23882129 resolves to DOI
10.1093/gbe/evt111 in the [PubMed entry inspected this session](https://pubmed.ncbi.nlm.nih.gov/23882129/).
That entry lists AUWW00000000 among associated sequence accessions.
The PMC full-text request returned a browser challenge. No phenotype
or mechanistic claim was imported from the abstract, and the YAML does
not cite the publication.

## Completeness

Ignored-inclusive compressed searches by taxon ID, E1165 and slug
covered every `*.jsonl.gz` file under `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/`, `data/straininfo/` and `data/seqcode/`.
Two irrelevant objects were fully inspected and excluded:

- `ncbi_genbank-0021.jsonl.gz:35637`, GCA_023458395.1, is E. coli
  taxon 562, strain 224, isolate E1165, not this Enterococcus strain.
- `ncbi_genbank-0066.jsonl.gz:7724`, GCA_982313185.1, is
  Faecalibacterium prausnitzii taxon 853; 1303771 is its genome length,
  not its taxon ID.

No target BacDive or StrainInfo native object was found within that
bounded search. The complete BacDive membership scan and singleton
subtree support strain count zero. This is not a genome-absence claim:
the native catalogs explicitly contain E1165 genome data.

The current model publishes genome assertions on source-supported
BacDive strain entries, using direct assertions or eligible culture
identifiers. Neither a bare designation nor the taxon ID establishes
a deposit-to-genome join. Native taxon-level genome representation would
be a separate modeling task, not justification to fabricate a strain row.

Ignored-inclusive searches of raw strain assembly/genome/related tables
and StrainInfo link/assembly/exclusion tables found no target ID, E1165
designation or slug. Compressed searches of `data/atb/` and the complete
`data/catalog/allthebacteria.tsv.xz`, additionally using SAMN02471488,
found no target/sample result. These misses are bounded to pinned
sources and do not imply biological absence.

There is no same-taxon LPSN inventory mapping. Optional nomenclature or
type flags need not be copied from the parent species. The record
names no gene, locus, regulator, pathway, specific phenotype or
transcriptomic dataset, so iModulonDB is not applicable. An unspecified
Madin assertion count does not establish a causal graph.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. YAML lines 46-51 make
  the entire `GTDB:s__Enterococcus_B_faecium` species an exact synonym
  and equivalence xref for E1165. The native cluster has 4,800 genomes
  spanning many strains, with one target-classified member. Membership
  is not identity. `src/taxonmech/seed.py:451` accepts a source
  `skos:closeMatch` as identity without checking rank/scope; lines
  466-469 emit the unsupported exact synonym and xref, contrary to
  `src/taxonmech/schema/taxonmech.yaml:180`. The maintained owners are
  `src/taxonmech/seed.py` and `tests/test_seed.py`, with separate review
  of kg-microbe's predicate. The 4,800 count is correct for the cluster,
  not E1165.
- Minor: None found.

## Recommended Edits

1. Make the seeder's equivalence decision rank/scope-aware. Preserve
   GTDB classification and provenance while suppressing the unsupported
   species exact synonym and xref on this strain. Explicitly scope
   the count to the species cluster; do not replace 4,800 with 1 while
   retaining species-count semantics.
2. Add a regression in `tests/test_seed.py` for a species closeMatch
   on a strain record, retaining valid same-scope mappings. Review
   kg-microbe's predicate at its maintained source rather than editing
   extracted TSVs or guessing relation direction.
3. After authorized implementation, follow dry-run/canary/regeneration
   steps. Do not hand-edit YAML, invent culture joins, merge E1165 with
   other E-designated strains or promote human review status.

## Follow-up Checks

Run the new regression and `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
Following authorized regeneration, rerun both focused validators and
inspect the emitted record: classification retained, unsupported exact
synonym/xref absent, cluster count scoped, NCBI identity unchanged.
Repeat the exact-terminal GTDB census and target-member check. Run
`just verify-corpus` and full QC for the regeneration. M1 remains
unresolved; this report is not a corrective implementation.

## Additional Notes

Absence checks included ignored files using full structured reads,
`find`, or `rg --no-ignore --hidden`, with `-z` for compressed sources.
The only manual write is this new report; strict validation produced
its standard diagnostic. No YAML, source, prior report, history or
status was edited. No generator, refresh, paid research, GitHub mutation
or cross-repository write occurred. Eukaryota was not re-reviewed.
