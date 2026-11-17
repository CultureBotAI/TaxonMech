# YAML Record Review: Microbacterium sp. DJM20

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/microbacterium_sp_djm20.yaml`
- Started UTC: 2026-10-05T03:49:43Z
- Finished UTC: 2026-10-05T03:51:03Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034221`. Microbacterium sp. DJM20 is a `SPECIES`-rank bacterial isolate placeholder, not a claim of a validly published species name. The record carries parent `NCBITaxon:2609290`, `EXACT` grounding, `SEEDED` status, genetic code 11, zero inventoried strains, and one NCBITAXON `NAME` assertion.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and the seeding behavior in `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`. Generated YAML is read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/microbacterium_sp_djm20.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/microbacterium_sp_djm20.yaml --out /private/tmp/microbacterium-djm20-strict-20261005.tsv`: exit 0; one file scanned, zero files with errors and zero error rows.
- Structured comparisons passed identity, full lineage, synonym, source-attestation, path, scope, and inline seed-event checks. They are not a substitute for corpus reproduction.
- `just verify-corpus`: not run; it exposes a full-corpus check, not a record selector. `--max-diffs` only caps diagnostics.
- `just validate-products`: not applicable; no curator-added graph nodes or product-label claims.
- `just validate-history`: not run; the separate ignored-inclusive target-history search returned no artifact. The inline seed event was inspected instead.

## Identity and Grounding

The backbone row at `data/raw/ncbitaxon_taxa.tsv:221489` matches the exact identifier, label, rank, parent, code, NCBI-only attestation, and 2026-09-13 snapshot. The full native object at `data/catalog/ncbi_names-0005.jsonl.gz:30841` is its scientific-name entry, with no unique-name qualifier. Neither backbone nor YAML supplies synonyms.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034221&retmode=xml) confirms the identity, parent, rank, code, and non-root ancestor labels and ranks. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034221) independently agrees and includes root in its ancestor list. The browser page was inaccessible through the web tool; both structured responses were inspected.

All ten root-first ancestors match: 1 root, 131567 cellular organisms, 2 Bacteria, 1783272 Bacillati, 201174 Actinomycetota, 1760 Actinomycetes, 85006 Micrococcales, 85023 Microbacteriaceae, 33882 Microbacterium, and 2609290 unclassified Microbacterium. No inferred placement replaces the NCBI chain.

## Evidence

The unique `data/taxa/PATHS.tsv:13951` entry has the correct slug. `curation/seed_scope.tsv:321807` supplies the 2026-09-13 date and one-source reason used by the 2026-09-13T17:54:04Z inline `SEEDED_FROM_SOURCES` event. The source assertion is one name, not a genome or phenotype count.

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. The backbone has no target children. Exact type-material, merged-ID, and dropped-record scans were negative.

The exact-taxid Nuccore query returned one accession. Its complete metadata, references, and features were inspected: [JF753539.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753539.1), a 271-base partial 16S rRNA gene sequence. Organism, strain DJM20, and taxon cross-reference 1034221 agree. Source qualifiers give Zea seed isolation context. This short marker is neither a genome nor independent proof of a species-level identification.

The accession explicitly cites PMID 21673982 and DOI 10.1371/journal.pone.0020396. These agree with the previously fetched and inspected [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml) for Johnston-Monje and Raizada's 2011 study. Previously inspected [publisher methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) place culture-derived sequences in JF753401-JF753552, including this accession. This review does not claim a new paper fetch, full-article inspection, or inspection of supplementary rows.

## Completeness

Boundary-aware searches for the whole identifier, label/slug, and designation used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only `SOURCE.json` manifests. Hidden, ignored, and compressed files were included. Exactly three contexts matched: the backbone, native scientific name, and scope. A secondary whole-accession/PMID/DOI search returned zero matches in the same scope. Separate ignored-inclusive prior-report filename and history searches were negative. These findings are local-source bounds, not universal absence claims.

The exact-taxid Assembly query returned count zero and no IDs, with phrase-not-found/no-items diagnostics. It is only a bounded query result. No genome or eligible culture-deposit link was established.

`strain_count: 0` is consistent with the BacDive entry-count semantics in `src/taxonmech/seed.py:483` and the assignment at line 543. GenBank's strain qualifier is not a BacDive entry or a CAFI-qualified collection accession. Empty optional nomenclature, strain, genome, mapping, and graph slots are appropriate. The optional marker/paper citation is not required for this identity seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Supported claims remain restricted to the seeded taxon identity and provenance. Community-level results and observations about other isolates cannot supply DJM20-specific traits. Supplementary tables S3/S4 remain uninspected.

## Recommended Edits

None required. Do not edit the generated YAML or promote `SEEDED` after this automated review. Do not turn DJM20 into a collection accession or the short 16S marker into a genome.

Any optional enrichment must first resolve an exact source row and be represented in an appropriate maintained inventory/overlay, with seeder changes and tests where necessary.

## Follow-up Checks

Before adding traits, host genotype, medium, growth promotion, or transmission claims, inspect the exact DJM20 supplementary row with headers and units. Validate any later authorized maintained-input change with the focused schema and strict commands, then full-corpus reproduction and relevant repository gates.

## Additional Notes

The spreadsheet dependency loader prescribed for supplement inspection is unavailable in the enabled tools; earlier supplement download attempts failed. No workaround or unsupported row-level claim was made. iModulonDB is not applicable to this taxonomic identity seed, which has no gene, regulatory, or transcriptomic assertions.

Only this new report was added. No YAML, source inventory, existing report, history event, generated page, or review status was changed.

