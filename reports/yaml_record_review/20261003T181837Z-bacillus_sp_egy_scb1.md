# YAML Record Review: Bacillus sp. EGY-SCB1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_egy_scb1.yaml`
- Started UTC: 2026-10-03T18:17:02Z
- Finished UTC: 2026-10-03T18:18:37Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303875`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:185979`,
code 11, grounding `EXACT` and mapping status `SEEDED`. Ten lineage
entries, one NCBI NAME attestation, zero strains and one embedded
seed event are present. No synonyms, nomenclature, taxonomy mappings,
equivalence xrefs, strain/genome links, experiments or graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bacillus_sp_egy_scb1.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/bacillus_sp_egy_scb1.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduced identity, rank, parent,
  code, empty synonym fields and all ten lineage objects. No children
  occur. Complete exact-field scans found no membership in seven other
  source inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only, with no invented
  focused substitute. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308193` supports the label, species
rank, parent, code, empty synonyms and 2026-09-13 snapshot. The full
scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30746` agrees. Every ancestor
matches the pinned backbone: root, cellular organisms, Bacteria,
Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae, Bacillus
and unclassified Bacillus (in: firmicutes). Preserve the entire
carried chain and the parent's `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303875&retmode=xml)
confirms ID, label, species rank, parent 185979, code 11 and the
complete non-root lineage. It supplies no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303875)
confirms label, rank and all ten ancestor identifiers, including root.
Exact grounding and bacterial domain are supported. NCBI still uses
the parent label's firmicutes qualifier; it is not a TaxonMech spelling
error to normalize. The isolate-like species label does not establish
a registered deposit, a type strain or grounds for changing the rank.

## Evidence

The NCBITAXON / NCBITaxon:1303875 / 1 NAME attestation agrees with
the backbone and snapshot. NAME counts source coverage, not cultures,
phenotypes or genomes. No DOI, PMID, assembly accession or experimental
quotation is asserted by this YAML.

`data/taxa/PATHS.tsv:106298` pins the slug.
`curation/seed_scope.tsv:393139` admits this species on 2026-09-13
with the exact one-source reason carried by the seed event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. YAML line folding does
not change the reason. `SEEDED` remains appropriate; this review
does not confer human-review status.

## Completeness

Complete ignored-inclusive whole-token ID, full-label, slug and
EGY-SCB1 searches covered raw inventories, curation and history,
returning only the target backbone and scope rows. Complete structured
exact-field scans found no direct BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits membership. With no descendants in
the inspected backbone, none can contribute BacDive strains. The zero
count is supported within these inventories.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. The same identifiers returned
only the target scientific-name object, read in full. No eligible
culture-deposit or explicit strain-genome chain was established.

Additional complete ignored-inclusive searches covered `data/atb/`,
the entire `data/catalog/allthebacteria.tsv.xz`, and StrainInfo TSV
and compressed TSV link, assembly, exclusion and related-record
tables, without a match. These bounded checks justify empty optional
fields; they are not proof that cultures or sequences cannot exist
elsewhere. No assertion about uninspected original archives is made.

No gene, regulator, pathway, trait or transcriptomic assertion is
present; iModulonDB is not applicable. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None. Preserve the supported identity, source lineage, zero strain
count and `SEEDED` status. Do not infer a registered deposit from
EGY-SCB1, join genomes by a shared taxon, or rewrite the parent label.
Future source additions belong in maintained extraction and source
inventories, followed by authorized seeding; never hand-edit this YAML.

## Follow-up Checks

No corrective check is required. After an authorized refresh, compare
this taxon's exact source rows and any explicit deposit/genome evidence
before rerunning both focused validators. Corpus-wide claims additionally
require `just verify-corpus` and full QC; neither was run here.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All searches and
validators completed. Public NCBI metadata reads used network escalation
after established sandbox DNS failures. Source projections were inspected
without claiming reproduction of original primary archives.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
