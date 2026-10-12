# YAML Record Review: Alvinella pompejana symbiont apg79

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg79.yaml`
- Started UTC: 2026-10-05T00:25:29Z
- Finished UTC: 2026-10-05T00:26:47Z
- Verdict: pass

## Target

Read the entire 42-line generated TaxonRecord for NCBITaxon:103402, Alvinella pompejana symbiont apg79: SPECIES, BACTERIA, parent NCBITaxon:122728, EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and a single NCBI NAME attestation. The target is the APG79 bacterial taxon, not its eukaryotic host, a community-wide taxon, or another APG clone.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg79.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg79.yaml --out /private/tmp/apg79-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: structured comparison of the full backbone row, six ancestors, seven mapped-source inventories, PATHS and scope entries, NCBI attestation and inline seed event. No descendant taxa occur in the pinned backbone.
- PASS: exact target type-material, merged-ID and dropped-row scans returned no matches.
- SKIPPED: `just verify-corpus` is full-corpus only; this report does not substitute a fabricated focused validator or treat a diagnostic limit as a scope filter.
- NOT APPLICABLE: `just validate-products`; no graph nodes or product labels are represented.
- SKIPPED: `just validate-history`; ignored-inclusive identifier/name/slug searches found no external target history. The inline event was checked directly.
- Source and authority checks below cover represented identifiers; no separate undocumented term/reference validator was claimed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18459` and the complete native scientific-name object at `data/catalog/ncbi_names-0000.jsonl.gz:38468` identify this exact entity without synonyms. The entire lineage matches the pinned backbone: root, cellular organisms, Bacteria, Pseudomonadati, Campylobacterota, unclassified Campylobacterota.

Live NCBI Taxonomy EFetch and Datasets responses independently confirm the label, species rank, bacterial placement, parent 122728, genetic code 11 and complete ancestor identifiers. No class, order, family or genus should be invented for the unclassified branch. [Official NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103402&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103402).

SPECIES is the database rank, not evidence of a validly published binomial or culture deposit. EXACT is grounded identity with NCBITaxon:103402, not equivalence with neighboring APG clones or all bacteria occurring on the same host.

## Evidence

- The sole September 13 NCBI NAME attestation matches the source identifier, label, count, unit and snapshot note exactly.
- Exact Nuccore search `txid103402[Organism:noexp]` returned one record, AF180303.1. Its full metadata, references and source/rRNA feature qualifiers were inspected. It is a 427-base partial 16S record explicitly bearing clone apg79 and taxon:103402. That establishes a clone-specific sequence association, not a genome assembly or culture-deposit match. [GenBank AF180303.1](https://www.ncbi.nlm.nih.gov/nuccore/AF180303.1).
- The accession lists Campbell and Cary, an unpublished research reference and an August 24, 1999 direct submission. It does not supply a verified DOI or PMID for that research title. No paper identity, metabolism, symbiotic function or measured phenotype was inferred from shared authors, a shared host or another clone's study.
- Exact NCBI Assembly search returned zero items with a no-items/phrase-not-found diagnostic. This is a result for the exact taxonomy query, not proof that no related sequence resource exists elsewhere.
- `data/taxa/PATHS.tsv:13876` and `curation/seed_scope.tsv:144110` agree on the slug, September 13 admission and one-source rationale. The September 13 inline event matches the source inventory and scope text; SEEDED is retained rather than misrepresenting this review as human sign-off.

## Completeness

Full scans of the seven mapped-source inventories found no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits rows. Since there are no descendants, no descendant BacDive strain is omitted. Zero inventoried strains is a source-coverage statement, not a claim of biological absence or inability to cultivate the organism.

An ignored-inclusive, hidden-file-inclusive and compressed-file-aware search for the identifier, complete name, slug-equivalent spelling and APG79 covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native scientific name and scope row. A second search for AF180303 found no matches in those same roots.

No eligible culture-deposit, supported genome crosswalk, taxonomic mapping or required overlay was established. The external marker is an optional enrichment lead, not a reason to fabricate a strain, nomenclature entry or assembly link. Empty optional evidence and causal fields are acceptable for this source-backed identity seed. iModulonDB is not applicable because the record makes no functional-gene or expression-module assertion.

Ignored-inclusive report and history searches found no previous target review or external history. Exact-name/accession web searches supplied no verified target-specific publication; that is not evidence that no publication exists.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The identity, lineage, count units and seed provenance agree with the checked sources.

## Recommended Edits

None required. Do not hand-edit the generated YAML, promote status or append history for this read-only review.

A future backbone correction belongs to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and the seeding implementation; scope changes belong in `curation/seed_scope.tsv`. Optional marker or literature enrichment requires a maintained evidence input and separately authorized curation rather than direct modification of `data/taxa/`.

## Follow-up Checks

- Rerun the focused schema and strict commands and source comparison after authorized source changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproduction.
- Preserve the exact AF180303/APG79 association. Do not transfer experimental claims from APG10, APG162 or other host-associated taxa.
- Verify an explicit accession-to-publication link before adding a DOI or phenotype. Keep the partial 16S sequence out of genome counts.
- Revisit the taxonomy browser page when available; the official structured NCBI responses, not inaccessible page content, support this review.

## Additional Notes

Two taxonomy-browser URL variants failed through the web tool. Both official structured taxonomy endpoints succeeded and were fully inspected. Broad tree search results were not used to replace the target-specific responses. Sequence bases were not reanalyzed, and no paper was treated as a verified APG79 study.

This is a single-record identity/evidence review, not a biological characterization or full-corpus certification. No source refresh, paid research, regeneration, history append, status promotion or GitHub mutation occurred. Only this timestamped Markdown report was written.

