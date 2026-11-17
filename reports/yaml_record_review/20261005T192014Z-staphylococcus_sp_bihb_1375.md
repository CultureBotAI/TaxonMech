# YAML Record Review: Staphylococcus sp. BIHB 1375

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_bihb_1375.yaml`
- Started UTC: 2026-10-05T19:18:25Z
- Finished UTC: 2026-10-05T19:20:14Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034644`, Staphylococcus sp. BIHB 1375, rank `SPECIES`,
domain `BACTERIA`, parent `NCBITaxon:91994`, genetic code 11,
`EXACT` grounding, `SEEDED` status, and `strain_count: 0`.
This taxon is not itself a culture deposit or genome.

Owning source and scope rows are `data/raw/ncbitaxon_taxa.tsv:221681`
and `curation/seed_scope.tsv:321992`.
`data/taxa/PATHS.tsv:14147` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_sp_bihb_1375.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_sp_bihb_1375.yaml --out /private/tmp/bihb1375-strict-20261005.tsv`: exit 0; one file, zero error files and zero error rows. The output TSV contains only its header.
- Structured comparisons read the full backbone row and ten ancestors, PATHS, scope, attestation, and seed event. Seven raw source inventories and exact type-material, merged-ID, and dropped-record tables were checked.
- `rg --no-ignore --hidden -n -z -i` searched the target ID, full label, slug, and BIHB 1375 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All three candidate rows were read completely with TSV headers or JSON decoding.
- Separate marker scanning across those roots found no JF766691 row. Ignored-inclusive filename and content searches under `reports` and `history`, including marker searches, found no prior target report or separate target history artifact before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, full sequence metadata, and three PubMed queries completed. Exact-name, marker, compact-strain-name, and strain/topic web searches were performed. The primary paper's Table 1, relevant methods/results, and full metadata of its comparison marker GU646894.1 were inspected.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused source agreement does not prove corpus reproduction.
- iModulonDB and curator-added graph ID/label checks are inapplicable because the record makes no gene, regulator, protein, phenotype, transcriptomic, or graph assertion. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

NCBI Taxonomy EFetch and Datasets agree on taxon 1034644, exact
label, species rank, parent 91994, Bacteria division, and code 11.
The full root-first lineage matches:
`1 > 131567 > 2 > 1783272 > 1239 > 91061 > 1385 > 90964 > 1279 > 91994`.
All ten ancestors have the correct labels and normalized ranks:
root, cellular organisms, Bacteria, Bacillati, Bacillota, Bacilli,
Caryophanales, Staphylococcaceae, Staphylococcus, and
unclassified Staphylococcus.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034644);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034644).

The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31069`.
The backbone contains no synonyms, retirement target, or direct
children. Exact type-material, merged-ID, and dropped-record checks
found no target row. Provisional species rank does not prove valid
nomenclatural publication. `EXACT` grounds this identifier, not a
genomic species assignment or equivalence with other BIHB isolates.

## Evidence

The sole NCBITAXON attestation agrees in ID, label, count 1, unit
`NAME`, and snapshot 2026-09-13. This is a count of name assertions,
not genomes or biological isolates. Scope and the
2026-09-13T17:54:04Z `seed_from_sources` /
`SEEDED_FROM_SOURCES` event agree exactly.

The query `txid1034644[Organism:noexp]` returned zero Assembly
items with missing-phrase/no-items diagnostics and one Nuccore
item, UID 333496469. Full metadata and source/rRNA features identify
`JF766691.1`, a 1,495-base partial 16S rRNA sequence, strain
BIHB 1375, with `taxon:1034644`. The explicit source qualifiers
record rhizosphere, host pea, and country India. These are submitted
provenance, not measured phenotypes, precise sampling coordinates,
a culture deposit, or a genome.
[GenBank JF766691.1](https://www.ncbi.nlm.nih.gov/nuccore/JF766691.1).

Gulati A., Rahi P., and Sharma N. directly submitted the marker
on 1 April 2011. The associated pea-rhizosphere phosphate-solubilizing
genotypes study is marked unpublished in the inspected sequence
record. Its title does not establish target-specific functional
results. The submitter's institutional address is not the sampling
locality.

PubMed queries for `JF766691[All Fields]`,
`"BIHB 1375"[All Fields] AND Staphylococcus[All Fields]`, and the
full sequence-reference title returned zero items. Query translations
and diagnostics were inspected. These queries do not search every
full-text table and are not proof that the marker is absent from
published literature.

Exact-name and marker web searches identified Papaleo et al. (2015),
DOI 10.2174/1874285801509010098. The publisher's Table 1 explicitly
separates isolate 708, its marker GU646894, and its first BLAST hit
JF766691 / Staphylococcus sp. BIHB 1375. Plasmid presence is positive
for isolate 708. The methods describe Italian field-soil isolates
and database similarity searches, not experimentation on BIHB 1375.
Consequently this is a comparison-reference citation, not evidence
that BIHB 1375 carries that plasmid or came from the Italian site.
[Primary paper, Table 1 and methods](https://openmicrobiologyjournal.com/VOLUME/9/PAGE/98/FULLTEXT/).

Independent full metadata for GU646894.1 confirm a 622-base partial
16S marker for Staphylococcus sp. 708(2010), strain 708,
`taxon:911461`, with maize-cultivated soil and Italy: Agugliano
source qualifiers. Those differ from BIHB 1375's exact taxon and
Indian pea-rhizosphere provenance. A first BLAST hit does not establish
isolate equivalence.
[Comparison marker GU646894.1](https://www.ncbi.nlm.nih.gov/nuccore/GU646894.1).

No phosphate-solubilization, growth-promotion, plasmid carriage,
resistance, or other trait is inferred from a title, similarity hit,
genus, or adjacent isolate numbers.

## Completeness

The seven parsed inventories contain no exact target BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin, or BacTraits row. The wider native
search found only target backbone, scope, and scientific-name rows,
not an exact deposit, type material, assembly, or GTDB mapping.
Optional nomenclature, synonyms, mappings, strains, traits, and
graphs are appropriately empty under the local checklist.

`strain_count: 0` measures inventory coverage, not whether a
biological isolate exists. The exact marker and its explicit source
qualifiers are optional enrichment leads, not a required genome
or deposit representation. No missing required field was demonstrated.
Eventual publication of the submitted study and target-specific
experimental results remain unresolved; no current YAML assertion
depends on them.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. Full-corpus reproduction and
uninspected experimental claims are not established by this review.

## Recommended Edits

No required edit is demonstrated. Preserve generated fields and
`SEEDED` status.

If optional sequence enrichment is separately authorized, define
and test the exact `taxon:1034644` / BIHB 1375 / `JF766691.1`
relation in maintained extraction inputs and logic
(`scripts/extract_source_inventory.py`, `src/taxonmech/extract.py`),
then adjust `scripts/seed_from_sources.py` only if needed.
`curation/seed_scope.tsv` owns scope, not inferred isolate identity.
Do not directly patch generated YAML/pages, label a marker as a
genome, or turn a BIHB strain number into a deposit accession.

## Follow-up Checks

Optional enrichment should re-read the versioned GenBank features,
preserve host/country/source as submitted provenance, and test that
other BIHB isolates and comparison isolate 708 / GU646894.1 remain
excluded. Regenerate through the maintained
pipeline, then rerun focused schema and strict validation.

Functional claims require inspected primary target-specific methods
and results plus an exact identity bridge. Before publishing
regenerated products, run the documented corpus reproduction, QC,
tests, strict validation, provenance, history, and site gates.
This report supplies no such result and does not promote status.

## Additional Notes

All three native candidates are the exact backbone, scope, and
scientific-name rows above. Search misses include ignored files
within the stated roots and remain bounded to those sources and
queries, not global absence claims. No paid research, outbound
contact, GitHub mutation, record/inventory/scope/history edit,
status promotion, regeneration, or Eukaryota review occurred.
