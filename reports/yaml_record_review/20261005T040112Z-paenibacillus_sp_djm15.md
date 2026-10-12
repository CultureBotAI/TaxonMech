# YAML Record Review: Paenibacillus sp. DJM15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_djm15.yaml`
- Started UTC: 2026-10-05T03:59:14Z
- Finished UTC: 2026-10-05T04:01:12Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1034225`, Paenibacillus sp. DJM15. It is an NCBI `SPECIES`-rank bacterial isolate placeholder with parent `NCBITaxon:185978`, genetic code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. One NCBITAXON `NAME` assertion cites the 2026-09-13 snapshot. The rank does not assert validly published species nomenclature.

The maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/paenibacillus_sp_djm15.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/paenibacillus_sp_djm15.yaml --out /private/tmp/paenibacillus-djm15-strict-20261005.tsv`: exit 0; one file scanned, zero files with errors and zero error rows.
- Bounded structured source checks passed identity, full ancestry, synonyms, attestation, path-index, scope, and inline seed-event comparisons.
- `just verify-corpus`: not run; the documented command has no record selector. `--max-diffs` caps diagnostics, not corpus scope.
- `just validate-products`: not applicable; the record has no curator-added graph nodes or product-label assertions.
- `just validate-history`: not run because the ignored-inclusive target-history search returned no separate artifact. The inline event was inspected, without adding history or promoting status.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221493` agrees with the exact identifier, label, rank, parent, code, NCBI-only source, and snapshot. Source and record both supply no synonyms. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30845` identifies this same taxon and has an empty unique-name field.

The first live taxonomy request failed with HTTP 500 and exited. A paced retry succeeded, and the full [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034225&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034225) responses were inspected before the verdict. They agree with identity, rank, and lineage; EFetch additionally confirms parent 185978 and genetic code 11. The browser page was inaccessible through the web tool, so structured responses supplied the authority check.

The ten-entry root-first chain matches the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 1783272 Bacillati, 1239 Bacillota, 91061 Bacilli, 1385 Caryophanales, 186822 Paenibacillaceae, 44249 Paenibacillus, and 185978 unclassified Paenibacillus. Every ancestor label and rank agrees. Datasets includes root; EFetch supplies the remaining ancestor labels/ranks. No placement is inferred.

## Evidence

`data/taxa/PATHS.tsv:13955` uniquely maps this identifier to the correct slug. `curation/seed_scope.tsv:321811` has the 2026-09-13 date and exact one-source reason used by the inline `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. The single assertion counts a name, not a genome or phenotype.

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. The backbone contains no target children. Exact type-material, merged-ID, and dropped-record scans were negative.

The exact-taxid Nuccore query returned one accession. Its full metadata, references, and features were inspected: [JF753535.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753535.1), a 633-base partial 16S rRNA gene sequence. Organism, strain DJM15, and taxon cross-reference 1034225 agree. Source qualifiers describe Zea seed isolation. This is marker identity and bounded isolation evidence, not a genome, authenticated culture deposit, or demonstrated phenotype.

The accession explicitly cites PMID 21673982 and DOI 10.1371/journal.pone.0020396. This agrees with previously fetched and inspected [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml) for Johnston-Monje and Raizada's 2011 paper. Previously inspected [publisher methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) give the culture-derived interval JF753401-JF753552, which contains this marker. No fresh whole-paper fetch or supplementary-row inspection is claimed.

Predicted genus-level signals, community-wide results, and observations for other isolates are not DJM15-specific evidence. No phenotype, host genotype, medium, growth-promotion, persistence, or transmission claim is inferred.

## Completeness

Boundary-aware searches for the identifier, label/slug, and designation used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only `SOURCE.json` manifests. Hidden, ignored, and compressed files were included. Exactly the backbone, native scientific name, and scope contexts matched. A secondary whole-accession/PMID/DOI search returned zero matches in the same scope. Separate ignored-inclusive exact prior-report filename and history searches were negative. These are bounded local-source findings, not universal absence claims.

The exact-taxid Assembly query returned count zero, no IDs, and phrase-not-found/no-items diagnostics. It establishes only a bounded current result. No eligible collection-deposit or genome join was established.

`strain_count: 0` correctly reflects BacDive entry-count semantics in `src/taxonmech/seed.py:483` and the count assignment at line 543. A GenBank strain qualifier and culture-derived marker are not a BacDive entry or CAFI-qualified collection accession. Empty optional nomenclature, mapping, strain, genome, and graph slots are appropriate. The optional marker/paper citation is not required for this identity seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The seeded claims are supported at their represented scope. The recovered external API failure is not a record defect. Uninspected supplementary tables S3/S4 limit optional enrichment but do not invalidate the identity record.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Do not create a collection accession from DJM15 or count the 16S marker as a genome.

Optional enrichment must first resolve an exact supported source row and a suitable maintained evidence input. Any needed inventory/overlay or `src/taxonmech/seed.py` change requires tests before authorized regeneration.

## Follow-up Checks

Inspect the exact DJM15 supplementary row with its headers and units before adding experimental assertions. For a later authorized maintained-input change, rerun focused schema and strict validation, then full-corpus reproduction and applicable repository gates.

## Additional Notes

The prescribed spreadsheet dependency loader was checked this turn and is unavailable; earlier supplement downloads failed. No workbook workaround or unsupported row-level claim was used. iModulonDB is not applicable to this taxonomy-only record, which makes no gene, regulatory, or transcriptomic assertion.

Only this new report was added. No YAML, source inventory, existing report, history event, generated page, or review status was edited.

