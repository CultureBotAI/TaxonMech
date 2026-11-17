# YAML Record Review: Pseudomonas sp. BIHB 1415

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_bihb_1415.yaml`
- Started UTC: 2026-10-05T19:01:58Z
- Finished UTC: 2026-10-05T19:04:48Z
- Verdict: pass

## Target

The full 54-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034640`, Pseudomonas sp. BIHB 1415, rank `SPECIES`,
domain `BACTERIA`, parent `NCBITaxon:196821`, genetic code 11,
`EXACT` grounding, `SEEDED` status, and `strain_count: 0`.
A taxon record is not itself a genome or deposit.

Owning source and scope rows are `data/raw/ncbitaxon_taxa.tsv:221677`
and `curation/seed_scope.tsv:321988`.
`data/taxa/PATHS.tsv:14143` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_bihb_1415.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_bihb_1415.yaml --out /private/tmp/bihb1415-strict-20261005.tsv`: exit 0; one file, zero error files and zero error rows. The TSV contains only its header.
- Structured comparisons read the full backbone row and ten ancestors, PATHS, scope, attestation, and seed event. Seven raw source inventories and exact type-material, merged-ID, and dropped-record tables were checked.
- `rg --no-ignore --hidden -n -z -i` searched the ID, full label, slug, and BIHB 1415 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Hidden, ignored, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All three candidate rows were read in full with TSV headers or JSON decoding.
- Separate marker scanning across those roots found no JF766699 row. Ignored-inclusive filename and content searches under `reports` and `history`, including marker searches, found no prior target report or separate target history artifact before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, full sequence metadata, and three PubMed queries completed. Exact-name, marker, compact-strain-name, and strain/topic web searches were run. An unexpected accession search hit was checked against the rendered primary PDF and the distinct printed accession's GenBank metadata.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused source agreement does not prove corpus reproduction.
- iModulonDB and curator-added graph ID/label checks are inapplicable: no gene, regulator, protein, phenotype, transcriptomic result, or causal graph is asserted. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

NCBI Taxonomy EFetch and Datasets agree on taxon 1034640, exact
label, species rank, parent 196821, Bacteria division, and code 11.
The entire root-first lineage matches:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 72274 > 135621 > 286 > 196821`.
Its ten ancestors are root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria,
Pseudomonadales, Pseudomonadaceae, Pseudomonas, and unclassified
Pseudomonas. Labels and normalized ranks also agree.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034640);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034640).

The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31065`.
No synonyms, retirement target, or direct children occur in the
backbone. Exact type-material, merged-ID, and dropped-record checks
found no target row. Provisional species rank does not establish
valid nomenclatural publication. `EXACT` grounds this identifier,
not a genomic species assignment or identity with other BIHB isolates.

## Evidence

The single NCBITAXON attestation agrees in ID, label, count 1,
unit `NAME`, and snapshot 2026-09-13. This counts a name assertion,
not a biological isolate or genome. The scope row and the
2026-09-13T17:54:04Z `seed_from_sources` /
`SEEDED_FROM_SOURCES` event agree exactly.

The query `txid1034640[Organism:noexp]` returned zero Assembly
items with missing-phrase/no-items diagnostics and one Nuccore
item, UID 333496477. Full metadata and source/rRNA features identify
`JF766699.1`, a 1,483-base partial 16S rRNA sequence, with strain
BIHB 1415 and `taxon:1034640`. Source qualifiers explicitly record
rhizosphere, host pea, and country India. These are submitted
provenance, not assay results, precise sampling coordinates,
deposit identifiers, or a whole genome.
[GenBank JF766699.1](https://www.ncbi.nlm.nih.gov/nuccore/JF766699.1).

Gulati A., Rahi P., and Sharma N. directly submitted the marker
on 1 April 2011. Its associated pea-rhizosphere phosphate-solubilizing
genotypes study is marked unpublished in the inspected sequence
record. The title does not establish isolate-specific functional
results, and the institution's address is not a sampling locality.

PubMed searches for `JF766699[All Fields]`,
`"BIHB 1415"[All Fields] AND Pseudomonas[All Fields]`, and the
full sequence-reference title returned zero items. Query translations
and diagnostics were inspected. Bounded web searches did not
establish a primary target-specific experimental publication.

The exact-accession web query produced a misleading indexed table
from Duellman, Marion, and Hedges (2016), DOI
10.11646/zootaxa.4104.1.1. Rendered appendix page 80 actually
prints `FJ766699` in the COI column for Ecnomiohyla miliaria,
not `JF766699`. NCBI independently identifies `FJ766699.1` as
a 648-base mitochondrial COI sequence of that species, voucher
USNM:572844, taxon 318329. This is a different accession and
biological entity, not a source for BIHB 1415. The rendered page
and authority metadata resolve the apparent search-result conflict.
[Primary article, appendix page 80](https://webapps.fhsu.edu/ksHerp/bibFiles/5537.pdf);
[Distinct GenBank FJ766699.1](https://www.ncbi.nlm.nih.gov/nuccore/FJ766699.1).

## Completeness

The seven parsed inventories contain no exact target BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin, or BacTraits row. The wider native
search found only target backbone, scope, and scientific-name rows,
not an exact deposit, assembly, type material, or GTDB mapping.
Optional nomenclature, synonyms, mappings, strains, traits, and
graphs are appropriately empty under the local checklist.

`strain_count: 0` measures inventory coverage, not whether a
biological isolate exists. The marker and its explicit submitted
source qualifiers are optional enrichment leads. No missing
required representation was demonstrated. Target-specific functional
results and eventual publication of the submitted study remain
unresolved; no current YAML assertion depends on them.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. The misleading indexed accession
is not a defect in this YAML. Full-corpus reproduction and uninspected
experimental claims are not established by this focused review.

## Recommended Edits

No required edit is demonstrated. Preserve generated fields and
`SEEDED` status.

If optional sequence enrichment is separately authorized, define
and test the exact `taxon:1034640` / BIHB 1415 / `JF766699.1`
relation in maintained extraction inputs and logic
(`scripts/extract_source_inventory.py`, `src/taxonmech/extract.py`),
then adjust `scripts/seed_from_sources.py` only if needed.
`curation/seed_scope.tsv` owns scope, not inferred isolate identity.
Do not directly patch generated YAML/pages, label a marker as a
genome, or collapse the distinct JF and FJ accession prefixes.

## Follow-up Checks

For optional enrichment, re-read the versioned GenBank features,
retain host/country/source as submitted provenance, and test that
`FJ766699.1` and other BIHB isolates remain excluded. Regenerate
through the maintained pipeline, then rerun schema and strict checks.

Functional claims require inspected primary target-specific methods
and results with an exact identity bridge. Before publishing
regenerated products, run the documented corpus reproduction, QC,
tests, strict validation, provenance, history, and site gates.
This report supplies no such result and does not promote status.

## Additional Notes

PDF text extraction failed for many appendix glyphs, so page 80 was
rendered and inspected visually, including an upright rendering.
The indexed text was not trusted over the page image. The unrelated
external accession was checked only to reject a false evidence lead;
no Eukaryota YAML record was reviewed or changed.

All three native candidate rows were inspected. Search misses include
ignored files within the stated roots and remain bounded to those
sources and queries, not global absence claims. No paid research,
outbound contact, GitHub mutation, record/inventory/scope/history
edit, status promotion, or regeneration occurred.
