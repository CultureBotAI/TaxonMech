# YAML Record Review: Micrococcus sp. DJM1B8

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/micrococcus_sp_djm1b8.yaml`
- Started UTC: 2026-10-05T03:53:52Z
- Finished UTC: 2026-10-05T03:55:08Z
- Verdict: pass

## Target

Read the complete 54-line generated `TaxonRecord` for `NCBITaxon:1034223`, Micrococcus sp. DJM1B8. The record is a bacterial isolate placeholder with NCBI `SPECIES` rank, parent `NCBITaxon:2620948`, genetic code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. Its one NCBITAXON assertion has unit `NAME` and cites the 2026-09-13 snapshot.

Species rank here identifies NCBI's entity, not a validly published species name. Maintained inputs are `data/raw/ncbitaxon_taxa.tsv` and `curation/seed_scope.tsv`; seeding behavior is in `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/micrococcus_sp_djm1b8.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/micrococcus_sp_djm1b8.yaml --out /private/tmp/micrococcus-djm1b8-strict-20261005.tsv`: exit 0; one file scanned, zero files with errors and zero error rows.
- Bounded structured comparisons passed all identity fields, the complete ancestor chain, synonyms, attestation, path, scope, and inline seed-event checks.
- `just verify-corpus`: not run; the documented command is full-corpus-only. `--max-diffs` limits diagnostics, not record scope.
- `just validate-products`: not applicable; no curator-added graph nodes or product-label assertions occur.
- `just validate-history`: not run; the ignored-inclusive target-history search returned no separate history artifact. The inline seed event was inspected, without adding an event or promoting status.

## Identity and Grounding

The row at `data/raw/ncbitaxon_taxa.tsv:221491` matches the exact identifier, label, rank, domain placement, parent, code, and NCBI-only snapshot provenance. Neither the backbone nor the YAML supplies synonyms. The complete object at `data/catalog/ncbi_names-0005.jsonl.gz:30843` is the matching scientific-name entry with an empty unique-name field.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034223&retmode=xml) agrees with the identity, rank, parent, code, and non-root ancestor labels/ranks. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034223) independently confirms identity and the root-inclusive ancestor list. The browser page was inaccessible through the web tool; both structured responses were inspected.

The exact ten-entry root-first chain is 1 root, 131567 cellular organisms, 2 Bacteria, 1783272 Bacillati, 201174 Actinomycetota, 1760 Actinomycetes, 85006 Micrococcales, 1268 Micrococcaceae, 1269 Micrococcus, and 2620948 unclassified Micrococcus. Every label and rank matches the pinned NCBI backbone. No inferred classification is substituted.

## Evidence

`data/taxa/PATHS.tsv:13953` uniquely maps the taxon to the correct slug. `curation/seed_scope.tsv:321809` supplies the date and exact one-source reason recorded by the inline 2026-09-13T17:54:04Z `SEEDED_FROM_SOURCES` event. The source count represents one name, not a strain, genome, or experimental observation.

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. The backbone has no children for this taxon. Exact type-material, merged-ID, and dropped-record scans were negative.

The exact-taxid Nuccore query returned one accession, [JF753417.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753417.1), a 657-base partial 16S rRNA gene sequence. Its complete metadata, references, and features were inspected. The organism label, strain DJM1B8, and taxon cross-reference 1034223 agree; source qualifiers describe Zea seed isolation. This is marker identity and bounded isolation evidence, not a complete genome, authenticated deposit, or independently demonstrated phenotype.

The sequence explicitly cites PMID 21673982 and DOI 10.1371/journal.pone.0020396. Its citation agrees with previously fetched and inspected [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml) for Johnston-Monje and Raizada's 2011 study. Previously inspected [publisher methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) give culture-derived accession interval JF753401-JF753552, which contains this marker. No fresh whole-paper fetch or supplementary-row inspection is claimed.

## Completeness

Boundary-aware searches for the identifier, label/slug, and designation used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only `SOURCE.json` manifests. Ignored, hidden, and compressed files were included. Exactly the backbone, native scientific name, and scope contexts matched. A secondary search for the whole accession, PMID, and DOI returned zero matches in that scope. Separate ignored-inclusive exact prior-report filename and history searches were also negative. These results are local-source bounds, not global evidence-absence claims.

The current exact-taxid Assembly query returned count zero, no IDs, and phrase-not-found/no-items diagnostics. It does not prove universal genome absence. The inspected evidence establishes no eligible culture-deposit or genome join.

`strain_count: 0` agrees with the BacDive entry-count semantics in `src/taxonmech/seed.py:483` and the count assignment at line 543. A strain qualifier on a cultured marker does not create a BacDive entry or CAFI-qualified collection accession. Optional nomenclature, mappings, strains, genomes, and graph slots are appropriately empty. An optional marker/paper citation is not required for this seeded identity record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Represented identity and provenance are supported at their stated scope. Supplementary tables S3/S4 remain uninspected, so no DJM1B8-specific host genotype, medium, phenotype, growth-promotion, or transmission claim is inferred. Community-level results and results for other named isolates are not evidence for this isolate's traits.

## Recommended Edits

None required. Leave generated YAML and `SEEDED` status unchanged. Do not convert DJM1B8 into a culture-collection accession or its marker into a genome.

Optional enrichment should first resolve the exact primary source row and an appropriate maintained evidence input. If changes are needed, their owners are the relevant inventory/overlay and `src/taxonmech/seed.py`, with tests before authorized regeneration.

## Follow-up Checks

Inspect the exact DJM1B8 supplementary row, table headers, and units before adding any experimental claim. After a later authorized maintained-input change, rerun the focused schema and strict validators, then full-corpus reproduction and relevant repository gates.

## Additional Notes

The prescribed spreadsheet dependency loader was checked this turn and is unavailable; earlier supplement download attempts failed. No workbook workaround or uninspected row claim was used. iModulonDB is not applicable because this identity seed contains no gene, regulator, or transcriptomic assertions.

Only this new report was added. No target YAML, source inventory, existing report, history, generated page, or review status was changed.

