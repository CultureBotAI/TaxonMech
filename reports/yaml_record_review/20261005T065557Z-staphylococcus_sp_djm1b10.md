# YAML Record Review: Staphylococcus sp. DJM1B10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_djm1b10.yaml`
- Started UTC: 2026-10-05T06:54:38Z
- Finished UTC: 2026-10-05T06:55:57Z
- Verdict: pass

## Target

Read all 54 lines of the generated `TaxonRecord` for `NCBITaxon:1034287`, Staphylococcus sp. DJM1B10. It is a bacterial isolate placeholder with NCBI `SPECIES` rank, parent `NCBITaxon:91994`, genetic code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. Its sole source attestation counts one NCBITAXON `NAME` from 2026-09-13. Rank does not establish validly published nomenclature, a named species, or a pathogenic phenotype.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py`, invoked by `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/staphylococcus_sp_djm1b10.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/staphylococcus_sp_djm1b10.yaml --out /private/tmp/staphylococcus-djm1b10-strict-20261005.tsv`: exit 0; one file scanned, zero error files or rows.
- Structured comparisons passed identity, complete lineage, synonyms, attestation, path-index, scope, and inline-event checks.
- `just verify-corpus`: not run; full-corpus-only. Its `--max-diffs` option limits diagnostics, not record scope.
- `just validate-products`: not applicable without curator-added graph/product-label assertions.
- `just validate-history`: not run; ignored-inclusive target-history search found no separate artifact. Inline provenance was inspected without history writes or status promotion.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221555` supports identity, rank, parent, genetic code, and snapshot. Source and YAML have no synonyms. The entire native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30907` agrees and has an empty unique-name field.

Complete live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034287&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034287) responses were inspected after the browser page was unavailable through the web tool. They confirm identity and lineage; EFetch also confirms parent, ancestor ranks, and code.

All ten root-first ancestors agree with the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 1783272 Bacillati, 1239 Bacillota, 91061 Bacilli, 1385 Caryophanales, 90964 Staphylococcaceae, 1279 Staphylococcus, and 91994 unclassified Staphylococcus. Labels and ranks match throughout. No placement under a named species is inferred.

## Evidence

`data/taxa/PATHS.tsv:14018` uniquely maps identifier to slug. `curation/seed_scope.tsv:321873` supplies the exact one-source reason reproduced by the inline `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. The attestation counts a name, not an experiment, strain, or genome.

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. The backbone has no target children. Exact type-material, merged-ID, and dropped-record scans were negative.

Exact-taxid Nuccore search returned one sequence. Complete metadata, references, and features for [JF753419.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753419.1) identify a 651-base partial 16S rRNA gene, organism Staphylococcus sp. DJM1B10, strain DJM1B10, and taxon cross-reference 1034287. Host and isolation-source qualifiers support a bounded Zea seed context. This marker is not an assembly, authenticated collection deposit, independent named-species identification, or measured phenotype.

The sequence cites PMID 21673982 and DOI 10.1371/journal.pone.0020396. Cached [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml) were reread and agree with Johnston-Monje and Raizada's 2011 study; this was not a fresh PubMed fetch. Previously inspected [publisher methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) give cultured-isolate interval JF753401-JF753552, including this accession. No fresh whole-paper or supplementary-row inspection is claimed.

Community-level findings and other isolates' results are not DJM1B10-specific evidence. No host genotype, medium, growth promotion, transmission, pathogenicity, or antimicrobial-resistance assertion is inferred from the paper or genus.

## Completeness

Primary identifier, label/slug, and designation searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only `SOURCE.json` manifests. Hidden, ignored, and compressed sources were included. Only the backbone, native name, and scope contexts matched. A secondary whole-accession/PMID/DOI search returned zero matches. Separate ignored-inclusive exact prior-report filename and target-history searches were negative. These are bounded source results, not universal absence claims.

Exact-taxid Assembly search returned zero with no IDs and phrase-not-found/no-items diagnostics. No eligible deposit or genome join was established. `strain_count: 0` agrees with BacDive entry-count semantics in `src/taxonmech/seed.py`; a GenBank strain qualifier is not a BacDive entry or CAFI-qualified deposit. Optional nomenclature, mappings, strains, genomes, graphs, and literature enrichment are not required for this supported identity seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Uninspected supplementary tables S3/S4 limit optional enrichment without invalidating the represented identity or provenance.

## Recommended Edits

None required. Retain generated YAML and `SEEDED` status. Do not turn DJM1B10 into a collection accession or its marker into a genome. Future enrichment needs an exact supported source row and a suitable maintained input.

## Follow-up Checks

Inspect the exact DJM1B10 supplementary row with headers and units before adding experimental assertions. After an authorized maintained-input change, rerun focused schema and strict validation, full-corpus reproduction, and applicable repository gates.

## Additional Notes

The prescribed spreadsheet dependency loader was checked and is unavailable; earlier supplement download attempts failed. No workbook workaround or unsupported row-level claim was used. iModulonDB is not applicable to this seed, which contains no gene, regulatory, or transcriptomic assertions.

Only this new report was added for the target. No YAML, inventory, prior report, generated page, history, or status was changed.

