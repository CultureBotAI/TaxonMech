# YAML Record Review: Streptomyces sp. SPF3

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_spf3.yaml`
- Started UTC: 2026-10-03T16:49:56Z
- Finished UTC: 2026-10-03T16:50:54Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303830`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2593676`, genetic code 11, grounding `EXACT`, status
`SEEDED`. Ten lineage entries, one NCBI NAME attestation, zero strains
and one embedded seed event are present. No synonyms, nomenclature,
taxonomy mappings, equivalence xrefs, strain/genome links, experimental
claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_spf3.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptomyces_sp_spf3.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured backbone comparison reproduces identity, rank,
  parent, genetic code and all ten lineage objects. No target children
  occur. Full exact-field scans find no target membership in the seven
  other source inventories. PATHS and scope each contain one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence content were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308163` matches the exact SPF3 label,
species rank, unclassified-Streptomyces parent, code and empty synonym
fields. The full native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30714` agrees. Every root-first
lineage entry matches the pinned NCBI backbone.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303830&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 2593676,
code 11 and the complete non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303830)
confirms rank and all ten ancestor IDs including root. Kitasatosporales
and Streptomycetaceae are supported source placements. Exact grounding
to this NCBI entity is supported.

Keep NCBI's species rank and the direct unclassified parent's `NO_RANK`.
SPF3 is not a collection accession or evidence for a named species,
validly published binomial, type strain or functional property. It must
not be conflated with the distinct Aeromonas SPF3-1-srbf designation.

## Evidence

The NCBITAXON / NCBITaxon:1303830 / 1 NAME attestation matches the
backbone row and the 2026-09-13 taxonomy snapshot. NAME counts source
coverage, not biological strains or genomes. No DOI, PMID, assembly
identifier or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106268` pins the slug.
`curation/seed_scope.tsv:393110` admits the target on 2026-09-13 with
the exact one-source reason reproduced in the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` is preserved;
this report does not grant human-reviewed status.

## Completeness

Complete ignored-inclusive, case-insensitive whole-token searches by
ID, label, slug and SPF3 covered `data/raw/`, `curation/`, `history/`
and all compressed native JSONL catalogs under `data/catalog/`,
`data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/` and
`data/straininfo/`. Only the target scientific-name object was native
target evidence. Full exact-field BacDive, LPSN, GTDB, GOLD, MediaDive,
Madin and BactoTraits membership scans found no target row. With no
descendants, zero strains is supported at the complete BacDive boundary.

The token search also matched the beginning of the hyphenated name
Aeromonas sp. SPF3-1-srbf. Its raw row at
`data/raw/ncbitaxon_taxa.tsv:75447`, scope row at
`curation/seed_scope.tsv:191555` and complete native name object at
`data/catalog/ncbi_names-0002.jsonl.gz:10366` identify taxon 362296,
parent 257493, not this Streptomyces taxon. Those full rows/objects were
read and excluded; a token boundary does not establish biological identity.

Additional complete ignored-inclusive, case-insensitive whole-token
searches covered `data/atb/`, the full
`data/catalog/allthebacteria.tsv.xz` and StrainInfo link, assembly,
exclusion and compressed related-record tables. No target ID, label,
slug or SPF3 token matched. The raw-directory search included all
assembly/genome/related inventories. No eligible culture-deposit or
BioSample source chain was established.

These bounded searches support empty optional nomenclature, mappings
and genome links; they do not assert that isolates or sequences are
absent elsewhere. No gene, regulator, pathway, trait or transcriptomics
dataset is asserted; iModulonDB is not applicable. No causal graph is
required for this identity-only record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Keep the supported backbone and `SEEDED` status.
Future enrichment belongs in maintained source inputs or
`src/taxonmech/extract.py`, with changed seeding behavior in
`src/taxonmech/seed.py` and regression tests. Do not patch generated
YAML or join a partial strain designation across different taxa.

## Follow-up Checks

No finding-specific check remains. New evidence requires exact
taxon/deposit verification, authorized dry-run/canary steps and both
focused validators after regeneration. Any corpus change also requires
`just verify-corpus` and full QC, neither claimed by this focused pass.

## Additional Notes

Absence checks included ignored files via full structured reads,
`find`, and `rg --no-ignore --hidden -z -i -w` token searches. Public
read-only NCBI API requests used network escalation after established
sandbox DNS failures. The only manual write is this report; strict
validation wrote its standard diagnostic. No record, source, prior
report, history or status was edited. No generator, refresh, paid
research, GitHub action or cross-repository write occurred. Eukaryota
was not re-reviewed.
