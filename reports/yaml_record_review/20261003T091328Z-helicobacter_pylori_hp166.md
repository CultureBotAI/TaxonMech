# YAML Record Review: Helicobacter pylori HP166

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_hp166.yaml`
- Started UTC: 2026-10-03T09:12:50Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:13:28Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:103176` denotes
Helicobacter pylori HP166 beneath species `NCBITaxon:210`. It declares
`STRAIN`, `BACTERIA`, `EXACT` grounding and `SEEDED` mapping status, ten
ancestors, genetic code 11 and zero attached strains. It has one NCBI
NAME attestation and one seed event, with no synonym, nomenclature, GTDB,
genome or causal-graph assertions.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_hp166.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_hp166.yaml`:
  passed, one file and zero errors.
- Structured checks matched identity, stored rank, parent, code and all
  ten ancestor IDs, labels, ranks and parent links against the taxonomy
  inventory. A complete inventory scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_hp166.yaml`
  passed. No generated record or maintained input was changed.
- `just verify-corpus` was not rerun: it is full-corpus-only. Full catalog
  hashes/reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped because the ignored-file-inclusive
  search found no separate target history artifact. Strict validation
  covers the inspected embedded seed event.

## Identity and Grounding

The inspected [NCBI HP166 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103176&lvl=&mode=node)
agrees on ID, label, code and lineage below H. pylori. It reports `no rank`
rather than the retained inventory's `STRAIN`; the source discrepancy is
unresolved. The primary taxon and species-and-below scope are supported.

The HP166 shorthand also occurs in Pseudomonas sp. HP166, taxon 3713290.
That is not this target. Exact taxon fields and full names, not the reused
isolate shorthand, were used to evaluate matches.

## Evidence

| Claim group | Inspected evidence and conclusion |
| --- | --- |
| Taxonomy | `data/raw/ncbitaxon_taxa.tsv:18343` supplies target ID/name, stored rank, parent 210, genetic code 11 and snapshot 2026-09-13. All ancestor rows were checked separately. |
| Native name | `data/catalog/ncbi_names-0000.jsonl.gz:38356` records Helicobacter pylori HP166 as the scientific name for 103176. |
| Attestation | The source row lists NCBI alone, supporting one NAME assertion and its snapshot note, not a phenotype or genome count. |
| Scope/history | `curation/seed_scope.tsv:144004` supplies the one-source rationale retained by the seed event. SEEDED does not imply completed human review. |

The record cites no literature, gene identifier, functional or transcriptomic
claim. iModulonDB is not applicable; gene-name similarity would not establish
a strain-level assertion.

## Completeness

Ignored-file-inclusive ID/full-name/slug and standalone HP166 searches
covered reports, history, curation, raw, ATB and StrainInfo uncompressed
inventories. Target-specific matches were the taxonomy/scope rows; there
was no prior target report or separate history artifact in those surfaces.
The additional Pseudomonas taxonomy/scope rows were inspected and excluded.
The search found no HP166 BacDive or culture-collection candidate there.

Decompressed, ignored-file-inclusive JSONL.GZ/TSV.GZ searches covered
catalog, BacDive, BV-BRC, GOLD and StrainInfo. After inspecting taxon/name
fields, the only target-specific match was its native NCBI name row.
Unrelated numeric matches in genome statistics were discarded. Pseudomonas
HP166's paired GCA_058070675.1/GCF_058070675.1 records explicitly carry
taxid 3713290, not 103176 (`ncbi_genbank-0053.jsonl.gz:35611` and
`ncbi_refseq-0008.jsonl.gz:46391`). They must not populate this record.

The ATB full TSV.XZ was not scanned. These bounded findings do not prove
that the target has never been deposited or sequenced. Empty optional
fields and zero attached strains are consistent with the evidence inspected.

## Findings

- **Blocker:** None found in identity or structure.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** The browser reports `no rank`,
  while the inventory/YAML report `STRAIN`. The importer in
  `src/taxonmech/ncbi_taxdump.py` normalizes the source rank directly.
  The archive pinned by `conf/ncbi_taxdump.yaml` was not found by the
  ignored-inclusive checkout filename search in this session, leaving
  source-version divergence versus import error unresolved. Parentage
  and eligibility below species are unaffected.

## Recommended Edits

No immediate generated-record edit is justified. Recover the pinned source
before changing the rank input or importer. Preserve empty optional slots
and do not join the Pseudomonas assembly by the reused HP166 shorthand.

## Follow-up Checks

- Inspect target 103176 in the taxonomy archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- If a correction is supported and separately authorized, use the normal
  input refresh, `just seed-canary NCBITaxon:103176`, both target
  validators and full `just verify-corpus`.

## Additional Notes

Direct NCBI requests failed initially. Following the HP166 link from the
previously inspected parent-species page succeeded. External copies of
the pinned taxonomy archive were not assessed. No paid research, outbound
messages, GitHub mutation, history addition or status promotion occurred.
