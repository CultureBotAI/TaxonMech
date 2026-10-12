# YAML Record Review: Paenibacillus sp. DJM1G7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_djm1g7.yaml`
- Started UTC: 2026-10-05T04:05:33Z
- Finished UTC: 2026-10-05T04:07:17Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034227`, Paenibacillus sp. DJM1G7. It is an NCBI `SPECIES`-rank bacterial isolate placeholder, with parent `NCBITaxon:185978`, genetic code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. Its sole source assertion is one NCBITAXON `NAME` from the 2026-09-13 snapshot. Species rank does not assert validly published species nomenclature.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/paenibacillus_sp_djm1g7.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/paenibacillus_sp_djm1g7.yaml --out /private/tmp/paenibacillus-djm1g7-strict-20261005.tsv`: exit 0; one file scanned, zero files with errors and zero error rows.
- Bounded structured source comparisons passed identity, all ancestors, synonyms, attestation, path-index, scope, and inline seed-event checks.
- `just verify-corpus`: not run; it exposes no record selector. `--max-diffs` caps diagnostics, not corpus scope.
- `just validate-products`: not applicable; no curator-added graph nodes or product-label assertions occur.
- `just validate-history`: not run; the ignored-inclusive target-history search found no separate artifact. The inline event was inspected without adding an event or promoting status.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221495` agrees with the exact identifier, label, rank, parent, code, NCBI-only source, and snapshot date. Source and YAML both supply no synonyms. The full native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30847` identifies the same taxon, with an empty unique-name field.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034227&retmode=xml) confirms exact label, rank, parent, genetic code, and non-root ancestor labels/ranks. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034227) independently agrees and includes root in its ancestor list. The browser page was inaccessible through the web tool; the complete structured responses were inspected instead.

All ten root-first ancestors match the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 1783272 Bacillati, 1239 Bacillota, 91061 Bacilli, 1385 Caryophanales, 186822 Paenibacillaceae, 44249 Paenibacillus, and 185978 unclassified Paenibacillus. Labels and ranks agree throughout. No inferred or reconciled placement replaces the NCBI chain.

## Evidence

`data/taxa/PATHS.tsv:13957` uniquely maps the taxon to the correct slug. `curation/seed_scope.tsv:321813` supplies the scope date and exact one-source reason in the inline `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. The source assertion counts one name, not a genome or experimental observation.

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. The backbone has no target children. Exact type-material, merged-ID, and dropped-record scans were negative.

The exact-taxid Nuccore query returned one accession. Its complete metadata, references, and features were inspected: [JF753468.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753468.1), a 663-base partial 16S rRNA gene sequence. The organism, strain DJM1G7, and taxon cross-reference 1034227 agree. Source qualifiers describe Zea seed isolation. This supports marker identity and a bounded isolation context, not an assembly, authenticated collection deposit, or phenotype.

The marker explicitly cites PMID 21673982 and DOI 10.1371/journal.pone.0020396. These agree with previously fetched and inspected [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml) for Johnston-Monje and Raizada's 2011 study. Previously inspected [publisher methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) give culture-derived interval JF753401-JF753552, which contains this accession. No new whole-paper fetch or supplementary-row inspection is claimed here.

Predicted genus-level Paenibacillus signals, community-wide results, and observations about other isolates are not DJM1G7-specific evidence. No host genotype, medium, phenotype, growth promotion, persistence, or transmission claim is inferred.

## Completeness

Boundary-aware identifier, label/slug, and designation searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only `SOURCE.json` manifests. Hidden, ignored, and compressed files were included. Exactly three contexts matched: backbone, native scientific name, and scope. A secondary whole-accession/PMID/DOI search returned zero matches in that same scope. Separate ignored-inclusive exact prior-report filename and history searches were negative. These are bounded local-source results, not universal absence claims.

The live exact-taxid Assembly query returned count zero, no IDs, and phrase-not-found/no-items diagnostics. This is a bounded current query result, not proof of universal genome absence. No eligible culture-deposit or genome join was established.

`strain_count: 0` follows BacDive entry-count semantics in `src/taxonmech/seed.py:483` and the line-543 count assignment. A GenBank strain qualifier and culture-derived marker do not create a BacDive entry or CAFI-qualified culture accession. Empty optional nomenclature, mapping, strain, genome, and graph slots are appropriate. The optional marker/paper citation is not required for this identity seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Seeded identity and provenance are supported at their represented scope. Supplementary tables S3/S4 remain uninspected, limiting optional enrichment without invalidating this record.

## Recommended Edits

None required. Leave generated YAML and `SEEDED` status unchanged. Do not create a collection accession from DJM1G7 or count its partial 16S marker as a genome.

Optional enrichment must first resolve an exact supported source row and a suitable maintained evidence input. Any needed inventory/overlay or `src/taxonmech/seed.py` change requires tests before authorized regeneration.

## Follow-up Checks

Inspect the exact DJM1G7 supplementary row with headers and units before adding isolate-level experimental assertions. After a later authorized maintained-input change, rerun focused schema and strict validation, then full-corpus reproduction and applicable repository gates.

## Additional Notes

The prescribed spreadsheet dependency loader was checked this turn and is unavailable; earlier supplement downloads failed. No workbook workaround or unsupported row-level claim was used. iModulonDB is not applicable because this taxonomic identity seed contains no gene, regulatory, or transcriptomic assertion.

Only this new report was added. No target YAML, source inventory, existing report, history event, generated page, or review status was changed.

