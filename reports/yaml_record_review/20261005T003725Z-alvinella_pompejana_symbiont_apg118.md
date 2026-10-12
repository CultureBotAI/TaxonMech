# YAML Record Review: Alvinella pompejana symbiont apg118

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg118.yaml`
- Started UTC: 2026-10-05T00:36:02Z
- Finished UTC: 2026-10-05T00:37:25Z
- Verdict: pass

## Target

Read the entire 42-line generated TaxonRecord for NCBITaxon:103406, Alvinella pompejana symbiont apg118. It denotes a bacterial SPECIES-rank source taxon with parent NCBITaxon:122728, genetic code 11, EXACT grounding, SEEDED status, zero inventoried strains and one NCBI NAME attestation. It is not the eukaryotic host, another APG clone or the entire symbiont community.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg118.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg118.yaml --out /private/tmp/apg118-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: structured comparison of the complete backbone row, all six ancestors, seven mapped-source inventories, PATHS entry, seed-scope row, NCBI attestation and inline-event text. No children occur in the pinned backbone.
- PASS: exact target scans of type-material, merged-ID and dropped inventories found no rows.
- SKIPPED: `just verify-corpus`, a full-corpus check with no focused target mode. A diagnostic cap is not a scope filter.
- NOT APPLICABLE: `just validate-products`; no causal nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive target identifier/name/slug searches found no external target history. The inline event was checked directly.
- No undocumented focused term/reference validator was substituted; represented identifiers were checked against their source evidence.

## Identity and Grounding

The backbone row at `data/raw/ncbitaxon_taxa.tsv:18463` and complete native scientific-name object at `data/catalog/ncbi_names-0000.jsonl.gz:38472` agree on APG118 and supply no synonym.

All six root-first ancestor entries agree by identifier, label and rank: root, cellular organisms, Bacteria, Pseudomonadati, Campylobacterota and unclassified Campylobacterota. Live NCBI EFetch and Datasets responses independently confirm the name, species rank, bacterial placement, parent 122728, code 11 and ancestor identifiers. Missing class/order/family/genus entries preserve the source's unclassified branch. [Official taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103406&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103406).

EXACT denotes identity with NCBITaxon:103406. The database's SPECIES rank is not proof of valid nomenclatural publication, a type strain or a cultured isolate. Shared host association does not establish equivalence with other clones.

## Evidence

- The September 13 NCBI attestation exactly preserves the identifier, label, count of one and NAME unit.
- Exact Nuccore query `txid103406[Organism:noexp]` returned one record, AF180308.1. Full metadata, references and source/rRNA feature qualifiers identify a 417-base partial 16S sequence, clone apg118, with taxon:103406. This supports a clone-specific marker association, not a genome or culture-deposit link. [GenBank AF180308.1](https://www.ncbi.nlm.nih.gov/nuccore/AF180308.1).
- The accession lists Campbell and Cary, an unpublished research reference and a direct submission dated August 24, 1999. It supplies no verified DOI or PMID for that research title. No experimental claim or publication identity was imported from another clone's study merely because authors or the host match.
- Exact NCBI Assembly query returned zero items with the service's no-items/phrase-not-found diagnostic. This is bounded to the exact taxonomy query, not proof that no related resource could exist under another assignment.
- `data/taxa/PATHS.tsv:13880` matches the slug, and `curation/seed_scope.tsv:144114` records September 13 admission under the one-source rationale. The inline seed event matches both the source list and scope text; it does not assert human review.

## Completeness

Full scans found no exact target rows in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits mapped inventories. No children exist to contribute descendant BacDive strains. Zero inventoried strains therefore agrees with the checked source scope and is not a statement of biological absence or inability to culture the organism.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug/APG118 search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native name and scope. A second exact-accession search for AF180308 returned zero matches in those same roots.

No eligible culture-deposit, supported strain/genome join, taxonomy mapping or missing required overlay was established. Optional marker/literature enrichment is a possible later curation task, not grounds for inventing a BacDive strain, nomenclature record or genome association. Optional evidence and causal fields may remain empty. iModulonDB is not applicable because the record asserts no functional-gene or expression-module claim.

Ignored-inclusive searches found no previous target report or external history. Exact-accession web-search misses were not treated as proof that no publication exists.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The record's identity, lineage, count semantics and seeded provenance agree with the inspected evidence.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future backbone corrections belong to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and its generator; scope changes belong in `curation/seed_scope.tsv`. Optional evidence enrichment requires a maintained input and separately authorized curation, not a hand edit of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the complete target/source comparison after authorized source changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Preserve AF180308/APG118 scope and verify an explicit publication link before assigning a DOI, phenotype or causal claim.
- Keep this partial 16S accession outside genome counts and culture-deposit assertions. Recheck authority sources when refreshing snapshots.

## Additional Notes

The NCBI taxonomy-browser page was unavailable through the web tool; both official structured taxonomy responses succeeded and were fully inspected. Raw sequence bases were not reanalyzed, and no article was treated as a verified APG118 study. No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written.

