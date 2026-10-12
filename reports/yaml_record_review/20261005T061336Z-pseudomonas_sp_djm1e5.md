# YAML Record Review: Pseudomonas sp. DJM1E5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudomonas_sp_djm1e5.yaml`
- Started UTC: 2026-10-05T06:12:08Z
- Finished UTC: 2026-10-05T06:13:36Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034272`, Pseudomonas sp. DJM1E5. This bacterial isolate placeholder carries NCBI `SPECIES` rank, parent `NCBITaxon:196821`, genetic code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. The sole attestation counts one NCBITAXON `NAME` from the 2026-09-13 snapshot. Species rank does not establish validly published nomenclature or identification as a named Pseudomonas species.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/pseudomonas_sp_djm1e5.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/pseudomonas_sp_djm1e5.yaml --out /private/tmp/pseudomonas-djm1e5-strict-20261005.tsv`: exit 0; one file scanned, zero error files or rows.
- Structured comparisons passed identity, full lineage, synonyms, attestation, path-index, scope, and inline-event checks.
- `just verify-corpus`: not run; full-corpus-only. Its inspected `--max-diffs` option caps diagnostic output, not record scope.
- `just validate-products`: not applicable without curator-added graph/product-label assertions.
- `just validate-history`: not run; an ignored-inclusive target-history search found no separate artifact. The inline event was inspected without history writes or status promotion.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221540` agrees with identity, rank, parent, genetic code, provenance, and snapshot. Source and YAML have no synonyms. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30892` identifies this taxon with an empty unique-name field.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034272&retmode=xml) confirms identity, parent, rank, code, and non-root ancestor labels/ranks. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034272) agrees and includes root. Complete structured responses were inspected after the browser page was unavailable through the web tool.

All ten root-first ancestors match the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 3379134 Pseudomonadati, 1224 Pseudomonadota, 1236 Gammaproteobacteria, 72274 Pseudomonadales, 135621 Pseudomonadaceae, 286 Pseudomonas, and 196821 unclassified Pseudomonas. Labels and ranks agree throughout; no inferred placement replaces this chain.

## Evidence

`data/taxa/PATHS.tsv:14002` uniquely maps identifier to slug. `curation/seed_scope.tsv:321858` supplies the date and exact one-source reason reproduced in the inline `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. The attestation counts a name, not a strain, genome, or experiment.

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. The backbone has no target children. Exact type-material, merged-ID, and dropped-record scans were negative.

Exact-taxid Nuccore search returned one accession. Complete metadata, references, and features were inspected for [JF753444.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753444.1), a 657-base partial 16S rRNA gene sequence. Organism, strain DJM1E5, and taxon cross-reference 1034272 agree. Source qualifiers support a bounded Zea seed isolation context. This marker is not an assembly, authenticated culture deposit, independent named-species identification, or phenotype observation.

The sequence cites PMID 21673982 and DOI 10.1371/journal.pone.0020396, agreeing with previously fetched [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml), reread this turn, for Johnston-Monje and Raizada's 2011 study. Previously inspected [publisher methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) give cultured-isolate interval JF753401-JF753552, including this accession. No fresh whole-paper fetch or supplementary-row inspection is claimed.

Community-wide observations, Pseudomonas distribution, and findings for other isolates are not DJM1E5-specific evidence. No host genotype, medium, phenotype, growth promotion, persistence, or transmission claim is inferred.

## Completeness

Boundary-aware identifier, label/slug, and designation searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only `SOURCE.json` manifests. Hidden, ignored, and compressed files were included. Only the backbone, scientific-name, and scope contexts matched. A secondary whole-accession/PMID/DOI search returned zero matches in that scope. Separate ignored-inclusive exact prior-report filename and history searches were negative. These are bounded source results, not universal absence claims.

The exact-taxid Assembly query returned count zero, no IDs, and phrase-not-found/no-items diagnostics. No eligible culture-deposit or genome join was established.

`strain_count: 0` agrees with BacDive entry-count semantics inspected this turn at `src/taxonmech/seed.py:483` through the line-543 assignment. A GenBank strain qualifier does not create a BacDive entry or CAFI-qualified collection accession. Optional nomenclature, mapping, strain, genome, and graph slots are appropriately empty. Marker/paper citations are optional for this identity seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Represented identity and provenance are supported. Uninspected supplementary tables S3/S4 limit optional enrichment without invalidating the seed.

## Recommended Edits

None required. Leave generated YAML and `SEEDED` status unchanged. Do not manufacture a collection accession from DJM1E5 or count its marker as a genome. Optional enrichment requires an exact supported source row and suitable maintained evidence input.

## Follow-up Checks

Inspect the exact DJM1E5 supplementary row, including headers and units, before adding isolate-level experimental assertions. After an authorized maintained-input change, rerun focused schema and strict validation, full-corpus reproduction, and applicable repository gates.

## Additional Notes

The prescribed spreadsheet dependency loader was checked this turn and is unavailable; earlier supplement downloads failed. No workbook workaround or unsupported row-level claim was used. iModulonDB is not applicable because this seed contains no gene, regulatory, or transcriptomic assertion.

Only this new report was added for this target. No target YAML, source inventory, earlier report, history event, generated page, or status was changed.

