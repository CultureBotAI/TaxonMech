# YAML Record Review: Christiangramia aestuarii

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/christiangramia_aestuarii.yaml`
- Started UTC: 2026-10-03T12:28:28Z
- Finished UTC: 2026-10-03T12:33:29Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:1028746`, Christiangramia aestuarii,
rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:292691` (Christiangramia).
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read the entire 520-line YAML, including every nested source assertion.
It contains one BacDive strain, ten assembly assertions, seven genome-record
assertions, 20 related-record assertions and six source attestations.
Repeated accessions preserve different sources or matching fields; these
assertion totals are not counts of unique biological genomes.

This is a read-only review. No generated record, maintained source, snapshot,
history, status or page was edited.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/christiangramia_aestuarii.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/christiangramia_aestuarii.yaml` | PASS; one file, zero errors. |
| Complete lineage and BacDive subtree | PASS; all 11 ancestor objects, complete strain membership and strain scalar fields agree with raw inventories. |
| Full raw strain-link equality | PASS; all ten assembly, seven genome and 20 related-record objects match their raw rows in full. |
| Native source-field checks | PASS; all 37 assertions: four BacDive, eight BV-BRC, 14 GOLD, five GTDB and six NCBI Assembly. Checks covered identifiers, source fields, taxids, supplied names/levels, deposit evidence and GOLD chains. |
| Native source censuses | Two BV-BRC objects, four current/historical NCBI assembly objects, two GTDB species members and two GOLD organism objects; all matching objects read in full. |
| `just verify-corpus` | Not run: full-corpus reproduction check, not a focused record validator. The comparisons above do not substitute for it. |
| `just validate-history` | Not run: ignored-inclusive identifier/label/slug search found no target-specific standalone history. Strict validation checked the embedded seed event. |
| Graph and generated-product checks | Not run: no graph is asserted; generated pages and other products were outside this review. |

Reference verification used inspected authority pages and native snapshots.
Some independent live reference checks were unavailable, as detailed below;
schema validation does not establish live availability or sequence quality.

## Identity and Grounding

The inspected [NCBI Taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028746)
agrees on ID, current name, species rank, parent, genetic code 11 and lineage.
The complete local subtree contains only this taxon. Native NCBI names classify
the authority-bearing current name as authority, Gramella sp. BS12 as includes,
and Gramella aestuarii Jeong et al. 2013 as synonym. The record preserves the
first two as related synonyms and the latter as an exact NCBI synonym.

The inspected [current LPSN name](https://lpsn.dsmz.de/species/christiangramia-aestuarii)
supports record 37615, valid correct-name status and the 2023 combination.
Its served page bears a November 2025 print date; the pinned 2026 inventory
agrees. The [basonym page](https://lpsn.dsmz.de/species/gramella-aestuarii)
confirms record 791014, homotypic synonymy and the old name's illegitimate
status. The old name is retained as an LPSN related synonym, not presented
as a second current name. Its raw row lacks a direct NCBI mapping, explaining
why the seeder includes it through the synonym relation rather than as a
second mapped nomenclature entry.

The complete native GTDB species census contains two genomes:

| GTDB genome | Strain | Representative | Assembly level |
| --- | --- | --- | --- |
| RS_GCF_009735585.1 | BS12 | Yes | Contig |
| RS_GCF_039541495.1 | JCM 17790 | No | Scaffold |

Both have species/taxon ID 1028746 and are marked as assemblies from type
material. The count of two is correctly species-cluster-scoped. The record
does not claim the linked JCM genome is the GTDB representative. GTDB's class
Bacteroidia differs from NCBI's Flavobacteriia; the mapping preserves that
source distinction rather than replacing the NCBI backbone.

## Evidence

**Inventory provenance.** Identity is supported by
`data/raw/ncbitaxon_taxa.tsv:219196`, nomenclature by
`data/raw/lpsn_names.tsv:6573`, and the strain by
`data/raw/bacdive_strains.tsv:56273`. The old LPSN name is at raw line 27914.
Scope, legacy-path and both culture-deposit crosswalk rows exist.

**Publications.** The inspected
[replacement-name publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.005806)
and [PubMed record](https://pubmed.ncbi.nlm.nih.gov/37040175/)
agree on DOI 10.1099/ijsem.0.005806, PMID 37040175, Deshmukh and Oren,
and April 2023 publication. Their abstract explains the replacement of the
illegitimate generic name Gramella by Christiangramia and new combinations.
The species-specific nomenclatural assignment is independently explicit in
LPSN; the full article body was not read.

The notification DOI's publisher and DOI landing pages were unavailable.
The inspected [notification PubMed record](https://pubmed.ncbi.nlm.nih.gov/37526974/)
confirms DOI 10.1099/ijsem.0.005937, its volume-73-part-4 notification title,
authors and 2023 publication. It supplies no abstract; the full species list
was not checked. This verifies bibliographic identity, not a new taxonomic claim.

The inspected [original species-description abstract](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.048694-0)
explicitly identifies BS12 with KACC 16188 and JCM 17790. It independently
supports M1. No phenotype from that abstract was generalized into new
species assertions, and the full article body was not read.

**BacDive and marker.** Read all native identity, literature and sequence
objects for 133966 and the relevant sections and references of the
[BacDive page](https://bacdive.dsmz.de/strain/133966).
Designation BS12, both deposits, taxid and true type status agree. The native
older classification still says Gramella, while its LPSN block supplies the
current Christiangramia name; this is source history, not a mismatched strain.

Reference 66792 explicitly supplies unversioned GCA_009735585, BV-BRC
1028746.3 and IMG 2891820663 with the BS12 description and contig level.
Reference 124043 supplies unversioned GCA_039541495 with the JCM 17790
description and scaffold level, but no BV-BRC or IMG ID. All four BacDive
assertions match their complete native sequence objects. These are retained
as BacDive's automatically annotated links, not promoted to independent
proof that different genome identifiers denote identical sequence.

LPSN and BacDive support marker JF751047; native BacDive describes a
1,492-base partial BS12 16S sequence. The live nucleotide page did not
return usable text, so the sequence payload was not independently reassessed.

**Assembly and genome distinctions.** Native BV-BRC 1028746.11 and the
GCA_039541495.1/GCF_039541495.1 pair explicitly name JCM 17790 and
BioSample SAMD00645732. GenBank/BV-BRC use PRJDB10510; RefSeq/GTDB use
PRJNA224116. NCBI explicitly pairs the accessions as identical and marks
them latest and from type material. The record retains each source's project,
assembly version, description and matching field.

The BS12 branch is BV-BRC 1028746.3 and
GCA_009735585.1/GCF_009735585.1, BioSample SAMN12179531. Its native BV-BRC
culture field is absent, and NCBI/GTDB name only BS12 as strain identifier.
The original paper establishes the strain-name relationship, but the
collection-based importer cannot use bare BS12 as a registered deposit.
Direct BacDive links remain valid source assertions; they do not authorize
transferring every same-species or BS12-only source row into the strain.

Whole-culture parser checks accept JCM 17790, JCM:17790 and KACC 16188,
while BS12 remains ineligible. No source association asserts equivalence
between the BS12 and JCM genome datasets. GTDB wrappers are retained in GTDB
IDs and removed only when projecting an explicitly supplied NCBI accession.

**GOLD chain.** The direct-taxon organisms are Go0546439 (BS12, empty
culture field) and Go0704300 (JCM 17790). The included chain is
Go0704300 -> Gp0829618 -> Ga0675234. The analysis has no direct organism
ID, but its explicit project resolves to Go0704300. The project supplies
PRJDB10510 and SAMD00645732; the analysis supplies GCA_039541495.1 and
IMG 8127188043. Both organism culture and strain fields explicitly name
JCM 17790. All 14 provenance assertions match those full native objects.

**Counts and overlays.** Raw inventories support one NCBI name, one LPSN
name, two GTDB genomes, one BacDive strain, two GOLD organisms and 33 MADIN
trait assertions. These heterogeneous units are not summed. The strain's
`medium_count: 1` is a strain-level inventory count, not a species-level
MediaDive attestation or a newly asserted growth recipe.

BacDive links StrainInfo SI-ID 28059. Ignored-inclusive, decompressed
searches of all local StrainInfo files found no matching typed SI-ID,
source BacDive ID, target taxid, label/slug or JCM/KACC deposit. Broad numeric
hits for 28059 were unrelated collection numbers or a different SI-DP, not
the target SI-ID. Its live page exposed only a JavaScript shell. This is a
bounded snapshot/access limitation, not evidence of global nonexistence.

SAMD00645732 was absent from the full native ATB table. Ignored-inclusive
searches of committed ATB files also found no target ID, BacDive ID, JCM/KACC
deposit or that BioSample. These inputs supply no ATB assertion for the
included JCM branch. No absence claim is made for SAMN12179531.

## Completeness

The complete BacDive subtree has one strain and it is included. Every assembly,
genome and related-record assertion is accounted for. M1 is the only confirmed
record-level gap. Optional phenotype, mechanism and graph fields are correctly
unfilled for a source-inventory seed; aggregate counts are not experimental evidence.

Identifier, label and slug searches covered ignored/hidden raw, curation and
history files and prior-report names. No target-specific standalone history
or prior report was found. Compressed source catalogs were explicitly searched
with decompression rather than relying on an ignored-aware search.

## Findings

Counts: **0 blocker, 0 major, 1 minor**.

**M1 - Minor: the LPSN type-deposit list omits KACC 16188.**
YAML lines 54-55 list only JCM 17790. Both LPSN name pages and the original
description support KACC 16188; NCBI's native type-material row at
`data/raw/ncbi_type_material.tsv:1448` agrees. YAML line 95 already retains
KACC 16188 in the same strain's culture list, and the existing JCM match
correctly establishes `is_type_strain: true` at line 96.

The omission is already present in `data/raw/lpsn_names.tsv:6573`.
`src/taxonmech/seed.py:405` faithfully projects the raw type list. The future
fix belongs in the maintained upstream KG-Microbe LPSN transform supplying
type-deposit edges, consumed by `src/taxonmech/extract.py:461`. The exact
upstream loss stage was not established. Do not hand-patch generated YAML
or raw inventories to conceal the discrepancy.

## Recommended Edits

1. In a separate authorized curation change, inspect the upstream LPSN source
   and transform for 37615 and its basonym 791014, preserving KACC 16188
   alongside JCM 17790. Preserve the true type flag and the current-name /
   synonym distinction; do not relax culture matching to admit bare BS12.
2. After correcting the maintained input/transform, run `just extract-inventory`
   with the configured checkout, dry-run `just seed`, then use
   `just seed-canary NCBITaxon:1028746` to regenerate this record.

## Follow-up Checks

- Compare both type deposits to LPSN and the original description; add a
  focused regression at the maintained extraction boundary.
- Rerun both exact record validators and full source-link comparisons. The
  deposit-list correction should not alter the strain's genome assertions.
- Run `just verify-corpus` before merging curation changes; it was skipped here.
- Retry live GTDB, nucleotide and StrainInfo access, and the notification's
  full text, when available. Require StrainInfo's own deposit evidence before
  proposing an overlay.

## Additional Notes

The historical scope reason quotes five sources; the current record explicitly
attests six. The seed event preserves that earlier reason from the scope row
and separately lists all six current sources. The quoted rationale is not
used as a current source count in this review.

iModulonDB was not applicable: the YAML asserts no named functional gene,
regulator, pathway or transcriptomic relationship. No phenotype was derived
from literature titles, predictions, genome metadata or source counts.
This review does not certify the full corpus, archive payloads or published
site. No source refresh, catalog rebuild, history event or status promotion
was performed.
