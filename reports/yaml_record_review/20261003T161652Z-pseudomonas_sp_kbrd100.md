# YAML Record Review: Pseudomonas sp. KBRD100

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_kbrd100.yaml`
- Started UTC: 2026-10-03T16:15:41Z
- Finished UTC: 2026-10-03T16:16:52Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303816`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:196821`, genetic code 11, grounding `EXACT`, status `SEEDED`.
Ten lineage entries, one NCBI NAME attestation, strain count zero and one
embedded seed event are present. There are no synonyms, nomenclature,
taxonomy mappings, equivalence xrefs, strain rows, genome links,
experimental claims or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_kbrd100.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_kbrd100.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured NCBI backbone comparison reproduces identity,
  rank, parent, code and every lineage entry. No target children occur
  in that backbone. Full exact-field inventory scans find no direct
  BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits taxon
  membership. PATHS and scope each contain exactly one target row.
- `just verify-corpus`: Not checked; full-corpus-only, with no focused
  substitute invented. Full QC, global provenance, rendered products,
  exports and sequence content were not audited.
- Ignored-inclusive history searches found no target standalone entry;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308149` reproduces the exact label,
species rank, unclassified-Pseudomonas parent, code and empty synonym
fields. The complete native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30698` agrees.

The NCBI browser page was inaccessible through the web tool. Inspected
current [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303816&retmode=xml)
confirms ID, label, species rank, Bacteria division, parent 196821,
code 11 and the full non-root lineage without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303816)
confirms rank and all ten ancestor IDs including root. Read-only public
API requests used network escalation after established sandbox DNS
failures. NCBI grounding is supported.

Preserve NCBI's species rank and the `NO_RANK` unclassified parent;
the KBRD100 designation does not justify changing the rank or assigning
a named species. `EXACT` grounds this source entity, not a validly
published binomial or a broader Pseudomonas species equivalence.

## Evidence

The NCBITAXON / NCBITaxon:1303816 / 1 NAME attestation matches
the backbone row and its 2026-09-13 snapshot. The native name object
independently corroborates the spelling. One NAME is a source count,
not evidence for a strain deposit, phenotype or genome. No DOI, PMID,
assembly accession or experimental quotation is asserted.

`curation/seed_scope.tsv:393097` admits the target on 2026-09-13
with the exact one-source reason carried in its embedded event. That
event is dated 2026-09-13T17:54:04Z, curator seed_from_sources,
action SEEDED_FROM_SOURCES. Source names and `SEEDED` status agree;
no human-review claim is made.

## Completeness

Ignored-inclusive searches by target ID, full label, slug and KBRD100
covered `data/raw/`, `curation/`, `history/` and all compressed JSONL
files under `data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/straininfo/` and `data/seqcode/`. Only the target
scientific-name object matched the native catalogs.

No target BacDive strain, LPSN inventory name, GTDB mapping/genome,
NCBI assembly, BV-BRC genome, GOLD organism, SeqCode name or StrainInfo
native object was found in those bounded sources. Complete BacDive
membership and the singleton subtree support strain count zero; this
does not assert that biological strains or sequences are absent elsewhere.

Additional ignored-inclusive searches of StrainInfo link, assembly and
exclusion TSVs, its compressed related-record table, `data/atb/` and the
complete `data/catalog/allthebacteria.tsv.xz` found no target ID,
designation, label or slug. Raw assembly/genome/related tables were
included in the raw-directory search. No eligible culture-deposit,
BioSample or genome source chain was established.

Optional synonym, nomenclature, mapping and strain fields are correctly
empty at the checked source boundary. Do not inherit a nearby species'
type status or phenotype. No named gene, locus, regulator, pathway,
trait or transcriptomics dataset is asserted; iModulonDB is not applicable.
No causal graph is required for this identity-only record.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required. Preserve the supported backbone and generated-file
boundary. Any future source-backed enrichment belongs in maintained
extraction inputs or `src/taxonmech/extract.py`, with changed seeding
behavior in `src/taxonmech/seed.py` and regression tests, not a manual
YAML edit. Keep `SEEDED`; this automated review does not promote status.

## Follow-up Checks

No finding-specific check is outstanding. New primary evidence would
require exact identity/deposit verification, authorized dry-run/canary
steps and both focused validators after regeneration. Any corpus change
also requires `just verify-corpus` and full QC. This focused passing
verdict does not claim those unrun corpus-wide gates passed.

## Additional Notes

Absence checks included ignored files through full structured reads,
`find`, and `rg --no-ignore --hidden`, using `-z` for compressed sources.
The only manual write is this report; strict validation wrote its standard
diagnostic. No record, source, prior report, history or status was edited.
No generator, refresh, paid research, GitHub mutation or cross-repository
write occurred. No Eukaryota record was re-reviewed.
