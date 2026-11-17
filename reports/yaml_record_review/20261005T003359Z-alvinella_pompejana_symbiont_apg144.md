# YAML Record Review: Alvinella pompejana symbiont apg144

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg144.yaml`
- Started UTC: 2026-10-05T00:32:37Z
- Finished UTC: 2026-10-05T00:33:59Z
- Verdict: pass

## Target

Read the complete 42-line generated TaxonRecord for NCBITaxon:103405, Alvinella pompejana symbiont apg144. It is SPECIES rank in BACTERIA, parent NCBITaxon:122728, genetic code 11, EXACT grounding, SEEDED status, zero inventoried strains and one NCBI NAME attestation. The target is this bacterial clone-associated taxon, not the eukaryotic host or another host-associated clone.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg144.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg144.yaml --out /private/tmp/apg144-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: structured comparison of the complete backbone row, all six ancestors, seven mapped-source inventories, PATHS entry, seed-scope row, NCBI attestation and inline-event text. The pinned backbone has no children for this taxon.
- PASS: exact target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus` is full-corpus only. Its diagnostic limit does not make it a focused check, and no substitute reproduction claim is made.
- NOT APPLICABLE: `just validate-products`; the record has no causal nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive identifier/name/slug searches found no external target history. The inline event was checked directly.
- No undocumented focused term/reference validator was invented; relevant source identifiers were verified directly.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:18462` and complete native scientific-name object at `data/catalog/ncbi_names-0000.jsonl.gz:38471` agree on APG144. Neither source supplies synonyms.

The root-first ancestor chain matches by identifier, label and rank: root, cellular organisms, Bacteria, Pseudomonadati, Campylobacterota and unclassified Campylobacterota. Live NCBI Taxonomy EFetch and Datasets responses independently confirm the name, rank, bacterial placement, parent 122728, code 11 and ancestor identifiers. The absence of class/order/family/genus entries follows the unclassified source branch. [Official taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103405&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103405).

EXACT is correspondence with NCBITaxon:103405. SPECIES is the source rank, not a claim of nomenclatural validity, a type strain or a cultured isolate. Shared host association does not establish identity with other APG designations.

## Evidence

- The sole NCBI attestation preserves the identifier, label, one-NAME count and September 13 snapshot note exactly.
- Exact Nuccore query `txid103405[Organism:noexp]` returned one record, AF180307.1. Full metadata, references and source/rRNA qualifiers were inspected. It is a 458-base partial 16S sequence with explicit clone apg144 and taxon:103405, not a genome assembly or deposit identifier. [GenBank AF180307.1](https://www.ncbi.nlm.nih.gov/nuccore/AF180307.1).
- The accession lists Campbell and Cary, an unpublished research reference and an August 24, 1999 direct submission. It supplies no verified DOI or PMID for the research title. A target-specific publication was not established from the checked leads; shared authors, host names or similar clone names cannot transfer experimental claims.
- Exact NCBI Assembly query returned zero items with the service's no-items/phrase-not-found diagnostic. This is a bounded exact-taxonomy result, not proof that no related genome can exist under other classifications.
- `data/taxa/PATHS.tsv:13879` agrees with this slug. `curation/seed_scope.tsv:144113` records September 13 admission and the one-source rationale. The inline event matches the source list and scope text without implying prior human review.

## Completeness

Full scans found no exact target rows in the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits mapped inventories. No descendant BacDive strains can be gathered because there are no children in the backbone. Zero inventoried strains is consistent with these sources, not evidence of biological absence or inability to cultivate the organism.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug/APG144 search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching row contexts were inspected: backbone, native name and seed scope. A second exact-accession search for AF180307 returned no matches in those same roots.

No eligible culture-deposit, supported genome join, taxonomy mapping or missing required overlay was established. The external marker may be useful for optional later enrichment, but it does not justify a fabricated BacDive strain, type deposit, LPSN nomenclature entry or genome association. Optional evidence and causal fields may remain empty in this source-backed identity seed. iModulonDB is not applicable because the record asserts no functional-gene or expression-module relationship.

Ignored-inclusive searches found no prior target report or external history. Web-search misses are not treated as proof of publication absence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The identity, lineage, source-count semantics and seed provenance are supported within the checked scope.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future backbone corrections belong to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and its generator; scope changes belong in `curation/seed_scope.tsv`. Optional sequence/literature enrichment requires a maintained source input and separately authorized curation, not a direct edit of `data/taxa/`.

## Follow-up Checks

- After authorized source changes, rerun the focused schema and strict commands and the complete target/source comparison.
- Run `just verify-corpus` separately before asserting corpus-wide reproduction.
- Preserve AF180307/APG144 identity and verify an explicit publication link before adding a DOI, measured trait or causal claim.
- Keep the partial 16S sequence outside genome counts and culture-deposit evidence. Recheck authority sources when refreshing snapshots.

## Additional Notes

The taxonomy-browser page was unavailable through the web tool. Both official structured taxonomy endpoints succeeded and were fully inspected; broad tree search results did not substitute for target-specific evidence. Raw sequence bases were not reanalyzed, and no article was treated as a verified APG144 study. No source refresh, paid research, regeneration, history append, status promotion or GitHub mutation occurred. Only this timestamped report was written.

