# YAML Record Review: Helicobacter pylori 10700

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_10700.yaml`
- Started UTC: 2026-10-03T13:26:29Z
- Finished UTC: 2026-10-03T13:28:37Z
- Verdict: needs curation

## Target

Generated `TaxonRecord`, `NCBITaxon:1028810`, Helicobacter pylori 10700;
rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:210`.
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read all 84 YAML lines: ten ancestors, one GTDB mapping, three synonyms,
one GTDB xref, code 11, zero BacDive strains, three source attestations
and one embedded seed event. No publication, phenotype or graph is asserted.

Read-only review: only this report was manually written. No source,
generated YAML, history, status or page was changed. Eukaryota was excluded.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/helicobacter_pylori_10700.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/helicobacter_pylori_10700.yaml` | PASS; one file, zero errors. |
| Complete raw identity, lineage and NCBI alias comparison | PASS; all ten ancestors, identity, rank, parent, code and two NCBI synonyms agree. |
| Complete BacDive subtree membership | PASS; the target is its only subtree member and has zero classified BacDive entries. |
| GTDB census | Exact terminal-species scan of all 19 manifest-listed native shards: 633 genomes, 55 distinct NCBI taxids, one target-taxid genome. |
| Source counts and selection | PASS as inventory values; their identity interpretation is the major finding. |
| `just verify-corpus` | Not run: full-corpus reproduction check; no focused equivalent was substituted. |
| `just validate-history` | Not run: ignored-inclusive target search found no standalone history; strict validation checked the embedded event. |
| Graph and products | Graph gate not applicable; no graph asserted. Pages and exports were not audited. |

Live NCBI Taxonomy, BioSample, BioProject and the candidate PMSS1 BacDive
page were inspected. Relevant identity passages of a primary paper were
read. GTDB web pages were inaccessible; the pinned RS232 native catalog
was used. No sequence payload or experimental phenotype was reassessed.

## Identity and Grounding

The [current NCBI summary](https://www.ncbi.nlm.nih.gov/taxonomy/1028810)
identifies 10700 as a strain. The
[legacy taxonomy browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1028810&lvl=3&mode=node)
agrees on identifier, scientific name, equivalent strain names, code 11
and lineage, but displays `no rank`. The current summary and pinned
inventory support `STRAIN`; the interface disagreement is not silently
discarded or used to rewrite the record.

`data/raw/ncbitaxon_taxa.tsv:219213` matches the target. The three native
name objects at `data/catalog/ncbi_names-0005.jsonl.gz:28279` onward
contain the scientific name and two equivalent names retaining 10700.
The GTDB synonym at YAML line 46 drops the strain designation and denotes
the species. The equivalent xref at line 57 has the same scope problem.

## Evidence

**Attestations and audit.** `data/raw/madin_taxa.tsv:539` supplies one
trait assertion; no unspecified trait is inferred from that count.
The NCBI count is one scientific-name attestation, not three name strings.
`curation/seed_scope.tsv:36105` agrees with the three-source selection and
the embedded seed event dated 2026-09-13T17:54:04Z. The NCBI snapshot date
is explicitly 2026-09-13.

**GTDB classification and count.** `data/raw/gtdb_mappings.tsv:1244`
supplies the target closeMatch and count 633;
`data/raw/gtdb_species.tsv:73699` supplies the species count. A structured
scan of every native GTDB genome shard selected only records whose last
taxonomy component is exactly `s__Helicobacter pylori`, excluding suffixed
neighboring clusters. Results: 633 genomes, 55 distinct NCBI taxids and
603 distinct strain-field strings. The latter are source strings, not a
claim of 603 proven biological strains. Only one genome has taxid 1028810.
All scanned paths match the 19 files in `data/catalog/MANIFEST.json`.

Complete target and representative source objects were read:

| Native object | Classification and identity |
| --- | --- |
| `data/catalog/gtdb_genomes-0012.jsonl.gz:22527` | GB_GCA_009901925.1, strain 10700, taxid 1028810, SAMN13850676, PRJNA66587; nonrepresentative member. |
| `data/catalog/gtdb_genomes-0003.jsonl.gz:6716` | RS_GCF_900478295.1, NCTC 11637, taxid 102618, SAMEA3178013; representative, assembly from type material. |

The representative is not 10700. Its culture deposits and type-material
status cannot be transferred to this record. The raw LPSN row at
`data/raw/lpsn_names.tsv:17436` maps the species name and its GTDB species
ID to NCBITaxon:210, not to 1028810. Likewise, GTDB's Campylobacteria
class does not replace the carried NCBI Epsilonproteobacteria lineage.

Live [GTDB search](https://gtdb.ecogenomic.org/searches?s=al&q=Helicobacter%20pylori)
and [genome page](https://gtdb.ecogenomic.org/genome?gid=GCA_009901925.1)
requests failed through the web tool. The count and classification above
are for the committed RS232 snapshot, not a new live-release census.

**Genome metadata.** `data/catalog/ncbi_genbank-0008.jsonl.gz:36925`
contains current GCA_009901925.1, assembly ASM990192v1, Scaffold level,
31 scaffolds and 110 contigs, 1,647,427 bp total and 1,599,347 bp ungapped.
It explicitly names taxid 1028810, strain 10700, SAMN13850676,
PRJNA66587 and AFND00000000.1. RefSeq exclusion reasons are annotation
completeness failure and many frameshifted proteins; no paired RefSeq
assembly is supplied. These are source quality flags, not a clinical or
mechanistic finding about the strain.

`data/bvbrc/bvbrc-0000.jsonl.gz:2996` independently carries genome
1028810.6, WGS, the same assembly, sample, project and WGS stem.
The [BioSample page](https://www.ncbi.nlm.nih.gov/biosample/SAMN13850676)
confirms the strain and project. The
[BioProject page](https://www.ncbi.nlm.nih.gov/bioproject/66587)
explicitly joins the target taxid, assembly at Scaffold level and sample.
It describes 10700 as SS1's progenitor, not as SS1 itself. Its multiisolate
scope does not make every project sample the same strain or assembly.

**GOLD context.** Full objects at
`data/gold/organisms.jsonl.gz:10579` and
`data/gold/projects.jsonl.gz:10437` identify Go0012012 and Gp0012012,
10700, taxid 1028810 and PRJNA66587. The organism's culture-collection
field and the project's BioSample field are empty. Ignored-inclusive
decompressed searches for those GOLD IDs, target assembly and WGS stem
found no matching analysis object in `data/gold/`. Do not invent an IMG
identifier or fill the workbook's empty sample field by name matching.

**PMSS1 is an identity lead requiring preserved distinctions.**
[Draper et al. 2017, DOI 10.1128/mBio.02321-16](https://journals.asm.org/doi/10.1128/mbio.02321-16),
in the inspected introduction, identifies 10700 as PMSS1 and distinguishes
the mouse-passaged derivative SS1. This supports a literature alias and
parent/derivative distinction, not equivalence of every laboratory stock
or assembly using those names.

The pinned taxonomy separately retains PMSS1 at NCBITaxon:1431450
(`data/raw/ncbitaxon_taxa.tsv:357530`).
`data/raw/bacdive_strains.tsv:79889` and the full native object at
`data/bacdive/records.jsonl.gz:79888` give PMSS1, DSM 105294 and
BacDive 157650, classified at the parent species 210. The
[BacDive authority page](https://bacdive.dsmz.de/strain/157650)
confirms that deposit and classification and gives its laboratory history.
Neither a paper alias nor a shared species automatically moves this
deposit into the 10700 subtree. This source disagreement is retained as a
bounded follow-up, not resolved by a taxon merge or inferred genome join.

## Completeness

No additional required-field omission was established. Zero BacDive
strains is correct under the pinned classification rule; it does not
mean 10700 has never been cultured, sequenced or discussed under an alias.
The parent species' LPSN/type-strain data must not be copied here.

Ignored-inclusive target identifier, label, slug, sample and assembly/WGS
searches covered `history/`, `data/atb/`, `data/bacdive/` and
`data/straininfo/`, decompressing files where needed. No direct target
history, BacDive entry or overlay match was found. A separate bare-10700
BacDive search returned unrelated identifiers and deposits, not a target
identity. The PMSS1 candidate described above was searched separately.

Decompressed, ignored-inclusive searches of current RefSeq, historical
RefSeq and historical GenBank catalogs found no target-taxid/name/sample/
assembly match. A direct sample/assembly search of the complete local
`data/catalog/allthebacteria.tsv.xz` likewise found no match. These
bounded results do not claim worldwide absence or explain noncoverage.

Raw-inventory searches found no target LPSN or GOLD count row. The native
GOLD workbook and KGX-derived taxon-count inventory are distinct routes,
as documented in `docs/HARMONIZATION.md`; their coverage difference alone
does not establish a missing required attestation. Bare 10700 is not a
registered collection accession for importing its native genome metadata.

The YAML asserts no gene, regulator, transcriptomic dataset or causal
graph; iModulonDB and graph gates are not applicable. The paper was used
only for identity context, not to add experimental traits to this record.

## Findings

**Major M1: a GTDB species is asserted as equivalent to one strain.**
The exact synonym at YAML lines 46-49 and xref at line 57 equate 10700 to
the 633-genome species cluster. Native evidence shows membership of one
target-taxid genome, not equality of scopes. Schema
`src/taxonmech/schema/taxonmech.yaml:180` reserves xrefs for true
equivalences; its mapping description at line 428 describes closeMatch
between the same species, not a species and an individual strain.

The local maintained owner is `src/taxonmech/seed.py:451`, where any
closeMatch is accepted as identity without a rank/scope guard, leading
to the xref and exact synonym at lines 467-469. The raw predicate is
preserved by `src/taxonmech/extract.py:519`; its upstream kg-microbe
interpretation also requires review. These manifestations are one
connected major finding.

Blocker: 0. Major: 1. Minor: 0. The PMSS1 lead is not counted as a
confirmed defect: local policy does not permit inference of a deposit
classification or a taxon merge from that alias.

## Recommended Edits

1. Make identity promotion in `src/taxonmech/seed.py` rank- and scope-aware.
   Remove unsupported exact-strain claims through the generator while
   retaining evidenced GTDB membership and the species count of 633.
2. Review source mapping semantics upstream in kg-microbe and update
   `docs/HARMONIZATION.md` for an approved interpretation. Do not guess a
   replacement predicate or manually patch raw/generated artifacts.
3. Add regression tests for below-species targets, singleton and
   multi-genome clusters, and positive same-scope species equivalence.
4. In a separately authorized identity review, resolve the 10700/PMSS1
   naming and stock-history question with NCBI and culture-source
   evidence. Any retained literature alias needs explicit provenance;
   neither SS1 nor every PMSS1 assembly becomes an equivalent identifier.

## Follow-up Checks

After an authorized fix, run focused seeder tests, both target validators,
a dry `just seed`, and `just seed-canary NCBITaxon:1028810`. Inspect the
canary for preservation of NCBI identity, both strain aliases and the
633-genome cluster count without a species-level exact-strain alias or
xref. Run full `just verify-corpus` before corpus-wide reproduction claims.

Revisit the GTDB web authority when accessible. For any future PMSS1
enrichment, check deposit lineage and explicitly supported genome/sample
chains before joining them; keep the NCBI taxon concepts and SS1
derivative distinct unless authoritative source changes justify otherwise.
No curation changes or outbound contacts were made during this review.

## Additional Notes

The complete target was inspected, not sampled. It remains `SEEDED` and
has no newly added human-review status or history event. Passing schema
validation does not resolve M1. This report establishes neither complete
corpus review nor an audit of all PMSS1 or parent-species source assertions.
