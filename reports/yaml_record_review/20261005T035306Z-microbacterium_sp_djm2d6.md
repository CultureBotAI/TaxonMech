# YAML Record Review: Microbacterium sp. DJM2D6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_djm2d6.yaml`
- Started UTC: 2026-10-05T03:51:47Z
- Finished UTC: 2026-10-05T03:53:06Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034222`, Microbacterium sp. DJM2D6. It represents an isolate placeholder assigned `SPECIES` rank by NCBI, with bacterial domain, parent `NCBITaxon:2609290`, genetic code 11, `EXACT` grounding, `SEEDED` status, and `strain_count: 0`. The single NCBITAXON attestation counts one `NAME` from the 2026-09-13 snapshot.

This is not a claim of validly published species nomenclature. Maintained ownership lies in `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`. The generated record is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/microbacterium_sp_djm2d6.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/microbacterium_sp_djm2d6.yaml --out /private/tmp/microbacterium-djm2d6-strict-20261005.tsv`: exit 0; one file scanned, zero files with errors and zero error rows.
- Bounded structured source checks passed identifier, label, rank, parent, code, all ancestors, synonyms, attestation, path, scope, and inline seed-event comparisons.
- `just verify-corpus`: not run; it has no record selector. Its `--max-diffs` diagnostic cap does not limit corpus scope.
- `just validate-products`: not applicable because no curator-added graph nodes or product labels occur.
- `just validate-history`: not run because the ignored-inclusive target-history search found no separate artifact. The inline seed event was inspected. No event or review-status change was added.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221490` agrees with every seeded identity field and supplies no synonyms. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30842` identifies the same taxon and has an empty unique-name field.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034222&retmode=xml) confirms exact label, parent, species rank, genetic code 11, and ancestor labels/ranks. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034222) independently agrees with identity and the root-inclusive lineage. The taxonomy browser page was inaccessible through the web tool; the structured responses were read.

All ten root-first ancestors match the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 1783272 Bacillati, 201174 Actinomycetota, 1760 Actinomycetes, 85006 Micrococcales, 85023 Microbacteriaceae, 33882 Microbacterium, and 2609290 unclassified Microbacterium. The record preserves NCBI's placement without reconciling or inferring another taxonomy.

## Evidence

`data/taxa/PATHS.tsv:13952` uniquely assigns the record slug. `curation/seed_scope.tsv:321808` has the 2026-09-13 scope date and exact one-source reason carried by the inline 2026-09-13T17:54:04Z `SEEDED_FROM_SOURCES` event. The one-name attestation is not a strain or genome count.

Full structured scans found no target rows in the mapped BacDive, LPSN, GTDB, GOLD organism, MediaDive, Madin, or BactoTraits inventories. No target children were present in the backbone. Exact type-material, merged-ID, and dropped-record scans were negative.

The exact-taxid Nuccore query returned one accession. Its full metadata, references, and features were inspected: [JF753515.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753515.1), a 658-base partial 16S rRNA gene sequence. The organism label, strain DJM2D6, and taxon cross-reference 1034222 agree. Source qualifiers describe Zea seed isolation. This supplies a marker identity and bounded isolation context, not an assembly, authenticated collection deposit, or phenotype.

The marker explicitly cites PMID 21673982 and DOI 10.1371/journal.pone.0020396. They agree with previously fetched and inspected [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml) for Johnston-Monje and Raizada's 2011 paper. Previously inspected [publisher methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) give the culture-derived interval JF753401-JF753552, containing this accession. No new full-paper fetch or supplementary-row inspection is claimed here.

## Completeness

Boundary-aware identifier, label/slug, and designation searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only `SOURCE.json` manifests. Searches included ignored, hidden, and compressed files. Exactly the backbone, native scientific name, and scope contexts matched. A secondary search for the whole marker accession, PMID, and DOI found zero matches in this scope. Separate ignored-inclusive exact prior-report filename and history searches were negative. These are bounded local-source results.

The live exact-taxid Assembly search returned count zero and no IDs, with phrase-not-found/no-items diagnostics. That result does not prove no genome exists anywhere. No eligible collection-deposit or genome join was established by the inspected evidence.

`strain_count: 0` correctly counts inventoried BacDive entries, according to `src/taxonmech/seed.py:483` and its line-543 count assignment. A culture-derived marker and GenBank strain qualifier do not create a BacDive entry or a CAFI-qualified deposit. Optional nomenclature, mapping, strain, genome, and causal-graph slots are appropriately empty. Omitting an optional marker/paper citation is not a material defect in this identity seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record's represented identity and provenance are supported. Supplementary tables S3/S4 remain uninspected, so no DJM2D6-specific phenotype, host genotype, medium, transmission, or growth-promotion claim is made. Community-level results and results for other named isolates cannot supply those claims.

## Recommended Edits

None required. Preserve the generated record and `SEEDED` status. Do not manufacture a culture accession from DJM2D6 or count its 16S marker as a genome.

Optional enrichment would first require an exact supported source row and a suitable maintained evidence input. Inventory/overlay and `src/taxonmech/seed.py` changes, if necessary, need focused tests before authorized regeneration.

## Follow-up Checks

Inspect the exact supplementary DJM2D6 row with headers and units before adding any isolate-level experimental assertion. For a later authorized maintained-input change, rerun the focused schema and strict validators and then full-corpus reproduction and relevant repository gates.

## Additional Notes

The prescribed spreadsheet dependency loader was checked this turn and is unavailable; earlier supplement downloads failed. No spreadsheet workaround or uninspected row claim was used. iModulonDB is not applicable to this taxonomic identity seed, which names no gene, regulator, or transcriptomic assertion.

Only this new report was added. No target YAML, inventory, existing report, history, generated page, or review status was edited.

