# YAML Record Review: Bacillus sp. EGY-SCQ4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bacillus_sp_egy_scq4.yaml`
- Started UTC: 2026-10-03T18:22:53Z
- Finished UTC: 2026-10-03T18:23:58Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303878`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:185979`,
code 11, grounding `EXACT` and mapping status `SEEDED`. Ten lineage
entries, one NCBI NAME attestation, zero strains and one embedded
seed event are present. No synonyms, nomenclature, taxonomy mappings,
equivalence xrefs, strain/genome links, experiments or graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/bacillus_sp_egy_scq4.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/bacillus_sp_egy_scq4.yaml`:
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

`data/raw/ncbitaxon_taxa.tsv:308196` supports the label, species
rank, parent, code, empty synonyms and 2026-09-13 snapshot. The full
scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30749` agrees. All ancestors
match the pinned backbone: root, cellular organisms, Bacteria,
Bacillati, Bacillota, Bacilli, Caryophanales, Bacillaceae, Bacillus
and unclassified Bacillus (in: firmicutes). Preserve the carried
chain, including the parent's qualified source label and `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303878&retmode=xml)
confirms ID, name, species rank, parent 185979, code 11 and the
complete non-root lineage. It supplies no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303878)
confirms label, rank and all ten ancestor identifiers, including root.
Exact grounding and bacterial domain are supported. The isolate-like
species label is not evidence for a registered deposit, a type strain
or a rank change.

## Evidence

The NCBITAXON / NCBITaxon:1303878 / 1 NAME attestation agrees
with the backbone and snapshot. NAME counts source coverage, not
biological strains, phenotypes or genomes. No DOI, PMID, assembly
accession or experimental quotation is asserted by the YAML.

`data/taxa/PATHS.tsv:106301` pins the slug.
`curation/seed_scope.tsv:393142` admits this species on 2026-09-13
with the exact one-source reason carried by the embedded seed event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. YAML line folding does
not change the reason. `SEEDED` remains appropriate; this review
does not confer human-review status.

## Completeness

Complete ignored-inclusive whole-token ID, full-label, slug and
EGY-SCQ4 searches covered raw inventories, curation and history,
returning only the target backbone and scope rows. Complete structured
exact-field scans found no direct BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits membership. No descendants in the
inspected backbone can contribute BacDive strains, supporting the
zero count within these inventories.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. Three objects matched and
were read in full: the target scientific-name object and two unrelated
assembly metadata objects. No eligible deposit or strain-genome chain
was established for EGY-SCQ4.

The unrelated objects are
`data/catalog/gtdb_genomes-0014.jsonl.gz:24677` and
`data/catalog/ncbi_genbank-0042.jsonl.gz:34473`. Both identify
GCA_046294875.1, isolate 21H_022.bin.22, Aquificaceae bacterium
taxon 2053503, BioProject PRJNA1185458 and BioSample SAMN45832984.
The GTDB object places it in Pampinifervens sp046294875. The number
1303878 is the ungapped genome length, not a taxonomy reference.
These objects provide no Bacillus link; preserve their source identity
and do not join on an untyped numeric match.

Additional complete ignored-inclusive searches covered `data/atb/`,
the entire `data/catalog/allthebacteria.tsv.xz`, and StrainInfo TSV
and compressed TSV link, assembly, exclusion and related-record tables,
without a match. Empty optional fields are supported within these
boundaries, not proof that cultures or sequences cannot exist elsewhere.
No original primary archive was independently reproduced.

No gene, regulator, pathway, trait or transcriptomic assertion is
present; iModulonDB is not applicable. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None. Retain the supported identity, source lineage, zero strain count
and `SEEDED` status. Do not infer a deposit from EGY-SCQ4 or join
the unrelated Aquificaceae assembly through its numerical genome length.
Future evidence additions belong in the maintained source pipeline and
inventories, followed by authorized seeding, not manual YAML edits.

## Follow-up Checks

No corrective check is required. After an authorized refresh, compare
this taxon's exact source rows and explicit deposit/genome evidence,
then rerun both focused validators. Corpus-wide claims additionally
require `just verify-corpus` and full QC; neither was run here.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find` and `rg --no-ignore --hidden -z -i -w`. All searches and
validators completed. Public NCBI metadata reads used network escalation
after established sandbox DNS failures.

The only manual write is this report; strict validation wrote its
standard diagnostic. No record, source, prior report, history or status
was changed. No generator, refresh, paid research, GitHub action or
cross-repository write occurred. Eukaryota was not re-reviewed.
