# YAML Record Review: Pseudomonas sp. GFP8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_gfp8.yaml`
- Started UTC: 2026-10-03T17:39:41Z
- Finished UTC: 2026-10-03T17:40:50Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303850`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`,
genetic code 11, grounding `EXACT` and mapping status `SEEDED`.
There are ten lineage entries, one NCBI NAME attestation, zero strains
and one embedded seed event. No synonyms, nomenclature, taxonomy
mappings, equivalence xrefs, strain/genome links, experiments or graph
are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_gfp8.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_gfp8.yaml`:
  PASS; one file and zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured comparison reproduced backbone identity, rank, parent,
  code and all ten lineage objects. No children occur. Complete
  exact-field scans found no membership in seven other inventories.
  PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated
  products, exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.
- The configured primary taxdump cannot be checked: ignored-inclusive
  `find data -maxdepth 1 -name source_snapshots` confirms its parent
  directory is absent. No source download or refresh was attempted.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308180` supplies the exact label,
species rank, parent, code, empty synonym fields and 2026-09-13
snapshot. The complete native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30731` agrees.
All ten ancestors independently match the pinned backbone: root,
cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota,
Gammaproteobacteria, Pseudomonadales, Pseudomonadaceae, Pseudomonas
and unclassified Pseudomonas. Preserve the carried lineage and
the unclassified parent's `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303850&retmode=xml)
confirms ID, current label, species rank, parent 196821, genetic code
11 and the complete non-root lineage.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303850)
confirms label, rank and all ten ancestor IDs including root.
Exact grounding and domain are supported. The isolate-like label does
not prove a culture-collection accession or justify a rank change.

EFetch also lists `Pseudomonas sp. TAS19` with class `misspelling`.
The local native catalog, raw inventory and YAML omit this alternate
name. A misspelling is not exact equivalence or a separately established
strain identity. The source discrepancy is preserved below.

## Evidence

The NCBITAXON / NCBITaxon:1303850 / 1 NAME attestation matches
the backbone and snapshot. NAME counts source coverage, not strains
or genomes. No DOI, PMID, assembly accession or experimental quotation
is asserted by the YAML.

`data/taxa/PATHS.tsv:106285` pins the slug.
`curation/seed_scope.tsv:393127` admits this taxon on 2026-09-13
with the exact one-source reason carried by the embedded event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` remains correct;
this report does not confer human-review status.

## Completeness

Complete ignored-inclusive whole-token ID/label/slug/GFP8 searches
covered raw inventories, curation and history, returning only the
target backbone and scope rows. Full exact-field scans found no
direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits
membership. No descendants can contribute BacDive strains, supporting
the zero count within the inventories.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. ID, label, slug and GFP8
returned only the target scientific-name object, read in full.
A separate complete native search for TAS19 and its full live name
returned no match.

Complete ignored-inclusive ID/label/slug/GFP8 searches also covered
`data/atb/`, the entire `data/catalog/allthebacteria.tsv.xz`, and
StrainInfo link, assembly, exclusion and compressed related-record
tables, without a match. TAS19/full-name searches covered those
tables, raw inventories, curation and history, also without a match.
No eligible target deposit/BioSample chain was established.

Empty optional biological fields are justified within the inspected
source boundary, not proof that no cultures or sequences exist elsewhere.
The live alternative-name discrepancy remains a limited completeness
issue. No gene, regulator, pathway, trait or transcriptomic assertion
is present; iModulonDB is not applicable. No graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor M1: Live alternative-name coverage differs from the local
  snapshot. EFetch associates `Pseudomonas sp. TAS19` as a misspelling
  with taxon 1303850, while native catalog, inventory and YAML omit
  it. Current identity and label remain correct. Without the original
  pinned archive, a snapshot difference cannot be distinguished from
  extraction loss. Maintained owners: `conf/ncbi_taxdump.yaml`,
  `src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
  `src/taxonmech/seed.py`.

## Recommended Edits

For M1, inspect taxon 1303850 in the hash-verified original name rows
specified by `conf/ncbi_taxdump.yaml`. If TAS19 is present, trace
its omission through maintained extraction/projection code and add a
regression test with any correction. If absent, preserve the existing
snapshot and obtain the live name in an authorized future refresh.
The current parser maps misspellings to `RELATED_SYNONYM`, and the
seeder emits inventory related synonyms. No code defect is established
without the original snapshot comparison.

Do not hand-edit generated YAML, promote a misspelling to exact
equivalence, infer a deposit/genome relationship from a bare designation,
or change supported identity, lineage and `SEEDED` status.

## Follow-up Checks

Resolve M1 using the configured archive hash and exact name rows,
then compare native catalog and inventory. Test that misspellings
never become `EXACT_SYNONYM`. Any authorized correction requires
the documented dry-run/canary workflow and both focused validators
after regeneration. Full-corpus claims additionally require
`just verify-corpus` and full QC, neither run here.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All evidence searches
and validators completed. Public NCBI metadata reads used network
escalation after established sandbox DNS failures. Committed source
projections were inspected without claiming primary-archive reproduction.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
