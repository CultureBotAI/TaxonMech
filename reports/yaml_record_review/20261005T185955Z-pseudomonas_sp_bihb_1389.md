# YAML Record Review: Pseudomonas sp. BIHB 1389

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_bihb_1389.yaml`
- Started UTC: 2026-10-05T18:58:22Z
- Finished UTC: 2026-10-05T18:59:55Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. The target is
`NCBITaxon:1034639`, Pseudomonas sp. BIHB 1389, rank `SPECIES`,
domain `BACTERIA`, parent `NCBITaxon:196821`, genetic code 11,
`EXACT` grounding, `SEEDED` status, and `strain_count: 0`.
It denotes a taxon, not a genome or deposit.

The owning source and scope rows are
`data/raw/ncbitaxon_taxa.tsv:221676` and
`curation/seed_scope.tsv:321987`.
`data/taxa/PATHS.tsv:14142` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_bihb_1389.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_bihb_1389.yaml --out /private/tmp/bihb1389-strict-20261005.tsv`: exit 0; one file, zero error files and zero error rows. The output TSV contains only its header.
- Structured comparisons read the full backbone row and ten ancestors, PATHS, scope, attestation, and seed event. Seven raw source inventories and exact type-material, merged-ID, and dropped-record tables were checked.
- `rg --no-ignore --hidden -n -z -i` searched the target ID, full label, slug, and BIHB 1389 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All four candidate rows were read completely with TSV headers or JSON decoding.
- Separate marker scanning across those roots found no JF766695 row. Ignored-inclusive filename and content searches under `reports` and `history`, including marker searches, found no prior target report or separate target history artifact before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, full sequence metadata, and three PubMed queries completed. Exact-name, marker, compact-strain-name, and strain/topic web searches were performed.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused checks do not establish corpus reproduction.
- iModulonDB and curator-added graph ID/label checks are inapplicable because no gene, regulator, protein, phenotype, transcriptomic, or graph assertion is present. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

NCBI Taxonomy EFetch and Datasets agree on taxon 1034639, exact
label, species rank, parent 196821, Bacteria division, and code 11.
The full root-first chain matches:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 72274 > 135621 > 286 > 196821`.
Its ten ancestors are root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria,
Pseudomonadales, Pseudomonadaceae, Pseudomonas, and unclassified
Pseudomonas; their labels and normalized ranks agree with the source.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034639);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034639).

The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31064`.
The backbone has no synonyms, retirement target, or direct children.
Exact type-material, merged-ID, and dropped-record checks found no
target row. Provisional species rank does not prove nomenclatural
publication, and `EXACT` does not imply a genome-defined species
or equivalence with other numbered BIHB isolates.

## Evidence

The single NCBITAXON attestation agrees in ID, label, count 1, unit
`NAME`, and snapshot 2026-09-13. A name assertion is not a strain
or genome count. Scope and the 2026-09-13T17:54:04Z
`seed_from_sources` / `SEEDED_FROM_SOURCES` event agree exactly.

The query `txid1034639[Organism:noexp]` returned zero Assembly
items with missing-phrase/no-items diagnostics and one Nuccore
item, UID 333496473. Full metadata and source/rRNA features identify
`JF766695.1`, a 1,483-base partial 16S rRNA sequence, with strain
BIHB 1389 and `taxon:1034639`. Explicit source qualifiers record
rhizosphere, host pea, and country India. Those support submitted
provenance, not assays, precise sampling coordinates, a culture
deposit, or a genome.
[GenBank JF766695.1](https://www.ncbi.nlm.nih.gov/nuccore/JF766695.1).

Gulati A., Rahi P., and Sharma N. directly submitted this marker
on 1 April 2011. Its associated pea-rhizosphere phosphate-solubilizing
genotypes study is marked unpublished in the inspected sequence
record. The study title does not prove target-specific functional
results; the submitter's institutional address is not an isolation
locality.

PubMed queries for `JF766695[All Fields]`,
`"BIHB 1389"[All Fields] AND Pseudomonas[All Fields]`, and the
full sequence-reference title returned zero items. Query translations
and diagnostics were inspected. Exact marker and compact-name web
queries returned no results; the broader bounded searches did not
establish a primary target-specific experimental publication.
No trait is transferred from generic Pseudomonas literature or
other BIHB isolates.

## Completeness

The seven parsed inventories contain no exact target BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin, or BacTraits row. The wider native
search found target backbone, scope, and scientific-name rows plus
one unrelated length-field collision. It did not establish a target
deposit, assembly, type material, or GTDB mapping.

Empty optional nomenclature, synonyms, mappings, strains, traits,
and graphs are appropriate under the local checklist.
`strain_count: 0` measures inventory coverage; it does not deny
the isolate documented by GenBank. The marker and its explicit source
qualifiers are optional enrichment leads, not a missing required
genome/deposit representation. Eventual publication of the submitted
study and target-specific functional results remain unresolved, and
the current YAML makes no assertion depending on them.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. Full-corpus reproduction and
uninspected experimental claims are not established by this focused
review.

## Recommended Edits

No required edit is demonstrated. Preserve generated values and
`SEEDED` status.

If sequence enrichment is separately authorized, define and test the
exact `taxon:1034639` / BIHB 1389 / `JF766695.1` relation in
maintained extraction inputs and logic
(`scripts/extract_source_inventory.py`, `src/taxonmech/extract.py`),
then adjust `scripts/seed_from_sources.py` only if needed.
`curation/seed_scope.tsv` owns scope, not inferred isolate identity.
Do not patch generated YAML/pages, label a marker as a genome, or
interpret an ungapped-length match as a taxon identity.

## Follow-up Checks

Optional enrichment should re-read the versioned GenBank features,
preserve submitted source scope, and test that other BIHB isolates
and the unrelated assembly below remain excluded. Regenerate through
the maintained pipeline, then rerun focused schema and strict checks.

Functional claims need inspected primary target-specific methods
and results plus an exact identity bridge. Before publishing
regenerated products, run the documented corpus reproduction, QC,
tests, strict validation, provenance, history, and site gates.
This report supplies no such result and does not promote status.

## Additional Notes

The fourth native candidate,
`data/catalog/ncbi_genbank-0034.jsonl.gz:21827`, is
`GCA_036806045.1`, Salinicoccus roseus isolate CTOTU5042,
with taxid/species_taxid 45670, BioSample SAMN28750010, and
BioProject PRJNA843551. Its `genome_size_ungapped: 1034639`
caused the match, not a target identifier. The full decoded row
was inspected and rejected as target evidence.

Search misses include ignored files within the stated roots and
remain bounded to those sources and queries, not global absence
claims. No paid research, outbound contact, GitHub mutation,
record/inventory/scope/history edit, status promotion, regeneration,
or Eukaryota review occurred.
