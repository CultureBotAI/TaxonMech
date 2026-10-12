# YAML Record Review: Alvinella pompejana symbiont apg10

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg10.yaml`
- Started UTC: 2026-10-05T00:21:04Z
- Finished UTC: 2026-10-05T00:22:48Z
- Verdict: pass

## Target

Read the entire 51-line generated TaxonRecord for NCBITaxon:103400, Alvinella pompejana symbiont apg10: SPECIES, BACTERIA, parent NCBITaxon:38780, EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. The target is the bacterial taxon, not its eukaryotic host or a generic host-associated community.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg10.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg10.yaml --out /private/tmp/apg10-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: structured comparison of the complete backbone row, all nine ancestors, seven mapped-source inventories, PATHS entry, seed-scope row, sole attestation and inline seed event. No descendants occur in the pinned backbone.
- PASS: exact target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus` is full-corpus only; no focused mode was invented and the diagnostic cap was not treated as a scope selector.
- NOT APPLICABLE: `just validate-products`; no causal nodes or product labels.
- SKIPPED: `just validate-history`; an ignored-inclusive identifier/name/slug search found no external target history. The inline seed event was checked directly.
- No separate documented focused term/reference validator was substituted; source identifiers were checked directly.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18457` and the full native scientific-name object at `data/catalog/ncbi_names-0000.jsonl.gz:38466` identify this exact taxon, without additional synonyms. Its root-first lineage through Spirochaetota, Spirochaetia, Spirochaetales, Spirochaetaceae and unclassified Spirochaetaceae agrees with the generated record.

Live NCBI Taxonomy EFetch and Datasets responses confirm the label, species rank, bacterial placement, parent, genetic code and ancestor identifiers. SPECIES is the source database's taxonomic rank; it does not establish a validly published binomial or a cultured isolate. EXACT grounds the record to this NCBI entity, not to all bacteria associated with the host. [NCBI taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103400).

The bare designation APG10 also appears on NCBITaxon:1308970, Chryseobacterium sp. APG10. Its separate backbone, native name and scope rows were inspected as search contexts and rejected as a name collision, not imported as evidence for 103400.

## Evidence

- The sole attestation matches the pinned 2026-09-13 NCBI NAME assertion exactly. All lineage labels and rank values were compared to the backbone; live taxonomy independently corroborates them.
- Exact NCBI Nuccore search `txid103400[Organism:noexp]` returned one record. Full GenBank metadata and feature qualifiers identify AF180309.1 as a 474-base partial 16S sequence, clone apg10, taxon:103400. The record retains an unpublished research-reference title and an August 1999 direct submission; it does not itself supply a publication DOI. The raw nucleotide string was not analyzed. [GenBank AF180309.1](https://www.ncbi.nlm.nih.gov/nuccore/AF180309.1).
- The inspected Campbell and Cary 2001 primary article explicitly links APG10 to AF180309 and identifies it as spirochete A. Its abstract, clone-sequencing context, accession paragraph and relevant results distinguish APG10 from spirochete B. The broader distribution attributed to B must not be assigned to A, nor does community-level discussion prove a specific metabolic mechanism for APG10. This is supporting identity context, not a new YAML phenotype claim. [Primary study, DOI:10.1128/AEM.67.1.110-117.2001](https://journals.asm.org/doi/full/10.1128/aem.67.1.110-117.2001).
- Exact NCBI Assembly search for 103400 returned zero records, with the service's no-items/phrase-not-found diagnostic. This is a bounded query result, not proof that no relevant genome could exist under another classification.
- `data/taxa/PATHS.tsv:13873` and `curation/seed_scope.tsv:144108` support the slug, September 13 admission and one-source rationale. The inline event matches the source list and rationale; it does not claim a previous human review.

## Completeness

The full scans found no target rows in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits mapped inventories. There are no descendants to contribute BacDive strains. The empty strain listing and count zero are consequently consistent with source coverage, not statements that the organism does not exist or cannot be cultured.

An ignored-inclusive, hidden-file-inclusive and compressed-file-aware search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All six matching contexts were read: three target records and three unrelated Chryseobacterium name-collision contexts. A second accession search for AF180309 in those roots returned zero matches. No target culture-deposit, supported strain/genome crosswalk, mapping or required overlay was established.

The external marker and paper are useful future enrichment leads, not grounds to fabricate a BacDive strain, type deposit, genome assembly or nomenclature entry. Optional evidence and causal-graph fields may remain empty in this identity-only seed. iModulonDB is not applicable: no functional gene, regulator or expression-module claim is made. Ignored-inclusive report and history searches found no previous target report or external history record.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The seeded identity, lineage, count and provenance are supported within the checked source scope.

## Recommended Edits

None required. Do not edit the generated YAML or promote its status for this review.

Optional later literature enrichment belongs in a separately authorized maintained evidence input and its seeding path, not a hand edit of `data/taxa/`. Any future backbone correction belongs to the pinned NCBI source extraction feeding `data/raw/ncbitaxon_taxa.tsv`; scope changes belong to `curation/seed_scope.tsv`.

## Follow-up Checks

- Rerun the two focused validators and source comparisons after any authorized curation.
- Run `just verify-corpus` separately before asserting full-corpus reproduction.
- Preserve APG10/spirochete-A versus spirochete-B scope when adding paper-derived evidence, and preserve the unrelated Chryseobacterium APG10 boundary.
- Treat AF180309 as marker-sequence evidence, not a genome or a culture deposit. Recheck live sources if source versions are refreshed.

## Additional Notes

This review checked a single resolved bacterial record. The primary paper was read for target identity and scope; not all images, sequence bases or experimental conclusions were audited. Searches establish absence only within the named inventories and exact external query. No paid research, source refresh, regeneration, GitHub mutation, status promotion or history append occurred. Only this new timestamped review report was written.

