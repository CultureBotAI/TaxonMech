# YAML Record Review: Escherichia sp. DJM1A8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/escherichia_sp_djm1a8.yaml`
- Started UTC: 2026-10-05T07:43:32Z
- Finished UTC: 2026-10-05T07:45:01Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034306`, Escherichia sp. DJM1A8. It carries `SPECIES` rank, `BACTERIA` domain, parent `NCBITaxon:2608889`, code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. Its sole attestation counts one NCBITAXON `NAME` at snapshot 2026-09-13. This placeholder's NCBI rank does not establish nomenclatural publication or identity as E. coli.

Maintained ownership is `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py` through `scripts/seed_from_sources.py`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/escherichia_sp_djm1a8.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/escherichia_sp_djm1a8.yaml --out /private/tmp/escherichia-djm1a8-strict-20261005.tsv`: exit 0; one file scanned, zero error files or rows.
- Structured comparisons passed identity, complete lineage, synonyms, source attestation, path-index, scope, and inline-event checks.
- `just verify-corpus`: not run; full-corpus-only. The inspected `--max-diffs` option limits diagnostics, not record scope.
- `just validate-products`: not applicable without curator-added graph/product-label assertions.
- `just validate-history`: not run; ignored-inclusive target searches found no separate artifact. Inline history was inspected without adding an event.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221574` agrees with every identity field and has empty synonym fields. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30923` agrees, including empty unique-name text.

After the browser page was inaccessible through the web tool, complete live [Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034306&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034306) responses were inspected. Identity, rank, and lineage agree; EFetch confirms parent, code, and ancestor ranks.

The ten root-first ancestors match the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 3379134 Pseudomonadati, 1224 Pseudomonadota, 1236 Gammaproteobacteria, 91347 Enterobacterales, 543 Enterobacteriaceae, 561 Escherichia, and 2608889 unclassified Escherichia. No synonym, neighboring DJM identity, or E. coli equivalence is inferred.

## Evidence

`data/taxa/PATHS.tsv:14038` uniquely maps identifier to slug. `curation/seed_scope.tsv:321889` supplies the exact reason carried by the inline `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. The attestation's count and `NAME` unit agree with its source.

Full scans found no target rows in the mapped BacDive, LPSN, GTDB, GOLD-organism, MediaDive, Madin, or BactoTraits inventories. The backbone has no target children. Exact type-material, merged-ID, and dropped-record scans were negative.

Exact-taxid Nuccore search returned one sequence: [JF753407.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753407.1), a 450-base partial 16S rRNA marker. Complete metadata, references, and features, excluding raw bases, name strain DJM1A8 and taxon 1034306. Host and isolation qualifiers support a bounded Zea seed context. Neither the marker length nor these qualifiers establish a species reassignment, culture deposit, genome, pathogenicity, or plant-beneficial phenotype.

The sequence cites Johnston-Monje and Raizada (2011), [PMID 21673982](https://pubmed.ncbi.nlm.nih.gov/21673982/), [DOI 10.1371/journal.pone.0020396](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396). Previously fetched PubMed metadata and abstract were fully reread earlier in this review turn, not freshly fetched for DJM1A8. Earlier publisher inspection covered citation, abstract, relevant methods, and supplement descriptions, not every article or supplement row. This accession lies in the cultured-isolate series. Community results and experiments on other named isolates do not establish DJM1A8-specific functions.

Exact-taxid Assembly search returned zero IDs and phrase-not-found/no-items diagnostics. It does not prove global assembly absence.

## Completeness

The identity seed is supported at its represented scope. Empty optional nomenclature, mappings, strain/deposit, genome, and phenotype surfaces are not material omissions on the inspected evidence. Seeder logic counts deduplicated BacDive entries; a GenBank strain qualifier is not an inventory entry, so `strain_count: 0` is consistent.

Ignored-inclusive searches included hidden files and compressed contents in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding generic `SOURCE.json` descriptors. Whole identifier, label, and designation searches returned only backbone, native-name, and scope contexts. A separate whole-accession/PMID/DOI search returned none. Target report/history filename and history-content searches were also negative before this report. These are local bounded findings, not universal biological absences.

Not checked: exact S3/S4 workbook rows. Earlier downloads failed and the prescribed spreadsheet workspace loader is unavailable. No exact host genotype, medium, persistence, resistance, or growth-promotion result is asserted. iModulonDB is not applicable to this identity-only seed without relevant expression-module, gene, or regulator claims.

## Findings

None found.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

No required edits. Do not patch generated YAML, promote review status, convert the marker into a genome association, or assign a named species from genus membership. Optional enrichment requires inspected exact-row evidence and an authorized maintained input or reviewed ingestion/schema change. Phenotype and isolation-source modeling belongs to the appropriate sibling repository.

## Follow-up Checks

Resolve exact supplementary accession/designation rows, headers, units, and conditions before functional enrichment. Require eligible whole culture-deposit identities and explicit source chains before genome linking. After a future authorized upstream change, regenerate through the validated writer, rerun focused schema/strict validation, and run full corpus reproduction.

## Additional Notes

All invoked target checks terminated successfully. Negative searches use the expected no-match exit status. Curation and harmonization documentation were reread. Full lineage and source comparisons are bounded checks, not a claim of whole-corpus regeneration. No record, source, generated page, earlier report, history, or status was modified; this new report is the only repository write for this review.

