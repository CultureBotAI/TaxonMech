# YAML Record Review: Staphylococcus aureus M1060

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_aureus_m1060.yaml`
- Started UTC: 2026-10-03T15:38:17Z
- Finished UTC: 2026-10-03T15:39:30Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord` before judgement. The target is
`NCBITaxon:1303782`, rank `STRAIN`, domain `BACTERIA`, parent
`NCBITaxon:1280`, genetic code 11. Grounding is `EXACT`, mapping status
`SEEDED`. One GTDB mapping, one GTDB exact synonym, one equivalence
xref, three source attestations and one seed event are present. Strain
count is zero; no strains, genome links, nomenclature, experimental
claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_aureus_m1060.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_aureus_m1060.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison confirms identity, rank,
  parent, genetic code and all ten lineage entries. No target children
  occur in the pinned backbone.
- Full exact-field inventory scans reproduce the GTDB mapping and
  Madin count 2. No direct BacDive, LPSN, GOLD, MediaDive or BactoTraits
  taxon inventory membership was found.
- Fresh complete native GTDB census: 19,502 distinct species-cluster
  accessions, 4,209 taxon IDs, one target-classified member. Source-count
  reproduction does not establish species/strain equivalence.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, generated products,
  exports and genome sequences were not audited.
- Ignored-inclusive history searches found no target entry. Standalone
  history validation had no target; strict validation checked the embedded
  event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308138` and the complete native name object
at `data/catalog/ncbi_names-0007.jsonl.gz:30685` support the exact
Staphylococcus M1060 identity and empty NCBI synonym fields. The PATHS
index contains one target row with this slug.

The browser URL was inaccessible through the web tool. Inspected current
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303782&retmode=xml)
confirms ID, label, strain rank, Bacteria division, parent 1280, code
11 and complete non-root lineage without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303782)
confirms strain rank and all ten ancestor IDs including root. Read-only
API requests used network escalation after sandbox DNS failure had been
established in this session. NCBI grounding is supported.

The order Caryophanales is current NCBI placement. Older BV-BRC/GTDB
NCBI-lineage fields retain Bacillales, while GTDB's own hierarchy uses
Staphylococcales. Preserve those source distinctions without replacing
the NCBI backbone. The GTDB species equivalence remains unsupported.

## Evidence

| Assertion | Inspected inventory | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308138` | Exact identity; snapshot 2026-09-13 |
| GTDB 19502 GENOME | `data/raw/gtdb_species.tsv:168198`; `gtdb_mappings.tsv:17470` | Correct species-cluster count, not M1060 count |
| MADIN 2 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11835` | Count reproduced; no particular trait asserted |

The scope row at `curation/seed_scope.tsv:42160` admits this target on
2026-09-12 with three sources. The embedded 2026-09-13T17:54:04Z seed
event preserves that reason and the actual attesting sources. It does
not claim human review. Counts with different units must not be combined.

The census parsed every `gtdb_genomes-*.jsonl.gz` file for terminal
species exactly `s__Staphylococcus aureus`, excluding aureus_A. The
sole target-classified row is RS_GCF_000364045.1 at
`gtdb_genomes-0014.jsonl.gz:13325`, with M1060, sample SAMN02596937
and GenBank GCA_000364045.1. The complete representative object at
`gtdb_genomes-0006.jsonl.gz:29983` is RS_GCF_001027105.1, DSM 20231,
taxon 1280, not M1060. The shared GTDB taxon-page request in this
session was inaccessible; pinned primary metadata establish the broader
species scope and the single target member.

Complete NCBI native objects at `ncbi_genbank-0000.jsonl.gz:10014` and
`ncbi_refseq-0000.jsonl.gz:8739` retain GCA/GCF_000364045.1,
assembly Stap_aure_M1060_V1, strain M1060, taxon 1303782 and sample
SAMN02596937. They explicitly identify an identical GenBank/RefSeq pair,
scaffold level, 19 contigs, five scaffolds and 2,907,360 bp including
gaps. GenBank project PRJNA192843 and RefSeq umbrella PRJNA224116
remain separate source values. The complete BV-BRC object at
`data/bvbrc/bvbrc-0001.jsonl.gz:23828` supplies genome 1303782.3,
GCA_000364045.1, PRJNA192843 and the same strain/sample.

Primary GOLD retains Go0036997 -> Gp0036997 -> Ga0018167, with
GCA_000364045.1, IMG 2545824671, PRJNA192843 and SAMN02596937.
Complete objects are at `data/gold/organisms.jsonl.gz:31291`,
`projects.jsonl.gz:25166` and `analyses.jsonl.gz:11542`. The culture
field is empty, and the strain field is only M1060. Native GOLD chain
evidence does not create a KGX-derived taxon count; those derivations
remain separate under the documented current model.

## Completeness

Ignored-inclusive compressed searches by target ID, M1060 and slug
covered every `*.jsonl.gz` file under `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/`, `data/straininfo/` and `data/seqcode/`.
All matching native objects were inspected.

The search also found Mesorhizobium sp. M1060, taxon 2957052,
GCA/GCF_040318675.1, sample SAMN29272244, BV-BRC 2957052.3 and
GTDB RS_GCF_040318675.1. Those complete objects and their name record
refer to a different genus and taxon. They were excluded, not joined
by the shared M1060 designation. No target BacDive or StrainInfo native
object was found within this bounded search.

The full BacDive membership scan and singleton subtree support strain
count zero. Native genome data nevertheless exist. The current model
publishes genome assertions on source-supported BacDive strain entries
using direct assertions or eligible culture identifiers. Neither the
taxon ID nor bare M1060 establishes a culture-deposit join. Broader
native taxon-genome representation is a separate modeling question,
not permission to fabricate a strain row.

Ignored-inclusive searches of raw strain assembly/genome/related tables
and StrainInfo link/assembly/exclusion tables found no target ID, M1060
designation or slug. Compressed searches of `data/atb/` and the complete
`data/catalog/allthebacteria.tsv.xz`, additionally using SAMN02596937,
found no target/sample result. These misses are bounded to pinned sources.

No LPSN name maps directly to this strain. Optional nomenclature and
type flags need not be copied from the parent species. No DOI, PMID,
gene, locus, regulator, pathway, specific phenotype or transcriptomic
dataset is asserted; iModulonDB is not applicable. Two unspecified
Madin assertions do not establish an experiment or causal mechanism.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. The GTDB exact synonym
  and equivalence xref imply that all of `GTDB:s__Staphylococcus_aureus`
  is strain M1060. The 19,502-genome cluster contains many strains,
  with one target-classified member. Membership is not identity.
  `src/taxonmech/seed.py:451` treats `skos:closeMatch` as identity
  without rank/scope checks; lines 466-469 emit the unsupported exact
  synonym and xref. This violates the true-equivalence contract at
  `src/taxonmech/schema/taxonmech.yaml:180`. Owners are
  `src/taxonmech/seed.py` and `tests/test_seed.py`, with separate review
  of the upstream kg-microbe predicate. The count is correct for the
  species cluster, not this strain.
- Minor: None found.

## Recommended Edits

1. Make the maintained seeder's equivalence decision rank/scope-aware.
   Preserve GTDB classification and provenance while suppressing the
   unsupported species exact synonym/xref on this strain. Explicitly
   scope the genome count to its cluster; do not replace 19,502 with 1
   under unchanged species-count semantics.
2. Add a strain/species regression to `tests/test_seed.py`, retaining
   valid same-scope mappings. Review the source predicate in kg-microbe;
   do not patch extracted TSVs or guess predicate direction.
3. Follow an authorized dry-run/canary/regeneration workflow after the
   maintained fix. Do not hand-edit YAML, infer culture joins, merge
   the unrelated Mesorhizobium identity or promote human review status.

## Follow-up Checks

Run the new regression and `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, rerun both focused validators and inspect
the emitted YAML for retained classification, absent unsupported exact
synonym/xref, explicit count scope and unchanged NCBI identity. Repeat
the exact-terminal cluster census and target-member check. Run
`just verify-corpus` and full QC for regeneration. M1 remains unresolved;
this read-only review did not implement the corrective change.

## Additional Notes

Absence checks included ignored files using full structured reads,
`find`, or `rg --no-ignore --hidden`, with `-z` for compressed sources.
The only manual write is this report; strict validation wrote its
standard diagnostic. No YAML, source, prior report, history or status
was edited. No generator, refresh, paid research, GitHub mutation or
cross-repository write occurred. Eukaryota was not re-reviewed.
