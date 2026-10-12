# YAML Record Review: Pseudomonas sp. BFP4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_bfp4.yaml`
- Started UTC: 2026-10-03T17:41:38Z
- Finished UTC: 2026-10-03T17:42:52Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303851`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`,
genetic code 11, grounding `EXACT` and mapping status `SEEDED`.
Ten lineage entries, one NCBI NAME attestation, zero strains and one
embedded seed event are present. No synonyms, nomenclature, taxonomy
mappings, equivalence xrefs, strain/genome links, experiments or graph
are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_bfp4.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_bfp4.yaml`:
  PASS; one file and zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduced identity, rank, parent,
  code and all ten lineage objects. No children occur. Complete
  exact-field scans found no membership in seven other inventories.
  PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated
  products, exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.
- The configured primary taxdump is unavailable: ignored-inclusive
  `find data -maxdepth 1 -name source_snapshots` confirms its parent
  directory is absent. No source download or refresh was attempted.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308181` supplies the exact label,
species rank, parent, code, empty synonym fields and 2026-09-13
snapshot. The complete native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30732` agrees.
All ten ancestors match the pinned backbone: root, cellular organisms,
Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria,
Pseudomonadales, Pseudomonadaceae, Pseudomonas and unclassified
Pseudomonas. Preserve the carried lineage and parent's `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303851&retmode=xml)
confirms ID, label, species rank, parent 196821, code 11 and the
complete non-root lineage.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303851)
confirms label, rank and all ten ancestor IDs including root.
Exact grounding and bacterial domain are supported. BFP4 is not
evidence of a registered deposit, type strain or different rank.

EFetch also lists `Pseudomonas sp. TAS2` as a `misspelling`.
The local native catalog, raw inventory and YAML omit that name.
It is not exact equivalence or an independently established strain
identity. The bounded source discrepancy is retained below.

## Evidence

The NCBITAXON / NCBITaxon:1303851 / 1 NAME attestation agrees with
the backbone and snapshot. NAME counts source coverage, not biological
strains or genomes. No DOI, PMID, assembly accession or experimental
quotation is asserted by the YAML.

`data/taxa/PATHS.tsv:106286` pins the slug.
`curation/seed_scope.tsv:393128` admits the taxon on 2026-09-13
with the exact one-source reason carried by the embedded event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` remains accurate;
this review does not grant human-review status.

## Completeness

Complete ignored-inclusive whole-token ID/label/slug/BFP4 searches
covered raw inventories, curation and history, returning only the
target backbone and scope rows. Complete exact-field scans found no
direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits
membership. No descendants can contribute BacDive strains, supporting
the zero count at the inventory boundary.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. ID, label, slug and BFP4
returned only the target scientific-name object. A separate complete
TAS2/full-live-name search returned eleven native objects, all read
in full; none identifies this Pseudomonas taxon.

The alternate-name search found these distinct identities:

- `data/bacdive/records.jsonl.gz:2232`, BacDive 2320, identifies
  Brevundimonas naejangsanensis BIO-TAS2-2, species 588932 and strain
  taxon 1121125. Its deposits DSM 23858, CCUG 57609 and KCTC 22631,
  type status, 16S FJ544245, assembly GCA_000421705, BV-BRC 1121125.3
  and IMG 2524614659 do not belong to Pseudomonas BFP4.
- `data/straininfo/records.jsonl.gz:299781`, SI-ID 401892, independently
  names Brevundimonas naejangsanensis, taxon 588932. Its own deposits
  LMG 29606 / SI-DP 26208, DSM 23858 / SI-DP 908856 and
  CCUG 57609 / SI-DP 919444, and the explicitly deposit-linked
  GCA_000421705, OM074022 and FR775457, concern that organism.
  Its BIO-TAS2-2 designation cannot transfer these links to Pseudomonas.
  Supplied unversioned genome accessions were not assigned a version.
- `data/catalog/ncbi_names-0006.jsonl.gz:5462` assigns synonym
  Brevundimonas sp. BIO-TAS2-2 to taxon 1121125. The corresponding
  `data/raw/ncbitaxon_taxa.tsv:242049`, BacDive row 2233 and
  type-material rows 239802-239803 likewise concern Brevundimonas.
- `data/gold/organisms.jsonl.gz:444011`, Go0613270, identifies
  Brevundimonas naejangsanensis BIO-TAS2-2, taxon 588932, without a
  culture-collection field. It supplies no Pseudomonas relationship.
- `data/gold/organisms.jsonl.gz:283058`, Go0389714, identifies
  Hymenogaster sp. TAS2, taxon 2136018. Six full GOLD project objects
  at lines 166760-166765 link Gp0251400 through Gp0251405 to that
  organism and name its gene-expression projects, with PRJNA440047
  through PRJNA440052 and their individual BioSamples. These are
  fungal projects, not Pseudomonas deposits or genomes. The source
  hits were excluded by identity; no Eukaryota YAML was re-reviewed.

Complete ignored-inclusive ID/label/slug/BFP4 searches also covered
`data/atb/`, the entire `data/catalog/allthebacteria.tsv.xz`, and
StrainInfo link, assembly, exclusion and compressed related-record
tables, without a match. TAS2/full-name searches covered these tables
plus raw inventories, curation and history; only the four unrelated
Brevundimonas raw rows described above matched. No eligible target
deposit/BioSample chain was established within these boundaries.

Empty optional biological fields are justified at the inspected source
boundary, not proof that no cultures or sequences exist elsewhere.
The live alternative-name discrepancy remains a limited completeness
issue. No gene, regulator, pathway, trait or transcriptomic assertion
is present in this YAML; iModulonDB is not applicable. Unrelated GOLD
expression projects do not change that scope. No graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor M1: Live alternative-name coverage differs from the local
  snapshot. EFetch associates `Pseudomonas sp. TAS2` as a misspelling
  with taxon 1303851, while local native catalog, inventory and YAML
  omit it. The correct current label and identity are unaffected.
  The missing original pinned archive prevents distinguishing snapshot
  differences from an extraction omission. Maintained owners:
  `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py`,
  `src/taxonmech/extract.py` and `src/taxonmech/seed.py`.

## Recommended Edits

For M1, inspect this taxon's exact name rows in the hash-verified
original archive named by `conf/ncbi_taxdump.yaml`. If TAS2 is
present, trace its omission through maintained extraction/projection
code and add a regression test with any correction. If absent,
preserve the snapshot and obtain the live name in an authorized
future refresh. The existing parser maps misspellings to
`RELATED_SYNONYM`, and the seeder emits inventory related synonyms;
no code defect is established without the primary snapshot comparison.

Do not patch generated YAML, promote the misspelling to exact
equivalence, join Brevundimonas deposits or fungal projects by TAS2,
or change the supported identity, lineage and `SEEDED` status.

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
