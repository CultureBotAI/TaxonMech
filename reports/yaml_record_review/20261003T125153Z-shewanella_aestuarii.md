# YAML Record Review: Shewanella aestuarii

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/shewanella_aestuarii.yaml`
- Started UTC: 2026-10-03T12:48:30Z
- Finished UTC: 2026-10-03T12:51:53Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:1028752`, Shewanella aestuarii,
rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:22` (Shewanella).
Grounding is `EXACT`; mapping status remains `SEEDED`.

Read the entire 819-line YAML. It contains two GTDB mappings, one BacDive
strain, 17 assembly assertions, 13 other genome assertions, 36 related-record
assertions and six source attestations. Repeated identifiers preserve distinct
source assertions; these counts do not measure distinct biological genomes.

This is a read-only review. Only this report was manually written. No source,
generated taxon, status, history or page was edited.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/shewanella_aestuarii.yaml` | PASS; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/shewanella_aestuarii.yaml` | PASS; one file, zero errors. |
| Complete lineage and BacDive subtree | PASS; all nine ancestor objects, complete strain membership and strain scalar fields agree with raw inventories. |
| Full raw link equality | PASS; all 17 assembly, 13 genome and 36 related-record objects equal the raw link inventories. |
| Native source-field checks | PASS; all 66 assertions checked against native identifiers, taxids, source fields, names, collection matches and applicable project chains. |
| GTDB species census and mapping targets | PASS for counts and predicates; full native membership and all raw mapping targets inspected. The generated explanation has M2. |
| `just verify-corpus` | Not run: full-corpus reproduction check, not a focused record validator. Target comparisons do not substitute for it. |
| `just validate-history` | Not run: ignored-inclusive target search found no standalone history. Strict validation checked the embedded seed event. |
| Graph and generated products | Not run: no graph is asserted; generated pages and other products were outside this review. |

GTDB live pages, StrainInfo and detailed live assembly metadata were
unavailable through the browser tool. Native snapshots support the bounded
checks below. Sequence payloads and full publication bodies were not reviewed.

## Identity and Grounding

The inspected [NCBI Taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028752)
agrees on current name, identifier, species rank, parent, genetic code 11
and lineage. The complete raw subtree has only this taxon. Native name
rows at `data/catalog/ncbi_names-0005.jsonl.gz:28248` onward classify the
authority-bearing name as authority and Shewanella sp. SC18 as includes;
both correctly remain related synonyms.

The [LPSN page](https://lpsn.dsmz.de/species/shewanella-aestuarii)
confirms name 791380, Park and Jeon 2013 authorship and valid correct-name
status. It lists JCM 17801, KACC 16187 and SC 18 as type designations.
The existing JCM match correctly supports the true type flag despite M1.
The medical-use phrase concerns the recommended name, not therapeutic use
or a demonstrated pathogenic phenotype.

This is not Alishewanella aestuarii, `NCBITaxon:453835`; broader text searches
also returned that distinct genus/species and its descendant, which were
excluded from this target's evidence.

Both GTDB predicates are preserved as `skos:broadMatch`. Only the unsuffixed
species is LPSN-linked and becomes an xref; `_A` is neither an xref nor an
exact synonym. NCBI's Alteromonadales lineage is not replaced with GTDB's
Enterobacterales placement. Counts and classifications are source-specific.

## Evidence

**Raw provenance.** Identity traces to `data/raw/ncbitaxon_taxa.tsv:219202`,
nomenclature to `data/raw/lpsn_names.tsv:28233`, and the strain to
`data/raw/bacdive_strains.tsv:56379`. All three culture/alias crosswalk rows
exist. `curation/seed_scope.tsv:10786` and the embedded seed event agree
on six sources; the legacy-page path also resolves in its inventory.

**Literature and collection identity.** The inspected
[original publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.055178-0)
supports the DOI, December 2013 journal metadata, authors and abstract's
type assignment SC18 = KACC 16187 = JCM 17801. The separately inspected
[PubMed record](https://pubmed.ncbi.nlm.nih.gov/23950150/)
confirms PMID 23950150, that DOI and the same article; its earlier August
2013 electronic date does not conflict with the journal date. Initial direct
PubMed retrieval showed a browser check, but the NCBI reference link later
returned usable metadata and abstract without bypassing that check.

The inspected [notification publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.061861-0)
confirms the second DOI, Oren/Garrity authorship, March 2014 publication and
notification for volume 63, part 12. Its abstract was inspected; the full
species table was not. LPSN associates the notification with this name.

The [JCM catalogue](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=17801)
independently connects JCM 17801 to KACC 16187 and Jeon's SC18 and identifies
it as type material. It also lists BacDive 134072, taxid 1028752, the marker
and genome accessions. Co-listing a WGS master and an assembly on this
collection page is not used to infer that they denote the same submission.

**BacDive and marker evidence.** Read the complete native BacDive 134072
object and the relevant sections and references of the
[BacDive page](https://bacdive.dsmz.de/strain/134072).
The source retains KACC 16187, JCM 17801 and SC 18. Its structured designation
field is absent, so omitting `designation` in YAML faithfully follows the
inventory. The encoded SC alias remains preserved, but the whole-culture
matcher correctly rejects SC 18, SC18 and `kgmicrobe.strain:SC%2018` as
collection join keys. JCM 17801 and KACC 16187 are accepted.

The native 16S entries are JF751044 (SC18, 1,509 bases) and MT760375
(JCM 17801, 1,406 bases). The inspected
[NCBI nucleotide page](https://www.ncbi.nlm.nih.gov/nuccore/JF751044)
resolves the nomenclature marker to JF751044.2 with the expected SC18
partial-16S description. The unsuffixed source accession is not rewritten
to a guessed version. Neither marker is promoted to a genome identifier.

BacDive's two genome objects explicitly supply GCA_014647215 / 1028752.7 /
2996171577 and GCA_023283685 / 1028752.9 / 8114308885. All six projected
assertions preserve source reference 66792, descriptions, taxid and `contig`
level. The live reference identifies an automated DiASPora annotation, not
an independently performed assembly or sequence-equivalence experiment.
Unversioned BacDive assembly accessions remain unversioned.

**Complete native link audit.** The following counts include every assertion,
not a sample. Full-object equality against the raw tables was followed by
native field and eligible culture-match checks.

| Source | Assertions checked | Native support |
| --- | ---: | --- |
| BacDive | 6 | Both complete genome objects on 134072; each accession, reference, description, level and taxid. |
| BV-BRC | 12 | Complete native 1028752.7 and 1028752.9 records; strain fields plus the former's separate `culture_collection` field. |
| GOLD | 26 | Go0596559, two projects and two isolate analyses; both organism culture/strain fields and each explicit project chain. |
| GTDB | 10 | RS_GCF_014647215.1 and RS_GCF_023283685.1; JCM 17801, both assembly fields, genome IDs, samples and projects. |
| NCBI Assembly | 12 | Four current GenBank/RefSeq rows; explicit `strain=JCM 17801`, assembly metadata, samples and source-specific projects. |

The two independently supported submission chains are:

| GenBank / RefSeq | BioSample | GenBank project | GOLD project / analysis | IMG | BV-BRC |
| --- | --- | --- | --- | --- | --- |
| GCA_014647215.1 / GCF_014647215.1 | SAMD00245266 | PRJDB10510 | Gp0610512 / Ga0520901 | 2996171577 | 1028752.7 |
| GCA_023283685.1 / GCF_023283685.1 | SAMN24537885 | PRJNA526057 | Gp0786639 / Ga0626576 | 8114308885 | 1028752.9 |

RefSeq and GTDB supply PRJNA224116; GenBank, BV-BRC and GOLD preserve the
submission-specific projects above. That difference is source provenance,
not a reason to replace one project with another. GOLD analyses have empty
direct organism fields but each resolves through exactly one known project
to Go0596559. Their structured `AP GENBANK` values and IMG IDs agree.
Samples, projects and GOLD identifiers remain related records, not genomes.
No universal cross-database sequence identity is inferred.

**GTDB membership and conflict scope.** Complete native catalog checks
establish three unsuffixed-species members and one `_A` member:

- RS_GCF_014647215.1 and RS_GCF_023283685.1: taxid 1028752, JCM 17801.
- GB_GCA_039524135.1: taxid 398053, JCM 17081, NCBI name Mucilaginibacter
  ginsenosidivorans, but GTDB species Shewanella aestuarii.
- RS_GCF_011765625.1: taxid 1028752, PN3F2, GTDB species Shewanella aestuarii_A.

The discordant JCM 17081 row is preserved as source disagreement; it is
not a culture match to JCM 17801 and supplies no strain link here. Likewise
PN3F2 is not the type-strain deposit. Its NCBI assembly, BV-BRC record and
Go0540134/Gp0490977/Ga0439720 chain are present natively but correctly not
attached to BacDive 134072. The taxon-level GOLD count of two includes its
organism; that count does not authorize a strain join.

Raw GTDB species rows 164719-164720 support counts 3 and 1. Complete mapping
rows show the unsuffixed species maps to 1028752 and 398053, whereas `_A`
maps only to 1028752. The primary GTDB attestation correctly counts three,
not four, genomes. M2 concerns only the inaccurate generated explanation.
Live GTDB species and representative-genome pages were unavailable; no
newest-release classification is claimed beyond the inspected snapshot.

**Other counts.** Raw inventories support one NCBI name, one LPSN name,
one BacDive strain, two GOLD organisms and ten Madin trait assertions.
The strain's `medium_count: 1` agrees with its inventory. These units are
not summed, and no specific phenotype or growth recipe is inferred from them.

## Completeness

The full BacDive subtree has one strain and it is included. Complete native
genome catalogs were searched for taxid, normalized species name and both
collection accessions, with ignored/hidden files and compression included.
The type-strain links account for the eligible native matches. The GTDB
species census separately checked all four cluster members, including the
cross-classified row. There is no justified additional type-strain link
from PN3F2 or JCM 17081.

BacDive links SI-ID 133191, but ignored-inclusive decompressed searches of
all local StrainInfo files found no target typed SI-ID, source BacDive ID,
taxid, name/slug or JCM/KACC deposit. Broad numeric hits were unrelated SI-DP
identifiers and were explicitly rejected. The live strain page was unavailable;
a BacDive cross-reference alone does not prove an eligible own deposit or
sequence-specific SI link.

Ignored-inclusive decompressed searches of the ATB overlay and complete
native `data/catalog/allthebacteria.tsv.xz` found neither SAMD00245266 nor
SAMN24537885. No ATB genome can therefore be added through this record's
existing sample evidence in that snapshot. This is not a claim about every
unlabelled or future sample.

Ignored-inclusive identifier/name/slug searches covered raw, curation,
history and prior-report files. No standalone target history or prior report
was found. Optional phenotype, graph and record-level evidence fields may
remain empty for a source-inventory seed.

## Findings

Counts: **0 blocker, 0 major, 2 minor**.

**M1 - Minor: the LPSN type-deposit list omits KACC 16187.**
YAML lines 48-49 list only JCM 17801. The inspected LPSN, original description
and JCM catalogue support KACC 16187; `data/raw/ncbi_type_material.tsv:1466`
agrees. YAML line 88 already retains KACC in the strain culture list, and
line 90 correctly marks it as type material.

The omission already occurs in `data/raw/lpsn_names.tsv:28233`.
`src/taxonmech/seed.py:405` faithfully projects that input. A future fix
belongs to the maintained upstream KG-Microbe LPSN transform supplying
type-deposit edges consumed by `src/taxonmech/extract.py:461`; the exact
upstream loss stage was not established. Do not hand-patch generated YAML
or raw inventories to conceal it.

**M2 - Minor: the pooled-mapping note invents other NCBI targets for `_A`.**
YAML lines 68-69 say this GTDB species also maps to other NCBI taxa. The
complete raw mapping table and native `_A` membership show only 1028752.
The extra 398053 target belongs to the unsuffixed species. The broadMatch
predicate still correctly preserves the source's split/pooling signal;
the nonidentity treatment and counts are not broken.

Owner: `src/taxonmech/seed.py:462`, which unconditionally emits the stronger
claim for nonidentity broadMatch mappings. `tests/test_seed.py:115` checks
only that the note contains `Pooled`, not that its target-cardinality claim
is supported. This is a generated explanatory-text defect, not a request to
alter the source mapping or reconcile NCBI and GTDB taxonomies.

## Recommended Edits

1. In separate authorized curation, inspect the upstream LPSN transform for
   791380 and preserve KACC 16187 alongside JCM 17801. Retain SC 18 as an
   alias, not a newly eligible culture registry.
2. Revise the broadMatch note in `src/taxonmech/seed.py` to state only that
   this additional GTDB species contains genomes classified here by NCBI,
   unless multiple NCBI targets have actually been established. Add a focused
   single-target/multiple-target regression in `tests/test_seed.py`.
3. After the upstream fix, re-extract with `just extract-inventory`; dry-run
   `just seed` and regenerate the target with
   `just seed-canary NCBITaxon:1028752`. Do not manually modify this YAML.

## Follow-up Checks

- Compare both type deposits to the inspected authorities and add a regression
  at the maintained extraction boundary.
- Run focused seeder tests for M2, checking truthful notes while retaining
  mapping predicates, counts, xrefs and nonidentity exclusions.
- Rerun both exact record validators and full raw/native link comparisons;
  these two fixes should not change the 66 supported link assertions.
- Run `just verify-corpus` before merging curation changes; it was skipped here.
- Retry live GTDB, StrainInfo and detailed assembly metadata access. Keep
  genome classification conflicts explicit; do not infer corrected taxonomy
  or missing SI deposit/sequence links from names alone.

## Additional Notes

iModulonDB was not applicable: the YAML asserts no named functional gene,
regulator, pathway or transcriptomic relationship. Literature phenotype
statements and BacDive predictions were not imported into this seed record.

This review does not certify the full corpus, archive sequence payloads or
published site. No source refresh, catalog rebuild, curation-history event,
GitHub mutation or review-status promotion was performed.
