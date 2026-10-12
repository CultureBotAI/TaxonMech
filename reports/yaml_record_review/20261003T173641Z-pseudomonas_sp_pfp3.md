# YAML Record Review: Pseudomonas sp. PFP3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_pfp3.yaml`
- Started UTC: 2026-10-03T17:35:26Z
- Finished UTC: 2026-10-03T17:36:41Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303848`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`,
genetic code 11, grounding `EXACT` and mapping status `SEEDED`.
Ten lineage entries, one NCBI NAME attestation, zero strains and one
embedded seed event are present. No synonyms, nomenclature, taxonomy
mappings, equivalence xrefs, strain/genome links, experiments or graph
are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_pfp3.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_pfp3.yaml`:
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
- Original taxdump verification was unavailable: direct path inspection
  and ignored-inclusive `find data -maxdepth 1 -name source_snapshots`
  confirmed that the configured archive's parent directory is absent.
  No download or source refresh was attempted.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308178` supplies the exact label, species
rank, parent, code, empty synonym fields and 2026-09-13 snapshot.
The complete native name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30729` agrees.
All ancestors match the pinned backbone, including root, cellular
organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria,
Pseudomonadales, Pseudomonadaceae, Pseudomonas and unclassified
Pseudomonas. Preserve the carried chain and the parent's `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303848&retmode=xml)
confirms ID, label, species rank, parent 196821, code 11 and the
complete non-root lineage.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303848)
confirms label, rank and all ten ancestor IDs including root.
Exact grounding and domain are supported. The isolate-like label is
not a culture-collection accession or a reason to change NCBI's rank.

EFetch also lists `Pseudomonas sp. TAS16` with class `misspelling`.
The local inventory, native name catalog and YAML omit that alternate
name. It is not an exact synonym or a separately established strain;
the bounded discrepancy is retained below.

## Evidence

The NCBITAXON / NCBITaxon:1303848 / 1 NAME attestation agrees with
the backbone and snapshot. NAME counts source coverage, not strains
or genomes. No DOI, PMID, assembly accession or experimental quotation
is asserted by the YAML.

`data/taxa/PATHS.tsv:106283` pins the slug.
`curation/seed_scope.tsv:393125` admits the taxon on 2026-09-13 with
the exact one-source reason carried by the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` remains accurate;
this review neither claims nor grants human-review status.

## Completeness

Complete ignored-inclusive whole-token ID/label/slug/PFP3 searches
covered raw inventories, curation and history and returned only the
target backbone and scope rows. Complete exact-field scans found no
direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits
membership. No descendants can contribute BacDive strains, supporting
the zero count.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. ID, full label, slug and
PFP3 returned only the target scientific-name object, read in full.
A second complete native search for TAS16 and its full live name
returned no match.

Complete ignored-inclusive ID/label/slug/PFP3 searches also covered
`data/atb/`, the full `data/catalog/allthebacteria.tsv.xz`, and
StrainInfo link, assembly, exclusion and compressed related-record
tables, without a match. Complete TAS16/full-name searches additionally
covered those tables, raw inventories, curation and history, also
without a match. No eligible target deposit/BioSample chain was
established within this boundary.

Empty optional biological fields are justified at the inspected source
boundary, not proof that no cultures or sequences exist elsewhere.
The live misspelling-name discrepancy remains a limited completeness
issue. No functional gene, regulator, pathway, trait or transcriptomic
assertion is present; iModulonDB is not applicable. No graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor M1: Live alternative-name coverage differs from the local
  snapshot. EFetch associates `Pseudomonas sp. TAS16` as a misspelling
  with taxon 1303848, but the local native catalog, raw inventory and
  generated YAML omit it. The correct current label and identity are
  unaffected. Without the original pinned archive, snapshot differences
  cannot be distinguished from an extraction omission. Maintained
  owners: `conf/ncbi_taxdump.yaml`, `src/taxonmech/ncbi_taxdump.py`,
  `src/taxonmech/extract.py` and `src/taxonmech/seed.py`. Do not
  hand-edit generated YAML or represent a misspelling as exact equivalence.

## Recommended Edits

For M1, inspect taxon 1303848 in the hash-verified original `names.dmp`
named by `conf/ncbi_taxdump.yaml`. If TAS16 is present, trace and
correct its omission in maintained extraction/projection code with a
regression test. If absent, preserve the existing snapshot and capture
the live name in a separately authorized refresh. The current parser
already classifies misspellings as `RELATED_SYNONYM`, and the seeder
emits the inventory's related synonyms. A code defect is not established
without the primary snapshot check.

Preserve identity, carried lineage, zero supported strain count and
`SEEDED` status. No source refresh, code change or YAML edit was made.

## Follow-up Checks

Resolve M1 against the configured archive and hash, comparing its exact
name rows with native catalog and inventory. Test that misspellings
never become `EXACT_SYNONYM`. Any authorized correction requires the
documented dry-run/canary workflow, then both focused validators after
regeneration. Corpus-wide claims additionally require
`just verify-corpus` and full QC, neither run here.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All evidence searches
and validators completed. Public NCBI metadata reads used network
escalation after established sandbox DNS failures. Committed
projections were inspected without claiming original-archive reproduction.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
