# YAML Record Review: Staphylococcus aureus M1466

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_aureus_m1466.yaml`
- Started UTC: 2026-10-03T15:56:11Z
- Finished UTC: 2026-10-03T15:57:50Z
- Verdict: needs curation

## Target

The whole generated `TaxonRecord` was read before judgement. It denotes
`NCBITaxon:1303787`, strain M1466, domain `BACTERIA`, parent
`NCBITaxon:1280`, genetic code 11. Grounding is `EXACT`, status
`SEEDED`. There are ten lineage entries, one GTDB mapping, one GTDB exact
synonym, one equivalence xref, three attestations and one seed event.
Strain count is zero. No strain list, genome links, nomenclature,
experimental claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_aureus_m1466.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_aureus_m1466.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison reproduces rank, parent,
  genetic code and all ten lineage entries. No children occur under this
  target. Full exact-field inventory scans reproduce GTDB and Madin
  rows; no direct BacDive, LPSN, GOLD, MediaDive or BactoTraits taxon
  inventory membership was found.
- A fresh complete GTDB genome-shard census finds 19,502 distinct
  accessions across 4,209 source taxon IDs for the exact species; one
  member has taxon 1303787. Counts do not prove equivalence.
- `just verify-corpus`: Not checked; full-corpus-only, with no focused
  substitute invented. Full QC, global provenance, generated products,
  exports and genome sequences were not audited.
- Ignored-inclusive history searches found no target standalone entry.
  Standalone history validation had no target; strict validation checked
  the embedded seed event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308143` and the full native name object
at `data/catalog/ncbi_names-0007.jsonl.gz:30690` support exact strain
identity and empty NCBI synonym fields. The PATHS index has one target
row for this identifier/slug.

The NCBI browser page was inaccessible through the web tool. Current
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303787&retmode=xml)
confirms ID, label, strain rank, Bacteria division, parent 1280, genetic
code 11 and the full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303787)
confirms rank and all ten ancestor IDs including root. Read-only public
API calls used network escalation after sandbox DNS failure had already
been established. NCBI grounding is supported.

The current NCBI backbone uses Caryophanales. Native BV-BRC/GTDB NCBI
fields retain older Bacillales, and GTDB's own taxonomy uses
Staphylococcales. Preserve these source distinctions, not a reconciled
lineage. Species-level GTDB equivalence is separate and unsupported.

## Evidence

| Assertion | Inspected source | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308143` | Exact identity; snapshot 2026-09-13 |
| GTDB 19502 GENOME | `data/raw/gtdb_mappings.tsv:17475`; `gtdb_species.tsv:168198` | Species-cluster count, not M1466 count |
| MADIN 2 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11840` | Count reproduced; no named trait claimed |

Scope row `curation/seed_scope.tsv:42165` admits this taxon on
2026-09-12 with three sources. The 2026-09-13T17:54:04Z embedded
seed event matches that reason and those sources without claiming human
review. Counts with different units must not be combined.

The exact-terminal GTDB census selects `s__Staphylococcus aureus`,
excluding aureus_A. The only target-classified member is
RS_GCF_000364145.1, whose complete object at
`data/catalog/gtdb_genomes-0002.jsonl.gz:43230` preserves strain
M1466, taxon 1303787, GCA_000364145.1 and SAMN02596942. The
representative at `data/catalog/gtdb_genomes-0006.jsonl.gz:29983`
is instead RS_GCF_001027105.1, DSM 20231, taxon 1280. The GTDB
taxon-page request in this turn was inaccessible; pinned primary
metadata establish cluster scope and target membership.

Complete native NCBI objects at `data/catalog/ncbi_genbank-0000.jsonl.gz:10019`
and `data/catalog/ncbi_refseq-0000.jsonl.gz:8744` identify the identical
GCA/GCF_000364145.1 pair, assembly Stap_aure_M1466_V1, strain
M1466, taxon 1303787 and SAMN02596942. Both describe 38 contigs,
20 scaffolds and 2,967,356 bp including gaps. GenBank project
PRJNA192848 and RefSeq umbrella PRJNA224116 are distinct source
values. BV-BRC's full object at `data/bvbrc/bvbrc-0001.jsonl.gz:23833`
retains genome 1303787.3, GCA_000364145.1, PRJNA192848 and
the same strain/sample.

Complete primary GOLD objects at `data/gold/organisms.jsonl.gz:31296`,
`data/gold/projects.jsonl.gz:25171` and
`data/gold/analyses.jsonl.gz:11521` retain
Go0037003 -> Gp0037003 -> Ga0018146, IMG 2545824650,
GCA_000364145.1, PRJNA192848 and SAMN02596942. The organism's
culture field is empty; M1466 is a bare designation. Native GOLD
identity evidence does not supply a KGX-derived taxon count; these
different derivations remain separate.

## Completeness

Ignored-inclusive compressed searches used ID, M1466 and slug across
all JSONL shards under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/straininfo/` and `data/seqcode/`. Matching objects
were read in full. Unrelated matches were excluded:

- StrainInfo SI-ID324220 at `data/straininfo/records.jsonl.gz:250936`,
  Aspergillus nidulans taxon 162425, FGSC A391, SI-DP766658, alias M1466.
- Helicobacter pylori taxon 210, strain YN-M1466, GCA/GCF_019671975.1,
  SAMN19664461. Full objects at
  `data/catalog/ncbi_genbank-0018.jsonl.gz:3555` and
  `data/catalog/ncbi_refseq_historical-0000.jsonl.gz:43956` concern
  that organism, not this target; the historical RefSeq object is suppressed.
- Uncultured Candidatus Planktophila sp., taxon 878252,
  GCA_964576165.1, SAMEA117365110, in
  `data/catalog/ncbi_genbank-0063.jsonl.gz:32128` and
  `data/catalog/gtdb_genomes-0007.jsonl.gz:35780`. Its ungapped genome
  length is 1303787, not its taxon identity.

No target BacDive or StrainInfo native object was found in this bounded
search. The complete BacDive membership scan and singleton subtree
support strain count zero, not absence of genomes. Native target genome
metadata exist, but the documented model exposes links through supported
BacDive strain rows using direct source assertions or eligible culture
matches. Bare strain designations and taxon IDs are not culture-deposit
keys. Catalog-level genome representation is a separate modeling question;
do not fabricate strain rows or borrow unrelated deposit evidence.

Ignored-inclusive searches of raw strain assembly/genome/related tables,
StrainInfo link/assembly/exclusion tables and history found no target ID,
M1466 designation or slug. Compressed searches of `data/atb/` and the
complete `data/catalog/allthebacteria.tsv.xz`, also using SAMN02596942,
found no target/sample result. These misses concern pinned source scope.

No same-taxon LPSN inventory row supports nomenclature or type flags;
the parent's nomenclature must not be inherited. No DOI, PMID, gene,
regulator, pathway, named phenotype or transcriptomic dataset is asserted.
iModulonDB is not applicable. Two unspecified Madin assertions do not
establish an experimental phenotype or causal graph.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. The GTDB exact synonym
  and equivalence xref identify strain M1466 with
  `GTDB:s__Staphylococcus_aureus`, a 19,502-genome cluster containing
  many strains and only one target-classified member. Membership supports
  classification, not identity. `src/taxonmech/seed.py:451` treats
  `skos:closeMatch` as identity without rank/scope checks; lines 466-469
  emit the synonym/xref contrary to
  `src/taxonmech/schema/taxonmech.yaml:180`. Maintained fix owners are
  `src/taxonmech/seed.py` and `tests/test_seed.py`, with separate
  upstream kg-microbe predicate review. Count 19,502 is correct only
  at species-cluster scope, not as an M1466 genome count.
- Minor: None found.

## Recommended Edits

1. Make the maintained seeder's equivalence decision rank/scope-aware.
   Preserve GTDB classification and provenance while suppressing this
   unsupported exact synonym and equivalence xref. Explicitly scope the
   species-cluster count; do not replace it with 1 under unchanged semantics.
2. Add a strain/species regression in `tests/test_seed.py`, retaining
   supported same-scope mappings. Review kg-microbe's source predicate;
   do not hand-patch extracted TSVs or guess relation direction.
3. Follow authorized dry-run/canary/regeneration steps after fixing the
   maintained rule. Do not hand-edit YAML, invent culture joins or
   promote human review status.

## Follow-up Checks

Run the new regression with
`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, rerun both focused validators and inspect
retained classification, explicit count scope, suppressed unsupported
synonym/xref and unchanged NCBI identity. Repeat the exact-terminal
cluster/member census; run `just verify-corpus` and full QC. M1 remains
unresolved; this review did not implement the correction.

## Additional Notes

Absence checks included ignored files using full structured reads,
`find`, or `rg --no-ignore --hidden`, with `-z` for compressed sources.
The only manual write is this report; strict validation wrote its standard
diagnostic. No record, source, prior report, history or status was edited.
No generator, refresh, paid research, GitHub mutation or cross-repository
write occurred. No Eukaryota record was re-reviewed; unrelated native
objects were inspected only to exclude false matches.
