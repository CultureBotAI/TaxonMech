# YAML Record Review: Alvinella pompejana symbiont apg73

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg73.yaml`
- Started UTC: 2026-10-05T00:28:34Z
- Finished UTC: 2026-10-05T00:29:52Z
- Verdict: pass

## Target

Read the complete 42-line generated TaxonRecord for NCBITaxon:103403, Alvinella pompejana symbiont apg73. It is a bacterial SPECIES-rank entity with parent NCBITaxon:122728, EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. The review concerns APG73, not its eukaryotic host, another APG clone or the entire host-associated community.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg73.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg73.yaml --out /private/tmp/apg73-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: structured comparison of the backbone, all six ancestors, seven mapped-source inventories, PATHS entry, scope row, source attestation and inline seed-event text. The pinned backbone has no children for this taxon.
- PASS: full scans of the type-material, merged-ID and dropped inventories found no exact target rows.
- SKIPPED: `just verify-corpus`, a full-corpus reproduction check without a focused target mode. A diagnostic limit is not a scope selector.
- NOT APPLICABLE: `just validate-products`; no causal nodes or product labels are present.
- SKIPPED: `just validate-history`; ignored-inclusive target identifier/name/slug searches found no external history record. The inline event was checked directly.
- No undocumented focused term/reference validator was substituted. Represented identifiers were checked against their source evidence.

## Identity and Grounding

The backbone at `data/raw/ncbitaxon_taxa.tsv:18460` and complete native name object at `data/catalog/ncbi_names-0000.jsonl.gz:38469` agree on APG73 and supply no synonym. Every root-first ancestor identifier, label and rank matches: root, cellular organisms, Bacteria, Pseudomonadati, Campylobacterota and unclassified Campylobacterota.

Live NCBI Taxonomy EFetch and Datasets responses independently confirm the scientific name, species rank, bacterial placement, parent 122728, genetic code 11 and ancestor identifiers. Missing class/order/family/genus ranks are source structure, not a reason to invent a more specific placement. [Official taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103403&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103403).

EXACT denotes correspondence with this NCBI entity. The source's SPECIES rank does not establish a validly published binomial, a type strain or a culture deposit.

## Evidence

- The NCBI attestation exactly preserves the target identifier, label, one-NAME count and September 13 snapshot note.
- Exact Nuccore search `txid103403[Organism:noexp]` returned one sequence, AF180304.1. Its complete metadata, references and feature qualifiers identify a 435-base partial 16S record with clone apg73 and taxon:103403. It is marker evidence, not a genome assembly or a culture-collection association. [GenBank AF180304.1](https://www.ncbi.nlm.nih.gov/nuccore/AF180304.1).
- The accession retains a Campbell/Cary unpublished research reference and an August 24, 1999 direct submission. No DOI or PMID was supplied there. A verified publication corresponding to that research title was not established; no paper about another clone or the broader community was treated as proof of APG73's properties.
- Exact NCBI Assembly search returned zero items with the service's no-items/phrase-not-found diagnostic. This is limited to that query and does not prove absence of resources under other taxonomic assignments.
- `data/taxa/PATHS.tsv:13877` matches the slug. `curation/seed_scope.tsv:144111` records September 13 admission under the one-source rule. The inline seed event matches the inventory and scope rationale and does not claim a previous review.

## Completeness

Full mapped-inventory scans found no APG73 rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. No descendants can contribute additional BacDive strains. The empty strain list and zero count agree with this inventory scope; neither implies biological absence or inability to culture the organism.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug/APG73 search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: target backbone, native name and scope. A second exact-accession search for AF180304 returned zero matches in those roots.

No eligible culture-deposit, supported strain/genome join, taxonomy mapping or missing required overlay was established. Optional literature/marker enrichment could add context later, but it cannot supply a fabricated BacDive strain, type deposit, nomenclatural entry or genome link. Optional evidence and causal-graph slots may remain empty for this identity seed. iModulonDB is not applicable: the record asserts no functional-gene or expression-module claim.

Ignored-inclusive searches found no prior target review or external target history. Exact-accession web-search misses are not treated as proof that no publication exists.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source-count semantics and seeded provenance agree with the evidence inspected.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Any future backbone correction belongs to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and its generator; scope changes belong in `curation/seed_scope.tsv`. Optional evidence enrichment needs a maintained input and separately authorized curation, not a hand edit to `data/taxa/`.

## Follow-up Checks

- After authorized source changes, rerun both focused validators and the complete target/source comparison.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Preserve the clone-specific AF180304/APG73 identity when adding evidence, and verify an explicit publication link before adding a DOI or experimental claim.
- Keep the partial 16S marker separate from genome counts and culture-deposit evidence. Recheck source versions when refreshing the taxonomy.

## Additional Notes

The NCBI taxonomy-browser page was inaccessible through the web tool; both official structured taxonomy responses succeeded and were fully inspected. Sequence bases were not reanalyzed. The review does not establish metabolic function, host benefit or community-wide prevalence. No source refresh, paid research, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written.

