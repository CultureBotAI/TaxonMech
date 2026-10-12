# YAML Record Review: Helicobacter pylori JK22

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_jk22.yaml`
- Started UTC: 2026-10-03T09:20:17Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:23:31Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:103181` denotes
Helicobacter pylori JK22 beneath species 210. It declares `STRAIN`,
`BACTERIA`, `EXACT` grounding and `SEEDED` mapping status. It carries ten
ancestors, code 11, zero attached strains, one NCBI NAME attestation and
a seed event. There are no synonym, GTDB, nomenclature, genome or graph
assertions. The index entry is `data/taxa/PATHS.tsv:13141`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_jk22.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_jk22.yaml`:
  passed, one file and zero errors.
- Structured checks matched ID, label, stored rank, parent, code and all
  ten ancestor IDs, labels, ranks and parent links. The complete taxonomy
  inventory scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_jk22.yaml`
  passed. No record or maintained input changed.
- `just verify-corpus` was not rerun: it is full-corpus-only. Full catalog
  hashes/reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped because the ignored-inclusive target
  search found no separate history artifact. Strict validation covers
  the inspected embedded seed event.

## Identity and Grounding

The inspected [NCBI JK22 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103181&lvl=&mode=node)
supports the ID, label, genetic code and lineage beneath H. pylori. It
reports `no rank` rather than the inventory's `STRAIN`. Primary identity
and scope below species are supported; the rank discrepancy is unresolved.

Assembly hits for JK22-1 through JK22-10 and JK22-3 derivatives belong to
Xanthomonas perforans, taxon 442694, not this target. Shared strain-name
prefixes do not establish taxon, culture or genome identity.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18348` supplies the target identity,
  stored rank, parent 210, code 11 and snapshot 2026-09-13. Every ancestor
  was checked against its separate inventory row.
- `data/catalog/ncbi_names-0000.jsonl.gz:38361` supplies the scientific
  name for taxon 103181.
- The source row lists only NCBI, matching one NAME assertion and its
  snapshot note, not a phenotype or genome count.
- `curation/seed_scope.tsv:144009` supports the one-source rationale
  retained by the seed event. SEEDED does not imply human review.

The record cites no literature, gene, regulator, phenotype or transcriptomic
claim. iModulonDB is not applicable.

## Completeness

Ignored-file-inclusive ID/name/slug and standalone JK22 searches covered
reports, history, curation, raw, ATB and StrainInfo uncompressed inventories.
Only the target taxonomy/scope rows matched. No prior target report,
separate history artifact or BacDive/culture candidate was found there.

Decompressed JSONL.GZ/TSV.GZ searches included ignored files under catalog,
BacDive, BV-BRC, GOLD and StrainInfo. The only target-specific match was
the native NCBI name. Seventeen additional catalog hits were parsed and
confirmed as Xanthomonas perforans taxon 442694: one historical GenBank
row in `ncbi_genbank_historical-0000.jsonl.gz`, ten rows in
`ncbi_genbank-0018.jsonl.gz`, three rows in `ncbi_genbank-0050.jsonl.gz`
and three rows in `ncbi_refseq-0008.jsonl.gz`. For example, historical
GCA_019989925.1 and current GCA_019989925.2 identify JK22-3, not this
Helicobacter. No accession was transferred from these near misses.

The ATB full TSV.XZ was not scanned. These bounded findings do not prove
that the target has never been deposited or sequenced. Empty optional slots
and zero attached strains remain consistent with the evidence inspected.

## Findings

- **Blocker:** None found in primary identity or structure.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** The browser reports `no rank`,
  while the inventory/YAML store `STRAIN`. The importer in
  `src/taxonmech/ncbi_taxdump.py` directly normalizes source rank. The
  archive pinned by `conf/ncbi_taxdump.yaml` was not found by the
  ignored-inclusive checkout filename search in this review session.
  Source-version divergence versus import error remains unresolved;
  species parentage and scope are unaffected.

## Recommended Edits

No immediate generated-record edit is justified. Inspect the hash-verified
pinned source before changing rank inputs or importer behavior. Do not
create a genome or deposit link from a matching strain-name prefix.

## Follow-up Checks

- Inspect target 103181 in the archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- If a correction is supported and separately authorized, use the normal
  input refresh, `just seed-canary NCBITaxon:103181`, both target
  validators and full `just verify-corpus`.

## Additional Notes

The authority page was reached through its link on the previously inspected
parent-species page and successfully reopened by reference after a direct
URL retry failed. External archive copies were not checked. No paid
research, outbound messages, GitHub mutation, history addition or status
promotion occurred.
