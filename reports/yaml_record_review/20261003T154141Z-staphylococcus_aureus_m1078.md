# YAML Record Review: Staphylococcus aureus M1078

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_aureus_m1078.yaml`
- Started UTC: 2026-10-03T15:40:25Z
- Finished UTC: 2026-10-03T15:41:41Z
- Verdict: needs curation

## Target

Read the complete generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303783`, rank `STRAIN`, domain `BACTERIA`, parent
`NCBITaxon:1280`, genetic code 11. Grounding is `EXACT` and mapping
status `SEEDED`. One GTDB mapping, one GTDB exact synonym, one
equivalence xref, three source attestations and one seed event are
present. Strain count is zero. No strains, genome links, nomenclature,
experimental claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_aureus_m1078.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_aureus_m1078.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison confirms identity, rank,
  parent, genetic code and all ten lineage entries. The pinned backbone
  has no children under this target.
- Full exact-field scans reproduce the GTDB mapping and Madin count 2;
  no direct BacDive, LPSN, GOLD, MediaDive or BactoTraits taxon inventory
  membership was found.
- A fresh complete GTDB census confirms 19,502 distinct species-cluster
  accessions across 4,209 source taxon IDs. One member has target taxon
  1303783. Count reproduction does not establish equivalence.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, generated products,
  exports and genome sequences were not audited.
- Ignored-inclusive history searches found no target entry. Standalone
  history validation had no target; strict validation checked the embedded
  event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308139` and the complete native name object
at `data/catalog/ncbi_names-0007.jsonl.gz:30686` support this exact
Staphylococcus M1078 identity and empty NCBI synonym fields. The PATHS
index has exactly one target row with this slug.

The browser URL was inaccessible through the web tool. Inspected current
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303783&retmode=xml)
confirms ID, label, strain rank, Bacteria division, parent 1280, code
11 and full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303783)
confirms strain rank and all ten ancestor IDs including root. Read-only
public API calls used network escalation after sandbox DNS failure was
established in this session. NCBI grounding is supported.

The record retains current NCBI order Caryophanales. Older native
BV-BRC/GTDB NCBI fields use Bacillales, and GTDB's own taxonomy uses
Staphylococcales. Those source hierarchies remain distinct and do not
override the NCBI backbone. The species-level GTDB equivalence is not
supported by strain membership.

## Evidence

| Assertion | Inspected inventory | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308139` | Exact identity; snapshot 2026-09-13 |
| GTDB 19502 GENOME | `data/raw/gtdb_species.tsv:168198`; `gtdb_mappings.tsv:17471` | Correct species-cluster count, not M1078 count |
| MADIN 2 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11836` | Count reproduced; no particular trait asserted |

The scope row at `curation/seed_scope.tsv:42161` admits this taxon on
2026-09-12 with three sources. The 2026-09-13T17:54:04Z embedded seed
event preserves that reason and the actual source names without claiming
human review. Counts with different units must not be combined.

The census parsed every `gtdb_genomes-*.jsonl.gz` file for terminal
species exactly `s__Staphylococcus aureus`, excluding aureus_A. Only
RS_GCF_000364065.1 carries taxon 1303783. Its complete object at
`gtdb_genomes-0005.jsonl.gz:14549` retains M1078, SAMN02596938 and
GCA_000364065.1. The representative object at
`gtdb_genomes-0006.jsonl.gz:29983` is RS_GCF_001027105.1, DSM 20231,
taxon 1280, not M1078. The shared GTDB taxon-page request in this
session was inaccessible; pinned primary metadata establish the cluster
scope and target membership.

Complete NCBI native objects at `ncbi_genbank-0000.jsonl.gz:10015` and
`ncbi_refseq-0000.jsonl.gz:8740` supply GCA/GCF_000364065.1,
assembly Stap_aure_M1078_V1, strain M1078, taxon 1303783 and sample
SAMN02596938. They explicitly identify an identical GenBank/RefSeq pair,
scaffold level, 26 contigs, six scaffolds and 2,882,239 bp including
gaps. GenBank project PRJNA192844 and RefSeq umbrella PRJNA224116
remain distinct source values. BV-BRC's complete object at
`data/bvbrc/bvbrc-0001.jsonl.gz:23829` retains genome 1303783.3,
GCA_000364065.1, PRJNA192844 and the same strain/sample.

Primary GOLD retains Go0036998 -> Gp0036998 -> Ga0018161, with
GCA_000364065.1, IMG 2545824665, PRJNA192844 and SAMN02596938.
The complete objects are at `data/gold/organisms.jsonl.gz:31292`,
`projects.jsonl.gz:25167` and `analyses.jsonl.gz:11536`. The organism
has an empty culture field and only bare designation M1078. Native
primary-chain evidence does not supply a KGX-derived GOLD taxon count;
those derivations remain separate under the documented model.

## Completeness

Ignored-inclusive compressed searches by target ID, M1078 and slug
covered all `*.jsonl.gz` files under `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/`, `data/straininfo/` and `data/seqcode/`.
Matching native objects were read in full. Unrelated hits were excluded:

- Mesorhizobium sp. M1078, taxon 2957055, GCA/GCF_040318615.1,
  sample SAMN29272247 and BV-BRC 2957055.3. Its name, assembly, GTDB
  and BV-BRC objects describe a different genus and taxon.
- `data/straininfo/records.jsonl.gz:265827`, SI-ID339118 and deposit
  SI-DP791363 (FGSC A186), describes Aspergillus nidulans taxon 162425.
  Its M1078 alias is not evidence for this bacterial strain.
- `data/catalog/gtdb_genomes-0005.jsonl.gz:44155`, RS_GCF_947494625.1,
  describes an uncultured Litoreibacter taxon 1392394. The number
  1303783 is a contig N50 value, not its taxon identity.

No target BacDive or StrainInfo native object was found in this bounded
search. The complete BacDive membership scan and singleton subtree
support strain count zero, not a lack of genomes. Native target genome
data exist, but the current model publishes them on source-supported
BacDive strain rows using direct assertions or eligible culture matches.
A bare designation or taxon ID is not a culture-deposit join key.
Native taxon-level genome representation is a separate modeling question,
not permission to fabricate a strain row or copy an unrelated deposit.

Ignored-inclusive searches of raw strain assembly/genome/related tables
and StrainInfo link/assembly/exclusion tables found no target ID, M1078
designation or slug. Compressed searches of `data/atb/` and the complete
`data/catalog/allthebacteria.tsv.xz`, additionally using SAMN02596938,
found no target/sample result. These misses are bounded to pinned sources.

There is no same-taxon LPSN inventory mapping. Optional nomenclature and
type flags must not be inherited from the parent species. No DOI, PMID,
gene, locus, regulator, pathway, particular phenotype or transcriptomic
dataset is asserted; iModulonDB is not applicable. Two unspecified Madin
assertions do not establish an experiment or causal graph.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. The GTDB exact synonym
  and equivalence xref make `GTDB:s__Staphylococcus_aureus` appear
  identical to strain M1078. The species cluster contains 19,502 genomes
  spanning many strains, with one target-classified member. Membership
  supports classification, not identity. `src/taxonmech/seed.py:451`
  accepts `skos:closeMatch` as identity without rank/scope checks;
  lines 466-469 emit the unsupported synonym and xref, contrary to
  `src/taxonmech/schema/taxonmech.yaml:180`. Owners are
  `src/taxonmech/seed.py` and `tests/test_seed.py`, with separate review
  of kg-microbe's source predicate. The count is correct at cluster
  scope, not as a count of M1078 genomes.
- Minor: None found.

## Recommended Edits

1. Make the maintained seeder's equivalence decision rank/scope-aware.
   Preserve GTDB classification and provenance while suppressing the
   unsupported species exact synonym/xref for this strain. Explicitly
   scope the count to the species cluster; do not replace 19,502 with 1
   while retaining species-count semantics.
2. Add a strain/species regression in `tests/test_seed.py`, preserving
   supported same-scope mappings. Review the upstream predicate in
   kg-microbe; do not hand-patch extracted TSVs or guess relation direction.
3. Follow authorized dry-run/canary/regeneration steps after fixing the
   maintained rule. Do not hand-edit YAML, merge name-only matches,
   invent culture joins or promote human review status.

## Follow-up Checks

Run the new regression and `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, rerun both focused validators and inspect
the emitted record for retained classification, absent unsupported exact
synonym/xref, explicit count scope and unchanged NCBI identity. Repeat
the exact-terminal GTDB census and target-member check. Run
`just verify-corpus` and full QC for regeneration. M1 remains unresolved;
this report did not implement a corrective change.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find`, or `rg --no-ignore --hidden`, with `-z` for compressed sources.
The only manual write is this report; strict validation wrote its
standard diagnostic. No YAML, source, prior report, history or status
was edited. No generator, refresh, paid research, GitHub mutation or
cross-repository write occurred. No Eukaryota record was re-reviewed.
