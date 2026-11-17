# YAML Record Review: Helicobacter pylori HP168

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_hp168.yaml`
- Started UTC: 2026-10-03T09:14:11Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:14:50Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:103177` denotes
Helicobacter pylori HP168 beneath species `NCBITaxon:210`. It declares
`STRAIN`, `BACTERIA`, `EXACT` grounding and `SEEDED` mapping status, ten
ancestors, genetic code 11 and zero attached strains. It has one NCBI NAME
attestation and one seed event, with no synonym, GTDB, nomenclature,
genome or causal-graph assertions.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_hp168.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_hp168.yaml`:
  passed, one file and zero errors.
- Structured YAML/TSV checks matched ID, label, stored rank, parent, code
  and all ten ancestor IDs, labels, ranks and parent links. A complete
  taxonomy inventory scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_hp168.yaml`
  passed. No generated record or maintained input was changed.
- `just verify-corpus` was not rerun: it is full-corpus-only. Full catalog
  hashes/reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped because the ignored-file-inclusive
  target search found no separate history artifact. Strict validation
  covers the inspected embedded seed event.

## Identity and Grounding

The inspected [NCBI HP168 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103177&lvl=&mode=node)
agrees on identifier, name, code and lineage beneath H. pylori. It reports
`no rank` rather than the inventory's `STRAIN`; the source discrepancy
remains unresolved. Primary identity and eligibility below species are
supported. HP168 is not equated to the parent species or neighboring strains.

## Evidence

| Claim group | Inspected evidence and conclusion |
| --- | --- |
| Taxonomy | `data/raw/ncbitaxon_taxa.tsv:18344` supplies ID/name, stored rank, parent 210, code 11 and snapshot 2026-09-13. Every ancestor row was checked separately. |
| Native name | `data/catalog/ncbi_names-0000.jsonl.gz:38357` records Helicobacter pylori HP168 as the scientific name for 103177. |
| Attestation | The source row lists NCBI alone, supporting one NAME assertion and its snapshot note, not a genome count or biological trait. |
| Scope/history | `curation/seed_scope.tsv:144005` supports the one-source rationale retained by the seed event. SEEDED is not human review. |

The record cites no paper, gene, regulator, phenotype or transcriptomic
claim. iModulonDB is not applicable; similarly named genes would not
establish assertions about this taxon.

## Completeness

Ignored-file-inclusive identifier, full name, slug and standalone HP168
searches covered reports, history, curation, raw, ATB and StrainInfo
uncompressed inventories. Only the target taxonomy and scope rows matched.
No prior target review, separate history artifact, BacDive candidate or
culture-collection candidate was found in those inspected surfaces.

Decompressed, ignored-file-inclusive JSONL.GZ/TSV.GZ searches covered
catalog, BacDive, BV-BRC, GOLD and StrainInfo using exact taxon fields,
name, slug and standalone HP168. The only match was the native NCBI name
row. The ATB full TSV.XZ was not scanned. These are bounded findings,
not proof that the strain has never been deposited or sequenced.

Zero attached strains and empty optional slots are consistent with the
evidence inspected. No species-level genome, type deposit or phenotype
was transferred to this target.

## Findings

- **Blocker:** None found in primary identity or structure.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** The browser reports `no rank`,
  while the inventory/YAML store `STRAIN`. The importer in
  `src/taxonmech/ncbi_taxdump.py` directly normalizes the source rank.
  The archive pinned by `conf/ncbi_taxdump.yaml` was not found by an
  ignored-inclusive checkout filename search in this session, leaving
  source-version divergence versus import error unresolved. Species
  parentage and scope eligibility are unaffected.

## Recommended Edits

No immediate generated-record edit is justified. Recover and inspect the
hash-verified pinned source before changing rank inputs or importer behavior.
Preserve empty optional fields until target-specific evidence is established.

## Follow-up Checks

- Inspect target 103177 in the taxonomy archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- If a correction is supported and separately authorized, use the normal
  input refresh, `just seed-canary NCBITaxon:103177`, both target
  validators and full `just verify-corpus`.

## Additional Notes

The authority page was reached through its link on the previously inspected
parent-species page. External copies of the pinned taxonomy archive were
not assessed. No paid research, outbound messages, GitHub mutation, history
addition or review-status promotion occurred.
