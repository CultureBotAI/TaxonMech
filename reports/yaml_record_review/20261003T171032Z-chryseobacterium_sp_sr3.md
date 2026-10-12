# YAML Record Review: Chryseobacterium sp. SR3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chryseobacterium_sp_sr3.yaml`
- Started UTC: 2026-10-03T17:09:20Z
- Finished UTC: 2026-10-03T17:10:32Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303837`.
It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2593645`,
genetic code 11, grounding `EXACT` and mapping status `SEEDED`.
Thirteen lineage entries, one NCBI NAME attestation, zero strains and
one embedded seed event are present. No synonyms, nomenclature,
taxonomy mappings, equivalence xrefs, strain/genome links, experiments
or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/chryseobacterium_sp_sr3.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/chryseobacterium_sp_sr3.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduced identity, rank, parent,
  code and all thirteen lineage objects. No children occur. Complete
  exact-field scans found no direct membership in the seven other source
  inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308170` supplies the exact label, species
rank, unclassified-Chryseobacterium parent, code, empty synonym fields
and 2026-09-13 snapshot. The full native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30721` agrees. Every ancestor
matches the pinned backbone, including both clade entries, Weeksellaceae
and the unranked Chryseobacterium group.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303837&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 2593645,
code 11 and all non-root ancestors, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303837)
confirms rank and all thirteen ancestor IDs including root. Exact
grounding is supported. Carry these ranks and the full hierarchy
verbatim; do not replace them with an inferred placement.

Three same-genus prefix matches are different NCBI entities:
SR3-14-l (944041), SR3-15-l (944042) and SR3-16-l (944043), in full
native objects at `data/catalog/ncbi_names-0005.jsonl.gz:8421`,
line 8422 and line 8423, and raw rows 201549-201551. They share the
unclassified parent but are not synonyms or children of SR3.

## Evidence

The NCBITAXON / NCBITaxon:1303837 / 1 NAME attestation agrees with
the backbone and snapshot. NAME counts source coverage, not biological
strains or genomes. The YAML asserts no DOI, PMID, assembly or
experimental quotation.

`data/taxa/PATHS.tsv:106275` pins the slug.
`curation/seed_scope.tsv:393117` admits the taxon on 2026-09-13 using
the exact one-source reason carried by the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and NCBITAXON provenance agree. `SEEDED` remains
accurate; this review does not grant human-review status.

## Completeness

Complete ignored-inclusive whole-token ID/label/slug/SR3 searches
covered raw inventories, curation and history. Complete exact-field
scans found no direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or
BactoTraits membership. There are no descendants to contribute BacDive
strains, supporting the zero count.

Ignored-inclusive compressed JSONL searches covered `data/catalog/`,
`data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/` and
`data/straininfo/`. Full ID/label/slug matches were read as complete
objects: the target name and the three distinct longer Chryseobacterium
names above. The complete SR3 token scan returned 129 lines. Identity
fields were inspected for every match without truncation; all
Chryseobacterium and StrainInfo hits were read as complete objects.
The two BacDive hits were also read in full separately.

Important exclusions:

| Source evidence | Why it does not support a target link |
| --- | --- |
| BacDive 168170, `data/raw/bacdive_strains.tsv:90403`; full native object `data/bacdive/records.jsonl.gz:90402` | Clostridium methoxybenzovorans / Lacrimispora indolis, taxon 69825, deposits DSM 12182 and ATCC 700855. Its SR3 genome taxon 1286820, GCA_000421505, other genome links and markers are not Chryseobacterium evidence. |
| Full StrainInfo object `data/straininfo/records.jsonl.gz:32350` | SI-ID 44179, own ATCC 700855 / SI-DP 118602 and DSM 12182 / SI-DP 118603. Markers LC575943 and AF067965 explicitly concern those deposits. |
| BacDive 141054, raw line 63339; full native object `data/bacdive/records.jsonl.gz:63338` | Streptomyces cerasinus SR3-134, taxon 1807875, deposits TISTR 2494, KCTC 39910 and DSM 114639, marker LC128347. |
| Full StrainInfo object at line 223713 | SI-ID 281769, Streptomyces cerasinus, own DSM 114639 / SI-DP 53049, not the target. |
| Full StrainInfo object at line 2458 | SI-ID 2458, Pectobacterium atrosepticum Graham SR3, taxon 29471, own LMG 2381 / SI-DP 9888 and NCPPB 433 / SI-DP 9890. |
| Native NCBI/GTDB/BV-BRC identity fields | Cryobacterium sp. Sr3 taxon 1259194 (GCA/GCF_004402835.1), Pectobacterium versatile SR3 taxon 2488639 (GCA/GCF_020295565.1), Klebsiella pneumoniae isolate SR3 taxon 573 (GCA_022184225.1), Lacrimispora indolis SR3 taxon 1286820 and other explicitly different taxa. |

One full StrainInfo object required an additional authority check:
`data/straininfo/records.jsonl.gz:223570`, SI-ID 281626, lacks a taxon
but names its own NBRC 102833 / SI-DP 716984 and aliases SR3 / MBIC10597.
The inspected primary
[NBRC 102833 catalog](https://www.nite.go.jp/nbrc/catalogue/NBRCCatalogueDetailServlet?CAT=00102833&ID=NBRC)
identifies the deposit as LPP-group-B, class Cyanophyceae, explicitly
equates MBIC10597 with SR3 and describes a non-axenic culture. This
does not identify the reviewed Chryseobacterium strain. Its shared bare
alias supplies no permissible join, and no community member was inferred.

Other inspected native fields identify SR3 names or longer designations
in Enterococcus, Photobacterium, Lacticaseibacillus, Ligilactobacillus,
Peribacillus, Salmonella and several other genera. These projections
exclude unrelated source identities; they are not full reviews of those
records' biological claims.

GOLD's organism identities include Lacrimispora/Clostridium SR3,
Go0032983, Pectobacterium atrosepticum Go0252814 and Cryobacterium
Go0533264. Its raw Go0032983 / Gp0032983 / Ga0002391 chain explicitly
matches ATCC 700855 and taxon 1286820, not this record.
Four environmental projects were read in full at
`data/gold/projects.jsonl.gz:40779`, line 398149, line 472117 and
line 505416: Gp0061086, Gp0543433, Gp0631373 and Gp0674087.
They describe macroalgal-surface, bioreactor, forest-soil and sediment
communities, with no organism GOLD IDs. The corresponding full
Ga0011295, Ga0484309 and Ga0555681 objects explicitly describe
metagenome analyses. Neither environmental SR3 labels nor shared
source grouping identify a Chryseobacterium deposit.

Complete ignored-inclusive ID/label/slug/SR3 searches additionally
covered `data/atb/`, the full `data/catalog/allthebacteria.tsv.xz`
and StrainInfo link, assembly, exclusion and compressed related-record
tables. Full ATB rows identify Lacrimispora SR3 samples SAMEA9956914
(catalog line 994067) and SAMN02440585 (line 1029470; compact assembly
line 2759). The two genome-link rows at `data/atb/genome_links.tsv:11494`
and line 11495 explicitly belong to BacDive 168170, ATCC 700855,
taxon 1286820 and the GOLD chain above. Their shared-BioSample relation
is neither target identity nor genome equivalence. No eligible
Chryseobacterium deposit/BioSample chain was established.

Empty optional fields are justified at the checked source boundary,
not proof that no isolates or sequences exist elsewhere. No gene,
regulator, pathway, trait or transcriptomic assertion is present;
iModulonDB is not applicable. No graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Retain the supported backbone and `SEEDED` status.
Future enrichment belongs in maintained extraction inputs or
`src/taxonmech/extract.py`, with seeding changes in
`src/taxonmech/seed.py` and regression tests. Do not patch generated
YAML or transfer sibling designations, bare SR3 aliases, type flags,
genomes or community samples across different taxa.

## Follow-up Checks

No finding-specific check remains. New links require exact target
identity and explicit primary deposit/sample provenance. Authorized
future changes should use documented dry-run/canary steps and both
focused validators after regeneration. Corpus-wide claims additionally
require `just verify-corpus` and full QC, not run in this focused review.

## Additional Notes

Absence checks included ignored files via full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All search and validator
processes completed. Public NCBI metadata reads used network escalation
after established sandbox DNS failures. NBRC was inspected directly;
search snippets alone were not used to resolve its culture identity.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, earlier report, history or
status was changed. No generator, refresh, paid research, GitHub action
or cross-repository write occurred. Eukaryota was not re-reviewed.
