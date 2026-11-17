# YAML Record Review: Streptomyces sp. SPF4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_spf4.yaml`
- Started UTC: 2026-10-03T16:51:34Z
- Finished UTC: 2026-10-03T16:52:39Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303831`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2593676`, genetic code 11, grounding `EXACT`, status
`SEEDED`. It carries ten lineage entries, one NCBI NAME attestation,
zero strains and one embedded seed event. No synonyms, nomenclature,
taxonomy mappings, xrefs, strain/genome links, experimental claims or
causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_spf4.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptomyces_sp_spf4.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, parent,
  code and all ten lineage entries. No target children occur. Complete
  exact-field scans find no membership in the seven other source
  inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence content were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308164` agrees on the exact SPF4 label,
species rank, unclassified-Streptomyces parent, code and empty synonym
fields. The complete native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30715` agrees. Every root-first
ancestor matches its pinned NCBI backbone row.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303831&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 2593676,
code 11 and the complete non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303831)
confirms rank and all ten ancestor IDs including root. Kitasatosporales
and Streptomycetaceae agree in pinned and live sources. Exact NCBI
grounding is supported.

Keep the source species rank and direct unclassified parent's `NO_RANK`.
SPF4 is not a culture accession or evidence for a named species,
validly published binomial, type strain or functional property. Nearby
SPF designations do not establish equivalent taxon or strain identities.

## Evidence

The NCBITAXON / NCBITaxon:1303831 / 1 NAME attestation matches the
backbone row and its 2026-09-13 taxonomy snapshot. NAME is a source
count, not a biological strain or genome count. No DOI, PMID, assembly
identifier or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106269` pins the slug.
`curation/seed_scope.tsv:393111` admits this target on 2026-09-13 with
the exact one-source reason in the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` remains appropriate;
no human-review status is claimed or granted.

## Completeness

Complete ignored-inclusive, case-insensitive whole-token searches by
ID, label, slug and SPF4 covered raw inventories, curation, history and
all compressed native JSONL catalogs under `data/catalog/`,
`data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/` and
`data/straininfo/`. The native search found only the scientific-name
object. Full exact-field BacDive, LPSN, GTDB, GOLD, MediaDive, Madin
and BactoTraits membership scans found no target row. No descendants
exist to contribute strains, supporting the uncapped zero strain count.

Additional complete ignored-inclusive, case-insensitive whole-token
searches covered `data/atb/`, the full
`data/catalog/allthebacteria.tsv.xz` and StrainInfo link, assembly,
exclusion and compressed related-record tables. No target ID, label,
slug or SPF4 token matched. The raw-directory search included all
assembly/genome/related inventories. No eligible culture-deposit or
BioSample source chain was established.

These bounded results justify empty optional nomenclature, mappings
and genome links, not a claim that no isolates or sequences exist
elsewhere. No gene, regulator, pathway, trait or transcriptomics dataset
is asserted; iModulonDB is not applicable. No causal graph is required
for this identity-only record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Preserve the supported backbone and `SEEDED` status.
Future source-backed enrichment belongs in maintained extraction inputs
or `src/taxonmech/extract.py`, with changed seeding behavior in
`src/taxonmech/seed.py` and regression tests. Do not patch generated
YAML or transfer evidence from a similar designation.

## Follow-up Checks

No finding-specific check remains. New evidence requires exact
taxon/deposit verification, authorized dry-run/canary steps and both
focused validators after regeneration. Corpus changes additionally
require `just verify-corpus` and full QC, neither claimed by this pass.

## Additional Notes

Absence checks included ignored files via full structured reads,
`find`, and `rg --no-ignore --hidden -z -i -w` token searches. Public
read-only NCBI requests used network escalation after established
sandbox DNS failures. The only manual write is this report; strict
validation wrote its standard diagnostic. No record, source, earlier
report, history or status was edited. No generator, refresh, paid
research, GitHub action or cross-repository write occurred. Eukaryota
was not re-reviewed.
