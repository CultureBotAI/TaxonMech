# YAML Record Review: Halobacillus sp. HSQAY1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/halobacillus_sp_hsqay1.yaml`
- Started UTC: 2026-10-03T16:04:46Z
- Finished UTC: 2026-10-03T16:06:24Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` before judgement. It denotes
`NCBITaxon:1303812`, rank `SPECIES`, domain `BACTERIA`, parent
`NCBITaxon:2636472`, genetic code 11, grounding `EXACT`, status `SEEDED`.
Ten lineage entries, a single NCBI NAME attestation, strain count zero
and one seed event are present. There are no synonyms, nomenclature,
taxonomy mappings, equivalence xrefs, strain rows, genome links,
experimental claims or causal graph.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/halobacillus_sp_hsqay1.yaml`:
  PASS; no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/halobacillus_sp_hsqay1.yaml`:
  PASS; one file, zero errors; diagnostic
  `reports/instance_validation_failures.tsv`.
- Complete structured NCBI backbone comparison reproduces identity,
  rank, parent, genetic code and every lineage entry. No children occur
  under this target in the pinned backbone.
- Complete exact-field scans find no BacDive, LPSN, GTDB, GOLD,
  MediaDive, Madin or BactoTraits taxon inventory membership. The PATHS
  index and scope each have one target row.
- `just verify-corpus`: Not checked; full-corpus-only. No focused
  substitute was invented. Full QC, global provenance, generated products,
  exports and sequence content were not audited.
- Ignored-inclusive history searches found no target standalone entry;
  standalone history validation had no target. Strict validation checked
  the embedded event. Graph/product gates are not applicable.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:308145` supports the exact scientific
name, species rank, unclassified-Halobacillus parent, code 11 and empty
synonym fields. The complete native scientific-name object at
`data/catalog/ncbi_names-0007.jsonl.gz:30694` agrees.

The NCBI browser page was inaccessible through the web tool. Inspected
current [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1303812&retmode=xml)
confirms the target ID, label, species rank, Bacteria division, parent
2636472, code 11 and full non-root lineage, without alternate names.
[NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1303812)
confirms rank and all ten ancestor IDs including root. Public read-only
API calls used network escalation after sandbox DNS failures had been
established during this review session.

The designation HSQAY1 does not justify changing NCBI's species rank
to strain. The unclassified grouping is an explicit `NO_RANK` ancestor,
not an inferred species assignment. `EXACT` refers to this NCBI entity,
not to a nomenclaturally validated binomial or a resolved named species.

## Evidence

The single attestation, NCBITAXON / NCBITaxon:1303812 / 1 NAME,
matches the primary-backbone row and its 2026-09-13 snapshot. One NAME
is a source count, not an experimental observation, strain count or genome
count. No cited DOI, PMID, source accession or quoted snippet is present.

`curation/seed_scope.tsv:393093` admits the record on 2026-09-13
with the exact one-source reason carried in its embedded seed event.
The event timestamp is 2026-09-13T17:54:04Z, curator seed_from_sources,
action SEEDED_FROM_SOURCES. Source names and `SEEDED` status agree;
the event does not claim human review.

## Completeness

Ignored-inclusive searches by taxon ID, full label, slug and HSQAY1
covered `data/raw/`, `curation/` and `history/`. Compressed searches
covered all JSONL files under `data/catalog/`, `data/bacdive/`,
`data/bvbrc/`, `data/gold/`, `data/straininfo/` and `data/seqcode/`.
Only the target NCBI scientific-name object matched the native catalogs.

No matching BacDive strain, LPSN inventory name, GTDB genome/mapping,
NCBI assembly, BV-BRC genome, GOLD organism, SeqCode name or StrainInfo
native object was found in those bounded sources. Full BacDive membership
and the singleton subtree support strain count zero; this does not assert
that the biological isolate or its sequences are absent elsewhere.

Additional ignored-inclusive searches of StrainInfo link, assembly and
exclusion TSVs, its compressed related-record table, `data/atb/` and the
complete `data/catalog/allthebacteria.tsv.xz` found no target ID,
designation, label or slug. Raw genome/assembly/related tables were covered
by the raw-directory search. No supported culture deposit or BioSample
join was discovered, so no genome link should be invented.

Optional synonym, nomenclature, mapping and strain slots are correctly
empty at the checked source boundary. No type status can be inherited
from a nearby species. No named gene, locus, regulator, pathway, trait or
transcriptomics dataset is asserted; iModulonDB is not applicable. Lack
of such evidence does not call for an invented phenotype or causal graph.

## Findings

- Blocker: None found.
- Major: None found.
- Minor: None found.

## Recommended Edits

None required by this review. Preserve the supported NCBI classification
and generated-file boundary. Any future source-backed enrichment belongs
in maintained extraction inputs or `src/taxonmech/extract.py`, with
seeder behavior in `src/taxonmech/seed.py` and regression coverage,
not a hand edit to the YAML. Keep `SEEDED`; this report does not authorize
a human-review status promotion.

## Follow-up Checks

No finding-specific follow-up is required. If new primary identity,
deposit or genome evidence becomes available, verify exact source scope
before changing maintained inputs, use the documented authorized
dry-run/canary workflow, and rerun both focused validators. Any generated
corpus change also requires `just verify-corpus` and full QC. This focused
passing verdict does not claim those unrun corpus-wide gates passed.

## Additional Notes

The only manual write is this report; strict validation wrote its standard
diagnostic. Searches used full structured reads, `find`, or
`rg --no-ignore --hidden`, with `-z` for compressed sources, so ignored
files were included. No record, source, prior report, history or status was
edited. No generator, refresh, paid research, GitHub mutation or
cross-repository write occurred. No Eukaryota record was re-reviewed.
