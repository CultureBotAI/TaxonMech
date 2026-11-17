# YAML Record Review: Acinetobacter sp. EGY-SCQ2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/acinetobacter_sp_egy_scq2.yaml`
- Started UTC: 2026-10-03T18:14:49Z
- Finished UTC: 2026-10-03T18:16:25Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1303874`.
Rank is `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:196816`,
genetic code 11, grounding `EXACT` and mapping status `SEEDED`.
The record has ten lineage entries, one NCBI NAME attestation, zero
strains and one embedded seed event. No synonyms, nomenclature,
taxonomy mappings, equivalence xrefs, strain/genome links, experimental
assertions or causal graph are present.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/acinetobacter_sp_egy_scq2.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/acinetobacter_sp_egy_scq2.yaml`:
  PASS; one file, zero errors; standard diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduced identity, rank,
  parent, code, empty synonym fields and every lineage object. No
  children occur. Complete exact-field scans found no membership in
  seven other source inventories. PATHS and scope each have one row.
- `just verify-corpus`: Not checked; full-corpus-only, with no invented
  focused substitute. Full QC, global provenance, generated products,
  exports and sequence contents were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308192` supports the exact identity,
rank, parent, code, empty synonyms and 2026-09-13 snapshot. The full
scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30745` agrees. All ten
ancestors match the pinned backbone: root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Moraxellales,
Moraxellaceae, Acinetobacter and unclassified Acinetobacter. Preserve
the carried chain and the parent's `NO_RANK`.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303874&retmode=xml)
confirms ID, scientific name, species rank, parent 196816, code 11
and all non-root lineage entries. It supplies no alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303874)
confirms the label, rank and all ten ancestor identifiers, including
root. Exact grounding and bacterial domain are supported. The
isolate-like label does not authorize a rank change or establish a
registered culture deposit or type strain.

## Evidence

The NCBITAXON / NCBITaxon:1303874 / 1 NAME attestation agrees with
the raw row and pinned snapshot. NAME counts source coverage, not
biological strains or genomes. No DOI, PMID, assembly accession or
experimental quotation is asserted by this YAML.

`data/taxa/PATHS.tsv:106297` pins the slug.
`curation/seed_scope.tsv:393138` admits this species on 2026-09-13
with the exact one-source reason carried by the embedded event.
Timestamp 2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. YAML folding does not
change the reason. `SEEDED` remains appropriate; the report grants
no human-review status.

## Completeness

Complete ignored-inclusive whole-token ID, full-label, slug and
EGY-SCQ2 searches covered raw inventories, curation and history,
returning only the target backbone and scope rows. Complete structured
exact-field scans found no direct BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits membership. With no descendants in
the inspected backbone, none can contribute additional BacDive strains.
The zero strain count is supported within these inventories.

Complete ignored-inclusive compressed JSONL searches covered
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/` and `data/straininfo/`. The same target identifiers
returned only its scientific-name object, read in full. No eligible
culture-deposit or explicit strain-genome chain was established.

Additional complete ignored-inclusive searches covered `data/atb/`,
the entire `data/catalog/allthebacteria.tsv.xz`, and StrainInfo TSV
and compressed TSV link, assembly, exclusion and related-record
tables, without a match. These bounded negative checks justify empty
optional fields; they do not prove that cultures or sequences do not
exist elsewhere.

No gene, regulator, pathway, trait or transcriptomic assertion is
present; iModulonDB is not applicable. No causal graph is required.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None. Retain the supported identity, source lineage, zero strain count
and `SEEDED` status. Do not invent a deposit identifier from EGY-SCQ2
or infer a genome association from taxonomy alone. Any future source
addition belongs in the maintained source pipeline and inventories,
followed by authorized seeding, not a hand edit of the generated YAML.

## Follow-up Checks

No corrective check is required by this review. After an authorized
source refresh, compare this taxon's exact rows and any explicit deposit
and genome chains, then run both focused validators. Corpus-wide
reproducibility claims additionally require `just verify-corpus` and
full QC; neither was run here.

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
