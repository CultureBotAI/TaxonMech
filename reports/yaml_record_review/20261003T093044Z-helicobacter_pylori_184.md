# YAML Record Review: Helicobacter pylori 184

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_184.yaml`
- Started UTC: 2026-10-03T09:29:31Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:30:44Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:103185` denotes
Helicobacter pylori 184, rank `STRAIN`, in `BACTERIA` beneath species 210.
It contains ten ancestors, code 11, `EXACT` grounding, `SEEDED` mapping
status, zero attached strains, one NCBI NAME attestation and an embedded
seed event. There are no synonym, GTDB, nomenclature, genome or graph
assertions. Its index row is `data/taxa/PATHS.tsv:13145`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_184.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_184.yaml`:
  passed, one file and zero errors.
- Structured inventory checks matched ID, label, stored rank, parent,
  genetic code and all ten ancestor IDs, labels, ranks and parent links.
  A complete taxonomy parent-column scan found zero direct children.
- `git diff --exit-code -- data/taxa/bacteria/helicobacter_pylori_184.yaml`
  passed. No record or maintained input changed.
- `just verify-corpus` was skipped: only full-corpus reproduction is
  exposed. Full catalog hashes and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped: an ignored-inclusive target search
  found no separate history artifact. The embedded event was inspected
  and included in strict validation.

## Identity and Grounding

The inspected [NCBI 184 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103185&lvl=&mode=node)
confirms the target's ID, full label, code and lineage beneath H. pylori.
It reports `no rank`, not the stored `STRAIN`. Both representations place
the target below a species, within scope.

The numeric designation 184 is not globally unique. Source assembly and
genome hits with that designation include unrelated bacterial taxa and
cannot establish identity with this Helicobacter record.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:18352` supplies identity, stored rank,
  parent, code and snapshot 2026-09-13. Each ancestor was compared to its
  own source row.
- `data/catalog/ncbi_names-0000.jsonl.gz:38365` supplies the exact
  scientific name for taxon 103185.
- `curation/seed_scope.tsv:144013` supports the seed event's one-source
  rationale. One NCBI NAME attestation agrees with the source evidence;
  it is not a count of genomes or independent biological observations.
- No literature, gene, pathway, regulator, phenotype or expression-module
  claim is asserted. iModulonDB is not applicable.

## Completeness

Ignored-file-inclusive searches for the target ID, full name and slug covered
reports, history, curation, raw, ATB and StrainInfo uncompressed inventories.
Only the target taxonomy and scope rows matched. No prior target report,
separate history artifact or culture candidate was found by those keys.

Decompressed JSONL.GZ/TSV.GZ searches included ignored files under catalog,
BacDive, BV-BRC, GOLD and StrainInfo. Alongside the target keys, exact 184
values were sought in `strain`, `ncbi_strain_identifiers` and
`infraspecific_name` (including `strain=184`). All 88 matching JSON rows
were parsed for names and taxon IDs: one was the native target name and
87 were other taxa, with no additional Helicobacter match. Examples include
Lactococcus lactis subsp. lactis taxon 1360 (GCA_002078395.2),
Pseudomonas aeruginosa taxon 287 (GCF_900145265.1), and Escherichia coli
taxon 562 (GCA_916162085.1). No accession was transferred.

Arbitrary numeric substrings and every possible alias field were not searched;
the ATB full TSV.XZ was not scanned. These bounded results do not prove
the target has never been deposited or sequenced. Zero attached strains
and empty optional fields remain consistent with the inspected evidence.

## Findings

- **Blocker:** None found.
- **Major:** None found.
- **Minor (1): NCBI rank discrepancy.** The live browser gives `no rank`,
  whereas inventory/YAML give `STRAIN`. The inspected importer in
  `src/taxonmech/ncbi_taxdump.py` directly normalizes native ranks. The
  archive pinned in `conf/ncbi_taxdump.yaml` was not found by an
  ignored-inclusive checkout filename search. Source-version divergence
  versus import error remains unresolved.

## Recommended Edits

No immediate generated-record edit is supported. Check the hash-verified
pinned source before changing the configured snapshot or importer, and
retain the full taxon-identity boundary when evaluating numeric strain
designations. Any demonstrated importer defect belongs in
`src/taxonmech/ncbi_taxdump.py` with a regression test, followed by normal
extraction and seeding.

## Follow-up Checks

- Inspect taxon 103185 in the archive whose configured SHA256 is
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
- After a separately authorized correction, refresh the input, run
  `just seed-canary NCBITaxon:103185`, rerun both target validators and
  run full `just verify-corpus`.

## Additional Notes

The authority page was inspected through the parent-species page's link.
A structured projection recovered every expanded catalog-search hit after
raw tool output was truncated. External archive copies were not checked.
No paid research, outbound message, GitHub mutation, curation-history
addition or review-status promotion occurred.
