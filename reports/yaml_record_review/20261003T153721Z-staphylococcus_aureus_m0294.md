# YAML Record Review: Staphylococcus aureus M0294

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_aureus_m0294.yaml`
- Started UTC: 2026-10-03T15:35:55Z
- Finished UTC: 2026-10-03T15:37:21Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303781`, rank `STRAIN`, domain `BACTERIA`, parent
`NCBITaxon:1280`, genetic code 11. Grounding is `EXACT`, mapping status
`SEEDED`. One GTDB mapping, one GTDB exact synonym, one equivalence
xref, three source attestations and one seed event are present. Strain
count is zero. No strains, genome links, nomenclature, experimental
evidence or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_aureus_m0294.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_aureus_m0294.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone read confirms identity, rank, parent,
  code and all ten lineage entries. No target children occur in the
  pinned backbone.
- Full exact-field scans reproduce the GTDB mapping and Madin count 2.
  No direct BacDive, LPSN, GOLD, MediaDive or BactoTraits taxon inventory
  membership was found.
- A fresh complete GTDB native census confirms 19,502 distinct species
  cluster accessions across 4,209 source taxon IDs. One row has target
  ID 1303781. Count reproduction does not establish equivalence.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, rendered products,
  exports and genome sequences were not audited.
- Ignored-inclusive history searches found no target entry. Standalone
  history validation had no target; strict validation checked the embedded
  event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308137` and the complete native name object
at `data/catalog/ncbi_names-0007.jsonl.gz:30684` support the exact
M0294 identity and empty NCBI synonym fields. The PATHS index contains
one target row with this slug.

The browser URL was inaccessible through the web tool. Inspected current
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303781&retmode=xml)
confirms ID, label, strain rank, Bacteria division, parent 1280, code
11 and full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303781)
also confirms strain rank and all ten ancestor IDs including root.
Read-only API calls used network escalation after sandbox DNS failure
had been established in this session. NCBI grounding is supported.

Current NCBI order Caryophanales is correctly retained. Older native
BV-BRC/GTDB NCBI fields say Bacillales; GTDB's own hierarchy says
Staphylococcales. Those source differences must not override NCBI's
backbone or be silently reconciled. The additional GTDB species
equivalence remains unsupported.

## Evidence

| Assertion | Inspected inventory | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308137` | Exact identity; snapshot 2026-09-13 |
| GTDB 19502 GENOME | `data/raw/gtdb_species.tsv:168198`; `gtdb_mappings.tsv:17469` | Correct species-cluster count, not M0294 count |
| MADIN 2 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11834` | Count reproduced; no particular trait asserted |

The scope row at `curation/seed_scope.tsv:42159` admits the target on
2026-09-12 with three sources. The embedded 2026-09-13T17:54:04Z event
preserves that reason and the actual source names, without claiming
human review. Different assertion units must not be combined.

All `gtdb_genomes-*.jsonl.gz` files were parsed for terminal taxonomy
exactly `s__Staphylococcus aureus`, excluding the separate aureus_A
cluster. The sole target-classified member is RS_GCF_000364025.1 at
`gtdb_genomes-0009.jsonl.gz:15056`, with M0294, SAMN02596936 and
GCA_000364025.1. The complete representative object at
`gtdb_genomes-0006.jsonl.gz:29983` is RS_GCF_001027105.1, DSM 20231,
taxon 1280, not M0294. The shared GTDB taxon-page attempt in this
session was inaccessible. Inspected pinned primary metadata establish
species-cluster scope and the rank mismatch.

Complete native NCBI objects at `ncbi_genbank-0000.jsonl.gz:10013` and
`ncbi_refseq-0000.jsonl.gz:8738` supply GCA/GCF_000364025.1,
assembly Stap_aure_M0294_V1, strain M0294, taxon 1303781 and sample
SAMN02596936. They explicitly identify an identical GenBank/RefSeq pair,
scaffold level, 27 contigs, ten scaffolds and 2,914,242 bp including
gaps. GenBank PRJNA192842 and RefSeq umbrella PRJNA224116 remain
distinct source projects. BV-BRC's complete object at
`data/bvbrc/bvbrc-0001.jsonl.gz:23827` retains genome 1303781.3,
GCA_000364025.1, PRJNA192842 and the same strain/sample.

Primary GOLD retains Go0036996 -> Gp0036996 -> Ga0018150, with
GCA_000364025.1, IMG 2545824654, PRJNA192842 and SAMN02596936.
The complete objects are at `data/gold/organisms.jsonl.gz:31290`,
`projects.jsonl.gz:25165` and `analyses.jsonl.gz:11525`. The organism
has an empty culture field and only the bare strain designation M0294.
This primary chain is distinct from the absent KGX-derived GOLD taxon
count; it does not authorize inventing a source attestation.

## Completeness

Ignored-inclusive compressed searches using target ID, M0294 and slug
covered every `*.jsonl.gz` file under `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/`, `data/straininfo/` and `data/seqcode/`.
All hits were inspected. No target BacDive or StrainInfo native object
was found within this bounded search.

Complete BacDive membership and singleton-subtree checks support strain
count zero, not genome absence. Native genome data exist, but the current
model publishes genome assertions on source-supported BacDive strains
through direct evidence or eligible culture-deposit matches. A bare
M0294 name or taxon ID is not a culture key. Native taxon-level genome
representation would be a separate modeling change, not a YAML patch.

Ignored-inclusive searches of raw strain assembly/genome/related tables
and StrainInfo link/assembly/exclusion tables found no target ID, M0294
designation or slug. Compressed searches of `data/atb/` and the full
`data/catalog/allthebacteria.tsv.xz`, additionally using SAMN02596936,
found no target/sample result. These are bounded pinned-source misses.

No LPSN name maps directly to this strain. Optional nomenclature and type
flags must not be copied from the parent species. No DOI, PMID, gene,
locus, regulator, pathway, specific phenotype or transcriptomic dataset
is asserted; iModulonDB is not applicable. Two unspecified Madin
assertions do not establish an experimental claim or causal mechanism.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. The exact GTDB synonym
  and equivalence xref imply that `GTDB:s__Staphylococcus_aureus` is
  M0294. The 19,502-genome cluster spans many strains, with one
  target-classified member; membership is not identity.
  `src/taxonmech/seed.py:451` treats `skos:closeMatch` as identity
  without rank/scope checks, and lines 466-469 emit the unsupported
  exact synonym and xref. This conflicts with the true-equivalence
  contract at `src/taxonmech/schema/taxonmech.yaml:180`. Maintained
  owners are `src/taxonmech/seed.py` and `tests/test_seed.py`, with
  separate review of the upstream kg-microbe predicate. The count is
  valid only at species-cluster scope.
- Minor: None found.

## Recommended Edits

1. Make equivalence generation in `src/taxonmech/seed.py` rank/scope-aware.
   Retain classification and provenance while suppressing the unsupported
   species exact synonym/xref for this strain. Label the count as
   species-cluster scope; do not replace 19,502 with 1 under unchanged
   species-count semantics.
2. Add a regression in `tests/test_seed.py` while retaining supported
   same-scope mappings. Review kg-microbe's source predicate separately;
   do not hand-patch extracted TSVs or guess predicate direction.
3. Follow authorized dry-run/canary/regeneration steps after fixing the
   maintained rule. Do not hand-edit YAML, infer culture joins, overwrite
   NCBI lineage or promote human review status.

## Follow-up Checks

Run the new regression and `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, rerun both focused validators and inspect
the actual YAML for retained classification, absent unsupported exact
synonym/xref, explicit count scope and unchanged NCBI identity. Repeat
the exact-terminal GTDB census and target-member check. Run
`just verify-corpus` and full QC for the regeneration. M1 remains
unresolved; this read-only review made no corrective change.

## Additional Notes

Absence checks included ignored files through complete structured reads,
`find`, or `rg --no-ignore --hidden`, with `-z` for compressed sources.
The only manual write is this report; strict validation wrote its
standard diagnostic. No YAML, source, prior report, history or status
was edited. No generator, refresh, paid research, GitHub mutation or
cross-repository write occurred. Eukaryota was not re-reviewed.
