# YAML Record Review: Helicobacter pylori HP112

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/helicobacter_pylori_hp112.yaml`
- Started UTC: 2026-10-03T08:21:16Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T08:23:12Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:103169` denotes the
HP112 infraspecific taxon under `NCBITaxon:210`, Helicobacter pylori, not the
species as a whole or a similarly named gene. The YAML declares `STRAIN`,
`BACTERIA`, `EXACT` grounding, `SEEDED` mapping status, genetic code 11, zero
attached BacDive strains and one NCBI name attestation. Its sole history event
is the 2026-09-13 seeding event. The target is at `data/taxa/PATHS.tsv:13118`.

## Validation

- `just validate data/taxa/bacteria/helicobacter_pylori_hp112.yaml`: passed,
  no issues found.
- `just validate-strict data/taxa/bacteria/helicobacter_pylori_hp112.yaml`:
  passed, one file scanned and zero errors.
- A structured YAML/TSV comparison checked the target label, rank, parent and
  genetic code, and every ID, label, rank and parent link in the ten-entry
  root-first lineage against `data/raw/ncbitaxon_taxa.tsv`: all matched.
- A complete structured scan of that taxonomy inventory found zero children
  of this taxon. Together with the source searches below, this supports the
  empty attached-strain listing without overlooking descendant aggregation.
- `just verify-corpus` was not rerun: the recipe is full-corpus-only. These
  focused comparisons do not constitute a new full-corpus reproduction pass.
- `just validate-products` was not run: its OAK checks concern causal-graph
  groundings; this record has no causal graph.
- `just validate-history` was not run: the ignored-file-inclusive target
  search found no separate history artifact. The embedded event was inspected
  and covered by strict validation. No history artifact was created.
- Full catalog hash/census and rendered-site checks were not rerun. No source
  inventories, generated record or page were changed.

## Identity and Grounding

The inspected [NCBI HP112 page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103169&lvl=&mode=node)
agrees on taxon ID, scientific name, genetic code 11 and the displayed
species-to-domain ancestry. The separate [species tree](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=210)
lists HP112 beneath Helicobacter pylori, separately from HP125 and HP131.
The pinned taxonomy inventory supports all ancestor identifiers and ranks,
including the additional root entry. No identity or domain conflict was found.

The source-browser rank is `no rank`, whereas the pinned inventory and YAML
say `STRAIN`. This discrepancy remains unresolved; it was not silently
normalized away. Both representations remain eligible under the repository's
species-and-below scope rule because the immediate parent is a species.

## Evidence

| Assertion | Inspected support |
| --- | --- |
| ID, label, parent, code, stored rank and snapshot | `data/raw/ncbitaxon_taxa.tsv:18336` has NCBITaxon:103169, HP112, parent 210, code 11, STRAIN and snapshot 2026-09-13. The live rank qualification is recorded above. |
| Scientific name | `data/catalog/ncbi_names-0000.jsonl.gz:38349` contains the exact scientific-name assertion. No alternate name was found in the bounded native-source search. |
| NCBI attestation | The inventory has `attested_by=ncbitaxon`; the YAML retains one `NAME` assertion for this ID and label, not a phenotype or genome assertion. |
| Scope and seed history | `curation/seed_scope.tsv:143997` supplies the target's 2026-09-13 inclusion and one-source rationale, agreeing with the embedded seed event. The event records generation, not human review approval. |

There are no record-level citations, LPSN names, GTDB mappings, BacDive
deposits, assembly accessions or causal edges requiring independent claim
verification in this YAML. Parent-species nomenclature and other strains'
genomes were not transferred to HP112.

## Completeness

Identifier, exact label and slug were searched with `rg --no-ignore --hidden`
in `data/raw/`, `data/atb/`, `data/straininfo/`, `curation/`, `history/` and
`reports/yaml_record_review/`. The uncompressed inventory search covered TSV
and YAML files; compressed-source searches used `rg -z` over JSONL.GZ,
TSV.GZ and TSV.XZ files in `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/` and `data/straininfo/`. Numeric source taxonomy fields were included
in the query, and a second search checked the standalone designation HP112.
The only native-catalog hit was the NCBI scientific-name row. The only
uncompressed inventory hit was the taxonomy row. No prior target report or
separate history entry was found. All these searches included ignored files;
the conclusions are limited to the specified source surfaces.

`strain_count: 0` means no supported attached BacDive strain, not that the
taxon lacks a physical strain, sequence or biological characteristics.
Optional definition, evidence and causal-graph slots need not be invented.
The unresolved source-rank discrepancy is the only finding.

## Findings

- **Blocker:** None found.
- **Major:** None found.
- **Minor (1): Unresolved NCBI rank discrepancy.** The accessible NCBI browser
  reports `no rank`; `data/raw/ncbitaxon_taxa.tsv` and the generated YAML
  report `STRAIN`. `src/taxonmech/ncbi_taxdump.py:load_taxdump` reads the source
  rank directly, uppercases it and replaces spaces with underscores; it does
  not infer strain rank from HP112. The pinned archive named in
  `conf/ncbi_taxdump.yaml` was unavailable locally, preventing a direct
  comparison with its original `nodes.dmp` row. This may be source-version
  divergence rather than an importer defect. Identity, parentage and scope
  eligibility are unaffected. Ownership is the pinned NCBI input/configuration
  and its importer, not the generated YAML.

## Recommended Edits

No immediate record edit is justified. First compare taxon 103169 in the
hash-verified archive pinned by `conf/ncbi_taxdump.yaml` with a dated current
NCBI source. If the pinned row says `strain`, retain the reproducible value
until an authorized source refresh. If it says `no rank`, correct the owning
extraction path in `src/taxonmech/ncbi_taxdump.py` or its inventory integration,
with a regression test, then re-extract and regenerate. Do not infer a rank
from a strain-like label or patch the YAML directly.

## Follow-up Checks

1. Recover the archive with SHA256
   `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`;
   inspect the exact `nodes.dmp` row before attributing the discrepancy to code.
2. After any separately authorized correction, run the relevant
   `tests/test_ncbi_taxdump.py` tests, re-extract, seed the target through
   `just seed-canary NCBITaxon:103169`, repeat both target validators and run
   the full `just verify-corpus`.
3. Keep the current parent, scientific name, empty source-specific assertions
   and history/status boundaries unless new exact-target evidence warrants
   a change.

## Additional Notes

The browser page was obtained through NCBI's species-tree link after direct
URL attempts failed. A second NCBI Datasets API check was unavailable, so it
does not resolve the rank discrepancy. An ignored-file-inclusive repository
filename search for taxdump/nodes artifacts found the configuration, importer,
test and bytecode files, but no archive or `nodes.dmp`; the configured
`data/source_snapshots/` directory was also unavailable. No claim is made
about archives outside this repository.

iModulonDB is not applicable: HP112 is the taxon designation here, not a gene
or transcriptomic claim. No paid research, external messages, GitHub changes,
history additions or status promotion were performed.
