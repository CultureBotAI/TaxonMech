# YAML Record Review: Microbulbifer gwangyangensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbulbifer_gwangyangensis.yaml`
- Started UTC: 2026-10-03T12:35:34Z
- Finished UTC: 2026-10-03T12:38:30Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:1028749`, Microbulbifer gwangyangensis,
rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:48073` (Microbulbifer).
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read the entire 137-line YAML. It contains one BacDive strain, two related
GOLD organism assertions and five source attestations. No assembly, genome
record or GTDB species mapping is asserted. The two GOLD assertions preserve
different matching fields on one source organism; they are not two organisms
or two genomes.

This is a read-only review. No generated record, maintained source, snapshot,
history, status or page was edited.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/microbulbifer_gwangyangensis.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/microbulbifer_gwangyangensis.yaml` | PASS; one file, zero errors. |
| Complete lineage and BacDive subtree | PASS; all nine ancestor objects, complete strain membership and strain scalar fields agree with raw inventories. |
| Full raw strain-link equality | PASS; zero assembly, zero genome and two related-record objects exactly match the raw strain-link rows. |
| Native GOLD field checks | PASS; both complete assertions agree on source ID, name, taxid, organism ID, source field, verbatim culture/strain value and eligible deposit match. |
| Native genome-source search | No matching NCBI current/historical assembly, BV-BRC or GTDB genome row in the inspected complete catalogs; searched both current and merged taxids, species names, included names and culture deposits, including ignored/compressed files. |
| `just verify-corpus` | Not run: full-corpus reproduction check, not a focused record validator. The comparisons above do not substitute for it. |
| `just validate-history` | Not run: ignored-inclusive identifier/label/slug search found no target-specific standalone history. Strict validation checked the embedded seed event. |
| Graph and generated-product checks | Not run: no graph is asserted; generated pages and other products were outside this review. |

Reference verification used inspected authority/publisher pages and native
snapshots. Independent PubMed, nucleotide, StrainInfo and merged-ID live
checks did not expose usable record text; these limitations are detailed below.

## Identity and Grounding

The inspected [NCBI Taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028749)
agrees on ID, current name, species rank, parent, genetic code 11 and lineage.
The full local subtree contains only this taxon. The complete native name rows
classify the authority-bearing name as authority and Microbulbifer sp. GY2
and Microbulbifer sp. M9 as includes. All three correctly remain related,
not exact, synonyms. This does not equate the M9 isolate with the GY2 type strain.

The [LPSN page](https://lpsn.dsmz.de/species/microbulbifer-gwangyangensis)
confirms record 790670, Jeong et al. 2013 authorship, valid correct-name
status and type strain GY2 with JCM 17800 and KACC 16189. The existing JCM
match correctly establishes the true type flag, despite M1's incomplete
nomenclature deposit list.

`data/raw/ncbi_merged_ids.tsv:9489` maps old ID 1243626 to 1028749. The live
old-ID page was unavailable, so the merge assertion here rests on the pinned
inventory. Both IDs were included in the genome-source searches. The merge
does not create a second strain, species record or genome association.

## Evidence

**Raw provenance.** Identity is supported by
`data/raw/ncbitaxon_taxa.tsv:219199`, nomenclature by
`data/raw/lpsn_names.tsv:27608`, and the strain by
`data/raw/bacdive_strains.tsv:56174`. Both culture crosswalk rows, the
scope row and the legacy-page path exist. The scope reason and seed event
agree on five sources.

**Literature and strain scope.** The inspected
[original description publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.042606-0)
confirms the DOI, authors, April 2013 publication metadata and abstract.
The paper describes two species, but its abstract explicitly assigns
GY2 = KACC 16189 = JCM 17800 to M. gwangyangensis. Its separate SPO729
type and deposits belong to M. pacificus and were not transferred here.
This independently supports M1 without importing phenotype claims.

The [notification publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.053850-0)
confirms the second DOI, volume-63-part-4 notification title and July 2013
publication. Its abstract explains the notification's purpose; the full species
list was not read. Neither publication's full article body was reassessed.

The inspected BacDive reference section associates PMID 22798656 with the
original description and DOI 10.1099/ijs.0.042606-0. The independent PubMed
retrieval ultimately returned only footer text, so it did not independently
verify the full PMID record. BacDive's literature list uses 2012 while the
publisher and LPSN use the 2013 journal date; the YAML correctly carries
the latter authorship year. No new publication-date field was inferred.

**BacDive and marker.** Read the complete native BacDive 133864 object and
the relevant sections and references of the
[BacDive page](https://bacdive.dsmz.de/strain/133864).
Designation GY2, taxid, JCM/KACC deposits and type status agree. Its native
sequence section contains only the GY2 16S marker JF751045, described as a
1,497-base partial sequence; there is no native genome-sequence object.
The live nucleotide page was unavailable. LPSN and BacDive support the
marker identity, but its sequence payload was not independently reassessed.
The marker is not promoted to an assembly or whole-genome identifier.

**GOLD is organism context, not a genome.** The complete native organism
object Go0044332 names Microbulbifer gwangyangensis JCM 17800, taxid 1028749,
and JCM 17800 in both its culture-collection and strain fields. Both YAML
assertions preserve those exact, separately evidenced matching fields.
Whole-culture parser checks accept JCM 17800 and KACC 16189, while GY2
and M9 remain ineligible bare designations.

Ignored-inclusive decompressed searches of all native GOLD organism,
project and analysis files found only this organism for the target IDs,
name, deposits and explicit Go0044332 chain. No corresponding project or
analysis row supplied an assembly, IMG, BioSample or BioProject link.
Consequently no GOLD genome or project assertion is missing from the
inspected chain. The taxon-level GOLD count of one is consistent with it.

**Genome and overlay completeness.** Searched all native GenBank and RefSeq
current/historical shards, GTDB genome shards and BV-BRC shards for the
current and merged taxids, species name and normalized form, included names,
and JCM/KACC accession spellings. Case-insensitive, ignored-inclusive,
decompressed searches found no relevant genome row. Raw GTDB inventory
searches likewise found no target mapping. This supports leaving the fields
empty for the inspected snapshots; it does not establish that a genome
cannot exist elsewhere or in a later release.

BacDive links StrainInfo SI-ID 132269. Ignored-inclusive, decompressed
searches of all local StrainInfo files found no exact typed SI-ID, source
BacDive ID, current/merged taxid, species name/slug or JCM/KACC deposit.
The live SI page was unavailable. Its BacDive link alone cannot establish
an eligible own-deposit match or supply sequence evidence.

The committed ATB overlay and full native ATB table yielded no target
ID/name/deposit match under ignored-inclusive searches. More importantly,
the record and raw links supply no BIOSAMPLE assertion through which an
ATB assembly could be joined. These are bounded source searches, not a
global claim that every unlabelled ATB sample has been identified.

**Counts.** Inventories support one NCBI name, one LPSN name, one BacDive
strain, one GOLD organism and seven MADIN trait assertions. These units
are not interchangeable and are not summed. The strain's `medium_count: 1`
is a strain-level inventory count, not a species-level MediaDive attestation
or an independently curated growth recipe.

## Completeness

The full BacDive subtree has one strain and it is included. Every existing
related-record assertion is accounted for. M1 is the only confirmed gap;
the absence of genome fields is supported within the inspected source scope.
Optional phenotype, mechanism, graph and record-level evidence slots may
remain empty for a source-inventory seed.

Identifier, label and slug searches covered ignored/hidden raw, curation
and history files and prior-report names. No target-specific standalone
history or prior report was found. Compressed sources were explicitly
searched with decompression, not an ignored-aware search.

## Findings

Counts: **0 blocker, 0 major, 1 minor**.

**M1 - Minor: the LPSN type-deposit list omits KACC 16189.**
YAML lines 48-49 list only JCM 17800. The inspected LPSN page and original
description support KACC 16189; NCBI's native type-material row at
`data/raw/ncbi_type_material.tsv:1454` agrees. YAML line 77 already retains
KACC 16189 in the same strain's culture list, and the existing JCM match
correctly establishes `is_type_strain: true` at line 78.

The omission is already present in `data/raw/lpsn_names.tsv:27608`.
`src/taxonmech/seed.py:405` faithfully projects that raw list. The future
fix belongs in the maintained upstream KG-Microbe LPSN transform supplying
type-deposit edges, consumed by `src/taxonmech/extract.py:461`. The precise
upstream loss stage was not established. Do not hand-patch generated YAML
or raw inventories to conceal it.

## Recommended Edits

1. In a separate authorized curation change, inspect the upstream LPSN source
   and transform for 790670 and preserve KACC 16189 alongside JCM 17800.
   Preserve the true type flag; do not treat GY2 or M9 as culture registries
   or add genome links without new source evidence.
2. After correcting the maintained input/transform, run `just extract-inventory`
   with the configured checkout, dry-run `just seed`, then use
   `just seed-canary NCBITaxon:1028749` to regenerate this record.

## Follow-up Checks

- Compare both type deposits to LPSN and the original description; add a
  focused regression at the maintained extraction boundary.
- Rerun both exact record validators and full raw/native link comparisons;
  the deposit-list fix should not create genome or sample associations.
- Run `just verify-corpus` before merging curation changes; it was skipped here.
- Retry live PubMed, nucleotide, StrainInfo and merged-ID access when available.
  Require own-deposit and sequence-specific evidence before adding SI links.

## Additional Notes

iModulonDB was not applicable: the YAML asserts no named functional gene,
regulator, pathway or transcriptomic relationship. No phenotype was inferred
from source counts or literature titles. No GTDB authority page was needed
to validate an asserted mapping because the record asserts none; native
catalog and raw-inventory absence checks are bounded as stated above.

This review does not certify the full corpus, archive payloads or published
site. No source refresh, catalog rebuild, history event or status promotion
was performed.
