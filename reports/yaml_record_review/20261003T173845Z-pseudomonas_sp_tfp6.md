# YAML Record Review: Pseudomonas sp. TFP6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_tfp6.yaml`
- Started UTC: 2026-10-03T17:37:34Z
- Finished UTC: 2026-10-03T17:38:45Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303849`.
It asserts rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:196821`, genetic code 11, grounding `EXACT`, mapping
status `SEEDED`, ten lineage entries, one NCBI NAME attestation,
zero strains and one embedded seed event. Synonyms, nomenclature,
taxonomy mappings, equivalence xrefs, strain/genome links, experimental
claims and causal graph are not asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_tfp6.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_tfp6.yaml`:
  PASS; one file and zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduced identity, rank, parent,
  code and all ten lineage objects. No children occur. Complete
  exact-field source scans found no membership in seven other
  inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated
  products, exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.
- Original taxdump verification is unavailable: the configured
  `data/source_snapshots/` parent is absent, confirmed by an
  ignored-inclusive depth-one `find data`. No snapshot was downloaded.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308179` supports the exact label,
species rank, parent, code, empty synonym fields and 2026-09-13
snapshot. The native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30730` was read in full and
agrees. All ten ancestors independently match the pinned backbone:
root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas
and unclassified Pseudomonas. Preserve the parent's `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303849&retmode=xml)
confirms taxon 1303849, current label, species rank, parent 196821,
code 11 and the complete non-root lineage.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303849)
confirms label, rank and all ten ancestor IDs including root.
Exact grounding and the bacterial domain are supported. The isolate-like
label does not establish a registered deposit or justify changing rank.

EFetch also associates `Pseudomonas sp. TAS18` with this taxon as a
`misspelling`. That alternate name is absent from the local inventory,
native catalog and YAML. It must not become an exact synonym or an
independently inferred strain identity.

## Evidence

The NCBITAXON / NCBITaxon:1303849 / 1 NAME attestation agrees with
the backbone and snapshot. NAME is source coverage, not a biological
strain or genome count. No DOI, PMID, genome accession or experimental
quotation requires verification in the YAML.

`data/taxa/PATHS.tsv:106284` pins the slug.
`curation/seed_scope.tsv:393126` admits this taxon on 2026-09-13
with the exact one-source reason carried by the embedded event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` is appropriate;
this report does not grant human-review status.

## Completeness

Complete ignored-inclusive whole-token ID/label/slug/TFP6 searches
covered raw inventories, curation and history, returning only the
target backbone and scope rows. Full exact-field scans found no
direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits
membership. With no descendants, no descendant BacDive strains
contribute to the count; zero is supported by these inventories.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. ID, full label, slug and
TFP6 returned only the target scientific-name object. A separate
complete search for TAS18 and its full live name returned no match.

Complete ignored-inclusive ID/label/slug/TFP6 searches also covered
`data/atb/`, the entire `data/catalog/allthebacteria.tsv.xz`, and
StrainInfo link, assembly, exclusion and compressed related-record
tables, without a match. Separate TAS18/full-name searches covered
these tables plus raw inventories, curation and history, also without
a match. No eligible deposit/BioSample chain was established.

The empty optional biological fields are justified at this source
boundary, not proof that cultures or sequences do not exist elsewhere.
The live alternate-name discrepancy remains a limited completeness
issue. No gene, regulator, pathway, trait or transcriptomic assertion
is present; iModulonDB is not applicable. No graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor M1: Live alternative-name coverage differs from the local
  snapshot. EFetch identifies `Pseudomonas sp. TAS18` as a misspelling
  for taxon 1303849, but local native catalog, inventory and YAML omit
  it. Current identity and label remain sound. The missing original
  pinned archive prevents attributing the discrepancy to snapshot
  differences or an extraction omission. Maintained owners are
  `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py`,
  `src/taxonmech/extract.py` and `src/taxonmech/seed.py`.

## Recommended Edits

For M1, inspect this taxon's original name rows in the hash-verified
archive named by `conf/ncbi_taxdump.yaml`. If TAS18 is present,
trace its omission in maintained extraction/projection code and add
a regression test with any correction. If absent, preserve the current
snapshot and obtain the live name through an authorized future refresh.
The existing parser maps misspellings to `RELATED_SYNONYM`, and the
seeder emits the inventory's related synonyms; no code defect is proved
without the original snapshot comparison.

Do not hand-edit generated YAML, promote the misspelling to exact
equivalence, infer deposit/genome links from a bare designation, or
change the supported lineage and `SEEDED` status.

## Follow-up Checks

Resolve M1 by checking the configured archive's hash and exact name
rows against the native catalog and inventory. Test that misspellings
never become `EXACT_SYNONYM`. Any authorized correction requires the
documented dry-run/canary workflow and both focused validators after
regeneration. Full-corpus claims require `just verify-corpus` and
full QC, neither run here.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All evidence searches
and validators completed. Public NCBI metadata reads used network
escalation after established sandbox DNS failures. Committed source
projections were checked without claiming original-archive reproduction.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, previous report, history or
status was changed. No generator, refresh, paid research, GitHub action
or cross-repository write occurred. Eukaryota was not re-reviewed.
