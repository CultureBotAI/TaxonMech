# YAML Record Review: Helicobacter pylori HP156

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_hp156.yaml`
- Started UTC: 2026-10-03T08:45:21Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:46:02Z
- Verdict: pass with minor issues

## Target

The entire generated `TaxonRecord` was read. `NCBITaxon:103173` denotes
Helicobacter pylori HP156 beneath species `NCBITaxon:210`. It declares
`STRAIN`, `BACTERIA`, `EXACT` grounding and `SEEDED` mapping status. The record
has ten ancestors, code 11, zero attached strains, one NCBI name attestation
and one seed event. It contains no synonyms, nomenclature, GTDB mappings,
genome links or causal graph. Its index entry is `data/taxa/PATHS.tsv:13127`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_hp156.yaml`: passed,
  no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_hp156.yaml`:
  passed, one file scanned and zero errors.
- Structured comparisons against the full taxonomy inventory confirmed the
  identifier, label, stored rank, parent, code and all ten ancestor IDs,
  labels, ranks and parent links. No direct child was found in that inventory.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_hp156.yaml`
  passed. No generated record or maintained input was modified.
- `just verify-corpus` was not rerun: it is full-corpus-only, and these
  focused checks do not establish current corpus reproduction. Full source
  hashes/censuses and generated pages were not checked.
- `just validate-products` is not applicable without causal-graph nodes.
  `just validate-history` was not run: the ignored-file-inclusive target
  search found no separate history artifact. The embedded event was inspected
  and covered by strict validation.

## Identity and Grounding

The pinned taxonomy row and native name entry identify HP156 as 103173,
with species parent 210. The lineage is internally consistent and the record
is within species-and-below scope. No species-wide exact-synonym or genome
equivalence assertion is present.

Requests to the [NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103173),
its alternate Info URL, [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/taxonomy/103173/)
and the NCBI taxonomy EFetch endpoint returned no usable content. These are
attempted checks, not successful external confirmation. In particular, no
claim is made that the current browser shows a different rank for this target.

## Evidence

| Claim group | Inspected source and conclusion |
| --- | --- |
| Identity, rank, parent and code | `data/raw/ncbitaxon_taxa.tsv:18340` supplies the exact ID/name, STRAIN rank, parent 210, code 11 and 2026-09-13 snapshot. Every ancestor was separately checked against its inventory row. |
| Native name | `data/catalog/ncbi_names-0000.jsonl.gz:38353` records Helicobacter pylori HP156 as the scientific name of 103173. |
| Attestation | The inventory's sole attested source is NCBI, agreeing with one NAME assertion. This is not a phenotype or genome count. |
| Scope and seed event | `curation/seed_scope.tsv:144001` supplies the 2026-09-13 one-source rationale retained by the embedded event. SEEDED remains a generation status, not human review. |

The target cites no papers, LPSN identifiers, ontology graph nodes or assembly
accessions. iModulonDB is not applicable to this taxonomy-only record: it
asserts no gene, regulator or expression-module evidence.

## Completeness

The exact identifier, label and slug were searched using
`rg --no-ignore --hidden` across review reports, history, curation, raw,
ATB and StrainInfo uncompressed inventories. Only the taxonomy and scope rows
matched before this report; no prior target report or separate history
artifact was found in those surfaces. A standalone HP156 search across the
BacDive and culture-collection inventories found no candidate, including
ignored files.

A decompressed, ignored-file-inclusive search of JSONL.GZ/TSV.GZ under
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/` and
`data/straininfo/` checked exact taxonomy fields, label, slug and standalone
HP156. The only match was the native NCBI scientific-name row. This does not
establish worldwide absence of deposits or sequencing. The compressed ATB
full TSV.XZ and sources outside these bounded surfaces were not searched.

The zero strain count and empty optional evidence slots are consistent with
the inspected sources. They should not be filled by transferring a species
type strain, another HP-numbered strain's genome or species-level traits.

## Findings

- **Blocker:** None found in the file or inspected pinned evidence.
- **Major:** None found.
- **Minor (1): Current authority verification remains incomplete.** Multiple
  NCBI endpoints were unavailable, leaving present-day name/rank/parent
  confirmation unresolved. This is a review-evidence limit, not an observed
  incorrect field. If a later check reveals a discrepancy, the maintained
  ownership is the source pinned by `conf/ncbi_taxdump.yaml` and its importer
  `src/taxonmech/ncbi_taxdump.py`, followed by regeneration.

## Recommended Edits

No evidence-backed record edit is recommended. Retry the exact NCBI lookup;
if it disagrees, inspect the pinned source before changing the inventory or
importer. Do not infer HP156's rank from nearby records or hand-edit generated
YAML. Preserve empty optional slots until target-specific evidence supports
an addition.

## Follow-up Checks

- Retry the authority lookup for taxon 103173, explicitly comparing label,
  rank and parent with the retained source version.
- If needed, inspect the original `nodes.dmp` and `names.dmp` rows from the
  archive pinned in `conf/ncbi_taxdump.yaml`, SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- After a separately authorized source correction, run the normal refresh,
  `just seed-canary NCBITaxon:103173`, both target validators and the full
  `just verify-corpus`.

## Additional Notes

The repository-wide ignored-file-inclusive taxdump filename search in this
session found no archive or `nodes.dmp` in the checkout. Copies outside it
were not assessed. No successful live verification is implied by the attempted
URLs. No paid research, external messages, GitHub mutation, history addition,
review-status promotion or sequence download occurred.
