# YAML Record Review: Campylobacter sputorum biovar fecalis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/campylobacter_sputorum_biovar_fecalis.yaml`
- Started UTC: 2026-10-03T09:39:51Z (first recorded checkpoint)
- Finished UTC: 2026-10-03T09:43:41Z
- Verdict: pass with minor issues

## Target

The full generated `TaxonRecord` was read. `NCBITaxon:1031919` denotes
Campylobacter sputorum biovar fecalis, `NO_RANK`, beneath species 206 in
`BACTERIA`. It has ten ancestors, code 11, `EXACT` grounding, `SEEDED`
mapping status, five NCBI synonyms, zero attached BacDive strains, one
NCBI NAME attestation and a seed event. No nomenclature, GTDB mapping,
genome, phenotype or graph assertion is present. Its index entry is
`data/taxa/PATHS.tsv:13149`.

## Validation

- `just validate data/taxa/bacteria/campylobacter_sputorum_biovar_fecalis.yaml`:
  passed, no issues found.
- `just validate-strict data/taxa/bacteria/campylobacter_sputorum_biovar_fecalis.yaml`:
  passed, one file and zero errors.
- Structured checks matched identity, rank, parent, code, all ten ancestor
  IDs/labels/ranks/parent links and all five synonym values/scopes/sources.
  The full subtree contains only this taxon and child 1031920; a complete
  BacDive inventory scan found no strains classified in that subtree.
- `just straininfo-query --strain SI-ID13604 --evidence --limit 20`:
  passed, three matched deposit paths. The query checks source/configuration
  and hashes with `reproduce=False`, not full source replay. Native and
  committed rows independently confirmed the deposit-specific assembly.
- `git diff --exit-code -- data/taxa/bacteria/campylobacter_sputorum_biovar_fecalis.yaml`
  passed. No record or maintained input changed.
- `just verify-corpus` was skipped: it is full-corpus-only. Full catalog
  reproduction and generated pages were not checked.
- `just validate-products` is not applicable without graph nodes.
  `just validate-history` was skipped because the ignored-inclusive target
  search found no separate history artifact. The embedded event was read
  and included in strict validation.

## Identity and Grounding

The inspected [NCBI target page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=1031919&lvl=&mode=node)
supports the ID, name, no-rank status, code and species parent. Its tree
places CCUG 20703 (taxon 1031920) beneath this biovar. The spelling
faecalis is an orthographic equivalent, not a separate taxon to merge by
inference. Current NCBI also lists the shorter equivalent Campylobacter
faecalis, which is absent from the pinned target names.

The inspected abstract of [On et al. (1998)](https://pubmed.ncbi.nlm.nih.gov/9542089/),
DOI 10.1099/00207713-48-1-195, supports recognizing fecalis as a biovar
within C. sputorum. It does not justify promoting this record to species
or projecting a biochemical claim into every stored strain.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:220788` supports the stored identity,
  rank, parent, code, synonyms and snapshot date 2026-09-13.
- Six native rows at `data/catalog/ncbi_names-0005.jsonl.gz:29986`
  onward provide one scientific name and five other names. Three are
  native synonym/equivalent-name entries and two are authority strings.
  The exact/related scopes agree with `src/taxonmech/ncbi_taxdump.py`.
- `curation/seed_scope.tsv:321182` supports the one-source seed rationale.
  `data/raw/ncbi_merged_ids.tsv:7001` retains old ID 119231 as redirect
  evidence to this target; no other source ID was silently rewritten.
- Structured StrainInfo tables contain 27 deposit paths on 20 distinct
  local strains with source taxon 1031919, one assembly assertion, and
  57 related assertions: 27 deposit, 27 strain and three nucleotide rows.
  All 20 corresponding BacDive inventory records are classified at
  species 206, not in this target's subtree.
- Full native SI-ID13604, `data/straininfo/records.jsonl.gz:13604`,
  identifies CCUG 20703 / SI-DP52020, LMG 8532 / SI-DP52018 and CIP
  105558 / SI-DP149640. Only CCUG 20703 explicitly supplies the unversioned
  GCA_002220735. Preserve DOI 10.60712/SI-ID13604.2 as a source-record
  version, not a publication or deposit ID; do not append `.1` to that
  source's assembly assertion or transfer it to another deposit.
- The inspected [BacDive 134440 page](https://bacdive.dsmz.de/strain/134440)
  confirms the three deposits, taxon 206 and genome metadata naming child
  1031920. Native BV-BRC `bvbrc-0000.jsonl.gz:3102` and GTDB
  `gtdb_genomes-0004.jsonl.gz:33531` likewise identify the CCUG 20703
  genome at the child taxon. Genome classification does not override the
  strain's BacDive classification.
- The corresponding strain entry in `data/taxa/bacteria/campylobacter_sputorum.yaml`
  retains these assembly/genome/related assertions on the parent species.
  They are not globally lost from the corpus. This was a focused context
  check, not a review verdict on the whole species record.

iModulonDB is not applicable to this taxon/name record. Sequence descriptions
were used to distinguish reference types, not to infer functional traits.

## Completeness

Ignored-file-inclusive ID/name/slug and fecalis/faecalis spelling searches
covered reports, history, curation, raw, ATB and StrainInfo inventories.
No prior target review or separate history artifact was found. Decompressed
JSONL.GZ/TSV.GZ searches also included ignored files under catalog, BacDive,
BV-BRC, GOLD and StrainInfo. Truncated raw output was recovered with JSON
and CSV parsing; the native matches comprised six NCBI name rows, 20
StrainInfo source records, one BV-BRC and one GTDB row.

The seeder gathers only BacDive strains classified in the NCBI subtree;
the StrainInfo overlay does not reclassify them. Zero attached strains is
consistent with that contract, not proof of no biovar cultures or genomes.
Source disagreement must remain explicit. For example, SI-ID13601 groups
a biovar-fecalis CCUG deposit with an LMG deposit assigned to C.
hyointestinalis; SI-ID1569 likewise has different biovar labels across
deposits. Group membership cannot settle taxonomic identity or transfer
sequences.

The full ATB TSV.XZ was not scanned. Individual live pages and sequences
for all 20 StrainInfo candidates were not audited. The live SI-ID13604 page
returned a JavaScript shell; its native projection and matched inventory
were inspected instead. No global absence of additional evidence is claimed.

## Findings

- **Blocker:** None found.
- **Major:** None found. The stored rank agrees with NCBI, and the zero
  count follows the documented BacDive classification boundary.
- **Minor (1): Name-snapshot freshness.** Current NCBI lists Campylobacter
  faecalis as an additional orthographic equivalent absent from this
  pinned target's native names and YAML. Determine whether a source
  refresh, rather than an importer change, is required. The maintained
  owners are `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`;
  do not manually insert a generated synonym.
- **Minor (2): Alternate source classifications are not discoverable here.**
  Deposit/sequence context with StrainInfo taxon 1031919 is retained on
  species-level BacDive strains, not surfaced on this biovar record.
  This is a non-blocking visibility limitation, not justification for
  changing `strain_count` or silently reconciling sources. Any source-aware
  navigation or representation change belongs in the seeder/templates and
  `docs/HARMONIZATION.md` / `docs/STRAININFO.md` with explicit provenance.

## Recommended Edits

No direct YAML edit is justified. Compare the current name set against the
hash-verified pinned taxonomy before planning a refresh. For improved
discoverability, design an explicitly source-labeled link to already stored
culture assertions without relocating strains or treating a source's
taxonomic statement as consensus. Preserve the same-deposit sequence rule.

## Follow-up Checks

- Inspect target names in the NCBI archive pinned by SHA256
  `8b32317216712ecf04f4c9b65e7ab82dacbd0a0e5512dd7aa904e24cc6bc0955`.
  An ignored-inclusive checkout filename search did not locate that archive.
- Retry native live StrainInfo/CCUG verification before publishing new
  classification links; no source group should be reassigned wholesale.
- After separately authorized input or presentation changes, run the
  relevant name/deposit/classification tests, normal input refresh,
  `just seed-canary NCBITaxon:1031919`, both target validators and full
  `just verify-corpus`; check generated pages if templates change.

## Additional Notes

The NCBI node page succeeded through its tree link after direct requests
failed. An initial auxiliary inventory check used singular `taxon_id`
instead of BacDive's `taxon_ids`; it was corrected and rerun successfully.
No paid research, outbound messages, GitHub mutation, curation-history
addition or review-status promotion occurred.
