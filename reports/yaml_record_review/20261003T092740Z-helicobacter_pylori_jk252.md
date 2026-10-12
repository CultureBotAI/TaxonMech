# YAML Record Review: Helicobacter pylori JK252

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_jk252.yaml`
- Started UTC: 2026-10-03T09:27:00Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:27:40Z
- Verdict: pass with minor issues

## Target

The complete generated `TaxonRecord` was read. `NCBITaxon:103183` identifies
Helicobacter pylori JK252, a `STRAIN` under species 210 in `BACTERIA`.
It has `EXACT` grounding, `SEEDED` mapping status, ten lineage entries,
genetic code 11, no attached strains, one NCBI NAME attestation and one seed
event. No other taxonomic mapping, synonym, nomenclature, genome or graph
assertion is present. Its index row is `data/taxa/PATHS.tsv:13143`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_jk252.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_jk252.yaml`:
  passed, one file and zero errors.
- Structured checks matched ID, label, stored rank, parent, code and all
  ten ancestor IDs, labels, ranks and parent links to the taxonomy inventory.
  A complete parent-column scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_jk252.yaml`
  passed. No record or maintained input changed.
- `just verify-corpus` was skipped because it exposes only full-corpus
  reproduction. Full manifest hashes and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped: the ignored-inclusive target search
  found no separate history artifact. The embedded event was read and
  included in strict validation.

## Identity and Grounding

The inspected [NCBI JK252 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103183&lvl=&mode=node)
confirms taxon 103183, the full label, code 11 and lineage beneath
H. pylori. The live rank is `no rank`, not the stored `STRAIN`. That
conflict does not change the ID or its eligibility below species.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18350` gives the target's identity,
  stored rank, parent, code and snapshot date 2026-09-13. Each ancestor
  was matched to its own inventory row.
- `data/catalog/ncbi_names-0000.jsonl.gz:38363` supplies the scientific
  name under the exact target taxon ID.
- `curation/seed_scope.tsv:144011` supplies the seed event's rationale.
  One NCBI NAME assertion is supported; it denotes neither a genome
  count nor an independently curated biological trait.
- There is no literature, gene, pathway, regulator or expression-module
  claim to cross-check. iModulonDB is not applicable.

## Completeness

Ignored-file-inclusive searches for the ID, label, slug and whole JK252
covered uncompressed reports, history, curation, raw, ATB and StrainInfo
inventories. Only target taxonomy and scope rows matched. No prior target
report, separate history artifact or culture candidate was found there.

Decompressed JSONL.GZ/TSV.GZ searches, also including ignored files, covered
catalog, BacDive, BV-BRC, GOLD and StrainInfo. Only the native NCBI name
matched. The ATB full TSV.XZ was not scanned. This bounded search does not
prove a global absence of cultures, deposits or sequence data. It supplies
no basis to add a strain or genome here; optional empty fields and zero
attached strains agree with the inspected evidence.

## Findings

- **Blocker:** None found.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** Current NCBI gives `no rank`;
  the pinned inventory and generated YAML give `STRAIN`. The inspected
  `src/taxonmech/ncbi_taxdump.py` directly normalizes source ranks.
  The ignored-inclusive checkout filename search did not locate the
  archive pinned by `conf/ncbi_taxdump.yaml`. A source-version difference
  cannot yet be distinguished from an import defect.

## Recommended Edits

No immediate record edit is warranted. First resolve the rank discrepancy
from the verified pinned source. Any supported correction belongs in the
configured source refresh or, if an import defect is demonstrated, in
`src/taxonmech/ncbi_taxdump.py` with a regression test. Regenerate through
the normal inventory and seeding workflow; do not hand-edit this YAML.

## Follow-up Checks

- Check taxon 103183 in the source archive whose configured SHA256 is
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- After a separately authorized correction, refresh the input, run
  `just seed-canary NCBITaxon:103183`, rerun both target validators and
  run full `just verify-corpus`.

## Additional Notes

The authority page was inspected through the parent-species page's link.
External archive copies were not checked. No paid research, outbound
message, GitHub mutation, curation-history addition or review-status
promotion occurred.
