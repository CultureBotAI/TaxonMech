# YAML Record Review: Flavobacterium sp. P13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/flavobacterium_sp_p13.yaml`
- Started UTC: 2026-10-03T18:56:33Z
- Finished UTC: 2026-10-03T19:00:10Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303894`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196869`,
code 11, grounding `EXACT` and mapping status `SEEDED`. Twelve
lineage entries, one NCBI NAME attestation, zero strains and one
embedded seed event are present. No synonyms, nomenclature, taxonomy
mappings, equivalence xrefs, strain/genome links, experiments or graph
are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/flavobacterium_sp_p13.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/flavobacterium_sp_p13.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured comparison reproduced identity, rank, parent, code,
  empty synonym fields and all twelve lineage objects. No children
  occur. Complete exact-field scans found no membership in seven other
  source inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only, with no invented
  focused substitute. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive exact-ID, label and slug searches found no standalone
  target history event; standalone history validation had no target.
  Strict validation checked the embedded event. Graph/product gates
  are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308212` supports the label, species
rank, parent, code, empty synonyms and 2026-09-13 snapshot. The full
scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30765` agrees. Every ancestor
matches the pinned backbone: root, cellular organisms, Bacteria,
Pseudomonadati, FCB group, Bacteroidota/Chlorobiota group, Bacteroidota,
Flavobacteriia, Flavobacteriales, Flavobacteriaceae, Flavobacterium and
unclassified Flavobacterium.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303894&retmode=xml)
confirms ID, label, species rank, parent 196869, code 11 and all
non-root lineage entries. It supplies no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303894)
confirms label, rank and all twelve ancestor identifiers, including
root. Preserve both `CLADE` ranks and the parent's `NO_RANK`.
Exact grounding and bacterial domain are supported. P13 is an
isolate-like species label, not a registered culture accession,
type-strain claim or reason to change the source rank.

## Evidence

The NCBITAXON / NCBITaxon:1303894 / 1 NAME attestation agrees
with the backbone and snapshot. NAME counts source coverage, not
biological strains, phenotypes or genomes. No DOI, PMID, assembly
accession or experimental quotation is asserted by this YAML.

`data/taxa/PATHS.tsv:106317` pins the slug.
`curation/seed_scope.tsv:393158` admits this species on 2026-09-13
with the exact one-source reason carried by the embedded seed event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. YAML folding does not
change the reason. `SEEDED` remains appropriate; this review does
not confer human-review status.

## Completeness

Exact identity searches and structured source comparisons were completed
before using the ambiguous P13 label. Ignored-inclusive ID, full-label
and slug searches covered raw inventories, curation and history, returning
only the target backbone and scope rows. Complete exact-field scans
found no direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or
BactoTraits membership. No descendants can contribute BacDive strains
in the inspected backbone, supporting the zero count in these inventories.

Ignored-inclusive exact-identity compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. The two matches were read
in full: the target scientific name and an unrelated GenBank assembly.
`data/catalog/ncbi_genbank-0016.jsonl.gz:2053` identifies
GCA_017547925.1, Bacteroidales bacterium taxon 2030927, isolate
RGIG7266, BioProject PRJNA657473 and BioSample SAMN16347737. The
matching number 1303894 is a total/ungapped genome length, not a
taxonomy reference; it does not establish a Flavobacterium relationship.

Exact-identity searches of `data/atb/`, the full
`data/catalog/allthebacteria.tsv.xz`, and StrainInfo TSV/compressed
TSV link, assembly, exclusion and related-record tables found no match.
All searches included ignored files.

The broader whole-token, case-insensitive P13 search across the same
native JSONL directories returned 1,361 objects. Every returned object
was parsed; this was a complete candidate screen, not a sampled count.
Counts were 3 BacDive, 7 StrainInfo, 199 BV-BRC, 228 GTDB genomes,
227 current and 2 historical GenBank, 119 current and 22 historical
RefSeq, 139 NCBI names, and 415 GOLD objects. A substring-safe
full-object screen for Flavobacterium or target ID 1303894 retained
only the target scientific-name object. The screen included GTDB
underscore-prefixed taxonomy strings, not just ordinary word boundaries.

All 797 matching genome objects had explicit organism-name and taxon
fields. They represented 248 distinct name/ID pairs, none with the
target ID. This identity screen does not infer equivalence among
their assemblies or constitute individual reviews of those foreign
records. Genome sequences themselves were not inspected.

All three matching BacDive objects were read in full:

- Native line 10170, BacDive 10309: Nannocystis pusilla taxon
  889268, designation Na p13, DSM 53162, not a type strain.
- Native line 79264, BacDive 157025: Klebsiella pneumoniae taxon
  573, CCUG 68727 / NCTC 13442. P13-U61 is an assembly description,
  not evidence for the target Flavobacterium. Preserve its unversioned
  source GCA_020251505 and BV-BRC 573.41284 as foreign identifiers.
- Native line 99859, BacDive 177636: Herbiconiux liangxiaofengii
  taxon 3342795, designation P13, GDMCC 1.4677 / JCM 37540, type
  strain. Its marker PQ452531 and type status belong to Herbiconiux.

All seven matching StrainInfo objects were also read in full. SI-ID
38441 is Pediococcus damnosus, 40240 Klebsiella/Raoultella
ornithinolytica, 41125 Proteus mirabilis, 51984 Mannheimia
granulomatis with a second deposit classified at Pasteurellaceae,
215736 Nannocystis pusilla, and 300018/300865 Pleurotus pulmonarius.
Their P13 matches occur in clone descriptions or longer designations;
none supplies a Flavobacterium deposit. The source inconsistencies
within these foreign records were not resolved or transferred to the
target. No Eukaryota YAML was re-reviewed.

The matching GOLD objects comprise 123 organisms, 153 projects and
139 analyses. Structured inspection of every matched organism found
an explicit name and taxon ID, 28 distinct taxon values, no target
taxon and no culture-collection identifier. The full-object screen
found no Flavobacterium reference in the matched GOLD objects. P13
alone cannot establish an eligible culture match; the 292 project and
analysis objects were screened, not individually reconstructed as
unrelated genome chains. No GOLD organism/project/analysis relationship
was added on the strength of that ambiguous label.

The broader ignored-inclusive TSV search parsed all 364 matching rows:
134 backbone, 132 scope, 25 GTDB species, 47 GTDB mappings,
2 BacDive strains, 2 NCBI type-material, 5 strain assemblies,
1 strain genome record, 2 StrainInfo related records and 14 ATB
catalog rows. The only rows containing Flavobacterium or target ID
were the target backbone and scope rows. Matching culture, type,
genome, StrainInfo and ATB rows were read in full.

The BacDive and type-material rows identify Nannocystis/Herbiconiux,
while the five assembly rows and BV-BRC row identify Klebsiella
NCTC 13442. The two StrainInfo rows carry nucleotide EU623109 for
ATCC 31898 / SI-DP 108609 under taxon 54291; one preserves a
BacDive-reference-conflict flag. They are clone-marker evidence for
that deposit, not whole-genome evidence or Flavobacterium links.

Of the 14 ATB P13 matches, 12 carry META_FAIL and two have PASS
status: SAMN02256396 and SAMN02440552. Their source names identify
SCGC AB-629-P13 and SCGC AAA252-P13 in other taxonomic contexts;
neither supplies a deposit/BioSample chain to this taxon. PASS status,
an ENA analysis or an available download URL alone cannot establish
identity. No sample/genome equivalence was inferred and no FASTA was
downloaded. Unknown or conflicting foreign names remain unresolved,
not silently assigned to Flavobacterium.

These checks justify empty optional fields within the inspected source
boundary; they do not prove that cultures or sequences cannot exist
elsewhere. Original primary archives were not independently reproduced.
No gene, regulator, pathway, trait or transcriptomic assertion is
present in the target; iModulonDB is not applicable. Foreign marker
descriptions do not change that scope. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None. Retain the exact identity, all twelve source lineage entries,
zero strain count and `SEEDED` status. Do not join by P13 alone,
transfer a foreign type-strain flag, promote marker sequences to
genomes, or attach ATB assemblies without the required explicit
source chain. Future evidence belongs in maintained source pipelines
and inventories, followed by authorized seeding, not manual YAML edits.

## Follow-up Checks

No corrective check is required. After an authorized source refresh,
compare exact identity rows and require an eligible culture accession
and explicit deposit/genome evidence before adding links. Keep negative
regression cases for ambiguous aliases separate from any biological
claim. Rerun both focused validators after regeneration. Corpus-wide
claims additionally require `just verify-corpus` and full QC, neither
run here. Foreign record conflicts were outside this target's review.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. Broad native and TSV
search results were captured and parsed completely without truncation.
The 1,361-object screen is not described as a manual full review of
every foreign object: full reading covered the exact-identity hits and
all ten BacDive/StrainInfo matches; remaining candidates were screened
through structured identity fields and complete object text. All searches
and validators completed. Public NCBI reads used network escalation
after established sandbox DNS failures.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
