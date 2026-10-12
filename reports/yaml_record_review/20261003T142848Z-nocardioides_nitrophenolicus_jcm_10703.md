# YAML Record Review: Nocardioides nitrophenolicus JCM 10703

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nocardioides_nitrophenolicus_jcm_10703.yaml`
- Started UTC: 2026-10-03T14:25:51Z
- Finished UTC: 2026-10-03T14:28:48Z
- Verdict: pass

## Target

- Class `TaxonRecord`; identifier `NCBITaxon:1303688`; rank `STRAIN`;
  domain `BACTERIA`; parent `NCBITaxon:60489`, Nocardioides nitrophenolicus.
- Read all 1,063 YAML lines in three untruncated portions. Grounding is
  `EXACT`, mapping status `SEEDED`, and genetic code 11.
- One BacDive strain, 11110, carries six retained identifiers, 19 assembly
  assertions, 15 other-genome assertions, and 54 related assertions.
  These are source-qualified assertions, not counts of distinct genomes.
- Four source attestations and one seed event are present. There are no
  synonyms, taxon-level GTDB mappings, nomenclature entries, or causal graphs.
- The YAML is generated and remains unchanged. This review writes only
  this report, apart from the strict validator's standard diagnostic.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/nocardioides_nitrophenolicus_jcm_10703.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/nocardioides_nitrophenolicus_jcm_10703.yaml`:
  PASS; one file scanned, zero errors. Standard diagnostic:
  `reports/instance_validation_failures.tsv`.
- Structured identity, ten ancestor labels/ranks and complete parent chain,
  empty NCBI synonym fields, singleton subtree, and exact source-classified
  strain-count checks: PASS.
- Exact assertion comparison: 17 raw plus two StrainInfo assemblies,
  15 raw genome assertions, and 48 raw plus six StrainInfo related
  assertions reproduce every corresponding YAML field.
- In-memory StrainInfo replay reproduces three strain/deposit links,
  two assemblies, and six related assertions, with no exclusions.
- Every actual matched-deposit field passes the maintained CAFI matcher.
  Two retained identifiers correctly do not qualify as join keys.
- In-memory ATB replay reproduces zero strain links, zero genome links,
  and the one sample exclusion `assembly_unavailable`.
- `just verify-corpus`: Not checked; full-corpus-only. Global provenance,
  downloaded sequences, pages, and exports were not audited.
- Ignored-inclusive ID/name/slug searches of `history/` found no target
  entry. Standalone history validation had no target; strict validation
  checked the embedded event. No history or review-status change was made.
- Graph/product evidence gates are not applicable to this graph-free
  record. Semantic checks were not inferred from validator success.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308112` supports the exact label, rank,
species parent, code, and empty synonym fields. The complete native name
object at `data/catalog/ncbi_names-0007.jsonl.gz:30658` supplies the
scientific name. All ten root-first lineage entries match the complete
pinned parent chain, and the target subtree contains only 1303688.

The NCBI browser failed through the web tool. Inspected read-only
[Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303688&retmode=xml)
confirms strain rank, label, parent 60489, code 11, and lineage.
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303688)
also returns `STRAIN` and all ten lineage IDs. The strain record is not
interchangeable with its parent species, despite shared culture evidence.

[JCM 10703](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=10703)
supports the history from Y.-H. Park NSP41 and the CIP 107017, DSM 15529,
KCTC 0457BP, and NRRL B-24725 equivalences. Its current page links to
species taxon 60489 and the newer complete assembly. NCBI still retains
the strain node for the older assembly. These different taxon scopes are
preserved rather than silently reassigning the record.

[LPSN 778827](https://lpsn.dsmz.de/species/nocardioides-nitrophenolicus)
supports the validly published correct species name and these type-culture
designations. `data/raw/lpsn_names.tsv:18674` maps that name to species
60489, not strain 1303688. The missing strain-level nomenclature and
derived type flag follow the documented same-record LPSN rule. They do
not assert that this culture is non-type: native BacDive and all three
StrainInfo own deposits explicitly identify type material.

There is no species-to-strain GTDB synonym promotion here. A correctly
qualified DSM genome link does not require a taxon-level GTDB mapping.

## Evidence

**Identity inventory and attestations.**
`data/raw/bacdive_strains.tsv:10963` supports all six retained identifiers,
empty designation, direct strain taxon, and raw medium count zero. The
zero is omitted from the strain entry. It is not the same count as the
direct taxon-level MediaDive attestation:

| Source | Inventory location | Supported count |
| --- | --- | --- |
| NCBI | `data/raw/ncbitaxon_taxa.tsv:308112` | 1 NAME |
| BacDive | `data/raw/bacdive_strains.tsv:10963` | 1 STRAIN |
| MediaDive | `data/raw/mediadive_taxa.tsv:2814` | 3 MEDIUM: 65, 92, J22 |
| BactoTraits | `data/raw/bactotraits_taxa.tsv:2279` | 1 TRAIT_ASSERTION |

`curation/seed_scope.tsv:22455` supplies the four-source admission reason.
The 2026-09-13T17:54:04Z seed event reproduces it, without claiming human
review. Complete exact-field scans found no direct target LPSN, GTDB,
GOLD, or Madin row. Native GOLD/GTDB genome associations below do not
manufacture additional KGX taxon-attestation counts. The units cannot be
summed into a count of experiments, strains, or genomes.

**Culture-key boundary.** The complete BacDive object at
`data/bacdive/records.jsonl.gz:10962` retains CIP 107017, DSM 15529,
JCM 10703, KCTC 0457BP, NRRL B-24725, and NSP 41. Its two genome
objects agree with the inspected [BacDive page](https://bacdive.dsmz.de/strain/11110).
Reference 66792 remains attached to the appropriate JCM or DSM genome.

The pinned CAFI register's KCTC full-accession template is `^\d+$`.
Consequently KCTC 0457BP is retained, percent-encoded in the CURIE, but
does not supply a supported genome join. This is a matcher limitation,
not a declaration that the culture number is fictitious: JCM and LPSN
explicitly list it. NSP 41 is a laboratory designation, not a registered
culture key. Do not remove leading zeroes or BP, rewrite collection
prefixes, or treat the retained alias as an authority-qualified accession.
The other four retained identifiers pass the matcher.

**Three assembly families.** Full source-native objects support:

| Deposit/family | Assembly accession(s) | Sample | Original project | Native sequence context |
| --- | --- | --- | --- | --- |
| Older JCM 10703 | GCA_001313605.1 | SAMD00016918 | PRJDB946 | BBGE00000000.1 |
| DSM 15529 | GCA_016907515.1 / GCF_016907515.1 | SAMN17620042 | PRJNA695682 | JAFBBY000000000.1 |
| Newer JCM 10703 | GCA_055397175.1 / GCF_055397175.1 | SAMD01611097 | PRJDB20694 | AP043736 in BV-BRC/JCM |

- Older JCM: `data/catalog/ncbi_genbank-0000.jsonl.gz:49286`,
  ASM131360v1, 1,570 contigs and 1,570,668 bp; taxon 1303688;
  no RefSeq pair. Source exclusion notes state fragmentation and that
  this assembly is not used as type.
- DSM: `data/catalog/ncbi_genbank-0015.jsonl.gz:20547` and
  `ncbi_refseq-0003.jsonl.gz:21935`, ASM1690751v1, 5,815,017 bp,
  one contig, source level `Contig`, taxon 60489. A single contig is not
  permission to change the source level to Complete Genome.
- Newer JCM: `data/catalog/ncbi_genbank-0051.jsonl.gz:9662` and
  `ncbi_refseq-0008.jsonl.gz:21269`, ASM5539717v1, 5,815,021 bp,
  one replicon, source level Complete Genome, taxon 60489, released
  2025-08-27. Both source GenBank/RefSeq pairs are marked identical.

Inspected [live NCBI assembly reports](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_001313605.1,GCA_016907515.1,GCF_016907515.1,GCA_055397175.1,GCF_055397175.1/dataset_report)
resolve all five versioned accessions as current and confirm strains,
levels, pairs, sample accessions, original projects, and the old JCM
quality notes. BioSample attributes explicitly name JCM:10703 or
DSM:15529. The pinned RefSeq and GTDB sources instead use umbrella
project PRJNA224116; those source-specific fields remain preserved.
The association of the older assembly does not certify its quality.

**Other genome sources.** Full BV-BRC objects are:

- `data/bvbrc/bvbrc-0001.jsonl.gz:23815`: 1303688.4,
  GCA_001313605.1, older JCM sample/project, and both culture and strain
  fields. Native WGS accession is BBGE00000000.
- `data/bvbrc/bvbrc-0025.jsonl.gz:34254`: 60489.4,
  GCA_016907515.1, DSM sample/project, and both culture and strain fields.
  Native WGS accession is JAFBBY000000000.
- `data/bvbrc/bvbrc-0025.jsonl.gz:34255`: 60489.6,
  newer JCM sample/project, AP043736, and both culture and strain fields.
  It has no `assembly_accession` field. The YAML therefore keeps this
  BV-BRC genome and related evidence without inventing a BV-BRC-sourced
  NCBI assembly assertion from another source's accession.

`data/catalog/gtdb_genomes-0004.jsonl.gz:42210` explicitly identifies
DSM 15529 on RS_GCF_016907515.1, with the corresponding GenBank accession,
sample, umbrella project, contig level, and species taxon 60489. It is
the GTDB cluster representative. The culture match, not species-name
similarity, supplies the strain-genome association.

**GOLD chains.** Complete native objects establish:

- Go0093083 -> Gp0093083 -> Ga0128438 -> GCA_001313605.1,
  IMG 2734481954. Locations are `data/gold/organisms.jsonl.gz:54595`,
  `projects.jsonl.gz:54971`, and `analyses.jsonl.gz:74800`.
- Go0551218 -> Gp0502579 -> Ga0451139 -> GCA_016907515.1,
  IMG 2893560988. Locations are `data/gold/organisms.jsonl.gz:389566`,
  `projects.jsonl.gz:362451`, and `analyses.jsonl.gz:284104`.

Both analyses are isolate genome analyses; the project IDs resolve to
the named organisms, and their direct organism fields are blank rather
than conflicting. Both culture and strain fields supply retained evidence.
Go0626812 and Go0626813 at organism rows 457401 and 457402 support
NRRL and CIP organism-only references, not fabricated assemblies.
Native Go0028200 at row 23974 names KCTC 0457BP; it is retained in the
catalog but does not pass the current whole-accession matching boundary.
All sample/project/organism/analysis references remain outside genome counts.

**StrainInfo.** The complete object at
`data/straininfo/records.jsonl.gz:70881` is SI-ID 100824, published
online, with source BacDive 11110. Three own deposits are available,
nondeprecated, and nonerroneous: DSM SI-DP 303273, CIP 305333, and
JCM 305334. [DataCite](https://api.datacite.org/dois/10.60712/si-id100824.3)
confirms DOI 10.60712/SI-ID100824.3 as a findable version-3 source strain
record, not a publication or separate deposit identifier.

`data/straininfo/strain_links.tsv:3317` through 3319 preserve all three
matches. Assembly rows 439 and 440 preserve unversioned source accessions:
GCA_001313605 explicitly names JCM 305334, while GCA_016907515 explicitly
names DSM 303273. Neither transfers to CIP despite its relation to JCM.
The six related assertions are three deposit and three source-strain
references. KCTC, NRRL, and NSP41 occur only as relation designations in
this source object; no additional own-deposit or sequence evidence follows.

**AllTheBacteria exclusion.** `data/atb/assemblies.tsv:8090` retains
SAMN17620042 with `NOT_PROCESSED`, dataset `not_processed`, unavailable
FASTA flag 0, and no run, ENA assembly, checksum, or download URLs.
The complete catalog contains the same row at
`data/catalog/allthebacteria.tsv.xz:1990968`.
`data/atb/exclusions.tsv:3318` records `assembly_unavailable`.
Replaying the source evidence yields precisely this exclusion and no
strain/genome links. An available NCBI assembly does not make an ATB
assembly available, and no download URL should be constructed from it.

## Completeness

- Complete taxonomy and BacDive scans confirm one relevant strain and
  no omitted descendants. Complete raw and SI comparisons reproduce
  every asserted link, with versions and nested evidence intact.
- A full native StrainInfo own-deposit scan finds only SI-ID 100824
  for eligible retained culture keys. All three eligible deposits and
  both source sequence objects are represented at their explicit scope.
- Ignored-inclusive, decompression-aware searches covered the complete
  native NCBI/GTDB catalog shards, BV-BRC, GOLD, BacDive, and StrainInfo.
  Unsupported KCTC/NSP keys were preserved rather than forced into joins.
- Ignored-inclusive searches of all ATB inventories and the full
  compressed ATB catalog found the unavailable DSM row above and no
  rows for SAMD00016918 or SAMD01611097. This is bounded pinned-snapshot
  coverage, not evidence that public reads or other assemblies do not exist.
- Native BacDive/JCM pages contain marker and RNase P sequence context
  outside this SI snapshot. No marker accession or phenotype was copied
  onto another deposit or represented as an assembly. This is not a
  claim of exhaustive literature or marker-sequence coverage.
- The YAML names no gene, locus, regulator, pathway, or transcriptomics
  dataset. Its BactoTraits count is an inventory attestation, not a named
  mechanistic claim. An iModulonDB component query is not applicable.
- Optional definition, phenotype evidence, and causal graph are correctly
  unfilled. The absent type flag must not be read as a negative biological
  assertion; its derivation is explicitly limited to same-taxon LPSN data.

## Findings

None found under the documented source-preserving contract.
Finding counts: zero blockers, zero major, zero minor.

Assembly quality, unsupported culture-accession syntax, and the limited
type-flag derivation are documented boundaries, not reasons to fabricate
new equivalences or to patch generated YAML in this read-only review.

## Recommended Edits

None required for this record. Preserve the three assembly/sample families,
native versions and levels, separate genome namespaces, and SI-DP scope.

Any authorized future expansion for KCTC accession syntax belongs
in the maintained authority register/matcher with source-backed tests, not
by trimming BP or overriding the generated record. Future type-flag policy
changes belong in `src/taxonmech/seed.py` with regression tests, not by
silently promoting parent-species nomenclature to strain identity.

## Follow-up Checks

- After a source refresh, replay the exact raw/SI comparisons and ATB
  eligibility decision before adding, replacing, or deleting a link.
- Check for explicit new CIP or NRRL deposit-sequence evidence; grouping
  with DSM/JCM remains insufficient to transfer an assembly.
- Preserve the old assembly's quality notes, the newer assembly's own
  sample, and the DSM source's Contig level even though it has one contig.
- Rerun both focused validators after an authorized change. Broad
  regeneration requires `just verify-corpus` and documented product gates.

## Additional Notes

Public NCBI, DataCite, and JCM verification used approved read-only network
access after the browser/sandbox limitations observed during this review
session. No paid research, source refresh, GitHub mutation, history write,
or promotion from `SEEDED` to `REVIEWED` was performed.
