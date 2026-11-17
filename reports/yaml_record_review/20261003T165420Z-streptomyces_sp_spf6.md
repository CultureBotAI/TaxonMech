# YAML Record Review: Streptomyces sp. SPF6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_spf6.yaml`
- Started UTC: 2026-10-03T16:53:19Z
- Finished UTC: 2026-10-03T16:54:20Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303832`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2593676`, genetic code 11, grounding `EXACT`, status
`SEEDED`. It carries ten lineage entries, one NCBI NAME attestation,
zero strains and one embedded seed event. No synonyms, nomenclature,
taxonomy mappings, equivalence xrefs, strain/genome links, experimental
claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_spf6.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptomyces_sp_spf6.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, parent,
  genetic code and all ten lineage objects. No target children occur.
  Complete exact-field scans find no membership in the seven other source
  inventories. PATHS and scope each contain exactly one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence content were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308165` matches the exact SPF6 label,
species rank, unclassified-Streptomyces parent, code and empty synonym
fields. The complete scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30716` agrees. Every root-first
ancestor matches its pinned NCBI backbone row.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303832&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 2593676,
code 11 and the full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303832)
confirms rank and all ten ancestor IDs including root. Kitasatosporales
and Streptomycetaceae agree in pinned and live sources. Exact NCBI
grounding is supported.

Preserve the source species rank and direct unclassified parent's
`NO_RANK`. SPF6 is not a culture accession or evidence for a named
species, validly published binomial, type strain or functional property.
Similar SPF designations do not establish strain or taxon equivalence.

## Evidence

The NCBITAXON / NCBITaxon:1303832 / 1 NAME attestation matches the
backbone row and its 2026-09-13 snapshot. NAME describes source
coverage, not biological strains or genomes. No DOI, PMID, assembly
identifier or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106270` pins the slug.
`curation/seed_scope.tsv:393112` admits the taxon on 2026-09-13 with
the exact one-source reason in the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` is retained;
no human-review status is claimed or granted.

## Completeness

Complete ignored-inclusive, case-insensitive whole-token searches by
ID, label, slug and SPF6 covered raw inventories, curation, history and
all compressed native JSONL catalogs under `data/catalog/`,
`data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/` and
`data/straininfo/`. Only the scientific-name object matched the native
search. Full exact-field BacDive, LPSN, GTDB, GOLD, MediaDive, Madin
and BactoTraits membership scans found no target row. No descendants
exist to contribute strains, supporting the uncapped zero strain count.

Additional complete ignored-inclusive, case-insensitive whole-token
searches covered `data/atb/`, the full
`data/catalog/allthebacteria.tsv.xz` and StrainInfo link, assembly,
exclusion and compressed related-record tables. No target ID, label,
slug or SPF6 token matched. The raw-directory search included all
assembly/genome/related inventories. No eligible culture-deposit or
BioSample source chain was established.

These bounded checks justify empty optional nomenclature, mappings and
genome links; they do not assert that no isolates or sequences exist
elsewhere. No gene, regulator, pathway, trait or transcriptomics dataset
is asserted; iModulonDB is not applicable. No causal graph is required
for this identity-only record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Keep the supported NCBI backbone and `SEEDED` status.
Future source-backed enrichment belongs in maintained extraction inputs
or `src/taxonmech/extract.py`, with changed seeding behavior in
`src/taxonmech/seed.py` and regression tests. Do not patch generated
YAML or transfer evidence from a similarly named record.

## Follow-up Checks

No finding-specific check remains. New evidence requires exact
taxon/deposit verification, authorized dry-run/canary steps and both
focused validators after regeneration. Any corpus change additionally
requires `just verify-corpus` and full QC, neither claimed by this pass.

## Additional Notes

Absence checks included ignored files via full structured reads,
`find`, and `rg --no-ignore --hidden -z -i -w` token searches. Public
read-only NCBI API requests used network escalation after established
sandbox DNS failures. The only manual write is this report; strict
validation wrote its standard diagnostic. No record, source, earlier
report, history or status was edited. No generator, refresh, paid
research, GitHub action or cross-repository write occurred. Eukaryota
was not re-reviewed.
