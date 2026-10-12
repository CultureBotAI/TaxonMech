# YAML Record Review: Helicobacter pylori HP180

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_hp180.yaml`
- Started UTC: 2026-10-03T09:16:22Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:17:06Z
- Verdict: pass with minor issues

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:103178` denotes
Helicobacter pylori HP180 below species 210. It declares `STRAIN`,
`BACTERIA`, `EXACT` grounding and `SEEDED` mapping status. It carries ten
ancestors, genetic code 11, zero attached strains, one NCBI NAME attestation
and a seed event. There are no synonym, nomenclature, GTDB, genome or
causal-graph assertions. The index entry is `data/taxa/PATHS.tsv:13138`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_hp180.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_hp180.yaml`:
  passed, one file and zero errors.
- Structured checks matched ID, label, stored rank, parent, code and all
  ten ancestor IDs, labels, ranks and parent links. The complete taxonomy
  inventory scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_hp180.yaml`
  passed; no record or maintained input changed.
- `just verify-corpus` was not rerun: it is full-corpus-only. Full catalog
  hashes/reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped because the ignored-inclusive search
  found no separate target history artifact. Strict validation covers the
  inspected embedded event.

## Identity and Grounding

The inspected [NCBI HP180 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103178&lvl=&mode=node)
agrees on ID, label, genetic code and lineage beneath H. pylori. It reports
`no rank` rather than the pinned inventory's `STRAIN`. Primary identity
and species-and-below scope are supported; the rank discrepancy remains
unresolved. HP18045 is not an alternative spelling of this target.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18345` supplies identity, stored rank,
  parent 210, code 11 and snapshot 2026-09-13; every ancestor row was
  checked separately.
- `data/catalog/ncbi_names-0000.jsonl.gz:38358` supplies the scientific
  name for taxon 103178.
- The taxonomy row lists NCBI alone, matching one NAME assertion, not a
  phenotype or genome count.
- `curation/seed_scope.tsv:144006` supplies the one-source rationale
  reproduced in the seed event. SEEDED does not imply human review.

The record cites no paper, gene, regulator, phenotype or transcriptomic
claim. iModulonDB is not applicable.

## Completeness

Ignored-file-inclusive ID/name/slug and standalone HP180 searches covered
reports, history, curation, raw, ATB and StrainInfo uncompressed inventories.
Only the target taxonomy/scope rows matched; no prior target report,
separate history artifact or BacDive/culture candidate was found there.

Decompressed JSONL.GZ/TSV.GZ searches included ignored files under catalog,
BacDive, BV-BRC, GOLD and StrainInfo. The only target-specific match was
the native NCBI name row. The name-prefix hit at
`data/bvbrc/bvbrc-0012.jsonl.gz:46513` instead names HP18045, genome
210.10873, assembly GCA_033356075.1 and species taxid 210. It is not
evidence for HP180 and was excluded.

The ATB full TSV.XZ was not scanned. These bounded findings do not prove
that HP180 has never been deposited or sequenced. Empty optional fields
and zero attached strains are consistent with the inspected evidence.

## Findings

- **Blocker:** None found in identity or structure.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** The browser reports `no rank`,
  while the inventory/YAML store `STRAIN`. The importer in
  `src/taxonmech/ncbi_taxdump.py` directly normalizes source rank. The
  archive pinned by `conf/ncbi_taxdump.yaml` was not found by an
  ignored-inclusive checkout filename search, leaving source-version
  divergence versus import error unresolved. Parentage and scope remain valid.

## Recommended Edits

No immediate generated-record edit is justified. Recover the pinned
taxonomy before changing rank inputs or importer behavior. Preserve empty
optional fields and do not import HP18045's genome by a prefix match.

## Follow-up Checks

- Inspect taxon 103178 in the archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- If a correction is supported and separately authorized, use the normal
  input refresh, `just seed-canary NCBITaxon:103178`, both target
  validators and full `just verify-corpus`.

## Additional Notes

The authority page was reached through its link on the previously inspected
parent-species page. External archive copies were not assessed. No paid
research, outbound message, GitHub mutation, history addition or review-status
promotion occurred.
