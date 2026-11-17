# YAML Record Review: Agromyces mediolanus JCM 9631

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/agromyces_mediolanus_jcm_9631.yaml`
- Started UTC: 2026-10-03T14:20:32Z
- Finished UTC: 2026-10-03T14:24:21Z
- Verdict: pass

## Target

- Class `TaxonRecord`; identifier `NCBITaxon:1303686`; rank `STRAIN`;
  domain `BACTERIA`; parent `NCBITaxon:41986`, Agromyces mediolanus.
- Read the entire 502-line YAML. Grounding is `EXACT`, mapping status
  `SEEDED`, genetic code 11, and strain count 1.
- The strain is `kgmicrobe.strain:bacdive_166041`, with JCM 9631 and
  LMG 18118 deposits, seven assembly assertions, six other-genome
  assertions, and 23 related-record assertions. These are qualified source
  assertions, not distinct-genome counts.
- Two attestations and one seed event are present; synonyms, GTDB
  mappings, nomenclature, and causal graphs are absent.
- Generated YAML remains unchanged. This review writes only this report,
  apart from the strict validator's standard diagnostic output.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/agromyces_mediolanus_jcm_9631.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/agromyces_mediolanus_jcm_9631.yaml`:
  PASS; one file scanned, zero errors. Standard diagnostic:
  `reports/instance_validation_failures.tsv`.
- Complete structured taxonomy parent-chain, ten ancestor labels/ranks,
  identity, synonym absence, singleton subtree, and source-classified
  strain-count checks: PASS.
- Exact raw/overlay comparisons: six raw plus one StrainInfo assembly
  assertions, six raw genome assertions, and 18 raw plus five StrainInfo
  related assertions reproduce every corresponding YAML field.
- In-memory `straininfo_links.build_links` replay reproduces two
  strain/deposit links, one assembly, and five related assertions, with
  no exclusions. All explicit culture-match fields pass the maintained
  CAFI/full-accession matcher.
- `just verify-corpus`: Not checked; full-corpus-only, not a focused
  validator. Global provenance, pages, and exports were not audited.
- Ignored-inclusive target ID/name/slug searches of `history/` found no
  standalone entry, so standalone history validation had no target. The
  embedded seed event passed strict validation; no history was created.
- Graph/product evidence gates are not applicable to this graph-free
  record. Schema success alone is not biological verification.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308111` supports the exact label, strain rank,
species parent 41986, code 11, and empty synonym fields. The complete
native name entry at `data/catalog/ncbi_names-0007.jsonl.gz:30657`
contains only the scientific name for this taxon. The ten root-first
ancestors agree with the complete pinned parent chain, and the target's
complete subtree is the singleton 1303686.

The NCBI browser was unavailable through the web tool. Approved read-only
[Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303686&retmode=xml)
confirms strain rank, identity, parent, code, and lineage;
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303686)
independently returns `STRAIN` and the same ten lineage IDs. This is not
the parent species record and not a neighboring JCM culture.

[JCM's catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=9631),
retrieved directly after the web tool failed, confirms JCM 9631 = LMG
18118, history through Suzuki CNF183 and Aoki AN-9, BacDive 166041, and
NCBI 1303686. Those laboratory names are source context, not new global
culture-collection join keys or required NCBI synonyms.

[LPSN's species entry](https://lpsn.dsmz.de/species/agromyces-mediolanus)
772992 is validly published and the correct name. Its type deposits
include JCM 3346 and DSM 20152, not either deposit on this record.
`data/raw/lpsn_names.tsv:15132` maps that name to species 41986, not
strain 1303686. Accordingly, no species nomenclature or type flag is
required here. Parent-species synonyms must not become exact strain names.

## Evidence

**BacDive and attestations.** `data/raw/bacdive_strains.tsv:88277`
supports the direct taxon assignment, both deposit identifiers, empty
designation, and medium count 1. The count is MediaDive's strain-linked
inventory count, not a direct taxon-level MEDIADIVE attestation. JCM also
lists one culture medium, 26; the record does not import the recipe or
assert a new growth experiment.

The complete native [BacDive](https://bacdive.dsmz.de/strain/166041)
object at `data/bacdive/records.jsonl.gz:88276` distinguishes strain
1303686 from species 41986, retains both deposits, and explicitly says
`type strain: no`. StrainInfo's two deposit flags are also false. The
web page's generic Type strain heading is not evidence to override these
fields or LPSN's different type deposits.

Native BacDive reference 66792 supplies one contig-level genome object:
GCA_001313565, BV-BRC 1303686.3, and IMG 2734481952. Each reference is
attached to its own assertion. Co-occurrence is not by itself a claim of
cross-database genome equivalence.

`curation/seed_scope.tsv:51421` and the raw NCBI row support precisely
the two record-level attestations: one NCBI NAME and one BacDive STRAIN.
The 2026-09-13T17:54:04Z seed event reproduces that reason. Complete
exact-field scans found no direct target GTDB, LPSN, GOLD, MediaDive,
Madin, or BactoTraits attestation/mapping in their maintained tables.
Native GOLD links below are a separate primary-metadata contribution;
their presence does not manufacture a KGX taxon-attestation count.

**Assembly and genome evidence.** The complete GenBank source object at
`data/catalog/ncbi_genbank-0000.jsonl.gz:49284` identifies
GCA_001313565.1, ASM131356v1, explicit strain JCM 9631, taxon 1303686,
species 41986, BioProject PRJDB944, BioSample SAMD00016953, and WGS
BBGC00000000.1. It is a contig assembly with 1,272 contigs and 1,314,348
bp. There is no paired RefSeq accession in the source object; exclusion
notes state fragmentation and a genome length that is too small.

The inspected [live NCBI assembly report](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_001313565.1/dataset_report)
confirms the current accession, strain, assembly level, project, sample,
WGS accession, absence of a paired accession, and both quality warnings.
Its BioSample attributes explicitly name JCM: 9631. Retaining the
association does not certify completeness, sequence quality, or suitability
for comparative biology.

The full BV-BRC object at `data/bvbrc/bvbrc-0001.jsonl.gz:23814`
supports genome 1303686.3, the same versioned assembly/project/sample,
WGS BBGC00000000, and separate strain and culture-collection fields.
Those two fields legitimately produce distinct evidence assertions.
The unversioned BacDive and StrainInfo accessions remain as supplied;
the importer must not append a version merely because NCBI resolves .1.

**GOLD provenance.** Full native objects establish the explicit chain:

- `data/gold/organisms.jsonl.gz:54713`: Go0093204, JCM 9631 in both
  culture and strain fields, taxon 1303686.
- `data/gold/projects.jsonl.gz:55091`: Gp0093204 explicitly points
  to Go0093204 and supplies PRJDB944 and SAMD00016953.
- `data/gold/analyses.jsonl.gz:74798`: Ga0128436 is an isolate genome
  analysis, explicitly points to Gp0093204, and supplies GCA_001313565.1,
  BBGC00000000, and IMG 2734481952. Its direct organism field is blank,
  not a conflicting organism assignment.
- `data/gold/organisms.jsonl.gz:214128`: Go0276092 explicitly names
  LMG 18118 under species 41986. It supplies two organism-only assertions,
  not a project, an assembly, or permission to copy the JCM analysis.

All 18 raw related assertions retain their sample, project, analysis, or
organism types and remain outside genome counts. Source classification
41986 on an LMG assertion does not overwrite the record's strain taxon.

**StrainInfo and nucleotide evidence.** The complete native object at
`data/straininfo/records.jsonl.gz:10854` is SI-ID 10854, published
online, with source BacDive ID 166041. Both own deposits are available,
nondeprecated, and nonerroneous: LMG 18118 = SI-DP 42471 and JCM 9631 =
SI-DP 42473. [DataCite](https://api.datacite.org/dois/10.60712/si-id10854.2)
confirms DOI 10.60712/SI-ID10854.2 as a findable version-2 strain record,
not a publication or separate deposit DOI.

`data/straininfo/strain_links.tsv:68507` and 68508 preserve these two
matches. `data/straininfo/assemblies.tsv:5926` and the related-record
overlay reproduce the native source without transferring sequence claims
between deposits. The genome GCA_001313565 and 16S sequence LC066589
explicitly name JCM's SI-DP 42473 only. LMG receives its deposit and
source-strain references, but neither sequence. The five related assertions
are two deposit references, two source-strain references, and one nucleotide.

Inspected [NCBI nucleotide EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=LC066589&rettype=gb&retmode=xml)
resolves LC066589.1 as a 1,422-bp partial 16S sequence with strain JCM
9631, culture collection JCM:9631, and species taxon 41986. This supports
the narrower nucleotide claim, not a second genome or a phenotype.

## Completeness

- Full structured scans of the taxonomy and BacDive classifications
  confirm one relevant strain and no omitted descendant strains.
- Ignore-independent exact raw/SI comparisons reproduce every assembly,
  genome, and related-record assertion, including nested SI evidence.
- A complete native StrainInfo own-deposit scan found only SI-ID 10854
  for these two culture keys. Both eligible deposits and both explicit
  source sequence objects are represented at their correct scope.
- Ignored-inclusive, decompression-aware native catalog searches cover
  NCBI names/assemblies, all GTDB shards, BV-BRC, and GOLD. They found
  the explicit source objects documented above. Numerical substring hits
  on unrelated Salmonella sample/accession names were not identity matches.
- A separate ignored-inclusive decompression-aware search of `data/atb/`,
  the full compressed ATB catalog, and `history/` for the exact BioSample,
  target label/slug, and BacDive strain ID returned no matches. The
  absence of an ATB link is therefore supported for the pinned snapshot,
  not a claim that no sequencing reads or future assemblies exist.
- Native BacDive/JCM additionally mention D45053 for laboratory strain
  CNF183. It is not an explicit own-deposit sequence in the pinned SI
  object. No sequence was invented from group membership, and this review
  does not claim to exhaust every public marker accession for the culture.
- The local iModulonDB runner was attempted with
  `uv run --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`.
  Sandbox DNS failed. An approved read-only request to the official
  [datasets API](https://imodulondb.org/api/datasets) returned 20 organism
  entries, none covering Agromyces. Component searches are not applicable;
  absence is not negative biological evidence.
- Optional definition, phenotype evidence, graph, synonyms, nomenclature,
  and type flag need not be filled by borrowing parent-species claims.

## Findings

None found in the target under the documented source-preserving contract.
Finding counts: zero blockers, zero major, zero minor.

The assembly's documented quality warnings are important source context,
not evidence that the strain link is false. No equivalence, complete-genome,
type-strain, or experimentally established phenotype claim is asserted.

## Recommended Edits

None required. Preserve source-qualified versions, both culture identifiers,
the typed related records, and the JCM-specific sequence-deposit evidence.

A future authorized source refresh belongs in the maintained inventories
and `src/taxonmech/seed.py` workflow. Do not hand-edit generated YAML,
copy JCM sequence claims to LMG, or promote the parent species' type data.

## Follow-up Checks

- After a source refresh, check whether a better assembly or an explicit
  LMG-deposit sequence has been added, using whole culture identifiers.
- Recheck exact SI-DP sequence assignment, assembly quality notes, and
  GOLD organism/project/analysis chains before changing the links.
- Rerun both focused validators after any authorized change. Broad
  regeneration requires `just verify-corpus` and documented product gates.

## Additional Notes

The initial broad native search also returned numerical substring matches;
only complete identifiers and inspected source fields informed this verdict.
The SI-ID object was re-read with a terminating numeric boundary. Public
source APIs and JCM were retrieved with approved read-only network access
after sandbox/web-tool limitations. No paid research or GitHub mutation
was performed, and the record remains `SEEDED`.
