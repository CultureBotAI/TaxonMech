# YAML Record Review: Paenibacillus sp. DJM1G10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_djm1g10.yaml`
- Started UTC: 2026-10-05T04:02:02Z
- Finished UTC: 2026-10-05T04:03:43Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1034226`, Paenibacillus sp. DJM1G10. This NCBI `SPECIES`-rank bacterial isolate placeholder has parent `NCBITaxon:185978`, genetic code 11, `EXACT` grounding, `SEEDED` status, zero inventoried strains, and one NCBITAXON `NAME` assertion from the 2026-09-13 snapshot. The rank does not assert validly published species nomenclature.

The maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/paenibacillus_sp_djm1g10.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/paenibacillus_sp_djm1g10.yaml --out /private/tmp/paenibacillus-djm1g10-strict-20261005.tsv`: exit 0; one file scanned, zero files with errors and zero error rows.
- Bounded structured source comparisons passed identity, full ancestry, synonyms, attestation, path-index, scope, and inline seed-event checks.
- `just verify-corpus`: not run; it has no record selector. `--max-diffs` caps diagnostics rather than corpus scope.
- `just validate-products`: not applicable because no curator-added graph nodes or product labels occur.
- `just validate-history`: not run; an ignored-inclusive target-history search found no separate artifact. The inline event was inspected, without adding history or promoting status.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221494` agrees with all seeded identity fields, NCBI-only attestation, and snapshot date. Neither source nor YAML supplies synonyms. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30846` matches the exact taxon and has an empty unique-name field.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034226&retmode=xml) confirms exact label, species rank, parent, genetic code, and non-root ancestor labels/ranks. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034226) independently agrees and includes root in its ancestor list. The browser page was inaccessible through the web tool; the full structured responses were inspected.

All ten root-first ancestors match the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 1783272 Bacillati, 1239 Bacillota, 91061 Bacilli, 1385 Caryophanales, 186822 Paenibacillaceae, 44249 Paenibacillus, and 185978 unclassified Paenibacillus. Every label and rank agrees. No inferred or reconciled taxonomy replaces the NCBI chain.

## Evidence

`data/taxa/PATHS.tsv:13956` uniquely maps the taxon to the correct slug. `curation/seed_scope.tsv:321812` supplies the scope date and exact one-source reason carried by the inline `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. The attestation counts one name, not an experimental observation or genome.

Full mapped-inventory scans found no target rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. The backbone has no target children. Exact type-material, merged-ID, and dropped-record scans were negative.

The exact-taxid Nuccore search returned one accession. Its complete metadata, references, and features were inspected: [JF753471.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753471.1), a 387-base partial 16S rRNA gene sequence. Organism, strain DJM1G10, and taxon cross-reference 1034226 agree. Source qualifiers describe Zea seed isolation. This establishes marker identity and bounded isolation context, not a genome, authenticated culture deposit, independent species assignment, or demonstrated phenotype.

The marker explicitly cites PMID 21673982 and DOI 10.1371/journal.pone.0020396. These agree with previously fetched and inspected [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml) for Johnston-Monje and Raizada's 2011 study. Previously inspected [publisher methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) give culture-derived interval JF753401-JF753552, which contains this accession. No fresh whole-paper fetch or supplementary-row inspection is claimed here.

Predicted genus-level Paenibacillus signals, community-wide results, and observations for other named isolates are not DJM1G10-specific evidence. No host genotype, medium, phenotype, growth promotion, persistence, or transmission claim is inferred.

## Completeness

Boundary-aware identifier, label/slug, and designation searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only `SOURCE.json` manifests. Ignored, hidden, and compressed files were included. Exactly three contexts matched: backbone, native scientific name, and scope. A secondary whole-accession/PMID/DOI search returned zero matches in that same scope. Separate ignored-inclusive exact prior-report filename and history searches were negative. These are bounded local-source findings, not universal absence claims.

The exact-taxid Assembly query returned count zero, no IDs, and phrase-not-found/no-items diagnostics. This establishes only a bounded current query result. No eligible culture-deposit or genome join was established.

`strain_count: 0` follows the BacDive entry-count semantics in `src/taxonmech/seed.py:483` and the count assignment at line 543. GenBank's strain qualifier and a culture-derived marker do not create a BacDive entry or CAFI-qualified culture accession. Optional nomenclature, mapping, strain, genome, and graph fields are appropriately empty. The optional marker/paper citation is not required for this identity seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The seeded identity and provenance are supported at their represented scope. Supplementary tables S3/S4 remain uninspected; that limits optional enrichment but does not invalidate this record.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not turn DJM1G10 into a culture-collection accession or its short 16S marker into a genome.

Optional enrichment must first resolve the exact supported source row and a suitable maintained evidence input. Any needed inventory/overlay or `src/taxonmech/seed.py` change requires focused tests before authorized regeneration.

## Follow-up Checks

Inspect the exact DJM1G10 supplementary row with headers and units before adding isolate-level experimental assertions. After a later authorized maintained-input change, rerun focused schema and strict validation, then full-corpus reproduction and applicable repository gates.

## Additional Notes

The prescribed spreadsheet dependency loader was checked this turn and is unavailable; earlier supplement downloads failed. No workbook workaround or unsupported row-level claim was used. iModulonDB is not applicable because the record contains no gene, regulatory, or transcriptomic assertion.

Only this new report was added. No target YAML, source inventory, existing report, history event, generated page, or review status was changed.

