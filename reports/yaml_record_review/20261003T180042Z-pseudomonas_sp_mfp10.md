# YAML Record Review: Pseudomonas sp. MFP10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_mfp10.yaml`
- Started UTC: 2026-10-03T17:59:37Z
- Finished UTC: 2026-10-03T18:00:42Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303859`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`,
code 11, grounding `EXACT` and mapping status `SEEDED`. Ten lineage
entries, one NCBI NAME attestation, zero strains and one embedded
seed event are present. No synonyms, nomenclature, taxonomy mappings,
equivalence xrefs, strain/genome links, experiments or graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_mfp10.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_mfp10.yaml`:
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
- The configured original taxdump cannot be verified: ignored-inclusive
  `find data -maxdepth 1 -name source_snapshots` confirms its parent
  directory is absent. No source download or refresh was attempted.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308189` supports the exact label,
species rank, parent, code, empty synonym fields and 2026-09-13
snapshot. The full scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30740` agrees. All ten
ancestors match the pinned backbone: root, cellular organisms,
Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria,
Pseudomonadales, Pseudomonadaceae, Pseudomonas and unclassified
Pseudomonas. Preserve the carried lineage and parent's `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303859&retmode=xml)
confirms ID, label, species rank, parent 196821, code 11 and the
complete non-root lineage.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303859)
confirms label, rank and all ten ancestor IDs including root.
Exact grounding and bacterial domain are supported. The isolate-like
label is not a registered deposit, type-strain claim or rank correction.

EFetch additionally lists `Pseudomonas sp. TAS7` as a `misspelling`.
The local native catalog, raw inventory and YAML omit that alternate
name. It must not be promoted to exact equivalence or used to infer
an independent strain identity. The discrepancy is retained below.

## Evidence

The NCBITAXON / NCBITaxon:1303859 / 1 NAME attestation agrees
with the backbone and snapshot. NAME counts source coverage, not
biological strains or genomes. No DOI, PMID, assembly accession or
experimental quotation is asserted by the YAML.

`data/taxa/PATHS.tsv:106294` pins the slug.
`curation/seed_scope.tsv:393136` admits the taxon on 2026-09-13
with the exact one-source reason carried by the embedded event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. YAML line folding does
not change the reason. `SEEDED` remains appropriate; this report
does not grant human-review status.

## Completeness

Complete ignored-inclusive whole-token ID/label/slug/MFP10 searches
covered raw inventories, curation and history, returning only target
backbone and scope rows. Full exact-field scans found no direct
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits membership.
No descendants can contribute BacDive strains, supporting the zero
count within those inventories.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. ID, label, slug and MFP10
returned two objects, both read in full: the target scientific name
and an unrelated NCBI assembly.

`data/catalog/ncbi_genbank-0016.jsonl.gz:8609` identifies Citrobacter
koseri MFP10, taxon/species 545, assembly GCA_017684525.1,
PRJNA514245 / SAMN18416534. MFP10 is its isolate value, not a
Pseudomonas deposit; `infraspecific_name` is unavailable. No assembly
or sample relationship can be transferred from this distinct taxon.

A separate complete TAS7/full-live-name search returned ten GOLD
objects, all read in full, concerning two fungal identities:

- `data/gold/organisms.jsonl.gz:283055`, Go0389711, identifies
  Descomyces sp. TAS7, taxon 2136015, without a culture accession.
  Projects at lines 166745-166747, Gp0251385 through Gp0251387,
  and lines 238450-238452, Gp0345225 through Gp0345227, link to
  that organism and name its expression studies. Their BioProjects
  are PRJNA440032-PRJNA440034 and PRJNA621860-PRJNA621862, with
  individual BioSamples, not Pseudomonas deposit links.
- `data/gold/organisms.jsonl.gz:505311`, Go0680680, identifies
  Eutypa lata TAS7, taxon 97096, without a culture accession.
  Project Gp0782702 at line 581739 links to it and supplies
  PRJNA787025 / SAMN23765751.
- `data/gold/analyses.jsonl.gz:411907`, Ga0622627, names Eutypa
  lata TAS7 and links Gp0782702. Its GenBank field supplies
  JAKUDF00000000 and GCA_022712995.1; its analysis organism GOLD
  ID and IMG taxon ID are empty. The fungal project identity and
  bare reused TAS7 label do not establish a Pseudomonas relationship.

Fungal source hits were excluded by identity; no Eukaryota YAML was
re-reviewed. Supplied accession versions were preserved in this report.
GOLD organism, project and analysis identifiers are not genome IDs.

Complete ignored-inclusive ID/label/slug/MFP10 searches also covered
`data/atb/`, the entire `data/catalog/allthebacteria.tsv.xz`, and
StrainInfo link, assembly, exclusion and compressed related-record
tables, without a match. TAS7/full-name searches covered those
tables plus raw inventories, curation and history, also without a
match. No eligible target deposit/BioSample chain was established.

Empty optional biological fields are justified at the inspected source
boundary, not proof that no cultures or sequences exist elsewhere.
The live alternate-name discrepancy remains a limited completeness
issue. No gene, regulator, pathway, trait or transcriptomic assertion
is present in the YAML; iModulonDB is not applicable. Unrelated GOLD
expression projects do not change that scope. No graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor M1: Live alternative-name coverage differs from the local
  snapshot. EFetch associates `Pseudomonas sp. TAS7` as a misspelling
  with taxon 1303859, while native catalog, inventory and YAML omit
  it. Current identity and label remain sound. The missing original
  pinned archive prevents distinguishing snapshot differences from
  extraction loss. Maintained owners: `conf/ncbi_taxdump.yaml`,
  `src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
  `src/taxonmech/seed.py`.

## Recommended Edits

For M1, inspect this taxon's exact name rows in the hash-verified
original archive named by `conf/ncbi_taxdump.yaml`. If TAS7 is
present, trace its omission through maintained extraction/projection
code and add a regression test with any correction. If absent,
preserve the snapshot and obtain the live name in an authorized
future refresh. The parser already maps misspellings to
`RELATED_SYNONYM`, and the seeder emits inventory related synonyms;
no code defect is established without the original snapshot check.

Do not patch generated YAML, promote a misspelling to exact equivalence,
join Citrobacter or fungal genomes by reused labels, or change the
supported identity, lineage and `SEEDED` status.

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
