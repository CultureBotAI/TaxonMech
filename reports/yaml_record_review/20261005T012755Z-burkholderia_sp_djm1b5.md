# YAML Record Review: Burkholderia sp. DJM1B5

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/burkholderia_sp_djm1b5.yaml`
- Started UTC: 2026-10-05T01:26:12Z
- Finished UTC: 2026-10-05T01:27:55Z
- Verdict: pass

## Target

Read the entire 54-line generated TaxonRecord for NCBITaxon:1034168, Burkholderia sp. DJM1B5. This bacterial SPECIES-rank placeholder has parent NCBITaxon:2613784, EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. The reviewed identity is this specific NCBI entity, not another study isolate or an inferred named Burkholderia species.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/burkholderia_sp_djm1b5.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/burkholderia_sp_djm1b5.yaml --out /private/tmp/djm1b5-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: complete target and ten-ancestor backbone comparison, seven mapped-source inventories, PATHS and scope rows, NCBI attestation and inline-event text. No target children occur in the pinned backbone.
- PASS: full exact-target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus` is full-corpus-only; diagnostic output limits are not record scoping.
- NOT APPLICABLE: `just validate-products`; no graph nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive searches found no external target history. The inline seed event was checked directly.
- No undocumented focused term/reference validator was substituted. Represented identifiers were checked against source evidence.

## Identity and Grounding

The full backbone row at `data/raw/ncbitaxon_taxa.tsv:221436` and complete native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30788` agree with the identifier and label. No source synonym is omitted.

All ten root-first ancestors match by identifier, label and rank: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Burkholderiaceae, Burkholderia and unclassified Burkholderia. Live EFetch confirms the name, species rank, bacterial placement, parent 2613784, code 11 and labeled ancestry; Datasets confirms ancestor identifiers including root. [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034168&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034168).

EXACT denotes the NCBI identity, not a species-cluster or deposit equivalence. The SPECIES-rank placeholder does not itself establish nomenclatural validity or type material. The source lineage is retained without inferring a different genus or species from related study organisms.

## Evidence

- The NCBI attestation matches the September 13 snapshot, identifier, label, count of one and NAME unit exactly.
- Exact Nuccore query `txid1034168[Organism:noexp]` returned JF753414.1 alone. Full metadata, references and source/rRNA qualifiers identify a 642-base partial 16S marker, strain DJM1B5, taxon:1034168, and a surface-sterilized Zea seed source. This supports a marker association, not a genome or collection-deposit relationship. [GenBank JF753414.1](https://www.ncbi.nlm.nih.gov/nuccore/JF753414.1).
- Its explicit citation to PMID:21673982 and DOI:10.1371/journal.pone.0020396 agrees with the previously fetched PubMed metadata and abstract reread this turn. Community-level findings and named-species results were not transferred to DJM1B5. [PubMed XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21673982&retmode=xml).
- The exact Assembly query returned zero items with the no-items/phrase-not-found diagnostic. This is a bounded result, not proof of absence under every other assignment.
- `data/taxa/PATHS.tsv:13898` matches the slug. `curation/seed_scope.tsv:321754` supplies the September 13 one-source admission rationale. The inline seed event matches this rationale and the attestation list and does not claim human review.

## Completeness

Full mapped-inventory scans found no exact target rows in BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits. No child taxon contributes descendant BacDive strains. Zero inventoried strains is consistent with the source-count definition, even though a research isolate is named in GenBank.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug/designation search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native name and scope. The boundary-aware accession/PMID/DOI follow-up search returned zero matches in those roots. Separate ignored-inclusive searches found no prior target report or external history.

No eligible whole-deposit/genome join, additional supported mapping or missing required overlay was established. Bare DJM1B5 is not a validated collection accession. Optional marker/literature enrichment remains possible; empty optional evidence and causal fields are appropriate for the represented identity-only seed. iModulonDB is not applicable because no functional-gene or expression-module assertion occurs.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source counts and seeded provenance agree with inspected evidence. No represented phenotype relies on unreviewed supplementary rows.

## Recommended Edits

None required. Preserve the generated YAML and SEEDED status.

Future backbone corrections belong to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv` and its generator; scope changes belong in `curation/seed_scope.tsv`. Optional evidence enrichment requires an appropriate maintained input and separate curation authorization, not a hand edit of `data/taxa/`.

## Follow-up Checks

- Rerun both focused validators and the complete target/source comparison after authorized input changes.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Inspect exact DJM1B5 supplementary rows, headers, units and negative results before phenotype enrichment. Shared genus, paper or host is insufficient to transfer another isolate's results.
- Keep JF753414.1 outside genome counts. Require explicit eligible whole-deposit evidence for future strain/genome joins, and do not infer a named-species assignment from the marker alone.

## Additional Notes

The taxonomy-browser page was unavailable through the web tool; both official structured responses succeeded and were fully inspected. This accession's citation was independently checked against PubMed material already fetched and reread this turn; no fresh publisher full-text review is claimed.

Supplementary workbooks remain uninspected because previous web download attempts failed and the prescribed spreadsheet dependency loader remains unavailable. This limits optional phenotype enrichment, not any represented claim. Raw marker bases were not reanalyzed. No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this new timestamped report was written.

