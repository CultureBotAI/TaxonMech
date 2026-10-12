# YAML Record Review: Rhodococcus koreensis JCM 10743 = NBRC 100607

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhodococcus_koreensis_jcm_10743_nbrc_100607.yaml`
- Started UTC: 2026-10-03T14:31:36Z
- Finished UTC: 2026-10-03T14:38:49Z
- Verdict: needs curation

## Target

- Class `TaxonRecord`; identifier `NCBITaxon:1303689`; rank `STRAIN`;
  domain `BACTERIA`; species parent `NCBITaxon:99653`.
- Read the entire 1,489-line YAML in four untruncated portions. Grounding
  is `EXACT`, mapping status `SEEDED`, and genetic code 11.
- One BacDive strain, 11027, has eight retained culture identifiers,
  26 assembly assertions, 16 other-genome assertions, and 66 related
  assertions. These are source-qualified assertions, not distinct genomes.
- One GTDB mapping, four exact synonyms, six source attestations, and one
  seed event are present. There is no nomenclature or causal graph.
- Generated YAML remains unchanged. The only manual write is this report;
  strict validation also produced its standard diagnostic TSV.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/rhodococcus_koreensis_jcm_10743_nbrc_100607.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/rhodococcus_koreensis_jcm_10743_nbrc_100607.yaml`:
  PASS; one file scanned, zero errors. Diagnostic:
  `reports/instance_validation_failures.tsv`.
- Structured identity, all ten ancestor labels/ranks and the complete
  parent chain, singleton subtree, NCBI synonym fields, and direct
  BacDive membership checks: PASS.
- Exact multiset comparison reproduces all 21 raw plus five StrainInfo
  assembly assertions, 16 raw other-genome assertions, and 44 raw plus
  22 StrainInfo related assertions, including nested evidence.
- Full own-deposit census and in-memory StrainInfo replay reproduce seven
  strain/deposit links, five assemblies, and 22 related assertions, with
  no exclusions. All actual matched-deposit fields pass the CAFI matcher.
- GTDB cluster census confirms seven members, but species identity is
  incorrectly promoted to strain identity: semantic finding M1 below.
- `just verify-corpus`: Not checked; full-corpus-only. No substitute
  focused reproduction validator was invented. Global provenance,
  downloaded sequence content, generated pages, and exports were not audited.
- Ignored-inclusive ID, label, and slug searches in `history/` found no
  target history entry. Standalone history validation therefore had no
  target; strict validation checked the embedded event.
- Graph/product evidence gates are not applicable to this graph-free
  record. Schema success does not establish biological correctness.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308113` supports the label, strain rank,
species parent, code, and three NCBI exact synonyms. Native scientific,
synonym, and equivalent-name objects are at
`data/catalog/ncbi_names-0007.jsonl.gz:30659` through 30662. All ten
root-first lineage entries match the pinned taxonomy parent chain.
There are no children of 1303689 in that complete backbone.

Inspected [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303689&retmode=xml)
confirms strain identity, parent 99653, code 11, names, and lineage.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303689)
also returns strain rank and all ten ancestor IDs. The NCBI grounding is
sound; the additional GTDB identity assertion is not.

[JCM 10743](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=10743)
supports the DNP505 deposit history and equivalences to CGMCC 4.1724,
CGMCC 4.1822, CIP 106721, DSM 44498, KCTC 0569BP, NBRC 100607,
and NCIMB 13709. Its current taxonomic link is to the parent species,
not a replacement identifier for the retained NCBI strain node.

[LPSN 780454](https://lpsn.dsmz.de/species/rhodococcus-koreensis)
supports the validly published correct species name and type-culture
designations. `data/raw/lpsn_names.tsv:19550` maps that name to species
99653, not strain 1303689. Missing strain-level nomenclature and
`is_type_strain` follow the documented same-record LPSN derivation.
They do not assert that the culture is non-type: BacDive and StrainInfo
explicitly identify type material.

GTDB uses genus `Rhodococcus_F` and family Mycobacteriaceae, while the
NCBI lineage uses Rhodococcus and Nocardiaceae. These are source
classification differences, not permission to rewrite the NCBI lineage.

## Evidence

**Inventory and attestations.** The following source rows reproduce
the stored counts and units:

| Source | Inventory location | Count and scope |
| --- | --- | --- |
| NCBI | `data/raw/ncbitaxon_taxa.tsv:308113` | 1 NAME |
| GTDB | `data/raw/gtdb_species.tsv:154083`; `gtdb_mappings.tsv:17461` | 7 GENOME for the species cluster, not seven genomes of this strain |
| BacDive | `data/raw/bacdive_strains.tsv:10882` | 1 STRAIN |
| MediaDive | `data/raw/mediadive_taxa.tsv:2815` | 2 MEDIUM: 535 and J43 |
| Madin | `data/raw/madin_taxa.tsv:11826` | 4 TRAIT_ASSERTION |
| BactoTraits | `data/raw/bactotraits_taxa.tsv:2280` | 3 TRAIT_ASSERTION |

`curation/seed_scope.tsv:12070` supplies the six-source admission reason;
the 2026-09-13T17:54:04Z seed event agrees and makes no human-review claim.
Complete exact-field scans found no direct target LPSN or GOLD inventory
row. GOLD primary genome associations do not create a KGX taxon-level
GOLD attestation. Counts with different units must not be summed.

**BacDive and culture matching.** The complete native object at
`data/bacdive/records.jsonl.gz:10881` supports BacDive 11027, designation
DNP 505/DNP505, all eight retained identifiers, and the three genome
objects. The inspected [BacDive page](https://bacdive.dsmz.de/strain/11027)
corroborates culture identity and the source taxon IDs.
The raw strain medium count is zero and is omitted; the separate direct
MediaDive count is two. These different inventories are not contradictory.

Seven retained identifiers pass the maintained CAFI matcher. KCTC 0569BP
is retained as `kgmicrobe.strain:KCTC%200569BP` but does not match the
pinned KCTC full-accession template `^\d+$`. This is a matching boundary,
not proof of an invalid culture number. Do not remove its leading zero
or BP suffix to force a join. Bare DNP505 and DNP 505 are designations,
not registered culture-accession join keys.

**Three assembly families.** Complete NCBI native objects establish:

| Deposit | Assembly accession(s) | BioSample | Original BioProject | Pinned assembly context |
| --- | --- | --- | --- | --- |
| JCM 10743 | GCA_001313625.1 | SAMD00016919 | PRJDB947 | 4,096 contigs; 8,291,864 bp; BBGF00000000.1 |
| NBRC 100607 | GCA_001894845.1 / GCF_001894845.1 | SAMD00046766 | PRJDB297 | 227 contigs; 10,106,405 bp; BCWZ00000000.1 |
| DSM 44498 | GCA_900105905.1 / GCF_900105905.1 | SAMN04490239 | PRJEB16386 | 9 contigs; 10,311,574 bp; FNSV00000000.1 |

Native locations, all under `data/catalog/`, are:

- JCM: `ncbi_genbank-0000.jsonl.gz:49287`.
- NBRC: `ncbi_genbank-0001.jsonl.gz:24464` and
  `ncbi_refseq-0001.jsonl.gz:10624`.
- DSM: `ncbi_genbank-0056.jsonl.gz:39288` and
  `ncbi_refseq-0009.jsonl.gz:27032`.

All are source level Contig. Both GenBank/RefSeq pairs are marked
identical. JCM has no RefSeq pair and carries source quality exclusions:
fragmentation, short genome length, and not used as type. The association
is supported but must not be presented as quality certification.

Inspected [live NCBI assembly reports](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_001313625.1,GCA_001894845.1,GCF_001894845.1,GCA_900105905.1,GCF_900105905.1/dataset_report)
resolve all five versioned accessions as current and confirm their
strains, levels, pairs, samples, original projects, and JCM quality notes.
BioSample attributes identify the corresponding JCM, NBRC, or DSM strain.
The pinned RefSeq/GTDB umbrella project PRJNA224116 remains distinct
from the original projects; GOLD's DSM project is PRJNA303863.
Source differences must remain attributed, not silently overwritten.

**BV-BRC, IMG, and GOLD.** Complete BV-BRC objects preserve the following
explicit culture/strain fields and source chains:

- `data/bvbrc/bvbrc-0001.jsonl.gz:23816`: 1303689.3, JCM 10743,
  GCA_001313625.1, SAMD00016919, PRJDB947, and BBGF00000000.
- `data/bvbrc/bvbrc-0001.jsonl.gz:23817`: 1303689.4, NBRC 100607,
  GCF_001894845.1, SAMD00046766, PRJDB297, and BCWZ00000000.
- `data/bvbrc/bvbrc-0028.jsonl.gz:19093`: 99653.4, DSM 44498,
  GCA_900105905.1, SAMN04490239, PRJEB16386, and FNSV00000000.

BacDive reference 66792 supports its JCM genome object and IMG
2734481955; reference 67770 supports NBRC and DSM, with IMG 2634166362
only on the DSM object. An absent NBRC IMG field is not filled by
co-occurrence with another genome object.

Complete GOLD organism/project/analysis objects supply:

- JCM: Go0094245 -> Gp0094245 -> Ga0128439 -> GCA_001313625.1,
  IMG 2734481955. Native organism, project, and analysis rows are
  55136, 55640, and 74801 in `data/gold/{organisms,projects,analyses}.jsonl.gz`.
- DSM: Go0113577 -> Gp0117005 -> Ga0074767 -> GCA_900105905.1,
  IMG 2634166362. Corresponding rows are 63472, 67289, and 47310.
- NBRC: Go0023592 -> Gp0023592, at organism row 19961 and project
  row 19449, supports the project PRJDB297. The native project has no
  BioSample; none is attributed to that GOLD project by borrowing
  the NCBI field. This retained chain has no analysis/assembly assertion.

The two analysis objects are isolate genome analyses, with valid project
links and blank, not conflicting, direct organism fields. JCM and NBRC
organism culture fields qualify; their bare DNP505 strain fields do not.
DSM's culture and strain fields both qualify. Go0606495 at organism
row 437484 names KCTC 0569BP but fails the current CAFI accession boundary.
GOLD Go/Gp/Ga and sample/project IDs remain related records, not genomes.

**StrainInfo.** The complete native object at
`data/straininfo/records.jsonl.gz:38455` is SI-ID 50657, published online,
with source BacDive 11027. It contains nine own deposits; seven match
retained culture keys. All seven are available, nondeprecated, and
nonerroneous:

| Deposit | SI-DP |
| --- | --- |
| CIP 106721 | 154610 |
| JCM 10743 | 154611 |
| DSM 44498 | 169738 |
| NBRC 100607 | 491384 |
| NCIMB 13709 | 565418 |
| CGMCC 4.1724 | 753432 |
| CGMCC 4.1822 | 753561 |

The other two own deposits are AS 4.1724 and AS 4.1822. Their collection
prefix is not rewritten to CGMCC. KCTC and DNP values occur as relation
designations, not additional eligible own deposits. A full native
own-deposit scan found no other SI record matching eligible retained keys.

[DataCite](https://api.datacite.org/dois/10.60712/si-id50657.3)
confirms findable DOI 10.60712/SI-ID50657.3 as version 3 of the source
strain record. It is neither a deposit DOI nor a research publication.
`data/straininfo/strain_links.tsv:2906` through 2912 reproduce all seven
matches; assembly rows 370 through 374 preserve the native unversioned
accessions. Both GCA_001313625 and GCA_001894845 explicitly name both
JCM 154611 and NBRC 491384 in SI sequence objects. GCA_900105905 names
only DSM 169738. The five assertions preserve those source-specific
associations without transferring sequences to the other deposits.

Eight nucleotide assertions retain explicit sequence-deposit evidence:

| Native accession | Deposit | Sequence context | Length, bp |
| --- | --- | --- | --- |
| AB450821 | JCM 10743 | gyrB | 1,209 |
| KF410358 | DSM 44498 | 16S rRNA | 1,473 |
| KF410394 | DSM 44498 | rpsA | 861 |
| KF410430 | DSM 44498 | pnp | 825 |
| KF410466 | DSM 44498 | purF | 675 |
| KF410502 | DSM 44498 | purL | 1,266 |
| KF410538 | DSM 44498 | rpoC | 1,416 |
| KF410574 | DSM 44498 | secY | 663 |

Inspected [NCBI nucleotide EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB450821,KF410358,KF410394,KF410430,KF410466,KF410502,KF410538,KF410574&rettype=gb&retmode=xml)
resolves all eight as version .1, confirming lengths, strain qualifiers,
species taxon 99653, and gene/product annotations. The YAML correctly
retains SI's unversioned IDs. These partial sequences are typed related
records, not assemblies or experimental proof of a phenotype.
The remaining 14 SI related assertions are seven source-strain and seven
deposit references.

**GTDB cluster census.** The GTDB web tree was inaccessible through the
web tool. An ignored-inclusive, decompression-aware census of all 19
native GTDB genome shards found exactly seven complete objects with
terminal species `s__Rhodococcus_F koreensis`:

| Genome | Native strain | NCBI taxon | Catalog shard and row |
| --- | --- | --- | --- |
| RS_GCF_900105905.1 | DSM 44498 | 99653 | `gtdb_genomes-0001.jsonl.gz:33771` |
| RS_GCF_001894845.1 | NBRC 100607 | 1303689 | `gtdb_genomes-0012.jsonl.gz:45747` |
| RS_GCF_042794615.1 | NPDC056520 | 99653 | `gtdb_genomes-0008.jsonl.gz:43392` |
| RS_GCF_042883925.1 | NPDC058172 | 99653 | `gtdb_genomes-0010.jsonl.gz:8625` |
| RS_GCF_017068375.1 | R85 | 99653 | `gtdb_genomes-0013.jsonl.gz:11983` |
| RS_GCF_002300155.1 | ACS1 | 2028570 | `gtdb_genomes-0013.jsonl.gz:41104` |
| RS_GCF_029269925.1 | T2V | 3034164 | `gtdb_genomes-0012.jsonl.gz:15555` |

All paths are under `data/catalog/`. DSM is the sole representative.
The DSM and NBRC objects support their culture-matched genome links.
R85 has German rhizosphere context, ACS1 UK soil, and T2V Thai soil;
these objects provide no evidence that those isolates or the NPDC
isolates are deposits of JCM 10743. The same cluster has raw closeMatch
rows to 2028570, 3034164, and 99653 at mapping rows 141516, 249096,
and 322105. A source mapping does not establish strain equivalence.

## Completeness

- Complete taxonomy and BacDive scans establish one directly classified
  strain and no omitted descendants. All raw and SI link assertions
  reproduce exactly; nothing was inferred from accession resemblance.
- Ignored-inclusive native searches covered NCBI/GTDB catalog shards,
  BV-BRC, GOLD, BacDive, and StrainInfo, including unsupported KCTC
  syntax and both CGMCC accessions.
- Ignored-inclusive, decompression-aware searches across `data/atb/`
  and the complete `data/catalog/allthebacteria.tsv.xz` found no rows
  for SAMD00016919, SAMD00046766, SAMN04490239, the local strain ID,
  target taxon ID, label, or slug. No ATB link or download URL is
  fabricated. This is pinned-snapshot coverage, not absence of public reads.
- The structured iModulonDB datasets command was attempted first through
  the local `culturebotai-claw` runner and failed with sandbox DNS error.
  A read-only fallback to the official
  [datasets API](https://imodulondb.org/api/datasets) returned 20 organism
  entries and no Rhodococcus organism. Component search is not applicable;
  no gene/module evidence was borrowed from another organism.
- BacDive and JCM expose additional marker accessions outside this SI
  snapshot. Their presence is not permission to attach them to all
  related deposits. This review does not claim exhaustive literature
  or marker coverage.
- Optional definition, phenotype evidence, and causal graph are correctly
  empty. The absent derived type flag is not a negative biological claim.
- No missing source field compensates for M1: the strain and species
  scopes are explicitly distinguishable in the inspected records.

## Findings

**M1 - Major: a species cluster is promoted to exact strain identity.**

The target YAML's mapping at line 39 names a seven-member GTDB species
cluster. Lines 46-49 promote its label to `EXACT_SYNONYM`, and line 60
adds its ID as an identity xref. The seven-member census includes
several distinct strain designations and four NCBI taxon IDs. NCBI
1303689 is specifically a strain under species 99653. Therefore neither
the entire cluster nor its species name is an exact synonym of this
strain. The seven-genome attestation must also remain explicitly scoped
to the source cluster, not interpreted as seven genomes of this strain.

The rendered synonym additionally changes native `Rhodococcus_F koreensis`
to `Rhodococcus F koreensis`, losing the GTDB genus-suffix delimiter.
This is part of the same faulty identity-promotion path, not counted as
a second finding. Merely fixing the spelling would leave the scope error.

Maintained owner: `src/taxonmech/seed.py:451` treats any closeMatch as
identity, without checking rank or source scope; lines 467-468 create
the xref and exact synonym using blanket underscore replacement.
Regression coverage belongs in `tests/test_seed.py`. The upstream
GTDB mapping transform configured by `conf/sources.yaml:24` owns any
change to the raw mapping predicate or source label. Do not hand-edit
`data/raw/`, this YAML, or rendered pages, and do not invent a replacement
SKOS direction without checking the upstream edge convention.

Finding counts: zero blockers, one major, zero minor.
The strain's NCBI identity and qualified genome/sequence links remain
supported; this finding does not invalidate those narrower associations.

## Recommended Edits

1. In a separately authorized curation change, make GTDB identity
   promotion in `src/taxonmech/seed.py` sensitive to rank and demonstrated
   scope. Stop emitting this species-level exact synonym and identity
   xref on the strain record. Preserve provenance for the original mapping
   and clarify the species-cluster scope of its seven-genome count.
2. Add a `tests/test_seed.py` regression with a strain under a species
   and a GTDB cluster containing other strains/taxon IDs. Retain valid
   culture-qualified DSM and NBRC genome links and valid species mappings.
   Preserve GTDB suffix syntax wherever a supported label is rendered.
3. Review the upstream kg-microbe GTDB mapping transform before changing
   closeMatch semantics. If the transform is corrected, re-extract through
   `scripts/extract_source_inventory.py`; do not patch generated TSV rows.
4. After tests pass and curation is authorized, regenerate the target
   through `scripts/seed_from_sources.py` using its documented target
   selection, then carry out the required corpus and publication checks.
   No such changes were made by this review.

## Follow-up Checks

- Run `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run pytest tests/test_seed.py`
  after adding the rank/scope regression; verify valid species mappings
  still work and the native suffix survives supported label rendering.
- Rerun both focused validation commands above after authorized generation.
- Recheck all seven cluster members, absence of species exact-identity
  promotion on strain 1303689, and explicit scope of the GTDB count.
- Repeat raw/SI multiset comparisons and in-memory SI replay to ensure
  all 26 assembly, 16 other-genome, and 66 related assertions survive.
- Run `just verify-corpus` and the documented publication/quality gates
  after a maintained-input fix. They were not run in this read-only review.

## Additional Notes

- The other session was reported closed. This checkout has one worktree
  on `codex/record-review-extensimonas-20261003`; tracked files were clean.
  Existing untracked reports were preserved. No branch/worktree mutation,
  curation event, review-status promotion, or GitHub action was performed.
- Before this report, direct filesystem/index comparison including ignored
  files found 21,558 unique matching reports for 625,960 indexed records;
  all 6,243 Eukaryota records were covered. Filename coverage measures
  report presence, not a passing verdict or a new audit of older reports.
- One ad hoc inventory scan stopped at an incorrect local GOLD filename
  after completing the assertion, SI, taxonomy, LPSN, and GTDB checks.
  The remaining exact-field scans were rerun against the actual
  `data/raw/gold_organisms.tsv` and trait/media inventories successfully.
- Live taxonomy, assembly, nucleotide, DOI, and iModulonDB APIs were
  inspected through read-only public requests. No provider credits,
  sequence downloads, credentials, or source-snapshot writes were used.
