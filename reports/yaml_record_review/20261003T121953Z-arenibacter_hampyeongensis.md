# YAML Record Review: Arenibacter hampyeongensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arenibacter_hampyeongensis.yaml`
- Started UTC: 2026-10-03T12:16:43Z
- Finished UTC: 2026-10-03T12:19:53Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:1028743`, Arenibacter hampyeongensis,
rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:178469` (Arenibacter).
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read the entire 468-line YAML, including every nested source assertion.
It contains one BacDive strain, eight assembly assertions, six genome-record
assertions, 18 related-record assertions and six source attestations.
Repeated accessions preserve different sources or matching fields; these
assertion totals are not counts of unique biological genomes.

This is a read-only review. No generated record, maintained source, snapshot,
history, status or page was edited.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/arenibacter_hampyeongensis.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/arenibacter_hampyeongensis.yaml` | PASS; one file, zero errors. |
| Complete lineage and BacDive subtree | PASS; all 11 ancestor objects, complete strain membership and strain scalar fields agree with the raw inventories. |
| Full raw strain-link equality | PASS; eight assembly, six genome and 18 related-record objects match their raw rows in full. |
| Native BV-BRC/NCBI/GTDB field checks | PASS; four BV-BRC, six NCBI and five GTDB assertions agree on their source fields, deposit evidence, taxids and supplied names/levels. GTDB's RS_ wrapper is removed only when projecting its NCBI assembly accession. |
| Native GOLD checks | PASS; all 14 assertions match source fields, labels, taxids, deposits and the full organism/project chain. Native direct-taxon organism count is one. |
| `just verify-corpus` | Not run: full-corpus reproduction check, not a focused record validator. The comparisons above do not substitute for it. |
| `just validate-history` | Not run: ignored-inclusive identifier/label/slug search found no target-specific standalone history. Strict validation checked the embedded seed event. |
| Graph and generated-product checks | Not run: no graph is asserted; generated pages and other products were outside this review. |

Reference verification used inspected authority pages and native snapshots.
Several independent live reference pages were unavailable, as detailed below;
the validators do not prove their live availability.

## Identity and Grounding

The inspected [NCBI Taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028743)
agrees on the ID, current name, species rank, parent, genetic code 11 and
root-first lineage. The local full subtree contains only this taxon.
Native NCBI name records classify the authority-bearing name as authority
and Arenibacter sp. HP12 as includes; both correctly remain related synonyms.

The inspected [LPSN page](https://lpsn.dsmz.de/species/arenibacter-hampyeongensis)
supports name 790480, correct-name status, the 2013 authorship and the listed
2019 emendation. Its served text bears a 2024 print date; the pinned 2026
inventory agrees on these facts. The type-deposit list is incomplete in the
YAML, but the existing JCM match establishes the correct type-strain flag.

GTDB's native species cluster has two members:

| GTDB genome | NCBI identity | Strain context |
| --- | --- | --- |
| RS_GCF_002909255.1 | 1028743, Arenibacter hampyeongensis | JCM 17788, representative, type-material assembly. |
| RS_GCF_023718315.1 | 2183746, Arenibacter sp. N53 | N53, nonrepresentative, not a matching culture deposit. |

Both full native rows were inspected. The species mapping's count of two is
correctly cluster-scoped, not a claim of two HP12 genomes. N53 is not imported
into the type strain merely because GTDB groups the genomes together.
GTDB uses class Bacteroidia, whereas the NCBI backbone uses Flavobacteriia;
the record preserves that source distinction rather than replacing its lineage.

## Evidence

**Inventory provenance.** Identity is supported by
`data/raw/ncbitaxon_taxa.tsv:219193`, nomenclature by
`data/raw/lpsn_names.tsv:27436`, and the strain by
`data/raw/bacdive_strains.tsv:56145`. The scope and legacy-path rows exist.
The two culture-collection crosswalk entries both use taxid 1028743.

**Publications.** The inspected
[original description publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.040683-0)
confirms its DOI, authors, 2013 journal date and abstract. The abstract
explicitly identifies HP12 with KACC 16193 and JCM 17788, independently
supporting the omitted-deposit finding. Phenotypes in that abstract were not
generalized into new species assertions.

The [notification-list publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.051771-0)
confirms the second DOI, title and May 2013 publication metadata. Its abstract
describes the notification's scope; the list's full species table was not
read. BacDive's inspected reference section links PMID 22544794 to the original
paper, but the independent PubMed page presented a browser check.

The authority's 2019 emendation is supported by the inspected LPSN emendations
section. Searches located the corresponding Garcia-Lopez et al. paper, but
its primary full-text retrieval did not expose the target section. No claim
from those search excerpts was promoted into this review. Adding a direct
emendation DOI could improve citation convenience; its absence is not treated
as a separate unsupported-authority finding because the LPSN source is explicit.

**BacDive and marker.** Read all native identity, literature and sequence
objects for 133835 and the relevant sections of the
[BacDive page](https://bacdive.dsmz.de/strain/133835).
Designation HP12, species taxid, JCM/KACC deposits and type status agree.
Source reference 67770 supports unversioned GCA_002909255, BV-BRC 1028743.3
and IMG 2835195961, with their exact descriptions and contig-level scope.
LPSN and BacDive support JF751052 as the HP12 16S accession; native BacDive
specifies a 1,462-base partial sequence. Its live nucleotide page was
unavailable, so the sequence itself was not independently reassessed.

**Genome and related-record chains.** Full direct-taxid searches found one
native BV-BRC object and two current/historical NCBI assembly objects, all
read in full. NCBI explicitly pairs GCA_002909255.1 and GCF_002909255.1,
identifies JCM 17788 and BioSample SAMN08100003, and marks the assemblies as
from type material. GenBank/BV-BRC use PRJNA419854; RefSeq/GTDB use
PRJNA224116. The record preserves both source project contexts.

GOLD's three native objects form Go0043515 -> Gp0388919 -> Ga0350405.
The analysis has no direct organism ID, but its project resolves to the same
organism. Its explicit assembly and IMG fields support the genome assertions;
BioSample and BioProject come from the project. Both organism culture and
strain fields explicitly give JCM 17788 and support the separate provenance rows.

Whole-culture parser checks accept JCM 17788 and KACC 16193, while HP12 and
N53 remain ineligible bare designations. All non-BacDive genome joins use
the existing JCM deposit. Assembly versions, GTDB wrappers and database-specific
IDs remain distinct; sharing a strain is not asserted as genome equivalence.

**Counts and overlays.** Inventory rows support one NCBI name, one LPSN name,
two GTDB genomes, one BacDive strain, one GOLD organism and 13 MADIN trait
assertions. These heterogeneous units are not summed. The strain's
`medium_count: 1` is the inventoried MediaDive strain-level count; it is not
a species-level MediaDive attestation or a newly asserted growth recipe.

BacDive links StrainInfo SI-ID 132219. Ignored-inclusive, decompressed searches
of the native snapshot and all committed StrainInfo overlay files found no
matching exact SI-ID, source BacDive ID, species label/slug or deposit. Its
live page was unavailable. This is a bounded snapshot/access limitation, not
evidence that the strain does not exist or permission to invent a deposit join.
SAMN08100003 was absent from the full native ATB table and committed ATB
overlap under ignored-inclusive searches, so those inputs supply no ATB link.

## Completeness

The complete BacDive subtree has one strain and it is included. Every assembly,
genome and related-record assertion is accounted for. M1 is the only confirmed
record-level gap. Optional phenotype, mechanism and graph fields are correctly
unfilled for a source-inventory seed; aggregate counts are not experimental evidence.

Identifier, label and slug searches covered ignored/hidden raw, curation and
history files, and prior-report names. No standalone target history or prior
review report was found. Native compressed catalogs were explicitly searched
with decompression rather than relying on an ignored-aware search.

## Findings

Counts: **0 blocker, 0 major, 1 minor**.

**M1 - Minor: the LPSN type-deposit list omits KACC 16193.**
YAML lines 54-55 list only JCM 17788. The inspected LPSN page and original
description support KACC 16193 as the other type deposit; NCBI's native
type-material row at `data/raw/ncbi_type_material.tsv:1436` agrees. The record
already retains KACC 16193 in the same strain's collection list at YAML line 88,
and the JCM match correctly establishes `is_type_strain: true`.

The omission is already present in `data/raw/lpsn_names.tsv:27436`.
`src/taxonmech/seed.py:405` faithfully projects it. Future correction belongs
in the maintained upstream KG-Microbe LPSN transform supplying type-deposit
edges, consumed by `src/taxonmech/extract.py:461`. The precise upstream loss
stage was not established from available inputs. Generated YAML and raw
inventories must not be hand-patched to hide the discrepancy.

## Recommended Edits

1. In a separate authorized curation change, inspect the upstream LPSN source
   and transform for 790480, and preserve KACC 16193 alongside JCM 17788.
   Leave HP12 as a designation and do not relax culture matching or add N53
   genome links. The existing true type flag should remain unchanged.
2. After correcting the maintained input/transform, run `just extract-inventory`
   with the configured checkout, dry-run `just seed`, then use
   `just seed-canary NCBITaxon:1028743` to regenerate this record.

## Follow-up Checks

- Compare both type deposits to LPSN and the original description; add a
  focused regression at the maintained extraction boundary.
- Rerun both exact record validators and full source-link comparisons; the
  deposit-list fix should not change the strain's genome assertions.
- Run `just verify-corpus` before merging curation changes; it was skipped here.
- Retry live PubMed, nucleotide, GTDB and StrainInfo access when available;
  require StrainInfo's own-deposit evidence before proposing an overlay.

## Additional Notes

The GTDB live page did not return usable text; native metadata supplied the
complete cluster and linked-genome checks. PubMed/PMC browser checks were not
bypassed. The served LPSN page is older cached content, corroborated here by
the pinned inventory, native NCBI type material and original description.

iModulonDB was not applicable: the YAML asserts no named functional gene,
regulator, pathway or transcriptomic relationship. No phenotype or functional
claim was derived from literature titles, genome metadata or source counts.
This review does not certify the full corpus, archive payloads or published
site. No source refresh, catalog rebuild, history event or status promotion
was performed.
