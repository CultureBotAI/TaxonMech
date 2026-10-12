# YAML Record Review: Bacillus sp. CV-B.sp3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_cv_b_sp3.yaml`
- Started UTC: 2026-10-03T19:17:53Z
- Finished UTC: 2026-10-03T19:18:49Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303902`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:185979`,
code 11, grounding `EXACT` and mapping status `SEEDED`. Ten lineage
entries, one NCBI NAME attestation, zero strains and one embedded seed
event are present. No synonyms, nomenclature, taxonomy mappings, xrefs,
strain/genome links, experiments or graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bacillus_sp_cv_b_sp3.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/bacillus_sp_cv_b_sp3.yaml`:
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

`data/raw/ncbitaxon_taxa.tsv:308219` supports label, species rank,
parent, code, empty synonyms and the 2026-09-13 snapshot. The complete
scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30772` agrees. Every ancestor
matches the pinned backbone: root, cellular organisms, Bacteria,
Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae, Bacillus
and unclassified Bacillus (in: firmicutes). Preserve that qualified
parent label and its `NO_RANK`, without replacing source wording.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303902&retmode=xml)
confirms ID, label, species rank, parent 185979, code 11 and every
non-root ancestor. It supplies no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303902)
confirms label, rank and all ten ancestor identifiers, including root.
Exact grounding and bacterial domain are supported. Preserve CV-B.sp3's
case and punctuation. Its isolate-like wording does not prove a
registered culture deposit, type strain or different taxonomic rank.

## Evidence

The NCBITAXON / NCBITaxon:1303902 / 1 NAME attestation matches
the backbone and snapshot. NAME counts source coverage, not biological
strains, phenotypes or genomes. No DOI, PMID, assembly accession or
experimental quotation is asserted by this YAML.

`data/taxa/PATHS.tsv:106324` pins the slug.
`curation/seed_scope.tsv:393165` admits this species on 2026-09-13
with the exact one-source reason carried by the embedded seed event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources,
SEEDED_FROM_SOURCES action and NCBITAXON source list are consistent.
This report does not confer human-review status; retain `SEEDED`.

The full object at
`data/catalog/gtdb_genomes-0005.jsonl.gz:36865` is an unrelated
numeric collision: `GB_GCA_963786185.1`, NCBI uncultured Thermoleophilia
bacterium 1497501, GTDB PALSA-600 sp963786185, isolate MFD06085.bin.2.143,
project PRJEB58634 and BioSample SAMEA114825823. Its `ncbi_contig_n50`
is 1303902; its explicit taxon fields are not this Bacillus record.
No target association or assembly equivalence was inferred.

## Completeness

Complete ignored-inclusive whole-token ID, full-label, slug and CV-B.sp3
searches covered raw inventories, curation and history, returning only
the target backbone and scope rows. Complete structured exact-field
scans found no direct BacDive, LPSN, GTDB, GOLD, MediaDive, Madin
or BactoTraits membership. No backbone descendants can contribute
BacDive strains, supporting zero strains within these inventories.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. The two matching objects
were read in full: the target scientific name and the unrelated N50
collision above. No eligible culture-deposit or explicit strain-genome
chain was established.

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
and `SEEDED` status. Do not infer a registered deposit from CV-B.sp3,
normalize its punctuation or join evidence through shared taxonomy or
an N50 collision. Future evidence belongs in maintained source pipelines
and inventories, followed by authorized seeding, not manual YAML edits.

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
