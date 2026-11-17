# YAML Record Review: Helicobacter pylori JK25

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_jk25.yaml`
- Started UTC: 2026-10-03T09:25:14Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:26:28Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:103182` denotes
Helicobacter pylori JK25 beneath species 210, with rank `STRAIN`, domain
`BACTERIA`, `EXACT` grounding and `SEEDED` mapping status. It carries ten
ancestors, code 11, zero attached strains, one NCBI NAME attestation and
an embedded seed event. There are no synonym, nomenclature, GTDB, genome
or causal-graph assertions. The index entry is `data/taxa/PATHS.tsv:13142`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_jk25.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_jk25.yaml`:
  passed, one file and zero errors.
- Structured inventory checks matched ID, label, stored rank, parent,
  genetic code and all ten ancestor IDs, labels, ranks and parent links.
  A complete taxonomy inventory scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_jk25.yaml`
  passed. No record or maintained input changed.
- `just verify-corpus` was skipped: the documented gate is full-corpus-only.
  Full source hashes/reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped: the ignored-inclusive target search
  found no separate history artifact. The embedded event was inspected
  and included in strict validation.

## Identity and Grounding

The inspected [NCBI JK25 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103182&lvl=&mode=node)
supports the exact ID, label, genetic code and lineage beneath H. pylori.
It reports `no rank`, differing from the pinned inventory's `STRAIN`.
The taxon remains below a species and in scope under either value.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18349` supports the stored identity,
  rank, parent, code and snapshot date 2026-09-13. The ancestor chain was
  checked against the separate source rows.
- `data/catalog/ncbi_names-0000.jsonl.gz:38362` supplies the target's
  scientific name under taxon 103182.
- `curation/seed_scope.tsv:144010` supports the one-source rationale in
  the seed event. The attestation's count of one NAME agrees with the
  identity evidence; it is not a genome or phenotype count.
- No literature, gene, regulator, phenotype or transcriptomic assertion
  is present. iModulonDB is not applicable.

## Completeness

Ignored-file-inclusive ID/name/slug and whole JK25 searches covered reports,
history, curation, raw, ATB and StrainInfo uncompressed inventories. Only
the target taxonomy and scope rows matched. No prior target report,
separate history artifact or culture candidate was found there.

Decompressed JSONL.GZ/TSV.GZ searches included ignored files under catalog,
BacDive, BV-BRC, GOLD and StrainInfo. Only the native NCBI scientific-name
row matched. The ATB full TSV.XZ was not scanned. These bounded results
do not establish that JK25 has never been cultured, deposited or sequenced;
they do not support adding a deposit or genome to this record. Empty
optional fields and zero attached strains are consistent with the inspected
source material.

## Findings

- **Blocker:** None found.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** The live browser says `no rank`
  while the inventory and YAML say `STRAIN`. The inspected importer,
  `src/taxonmech/ncbi_taxdump.py`, directly normalizes the native rank.
  The archive pinned in `conf/ncbi_taxdump.yaml` was not found by the
  ignored-inclusive checkout filename search. Source-version divergence
  versus import error is unresolved; identity and species parentage agree.

## Recommended Edits

No generated-record edit is justified by the inspected evidence. Resolve
the rank conflict against the hash-verified pinned source first. Any supported
fix belongs in the configured source refresh or the importer with a focused
test, followed by normal extraction and seeding, not a YAML hand edit.

## Follow-up Checks

- Inspect taxon 103182 in the archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- After a separately authorized correction, use the normal input refresh,
  `just seed-canary NCBITaxon:103182`, both target validators and full
  `just verify-corpus`.

## Additional Notes

The authority page was inspected via its link on the parent-species page.
No external archive copy was checked. SEEDED remains unchanged; this review
does not confer human sign-off. No history addition, paid research, outbound
message or GitHub mutation occurred.
