# YAML Record Review: Streptomyces lavendulae subsp. lavendulae JCM 4055

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_lavendulae_subsp_lavendulae_jcm_4055.yaml`
- Started UTC: 2026-10-03T14:47:17Z
- Finished UTC: 2026-10-03T14:53:55Z
- Verdict: pass

## Target

- Class `TaxonRecord`; identifier `NCBITaxon:1303691`; rank `STRAIN`;
  domain `BACTERIA`; parent subspecies `NCBITaxon:58340`.
- Read all 2,833 YAML lines in eight untruncated portions before judging
  the record. Grounding is `EXACT`, mapping status `SEEDED`, genetic code 11.
- One BacDive strain, 15344, retains 43 culture identifiers, 15 assembly
  assertions, 12 other-genome assertions, and 166 related assertions.
  Assertion counts are not counts of distinct genomes or organisms.
- Four source attestations and one embedded seed event are present.
  There is no taxon-level GTDB mapping, synonym list, nomenclature block,
  or causal graph. The strain is directly filed under this taxon.
- Generated YAML remains unchanged. The only manual write is this report;
  strict validation also produced its standard diagnostic TSV.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_lavendulae_subsp_lavendulae_jcm_4055.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptomyces_lavendulae_subsp_lavendulae_jcm_4055.yaml`:
  PASS; one file scanned, zero errors. Standard diagnostic:
  `reports/instance_validation_failures.tsv`.
- Structured checks reproduce identity, parent, code, all 11 root-first
  lineage entries, the singleton subtree, and directly filed BacDive membership.
- Exact multiset comparisons reproduce 13 raw plus two StrainInfo assembly
  assertions, 12 raw other-genome assertions, and 95 raw plus 71 StrainInfo
  related assertions, including nested StrainInfo evidence.
- A complete own-deposit scan and in-memory StrainInfo replay reproduce
  31 deposit links, two assemblies, and 71 related assertions with no
  exclusions. All actual matched-deposit fields pass the culture matcher.
- Structured native GOLD checks recover 38 organisms, three projects,
  and two analyses; all 91 GOLD assertions have matching native IDs,
  source strain fields, and source taxon IDs.
- `just verify-corpus`: Not checked; full-corpus-only. No focused substitute
  was invented. Global provenance, rendered pages, exports, and downloaded
  genome sequences were not audited.
- Ignored-inclusive ID, label, and slug searches of `history/` found no
  target entry. Standalone history validation therefore had no target;
  strict validation checked the embedded event.
- Graph/product evidence gates are not applicable to this graph-free
  record. Schema success alone was not treated as semantic evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308115` supports the exact scientific name,
strain rank, subspecies parent, code 11, and empty synonym fields.
The native scientific-name object is at
`data/catalog/ncbi_names-0007.jsonl.gz:30667`. The pinned backbone has no
descendants of 1303691; the root-first chain exactly matches the YAML.

Inspected [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303691&retmode=xml)
confirms the name, strain rank, parent 58340, code, and lineage.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303691)
also supplies strain rank and all 11 ancestor IDs, including root.

[JCM 4055](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=4055)
supports the culture history through KCC S-0055, IAM 0009, ATCC 8664,
and IMRU 3440-8, as well as the retained NRRL B-2774 equivalence.
Its current NCBI link is species 1914; this does not replace the separately
retained strain taxon. Culture equivalence is not sequence identity.

[LPSN 781798](https://lpsn.dsmz.de/subspecies/streptomyces-lavendulae-lavendulae)
supports the validly published correct subspecies name and type cultures.
`data/raw/lpsn_names.tsv:20451` contains that subspecies name but no NCBI
mapping. The species row at line 20449 maps to 1914, not to this strain.
Absent strain-level nomenclature and `is_type_strain` follow the documented
same-taxon LPSN derivation; they do not assert that JCM 4055 is non-type.
No broader species synonym or GTDB exact mapping has been promoted here.

NCBI uses Kitasatosporales while the retained GTDB genome metadata uses
Streptomycetales. These source placements remain distinct; the record's
lineage correctly follows NCBI.

## Evidence

**Source inventories.** Exact-field scans reproduce the following counts:

| Source | Inventory location | Count and unit |
| --- | --- | --- |
| NCBI | `data/raw/ncbitaxon_taxa.tsv:308115` | 1 NAME |
| BacDive | `data/raw/bacdive_strains.tsv:15169` | 1 STRAIN |
| MediaDive | `data/raw/mediadive_taxa.tsv:2817` | 5 MEDIUM: 252, 65, 84, 993, J42 |
| GOLD | `data/raw/gold_organisms.tsv:7429` | 1 ORGANISM |

`curation/seed_scope.tsv:22456` supplies the four-source admission reason.
The embedded 2026-09-13T17:54:04Z seed event preserves those sources and
does not claim human review. The direct GOLD attestation is not a count
of the 38 culture-linked primary GOLD organism objects. Units cannot be summed.

**BacDive and matching boundaries.** The complete native object at
`data/bacdive/records.jsonl.gz:15168` supports all 43 retained culture IDs,
the three genome objects, and their source references. The inspected
[BacDive page](https://bacdive.dsmz.de/strain/15344) corroborates the identity
and associated strain/species/subspecies taxon IDs; its current isotype
status and expanded culture listing are not silently retrofitted into the
pinned snapshot. Empty raw designation, medium count zero, and empty LPSN
links explain the omitted corresponding strain fields. The direct MediaDive
count is a different source measure.

Forty retained IDs pass the pinned culture matcher. IFM 1031 and ISP 5069/5213
remain faithfully retained as encoded CURIEs but do not pass the pinned
CAFI authority registry. An ignored-inclusive search of the registry found
neither authority. No alias rewriting to NRRL ISP accessions was performed.
NCIB and NCIMB, and IMRU 3440 versus IMRU 3440-8/-14, remain distinct keys.
Substring hits such as DSM 20140/20147 and RIA 1441 are not matches.

**Assembly families and quality.** Complete native NCBI rows support:

| Deposit | Assembly | Native location | Sample / project |
| --- | --- | --- | --- |
| NRRL B-2774 | GCA_000718155.1 | `data/catalog/ncbi_genbank-0000.jsonl.gz:26500` | SAMN02645248 / PRJNA238534 |
| NRRL B-2774 | GCF_000718155.1 | `data/catalog/ncbi_refseq-0000.jsonl.gz:23035` | SAMN02645248 / PRJNA224116 |
| JCM 4055 | GCA_001313525.1 | `data/catalog/ncbi_genbank-0000.jsonl.gz:49282` | SAMD00016951 / PRJDB942 |

The NRRL GenBank/RefSeq assemblies are an explicit identical pair, contig
level, 8,466,185 bp and 357 contigs in the snapshot, WGS JOEW00000000.1.
The separate JCM assembly has 2,177,606 bp and 2,190 contigs, WGS
BBGA00000000.1, and no RefSeq pair. Its native exclusion reasons include
fragmentation, insufficient genome length, frameshifted proteins, and
not being used as type. These are quality warnings, not a broken identity
link or a claim that the culture itself is not nomenclatural type material.

Live NCBI Datasets reports for
[GCA_000718155.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000718155.1/dataset_report),
[GCF_000718155.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000718155.1/dataset_report),
and [GCA_001313525.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_001313525.1/dataset_report)
confirm the deposits, live samples, projects, contig status, and NRRL pair.
The JCM report still marks the assembly atypical and gives the same quality
caveats. Live Datasets associates the RefSeq assembly with PRJNA238534;
the snapshot's RefSeq umbrella PRJNA224116 remains a source-qualified value.
No interchangeability of the JCM and NRRL assemblies is asserted.

**Other genome sources.**

- `data/catalog/gtdb_genomes-0006.jsonl.gz:14769` supplies
  `RS_GCF_000718155.1`, its GenBank accession, sample, umbrella project,
  and exact NRRL B-2774 culture field. A species placement in this genome
  object is not a taxon-level exact mapping of JCM 4055.
- `data/bvbrc/bvbrc-0001.jsonl.gz:23820` supplies `1303691.7`, the JCM
  assembly, sample, and project through both `strain` and `culture_collection`.
- `data/bvbrc/bvbrc-0025.jsonl.gz:11911` supplies `58340.12` and the NRRL
  assembly/sample/project but has no qualifying explicit culture field.
  Its BacDive genome-record assertion is retained; a new direct BV-BRC
  strain join is correctly not inferred from its assembly or taxon alone.
- BacDive references 67770 and 66792 support IMG 2862351378 for NRRL,
  IMG 2734481950 for JCM, and IMG 2582581651 for NBRC 12789. The last
  object carries source level `complete` but no INSDC assembly or BV-BRC
  identifier. It does not make either contig assembly complete.

**GOLD provenance.** Full native organism/project/analysis scans recover
38 matching organism objects, three projects, and two analyses. The 65
GOLD organism assertions preserve the distinct culture and strain-field
routes rather than counting as 65 different organisms. All 91 GOLD
assertions across the three YAML link lists retain native source IDs,
taxon IDs, and verbatim matching strain fields.

| Culture | Organism | Project | Analysis | IMG |
| --- | --- | --- | --- | --- |
| JCM 4055 | Go0094275 | Gp0094275 | Ga0128434 | 2734481950 |
| NRRL B-2774 | Go0353727 | Gp0187984 | Ga0163490 | 2862351378 |
| NBRC 12789 | Go0098871 | Gp0098871 | None in inspected chain | None supplied by this project |

The project objects are at `data/gold/projects.jsonl.gz:55670`, 122027,
and 57679 respectively; analyses are at `data/gold/analyses.jsonl.gz:74796`
and 104281. Their explicit GenBank/IMG fields reproduce the two supported
assembly chains. Gp0098871 has empty sample/project accessions; these are
not borrowed from the other cultures. The remaining 35 matched organisms
retain species taxon 1914 and their own culture context without gaining
genomes. Native IFM/ISP objects and IMRU 3440 substrains were inspected
as near-matches but correctly supply no unsupported joins.

**StrainInfo deposit scope.** Complete source objects at
`data/straininfo/records.jsonl.gz:24531` and 120664 contain SI-ID 35983
and 168245 respectively. The first has 71 own deposits and 12 sequences;
30 own deposits match retained eligible keys. The second contributes only
CBS 515.69, SI-DP 439384. All relevant deposits are available and their
collections nondeprecated. No matched relation is marked erroneous.

| Matched culture | SI-DP | Deposit taxon |
| --- | --- | --- |
| ATCC 14158 | 97353 | 58340 |
| ATCC 19777 | 119185 | 58340 |
| ATCC 23950 | 103491 | 1883 |
| ATCC 8664 | 119184 | 58340 |
| CBS 515.68 | 230905 | 1914 |
| CBS 515.69 | 439384 | Not supplied; SI-ID 168245 |
| CCM 3010 | 119186 | 58340 |
| CCUG 11120 | 178094 | 58340 |
| CGMCC 4.1949 | 753700 | 1914 |
| DSM 2014 | 164670 | 58340 |
| DSM 40069 | 164668 | 58340 |
| DSM 40213 | 164671 | 58340 |
| HUT 6006 | 178095 | 1914 |
| IFO 12789 | 119191 | 58340 |
| IFO 12903 | 103493 | 58340 |
| IFO 3177 | 119190 | 58340 |
| JCM 4055 | 164674 | 58340 |
| JCM 4589 | 164675 | 58340 |
| JCM 4664 | 180044 | 58340 |
| KCTC 19942 | 556615 | Not supplied |
| NBRC 12789 | 334029 | 58340 |
| NBRC 12903 | 334030 | 58340 |
| NBRC 3177 | 334031 | 58340 |
| NCIB 6959 | 97354 | 58340 |
| NCIMB 9840 | 178097 | 1914 |
| NCTC 6950 | 164676 | 58340 |
| NRRL B-1230 | 164677 | 1914 |
| NRRL B-2774 | 682989 | 1914 |
| NRRL B-5617 | 178098 | 1914 |
| VKM Ac-1278 | 178102 | 58340 |
| VKM Ac-624 | 178103 | 58340 |

ATCC 23950 has only genus-level classification and a false type flag in
the SI source, while JCM/LPSN identify it among type cultures. HUT 6006,
IFO 12903, and NBRC 12903 also illustrate source type-status differences.
These are preserved source disagreements, not permission to rewrite the
record's NCBI lineage or derive a new uniform type flag. KCTC 19942 and
CBS 515.69 retain absent source taxon fields rather than inheriting one.
KCTC 1398 in LPSN is a separate accession, not a rewrite of KCTC 19942.

CBS 515.69 occurs as a designation relation in SI-ID 35983 but as an own
deposit in SI-ID 168245. The latter's alternative pointer to 35983 does
not transfer sequences. The record correctly has no CBS sequence links.
Live DataCite metadata for
[SI-ID35983.3](https://api.datacite.org/dois/10.60712/si-id35983.3) and
[SI-ID168245.1](https://api.datacite.org/dois/10.60712/si-id168245.1)
confirms findable DSMZ strain-record DOIs, not deposit IDs or publications.

**Sequence evidence.** All nine nucleotide references have explicit
sequence-to-own-deposit links, and live NCBI nucleotide EFetch confirms
their accessions, lengths, descriptions, and source cultures:

| Accession | Culture | Length | Scope |
| --- | --- | --- | --- |
| [AB184146.1](https://www.ncbi.nlm.nih.gov/nuccore/AB184146.1) | NBRC 12789 | 1,435 | Partial 16S |
| [AB249971.1](https://www.ncbi.nlm.nih.gov/nuccore/AB249971.1) | NBRC 12903 | 1,457 | Partial 16S |
| [AB684620.1](https://www.ncbi.nlm.nih.gov/nuccore/AB684620.1) | NBRC 12789 | 34,315 | Streptothricin biosynthetic cluster |
| [D44250.1](https://www.ncbi.nlm.nih.gov/nuccore/D44250.1) | JCM 4589 | 121 | Partial 16S |
| [D44293.1](https://www.ncbi.nlm.nih.gov/nuccore/D44293.1) | JCM 4664 | 120 | Partial 16S |
| [D85116.1](https://www.ncbi.nlm.nih.gov/nuccore/D85116.1) | IFO 12789 | 1,514 | 16S |
| [HQ426713.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ426713.1) | NRRL B-1230 | 1,530 | Partial 16S |
| [U93347.1](https://www.ncbi.nlm.nih.gov/nuccore/U93347.1) | JCM 4055 | 280 | Partial 16S-23S spacer |
| [X53173.1](https://www.ncbi.nlm.nih.gov/nuccore/X53173.1) | DSM 2014 | 1,329 | Partial 16S |

The YAML preserves unversioned source accessions and does not upgrade
them from the live responses. X53173's current nucleotide taxon is species
1914 while its SI deposit context is subspecies 58340; the latter remains
source-qualified. AB684620 is an annotated cluster, not a whole genome
or experimental proof of activity, resistance, or production by every
deposit grouped in BacDive. KF498701 belongs to unretained BCRC 12163
in the SI object and is correctly not copied into this record.

The local `kg-microbe-sources imodulondb datasets` adapter was attempted
through `uv run --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw`
and failed on sandbox DNS. Read-only fallback to the official
[dataset API](https://imodulondb.org/api/datasets) returned 20 organism
entries, none S. lavendulae. S. albidoflavus and S. coelicolor are not
substitutes. iModulonDB is not applicable; this is not negative evidence
for the annotated cluster. No component summary was warranted.

## Completeness

- The sole directly filed BacDive strain and all 43 source culture IDs
  are retained; there is no hidden truncation of the strain list.
- Complete raw inventories reproduce all implemented fields and find no
  direct target LPSN, GTDB mapping, Madin, or BactoTraits taxon row.
- Ignored-inclusive compressed searches across all 149 selected NCBI,
  GTDB, and BV-BRC native shards checked retained culture-key spellings
  and the otherwise culture-free BacDive BV-BRC identifier. Actual keys
  were distinguished from longer accession substring hits.
- Ignored-inclusive compressed searches of `data/atb/` and
  `data/catalog/allthebacteria.tsv.xz` found no target ID, label, slug,
  BacDive key, SAMD00016951, or SAMN02645248. This is a bounded pinned
  source miss, not proof that the organism lacks genomes elsewhere.
- Optional record-level evidence, nomenclature, type flag, synonyms,
  and causal graph are not required additions for this seeded identity
  record. Phenotypes and media recipes belong to their respective Mechs.
- Current BacDive culture-list expansion and assembly quality caveats
  remain documented limitations. This review did not refresh sources or
  establish sequence equality across the retained deposits.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

The source classification/type-status disagreements and JCM assembly
quality warnings above remain unresolved at their authorities. The YAML
preserves their scope and makes no contrary completeness, quality, or
genome-equivalence claim, so they are not classified as curation defects.

## Recommended Edits

None required for this record under the documented source-preserving
contract. Do not hand-edit generated YAML, infer a CBS sequence link,
replace KCTC or NCIB accessions, upgrade unversioned accessions, or promote
this automated review to human `REVIEWED` status.

Any future source refresh belongs in the maintained primary snapshot and
extraction workflow, followed by `src/taxonmech/seed.py`; culture matching
is owned by `src/taxonmech/genome_sources.py`, and SI own-deposit matching
by `src/taxonmech/straininfo.py`. No change to these owners is proposed here.

## Follow-up Checks

No corrective change needs verification. For a future authorized refresh,
repeat the own-deposit and source-chain comparisons, especially the two
SI strain IDs, ATCC 23950, KCTC 19942, and the separate JCM/NRRL assembly
families. Run the two focused validators above; use `just verify-corpus`
in the full-corpus workflow after regeneration.

Do not use the atypical JCM assembly for downstream complete-genome or
type-genome claims without a separate quality assessment. Confirm any
new culture or sequence relationship at its own source before importing it.

## Additional Notes

- All absence searches described here include ignored files by direct
  filesystem/table reads or `rg --no-ignore --hidden`, with `-z` for
  compressed inputs. Their scope is explicitly bounded above.
- Native SI objects were reread in separate untruncated portions after
  an initial combined output truncated. Complete target/source reads,
  not truncated snippets, support the verdict.
- No source refresh, generator, paid provider, GitHub mutation, history
  append, status promotion, or tracked record edit was performed.
- Before this report, the ignored-inclusive report/index comparison
  counted 21,560 unique matched reports among 625,960 indexed records,
  with zero duplicate or unmatched report stems. Eukaryota remained
  6,243/6,243 and was not re-reviewed. This is report-presence coverage,
  not a claim that every earlier review passed or was re-audited here.
