# YAML Record Review: Streptomyces sp. SPF1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_spf1.yaml`
- Started UTC: 2026-10-03T16:45:37Z
- Finished UTC: 2026-10-03T16:46:42Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303828`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2593676`, genetic code 11, grounding `EXACT`, status
`SEEDED`. It contains ten lineage entries, one NCBI NAME attestation,
zero strains and one embedded seed event. No synonyms, nomenclature,
taxonomy mappings, equivalence xrefs, strain/genome links, experimental
claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_spf1.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptomyces_sp_spf1.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, parent,
  code and all ten lineage objects. No target children occur. Complete
  exact-field scans find no target membership in the seven other source
  inventories. PATHS and scope each contain exactly one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence content were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308161` supplies the exact uppercase
SPF1 label, species rank, unclassified-Streptomyces parent, code and
empty synonym fields. The complete native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30712` agrees. Every root-first
ancestor matches its pinned NCBI backbone row.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303828&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 2593676,
code 11 and the complete non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303828)
confirms rank and all ten ancestor IDs including root. Kitasatosporales
and Streptomycetaceae are supported source placements, not inferred
reconciliation. Exact grounding to this NCBI entity is supported.

Preserve NCBI's species rank and the direct unclassified parent's
`NO_RANK`. SPF1 is not a collection accession or evidence for a named
species, validly published binomial, type strain or functional property.
Its spelling alone does not connect it to other strains called spf1.

## Evidence

The NCBITAXON / NCBITaxon:1303828 / 1 NAME attestation matches the
backbone row and its 2026-09-13 snapshot. NAME describes source
coverage, not a strain or genome count. No DOI, PMID, assembly
accession or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106266` pins the slug.
`curation/seed_scope.tsv:393108` admits the taxon on 2026-09-13 with
the exact one-source reason in the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and source list agree. `SEEDED` is preserved;
this review does not grant human-reviewed status.

## Completeness

Complete ignored-inclusive, case-insensitive whole-token searches by
ID, label, slug and SPF1 covered `data/raw/`, `curation/`, `history/`
and all compressed native JSONL files under `data/catalog/`,
`data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/` and
`data/straininfo/`. The target's only native evidence was its NCBI name
object. Exact-field membership scans of the complete BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no target
row. There are no descendants to contribute strains.

A genuine bare-designation collision was inspected and excluded:

- `data/raw/bacdive_strains.tsv:82791` is BacDive 160554, designation
  `spf1, PROD`, classified under NCBITaxon:2736289, with LPSN 36255
  and deposit DSM-103721. It is not filed under the target or its subtree.
- The full object at `data/bacdive/records.jsonl.gz:82790` identifies
  Xylanibacter rodentium, with that same taxon and deposit. Its type
  status and genome references belong to Xylanibacter, not Streptomyces.
- The full object at `data/straininfo/records.jsonl.gz:296510` is
  SI-ID 398621, own deposit SI-DP 905347 / DSM 103721, taxon 2736289,
  Xylanibacter rodentium. Its relation lists PROD and spf1. That
  source-specific identity is distinct from Streptomyces SPF1.

Do not import DSM 103721, its type flag, BacDive genome references or
the StrainInfo record merely because the bare alias matches. The correct
target strain count remains zero at the inspected inventory boundary.

Additional complete, ignored-inclusive, case-insensitive whole-token
searches covered `data/atb/`, the full
`data/catalog/allthebacteria.tsv.xz` and StrainInfo link, assembly,
exclusion and compressed related-record tables. They found no target
ID, label, slug or SPF1 token. Raw assembly/genome/related inventories
were included in the raw-directory search. No eligible target
culture-deposit or BioSample source chain was established.

Optional nomenclature, mappings and genome links are appropriately empty
at this checked boundary, not evidence that no isolates or sequences
exist elsewhere. No gene, regulator, pathway, trait or transcriptomics
dataset is asserted; iModulonDB is not applicable. No causal graph is
required for an identity-only record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Keep the supported backbone and `SEEDED` status.
Future enrichment belongs in maintained source inputs or
`src/taxonmech/extract.py`, with changed seeding behavior in
`src/taxonmech/seed.py` and regression tests. Do not patch generated
YAML or join a bare strain alias across conflicting taxa.

## Follow-up Checks

No finding-specific check remains. Any proposed SPF1 enrichment must
first disambiguate the Streptomyces target from Xylanibacter's alias
using primary taxon/deposit evidence. Then use authorized dry-run/canary
steps and both focused validators after regeneration. Corpus changes
also require `just verify-corpus` and full QC, neither claimed here.

## Additional Notes

Absence checks included ignored files via full structured reads,
`find`, and `rg --no-ignore --hidden -z -i -w` token searches. Public
read-only NCBI API requests used network escalation after established
sandbox DNS failures. The only manual write is this report; strict
validation wrote its standard diagnostic. No record, source, prior
report, history or status was edited. No generator, refresh, paid
research, GitHub action or cross-repository write occurred. No Eukaryota
record was re-reviewed.
