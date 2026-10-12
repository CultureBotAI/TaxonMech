# YAML Record Review: Enterococcus faecium E525

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enterococcus_faecium_e525.yaml`
- Started UTC: 2026-10-03T15:28:00Z
- Finished UTC: 2026-10-03T15:29:12Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord` before judgement. The target is
`NCBITaxon:1303770`, rank `STRAIN`, domain `BACTERIA`, parent
`NCBITaxon:1352`, genetic code 11. Grounding is `EXACT`, mapping status
`SEEDED`. There is one GTDB mapping, one GTDB exact synonym, one
equivalence xref, three source attestations and one embedded seed event.
Strain count is zero. No strains, genome links, nomenclature,
experimental claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/enterococcus_faecium_e525.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/enterococcus_faecium_e525.yaml`:
  PASS; one file scanned, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison confirms identity, rank,
  parent, genetic code and all ten lineage entries. The pinned backbone
  has no children under this target.
- Full exact-field inventory scans reproduce the GTDB mapping and Madin
  count 4; no direct BacDive, LPSN, GOLD, MediaDive or BactoTraits taxon
  inventory membership was found.
- A fresh full native GTDB census confirms 4,800 distinct species-cluster
  accessions across 353 source taxon IDs, with only one target-classified
  row. Reproducing the source count does not validate equivalence.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Global provenance, generated products,
  exports and genome sequences were not audited.
- Ignored-inclusive history searches found no target entry; standalone
  history validation had no target. Strict validation checked the embedded
  event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308134` and the complete scientific-name
object at `data/catalog/ncbi_names-0007.jsonl.gz:30681` support the
exact E525 identity and empty NCBI synonym fields. The PATHS index
contains exactly one target row for this slug.

The browser URL was inaccessible through the web tool. Inspected current
[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303770&retmode=xml)
confirms the ID, exact label, strain rank, Bacteria division, parent
1352, code 11 and complete non-root lineage with no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303770)
also confirms strain rank and all ten ancestor IDs including root.
Read-only public API calls used network escalation after sandbox DNS
failure was established in this session. NCBI grounding is supported;
the additional GTDB species equivalence is not.

## Evidence

| Assertion | Inspected inventory | Assessment |
| --- | --- | --- |
| NCBI 1 NAME | `data/raw/ncbitaxon_taxa.tsv:308134` | Exact ID and label; snapshot 2026-09-13 |
| GTDB 4800 GENOME | `data/raw/gtdb_species.tsv:58284`; `gtdb_mappings.tsv:17466` | Species-cluster count, not an E525 count |
| MADIN 4 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:11831` | Count reproduced; no specific trait asserted |

`curation/seed_scope.tsv:42156` admits the target on 2026-09-12 with
three sources. The 2026-09-13T17:54:04Z seed event preserves that reason
and the actual source names without claiming human review. Counts of
different units must not be combined.

The census parsed all `gtdb_genomes-*.jsonl.gz` files and selected the
terminal species exactly `s__Enterococcus_B faecium`. Only
RS_GCF_000477575.1 has target taxon 1303770; its complete source object
at `gtdb_genomes-0010.jsonl.gz:39042` specifies E525, sample
SAMN02471505, GenBank GCA_000477575.1 and source strain field E525.
The cluster representative RS_GCF_029023785.1 is DSM 20477, taxon 1352,
not E525 (`gtdb_genomes-0004.jsonl.gz:21353`). Many other strains are
members. The shared GTDB taxon-page request in this review session was
inaccessible; inspected pinned primary metadata establish the scope.

Complete native objects at `ncbi_genbank-0000.jsonl.gz:15200` and
`ncbi_refseq-0000.jsonl.gz:12778` preserve GCA/GCF_000477575.1,
assembly EfmE525_v1.0, strain E525, sample SAMN02471505 and taxon
1303770. They explicitly identify an identical GenBank/RefSeq pair,
contig level, 539 contigs and 2,904,426 bp. GenBank project PRJNA192893
and RefSeq umbrella PRJNA224116 remain distinct source values.
The complete BV-BRC object at `data/bvbrc/bvbrc-0001.jsonl.gz:23824`
retains genome 1303770.3, GCA_000477575.1, PRJNA192893 and the same
strain/sample; its culture-collection field is blank.

Primary GOLD objects preserve Go0036861 -> Gp0036861 -> Ga0032123,
with GCA_000477575.1, IMG 2565956809, PRJNA192893 and SAMN02471505.
Locations are `data/gold/organisms.jsonl.gz:31199`,
`projects.jsonl.gz:25045` and `analyses.jsonl.gz:22062`. The organism
has no culture-collection value and only the bare strain designation
E525. This native chain does not fabricate a KGX-derived GOLD taxon
attestation; the existing model keeps those derivations separate.

The assembly's PMID 23882129 resolves to DOI 10.1093/gbe/evt111 in the
[PubMed entry inspected this session](https://pubmed.ncbi.nlm.nih.gov/23882129/),
which lists AUWV00000000 among its associated sequences. The PMC
full-text request returned a browser challenge. No experimental claim
was imported from the abstract, and the YAML does not cite the paper.

## Completeness

Ignored-inclusive compressed searches covered all `*.jsonl.gz` files
under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/straininfo/` and `data/seqcode/`, using target ID, E525 and slug.
The E. coli isolate E525 assembly GCA_023038175.1 and Shewanella sp.
E525-6 name object were inspected and excluded as different identities.
No target BacDive or StrainInfo native object was found in that bounded
search. Bare designations must not be treated as culture identifiers.

The full BacDive membership scan and singleton subtree support strain
count zero. Genome data nevertheless exist in native catalogs. The
current model requires a supported BacDive strain association before
publishing strain-linked genome assertions; it does not join by taxon
or bare name. Missing taxon-level native genome representation is a
separate modeling question, not justification for a fabricated strain.

Ignored-inclusive searches of raw strain assembly/genome/related tables
and StrainInfo link/assembly/exclusion tables found no target ID, E525
designation or slug. Compressed searches of `data/atb/` and the complete
`data/catalog/allthebacteria.tsv.xz`, additionally using SAMN02471505,
found no target/sample result. The scope of these misses is the pinned
sources, not biological absence.

No LPSN name maps directly to this strain in the complete inventory.
Optional nomenclature and type flags need not be inherited from its
parent. No gene, locus, regulator, pathway, particular phenotype or
transcriptomic dataset is asserted, so iModulonDB is not applicable.
Four unspecified Madin assertions do not establish a causal mechanism.

## Findings

- Blocker: None found.
- Major M1: Species-to-strain scope inflation. The GTDB exact synonym
  and xref at YAML lines 46-51 imply that the whole
  `GTDB:s__Enterococcus_B_faecium` species is E525. The cluster contains
  4,800 genomes across many strains, with one target-classified member.
  Membership supports classification, not identity. The rule at
  `src/taxonmech/seed.py:451` accepts `skos:closeMatch` as identity
  without rank/scope checks, and lines 466-469 emit the unsupported exact
  synonym and xref. This conflicts with the true-equivalence contract at
  `src/taxonmech/schema/taxonmech.yaml:180`. Owners are
  `src/taxonmech/seed.py` and `tests/test_seed.py`, with separate review
  of the upstream kg-microbe predicate. The 4,800 count is numerically
  correct for the species cluster, not E525.
- Minor: None found.

## Recommended Edits

1. Make equivalence generation in `src/taxonmech/seed.py` rank/scope-aware.
   Retain GTDB classification and source provenance while suppressing
   the unsupported species exact synonym and equivalence xref on this
   strain. Label the count as species-cluster scope; do not replace
   4,800 with 1 under unchanged species-count semantics.
2. Add a strain/species regression in `tests/test_seed.py`, retaining
   valid same-scope mappings. Review the source predicate in kg-microbe;
   do not hand-patch extracted TSVs or guess predicate direction.
3. Follow authorized dry-run/canary/regeneration steps after fixing the
   maintained rule. Do not hand-edit YAML, invent culture joins, merge
   E525 with other E-designated strains or promote human review status.

## Follow-up Checks

Run the new regression and `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just test tests/test_seed.py`.
After authorized regeneration, rerun both focused validators and inspect
the written YAML for retained classification, removed unsupported exact
synonym/xref, explicit cluster-count scope and unchanged NCBI identity.
Repeat the terminal-species census and target-member check. Run
`just verify-corpus` and full QC for the regeneration. M1 remains
unresolved; this read-only review made no corrective change.

## Additional Notes

Absence searches included ignored files using full structured reads,
`find`, or `rg --no-ignore --hidden`, with `-z` for compressed sources.
The only manual write is this report; strict validation wrote its
standard diagnostic. No YAML, source, prior report, history or status
was edited. No generator, source refresh, paid research, GitHub mutation
or cross-repository write occurred. Eukaryota was not re-reviewed.
