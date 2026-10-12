# YAML Record Review: Alvinella pompejana symbiont apg115

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg115.yaml`
- Started UTC: 2026-10-05T00:43:20Z
- Finished UTC: 2026-10-05T00:44:52Z
- Verdict: pass

## Target

Read the entire 42-line generated TaxonRecord for NCBITaxon:103407, Alvinella pompejana symbiont apg115. This is a bacterial SPECIES-rank source taxon with parent NCBITaxon:122728, genetic code 11, EXACT grounding, SEEDED status, zero inventoried strains and one NCBI NAME attestation. It denotes this clone-associated taxon, not the host or the entire symbiont community.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/alvinella_pompejana_symbiont_apg115.yaml`; LinkML exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/alvinella_pompejana_symbiont_apg115.yaml --out /private/tmp/apg115-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: structured comparison of the complete backbone row, all six ancestors, seven mapped-source inventories, PATHS entry, scope row, NCBI attestation and inline-event text. The pinned backbone has no children of this target.
- PASS: full exact-target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus` is a full-corpus check without a focused target mode; a diagnostic cap is not a scope filter.
- NOT APPLICABLE: `just validate-products`; the record has no curator-added graph nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive identifier/name/slug searches found no external target history. The inline seed event was checked directly.
- No undocumented focused term/reference validator was substituted. Represented identifiers were checked against source evidence.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:18464` and native scientific-name object at `data/catalog/ncbi_names-0000.jsonl.gz:38473` agree on APG115 and supply no synonym.

All six root-first ancestors match by identifier, label and rank: root, cellular organisms, Bacteria, Pseudomonadati, Campylobacterota and unclassified Campylobacterota. Live official responses confirm the name, species rank, bacterial placement, parent 122728, code 11 and lineage identifiers. EFetch omits root from its labeled lineage; Datasets includes root identifier 1. The source's unclassified branch does not justify inventing missing class/order/family/genus entries. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103407&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103407).

EXACT denotes identity with NCBITaxon:103407, not equivalence with another host-associated clone. The database's SPECIES rank does not establish nomenclatural validity, a type strain or a cultured isolate.

## Evidence

- The September 13 NCBI snapshot attestation exactly preserves the identifier, label, count of one and NAME unit.
- Exact Nuccore query `txid103407[Organism:noexp]` returned one record, AF180310.1. Its full metadata, references and source/rRNA feature qualifiers identify a 422-base partial 16S marker, clone apg115, with taxon:103407. This supports the clone-specific sequence association, not a genome or deposit relationship. [GenBank AF180310.1](https://www.ncbi.nlm.nih.gov/nuccore/AF180310.1).
- That accession lists an unpublished Campbell and Cary research reference and a direct submission dated August 24, 1999. Its reference metadata supplies no DOI or PMID. No article identity, experimental phenotype or mechanism was transferred from a similarly named study or neighboring clone.
- Exact NCBI Assembly query returned zero items and the service's no-items/phrase-not-found diagnostic. This result is bounded to that exact taxonomy query, not proof of universal resource absence.
- `data/taxa/PATHS.tsv:13882` matches the slug. `curation/seed_scope.tsv:144115` records September 13 admission with the one-source rationale. The inline event matches the scope text and source list; it does not claim human review.

## Completeness

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. No child taxon supplies descendant BacDive strains. Zero inventoried strains agrees with this source scope; it is not a claim that the organism cannot be cultured.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug/APG115 search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native name and scope. A second exact-accession search for AF180310 returned zero matches in those roots. Separate ignored-inclusive searches found no previous target report or external target history.

No supported culture-deposit join, genome association, additional taxonomy mapping or missing required overlay was established. Optional marker/literature enrichment is a later curation opportunity, not a required correction to an identity-only seed. Optional evidence and causal fields may remain empty. iModulonDB is not applicable because the record asserts no functional-gene or expression-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source-count semantics and seeded provenance agree with the inspected evidence.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Any future backbone correction belongs to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and its generator; scope changes belong in `curation/seed_scope.tsv`. Optional evidence enrichment requires a maintained input and separately authorized curation, not a hand edit of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the complete target/source comparison after authorized source changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Verify an explicit APG115/AF180310 publication link before assigning a DOI, phenotype or causal claim.
- Keep the partial 16S marker outside genome counts and culture-deposit assertions. Recheck authority sources when refreshing snapshots.

## Additional Notes

The taxonomy-browser page was unavailable through the web tool; both official structured taxonomy responses succeeded and were fully inspected. Raw sequence bases were not reanalyzed. Web searches were leads only and did not establish a target-specific publication; search misses were not treated as proof that none exists.

No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written.

