# YAML Record Review: Helicobacter pylori HP158

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_hp158.yaml`
- Started UTC: 2026-10-03T08:54:08Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:55:12Z
- Verdict: pass with minor issues

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:103174` denotes
Helicobacter pylori HP158 beneath species `NCBITaxon:210`. It declares
`STRAIN`, `BACTERIA`, `EXACT` grounding and `SEEDED` mapping status. It has
ten ancestors, genetic code 11, zero attached strains, one NCBI NAME
attestation and one seed event. There are no synonym, GTDB, nomenclature,
genome or causal-graph assertions. The index entry is `data/taxa/PATHS.tsv:13130`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_hp158.yaml`: passed,
  no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_hp158.yaml`:
  passed, one file scanned and zero errors.
- Structured YAML/TSV checks confirmed ID, label, stored rank, parent, code
  and all ten ancestor IDs, labels, ranks and parent links. A complete scan
  of the taxonomy inventory found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_hp158.yaml`
  passed. No generated record or maintained input was changed.
- `just verify-corpus` was not rerun: it is full-corpus-only. Full catalog
  hashes/censuses and generated pages were not checked. These focused checks
  are not a fresh reproduction pass.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was not run: the ignored-file-inclusive target
  search found no separate history artifact. The embedded event was inspected
  and covered by strict validation.

## Identity and Grounding

The inspected [NCBI HP158 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103174&lvl=3&mode=node)
agrees on identifier, label, code 11 and lineage beneath H. pylori. It reports
`no rank`, unlike the pinned inventory's `STRAIN`. Primary identity and
species-and-below scope are supported; the rank-source discrepancy remains
unresolved. HP158 is not being equated to the parent species or another
HP-numbered strain.

## Evidence

| Claim group | Inspected evidence and conclusion |
| --- | --- |
| Taxonomy fields and lineage | `data/raw/ncbitaxon_taxa.tsv:18341` supplies the target ID/name, stored rank, parent 210, code 11 and 2026-09-13 snapshot. Every ancestor row was checked separately. |
| Native name | `data/catalog/ncbi_names-0000.jsonl.gz:38354` records Helicobacter pylori HP158 as the scientific name for 103174. |
| Attestation | The taxonomy row lists only NCBI, matching the one NAME assertion and snapshot note. This is neither a phenotype nor a genome count. |
| Scope and event | `curation/seed_scope.tsv:144002` supplies the 2026-09-13 one-source rationale retained in the seed event. SEEDED does not imply human review. |

A search hit for [PMID 14729704](https://pubmed.ncbi.nlm.nih.gov/14729704/)
was checked at its figure captions. It concerns the gene hp158 and mutants
in strain P1, not evidence establishing this taxon as that mutant. No RecA,
glycosylation or susceptibility assertion was transferred to HP158. The
record itself cites no paper, gene identifier or regulatory claim, so
iModulonDB is not applicable.

## Completeness

Identifier, exact name and slug were searched with
`rg --no-ignore --hidden` across reports, history, curation, raw, ATB and
StrainInfo uncompressed inventories. Before this report, only the taxonomy
and scope rows matched; no prior target review or separate history artifact
was found in those surfaces. A standalone HP158 search of the BacDive and
culture-collection inventories returned no candidates, including ignored files.

A decompressed, ignored-file-inclusive JSONL.GZ/TSV.GZ search of
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/` and
`data/straininfo/` checked exact taxon fields, name, slug and standalone
HP158. Its only match was the native NCBI name row. These are bounded findings,
not proof that the strain has never been deposited or sequenced. The
compressed ATB full TSV.XZ was not scanned.

The search-returned type-strain link-out was not used as a deposit match.
Its candidate BacDive 6102 is inventoried as RPH 13487 under taxon 102618
at `data/raw/bacdive_strains.tsv:5989`, not taxon 103174. Empty optional
slots and zero attached strains are consistent with the inspected evidence.

## Findings

- **Blocker:** None found in identity or structure.
- **Major:** None found.
- **Minor (1): NCBI rank differs from the retained inventory.** The inspected
  browser reports `no rank`; the inventory/YAML store `STRAIN`. The importer
  in `src/taxonmech/ncbi_taxdump.py` normalizes the source rank directly.
  The archive pinned by `conf/ncbi_taxdump.yaml` is unavailable in the
  checkout, so source-version divergence versus import error remains
  unresolved. Parentage and eligibility below species are unaffected.

## Recommended Edits

No immediate generated-record edit is justified. Inspect the hash-verified
pinned taxonomy before correcting the input or importer. Preserve empty
optional fields; neither a gene-name collision nor a species-level type
strain supplies target-specific evidence.

## Follow-up Checks

- Recover the archive pinned by `conf/ncbi_taxdump.yaml`, SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`,
  and inspect taxon 103174's original `nodes.dmp` rank.
- If a correction is supported and separately authorized, use the normal
  input refresh, `just seed-canary NCBITaxon:103174`, both target validators
  and the full `just verify-corpus`.

## Additional Notes

Initial browser requests failed, but the node-mode authority page succeeded.
A direct EFetch request with curl failed DNS resolution and supplied no
evidence. The ignored-file-inclusive repository taxdump filename search in
this review session found no archive or `nodes.dmp`; external copies were
not assessed. No paid research, outbound messages, GitHub mutation, history
addition or review-status promotion occurred.
