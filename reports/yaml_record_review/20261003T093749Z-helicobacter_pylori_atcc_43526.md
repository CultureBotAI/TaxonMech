# YAML Record Review: Helicobacter pylori ATCC 43526

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_atcc_43526.yaml`
- Started UTC: 2026-10-03T09:34:07Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:37:49Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:103189` denotes
Helicobacter pylori ATCC 43526, stored as `STRAIN` beneath species 210 in
`BACTERIA`. It has ten ancestors, code 11, `EXACT` grounding, `SEEDED`
mapping status, zero attached BacDive strains, one NCBI NAME attestation
and a seed event. There are no synonym, nomenclature, GTDB, genome or
graph assertions. Its index entry is `data/taxa/PATHS.tsv:13148`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_atcc_43526.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_atcc_43526.yaml`:
  passed, one file and zero errors.
- Structured checks matched identity, stored rank, parent, code and all
  ten ancestor IDs, labels, ranks and parent links to source rows.
  The complete taxonomy parent-column scan found zero direct children.
- `just straininfo-query --strain SI-ID41893 --evidence --limit 20`:
  passed and returned zero imported deposit paths. The inspected query
  code calls StrainInfo and ATB provenance checks with `reproduce=False`;
  success verifies source/configuration and hashes, not full source replay.
- A separate focused `build_links` replay of native SI-ID41893 against
  the complete BacDive inventory returned no links, assemblies or related
  records and exactly `no_eligible_own_deposit_match`.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_atcc_43526.yaml`
  passed. No record or maintained input changed.
- `just verify-corpus` was skipped: it is full-corpus-only. Full corpus
  reproduction, all source catalogs and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped: the ignored-inclusive target search
  found no separate history artifact. The embedded event was inspected
  and included in strict validation.

## Identity and Grounding

The inspected [NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103189&lvl=&mode=node)
supports the ID, full label, code and lineage beneath H. pylori. The live
rank is `no rank`, differing from stored `STRAIN`; scope below species
remains supported.

The inspected [ATCC catalog](https://www.atcc.org/products/43526) identifies
this culture as H. pylori, lists NCTC 11916 and JCM 7654, and says it is
not a type strain. That supports the culture identity but does not create
a BacDive identifier or alter the source taxonomy. StrainInfo classifies
its deposits at species 210; that broader source value must remain visible.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18355` supports the stored identity,
  rank, parent, code and snapshot 2026-09-13. Ancestors were checked
  against their separate rows.
- `data/catalog/ncbi_names-0000.jsonl.gz:38368` supplies the exact target
  scientific name. One NCBI NAME attestation is supported.
- `curation/seed_scope.tsv:144016` supports the seed event's rationale.
- The full native projection at `data/straininfo/records.jsonl.gz:30131`
  is SI-ID41893, version DOI `10.60712/SI-ID41893.2`, published online.
  It lists ATCC 43526 / SI-DP112748, NCTC 11916 / SI-DP112749,
  JCM 7654 / SI-DP112750, BCRC 17027 / SI-DP513140 and CCRC 17027 /
  SI-DP513141. All five own deposit records are present and non-erroneous.
- Its AF001358 and AF001357 gene references explicitly name ATCC deposit
  SI-DP112748. Its Z25744 rRNA reference names NCTC deposit SI-DP112749,
  not ATCC. No sequence of type `genome` is present. A group-level culture
  relationship cannot transfer Z25744 to the ATCC deposit.
- ATCC independently lists AF001358 and AF001357. The inspected
  [NCBI AF001358 page](https://www.ncbi.nlm.nih.gov/nuccore/AF001358)
  resolves the former as a gene record, currently displayed as AF001358.1.
  Keep the unversioned StrainInfo assertion as supplied; do not append `.1`.
- The inspected [ATCC genome portal entry](https://genomes.atcc.org/genomes/2c7d995e20864f25)
  explicitly names ATCC 43526 and the same collection aliases. It reports
  a 1,680,926-nt, single-contig assembly published in 2023. No GCA/GCF
  accession was visible in the inspected text. Its portal key must not
  be invented into a supported genome CURIE or equated with gene records.

No mechanism or phenotype claim was inferred from sequence descriptions.
iModulonDB is not applicable to this taxon-only record; gene titles were
examined only to distinguish nucleotide references from genome identifiers.

## Completeness

Ignored-file-inclusive ID/full-name/slug and whole ATCC 43526 searches covered
reports, history, curation, raw, ATB and StrainInfo uncompressed inventories.
Only target taxonomy and scope rows matched. Follow-up searches included
NCTC 11916, JCM 7654, BCRC/CCRC 17027, SI-ID41893, SI-DP112748 and the
ATCC portal key. They found the explicit exclusion at
`data/straininfo/exclusions.tsv:232331`, but no existing target review,
separate history artifact or imported strain link on those surfaces.

Decompressed JSONL.GZ/TSV.GZ searches included ignored files under catalog,
BacDive, BV-BRC, GOLD and StrainInfo using the target identity and deposit
aliases. Matches were confined to the native NCBI name and SI-ID41893.
All five deposit designations successfully normalized through the pinned
CAFI matcher, but each had zero matches in a complete structured index of
`data/raw/bacdive_strains.tsv`. The exclusion is not a malformed collection
identifier or an ignored-source-search artifact.

`docs/STRAININFO.md` and `src/taxonmech/straininfo_links.py` explicitly
require an existing BacDive deposit and do not create new strain identities.
Zero attached strains is therefore consistent with the current model,
not evidence that no culture or sequence exists. The ATB full TSV.XZ was
not scanned. No global absence of additional genomes is claimed.

## Findings

- **Blocker:** None found.
- **Major:** None found; no false taxon identity or broken import rule
  was demonstrated.
- **Minor (1): NCBI rank discrepancy.** Current NCBI gives `no rank`,
  inventory/YAML give `STRAIN`. `src/taxonmech/ncbi_taxdump.py` directly
  normalizes native ranks. The archive pinned in `conf/ncbi_taxdump.yaml`
  was not located by an ignored-inclusive checkout filename search;
  source-version divergence versus import error remains unresolved.
- **Minor (2): Model-limited visibility of supported culture evidence.**
  The record exposes none of the inspected own-deposit sequence context
  or ATCC genome page. This is a non-blocking enrichment limitation,
  explained by the BacDive-only strain backbone and supported genome-ID
  types, not an incorrect `strain_count`. A design change would belong in
  `docs/STRAININFO.md`, `src/taxonmech/straininfo_links.py`,
  `src/taxonmech/seed.py` and, for ATCC-native genome IDs, the schema and
  source adapter. Do not manufacture a BacDive ID or bypass deposit matching.

## Recommended Edits

No immediate generated-record edit is justified. Resolve the rank discrepancy
against the hash-verified pinned NCBI source first. For a separately scoped
enrichment change, decide how non-BacDive culture evidence and unsupported
native genome resources can be represented while preserving taxon, strain,
deposit, sequence and assembly identity. The current schema's genome-ID
pattern does not admit an ATCC portal key.

Retain source-specific classifications and same-deposit evidence. Gene/rRNA
accessions belong in typed nucleotide related records, never genome counts.
Do not use shared SI-ID membership, culture aliases alone or a taxon label
as a shortcut to assigning assemblies or sequences.

## Follow-up Checks

- Inspect taxon 103189 in the archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- Retry live SI-ID41893 / DOI resolution and independent AF001357 and
  Z25744 sequence inspection before publishing new links. These pages
  were inaccessible or challenged in this review; native source evidence
  remains the basis for their deposit assignments.
- Any authorized source/model extension needs focused deposit-isolation,
  classification and identifier tests in `tests/test_straininfo_links.py`
  and relevant seed/schema tests. Rebuild the overlay only when the source
  and matching inventory support it, then run
  `just seed-canary NCBITaxon:103189`, both record validators and full
  `just verify-corpus`.

## Additional Notes

The live StrainInfo page/DOI and some NCBI/ENA sequence endpoints could not
be verified through the browser tool. A neighboring StrainInfo page returned
only a JavaScript shell and was not used as substitute evidence. No genome
FASTA was downloaded and no access restriction was bypassed. External
NCBI archive copies were not checked. No paid research, outbound messages,
GitHub mutation, curation-history addition or review-status promotion occurred.
