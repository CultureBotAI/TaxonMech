# YAML Record Review: Providencia sp. BIHB 1402

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/providencia_sp_bihb_1402.yaml`
- Started UTC: 2026-10-05T18:43:29Z
- Finished UTC: 2026-10-05T18:49:12Z
- Verdict: pass

## Target

The complete 54-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034636`, Providencia sp. BIHB 1402, with `SPECIES`
rank, `BACTERIA` domain, parent `NCBITaxon:2633465`, genetic
code 11, `EXACT` grounding, `SEEDED` status, and
`strain_count: 0`. This taxon record is not itself a genome or deposit.

Owning source and scope rows are
`data/raw/ncbitaxon_taxa.tsv:221673` and
`curation/seed_scope.tsv:321984`.
`data/taxa/PATHS.tsv:14139` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/providencia_sp_bihb_1402.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/providencia_sp_bihb_1402.yaml --out /private/tmp/bihb1402-strict-20261005.tsv`: exit 0; one file, zero files with errors and zero error rows. The output TSV contains only its header.
- Structured checks read the full backbone row and ten ancestors, PATHS, scope, attestation, and seed event. Exact-ID comparisons covered seven raw source inventories, type material, merged IDs, and dropped records.
- `rg --no-ignore --hidden -n -z -i` searched target ID, full label, slug, and BIHB 1402 separator variants across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All four matches were read in full with TSV headers or JSON decoding: backbone, scope, native NCBI name, and an unrelated assembly row with a numeric collision.
- Separate marker scanning across those roots found no JF766697 row. Ignored-inclusive filename and content searches under `reports` and `history` found no prior target report or separate target history artifact, including marker searches, before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, full sequence metadata, and three bounded PubMed queries completed. Exact-name, marker, and strain/topic web searches were performed. Relevant primary article text and a university-hosted thesis table were inspected, including visual checks of both comparison tables.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused source agreement does not prove corpus reproduction.
- iModulonDB and curator-added graph ID/label checks are not applicable: the record asserts no gene, regulator, protein, phenotype, transcriptomic result, or causal graph. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

NCBI Taxonomy EFetch and Datasets agree on taxon 1034636, exact label,
species rank, parent 2633465, Bacteria division, and code 11.
The complete root-first chain matches:
`1 > 131567 > 2 > 3379134 > 1224 > 1236 > 91347 > 1903414 > 586 > 2633465`.
The ten ancestors are root, cellular organisms, Bacteria,
Pseudomonadati, Pseudomonadota, Gammaproteobacteria,
Enterobacterales, Morganellaceae, Providencia, and unclassified
Providencia. Their labels and normalized ranks agree with the source.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034636);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034636).

The native scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31061`.
The backbone has no synonyms, retirement target, or direct children.
Exact type-material, merged-ID, and dropped-record checks found no
target row. Provisional species rank does not imply valid nomenclatural
publication; `EXACT` grounds this identifier, not a genomic species
assignment or identity with other numbered BIHB isolates.

## Evidence

The single NCBITAXON attestation agrees in identifier, label, count 1,
unit `NAME`, and snapshot 2026-09-13. It counts a name assertion,
not a strain or genome. Scope and the 2026-09-13T17:54:04Z
`seed_from_sources` / `SEEDED_FROM_SOURCES` event agree.

The exact query `txid1034636[Organism:noexp]` returned zero Assembly
items with missing-phrase/no-items diagnostics and one Nuccore item,
UID 333496475. Full metadata and source/rRNA features identify
`JF766697.1`, a 1,487-base partial 16S rRNA sequence, strain
BIHB 1402, taxon 1034636. Source qualifiers explicitly record
rhizosphere, host pea, and country India. These are submitted
provenance, not assay results, precise sampling coordinates, a
culture-deposit accession, or a genome.
[GenBank JF766697.1](https://www.ncbi.nlm.nih.gov/nuccore/JF766697.1).

Gulati A., Rahi P., and Sharma N. directly submitted the marker on
1 April 2011. The associated pea-rhizosphere phosphate-solubilizing
genotypes study remains marked unpublished in the inspected sequence
record. Its title does not establish BIHB 1402's measured phenotype;
the institution's address is not a sampling location.

PubMed queries for `JF766697[All Fields]`,
`"BIHB 1402"[All Fields] AND Providencia[All Fields]`, and the
full sequence-reference title returned zero items. Returned query
translations and diagnostics were inspected. This is a bounded
index result, not proof that the sequence is never mentioned in
published literature: two exact-name comparison leads were found.

Zhang and colleagues' 2013 article concerns experimentally tested
isolate SY-1. Table 2, printed page 25, lists BIHB 1402 / JF766697
as a reference sequence with an RDP S_ab score of 0.963 relative
to SY-1. That score is not reported percent identity, and neither
the sequence comparison nor the adjacent SY-1 biochemical table
makes the isolates identical. SY-1's pathogenicity and physiology
must not be assigned to BIHB 1402.
[Zhang et al., primary article, DOI 10.5897/JBR2012.0109](https://academicjournals.org/journal/JBR/article-full-text-pdf/2DA6A219996).

Philipp Heise's 2019 thesis, appendix printed page 95 (PDF page 101),
separately lists study isolates 1FH2, 1FM2, and 1MH1 with BIHB 1402
as their closest available BLASTn reference. The table distinguishes
the isolate identifiers from their reference match and supplies no
identity bridge making them BIHB 1402. It does not establish a beetle
origin or antimicrobial phenotype for the target isolate.
[Heise thesis, university repository](https://jlupub.ub.uni-giessen.de/server/api/core/bitstreams/de3c2e62-179c-4975-b603-55666d2c2055/content).

## Completeness

The seven raw-source checks found no exact target BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin, or BacTraits row. The wider native search
did not establish a target deposit, type material, assembly, or GTDB
mapping. Optional nomenclature, synonyms, mappings, strains, traits,
and graphs are appropriately empty for the seeded record.
`strain_count: 0` measures classified inventory coverage; it
does not deny the isolate documented by GenBank.

The exact marker and its explicit host/country/source qualifiers are
optional enrichment leads, not a required whole-genome or deposit
representation under the local checklist. No consequential missing
required field was demonstrated. The submitted pea-rhizosphere
study's eventual publication and target-specific experimental
details remain unresolved; no current YAML phenotype assertion
depends on them.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed record. Full-corpus reproduction and
uninspected experimental claims are not established by this focused
review.

## Recommended Edits

No required edit is demonstrated. Preserve generated fields and
`SEEDED` status.

If sequence enrichment is separately authorized, define and test the
exact `taxon:1034636` / BIHB 1402 / `JF766697.1` relation in
maintained extraction inputs and logic
(`scripts/extract_source_inventory.py`, `src/taxonmech/extract.py`),
then adjust `scripts/seed_from_sources.py` only if needed.
`curation/seed_scope.tsv` owns scope, not inferred isolate identity.
Do not patch generated YAML/pages or turn a marker into a genome,
a sequence-reference comparison into isolate equivalence, or a
BIHB number into a deposit.

## Follow-up Checks

Future enrichment should re-read the versioned GenBank features,
preserve host/country/source at submitted-provenance scope, and test
that SY-1, 1FH2, 1FM2, 1MH1, and unrelated BIHB isolates remain
excluded. Regenerate through the documented maintained pipeline,
then rerun focused schema and strict validation.

Future functional claims require inspected primary target-specific
methods/results and an exact identity bridge. Before publishing
regenerated products, run the documented full-corpus reproduction,
QC, tests, strict validation, provenance, history, and site gates.
This report supplies no such result and does not promote status.

## Additional Notes

The fourth native candidate,
`data/catalog/ncbi_genbank-0063.jsonl.gz:33633`, is
`GCA_964591215.1`, an uncultured archaeon with taxid and
species_taxid 115547, isolate SRP201947_co1_36, BioSample
SAMEA117392068, and BioProject PRJEB82487. The search matched its
`genome_size: 1034636`, not a taxon identity. Its complete decoded
row was inspected and rejected as target evidence.

The article's publisher PDF was readable through the web tool;
direct download returned HTTP 403, so the indexed article mirror
was used for the page-25 visual check. The university's download
route returned HTML; its content API supplied the thesis PDF for
text and page-95 visual inspection. These access fallbacks do not
change the source attribution.

Search misses are bounded to the stated sources and queries, not
global proof of absence. No paid research, outbound contact,
GitHub mutation, YAML/inventory/scope/history edit, status promotion,
regeneration, or Eukaryota-record review occurred.
