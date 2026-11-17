# YAML Record Review: Azospirillum sp. DJM2D4

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/azospirillum_sp_djm2d4.yaml`
- Started UTC: 2026-10-05T07:40:34Z
- Finished UTC: 2026-10-05T07:42:34Z
- Verdict: pass

## Target

Read all 54 lines of this generated `TaxonRecord`: `NCBITaxon:1034305`, Azospirillum sp. DJM2D4, `SPECIES` rank, `BACTERIA` domain, parent `NCBITaxon:2630922`, code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. Its single NCBITAXON attestation counts one `NAME` in snapshot 2026-09-13. NCBI species rank for an isolate placeholder is not a claim of valid nomenclatural publication.

Future identity/provenance fixes belong in `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, or `src/taxonmech/seed.py` through `scripts/seed_from_sources.py`, not generated YAML.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/azospirillum_sp_djm2d4.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/azospirillum_sp_djm2d4.yaml --out /private/tmp/azospirillum-djm2d4-strict-20261005.tsv`: exit 0; one file, zero error files or rows.
- Full structured source comparisons passed identity, lineage, attestation, scope, path-index, and inline-event checks.
- `just verify-corpus`: not run; full-corpus-only. Its inspected CLI offers no record selector; `--max-diffs` only caps diagnostics.
- `just validate-products`: not applicable without curator-added graph/product assertions.
- `just validate-history`: not run; ignored-inclusive target searches found no separate history artifact. Inline provenance was inspected; no history write is authorized by this review.

## Identity and Grounding

The exact backbone row at `data/raw/ncbitaxon_taxa.tsv:221573` agrees with every identity field and contains no synonyms. The complete scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30922` confirms the name and identifier, with empty unique-name text.

The browser page was inaccessible through the web tool. Complete live [Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034305&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034305) responses were inspected instead. They confirm identity, rank, and lineage; EFetch confirms parent, code, and ancestor ranks.

All ten root-first ancestors match the pinned source: 1 root, 131567 cellular organisms, 2 Bacteria, 3379134 Pseudomonadati, 1224 Pseudomonadota, 28211 Alphaproteobacteria, 204441 Rhodospirillales, 2829815 Azospirillaceae, 191 Azospirillum, and 2630922 unclassified Azospirillum. No adjacent isolate or named-species equivalence is inferred.

## Evidence

`data/taxa/PATHS.tsv:14037` supplies the unique slug; `curation/seed_scope.tsv:321888` supplies the exact reason reproduced in the inline `SEEDED_FROM_SOURCES` event dated 2026-09-13T17:54:04Z. The one-source attestation matches the inventory count and unit.

Full scans found no exact mapped rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. There are no target children in the backbone and no exact type-material, merged-ID, or dropped rows.

Exact-taxid Nuccore search found one sequence, [JF753513.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753513.1). Its complete metadata, references, and features were inspected, excluding raw bases. The 659-base partial 16S rRNA marker names strain DJM2D4 and taxon 1034305, with Zea host and surface-sterilized seed isolation qualifiers. It is not a genome assembly, authenticated deposit, or functional assay.

The accession cites Johnston-Monje and Raizada (2011), [PMID 21673982](https://pubmed.ncbi.nlm.nih.gov/21673982/) and [DOI 10.1371/journal.pone.0020396](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396). Previously fetched PubMed metadata and abstract were fully reread earlier in this same review turn, not freshly fetched for DJM2D4. Earlier publisher inspection covered citation, abstract, relevant methods, and supplement descriptions. The accession belongs to the cultured-isolate series. Neither community-wide observations nor another isolate's experiments support DJM2D4-specific nitrogen fixation, growth promotion, or other phenotypes.

Exact-taxid Assembly search returned zero IDs with phrase-not-found/no-items diagnostics. This is a bounded query result, not global absence evidence.

## Completeness

The represented identity claims are supported. Optional nomenclature, mappings, strain/deposit entries, genome links, and phenotypes are correctly unasserted on the inspected evidence. Seeder logic counts BacDive entries, not sequence strain qualifiers; `strain_count: 0` is consistent.

Hidden and ignored files and compressed catalogs were included in searches over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding generic `SOURCE.json` descriptors. Whole identity/name/designation matching returned only the backbone, native scientific name, and scope contexts. A separate whole-accession/PMID/DOI search returned none. Target report/history filename and history-content searches found no earlier target artifact. These conclusions are bounded to the searched local surfaces.

Not checked: exact S3/S4 workbook rows, because prior downloads failed and the prescribed spreadsheet workspace loader is unavailable. Host genotype, medium, transmission, and isolate-level functional outcomes remain unasserted. iModulonDB is not applicable without a relevant expression, gene, or regulator claim.

## Findings

None found.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

No required edits. Do not patch the generated record, infer nitrogen fixation from its genus, convert the marker to a genome link, or promote status. Optional future enrichment requires an exact supplementary-row match and an authorized maintained input or reviewed ingestion/schema change.

## Follow-up Checks

For enrichment, inspect exact accession/designation rows with their headers, units, and experimental conditions. Require eligible whole deposit identifiers and explicit source chains before genome linking. After a future authorized upstream change, regenerate with the validated writer, rerun focused schema/strict validation, and run full corpus reproduction.

## Additional Notes

All invoked target checks terminated successfully; negative searches returned the expected no-match status. The entire YAML and complete matched native object were read. The history README was reread, with the review skill's no-history-write rule controlling this task. No sources, records, generated pages, earlier reports, histories, or statuses changed; only this new report is added.

