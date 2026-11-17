# YAML Record Review: Rhodococcus pyridinivorans JCM 10940 = NBRC 100608

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rhodococcus_pyridinivorans_jcm_10940_nbrc_100608.yaml`
- Started UTC: 2026-10-03T14:41:27Z
- Finished UTC: 2026-10-03T14:44:37Z
- Verdict: needs curation

## Target

- Class `TaxonRecord`; identifier `NCBITaxon:1303690`; rank `STRAIN`;
  domain `BACTERIA`; species parent `NCBITaxon:103816`.
- Read all 1,954 YAML lines in five untruncated portions. Grounding is
  `EXACT`, mapping status `SEEDED`, and genetic code 11.
- One BacDive strain, 11029, has nine retained identifiers, 36 assembly
  assertions, 23 other-genome assertions, and 92 related assertions.
  These are source-qualified assertions, not distinct genome counts.
- One GTDB mapping, four exact synonyms, six source attestations, and
  one seed event are present. There is no nomenclature or causal graph.
- Generated YAML remains unchanged. The sole manual write is this report;
  strict validation also wrote its standard diagnostic TSV.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/rhodococcus_pyridinivorans_jcm_10940_nbrc_100608.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/rhodococcus_pyridinivorans_jcm_10940_nbrc_100608.yaml`:
  PASS; one file scanned, zero errors. Diagnostic:
  `reports/instance_validation_failures.tsv`.
- Structured identity, all ten ancestor labels/ranks and parent-chain
  entries, singleton subtree, NCBI synonyms, and directly classified
  BacDive membership: PASS.
- Exact multiset comparison reproduces all 30 raw plus six StrainInfo
  assembly assertions, 23 raw other-genome assertions, and 70 raw plus
  22 StrainInfo related assertions, including nested evidence.
- Full own-deposit scan and in-memory StrainInfo replay reproduce six
  strain/deposit links, six assemblies, and 22 related assertions, with
  no exclusions. Every actual matched-deposit field passes the CAFI matcher.
- Native GTDB census confirms 46 cluster members. Their species scope
  does not establish exact strain identity: finding M1 below.
- `just verify-corpus`: Not checked; full-corpus-only. No focused substitute
  was invented. Global provenance, downloaded sequences, generated pages,
  and exports were not audited.
- Ignored-inclusive ID, label, and slug searches of `history/` found no
  target entry. Standalone history validation had no target; strict
  validation checked the embedded event. No history/status change was made.
- Graph/product evidence gates are not applicable to this graph-free
  record. Validator success was not treated as semantic evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308114` supports the exact label, strain
rank, species parent, code, and three NCBI synonyms. The complete native
name objects at `data/catalog/ncbi_names-0007.jsonl.gz:30663` through
30666 preserve scientific, synonym, and equivalent-name classes.
All ten root-first lineage entries match the pinned parent chain, and
the complete backbone contains no descendants of strain 1303690.

Inspected [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303690&retmode=xml)
confirms label, strain rank, parent 103816, code 11, synonyms, and lineage.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303690)
independently supplies strain rank and the ten ancestor IDs. The NCBI
grounding is supported; the extra species-level exact synonym is not.

[JCM 10940](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=10940)
supports the PDB9 deposit history and BCRC 16332, CGMCC 4.1825,
CIP 107477, DSM 44555, KCCM 80005, KCTC 0647BP, and NBRC 100608
equivalences. Its current taxonomic link is to species 103816. That does
not authorize replacing the separately retained NCBI strain identifier.

[LPSN 780467](https://lpsn.dsmz.de/species/rhodococcus-pyridinivorans)
supports the validly published correct species name and type material.
`data/raw/lpsn_names.tsv:19561` maps that name and its GTDB link to the
parent species, not to strain 1303690. The species-level heterotypic
synonym Rhodococcus biphenylivorans is not an exact synonym of this
particular strain and must not be copied into its synonym list.

Absent strain-level nomenclature and `is_type_strain` follow the documented
same-record LPSN derivation. Their absence does not mean non-type:
BacDive and StrainInfo explicitly identify type material. GTDB's family
Mycobacteriaceae and NCBI's Nocardiaceae are different source placements;
preserve NCBI lineage rather than reconciling it locally.

## Evidence

**Source inventories and history.** Exact-field scans reproduce:

| Source | Inventory location | Count and unit |
| --- | --- | --- |
| NCBI | `data/raw/ncbitaxon_taxa.tsv:308114` | 1 NAME |
| GTDB | `data/raw/gtdb_species.tsv:154141`; `gtdb_mappings.tsv:17462` | 46 GENOME for the species cluster |
| BacDive | `data/raw/bacdive_strains.tsv:10884` | 1 STRAIN |
| MediaDive | `data/raw/mediadive_taxa.tsv:2816` | 2 MEDIUM: 535 and J43 |
| Madin | `data/raw/madin_taxa.tsv:11827` | 6 TRAIT_ASSERTION |
| BactoTraits | `data/raw/bactotraits_taxa.tsv:2281` | 1 TRAIT_ASSERTION |

`curation/seed_scope.tsv:12071` supplies the six-source admission reason,
which the 2026-09-13T17:54:04Z seed event preserves. There is no claim of
human review. Complete exact-field scans found no direct target LPSN or
GOLD taxon-inventory row. Primary GOLD genome links do not manufacture
a KGX taxon-level GOLD count. These differently scoped units cannot be
summed, and 46 is not a count of this strain's genomes.

**BacDive and culture keys.** The full native object at
`data/bacdive/records.jsonl.gz:10883` and inspected
[BacDive page](https://bacdive.dsmz.de/strain/11029) support the culture
identity, retained identifiers, and strain/species taxon associations.
The raw designation is empty and medium count zero; omitting those
fields is consistent with the inventory. The separate direct MediaDive
count is not the BacDive strain medium count.

Seven identifiers pass the pinned CAFI matcher. KCTC 0647BP fails the
KCTC template `^\d+$`; PDB is not in the pinned authority patterns.
Both values remain retained in encoded CURIEs but do not supply genome
joins. Neither trimming the KCTC suffix/leading zero nor treating the
PDB9 laboratory designation as a culture accession is justified.
This matcher boundary does not invalidate JCM's culture equivalence.

**Four distinct assembly families.** Complete native NCBI objects support:

| Deposit/family | Assembly accession(s) | BioSample | Original BioProject | Source assembly context |
| --- | --- | --- | --- | --- |
| JCM 10940 | GCA_001313645.1 | SAMD00016920 | PRJDB948 | Contig; 2,305 contigs; 3,651,627 bp; BBGG00000000.1 |
| DSM 44555, Northumbria | GCA_001646805.1 / GCF_001646805.1 | SAMN04357314 | PRJNA306614 | Scaffold; 155 contigs, 154 scaffolds; 5,181,477 bp; LRRI00000000.1 |
| NBRC 100608 | GCA_001894905.1 / GCF_001894905.1 | SAMD00046767 | PRJDB301 | Contig; 41 contigs; 5,205,912 bp; BCXC00000000.1 |
| DSM 44555, JGI | GCA_900105195.1 / GCF_900105195.1 | SAMN04490240 | PRJEB16436 | Contig; 3 contigs; 5,262,484 bp; FNRX00000000.1 |

Native locations, all under `data/catalog/`, are:

- JCM: `ncbi_genbank-0000.jsonl.gz:49288`.
- Northumbria DSM: `ncbi_genbank-0001.jsonl.gz:13853` and
  `ncbi_refseq-0001.jsonl.gz:3449`.
- NBRC: `ncbi_genbank-0001.jsonl.gz:24467` and
  `ncbi_refseq-0001.jsonl.gz:10627`.
- JGI DSM: `ncbi_genbank-0056.jsonl.gz:39217` and
  `ncbi_refseq-0009.jsonl.gz:26963`.

All three GenBank/RefSeq pairs are marked identical. The JCM assembly
has no RefSeq pair and source exclusions for fragmentation, short genome
length, many frameshifted proteins, and not being used as type. A supported
association does not certify its sequence quality. The Northumbria total
includes 36 gap bases; its ungapped length is 5,181,441 bp. Shared DSM
identity does not merge its two assemblies, samples, or project chains.

Inspected [live NCBI assembly reports](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_001313645.1,GCA_001646805.1,GCF_001646805.1,GCA_001894905.1,GCF_001894905.1,GCA_900105195.1,GCF_900105195.1/dataset_report)
resolve all seven versioned accessions as current and confirm their
strains, pairs, levels, BioSamples, original projects, and JCM quality
notes. Sample attributes independently name the corresponding deposits.
Pinned RefSeq/GTDB entries use umbrella project PRJNA224116, while GOLD
uses PRJNA303862 for its JGI DSM project. Keep these source-specific
fields; do not silently replace them with live API values.

**Other genome sources.** Full BV-BRC objects preserve explicit strain
and culture fields:

| Native location under `data/bvbrc/` | BV-BRC ID | Assembly field | Sample/project |
| --- | --- | --- | --- |
| `bvbrc-0001.jsonl.gz:23818` | 1303690.3 | GCA_001313645.1 | SAMD00016920 / PRJDB948 |
| `bvbrc-0000.jsonl.gz:3658` | 103816.9 | GCF_001646805.1 | SAMN04357314 / PRJNA306614 |
| `bvbrc-0001.jsonl.gz:23819` | 1303690.4 | GCF_001894905.1 | SAMD00046767 / PRJDB301 |
| `bvbrc-0000.jsonl.gz:3613` | 103816.10 | GCA_900105195.1 | SAMN04490240 / PRJEB16436 |

BacDive's four genome objects agree. Reference 66792 supports JCM and
IMG 2734481956. Reference 67770 supports the other three, with IMG
2744054615 on Northumbria DSM and IMG 2630969012 on JGI DSM. The NBRC
object has no IMG accession; none is borrowed from another object.

Three complete GTDB native objects support the explicit DSM/NBRC
culture-qualified genome associations: `gtdb_genomes-0007.jsonl.gz:42910`
for RS_GCF_001646805.1, `gtdb_genomes-0006.jsonl.gz:13732` for
RS_GCF_001894905.1, and `gtdb_genomes-0007.jsonl.gz:11823` for
RS_GCF_900105195.1, all under `data/catalog/`. The last is the cluster
representative. Their existence does not turn the entire species cluster
into a synonym of this strain.

**GOLD evidence chains.** Full native objects establish:

| Organism -> project -> analysis | Genome endpoint | Native organism/project/analysis rows |
| --- | --- | --- |
| Go0093754 -> Gp0093754 -> Ga0128440 | GCA_001313645.1; IMG 2734481956 | 54936 / 55415 / 74802 |
| Go0113579 -> Gp0150349 -> Ga0132899 | GCA_001646805.1; IMG 2744054615 | 63474 / 95397 / 78912 |
| Go0113579 -> Gp0117007 -> Ga0074769 | GCA_900105195.1; IMG 2630969012 | 63474 / 67291 / 47312 |
| Go0023802 -> Gp0023802 | Related organism/project only; PRJDB301 | 20165 / 19652 / not present in this chain |

The row columns refer to `data/gold/organisms.jsonl.gz`,
`projects.jsonl.gz`, and `analyses.jsonl.gz`, respectively. Each analysis
is an isolate analysis linked to the specified project; direct analysis
organism fields are blank rather than conflicting. The NBRC project has
an empty BioSample field, correctly not filled from NCBI evidence.
JCM/NBRC organism culture fields qualify, but their PDB9 strain fields
do not. Both DSM culture and strain fields qualify.

Organism-only references Go0271502, Go0271504, Go0271505, and Go0271506
at organism rows 209544, 209546, 209547, and 209548 explicitly name
BCRC 16332, CGMCC 4.1825, CIP 107477, and KCCM 80005. They do not
fabricate additional genomes. Go0608874 at row 439841 names KCTC
0647BP and remains outside the current CAFI matching boundary.
GOLD Go/Gp/Ga, projects, and samples remain typed related records.

**StrainInfo.** The full source object at
`data/straininfo/records.jsonl.gz:38477` is SI-ID 50680, published online,
with source BacDive 11029. Six of its seven own deposits match retained
culture keys. All six are available, nondeprecated, and nonerroneous:

| Deposit | SI-DP | Native NCBI taxon |
| --- | --- | --- |
| DSM 44555 | 169811 | 103816 |
| JCM 10940 | 336816 | 103816 |
| NBRC 100608 | 491385 | 103816 |
| CIP 107477 | 491386 | 103816 |
| BCRC 16332 | 512272 | absent |
| CGMCC 4.1825 | 753564 | 103816 |

The BCRC deposit has no native taxon object, and the YAML correctly
does not borrow a taxon from its source-strain grouping. The other own
deposit is CCRC 16332, SI-DP 512273; it is not rewritten to BCRC.
KCCM, KCTC, and PDB9 occur only as relation designations in this object.
The full native own-deposit scan found only SI-ID 50680 for eligible keys.

[DataCite](https://api.datacite.org/dois/10.60712/si-id50680.3)
confirms findable version-3 DOI 10.60712/SI-ID50680.3 for this source
strain record. It is not a deposit ID or a research publication.
`data/straininfo/strain_links.tsv:2918` through 2923 reproduce the six
deposit links. Assembly rows 375 through 380 preserve unversioned
source IDs: GCA_001313645 and GCA_001894905 each explicitly name both
JCM 336816 and NBRC 491385, while GCA_001646805 and GCA_900105195
name only DSM 169811. No sequence is transferred to the other deposits.

Ten nucleotide assertions preserve explicit sequence-deposit evidence:

| Source accession | Deposit | Sequence context | Length, bp |
| --- | --- | --- | --- |
| AB088665 | JCM 10940 | gyrB | 1,263 |
| KF410365 | DSM 44555 | 16S rRNA | 1,363 |
| KF410401 | DSM 44555 | rpsA | 870 |
| KF410437 | DSM 44555 | pnp | 861 |
| KF410473 | DSM 44555 | purF | 660 |
| KF410509 | DSM 44555 | purL | 1,275 |
| KF410545 | DSM 44555 | rpoC | 1,422 |
| KF410581 | DSM 44555 | secY | 669 |
| MH298656 | DSM 44555 | 16S rRNA | 680 |
| OR398607 | DSM 44555 | 16S rRNA | 1,463 |

Inspected [NCBI nucleotide EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB088665,KF410365,KF410401,KF410437,KF410473,KF410509,KF410545,KF410581,MH298656,OR398607&rettype=gb&retmode=xml)
resolves all ten as version .1 and confirms lengths, species taxon
103816, and the corresponding strain/gene annotations. AB088665 has
strain `JCM 10940T` and explicit xref `JCM:10940`; the two recent rRNA
records retain `DSM 44555(T)` qualifiers. SI's explicit sequence-to-SI-DP
evidence supplies the joins; this is not permission to strip type suffixes
in general culture matching. The YAML correctly keeps source-unversioned
IDs and typed nucleotide records, not assemblies or phenotype evidence.
The remaining 12 SI related assertions are six strain and six deposit IDs.

**GTDB species census and counterexamples.** The web tree was inaccessible.
An ignored-inclusive decompression-aware search of all 19 native GTDB
shards, followed by exact parsing of the terminal `gtdb_taxonomy` value,
found 46 distinct accessions in `s__Rhodococcus pyridinivorans`. They span
16 NCBI taxon IDs: 31 objects at species 103816 and one at each of 15
other IDs, including target 1303690. Full inspected counterexamples are:

- `data/catalog/gtdb_genomes-0011.jsonl.gz:29073`:
  RS_GCF_000511305.1, strain SB3094, NCBI 1435356,
  SAMN02641478; source Complete Genome, three molecules, 5,590,512 bp.
- `data/catalog/gtdb_genomes-0016.jsonl.gz:45069`:
  RS_GCF_000236965.1, strain AK37, NCBI 1114960,
  SAMN02469321; GenBank GCA_000236965.2, 98 contigs, 5,244,611 bp.
- `data/catalog/gtdb_genomes-0004.jsonl.gz:23471`:
  RS_GCF_044462715.1, mag.19i, SAMN43959921; the native object
  identifies a metagenome-derived genome, not this culture deposit.

None supplies an eligible retained culture identifier for JCM 10940.
The raw cluster has mappings to 16 NCBI targets, including closeMatch
to AK37 and SB3094 at `data/raw/gtdb_mappings.tsv:3950` and 28966,
and broadMatch to parent species 103816 at row 1503. The parent LPSN
row links the GTDB species to the species name, not to this strain.

The initial text search also returned five objects whose NCBI taxonomy
contains this species but whose GTDB terminal species is
`s__Rhodococcus sp001017865`. Exact-field filtering excluded those;
the reviewed GTDB count is 46, not the broader text-hit count of 51.

## Completeness

- Complete taxonomy and BacDive scans establish one directly classified
  strain and no omitted descendants. All raw and SI assertions reproduce
  exactly, with source versions, fields, and nested evidence preserved.
- Ignored-inclusive native searches covered NCBI catalog shards, BV-BRC,
  GOLD, BacDive, and StrainInfo using all retained eligible culture keys
  plus the unsupported KCTC value. The GTDB census covered every shard
  and used exact source taxonomy, not NCBI-label similarity.
- Ignored-inclusive, decompression-aware searches of `data/atb/` and
  the complete `data/catalog/allthebacteria.tsv.xz` found no rows for
  SAMD00016920, SAMD00046767, SAMN04357314, SAMN04490240, target
  taxon/local strain IDs, label, or slug. No ATB assembly or URL is
  fabricated. This is a pinned-snapshot result, not absence of public reads.
- The local `culturebotai-claw` structured iModulonDB datasets command
  was attempted first and failed with sandbox DNS error. Read-only
  fallback to the official [datasets API](https://imodulondb.org/api/datasets)
  returned 20 organisms and no Rhodococcus entry. Component search is
  not applicable; absence is not negative gene or phenotype evidence.
- BacDive and JCM contain additional marker context outside the SI
  snapshot. No marker is copied onto every related deposit. This review
  does not claim exhaustive sequence or literature coverage.
- Optional definition, phenotype evidence, causal graph, and derived
  type flag remain unfilled within the documented source contract.
  The BCRC SI taxon omission correctly preserves source uncertainty.

## Findings

**M1 - Major: a species cluster is promoted to exact strain identity.**

The YAML mapping at line 39 names a 46-genome GTDB species. Lines
46-49 emit that species name as an `EXACT_SYNONYM`, and line 60 emits
its identity xref on strain 1303690. The native cluster includes SB3094,
AK37, and other genomes not supported as deposits of JCM 10940.
NCBI explicitly distinguishes this strain from parent species 103816.
Neither the source closeMatch nor the parent species' LPSN mapping
establishes exact strain equivalence. The 46-genome attestation must
remain scoped to the source species cluster, not this strain's genomes.

Maintained owner: `src/taxonmech/seed.py:451` treats closeMatch as
identity without checking rank or demonstrated biological scope;
lines 467-468 emit the xref and exact synonym. Add regression coverage
in `tests/test_seed.py`. The kg-microbe GTDB transform configured by
`conf/sources.yaml:24` owns any change to the raw predicate. Do not
hand-edit generated inventories, this YAML, or pages, and do not invent
a replacement SKOS direction without verifying the upstream convention.

Finding counts: zero blockers, one major, zero minor.
The NCBI grounding and narrower culture-qualified genome/sequence links
remain supported. This finding does not justify deleting those links.

## Recommended Edits

1. In a separately authorized curation change, make GTDB identity
   promotion in `src/taxonmech/seed.py` rank- and scope-aware. Stop
   generating the species exact synonym and identity xref on this strain;
   retain original mapping provenance and explicitly scope its count.
2. Add a `tests/test_seed.py` regression with a strain under a species
   whose GTDB cluster includes other strains/taxon IDs. Preserve valid
   species identity and the three culture-qualified GTDB genome links.
3. Review the maintained upstream GTDB mapping transform before changing
   the source predicate. Re-extract with `scripts/extract_source_inventory.py`
   if an upstream fix is authorized; never patch raw TSV rows by hand.
4. After tests pass, regenerate through `scripts/seed_from_sources.py`
   with documented target selection and complete the required corpus and
   publication gates. This read-only review performs none of those writes.

## Follow-up Checks

- After adding the regression, run
  `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run pytest tests/test_seed.py`.
- Rerun both focused validation commands after authorized regeneration.
- Recheck exact GTDB cluster membership and species/strain boundaries;
  ensure the parent LPSN mapping is not inherited as strain equivalence.
- Repeat raw/SI multiset comparisons and in-memory SI replay. Preserve
  all 36 assembly, 23 other-genome, and 92 related assertions, the two
  distinct DSM sample chains, and the unfilled BCRC SI taxon field.
- Run `just verify-corpus` and documented publication/quality gates after
  a maintained-input fix. They were not run in this read-only review.

## Additional Notes

- Direct filesystem inspection including ignored files confirmed there
  was no prior report for this stem. The other session is closed; this
  checkout remains on `codex/record-review-extensimonas-20261003`.
  Existing reports and tracked files were left unchanged.
- Public taxonomy, assembly, nucleotide, DOI, and iModulonDB APIs were
  inspected with read-only requests. No paid research, source refresh,
  sequence download, credential access, or GitHub mutation was used.
- This verdict concerns one individually read record. It neither counts
  all cluster members as reviewed nor establishes quality of prior reports.
