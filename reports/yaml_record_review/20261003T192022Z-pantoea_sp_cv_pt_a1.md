# YAML Record Review: Pantoea sp. CV-Pt.a1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pantoea_sp_cv_pt_a1.yaml`
- Started UTC: 2026-10-03T19:19:26Z
- Finished UTC: 2026-10-03T19:20:22Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303903`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2630326`,
code 11, grounding `EXACT` and mapping status `SEEDED`. Ten lineage
entries, one NCBI NAME attestation, zero strains and one embedded seed
event are present. No synonyms, nomenclature, taxonomy mappings, xrefs,
strain/genome links, experiments or graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pantoea_sp_cv_pt_a1.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pantoea_sp_cv_pt_a1.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured comparison reproduced identity, rank, parent, code,
  empty synonyms and all ten lineage objects. No children occur.
  Complete exact-field scans found no membership in seven other source
  inventories. PATHS and scope each contain one row; the attestation
  and embedded reason match their source inputs.
- `just verify-corpus`: Not checked; full-corpus-only, with no invented
  focused substitute. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive searches found no standalone target history event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308220` supports label, species rank,
parent, code, empty synonyms and the 2026-09-13 snapshot. The complete
scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30773` agrees. Every ancestor
matches the pinned backbone: root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales,
Erwiniaceae, Pantoea and unclassified Pantoea. Preserve the source
chain, including family Erwiniaceae 1903409 and the parent's `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303903&retmode=xml)
confirms ID, label, species rank, parent 2630326, code 11 and every
non-root ancestor. It supplies no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303903)
confirms label, rank and all ten ancestor identifiers, including root.
Exact grounding and bacterial domain are supported. Preserve CV-Pt.a1's
case and punctuation. Its isolate-like wording does not prove a
registered culture deposit, type strain or different taxonomic rank.

## Evidence

The NCBITAXON / NCBITaxon:1303903 / 1 NAME attestation matches
the backbone and snapshot. NAME counts source coverage, not biological
strains, phenotypes or genomes. No DOI, PMID, assembly accession or
experimental quotation is asserted by this YAML.

`data/taxa/PATHS.tsv:106325` pins the slug.
`curation/seed_scope.tsv:393166` admits this species on 2026-09-13
with the exact one-source reason carried by the embedded seed event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources,
SEEDED_FROM_SOURCES action and NCBITAXON source list are consistent.
This report does not confer human-review status; retain `SEEDED`.

Two unrelated numeric matches were read in full:

- `data/catalog/gtdb_genomes-0004.jsonl.gz:11475` is
  `GB_GCA_903896035.1`, GTDB Methylotenera sp903882525, with NCBI
  uncultured Pseudomonadota bacterium 153809, isolate MJ111018B_bin-1117,
  project PRJEB38681 and BioSample SAMEA6945261.
- `data/catalog/ncbi_genbank-0058.jsonl.gz:14033` is
  `GCA_903896035.1`, with those same explicit NCBI taxon, isolate,
  project and sample identifiers.

The value 1303903 occurs in total/ungapped genome-length fields, not
their taxon fields. Neither object supplies evidence for this Pantoea
record. No target association or assembly equivalence was inferred.

## Completeness

Complete ignored-inclusive whole-token ID, full-label, slug and CV-Pt.a1
searches covered raw inventories, curation and history, returning only
the target backbone and scope rows. Complete structured exact-field
scans found no direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin
or BactoTraits membership. No backbone descendants can contribute
BacDive strains, supporting zero strains within these inventories.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. The three matching objects
were read in full: the target scientific name and the two unrelated
genome-length matches above. No eligible culture-deposit or explicit
strain-genome chain was established.

Additional complete ignored-inclusive searches covered `data/atb/`,
the entire `data/catalog/allthebacteria.tsv.xz`, and StrainInfo TSV
and compressed TSV link, assembly, exclusion and related-record tables,
without a match. Empty optional fields are justified at this source
boundary, not proof that cultures or sequences cannot exist elsewhere.
Original primary archives were not independently reproduced.

No gene, regulator, pathway, trait or transcriptomic assertion is
present; iModulonDB is not applicable. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None. Retain the supported identity, source lineage, zero strain count
and `SEEDED` status. Do not infer a registered deposit from CV-Pt.a1,
normalize its punctuation or join evidence through shared taxonomy or
genome-length collisions. Future evidence belongs in maintained source
pipelines and inventories, followed by authorized seeding, not manual
edits to generated YAML.

## Follow-up Checks

No corrective check is required. After an authorized source refresh,
compare exact source rows and any explicit deposit/genome chain, then
rerun both focused validators. Corpus-wide claims additionally require
`just verify-corpus` and full QC; neither was run here.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All searches and
validators completed. Public NCBI metadata reads used network escalation
after established sandbox DNS failures.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
