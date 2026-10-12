# YAML Record Review: Alvinella pompejana symbiont apg162

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/alvinella_pompejana_symbiont_apg162.yaml`
- Started UTC: 2026-10-05T00:23:32Z
- Finished UTC: 2026-10-05T00:24:47Z
- Verdict: pass

## Target

Read the entire 42-line generated TaxonRecord for NCBITaxon:103401, Alvinella pompejana symbiont apg162. It is a bacterial SPECIES-rank source taxon with parent NCBITaxon:122706, EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains, one NCBI NAME attestation and one inline seed event. It is not the eukaryotic host or the separately classified APG10 clone.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/alvinella_pompejana_symbiont_apg162.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/alvinella_pompejana_symbiont_apg162.yaml --out /private/tmp/apg162-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: structured comparison of backbone identity, every ancestor, seven mapped-source inventories, PATHS entry, seed scope, NCBI attestation and inline-event text. The pinned backbone has no children for this taxon.
- PASS: exact target checks of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus`, which is a full-corpus check with no record-focused mode. No focused substitute is claimed.
- NOT APPLICABLE: `just validate-products`; this record has no causal nodes.
- SKIPPED: `just validate-history`; ignored-inclusive target identifier/name/slug searches found no external target history. The inline event was checked directly.
- No separate documented focused term/reference validator was invented. Source identifiers were checked at the authority and against retained source objects.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:18458` and native scientific-name object at `data/catalog/ncbi_names-0000.jsonl.gz:38467` agree on the target. No synonym is supplied by either source.

All six root-first ancestors match the pinned backbone. Live NCBI Taxonomy EFetch, Datasets and the inspected taxonomy page confirm the bacterial species rank, parent, translation code and lineage. In particular, NCBI retains the delta/epsilon subdivisions CLADE followed by Deltaproteobacteria and unclassified Deltaproteobacteria. The record correctly preserves that chain rather than inventing a kingdom, phylum, order or family from a neighboring taxon. [NCBI taxonomy](https://ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?command=show&id=103401&lvl=3&mode=node).

SPECIES describes the NCBI rank, not evidence of valid nomenclatural publication. EXACT denotes identity with NCBITaxon:103401; it does not equate this clone with all host-associated bacteria or with the host itself.

## Evidence

- The September 13 NCBI snapshot supplies the sole NAME assertion. Its identifier, label, count, unit and snapshot note match the YAML exactly.
- An exact NCBI Nuccore query, `txid103401[Organism:noexp]`, returned one record, AF180306.1. Full metadata, references and feature qualifiers were inspected. It is a 427-base partial 16S rRNA sequence with clone apg162 and explicit taxon:103401, not a genome assembly or culture-collection deposit. [GenBank AF180306.1](https://www.ncbi.nlm.nih.gov/nuccore/AF180306.1).
- The sequence record lists Campbell and Cary, an unpublished research-reference title, and a direct submission dated August 24, 1999. It does not supply a verified DOI or PMID for that research title. No publication identity or mechanism was inferred from the shared authors or from papers about other clones.
- An exact NCBI Assembly query returned zero records with the service's no-items/phrase-not-found diagnostic. This is a bounded source-query result, not a claim that no relevant genome can exist elsewhere or under another classification.
- `data/taxa/PATHS.tsv:13874` resolves the identifier to this slug. `curation/seed_scope.tsv:144109` records September 13 admission and the one-source rationale. The seed event matches the source list and scope reason and does not assert that a human review occurred.

## Completeness

Full mapped-inventory scans found no target BacDive strains, LPSN names, GTDB mappings, GOLD organisms, MediaDive, Madin or BactoTraits rows. With no children in the backbone, no descendant strains need to be gathered. Zero inventoried strains is consistent with these sources and is not a claim about biological absence or culturability.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. Identifier, full name, slug-equivalent spelling and APG162 yielded three matching contexts: the backbone, native name and scope row. All were inspected. A second exact-accession search for AF180306 returned zero matches in those same roots.

No supported culture-deposit, genome-join, taxonomic mapping or missing required overlay was established. The marker accession is a possible future enrichment lead, but it cannot justify fabricating a strain entry, a nomenclature record or a genome link. Optional evidence, trait and causal-graph slots may remain empty. iModulonDB is not applicable because no functional-gene or expression-module claim is represented.

Ignored-inclusive searches also found no previous review for this record and no external target history. Web searches were used only as leads; their failure to retrieve an exact-accession publication is not evidence that no publication exists.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The source-backed identity, lineage, provenance and empty optional fields are internally consistent within the checked scope.

## Recommended Edits

None required. Do not hand-edit this generated record or promote its mapping status as a result of the review.

A later source classification correction belongs in the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and its generator, with scope changes in `curation/seed_scope.tsv`. Optional marker or literature enrichment requires an explicitly maintained input path and separately authorized curation, not direct YAML editing.

## Follow-up Checks

- Rerun the focused schema and strict commands plus the identity/source comparison after authorized changes.
- Run documented `just verify-corpus` separately before claiming corpus-wide reproduction.
- Recheck the NCBI source lineage when refreshing the taxonomy snapshot; do not resolve its legacy clade by importing a newer classification from a different organism.
- Verify an explicit clone/accession-to-publication link before assigning a DOI, phenotype or mechanism to APG162. Retain AF180306 as partial marker evidence, not a genome or deposit.

## Additional Notes

The initial default taxonomy-page route failed through the web tool; the alternative NCBI page and both official structured endpoints succeeded. The entire nucleotide string was not analyzed. No article was treated as a verified APG162 study, and the record asserts no such citation. This single-record review did not change YAML, source inputs, history, status, generated pages or GitHub state. Only this timestamped report was written.

