# YAML Record Review: Pseudomonas sp. CHFP23

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_chfp23.yaml`
- Started UTC: 2026-10-03T18:02:42Z
- Finished UTC: 2026-10-03T18:03:55Z
- Verdict: pass with minor issues

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303860`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196821`,
code 11, grounding `EXACT` and mapping status `SEEDED`. Ten lineage
entries, one NCBI NAME attestation, zero strains and one embedded
seed event are present. No synonyms, nomenclature, taxonomy mappings,
equivalence xrefs, strain/genome links, experiments or graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_chfp23.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_chfp23.yaml`:
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

`data/raw/ncbitaxon_taxa.tsv:308190` supports the exact label,
species rank, parent, code, empty synonym fields and 2026-09-13
snapshot. The full scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30741` agrees. Every ancestor
matches the pinned backbone: root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pseudomonadales,
Pseudomonadaceae, Pseudomonas and unclassified Pseudomonas.
Preserve the carried chain and parent's `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303860&retmode=xml)
confirms ID, label, species rank, parent 196821, code 11 and the
complete non-root lineage.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303860)
confirms label, rank and all ten ancestor IDs including root.
Exact grounding and bacterial domain are supported. The isolate-like
label is not a registered deposit, type-strain claim or rank correction.

EFetch additionally lists `Pseudomonas sp. TAS8` as a `misspelling`.
The local native catalog, raw inventory and YAML omit that alternate
name. It must not be promoted to exact equivalence or used to infer
an independent strain identity. The discrepancy is retained below.

## Evidence

The NCBITAXON / NCBITaxon:1303860 / 1 NAME attestation agrees
with the backbone and snapshot. NAME counts source coverage, not
biological strains or genomes. No DOI, PMID, assembly accession or
experimental quotation is asserted by the YAML.

`data/taxa/PATHS.tsv:106295` pins the slug.
`curation/seed_scope.tsv:393137` admits the taxon on 2026-09-13
with the exact one-source reason carried by the embedded event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. YAML line folding does
not change the reason. `SEEDED` remains appropriate; this report
does not grant human-review status.

## Completeness

Complete ignored-inclusive whole-token ID/label/slug/CHFP23 searches
covered raw inventories, curation and history, returning only target
backbone and scope rows. Full exact-field scans found no direct
BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits membership.
No descendants can contribute BacDive strains, supporting the zero
count within those inventories.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. ID, full label, slug and
CHFP23 returned only the target scientific-name object, read in full.
A separate complete TAS8/full-live-name search returned eight GOLD
objects, all read in full; none identifies this Pseudomonas taxon.

`data/gold/organisms.jsonl.gz:414665`, Go0580402, identifies
Russula sp. TAS8 PSC4658, taxon 3127164, without a culture accession.
Project Gp0568791 at line 419346 links to this organism and names
its fungal draft, PRJNA1080841 / SAMN40217760. Six projects at
lines 457399-457404, Gp0614049 through Gp0614054, name that
organism's expression studies and preserve their individual BioProject
and BioSample accessions. These fungal projects supply no Pseudomonas
deposit or genome relationship.

The alternate-name search also found Russula's distinct backbone row
at `data/raw/ncbitaxon_taxa.tsv:604548` and scope row at
`curation/seed_scope.tsv:63575`. These are taxon 3127164, not
1303860. Source hits were excluded by identity; no Eukaryota YAML
was re-reviewed.

Complete ignored-inclusive ID/label/slug/CHFP23 searches additionally
covered `data/atb/`, the entire `data/catalog/allthebacteria.tsv.xz`,
and StrainInfo link, assembly, exclusion and compressed related-record
tables, without a match. TAS8/full-name searches covered those
tables plus raw inventories, curation and history; only the two
unrelated Russula rows described above matched. No eligible target
deposit/BioSample chain was established within these boundaries.

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
  snapshot. EFetch associates `Pseudomonas sp. TAS8` as a misspelling
  with taxon 1303860, while native catalog, inventory and YAML omit
  it. Current identity and label remain sound. The missing original
  pinned archive prevents distinguishing snapshot differences from
  extraction loss. Maintained owners: `conf/ncbi_taxdump.yaml`,
  `src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and
  `src/taxonmech/seed.py`.

## Recommended Edits

For M1, inspect this taxon's exact name rows in the hash-verified
original archive named by `conf/ncbi_taxdump.yaml`. If TAS8 is
present, trace its omission through maintained extraction/projection
code and add a regression test with any correction. If absent,
preserve the snapshot and obtain the live name in an authorized
future refresh. The parser already maps misspellings to
`RELATED_SYNONYM`, and the seeder emits inventory related synonyms;
no code defect is established without the original snapshot check.

Do not patch generated YAML, promote a misspelling to exact
equivalence, join fungal projects by TAS8, or change the supported
identity, lineage and `SEEDED` status.

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
