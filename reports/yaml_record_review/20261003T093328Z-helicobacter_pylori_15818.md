# YAML Record Review: Helicobacter pylori 15818

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_15818.yaml`
- Started UTC: 2026-10-03T09:32:48Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:33:28Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:103187` identifies
Helicobacter pylori 15818, stored as `STRAIN` beneath species 210 in
`BACTERIA`. It has ten ancestors, code 11, `EXACT` grounding, `SEEDED`
mapping status, no attached strains, one NCBI NAME attestation and one
seed event. There are no synonym, nomenclature, GTDB, genome or graph
assertions. The index entry is `data/taxa/PATHS.tsv:13147`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_15818.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_15818.yaml`:
  passed, one file and zero errors.
- Structured checks matched ID, label, stored rank, parent, code and all
  ten ancestor IDs, labels, ranks and parent links to inventory rows.
  A complete taxonomy parent-column scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_15818.yaml`
  passed. No record or maintained input changed.
- `just verify-corpus` was skipped because the gate is full-corpus-only.
  Full source hashes/reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped: the ignored-inclusive target search
  found no separate history artifact. The embedded event was inspected
  and included in strict validation.

## Identity and Grounding

The inspected [NCBI 15818 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103187&lvl=&mode=node)
confirms the exact ID, name, code and lineage beneath H. pylori. It says
`no rank`, differing from the stored `STRAIN`. Identity and scope below
species remain supported.

Genome catalog uses of the numeric designation 15818 refer to Klebsiella
pneumoniae, taxon 573, not this Helicobacter taxon. No identity or genome
association follows from the reused designation.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18354` supports stored identity, rank,
  parent, code and snapshot 2026-09-13. Each ancestor was checked against
  its own inventory row.
- `data/catalog/ncbi_names-0000.jsonl.gz:38367` supplies the scientific
  name under the exact target ID.
- `curation/seed_scope.tsv:144015` supports the one-source rationale in
  the seed event. The attestation correctly counts one NCBI NAME, not
  a genome or phenotype observation.
- No literature, gene, regulator, pathway, phenotype or transcriptomic
  claim is asserted. iModulonDB is not applicable.

## Completeness

Ignored-file-inclusive ID/full-name/slug searches covered reports, history,
curation, raw, ATB and StrainInfo uncompressed inventories. Only the target
taxonomy and scope rows matched. No prior target report, separate history
artifact or culture candidate was found by those keys.

Decompressed JSONL.GZ/TSV.GZ searches included ignored files under catalog,
BacDive, BV-BRC, GOLD and StrainInfo. Alongside target identity keys, exact
15818 values were searched in `strain`, `ncbi_strain_identifiers` and
`infraspecific_name` (including `strain=15818`). The target name and three
unrelated Klebsiella pneumoniae rows matched:

- `data/catalog/ncbi_genbank_historical-0001.jsonl.gz:13660`:
  GCA_028089775.1, suppressed, taxon 573.
- `data/catalog/ncbi_refseq_historical-0002.jsonl.gz:8768`:
  GCF_947661985.1, suppressed, taxon 573.
- `data/catalog/ncbi_genbank-0059.jsonl.gz:46620`:
  GCA_947661985.1, latest, taxon 573.

All three identify BioSample SAMEA112229013 and strain 15818 in Klebsiella;
none supports a link to Helicobacter. Arbitrary numeric substrings and every
possible alias field were not searched, and the ATB full TSV.XZ was not
scanned. The bounded search is not proof that the target has never been
deposited or sequenced. Empty optional slots and zero attached strains
remain consistent with the inspected target evidence.

## Findings

- **Blocker:** None found.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** Current NCBI gives `no rank`,
  while the inventory/YAML give `STRAIN`. The inspected importer,
  `src/taxonmech/ncbi_taxdump.py`, directly normalizes native ranks.
  The ignored-inclusive checkout filename search did not locate the
  archive pinned by `conf/ncbi_taxdump.yaml`. Source-version divergence
  versus import error remains unresolved.

## Recommended Edits

No generated-record edit is justified. Resolve the rank conflict against the
hash-verified pinned source before changing the configured snapshot or
importer. Preserve the identity boundary for reused numeric strain names.
Any demonstrated importer defect belongs in `src/taxonmech/ncbi_taxdump.py`
with a regression test, then normal extraction and seeding.

## Follow-up Checks

- Inspect taxon 103187 in the archive whose configured SHA256 is
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- After a separately authorized correction, refresh inputs, run
  `just seed-canary NCBITaxon:103187`, both target validators and full
  `just verify-corpus`.

## Additional Notes

The authority page was inspected through its link on the parent-species
page. External archive copies were not checked. No paid research, outbound
messages, GitHub mutation, history addition or review-status promotion occurred.
