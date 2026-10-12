# YAML Record Review: Pseudomonas sp. DJM1D9

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_djm1d9.yaml`
- Started UTC: 2026-10-05T06:00:25Z
- Finished UTC: 2026-10-05T06:05:19Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034269`, Pseudomonas sp. DJM1D9. This bacterial isolate placeholder has NCBI `SPECIES` rank, parent `NCBITaxon:196821`, genetic code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. Its sole source attestation counts one NCBITAXON `NAME` from the 2026-09-13 snapshot. Species rank does not establish validly published nomenclature or identification as a named Pseudomonas species.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_djm1d9.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_djm1d9.yaml --out /private/tmp/pseudomonas-djm1d9-strict-20261005.tsv`: exit 0; one file scanned, zero files with errors and zero error rows.
- Structured source comparisons passed identity, full lineage, synonyms, attestation, path-index, scope, and inline seed-event checks.
- `just verify-corpus`: not run; full-corpus-only, without a record selector. Its `--max-diffs` option limits diagnostic output, not scope.
- `just validate-products`: not applicable without curator-added graph or product-label assertions.
- `just validate-history`: not run; an ignored-inclusive target-history search found no separate artifact. The inline event was inspected without history writes or status promotion.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221537` agrees with identifier, label, rank, parent, genetic code, provenance, and snapshot. Source and YAML have no synonyms. The complete native object at `data/catalog/ncbi_names-0005.jsonl.gz:30889` is this taxon's scientific name, with an empty unique-name field.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034269&retmode=xml) confirms identity, parent, rank, code, and non-root ancestor labels/ranks. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034269) agrees and includes root in its ancestor list. The browser page was unavailable through the web tool; complete structured responses were inspected.

All ten root-first ancestors match the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 3379134 Pseudomonadati, 1224 Pseudomonadota, 1236 Gammaproteobacteria, 72274 Pseudomonadales, 135621 Pseudomonadaceae, 286 Pseudomonas, and 196821 unclassified Pseudomonas. Labels and ranks agree throughout.

## Evidence

`data/taxa/PATHS.tsv:13999` uniquely maps the identifier to this slug. `curation/seed_scope.tsv:321855` supplies the date and exact one-source reason reproduced in the inline `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. The attestation counts a name, not a strain, genome, or experiment.

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. The backbone has no target children. Exact type-material, merged-ID, and dropped-record scans were negative.

The exact-taxid Nuccore query returned one accession. Complete metadata, references, and features were inspected for [JF753437.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753437.1), a 657-base partial 16S rRNA gene sequence. Its organism, strain DJM1D9, and taxon cross-reference 1034269 agree. Source qualifiers support a bounded Zea seed isolation context. This marker is not an assembly, authenticated culture deposit, independent named-species identification, or phenotype observation.

The accession explicitly cites PMID 21673982 and DOI 10.1371/journal.pone.0020396. These agree with previously inspected [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml) for Johnston-Monje and Raizada's 2011 study. Previously inspected [publisher methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) give cultured-isolate interval JF753401-JF753552, including this accession. No fresh whole-paper fetch or supplementary-row inspection is claimed.

Community-wide results, genus-level distribution, and findings for other named isolates are not DJM1D9-specific evidence. No host genotype, medium, phenotype, growth promotion, persistence, or transmission claim is inferred.

## Completeness

Boundary-aware identifier, label/slug, and designation searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only `SOURCE.json` manifests. Hidden, ignored, and compressed files were included. Exactly the backbone, native scientific-name, and scope contexts matched. A secondary whole-accession/PMID/DOI search returned zero matches in that scope. Separate ignored-inclusive exact prior-report filename and history searches were negative. These are bounded local-source results, not universal absence claims.

The exact-taxid Assembly query returned count zero, no IDs, and phrase-not-found/no-items diagnostics. No eligible culture-deposit or genome join was established.

`strain_count: 0` agrees with the previously inspected BacDive entry-count semantics in `src/taxonmech/seed.py:483` and the line-543 assignment. A GenBank strain qualifier does not create a BacDive entry or CAFI-qualified collection accession. Optional nomenclature, mapping, strain, genome, and graph slots are appropriately empty. A marker/paper citation is optional for this identity seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Represented identity and provenance are supported. Uninspected supplementary tables S3/S4 limit optional enrichment without invalidating this seed.

## Recommended Edits

None required. Leave generated YAML and `SEEDED` status unchanged. Do not manufacture a collection accession from DJM1D9 or count its partial marker as a genome.

Optional enrichment requires an exact supported source row and an appropriate maintained evidence input. Any later inventory/overlay or seeder change needs focused tests before authorized regeneration.

## Follow-up Checks

Inspect the exact DJM1D9 supplementary row, including headers and units, before adding isolate-level experimental assertions. After an authorized maintained-input change, rerun focused schema and strict validation, then full-corpus reproduction and applicable repository gates.

## Additional Notes

The prescribed spreadsheet dependency loader was checked during this review and is unavailable; earlier supplement downloads failed. No workbook workaround or unsupported row-level claim was used. iModulonDB is not applicable because this seed contains no gene, regulatory, or transcriptomic assertion.

Only this new report was added. No target YAML, source inventory, earlier report, history event, generated page, or review status was changed.

