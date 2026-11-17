# YAML Record Review: Staphylococcus aureus M0075

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_aureus_m0075.yaml`
- Started UTC: 2026-10-03T15:33:23Z
- Finished UTC: 2026-10-03T15:35:00Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord` before judgement. Identity is
`NCBITaxon:1303780`, rank `STRAIN`, domain `BACTERIA`, parent
`NCBITaxon:1280`, genetic code 11. Grounding is `EXACT` and mapping
status `SEEDED`. One GTDB mapping, one GTDB exact synonym, one
equivalence xref, three source attestations and one embedded seed event
are present. Strain count is zero; no strains, genome links,
nomenclature, experimental claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_aureus_m0075.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_aureus_m0075.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison confirms identity, rank,
  parent, genetic code and all ten lineage entries. No target children
  occur in the pinned backbone.
- Complete exact-field inventory scans reproduce the GTDB mapping and
  Madin count 2. No direct BacDive, LPSN, GOLD, MediaDive or BactoTraits
  taxon inventory membership was found.
- Complete native GTDB census confirms 19,502 distinct cluster genomes
  across 4,209 source taxon IDs, with one target-classified member.
  Reproduction of the count does not establish strain/species identity.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, generated products,
  exports and genome sequences were not audited.
- Ignored-inclusive history searches found no target entry. Standalone
  history validation had no target; strict validation checked the embedded
  event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308136` and the complete native name object
at `data/catalog/ncbi_names-0007.jsonl.gz:30683` support the exact
M0075 identity and empty NCBI synonym fields. The PATHS index resolves
this identifier to exactly one slug.

The browser URL was inaccessible through the web tool. Initial sandboxed
API requests failed DNS resolution; subsequent read-only escalated calls
succeeded. Inspected current
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303780&retmode=xml)
confirms the exact label, strain rank, Bacteria division, parent 1280,
code 11 and full non-root lineage, with no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303780)
confirms strain rank and all ten ancestor IDs including root.

The record correctly carries current NCBI order Caryophanales. Older
BV-BRC/GTDB NCBI-lineage fields say Bacillales, and GTDB's own hierarchy
uses Staphylococcales. These source classifications remain distinct;
neither replaces the NCBI backbone. Exact NCBI grounding is supported,
but equivalence to the entire GTDB species is not.

## Evidence

| Assertion | Inspected inventory | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308136` | Exact identity; snapshot 2026-09-13 |
| GTDB 19502 GENOME | `data/raw/gtdb_species.tsv:168198`; `gtdb_mappings.tsv:17468` | Correct species-cluster count, not M0075 count |
| MADIN 2 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11833` | Count reproduced; no specific trait asserted |

`curation/seed_scope.tsv:42158` admits the target on 2026-09-12 with
three sources. The 2026-09-13T17:54:04Z seed event preserves that reason
and the actual source names. It does not claim human review. Units
must not be summed across sources.

The GTDB census parsed every `gtdb_genomes-*.jsonl.gz` file, selecting
terminal species exactly `s__Staphylococcus aureus`; the distinct
`s__Staphylococcus aureus_A` cluster was not counted. Only
RS_GCF_000364005.1 carries target taxon 1303780. Its complete object
at `gtdb_genomes-0003.jsonl.gz:11507` records M0075, sample
SAMN02596935 and GCA_000364005.1. The representative is
RS_GCF_001027105.1, DSM 20231, source taxon 1280
(`gtdb_genomes-0006.jsonl.gz:29983`). Other cluster members include
LCT-SAS, H87668 and M1051. The GTDB web page was inaccessible; pinned
primary metadata establish species scope, not snippets or name similarity.

Complete native NCBI objects at `ncbi_genbank-0000.jsonl.gz:10012` and
`ncbi_refseq-0000.jsonl.gz:8737` retain GCA/GCF_000364005.1,
assembly Stap_aure_M0075_V1, strain M0075, taxon 1303780 and sample
SAMN02596935. They explicitly identify an identical GenBank/RefSeq pair,
scaffold level, 16 contigs, five scaffolds and 2,871,499 bp including
gaps. GenBank project PRJNA192841 and RefSeq umbrella PRJNA224116
remain distinct source values. The complete BV-BRC object at
`data/bvbrc/bvbrc-0001.jsonl.gz:23826` supplies genome 1303780.3,
GCA_000364005.1, PRJNA192841 and the same strain/sample.

Native GOLD retains the explicit chain Go0036995 -> Gp0036995 ->
Ga0018156 with GCA_000364005.1, IMG 2545824660, PRJNA192841 and
SAMN02596935. Its objects are at `data/gold/organisms.jsonl.gz:31289`,
`projects.jsonl.gz:25164` and `analyses.jsonl.gz:11531`. The organism's
culture field is empty; M0075 is a bare strain designation. This native
chain does not supply a missing KGX-derived GOLD taxon count: those are
separate derivations under the documented current model.

## Completeness

Ignored-inclusive compressed ID, M0075 and slug searches covered every
`*.jsonl.gz` file under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/straininfo/` and `data/seqcode/`. All matching objects
were inspected. No target BacDive or StrainInfo native object was found
within that bounded search.

The complete BacDive membership scan and singleton subtree support strain
count zero. This is not genome absence: native NCBI, GTDB, BV-BRC and
GOLD records explicitly contain genome data. The current model publishes
genome assertions on source-supported BacDive strains, through direct
assertions or eligible culture-deposit matches. A taxon ID or bare M0075
designation does not establish a culture join. Broader native taxon-genome
representation is a separate modeling question, not a YAML patch.

Ignored-inclusive searches of raw strain assembly/genome/related tables
and StrainInfo link/assembly/exclusion tables found no target ID, M0075
designation or slug. Compressed searches of `data/atb/` and the complete
`data/catalog/allthebacteria.tsv.xz`, additionally using SAMN02596935,
found no target/sample result. These are bounded pinned-source misses.

No same-taxon LPSN name is mapped. Optional nomenclature and type flags
need not be inherited from the parent species. No DOI, PMID, gene, locus,
regulator, pathway, particular phenotype or transcriptomic dataset is
asserted; iModulonDB is not applicable. Two unspecified Madin assertions
do not support a mechanism, and no causal graph needs to be invented.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. The GTDB exact synonym
  and equivalence xref imply that all of `GTDB:s__Staphylococcus_aureus`
  is M0075. The 19,502-member cluster spans many strains, with only one
  target-classified member. Classification is not identity.
  `src/taxonmech/seed.py:451` accepts `skos:closeMatch` as identity
  without rank/scope checks; lines 466-469 emit the unsupported synonym
  and xref. This violates the true-equivalence contract at
  `src/taxonmech/schema/taxonmech.yaml:180`. Maintained owners are
  `src/taxonmech/seed.py` and `tests/test_seed.py`, with separate review
  of the upstream kg-microbe predicate. The count is correct only at
  species-cluster scope.
- Minor: None found.

## Recommended Edits

1. Make the seeder's equivalence rule rank/scope-aware. Retain the GTDB
   classification and provenance, but suppress the unsupported species
   exact synonym and xref for this strain. Explicitly scope the genome
   count to its cluster; do not replace 19,502 with 1 under unchanged
   species-count semantics.
2. Add a strain/species regression to `tests/test_seed.py`, preserving
   valid same-scope mappings. Review kg-microbe's source predicate;
   do not hand-patch extracted TSVs or guess predicate direction.
3. Follow an authorized dry-run/canary/regeneration workflow after the
   maintained fix. Do not hand-edit YAML, infer culture joins or promote
   human review status. Preserve the NCBI lineage and source distinctions.

## Follow-up Checks

Run the new regression and `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, rerun both focused validators and inspect
the emitted record for retained GTDB classification, absent unsupported
exact synonym/xref, explicit count scope and unchanged NCBI identity.
Repeat the exact-terminal cluster census and target-member check. Run
`just verify-corpus` and full QC for the regeneration. M1 remains
unresolved; this review did not implement the fix.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find`, or `rg --no-ignore --hidden`, with `-z` for compressed sources.
The only manual write is this new report; strict validation produced
its standard diagnostic. No YAML, source, prior report, history or
status was edited. No generator, refresh, paid research, GitHub mutation
or cross-repository write occurred. Eukaryota was not re-reviewed.
