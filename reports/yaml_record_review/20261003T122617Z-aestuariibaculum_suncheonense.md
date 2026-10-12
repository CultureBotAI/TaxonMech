# YAML Record Review: Aestuariibaculum suncheonense

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/aestuariibaculum_suncheonense.yaml`
- Started UTC: 2026-10-03T12:21:46Z
- Finished UTC: 2026-10-03T12:26:17Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:1028745`, Aestuariibaculum suncheonense,
rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:1386924` (Aestuariibaculum).
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read the entire 487-line YAML, including every nested source assertion.
It contains one BacDive strain, nine assembly assertions, five genome-record
assertions, 20 related-record assertions and six source attestations.
Repeated accessions preserve different sources or matching fields; assertion
totals are not counts of unique biological genomes.

This is a read-only review. No generated record, maintained source, snapshot,
history, status or page was edited.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/aestuariibaculum_suncheonense.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/aestuariibaculum_suncheonense.yaml` | PASS; one file, zero errors. |
| Complete lineage and BacDive subtree | PASS; all 11 ancestor objects, complete strain membership and strain scalar fields agree with raw inventories. |
| Full raw strain-link equality | PASS; all nine assembly, five genome and 20 related-record objects match their raw rows in full. |
| Native BV-BRC/NCBI/GTDB field checks | PASS; eight BV-BRC, six NCBI and five GTDB assertions agree on source fields, deposit evidence, taxids and supplied names/levels. GTDB's RS_ wrapper is removed only when projecting its NCBI assembly accession. |
| Native GOLD checks | PASS; all 14 assertions agree on source fields, names, taxids, deposits and organism/project chain. Both direct-taxon organism objects were read. |
| Native BacDive assembly | PASS; the complete native sequence object supports the remaining assembly assertion and its source reference. |
| `just verify-corpus` | Not run: full-corpus reproduction check, not a focused record validator. These comparisons do not substitute for it. |
| `just validate-history` | Not run: ignored-inclusive identifier/label/slug search found no target-specific standalone history. Strict validation checked the embedded seed event. |
| Graph and generated-product checks | Not run: no graph is asserted; generated pages and other products were outside this review. |

Reference checks used inspected authority pages and native snapshots. Some
independent live pages were unavailable, as detailed below; schema validation
does not prove their availability or independently reassess sequence payloads.

## Identity and Grounding

The inspected [NCBI Taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028745)
agrees on ID, name, species rank, parent, genetic code 11 and lineage. The
full local subtree contains only this taxon. Native NCBI name records classify
the authority-bearing name as authority and Gaetbulibacter sp. SC17 as includes;
both appropriately remain related synonyms.

The inspected [LPSN page](https://lpsn.dsmz.de/species/aestuariibaculum-suncheonense)
supports name 790362, valid and legitimate correct-name status, Jeong et al.
2013 authorship and status as the genus's type species. Its served text bears
a June 2026 print date. Its type list includes JCM 17789, KACC 16186 and SC 17;
the YAML nomenclature list omits the KACC deposit, but the existing JCM match
correctly establishes the strain's true type flag.

The complete native GTDB species census contains two members, both read in full:

| GTDB genome | Strain context | Representative |
| --- | --- | --- |
| RS_GCF_039541475.1 | JCM 17789; taxid 1028745; type-material assembly. | No |
| RS_GCF_014596935.1 | SC17; taxid 1028745; type-material assembly. | Yes |

The count of two is correctly species-cluster-scoped. The record does not
assert that the linked JCM genome is the representative. GTDB uses class
Bacteroidia, whereas the NCBI backbone uses Flavobacteriia; the source mapping
does not replace the NCBI lineage or assert identical classifications.

## Evidence

**Inventory provenance.** Identity is supported by
`data/raw/ncbitaxon_taxa.tsv:219195`, nomenclature by
`data/raw/lpsn_names.tsv:27335`, and the strain by
`data/raw/bacdive_strains.tsv:56101`. Scope and legacy-path rows exist.
The culture crosswalk retains JCM 17789, KACC 16186 and encoded SC 17.

**Publications.** The inspected
[original description publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.037846-0)
confirms the DOI, authors, January 2013 publication metadata and abstract.
Its abstract explicitly identifies SC17 with KACC 16186 and JCM 17789,
independently supporting M1. The full article body was not read and no
phenotype was imported from the abstract into this source-inventory record.

The [notification-list publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.051581-0)
confirms the second DOI, volume 63 part 1 title and April 2013 metadata.
Its abstract explains the notification's purpose; the full species table was
not read. BacDive's inspected reference section associates PMID 22427453
with the original description. The independent PubMed page presented a
browser check, which was not bypassed.

**BacDive and marker.** Read the complete native identity, literature and
sequence objects for 133791 and the relevant sections and references of the
[BacDive page](https://bacdive.dsmz.de/strain/133791).
Its culture list contains JCM 17789, KACC 16186 and SC 17. The native strain
designation property is absent and the raw designation is empty, so the YAML's
absent designation is source-faithful rather than an established omission.

Native sequence reference 124043 supports unversioned GCA_039541475, contig
level, the exact assembly description and taxid. BacDive identifies that
reference as automatic sequence-database matching, not manually established
genome equivalence. This native object supplies no BV-BRC or IMG accession;
those YAML links have their own inspected source chains. LPSN and BacDive
support JF751043; native BacDive describes a 1,482-base partial SC17 16S
sequence. Its live nucleotide page was unavailable.

**Genome source distinctions.** Full native direct-taxid searches found two
BV-BRC objects and four current/historical NCBI assembly objects, all read
in full. The JCM branch is BV-BRC 1028745.8, GCA_039541475.1 and
GCF_039541475.1, BioSample SAMD00645731. NCBI explicitly marks the GCA/GCF
pair as identical, latest and assembled from type material. GenBank/BV-BRC
use PRJDB10510, whereas RefSeq/GTDB use PRJNA224116. All asserted values
retain their own source context.

The other branch is BV-BRC 1028745.3, GCA_014596935.1 and
GCF_014596935.1, BioSample SAMN16078603. Its native strain value is SC17;
BV-BRC supplies no culture-collection value. The original paper establishes
the strain-name relationship, but the importer requires an explicit eligible
culture identifier in the source row. Thus these SC17-only rows are not
joined through a species taxid or by treating a bare designation as a registry.

**GOLD chain.** The two direct-taxon organism objects are Go0043527 (JCM
17789) and Go0576240 (SC17, empty culture field). The included JCM chain is
Go0043527 -> Gp0855073 -> Ga0682164. The analysis has no direct organism ID,
but its explicit project resolves to Go0043527. The project supplies
PRJDB10510 and SAMD00645731; the analysis supplies GCA_039541475.1 and
IMG 8148099366. Both organism culture and strain fields explicitly name JCM
17789, supporting the separate provenance assertions. NCBI web LinkOut's
SC17-associated GOLD/IMG links were not substituted for this native JCM chain.

Whole-culture parser checks accept JCM 17789, JCM:17789 and KACC 16186;
SC17 and SC 17 remain ineligible bare designations. The encoded SC 17 entry
is preserved from BacDive but does not become an eligible SC registry key.
Shared strain identity is not asserted as equivalence between genome datasets.

**Counts and bounded absences.** Inventory rows support one NCBI name, one
LPSN name, two GTDB genomes, one BacDive strain, two GOLD organisms and 29
MADIN trait assertions. These units are not interchangeable. The strain's
`medium_count: 1` is a strain-level inventory count, not a species-level
MediaDive attestation or a newly asserted growth recipe.

BacDive links StrainInfo SI-ID 393818. Ignored-inclusive, decompressed
searches of all local StrainInfo files found no matching exact SI-ID, source
BacDive ID, target taxid, label/slug or JCM/KACC deposit. Its live page was
unavailable. This bounds a snapshot/access limitation; it does not establish
global nonexistence or authorize an inferred StrainInfo strain join.

The full native ATB table contained no SAMD00645731. Ignored-inclusive
searches of committed ATB files also found no target ID, BacDive ID, JCM/KACC
deposit or that BioSample. Those inspected inputs supply no ATB assertion
for the included JCM branch; no absence claim is made for SAMN16078603.

## Completeness

The complete BacDive subtree has one strain and it is included. Every assembly,
genome and related-record assertion is accounted for. M1 is the only confirmed
record-level gap. Optional phenotype, mechanism and graph fields are correctly
unfilled for a source-inventory seed; aggregate counts are not experimental evidence.

Identifier, label and slug searches covered ignored/hidden raw, curation and
history files and prior-report names. No target-specific standalone history
or prior review report was found. Compressed catalogs were explicitly searched
with decompression, not an ignored-aware search. Source counts do not imply
that every same-species genome qualifies for this strain's collection join.

## Findings

Counts: **0 blocker, 0 major, 1 minor**.

**M1 - Minor: the LPSN type-deposit list omits KACC 16186.**
YAML lines 54-55 list only JCM 17789. The inspected LPSN page and original
description also support KACC 16186; NCBI's native type-material row at
`data/raw/ncbi_type_material.tsv:1442` agrees. YAML line 87 already retains
KACC 16186 in the same strain's culture list, and the existing JCM match
correctly establishes `is_type_strain: true`.

The omission is already present in `data/raw/lpsn_names.tsv:27335`.
`src/taxonmech/seed.py:405` faithfully projects that list. The future fix
belongs in the maintained upstream KG-Microbe LPSN transform supplying
type-deposit edges, consumed by `src/taxonmech/extract.py:461`. The precise
upstream loss stage was not established from these inputs. Do not hand-patch
generated YAML or raw inventories to conceal the discrepancy.

## Recommended Edits

1. In a separate authorized curation change, inspect the upstream LPSN source
   and transform for 790362 and preserve KACC 16186 alongside JCM 17789.
   Preserve the true type flag. Do not relax culture matching or treat SC17
   as a culture registry to force additional genome assertions.
2. After correcting the maintained input/transform, run `just extract-inventory`
   with the configured checkout, dry-run `just seed`, then use
   `just seed-canary NCBITaxon:1028745` to regenerate this record.

## Follow-up Checks

- Compare both type deposits to LPSN and the original description; add a
  focused regression at the maintained extraction boundary.
- Rerun both exact record validators and full source-link comparisons. The
  type-deposit-list correction should not alter the strain's genome assertions.
- Run `just verify-corpus` before merging curation changes; it was skipped here.
- Retry live PubMed, nucleotide, GTDB and StrainInfo access when available;
  require StrainInfo's own deposit evidence before proposing an overlay.

## Additional Notes

The live GTDB page did not return usable text; native metadata supplied the
complete two-member census and linked-genome checks. Independent live PubMed,
nucleotide and StrainInfo checks remain incomplete; local evidence and the
inspected authority/publisher pages support the bounded verdict above.

iModulonDB was not applicable: the YAML asserts no named functional gene,
regulator, pathway or transcriptomic relationship. No phenotype was inferred
from literature titles, genome metadata or source counts. This review does
not certify the full corpus, archive payloads or published site. No source
refresh, catalog rebuild, history event or status promotion was performed.
