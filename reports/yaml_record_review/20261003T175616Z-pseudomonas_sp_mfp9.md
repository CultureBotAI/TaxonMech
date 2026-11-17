# YAML Record Review: Pseudomonas sp. MFP9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_mfp9.yaml`
- Started UTC: 2026-10-03T17:54:56Z
- Finished UTC: 2026-10-03T17:56:16Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303857`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`,
code 11, grounding `EXACT` and mapping status `SEEDED`. Ten lineage
entries, one NCBI NAME attestation, zero strains and one embedded
seed event are present. No synonyms, nomenclature, taxonomy mappings,
equivalence xrefs, strain/genome links, experiments or graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_mfp9.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_mfp9.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduced identity, rank, parent,
  code and all ten lineage objects. No children occur. Complete
  exact-field scans found no membership in seven other inventories.
  PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only, with no invented
  focused substitute. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.
- The configured original taxdump is unavailable: ignored-inclusive
  `find data -maxdepth 1 -name source_snapshots` confirms its parent
  directory is absent. No source download or refresh was attempted.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308187` supports the exact label,
species rank, parent, code, empty synonym fields and 2026-09-13
snapshot. The full scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30738` agrees. Every ancestor
matches the pinned backbone: root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales,
Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas.
Preserve the carried lineage and the parent's `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303857&retmode=xml)
confirms ID, label, species rank, parent 196821, code 11 and the
complete non-root lineage.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303857)
confirms label, rank and all ten ancestor IDs including root.
Exact grounding and bacterial domain are supported. MFP9 is not
a registered deposit, type-strain claim or reason to change rank.

EFetch also lists `Pseudomonas sp. TAS4` as a `misspelling`.
The local native catalog, raw inventory and YAML omit that alternate
name. It must not become exact equivalence or a separately inferred
strain identity. The source discrepancy is retained below.

## Evidence

The NCBITAXON / NCBITaxon:1303857 / 1 NAME attestation agrees
with the backbone and snapshot. NAME counts source coverage, not
biological strains or genomes. No DOI, PMID, assembly accession or
experimental quotation is asserted by the YAML.

`data/taxa/PATHS.tsv:106292` pins the slug.
`curation/seed_scope.tsv:393134` admits the taxon on 2026-09-13
with the exact one-source reason carried by the embedded event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` remains
appropriate; this report does not grant human-review status.

## Completeness

Complete ignored-inclusive whole-token ID/label/slug/MFP9 searches
covered raw inventories, curation and history, returning only target
backbone and scope rows. Full exact-field scans found no direct
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits membership.
No descendants can contribute BacDive strains, supporting the zero
count within those inventories.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. ID, full label, slug and
MFP9 returned only the target scientific-name object, read in full.
A separate complete TAS4/full-live-name search returned eleven
native objects, all read in full; none identifies this Pseudomonas taxon.

Important exclusions from the alternate-name search:

- `data/bacdive/records.jsonl.gz:10389`, BacDive 10529, identifies
  Jeongeupia naejangsanensis BIO-TAS4-2, taxon 613195. Its deposits
  DSM 24253, CCUG 57610 and KCTC 22633, type status, 16S FJ669217,
  assemblies GCA_016865585 and GCA_042663185, BV-BRC 613195.3 and
  IMG 2994949654 do not belong to Pseudomonas MFP9.
- `data/straininfo/records.jsonl.gz:304699`, SI-ID 406810, also
  identifies Jeongeupia taxon 613195. It explicitly attaches
  GCA_016865585 to its own DSM 24253 / SI-DP 914139 deposit and
  names CCUG 57610 / SI-DP 916309 as another deposit. The
  BIO-TAS4-2 designation cannot transfer these relationships to
  Pseudomonas. Supplied unversioned accessions were not given a version.
- `data/catalog/ncbi_names-0003.jsonl.gz:40207` assigns the
  `includes` name Neisseriaceae bacterium BIO-TAS4-2 to taxon 613195.
  The corresponding backbone row 142674, BacDive inventory row 10390
  and type-material rows 241783-241784 also concern Jeongeupia.
- `data/gold/organisms.jsonl.gz:444323`, Go0613588, identifies
  Jeongeupia naejangsanensis BIO-TAS4-2, taxon 613195, without a
  culture-collection field. It does not establish Pseudomonas identity.
- `data/gold/organisms.jsonl.gz:283056`, Go0389712, identifies
  Zelleromyces sp. TAS4, taxon 2136034. Six full GOLD project objects
  at lines 166748-166753 link Gp0251388 through Gp0251393 to that
  organism, naming its gene-expression projects, PRJNA440035 through
  PRJNA440040 and their individual BioSamples. These are fungal
  projects, not Pseudomonas deposits or genomes. The source hits
  were excluded by identity; no Eukaryota YAML was re-reviewed.

Complete ignored-inclusive ID/label/slug/MFP9 searches also covered
`data/atb/`, the entire `data/catalog/allthebacteria.tsv.xz`, and
StrainInfo link, assembly, exclusion and compressed related-record
tables, without a match. TAS4/full-name searches covered these tables
plus raw inventories, curation and history; only the four unrelated
Jeongeupia raw rows described above matched. No eligible target
deposit/BioSample chain was established within these boundaries.

Empty optional biological fields are justified at the inspected source
boundary, not proof that cultures or sequences do not exist elsewhere.
The live alternate-name discrepancy remains a limited completeness
issue. No gene, regulator, pathway, trait or transcriptomic assertion
is present in the YAML; iModulonDB is not applicable. Unrelated GOLD
expression projects do not change that scope. No graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor M1: Live alternative-name coverage differs from the local
  snapshot. EFetch associates `Pseudomonas sp. TAS4` as a misspelling
  with taxon 1303857, while native catalog, inventory and YAML omit
  it. Current identity and label remain sound. The missing original
  pinned archive prevents distinguishing snapshot differences from
  extraction loss. Maintained owners: `conf/ncbi_taxdump.yaml`,
  `src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
  `src/taxonmech/seed.py`.

## Recommended Edits

For M1, inspect this taxon's exact name rows in the hash-verified
original archive named by `conf/ncbi_taxdump.yaml`. If TAS4 is
present, trace its omission through maintained extraction/projection
code and add a regression test with any correction. If absent,
preserve the snapshot and obtain the live name in an authorized
future refresh. The parser already maps misspellings to
`RELATED_SYNONYM`, and the seeder emits inventory related synonyms;
no code defect is established without the original snapshot check.

Do not patch generated YAML, promote a misspelling to exact
equivalence, join Jeongeupia deposits or fungal projects by TAS4,
or change the supported identity, lineage and `SEEDED` status.

## Follow-up Checks

Resolve M1 using the configured archive hash and exact name rows,
then compare native catalog and inventory. Test that misspellings
never become `EXACT_SYNONYM`. Authorized corrections require the
documented dry-run/canary workflow and both focused validators after
regeneration. Corpus-wide claims additionally require
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
