# YAML Record Review: Alvinella pompejana symbiont apg68

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg68.yaml`
- Started UTC: 2026-10-05T00:30:35Z
- Finished UTC: 2026-10-05T00:31:57Z
- Verdict: pass

## Target

Read the complete 42-line generated TaxonRecord for NCBITaxon:103404, Alvinella pompejana symbiont apg68. It is a bacterial SPECIES-rank source entity, parent NCBITaxon:122728, genetic code 11, EXACT grounding, SEEDED status, zero inventoried strains and one NCBI NAME attestation. The target is APG68, not the eukaryotic host or any similarly named APG clone.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg68.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg68.yaml --out /private/tmp/apg68-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: structured comparison of the complete backbone row, six ancestors, seven mapped-source inventories, PATHS and scope entries, sole attestation and inline-event text. No children occur under this taxon in the pinned backbone.
- PASS: exact target scans of type-material, merged-ID and dropped inventories returned no matches.
- SKIPPED: `just verify-corpus` is full-corpus only; no focused equivalent was invented and the diagnostic cap was not mistaken for a scope selector.
- NOT APPLICABLE: `just validate-products`; no causal nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive identifier/name/slug searches found no external target history. The inline event was checked directly.
- No additional undocumented single-record term/reference validator was substituted; identifiers were checked at their source.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18461` and the complete native name object at `data/catalog/ncbi_names-0000.jsonl.gz:38470` agree on the exact scientific name and identifier. Neither supplies additional synonyms.

The six root-first ancestors match by identifier, label and rank: root, cellular organisms, Bacteria, Pseudomonadati, Campylobacterota and unclassified Campylobacterota. Live NCBI EFetch and Datasets responses confirm the name, rank, parent 122728, genetic code and lineage. The inspected NCBI taxonomy page independently agrees. [NCBI taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103404&lvl=0).

Unrepresented class, order, family and genus ranks reflect the source's unclassified branch. SPECIES is the database rank, not evidence of nomenclatural validity or a type culture. EXACT grounds this record to NCBITaxon:103404 without equating it with other host-associated clones.

## Evidence

- The NCBI source attestation preserves the target name, identifier, count of one, NAME unit and September 13 snapshot note exactly.
- Exact Nuccore query `txid103404[Organism:noexp]` returned one record. Full GenBank metadata, references and source/rRNA qualifiers resolve AF180305.1 to a 442-base partial 16S sequence with clone apg68 and taxon:103404. This is a clone-specific marker association, not a genome assembly or a culture deposit. [GenBank AF180305.1](https://www.ncbi.nlm.nih.gov/nuccore/AF180305.1).
- The accession retains Campbell and Cary's unpublished research reference and a direct submission dated August 24, 1999. It supplies no verified DOI or PMID for that research title. No publication identity, community prevalence or metabolic mechanism was inferred from the authors, host name or another clone's evidence.
- Exact NCBI Assembly query returned zero items with the service's no-items/phrase-not-found diagnostic. This is a bounded query result, not proof that no related resources exist under another classification.
- `data/taxa/PATHS.tsv:13878` matches this slug; `curation/seed_scope.tsv:144112` records September 13 admission and the one-source rationale. The inline seed event matches these inputs and retains SEEDED status rather than claiming a prior review.

## Completeness

The seven mapped-source inventories have no exact target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits rows. The backbone has no descendants from which additional BacDive strains could be gathered. Zero inventoried strains and an empty list are consistent with this coverage, not claims that the organism is absent or unculturable.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug/APG68 search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native name and scope. A second search for AF180305 returned zero matches in those roots.

No eligible culture-deposit, supported strain/genome association, taxonomy mapping or missing required overlay was established. The external marker is an optional enrichment lead, not grounds to fabricate a BacDive strain, type deposit, LPSN nomenclature entry or genome link. Optional evidence and causal fields may remain empty. iModulonDB is not applicable because the record makes no functional-gene or expression-module claim.

Ignored-inclusive searches found no previous target report or external history. Web-search misses for the accession are not evidence that no publication exists.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The identity, full lineage, source counts and seed provenance are supported within the checked scope.

## Recommended Edits

None required. Preserve the generated record and its SEEDED status.

Future source classification corrections belong to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and the generator; scope changes belong in `curation/seed_scope.tsv`. Optional marker or literature enrichment requires a maintained input and separately authorized curation, not direct editing of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the source comparison after authorized changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Preserve AF180305/APG68 scope and verify an explicit accession-to-publication link before assigning a DOI or experimental claim.
- Keep the partial 16S marker outside genome counts and culture-deposit assertions; recheck the NCBI source chain when refreshing snapshots.

## Additional Notes

The initial taxonomy-browser URL failed through the web tool; the alternative URL with `lvl=0` and both official structured endpoints succeeded. Those successful sources were inspected directly; search snippets did not substitute for them. Raw sequence bases were not reanalyzed. No source refresh, paid research, regeneration, history append, status promotion or GitHub mutation occurred. Only this timestamped report was written.

