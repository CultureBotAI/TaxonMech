# YAML Record Review: Pseudomonas sp. OFP4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_ofp4.yaml`
- Started UTC: 2026-10-03T17:27:18Z
- Finished UTC: 2026-10-03T17:33:42Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303847`.
It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`,
genetic code 11, grounding `EXACT` and mapping status `SEEDED`.
Ten lineage entries, one NCBI NAME attestation, zero strains and one
embedded seed event are present. No synonyms, nomenclature, taxonomy
mappings, equivalence xrefs, strain/genome links, experiments or graph
are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_ofp4.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_ofp4.yaml`:
  PASS; one file and zero errors. Standard diagnostic:
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduced identity, rank, parent,
  code and all ten lineage objects. No children occur. Complete
  exact-field scans found no membership in the seven other source
  inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.
- Reading the configured primary NCBI archive failed with
  `FileNotFoundError`. A repository-wide `find`, including ignored files,
  found no taxdump archive. Its original name rows and checksum could not
  be verified; no download or source refresh was attempted.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308177` supplies the exact label, species
rank, parent, code, empty synonym fields and 2026-09-13 snapshot.
The full native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30728` agrees.
Every ancestor matches the pinned backbone, including Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales,
Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303847&retmode=xml)
confirms ID, label, species rank, parent 196821, genetic code 11 and
the complete non-root lineage.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303847)
confirms the label, rank and all ten ancestor IDs including root.
Exact grounding and the bacterial domain are supported. OFP4 is not a
culture-collection accession or a reason to change NCBI's species rank.

Live EFetch additionally lists `Pseudomonas sp. TAS10` with name class
`misspelling`. That is not an exact synonym or a separate strain identity.
The local inventory and native name catalog do not carry it. This bounded
alternative-name discrepancy is retained below, not silently reconciled.

## Evidence

The NCBITAXON / NCBITaxon:1303847 / 1 NAME attestation agrees with
the backbone and snapshot. NAME counts source coverage, not biological
strains or genomes. No DOI, PMID, assembly identifier or experimental
quotation is asserted by the YAML.

`data/taxa/PATHS.tsv:106282` pins the slug.
`curation/seed_scope.tsv:393124` admits the taxon on 2026-09-13 with
the exact one-source reason carried by the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` remains accurate;
this review neither claims nor grants human-review status.

## Completeness

Complete ignored-inclusive whole-token ID/label/slug/OFP4 searches
covered raw inventories, curation and history. Complete exact-field scans
found no direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits
membership. There are no descendants to contribute BacDive strains,
supporting the zero count.

Ignored-inclusive compressed JSONL searches covered `data/catalog/`,
`data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/` and
`data/straininfo/`. The complete ID/label/slug/OFP4 search returned three
objects, all read in full: the target NCBI name and two GOLD records.
`data/gold/projects.jsonl.gz:477926` is Gp0640166, a biofertilizer
microbial-community project from Xiamen, China, sample OFP4,
PRJNA744040 / SAMN20066010, without an organism GOLD ID.
`data/gold/analyses.jsonl.gz:358512` is Ga0549326, a metagenome
analysis linked to that project, also without an organism GOLD ID or
genome accession. Neither establishes a Pseudomonas culture or a
deposit-specific genome relationship.

Additional complete native searches for TAS10 and its full live name
returned only `data/gold/organisms.jsonl.gz:310646`, read in full:
Go0452922 is Cortinarius abnormis PSC4364-TAS10, taxon 231915,
without a culture-collection accession. This unrelated fungal source
hit was excluded by identity; no Eukaryota YAML was re-reviewed.

Complete ignored-inclusive ID/label/slug/OFP4 searches also covered
`data/atb/`, the full `data/catalog/allthebacteria.tsv.xz`, and
StrainInfo link, assembly, exclusion and compressed related-record
tables. No match occurred in that boundary. Complete TAS10/full-name
searches additionally covered these tables, raw inventories, curation
and history, with no match. No eligible target deposit/BioSample chain
was established within the inspected sources.

Empty optional biological fields are justified at this source boundary,
not proof that no isolates or sequences exist elsewhere. The live
misspelling-name discrepancy remains a limited completeness issue.
No functional gene, regulator, pathway, trait or transcriptomic assertion
is present; iModulonDB is not applicable. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor M1: Live alternative-name coverage differs from the local
  snapshot. EFetch explicitly associates `Pseudomonas sp. TAS10` as a
  misspelling with taxon 1303847, while the raw inventory, native name
  catalog and generated YAML omit it. Identity and the supported current
  label remain correct. The missing original pinned archive prevents
  attributing this discrepancy to snapshot differences or an extraction
  omission. Maintained owners: the source pin in `conf/ncbi_taxdump.yaml`,
  name-class extraction in `src/taxonmech/ncbi_taxdump.py`, inventory
  extraction in `src/taxonmech/extract.py`, and synonym emission in
  `src/taxonmech/seed.py`. Do not hand-edit generated YAML or upgrade the
  misspelling to an exact synonym.

## Recommended Edits

For M1, first inspect taxon 1303847 in the hash-verified original
`names.dmp` named by `conf/ncbi_taxdump.yaml`. If TAS10 is present,
trace why the maintained extraction/projection omitted it and add a
targeted regression test with the correction. If it is absent, preserve
the existing snapshot and capture the live name in a separately
authorized source refresh. The existing parser maps non-scientific
names other than synonym/equivalent-name classes to `RELATED_SYNONYM`;
the seeder already emits the inventory's related synonyms. No code
change is established as necessary without the primary snapshot check.

Preserve identity, lineage, zero supported strain count and `SEEDED`
status. Do not join the GOLD community sample or fungal TAS10 record
by bare designation. No changes were made by this review.

## Follow-up Checks

Resolve M1 using the configured primary archive and source hash, compare
its exact name rows with the native catalog and raw inventory, and test
that a misspelling is never emitted as `EXACT_SYNONYM`. Any authorized
refresh or extraction correction requires the documented dry-run and
canary workflow, then both focused validators after regeneration.
Corpus-wide claims additionally require `just verify-corpus` and full
QC, neither run in this focused review.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All evidence searches
and validators completed. The original configured taxdump archive is
unavailable in this checkout; committed projections were inspected
without claiming primary-archive reproduction. Public NCBI metadata
reads used network escalation after established sandbox DNS failures.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
