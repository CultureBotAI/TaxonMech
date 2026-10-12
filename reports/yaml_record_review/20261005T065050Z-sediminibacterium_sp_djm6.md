# YAML Record Review: Sediminibacterium sp. DJM6

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sediminibacterium_sp_djm6.yaml`
- Started UTC: 2026-10-05T06:46:24Z
- Finished UTC: 2026-10-05T06:50:50Z
- Verdict: pass

## Target

Read all 60 lines of the generated `TaxonRecord` for `NCBITaxon:1034285`, Sediminibacterium sp. DJM6. The record represents a bacterial isolate placeholder with NCBI `SPECIES` rank, parent `NCBITaxon:2635961`, genetic code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. Its sole attestation counts one NCBITAXON `NAME` from the 2026-09-13 snapshot. This rank is not a claim of validly published nomenclature or identification as a named species.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`. The generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/sediminibacterium_sp_djm6.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/sediminibacterium_sp_djm6.yaml --out /private/tmp/sediminibacterium-djm6-strict-20261005.tsv`: exit 0; one file scanned, zero error files or rows.
- Structured source comparisons passed identity, full lineage, synonyms, attestation, path-index, scope, and inline-event checks.
- `just verify-corpus`: not run; full-corpus-only. Its `--max-diffs` option caps diagnostics, not record scope.
- `just validate-products`: not applicable without curator-added graph/product-label assertions.
- `just validate-history`: not run; an ignored-inclusive target-history search found no separate artifact. The inline event was inspected without history writes or status promotion.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221553` agrees with identity, rank, parent, genetic code, provenance, and snapshot. Source and YAML have no synonyms. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30905` identifies this taxon with an empty unique-name field.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034285&retmode=xml) confirms identity, parent, rank, code, and non-root ancestor labels/ranks. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034285) agrees and includes root. Complete structured responses were inspected after the browser page was unavailable through the web tool.

All twelve root-first ancestors match the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 3379134 Pseudomonadati, 1783270 FCB group, 68336 Bacteroidota/Chlorobiota group, 976 Bacteroidota, 1853228 Chitinophagia, 1853229 Chitinophagales, 563835 Chitinophagaceae, 504481 Sediminibacterium, and 2635961 unclassified Sediminibacterium. Labels and ranks agree throughout, including both intermediate groups at `CLADE` rank.

## Evidence

`data/taxa/PATHS.tsv:14016` uniquely maps identifier to slug. `curation/seed_scope.tsv:321871` supplies the date and exact one-source reason reproduced in the inline `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. The attestation counts a name, not a strain, genome, or experiment.

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. The backbone has no target children. Exact type-material, merged-ID, and dropped-record scans were negative.

Exact-taxid Nuccore search returned one accession. Complete metadata, references, and features were inspected for [JF753526.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753526.1), a 314-base partial 16S rRNA gene sequence. Organism, strain DJM6, and taxon cross-reference 1034285 agree. Source qualifiers support a bounded Zea seed isolation context. This short marker is not an assembly, authenticated deposit, independent named-species identification, or phenotype observation. Its length limits enrichment but does not invalidate the YAML's supported NCBI identity.

The sequence cites PMID 21673982 and DOI 10.1371/journal.pone.0020396. Cached [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml) were reread and agree with Johnston-Monje and Raizada's 2011 study; this was not a fresh PubMed fetch. Previously inspected [publisher methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) give cultured-isolate interval JF753401-JF753552, which includes this accession. No whole-paper or supplementary-row inspection is claimed for this review.

Community-level findings and results for other isolates are not DJM6-specific evidence. No host genotype, medium, growth promotion, persistence, or transmission assertion is inferred. Taxonomic names do not establish a sediment habitat or chitin-degradation phenotype for this isolate.

## Completeness

Boundary-aware identifier, label/slug, and designation searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only `SOURCE.json` manifests. Hidden, ignored, and compressed files were included. Only the backbone, scientific-name, and scope contexts matched. A secondary whole-accession/PMID/DOI search returned zero matches in that scope. Separate ignored-inclusive exact prior-report filename and history searches were negative. These are bounded source results, not universal absence claims.

The exact-taxid Assembly query returned count zero, no IDs, and phrase-not-found/no-items diagnostics. No eligible culture-deposit or genome join was established.

`strain_count: 0` agrees with the BacDive entry-count semantics in `src/taxonmech/seed.py`. A GenBank strain qualifier does not create a BacDive entry or CAFI-qualified deposit. Optional nomenclature, mapping, strain, genome, and graph slots are appropriately empty. Marker/paper citations are optional for this identity seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Represented identity and provenance are supported. Uninspected supplementary tables S3/S4 limit optional enrichment without invalidating the seed.

## Recommended Edits

None required. Leave generated YAML and `SEEDED` status unchanged. Do not manufacture a collection accession from DJM6 or count its marker as a genome. Optional enrichment requires an exact supported source row and suitable maintained evidence input.

## Follow-up Checks

Inspect the exact DJM6 supplementary row, including headers and units, before adding experimental assertions. After an authorized maintained-input change, rerun focused schema and strict validation, full-corpus reproduction, and applicable repository gates.

## Additional Notes

The prescribed spreadsheet dependency loader was checked during this review and is unavailable; earlier supplement downloads failed. No workbook workaround or unsupported row-level claim was used. iModulonDB is not applicable because this seed contains no gene, regulatory, or transcriptomic assertion.

Only this new report was added for this target. No target YAML, source inventory, earlier report, history event, generated page, or status was changed.

