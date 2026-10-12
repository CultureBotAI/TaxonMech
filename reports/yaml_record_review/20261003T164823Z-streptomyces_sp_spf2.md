# YAML Record Review: Streptomyces sp. SPF2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_spf2.yaml`
- Started UTC: 2026-10-03T16:47:26Z
- Finished UTC: 2026-10-03T16:48:23Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303829`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2593676`, genetic code 11, grounding `EXACT`, status
`SEEDED`. Ten lineage entries, one NCBI NAME attestation, zero strains
and one embedded seed event are present. No synonyms, nomenclature,
taxonomy mappings, equivalence xrefs, strain/genome links, experimental
claims or causal graph are asserted.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_spf2.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptomyces_sp_spf2.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Full structured backbone comparison reproduces identity, rank, parent,
  genetic code and all ten lineage objects. No target children occur.
  Complete exact-field scans find no target membership in the seven other
  source inventories. PATHS and scope each contain exactly one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence content were not audited.
- Ignored-inclusive history searches found no standalone target event;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308162` agrees with the exact uppercase
SPF2 label, species rank, unclassified-Streptomyces parent, code and
empty synonym fields. The complete native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30713` agrees. Every root-first
lineage entry matches its pinned NCBI backbone row.

The browser page was inaccessible through the web tool. Inspected
[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303829&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 2593676,
code 11 and all non-root lineage labels/ranks, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303829)
confirms rank and all ten ancestor IDs including root. Kitasatosporales
and Streptomycetaceae agree in the pinned and live sources. Exact NCBI
grounding is supported.

Keep NCBI's species rank and the direct unclassified parent's `NO_RANK`.
The SPF2 designation is not a culture accession or evidence for a named
species, validly published binomial, type strain or functional property.
It does not establish identity with a strain alias used by another taxon.

## Evidence

The NCBITAXON / NCBITaxon:1303829 / 1 NAME attestation matches the
backbone row and its 2026-09-13 snapshot. NAME is a source count,
not a biological strain or genome count. No DOI, PMID, assembly
identifier or experimental quotation is asserted.

`data/taxa/PATHS.tsv:106267` pins the slug.
`curation/seed_scope.tsv:393109` admits the taxon on 2026-09-13 with
the exact one-source reason carried by the embedded event. Timestamp
2026-09-13T17:54:04Z, curator seed_from_sources, action
SEEDED_FROM_SOURCES and the source list agree. `SEEDED` remains
appropriate; no human review is claimed or granted.

## Completeness

Complete ignored-inclusive, case-insensitive whole-token searches by
ID, label, slug and SPF2 covered raw inventories, curation, history and
all compressed native JSONL files under `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/`, `data/seqcode/` and `data/straininfo/`.
Only the scientific-name object was native target evidence. Exact-field
membership scans of the complete BacDive, LPSN, GTDB, GOLD, MediaDive,
Madin and BactoTraits inventories found no target row. No descendants
exist to contribute strains.

A separate taxon's use of the bare alias spf2 was inspected and excluded:

- `data/raw/bacdive_strains.tsv:82792` is BacDive 160555,
  designation `spf2, PMUR`, taxon NCBITaxon:2736290, LPSN 36254,
  deposit DSM-103722. It is not filed under this target or its subtree.
- The full native object at `data/bacdive/records.jsonl.gz:82791`
  identifies Xylanibacter muris, taxon 2736290, with the same deposit
  and alias. Its type flag and genome references belong to Xylanibacter.
- The full native object at `data/straininfo/records.jsonl.gz:294672`
  is SI-ID 396783, own deposit SI-DP 903360 / DSM 103722,
  Xylanibacter muris taxon 2736290. Its relation lists PMUR and spf2.

These objects do not justify importing DSM 103722, its type status,
BacDive genome references or StrainInfo identity onto Streptomyces SPF2.
The zero target strain count is supported at the complete BacDive
inventory boundary despite the shared bare alias.

Additional complete, ignored-inclusive, case-insensitive whole-token
searches covered `data/atb/`, the full
`data/catalog/allthebacteria.tsv.xz` and StrainInfo link, assembly,
exclusion and compressed related-record tables. No target ID, label,
slug or SPF2 token matched. The raw-directory search included all
assembly/genome/related inventories. No eligible target culture-deposit
or BioSample source chain was established.

These bounded results support empty optional nomenclature, mappings and
genome links; they do not assert that no isolates or sequences exist
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
YAML or join a bare strain alias across conflicting source taxa.

## Follow-up Checks

No finding-specific check remains. Proposed SPF2 enrichment must first
distinguish the Streptomyces target from Xylanibacter's alias using
primary taxon/deposit evidence. Use authorized dry-run/canary steps and
both focused validators after regeneration. Corpus changes additionally
require `just verify-corpus` and full QC, neither claimed by this pass.

## Additional Notes

Absence checks included ignored files via full structured reads,
`find`, and `rg --no-ignore --hidden -z -i -w` token searches. Public
read-only NCBI requests used network escalation after established
sandbox DNS failures. The only manual write is this new report; strict
validation wrote its standard diagnostic. No record, source, prior
report, history or status was edited. No generator, refresh, paid
research, GitHub action or cross-repository write occurred. No Eukaryota
record was re-reviewed.
