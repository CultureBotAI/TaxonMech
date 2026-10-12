# YAML Record Review: Paenibacillus sp. DJM1

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/paenibacillus_sp_djm1.yaml`
- Started UTC: 2026-10-05T03:56:46Z
- Finished UTC: 2026-10-05T03:58:26Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1034224`, Paenibacillus sp. DJM1. It is an NCBI `SPECIES`-rank bacterial isolate placeholder with parent `NCBITaxon:185978`, genetic code 11, `EXACT` grounding, `SEEDED` status, and zero inventoried strains. The sole attestation is one NCBITAXON `NAME` assertion from the 2026-09-13 snapshot. NCBI species rank is not a claim of validly published species nomenclature.

Maintained owners are `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `src/taxonmech/seed.py`, invoked through `scripts/seed_from_sources.py`. Generated YAML remains read-only.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/paenibacillus_sp_djm1.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/paenibacillus_sp_djm1.yaml --out /private/tmp/paenibacillus-djm1-strict-20261005.tsv`: exit 0; one file scanned, zero files with errors and zero error rows.
- Structured source comparisons passed all identity fields, full lineage, synonyms, attestation, path-index, scope, and inline seed-event checks.
- `just verify-corpus`: not run; it is full-corpus-only. `--max-diffs` caps diagnostics and is not a record selector.
- `just validate-products`: not applicable; no curator-added graph nodes or product-label claims occur.
- `just validate-history`: not run; an ignored-inclusive target-history search found no separate history artifact. The inline seed event was inspected without adding an event or changing status.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221492` agrees with the exact identifier, label, rank, parent, code, NCBI-only provenance, and snapshot date. No synonyms appear in either the source row or YAML. The complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30844` identifies this taxon and has an empty unique-name field.

Live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034224&retmode=xml) confirms the identity, parent, rank, code, and non-root ancestor labels/ranks. [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034224) independently agrees and includes root in the ancestor list. The browser page could not be opened through the web tool; the structured responses were inspected instead.

The complete ten-entry root-first chain matches: 1 root, 131567 cellular organisms, 2 Bacteria, 1783272 Bacillati, 1239 Bacillota, 91061 Bacilli, 1385 Caryophanales, 186822 Paenibacillaceae, 44249 Paenibacillus, and 185978 unclassified Paenibacillus. All labels and ranks agree with the pinned backbone. No inferred or reconciled placement replaces NCBI's chain.

## Evidence

`data/taxa/PATHS.tsv:13954` uniquely maps the identifier to the correct slug. `curation/seed_scope.tsv:321810` supplies the scope date and one-source reason used by the inline `SEEDED_FROM_SOURCES` event at 2026-09-13T17:54:04Z. The one-name assertion is not a strain, genome, or phenotype count.

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD organisms, MediaDive, Madin, or BactoTraits. The backbone has no target children. Exact type-material, merged-ID, and dropped-record scans were negative.

The exact-taxid Nuccore query returned one accession. Its complete metadata, references, and features were inspected: [JF753521.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753521.1), a 599-base partial 16S rRNA gene sequence. Organism, strain DJM1, and taxon cross-reference 1034224 agree. Source qualifiers give Zea seed isolation context. This supports marker identity and a bounded isolation context, not an assembly, authenticated culture deposit, or experimental phenotype.

The sequence explicitly cites PMID 21673982 and DOI 10.1371/journal.pone.0020396. Its citation agrees with the previously fetched and inspected [PubMed metadata and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml) for Johnston-Monje and Raizada's 2011 study. Previously inspected [publisher methods and supplement descriptions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020396) give culture-derived accession interval JF753401-JF753552, which includes this marker. No fresh whole-paper fetch or supplementary-row inspection is claimed.

The paper's predicted genus-level Paenibacillus signals and community-wide observations are not evidence that DJM1 has a particular distribution or phenotype. No host genotype, medium, growth promotion, persistence, or transmission claim is transferred from those results.

## Completeness

Boundary-aware identifier, label/slug, and designation searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding only `SOURCE.json` manifests. Ignored, hidden, and compressed files were included. Exactly the backbone, native scientific name, and scope contexts matched. A secondary whole-accession/PMID/DOI search returned zero matches in that scope. Separate ignored-inclusive exact prior-report filename and history searches were negative. Whole-designation boundaries excluded longer DJM1-prefixed names; no substring join was used.

The live exact-taxid Assembly query returned count zero, no IDs, and phrase-not-found/no-items diagnostics. This is a bounded result, not proof of universal genome absence. No eligible culture-deposit or genome join was established.

`strain_count: 0` is consistent with BacDive entry-count semantics in `src/taxonmech/seed.py:483` and the line-543 count assignment. A strain qualifier on a culture-derived marker does not create a BacDive entry or a CAFI-qualified collection accession. Optional nomenclature, mapping, strain, genome, and graph slots are appropriately empty. The optional marker citation is not required for this identity seed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity and provenance are supported at the represented scope. Supplementary tables S3/S4 remain uninspected; this limits optional enrichment but does not invalidate the seeded record.

## Recommended Edits

None required. Leave generated YAML and `SEEDED` status unchanged. Do not manufacture a collection accession from DJM1 or count its 16S marker as a genome.

Optional enrichment must first resolve an exact supported source row and a suitable maintained evidence input. Relevant inventory/overlay and `src/taxonmech/seed.py` changes, if necessary, need tests before authorized regeneration.

## Follow-up Checks

Inspect the exact DJM1 supplementary row with its headers and units before adding isolate-level experimental assertions. After any later authorized maintained-input change, rerun focused schema and strict validation, then full-corpus reproduction and applicable repository gates.

## Additional Notes

The prescribed spreadsheet dependency loader was checked this turn and is unavailable; earlier supplement downloads failed. No workaround or uninspected row claim was used. iModulonDB is not applicable because the record makes no gene, regulatory, or transcriptomic assertion.

Only this new report was added. No target YAML, source inventory, existing report, history event, generated page, or review status was changed.

