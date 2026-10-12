# YAML Record Review: Sphingomonas sp. DJM1C12

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/sphingomonas_sp_djm1c12.yaml`
- Started UTC: 2026-10-05T07:46:58Z
- Finished UTC: 2026-10-05T07:48:56Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034307`, Sphingomonas sp. DJM1C12: `SPECIES` rank, `BACTERIA` domain, parent `NCBITaxon:196159`, code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. Its sole attestation is one NCBITAXON `NAME` from snapshot 2026-09-13. This isolate placeholder's species rank is not a nomenclatural-publication claim.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py` through `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/sphingomonas_sp_djm1c12.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/sphingomonas_sp_djm1c12.yaml --out /private/tmp/sphingomonas-djm1c12-strict-20261005.tsv`: exit 0; one file, zero error files or rows.
- Structured comparisons passed identity, complete lineage, source attestation, path-index, scope, and inline-event checks.
- `just verify-corpus`: not run; full-corpus-only. Its inspected `--max-diffs` option caps diagnostics, not record scope.
- `just validate-products`: not applicable without curator-added graph/product-label assertions.
- `just validate-history`: not run; ignored-inclusive searches found no separate target artifact. Inline provenance was inspected without history writes.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221575` agrees with identity, rank, parent, code, and snapshot. Source synonym fields and YAML synonyms are empty. The full scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30924` agrees and has empty unique-name text.

The browser page was inaccessible through the web tool. Complete live [Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034307&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034307) responses were inspected instead. Identity, rank, and lineage agree; EFetch also confirms parent, code, and ancestor ranks.

All ten root-first ancestors match the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 3379134 Pseudomonadati, 1224 Pseudomonadota, 28211 Alphaproteobacteria, 204457 Sphingomonadales, 41297 Sphingomonadaceae, 13687 Sphingomonas, and 196159 unclassified Sphingomonas. No named-species or neighboring DJM-isolate equivalence is inferred.

## Evidence

`data/taxa/PATHS.tsv:14039` uniquely maps identifier to slug. `curation/seed_scope.tsv:321890` supplies the exact reason reproduced in the inline `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. Source count and `NAME` unit agree.

Full scans found no target rows in mapped BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits inventories, and no target children in the backbone. Exact type-material, merged-ID, and dropped-record scans were negative.

Exact-taxid Nuccore search returned one sequence: [JF753431.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753431.1), a 656-base partial 16S rRNA marker. Its complete metadata, references, and features, excluding raw bases, name strain DJM1C12 and taxon 1034307. Host and isolation qualifiers support a bounded Zea seed context, not a genome, culture deposit, or measured phenotype.

The accession cites Johnston-Monje and Raizada (2011), [PMID 21673982](https://pubmed.ncbi.nlm.nih.gov/21673982/), [DOI 10.1371/journal.pone.0020396](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396). The complete PubMed metadata and abstract were inspected in the preceding review turn; no fresh PubMed fetch is claimed here. Earlier publisher inspection covered citation, abstract, relevant methods, and supplement descriptions, not the complete article or exact supplementary rows. The accession falls in the cultured-isolate series. Other isolates' experiments and community findings are not DJM1C12 phenotypes.

Exact-taxid Assembly search returned zero IDs with phrase-not-found and no-items diagnostics. This is a bounded query result, not global assembly absence.

## Completeness

The represented identity seed is supported. Optional nomenclature, mappings, strain/deposit, genome, and phenotype assertions are not justified by inspected target-specific evidence. Seeder logic counts deduplicated BacDive entries, not GenBank strain qualifiers, so `strain_count: 0` is consistent.

Ignored-inclusive searches included hidden files and compressed contents in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding generic `SOURCE.json` descriptors. Whole identifier, label, and designation matching returned only backbone, native-name, and scope contexts. A separate whole-accession/PMID/DOI search returned none. Target report/history filename and history-content searches were negative before this report. These findings are bounded to those surfaces.

Not checked: exact S3/S4 workbook rows. Earlier downloads failed; current tool discovery again found no prescribed spreadsheet workspace loader. No host genotype, medium, functional trait, transmission, or growth-promotion outcome is inferred. iModulonDB is not applicable without a relevant gene, regulator, or expression-module claim.

## Findings

None found.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

No required edits. Do not patch generated YAML, promote status, or turn the 16S marker into a genome link. Optional future identity/link enrichment requires exact-row evidence and an authorized maintained input or reviewed ingestion/schema change. Trait and isolation-source modeling belongs to the appropriate sibling repository.

## Follow-up Checks

Inspect exact accession/designation rows, headers, units, and experimental conditions before functional enrichment. Require eligible whole collection identifiers and explicit source chains before any strain-genome association. After a future authorized upstream change, regenerate with the validated writer, rerun focused schema/strict validation, and run full corpus reproduction.

## Additional Notes

All invoked target checks terminated successfully; negative searches returned the expected no-match status. The schema guide was reread. Full source comparisons are bounded evidence checks, not a claim of corpus regeneration. No record, source, generated page, earlier report, history, or status was modified. Only this new report is added.

