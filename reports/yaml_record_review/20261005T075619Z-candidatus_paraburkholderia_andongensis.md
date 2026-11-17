# YAML Record Review: Candidatus Paraburkholderia andongensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/candidatus_paraburkholderia_andongensis.yaml`
- Started UTC: 2026-10-05T07:49:45Z
- Finished UTC: 2026-10-05T07:56:19Z
- Verdict: pass

## Target

Read the entire 77-line generated `TaxonRecord` for `NCBITaxon:1034313`. It represents Candidatus Paraburkholderia andongensis at `SPECIES` rank in `BACTERIA`, parent `NCBITaxon:1822464`, with code 11, eight NCBI synonyms, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. The sole attestation counts one NCBITAXON `NAME` from snapshot 2026-09-13, not nine native name rows or five isolates.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, `src/taxonmech/ncbi_taxdump.py`, and `src/taxonmech/seed.py` through `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/candidatus_paraburkholderia_andongensis.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/candidatus_paraburkholderia_andongensis.yaml --out /private/tmp/andongensis-strict-20261005.tsv`: exit 0; one file, zero error files or rows.
- Structured comparisons passed identity, full lineage, attestation, path-index, scope, and inline-event checks. An additional exact-set check verified all eight synonym text/type/source tuples, with no duplicates.
- `just verify-corpus`: not run; full-corpus-only. Its inspected `--max-diffs` option limits diagnostics, not record scope.
- `just validate-products`: not applicable without curator-added graph/product-label assertions.
- `just validate-history`: not run; ignored-inclusive target/alias/history searches found no separate artifact. Inline history was inspected.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221576` supports the record. All nine complete native name objects at `data/catalog/ncbi_names-0005.jsonl.gz:30925` through line 30933 were inspected, including their empty unique-name fields.

Complete live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034313&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034313) responses confirm identity, rank, parent chain, and code. The browser page was inaccessible through the web tool.

The nine root-first ancestors match the pinned backbone: 1 root, 131567 cellular organisms, 2 Bacteria, 3379134 Pseudomonadati, 1224 Pseudomonadota, 28216 Betaproteobacteria, 80840 Burkholderiales, 119060 Burkholderiaceae, and 1822464 Paraburkholderia. Labels and ranks agree.

The two exact synonyms correspond to NCBI's synonym and equivalent-name classes: the Lemaire 2011 Burkholderia name and Paraburkholderia andongensis. The authority string is related, as are the five `includes` names for BL259, BL271, BL286, BL293, and SD1097. This matches `ncbi_taxdump.py:91` and `seed.py:381`; isolate names are not promoted to exact species equivalences.

`data/raw/ncbi_merged_ids.tsv` lines 1001, 1002, 1003, and 1005 redirect 1034314, 1034315, 1034316, and 1034318 into 1034313. The target is the current destination, not a retired source ID. No exact dropped or type-material rows were found.

## Evidence

`data/taxa/PATHS.tsv:14040` uniquely supplies the slug. `curation/seed_scope.tsv:321891` matches the exact reason in the inline `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. Full mapped-inventory scans found no target entries in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits; the backbone has no target children.

The inspected [LPSN Paraburkholderia page](https://lpsn.dsmz.de/species/paraburkholderia-andongensis), record 22381, recognizes the Candidatus name and reports not-validly-published status alongside pro-validly-published/pro-correct status. Its type field says no type strain is designated. The [LPSN Burkholderia page](https://lpsn.dsmz.de/species/burkholderia-andongensis), record 800196, instead names SD 1097 and marker JF916921. These name-specific fields are preserved as external source context, not silently reconciled into a culture-deposit or type-strain assertion. NCBI's authority attribution also retains Lemaire in parentheses, whereas the Paraburkholderia LPSN heading credits Sawana directly; the YAML correctly attributes its own string to NCBI.

Exact-taxid Nuccore search returned 13 records. Every record's full metadata, references, and features were inspected, excluding raw bases and protein translations. All carry taxon 1034313 and the indicated isolate. The following lists all returned nucleotide accessions, each at version `.1`, with lengths in bases; a dash means no returned marker for that isolate in this query, not biological absence.

| Isolate | 16S rRNA | recA | gyrB |
| --- | --- | --- | --- |
| BL259 | - | JF916912.1, 549 | JF916907.1, 588 |
| BL271 | JF916918.1, 1139 | JF916913.1, 549 | JF916908.1, 588 |
| BL286 | JF916919.1, 1139 | - | JF916906.1, 564 |
| BL293 | JF916920.1, 1139 | JF916914.1, 549 | JF916909.1, 562 |
| SD1097 | [JF916921.1](https://www.ncbi.nlm.nih.gov/nuccore/JF916921.1), 1138 | JF916915.1, 549 | JF916905.1, 588 |

These are partial marker sequences, not genomes or collection deposits. Exact-taxid Assembly search returned zero IDs with phrase-not-found/no-items diagnostics, a bounded query rather than global absence proof.

All 13 records cite Lemaire et al. (2011), [PMID 22203556](https://pubmed.ncbi.nlm.nih.gov/22203556/), [DOI 10.1007/s12275-011-1163-5](https://link.springer.com/article/10.1007/s12275-011-1163-5). Complete primary PubMed metadata/abstract and the publisher abstract were inspected. They support the original Candidatus proposal in the Sericanthe leaf-symbiont study using 16S, recA, and gyrB; main-text access was subscription-only.

The public [supplementary PDF](https://static-content.springer.com/esm/art%3A10.1007%2Fs12275-011-1163-5/MediaObjects/12275_2011_1163_MOESM1_ESM.pdf) was text-inspected and its Figure S1 panels A-C visually inspected on PDF pages 3-5. The four, four, and five andongensis isolate labels respectively agree with the marker sets above. This supports the alias association, not any genome identity or experimental phenotype.

Sawana et al. (2014), [DOI 10.3389/fgene.2014.00429](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2014.00429/full), was inspected at the publisher for citation, abstract, and opening methods. It supplies the generic reclassification context referenced by LPSN, not a target-specific phenotype; later attempts to inspect deeper text timed out. No whole-paper reading is claimed.

## Completeness

The seed's represented identity, synonym scopes, lineage, count, and provenance are supported. Optional nomenclature enrichment is available externally, but no target LPSN input or mapping is present locally. Absence of that optional enrichment is not treated as an invalid NCBI identity or a required direct YAML edit.

Ignored-inclusive searches covered hidden and compressed contents under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding generic `SOURCE.json` descriptors. Exact identity/name/alias matching found 15 contexts: backbone, scope, four redirects, and nine native names. Boundary-corrected old-ID/spaced-alias searches returned only the four redirects. Exact nucleotide/original-paper searches and LPSN record-ID/record-DOI searches returned none. The Sawana DOI occurs in 53 LPSN rows; all source names were inspected and none denotes this target. Sharing that paper does not transfer another species' deposits or genomes.

An exploratory broad substring search also matched unrelated names and accession substrings; its truncated output was not used to establish absence. The bounded searches above support the stated conclusions.

Seeder code counts BacDive entries, not NCBI isolate aliases or marker sequences. Zero strains is therefore consistent. No authenticated collection identifier or explicit genome source chain was established. iModulonDB is not applicable: the markers serve taxonomy here, not a claimed expression module or regulatory mechanism.

## Findings

None found.

Counts: 0 blocker, 0 major, 0 minor.

## Recommended Edits

No required edits. Retain the current NCBI identity and scoped synonyms; do not add five culture strains, thirteen genomes, or a synthesized type designation.

Optional nomenclature enrichment should be researched in the maintained LPSN source/mapping pipeline (`src/taxonmech/extract.py` and upstream kg-microbe inputs), preserving both name records, their distinct fields, stable source identifiers, and Candidatus pro-status semantics. Resolve the type-field discrepancy at its authorities before adding a type assertion. Do not patch generated YAML or promote status.

## Follow-up Checks

For optional enrichment, inspect the complete original description and current name-specific authority records, verify any explicit NCBI mapping, and test preservation of synonym scope and nomenclatural status. Require whole eligible collection accessions and explicit source chains for genome joins. After an authorized upstream change, regenerate with the validated writer and run focused schema/strict checks plus full corpus reproduction.

## Additional Notes

All invoked command sessions terminated. Web screenshot calls returned no usable image payload, and Poppler was unavailable on PATH; the public PDF was instead rendered with local PDFKit to temporary PNGs and visually inspected. No PDF was edited. Main-text and deeper 2014 reading limits remain explicit.

No taxon, source, generated page, earlier report, curation history, or status changed. This review adds only this new repository report; downloaded/rendered inspection artifacts are under `/private/tmp`.

