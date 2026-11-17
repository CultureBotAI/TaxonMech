# YAML Record Review: Streptomyces sp. DJM2B2

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptomyces_sp_djm2b2.yaml`
- Started UTC: 2026-10-05T07:37:44Z
- Finished UTC: 2026-10-05T07:39:42Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1034301`, Streptomyces sp. DJM2B2. It has `SPECIES` rank, `BACTERIA` domain, parent `NCBITaxon:2593676`, genetic code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. Its sole source attestation is one NCBITAXON `NAME` from snapshot 2026-09-13. NCBI species rank for this isolate placeholder does not establish a validly published species name.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/streptomyces_sp_djm2b2.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/streptomyces_sp_djm2b2.yaml --out /private/tmp/streptomyces-djm2b2-strict-20261005.tsv`: exit 0; one file, zero error files and rows.
- Structured source comparisons passed identity, complete lineage, synonyms, attestation, path-index, scope, and inline-event checks.
- `just verify-corpus`: not run; full-corpus-only. Rereading its CLI confirmed that `--max-diffs` limits diagnostics, not scope.
- `just validate-products`: not applicable without curator-added graph/product-label assertions.
- `just validate-history`: not run; ignored-inclusive target-history searches found no separate artifact. Inline provenance was inspected.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221569` supports the identifier, label, rank, parent, code, and snapshot. Source synonym fields and YAML synonyms are empty. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30921` agrees and has an empty unique-name field.

Complete live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034301&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034301) responses were inspected after the browser page was inaccessible through the web tool. They agree on identity, species rank, and lineage; EFetch also confirms the parent, ancestor ranks, and code.

All ten root-first ancestors match the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 1783272 Bacillati, 201174 Actinomycetota, 1760 Actinomycetes, 85011 Kitasatosporales, 2062 Streptomycetaceae, 1883 Streptomyces, and 2593676 unclassified Streptomyces. Labels and ranks agree throughout. Neither the genus nor the Datasets blast-group label is treated as measured isolate physiology.

## Evidence

`data/taxa/PATHS.tsv:14033` uniquely maps the identifier to this slug. `curation/seed_scope.tsv:321887` supplies the exact one-source reason reproduced by the `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. The attestation counts a name, not an experiment, strain inventory entry, or genome.

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. The backbone has no target children. Exact type-material, merged-ID, and dropped-record scans were negative.

Exact-taxid Nuccore search returned one sequence. Complete metadata, references, and features for [JF753494.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753494.1), excluding raw bases, identify a 660-base partial 16S rRNA gene, strain DJM2B2, and taxon cross-reference 1034301. Source qualifiers support isolation from surface-sterilized Zea seed. This marker is not a genome assembly, culture-collection accession, or independent named-species determination.

Its citation identifies Johnston-Monje and Raizada (2011), [PMID 21673982](https://pubmed.ncbi.nlm.nih.gov/21673982/), [DOI 10.1371/journal.pone.0020396](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396). The previously fetched PubMed metadata and abstract were reread during this review; this was not a fresh PubMed request. Prior publisher inspection covered citation, abstract, relevant methods, and supplement descriptions, not every article or supplement row. The accession falls within the study's cultured-isolate series. Community findings and experiments on other named isolates are not DJM2B2 phenotypes.

Exact-taxid Assembly search returned zero IDs, with phrase-not-found and no-items diagnostics. This describes the bounded query, not proof that no assembly exists anywhere.

## Completeness

The identity seed is complete enough for its represented claims. Optional nomenclature, taxonomy mappings, deposited strains, genome links, and phenotypes are not justified by the inspected target-specific evidence. `seed.py:483` through the strain-count assignment confirms that `strain_count` counts deduplicated BacDive entries; a GenBank strain qualifier does not make zero inconsistent.

Ignored-inclusive, hidden-file and compressed-content searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Whole identifier, label, and designation searches returned only the backbone, native name, and scope contexts. A separate whole-accession/PMID/DOI search returned no contexts. Exact target report/history filename searches and history-content searches were also negative before this report. These are bounded inventory findings, not global biological absences.

Exact S3/S4 workbook rows were not inspected: prior downloads failed and the prescribed spreadsheet workspace loader is unavailable in the current tool inventory. No host genotype, medium, antibiotic production, growth promotion, or other measured trait is inferred. iModulonDB is not applicable to this identity-only seed without a relevant gene, regulator, or expression-module claim.

## Findings

None found.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

No required edits. Do not patch the generated YAML, add a genome for a 16S marker, or promote status. Optional future enrichment must first inspect the exact accession/designation row and establish a supported maintained input or reviewed schema/ingestion change.

## Follow-up Checks

For optional enrichment, resolve exact S3/S4 rows and their experimental scope. Before any strain-genome association, verify an eligible whole collection accession and its explicit source chain. Apply future authorized changes upstream, regenerate through the validated writer, then run focused schema and strict checks and full corpus reproduction. No remediation is required by this review.

## Additional Notes

All invoked record checks terminated successfully; bounded negative searches use exit 1 as no match. The NCBI browser fallback was a complete structured API read, not a search snippet. Local guidance, validator recipes, seeder counting logic, and full-corpus CLI limits were reread. No record, source, generated page, prior report, curation history, or status was changed. This review adds only this new report.

