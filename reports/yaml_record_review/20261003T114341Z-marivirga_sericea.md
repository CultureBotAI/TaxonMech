# YAML Record Review: Marivirga sericea

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marivirga_sericea.yaml`
- Started UTC: 2026-10-03T11:40:46Z
- Finished UTC: 2026-10-03T11:43:41Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:1028`, Marivirga sericea,
rank SPECIES, domain BACTERIA, parent `NCBITaxon:869806`. The entire
836-line YAML was read in three contiguous sections. It has EXACT
grounding, SEEDED mapping status, one LPSN name, two GTDB mappings,
three synonyms, two xrefs, one BacDive strain, eight source attestations
and one embedded seed event. The strain carries nine assembly, seven
genome-record and 33 related-record assertions, not that many distinct
genomes.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/marivirga_sericea.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/marivirga_sericea.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive target searches found no history entry. Strict validation covered the embedded event. |

All eleven lineage entries matched the full pinned taxonomy table.
Complete subtree traversal found only this taxon; complete BacDive
inventory inspection found exactly strain 5474 classified here.
Structured comparisons proved exact reproduction of eight raw assembly,
six raw genome and 24 raw related-record assertions. Native StrainInfo
and ATB objects support the remaining overlay assertions. All six ATB
sample links matched the committed strain-link evidence exactly.

## Identity and Grounding

Raw taxonomy row 799 and the inspected
[NCBI taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1028)
agree on species identity, rank, code 11 and lineage through
Marivirgaceae. Native NCBI names contain the scientific name, two
authority names and the Microscilla sericea synonym. The YAML's
related authority forms and exact generic synonym follow those source
categories. An exact taxonomic synonym does not assert valid publication
of the old Microscilla name, which the NCBI page distinguishes explicitly.

Raw LPSN row 25838 supplies name 788714, the author/emendation citation,
legitimate/valid/correct flags, four type designations and the GTDB
Marivirga sericea cross-reference. The inspected
[LPSN page](https://lpsn.dsmz.de/species/marivirga-sericea) supports the
name, status and 2019 emendation, but also lists NCIMB 1403 and NCMB
1403 as type designations. The web tool returned an older cached LPSN
page; the NCIMB designation is independently corroborated by the
original publication and native NCBI/StrainInfo evidence.

## Evidence

**Two GTDB concepts, not two equivalent names.** Ignored-inclusive
decompressed searches of every native GTDB genome shard found one member
of `s__Marivirga sericea`: representative RS_GCF_900177665.1, DSM 4125,
NCBI taxid 1028. LPSN independently links this species concept, explaining
its equivalence xref even though the upstream predicate is broadMatch.

The complete `s__ELB16-189 sp020403045` cluster has 16 members: fourteen
with taxid 2053541, one with taxid 2099675 and one with target taxid 1028.
Its representative is GB_GCA_020403045.1, designation M037S2SP1A04QC,
taxid 2053541. The sole target-taxid member is GB_GCA_943369935.1,
isolate JJ-KL17-317-1-m2-bin62, sample SAMEA14447138, project PRJEB49198.
Raw GTDB rows 1220-1221 retain the cluster counts 16 and 1 respectively.

The pooled cluster is neither an exact synonym nor an xref. Its count
is not added to the primary one-genome attestation, which points readers
to the additional mapping. This preserves the documented pooling
semantics. GTDB uses Bacteroidia/Cyclobacteriaceae while NCBI uses
Cytophagia/Marivirgaceae; the NCBI tree is retained. Both GTDB web
endpoints were inaccessible, so native RS232 metadata supplied the audit.

**Type strain and primary genome.** Raw BacDive row 5365, its complete
native identity/sequence object and the inspected
[BacDive page](https://bacdive.dsmz.de/strain/5474) agree on strain 5474,
target classification, type status and the four listed deposits.
The designation NICMB 1403, SIO-7 is verbatim source text, not a license
to correct a prefix or create a culture join. All four listed culture
identifiers pass the repository's full authority/accession matcher;
NICMB 1403 and SIO-7 do not.

Native current/historical NCBI assembly searches retain the paired
GCA/GCF_900177665.1 scaffold assembly, DSM 4125, taxid/species taxid
1028, BioSample SAMN05661096 and WGS FXAW00000000.1. GenBank supplies
PRJEB20272 and RefSeq PRJNA224116. Native BV-BRC 1028.3 reproduces the
GenBank assembly, sample, project and explicit DSM deposit. GTDB's
representative reproduces the same sample and paired accessions.

Native GOLD Go0103658 -> Gp0103658 -> Ga0056958 explicitly connects
DSM 4125, SAMN05661096, GCA_900177665.1 and IMG 2595699006. GOLD's project
is PRJNA262279, preserved separately from the NCBI/BV-BRC projects.
The analysis has an empty organism field but an unambiguous project
chain. BacDive reference 66792 independently supplies unversioned
GCA_900177665, BV-BRC 1028.3 and IMG 2595699006. Unversioned assertions
remain unversioned; co-listing alone is not treated as genome equivalence.

The native NCBI object for GCA_943369935.1 identifies a metagenomic
isolate, no culture-deposit strain, and RefSeq exclusions for unverified
source organism and metagenome derivation. Its GTDB placement explains
the pooled mapping but does not support assigning this genome to DSM
4125. The target correctly lacks that strain-genome join.

**GOLD organism coverage.** The six native organisms at taxid 1028
match raw GOLD count 6. Go0029858, Go0103658, Go0620226 and Go0620227
explicitly name ATCC 23182, DSM 4125, NBRC 15983 and LMG 13021. The
remaining Go0620224 and Go0620225 retain bare SIO-7 and NICMB 1403
with empty collection fields. Their taxon attestations do not authorize
deposit-level links. The four supported organism associations are
retained separately from genome and project records.

**StrainInfo boundaries.** Native SI-ID 10157, DOI
10.60712/SI-ID10157.3, owns available DSM 4125 (SI-DP 158648), LMG
13021 (39946), ATCC 23182 (39947) and NBRC 15983 (487124). These
four exact existing-deposit matches supply the eight strain/deposit
assertions. GCA_900177665 and gene AB032590 each explicitly name DSM
4125 / SI-DP 158648; no other deposit inherits either sequence.
The gene remains a NUCLEOTIDE_SEQUENCE rather than a genome.

The native source also retains NCIMB 1403 (39949), NCMB 1403 (158649),
IFO15983 (205741) and KCTC 2899 (314477). They are not current BacDive
collection IDs. KCTC has genus-level taxid 1023 and type false; ATCC's
source-specific type flag is also false, unlike LPSN/BacDive. Those
native conflicts do not override the YAML's LPSN-derived type flag.
Source grouping and alias similarity cannot create missing deposit joins.
The version DOI endpoint was unavailable, but the native record and
archive both retain that exact DOI.

**ATB evidence.** The full pinned `data/catalog/allthebacteria.tsv.xz`
contains SAMN05661096 with run SRR4136499, ENA analysis ERZ26859507,
dataset 661k, assembly/HQ filters PASS and an available FASTA flag.
The complete row matches `data/atb/assemblies.tsv`, including SeqKit
sum `seqkit.v0.1_DLS_k0_1db7487a495d87bd903cedcd73b8df20`, supplied AWS
URL, OSF archive URL and batch filename. No exclusion row was found
in the complete committed exclusion table for this strain/sample.

The six retained sample assertions derive from BV-BRC, GOLD, GTDB and
NCBI with explicit DSM deposit evidence. All five committed genome
crosslinks have inspected matching genome/sample source chains and
relationship shares_biosample: GTDB, IMG, GenBank, RefSeq and BV-BRC.
This supports the local snapshot assembly ID, not sequence identity
with those other genomes. No FASTA was downloaded; current remote
availability or checksum validity was not tested. ENA's live analysis
page was inaccessible.

**Literature and sequences.** The inspected
[original publication abstract](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.016121-0)
supports the name revision and explicitly lists LMG 13021, ATCC 23182,
NBRC 15983 and NCIMB 1403 as the type strain. PMID 19767357 resolves
to the matching article title, although reliable PubMed body retrieval
was unavailable. The inspected
[notification-list abstract](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.028779-0)
matches LPSN's cited volume and publication; its full list was not read.

AB078081 is linked by LPSN and the native BacDive 16S entry for IFO
15983. AB032590 is explicitly a DSM 4125 gyrB sequence in the native
StrainInfo object, including the source's misspelled descriptive title.
Direct NCBI/ENA sequence retrieval failed for both, so those live
authority records remain independently unresolved, not proven broken.

**Attestations and audit.** NCBI, LPSN, GTDB, BacDive, MediaDive, GOLD,
Madin and BactoTraits inventories support counts 1 NAME, 1 NAME,
1 primary-cluster GENOME, 1 STRAIN, 2 MEDIUM, 6 ORGANISM, 1
TRAIT_ASSERTION and 1 TRAIT_ASSERTION. MediaDive row 85 names 172 and
514. Scope row 1615 and the seed event name the same eight sources.
Source counts do not introduce phenotype or medium-performance claims.

## Completeness

The complete source-classified strain listing and supported genome
systems are present. The pooled metagenome, unrecognized GOLD names
and unmatched StrainInfo deposits correctly remain outside strain joins.
The consequential presentation gap is in LPSN type-designation coverage,
not an absent biological strain or unsupported genome claim.

Ignored-inclusive target ID, label and slug searches covered raw data,
curation, history and report filenames. No prior report or history
entry was found. Separate raw culture/StrainInfo inventory searches
distinguished the existing four join keys from additional native deposits.
No whole-repository absence of those additional identities is claimed.

The gyrB reference triggered a structured iModulonDB check. The installed
runner in the local culturebotai-claw checkout was located, but
`kg-microbe-sources imodulondb datasets` failed resolving its endpoint.
Web API and home-page fallbacks returned no usable dataset body. Coverage
was therefore not established; no negative expression evidence is inferred.
The YAML asserts sequence identity, not an expression module or phenotype.
Empty definition, discussion, curator evidence and causal-graph slots
are otherwise appropriate for the seeded record.

## Findings

**Minor m1: LPSN type-designation list is incomplete.** NCIMB 1403 and
NCMB 1403 appear on the inspected LPSN page but not in raw LPSN row
25838 or the YAML nomenclature list. NCIMB is independently corroborated
by the original publication, NCBI type material and native StrainInfo;
NCMB also has its own native StrainInfo deposit. The four retained
designations and type flag remain supported, so this is non-blocking.

Maintained owners: upstream kg-microbe LPSN type-strain edges feeding
`data/raw/lpsn_names.tsv`, consumed by `src/taxonmech/extract.py:445`
and projected by `src/taxonmech/seed.py:405`. Configured upstream edge
files are unavailable at their configured paths, so the exact upstream
loss stage is unresolved. The seeder faithfully copies its current input.

Finding counts: 0 blocker, 0 major, 1 minor. The native ATCC type-flag
conflict, historical aliases, source-specific taxonomy and inaccessible
live endpoints are preserved as caveats, not additional proven defects.

## Recommended Edits

1. Refresh or repair the upstream LPSN type-designation representation,
   preserving distinct authoritative NCIMB and NCMB identifiers and their
   provenance. Do not manufacture them by rewriting BacDive's NICMB text.
2. Re-extract and re-seed through the maintained workflow. Any proposed
   addition to BacDive strain deposits needs its own source-supported
   inventory change; adding nomenclature alone does not authorize joins.
3. Preserve the LPSN-supported GTDB identity, pooled-cluster separation,
   sequence typing, source accession versions and ATB sample evidence.

## Follow-up Checks

1. Compare regenerated LPSN designations against inspected authoritative
   source text; test both retention of distinct prefixes and rejection
   of the unrecognized NICMB alias as a join key.
2. After maintained changes, use the documented dry-run/canary workflow,
   both focused validators and `just verify-corpus`. Confirm the metagenome
   remains unjoined and all five ATB crosslinks remain shares_biosample.
3. Retry live nucleotide, StrainInfo DOI and ENA endpoints for independent
   resolution. Repeat the iModulonDB dataset lookup only before making
   any expression-context claim; none is supported or needed here.

## Additional Notes

Only this new report was manually written. No YAML, inventory, status
or history event changed. Strict validation emitted its normal diagnostic
TSV. No paid research, GitHub mutation, index rebuild or sequence download
was performed. Eukaryota was untouched.
